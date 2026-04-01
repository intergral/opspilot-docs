An **Alert Rule** is a set of criteria that defines when OpsPilot should trigger an alert. Rules are evaluated continuously by the Grafana Ruler and route notifications through the Alertmanager.

## What makes up an Alert Rule?

An alert rule is built from four core components:

1. **Queries**

    The **Query** selects the specific dataset you want to monitor (such as, CPU usage, heap memory, or error rates).

2. **Conditions**

    The **Condition** is the threshold your query must reach or exceed to trigger an alert (such as, `CPU Usage > 90%`).

    !!! info "Learn more"
        [Queries & conditions](https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/queries-conditions/)

3. **Evaluation schedule**
    * **Interval:** How often the rule is checked (such as, every 1 minute).
    * **Duration:** How long the condition must stay "True" before the alert actually fires. This helps prevent notifications for temporary spikes.

4. **Customization & routing**
    * **Expressions:** Use math to combine multiple queries.
    * **[Labels & annotations](https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/annotation-label/):** Add metadata like severity levels or links to troubleshooting guides.
    * **Notification routing:** Define where the alert goes (such as, Slack, Email, or PagerDuty).
    * **Error handling:** Set rules for how to behave if the system encounters "No Data."

Grafana-managed rules also offer additional flexibility, including:

* **Multi-source queries**: Pull data from multiple data sources in a single alert.
* **Expressions**: Use math operations to combine or transform queries before evaluation.
* **Custom state handling**: Define specific behaviours for No Data and Error conditions.
* **Enhanced annotations**: Include dynamic metric values and runbook links in notifications.

!!! info "Migrating from simple alerting?"
    If you previously used FusionReactor's Mimir-based alerting, there are three key differences to be aware of:

    - **Folders** - Alert rules must now be placed in a folder. You will need to create one if you haven't already.
    - **Evaluation groups** - Rules are assigned to a group that controls their evaluation interval. Each rule must belong to a group.
    - **Labels for routing** - Alerts are routed to contact points via notification policies using label matchers. You must add the correct label to your rule for it to reach the right destination. See [Notification Policies](../Notifications.md) for the recommended approach.

!!! tip "Getting started"
    For quick-start tutorials on key alerting features, see [Getting started with Grafana Alerting tutorials](https://grafana.com/docs/grafana/latest/alerting/best-practices/tutorials/).

---

## How to Create an Alert Rule

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

### 1. Name the Alert Rule

Enter a descriptive and unique name in the **Name** field. This name appears in notifications, so make it meaningful (such as, `High CPU - Production Server`).

!!! note
    The rule name automatically becomes the `alertname` label on every alert instance the rule produces. This label can be used in notification policy matchers and in notification message templates (such as, `{{ $labels.alertname }}`).

### 2. Define Query and Alert Condition

* Select your **Data source** from the dropdown.
* Enter your query to select the metric you want to monitor (such as, a PromQL expression for CPU usage).
* Under **Alert condition**, define the threshold that triggers the alert (such as, `WHEN QUERY IS ABOVE 80`).
* Click **Preview** to see a live visualization of when the rule would fire.

!!! info "Advanced queries"
    For math expressions, multi-query conditions, and classic condition types, see [Queries and conditions](https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/queries-conditions/) in the Grafana documentation.

### 3. Set Folder and Evaluation Group

!!! warning "Required for all rules"
    Every alert rule must be assigned to a **folder** and an **evaluation group**. This is new compared to the previous alerting setup.

* **Folder:** Select an existing folder or click **+ New folder** to create one. Folders keep your rules organised and control access permissions.
* **Evaluation group:** Select an existing group or create a new one. The group sets the **evaluation interval** - how often all rules in the group are checked (such as, `1m`).
* **Pending period:** Set how long the condition must be continuously met before the alert fires (such as, `5m`). This prevents notifications for temporary spikes.
* **Keep firing for:** Optionally hold the alert in a firing state for a period after the condition resolves, to avoid noisy recovered/re-fired cycles for flapping metrics.

### 4. Add Routing Labels

Labels are how OpsPilot routes alerts to the correct contact point via notification policies. **At minimum, add a `channel` label** matching the destination you want to use.

| Label | Value | Routes to |
| --- | --- | --- |
| `channel` | `email` | Email contact point (policy matcher: `channel =~ .*email.*`) |
| `channel` | `slack` | Slack contact point (policy matcher: `channel =~ .*slack.*`) |
| `channel` | `webhook` | Webhook contact point (policy matcher: `channel =~ .*webhook.*`) |

Click **+ Add labels** and enter the key/value pair (such as, `channel` = `slack`).

You can add additional labels for filtering or grouping (such as, `severity=critical` or `team=ops`), but the `channel` label is what drives routing.

!!! info "How routing works"
    See [Notification Policies](../Notifications.md) for how to configure the matching policies that read these labels.

### 5. Configure No Data and Error Handling

Use the **Configure no data and error handling** section to define what state the alert enters when the query returns no data or fails to evaluate:

| Scenario | Option | Behaviour |
| --- | --- | --- |
| **No Data** | No Data | Alert enters the **No Data** state. |
| **No Data** | Alerting | Treat as if the condition was met - alert fires. |
| **No Data** | Normal | Treat as healthy - no notification sent. |
| **No Data** | Keep last state | Hold the previous evaluation result until data returns. |
| **Error** | Error | Alert enters the **Error** state. |
| **Error** | Alerting | Treat as if the condition was met - alert fires. |
| **Error** | Normal | Treat as healthy - no notification sent. |
| **Error** | Keep last state | Hold the previous evaluation result until the error clears. |

!!! tip
    **Keep last state** is a safe default for transient issues (such as, a data source briefly going offline). Use **Alerting** if you want to be notified any time data is missing or a query fails.

### 6. Configure Notifications

* Under **Notifications**, confirm the routing labels from Step 4 are correct.
* Expand **Muting, grouping and timings** to apply specific [mute timings](../Mute-timings.md) or override the default grouping behaviour inherited from the [notification policy](../Notifications.md).

### 7. Add a Notification Message

Add context to help the responder act quickly:

* **Summary:** A brief description of what happened (such as, `CPU usage has exceeded 80% on {{ $labels.instance }}`).
* **Description:** More detail or potential troubleshooting steps.

Dynamic metric values can be included using Go template syntax (such as, `{{ $values.A.Value }}`).

The following annotation fields are available:

| Field | Purpose |
| --- | --- |
| **Summary** | A brief description of what happened. Appears prominently in most notification integrations. |
| **Description** | More detail or troubleshooting context for the responder. |
| **Runbook URL** | A link to your runbook or incident response guide. Displayed in the **Firing Alerts** view and included in notifications. |
| **Dashboard URL** | A link to a relevant Grafana dashboard for deeper investigation. |
| **Panel URL** | A link to a specific panel on a dashboard. |

!!! info "Templating"
    For examples and syntax, see [Templates](../Templates.md).

### 8. Save and Deploy

Click **Save rule and exit** to activate the alert rule. It will begin evaluating on its next scheduled interval.

---

## Pausing evaluation

After saving, you can pause evaluation of a rule without deleting it. From the **Alert rules** list, click the **pause** icon on any rule. While paused, the rule stops evaluating and no new alert instances are created or updated. Existing firing instances are not resolved - they remain in their last state until evaluation resumes.

This is useful for temporarily disabling a noisy rule without losing its configuration.

## Alert rule limits

| Plan | Maximum rules |
| --- | --- |
| Free | 100 |
| Paid | 2,000 (soft limit) |

!!! info "Learn more"
    [Configure Grafana-managed alert rules](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/)
