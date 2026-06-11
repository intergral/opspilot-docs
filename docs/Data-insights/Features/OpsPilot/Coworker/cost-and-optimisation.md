# Cost and Optimisation

Coworker tracks the cost of running your tasks and gives you full transparency into spend. Click **Usage** from the top right of the dashboard to open the view.

!!! tip
    One of the most effective ways to reduce costs over time is simply to let tasks run. As [task-specific memory](overview.md#memory) builds up, Coworker re-uses context it already knows rather than fetching it fresh on every run, reducing token usage by up to 50% in some cases.

![!Screenshot](/Coworker/cost-optimize.png)

---

## Budget

At the top, the **Task Budget** bar shows your current spend broken down into **Chat**, **Coworker**, and **Projected** segments, with the total tokens used against your budget (e.g. 1,592 / 5,000 tokens). Click **Configure** to open the Budget Settings modal.

![!Screenshot](/Coworker/budget-settings.png)

| Setting | Description |
|---|---|
| **Plan Allowance** | Your total token allowance per month, set by your plan |
| **Monthly task budget** | The percentage of your plan allowance allocated to tasks. Select a preset or use the slider |
| **Warning threshold** | The percentage of your task budget at which Coworker warns you about spend |
| **Halt threshold** | The percentage at which Coworker stops running tasks to prevent overspend |

Below the Task Budget bar, **Total org usage** shows the full organisation-level token consumption including non-task usage.

---

## Usage overview

The **Usage** section shows three key metrics:

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

---

## Per-task analysis

Click through to a specific task to see its full cost breakdown:

![!Screenshot](/Coworker/optimize.png)

| Metric | Description |
|---|---|
| **Avg cost / run** | Average tokens consumed per execution |
| **Total this period** | Tokens used so far, with execution count and percentage of your plan |
| **Projected monthly** | Estimated monthly token usage and number of runs |

The **Cost by Model Tier** section breaks down spend across Efficient and Thorough runs, showing tokens per run, projected monthly cost, and the number of samples for each tier.

A **Cost per Run** chart shows token usage over time so you can spot trends or spikes.

---

## Optimisation suggestions

After a task has run a few times, Coworker automatically reviews its performance and may suggest a small change to reduce cost: running a slow-moving check less often, switching a straightforward task to a lighter model, sharpening its instructions so it does less wasted work, or merging overlapping tasks into one.

Suggestions appear as a **Pending Suggestions** count at the bottom of the Cost & Optimisation panel, and as a numbered badge on the Overview page widget. Each suggestion shows the recommended change, an explanation, and an estimated monthly token saving.

![!Screenshot](/Coworker/optimize-alert.png)

Expand a suggestion to see the full reasoning, including a **Why this suggestion** breakdown of the cost data behind the recommendation.

![!Screenshot](/Coworker/optimize-accept.png)

From here you can:

- **Accept**: apply the change immediately
- **Dismiss**: ignore it. Coworker won't keep pushing the same suggestion.
- **View task config**: review the full task setup before deciding

Suggestions never come at the expense of monitoring quality. Coworker won't suggest anything that would reduce its ability to catch real problems. Where a task is already running efficiently, it will say so.

---

## Auto-accept

Use **Accept all** to apply all current suggestions at once. Enable **Auto-accept** to have Coworker automatically apply future suggestions as they are generated.

Auto-accept is off by default, as most teams prefer to review each suggestion first. Dismiss any suggestion and Coworker won't push the same idea again.

---

## On-demand analysis

Click **Analyse & Optimise** to trigger an on-demand optimisation review at any time. If no optimisations are needed, you'll see a **Looking good!** confirmation.

![!Screenshot](/Coworker/looking-good.png)

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
