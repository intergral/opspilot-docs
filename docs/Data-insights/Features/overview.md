# Overview

<div class="video-wrapper">
  <iframe src="https://player.vimeo.com/video/1175447059" width="100%" height="450" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
</div>

The **Overview** page is your observability dashboard at a glance. It gives you an immediate, high-level summary of your entire environment - services, servers, applications, alerts, anomaly detection, and usage - all in one place.

## Active account view

Once your environment is sending data, the Overview page shows a full observability summary.

![!Screenshot](../../Data-insights/Features/images/Active-account-overview.png)

### Services

The **Services** section displays key performance metrics aggregated across all your monitored services for the last hour.

| Metric | Description |
|---|---|
| **Overview (All Service Avg)** | Average latency across all services |
| **P95** | 95th percentile latency |
| **P99** | 99th percentile latency |
| **Error Rate** | Percentage of requests resulting in errors |
| **Throughput** | Number of requests per second |
| **Total Time** | Cumulative request time |

#### Services by latency

Below the summary metrics, **Services by latency** lists your top 10 services ranked by average latency over the last hour. Each service card shows:

- **Avg Latency**
- **P95 / P99**
- **Alerts** count
- **Throughput**

Click any service card to drill into that service's detailed performance data.

### Servers

The **Servers** section provides a summary of all servers running a FusionReactor agent, including:

- **Total Servers**
- **Avg Request Duration**
- **Error Count**
- **Throughput**
- **CPU Usage**
- **Memory Usage**

**Servers by latency** lists your top servers ranked by average latency, with CPU and memory breakdowns per server.

Click **Servers ->** to go to the full [Servers](/Data-insights/Features/servers/) view.

### Applications

The **Applications** section summarises all monitored applications, showing:

- **Total Applications**
- **Avg Request Duration**
- **Error Count**
- **Throughput**

**Applications by latency** lists your top applications ranked by average latency.

Click **Applications ->** to go to the full [Applications](/Data-insights/Features/applications/) view.

### Alerts

The **Alerts** panel shows a live count of alerts grouped by state:

| State | Description |
|---|---|
| **Firing** | Alerts currently breaching their threshold |
| **Pending** | Alerts that have triggered but not yet confirmed |
| **Recovering** | Alerts returning to a normal state |
| **Normal** | Alert rules currently within threshold |

Click **Alerts ->** to go to the full [Alerts](/Data-insights/Features/Alerting/Active-alerts/) view.

### Anomaly Detection

The **Anomaly Detection** panel shows a live count of anomaly alerts by state, mirroring the same Firing / Pending / Recovering / Normal breakdown.

Click **Anomaly Detection ->** to go to the full [Anomaly Detection](/Data-insights/Features/Anomaly-Detection/ADoverview/) view.

### Usage

The **Usage** panel shows your current consumption against your plan limits for the current pay period:

| Signal | Description |
|---|---|
| **Logs** | Log volume ingested (MB / GB) |
| **Traces** | Trace volume ingested (MB / GB) |
| **Metrics** | Active metric series |
| **Agents** | Number of connected FusionReactor agents |
| **OpsPilot** | OpsPilot AI tokens consumed |

A progress bar indicates how much of your plan allowance has been used.

## No Data view

If your account has no data yet, each section of the Overview displays a **Get Started** prompt to guide you through setup:

![!Screenshot](../../Data-insights/Features/images/New-account-overview.png)

| Section | Prompt |
|---|---|
| **Services** | You'll need an API key to instrument your application with OpenTelemetry. |
| **Servers** | Install FusionReactor on your servers to start monitoring. You'll need a license key. |
| **Applications** | Install FusionReactor to monitor your applications. You'll need a license key. |
| **Alerts** | Configure alert rules to monitor your infrastructure. |
| **Anomaly Detection** | Enable anomaly detection to automatically detect unusual behavior in your data. |

The **Servers** and **Applications** prompts also display your **FusionReactor Cloud license key** directly on the page so you can copy it for use during agent installation.

The **Usage** panel shows your plan limits with all values at zero until data starts flowing (for example, `0 bytes / 27 GB` for Logs).

Once data starts flowing in, the Overview automatically populates with your live metrics and telemetry.

!!! tip "Getting started"
    Follow the prompts on the Overview page to install the right agent or instrumentation for your stack, then return to the Overview to see your data appear.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
