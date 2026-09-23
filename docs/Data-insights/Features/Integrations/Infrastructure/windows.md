# Windows

Monitor Windows hosts - CPU, memory, disks, and network.

Your Windows hosts show up alongside the rest of your telemetry on a dashboard that is already built, including which services set to start automatically are not running. When an application slows down or stops responding, you can see whether the machine or a service underneath it is the reason.

!!! info "What this integration does"
    It provisions a **dashboard**. It does not collect anything itself and never connects to your hosts - the metrics come from **Grafana Alloy**, which has a windows_exporter collector built in. Until Alloy is collecting them, the dashboard is empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Windows**.

---

## Permission tiers

Windows runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

---

## 1. Install Alloy on the host

Alloy runs as a Windows service. Download the Windows installer from [Grafana's releases](https://github.com/grafana/alloy/releases) and run it, or install with winget:

```powershell
winget install Grafana.Alloy
```

The installer puts the configuration at `C:\Program Files\GrafanaLabs\Alloy\config.alloy`.

---

## 2. Configure it

If you have no API key yet, the [Grafana Alloy guide](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) covers getting one. That guide configures Alloy for OTLP; host metrics are Prometheus-format, so the components below are different, but the API key is the same.

```river
prometheus.exporter.windows "host" {
  enabled_collectors = [
    "cpu",
    "memory",
    "logical_disk",
    "net",
    "os",
    "system",
    "service",
  ]
}

prometheus.scrape "host" {
  targets = prometheus.exporter.windows.host.targets

  job_name        = "windows"
  scrape_interval = "15s"

  forward_to = [prometheus.relabel.trim_services.receiver]
}

// The service collector is by far the largest thing in that list - see below.
// These rules keep the two label values this dashboard reads and drop the rest.
prometheus.relabel "trim_services" {
  forward_to = [prometheus.remote_write.opspilot.receiver]

  // Neither of these is read by the dashboard.
  rule {
    source_labels = ["__name__"]
    regex         = "windows_service_(info|process)"
    action        = "drop"
  }

  // windows_service_state ships one series per service per state. Only
  // "stopped" is read.
  rule {
    source_labels = ["__name__", "state"]
    separator     = ";"
    regex         = "windows_service_state;(continue pending|pause pending|paused|running|start pending|stop pending|unknown)"
    action        = "drop"
  }

  // windows_service_start_mode ships one per service per mode. Only "auto" is
  // read.
  rule {
    source_labels = ["__name__", "start_mode"]
    separator     = ";"
    regex         = "windows_service_start_mode;(boot|disabled|manual|system)"
    action        = "drop"
  }
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

Then restart the service:

```powershell
Restart-Service Alloy
```

### Four things that matter more than they look

**`memory` is not a default collector.** Alloy's defaults are `cpu`, `logical_disk`, `net`, `os`, `service` and `system` - no memory. Leave it out and the memory panels are permanently empty with nothing to explain why, so it is listed explicitly above.

**`job_name = "windows"` is required.** Every panel filters on it, because your metrics land in a store shared with everything else you send to OpsPilot. Alloy's default job label is the component's own id, which would change if you renamed the component, so it is set explicitly. Change it and the dashboard goes blank.

**windows_exporter 0.25 or newer.** The memory collector's `windows_memory_physical_total_bytes` and `windows_memory_physical_free_bytes` are relatively recent, and `windows_os_info` - which the host selector is built from - has to be present, or the dashboard shows nothing at all rather than partially working. Any Alloy release from 2024 onwards embeds a new enough exporter.

**The service collector is the expensive one.** It emits four metrics per service, two of them multiplied out across every possible value: `windows_service_state` once per state (eight of them) and `windows_service_start_mode` once per start mode (five). On a Windows Server with around 250 services that is roughly **3,750 active series**, against a couple of hundred for every other collector in this list combined - and your metrics are metered. This dashboard reads exactly two of those values, `state="stopped"` and `start_mode="auto"`, so the relabel rules above drop the rest and take it to about **500**.

---

## Narrowing it further

If you only care about specific services rather than every automatic one, filter at collection instead and skip the relabel entirely:

```river
prometheus.exporter.windows "host" {
  enabled_collectors = [...]

  service {
    include = "MSSQLSERVER|W3SVC|YourAppService"
  }
}
```

That is cheaper again, at the cost of the dashboard only knowing about the services you named.

!!! warning "Keep the collector list short"
    Several collectors fail, or take the whole Alloy process down, when the thing they measure is not installed - `mscluster`, `vmware`, `hyperv`, `ad`, `dns`, `msmq` and `nps` among them. The list above is what this dashboard reads and nothing more. Add others deliberately, one at a time, and check Alloy is still running afterwards.

Each host appears in the dashboard's host selector under its `instance` label, which Alloy sets from the scrape target - the machine's own hostname.

If you already run windows_exporter as a standalone service and would rather point Alloy at that than enable the built-in collector, that works: scrape `http://localhost:9182/metrics` instead. The only difference is that `instance` then reads `HOSTNAME:9182` rather than the bare hostname, so that is what the host selector and every legend will show.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
windows_os_info{job="windows"}
```

You should get one series per host. If that returns data, the dashboard will too.

---

## Troubleshooting

**Nothing in Explore.** Check the Alloy UI at `http://localhost:12345` on the host first - a failing component shows there with the error. If the scrape is healthy, check the `job` label really is `windows` by querying `windows_os_info` with no selector and reading the labels back.

**The memory panels are empty but everything else works.** The memory collector is not enabled. See step 2.

**The service panels are empty.** The service collector is not enabled, or the Alloy service lacks the rights to enumerate services. It runs as LocalSystem by default, which has them.

**Stopped services shows a count but the table below is empty.** The table also filters on start mode, so it lists only services set to start automatically - a stopped service set to Manual is stopped by design and is left out deliberately.

**A disk you expected is missing.** Volumes reporting a size of zero are excluded, because dividing by that gives nothing useful. An empty card reader or an unmounted optical drive reports zero.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
