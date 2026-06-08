# Servers FAQ

## General

### What is the difference between Servers, Services, and Applications?

**Servers** shows host-level metrics collected by the FusionReactor agent, such as CPU, memory, request counts, and database throughput, displayed as 3D cube icons on the overview. **Services** shows your OpenTelemetry-instrumented services as a dependency graph, focusing on request flow, latency, and errors between services. **Applications** shows FR agent application and JVM-level data. Use Servers when you want to investigate host or instance health; use Services when you want to understand how requests move across your system.

### Why is a server not appearing on the overview?

A server only appears if it has the FusionReactor agent installed and is sending data to OpsPilot. Check that the agent is running and that the instance is connected. If the server was recently added, try refreshing the page or extending the time range.

### What do the environment labels (e.g. `canary`, `stg_staging`, `prod`) mean?

These are the environment or group names configured in the FusionReactor agent. Servers are grouped by these labels on the overview, making it easier to filter and compare health across different deployment environments.

---

## Visual indicators

### What do the cube colours mean?

| Colour | Meaning |
|---|---|
| **Blue** | Healthy - all metrics are within normal thresholds |
| **Orange** | Warning - one or more metrics are approaching a critical threshold |
| **Red** | Critical - one or more metrics have exceeded a threshold and may be impacting performance |

### What do the M, C, R, and D bars on each cube represent?

| Bar | Metric |
|---|---|
| **M** | Memory usage |
| **C** | CPU load |
| **R** | Web request count |
| **D** | Database throughput |

The fill level and colour of each bar shows the current load and alert status for that metric at a glance.

---

## Thresholds

### How do I configure warning and critical thresholds?

Click the thresholds icon in the top right of the Servers Overview to open the **Thresholds** panel. Set **Warning** and **Critical** values for each metric - Process CPU, Heap Usage, Web Request Count, DB Throughput, and Error Count - then click **Save**.

### How do I reset thresholds back to their defaults?

In the **Thresholds** panel, click the **Reset** button to restore all threshold values to their defaults.

### Can I set thresholds for individual metrics rather than from the overview?

Yes. On the **Metrics** tab for a specific server, each graph has an **Edit thresholds** icon in its top-right corner. Click it to configure warning and critical thresholds inline for that metric.

---

## Metrics

### What does the "Stat show as" dropdown do?

It controls which aggregate function is applied to the values shown on the stat cards at the top of the Metrics page. Options include Last, First, Min, Max, Mean, Median, Mode, and Total. Use **Last** to see the most recent value, or **Max** to see the peak over the selected time range.

### Why are my stat cards not updating?

Stat cards update automatically if an auto-refresh interval is set. If auto-refresh is off, they update when you change the selected time range. Check the auto-refresh icon in the top bar to enable it.

### How do I investigate a spike I can see in a graph?

Click and drag on the graph to zoom into the spike. Hover over data points to see exact values. You can also click **Ask AI** in the graph's top-right corner to send the metric to OpsPilot for an AI-guided explanation of the pattern.

---

## Crash Protection

### What is Crash Protection?

Crash Protection is a diagnostic feature that captures a detailed snapshot of your server's state when a triggering condition occurs - such as a memory threshold breach or an unhandled exception. The snapshot is uploaded to OpsPilot and includes heap usage, CPU, active requests, database activity, stack traces, and lock information.

### What version is required to use Crash Protection?

Crash Protection is available from **FusionReactor version 2025.2** onwards.

### How long are Crash Protection reports retained?

Reports are retained for historical analysis. There is no automatic expiry, so you can review past events to identify recurring patterns.

### How do I send a Crash Protection report to OpsPilot for analysis?

From the Crash Protection page, click the **Ask OpsPilot** button on any report to send the full snapshot to OpsPilot AI for automated analysis and guidance.

---

## UI Tunnel

### What is the UI Tunnel?

The UI Tunnel gives you secure remote access to the local FusionReactor UI of an on-premises agent directly through OpsPilot Cloud, without needing to expose your server to the public internet.

### Can I switch to dark mode in the UI Tunnel?

Yes. Use the theme toggle (sun or moon icon) in the header bar of the UI Tunnel to switch between light and dark mode.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
