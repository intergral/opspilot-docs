# Unix

Monitor Unix and Linux hosts - CPU, memory, filesystems, and processes.

!!! info "What this integration does"
    It provisions a **dashboard**. It does not collect anything itself and never connects to your hosts - the metrics come from **Grafana Alloy**, which has a node_exporter collector built in. Until Alloy is collecting them, the dashboard is empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Unix**.

---

## Permission tiers

Unix runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

---

## 1. Configure Alloy

If you have no collector yet, the [Grafana Alloy guide](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) covers installing one and getting an API key. That guide configures Alloy for OTLP; host metrics are Prometheus-format, so the components below are different, but the install and the API key are the same.

Add this to your `config.alloy` on **each host you want to monitor**:

```river
prometheus.exporter.unix "host" { }

prometheus.scrape "host" {
  targets = prometheus.exporter.unix.host.targets

  job_name        = "unix"
  scrape_interval = "15s"

  forward_to = [prometheus.remote_write.opspilot.receiver]
}

prometheus.remote_write "opspilot" {
  endpoint {
    url = "https://api.fusionreactor.io/v1/metrics"

    headers = {
      "authorization" = sys.env("OPSPILOT_API_KEY"),
    }
  }
}
```

`job_name` can be `unix` or `node` - the dashboard accepts either. `node` is the long-standing convention for node_exporter, so if you are already scraping hosts under that name there is nothing to change. What matters is that it is one of the two: every panel filters on it, because your metrics land in a store shared with everything else you send to OpsPilot.

Each host appears in the dashboard's host selector under its `instance` label, which Alloy sets from the scrape target.

---

## 2. Run Alloy with access to the host

The collector reads from `/proc` and `/sys`, so if Alloy runs as a container it needs them mounted and the root path pointed at them:

```yaml
services:
  alloy:
    image: grafana/alloy:latest
    pid: host
    volumes:
      - /:/rootfs:ro
      - ./config.alloy:/etc/alloy/config.alloy
```

and in the exporter block:

```river
prometheus.exporter.unix "host" {
  rootfs_path = "/rootfs"
}
```

Without that, the collector reports the container's own view: every mount shows the size of the underlying filesystem rather than its own, and the hostname is a container id. Running Alloy directly on the host avoids the question entirely.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
node_uname_info{job="unix"}
```

You should get one series per host, carrying its `nodename` and `release`. If that returns data, the dashboard will too.

---

## Troubleshooting

**Nothing in Explore.** Check the Alloy UI on port 12345 first - a failing component shows there with the error. If the scrape is healthy, check the `job` label really is `unix` or `node` by querying `node_uname_info` with no selector and reading the labels back.

**Every filesystem reports the same size.** Alloy is running in a container without the root filesystem mounted, so the collector sees the container's view rather than the host's. See step 2.

**A filesystem you expected is missing.** The panel excludes pseudo-filesystems - tmpfs, overlay, squashfs and the rest - because they report the memory or image backing them rather than disk. A real mount with an unusual filesystem type may be caught by that too; the exclusion list is in the panel's query.

**The host selector shows a container id.** `instance` comes from the scrape target, which is the Alloy container when Alloy runs in Docker. Set it explicitly with a relabel rule if you want the hostname instead.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
