The following examples demonstrate how to create common alert rules in OpsPilot using the Grafana Ruler-based alerting system. Each example covers the full configuration - query, condition, folder, evaluation group, No Data handling, and notifications.

Before following these examples, make sure you have:

- At least one **folder** created for your alert rules.
- At least one **evaluation group** configured (or create one as part of the steps below).
- At least one **contact point** configured. See [Contact Points](Alerting/Contact-points.md).

### Routing your notifications

There are two ways to route notifications when creating an alert rule:

| Approach | When to use | Setup required |
| --- | --- | --- |
| **Direct contact point** | You want all notifications from this rule to go to one specific destination. | No extra setup - select the contact point in the rule editor. |
| **Label-based routing** | You want flexible routing through notification policies (such as, routing by severity or team). | Requires **Advanced Alerting** to be enabled and notification policies configured. See [Notification Policies](Alerting/Notifications.md). |

Each example below covers both options in the notifications step.

---

## Performance checks

### 1. When any instance goes offline for 5 minutes

This rule monitors all instances on your OpsPilot account and fires when any of them stops reporting data.

Offline detection works in two ways: if `app_up` drops to `0`, the alert condition (**IS BELOW 1**) triggers directly. If the instance stops reporting entirely and metrics disappear, the **No Data → Alerting** setting fires the alert. Both cases are covered by this rule.

Because the rule produces one alert instance per time series, each instance is monitored independently. If one instance goes offline, only that instance's alert fires.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `Any Instance Offline`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the `app_up` metric. Leave instance and job filters unset to monitor all instances.
- Set the alert condition to **IS BELOW 1**. When an instance is online, `app_up` returns `1` - so the condition is false and the alert stays normal. When an instance goes offline, `app_up` drops to `0` or stops reporting entirely, which triggers the alert.

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder (such as, `OpsPilot Alerts`).
- Select or create an evaluation group with an interval of `1m`.
- Set the **Pending period** to `5m`. The alert will only fire after the instance has been consistently offline for 5 minutes.

**4. No Data handling**

Under **Configure no data and error handling**, set **No Data** to **Alerting**. When an instance stops reporting, the query returns no data and this setting transitions the alert to Firing.

**5. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a label to route through your notification policies - for example, `channel` = `slack`.

**6. Annotations**

- **Summary:** `Instance offline: {{ $labels.instance }}`
- **Description:** `The instance {{ $labels.instance }} has not reported data for 5 minutes and may be offline.`

**7. Save**

Click **Save rule and exit**.



---

### 2. When a single job goes offline for 5 minutes

This rule monitors a specific instance or job and fires when it stops reporting data. Use this for named, business-critical instances where you want a dedicated alert rather than relying on the broad monitoring of Example 1.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `Instance Offline - [instance name]`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the `app_up` metric and filter by the specific **Job** or **Instance** label you want to monitor (such as, `instance = "production-server-01"`).
- Set the alert condition to **IS BELOW 1**. When the instance is online, `app_up` returns `1` - so the condition is false and the alert stays normal. When the instance goes offline, `app_up` drops to `0` or stops reporting, which triggers the alert.

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder.
- Select or create an evaluation group with an interval of `1m`.
- Set the **Pending period** to `5m`.

**4. No Data handling**

Under **Configure no data and error handling**, set **No Data** to **Alerting**. When the monitored instance stops reporting, this transitions the alert to Firing.

**5. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a label to route through your notification policies - for example, `channel` = `slack`.

**6. Annotations**

- **Summary:** `Instance offline: {{ $labels.job }}`
- **Description:** `The instance {{ $labels.job }} ({{ $labels.instance }}) has not reported data for 5 minutes.`

**7. Save**

Click **Save rule and exit**.



---

### 3. When any instance is using over 90% CPU for 2 minutes

This rule fires when any instance sustains high system CPU usage, helping you catch runaway processes or capacity issues before they affect users.

!!! tip
    You can also use a **less than** threshold for underflow alerts - for example, alert when request volume drops below a baseline. This is useful for high-traffic services where unexpectedly low activity may indicate requests are not reaching the service.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `High CPU - Any Instance`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the **System CPU usage** metric. Leave instance and job filters unset to monitor all instances.
- Set the alert condition to **IS ABOVE 90**.

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder.
- Select or create an evaluation group with an interval of `1m`.
- Set the **Pending period** to `2m`. The alert only fires if CPU remains above 90% for at least 2 consecutive minutes, avoiding notifications for momentary spikes.

**4. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a label to route through your notification policies - for example, `channel` = `slack`.

**5. Annotations**

- **Summary:** `High CPU on {{ $labels.instance }}: {{ $values.A.Value | printf "%.1f" }}%`
- **Description:** `CPU usage has been above 90% for over 2 minutes on {{ $labels.instance }}.`

**6. Save**

Click **Save rule and exit**.



---

### 4. When any instance in a group is using over 90% allocation memory for 10 minutes

