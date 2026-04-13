# Preferences

The **Preferences** page lets you control which data types are ingested into your OpsPilot account and configure metric shipping to third-party providers.

Navigate to **Administration** > **Preferences** to access these settings.

## Signals

The **Signals** section controls which OpenTelemetry signal types are ingested into your OpsPilot account. This applies to all incoming data regardless of source (FusionReactor agent, Grafana Alloy, OTel collector, etc.). Disabling a signal type will block all incoming data of that type from being collected or stored.

| Signal | Description |
|---|---|
| **Logs** | Enable or disable log ingestion |
| **Metrics** | Enable or disable metric ingestion |
| **Traces** | Enable or disable trace ingestion |
| **AI** | Enable or disable OpsPilot AI |

!!! warning
    Changes may take up to 15 minutes to take effect.

## Shipping

The **Shipping** tab is available if Metric Shipping is included on your plan. It configures where the FusionReactor agent sends its data. By default the agent ships to OpsPilot, but you can configure it to send to any OTel-compatible provider — such as Datadog, Grafana Cloud, or your own OTel collector.

### Simple

Configure a single destination for all signal types:

| Field | Description |
|---|---|
| **Endpoint URL** | The destination URL for your OTel collector (e.g. `https://otel-collector.example.com`) |
| **Protocol** | The transport protocol — **gRPC** or **HTTP** |
| **Headers** (optional) | Any authentication headers required by your collector (e.g. `Authorization=Bearer xxx`) |

### Advanced

Configure a separate destination for each signal type — **Logs**, **Metrics**, and **Traces** can each be sent to a different endpoint. This is useful if you want to route different data types to different providers.

Click **Save** to apply your changes.

!!! info "OTel shipping endpoints"
    For a full list of provider-specific endpoints (Datadog, Grafana Cloud, etc.), see the [FusionReactor OTel shipping configuration](https://docs.fusionreactor.io/Monitor-your-data/FR-Agent/Configuration/OTel-shipping-config/).

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
