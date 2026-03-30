# Traces Drilldown

![!Screenshot](../../Data-insights/Features/images/traces-main.png)

Trace requests across services to find bottlenecks.

Navigate to **Traces Drilldown** from the left-hand sidebar to explore distributed trace data without writing TraceQL queries.



---

## Filters

| Filter | Description |
|---|---|
| **Data source** | Select the Traces data source |
| **Root spans / All spans** | Toggle between root-level spans only or all spans |
| **Filter by label values** | Narrow traces by attribute values |
| **Trace ID** | Look up a specific trace by ID |
| **Time range** | Set the time window using the picker in the top right |

---

## Metric type

Select the metric type to drive your investigation:

- **Span rate** — requests per second across services
- **Errors** — error rate over time
- **Duration** — latency distribution across spans

The main graph updates to show the selected metric over the chosen time range.

---

## Tabs

### Breakdown

The default view. Shows how the selected metric breaks down across attribute values.

- **Attributes panel** (left) — browse and search attributes by category: Favorites, All, Resource, Span
- Common attributes include `resource.service.name`, `resource.service.namespace`, `k8s.pod.name`, `span.name`, `span.status`, `http.status_code`
- Click **Add to filters** on any service card to scope the view
- Switch between **Single**, **Grid**, and **Rows** view modes
- Attributes are ordered by rate of requests per second, with error rate overlaid in red

### Service structure

Visualizes the relationships and dependencies between services in your traces.

### Comparison

Compare trace metrics across two time ranges or filter sets to identify regressions.

### Traces

A list of individual traces matching the current filters. Shows up to 200 results. Hover over a trace and click **View trace** to open the full trace detail view.

---

## Trace detail view

Clicking **View trace** opens a detail panel showing the full trace waterfall.

| Field | Description |
|---|---|
| **Trace ID** | Unique identifier for the trace (click to copy) |
| **Start time** | When the trace began |
| **Duration** | Total end-to-end time for the trace |
| **Services** | Number of services involved |
| **URL** | The request URL that triggered the trace (if available) |

### Span waterfall

The waterfall view shows each span as a horizontal bar, positioned on a timeline from 0 to the total trace duration. Each row shows the **service name**, **operation**, and **duration**.

Use **Span Filters** to narrow the spans shown. Use **Prev** / **Next** to step through spans.

### Analyze Trace

Click **Analyze Trace** in the top right to open a deeper breakdown of the trace, including span-level metrics and structure.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
