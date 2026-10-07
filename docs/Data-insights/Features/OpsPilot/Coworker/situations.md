# Situations

Situations are what Coworker hands you to triage: coherent stories built from its findings and surfaced as a feed on your home page. This page covers how insights become situations, how severity and status work, what runs in the background to keep situations current, and how to work with them.

## Insights and situations

**Insights are the core of Coworker.** Everything Coworker does - investigating alerts, running scheduled checks, responding to webhooks - produces insights. An insight is one atomic finding: one observation, one anomaly, one error pattern. Each has a severity, a category, an affected service, and a short description with supporting evidence. Insights are how Coworker records what it has seen and reasoned about. You can browse every insight directly on the [Insights](insights.md) page.

**Situations** are the editorial layer built on top of insights. Coworker groups related insights into one coherent story: a title, a plain-language summary, the affected service, severity, and impact. Situations are what you triage. Insights are how Coworker writes them up; situations are what it hands you.

A situation is not a static record. As new insights arrive, Coworker decides whether to extend an existing situation, merge it with another, escalate or de-escalate its severity, or close it out. That continuous editing is the difference between a useful picture of your operations and a noisy alert feed.

## Severity and status

Severity and status answer two different questions:

| | Question | Values |
|---|---|---|
| **Severity** | How bad is this? | Critical, Warning, Info |
| **Status** | Where is it in its lifecycle? | Active, Watching, Resolved |

**Active** is a live problem, **Watching** is one Coworker is keeping an eye on rather than pressing you about, and **Resolved** is handled. You can also **dismiss** a situation that was never a real problem - it closes and drops out of the list.

!!! note "Severity and status are independent"
    A Critical can sit in Watching while Coworker keeps an eye on it, and a Warning can be Active. Keeping them separate lets the feed show what matters without conflating how bad something is with whether it is being handled.

---

## What runs in the background

Coworker is never just a snapshot. Three things run continuously:

**Investigating new signals.** When an alert fires or a task runs, Coworker pulls the relevant metrics, logs, and traces, writes insights, and decides what to do: raise a new situation, attach the finding to an existing one, or note that it looked and found nothing worth raising. Alerts that arrive close together are investigated as a group, so one underlying problem doesn't generate a wall of separate cards.

**Tidying up.** Every few minutes Coworker sweeps your open situations and consolidates them, merging two that turn out to be the same problem, escalating severity when a new signal warrants it, and attaching stray findings to the situation they belong to.

**Re-checking what's open.** Every open situation is re-investigated on a cadence that depends on its severity. Criticals are checked roughly every 10-15 minutes at first; warnings and quieter items less frequently. When a situation recovers on its own, Coworker resolves it and tells you why. As a situation stays stable, checks become less frequent; if something shifts, the cadence tightens back up. Once resolved, a situation gets a couple of follow-up checks over the next few hours to confirm the fix held.


---

## Your view or the team's

Use **Just for me** to filter situations to your personalized slice - those relevant to your services and setup. Switch to the broader view when you're on call, covering someone else's area, or want the full picture across your organization.

---

## The situations list

**Coworker > Situations** lists everything Coworker is actively working on, with the number of matches shown above the list.

