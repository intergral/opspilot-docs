# Logs

The Logs tab shows all log output for the selected service within the chosen time range. Use it to investigate errors, trace log patterns, and filter down to specific severity levels or log content.

![!Screenshot](logs.png)

## Filters

| Filter | Description |
|---|---|
| **Catalog / Raw** | Switch between catalog services and all detected services |
| **Select Catalog** | Filter logs to a specific service |
| **+ Filter** | Add additional filter conditions |

Click **Clear all** to reset all active filters.

## Log Rate chart

The **Log Rate** bar chart shows log volume over time, colour-coded by severity:

- <span style="color:#FF4D4D;">**Red**</span>: Error logs
- <span style="color:#4CAF50;">**Green**</span>: Info logs
- <span style="color:#9E9E9E;">**Grey**</span>: Unknown severity

Hover over a bar to see the exact counts per severity at that timestamp. Use this chart to quickly spot spikes in error output.

Three icons appear in the top right corner of the chart:

| Icon | Description |
|---|---|
| **Sync** | Refresh the chart data |
| **Ask AI** | Opens a Coworker conversation with this chart in context |
| **Fullscreen** | Expands the chart to full screen |

## Log list toolbar

Between the filters and the log list, a toolbar gives you additional controls:

| Control | Description |
|---|---|
| **Filter text** | Search log content by keyword or pattern |
| **All streams** | Select which log streams to include |
| **Labels** | Filter by log labels |
| **`{}`** | Toggle JSON formatting for structured log entries |
| **Sort order** | Switch between newest-first and oldest-first |
| **Single / split view** | Toggle between a single log panel and a split view |

## Severity filters

Above the log list, severity badges show the count for each level in the current view:

**Critical, Error, Warning, Info, Debug, Trace, Unknown**

Click a badge to filter the log list to that severity level only.

## Logs list

The **Logs** list displays log entries in chronological order. Each entry shows:

- **Timestamp**
- **Severity badge** (e.g. INFO, ERROR)
- **Log content**: the full log message, expandable for long entries

The list shows up to 100 lines at a time. Use the **Top** and **Bottom** buttons to jump to the start or end of the list.

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