This rule monitors memory allocation across all instances sharing a specific group label, and fires when any of them sustains high memory usage for an extended period.

Instances can be assigned a group in OpsPilot, which appears as a label on their metrics. Filtering by group lets you scope an alert to a logical subset of your estate - for example, all instances in a production environment or a specific application tier.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `High Memory - [Group Name] Group`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the **Allocation memory usage** metric.
- Filter by the **group** label to target the specific group (such as, `group = testfr`). This scopes the rule to only the instances in that group.
- Set the alert condition to **IS ABOVE 90**.

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder.
- Select or create an evaluation group with an interval of `1m`.
- Set the **Pending period** to `10m`. This prevents noise from short-lived spikes - the alert only fires if memory pressure is sustained for 10 full minutes.

**4. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a label to route through your notification policies - for example, `channel` = `slack`.

**5. Annotations**

- **Summary:** `High memory on {{ $labels.instance }} (group: {{ $labels.group }}): {{ $values.A.Value | printf "%.1f" }}%`
- **Description:** `Allocation memory usage has been above 90% for over 10 minutes on {{ $labels.instance }} in the {{ $labels.group }} group.`

**6. Save**

Click **Save rule and exit**.



---

## Billing checks

Billing alerts let you monitor your OpsPilot usage against thresholds before you exceed a plan limit or incur unexpected on-demand charges.

!!! warning "Always filter by `servicename`"
    All billing metrics aggregate usage across **all services** unless you filter by the `servicename` label. Failing to specify a `servicename` will result in aggregated usage data, leading to inaccurate alerts. Always add a `servicename` filter as shown in the examples below.

The following billing metrics are available:

| Metric | What it measures |
| --- | --- |
| `fr_billing_usage_current` | Current monthly usage for the selected service |
| `fr_billing_charges_metered` | On-demand usage charges for the selected service |
| `fr_billing_usage` | Total billable data usage for the selected service |
| `fr_billing_charges_total` | Total current billing charges for the selected service |

---

### 5. On-demand usage alert

Triggers when on-demand usage charges for a service exceed a threshold, using the `fr_billing_charges_metered` metric.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `On-Demand Charges - [Service Name]`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the `fr_billing_charges_metered` metric.
- Filter by `servicename` and specify the target service name. This is required to avoid aggregated data across all services.
- Set the alert condition to **IS ABOVE** and specify your threshold value (in the units your billing reports use).

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder.
- Select or create an evaluation group with an appropriate interval (such as, `1h` for billing checks).

**4. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a routing label - for example, `channel` = `email`.

**5. Annotations**

- **Summary:** `On-demand charges threshold exceeded for {{ $labels.servicename }}`
- **Description:** `On-demand usage charges for {{ $labels.servicename }} have exceeded the configured threshold.`

**6. Save**

Click **Save rule and exit**.



---

### 6. Billable data usage alert

Triggers when total billable data usage for a service exceeds a threshold, using the `fr_billing_usage` metric. Use this to monitor data volume before you approach a plan limit.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `Billable Data Usage - [Service Name]`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the `fr_billing_usage` metric.
- Filter by `servicename` and specify the target service name.
- Set the alert condition to **IS ABOVE** and specify your threshold in bytes. For example, to alert at 80 GB, enter `80000000000`.

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder.
- Select or create an evaluation group with an appropriate interval (such as, `1h`).

**4. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a routing label - for example, `channel` = `email`.

**5. Annotations**

- **Summary:** `Data usage threshold exceeded for {{ $labels.servicename }}`
- **Description:** `Billable data usage for {{ $labels.servicename }} has exceeded the configured threshold.`

**6. Save**

Click **Save rule and exit**.



---

### 7. Total billing charges alert

Triggers when total billing charges for a service exceed a threshold, using the `fr_billing_charges_total` metric. Use this for a high-level cost ceiling alert covering all charge types.

#### Configuration

Navigate to **Alerting** > **Alert rules** and click **+ New alert rule**.

**1. Name**

Enter a name such as `Total Billing Charges - [Service Name]`.

**2. Query and condition**

- Select the **Metrics** data source.
- Select the `fr_billing_charges_total` metric.
- Filter by `servicename` and specify the target service name.
- Set the alert condition to **IS ABOVE** and specify your threshold value.

!!! tip
    Click **Preview alert rule condition** to confirm data is being returned before continuing.

**3. Folder and evaluation group**

- Select or create a folder.
- Select or create an evaluation group with an appropriate interval (such as, `1h`).

**4. Notifications**

- **Direct contact point (simple):** Under **Notifications**, select your contact point directly from the **Contact point** dropdown.
- **Label-based routing (advanced alerting):** Leave the contact point unset and add a routing label - for example, `channel` = `email`.

**5. Annotations**

- **Summary:** `Total billing charges threshold exceeded for {{ $labels.servicename }}`
- **Description:** `Total billing charges for {{ $labels.servicename }} have exceeded the configured threshold.`

**6. Save**

Click **Save rule and exit**.
