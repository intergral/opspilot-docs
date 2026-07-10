# Rules

A well-configured alert rule is the difference between knowing about a problem before your users do and finding out from a support ticket. The Rules page is where you build, manage, and investigate every alert rule in your environment - with a live view of what's firing, what's pending, and what's healthy, all in one place.

Navigate to **Alerting > Rules** to open it.

## The rules list

Rules are displayed with four state counters at the top:

| State | Description |
|---|---|
| **Firing** | The alert condition is currently met |
| **Pending** | The condition is met but the pending period has not yet elapsed |
| **Normal** | The rule is evaluating and its condition is not met |
| **Normal (MissingSeries)** | The rule returned no data - the query matched no series. The rule remains Normal but flags that the data source returned nothing |
| **Paused** | The rule is paused and not being evaluated |

### Views

Switch between **Table** and **Tree** view using the buttons in the toolbar:

- **Table** - a flat list of all rules with their state, folder, and group
- **Tree** - rules grouped by folder and evaluation group, useful for seeing how rules are organised

Use **Collapse all** to fold all groups at once in Tree view.

The table has the following columns:

| Column | Description |
|---|---|
| **State** | Current state of the rule (Firing, Pending, Normal, Paused) |
| **Name** | The alert rule name |
| **Namespace** | The folder the rule belongs to |
| **Group** | The evaluation group and its interval (such as, `auto-1m`) |
| **Actions** | View, edit, and more options |

### Expanding a rule

Click a rule row to expand its detail view. The left panel shows:

- **Metric** - a live graph of the query with the threshold overlaid. Use the time range picker to adjust the window. The shaded region indicates when the condition was met
- **State history** - a log of state transitions showing Normal, Firing, and Pending counts. Click a row to zoom the graph to that moment

Two quick-link buttons appear in the top right of the expanded view:

| Button | Description |
|---|---|
| **Dashboard** | Opens the dashboard linked in the rule's annotations |
| **Runbook** | Opens the runbook URL linked in the rule's annotations |

The right panel shows:

| Field | Description |
|---|---|
| **Annotations** | The summary annotation from the rule |
| **Query** | The PromQL or metric query being evaluated |
| **Condition** | The threshold condition (such as, `> 80`) |
| **Evaluation** | How often the rule is checked and the pending duration (such as, `every 60s · pending 5m`) |
| **Data source** | The data source the rule queries |
| **On no data** | What state the rule enters when the query returns no data |
| **On query error** | What state the rule enters when the query fails |
| **Notifies** | The contact points configured to receive notifications |
| **Instances** | Count of firing and pending instances, with a list of all current instances and their labels |

### Sorting and filtering

- **Sort** - order rules by State, Name, or other fields. Toggle ascending/descending with the arrow button
- **Search** - find rules by name
- **Filters** - filter by folder, evaluation group, state, or label

### OpsPilot

Writing good alert rules is hard - thresholds that are too sensitive create noise, too lenient and real problems slip through. Click the **OpsPilot** button to get AI-assisted help directly in context:

| Option | Description |
|---|---|
| **Help me make a rule** | Guides you through creating a new alert rule |
| **Help me set up notifications** | Helps configure contact points and routing |
| **Explain my firing alerts** | Explains what your currently firing alerts mean |
| **Suggest alert thresholds** | Recommends threshold values based on your data |

---

## Creating an alert rule

A good alert rule has three things: a query that targets the right signal, a threshold that fires at the right level, and a routing label that gets the notification to the right person. The steps below walk through each.

Click **+ New** and select **Alert rule** to create a new rule.

### 1. Name the alert rule

Enter a descriptive and unique name in the **Name** field. This name appears in notifications (such as, `High CPU - Production Server`).

!!! note
    The rule name automatically becomes the `alertname` label on every alert instance the rule produces.

### 2. Define query and alert condition

- Select your **Data source** from the dropdown
- Enter your query to select the metric you want to monitor (such as, a PromQL expression for CPU usage)
- Under **Alert condition**, define the threshold that triggers the alert (such as, `WHEN QUERY IS ABOVE 80`)
- Click **Preview** to see a live visualisation of when the rule would fire

### 3. Set folder and evaluation group

!!! warning "Required for all rules"
    Every alert rule must be assigned to a **folder** and an **evaluation group**.

| Setting | Description |
|---|---|
| **Folder** | Keeps rules organised and controls access permissions. Click **+ New folder** to create one |
| **Evaluation group** | Sets the evaluation interval - how often rules in the group are checked (such as, `1m`) |
| **Pending period** | How long the condition must be continuously met before the alert fires (such as, `5m`). Prevents notifications for temporary spikes |
| **Keep firing for** | Optionally hold the alert in a firing state after the condition resolves, to avoid noisy recovered/re-fired cycles |

### 4. Add routing labels

Labels control how alerts are routed to contact points via notification policies. Add at minimum a `channel` label:

| Label | Value | Routes to |
|---|---|---|
| `channel` | `email` | Email contact point |
| `channel` | `slack` | Slack contact point |
| `channel` | `webhook` | Webhook contact point |

Click **+ Add labels** and enter the key/value pair.

!!! info "Learn more"
    [Notification Policy](notification-policy.md)

### 5. Configure no data and error handling

| Scenario | Option | Behaviour |
|---|---|---|
| **No Data** | No Data | Alert enters the No Data state |
| **No Data** | Alerting | Treat as if the condition was met - alert fires |
| **No Data** | Normal | Treat as healthy - no notification sent |
| **No Data** | Keep last state | Hold the previous result until data returns |
| **Error** | Error | Alert enters the Error state |
| **Error** | Alerting | Treat as if the condition was met - alert fires |
| **Error** | Normal | Treat as healthy - no notification sent |
| **Error** | Keep last state | Hold the previous result until the error clears |

### 6. Configure notifications

- Confirm your routing labels are correct
- Expand **Muting, grouping and timings** to apply [time intervals](time-intervals.md) or override grouping from the [notification policy](notification-policy.md)

### 7. Add a notification message

| Field | Purpose |
|---|---|
| **Summary** | A brief description of what happened. Appears prominently in most notification integrations |
| **Description** | More detail or troubleshooting context |
| **Runbook URL** | A link to your runbook or incident response guide |
| **Dashboard URL** | A link to a relevant dashboard for deeper investigation |
| **Panel URL** | A link to a specific panel on a dashboard |

Dynamic values can be included using Go template syntax (such as, `{{ $values.A.Value }}`).

### 8. Save and deploy

Click **Save rule and exit** to activate the rule. It will begin evaluating on its next scheduled interval.

---

## Pausing a rule

Click the **pause** icon on any rule in the list to pause evaluation without deleting it. While paused, the rule stops evaluating and no new alert instances are created. Existing firing instances remain in their last state until evaluation resumes.

## Alert rule limits

| Plan | Maximum rules |
|---|---|
| Free | 100 |
| Paid | 2,000 (soft limit) |
