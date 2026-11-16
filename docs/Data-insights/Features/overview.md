# Overview

The **Overview** page summarizes your whole environment at a glance - integrations, services, servers, applications, alerts, and anomaly detection.

## Active account view

![!Screenshot](../../images/active-account.png)

Once data is flowing, the Overview shows a full summary across several columns. Each panel has a header with a collapse control, its title, an arrow to the full view, and a status label (such as **Health**, **Live**, or **Last 1 hour**). Panel positions follow your [layout](#customizing-your-dashboard). A **time picker** in the top right sets the range for panels marked **Uses time picker**.

## Customizing your dashboard

Click the **My dashboard** icon (top right) to control which panels show and in what order. Each panel has two controls:

- **Visibility** - tick or untick to show or hide it.
- **Pin** - keep it at the top (see [Pinning panels](#pinning-panels)).

The list covers the core panels - **Coworker**, **Integrations**, **Services**, **Servers**, **Applications**, **Alerts**, **Service Anomaly Detection**, **Custom Anomaly Detection**, and **Incidents** - plus one per installed integration, named after its dashboard folder (for example **AWS · Database**).

**Reset to org defaults** restores the default layout.

### Pinning panels

Panels are ordered automatically - anything **warning** or **erroring** floats to the top. **Pinning** overrides that: a pinned panel always sits above the rest.

Pin at two levels:

- **Organization** - the default everyone in the org sees.
- **User** - your own overrides on top.

Pinning an **integration** panel also adds its **dashboard folder** to the left-hand nav under [Dashboards](Dashboards/about-dashboards.md), one click from its dashboards.

## Panels

Each panel summarizes one part of your environment. Pin or hide any from [My dashboard](#customizing-your-dashboard).

### Integrations

Shows the health of your installed integrations with a **Health** label, color-coded by worst state. A banner summarizes how many **need attention** and how many are **not sending data**. Each integration shows a status dot - green for **Healthy**, amber for **Not sending data** (with a **Check the install notes →** link). **Show more** and **Show less** expand the list.

Click **Integrations →** for the full [Integrations](/Data-insights/Features/integrations/) view.

### Coworker

A **Live** summary of your AI teammate's activity. The header counts what Coworker is **watching** and **investigating**.

**Situations** are grouped by severity - a **Critical** heading with a count, listing each situation with its severity, affected service, a one-line summary, and how long ago it changed. **Also watching N** is the count of everything else Coworker is monitoring that doesn't need you right now.

An **Investigating** section lists what Coworker is looking into now - the service, what it's investigating (for example *Frontend Call p95 Latency*), and the kind of check (such as a **Health screen**).

Click a situation to open it, or **Coworker →** for the full dashboard.

### Services

Key metrics across all monitored services for the last hour, as stat cards showing each metric's current value. The **Show min, avg and max** control in the header expands the cards to add **MIN**, **AVG**, and **MAX** (count-based cards - **Errors**, **Throughput** - show **SUM**, **AVG**, **MAX**):

- **Service names** - the services included, with a count and a sample of names
- **Services** - total number of monitored services
- **Latency** - average request latency
- **P95** / **P99** - 95th / 99th percentile latency
- **Errors**
- **Throughput**

#### Services by latency

**Services by latency** ranks your top 10 services by average latency. Each card shows **Latency**, **P95 / P99**, **Errors**, and **Throughput**. Click one to drill into its detailed data.

### Servers

A summary of all servers running a FusionReactor agent, as stat cards with the same **Show min, avg and max** toggle (count-based cards show **SUM**, **AVG**, **MAX**):

- **Server names** - the servers included, with a count and a sample of names
- **Servers** - total number of servers
- **Request Duration**
- **Errors**
- **Throughput**
- **CPU Usage**
- **Memory Usage**

#### Servers by latency

Ranks servers by average latency; each card shows **Request Duration**, **Errors**, **Throughput**, **CPU**, and **Memory**.

Click **Servers ->** for the full [Servers](/Data-insights/Features/Servers/overview/) view.

### Applications

A summary of all monitored applications, as stat cards with the same **Show min, avg and max** toggle (count-based cards show **SUM**, **AVG**, **MAX**):

- **Application names** - the applications included, with a count and a sample of names
- **Applications** - total number of applications
- **Request Duration**
- **Errors**
- **Throughput**

#### Applications by latency

Ranks applications by average latency; each card shows **Request Duration**, **Errors**, and **Throughput**.

Click **Applications ->** for the full [Applications](/Data-insights/Features/applications/) view.

### Integration and runtime panels

Each installed integration can add its own panel - for example a **.NET** runtime-metrics panel, or a database integration's dashboard folder. They follow the time picker (**Uses time picker**) and show the integration's key stat cards. Pin or hide them from [My dashboard](#customizing-your-dashboard).

### Panel anomaly detectors

The metric panels - **Services**, **Servers**, **Applications**, and integration panels - can run an **anomaly detector** per metric. A panel with none on reads **Anomaly detectors off**, with a **Choose detectors to switch on** link. That opens the list: each metric (for example **Latency**, **P95**, **P99**, **Errors/s**, **Throughput**) has a toggle, reading **Off** until enabled and then showing its state - **Normal** or **Pending**.

A detector does nothing until switched on, then needs a **warm-up period** to learn before it can alert. You enable detectors per metric (bulk enabling is coming).

Once on, the panel header reflects it - for example **2 pending** (*P99 pending · Errors/s pending*) - and a breaching detector shows a **firing** count.

### Alerts

A **Live** panel that reads **All clear** when nothing is firing (for example *1 of 124 rules normal*). When alerts fire it leads with the **firing** count and lists them - each with the alert name, how long it's been firing, and its rule group (for example *OpsPilot Rules*). A muted-bell icon marks a silenced alert.

**Open in Alerting** links to the full view, with a breakdown by state:

| State | Description |
|---|---|
| **Firing** | Alerts currently breaching their threshold |
| **Can't evaluate** | Rules that could not be evaluated |
| **Pending** | Alerts that have triggered but are not yet confirmed |
| **Normal** | Rules currently within threshold |
| **No data** | Rules with no data to evaluate against |
| **Paused** | Rules that are not currently evaluating |

Click **Alerts →** for the full [Alerting Status](/Data-insights/Features/New-alerting/status/) view.

### Service Anomaly Detection

A **Live** panel for the detectors OpsPilot maintains for your services. It reads **All clear** when none are active (for example *30 of 36 detectors normal*), and otherwise lists the firing and **pending** anomalies - each with its detector, service, and how long it's been pending - above a breakdown by state (**pending**, **normal**, **no data**, **paused**).

Click **Service Anomaly Detection ->** for the full [Anomaly Detection](/Data-insights/Features/New-alerting/service-anomaly-detectors/) view.

### Custom Anomaly Detection

The same for the custom detectors you've defined. It reads **All clear** when none are active, and otherwise lists any firing or **pending** anomalies (for example *go_cpu · pending for 2m*) above the same breakdown.

Click **Custom Anomaly Detection ->** for the full [Custom detectors](/Data-insights/Features/New-alerting/custom-anomaly-detectors/) view.

### Incidents

Tracks your open incidents. Before incidents are set up it shows a **Declare an incident** prompt with **Incident settings** and **Open incidents** buttons. Once configured, it reads **No open incidents** when there are none, and otherwise breaks them down by state - **Triage**, **Investigating**, **Mitigated** - listing each with its title, severity (such as **SEV-2**), and how long ago it was raised.

Click **Incidents ->** for the full [Incidents](/Data-insights/Features/Incidents/overview/) view.

## News

The **News** page is OpsPilot's feed of product announcements. The latest surfaces as a prompt at the top of the Overview that links to the full feed; the prompt changes each release. Each announcement is a card with its **date**, **title**, a short summary, and a **Read more** link.

## No Data view

With no data yet, each section shows a **Get Started** prompt:

| Section | Prompt |
|---|---|
| **Services** | You'll need an API key to instrument your application with OpenTelemetry. |
| **Servers** | Install FusionReactor on your servers to start monitoring. You'll need a license key. |
| **Applications** | Install FusionReactor to monitor your applications. You'll need a license key. |
| **Coworker** | Set up your AI Coworker to investigate alerts and track ongoing situations. |
| **Alerts** | Configure alert rules to monitor your infrastructure. |
| **Anomaly Detection** | Enable anomaly detection to spot unusual behavior in your data. |

The **Servers** and **Applications** prompts also show your **OpsPilot license key** to copy during agent installation. Once data flows in, the Overview populates automatically.

!!! tip "Getting started"
    Follow the prompts to install the right agent or instrumentation for your stack, then return to the Overview to see your data.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
