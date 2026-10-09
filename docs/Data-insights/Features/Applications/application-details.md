# Application Details

The **Application Details** view shows deeper performance data for a specific application.

Navigate to **Applications** > **Application Details** from the left-hand sidebar, or click into an application from the [Applications Overview](overview.md).

---

## Filters

| Filter | Description |
|---|---|
| **Application** | The selected application (e.g. QuoteCF) |
| **Show by** | Switch the Top 20 ranking between Throughput, Average Response Time, Max Response Time, and Error Count |
| **Status** | Filter transactions by HTTP status code |
| **Flavor** | Filter by transaction type (e.g. web request, JDBC) |
| **Min / Max Duration** | Filter transactions by duration range |
| **Adhoc Filters** | Add custom label-based filters |

---

## Top 20

The **Top 20** panel on the left ranks individual transactions by the selected **Show by** metric, with a bar chart showing relative volume.

---

## Metrics graphs

The same metrics from the overview are shown here, scoped to the selected application:

- Time Taken (%)
- Average Response Time
- Max Response Time
- Throughput
- Errors/s

---

## Traces

Below the graphs, a **Traces** table lists recent transactions:

| Column | Description |
|---|---|
| **Trace ID** | Unique identifier - click to open the full trace |
| **Start time** | When the transaction began |
| **Service** | The service that handled the request |
| **Name** | HTTP method (GET, POST, etc.) |
| **Duration** | How long the transaction took |

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
