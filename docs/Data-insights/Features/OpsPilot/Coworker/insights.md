# Insights

**Insights are the core of Coworker** - every observation, anomaly, and error pattern it records while investigating. [Situations](situations.md) are the curated stories Coworker builds from them and surfaces in your feed; the **Insights** page is the complete, unfiltered layer underneath.

Come here when you want the full picture rather than only what Coworker chose to raise: browse everything it has noticed, filter to a specific service or category, catch patterns before they escalate into a situation, and see how often each has recurred. It's the ground truth of what Coworker has seen.

Navigate to **Coworker > Insights** to open it.

![!Screenshot](../../../../Coworker/insight-overview.png)

The header shows the total insight count, and the **Search insights** box finds one by keyword. The filter rails on the left narrow the list by severity, group, age, and service.

## Filtering

### Severity

Each insight is ranked by severity - **Critical**, **Notable**, or **Info**, from most to least important. Select a severity to show only insights at that level; the count beside each shows how many insights it contains.

### Group

Insights are also grouped by category - for example **application**, **database**, **performance**, **memory-pressure**, **resource-exhaustion**, **baseline-healthy**, **anomaly-detection**, and **error-activity**. Use **Filter groups** to find a group by name, then select one to show only its insights. The count beside each group shows how many insights it holds.

### Age

Filter by how recently an insight was last seen - **Last 24h**, **Last 7 days**, or **Last 30 days**. The count beside each shows how many insights fall within that window.

### Service

Filter to a specific affected service. Use **Filter services** to find one by name, then select it to show only that service's insights. The count beside each shows how many insights it has.

## The insight list

Each row shows:

- A **severity dot** - Critical, Notable, or Info
- The **insight title** - a one-line summary of what Coworker found
- A **count badge** (for example `×4`) - how many times the insight has occurred (its recurrence count)
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
| **Chat** | Open quick actions and a conversation about the insight, with its full context already loaded (see below) |
| **Watch** | Set up a recurring check on the insight - opens the **Watch This Insight** dialog (see below) |
| **Resolve** | Mark the insight resolved |
| **...** | More actions: **Hide similar** (stop surfacing insights like this one) and **Not right** (tell Coworker the insight is off the mark, so it learns) |
| **✕** | Close the detail and return to the list |

### Chatting about an insight

**Chat** opens a menu of quick actions, each sending the insight to Coworker with its full context already loaded:

![!Screenshot](../../../../Coworker/insight-chat.png)

| Action | Description |
|---|---|
| **Is this still an issue?** | Checks the current state to see if the problem is ongoing or resolved |
| **Investigate root cause** | Kicks off a root cause analysis |
| **Create a ticket** | Creates a ticket for the issue |
| **Suggest a fix** | Recommends remediation steps or best practices |
| **Discuss this insight** | Opens a free-form conversation about the insight |

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
