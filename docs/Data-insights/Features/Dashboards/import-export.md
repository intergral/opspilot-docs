# Import and Export Dashboards

Dashboards in OpsPilot are stored as JSON. You can export any dashboard to a file and re-import it into the same account or a different one - useful for sharing dashboards across teams or keeping a backup outside the platform.

---

## Export a dashboard

**Step 1** - Open the dashboard you want to export.

**Step 2** - Click **Export** in the dashboard header and choose one of:

- **Export as code** - the dashboard's JSON, which you can copy or save as a `.json` file. Use this to [copy](manage-dashboards.md#copying-a-dashboard) a dashboard or keep a backup.
- **Export as image** - a static image of the dashboard.

---

## Import a dashboard

**Step 1** - Click **+ New dashboard** on the [All Dashboards](about-dashboards.md) page, then **Import dashboard**.

**Step 2** - Import the dashboard in one of three ways:

- **Upload a JSON file** - drag and drop a `.json` or `.txt` file onto **Upload dashboard JSON file**, or click to browse.
- **From grafana.com** - paste a **grafana.com dashboard URL or ID** and click **Load**.
- **Paste JSON** - paste the dashboard's JSON into **Import via dashboard JSON model** and click **Load**.

**Step 3** - Review the dashboard name and folder, update if needed, then click **Import**.

The dashboard is added to your library immediately.

!!! info
    If the imported dashboard references data sources that don't exist in your account, you will be prompted to map them to available sources before the import completes.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