| Control | What it does |
|---|---|
| **Search by title or service** | Find a situation by its name or the service it affects |
| **Status** | Filter by state - **Active**, **Watching**, or **Resolved**. Starts on Active and Watching, so resolved situations stay out of the way until you ask for them. Selections show as chips you can remove individually, with **Select all** and **Clear all** in the dropdown |
| **Any severity** | Filter to one severity |
| **Just for me** | Switch between your own slice and the full team view - see [Your view or the team's](#your-view-or-the-teams) |
| **By service** | Group the list by affected service |

Each row shows the situation's severity as a colored dot and as a label, the service it affects, its current state, and when it last changed. Services appear as they are named in your telemetry, so a namespaced one reads in full - `opentelemetry-demo/recommendation`, for example - which is also what **Search by title or service** matches on.

## Situations and threads

Every situation opens into a thread: a dedicated conversation about that one problem, with all context already loaded. At the top sits the situation itself; below it runs the history of Coworker's checkups and state changes, interleaved with any messages between you and it.


### What a situation shows you

Above the thread, the situation opens with its severity, the service it affects, and its status, then Coworker's own summary of what is happening and how far it has spread. Alongside that summary sit three panels:

| Panel | What it holds |
|---|---|
| **Right-now impact** | The numbers that make this matter at this moment - the latency, error rate, or throughput that moved, and the services it has reached |
| **Timeline** | What happened and when, oldest to newest, including whether this same pattern has occurred before |
| **Data** | The evidence behind the summary - trend charts over the recent window, and the log lines Coworker drew on |

### Signals watched

Coworker sets up its own watches on a situation so it hears about a change immediately, rather than waiting for its next scheduled checkup.

Each watched signal shows what it is watching and why, the threshold that counts as a breach, and its current state - **breaching** or **clear** - over a recent window. A signal that was clear at the last checkup and is breaching now is how Coworker catches an escalation early.

These are Coworker's own, set for this situation. They are not [alert rules](../../New-alerting/rules.md) and do not notify anyone on their own.

### Showing its working

A row of tabs at the foot of the situation opens up everything behind the summary, each with a count so you can see what is there before clicking:

| Tab | What it holds |
|---|---|
| **Evidence** | What Coworker read before it concluded any of this |
| **Raised from** | The insights the situation was built from |
| **Fixes** | Fixes recorded against this situation. Reads *No fixes recorded yet* until one is |
| **Repeat firings** | How many times this has recurred |
| **Updates** | Each time Coworker revised its own account of the situation. An entry gives its reasoning for the change and badges which fields it rewrote - **Updated title**, **Updated summary**, and so on |
| **History** | The full record of checkups and state changes |

The counts are worth reading on their own. A situation **raised from** several hundred insights with a high **repeat firings** count is a long-running pattern rather than a one-off, and tells you something before you have opened a single tab.

**Updates** is worth a look on anything long-running. A situation is not a fixed statement - as Coworker learns more it rewrites its own title and summary, and that tab is where it explains why. A situation that reads differently today than when you last saw it will say so there.

From a situation thread you can:

| Action | Description |
|---|---|
| **Ask follow-ups** | Type any question. Coworker answers with the situation's full context already in hand |
| **Verify now** | Triggers a fresh investigation immediately, rather than waiting for the next scheduled checkup. The result lands in the thread when done |
| **Suggest a fix** | Prompts Coworker to propose concrete remediation steps based on what it has found |
| **Assign** | Give the situation an owner. Click **I'll take this** to assign it to yourself, or search members and pick a teammate |
| **Set status** | Move the situation through its lifecycle - **Active**, **Watching**, or **Resolved** - or dismiss it. Closing a situation asks for a quick reason, which also teaches Coworker what not to raise next time |
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

These shortcuts are available everywhere insights appear: the priority queue, insight lists, and insight detail views. You can also click **Help me triage** to send your current priority insights and recent activity to Coworker for a prioritization recommendation.

---

## Chatting outside a situation

You can start a fresh thread at any time to ask about a service, a recent change, a metric, or anything else Coworker can investigate. Click **+** in the tab bar to open a new thread.


Three shortcuts are offered to get started quickly:

| Shortcut | Description |
|---|---|
| **Just chat** | Ask anything - running a query, debugging a service, exploring an idea |
| **Set up a task** | Schedule a check, watch a service, or react to a webhook |
| **Update your preferences** | Adjust the categories, services, or severities Coworker highlights for you |

These free-form chats have the full set of tools: attach images, use voice input, search the web, and pull context from your connected integrations.

Each task run produces a report with findings, the investigation process, and a final summary. An input field appears below each report (*Ask OpsPilot about this report...*) with the full report already in context, so you can ask follow-up questions without copying anything.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
