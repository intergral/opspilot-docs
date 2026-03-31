# Create a Dashboard

Custom dashboards allow you to curate specific datasets into a single, cohesive view. Whether you are monitoring high-level infrastructure health or debugging a specific microservice, dashboards provide the visual context needed to make informed decisions.

!!! note
    Custom dashboard creation is available on **all** FusionReactor plans.

## Before you start

- **Permissions** — ensure your user profile has the necessary permissions to create and edit dashboards.
- **Query knowledge** — familiarise yourself with the query language of your target data source (LogQL for logs, PromQL for metrics, or TraceQL for traces).

---

## Steps

<div class="video-wrapper">
  <iframe src="https://player.vimeo.com/video/893302849?badge=0&autopause=0&player_id=0&app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="How to create a FusionReactor dashboard"></iframe>
</div>

**Step 1** — Select **Dashboards** from the navigation menu.

**Step 2** — Click **New** in the top-right corner and select **New dashboard**.

**Step 3** — On the empty dashboard, click **+ Add visualization**.

![Screenshot](/Getting-started/Tutorials/step3.png)

**Step 4** — In the dialog box that opens, do one of the following:

- Select one of your existing data sources.
- Select one of the built-in special data sources.
- Click **Configure a new data source** to set up a new one (Admins only).

![Screenshot](/Getting-started/Tutorials/step4.png)

!!! info
    The **Edit panel** view initially displays your chosen data source. You can modify the panel data source at any time using the drop-down in the **Query** tab.

**Step 5** — Construct a query in the query language of your data source.

**Step 6** — Select the **Refresh dashboard** icon to query the data source.

![Screenshot](/Getting-started/Tutorials/step6.png)

**Step 7** — In the visualization list, select a visualization type.

![Screenshot](/Getting-started/Tutorials/step7.png)

**Step 8** — Under **Panel options**, enter a title and description for your panel.

**Step 9** — Adjust panel settings as needed. Refer to the following for options:

- [Configure value mappings](https://grafana.com/docs/grafana/latest/panels-visualizations/configure-value-mappings/)
- [Visualization-specific options](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/)
- [Override field values](https://grafana.com/docs/grafana/latest/panels-visualizations/configure-overrides/)
- [Configure thresholds](/Data-insights/Features/Dashboards/configure-panels/#configure-thresholds)
- [Configure standard options](https://grafana.com/docs/grafana/latest/panels-visualizations/configure-standard-options/)

**Step 10** — Click **Save** to save the dashboard, or **Apply** to preview changes first, then save via the dashboard header.

**Step 11** — Enter a summary of your dashboard changes.

**Step 12** — Enter a title and select a folder.

!!! info
    We recommend saving custom dashboards to the **General** folder.

**Step 13** — Select **Save**.

**Step 14** — To add more panels, click **Add** in the dashboard header and select **Visualization**.

![Screenshot](/Getting-started/Tutorials/add.png)

---

## Visualization types

OpsPilot offers a variety of visualizations to support different use cases.

### Graphs & charts

| Type | Description |
|---|---|
| [Timeseries](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/time-series/) | Default graph visualization for time-based data. |
| [State timeline](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/state-timeline/) | For state changes over time. |
| [Status history](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/status-history/) | For periodic state over time. |
| [Bar chart](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/bar-chart/) | Shows any categorical data. |
| [Histogram](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/histogram/) | Calculates and shows value distribution in a bar chart. |
| [Heatmap](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/heatmap/) | Visualizes data in two dimensions, typically for magnitude of a phenomenon. |
| [Pie chart](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/pie-chart/) | Typically used where proportionality is important. |
| [Candlestick](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/candlestick/) | Typically for financial data where the focus is price/data movement. |

### Stats & numbers

| Type | Description |
|---|---|
| Stat | Big stat display with optional sparkline. |
| Bar gauge | Horizontal or vertical bar gauge. |

!!! info "Learn more"
    See the [Grafana visualization docs](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/) for the full list of available types.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
