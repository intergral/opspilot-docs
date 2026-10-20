# Windows

Monitor Windows hosts - CPU, memory, disks, and network.

Your Windows hosts show up alongside the rest of your telemetry, on dashboards that are already built. When an application slows down or stops responding, you can see whether the machine or a service underneath it is the reason.

!!! info "What this integration does"
    It provisions **dashboards**. It does not collect anything itself and never connects to your hosts - the metrics come from **Grafana Alloy**, which has a `windows_exporter` collector built in. Until Alloy is collecting them, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Windows**.

---

## Permission tiers

Windows runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

Its one **capability** is **Dashboards**.

---

## The dashboards

Two dashboards are provisioned:

- **Windows Hosts** opens with a table of every host reporting, so you can see the estate before picking a machine; below that it covers CPU, memory, disk, network, and services for whichever one you choose.
- **Windows Hosts - Detail** is for working out *why* a machine is struggling rather than *whether* it is: memory commit and kernel pool, page file activity, disk latency and queue depth, per-core CPU, the processor queue, network errors, and TCP health.

Until Alloy is collecting them, both will be empty.

---

## 1. Install Alloy on the host

Alloy runs as a Windows service. The quickest way to install it is winget, from an administrator PowerShell:

```powershell
winget install Grafana.Alloy
```

If winget is not available, download the installer instead. On Grafana's [Alloy install guide](https://grafana.com/docs/alloy/latest/set-up/install/) follow the Windows page, which links to the current release; on that release, open **Assets** at the bottom and take `alloy-installer-windows-amd64.exe.zip`. Unzip it and run the installer.

Either way the installer registers Alloy as a service and puts its configuration at `C:\Program Files\GrafanaLabs\Alloy\config.alloy`. That is the file you edit in the next step.

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
    "tcp",
    "scheduled_task",
    "pagefile",
    "time",
    "thermalzone",
    "cpu_info",
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

**`memory` is not a default collector.** Alloy's defaults are `cpu`, `logical_disk`, `net`, `os`, `service`, and `system` - no memory. Leave it out and the memory panels are permanently empty with nothing to explain why, so it is listed explicitly above.

**The `job` label is set for you, and not by `job_name`.** Alloy's built-in windows exporter labels its own metrics `job="integrations/windows"`, and `job_name` on the scrape does not override it. The label follows the exporter type rather than the name you give the component, so calling the component something else does not change it. The dashboard reads that label, and also accepts `windows` for anyone scraping a standalone `windows_exporter`.

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

**The last four collectors are optional.** `pagefile`, `time`, `thermalzone`, and `cpu_info` each fill one panel in the detail dashboard's bottom row, which says so where it is empty. Drop any of them and nothing else is affected.

**`tcp` and `scheduled_task` are for the detail dashboard.** The overview needs neither. Leave them out and the overview is unaffected, while the detail dashboard's TCP panels and its scheduled-task table are empty.

!!! note
    `enabled_collectors` replaces Alloy's defaults rather than adding to them, which is why collectors documented as on-by-default have to appear in the list too.

!!! warning "Keep the collector list short"
    Several collectors fail, or take the whole Alloy process down, when the thing they measure is not installed - `mscluster`, `vmware`, `hyperv`, `ad`, `dns`, `msmq`, and `nps` among them. The list above is what these dashboards read and nothing more. Add others deliberately, one at a time, and check Alloy is still running afterwards.

Each host appears in the dashboard's host selector under its `instance` label, which Alloy sets from the scrape target - the machine's own hostname.

If you already run `windows_exporter` as a standalone service and would rather point Alloy at that than enable the built-in collector, that works: scrape `http://localhost:9182/metrics` instead. The only difference is that `instance` then reads `HOSTNAME:9182` rather than the bare hostname, so that is what the host selector and every legend will show.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
windows_os_info
```

You should get one series per host. If that returns data, the dashboards will too.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

## Troubleshooting

**Nothing in Explore.** Check the Alloy UI at `http://localhost:12345` on the host first - a failing component shows there with the error. If the scrape is healthy, query `windows_os_info` with no selector and read the labels back - whatever the `job` label says, the dashboard accepts both `windows` and `integrations/windows`.

**The memory panels are empty but everything else works.** The memory collector is not enabled. See step 2.

**The TCP panels or the scheduled-task table are empty.** The `tcp` and `scheduled_task` collectors are not enabled. Both are only read by the detail dashboard, so the overview will look fine without them.

**The service panels are empty.** The service collector is not enabled, or the Alloy service lacks the rights to enumerate services. It runs as LocalSystem by default, which has them.

**Stopped services shows a count but the table below is empty.** The table also filters on start mode, so it lists only services set to start automatically - a stopped service set to Manual is stopped by design and is left out deliberately.

**A disk you expected is missing.** Volumes reporting a size of zero are excluded, because dividing by that gives nothing useful. An empty card reader or an unmounted optical drive reports zero.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
