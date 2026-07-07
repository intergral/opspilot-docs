# FAQ

Common questions about setting up and tuning alerts in OpsPilot.

## Why isn't my alert firing?

Check the following:

- **Pending period** - the condition must be continuously met for the full pending duration before the alert fires. If the condition dips in and out, the pending timer resets.
- **Condition** - open the rule and check the Metric graph. The shaded region shows when the condition was met. If there's no shading, the threshold may be set too high.
- **No contact points** - the alert may be firing but silently. Check the **Notifies** field in the expanded rule view.
- **Paused** - check the rule isn't in a Paused state.

## What is the difference between Pending and Firing?

**Pending** means the alert condition is currently met, but the rule's pending period hasn't elapsed yet. This prevents short spikes from generating noise. Once the condition has been met continuously for the full pending period, the alert moves to **Firing** and notifications are sent.

## Why does my rule show Normal (MissingSeries)?

This means the query returned no data - the metric series the rule is watching doesn't exist or isn't being reported. The rule stays Normal but flags that nothing was found. Check that your data source is shipping data and that the query targets the correct metric name.

## Why am I getting too many alert notifications?

A few approaches to reduce noise:

- **Increase the pending period** - a longer pending period filters out brief spikes.
- **Use time intervals** - mute notifications during off-hours or maintenance windows in [Time intervals](time-intervals.md).
- **Use silences** - temporarily suppress a specific alert in [Silences](silences.md).
- **Review your notification policy** - check your group wait and group interval settings to batch notifications rather than sending one per instance.
- **OpsPilot Alerts event source** - if you have noisy FusionReactor alerts, sort the OpsPilot Alerts event source by volume to identify and tune the noisiest rules first.

## What is the difference between silences and time intervals?

| | Silences | Time intervals |
|---|---|---|
| **Purpose** | Suppress a specific alert now | Define recurring mute schedules |
| **Scope** | Matched by labels | Applied via notification policy routes |
| **Duration** | Fixed start and end time | Repeating (e.g. every weekend) |
| **Best for** | Planned maintenance, known incidents | Regular out-of-hours suppression |

## How do I route alerts to different channels?

Add a `channel` label to your alert rule (e.g. `channel=slack`) and set up a matching route in the [Notification policy](notification-policy.md). The route matches on the label and sends to the corresponding contact point.

## What happens if a rule has no contact points configured?

The alert will still fire and change state, but no notifications will be sent. The **Notifies** field in the expanded rule view will show "No contact points configured".

## How many alert rules can I have?

| Plan | Maximum rules |
|---|---|
| Free | 100 |
| Paid | 2,000 (soft limit) |

## Can I pause a rule without deleting it?

Yes - click the pause icon on any rule in the list. While paused the rule stops evaluating and no new instances are created. Existing firing instances remain in their last state until evaluation resumes.

## What is the post-mortem gate in anomaly detectors?

The post-mortem gate blocks an incident from moving to a terminal (closed) status until its post-mortem has been published. It defaults on and can be toggled per severity in [Incident Settings](../../Incidents/Settings.md).

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
