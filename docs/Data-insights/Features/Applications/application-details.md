# Application Details

The **Application Details** view breaks a single application down by operation, with ranked operations, per-operation metric graphs, and the traces behind them.

Navigate to **Applications** > **Application Details** from the left-hand sidebar. The view has two tabs, **Overview** and **Info** - this page covers **Overview**.

---

## Filters

A filter bar runs across the top:

| Control | What it does |
|---|---|
| **Catalog / Label** | Group by **Catalog** entry or by **Label** |
| **Application** | Select the application to inspect |
| **Show by** | Choose the metric the Top 20 is ranked by (for example **Throughput**) |
| **Select Status** | Filter transactions by HTTP status code |
| **Select Flavor** | Filter by transaction type (for example a web request or JDBC) |
| **Duration** | Filter transactions by duration |
| **Clear all** | Reset the filters |

---

## Top 20

The **Top 20** panel on the left ranks the application's operations by the selected **Show by** metric - its heading reflects the choice, for example **Top 20 - Throughput**. Each row shows the operation (such as `www/getquote.cfm`), its total, and a bar for relative volume.

---

## Metrics

The **Metrics** panel shows five graphs for the application, each broken down by operation over the selected time range:

- **Time Taken (%)**
- **Avg Response Time**
- **Max Response Time**
- **Throughput**
- **Errors/s**

A legend under each graph lists the operations. Collapse the panel with the **Metrics** tab on its left edge.

---

## Traces

Search by **Trace ID** above the table, or browse the **Traces** list of recent transactions:

| Column | Description |
|---|---|
| **Service** | The service that handled the request - an error icon marks a trace that contains errors |
| **Span Name** | The operation, such as `GET` or `POST`; a trace whose root span has not arrived yet reads *&lt;root span not yet received&gt;* |
| **Spans** | Number of spans in the trace |
| **Services** | Number of services the trace touched |
| **Trace ID** | Unique identifier - click to open the full trace |
| **Timestamp** | When the transaction occurred |
| **Duration** | How long the transaction took |

The table loads the most recent 100 traces and fetches more as you scroll.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
