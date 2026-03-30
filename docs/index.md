# Get Started with OpsPilot

![Get Started with OpsPilot](images/get-started.png)

From sign-up to your first insights in minutes.

This guide walks you through creating your account, connecting your first data source, and exploring your initial views in OpsPilot.

!!! info "Already have an account?"
    [Sign in](https://app.opspilot.com/auth/login) and head to your dashboard to start exploring your data. If you have an invitation, follow the link in your invitation email to access your organization.

---

## Step 1 — Create Your Account

Navigate to [app.opspilot.com/auth/register](https://app.opspilot.com/auth/register) and sign up. Once signed in, you will be prompted to set up your organization.

!!! tip
    Once signed in, you are prompted to define the name of your organization before proceeding to the dashboard.

---

## Step 2 — Instrument Your Application

Send telemetry from your applications using OpenTelemetry or the FusionReactor agent.

**Running ColdFusion?** Install the [FusionReactor agent](https://docs.fusionreactor.io/Getting-started/install-fr/) to automatically capture metrics, traces, and logs from your CF application — no code changes required.

**All other applications:** Instrument using OpenTelemetry. Use the guide for your language:

| Language | Guide |
|---|---|
| Java | [Java instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Java/) |
| .NET | [.NET instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/DotNet/) |
| Node.js | [Node.js instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/node/) |
| Python | [Python instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Python/) |
| Go | [Go instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Go/) |
| PHP | [PHP instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/PHP/) |
| Ruby | [Ruby instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Ruby/) |
| Other | [All languages](/Monitor-your-data/OpenTelemetry/Instrumentation/Overview/) |

Or deploy an [OpenTelemetry Collector](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) to receive and forward telemetry from your services.



---

## Step 3 — Instrument Your Infrastructure

Connect your infrastructure by installing the integrations you need. OpsPilot supports a wide range of integrations across cloud providers, databases, Kubernetes, and more.

Find setup instructions for your specific stack in the [Integrations Hub](/Data-insights/Features/integrations/).

---

## Step 4 — Query with AI

Once data is flowing, use the **OpsPilot AI assistant** to query your telemetry in plain English. Ask questions like:

- *"Which services had the highest error rate in the last hour?"*
- *"Show me latency trends for the checkout service"*
- *"Are there any anomalies in my infrastructure metrics today?"*

OpsPilot translates your questions into queries across metrics, logs, and traces — no PromQL or LogQL required.

---

## Step 5 — Explore Your Data

Dive deeper into your data using the built-in drilldown tools.

| Where to look | What you'll find | Required integration |
|---|---|---|
| [Servers](/Data-insights/Features/Explore-servers/) | Live and historic server health | FusionReactor agent |
| [Applications](/Data-insights/Features/applications/) | Request rates, errors, and latency | FusionReactor agent |
| [Dashboards](/Data-insights/Features/dashboards/) | Pre-built and custom visualizations | Any |
| [Metrics Drilldown](/Data-insights/Features/explore-metrics/) | Explore Prometheus metrics without PromQL | OpenTelemetry / Prometheus |
| [Logs Drilldown](/Data-insights/Features/explore-logs/) | Filter and analyze logs without LogQL | OpenTelemetry / Loki |
| [Traces Drilldown](/Data-insights/Features/explore-traces/) | Trace requests across services | OpenTelemetry |
| [Alerts](/Data-insights/Features/Alerting/Alerts-overview/) | Set up rules and get notified | Any |

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
