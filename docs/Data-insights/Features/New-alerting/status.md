# Status

The **Status** page gives you an at-a-glance view of every alert rule's current state - a live health overview across all your alert sources, including third-party integrations. Group it by **source** or by **namespace** to see what needs attention without opening each rule one by one.

Navigate to **Alerting > Status** to open it.

![Screenshot](/Data-insights/Features/images/Alerting/status.png)

## Needs attention

A summary band at the top leads with what matters: how many rules **need attention** out of the total, and how many are currently **firing** and **pending** (for example, *7 of 44 rules - 1 firing, 6 pending*). A health bar shows the split across states, with a count for each:

| State | Meaning |
|---|---|
| **Firing** | The alert condition is met and the rule is actively firing |
| **Pending** | The condition has been met, but not yet for long enough to fire |
| **Normal** | The rule is evaluating and its condition is not currently met |
| **Paused** | The rule is paused and not being evaluated |

## Viewing and filtering

Controls across the top shape how the page is laid out:

| Control | Description |
|---|---|
| **List / Grid** | Switch between the list view and a compact grid view |
| **Source / Namespace** | Group the cards by data source or by namespace |
| **All sources** | Filter to a specific source |
| **State filter** | A multi-select (for example, **4 selected**) to show only rules in the chosen states. Click **✕** to clear it |
| **Expand all** | Expand every group to show all of its rules; it toggles to **Shrink all** to collapse them |
| **Hide filtered-out cards** | Hide the groups and rules that don't match the current filters |
| **Refresh interval** | How often the page auto-refreshes (for example, **30s**) |
| **OpsPilot** | Alerting AI shortcuts - **Help me make a rule**, or **Recommend alerts to set up** |
| **+ Wizard** | Create alerting resources - a rule, contact point, or custom detector (see [Creating from Status](#creating-from-status)) |

## Groups and rules

Rules are organised into cards - by **namespace** or by **source**, depending on the toggle. Each group card shows its name, a health bar, and a count for each state, with its rules laid out inside.

Each rule shows:

- Its **name** - for example, *frontend Duration Anomaly*
- Its current **state** and how long it has been in it - for example, *Firing for 9m*
- An **Active** toggle to enable or disable the rule - it reads **Paused** when the rule is off
- A **mute** icon to silence its notifications
- An **eye** icon (**View rule**) to open the rule's [detail view](rules.md#rule-detail-view)

When a group has more rules than fit, click **Show all N rules** to expand it, and **Show less** to collapse it again.

The **List** view stacks the groups and shows their rule cards inline, while the **Grid** view lays the groups out as compact cards in a multi-column grid - each summarising its state at a glance, and expandable to reveal the rules inside.

## Creating from Status

The **+ Wizard** button in the top right lets you create alerting resources without leaving the Status page. Click it to start a new alert rule, or use its dropdown for more options:

| Option | Description |
|---|---|
| **New rule** | Create a new alert rule. See [Rules](rules.md) |
| **New contact point** | Add a new contact point. See [Contact Points](contact-points.md) |
| **New custom detector** | Create a custom anomaly detector. See [Custom Anomaly Detectors](custom-anomaly-detectors.md) |

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
