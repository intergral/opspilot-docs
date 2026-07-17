# Silences

Deploying during a maintenance window and don't want to wake the on-call team? A **silence** temporarily mutes matching alert notifications for a set time window, so planned maintenance, known outages, and active investigations don't flood people with noise - while the rules keep evaluating in the background so nothing is actually missed.

Navigate to **Alerting > Notifications** and open the **Silences** tab to view and manage silences. Use **Show expired** to see silences that have already ended.

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
2. Under **Label matchers**, add label key/value pairs to identify which alerts to mute. Click **+ Add matcher** to add more:

| Operator | Meaning |
|---|---|
| `=` | Exact match |
| `!=` | Does not match |
| `=~` | Regex match |
| `!~` | Regex does not match |

3. Set the **Time window**: pick a quick duration (**1h**, **2h**, **4h**, **8h**, **12h**, **24h**, **48h**, or **1 week**), or set **Starts at** and **Ends at** manually
4. Add a **Comment** describing why the silence was created (such as, `Replacing database server`)
5. Click **Create silence** to activate it

!!! tip
    Add a comment even for short silences - it helps teammates understand why alerts are quiet when they check the Silences page.

!!! info "Learn more"
    [Edit and remove silences](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/create-silence/)
