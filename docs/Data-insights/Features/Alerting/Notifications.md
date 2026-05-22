# Notification Policies

Notification policies are the engine of your alerting system, providing a flexible way to route alerts while minimising noise. They are organised in a **tree structure**, starting with a **Default (Root) policy** that can branch into child policies for more specific routing.

## How policies handle alerts

* **Label Matching:** Alerts are routed based on label matchers. Each policy checks the labels on an incoming alert to decide whether to handle it.
* **Hierarchical Routing:** Policies form a tree rather than a flat list. Alerts move through nested levels, inheriting settings from parents or being captured by specific child policies.
* **Alert Grouping:** Policies bundle multiple related alert instances into a single notification before delivering them to the contact point. This reduces alert fatigue.
* **Timing Control:** Policies define precisely when to send notifications, with support for group wait, repeat intervals, and [mute timings](Mute-timings.md).

## Recommended routing setup

The simplest approach - and the one we recommend to get started - is to use a **`channel` label** on your alert rules and match it with a regex policy per destination. This keeps your policy tree flat and makes routing immediately visible on the alert rule itself.

### Step 1 - Create a contact point per destination

Navigate to **Alerting** > **Contact Points** and create one contact point for each notification destination you need (such as, a Slack workspace, an email address, or a webhook endpoint). See [Contact Points](Contact-points.md) for setup instructions.

### Step 2 - Create a child policy per destination

Navigate to **Alerting** > **Notification policies** and add a child policy under the Default policy for each destination:

1. Click **+ New child policy**.
2. Under **Matching labels**, add a matcher:
    * **Label:** `channel`
    * **Operator:** `=~` (regex match)
    * **Value:** `.*slack.*` (or `.*email.*`, `.*webhook.*`)
3. Set the **Contact point** to the corresponding contact point created in Step 1.
4. Click **Save policy**.

The result is a flat set of policies, each routing a specific channel label to its destination:

| Policy matcher | Contact point |
| --- | --- |
| `channel =~ .*email.*` | Email contact point |
| `channel =~ .*slack.*` | Slack contact point |
| `channel =~ .*webhook.*` | Webhook contact point |

### Step 3 - Label your alert rules

When creating an [alert rule](Alert-Rules/Configure-rules.md), add a `channel` label with the value matching the destination you want (such as, `channel=slack`). The matching child policy routes it automatically.

Any alert without a matching `channel` label falls through to the **Default policy**, which acts as a safety net to ensure no alert is silently dropped.

!!! tip
    Using a regex matcher (`=~`) rather than an exact match (`=`) gives you flexibility. A label value of `slack-critical` will still be matched by `.*slack.*`, so you can be more specific on your rules without having to update the policy.

!!! info "Advanced routing"
    For more complex setups - such as nested policy trees, multi-team routing, or routing by severity across multiple destinations simultaneously - see [Notification policies](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/create-notification-policy/) in the Grafana documentation.

## Configuring the Default policy

The **Default policy** handles any alert that does not match a specific child policy. Configure it to point to a catch-all contact point so no alert is silently dropped.

1. Navigate to **Alerting** > **Notification policies**.
2. In the **Default policy** section, click **More** and select **Edit**.
3. Select a **Contact point** for unmatched alerts.
4. In the **Group by** field, choose labels to bundle related alerts (such as, `alertname` or `cluster`).
5. Set your timing preferences:
    * **Group wait:** How long to wait before sending the first notification for a new group (default `30s`).
    * **Group interval:** How long to wait before sending updates for an existing group (default `5m`).
    * **Repeat interval:** How long to wait before re-sending the same firing alert (default `4h`).
6. Click **Save**.

## Key routing concepts

* **Label matching:** An alert only enters a policy if all of the policy's label matchers are satisfied.
* **Top-to-bottom evaluation:** Policies are checked from top to bottom. Once a match is found, the system moves into that policy's children. Sibling policies below a match are skipped unless **Continue matching** is enabled.
* **Continue matching:** Enabling this on a policy allows one alert to match multiple policies at the same level, triggering notifications to multiple destinations simultaneously.
* **Inheritance:** A child policy with no contact point set inherits the parent's contact point.

!!! info "Learn more"
    [Notification policies](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/create-notification-policy/)
