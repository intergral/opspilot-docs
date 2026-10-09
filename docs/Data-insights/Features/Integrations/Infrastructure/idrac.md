# iDRAC

Monitor Dell PowerEdge hardware health through iDRAC.

Your servers' hardware shows up alongside the rest of your telemetry, on a dashboard that is already built - system health, sensors, power, storage, network, processors, and memory, read straight from each machine's baseboard management controller (BMC).

!!! info "What this integration does"
    It provisions a **dashboard**. It does not collect anything itself and never connects to your hardware. Unlike the [Docker](docker.md), [Unix](unix.md), and [Windows](windows.md) integrations, Alloy has no built-in collector for this one. You run `idrac_exporter` alongside Alloy, and it talks Redfish to each BMC. The same exporter works for HPE iLO and Lenovo XClarity, so a mixed estate needs only one of them. Until the exporter is running and Alloy is scraping it, the dashboard is empty.

Navigate to **Integrations** from the left-hand sidebar, then select **iDRAC**.

---

## Permission tiers

iDRAC runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

Its one **capability** is **Dashboards**: installing it provisions the dashboard and nothing else.

---

## 1. Create a read-only account on each BMC

In the iDRAC web interface, add a local user with the **Read Only** role. The exporter only ever reads, so anything more is unnecessary exposure. Where user management sits in the menus varies between iDRAC generations - on iDRAC 9 it is under **iDRAC Settings**.

If your BMCs are joined to Active Directory or LDAP you can use a directory account instead, as long as it has the read-only role on each machine.

---

## 2. Run the exporter

Its configuration file lists the hosts it will talk to and the credentials for each:

```yaml
address: 0.0.0.0
port: 9348
timeout: 60

hosts:
  # One entry per BMC. The key is the address you will scrape it at.
  192.168.1.21:
    username: opspilot
    password: <password>
  192.168.1.22:
    username: opspilot
    password: <password>

metrics:
  system: true
  sensors: true
  power: true
  storage: true
  network: true
  processors: true
  memory: true
```

Then run it:

```bash
docker run -d --name idrac_exporter \
  -p 127.0.0.1:9348:9348 \
  -v /etc/prometheus/idrac.yml:/etc/prometheus/idrac.yml:ro \
  ghcr.io/mrlhansen/idrac_exporter:latest
```

Two things above are deliberate, and both matter.

**The port is published on localhost only.** That is the `127.0.0.1:` prefix on the `-p` flag - the exporter still listens on `0.0.0.0` inside the container, which it has to, or Docker could not forward to it at all. What changes is that Docker binds the host side to loopback rather than to every interface. Alloy scrapes it from the same host, so nothing else needs to reach it; published wide, anyone who can reach port `9348` can ask the exporter to scrape an address of their choosing. If you run the exporter directly rather than in a container, set `address: 127.0.0.1` in its config instead - there is no Docker layer to do it for you.

**There is no `default:` entry.** The exporter's config allows one, as a fallback for any target not listed. With it, a request naming a host the exporter has never heard of makes it open a Redfish session to that host and send it the fallback account's username and password - so an attacker who can reach the exporter can have your BMC credentials delivered to a server they control. Listing each BMC explicitly means a request for anything else is simply refused.

The seven metric groups above are the ones this dashboard reads, and every one of them is off by default - the exporter enables nothing unless asked. Leaving `processors` or `memory` out is worth avoiding in particular: the component health panels would then show green while a CPU or a DIMM was reporting Critical, and a failed DIMM is the most common fault on this hardware. Adding groups beyond these seven costs scrape time for data nothing displays; see the exporter's documentation for the full list.

---

## 3. Scrape it with Alloy

If you have no collector yet, the [Grafana Alloy guide](../../../../Monitor-your-data/OpenTelemetry/Shipping/Collector.md) covers installing one and getting an API key. That guide configures Alloy for OTLP; these metrics are Prometheus-format, so the components below are different, but the install and the API key are the same.

The exporter is a **multi-target** exporter: one instance serves many BMCs, and you tell it which one you want with a `target` parameter. That shapes the Alloy config more than it looks:

```river
// One entry per BMC. The address here is what the exporter connects to and
// what identifies the machine on the dashboard.
discovery.relabel "idrac" {
  targets = [
    { "__address__" = "192.168.1.21" },
    { "__address__" = "192.168.1.22" },
  ]

  // Ask the exporter for this BMC...
  rule {
    source_labels = ["__address__"]
    target_label  = "__param_target"
  }

  // ...keep the BMC's address as the instance label, so each machine is
  // identifiable on the dashboard...
  rule {
    source_labels = ["__param_target"]
    target_label  = "instance"
  }

  // ...and point the scrape itself at the exporter rather than the BMC.
  rule {
    target_label = "__address__"
    replacement  = "localhost:9348"
  }
}

prometheus.scrape "idrac" {
  targets = discovery.relabel.idrac.output

  job_name        = "idrac"
  metrics_path    = "/metrics"
  scrape_interval = "2m"
  scrape_timeout  = "2m"

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

Three things in there matter more than they look.

**The three relabel rules are what make several machines distinguishable.** Without them every BMC is scraped as `localhost:9348`, so the dashboard shows one machine no matter how many you have, with their readings overwriting each other. The rules take the BMC address, pass it to the exporter as the target, keep it as the instance label, and then redirect the actual HTTP request to the exporter.

**`job_name = "idrac"` is required.** Every panel filters on it, because your metrics land in a store shared with everything else you send to OpsPilot. It matches the exporter's own documentation, so if you already scrape it you probably have this already.

**The intervals are deliberately long, but not longer than five minutes.** The exporter collects on demand: each scrape opens a Redfish session and walks the BMC, which is slow hardware doing slow work. A minute is normal and several is possible on a machine with many drives, so scraping every 15 seconds would queue requests faster than the BMC can answer them.

Two minutes is the balance. Going to five would be gentler still, but five minutes is also the query lookback window: samples would arrive exactly one lookback apart, and every cycle there would be a short gap where the previous sample has aged out and the next has not arrived. During it the point-in-time panels empty - and "Components not OK" would fall back to zero, which looks green rather than looking broken.

---

## 4. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
idrac_system_health{job="idrac"}
```

You should get one series per machine. `0` is OK, `1` Warning, `2` Critical.

---

## Troubleshooting

**Nothing in Explore.** Ask the exporter directly first, from the machine it runs on:

```bash
curl 'http://localhost:9348/metrics?target=192.168.1.21'
```

An error there is between the exporter and the BMC, and its own logs will say which. If that works but nothing reaches OpsPilot, the problem is in Alloy - check its UI on port `12345`.

**"failed to instantiate new client".** The exporter cannot open a Redfish session. Usually the credentials, or a BMC with Redfish disabled - it is on by default on iDRAC 9, but worth checking in the iDRAC settings if the credentials are definitely right.

**Every machine shows as one.** The relabel rules in step 3 are missing or wrong, so every scrape is labeled with the exporter's address rather than the BMC's. The Machines table at the bottom of the dashboard will show one row with an Endpoint of `localhost:9348`.

**Scrapes time out.** Raise `scrape_timeout`, and turn off metric groups you do not need in the exporter's configuration. Storage is the slowest on a machine with many drives.

**The drive life panel is empty.** Only SSDs report remaining endurance. Spinning disks do not, and are left out rather than shown at zero.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
