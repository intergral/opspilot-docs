# Traces

The Traces tab shows all traces for the selected service, with performance charts and a filterable trace list. Use it to investigate slow requests, errors, and individual spans in detail.

## Filters

At the top of the page, use the filter bar to narrow the trace list:

| Filter | Description |
|---|---|
| **Select Service** | Filter by service name |
| **Select Span Name** | Filter by a specific operation or endpoint |
| **Select Status** | Filter by span status (e.g. error, ok) |
| **Duration** | Sort or filter by trace duration |
| **+ Filter** | Add additional filter conditions |

Click **Clear all** to reset all filters.

Use the **Filter traces...** search box to search within the trace list by keyword.

## Performance charts

Four charts give you an overview of trace performance across the selected time range:

| Chart | Description |
|---|---|
| **P50 Latency** | Median trace duration, broken down by service |
| **P95 Latency** | 95th percentile duration, highlighting slower traces |
| **Span Status** | Breakdown of span outcomes across all traces |
| **Top Throughput** | Most active endpoints by request volume |

## Traces list

The **Traces** table lists individual traces with:

| Column | Description |
|---|---|
| **Service and Operation** | The service name, operation, and span count |
| **Trace ID** | The unique identifier for the trace |
| **Started** | When the trace began |
| **Duration** | Total end-to-end duration |

Click any row to expand it and view the full span breakdown. The list shows up to 100 traces at a time.

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
