# Billing FAQ

## How is usage calculated?

Different data types are calculated differently each billing period:

| Data type | Method |
| --- | --- |
| **Metrics** | Mean average over the billing period |
| **Logs** | Sum of all data ingested |
| **Traces** | Sum of all data ingested |
| **OpsPilot tokens** | Sum of all tokens used |
| **FR hours** | Sum of all instance hours |

## Why is my bill higher than expected?

The most common causes are:

- **Metrics cardinality** — A spike in unique metric series (e.g. a deployment creating many new label combinations) can push your mean average up.
- **Log volume** — Verbose log levels (DEBUG, TRACE) generate significantly more data than INFO or WARN.
- **Trace volume** — A high-traffic application with 100% sampling will ingest traces rapidly.
- **AI token usage** — Long, multi-turn OpsPilot AI conversations consume tokens quickly as previous context is included in each request.

Use the [Billing usage dashboard](/Admin-and-data/Billing/Cloud/overview/#billing-usage) for a full breakdown of where costs are coming from.

## How do I reduce costs?

### FusionReactor agent

Reduce the trace sampling ratio using the JVM property:

```
-Dfr.observability.trace.sampling.ratio=0.03
```

Common values:

| Ratio | Sampling rate | Recommended for |
| --- | --- | --- |
| `1.0` | 100% | Development / critical services |
| `0.1` | 10% | Standard production |
| `0.05` | 5% | Default |
| `0.03` | 3% | High-volume applications |
| `0.01` | 1% | Very high-volume, cost-sensitive |

### Grafana Alloy / OTel collector

Optimize at the collector level:

- **Traces** — Configure a [tail sampling processor](https://grafana.com/docs/alloy/latest/) to drop low-value spans.
- **Logs** — Add a filter stage to drop DEBUG/TRACE log levels or noisy sources before they are sent.
- **Metrics** — Increase scrape intervals or use relabelling to drop unused metric series.

### OpsPilot AI tokens

- Keep queries focused and concise — long conversations accumulate context quickly.
- Start a new conversation rather than extending a very long one.

## What happens when I exceed my plan limits?

Usage beyond your plan's included allowance is billed at [on-demand rates](/Admin-and-data/Billing/Cloud/overview/#on-demand-usage-costs). There is no hard cutoff — data continues to be ingested and you are charged for the overage at the end of the billing period.

## How do I set up a billing alert?

You can create an alert using the billing usage metrics to notify you before you exceed your allowance:

- `fr_billing_usage_current`
- `fr_billing_charges_metered`
- `fr_billing_usage`
- `fr_billing_charges_total`

!!! info "Learn more"
    [Create an alert](/Admin-and-data/Billing/Cloud/overview/#create-an-alert)

## What is the difference between annual and monthly pricing?

The annual plan is approximately 20% less expensive than monthly. Both are billed monthly, but the annual plan requires a 12-month commitment.

## What counts as a seat?

A seat covers a single unique virtual or physical host with up to 4 instances of Java/ColdFusion installed, or up to 4 Docker containers.

!!! example
    5–8 instances on a host requires 2 seats.

## How do I upgrade or downgrade my plan?

Upgrades take effect immediately. Downgrades take effect at the end of the current billing period.

Manage your plan from **Administration** > **Billing** in the OpsPilot Portal.

## When am I charged?

Both annual and monthly plan usage is calculated and billed each month.

## How do I cancel?

Contact support via the chat bubble in the OpsPilot Portal.

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
