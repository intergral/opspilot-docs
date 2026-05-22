# Alerting FAQ

## What changed from the previous Mimir-based alerting?

The advanced alerting system uses the full Grafana Ruler and Alertmanager stack. The key differences are:

- **Folders are required.** Rules must be organised into folders.
- **Evaluation groups are required.** The evaluation interval is set at the group level, not per rule.
- **Routing uses labels.** Alerts are routed to contact points via notification policies and label matchers, rather than by direct assignment at the rule level.
- **More configuration options** are available, including multi-source queries, math expressions, and custom state handling.

See [Configure Alert Rules](Alert-Rules/Configure-rules.md) for a full walkthrough of the new setup.

---

## What is the difference between a Contact Point and a Notification Policy?

A **[contact point](Contact-points.md)** defines *where* and *how* a notification is sent (such as, a specific Slack channel or email address).

A **[notification policy](Notifications.md)** defines *which* alerts are routed to which contact point, based on the labels on the alert rule.

Think of it as: the notification policy is the routing rule, and the contact point is the destination.

---

## How do I route an alert to a specific contact point?

Add a `channel` label to your alert rule (such as, `channel=slack`) and ensure a notification policy exists with a matching label matcher (such as, `channel =~ .*slack.*`).

See [Notification Policies](Notifications.md) for the recommended setup.

---

## When should I use a Silence vs. a Mute Timing?

| | Silence | Mute Timing (Time Interval) |
| --- | --- | --- |
| **Use for** | One-off suppression (such as, an emergency maintenance window) | Recurring schedules (such as, every weekend or overnight) |
| **Set up via** | Alerting > Silences | Alerting > Notification policies > Time intervals |
| **Applied to** | Individual alerts matched by label | Notification policies |

See [Silences](Silences.md) and [Time Intervals](Mute-timings.md) for setup instructions.

---

## Can I route the same alert to both Slack and email?

Yes. There are two ways:

1. **Single contact point with multiple integrations** - Add both a Slack integration and an email integration to the same contact point. Both will receive every notification sent to that contact point.

2. **Multiple policies with Continue matching** - Create separate child policies for each destination and enable **Continue matching** on each one. An alert matching the first policy will continue to be evaluated against sibling policies.

---

## How do I test whether my labels will route correctly?

Use the **Test** option on the Default policy in **Alerting** > **Notification policies**. Enter the label key/value pairs from your alert rule to simulate routing and see which policy and contact point the alert would be delivered to.

You can also click **Test** on an individual contact point to verify that the integration credentials and configuration are working correctly.

---

## My alert fired but I did not receive a runbook link in the notification

Runbook links are set as an annotation on the alert rule. Edit the rule, scroll to the **Configure notification message** section, and add a **Runbook URL** value.

---

## What does the Pending period do?

The pending period is how long the alert condition must be continuously met before the alert transitions from **Pending** to **Firing**. This prevents notifications for brief, transient spikes.

Setting it to `0s` means the alert fires immediately on the first evaluation where the condition is true. A value of `5m` means the condition must hold for five consecutive minutes before a notification is sent.

---

## Why is my alert in No Data state?

**No Data** means the alert rule's query returned no results during evaluation. Common causes:

- The FusionReactor agent is not sending data for the monitored instance.
- The query label selectors are too specific and match no active series.
- The data source connection is temporarily unavailable.

Review the **No Data** handling option on the rule - **Keep last state** is usually the safest default. See [Troubleshooting](Troubleshooting.md#alert-is-in-no-data-state) for more detail.

---

## How do I prevent an alert from repeatedly firing and recovering?

Enable **Keep firing for** on the alert rule. This holds the alert in a firing state for a defined period after the condition resolves, preventing noisy recovered/re-fired cycles for metrics that fluctuate around the threshold.

Increasing the **Pending period** also helps - a longer pending period requires the condition to be stable before firing.

---

## What happens to alerts that don't match any notification policy?

They are handled by the **Default policy**, which acts as a safety net. Configure the Default policy to point to a catch-all [contact point](Contact-points.md) (such as, a general-purpose email or Slack channel) to ensure no alert is silently dropped.
