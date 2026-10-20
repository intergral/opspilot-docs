# Microsoft SQL Server

Monitor Microsoft SQL Server - workload, deadlocks, I/O stall, memory, and the error log.

Your SQL Server instances show up alongside the rest of your telemetry, on dashboards that are already built. You can see how hard each instance is working and where it is struggling - deadlocks, severe errors, I/O waits, transaction log growth, and memory - alongside their error logs, with alerts when one stops reporting, comes under pressure, or is refusing logins.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - **Grafana Alloy** has a SQL Server exporter built in, so collecting metrics needs a login on the server and a few lines of Alloy config, and the error log needs a few more. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **Microsoft SQL Server**.

---

## Permission tiers

Microsoft SQL Server runs **Read-only**, the default. It requires a SQL Server login with **`VIEW SERVER STATE`** and **`VIEW ANY DEFINITION`**, read access to its error log for Alloy, and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

Grafana's own docs cover the exporter in full: see [`prometheus.exporter.mssql`](https://grafana.com/docs/alloy/latest/reference/components/prometheus/prometheus.exporter.mssql/) for every option, including Windows authentication, and [install Alloy](https://grafana.com/docs/alloy/latest/set-up/install/) on the SQL Server host if you want the error log (Alloy reads it from disk), or anywhere that can reach SQL Server's port for metrics alone.

---

## 1. Create a monitoring login

Alloy logs in to SQL Server to read its statistics. Give it a login of its own that can read those statistics and nothing else, rather than `sa` or an application's login. On each instance:

```sql
CREATE LOGIN opspilot_exporter WITH PASSWORD = '<a strong password>';
GRANT VIEW SERVER STATE TO opspilot_exporter;
GRANT VIEW ANY DEFINITION TO opspilot_exporter;
```

Both grants are read-only: they show server state and object definitions, never table data. Leave out `VIEW ANY DEFINITION` and the I/O stall panels are empty, with no error anywhere to say why.

---

## 2. Configure Alloy

Alloy's config file is in a different place on each system:

| OS | Config file | After a change |
|---|---|---|
| **Linux** | `/etc/alloy/config.alloy` | `sudo systemctl restart alloy` |
| **Windows** | `C:\Program Files\GrafanaLabs\Alloy\config.alloy` | restart the Alloy service in `services.msc` |
| **macOS** | `$(brew --prefix)/etc/alloy/config.alloy` | `brew services restart grafana/grafana/alloy` |

Keep the password in a file of its own beside it, readable only by Alloy. **URL-encode it first**, because it goes inside a URL: write `#` as `%23`, `/` as `%2F`, `?` as `%3F`, and `%` as `%25`. A raw `#`, `/`, or `?` stops Alloy loading its config at all, not just this block. On **Linux**:

```bash
read -rs PW && printf '%s' "$PW" | sudo tee /etc/alloy/mssql-password >/dev/null; unset PW
sudo chown root:alloy /etc/alloy/mssql-password
sudo chmod 640 /etc/alloy/mssql-password
```

On **Windows**, in an administrator PowerShell:

```powershell
Set-Content -NoNewline -Path "$env:ProgramFiles\GrafanaLabs\Alloy\mssql-password" -Value (Read-Host "Password")
```

On **macOS**, the first line alone, writing to `$(brew --prefix)/etc/alloy/mssql-password` without `sudo`.

!!! warning
    The file must hold the encoded password and nothing else: a trailing newline, which most editors add, makes the login fail.

Then add to the config file:

```river
local.file "mssql_password" {
  // Windows: "C:/Program Files/GrafanaLabs/Alloy/mssql-password"
  filename  = "/etc/alloy/mssql-password"
  is_secret = true
}

prometheus.exporter.mssql "db" {
  connection_string = "sqlserver://opspilot_exporter:" + local.file.mssql_password.content + "@sqlhost:1433?encrypt=true&trustservercertificate=true"
}

prometheus.scrape "db" {
  targets         = prometheus.exporter.mssql.db.targets
  scrape_interval = "30s"
  forward_to      = [prometheus.remote_write.opspilot.receiver]
}
```

- **Leave `job` alone.** Alloy labels these metrics `job="integrations/mssql"` whatever you call the block, and the dashboard and alerts select on that, so add no `job_name` and no relabel rule for `job`.
- **One exporter per instance.** For a second server, add a second pair of blocks with different names. Each instance appears on the dashboard as the `host:port` from its connection string.

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

