# Altinity ClickHouse

Monitor ClickHouse clusters managed by the Altinity Kubernetes operator - queries, inserts and merges, replication, tables, and Keeper.

Your ClickHouse installations show up alongside the rest of your telemetry, on dashboards that are already built. You can see how each cluster is doing - query, insert, and merge rates, replication, memory and disk, every table's size and parts, and ClickHouse Keeper - and get alerted when a host stops reporting, replicas go read-only or fall behind, inserts are delayed or refused, a mutation never finishes, or Keeper loses its leader.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - the Altinity operator's metrics exporter already measures every ClickHouse host it runs, and **Grafana Alloy**, running in the same Kubernetes cluster, collects from that exporter and from ClickHouse Keeper and sends the metrics to OpsPilot. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Altinity ClickHouse**.

---

## Permission tiers

Altinity ClickHouse runs **Read-only**, the default. It requires permission to install **Grafana Alloy** in the Kubernetes cluster, and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

For background, the [Altinity ClickHouse operator](https://github.com/Altinity/clickhouse-operator) documents how the exporter works, and the [Grafana Alloy Helm chart](https://github.com/grafana/helm-charts) covers running Alloy another way - the config below works as it is.

---

## 1. Turn on Keeper's metrics

The exporter covers ClickHouse, not **ClickHouse Keeper**, which serves its own metrics once told to. Skip this if your installations use ZooKeeper, or no coordination at all.

In each `ClickHouseKeeperInstallation`, add the settings and name the port in its pod template `metrics`:

```yaml
spec:
  configuration:
    settings:
      prometheus/endpoint: "/metrics"
      prometheus/port: "7000"
      prometheus/metrics: "true"
      prometheus/events: "true"
      prometheus/asynchronous_metrics: "true"
  templates:
    podTemplates:
      - name: <your keeper pod template>
        spec:
          containers:
            - name: clickhouse-keeper
              ports:
                - name: metrics
                  containerPort: 7000
```

The operator restarts the Keeper nodes one at a time to apply it.

---

## 2. Install Alloy

Create a secret with your OpsPilot API key - from **Data and Licenses > [API Keys](https://app.opspilot.com/organization/api-keys)** - in the namespace Alloy will run in:

```bash
kubectl create namespace monitoring
kubectl -n monitoring create secret generic opspilot --from-literal=api-key='<your API key>'
```

Save this as `clickhouse.alloy`:

```river
discovery.kubernetes "clickhouse" {
  role = "pod"
}

// The Altinity operator's metrics exporter: one target per operator, which
// queries every ClickHouse host the operator manages on each scrape.
discovery.relabel "clickhouse_exporter" {
  targets = discovery.kubernetes.clickhouse.targets

  rule {
    source_labels = ["__meta_kubernetes_pod_label_app", "__meta_kubernetes_pod_container_port_name"]
    regex         = "clickhouse-operator;ch-metrics"
    action        = "keep"
  }
  rule {
    source_labels = ["__meta_kubernetes_namespace"]
    target_label  = "operator_namespace"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_name"]
    target_label  = "instance"
  }
}

// ClickHouse Keeper's own Prometheus endpoint, on the container port named
// metrics.
discovery.relabel "clickhouse_keeper" {
  targets = discovery.kubernetes.clickhouse.targets

  rule {
    source_labels = ["__meta_kubernetes_pod_label_clickhouse_keeper_altinity_com_chk", "__meta_kubernetes_pod_container_port_name"]
    regex         = ".+;metrics"
    action        = "keep"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_label_clickhouse_keeper_altinity_com_chk"]
    target_label  = "chk"
  }
  rule {
    source_labels = ["__meta_kubernetes_namespace"]
    target_label  = "namespace"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_name"]
    target_label  = "instance"
  }
}

prometheus.scrape "clickhouse" {
  targets         = array.concat(discovery.relabel.clickhouse_exporter.output, discovery.relabel.clickhouse_keeper.output)
  job_name        = "integrations/altinity-clickhouse"
  scrape_interval = "30s"
  scrape_timeout  = "20s"
  forward_to      = [prometheus.relabel.clickhouse.receiver]
}

prometheus.relabel "clickhouse" {
  forward_to = [prometheus.remote_write.opspilot.receiver]

  rule {
    source_labels = ["__name__"]
    regex         = "up|chi_clickhouse_(table_.+|metric_(fetch_errors|Uptime|Query|LongestRunningQuery|MaxPartCountForPartition|PartsActive|Merge|BackgroundMergesAndMutationsPoolTask|ReadonlyReplica|ReplicasMaxAbsoluteDelay|ReplicasSumQueueSize|ZooKeeperSession|MemoryTracking|CGroupMemoryTotal|DiskFreeBytes|DiskTotalBytes|TCPConnection|HTTPConnection|DetachedParts)|event_(Query|SelectQuery|InsertQuery|FailedQuery|QueryTimeMicroseconds|InsertedRows|InsertedBytes|DelayedInserts|RejectedInserts|MergedRows|ZooKeeperHardwareExceptions))|ClickHouse(AsyncMetrics_Keeper.+|Metrics_Keeper(AliveConnections|OutstandingRequests)|ProfileEvents_Keeper(Commits|CommitsFailed))"
    action        = "keep"
  }
  rule {
    source_labels = ["hostname"]
    regex         = "([^.]+)\\..*"
    target_label  = "hostname"
  }
}

prometheus.remote_write "opspilot" {
  endpoint {
    url = "https://api.opspilot.com/v1/metrics"

    headers = {
      "authorization" = sys.env("OPSPILOT_API_KEY"),
    }
  }
}
```

and install Alloy with it:

```bash
helm install alloy alloy --repo https://grafana.github.io/helm-charts -n monitoring \
  --set-file alloy.configMap.content=clickhouse.alloy \
  --set 'alloy.extraEnv[0].name=OPSPILOT_API_KEY' \
  --set 'alloy.extraEnv[0].valueFrom.secretKeyRef.name=opspilot' \
  --set 'alloy.extraEnv[0].valueFrom.secretKeyRef.key=api-key'
```

A few things worth understanding:

- **One target covers every installation.** The exporter queries all the hosts the operator manages each time Alloy scrapes it, waiting up to nine seconds for slow ones - hence the 20-second timeout. Scrape it from **one Alloy only**: every scrape is a round of queries against every host.
- **The keep rule sends only what the dashboards read.** The exporter reports about a thousand series per host, and Keeper its whole metric set; the rule keeps about 35 per host plus five for each table holding data - ClickHouse's own system log tables, twenty or so, included.
- **`namespace` is the installation's.** The exporter labels each series with its `ClickHouseInstallation` (`chi`) and that installation's namespace, so the operator pod's own namespace goes in `operator_namespace`. Host names are shortened to the pod's name.

Already running Alloy in the cluster - the Kubernetes Monitoring chart, for instance? Add the blocks above to its config instead, with `forward_to` naming its existing `prometheus.remote_write`.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
chi_clickhouse_metric_Uptime{job="integrations/altinity-clickhouse"}
```

You should get one series per ClickHouse host. For Keeper, run `ClickHouseAsyncMetrics_KeeperIsLeader{job="integrations/altinity-clickhouse"}`.

Once data is flowing, the **Dashboard data** column on **Your installation** (for example *3 of 3 with data*) links straight to the provisioned dashboards.

---

## Troubleshooting

**Nothing comes back.** Open the Alloy UI (`kubectl -n monitoring port-forward ds/alloy 12345`) - it shows whether Alloy found the operator's `ch-metrics` port.

**A host is missing.** A host listed in `chi_clickhouse_metric_fetch_errors{fetch_type="system_metrics"} == 1` is one the exporter cannot query.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
