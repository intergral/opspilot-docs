# Custom Anomaly Detectors

Custom detectors run anomaly detection on any PromQL series you define. The model emits an anomaly probability (0-100%), and alerts fire when that probability stays above your configured threshold for the pending duration. Unlike the auto-created [Service Anomaly Detectors](service-anomaly-detectors.md), you define these against your own queries.

Navigate to **Alerting > Custom Anomaly Detectors** to open the page.

## The detectors list

Your custom detectors are listed with the same state counters as service detectors - **Firing**, **Pending**, **Normal**, **No Data**, and **Paused**. Use **Search detectors** to find one, and the **All states** and **All contact points** dropdowns to filter. The **OpsPilot** dropdown offers AI shortcuts. Until you add one, the page shows *"No custom detectors yet."*

Each detector row shows its **State**, **Name**, **Threshold**, and **Last evaluation**, plus actions: a notification count, an **Active** toggle, **Open dashboard**, **Tune detector** (edit), and **Delete**.

## Creating a custom detector

Click **+ New custom detector** (top right of the page), or use the **Wizard** (**New custom detector**) on the [Status](status.md) or [Rules](rules.md) page. Fill in the fields below, then click **Create detector** to save.

### Signal

Defines the PromQL series the detector watches. The query is validated against the Prometheus datasource on save.

| Field | Description |
|---|---|
| **Query name** | Required. Used as the `query_label` on `ml_anomaly_probability{query_label="..."}`. Letters, digits, `_` or `-` only; must start with a letter or underscore |
| **Aggregator** | How the series is aggregated before scoring (default: `avg`) |
| **PromQL expression** | The metric series to watch. Build it in **Builder** mode (*Watch [metric]*, with optional **aggregate** and **filter**), or switch to **Code** to write PromQL directly |

### When to fire

The model emits a 0-100% anomaly score. The alert fires if the score stays at or above your threshold for the pending duration.

| Field | Description |
|---|---|
| **Anomaly threshold (probability)** | Slider from 50% to 100%. The alert fires when the score is at or above this value (such as, 95%) |
| **Pending for** | How long the score must stay above the threshold before the alert fires (such as, `5m`) |

### Then notify

Choose which contact points receive alerts from this detector. Click **+ Add** to select a contact point.

Toggle **investigate on fire** to have Coworker automatically investigate when this detector fires.

---

!!! info "Learn more"
    [Anomaly Detection overview](../Anomaly-Detection/ADoverview.md)
