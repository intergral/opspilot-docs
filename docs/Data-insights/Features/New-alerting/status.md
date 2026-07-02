# Status

The **Status** page gives you an overview of alert rule states across your environment. Navigate to **Alerting > Status** to open it.

## Rules tab

The Rules tab shows all your alert rules as a hexagonal grid. Each hexagon represents one rule, colour-coded by its current state:

| State | Colour | Description |
|---|---|---|
| **Normal** | Green | The rule is evaluating and its condition is not currently met |
| **Firing** | Red | The alert condition is met and the rule is actively firing |
| **Paused** | Grey | The rule is paused and not being evaluated |

Hover over any hexagon to see the rule name, its current state, and the group it belongs to.

Rules that need attention are surfaced at the top of the page, above the grid, so firing alerts are visible without scrolling.

## Instances tab

The Instances tab shows individual alert instances rather than rules. Each hexagon is one instance, colour-coded by state using the same scheme as the Rules tab.

Hover over any hexagon to see the instance name, its state, the group it belongs to, and all labels attached to it (such as `alert_type`, `contact_points`, and `opspilot_coworker`).

Use the state filters to narrow the view - for example, selecting **Paused** shows only paused instances and hides the rest.

---

## Filtering and grouping

- Use **Search rules** to find a rule by name
- Use the state filters (**Normal**, **Paused**, **Firing**) to scope the count and highlight rules in a specific state
- Use **Group by** to reorganise the grid. Options are:

| Group | Description |
|---|---|
| **No grouping** | All rules in a single grid (default) |
| **Namespace** | Group by the folder or namespace the rule belongs to |
| **Rule Group** | Group by the rule group within a namespace |
| **severity** | Group by the severity label on the rule |
| **alert_type** | Group by alert type label |
| **contact_points** | Group by the contact point label |
| **opspilot_coworker** | Group by whether the rule is connected to Coworker |
| **opspilot_slack_post** | Group by Slack post label |
| **created_by** | Group by the user who created the rule |
| **agent_proposal_id** | Group by agent proposal ID |

## Creating from Status

Click **+ New** in the top right to create something new. Three options are available:

| Option | Description |
|---|---|
| **Alert rule** | Create a new alert rule. See [Rules](rules.md) for full details |
| **Contact point** | Add a new contact point. See [Contact Points](contact-points.md) for full details |
| **Custom detector** | Create a custom anomaly detector. See [Anomaly Detectors](anomaly-detectors.md) for full details |
