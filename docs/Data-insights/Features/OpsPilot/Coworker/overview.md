# Coworker

Coworker is your AI teammate for operations. It continuously monitors your systems, surfaces the issues that matter most, and helps you stay ahead of problems, so you spend less time investigating and more time building.

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
| **Chat integration** | Insight shortcuts, report discussion, triage, and onboarding via OpsPilot chat |
| **Memory** | System-wide and task-specific memory that connects the dots and improves over time |
| **Preferences** | Personalised focus on what matters to you |
| **Cost management** | Budget tracking and optimisation suggestions |

---

## Getting started

When you first access Coworker, a guided chat conversation walks you through setup:

![!Screenshot](/Coworker/getting-started.png)

1. Coworker asks about your role and what you monitor
2. You set your initial preferences: services, severity levels, and categories
3. You create your first task together
4. Coworker begins investigating

This setup can be restarted at any time from the dashboard settings.

![!Screenshot](/Coworker/restart-chat.png)

!!! tip
    The quickest way to get value from Coworker is to enable **OpsPilot Alerts**, which connects Coworker directly to your existing alert rules so it automatically investigates whenever an alert fires. A prompt on the dashboard will guide you through enabling it.

---

## Tasks

Tasks are the automated jobs Coworker runs in the background to proactively investigate your systems. You don't need to fill in forms or understand configuration options. Just describe what you want in plain language and OpsPilot builds the task for you through conversation.

Coworker is not limited to your observability data. As an LLM, it can also search the web as part of an investigation, meaning it can bring in external context — documentation, known issues, best practices — alongside your metrics, logs, and traces.

!!! info
    Tasks are currently configured at the organisation level.

To create a task, open a new thread and select **Set up a task**. Coworker asks *"What are you trying to achieve?"* and guides you through setup conversationally - no forms or configuration options to fill in. Suggested shortcuts help you get started quickly:

- *"Create a scheduled task to check error rates every hour"*
- *"Watch a service and tell me when something looks off"*
- *"Listen to a webhook and run a check on every event"*

To edit an existing task, click **Configure** from the task panel in the sidebar.

### Task types

#### Scheduled tasks

Run on a recurring schedule (hourly, daily, weekly, monthly, or a custom interval). Each run produces a report summarising what Coworker found. These are the core of Coworker's continuous analysis. Run any task on-demand with the **Run now** button and view the full execution history to see what it found on each run.

#### Monitoring tasks

Focused on a specific issue. Created by clicking **Watch** on an insight, or by describing what you want monitored in chat. A monitoring task periodically checks a particular pattern and notifies you if something changes, turning a one-off finding into continuous observation without you having to remember to check back.

#### Event sources

React to webhooks from external systems. Instead of running on a schedule, they wait for an event to arrive and immediately kick off an investigation, enabling real-time response to issues as they happen.

To set up an event source, open a new thread, select **Set up a task**, and describe the webhook you want to connect.

![!Screenshot](/Coworker/create-event-source.png)

