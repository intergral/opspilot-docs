# Services Overview
![!Screenshot](services.png)

<br>

The **Services** page gives you full visibility into your OpenTelemetry-instrumented services - how they connect, how they perform, and where problems are occurring.

<br>

<div class="intro-with-video">
  <div class="video-side">
    <iframe src="https://player.vimeo.com/video/1192175205?badge=0&autopause=0&player_id=0&app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" allowfullscreen></iframe>
  </div>
  <div class="intro-text">
    <p>Watch this short walkthrough to see the Services view in action - covering the service graph, dependency mapping, latency and error metrics, and how to drill into individual services for deeper investigation.</p>
  </div>
</div>

## Service Graph

The **Service Graph** displays your services as an interactive network diagram, showing the communication patterns and dependencies between them. Each node represents a service. Connections between nodes show how services call each other.

Use the graph to quickly identify which services are upstream or downstream of a problem area. You can pan by clicking and dragging, and zoom using the scroll wheel.

![!Screenshot](services-graph.png)

Each node shows the service's **average latency** and **request rate** directly on it. The colour of the node indicates its health: green means healthy, red means the service is producing errors. Connection lines between nodes also show the latency and request rate for that specific call path, and arrows indicate the direction of the call.

Two icons in the top right corner of the graph panel give you additional viewing options:

- **3D toggle**: switches the graph between a flat 2D layout and a 3D view
- **Expand**: opens the graph in full screen for a clearer view of complex environments

![!Screenshot](services-graph-expanded.png)

Use **Clear all** to reset any active service filters.

## Service Table

Below the graph, the **Service Table** lists all services with key performance metrics:

![!Screenshot](services-table.png)

| Column | Description |
|---|---|
| **Service** | The service name |
| **Throughput** | Request rate with a sparkline showing recent trend |
| **Avg Latency** | Average response time across all requests |
| **P50** | Median latency |
| **P95** | 95th percentile latency |
| **Errors/s** | Error rate per second |
| **Requests** | Total request count in the selected time range |
| **Errors** | Total error count in the selected time range |

Click any service name to open the [Service Detail](service-detail.md) view with that service pre-selected, giving you an immediate breakdown of its performance, errors, logs, and alerts.

Use the **Select Service** dropdown to filter the graph and table to a specific service. Use the time range selector in the top right to adjust the period shown.

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
