# Add Variables

Variables make dashboards dynamic. Instead of hard-coding a value like a service name or host into every query, you define a variable once and reference it across all panels. When a user changes the variable value from the dashboard toolbar, all panels update automatically.

---

## Variable types

| Type | Description |
|---|---|
| **Query** | Populates options by running a query against a data source (e.g. all service names from your metrics) |
| **Custom** | A static comma-separated list of values you define manually |
| **Constant** | A fixed, hidden value — useful for shared prefixes or environments |
| **Text box** | A free-text input the user can type into |
| **Interval** | A time interval (e.g. `1m`, `5m`, `1h`) for use in queries |

---

## Add a variable

**Step 1** — Open **Dashboard settings** (cog icon in the header).

**Step 2** — Select **Variables** from the left-hand menu.

**Step 3** — Click **+ Add variable**.

**Step 4** — Configure the variable:

- **Name** — the identifier used in queries (e.g. `$service`)
- **Type** — select from the types above
- **Query** — for Query-type variables, write the query that returns the list of options
- **Multi-value** — enable to allow selecting more than one value at once
- **Include All option** — adds an "All" selection that applies no filter

**Step 5** — Click **Apply** and then **Save dashboard**.

The variable appears as a dropdown in the dashboard toolbar.

---

## Use a variable in a query

Reference a variable in any panel query using the `$variableName` syntax:

```
rate(http_requests_total{service="$service"}[5m])
```

When the user selects a different value from the toolbar, all panels using `$service` automatically re-query with the new value.

---

## Repeating rows with variables

You can configure a dashboard row to repeat for each value of a multi-value variable — useful for creating per-service or per-host breakdowns automatically.

**Step 1** — Click **Dashboards** in the left-side menu and open the dashboard.

**Step 2** — Click **Add** in the header and select **Row**.

!!! info
    If the dashboard is empty, click the **+ Add row** button in the centre of the page.

**Step 3** — Hover over the row title and click the **cog icon**.

**Step 4** — In the **Row Options** dialog, add a title and select the variable to repeat by.

**Step 5** — Click **Update**.

**Step 6** — Include the variable in the row title to give users context (e.g. `$service — Request Rate`).

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
