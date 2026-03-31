# About Dashboards

Dashboards combine metrics, logs, and trace data in one place to give you a complete picture of your environment. Use them to monitor infrastructure health, debug application issues, or track business metrics — all in a single view.

Navigate to **Dashboards** from the left-hand menu in OpsPilot to access your full library of pre-built and custom dashboards.

---

## The Dashboards library

The Dashboards page shows all dashboards and folders available to you. From here you can:

- **Search** for any dashboard or folder by name
- **Filter by tag** to narrow results by category
- **Show Starred** to see only dashboards you have favourited
- Toggle between **grid** and **list** view
- **Sort** by name, last modified, or other criteria

To create or import a dashboard, click **New** in the top-right corner:

| Option | Description |
|---|---|
| **New dashboard** | Start a blank dashboard in the panel editor |
| **New folder** | Create a folder to organise your dashboards |
| **Import** | Import a dashboard from a JSON file |

---

## Dashboard folders

Dashboards are organised into folders. The following folders are provisioned automatically:

| Folder | Contents |
|---|---|
| **Anomaly Detection** | Dashboards for AI-detected anomalies |
| **Billing** | Data usage and plan consumption |
| **Custom Anomaly Detectors** | User-defined anomaly detector views |
| **Custom Dashboards Folder** | Your saved custom dashboards |
| **FusionReactor** | Application performance dashboards from the FR agent |
| **FusionReactor Alerts** | Alert state views from the FR agent |
| **Infrastructure** | Host and infrastructure health |
| **Integrations** | Pre-built dashboards for third-party integrations |
| **Kubernetes** | Cluster and pod resource dashboards |
| **Logs** | Log browsing and analysis |
| **Service Anomaly Detectors** | Anomaly views scoped to individual services |
| **Traces** | Trace browsing and lookup |
| **Shared with me** | Dashboards shared by other users in your organisation |

!!! info
    Dashboards will continue to evolve — over time we will add new sets of dashboards and improve existing dashboards provisioned to your account. Some dashboards are marked as **experimental**, allowing us to continually roll out new concepts.

---

## Pre-built dashboard categories

### Metrics dashboards

| Dashboard | Category | Description |
|---|---|---|
| Databases | FusionReactor | Observe database activity including throughput, time, total queries and error rate, broken down by database, collection/table, and action. |
| Instance Map | Infrastructure | Observe instance health based on process CPU, system CPU, or JVM memory usage. |
| Instances | FusionReactor | Observe throughput, response time, and error count broken down per instance. |
| Request Performance | FusionReactor | Observe throughput, response time, and error count broken down by application, transaction route, and status code. |
| Service Changes | Infrastructure | Observe infrastructure-level service change events. |
| Span Metrics | FusionReactor | Observe span-level metrics from distributed traces. |
| Status Codes | FusionReactor | Observe HTTP status code breakdown across your applications. |

### Logs dashboards

| Dashboard | Category | Description |
|---|---|---|
| FusionReactor Logs | Logs | View and filter logs shipped from the FusionReactor agent. |
| Log | Logs | General log browser for all ingested log data. |
| Log Browser | Logs | Browse and search logs with advanced filtering. |
| Log Errors | Logs | Focus view on error-level log entries. |
| Log Events | Logs | Observe log event volume and patterns over time. |

### Traces dashboards

| Dashboard | Category | Description |
|---|---|---|
| Show Status Traces | Traces | View traces filtered by status code. |
| Show Traces | Traces | Browse all ingested trace data. |
| Trace Lookup | Traces | Look up a specific trace by ID or URL. |

### Kubernetes dashboards

| Dashboard | Category | Description |
|---|---|---|
| Kubernetes / Compute Resources / Cluster | Kubernetes | Observe CPU and memory usage across the entire cluster. |
| Kubernetes / Compute Resources / Pod | Kubernetes | Observe CPU and memory usage broken down per pod. |

### Integration dashboards

| Dashboard | Category | Description |
|---|---|---|
| ElasticSearch | Integrations | Observe metrics from your ElasticSearch cluster. |
| IIS | Integrations | Observe metrics from IIS web server. |
| Kafka | Integrations | Observe metrics from the Kafka exporter. |
| MongoDB | Integrations | Observe metrics from MongoDB. |
| MSSQL | Integrations | Observe metrics from the MSSQL exporter. |
| MySQL | Integrations | Observe metrics from the MySQL exporter. |
| NGINX | Integrations | Observe metrics from the NGINX community exporter. |
| NGINX Pro | Integrations | Observe metrics from the NGINX Pro exporter. |
| Node Exporter | Integrations | Observe host-level metrics from the Node exporter. |
| OracleDB | Integrations | Observe metrics from the OracleDB monitor. |
| Postgres | Integrations | Observe metrics from the Postgres exporter. |

### Billing dashboards

| Dashboard | Category | Description |
|---|---|---|
| Data Usage | Billing | Monitor your data ingestion usage against your plan limits. |

### Experimental dashboards

Some dashboards are marked as experimental. This allows us to continually roll out new concepts before they are fully production-ready. These dashboards may contain issues as we continue to refine and develop them.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
