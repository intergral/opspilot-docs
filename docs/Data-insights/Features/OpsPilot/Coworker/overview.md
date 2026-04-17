# Coworker

Coworker is your AI teammate for operations. It continuously monitors your systems, surfaces the issues that matter most, and helps you stay ahead of problems — so you spend less time investigating and more time building.

![!Screenshot](/Coworker/coworker.png)

Each user gets their own personalised Coworker that learns what's relevant to them. It runs tasks in the background, builds context over time, and delivers prioritised, actionable insights directly to your dashboard.

## What Coworker does

| Capability | What it does |
|---|---|
| **Dashboard** | Centralised view of priorities, live metrics, and tasks |
| **Insights** | Investigated, contextualised findings with evidence and recommended actions |
| **Scheduled tasks** | Recurring automated analysis and reporting |
| **Monitoring tasks** | Continuous observation of specific patterns or issues |
| **Event sources** | React to external webhooks and investigate immediately |
| **Chat integration** | Insight shortcuts, report discussion, triage, and onboarding — all via OpsPilot chat |
| **Memory** | System-wide and task-specific memory that connects the dots and improves over time |
| **Preferences** | Personalised focus on what matters to you |
| **Cost management** | Budget tracking and optimisation suggestions |

---

## Getting started

When you first access Coworker, a guided chat conversation walks you through setup:

![!Screenshot](/Coworker/getting-started.png)

1. Coworker asks about your role and what you monitor
2. You set your initial preferences — services, severity levels, and categories
3. You create your first task together
4. Coworker begins investigating

This setup can be restarted at any time from the dashboard settings.

![!Screenshot](/Coworker/restart-chat.png)

!!! tip
    The quickest way to get value from Coworker is to enable **OpsPilot Alerts** — this connects Coworker directly to your existing alert rules so it automatically investigates whenever an alert fires. A prompt on the dashboard will guide you through enabling it.

---

## Tasks

Tasks are the automated jobs Coworker runs in the background to proactively investigate your systems. You don't need to fill in forms or understand configuration options — just describe what you want in plain language and OpsPilot builds the task for you through conversation.

Click **Create Task** to open the **Task Agent** — a conversational interface where you describe what you want monitored and OpsPilot builds the task for you through conversation, asking clarifying questions and setting it up.

![!Screenshot](/Coworker/create-task.png)

To edit an existing task, click **Edit with OpsPilot** from the task's detail view — the Task Agent opens pre-loaded with the current configuration.

### Task types

#### Scheduled tasks

Run on a recurring schedule — hourly, daily, weekly, monthly, or a custom interval. Each run produces a report summarising what Coworker found. These are the core of Coworker's continuous analysis. Run any task on-demand with the **Run now** button and view the full execution history to see what it found on each run.

#### Monitoring tasks

Focused on a specific issue. Created by clicking **Watch** on an insight, or by describing what you want monitored in chat. A monitoring task periodically checks a particular pattern and notifies you if something changes — turning a one-off finding into continuous observation without you having to remember to check back.

#### Event sources

React to webhooks from external systems. Instead of running on a schedule, they wait for an event to arrive and immediately kick off an investigation — enabling real-time response to issues as they happen.

Click **Connect** from the dashboard prompt or **+ Create Task** and select Event Source to open the setup modal.

![!Screenshot](/Coworker/create-event.png)

