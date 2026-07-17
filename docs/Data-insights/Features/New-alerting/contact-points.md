# Contact Points

A **contact point** answers one question: who gets told, and how? Set one up once - email, Slack, PagerDuty, webhook - and any alert you send to it lands in the right place. Each contact point contains one or more integrations and can be assigned directly to an alert rule or routed via a [notification policy](notification-policy.md).

Navigate to **Alerting > Notifications** and open the **Contact Points** tab to view and manage your contact points.

!!! note "Contact points vs OpsPilot integrations"
    Contact points are used **only for sending outbound alert notifications**. They are distinct from [OpsPilot integrations](../integrations.md), which let OpsPilot read information **inbound** from third-party sources for investigation and analysis.

## The contact points list

The list shows all configured contact points with three columns:

| Column | Description |
|---|---|
| **Name** | The contact point name |
| **Type** | The integration type (Email, Slack, Webhook, etc.) |
| **Usage** | Whether the contact point is in use by a notification policy or alert rule |
| **Actions** | Edit (pencil) or delete (bin) the contact point |

Use **Search contact points** to find one by name. Use the **type filter** dropdown to show only contact points of a specific type.

## Supported types

| Type | Description |
|---|---|
| **Slack** | Post notifications to a Slack channel |
| **Discord** | Post notifications to a Discord channel |
| **Microsoft Teams** | Send notifications to a Teams channel |
| **Telegram** | Send notifications via Telegram |
| **Google Chat** | Post notifications to Google Chat |
| **PagerDuty** | Create incidents in PagerDuty |
| **OpsGenie** | Create alerts in OpsGenie |
| **Pushover** | Send push notifications via Pushover |
| **Webhook** | POST a JSON payload to any URL |
| **Email** | Send notifications by email |
| **Kafka REST Proxy** | Publish notifications to a Kafka topic |

## Adding a contact point

1. Click **+ New contact point** to open the integration picker
2. Select an integration type from the grid. Use the category tabs to filter:

| Category | Integrations |
|---|---|
| **Chat** | Slack, Discord, Microsoft Teams, Telegram, Google Chat |
| **On-call** | PagerDuty, OpsGenie, Pushover |
| **Webhook** | Webhook |
| **Other** | Email, Kafka REST Proxy |

3. Fill in the required fields for the integration (such as, recipient addresses for Email, or a webhook URL for Slack)
4. Enter a unique, descriptive **Name** for the contact point
5. Click **Save contact point**

!!! note
    Credentials (webhook URLs, API keys) are encrypted at rest and never shown in the UI after saving.

### Adding multiple destinations

A single contact point can send to multiple places at once (such as, Email and Slack simultaneously):

1. While creating or editing a contact point, click **+ Add contact point integration**
2. Select a new integration type and fill in the required details
3. Click **Save contact point**

## Editing a contact point

To change an existing contact point:

1. Find it in the contact points list and click the **edit** (pencil) icon
2. Update any integration fields, rename the contact point, or add and remove destinations with **+ Add contact point integration**
3. Click **Save contact point**

Changes take effect immediately and apply everywhere the contact point is used - across every alert rule and notification policy referencing it.

!!! note
    A contact point that is in use (shown in the **Usage** column) cannot be deleted until it is removed from all notification policies and alert rules that reference it.

## Notification templates

Templates let you define reusable message formats instead of writing custom messages for every alert rule. See [Notification templates](../Alerting/Templates.md) for full details.

!!! info "Learn more"
    [Configure Contact Points](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/)
