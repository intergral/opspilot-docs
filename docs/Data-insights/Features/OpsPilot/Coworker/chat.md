# Chat

Coworker works in the background on its own, but you can also talk to it directly. Use the chat to investigate issues, query your telemetry in plain English, and get AI-guided analysis - without writing queries or navigating dashboards by hand.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/871379062?badge=0&amp;autopause=0&amp;quality_selector=1&amp;progress_bar=1&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="OpsPilot Coworker"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## Access

![!Screenshot](/Data-insights/Features/OpsPilot/images/OPmain.png)

Coworker opens by default on login. It can also be reached at any time from the Coworker buttons found throughout the platform.

## Web Search Toggle

You can **enable or disable web search** when asking a question. This gives you control over how your queries are handled, which matters when you are working with private or internal information.

### Where to find it

In the chat bar at the bottom of the screen there is a **globe icon** next to the microphone button. That is the web search toggle.

![!Screenshot](/Data-insights/Features/OpsPilot/images/web-search.png)

### How it works

- **Enabled** - Coworker uses live web search to help answer your question with up-to-date information.
- **Disabled** - Coworker uses only internal knowledge and the connected knowledge base. No external web queries are made.

### Why this matters

This exists for privacy control. Web search is useful, but there are cases where you would not want your input interpreted as a search - asking about passwords, credentials, or internal topics. With the toggle off, your message is not used for any web search.

### Best practice

- Internal, private, or sensitive questions - keep web search **off**
- General knowledge or live information - turn web search **on**

## Suggestions

When you start a new conversation, Coworker offers a set of **Suggestions** - pre-built questions covering common observability scenarios such as errors, performance, network latency, and database health. Clicking one sends it as your first message, so you have a starting point without typing.

You can ignore them entirely and type your own question instead.

## Conversations

Click the **Conversations** icon to view and search your previous conversations, grouped by date.

![!Screenshot](/Data-insights/Features/OpsPilot/images/history.png)

## Voice mode

You can speak a question instead of typing it:

1. Open Coworker, if it is not already open.
2. Click the blue microphone icon.
3. Wait for the **I'm listening** response.
4. Ask your question - for example, *do I have any errors?*

!!! tip
    While recording, click the **✕** icon to cancel.

## OpsPilot Vision

You can upload images to give Coworker visual context alongside your question. Add an image in any of three ways:

1. Paste it from your clipboard directly into the message box.
2. Click **Attach Image** in the bottom left corner.
3. Drag and drop it from your file explorer.

## PromQL queries

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/901201832?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="PromQL Queries: OpsPilot"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

Coworker can generate and run PromQL queries to answer questions about your metrics. Ask in plain English and it builds and runs the query for you.

![!Screenshot](/Data-insights/Features/OpsPilot/images/promql.png)

Type `/` to see the available commands.

![!Screenshot](/Data-insights/Features/OpsPilot/images/commands.png)

![!Screenshot](/Data-insights/Features/OpsPilot/images/activity.png)

## Query specific time frames

Ask for a specific period and Coworker scopes its answer to it - recent performance, anomalies from a particular week, or long-term trends. Useful for pinning down when something changed rather than only what is happening now.

![!Screenshot](/Data-insights/Features/OpsPilot/images/timeframe.png)

## FusionReactor integration points

Wherever you see the blue **OpsPilot AI** button in the FusionReactor UI, you can send that context straight to Coworker for analysis.

### Error context

🔎 **FusionReactor** > **Applications** > **Errors** > **Trace** > **Error Snapshot**

Sends error details to Coworker, which explains the method, identifies potential causes, and suggests fixes.

![!Screenshot](/Data-insights/Features/OpsPilot/images/code1.png)

### Code helper

Highlight any decompiled code and right-click for three options:

- **Debug code** - flags potential error causes
- **Explain code** - explains what the code does
- **Suggest optimization** - recommends readability and performance improvements

![!Screenshot](/Data-insights/Features/OpsPilot/images/codehelp1.png)

### Profile

🔎 **FusionReactor** > **Applications / Servers** > **Tracing** > **Trace** > **Profile**

Sends profile data to Coworker for an explanation of where issues may be located.

![!Screenshot](/Data-insights/Features/OpsPilot/images/profile1.png)

### Log explain

🔎 **FusionReactor** > **Logging** > **Logs**

Click the button next to a log entry for an explanation of what caused it, and suggested fixes.

![!Screenshot](/Data-insights/Features/OpsPilot/images/logexplain.png)

### Stack trace

🔎 **FusionReactor** > **Applications / Servers** > **Tracing** > **Trace** > **Error Output**

Click the button next to an error for insight into the stack trace and potential causes.

![!Screenshot](/Data-insights/Features/OpsPilot/images/stacktrace1.png)

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
