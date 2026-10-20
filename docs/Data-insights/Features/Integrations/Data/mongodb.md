# MongoDB

Monitor MongoDB - operations, latency, replication, sharding, the WiredTiger cache, and the log.

Your MongoDB servers show up alongside the rest of your telemetry, on dashboards that are already built. You can see how hard each server is working and where it is struggling - latency, connections, queues, and the WiredTiger cache - across your replica sets and sharded clusters, with the servers' logs, and get alerted when a server stops reporting, a member goes down, a secondary falls behind, or operations start to queue.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - **Grafana Alloy** has a MongoDB exporter built in, so collecting metrics needs a user on the server and a few lines of Alloy config, and the log needs a few more. This covers MongoDB 7.0 and later - standalone servers, replica sets, and sharded clusters. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **MongoDB**.

---

## Permission tiers

MongoDB runs **Read-only**, the default. It requires a MongoDB user with the **`clusterMonitor`** role, read access to the MongoDB log for Alloy, and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

Grafana's own docs cover the exporter in full: see [`prometheus.exporter.mongodb`](https://grafana.com/docs/alloy/latest/reference/components/prometheus/prometheus.exporter.mongodb/) for every option, and [install Alloy](https://grafana.com/docs/alloy/latest/set-up/install/) on each MongoDB host if you want the log (Alloy reads it from disk), or anywhere that can reach each server's port for metrics alone.

---

## 1. Create a monitoring user

Alloy logs in to read the server's status. Give it a user of its own with MongoDB's built-in read-only **`clusterMonitor`** role, rather than an administrator or an application's user. In `mongosh`:

```javascript
db.getSiblingDB("admin").createUser({
  user: "opspilot_exporter",
  pwd: passwordPrompt(),
  roles: [{ role: "clusterMonitor", db: "admin" }],
})
```

Run it once on each replica set's primary; it reaches the other members by replication. In a sharded cluster, run it through a `mongos`, and once more on each shard's primary - a connection straight to a shard member checks the shard's own users.

---

## 2. Configure Alloy

Alloy's config file is in a different place on each system:

| OS | Config file | After a change |
|---|---|---|
| **Linux** | `/etc/alloy/config.alloy` | `sudo systemctl restart alloy` |
| **Windows** | `C:\Program Files\GrafanaLabs\Alloy\config.alloy` | restart the Alloy service in `services.msc` |
| **macOS** | `$(brew --prefix)/etc/alloy/config.alloy` | `brew services restart grafana/grafana/alloy` |

Keep the password in a file of its own beside it, readable only by Alloy. **URL-encode it**, because it goes inside a `mongodb://` URI - a raw `@` fails the login, and a raw `:`, `#`, `/`, `?`, or `%` stops the exporter starting.

On **Linux**, this asks for the password and writes it encoded:

```bash
python3 -c 'import getpass, urllib.parse; print(urllib.parse.quote(getpass.getpass(), safe=""), end="")' | sudo tee /etc/alloy/mongodb-password >/dev/null
sudo chown root:alloy /etc/alloy/mongodb-password
sudo chmod 640 /etc/alloy/mongodb-password
```

On **Windows**, in an administrator PowerShell:

```powershell
Set-Content -NoNewline -Path "$env:ProgramFiles\GrafanaLabs\Alloy\mongodb-password" -Value ([uri]::EscapeDataString((Read-Host "Password")))
```

On **macOS**, the first line alone, writing to `$(brew --prefix)/etc/alloy/mongodb-password` without `sudo`.

!!! warning
    The file must hold the encoded password and nothing else: a trailing newline, which most editors add, makes the login fail.

Then add to the config file, with one exporter per `mongod` and `mongos`:

```river
local.file "mongodb_password" {
  // Windows: "C:/Program Files/GrafanaLabs/Alloy/mongodb-password"
  filename  = "/etc/alloy/mongodb-password"
  is_secret = true
}

prometheus.exporter.mongodb "db" {
  mongodb_uri            = "mongodb://opspilot_exporter:" + local.file.mongodb_password.content + "@dbhost:27017/admin"
  direct_connect         = true
  collect_all            = false
  enable_diagnostic_data = true
  enable_db_stats        = true
}

prometheus.scrape "db" {
  targets         = prometheus.exporter.mongodb.db.targets
  scrape_interval = "30s"
  forward_to      = [prometheus.relabel.mongodb.receiver]
}

prometheus.relabel "mongodb" {
  forward_to = [prometheus.remote_write.opspilot.receiver]

  rule {
    source_labels = ["__name__"]
    regex         = "mongodb_(ss|sys|oplog_stats|dbstats|config|local|admin)_.*"
    action        = "drop"
  }
}
```

