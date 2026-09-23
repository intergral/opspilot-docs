# Proxmox VE

Monitor Proxmox VE clusters, nodes, guests, and storage pools.

Your whole cluster shows up alongside the rest of your telemetry - every node, guest and storage pool from a single scrape, on dashboards that are already built. You can see how the cluster is behaving without opening Proxmox to look, and next to the applications running on it.

!!! info "What this integration does"
    It provisions **dashboards**. It does not collect anything itself and never talks to your Proxmox cluster - the metrics come from **pve-exporter** running somewhere you control, scraped by **Grafana Alloy** and forwarded to OpsPilot. Until both are running, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Proxmox VE**.

---

## Permission tiers

Proxmox VE runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

---

## 1. Create a Proxmox API token

The exporter needs read access to the cluster. In the Proxmox web UI:

1. **Datacenter → Permissions → Users**, add a user - `prometheus` is the convention. Set the realm to **Proxmox VE authentication server**, which is what makes it `prometheus@pve`. The PAM realm would give you `prometheus@pam` and the token below would not match.
2. **Datacenter → Permissions → API Tokens**, add a token for that user. Clear **Privilege Separation** so the token inherits the user's permissions. Copy the secret now - Proxmox shows it once.
3. **Datacenter → Permissions**, add a permission: path `/`, the user you created, role `PVEAuditor`, propagate on.

`PVEAuditor` is read-only. The exporter never needs more than that.

The token and permission can be created from a shell on any node once the user exists:

```bash
pveum user token add prometheus@pve monitoring -privsep 0
pveum acl modify / --user prometheus@pve --role PVEAuditor
```

The first command prints the token value. Copy it now.

---

## 2. Run pve-exporter

It needs to reach the Proxmox API on port 8006, so run it on a host that can - a management VM, a container host, or one of the nodes.

```yaml
services:
  pve-exporter:
    image: prompve/prometheus-pve-exporter:latest
    restart: unless-stopped
    ports:
      - "9221:9221"
    environment:
      PVE_USER: prometheus@pve
      PVE_TOKEN_NAME: monitoring
      PVE_TOKEN_VALUE: ${PVE_TOKEN_VALUE}
      PVE_VERIFY_SSL: "true"
```

!!! warning "About PVE_VERIFY_SSL"
    This is the exporter's own default, set here for visibility rather than to change anything. Proxmox ships with a self-signed certificate, so if you have not replaced it the exporter refuses to connect, because it cannot verify what it is talking to.

    Either add your cluster's CA to the exporter's trust store, or set `PVE_VERIFY_SSL: "false"` - which skips the check entirely, and means an attacker positioned between the exporter and the cluster could capture the API token. On a trusted network that is usually an acceptable trade, but make it deliberately rather than by default.

Check it works, substituting one of your node's hostnames:

```bash
curl "http://localhost:9221/pve?module=default&target=pve-node1"
```

You should get a few hundred lines beginning `pve_`. Note the path is `/pve`, not `/metrics`, and that the target is passed as a query parameter - the exporter queries the cluster API rather than reading the local machine.

---

## 3. Configure Alloy

If you have no collector yet, the [Grafana Alloy guide](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) covers installing one and getting an API key. That guide configures Alloy for OTLP; Proxmox metrics are Prometheus-format, so the components below are different, but the install and the API key are the same.

Add this to your `config.alloy`:

```river
prometheus.scrape "proxmox_ve" {
  targets = [{
    __address__      = "<exporter-host>:9221",
    __metrics_path__ = "/pve",
    "__param_module" = "default",
    "__param_target" = "<a-node-hostname>",
  }]

  job_name        = "proxmox-ve"
  scrape_interval = "30s"
  scrape_timeout  = "10s"

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
    cluster = "<your-cluster-name>",
  }
}
```

Two values matter more than they look:

| Value | Why it matters |
|---|---|
| `job_name = "proxmox-ve"` | Required. Every panel filters on it, because your metrics land in a store shared with everything else you send to OpsPilot. Alloy's default job label is the component's own id, which would change if you renamed the component, so it is set explicitly. Change it and the dashboards go blank |
| `cluster` | Yours to choose, and it populates the dashboard's cluster selector. Give each cluster a distinct name if you run more than one - otherwise they produce identical series and the panels cannot tell them apart |

`__param_target` only needs one node. The exporter asks that node's API about the whole cluster, so you get every node, guest, and storage pool from a single scrape. If you run the exporter directly on a Proxmox node rather than a separate host, `__param_target` can be dropped entirely - it defaults to localhost.

Restart Alloy and check `http://<alloy-host>:12345` - the `prometheus.scrape` component should show the target as up.

---

## 4. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
pve_up{job="proxmox-ve"}
```

You should get one series per node, guest, and storage pool. If that returns data, the dashboards will too.

---

## Troubleshooting

**Nothing in Explore.** Check the Alloy UI first - a failing scrape shows there with the error. If the target is up, check the `job` label really is `proxmox-ve` by querying `pve_up` with no selector and reading the labels back.

**Authentication failures from the exporter.** Privilege separation left on is the usual cause. A token with it enabled has no permissions of its own, regardless of what the user can do.

**Guests show `n/a` for disk usage.** Expected. Proxmox reports filesystem usage for LXC containers only - it cannot see inside a QEMU guest's disk. The allocated size is still shown.

**Two clusters overlapping.** Both are sending the same `cluster` label. Give them distinct names in `external_labels`.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
