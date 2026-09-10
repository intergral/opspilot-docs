# Custom Anomaly Detectors

**Custom detectors** let you define anomaly detection against any PromQL query - for the services and metrics that aren't covered by the auto-created [Service Anomaly Detectors](service-anomaly-detectors.md).

Create one from the **Wizard** (**New custom detector**) on the [Status](status.md) or [Rules](rules.md) page, then click **Create detector** to save.

## Signal

Defines the PromQL series the detector watches. The query is validated against the Prometheus datasource on save.

| Field | Description |
|---|---|
| **Query name** | Used as the `query_label` on `ml_anomaly_probability{query_label="..."}`. Letters, digits, `_` or `-` only; must start with a letter or underscore |
| **Aggregator** | How the series is aggregated before scoring (default: `avg`) |
| **Time range** | The lookback window used to train the model. Min 1h, max 7d. Determines model retrain cadence (capped at 15m) |
| **PromQL expression** | The metric series to watch |

## When to fire

The model emits a 0-100% anomaly score. The alert fires if the score stays at or above your threshold for the pending duration.

| Field | Description |
|---|---|
| **Anomaly threshold (probability)** | Slider from 50% to 100%. The alert fires when the score is at or above this value (such as, 95%) |
| **Pending for** | How long the score must stay above the threshold before the alert fires (such as, `5m`) |

## Then notify

Choose which contact points receive alerts from this detector. Click **+ Add** to select a contact point.

Toggle **investigate on fire** to have Coworker automatically investigate when this detector fires.

---

!!! info "Learn more"
    [Anomaly Detection overview](../Anomaly-Detection/ADoverview.md)
