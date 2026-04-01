This page covers common issues when setting up and operating OpsPilot alerting, with particular focus on the differences from the previous Mimir-based alerting system.

## Quick reference

| Symptom | Most likely cause | Jump to |
| --- | --- | --- |
| Alert is stuck in **Pending** | Pending period not yet elapsed | [Alert stuck in Pending](#alert-is-stuck-in-pending) |
| Alert fires but **no notification received** | Missing `channel` label or misconfigured policy | [No notifications received](#no-notifications-received) |
| Notifications going to **Default policy** | `channel` label missing or not matching any policy | [Alerts routing to Default policy](#alerts-routing-to-the-default-policy) |
| Alert in **No Data** state | Query returning no results | [Alert is in No Data state](#alert-is-in-no-data-state) |
| Alert is **flapping** (firing/recovering rapidly) | Pending period too short or metric is unstable | [Alert is flapping](#alert-is-flapping) |
| **Too many notifications** | Repeat interval or grouping not configured | [Receiving too many notifications](#receiving-too-many-notifications) |
| Contact point **test succeeds but no alerts arrive** | Alert not matching the policy for that contact point | [Contact point test works but alerts don't arrive](#contact-point-test-works-but-alerts-dont-arrive) |
| Alert rule **fails to save** | Missing folder or evaluation group | [Alert rule fails to save](#alert-rule-fails-to-save) |

---

## Alert is stuck in Pending

**Symptom:** The alert rule shows a **Pending** state but never transitions to **Firing**, even though the condition appears to be met.

**Cause:** The **Pending period** defines how long the condition must be continuously true before the alert fires. If the condition resolves before that period elapses, the alert resets to Normal.

**Fix:**

- Navigate to the rule and check the **Pending period** value under **Set evaluation behaviour**.
- If you want the alert to fire immediately, set the pending period to `0s`.
- If the metric is intermittently crossing the threshold, consider whether the pending period is appropriate or whether the condition itself needs adjusting.

---

## No notifications received

**Symptom:** The alert is in a **Firing** state in the UI, but no notification is delivered to your contact point.

**Causes and fixes:**

1. **Missing `channel` label on the alert rule**
    - The alert falls through to the Default policy. If the Default policy contact point is not configured, no notification is sent.
    - Fix: Edit the alert rule and add a `channel` label (such as, `channel=slack`). See [Configure Alert Rules](Alert-Rules/Configure-rules.md#4-add-routing-labels).

2. **No matching child policy**
    - Check that a notification policy exists with a matcher for the `channel` label value you used.
    - Fix: Navigate to **Alerting** > **Notification policies** and verify the policy matcher (such as, `channel =~ .*slack.*`).

3. **Contact point misconfigured**
    - The policy is matching but the integration is failing.
    - Fix: Navigate to **Alerting** > **Contact Points**, find the contact point, and click **Test** to verify delivery. Check the credentials and configuration fields.

4. **Silence or mute timing is active**
    - Navigate to **Alerting** > **Firing Alerts** and expand the alert. A **Suppressed** state means a silence or mute timing is blocking the notification.
    - Fix: Check **[Silences](Silences.md)** and **[Time intervals](Mute-timings.md)** for active suppression rules.

---

## Alerts routing to the Default policy

**Symptom:** Alerts are being delivered to the Default policy contact point instead of the expected specific contact point.

**Cause:** The `channel` label on the alert rule either does not exist or does not match any child policy's label matcher.

**Fix:**

1. Open the alert rule and confirm a `channel` label is present with the correct value (such as, `channel=slack`).
2. Navigate to **Alerting** > **Notification policies** and confirm a child policy exists with a matcher like `channel =~ .*slack.*`.
3. Verify the operator is `=~` (regex match) and the regex value is correct - `.*slack.*` will match any label value containing the word "slack".

!!! tip
    You can verify which policy an alert will match by using the **Test** option on the Default policy in **Notification policies**. Enter the label key/value pairs from your alert rule to simulate routing.

---

## Alert is in No Data state

**Symptom:** The alert instance shows **No Data** instead of Normal or Firing.

**Cause:** The alert rule's query returned no results for the evaluation period. This typically happens when:

- The FusionReactor agent is not sending data for the monitored resource.
- The query filters (such as, a label selector `instance="server-01"`) are too specific and no matching series exists.
- The data source connection is temporarily unavailable.

**Fix:**

1. Run the query manually in **Explore** to confirm whether data is being returned.
2. Check the agent or data source connection.
3. Review the **No Data** handling setting on the rule:
    - **Keep last state** is a safe default - the alert will not change state until data resumes.
    - **Alerting** causes the alert to fire when no data is received, which is appropriate for availability monitoring.
    - **Normal** suppresses the alert, which may hide genuine outages.

---

## Alert is flapping

**Symptom:** The alert fires and then immediately resolves, repeatedly, generating a large number of notifications.

**Cause:** The monitored metric is oscillating around the threshold, crossing it on each evaluation cycle.

**Fix:**

1. **Increase the Pending period** - A pending period of `5m` or `10m` requires the condition to be continuously true before firing, smoothing out brief spikes.
2. **Use "Keep firing for"** - This holds the alert in a firing state for a period after the condition resolves, preventing rapid recovered/re-fired cycles.
3. **Adjust the threshold** - If the metric hovers just at the threshold, add a buffer (such as, changing `> 80` to `> 85`).
4. **Increase the Repeat interval** on the [notification policy](Notifications.md) - This reduces re-notification frequency without changing how the rule evaluates.

---

## Receiving too many notifications

**Symptom:** You are receiving many individual notifications for a single event, or the same alert is re-notifying too frequently.

**Fixes:**

1. **Grouping** - Ensure your [notification policy](Notifications.md) has appropriate **Group by** labels (such as, `alertname` or `cluster`). This bundles related alerts into a single notification.
2. **Repeat interval** - Increase the **Repeat interval** on the notification policy (default `4h`). This controls how often a persistently firing alert re-notifies.
3. **Group wait / Group interval** - Increasing these values batches notifications over a longer window before sending.
4. **Flapping metric** - If the alert is repeatedly firing and resolving, see [Alert is flapping](#alert-is-flapping) above.

---

## Contact point test works but alerts don't arrive

**Symptom:** Clicking **Test** on a contact point delivers the test message, but real alerts from firing rules do not arrive.

**Cause:** The contact point is correctly configured, but the notification policy is not routing real alerts to it.

**Fix:**

1. Check that the alert rule has the correct `channel` label.
2. Check that the notification policy matcher (such as, `channel =~ .*slack.*`) matches the label value used on the rule.
3. Navigate to **Alerting** > **Firing Alerts** and expand the firing alert. The **Receivers** field shows which contact point is actually handling the notification.
4. If **Receivers** shows the Default policy or an unexpected contact point, the routing labels are not matching your intended child policy.

---

## Alert rule fails to save

**Symptom:** Clicking **Save rule and exit** produces an error or the rule does not appear in the rule list.

**Common causes:**

1. **No folder selected** - Every alert rule must be placed in a folder. If none exist, click **+ New folder** in the rule editor to create one.
2. **No evaluation group selected** - The rule must belong to an evaluation group. Create a new group if needed and set an evaluation interval (such as, `1m`).
3. **Invalid query** - If the query editor shows an error, the rule cannot be saved. Use the **Preview** button to validate your query before saving.
