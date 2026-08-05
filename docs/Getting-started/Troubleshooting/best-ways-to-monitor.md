# Best ways to monitor and troubleshoot issues


!!! question
    What are the best dashboards or views in FusionReactor to quickly find performance issues?

There are various views to explore, but we specifically recommend:

- **Server's Metrics tab** – Allows selection of multiple graphs for a comprehensive view.
- **Instance Dashboard** – Found under **Dashboards -> Instances**, providing an overview of instance performance.
- **System Resource Usage Dashboard** – Located at **Dashboards -> System Resource Usage**, offering insights into server resource consumption.
- **Web Applications Dashboard** – Accessible via **Dashboards -> Web Applications**, providing application-specific performance details.

Each of these dashboards can be filtered to show the data most relevant to your needs. You can also add them to **Favourites** for quicker access.

!!! question
    Can we track patterns over time to see if the same request or function keeps causing slowdowns?

Currently, this must be done manually using the monitoring steps outlined above. However, new features in development should improve this process in the future. In the meantime, you can use:

- **[Crash Protection](/Data-insights/Features/Servers/crash-protection/)** (On-premise) to monitor and react to repeated slowdowns.
- **[Anomaly Detection](/Data-insights/Features/Anomaly-Detection/ADoverview/)** (Cloud) to receive alerts when unusual patterns occur.