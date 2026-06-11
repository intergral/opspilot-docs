# Coworker

Coworker is your always-on AI operations partner. It watches your services, investigates what it finds, and gives you a clear, prioritised picture of what's worth your attention right now, so you spend less time watching dashboards and more time building.

![!Screenshot](/Coworker/coworker.png)

Each user gets their own personalised Coworker that learns what's relevant to them. It talks to you in the first person, remembers context, and keeps working between your visits.

## How to think about it

Think of Coworker as a single teammate rather than a monitoring tool. Behind that one voice it is doing several jobs at once: watching for signals, investigating them, writing down what it finds, and deciding what to tell you. You don't need to think about those internal jobs. You just get one Coworker who keeps you informed.

## What Coworker does

| Capability | Description |
|---|---|
| **Situations** | Intelligent, contextualised findings grouped into coherent stories with severity, evidence, and recommended actions |
| **Continuous monitoring** | Watches your systems around the clock and re-investigates open situations on a regular cadence |
| **Alert response** | Automatically investigates firing alerts and posts one clean situation instead of a stream of raw alert noise |
| **Tasks** | Scheduled, monitoring, and webhook-driven jobs that run recurring analysis and report back proactively |
| **Memory** | Builds a growing understanding of your systems, your team, and your preferences over time |
| **Cost management** | Budget tracking and optimisation suggestions to keep token spend under control |

---

## Insights and situations

Two concepts underpin everything Coworker shows you.

**Insights** are Coworker's atomic findings: one observation, one anomaly, one error pattern. They are written automatically whenever Coworker investigates something: an alert that fired, a scheduled check, or a webhook event. Each insight has a severity, a category, an affected service, and a short description with supporting evidence.

**Situations** are the editorial layer on top. Coworker groups related insights into one coherent story: a title, a plain-language summary, the affected service, severity, and impact. Situations are what you triage. Insights are how Coworker writes them up; situations are what it hands you.

A situation is not a static record. As new insights arrive, Coworker decides whether to extend an existing situation, merge it with another, escalate or de-escalate its severity, or close it out. That continuous editing is the difference between a useful picture of your operations and a noisy alert feed.

## Severity and status

Severity and status answer two different questions:

| | Question | Values |
|---|---|---|
| **Severity** | How bad is this? | Critical, Warning, Info |
| **Status** | Should you act on it right now? | Active, Watching, Resolved |

These don't always align the way you'd expect. A warning can be active if Coworker thinks you should look now. A critical is active by default, but once it's handled it moves to resolved. Splitting the two lets the page show "important but not urgent" items without either burying them or sounding false alarms.

---

## What runs in the background

Coworker is never just a snapshot. Three things run continuously:

**Investigating new signals.** When an alert fires or a task runs, Coworker pulls the relevant metrics, logs, and traces, writes insights, and decides what to do: raise a new situation, attach the finding to an existing one, or note that it looked and found nothing worth raising. Alerts that arrive close together are investigated as a group, so one underlying problem doesn't generate a wall of separate cards.

**Tidying up.** Every few minutes Coworker sweeps your active situations and consolidates them, merging two that turn out to be the same problem, escalating severity when a new signal warrants it, and attaching stray findings to the situation they belong to.

**Re-checking what's open.** Every active situation is re-investigated on a cadence that depends on its severity. Criticals are checked roughly every 10–15 minutes at first; warnings and quieter items less frequently. When a situation recovers on its own, Coworker resolves it and tells you why. As a situation stays stable, checks become less frequent; if something shifts, the cadence tightens back up. Once resolved, a situation gets a couple of follow-up checks over the next few hours to confirm the fix held.

---

## The home page

The home page is a feed of messages from your Coworker, more like a conversation with a colleague who has been working while you were away than a static dashboard. Everything arrives as a message in that feed: new situations, updates to existing ones, checks that came back clean, and pointers to coverage gaps.

![!Screenshot](/Coworker/dashboard.png)

A **WATCHING** badge in the header confirms Coworker is actively monitoring your environment.

The interface uses a tab bar across the top. **Home** is always the first tab. Each situation thread or conversation you open appears as an additional tab alongside it, so you can switch between multiple threads without losing context. Click **+** to open a new thread. Tabs with an orange dot indicate an active or critical situation.

### Your view or the team's

At the top of the page is a toggle between two views:

| View | Description |
|---|---|
| **You** | Your personalised slice, filtered to what is relevant to you based on your setup |
| **Team** | Everything Coworker has raised across your whole organisation, unfiltered |

Most of the time you'll work in **You**. Switch to **Team** when you're on call, covering someone else's area, or want the full picture. Both views show the same situations; the toggle only changes how much of them reaches your page.

