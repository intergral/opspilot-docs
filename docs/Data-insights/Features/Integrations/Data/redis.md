# Redis

Monitor Redis and Valkey - commands, latency, memory, clients, replication, persistence, and the log.

Your Redis and Valkey servers show up alongside the rest of your telemetry, on dashboards that are already built. You can see how hard each server is working and where it is struggling - command latency, hit ratio, memory, clients, and persistence - with a view of replication and the servers' logs, and alerts when one stops reporting, runs out of memory, refuses connections, loses its primary, or stops saving to disk.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - **Grafana Alloy** has a Redis exporter built in, so collecting metrics needs a user on the server and a few lines of Alloy config, and the log needs a few more. This covers Redis 7.2 and later and Valkey 8 and later. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Redis**.

---

## Permission tiers

Redis runs **Read-only**, the default. It requires a Redis user allowed `INFO` and a few read-only diagnostic commands (no access to keys), read access to the Redis log for Alloy, and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

Grafana's own docs cover the exporter in full: see [`prometheus.exporter.redis`](https://grafana.com/docs/alloy/latest/reference/components/prometheus/prometheus.exporter.redis/) for every option, and [install Alloy](https://grafana.com/docs/alloy/latest/set-up/install/) on the Redis host if you want the log (Alloy reads it from disk), or anywhere that can reach the server's port for metrics alone.

---

## 1. Create a monitoring user

Alloy logs in to read the server's status. Give it a user of its own that can read that status and nothing else, rather than the default user or an application's. In `redis-cli` (or `valkey-cli`), on each server - users are not replicated:

```text
ACL SETUSER opspilot_exporter on ><a strong password> -@all +info +ping +client|setname +slowlog|get +slowlog|len +latency|latest +latency|histogram
```

then `ACL SAVE` if the server keeps its users in an ACL file, or `CONFIG REWRITE` if not, so the user survives a restart.

That user can read no keys. The exporter's own ACL is wider: it adds key reads (`+get`, `+scan`, `+eval`), which only its optional key-checking features use, and `+config|get`, which would let the monitoring user read `requirepass` and `masterauth` - Alloy is set below not to call `CONFIG` at all. That ACL also names a command that only exists from Redis 8.8, so on earlier Redis and on Valkey the whole command is refused.

---

## 2. Configure Alloy

Alloy's config file is in a different place on each system:

| OS | Config file | After a change |
|---|---|---|
| **Linux** | `/etc/alloy/config.alloy` | `sudo systemctl restart alloy` |
| **Windows** | `C:\Program Files\GrafanaLabs\Alloy\config.alloy` | restart the Alloy service in `services.msc` |
| **macOS** | `$(brew --prefix)/etc/alloy/config.alloy` | `brew services restart grafana/grafana/alloy` |

Keep the password in a file of its own beside it, readable only by Alloy. On **Linux**:

```bash
read -rs PW && printf '%s' "$PW" | sudo tee /etc/alloy/redis-password >/dev/null; unset PW
sudo chown root:alloy /etc/alloy/redis-password
sudo chmod 640 /etc/alloy/redis-password
```

On **Windows**, in an administrator PowerShell:

```powershell
Set-Content -NoNewline -Path "$env:ProgramFiles\GrafanaLabs\Alloy\redis-password" -Value (Read-Host "Password")
```

On **macOS**, the first line alone, writing to `$(brew --prefix)/etc/alloy/redis-password` without `sudo`.

Then add to the config file:

```river
prometheus.exporter.redis "db" {
  redis_addr          = "dbhost:6379"
  redis_user          = "opspilot_exporter"
  // Windows: "C:/Program Files/GrafanaLabs/Alloy/redis-password"
  redis_password_file = "/etc/alloy/redis-password"
  config_command      = "-"
}

prometheus.scrape "db" {
  targets         = prometheus.exporter.redis.db.targets
  scrape_interval = "30s"
  forward_to      = [prometheus.remote_write.opspilot.receiver]
}
```

- **`config_command = "-"` keeps the user narrow.** It stops the exporter running `CONFIG GET *`; the figures that call would give - `maxclients` and `maxmemory` - come from `INFO` as well.
- **Keep the credentials out of `redis_addr`.** Each server appears on the dashboards as its `redis_addr`, so a `redis://user:password@host` address would put the password in every series' labels. Give the address alone, as above.
- **Leave `job` alone.** Alloy labels these metrics `job="integrations/redis"` whatever you call the blocks, and the dashboards and alerts select on that, so add no `job_name` and no relabel rule for `job`.
- **One exporter per server.** For a replica or a second server, add another exporter and scrape with different names.

