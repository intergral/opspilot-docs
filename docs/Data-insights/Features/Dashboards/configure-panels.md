# Configure Panels

## Edit a panel

After adding a panel to a dashboard, you can open it at any time to update queries, change visualizations, add transformations, or adjust display settings.


**Step 1** — Open the dashboard containing the panel you want to edit.

**Step 2** — Hover over the panel to display the actions menu in the top-right corner.

**Step 3** — Click the menu and select **Edit**.

!!! tip
    Keyboard shortcut: hover over the panel and press **E** to open it directly in edit mode.

---

## Move a panel

**Step 1** — Open the dashboard you want to modify.

**Step 2** — Click and hold the panel title.

**Step 3** — Drag the panel to its new position and release.

---

## Resize a panel

**Step 1** — Open the dashboard containing the panel.

**Step 2** — Click and drag the **lower-right corner** of the panel to adjust its dimensions.

---

## Configure thresholds

A threshold is a value associated with a metric that visually changes how a panel is styled when the value is met or exceeded. Thresholds apply to **Time-series**, **Stat**, **Gauge**, **Geomap**, **Table**, and **State timeline** visualizations.

### Threshold types

| Type | Description |
|---|---|
| **Absolute** | Triggered by a specific numeric value (e.g. 80) |
| **Percentage** | Triggered relative to the min or max value (e.g. 80%) |

**Default thresholds** applied by OpsPilot:

- `80` = red
- `Base` = green (Base represents minus infinity — the default "good" state)
- Mode = Absolute

### Add a threshold

**Step 1** — Edit the panel you want to add a threshold to.

**Step 2** — In the options pane, locate the **Thresholds** section and click **+ Add threshold**.

**Step 3** — Select a color, enter the threshold value, and set the mode (Absolute or Percentage).

!!! info
    For a Time-series panel, also set the **Show thresholds** option to control how the threshold line is displayed.

### Delete a threshold

**Step 1** — Open the panel in edit mode.

**Step 2** — Click the **trash icon** next to the threshold you want to remove.

!!! info
    Deleting a threshold removes it from all visualizations on that panel.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
