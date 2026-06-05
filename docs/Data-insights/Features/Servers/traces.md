# Traces

The **Traces** tab provides deep insights into the performance of individual requests (spans) as they move through the system. This view is critical for identifying slow transactions, latency issues, and service dependencies.

![Screenshot](traces.png)

Four key graphs display at the top of the view:

1. **50th Percentile Span Duration** - Shows the median response time for requests, indicating typical performance.
2. **95th Percentile Span Duration** - Displays response times for 95% of requests, helping identify slower outliers.
3. **Status (Top spans by status code)** - Breaks down request volume by HTTP status codes (errors vs. successful requests).
4. **Top 20 Span Throughput** - Shows request volume for the most active endpoints or operations.

Use the filter bar to narrow down traces by:

- **Job** - The service or application name (e.g., quote-service-lucee).
- **Span Name** - Specific operation or endpoint.
- **Status** - HTTP status code (All, error, ok, unset).
- **Flavor** - Request type or protocol.
- **Min/Max Duration** - Filter by response time range.
- **Adhoc Filters** - Add custom filters with the + button.

Below the metrics, the trace list shows individual requests with:

- **Trace ID** - Unique identifier for the request (click to view detailed trace timeline).
- **Start time** - When the request began.
- **Service** - Which service handled the request.
- **Name** - The HTTP method (GET, POST, etc.).
- **Duration** - Total request processing time in milliseconds.


## Trace Details

When you click on a specific Trace ID from the Traces list, you navigate to the **Trace Details** view. This view is the core of distributed tracing, presenting the entire transaction flow as a precise waterfall diagram.

![Screenshot](trace-details.png)

The header displays key information about the selected trace:

- **Service and Method** - The originating service and HTTP method (e.g., load-generator: POST).
- **Total Duration** - End-to-end request time (e.g., 513.22ms).
- **Timestamp** - Exact date and time the request started.
- **Status Code** - HTTP response code with visual badge (e.g., 200, POST).
- **Endpoint Path** - The API endpoint or route accessed.

### Navigation Tabs

The trace details interface includes multiple tabs:

- **Detail** - The default view showing the waterfall diagram of the trace spans.
- **Profile** - When available, this tab displays a hierarchical flame graph showing method execution times and call stacks. Each entry shows the percentage of total execution time and duration (e.g., "100% - 1.61s") along with the full method path, allowing you to identify performance hotspots at the code level.
    ![Screenshot](profile.png)

- **[Event Snapshot](https://docs.fusionreactor.io/Data-insights/Features/Debugger/Event-Snapshot/)** - This tab appears when a snapshot is associated with the trace, providing deep diagnostics including decompilation, frames, and request/response details captured at the point of the event.
     ![Screenshot](event-snap.png)

### Trace Actions

Three action buttons in the top-right allow you to:

1. **Analyze Trace** - Send the trace to OpsPilot AI for natural language analysis of performance bottlenecks, errors, and optimization recommendations.

2. **Trace ID** - Copy the unique trace identifier to your clipboard for sharing or external analysis.

3. **Export** - Download the trace data in a portable format for offline analysis or archival.

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
