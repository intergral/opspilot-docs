# Anomaly Detectors

Picking the right threshold is hard - too tight and you drown in false alarms, too loose and you miss the real problem. **Anomaly Detectors** flag unusual behaviour in your services automatically, so you get meaningful alerts without hand-tuning numbers. Navigate to **Alerting > Anomaly Detectors** to open it.

The page has two tabs: **Service detectors** and **Custom detectors**.

---

## Service detectors

Service detectors are auto-created from your instrumented services using templates. Alerts fire when the anomaly probability stays above the configured threshold for the pending duration.

Each instrumented service automatically gets detectors for:

- **Rate** - request rate anomalies
- **Error** - error rate anomalies
- **Latency** - response time anomalies

### Scanning for services

Click **Scan for services** to detect your instrumented services and auto-create detectors for them. If no service detectors exist yet, this is the first step.

### State counters

| State | Description |
|---|---|
| **Firing** | The anomaly condition is currently met |
| **Pending** | The condition is met but the pending duration has not elapsed |
| **Normal** | The detector is evaluating and no anomaly is detected |
| **No Data** | The detector has no data to evaluate |
| **Paused** | The detector is paused and not evaluating |

### Filtering the list

- **Search services** - find detectors by service name
- **All states** - filter by current state
- **All contact points** - filter by the contact point the detector routes to
- Switch between **Table** and **Tiles** view using the toggle in the top right

---

## Custom detectors

Custom detectors let you define anomaly detection rules against any PromQL query. Click **+ New custom detector** to open the creation page, then click **Create detector** to save.

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

---

!!! info "Learn more"
    [Anomaly Detection overview](../Anomaly-Detection/ADoverview.md)
