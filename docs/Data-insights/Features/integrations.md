# Integrations Hub

![Integrations hub](../../images/integrations.png)

Browse the integration catalog and what you've installed. The **Integrations** page lets you connect external tools and services to your OpsPilot workspace.

Integrations bring data into OpsPilot from wherever it lives - chat tools, cloud providers, language SDKs, Kubernetes, databases, and more - so you can work with all of it in one place.

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

For most integrations, onboarding is a single click: find it in the catalog and click **Install**. Once connected, the card shows an **Installed** badge and the button changes to **Uninstall**.

Some integrations need more than a click - credentials, endpoints, or other configuration. Where that applies, the steps are built into the UI, so you can work through them without leaving OpsPilot. Slack, for example, has its own **Add to Slack** button, which starts the Slack authorisation flow.

### What you get

Installing an integration does more than connect a data source. OpsPilot automatically loads a set of default **dashboards** and **alerts** onto your account for that integration, so you have useful monitoring in place from the start with nothing to build by hand.

### The integration detail view

Click any integration to open its detail view - this is where you'll find how to use it. The header shows the integration's name, its **category**, its **version**, and the **Install** button, with the same short description that appears on its catalog card.

Below the header, the detail view is made up of these panels:

| Panel | Description |
|---|---|
| **Overview** | What the integration does and why you'd use it |
| **Permission tiers** | The access levels the integration can run with, what each one requires, and which is applied by **default** |
| **Capabilities** | What the integration declares it can do. Some declare none |
| **Versions** | Each released version, what upgrading from the previous version involves, and a summary of what changed. The current version is marked **latest** |
| **Changelog** | The detail behind each version's changes |

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

!!! question "Don't see the integration you need?"
    If the integration you're looking for isn't in the list, contact support in the chat bubble and let us know which one you need.