| Field | Description |
|---|---|
| **Type** | The webhook type — e.g. Generic Webhook |
| **Name** | A name for the event source (e.g. Production Alerts) |
| **Description** | What events this webhook will receive |
| **Custom Instructions** (optional) | Guides how events are investigated — e.g. "Focus on database-related issues" |
| **Model Tier** | Controls how the event is investigated — see [Model tier](#model-tier) |

##### OpsPilot Alerts

A built-in event source present for every user. It connects Coworker directly to your configured alert rules so that when an alert fires, Coworker automatically investigates it.

![!Screenshot](/Coworker/op-alerts.png)

Use the toggle at the top to enable or disable the OpsPilot Alerts integration entirely. The **History** and **Cost & Optimisation** buttons are available for reviewing past investigations and spend.

Under **Alert Rules**, you can:

- **Search** alerts by name
- Filter by **All**, **Enabled**, or **Firing**
- **Enable All** or **Disable All** in bulk
- Toggle individual alerts on or off — each shows its name, type, and current state (inactive/firing)
- Expand an alert (using the `>` chevron) to add alert-specific instructions for Coworker (e.g. "Check the Redis connection pool first")

### Model tier

Every task and event source has a **Model Tier** setting that controls how Coworker analyses the data:

| Tier | Description |
|---|---|
| **Thorough** | Handles any task — more capable, higher cost |
| **Efficient** | Suited to simpler, focused tasks — lower cost |

Use **Thorough** for critical alerts and complex investigations where depth matters. Use **Efficient** for routine or high-volume tasks to keep token costs down.

---

## Insights

Insights are the findings Coworker surfaces from its background analysis — intelligent, contextualised observations with evidence and recommended actions, not just raw alerts.

Each insight includes:

- **Title and severity** — Critical, Warning, or Info
- **Category** — the type of issue (performance, reliability, cost, etc.)
- **Affected service**
- **Description** — a written explanation of what was found
- **Evidence** — the raw data, metrics, or logs that led to the finding
- **Occurrence history** — a timeline showing if this is a recurring pattern
- **Recommended actions** — what you can do about it

For each insight you can:

- **Chat** — ask Coworker to explain the issue or help you decide what to do
- **Watch** — create a monitoring task to track this pattern going forward
- **Resolve** — mark it as handled
- **Ignore** — dismiss it from your priority list

You can browse all insights, filter by date, search, and view resolved insights separately. The **Analytics** view breaks down insights by service, category, and label groupings — giving you a higher-level picture of where issues are concentrated over time.

Use the **My Insights** dropdown to switch between your personalised view and **All Team Insights** — which shows insights across all users in your organisation.

---

## Chat integration

Coworker is deeply integrated with the OpsPilot chat assistant throughout the experience.

### Insight shortcuts

Click **Chat** on any insight to access five quick actions:

| Action | Description |
|---|---|
| **Is this still an issue?** | Checks the current state to see if the issue is ongoing or resolved |
| **Investigate root cause** | Kicks off a root cause analysis |
| **Create a ticket** | Creates a ticket for the issue |
| **Suggest a fix** | Recommends remediation steps or best practices |
| **Discuss this insight** | Opens a free-form conversation about the insight |

These shortcuts are available everywhere insights appear — the priority queue, insight lists, and insight detail views.

### Task reports

After a task runs, an input field appears below the report: *Ask OpsPilot about this report...* The full report is included as context, so you can ask follow-up questions without copying anything.

### Execution history summary

In the task execution history timeline, a **Summarize** button sends details of your recent executions (up to 50) to OpsPilot for a summary — including success/failure counts, durations, and insight counts across runs.

### Triage

The **Help me triage** button sends your current priority insights, recent insights, and trending issues to OpsPilot and asks it to help you decide what to focus on first.

![!Screenshot](/Coworker/triage.png)

---

## Memory

One of Coworker's most powerful features is that it gets smarter over time. As it runs tasks, investigates insights, and chats with you, it continuously builds memory — learning about your systems, your preferences, and how things connect together.

### System-wide memory

Coworker's general understanding of your environment, gathered from every task run, chat, and investigation:

- What services and infrastructure you have and how they depend on each other
- What metrics exist and what they mean
- General patterns, best practices, and operational context

Browse this via the **Knowledge** button on the dashboard, which shows a visual knowledge graph. Memories are connected — Coworker understands how different pieces of knowledge relate to each other, joining the dots across everything it has learned.

### Task-specific memory

Each task builds its own memory over time — remembering what patterns matter, what turned out to be important, and what didn't. A task that has been running for weeks produces richer, more relevant results than one that just started, and becomes more cost-efficient as it re-uses context it already knows.

---

## Dashboard

The Coworker dashboard gives you a centralised view of your priorities, active tasks, and live system metrics — all in one place. The dashboard is personalised — it's named after you (e.g. *J's Coworker*) and shows only what's relevant to you.

