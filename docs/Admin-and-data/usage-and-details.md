# Usage & Details

The **Usage & Details** page gives you a real-time view of your subscription, current ingest usage, and upcoming bill — all in one place.

## Subscription

The **Subscription** panel shows the key details of your current plan:

| Field | Description |
|---|---|
| **Plan** | Your current subscription tier (e.g. Trial, Starter, Pro, Advanced) |
| **Interval** | Whether your plan is billed monthly or annually |
| **Status** | Current subscription status (e.g. active, expired) |
| **Renews At** | The date your subscription next renews |
| **Bills At** | The date your next invoice will be generated |
| **Ultimate Seats** | Number of FusionReactor Ultimate on-premise seats |
| **Developer Seats** | Number of FusionReactor Developer on-premise seats |
| **Shipping** | Whether Metric Shipping is included on your plan. Click the gear icon to configure the shipping endpoint in **Preferences**. |

The following actions are available from the Subscription panel:

| Icon | Action |
|---|---|
| Key | **View Licenses** — view your license keys |
| Gear | **Manage Subscription** — update your plan or seats |
| Red cancel | **Cancel Subscription** — cancel your current subscription |

## Usage

The **Usage** panel shows your current consumption against your plan limits for the active billing period:

| Signal | Description |
|---|---|
| **Agents — Ultimate** | FusionReactor Ultimate agent hours consumed vs allowance |
| **Agents — Developer** | FusionReactor Developer agent hours consumed vs allowance |
| **Metrics** | Number of active metric series vs allowance |
| **Logs** | Volume of log data ingested vs allowance |
| **Traces** | Volume of trace data ingested vs allowance |
| **AI Tokens** | OpsPilot AI tokens consumed vs allowance |

A progress bar shows the percentage of your allowance used. Each signal also shows a **Forecast** — a projection of your total usage by the end of the current pay period based on your current consumption rate. This helps you anticipate overages before they happen.

If you exceed your plan limit, on-demand billing applies for the overage.

!!! info "Learn more"
    [On-demand usage costs](/Admin-and-data/Billing/Cloud/overview/#on-demand-usage-costs)

## Upcoming bill

The **Upcoming bill** panel shows a forecast of your next invoice:

| Field | Description |
|---|---|
| **Amount due** | Total amount due on the next billing date |
| **Next billing date** | The date your next invoice will be generated |
| **Subtotal** | Charges before VAT |
| **VAT** | VAT applied to your subscription |
| **Total** | Total charges including VAT |
| **Credit** | Any credits applied to your account |

Expand **Bill Summary** to see a breakdown of charges by component.

!!! info "Metric Shipping"
    If Metric Shipping is included on your plan, click the gear icon next to **Shipping** to configure your shipping endpoint. See [Preferences](/Admin-and-data/preferences/) for full details.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
