# Chat

Coworker works in the background on its own, but you can also talk to it directly. Use the chat to investigate issues, query your telemetry in plain English, and get AI-guided analysis - without writing queries or navigating dashboards by hand.

## Access



Coworker opens by default on login. It can also be reached at any time from the Coworker buttons found throughout the platform.

Type your question in the message box and press **Enter** to send it. Press **Shift+Enter** for a new line instead, so you can write a longer question across several lines without sending it early.

The panel header shows the current thread's name, with a **book** icon for the documentation, a **⋯** menu, and a button to close the panel. The **⋯** menu holds:

| Option | What it does |
|---|---|
| **Set up a task** | Create a task by describing what you want watched |
| **Update preferences** | Change what Coworker shows you by talking to it |
| **All threads** | Open your thread history. See [Threads](#threads) |

The first two open a guided conversation rather than a form, and both reach settings you can also edit directly:

- **Set up a task** opens a thread headed **Task creation**, offering a starting point for each kind of task - *Create a scheduled task to check error rates every hour*, *Watch a service and tell me when something looks off*, or *Listen to a webhook and run a check on every event*. See [Tasks](tasks.md).
- **Update preferences** asks what you want to change - the services you track, the categories and severities you see, your role and team - and updates them as you go. The form version is in [Settings](Settings/overview.md).

## Suggestions

Rather than leaving you with an empty box, Coworker suggests ways to start.

A new conversation opens on **What can I help with?**, with **Get started** cards for the two things people most often want first:

| Card | What it does |
|---|---|
| **Set up a task** | Create a task by describing what you want watched. See [Tasks](tasks.md) |
| **Update preferences** | Change what Coworker shows you by talking to it, rather than filling in a form |

Both open a guided conversation rather than a form - see [the **⋯** menu](#access), which offers the same two.

Above the message box sit suggested questions drawn from what is happening right now. With a situation open they are about that situation - *What's the fastest fix?*, *Should we page someone?*, *Is anything else cascading?* Click one to send it.

You can ignore all of it and type your own question instead.

## Web search

Coworker can search the web when a question needs current information - a version number, a published advisory, a vendor's documentation. This is always available and there is no per-message switch for it.

## Threads

Each conversation with Coworker is a **thread**, and they are all kept. Click the **⋯** menu in the chat panel header and choose **All threads** to open the list.

Threads are grouped by when they happened - **Yesterday** at the top, then by month - and each row shows the thread's name and how long ago it was last used, such as *19h 37m ago* or *2 months ago*. A thread you never named is listed as **New thread**, so it is worth giving the ones you want to come back to a name.

Use **Search** to find a thread by name, or the **calendar** button beside it to narrow the list by date. Click the **✕** to close the panel.

## Voice mode

You can speak a question instead of typing it:

1. Open Coworker, if it is not already open.
2. Click the **microphone** icon in the message box.
3. The first time, your browser asks whether to let OpsPilot use your microphone. Allow it - the browser remembers your choice, so you are not asked again.
4. The panel shows **I'm listening.** and the icon turns **red**. Ask your question - for example, *do I have any errors?*

Your words appear in the message box once you stop speaking, not as you talk - so there is a pause before anything shows up. Wait for it rather than repeating yourself.

!!! tip
    While recording, click the **✕** icon to cancel.

## Images

Attach an image to give Coworker visual context alongside your question - a dashboard you want explained, a stack trace, a graph that looks wrong. Add one in any of three ways:

1. Paste it from your clipboard directly into the message box.
2. Click the **Add image** icon in the message box.
3. Drag and drop it from your file explorer.

## PromQL queries

Coworker can generate and run PromQL queries to answer questions about your metrics. Ask in plain English and it builds and runs the query for you.

## Query specific time frames

Ask for a specific period and Coworker scopes its answer to it - recent performance, anomalies from a particular week, or long-term trends. Useful for pinning down when something changed rather than only what is happening now.



## Sending context to Coworker

You don't have to arrive at the chat with a question already typed. Most places that chart or list your data can hand what you are looking at straight to Coworker, which opens with that context already loaded.

**Metric panels carry an Ask AI button** in their top-right corner, throughout OpsPilot - on Servers, Services, and anywhere else your data is graphed. Click it to send that panel to Coworker for an explanation of the pattern or anomaly in it. See [Metric graph actions](../../Servers/metrics.md#metric-graph-actions) for the icons alongside it.

A few views send richer context than a graph:

| Where | What it sends |
|---|---|
| [Logs](../../Servers/logs.md) | A log entry, for an explanation and troubleshooting suggestions |
| [Traces](../../Services/traces.md) | The whole trace, for analysis of where the time went |

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
