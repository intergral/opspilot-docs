Use templating to transform raw technical metrics-like heap usage or slow request counts-into human-readable alerts. By incorporating dynamic data, your team can diagnose issues directly from a Slack message or email without opening the dashboard first.

## Alert Rule Annotations

[Annotations](https://grafana.com/docs/grafana/latest/alerting/fundamentals/templates/#template-annotations) are the primary way to pass OpsPilot metadata into your alerts.

* **Purpose:** Use them for the **Summary** (what happened) and **Description** (why it matters).
* **Dynamic Values:** Use Go templating to display specific FR metrics. For example, show the exact millisecond duration of a slow request or the specific URL that triggered the alert.

!!! info "Learn more"
    [Annotations in Alerting](https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/annotation-label/)

## Alert Rule Labels

[Labels](https://grafana.com/docs/grafana/latest/alerting/fundamentals/templates/#template-labels) categorize your OpsPilot instances (such as, `app_name`, `environment`, or `server_id`).

* **Purpose:** Use labels to route alerts to different teams (such as, `tier: critical` goes to PagerDuty, while `tier: warning` goes to Slack).
* **Important:** Avoid putting highly variable data (like a dynamic timestamp or unique Request ID) in labels. This creates cardinality issues, making it harder to track alert history. Keep these values in **Annotations** instead.

!!! info "Learn more"
    [Labelling Alerts](https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/annotation-label/#labels)

## Notification Templates

Managed in the [Contact Points](Contact-points.md) section, these define the wrapper or envelope for your notifications.

* **Purpose:** Ensure every Slack alert from OpsPilot has the same layout, icon, or link to your runbooks.
* **Centralization:** Instead of writing the same Slack block for 50 different alert rules, you define it once in a **Notification Template** and reuse it across all OpsPilot alerts.

!!! info "Learn more"
    [Create Notification Templates](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/template-notifications/)


## Which one should I use?

| Goal | Use This | Example Syntax |
| --- | --- | --- |
| **Show the current CPU %** | Annotation | `Current Value: {{ $values.B.Value }}%` |
| **Direct to the correct Slack channel** | Label | `team: devops` |
| **Add a link to the FR Instance** | Annotation | `[View Instance]({{ .Labels.fr_url }})` |
| **Bold the Title for all Slack alerts** | Notification Template | `{{ define "my.title" }} *ALERT:* {{ .Labels.alertname }} {{ end }}` |

!!! tip
    For a practical example of templating, refer to this [tutorial](https://grafana.com/tutorials/alerting-get-started-pt4/).
