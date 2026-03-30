# Logs Drilldown

![!Screenshot](../../Data-insights/Features/images/logs-drilldown.png)


Search, filter, and analyze logs across services.

Navigate to **Logs Drilldown** from the left-hand sidebar to explore your log data without writing LogQL queries.


---

## Filters

| Filter | Description |
|---|---|
| **Filter by label values** | Narrow services by label (e.g., `service`, `namespace`) |
| **Show logs** | Display raw log lines alongside service charts |
| **Data source** | Select the Logs data source (top right) |
| **Time range** | Set the time window using the picker in the top right |

---

## Browsing services

The main view displays a list of services, each showing:

- A **log volume time series chart** for the selected time range
- A **log preview panel** on the right with recent log lines
- A **star icon** to favourite the service
- An **Include** button to scope the view to that service
- A **Show logs** button to open the full log stream for that service

---

## Filtering by label

Use the **Labels** section at the top to filter services by a specific label dimension.

1. Click **Filter by label values** and select a label (e.g., `service`).
2. The view updates to show matching services. The active label filter appears below the search bar (e.g., `service`), along with a count of results (e.g., Showing 9 of 9).
3. Use the **Search values** dropdown to search within the label values.
4. Click **Include** on a service to scope the view to that service only.

---

## Viewing logs for a service

Click **Show logs** on any service to open its full log stream. The breadcrumb updates to Home > Drilldown > Grafana Logs Drilldown > Logs, and the active service filter is shown at the top.

### Tabs

| Tab | Description |
|---|---|
| **Logs** | The default view. Shows all log lines matching the current filters, with a log volume chart above. |
| **Labels** | Log volume broken down by label. |
| **Fields** | Detected fields and their frequency across log lines. |
| **Patterns** | Automatically detected log patterns. Useful for spotting common issues or noise. |

### Log volume chart

The chart at the top shows log volume over the selected time range, colour-coded by log level (e.g., INFO). The total count is shown below the chart (e.g., INFO Total: 232).

### Filtering log lines

- Use **Filter logs by string** to search for specific text within log lines.
- Click **Include** or **Exclude** to scope or remove matching lines.
- Use the **Log levels** dropdown to filter by severity (e.g., INFO, ERROR, WARN).
- Use the **Fields** filter to narrow logs by a specific field value.
- Set a **Line limit** (top right) to control how many lines are loaded at once.

### Fields panel

The **Fields** panel on the left lists all detected fields across your logs, along with the percentage of log lines that contain each field. Click any field to explore its values.

### Display options

Use the icons on the right-hand side to adjust how logs are displayed — switch between **Logs**, **Table**, and **JSON** views, toggle **Newest logs first**, enable **Deduplication**, adjust font size, or **Download logs**.

You can click and drag on the log volume chart to zoom into a specific time window.

---

!!! info "Learn more"
    [Logs Drilldown](https://grafana.com/docs/grafana/latest/explore/simplified-exploration/logs/)

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
