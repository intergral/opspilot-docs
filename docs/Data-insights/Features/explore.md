# Explore: Metrics, Logs and Traces

🔎**Find it**: **FusionReactor** > **Explore** 

<iframe src="https://player.vimeo.com/video/840905546?h=dfe78f4f96" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

**Explore** gives you direct, flexible access to all metrics, logs, and traces in your OpsPilot account. Query raw telemetry, create custom data views, and filter across signals without writing PromQL, LogQL, or TraceQL.

!!! warning
    While with **Explore** you can technically search for any amount of data within your cloud account, there are strict execution times on queries that will restrict performance heavy queries. 

## Datasource selection

Within **Explore** there are three datasource configures. They are accessed using the dropdown located to the left of the screen. The default datasource is **Metrics**.

![](../../Data-insights/Features/images/Dashboards/datasources.png)

- Metrics will contain any metric sent from a FusionReactor agent, plus some additional metrics created within our ingest engine.
- Traces will contain any slow or error transactions sent from a FusionReactor agent, requests viewed in the recent or running tabs of the server view will not appear here as they are not ingested. 
- Logs will contain any logs sent to FusionReactor, either from a FusionReactor agent or log shipper.

!!! note
    Going forward we will allow ingest for traces and metrics from a non FusionReactor agents, however at this time this feature is unavailable.

## Metric queries

🔎**Find it**: **FusionReactor** > **Explore** > **Metrics**

To explore metrics, use the **Metric** browser.

![](../../Data-insights/Features/images/Dashboards/metricsbrowser2.png)

Within the **Metric** browser you can:

- Select one or more metrics to view.

- Filter metrics by any label, such as **instance**, **group** or **application**.

- Execute functions such as **Sum**, **Count**, or **Avg** on metrics.

- Compare metrics by using mathematical functions.

- Combine multiple queries in a single view.

- View data as various chart types, or as raw data in a table.

The metrics browser will create data views for you using [Promql](https://prometheus.io/docs/prometheus/latest/querying/basics/).

Using Promql directly you can create powerful and complex queries to get the most out of your FusionReactor data.

## Trace queries

🔎**Find it**: **FusionReactor** > **Explore** > **Traces** > **Search**

To explore traces we advise using the **Search** feature.

![](../../Data-insights/Features/images/Dashboards/tracemain.png)

Within search, you can specify:

|Type      | Description     |
|--------------|-----------|
| Service Name | Instance from which the trace originates.|
| Span Name | The URL or action of a transaction.|
| Tag | A label applied to a trace, for example ```txnId``` or ```status.code```. A full list of tags can be searched within the input field.|
| Min Duration | The minimum duration of a transaction. |
| Max Duration | The maximum duration of a transaction. |
|Limit | How many results you wish to view.|

You can view the trace information by clicking on the trace ID, which will open a window on the right of the screen.

![](../../Data-insights/Features/images/Dashboards/trace.png)

## Log queries

🔎**Find it**: **FusionReactor** > **Explore** > **Logs**

To explore logs, use the **Logs** browser.

The **Logs** browser allows you to filter and view any ingested logs.

![](../../Data-insights/Features/images/Dashboards/logsmain.png)

  

The log browser lets you:  

- Filter logs by labels like **job**, **filename** or **instance**.

- Perform calculations like **Sum**, **Count**, or **Avg** to extract metrics from logs.  

- Combine multiple queries in one view.  

- Display data as charts or raw tables.  

The browser automatically builds log queries and generates [LogQL](https://grafana.com/docs/loki/latest/logql/) for you.  

You can also use **Explore** to run custom LogQL queries.  

!!! info
    LogQL, developed by Grafana Labs, is a query language for filtering, searching, and generating metrics from log data.  



### LogQL examples
#### Search for logs with a specific job

!!! example
    ````{job="job1"}````



#### Search for specific filename

!!! example
    ````{filename=~"request"}````



#### Search for logs with a job using wildcard

!!! example
    ````{job=~"job.*"}````

#### Search for any stdout or stderr logs for any jobs matching the wildcard

!!! example
    ````{job=~"job.*",filename=~"std.*"}````


#### Query for the volume of jobs per job and instance

!!! example
    ````sum(count_over_time({job=~".+"}[5m])) by (job,instance)````

#### Query for the top IP addresses triggering requests in FusionReactor

!!! example
    ````topk(10,sum by (clientAddress)(rate({filename="request"} | logfmt | line_format "{{.clientAddress}}" | __error__="" [1m])))````

#### Query nginx for the top IP address hitting the load balancer

!!! example
    ````topk(10,sum by (remote_address)(rate({filename="/opt/access.log"} | logfmt | line_format "{{.remote_address}}" | __error__="" [1m])))````

#### Search all logs for the text exception

!!! example
    ````{ job=~".+"} |= "Exception"````

#### Process the request log for top hit page URLs

!!! example
    ````sum by (url)(rate({filename="request"} | logfmt | line_format "{{.url}}" | __error__="" [10s]))````

#### Graph the number of error or exception error lines   

!!! example
    ````sum by (job) (count_over_time({job=~"store-.*"} |= "error" != "exception" [5m]))````


#### Process the avg CPU time per page URL

!!! example
    ````topk(10, sum by (url)(avg_over_time({ filename="request"} | logfmt | __error__="" | unwrap cpuTime[5m])))````


#### Graph previous crashes caused by OutOfMemory errors 

!!! example
    ````sum by (job) (count_over_time({job=~".+"} |= "java.lang.OutOfMemory" [1m]))````

___

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
