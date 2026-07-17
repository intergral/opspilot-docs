# Contact Points

A **contact point** answers one question: who gets told, and how? Set one up once - email, Slack, PagerDuty, webhook - and any alert you send to it lands in the right place. Each contact point contains one or more integrations and can be assigned directly to an alert rule or routed via a [notification policy](notification-policy.md).

Navigate to **Alerting > Contact Points** to view and manage your contact points.

## The contact points list

The list shows all configured contact points with three columns:

| Column | Description |
|---|---|
| **Name** | The contact point name |
| **Type** | The integration type (Email, Slack, Webhook, etc.) |
| **Usage** | Whether the contact point is in use by a notification policy or alert rule |

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

## Notification templates

Templates let you define reusable message formats instead of writing custom messages for every alert rule. See [Notification templates](../Alerting/Templates.md) for full details.

!!! info "Learn more"
    [Configure Contact Points](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/)
