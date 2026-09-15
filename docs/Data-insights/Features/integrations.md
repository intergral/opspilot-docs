# Integrations Hub

![Integrations hub](../../images/integrations.png)

Browse the integration catalog and what you've installed. The **Integrations** page lets you connect external tools and services to your OpsPilot workspace.

Navigate to **Integrations** from the left-hand sidebar to browse and manage all available integrations.

---

## Browsing integrations

Integrations are grouped into categories, each showing how many it holds. Use the filter tabs at the top of the page to narrow the list:

| Tab | Description |
|---|---|
| **All** | Shows every integration |
| **Chat** | Messaging and notification tools |
| **Cloud** | Cloud platform providers |
| **Data** | Databases and data streaming services |
| **Infrastructure** | Infrastructure and orchestration tools |
| **Networking** | Service mesh and proxy tools |
| **Observability** | Third-party monitoring and observability platforms |
| **SDKs** | Language SDKs |
| **Ticketing** | Issue tracking and project management tools |

Use the **Search integrations** bar to find one by name, and the status dropdown beside it to filter by whether an integration is installed. The **Legacy** toggle in the top right switches to the previous catalog view.

Each card shows the integration's name, its category, a short description, and its current status - **Coming soon** for one not yet released, or **Installed** for one already connected.

## Installing an integration

Click **Install** on any available integration's card to connect it. Once connected, the card shows an **Installed** badge and the button changes to **Uninstall**. Slack has its own **Add to Slack** button, which starts the Slack authorisation flow.

---

## Available now

<div class="grid cards" markdown>

-   :material-robot-outline: **OpsPilot MCP** - Chat

    ---

    Let AI assistants query OpsPilot over the Model Context Protocol.

-   :material-chat-outline: **[Slack](Integrations/Chat/slack.md)** - Chat

    ---

    Talk to OpsPilot from Slack - mention it in a channel or DM it directly.

-   :material-cloud-outline: **AWS** - Cloud

    ---

    Connect AWS for EC2, RDS, and other CloudWatch-held metrics.

-   :material-code-tags: **OpenTrace** - Data

    ---

    Connect OpenTrace so OpsPilot can read your code alongside your telemetry.

</div>

### SDKs

Each SDK instruments your applications with OpenTelemetry for metrics, traces, and logs.

<div class="grid cards" markdown>

-   :material-language-go: **Go**

    ---

    [OpenTelemetry instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Go/)

-   :material-dot-net: **.NET**

    ---

    [OpenTelemetry instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/DotNet/)

-   :material-language-java: **Java**

    ---

    Instruments Java and JVM applications. [OpenTelemetry instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Java/)

-   :material-nodejs: **Node.js**

    ---

    [OpenTelemetry instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/node/)

-   :material-language-python: **Python**

    ---

    [OpenTelemetry instrumentation](/Monitor-your-data/OpenTelemetry/Instrumentation/Python/)

</div>

---

## Coming soon

<div class="grid cards" markdown>

-   :material-chat-outline: **Chat**

    ---

    Discord · MS Teams

-   :material-ticket-outline: **Ticketing**

    ---

    Jira · Linear · Notion

-   :material-cloud-outline: **Cloud**

    ---

    Azure · Google Cloud

-   :material-database-outline: **Data**

    ---

    Altinity ClickHouse Operator · Kafka · MongoDB · MySQL · PostgreSQL · RabbitMQ · Redis · Strimzi Kafka · TigerData

-   :material-server-network: **Infrastructure**

    ---

    ArgoCD · Host Metrics · KEDA · Kubernetes · Terraform · Unix · Windows

-   :material-lan: **Networking**

    ---

    Cilium · Istio · Linkerd · NGINX · Traefik

-   :material-chart-line: **Observability**

    ---

    AppDynamics · Dash0 · Datadog · Grafana · Loki · Mimir · New Relic · Sentry · Tempo

-   :material-code-braces: **SDKs**

    ---

    Browser · C++ · Erlang · PHP · Ruby · Rust · Swift

</div>

---

!!! info "FusionReactor"
    The [FusionReactor agent](Integrations/SDKs/fusionreactor.md) is installed separately rather than from this catalog. It gives deep visibility into ColdFusion, Java, and Lucee applications with no code changes.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