---

## 3. Send data to OpsPilot

You need an OpsPilot API key, from **Data and Licenses > [API Keys](https://app.opspilot.com/organization/api-keys)**. Put it in a file the same way, as `opspilot-api-key` beside the config file, and add:

```river
local.file "opspilot_api_key" {
  // Windows: "C:/Program Files/GrafanaLabs/Alloy/opspilot-api-key"
  filename = "/etc/alloy/opspilot-api-key"
}

prometheus.remote_write "opspilot" {
  endpoint {
    url = "https://api.opspilot.com/v1/metrics"

    headers = {
      "authorization" = string.trim_space(local.file.opspilot_api_key.content),
    }
  }
}
```

!!! note "Using environment variables instead"
    Environment variables work in place of files if you already manage Alloy's settings that way: write `redis_password = sys.env("REDIS_EXPORTER_PASSWORD")` in place of `redis_password_file`, and `sys.env("OPSPILOT_API_KEY")` for the key. Alloy reads its environment from `/etc/default/alloy` (Debian, Ubuntu), `/etc/sysconfig/alloy` (RHEL, SUSE), `$(brew --prefix)/etc/alloy/config.env` (macOS), or on Windows the `Environment` value of the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\GrafanaLabs\Alloy`.

---

## 4. Collect the log

This needs Alloy on the same machine as the server, since it reads the file. `CONFIG GET logfile` (as an administrator) gives its path; an empty value means the server logs to standard output - as the official container images do - and `logfile` needs setting in its config first. Use the path here, with the same `instance` the metrics have - `dbhost:6379` - so the dashboards line up:

```river
loki.source.file "redis_log" {
  targets = [{
    __path__ = "/var/log/redis/redis-server.log",
    job      = "integrations/redis",
    instance = "dbhost:6379",
  }]
  forward_to = [loki.process.redis_log.receiver]
}

loki.process "redis_log" {
  stage.multiline {
    firstline     = "^\\d+:[XCSM] "
    max_wait_time = "3s"
  }
  stage.regex {
    expression = "^\\d+:(?P<role>[XCSM]) (?P<ts>\\d{1,2} \\w{3} \\d{4} \\d{2}:\\d{2}:\\d{2}\\.\\d{3}) (?P<lvl>[.*#-]) "
  }
  stage.timestamp {
    source   = "ts"
    format   = "2 Jan 2006 15:04:05.000"
    location = "Local"
  }
  stage.drop {
    older_than = "24h"
  }
  stage.template {
    source   = "level"
    template = "{{ $l := .lvl }}{{ if eq $l \"#\" }}warning{{ else if eq $l \"*\" }}notice{{ else if eq $l \"-\" }}verbose{{ else if eq $l \".\" }}debug{{ end }}"
  }
  stage.template {
    source   = "role"
    template = "{{ $r := .role }}{{ if eq $r \"M\" }}primary{{ else if eq $r \"S\" }}replica{{ else if eq $r \"C\" }}child{{ else if eq $r \"X\" }}sentinel{{ end }}"
  }
  stage.labels {
    values = { level = "", role = "" }
  }
  forward_to = [loki.write.opspilot.receiver]
}

loki.write "opspilot" {
  endpoint {
    url = "https://api.opspilot.com/logs/v1/"

    headers = {
      "authorization" = string.trim_space(local.file.opspilot_api_key.content),
    }
  }
}
```

Keep the stages as they are. They join the multi-line blocks Redis writes at startup and on a crash, take each entry's time from the log itself, and turn its level character and role character into the labels the log dashboard filters on. The last 24 hours are sent when Alloy first starts, and nothing older.

Let Alloy read the file, then restart Alloy:

| Package | Log | Run |
|---|---|---|
| Redis, Debian or Ubuntu | `/var/log/redis/redis-server.log` | `sudo usermod -aG adm alloy` |
| Valkey, Debian or Ubuntu | `/var/log/valkey/valkey-server.log` | `sudo usermod -aG adm alloy` |
| Redis, RHEL family | `/var/log/redis/redis.log` | `sudo usermod -aG redis alloy` |

---

## 5. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
redis_up
```

You should get one series per server, reading `1`. `0` means Alloy cannot reach the server or log in, and the Alloy log for `prometheus.exporter.redis` says which.

For the log, select the **Logs** data source and run `{job="integrations/redis"}`. If nothing comes back, the Alloy log for `loki.source.file` says whether it could open the file.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