| Field | Description |
|---|---|
| **Type** | The webhook type, e.g. Generic Webhook |
| **Name** | A name for the event source (e.g. Production Alerts) |
| **Description** | What events this webhook will receive |
| **Custom Instructions** (optional) | Guides how events are investigated, e.g. "Focus on database-related issues and suggest query optimizations" |
| **Model Tier** | Controls how the event is investigated. See [Model tier](#model-tier). **Thorough** is best for critical alerts and complex events needing deep analysis; **Efficient** is best for high-volume, routine events like health checks |
| **Monthly Budget** (optional) | Set a token budget for this event source. Click **Set budget** to configure |

##### OpsPilot Alerts

A built-in event source present for every user. It connects Coworker directly to your configured alert rules so that when an alert fires, Coworker automatically investigates it.

![!Screenshot](/Coworker/op-alerts.png)

Use the toggle at the top to enable or disable the OpsPilot Alerts integration entirely. The **History** and **Cost & Optimisation** buttons are available for reviewing past investigations and spend.

You can also add **General Instructions** that apply to all alert investigations, or expand individual alerts (using the `>` chevron) to add alert-specific instructions. Both are optional but can improve the quality of Coworker's investigations.

Under **Alert Rules**, you can:

- **Search** alerts by name
- Filter by **All**, **Enabled**, or **Firing**
- **Enable All** or **Disable All** in bulk
- Toggle individual alerts on or off (each shows its name, type, and current state: inactive/firing)
- Expand an alert (using the `>` chevron) to add alert-specific instructions (e.g. "Check the Redis connection pool first")

### Model tier

Every task and event source has a **Model Tier** setting that controls how Coworker analyses the data:

| Tier | Description |
|---|---|
| **Thorough** | Handles any task, more capable, higher cost |
| **Efficient** | Suited to simpler, focused tasks, lower cost |

Use **Thorough** for critical alerts and complex investigations where depth matters. Use **Efficient** for routine or high-volume tasks to keep token costs down.

---

## Insights

Insights are the findings Coworker surfaces from its background analysis: intelligent, contextualised observations with supporting context and recommended actions, not just raw alerts.

Each insight includes:

- **Title and severity**: Critical, Warning, or Info
- **Category**: Errors, Performance, Notable, or Coverage
- **Affected service**
- **Description**: a written explanation of what was found, including supporting evidence
- **Occurrence history**: a timeline showing if this is a recurring pattern
- **Recommended actions**: what you can do about it

For each insight you can:

- **Chat**: ask Coworker to explain the issue or help you decide what to do
- **Watch**: create a monitoring task to track this pattern going forward
- **Resolve**: mark it as handled
- **Ignore**: dismiss it from your priority list

You can browse all insights, filter by date, search, and view resolved insights separately. The **Analytics** view breaks down insights by service, category, and label groupings, giving you a higher-level picture of where issues are concentrated over time.

Insights that are not resolved or ignored will age out after **30 days**, keeping your list focused and preventing stale findings from building up.

Coworker also proactively generates **observability gap insights** — flagging services that are not instrumented or areas where metrics are missing. These help you improve your coverage and give Coworker itself better data to work with over time.

Use the **My Insights** dropdown to switch between your personalised view and **All Team Insights**, which shows insights across all users in your organisation.

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

These shortcuts are available everywhere insights appear: the priority queue, insight lists, and insight detail views.

### Task reports

Each task run produces a report containing three parts: the **findings** (insights surfaced during the investigation), the **investigation process** (what Coworker checked and how it reached its conclusions), and a **final summary**. The default mode is reporting — Coworker surfaces what it found without proposing fixes unless you instruct it to. The insights themselves will suggest remediation steps where relevant.

After a task runs, an input field appears below the report: *Ask OpsPilot about this report...* The full report is included as context, so you can ask follow-up questions without copying anything.

### Execution history summary

In the task execution history timeline, a **Summarize** button sends details of your executions to OpsPilot for a summary, including success/failure counts, durations, and insight counts. The summary covers only the executions currently visible in the list, so you can filter the history first to control what gets summarised.

### Triage

The **Help me triage** button sends your current priority insights, recent insights, and trending issues to OpsPilot and asks it to help you decide what to focus on first.

![!Screenshot](/Coworker/triage.png)

---

## Memory

One of Coworker's most powerful features is that it gets smarter over time. As it runs tasks, investigates insights, and chats with you, it continuously builds memory, learning about your systems, your preferences, and how things connect together.

### System-wide memory

Coworker's general understanding of your environment, gathered from every task run, chat, and investigation:

- What services and infrastructure you have and how they depend on each other
- What metrics exist and what they mean
- General patterns, best practices, and operational context

Browse this via the **Knowledge** button on the dashboard, which shows a visual knowledge graph. Memories are connected. Coworker understands how different pieces of knowledge relate to each other, joining the dots across everything it has learned.

### Task-specific memory

Each task builds its own memory over time, remembering what patterns matter, what turned out to be important, and what didn't. A task that has been running for weeks produces richer, more relevant results than one that just started, and becomes more cost-efficient as it re-uses context it already knows. In some cases, task memory can reduce token costs by up to 50% by eliminating the need to re-fetch background information on every run.

### User memory

Coworker also remembers your personal preferences from conversations — for example, whether you prefer responses with or without tables, or other formatting preferences you have expressed. This makes the assistant and task output increasingly tailored to how you like to work.

---

## Dashboard

The Coworker dashboard is personalised, named after you (e.g. *J's Coworker*), and gives you a conversational interface to your AI teammate alongside a live view of your tasks.

![!Screenshot](/Coworker/dashboard.png)

A **WATCHING** badge in the header indicates Coworker is actively monitoring your environment. Use the dropdown in the top right to switch between **Just for me** (your personalised view) and **Across the team** (insights across all users in your organisation). **Usage** and **Knowledge** are also accessible from the top right.

### Home tab

The **Home** tab is the main feed where Coworker proactively surfaces what it has found. Coworker posts updates directly into the feed - for example, *"Nothing critical right now - a few things worth a look when you have the time."* Monitoring task results appear as inline cards showing the issue title, the service being watched, how long it has been watched, and when it was last checked.

Suggested questions appear at the bottom of the feed (e.g. *"What changed in the last hour?"*, *"Anything I should know before standup?"*). A persistent chat input lets you message Coworker directly from the Home tab at any time.

### Threads

Click **+** next to the Home tab to open a new thread. Each thread is a focused conversation with Coworker and runs alongside Home as a separate tab. When you open a new thread, Coworker offers three starting points:

| Option | Description |
|---|---|
| **Just chat** | Opens a freeform composer with *"I'm listening."* - ask anything: run a query, debug a service, explore an idea |
| **Set up a task** | Conversationally create a scheduled check, a watching task, or a webhook event source |
| **Update your preferences** | Adjust which services, categories, or severities Coworker highlights for you |

Threads can be closed with the **×** on the tab. You can have multiple threads open at once and switch between them freely.

### Tasks panel

The right-hand sidebar shows your active tasks, split into **Event Sources** and **Scheduled** sections. Each task shows its name, schedule, and when it last ran. Click **Manage all tasks** at the bottom to open the full task management panel.

The **All tasks** panel lets you view and manage everything Coworker runs:

- Use the **Preferences** button to update your monitoring preferences, or **+ Create Task** to create a new task
- Filter tasks using the tabs: **All**, **Scheduled**, **Monitoring**, **Event Sources**
- Search tasks by name using the search bar
- The **SYSTEM** section shows built-in tasks such as **OpsPilot Alerts**, which automatically investigates firing alerts. A badge shows how many alerts are currently being watched (e.g. *38/38 watched*)
- The **ACTIVE** section lists your tasks with schedule, next run time, and last run date. Each task has a **run** button to trigger it immediately, a toggle to enable or disable it, and a delete button

---

## Preferences

To update your preferences, open a new thread and select **Update your preferences**, or describe the change you want directly in any chat. Coworker will ask clarifying questions and update your settings conversationally - you can adjust which services you track, what types of insights you see, or your role and team info.

To hide insights of a similar type across your view, use the **Hide similar** button on any insight.

![!Screenshot](/Coworker/hide-similar.png)

This opens a modal where you can choose what to match: by category, severity, label, or title pattern. Coworker will stop surfacing insights that match your selected conditions.

![!Screenshot](/Coworker/hide-insights.png)

---

## Cost and optimisation

Coworker tracks the cost of running your tasks and provides full transparency into spend. Click **Usage** from the top right of the dashboard to open the view.

!!! tip
    One of the most effective ways to reduce costs over time is simply to let tasks run. As [task-specific memory](#task-specific-memory) builds up, Coworker re-uses context it already knows rather than fetching it fresh each run — reducing token usage by up to 50% in some cases.

![!Screenshot](/Coworker/cost-optimize.png)

### Budget

At the top, the **Task Budget** bar shows your current spend broken down into **Chat**, **Coworker**, and **Projected** segments, with the total tokens used against your budget (e.g. 1,592 / 5,000 tokens). Click **Configure** to open the Budget Settings modal.

![!Screenshot](/Coworker/budget-settings.png)

| Setting | Description |
|---|---|
| **Plan Allowance** | Your total token allowance per month (set by your plan) |
| **Monthly task budget** | The percentage of your plan allowance allocated to tasks. Select a preset or use the slider |
| **Warning threshold** | The percentage of your task budget at which Coworker warns you about spend |
| **Halt threshold** | The percentage at which Coworker stops running tasks to prevent overspend |

Below the Task Budget bar, **Total org usage** shows the full organisation-level token consumption including non-task usage.

### Usage overview

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

### Per-task analysis

Click through to a specific task to see its full cost breakdown:

![!Screenshot](/Coworker/optimize.png)

| Metric | Description |
|---|---|
| **Avg cost / run** | Average tokens consumed per execution |
| **Total this period** | Tokens used so far, with execution count and percentage of your plan |
| **Projected monthly** | Estimated monthly token usage and number of runs |

The **Cost by Model Tier** section breaks down spend across Efficient and Thorough runs, showing tokens per run, projected monthly cost, and number of samples for each tier.

A **Cost per Run** chart shows token usage over time so you can spot trends or spikes.

After a task has run a few times, Coworker automatically surfaces optimisation suggestions, shown as a **Pending Suggestions** count at the bottom of the Cost & Optimisation panel - and as a numbered badge on the Overview page widget. Each suggestion shows the recommended change, an explanation, and an estimated monthly token saving.

Use **Accept all** to apply all suggestions at once, or enable **Auto-accept** to have Coworker automatically apply future suggestions as they are generated.

![!Screenshot](/Coworker/optimize-alert.png)

Expand a suggestion to see the full reasoning, including a **Why this suggestion** breakdown of the cost data behind the recommendation and the specific change proposed (e.g. switching model tier).

![!Screenshot](/Coworker/optimize-accept.png)

From here you can **Accept** to apply the change immediately, or **Dismiss** to ignore it. Use **View task config** to review the full task setup before deciding.

Click **Analyse & Optimise** to trigger an on-demand analysis at any time. If no optimisations are needed, you'll see a **Looking good!** confirmation.

![!Screenshot](/Coworker/looking-good.png)

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
