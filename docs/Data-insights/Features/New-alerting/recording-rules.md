# Recording Rules

Recording rules pre-compute frequently used or computationally expensive PromQL expressions and save the result as a new time series. Instead of recalculating a heavy expression every time it's needed - on a dashboard, in an alert rule, or in an investigation - the expression is evaluated on a schedule and the result is stored, so it's fast to read and consistent everywhere it's used.

Navigate to **Alerting > Recording Rules** to view and manage them.

## The recording rules list

| Control | Description |
|---|---|
| **Table / Tree** | Switch between a flat list and a view grouped by folder and evaluation group |
| **Collapse all** | Fold all groups at once in Tree view |
| **Sort** | Order rules by **Name** or other fields; toggle ascending/descending with the arrow |
| **Search** | Find a recording rule by name |
| **Filters** | Narrow the list, such as by folder or evaluation group |

When nothing matches the current filters, the list shows *"No recording rules match your filters"*.

## Creating a recording rule

Click **+ New recording rule** to create one. A recording rule needs a **name** (the new metric the result is stored under), the **PromQL expression** to evaluate, and an **evaluation group** that controls how often it runs - the same folder and evaluation-group model as [alert rules](rules.md).

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
