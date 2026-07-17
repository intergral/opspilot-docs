# Time Intervals

Nobody wants a low-priority alert at 3am on a Sunday. **Time intervals** let you define recurring windows - business hours, weekends, maintenance slots - once, then reuse them across notification policies to control exactly when alerts are allowed to notify. Navigate to **Alerting > Notifications** and open the **Time Intervals** tab to view and manage them.

Once defined, time intervals are applied in your [notification policy](notification-policy.md) to control when notifications are delivered.

!!! note
    Time intervals suppress notifications only - the underlying alert rules continue evaluating normally.

## Creating a time interval

Click **+ New time interval** to open the creation panel.

### Name

Enter a descriptive name for the interval (such as, `weekends` or `business-hours`).

### Interval blocks

Each time interval is made up of one or more **interval blocks**. Multiple blocks are OR-combined, meaning the interval matches if any block matches.

Each block has the following fields:

| Field | Description |
|---|---|
| **Weekdays** | Select specific days (Mon-Sun). Leave unset to match all days |
| **Time ranges** | Click **+ Add time range** to define start and end times (such as, `22:00` to `06:00`). Leave unset to match all hours |
| **Days of month** | Comma-separated numbers or ranges from 1-31. Use negative values to count from the end of the month (such as, `-1` = last day, `20:25` = 20th to 25th) |
| **Months** | Select specific months (Jan-Dec). Leave unset to match all months |
| **Years** | A year or range (such as, `2025` or `2025:2030`). Leave unset to match all years |
| **Location (timezone)** | The timezone to evaluate the interval in (such as, `Europe/London`) |

Click **+ Add interval block** to add another block to the same interval.

Click **Create time interval** to save.

## Applying a time interval

After saving, apply the interval to a notification policy:

1. Go to **Alerting > Notifications** and open the **Notification Policy** tab
2. Find the policy you want to mute and click **Edit**
3. Select your time interval from the **Mute timings** dropdown
4. Click **Save policy**

!!! info "Learn more"
    [Mute timings and active intervals](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/mute-timings/)
