# Metrics Drilldown

Drill down into metrics to find trends and anomalies.

Navigate to **Metrics Drilldown** from the left-hand sidebar to explore Prometheus-compatible metrics without writing PromQL queries.

![!Screenshot](../../Data-insights/Features/images/metrics-main.png)

---

## Filters

| Filter | Description |
|---|---|
| **Data source** | Select the Metrics data source |
| **Filter by label values** | Narrow metrics by label |
| **Quick search metrics** | Type to search across all available metrics |
| **Sort by** | Order results by Default or other criteria |
| **View** | Switch between Grid and Rows layout |
| **Time range** | Set the window using the picker in the top right |

The total number of matching metrics is shown next to the search bar (e.g., 1613).

---

## Browsing metrics

A dynamic grid of metric panels is displayed, each representing a specific Prometheus metric. Click **Select** on any panel to drill into that metric in more detail.

### Search & filter metrics

Use search and filters to quickly narrow down the metrics you want to investigate - by system, service, or time frame. This helps you focus on what matters most.

To filter:

* Use the **Filter by label values** dropdown to select specific services or tags.
* Or type in the **Quick search metrics** box (e.g., `cpu`), then press **Enter**.

Matching metrics will appear. From here, you can dive deeper into your analysis.


###  Investigate the data

Once you've filtered your metrics, it’s time to analyze the data for patterns or unusual behavior. Understanding your system’s normal (baseline) performance makes it easier to spot issues.

To start:

1. Review the metric panels and look for ones with noticeable changes.

    * Metrics with little variation (e.g., JVM Uptime) are typically less insightful.

    * Focus on dynamic and performance-critical metrics (e.g., CPU Usage, Heap Memory Used, Active JDBC Connections, or Request Throughput) to uncover system trends and potential issues.hat show clear trends.

2. Click **Select** on a metric to view it in more detail.
    
3. Adjust the time range using the time picker in the top right if needed.

4. Use the **Breakdown** and **Related metrics** tabs:

     * **Breakdown:** Visualizes each label-value pair for the selected metric. You can drill down further or add filters directly.
     * **Related metrics:** Lists similar metrics based on keywords. You can continue your analysis from here.

    ![!Screenshot](../../Data-insights/Features/images/select.png)

### Open a metric in Explore

Explore lets you interact with your data in real time. You can build, test, and refine queries without needing to create a dashboard. If your data source supports it, you’ll see results in both graph and table views-perfect for quick and detailed analysis.

To drill deeper into a specific metric using Explore:

1. Click **Select** on the metric panel you want to investigate in more detail.

2. Once the panel expands, click the explore icon in the bottom-right corner of the graph.

    
    ![!Screenshot](../../Data-insights/Features/images/explore-icon.png)

3. This opens the metric in **Explore** view, where you’ll see the full query.

4. From here, you can modify the query, change the time range, and switch between graph and table views to further analyze the data.

    ![!Screenshot](../../Data-insights/Features/images/explore-metrics.png) 

Explore is great for experimenting with queries and uncovering deeper insights-without needing to build a full dashboard.

### Add metrics visualization to a dashboard

1. At the top of the **Explore** page, click **Add to dashboard**.

2. Choose one of the following:

    * New dashboard – to create a new one

    * Existing dashboard – and pick one from the list

3. Click **Open dashboard** to view it.

4. Click **Save dashboard** in the top-right corner.

5. Give your dashboard a name and description, choose a folder (if needed), and click **Save**.

    ![!Screenshot](../../Data-insights/Features/images/save-dashboard.png) 

!!! info "Learn more"
    [Metrics](https://grafana.com/docs/grafana/latest/explore/simplified-exploration/metrics/)