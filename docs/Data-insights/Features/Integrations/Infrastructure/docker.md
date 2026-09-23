# Docker

Monitor Docker containers - CPU, memory against limit, network and disk IO.

Your containers show up alongside the rest of your telemetry on a dashboard that is already built, so there are no panels to design. Memory is measured against the limit you set rather than as a raw number, which is what tells you a container is heading for a restart before it gets one.

!!! info "What this integration does"
    It provisions a **dashboard**. It does not collect anything itself and never talks to your Docker daemon - the metrics come from **Grafana Alloy**, which has a cAdvisor collector built in. Until Alloy is collecting them, the dashboard is empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Docker**.

---

## Permission tiers

Docker runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

---

## 1. Configure Alloy

If you have no collector yet, the [Grafana Alloy guide](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) covers installing one and getting an API key. That guide configures Alloy for OTLP; container metrics are Prometheus-format, so the components below are different, but the install and the API key are the same.

Add this to your `config.alloy`:

```river
prometheus.exporter.cadvisor "docker" {
  docker_host      = "unix:///var/run/docker.sock"
  docker_only      = true
  storage_duration = "5m"
}

prometheus.scrape "docker" {
  targets = prometheus.exporter.cadvisor.docker.targets

  job_name        = "docker"
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

  external_labels = {
    host = "<this-host's-name>",
  }
}
```

Three values matter more than they look:

| Value | Why it matters |
|---|---|
| `docker_only = true` | Keeps the collector to containers. Without it, it reports every cgroup on the host - systemd units, user sessions, desktop services - which on a typical machine is fifty times the series for no benefit, and none of them carry a container name for the dashboard to group by |
| `job_name = "docker"` | Required. Every panel filters on it, because your metrics land in a store shared with everything else you send to OpsPilot. Alloy's default job label is the component's own id, which would change if you renamed the component, so it is set explicitly. Change it and the dashboard goes blank |
| `host` | Yours to choose, and it populates the dashboard's host selector. Give each Docker host a distinct name if you run more than one - otherwise they produce indistinguishable series and the panels cannot tell them apart |

---

## 2. Run Alloy with access to Docker

The collector reads container metadata from the Docker socket and container resource usage from the host's cgroups, so it needs both. If Alloy runs as a container itself, it needs these mounts:

```yaml
services:
  alloy:
    image: grafana/alloy:latest
    privileged: true
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker:/var/lib/docker:ro
      - ./config.alloy:/etc/alloy/config.alloy
```

!!! warning "Linux hosts only"
    Docker Desktop for macOS and Windows runs containers inside a Linux VM, which stops the collector resolving container metadata: you get cgroup ids with no container names, and the dashboard has nothing readable to group by.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
container_cpu_usage_seconds_total{job="docker"}
```

You should get one series per container, each carrying a `name` and an `image`. If that returns data, the dashboard will too.

---

## Troubleshooting

**Nothing in Explore.** Check the Alloy UI on port 12345 first - a failing component shows there with the error. If the scrape is healthy, check the `job` label really is `docker` by querying `container_last_seen` with no selector and reading the labels back.

**Series with an `id` but no `name`.** The collector can see the cgroups but not the Docker daemon. Check the socket mount, and check you are on a Linux host rather than Docker Desktop.

**Memory against limit is empty.** No container has a memory limit set. Docker reports an unlimited container's limit as zero, and the panel excludes those rather than dividing by them. Set a limit on a container with `--memory`, or `mem_limit` in Compose, and it will appear.

**Disk IO is empty.** Container filesystem metrics depend on the storage driver. `overlay2` reports them; some others do not.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
