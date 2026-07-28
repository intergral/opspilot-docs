# Service Anomaly Detectors

Picking the right threshold is hard - too tight and you drown in false alarms, too loose and you miss the real problem. **Service anomaly detectors** flag unusual behaviour in your instrumented services automatically, so you get meaningful alerts without hand-tuning numbers. Navigate to **Alerting > Service Anomaly Detectors** to open the list.

Service detectors are auto-created from your instrumented services using templates. Alerts fire when the anomaly probability stays above the configured threshold for the pending duration.

Each instrumented service automatically gets detectors for:

- **Rate** - request rate anomalies
- **Error** - error rate anomalies
- **Latency** - response time anomalies

## Scanning for services

Click **Scan for services** to detect your instrumented services and auto-create detectors for them. If no service detectors exist yet, this is the first step.

## State counters

| State | Description |
|---|---|
| **Firing** | The anomaly condition is currently met |
| **Pending** | The condition is met but the pending duration has not elapsed |
| **Normal** | The detector is evaluating and no anomaly is detected |
| **No Data** | The detector has no data to evaluate |
| **Paused** | The detector is paused and not evaluating |

## Filtering the list

- **Search services** - find detectors by service name
- **All states** - filter by current state
- **All contact points** - filter by the contact point the detector routes to
- Set the **auto-refresh interval** (such as, `30s`) or refresh manually using the controls next to **Scan for services**
- Switch between **Table** and **Tiles** view using the toggle in the top right

!!! info "Learn more"
    [Anomaly Detection overview](../Anomaly-Detection/ADoverview.md)

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
