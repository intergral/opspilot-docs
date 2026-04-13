

# User Guide

OpsPilot is an AI assistant built into the OpsPilot platform. Ask questions in plain English to get insights about your applications, infrastructure, and logs — without needing to write queries or navigate dashboards manually.



<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/871379062?badge=0&amp;autopause=0&amp;quality_selector=1&amp;progress_bar=1&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="OpsPilot Assistant"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>



## Access

![!Screenshot](/Data-insights/Features/OpsPilot/images/OPmain.png)

OpsPilot opens by default on login. It can also be accessed at any time via the OpsPilot integration buttons found throughout the platform.


## Web Search Toggle



OpsPilot now includes a feature that allows users to **enable or disable web search** when asking questions. This gives you better control over how your queries are handled - especially when working with private or internal information.

### Where to find it

In the assistant chat bar (bottom of the screen), there is a **globe icon** next to the microphone button. This icon is the **web Search Toggle**.



![!Screenshot](/Data-insights/Features/OpsPilot/images/web-search.png)

### How it works

- **Enabled:** OpsPilot will use **live web search** to help answer your question with up-to-date information.

- **Disabled:** OpsPilot will only use internal knowledge and the connected knowledge base - no external web queries are made.




### Why this matters

This feature was added primarily for **privacy control**. While web search is helpful, there may be cases where you might not want your input interpreted as a search (e.g., asking about passwords, credentials, or internal topics). With the toggle off, your message won't be used for any web searches.


### Best practice

- For **internal, private, or sensitive questions** → Keep web search **OFF**.

- For **general knowledge or live information** → Toggle web search **ON**.



## Suggestions

When you start a new conversation, OpsPilot displays a set of **Suggestions** — pre-built questions based on common observability scenarios. Clicking a suggestion sends it directly as your first message, giving you a fast starting point without needing to type anything.

Suggestions cover areas such as errors, performance, network latency, and database health. You can also ignore them entirely and type your own question in the message box at the bottom of the screen.

## Conversations

Click the **Conversations** icon to view and search your previous OpsPilot conversations, grouped by date.

![!Screenshot](/Data-insights/Features/OpsPilot/images/history.png)

## Voice mode

OpsPilot allows you to send a voice message instead of typing your query. This is yet another time-saving feature of the assistant. 

Using voice mode:

1. Open OpsPilot (if not already open by default).

2. Click the blue microphone icon.

3. Wait for the 'I'm listening' written response.

4. Ask OpsPilot your question. For example, 'Do I have any errors?'

!!! tip
    While recording a question, you can click the X icon to cancel it.

## OpsPilot Vision

You can upload images to give OpsPilot visual context alongside your questions. Images can be added in three ways:

1. Paste an image from your clipboard directly into the message box.
2. Click the **Attach Image** button in the bottom left corner.
3. Drag and drop an image from your file explorer.




## PromQL queries


<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/901201832?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="PromQL Queries: OpsPilot"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

OpsPilot can generate and execute PromQL queries to answer questions about your metrics. Type your question in plain English and OpsPilot will build and run the query for you.

![!Screenshot](/Data-insights/Features/OpsPilot/images/promql.png)

Type `/` to see a list of available commands.


![!Screenshot](/Data-insights/Features/OpsPilot/images/commands.png)


![!Screenshot](/Data-insights/Features/OpsPilot/images/activity.png)







## Query specific time frames 

Whether you need to scrutinize recent performance data, investigate anomalies from a particular week, or review long-term trends, OpsPilot is at your service. Simply request information for the time frame of your choice, and OpsPilot swiftly generates insights tailored to that period. This feature ensures that you have the flexibility to focus on the time intervals that matter most to your monitoring and analysis efforts, empowering you to pinpoint issues, track progress, and make data-driven decisions with precision and confidence.


![!Screenshot](/Data-insights/Features/OpsPilot/images/timeframe.png)

## FusionReactor integration points

Wherever you see the blue **OpsPilot AI** button in the FusionReactor UI, you can send that context directly to OpsPilot for analysis.

### Error context

🔎 **FusionReactor** > **Applications** > **Errors** > **Trace** > **Error Snapshot**

Click the OpsPilot AI button to send error details to OpsPilot. It will explain the method, identify potential causes, and suggest fixes.

![!Screenshot](/Data-insights/Features/OpsPilot/images/code1.png)

### Code helper

Highlight any decompiled code and right-click to access three options:

- **Debug code** — flags potential error causes
- **Explain code** — explains what the code does
- **Suggest optimization** — recommends readability and performance improvements

![!Screenshot](/Data-insights/Features/OpsPilot/images/codehelp1.png)

### Profile

🔎 **FusionReactor** > **Applications / Servers** > **Tracing** > **Trace** > **Profile**

Sends profile data to OpsPilot for an explanation of where issues may be located.

![!Screenshot](/Data-insights/Features/OpsPilot/images/profile1.png)

### Log explain

🔎 **FusionReactor** > **Logging** > **Logs**

Click the OpsPilot AI button next to a log entry to get an explanation of what caused it and suggested fixes.

![!Screenshot](/Data-insights/Features/OpsPilot/images/logexplain.png)

### Stack trace

🔎 **FusionReactor** > **Applications / Servers** > **Tracing** > **Trace** > **Error Output**

Click the OpsPilot AI button next to an error to get insight into the stack trace and potential causes.

![!Screenshot](/Data-insights/Features/OpsPilot/images/stacktrace1.png)

___

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.