A few things matter here:

- **`collect_all = false`.** Left at its default, the exporter also collects statistics for every collection and index, with the collection's name in the metric's name - thousands of series per server, and more with every collection you add. The two collectors enabled here are what the dashboards read.
- **The relabel rule drops raw duplicates.** The diagnostic data arrives twice: as the named metrics the dashboards read, and as some 5,500 raw series per server that nothing here uses. Dropping them leaves 200 to 350 per server.
- **`direct_connect = true` for each server.** Without it, pointed at one replica set member, the exporter finds the primary and reports the primary's numbers under that member's name.
- **Leave `job` alone.** Alloy labels these metrics `job="integrations/mongodb"` whatever you call the blocks, and the dashboards and alerts select on that, so add no `job_name` and no relabel rule for `job`. Each server appears as the `host:port` in its URI.
- **One exporter per server.** For each further `mongod` or `mongos`, add another exporter and scrape with different names, all forwarding to the same relabel block.

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
    Environment variables work in place of files if you already manage Alloy's settings that way: write `sys.env("MONGODB_EXPORTER_PASSWORD")` in place of `local.file.mongodb_password.content`, and likewise for the key. Alloy reads its environment from `/etc/default/alloy` (Debian, Ubuntu), `/etc/sysconfig/alloy` (RHEL, SUSE), `$(brew --prefix)/etc/alloy/config.env` (macOS), or on Windows the `Environment` value of the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\GrafanaLabs\Alloy`.

---

## 4. Collect the log

This needs Alloy on the same machine as the server, since it reads the file. The log's path is `systemLog.path` in the server's config file (`/etc/mongod.conf` on Linux, `mongod.cfg` beside `mongod.exe` on Windows); the packages use `/var/log/mongodb/mongod.log`. Use it here, with the same `instance` the metrics have - `dbhost:27017` - so the dashboards line up:

```river
loki.source.file "mongodb_log" {
  targets = [{
    // Windows: "C:/Program Files/MongoDB/Server/8.0/log/mongod.log"
    __path__ = "/var/log/mongodb/mongod.log",
    job      = "integrations/mongodb",
    instance = "dbhost:27017",
  }]
  forward_to = [loki.process.mongodb_log.receiver]
}

loki.process "mongodb_log" {
  stage.json {
    expressions = { ts = "t.\"$date\"", s = "s", component = "c", id = "id" }
  }
  stage.drop {
    source     = "id"
    expression = "^(22943|22944|51800|5286306|6788604|6788700|10483900)$"
  }
  stage.timestamp {
    source = "ts"
    format = "RFC3339"
  }
  stage.drop {
    older_than = "24h"
  }
  stage.template {
    source   = "level"
    template = "{{ $s := .s }}{{ if eq $s \"F\" }}fatal{{ else if eq $s \"E\" }}error{{ else if eq $s \"W\" }}warning{{ else if eq $s \"I\" }}info{{ else }}debug{{ end }}"
  }
  stage.labels {
    values = { level = "", component = "" }
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

Keep the stages as they are. MongoDB writes its log as JSON; the stages take each entry's time from it, turn its severity and component into the labels the log dashboard filters on, and drop connection churn - every client connecting, authenticating, and leaving, the exporter's own scrapes included - which is most of the log by volume. Failed logins are kept. The last 24 hours are sent when Alloy first starts, and nothing older.

On **Linux**, let Alloy read the file. MongoDB creates its log readable by its own user only. Add this to `/etc/mongod.conf` and restart MongoDB, so the log is readable by its group:

```yaml
setParameter:
  processUmask: "027"
```

Then add Alloy to that group and restart Alloy: `sudo usermod -aG mongodb alloy` on Debian and Ubuntu, `sudo usermod -aG mongod alloy` on RHEL and its relatives. On **Windows**, Alloy runs as LocalSystem and can read the log as it is; write the path with forward slashes, as in the comment.

---

## 5. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
mongodb_up
```

You should get one series per server, reading `1`. `0` means Alloy cannot log in, and no result at all that it cannot reach the server - either way the Alloy log for `prometheus.exporter.mongodb` says why.

For the log, select the **Logs** data source and run `{job="integrations/mongodb"}`. If nothing comes back, the Alloy log for `loki.source.file` says whether it could open the file.

Once data is flowing, the **Dashboard data** column on **Your installation** (for example *4 of 4 with data*) links straight to the provisioned dashboards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
