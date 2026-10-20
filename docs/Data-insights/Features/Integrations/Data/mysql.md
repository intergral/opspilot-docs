# MySQL

Monitor MySQL and MariaDB - queries, connections, replication, InnoDB, and the error log.

Your MySQL and MariaDB servers show up alongside the rest of your telemetry, on dashboards that are already built. You can see how hard each server is working and where it is struggling - connections, slow queries, deadlocks, InnoDB, and replication - alongside their error logs, with alerts when one stops reporting, a replica stops or falls behind, or a server runs short of connections.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - **Grafana Alloy** has a MySQL exporter built in, so collecting metrics needs a user on the server and a few lines of Alloy config, and the error log needs a few more. This covers MySQL 8.0 and later and MariaDB 10.11 and later. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **MySQL**.

---

## Permission tiers

MySQL runs **Read-only**, the default. It requires a MySQL or MariaDB user that can read server status (**`PROCESS`** and **`REPLICATION CLIENT`**), read access to the error log for Alloy, and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

Grafana's own docs cover the exporter in full: see [`prometheus.exporter.mysql`](https://grafana.com/docs/alloy/latest/reference/components/prometheus/prometheus.exporter.mysql/) for every option, and [install Alloy](https://grafana.com/docs/alloy/latest/set-up/install/) on the database host if you want the error log (Alloy reads it from disk), or anywhere that can reach the server's port for metrics alone.

---

## 1. Create a monitoring user

Alloy logs in to read the server's status. Give it a user of its own that can read that status and nothing else, rather than `root` or an application's user. On each server:

```sql
CREATE USER 'opspilot_exporter'@'%' IDENTIFIED BY '<a strong password>' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT ON *.* TO 'opspilot_exporter'@'%';
```

On MariaDB, also:

```sql
GRANT SLAVE MONITOR ON *.* TO 'opspilot_exporter'@'%';
```

Neither grant reads table data. `mysqld_exporter`'s required grants also include `SELECT ON *.*`, which lets the user read every table; the collectors below do not need it, so leave it out. Replace `%` with the address Alloy connects from to allow only that host. `MAX_USER_CONNECTIONS 3` stops monitoring adding to the load on a server that is already struggling. The password cannot contain `?`; any other character works as it is.

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
read -rs PW && printf '%s' "$PW" | sudo tee /etc/alloy/mysql-password >/dev/null; unset PW
sudo chown root:alloy /etc/alloy/mysql-password
sudo chmod 640 /etc/alloy/mysql-password
```

On **Windows**, in an administrator PowerShell:

```powershell
Set-Content -NoNewline -Path "$env:ProgramFiles\GrafanaLabs\Alloy\mysql-password" -Value (Read-Host "Password")
```

On **macOS**, the first line alone, writing to `$(brew --prefix)/etc/alloy/mysql-password` without `sudo`.

!!! warning
    The file must hold the password and nothing else: a trailing newline, which most editors add, makes the login fail with `Access denied`.

Then add to the config file:

```river
local.file "mysql_password" {
  // Windows: "C:/Program Files/GrafanaLabs/Alloy/mysql-password"
  filename  = "/etc/alloy/mysql-password"
  is_secret = true
}

prometheus.exporter.mysql "db" {
  data_source_name  = "opspilot_exporter:" + local.file.mysql_password.content + "@tcp(dbhost:3306)/"
  enable_collectors = ["info_schema.innodb_metrics"]
}

discovery.relabel "db" {
  targets = prometheus.exporter.mysql.db.targets

  rule {
    source_labels = ["instance"]
    regex         = "[^(]*\\((.*)\\)/.*"
    target_label  = "instance"
  }
}

