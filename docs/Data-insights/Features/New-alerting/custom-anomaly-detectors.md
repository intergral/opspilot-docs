# Custom Anomaly Detectors

Custom anomaly detectors let you define anomaly detection against any PromQL query - useful when the signal you care about isn't one of the automatic [service detectors](service-anomaly-detectors.md). Navigate to **Alerting > Custom Anomaly Detectors** to open the list.

## The detectors list

The list shows your custom detectors with state counters at the top:

| State | Description |
|---|---|
| **Firing** | The anomaly condition is currently met |
| **Pending** | The condition is met but the pending duration has not elapsed |
| **Normal** | The detector is evaluating and no anomaly is detected |
| **No Data** | The detector has no data to evaluate |
| **Paused** | The detector is paused and not evaluating |

- **Search detectors** - find a detector by name
- **All states** - filter by current state
- **All contact points** - filter by the contact point the detector routes to
- Set the **auto-refresh interval** (such as, `30s`) or refresh manually

Before you add any, the list shows *"No custom detectors yet."*

## Creating a custom detector

Click **+ New custom detector** to open the creation page, then click **Create detector** to save.

### Signal

Defines the PromQL series the detector watches. The query is validated against the Prometheus datasource on save.

| Field | Description |
|---|---|
| **Query name** | Used as the `query_label` on `ml_anomaly_probability{query_label="..."}`. Letters, digits, `_` or `-` only; must start with a letter or underscore |
| **Aggregator** | How the series is aggregated before scoring (default: `avg`) |
| **Time range** | The lookback window used to train the model. Min 1h, max 7d. Determines model retrain cadence (capped at 15m) |
| **PromQL expression** | The metric series to watch |

### When to fire

The model emits a 0-100% anomaly score. The alert fires if the score stays at or above your threshold for the pending duration.

| Field | Description |
|---|---|
| **Anomaly threshold (probability)** | Slider from 50% to 100%. The alert fires when the score is at or above this value (such as, 95%) |
| **Pending for** | How long the score must stay above the threshold before the alert fires (such as, `5m`) |

### Then notify

Choose which contact points receive alerts from this detector. Click **+ Add** to select a contact point.

Toggle **investigate on fire** to have Coworker automatically investigate when this detector fires.

!!! info "Learn more"
    [Anomaly Detection overview](../Anomaly-Detection/ADoverview.md)

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
