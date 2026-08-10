# Coworker

Coworker is the connective layer that binds your observability data, alerting, service knowledge, and incident response into one place. Rather than switching between dashboards, alert feeds, and runbooks, you get a single AI SRE teammate that watches your systems, investigates what it finds, and hands you a clear, prioritised picture of what needs attention - so your team spends less time fighting tools and more time fixing problems.

Each user gets their own personalised Coworker that learns what's relevant to them. It talks to you in the first person, remembers context, and keeps working between your visits.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1215757524?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="OpsPilot Coworker"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## How to think about it

Think of Coworker as a single teammate rather than a monitoring tool. Behind that one voice it is doing several jobs at once: watching for signals, investigating them, writing down what it finds, and deciding what to tell you. You don't need to think about those internal jobs. You just get one Coworker who keeps you informed.

Coworker also shows you what it cannot see. Coverage gaps in your telemetry, unconnected alert rules, uncatalogued services - these surface in your feed so you know exactly what to fix to make Coworker more effective. The onboarding experience is not just setup; it is a diagnostic that tells you where your observability has blind spots.

## What Coworker does

| Capability | Description |
|---|---|
| **Insights** | The core of Coworker - atomic findings written every time Coworker investigates something, forming the foundation for everything it surfaces |
| **[Situations](situations.md)** | Insights grouped into coherent stories with severity, evidence, and recommended actions - the thing you triage |
| **Continuous monitoring** | Watches your systems around the clock and re-investigates open situations on a regular cadence |
| **[Heartbeat](heartbeat.md)** | An always-on health screen that watches each catalogued service against learned baselines and investigates sustained deviations on its own - no alert rules required |
| **Alert response** | Automatically investigates firing alerts and posts one clean situation instead of a stream of raw alert noise |
| **[Tasks](tasks.md)** | Scheduled, monitoring, and webhook-driven jobs that run recurring analysis and report back proactively |
| **[Memory](knowledge.md)** | Builds a growing understanding of your systems, your team, and your preferences over time |
| **Cost management** | Allowance tracking and optimisation suggestions to keep AI Token spend under control |

New here? [Getting started](getting-started.md) walks through onboarding. See [Situations](situations.md) for how findings surface in your feed and how to triage them.

---

## Memory

Coworker gets smarter over time. Everything it does - investigating alerts, running tasks, talking to you - builds memory that carries forward into every future investigation.

Click the **Knowledge** button on the dashboard to explore what Coworker has learned. See [Knowledge](knowledge.md) for full details.

---

## Settings

Click the settings icon on the Coworker dashboard to open the Settings modal. See [Settings](Settings/overview.md) for full details on your preferences, check-in cadence, behavior, and budget controls.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
