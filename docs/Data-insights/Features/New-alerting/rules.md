# Rules

A well-configured alert rule is the difference between knowing about a problem before your users do and finding out from a support ticket. The Rules page is where you build, manage, and investigate every alert rule in your environment - with a live view of what's firing, what's pending, and what's healthy, all in one place.

Navigate to **Alerting > Rules** to open it.

!!! info "Rules vs detectors"
    **Rules** are static checks - they run on a fixed schedule against fixed thresholds, best for known conditions with clear boundaries (like system CPU or allocated memory). **[Detectors](service-anomaly-detectors.md)** use AI to learn normal behaviour and flag anomalies automatically, so they adapt as your system changes.

## The rules list

![Screenshot](/Data-insights/Features/images/Alerting/rule-table.png)

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
| **Last evaluation** | When the rule was last evaluated |
| **Actions** | A notification count, an **Active** toggle to enable or pause the rule, and buttons to view (eye), edit, and open more options |

### Expanding a rule

Click a rule row in the list to expand it in place. The left side shows:

- **Metric** - a live graph of the query with the threshold overlaid. Use the time range picker (with step arrows and zoom) to adjust the window
- **State history** - a log of state transitions with counts for **Normal**, **Pending**, and **Error** (rows may show sub-reasons such as *Normal (MissingSeries)* or *Pending (Error)*). Click a row to zoom the graph to that moment

The **Dashboard** and **Runbook** buttons (top right of the expanded view) open the dashboard and runbook links from the rule's annotations. The right side shows:

| Field | Description |
|---|---|
| **Annotations** | The annotations from the rule (such as its description) |
| **Expression** | The query and threshold condition as chained steps - for example, `A` `max_over_time(up[5m])` feeding a `C` condition `< 1` |
| **Evaluation** | How often the rule is checked and the pending duration (such as, `every 60s · pending 5m`) |
| **Data source** | The data source the rule queries |
| **On no data** | What state the rule enters when the query returns no data |
| **On query error** | What state the rule enters when the query fails |
| **Notifies** | The contact points configured to receive notifications |
| **Instances** | The matched instances with a firing/pending breakdown and a **Firing only** toggle. Each row shows the instance's labels, its state and when it last fired, and a **Logs** button to jump to its logs |

![Screenshot](/Data-insights/Features/images/Alerting/rule-expanded.png)

### Rule detail view

![Screenshot](/Data-insights/Features/images/Alerting/high-cpu-rule.png)

From the [Status](status.md) page, click a hexagon to open the full rule detail view. The header shows the rule name and current state, with these actions in the top right:

| Action | Description |
|---|---|
| **Dashboard** | Opens the dashboard linked in the rule's annotations |
| **Runbook** | Opens the runbook URL linked in the rule's annotations |
| **Silence** | Create a [silence](silences.md) for this rule |
| **Pause** | Pause evaluation of the rule |
| **Edit rule** | Open the rule editor |
| **⋯** | More options |

A row of summary cards sits below the header:

| Card | Description |
|---|---|
| **Current value** | The latest query value, with the threshold shown alongside |
| **Threshold** | The condition and evaluation window (such as, `> 80 avg 5m`) |
| **Firing instances** | How many instances are firing out of the total |
| **Duration** | How long the rule has been in its current state |
| **Alerts this week** | Count of alerts over the last 7 days |

**Metric graph** (left) - a live graph of the query with the threshold overlaid. Toggle **Threshold**, **State transitions**, and **Pending window** overlays on or off. Use the time range picker (with step arrows and zoom) to adjust the window, shift-drag to zoom, or click the timeline to center. Click **Open in dashboard** to view the metric in a dashboard.

**State history** (left, below the graph) - a log of state transitions showing the change (such as, Normal from Pending) and when it happened. Shows the count over the last 24h; click **See all** for the full history.

**Investigate** (right) - quick links to explore the metric in related views.

**Rule** (right) - the rule's configuration:

| Field | Description |
|---|---|
| **Condition** | The threshold condition (such as, `> 80`) |
| **Evaluation** | How often the rule is checked and the pending duration (such as, `every 60s · pending 5m`) |
| **Data source** | The data source the rule queries |
| **Folder** | The folder the rule belongs to |
| **On no data** | What state the rule enters when the query returns no data |
| **On query error** | What state the rule enters when the query fails |
| **Notifies** | The contact points configured to receive notifications |

**Instances** (right, below Rule) - a count of matched, firing, and pending instances, with a list of all current instances and their labels. Toggle **Firing only** to hide healthy instances, and click **Logs** on any instance to view its logs.

### Sorting and filtering

- **Sort** - order rules by State, Name, or other fields. Toggle ascending/descending with the arrow button
- **Search** - find rules by name
- **Filters** - filter by folder, evaluation group, state, or label
- **Hide anomaly detectors** - toggle on to show only static rules and hide anomaly detectors from the list

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

A good alert rule has three things: a query that targets the right signal, a threshold that fires at the right level, and a routing label that gets the notification to the right person.

Click **+ New rule** (top right) to open the rule editor. (To create an anomaly detector instead, see [Service](service-anomaly-detectors.md) or [Custom Anomaly Detectors](custom-anomaly-detectors.md), or use the **Wizard** on the [Status](status.md) page.)

