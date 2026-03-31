# Infrastructure Monitoring

OpsPilot collects infrastructure metrics, logs, and traces using **Grafana Alloy** — a lightweight, vendor-neutral collector that runs on your hosts and pipelines telemetry signals to OpsPilot in a single agent.

Grafana Alloy is the recommended approach for infrastructure monitoring. It replaces the need for separate scraping agents by combining metric collection, log tailing, and trace forwarding into one configurable pipeline.

---

## What is Grafana Alloy?

[Grafana Alloy](https://grafana.com/docs/alloy/latest/) is an OpenTelemetry-compatible collector built on the Grafana Agent Flow architecture. It uses a component-based configuration model where you chain together sources, processors, and exporters to define exactly how telemetry flows through your infrastructure.

Key features:

- Scrapes **Prometheus-compatible metrics** from exporters and services
- Tails and forwards **log files** using Loki-compatible pipelines
- Receives and forwards **traces** via OTLP
- Runs on Linux, Windows, macOS, Kubernetes, and Docker
- Supports auto-discovery of targets in dynamic environments

---

## Kubernetes

Alloy is the recommended way to collect infrastructure telemetry from Kubernetes clusters. Deploy it as a **DaemonSet** to collect node-level metrics and logs, or as a **Deployment** for cluster-level scraping.

### What it collects

| Signal | Source |
|---|---|
| **Node metrics** | cAdvisor, kubelet `/metrics`, Node Exporter |
| **Pod/container logs** | `/var/log/pods/` via `loki.source.kubernetes` |
| **Cluster metrics** | kube-state-metrics |
| **Traces** | OTLP receiver forwarded from instrumented workloads |

### Deployment options

- **Helm chart** — the [Grafana k8s-monitoring Helm chart](https://github.com/grafana/k8s-monitoring-helm) bundles Alloy with pre-built pipelines for all signal types
- **Operator** — the [Grafana Agent Operator](https://grafana.com/docs/agent/latest/operator/) manages Alloy deployments via Kubernetes CRDs
- **Manual manifest** — deploy Alloy directly using a DaemonSet manifest and configure it with a ConfigMap

---

## Cloud providers

Alloy can be deployed on cloud VMs and managed services to collect infrastructure signals alongside your application telemetry.

### AWS

| What to collect | How |
|---|---|
| EC2 instance metrics | Node Exporter + Alloy on each instance |
| RDS / Aurora metrics | `prometheus.scrape` targeting the RDS exporter |
| CloudWatch metrics | `otelcol.receiver.awscloudwatch` component (via OTel Collector) |
| Application logs | `loki.source.file` tailing CloudWatch-synced log files or direct file tailing on instances |

### GCP

| What to collect | How |
|---|---|
| GCE instance metrics | Node Exporter + Alloy on each VM |
| GKE cluster metrics | Alloy DaemonSet with kubelet + cAdvisor scraping |
| Cloud Logging | Export logs to a Pub/Sub topic and consume via `otelcol.receiver.googlecloudpubsub` |

### Azure

| What to collect | How |
|---|---|
| Azure VM metrics | Node Exporter + Alloy on each VM or VMSS instance |
| AKS cluster metrics | Alloy DaemonSet (same as standard Kubernetes setup) |
| Azure Monitor metrics | `otelcol.receiver.azuremonitor` component |

---

## Other environments

Alloy runs anywhere you can install a binary or container:

- **Bare metal / on-premise** — install Alloy as a systemd service on Linux or a Windows service, point it at your exporters and log files
- **Docker / Docker Compose** — run Alloy as a sidecar or standalone container with a mounted config file
- **VMs (any cloud)** — deploy via your standard provisioning tooling (Ansible, Terraform, cloud-init)

---

## Getting started with Alloy

1. [Install Grafana Alloy](https://grafana.com/docs/alloy/latest/get-started/install/) on your target hosts
2. Configure an Alloy pipeline for your signals — see the [Grafana Alloy shipping guide](/Monitor-your-data/OpenTelemetry/Shipping/Grafana-agent/) for OpsPilot-specific configuration
3. Point the OTLP exporter at your OpsPilot endpoint using your API key
4. Verify data is flowing in the [Overview](/Data-insights/Features/overview/) page

!!! tip
    The [OTel Collector](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) is a valid alternative if you are already running a collector fleet or prefer the standard OpenTelemetry distribution.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
