

# Post-crash Troubleshooting with OpsPilot

## Overview

This guide explains how to use **OpsPilot** to diagnose and prevent application server crashes. It includes steps to identify root causes using memory metrics, transaction traces, and logs, followed by setting up proactive alerts.

!!! info 
    While this guide highlights a memory-related example, the same process can help uncover other root causes like CPU saturation, slow database calls, or blocked threads.

---

## Video

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1089031476?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Investigating Server Crashes with OpsPilot"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


---

## Key features for crash investigation

| Feature                 | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Historic Metrics**    | Retained for **13 months** - accessible even after server restarts.         |
| **Traces & Logs**       | Stored for **30 days** - detailed transaction-level visibility.             |
| **Anomaly Detection**   | Uses R.E.D. metrics to automatically flag unusual application behavior.     |
| **Custom Alerts**       | User-defined thresholds for memory, latency, CPU, and uptime monitoring.    |

---

## Example scenario

An application server (e.g., **Storefront 1**) is crashing intermittently. The goal is to:

1. Investigate the cause using OpsPilot.  
2. Prevent future crashes with proactive monitoring.

This example focuses on memory issues, but the same steps apply when diagnosing other causes such as CPU pressure or database slowdowns.

---

## Step 1: Spot the issue

1. Open the affected server in **OpsPilot**.
2. Use the **Live Mode Clock** to select a custom time range (e.g., last 6 hours).
3. The time filter syncs across:
    - Metrics  
    - Transactions  
    - JDBC calls  
    - Logs  


### What to look for

- Inspect the **Used Heap Memory** graph.
- Look for sharp spikes, followed by sudden drops or gaps, in the graph.
- Also check for anomalies in:
    - **CPU usage**
    - **GC activity**
    - **Thread states**

![!Screenshot](../../Getting-started/Tutorials/metrics.png)

---

## Step 2: Isolate the root cause

1. Navigate to the **Transactions** tab.
2. Select **Saved in Cloud** to access stored transaction history.
3. Sort by **Duration** to identify slow or abnormal requests.

### Signs of trouble

- A normally fast transaction (e.g., `Checkout`) starts taking significantly longer.
- Specific outliers (e.g., `Store Cache`) may be consuming **excessive memory**, **CPU**, or holding resources.
- Watch for patterns where long-running transactions line up with metric spikes.

### Validate with logs

- Check server logs for crash-related errors like:
    - `OutOfMemoryError`
    - Thread deadlocks
    - Uncaught exceptions
- Match the timestamps to metrics and transactions to confirm correlation.

![!Screenshot](../../Getting-started/Tutorials/log2.png)

---

## Step 3: Prevent future crashes

### Anomaly Detection (AI Plan)

Detects irregularities in:

- Request volume  
- Response times  
- Error rates  

**Sends alerts via:**

- Email  
- Webhooks (e.g., Slack, Microsoft Teams)  

Sensitivity is adjustable per environment.

### Custom Alerts

Set up rules under **Alerting & Thresholds**:

- Memory usage > 80%
- CPU usage > 90%
- Response time > 3 seconds
- Server offline
- JDBC pool nearly full

Get real-time alerts to act quickly when thresholds are breached.

---

## Outcome

By following this process, you can:

- Identify the specific cause of a crash - whether memory, CPU, thread, or database related.  
- Correlate data between metrics, transactions, and logs. 
- Configure automated alerts to catch early warning signs and avoid recurrence. 





