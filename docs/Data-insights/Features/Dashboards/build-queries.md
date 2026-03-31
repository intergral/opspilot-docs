# Build Queries

Each panel in a dashboard is powered by one or more queries against a data source. The query language depends on the signal type you are querying.

| Signal | Query language | Example use |
|---|---|---|
| **Metrics** | [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) | CPU usage, request rate, error rate |
| **Logs** | [LogQL](https://grafana.com/docs/loki/latest/query/) | Filter and aggregate log lines |
| **Traces** | [TraceQL](https://grafana.com/docs/tempo/latest/traceql/) | Search spans by duration, status, or attribute |

---

## Write a query in the panel editor

**Step 1** — Open a panel in edit mode (hover the panel and press **E**, or select **Edit** from the panel menu).

**Step 2** — In the **Query** tab at the bottom of the editor, select your data source from the drop-down.

**Step 3** — Write your query in the query field. OpsPilot provides syntax hints and auto-complete for supported query languages.

**Step 4** — Click **Refresh** (or the refresh icon) to run the query and preview results in the panel above.

**Step 5** — Click **Apply** to save the query to the panel, or **Save** to persist the entire dashboard.

---

## Multiple queries per panel

You can add more than one query to a single panel. Each query returns a separate series or dataset, and all results are rendered together in the visualization.

Click **+ Add query** below the existing query to add another.

!!! tip
    Use query aliases (the **Legend** field) to give each series a meaningful label in the panel legend.

---

## Switching data sources

The data source can be changed at any time from within the panel editor:

**Step 1** — Open the panel in edit mode.

**Step 2** — In the **Query** tab, click the data source drop-down and select a different source.

The query field resets to match the new data source's query language.

---

## Further reading

- [PromQL basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [LogQL documentation](https://grafana.com/docs/loki/latest/query/)
- [TraceQL documentation](https://grafana.com/docs/tempo/latest/traceql/)
- [Grafana query editor docs](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/)

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