At the top, a row of live metrics shows the current state:

| Metric | Description |
|---|---|
| **Total Insights** | Breakdown by severity (Critical, Warning, Info) with trend indicators |
| **Resolved Rate** | Progress ring showing how many insights have been handled |
| **Tasks Ran** | Number of background tasks completed |
| **Running** | Number of tasks currently active |

Use the **My Insights** dropdown to switch between your personalised view and **All Team Insights** — which shows insights across all users in your organisation. Use **Change what I show you** to update your preferences directly from the dashboard. The **Triage** and **Cost & Optimisation** buttons are also accessible from the top right.

Below the metrics, the **Priority Queue** highlights the top issues Coworker thinks you should look at — with chat, resolve, and ignore actions on each. Click **Browse all insights** to see the full list. When everything is handled, you'll see an **All caught up!** message.

The **Tasks** section below shows everything Coworker takes care of on schedule or when events come in. Filter tasks by **All**, **Favorites**, **Scheduled**, **Monitoring**, or **Events**. Each task card shows its last run time, next run time, number of runs, and a summary of findings. Use **Run Now**, **Last Run**, **Configure**, and **History** to manage each task, or use **+ Create Task** and **Manage** from the top of the section.

---

## Preferences

Personalise what your Coworker focuses on by clicking **Change what I show you** on the dashboard.

![!Screenshot](/Coworker/change-what-see.png)

| Preference | Description |
|---|---|
| **Severity** | Toggle which severity levels you care about — Critical, Warning, Info |
| **Category** | Choose which types of insights to prioritise — Errors, Performance, Notable, Coverage |
| **Service** | Select which services are relevant to you |
| **Label** | Filter by custom groupings and tags |

You can update preferences via chat using the **Update via chat** button, or restart the full setup with **Restart setup**.

---

## Cost and optimisation

Coworker tracks the cost of running your tasks and provides full transparency into spend. Click **Cost & Optimisation** from the dashboard to open the view.

![!Screenshot](/Coworker/cost-optimize.png)

At the top, the **Task Budget** bar shows your current spend against your configured budget, with a **Configure** button to adjust it. Below that, **Total org usage** shows the full organisation-level token consumption including non-task usage.

The **Usage** section provides three key metrics:

| Metric | Description |
|---|---|
| **Tokens spent** | Total tokens consumed in the current period |
| **Tasks executed** | Number of task runs completed |
| **Projected monthly** | Estimated end-of-month token usage and number of runs |

A **Token Usage** chart shows your consumption trend over time.

The **Cost Breakdown** table lists each task with:

| Column | Description |
|---|---|
| **Task** | The task name |
| **Schedule** | How often the task runs |
| **Avg / run** | Average token cost per execution |
| **Monthly** | Projected monthly token cost |
| **%** | Percentage of total task budget |

Click through to a specific task to see its full cost breakdown:

![!Screenshot](/Coworker/optimize.png)

| Metric | Description |
|---|---|
| **Avg cost / run** | Average tokens consumed per execution |
| **Total this period** | Tokens used so far, with execution count and percentage of your plan |
| **Projected monthly** | Estimated monthly token usage and number of runs |

The **Cost by Model Tier** section breaks down spend across Efficient and Thorough runs — showing tokens per run, projected monthly cost, and number of samples for each tier.

A **Cost per Run** chart shows token usage over time so you can spot trends or spikes.

After a task has run a few times, Coworker automatically surfaces **Optimisation Suggestions** — each showing the recommended change, an explanation, and an estimated monthly token saving.

![!Screenshot](/Coworker/optimize-alert.png)

Expand a suggestion to see the full reasoning — including a **Why this suggestion** breakdown of the cost data behind the recommendation and the specific change proposed (e.g. switching model tier).

![!Screenshot](/Coworker/optimize-accept.png)

From here you can **Accept** to apply the change immediately, or **Dismiss** to ignore it. Use **View task config** to review the full task setup before deciding.

Click **Analyse & Optimise** to trigger an on-demand analysis at any time. If no optimisations are needed, you'll see a **Looking good!** confirmation.

![!Screenshot](/Coworker/looking-good.png)

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
