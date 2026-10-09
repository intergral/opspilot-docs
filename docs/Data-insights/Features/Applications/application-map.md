# Application Map

The **Application Map** shows how your servers and applications connect, as a topology you can pan and zoom.

Navigate to **Applications** > **Application Map** from the left-hand sidebar.

---

## Filtering the map

A filter bar runs across the top:

| Control | What it does |
|---|---|
| **Catalog / Label** | Switch between grouping the map by **Catalog** entry or by **Label** |
| **Select servers or apps** | Narrow the map to specific servers or applications |
| **Select Group** | Filter to a group |
| **Select Instance** | Filter to a specific instance |
| **Clear all** | Reset the filters |

---

## The map

Nodes are collected into groups - for example `Group: otlp-fr-demo · 1 server · 1 application` - with an arrow from each server to the applications running on it. Each node carries a badge for its type, **FR Server** or **FR App**, and a few live metrics:

- A **server** node shows its instance ID, the number of **Apps**, and **Errors** per second with a sparkline
- An **application** node shows its **Spans** count and **Errors** per second

The summary in the top-right corner counts what is on the map - servers, applications, and the total. **Left-click** to pan and **scroll** to zoom; the icons at the top-right of the panel switch to a 3D view and expand the map to full screen.

---

## Servers

Below the map, the **Servers** table lists the servers behind it, one row each:

| Column | Description |
|---|---|
| **Group** | The group the server belongs to |
| **Job** | The job name |
| **Instance** | The instance ID - click to open it |
| **Apps** | How many applications run on the server |
| **Avg Req** | Average request time |
| **Errors/s** | Errors per second |
| **Throughput** | Requests per second |
| **CPU** | CPU usage |
| **Memory** | Memory usage |
| **Catalog** | The server's catalog status - **Create** if it is not yet in the [Catalog](../../../Admin-and-data/Catalog/catalog.md), or its badges (for example **FR Server**, **Java**) if it is |

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
