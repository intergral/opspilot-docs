# Silences

Silences temporarily mute alert notifications for a set time window using label matchers. Use them during planned maintenance, known outages, or while investigating an incident to reduce noise.

Navigate to **Alerting > Silences** to view and manage silences. Use **Show expired** to see silences that have already ended.

!!! note
    Silences stop notifications from being sent but do not stop alert rules from evaluating. Firing alerts remain visible in [Status](status.md).

## Silences vs. Time Intervals

Both suppress notifications without stopping rule evaluation, but serve different purposes:

| | Silences | Time Intervals |
|---|---|---|
| **Setup** | Created ad-hoc and matched to alerts using label matchers | Defined as a schedule and linked to a notification policy |
| **Period** | One-time, with a fixed start and end time | Recurring (such as, every weekend or every Monday) |
| **Primary use** | Unexpected maintenance, incident response, or quick one-offs | Scheduled maintenance windows or off-hours for non-critical alerts |

## Creating a silence

1. Click **+ New silence**
2. Set the **Start** and **End** time for the suppression window, or enter a **Duration** (such as, `2h`) to calculate the end time automatically
3. Under **Matchers**, add label key/value pairs to identify which alerts to mute:

| Operator | Meaning |
|---|---|
| `=` | Exact match |
| `!=` | Does not match |
| `=~` | Regex match |
| `!~` | Regex does not match |

4. Add a **Comment** describing why the silence was created (such as, `Replacing database server`)
5. Click **Submit** to activate the silence

!!! tip
    Add a comment even for short silences - it helps teammates understand why alerts are quiet when they check the Silences page.

!!! info "Learn more"
    [Edit and remove silences](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/create-silence/)
