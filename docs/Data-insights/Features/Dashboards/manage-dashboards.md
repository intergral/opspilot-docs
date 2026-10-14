# Manage Dashboards

Once a dashboard exists, you organize it into folders, copy it to customize, and adjust its settings. Browsing and filtering the dashboard list is covered in [About Dashboards](about-dashboards.md).

---

## Organizing into folders

In Grafana, choose **New → New folder** to group dashboards by project, team, or service. Folders then appear in the [All Dashboards](about-dashboards.md) list.

To move a dashboard into a folder, open it, go to **Settings → General → Folder**, choose a folder, and save.

---

## Copying a dashboard

To customize any dashboard - including a read-only [integration dashboard](about-dashboards.md#integration-dashboards) - export its JSON and import it again as your own:

**Step 1** - Open the dashboard and export its JSON (see [Export a dashboard](import-export.md#export-a-dashboard)).

**Step 2** - For an integration dashboard, first remove `integration` from its **tags** and **[OpsPilot - …]** from its **title** - otherwise the copy is still read as the integration's.

**Step 3** - [Import](import-export.md#import-a-dashboard) the JSON into a folder of your own.

The copy is yours to edit.

---

## Dashboard settings

Open **Settings** from the dashboard header to update:

- Name and description
- Folder
- Tags
- Time range defaults and refresh intervals
- Variable definitions (see [Add Variables](add-variables.md))

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
