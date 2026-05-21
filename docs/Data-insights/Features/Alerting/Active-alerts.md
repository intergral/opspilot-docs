# Firing Alerts

The **Firing Alerts** page shows all active notifications currently being managed by the Alertmanager. Notifications are grouped by label to reduce noise, and you can filter by state, contact point, or Alertmanager instance.

## Notification States

Each notification group will be in one of the following states:

| State | Description |
| --- | --- |
| **Active** | The alert is firing and notifications are being delivered to the configured contact point. |
| **Suppressed** | The alert is firing but notifications are being held back by a **[Silence](Silences.md)** or **[Mute Timing](Mute-timings.md)**. The alert is still visible here but no messages are being sent. |
| **Unprocessed** | The alert has been received by the Alertmanager but has not yet been matched to a notification policy. |

## Viewing Active Notifications

1. Navigate to **Alerting** > **Firing Alerts**.
2. Use the **Search by label** bar to filter by a specific label key or value (such as, `alertname=high-cpu`).
3. Use the **Notification state** buttons to filter by **Active**, **Suppressed**, or **Unprocessed**.
4. Use the **Filter by contact point** dropdown to show only notifications delivered to a specific destination.
5. Use **Custom group by** to regroup the list by a different label (such as, `severity` or `team`).

## Choosing an Alertmanager

Use the **Choose Alertmanager** dropdown in the top right to switch between Grafana's built-in Alertmanager and any external Alertmanager instances configured in your environment.

## Expanded Alert Detail

Click the **>** arrow on a notification group to expand it and view full details for each alert instance:

| Field | Description |
| --- | --- |
| **Duration** | How long the notification has been in its current state (such as, `Active for 3d 21h`). |
| **Instance labels** | All labels attached to this alert instance, displayed as colour-coded tags. |
| **Silence / See alert rule** | Action buttons to silence the alert or navigate directly to the rule that triggered it. |
| **__value_string__** | The raw metric values from the query at the time of firing, including label context. |
| **__values__** | JSON representation of query, threshold, and expression values. |
| **Runbook URL** | A link to your runbook or troubleshooting guide, if configured on the alert rule. |
| **Summary** | The summary annotation from the alert rule, describing what happened. |
| **Receivers** | The contact points currently handling this notification. |

## Silencing from Firing Alerts

You can create a silence directly from an active notification without navigating away:

1. Expand a notification group by clicking the **>** arrow on the left.
2. Click the **Silence** button on the alert instance row.
3. The silence form will be pre-filled with the alert's labels - adjust the duration as needed.
4. Click **Submit** to suppress notifications immediately.

!!! info "Learn more"
    [View and manage firing alerts](https://grafana.com/docs/grafana/latest/alerting/monitor-status/view-alert-state/)
