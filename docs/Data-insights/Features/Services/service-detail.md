# Service Detail

The Service Detail page gives you a deep breakdown of a single service — its performance, errors, log patterns, catalog metadata, and active incidents. Arrive here by clicking a service name in the [Services Overview](overview.md).

![!Screenshot](service-detail.png)

Use the **Catalog** dropdown at the top to switch between services. The time range selector in the top right adjusts the period shown across all tabs. Click **Clear all** to reset filters.

The page is organised into six tabs: **Details**, **Metrics**, **Traces**, **Logs**, **Info**, and **Incidents**.

## Details tab

### Performance charts

Five charts give you an at-a-glance view of the service's health:

| Chart | Description |
|---|---|
| **Avg Latency** | Average response time across all requests, broken down by operation |
| **P95 Latency** | 95th percentile latency, highlighting worst-case response times |
| **Span Status** | Breakdown of span outcomes: STATUS_CODE_ERROR, STATUS_CODE_OK, STATUS_CODE_UNSET |
| **Top Throughput** | Request rate by endpoint, showing which operations are busiest |
| **Log Rate** | Volume of log output over time |

Each chart can be expanded to full screen using the expand icon in its top right corner.

### Span Errors

Lists the operations generating the most errors. Each row shows the service and operation name, span count, and trace count. Use the trace icon to jump directly to a trace, or the link icon to copy a direct link.

### Span Latency

Lists the operations with the highest average latency. Each row shows the operation, average duration, and trace count.

### Log Patterns

Surfaces recurring patterns in log output. Displays "No patterns detected in the current time range" when nothing is found.

## Metrics tab

Detailed metric charts for the selected service. Use the **Select Tempo service** and **Select Loki service** dropdowns to scope the data.

## Traces tab

See [Traces](traces.md) for full documentation of the trace explorer.

## Logs tab

See [Logs](logs.md) for full documentation of the log explorer.

## Info tab

Shows the catalog record for the selected service — ownership, classification, dependencies, and OpsPilot's accumulated knowledge.

### Service card

At the top of the tab, a card summarises the catalog entry:

| Field | Description |
|---|---|
| **Owner** | The person or team responsible for the service |
| **Language** | The primary language (if set) |
| **Repository** | The linked source repository (if set) |

Status badges on the right show the service's current classification at a glance:

| Badge | Description |
|---|---|
| **Service / Database / etc.** | The catalog type |
| **Tier 1 / Tier 2** | Criticality tier — Tier 1 is customer-facing or revenue-critical; Tier 2 is important but not directly customer-facing |
| **Active** | Lifecycle state |
| **Human-managed / OpsPilot-managed** | Whether the catalog entry is maintained manually or by OpsPilot |

Action buttons on the card:

| Button | Description |
|---|---|
| **Eye icon** | Watch or unwatch this service |
| **Settings icon** | Open catalog settings for this service |
| **Let OpsPilot manage** | Allows OpsPilot to refresh aliases, type, and other auto-populated fields. Your manual edits are preserved — OpsPilot only updates fields it has new evidence for. The entry reverts to human-managed the next time someone edits it manually |
| **Re-audit** | Trigger a fresh audit of the service's catalog entry |
| **Edit (pencil)** | Manually edit the catalog entry |
| **Delete (red trash)** | Remove the service from the catalog |

### Request flow

Shows the operations and dependencies that OpsPilot has observed in telemetry for this service. Displays a placeholder message until telemetry data arrives.

### Metadata

Key/value pairs attached to the catalog entry. Click **+** to add a new entry. Useful for storing context that isn't captured elsewhere — links, team contacts, or custom classification data.

### Runbooks

Runbooks linked to this service. Displays the count and a list of attached runbooks. Use the **+** button to attach one.

### What OpsPilot remembers

OpsPilot builds up a memory of each service as it runs tasks, investigates alerts, and chats about it. This panel shows that accumulated knowledge.

Use the text input to tell OpsPilot something about the service directly — for example, known quirks, recent changes, or context that isn't visible in telemetry.

## Incidents tab

Lists all incidents that have referenced the selected service. Use the **Catalog** dropdown to switch services. The count in the top right shows the total number of linked incidents — click the arrow to open the full incidents list.

Displays "No incidents have referenced this service" when none exist.

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
