# Coworker

Coworker is the connective layer that binds your observability data, alerting, service knowledge, and incident response into one place. Rather than switching between dashboards, alert feeds, and runbooks, you get a single AI SRE teammate that watches your systems, investigates what it finds, and hands you a clear, prioritised picture of what needs attention - so your team spends less time fighting tools and more time fixing problems.

Each user gets their own personalised Coworker that learns what's relevant to them. It talks to you in the first person, remembers context, and keeps working between your visits.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1215757524?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="OpsPilot Coworker"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## OpsPilot and Coworker

The two names describe different halves of the same product:

- **OpsPilot** is the platform - where your metrics, logs, traces, alerts, dashboards, and service catalog live.
- **Coworker** is the AI working on top of it - the part that watches that data, investigates what it finds, and tells you about it.

The split is a useful one when you are deciding where to look. Storing, querying, and visualizing your data is OpsPilot. Reasoning about it is Coworker.

What Coworker can reason about depends on what is connected. Installing an [integration](../../integrations.md) widens its view - adding Windows, database, or cloud metrics gives it more to correlate the next time it investigates.

## How to think about it

Think of Coworker as a single teammate rather than a monitoring tool. Behind that one voice it is doing several jobs at once: watching for signals, investigating them, writing down what it finds, and deciding what to tell you. You don't need to think about those internal jobs. You just get one Coworker who keeps you informed.

Coworker also shows you what it cannot see. Coverage gaps in your telemetry, unconnected alert rules, uncataloged services - these surface in your feed so you know exactly what to fix to make Coworker more effective. The onboarding experience is not just setup; it is a diagnostic that tells you where your observability has blind spots.

## The dashboard

Coworker opens on its dashboard, which is also where you land when you log in. The left side is what Coworker has been doing; the right is the [chat](chat.md).

**Just for me** at the top filters what you see to your own slice of the organisation. Switch to the broader view when you are on call or covering someone else - see [How the feed adapts](situations.md#how-the-feed-adapts).

| Panel | What it holds |
|---|---|
| **Your standup** | A short summary of what matters right now, written by Coworker in its own words. It names the situation it is most concerned about and offers follow-ups you can click - jumping straight to that situation, or asking what to change and why earlier episodes closed. The panel says when it was last written, and you can rewrite it on demand with the refresh icon |
| **Situations** | The situations currently open, with their severity and the service they affect. See [Situations](situations.md) |
| **Help me see more** | Gaps in what Coworker can see - a service that has stopped shipping traces, telemetry it expected and is not getting. These are worth fixing first, because everything else Coworker does depends on what reaches it |
| **Recent activity** | What Coworker handled without involving you: checks it ran on its own, and findings it recorded without raising a situation. **Summarize** asks it to sum that up for you |
| **Tasks** | Your [Heartbeat](heartbeat.md), [event sources](event-sources.md) and [scheduled tasks](scheduled.md), each showing when it next runs or how long it has been quiet |

The standup is rewritten on a cadence you set in [Settings > Background activity](Settings/overview.md).

!!! tip "Findings are not situations"
    **Recent activity** often shows a large number of findings not tied to a situation - that is Coworker working as intended. It investigates far more than it reports, and records what turned out not to matter rather than interrupting you with it. See [Why does Coworker raise so few situations?](faq.md#why-does-coworker-raise-so-few-situations)

## What Coworker does

| Capability | Description |
|---|---|
| [**Insights**](insights.md) | The core of Coworker - atomic findings written every time Coworker investigates something, forming the foundation for everything it surfaces |
| **[Situations](situations.md)** | Insights grouped into coherent stories with severity, evidence, and recommended actions - the thing you triage |
| **Continuous monitoring** | Watches your systems around the clock and re-investigates open situations on a regular cadence |
| **[Heartbeat](heartbeat.md)** | An always-on health screen that watches each cataloged service against learned baselines and investigates sustained deviations on its own - no alert rules required |
| **Alert response** | Automatically investigates firing alerts and posts one clean situation instead of a stream of raw alert noise |
| **[Tasks](tasks.md)** | Scheduled, monitoring, and webhook-driven jobs that run recurring analysis and report back proactively |
| **[Memory](knowledge.md)** | Builds a growing understanding of your systems, your team, and your preferences over time |
| **[Cost management](usage.md)** | Allowance tracking and optimisation suggestions to keep AI Token spend under control |

New here? [Getting started](getting-started.md) walks through onboarding. See [Situations](situations.md) for how findings surface in your feed and how to triage them.

## Where you can reach it

Coworker is not confined to the OpsPilot UI:

| Where | What you get |
|---|---|
| **The platform** | The Coworker dashboard, and the Coworker buttons throughout the UI |
| **[Slack](../../Integrations/Chat/slack.md)** | The same Coworker you use in the app. Mention it in a channel or message it directly, and the alerts, situations, and digests it surfaces land there as they happen |
| **[OpsPilot MCP](../../Integrations/Chat/opspilot-mcp.md)** | Your own AI assistant - in an editor or elsewhere - reading your dashboards, metrics, logs, traces, and the situations Coworker is tracking |

The third row is a different kind of thing from the first two. An assistant connected over MCP reads your OpsPilot data; it is not Coworker itself.

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
