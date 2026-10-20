# Kubernetes

Monitor Kubernetes clusters - nodes, workloads, and control-plane health.

Your clusters show up alongside the rest of your telemetry, on dashboards that are already built. You can see how each cluster is using what it has, from the whole cluster down to a single pod, with alerts when workloads fail, nodes come under pressure, or storage runs out.

!!! info "What this integration does"
    It provisions **dashboards**, **recording rules**, and **alert rules**. It does not collect anything itself - metrics come from the **Grafana Kubernetes Monitoring Helm chart**, which you run once in every cluster you want to see. Until your cluster is sending metrics, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Kubernetes**.

---

## Permission tiers

Kubernetes runs **Read-only**, the default. It requires an **OpsPilot API key** for the collector in your cluster.

Its **capabilities** are **Dashboards**, **Recording Rules**, and **Alerts**.

---

## 1. Write the values file

You need an OpsPilot API key, from **Data and Licenses > [API Keys](https://app.opspilot.com/organization/api-keys)**.

Save this as `opspilot-values.yaml`, setting `cluster.name`:

```yaml
cluster:
  name: <this-cluster's-name>

destinations:
  opspilot:
    type: prometheus
    url: https://api.opspilot.com/v1/metrics
    extraHeaders:
      authorization: <your-api-key>

clusterMetrics:
  enabled: true
  apiServer:
    enabled: true
  kube-state-metrics:
    metricsTuning:
      includeMetrics:
        - kube_pod_status_ready
        - kube_poddisruptionbudget_status_current_healthy
        - kube_poddisruptionbudget_status_desired_healthy
  kubelet:
    metricsTuning:
      includeMetrics:
        - kubelet_evictions
        - kubelet_runtime_operations_duration_seconds_bucket
        - rest_client_request_duration_seconds_bucket
        - storage_operation_duration_seconds_bucket

hostMetrics:
  enabled: true
  linuxHosts:
    enabled: true
    metricsTuning:
      includeMetrics:
        - node_bonding_active
        - node_bonding_slaves
        - node_disk_io_time_seconds_total
        - node_disk_io_time_weighted_seconds_total
        - node_disk_read_bytes_total
        - node_disk_written_bytes_total
        - node_filefd_allocated
        - node_filefd_maximum
        - node_load1
        - node_load5
        - node_load15
        - node_md_disks
        - node_md_disks_required
        - node_netstat_Tcp_OutSegs
        - node_netstat_Tcp_RetransSegs
        - node_netstat_TcpExt_TCPSynRetrans
        - node_network_receive_errs_total
        - node_network_receive_packets_total
        - node_network_transmit_errs_total
        - node_network_transmit_packets_total
        - node_nf_conntrack_entries
        - node_nf_conntrack_entries_limit
        - node_textfile_scrape_error
        - node_time_seconds
        - node_timex_maxerror_seconds
        - node_timex_offset_seconds
        - node_timex_sync_status
        - node_uname_info
        - node_vmstat_pgmajfault

collectors:
  alloy-metrics:
    presets: [clustered, statefulset]

telemetryServices:
  kube-state-metrics:
    deploy: true
  node-exporter:
    deploy: true
```

- **`cluster.name` fills the dashboards' cluster selector.** Give every cluster a different one, or their series merge. Use only letters, digits, `-`, and `_`: Grafana escapes a quote or backslash in the name, and then every panel is empty.
- **The `includeMetrics` lists are needed.** The chart keeps a reduced set of metrics by default, and some dashboard panels and alerts read metrics outside it. Without these lines those panels are empty and those alerts never fire. If the chart already runs in a cluster, update the lists and run step 2 again; the Nodes dashboards stay empty until you do.

---

## 2. Install the chart

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update grafana
helm upgrade --install k8s-monitoring grafana/k8s-monitoring \
  --version ^4 --namespace monitoring --create-namespace \
  --values opspilot-values.yaml
```

---

## 3. Confirm the data arrived

After a couple of minutes, open **Explore**, select the **Metrics** data source, and run:

```promql
count by (cluster, job) (up)
```

Each cluster should show `integrations/kubernetes/kube-state-metrics`, `integrations/kubernetes/kubelet`, `integrations/kubernetes/cadvisor`, `integrations/kubernetes/kube-apiserver`, and `integrations/node_exporter`.

The Compute Resources and the Nodes USE Method dashboards read series that the installed recording rules derive, so they fill in a minute or two after the rest.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

## 4. Turn on the alerts you want

The alert rules are installed **paused**. Open **Alerting → Alert rules**, find the **Kubernetes** folder, and resume the ones you want. Each alert's runbook link explains what it means and what to do.

---

## Troubleshooting

**No series in Explore.** Check the Alloy pods with `kubectl -n monitoring logs statefulset/k8s-monitoring-alloy-metrics`. A 401 or 403 on remote write means the API key is wrong.

**The API server row is empty on a managed cluster.** Some providers do not let a workload scrape the API server's metrics. The rest of the dashboards are unaffected.

---

## Removing it

Uninstalling the integration removes the dashboards and rules, not the chart. In each cluster, run:

```bash
helm uninstall k8s-monitoring --namespace monitoring
kubectl delete crd alloys.collectors.grafana.com
kubectl delete namespace monitoring
```

Helm leaves the CRD and the namespace behind. Keep the CRD if another Grafana Alloy Operator runs in the cluster, and the namespace if anything else runs in `monitoring`.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
