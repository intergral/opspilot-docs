# SDK Integrations

The SDK integrations provision runtime dashboards and alert rules for applications instrumented with OpenTelemetry. Install one, instrument your application, and you have runtime monitoring in place without building it yourself.

Navigate to **Integrations** from the left-hand sidebar and open the **SDKs** tab.

---

## What they provision

Each SDK integration installs one runtime dashboard per upstream metric-set version, plus a handful of runtime alert rules.

| SDK | Dashboards | Alert rules | Instrumentation |
|---|---|---|---|
| Java | 26 | 4 | [Java](/Monitor-your-data/OpenTelemetry/Instrumentation/Java/) |
| .NET | 8 | 4 | [.NET](/Monitor-your-data/OpenTelemetry/Instrumentation/DotNet/) |
| Go | 6 | 4 | [Go](/Monitor-your-data/OpenTelemetry/Instrumentation/Go/) |
| Node.js | 9 | 3 | [Node.js](/Monitor-your-data/OpenTelemetry/Instrumentation/node/) |
| Python | 5 | 5 | [Python](/Monitor-your-data/OpenTelemetry/Instrumentation/Python/) |

The dashboard counts differ because each covers that language's full range of upstream metric-set versions. Java's 26 span thirteen Java-agent eras from v0.11.0 and thirteen semantic-convention sets from 1.9.0.

---

## Alerts ship paused

The alert rules are installed **paused**. You opt in per rule rather than being alerted on everything from the moment you install, and once you enable a rule that choice persists across integration upgrades.

Each SDK's rules sit in their own alert group, named after the language - `java_runtime_alerts` and `dotnet_runtime_alerts`, for example.

Every threshold is either scale-free or derived from the runtime itself, so the same rules apply unchanged whatever the size of your service. Go's four rules, for instance, cover heap usage against `GOMEMLIMIT`, goroutine count, GC pause overhead, and scheduler latency.

---

## Dashboards and data sources

Provisioned dashboards are tagged `integration` along with a tag for the language, such as `go`, so you can find everything an integration added.

The SDK integrations bind to your account's existing shared metrics data source rather than creating their own, so you keep a single Prometheus source for all metrics. That source is adopted, not owned - uninstalling the integration leaves it in place.

---

## Installing

SDK integrations run **Read-only**, which is the default and requires nothing: the metrics endpoint and signing key come from the service environment. There is no configuration to complete during the install itself.

Once installed, the **Installation guide** tab on the integration's detail view walks through instrumenting your application and points you to the dashboard to open. See [Integrations](../../integrations.md) for the install flow and how to manage an installation afterwards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
