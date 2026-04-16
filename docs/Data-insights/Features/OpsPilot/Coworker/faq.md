# Coworker FAQ

## Getting started

### How do I get started with Coworker?

When you first open Coworker, a [guided setup conversation](overview.md#getting-started) walks you through setting your preferences and creating your first task. The quickest way to get value is to enable [OpsPilot Alerts](overview.md#opspilot-alerts) — this connects Coworker to your existing alert rules so it automatically investigates whenever one fires.

### Can I have more than one Coworker?

Each user has their own personalised Coworker. It is not possible to create multiple Coworkers for a single user.

### Can my team share a Coworker?

Each Coworker is personal to the user it belongs to. However, team members can view **All Team Insights** from the [dashboard](overview.md#dashboard) to see insights across the whole organisation.

### Can I restart the setup?

Yes — click the settings icon on the [dashboard](overview.md#getting-started) and select **Restart setup** to go through the onboarding conversation again.

---

## Tasks

### How many tasks should I create?

Start with one or two [scheduled tasks](overview.md#scheduled-tasks) covering your most critical services, and enable [OpsPilot Alerts](overview.md#opspilot-alerts). Add more tasks over time as you identify gaps. Too many tasks running frequently can increase token costs.

### How often should I run scheduled tasks?

This depends on how dynamic your environment is. Daily is a good starting point for most teams. Hourly is useful for high-traffic or critical services where issues can escalate quickly. See [Scheduled tasks](overview.md#scheduled-tasks).

### Why isn't my task finding anything?

It may take a few runs for Coworker to build enough context to surface meaningful insights. If a task consistently finds nothing, consider adjusting the description to be more specific about what you want it to investigate.

### What is the difference between a scheduled task and a monitoring task?

A [scheduled task](overview.md#scheduled-tasks) runs on a recurring interval and produces a general report of findings. A [monitoring task](overview.md#monitoring-tasks) is focused on a specific pattern or issue — created from an insight — and tracks whether that pattern is improving, worsening, or stable over time.

---

## Insights

### What is the difference between Resolve and Ignore?

**Resolve** marks an insight as handled — it will appear in your resolved insights history. **Ignore** dismisses it from your priority list without marking it as resolved. Use Resolve when you've taken action; use Ignore when the insight isn't relevant to you. See [Insights](overview.md#insights).

### Why am I seeing the same insight repeatedly?

If the underlying issue hasn't been fixed, Coworker will continue to surface it. The occurrence history on each insight shows whether it is a recurring pattern. Use **Watch** to create a [monitoring task](overview.md#monitoring-tasks) that tracks whether the issue improves.

### How do I change what types of insights I see?

Click **Change what I show you** on the dashboard to adjust your severity and category preferences, or use **Update via chat** to describe your preferences in plain language. See [Preferences](overview.md#preferences).

---

## Costs

### How much does Coworker cost to run?

Coworker uses OpsPilot AI tokens to run tasks and generate insights. The cost depends on how many tasks you have, how frequently they run, and the [model tier](overview.md#model-tier) selected (Thorough uses more tokens than Efficient). See [Cost and optimisation](overview.md#cost-and-optimisation) on the dashboard for a full breakdown and projected monthly spend.

### How do I reduce Coworker token usage?

- Review the **optimisation suggestions** in the [Cost & Optimisation](overview.md#cost-and-optimisation) page — these appear automatically after a task has run a few times and Coworker detects ways it could be improved
- Click through to a specific task in the Cost & Optimisation page and click **Analyse & Optimise** to analyse it for potential cost reductions
- Switch high-volume or routine tasks to the [Efficient model tier](overview.md#model-tier)
- Reduce the frequency of scheduled tasks that run often but find little
- Review the **Cost Breakdown** table to identify the most expensive tasks and consolidate or adjust them

### What is the difference between Thorough and Efficient model tiers?

**Thorough** handles any task and is more capable — use it for critical alerts and complex investigations where depth matters. **Efficient** is suited to simpler, focused tasks and costs less — use it for routine or high-volume tasks to keep spend down. You can set the model tier per task or per event source. See [Model tier](overview.md#model-tier).

---

## Memory

### How long does it take for Coworker to become useful?

Coworker starts providing value immediately, but becomes noticeably smarter after a few days of running tasks. As it builds [memory](overview.md#memory) about your services and patterns, its insights become more relevant and its task analysis more accurate.

### Can I clear Coworker's memory?

Please contact support if you need to reset Coworker's [memory](overview.md#memory).

---

## Privacy and data

### What data does Coworker have access to?

Coworker has access to the observability data in your OpsPilot account — metrics, logs, traces, and alert rules. It does not have access to data outside your organisation's account.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