### How the feed adapts

Coworker changes how it leads depending on what it has to tell you:

| State | What you see |
|---|---|
| **Quiet** | An "all clear" note on what Coworker has been doing and watching. Silence means "checked and fine", not "nothing running" |
| **One critical** | A single focus card with the full story: summary, affected service, impact, latest checkup, and evidence |
| **A few criticals** | Prominent rows in urgency order, each with enough detail to triage at a glance |
| **Many criticals** | A status overview showing the count and affected services. When everything is urgent, a wall of full-size cards doesn't help |

Below the critical items sits the quieter list: warnings and lower-severity items Coworker is watching rather than actively raising. This is where tomorrow's situation often first appears. Recently resolved situations collapse into a short list near the bottom.

### Other message types

Alongside situations, the feed contains:

- **Coverage gaps**: pointers to things Coworker would have investigated but couldn't, because data is missing (for example, a service with no telemetry). Each names what's missing and includes a **Help me set this up** button that opens a guided thread.
- **The digest**: a snapshot Coworker keeps current, summarising the checks it ran and things it handled quietly in the background.
- **Debriefs**: short notes for when Coworker investigated something and concluded there was nothing worth raising, so the work is visible rather than silent.

---

## Situations and threads

Every situation opens into a thread: a dedicated conversation about that one problem, with all context already loaded. At the top sits the situation itself; below it runs the history of Coworker's checkups and state changes, interleaved with any messages between you and it.

From a situation thread you can:

| Action | Description |
|---|---|
| **Ask follow-ups** | Type any question. Coworker answers with the situation's full context already in hand |
| **Verify now** | Triggers a fresh investigation immediately, rather than waiting for the next scheduled checkup. The result lands in the thread when done |
| **Suggest a fix** | Prompts Coworker to propose concrete remediation steps based on what it has found |
| **Resolve / Dismiss** | Closes the situation. Coworker asks for a quick reason, which also teaches it what not to raise next time |
| **Share** | Copies a shareable link to the thread |
| **Copy** | Copies the full situation as a markdown brief, ready to paste into another tool or hand off to a teammate |

### Insight shortcuts

Click **Chat** on any insight for five quick actions:

| Action | Description |
|---|---|
| **Is this still an issue?** | Checks current state to see if the problem is ongoing or resolved |
| **Investigate root cause** | Kicks off a root cause analysis |
| **Create a ticket** | Creates a ticket for the issue |
| **Suggest a fix** | Recommends remediation steps or best practices |
| **Discuss this insight** | Opens a free-form conversation about the insight |

These shortcuts are available everywhere insights appear: the priority queue, insight lists, and insight detail views. You can also click **Help me triage** to send your current priority insights and recent activity to Coworker for a prioritisation recommendation.

---

## Chatting outside a situation

You can start a fresh thread at any time to ask about a service, a recent change, a metric, or anything else Coworker can investigate. These free-form chats have the full set of tools: attach images, use voice input, search the web, and pull context from your connected integrations.

Each task run produces a report with findings, the investigation process, and a final summary. An input field appears below each report (*Ask OpsPilot about this report...*) with the full report already in context, so you can ask follow-up questions without copying anything.

---

## Memory

Coworker gets smarter over time. Everything it does (investigating alerts, running tasks, talking to you) builds memory that carries forward.

| Memory type | What it holds |
|---|---|
| **System-wide** | How your services fit together, what's normal, and what tends to break. Shared across your whole organisation, so what Coworker learns helping one person makes it smarter for everyone |
| **Task-specific** | What recurring checks have turned up before and the patterns that matter. Can reduce token costs by up to 50% on long-running tasks |
| **Team** | Who owns what, where the runbook lives, what each channel is for |
| **User** | Your personal preferences and the way you like to work, learned from your conversations |

Browse what Coworker has learned via the **Knowledge** button on the dashboard: a visual knowledge graph of your services and the facts it holds about each.

### Correcting Coworker

When Coworker raises something that isn't a problem, dismiss it with a quick reason, such as "this is expected" or "too noisy". Coworker turns your correction into a lasting fact: next time it sees the same pattern on the same service, it remembers and won't raise it again. A few early corrections go a long way towards tuning Coworker to your reality.

---

## Preferences

To update your monitoring preferences at any time, open a new thread and select **Update your preferences**, or describe the change you want directly in any chat. Coworker will ask clarifying questions and update your settings conversationally.

To suppress a type of insight from your view, click **Hide similar** on any insight card.

![!Screenshot](/Coworker/hide-similar.png)

This opens a modal where you can match by category, severity, label, or title pattern. Coworker will stop surfacing insights that match your conditions.

![!Screenshot](/Coworker/hide-insights.png)

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
