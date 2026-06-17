# Analytics

The Analytics page gives you a high-level view of your incident history - how quickly your team responds, how incidents are distributed by severity, and which services keep coming back as repeat offenders.

Navigate to **Incidents > Analytics** to open it.

## Summary metrics

Four headline figures appear at the top of the page:

| Metric | Description |
|---|---|
| **Incidents** | Total incidents declared in the selected period |
| **Resolved** | Total incidents resolved in the selected period |
| **MTTR** | Mean time to resolution across all incidents |
| **Open tasks** | Number of tasks currently open across all active incidents |

## Response time metrics

Three panels break down response times by severity (SEV-1 through SEV-4):

**Mean time to acknowledge (MTTA)** - the average time from an incident being declared to it first reaching an acknowledged status. Stamped by the `ack` flag on a status in your configuration.

**Mean time to mitigate (MTTM)** - the average time from declaration to first reaching a mitigated status. Stamped by the `mitigated` flag on a status in your configuration.

**Time to publish post-mortem** - the average time from an incident being resolved to its post-mortem being marked as published.

All three panels show per-severity breakdowns so you can see whether response times differ across SEV-1, SEV-2, SEV-3, and SEV-4 incidents.

## Charts

**Incidents per week by severity** - a time series chart showing incident volume over time, colour-coded by severity.

**By severity** - a breakdown of the total incident count by severity for the selected period.

**Top catalog entries** - the catalog entries most frequently associated with incidents, helping you identify which services generate the most incident activity.

## Repeat offenders

The **Repeat offenders** section surfaces catalog entries that have been associated with three or more incidents in the last 30 days. This is a useful signal for services that may need deeper investigation or longer-term fixes rather than repeated reactive responses.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