The rule editor has two modes, toggled in the top right:

| Mode | Description |
|---|---|
| **Quick** | A streamlined single-page form for common metric alerts |
| **Advanced** | The full editor with every option (folder and evaluation group, no-data and error handling, muting/grouping/timings, and the full notification message) |

### Quick mode

![Screenshot](/Data-insights/Features/images/Alerting/quick-rule.png)

Quick mode puts the essentials on one page:

- **Rule name** - the alert's name (becomes the `alertname` label)
- **Data source** - the data source to query (such as, Metrics)
- **What should trigger this alert?** - build the condition in **Builder** mode (*Alert when [metric] is [above / below] [value] for [duration]*, with optional **aggregate** and **filter**), or switch to **Code** to write the query directly. A **Preview** graph shows the threshold against recent data, with 15m/1h/3h/6h/24h range buttons
- **Notify** - click **+ Add contact point** to choose where notifications are sent
- **Labels** - click **+ Add label** to add routing labels
- **Annotations** - describe what the alert means, set the **runbook** URL, and add extra custom fields
- **When data is missing** - choose the state to use when no data is received (for example, **No Data**)

### Advanced mode

Advanced mode is a single-page form that exposes the full configuration - chained queries and expressions, a dedicated alert condition, and complete evaluation, routing, and annotation settings. Its sections, top to bottom, are below.

![Screenshot](/Data-insights/Features/images/Alerting/new-adv-rule.png)

#### What should trigger this alert?

Build the alert from a chain of **Queries & expressions**. Click **Add query** (or use its dropdown) to add a step; each step has a **reference ID** (such as `$query`) that later steps can reference. The available step types are:

| Step | Category | Description |
|---|---|---|
| **Query** | Data | Query metrics or logs - pick a **Data source** and **Type**, enter the query, and use the **Preview** graph |
| **Math** | Expression | Compose a formula with `$referenceId` values |
| **Reduce** | Expression | Reduce a series to a single scalar value - choose an **Input**, a **Function** (such as `mean`), and how to handle **non-numbers** |
| **Resample** | Expression | Realign a series by a time window |
| **Threshold** | Expression | Compare an **Input** against a value using an **Operator** (such as *is above*) |
| **Complex conditions** | Expression | Combine multiple conditions with AND/OR |

A new rule starts with a default **Query → Reduce → Threshold** chain. The **Alert condition** dropdown at the top selects which step's firing state determines whether the rule alerts.

#### Evaluation

The **Evaluation** section controls how the rule runs:

| Setting | Description |
|---|---|
| **Evaluate every** | How often the rule is checked (such as, `1m`) |
| **Pending for** | How long the condition must be continuously met before the alert fires (such as, `5m`). Prevents notifications for temporary spikes |
| **No data** | The state the rule enters when the query returns no data - **No Data**, **Alerting**, **Normal**, or **Keep last state** |
| **On error** | The state the rule enters when the query fails - **Error**, **Alerting**, **Normal**, or **Keep last state** |

#### Namespace

Expand **Namespace** and choose the **namespace** where the rule is stored. Namespaces keep rules organised and control access.

#### Rule name

Enter a descriptive, unique **Rule name**. It appears in notifications, and automatically becomes the `alertname` label on every alert instance the rule produces.

#### Then notify

Under **Then notify**, click **+ Add contact point** to choose where notifications are sent.

#### Labels

Expand **Labels** and click **+ Add label** to add routing labels. Labels control how alerts reach contact points via notification policies - for example, a `channel` label:

| Label | Value | Routes to |
|---|---|---|
| `channel` | `email` | Email contact point |
| `channel` | `slack` | Slack contact point |
| `channel` | `webhook` | Webhook contact point |

!!! info "Learn more"
    [Notification Policy](notification-policy.md)

#### Annotations

Expand **Annotations** to describe the alert:

| Field | Purpose |
|---|---|
| **Description** | What the alert means and when it fires |
| **Runbook URL** | A link to your runbook or incident response guide |

Click **+ Add annotation** to add more annotation fields. Dynamic values can be included using Go template syntax (such as, `{{ $values.A.Value }}`).

#### Save

Click **Save rule** to activate the rule. It begins evaluating on its next scheduled interval.

---

## Editing a rule

Click **Edit rule** on a rule's [detail view](#rule-detail-view) to reopen the rule editor with all of its current settings pre-filled. Editing uses the same **Quick** and **Advanced** modes as creating a rule, so you can adjust the query, threshold, labels, or notifications and click **Save changes**.

Quick mode:

![Screenshot](/Data-insights/Features/images/Alerting/edit-rule.png)

Advanced mode:

![Screenshot](/Data-insights/Features/images/Alerting/adv-edit.png)

---

## Pausing a rule

Click the **pause** icon on any rule in the list to pause evaluation without deleting it. While paused, the rule stops evaluating and no new alert instances are created. Existing firing instances remain in their last state until evaluation resumes.

## Alert rule limits

| Plan | Maximum rules |
|---|---|
| Free | 100 |
| Paid | 2,000 (soft limit) |