prometheus.scrape "db" {
  targets         = discovery.relabel.db.output
  scrape_interval = "30s"
  forward_to      = [prometheus.remote_write.opspilot.receiver]
}
```

- **`enable_collectors`** is what counts deadlocks on MySQL. MariaDB reports them without it, so leave the line out there.
- **The relabel rule names each server `dbhost:3306`.** Without it the dashboards show `tcp(dbhost:3306)/`.
- **Leave `job` alone.** Alloy labels these metrics `job="integrations/mysql"` whatever you call the blocks, and the dashboards and alerts select on that, so add no `job_name` and no relabel rule for `job`.
- **One exporter per server.** For a second server, add a second set of blocks with different names.

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
    Environment variables work in place of files if you already manage Alloy's settings that way: write `sys.env("MYSQL_EXPORTER_PASSWORD")` in place of `local.file.mysql_password.content`, and likewise for the key. Alloy reads its environment from `/etc/default/alloy` (Debian, Ubuntu), `/etc/sysconfig/alloy` (RHEL, SUSE), `$(brew --prefix)/etc/alloy/config.env` (macOS), or on Windows the `Environment` value of the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\GrafanaLabs\Alloy`.

---

## 4. Collect the error log

This needs Alloy on the same machine as the server, since it reads the file. Ask the server where its log is:

```sql
SELECT @@log_error, @@datadir;
```

A relative path is inside the data directory. Use it here, with the same `instance` the metrics have - `dbhost:3306` - so the dashboards line up:

```river
loki.source.file "mysql_errorlog" {
  targets = [{
    // Windows, MySQL: "C:/ProgramData/MySQL/MySQL Server 8.4/Data/<host name>.err"
    // Windows, MariaDB: "C:/Program Files/MariaDB 11.8/data/<host name>.err"
    __path__ = "/var/log/mysql/error.log",
    job      = "integrations/mysql",
    instance = "dbhost:3306",
  }]
  forward_to = [loki.process.mysql_errorlog.receiver]
}

loki.process "mysql_errorlog" {
  stage.multiline {
    firstline     = "^\\d{4}-\\d{2}-\\d{2}[T ]\\d{2}:\\d{2}:\\d{2}"
    max_wait_time = "3s"
  }
  stage.regex {
    expression = "^(?P<ts_mysql>\\d{4}-\\d{2}-\\d{2}T\\S+) +\\d+ \\[(?P<level>[A-Za-z]+)\\]"
  }
  stage.regex {
    expression = "^(?P<ts_mariadb>\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}) +\\d+ \\[(?P<level>[A-Za-z]+)\\]"
  }
  stage.timestamp {
    source = "ts_mysql"
    format = "RFC3339Nano"
  }
  stage.timestamp {
    source   = "ts_mariadb"
    format   = "2006-01-02 15:04:05"
    location = "Local"
  }
  stage.drop {
    older_than = "24h"
  }
  stage.template {
    source   = "level"
    template = "{{ ToLower .Value }}"
  }
  stage.labels {
    values = { level = "" }
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

Keep the stages as they are. They handle both MySQL's and MariaDB's formats, join multi-line entries, take each entry's time from the log itself, and turn the level into the label the dashboard filters on. The last 24 hours are sent when Alloy first starts, and nothing older.

On **Windows**, write the path with forward slashes, as in the comment, or double every backslash. Alloy runs as LocalSystem there and can read the file as it is.

On **Linux**, let Alloy read the file, then restart Alloy:

| Server | Log | Run |
|---|---|---|
| MySQL, Debian or Ubuntu package | `/var/log/mysql/error.log` | `sudo usermod -aG adm alloy` |
| MySQL, RHEL family | `/var/log/mysql/mysqld.log` | `sudo usermod -aG mysql alloy` |
| MariaDB, RHEL family | `/var/log/mariadb/mariadb.log` | `sudo usermod -aG mysql alloy` |

MariaDB on Debian and Ubuntu writes no log file - `@@log_error` comes back empty and the log goes to the system journal. Turn the file on:

```bash
sudo install -d -o mysql -g mysql -m 750 /var/log/mysql
sudo sed -i 's|^#log_error = /var/log/mysql/error.log|log_error = /var/log/mysql/error.log|' /etc/mysql/mariadb.conf.d/50-server.cnf
sudo systemctl restart mariadb
sudo usermod -aG mysql alloy
```

---

## 5. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
mysql_up
```

You should get one series per server, reading `1`. `0` means Alloy cannot log in, and the Alloy log for `prometheus.exporter.mysql` says why - usually the password, or `%` replaced with an address that is not the one Alloy connects from.

For the error log, select the **Logs** data source and run `{job="integrations/mysql"}`. If nothing comes back, the Alloy log for `loki.source.file` says whether it could open the file.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
