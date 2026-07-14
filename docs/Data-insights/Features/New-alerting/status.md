# Status

When you have dozens of alert rules across multiple services, knowing what's healthy and what needs attention shouldn't require opening each rule individually. The Status page gives you that at-a-glance view - a live map of every rule and instance in your environment, colour-coded by state, so you can spot problems and act on them without scrolling through a list.

Navigate to **Alerting > Status** to open it.

![Screenshot](/Data-insights/Features/images/Alerting/status.png)

## Rules tab

The Rules tab shows all your alert rules as a hexagonal grid. Each hexagon represents one rule, colour-coded by its current state:

| State | Colour | Description |
|---|---|---|
| **Normal** | Green | The rule is evaluating and its condition is not currently met |
| **Pending** | Amber | The condition has been met, but not yet for long enough to fire |
| **Firing** | Red | The alert condition is met and the rule is actively firing |
| **Paused** | Grey | The rule is paused and not being evaluated |

Hover over any hexagon to see the rule name, its current state, and the group it belongs to. **Scroll to zoom**, **drag to pan**, and **click a hexagon to view that rule**. Use the zoom (**+** / **-**) and reset controls in the bottom-right corner.

Rules that need attention are surfaced at the top of the page, above the grid, so firing alerts are visible without scrolling.

## Instances tab

Where the Rules tab shows one hexagon per rule, the Instances tab shows one hexagon per alert instance. A single rule can produce multiple instances - one per server, service, or label combination it matches. This view is useful when you need to understand the blast radius of a firing rule: how many things are affected, and which specific ones.

![Screenshot](/Data-insights/Features/images/Alerting/instance.png)

Hover over any hexagon to see the instance name, its state, the group it belongs to, and all labels attached to it (such as `alert_type`, `contact_points`, and `opspilot_coworker`).

Use the state filters to narrow the view - for example, selecting **Paused** shows only paused instances and hides the rest.

---

## Filtering and grouping

- Use **Search rules** to find a rule by name
- Use the state filters (**Pending**, **Normal**, **Firing**, **Paused**) to scope the count and highlight rules in a specific state. Only the states currently present are shown
- Use **Group by** to reorganise the grid by any label or property:

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

Click **+ New** in the top right to create something new without leaving the Status view:

| Option | Description |
|---|---|
| **Alert rule** | Create a new alert rule. See [Rules](rules.md) for full details |
| **Contact point** | Add a new contact point. See [Contact Points](contact-points.md) for full details |
| **Custom detector** | Create a custom anomaly detector. See [Anomaly Detectors](anomaly-detectors.md) for full details |

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
