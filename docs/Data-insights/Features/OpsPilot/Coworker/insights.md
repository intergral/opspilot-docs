# Insights

**Insights are the core of Coworker** - the raw layer of everything it notices. Every time Coworker investigates an alert, runs a check, or watches a service's health, it records what it finds as an insight: one observation, anomaly, or error pattern. [Situations](situations.md) are the stories built on top of these insights; the **Insights** page is where you can browse every insight directly - the raw layer underneath any active situations.

Navigate to **Coworker > Insights** to open it.

![!Screenshot](../../../../Coworker/insight-overview.png)

The header shows the total insight count, and the **Search insights** box finds one by keyword. Two filter rails on the left narrow the list.

## Filtering

### Severity

Each insight is ranked by severity - **Critical**, **Notable**, or **Info**, from most to least important. Select a severity to show only insights at that level; the count beside each shows how many insights it contains.

### Group

Insights are also grouped by category - for example **application**, **database**, **performance**, **memory-pressure**, **resource-exhaustion**, **baseline-healthy**, **anomaly-detection**, and **error-activity**. Use **Filter groups** to find a group by name, then select one to show only its insights. The count beside each group shows how many insights it holds.

## The insight list

Each row shows:

- A **severity dot** - Critical, Notable, or Info
- The **insight title** - a one-line summary of what Coworker found
- A **count badge** (for example `×243`) - how many times the insight has occurred (its recurrence count)
- The **affected service or group**
- When it was **last seen**

Click any row to open the insight in full.

## Insight detail

![!Screenshot](../../../../Coworker/insight-detail.png)

Opening an insight shows the full write-up:

- **Header** - the severity, category, and affected service, plus the title, occurrence count, and when it was last seen
- **Part of** - if the insight belongs to a situation, a banner links through to that [situation](situations.md)
- **Description** - what Coworker found, with root-cause detail
- **Recommended** - concrete next steps Coworker suggests
- **Evidence** - the supporting signals: exceptions, transaction IDs, and log lines
- **History** - each occurrence of the insight over time. Click **View execution** to see the investigation run that produced it

### Acting on an insight

| Action | Description |
|---|---|
| **Chat** | Open a conversation about the insight, with its full context already loaded |
| **Watch** | Set up a recurring check on the insight - opens the **Watch This Insight** dialog (see below) |
| **Resolve** | Mark the insight resolved |
| **...** | More actions |
| **✕** | Close the detail and return to the list |

### Watching an insight

**Watch** opens the **Watch This Insight** dialog, which schedules a recurring check so Coworker keeps an eye on the insight for you:

![!Screenshot](../../../../Coworker/watch-insight.png)

| Field | Description |
|---|---|
| **Focus** | What each check should focus on - for example, **Verify a fix** |
| **Check every** | How often to run the check - for example, **Daily** |
| **Duration** | How long to keep watching - for example, **1 week** |
| **Model tier** | **Thorough** (more capable, higher cost) or **Efficient** (simpler tasks, lower cost) |

A summary line (for example, *"7 checks over 1 week"*) shows how many checks the schedule adds up to. Click **Start** to begin watching, or **Cancel** to close.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
