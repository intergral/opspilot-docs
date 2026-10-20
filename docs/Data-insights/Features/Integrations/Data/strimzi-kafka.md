# Strimzi Kafka

Monitor Kafka clusters managed by the Strimzi Kubernetes operator - brokers, the controller, topics, consumer lag, and the operators.

Your Strimzi-managed Kafka clusters show up alongside the rest of your telemetry, on dashboards that are already built. You can see how each cluster is doing - brokers, the controller quorum, replication and throughput, every topic and consumer group, and the operators reconciling them - with alerts when a broker drops out, partitions go offline or under-replicated, a consumer group falls behind, a change stops being applied, or a certificate is about to expire.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - Strimzi already serves the metrics these dashboards read (each Kafka node's JMX metrics, its Kafka Exporter's topic and consumer metrics, and the operators' own), and **Grafana Alloy**, running in the same Kubernetes cluster, finds those pods and sends their metrics to OpsPilot. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Strimzi Kafka**.

---

## Permission tiers

Strimzi Kafka runs **Read-only**, the default. It requires Strimzi's metrics turned on for each Kafka cluster, permission to install **Grafana Alloy** in the Kubernetes cluster, and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

For background, see [Strimzi's metrics guide](https://strimzi.io/docs/) for every option, and the [Grafana Alloy Helm chart](https://github.com/grafana/helm-charts) if you run Alloy in the cluster another way - the config below works as it is.

---

## 1. Turn on Strimzi's metrics

Strimzi publishes the JMX exporter rules its dashboards use as a ConfigMap in its examples. Create it in each namespace holding a Kafka cluster:

```bash
curl -fsSL https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/1.3.0/examples/metrics/kafka-metrics.yaml \
  | sed -n '/^kind: ConfigMap$/,$p' | kubectl -n <namespace> apply -f -
```

The example file also defines a Kafka cluster; the `sed` keeps only the ConfigMap at its end.

Then point each `Kafka` resource at it, and turn on the Kafka Exporter:

```yaml
spec:
  kafka:
    metricsConfig:
      type: jmxPrometheusExporter
      valueFrom:
        configMapKeyRef:
          name: kafka-metrics
          key: kafka-metrics-config.yml
  kafkaExporter:
    topicRegex: ".*"
    groupRegex: ".*"
```

Strimzi rolls the Kafka nodes one at a time to apply it. The cluster operator serves its metrics without any setting.

!!! note "Use these rules, not the Strimzi Metrics Reporter"
    Strimzi also offers `type: strimziMetricsReporter`, whose metric names differ; these dashboards read the JMX exporter's.

---

## 2. Install Alloy

Create a secret with your OpsPilot API key - from **Data and Licenses > [API Keys](https://app.opspilot.com/organization/api-keys)** - in the namespace Alloy will run in:

```bash
kubectl create namespace monitoring
kubectl -n monitoring create secret generic opspilot --from-literal=api-key='<your API key>'
```

Save this as `strimzi.alloy`:

```river
discovery.kubernetes "strimzi" {
  role = "pod"
}

discovery.relabel "strimzi_kafka" {
  targets = discovery.kubernetes.strimzi.targets

  rule {
    source_labels = ["__meta_kubernetes_pod_label_strimzi_io_kind", "__meta_kubernetes_pod_container_port_name"]
    regex         = "Kafka;tcp-prometheus"
    action        = "keep"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_label_strimzi_io_cluster"]
    target_label  = "strimzi_io_cluster"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_label_strimzi_io_component_type"]
    target_label  = "strimzi_io_component_type"
  }
  rule {
    source_labels = ["__meta_kubernetes_namespace"]
    target_label  = "namespace"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_name"]
    target_label  = "pod"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_name"]
    target_label  = "instance"
  }
}

discovery.relabel "strimzi_operators" {
  targets = discovery.kubernetes.strimzi.targets

  rule {
    source_labels = ["__meta_kubernetes_pod_label_strimzi_io_kind", "__meta_kubernetes_pod_label_app_kubernetes_io_name", "__meta_kubernetes_pod_container_port_name"]
    regex         = "cluster-operator;.*;http|.*;entity-operator;healthcheck(-to|-uo)?"
    action        = "keep"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_label_strimzi_io_cluster"]
    target_label  = "strimzi_io_cluster"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_container_name"]
    target_label  = "container"
  }
  rule {
    source_labels = ["__meta_kubernetes_namespace"]
    target_label  = "operator_namespace"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_name"]
    target_label  = "pod"
  }
  rule {
    source_labels = ["__meta_kubernetes_pod_name", "__meta_kubernetes_pod_container_name"]
    separator     = "/"
    target_label  = "instance"
  }
}

prometheus.scrape "strimzi" {
  targets         = array.concat(discovery.relabel.strimzi_kafka.output, discovery.relabel.strimzi_operators.output)
  job_name        = "integrations/strimzi"
  scrape_interval = "30s"
  forward_to      = [prometheus.relabel.strimzi.receiver]
}

prometheus.relabel "strimzi" {
  forward_to = [prometheus.remote_write.opspilot.receiver]

  rule {
    source_labels = ["__name__"]
    regex         = "kafka_(log_log|cluster_partition)_.+"
    action        = "drop"
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
  --set-file alloy.configMap.content=strimzi.alloy \
  --set 'alloy.extraEnv[0].name=OPSPILOT_API_KEY' \
  --set 'alloy.extraEnv[0].valueFrom.secretKeyRef.name=opspilot' \
  --set 'alloy.extraEnv[0].valueFrom.secretKeyRef.key=api-key'
```

A few things worth understanding:

- **It finds every Strimzi cluster in the Kubernetes cluster** - Kafka nodes, Kafka Exporters, Cruise Control, and the operators - by Strimzi's own pod labels and port names, so a new cluster is collected as soon as it starts.
- **The relabel rule drops the per-partition series** Strimzi's rules export: eleven for every partition replica a node holds, which the dashboards take from the Kafka Exporter instead. A Kafka node then sends about 400 series, however many partitions it has.
- **Keep `job_name` as it is.** Most of these metric names are the same as plain Kafka's, and the dashboards and alerts select on it.

Already running Alloy in the cluster - the Kubernetes Monitoring chart, for instance? Add the blocks above to its config instead, with `forward_to` naming its existing `prometheus.remote_write`.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
kafka_server_kafkaserver_brokerstate{job="integrations/strimzi"}
```

You should get one series per Kafka node, labeled with its namespace and cluster. If nothing comes back, check the `Kafka` resource has `metricsConfig` and its pods have rolled. Then run `kafka_brokers{job="integrations/strimzi"}` (the Kafka Exporter) and `strimzi_resources` (the cluster operator). The Alloy UI (`kubectl -n monitoring port-forward ds/alloy 12345`) shows each target and any scrape error.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
