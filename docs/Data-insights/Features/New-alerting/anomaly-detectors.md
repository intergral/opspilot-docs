# Anomaly Detectors

Picking the right threshold is hard - too tight and you drown in false alarms, too loose and you miss the real problem. **Anomaly Detectors** flag unusual behaviour in your services automatically, so you get meaningful alerts without hand-tuning numbers. Navigate to **Alerting > Anomaly Detectors** to open it.

The page has two tabs: **Service detectors** and **Custom detectors**.

---

## Service detectors

Service detectors are auto-created from your instrumented services. Each service is watched across three signals, shown as **R**, **E**, and **D** badges on its row:

- **Rate (R)** - request-rate anomalies
- **Error (E)** - error-rate anomalies
- **Duration (D)** - response-time (latency) anomalies

An alert fires when the anomaly probability stays above the configured threshold for the pending duration.

### Scanning for services

Click **Scan for services** (top right) to detect your instrumented services and auto-create detectors for them. If no service detectors exist yet, this is the first step.

### The service table

Each row is one service. Use the **Search** box to find a service by name, and the **filter** control in the top right to narrow the list.

| Column | Description |
|---|---|
| **Expand** | Open the row to configure each signal individually (see [Configuring a signal](#configuring-a-signal)) |
| **Service** | The service name |
| **Anomaly Detection** | Master toggle to turn detection on or off for the service, alongside the **R / E / D** signals it covers |
| **Status** | The detector's current state (see below) |
| **Contact Points** | Assign one or more contact points to route this service's alerts to |
| **Investigate** | Toggle to have Coworker automatically investigate when the service's detectors fire |
| **Actions** | Open the detector's detail view, or delete it |

### Configuring a signal

Expanding a service row reveals the settings for each signal (Rate, Error, Duration), split into query settings and alert settings:

| Setting | Description |
|---|---|
| **Time Range** | The lookback window used to train the model (e.g. `1d`) |
| **Threshold** | Slider from 50% to 100%. The alert fires when the anomaly score is at or above this value (e.g. 95) |
| **Pending For** | How long the score must stay at or above the threshold before the alert fires (e.g. `5m`) |

Click **Apply Changes** to save.

### Detector states

| State | Description |
|---|---|
| **Firing** | The anomaly condition is currently met |
| **Pending** | The condition is met but the pending duration has not elapsed |
| **Normal** | The detector is evaluating and no anomaly is detected |
| **No Data** | The detector has no data to evaluate |
| **Paused** | The detector is paused and not evaluating |

---

## Custom detectors

Custom detectors let you define anomaly detection against any PromQL query. Existing detectors are listed in a table, and you create new ones with **Add custom detector**.

### The custom detector table

Each row is one custom detector. Use the **Search** box and the **filter** control to narrow the list.

| Column | Description |
|---|---|
| **Expand** | Open the row to view and edit the detector's settings (the same fields as [Creating a custom detector](#creating-a-custom-detector)) |
| **Query Label** | The detector's name (the `query_label` on its metric) |
| **Anomaly Detection** | Toggle to turn the detector on or off |
| **Status** | The detector's current state (see [Detector states](#detector-states)) |
| **Contact Points** | Assign one or more contact points to route this detector's alerts to |
| **Actions** | Open the detector's detail view, or delete it |

### Creating a custom detector

Click **Add custom detector** to open the creation page, then **Create detector** to save. It has three sections:

**Signal** - defines the PromQL series the detector watches. The query is validated against the Prometheus datasource on save.

| Field | Description |
|---|---|
| **Query name** | Used as the `query_label` on `ml_anomaly_probability{query_label="..."}`, and must be unique per detector. Letters, digits, `_` or `-` only; must start with a letter or underscore |
| **Aggregator** | How the series is aggregated before scoring (default: `avg`) |
| **Time range** | The lookback window used to train the model. Min 1h, max 7d. Determines model retrain cadence (capped at 15m) |
| **PromQL expression** | The metric series to watch |

**When to fire** - the model emits a 0-100% anomaly score. The alert fires if the score stays at or above your threshold for the pending duration.

| Field | Description |
|---|---|
| **Anomaly threshold (probability)** | Slider from 50% to 100%. The alert fires when the score is at or above this value (such as, 95%) |
| **Pending for** | How long the score must stay above the threshold before the alert fires (such as, `5m`) |

**Then notify** - choose which contact points receive alerts from this detector. Click **+ Add** to select a contact point. Toggle **investigate on fire** to have Coworker automatically investigate when this detector fires.

---

!!! info "Learn more"
    [Anomaly Detection overview](../Anomaly-Detection/ADoverview.md)