Alloy also needs one environment variable, **`GODEBUG=x509negativeserial=1`** (explained in [The self-signed certificate](#the-self-signed-certificate) below) - set it now rather than after the first failure. It goes in `/etc/default/alloy` (Debian, Ubuntu), `/etc/sysconfig/alloy` (RHEL, SUSE), `$(brew --prefix)/etc/alloy/config.env` (macOS), or on Windows the `Environment` value of the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\GrafanaLabs\Alloy`, then restart Alloy.

!!! note "Using environment variables instead"
    Environment variables work in place of files, too, if you already manage Alloy's settings that way: write `sys.env("MSSQL_EXPORTER_PASSWORD")` in place of `local.file.mssql_password.content`, and likewise for the key, and set them in the same place as `GODEBUG`.

---

## 4. Collect the error log

This needs Alloy on the same machine as SQL Server, since it reads the file. Ask SQL Server where its log is:

```sql
SELECT SERVERPROPERTY('ErrorLogFileName');
```

and use that path here, with the same `instance` the metrics have - the `host:port` from the connection string - so the two dashboards line up:

```river
loki.source.file "mssql_errorlog" {
  targets = [{
    // Windows, SQL Server 2022 default instance:
    // "C:/Program Files/Microsoft SQL Server/MSSQL16.MSSQLSERVER/MSSQL/Log/ERRORLOG"
    __path__ = "/var/opt/mssql/log/errorlog",
    job      = "integrations/mssql",
    instance = "sqlhost:1433",
  }]
  forward_to = [loki.process.mssql_errorlog.receiver]
}

loki.process "mssql_errorlog" {
  stage.multiline {
    firstline     = "^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}\\.\\d{2}"
    max_wait_time = "3s"
  }
  stage.regex {
    expression = "^(?P<ts>\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}\\.\\d{2}) +(?P<source>\\S+)"
  }
  stage.regex {
    source     = "source"
    expression = "^(?P<source>spid)\\d+s?$"
  }
  stage.timestamp {
    source   = "ts"
    format   = "2006-01-02 15:04:05.00"
    location = "Local"
  }
  stage.drop {
    older_than = "24h"
  }
  stage.labels {
    values = { source = "" }
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

On **Linux**, let Alloy read the file. It is readable only by SQL Server's group, so `sudo usermod -aG mssql alloy` and restart Alloy.

On **Windows**, write the path with forward slashes, as in the comment, or double every backslash. `MSSQL16.MSSQLSERVER` is the version and instance name, so a named instance or another version has its own folder, and an in-place upgrade moves the log to a new one: update the path after upgrading. The file is UTF-16; Alloy reads that as it is, with no encoding setting.

Keep the stages as they are. They join multi-line entries, take each entry's time from the log itself, and turn `spid51`, `spid62s`, and the rest into one `source` label, which is what the logs dashboard filters on. The last 24 hours are sent when Alloy first starts, and nothing older.

---

## The self-signed certificate

With no certificate configured, SQL Server encrypts connections with one it generates itself. SQL Server 2017 and 2022 generate a new one every time they start, and about half of those carry a negative serial number, which Alloy refuses. So collection can work today and stop after the next SQL Server restart, with nothing failing visibly - the Alloy log just repeats:

```text
TLS Handshake failed: tls: failed to parse certificate from server: x509: negative serial number
```

The fix is to give SQL Server a proper certificate. Until then, the **`GODEBUG=x509negativeserial=1`** set above makes Alloy accept the certificate and keeps the connection encrypted.

!!! warning
    Don't reach for `encrypt=disable` instead. It also makes the error go away, but it does so by sending the login, password included, **unencrypted**.

---

## Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
mssql_local_time_seconds
```

You should get one series per instance. Don't check `up` instead: it reads `1` whenever Alloy reaches the exporter, even when the exporter cannot log in to SQL Server and is sending nothing else. If this query comes back empty, the Alloy log for `prometheus.exporter.mssql` says why - the login, the permissions, and the certificate above are the usual three.

For the error log, select the **Logs** data source and run `{job="integrations/mssql"}`. If nothing comes back, the Alloy log for `loki.source.file` says whether it could open the file.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
