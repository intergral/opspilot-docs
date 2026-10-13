# About Dashboards

Dashboards combine metric, log, and trace data, along with data from your integrations' data sources, in one place - so you get the full picture of your system on a single screen.

Navigate to **Dashboards** from the left-hand menu in OpsPilot.

---

## Using dashboards

- Open any dashboard from the list to view it.
- **Star** a dashboard to add it to your **Favorites**.
- Use the **time picker** to change the time range for every panel on the dashboard at once.
- Use the **variable dropdowns** along the top of a dashboard - service, environment, host, and the like - to filter every panel to the data you pick. Variables can hold more than one value, and your choices stay in the page address, so a link you share opens the same filtered view.

---

## Integration dashboards

Dashboards with **[OpsPilot - …]** at the end of their name are shipped by integrations. When you install an integration from the [Integrations](../integrations.md) page, its dashboards appear here automatically.

These dashboards are **read-only**. To customize one, make a copy (see [Creating your own](#creating-your-own) below).

---

## Status dots

The dots show whether a folder or dashboard has data behind it. Each folder shows the strongest color of anything inside it, except that a folder holding dashboards made by you or your team is never **No data**.

| Dot | Meaning |
|---|---|
| **Has data** | Has received data in the last two weeks. |
| **No data** | From an integration, with no data in the last two weeks. Hidden until you pick it in the status filter. |
| **Unknown** | Made by you or your team (including any dashboard not in a folder), not checked yet, or from an integration with no activity check. |

---

## Creating your own

| Action | How |
|---|---|
| **Create** | Click **New dashboard** above, then **Add new panel** to pick a data source, metrics, and a chart type. |
| **Import** | In Grafana, choose **New → Import**, then upload or paste a dashboard JSON file. |
| **Copy** | To customize any dashboard, including an integration dashboard, export its JSON and import it again. For a copy of an integration dashboard, first take `integration` out of its tags and **[OpsPilot - …]** out of its title, then import it into a folder of your own - otherwise it is still read as the integration's. The copy is yours to edit. |
| **Save** | Click the disk icon in the top right. Changes aren't saved automatically. |

---

## Organizing

In Grafana, choose **New → New folder** to group dashboards by project, team, or service. Folders show up in the list here.

To move a dashboard, open it, go to **Settings → General → Folder**, choose a folder, and save.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
