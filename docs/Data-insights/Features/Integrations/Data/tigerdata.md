# TigerData

Monitor TigerData (TimescaleDB) hypertables, the columnstore, and background jobs and policies.

Your TimescaleDB databases show up alongside the rest of your telemetry, on dashboards that are already built. You can see how your hypertables are growing and how much the columnstore saves, and keep watch on the background jobs that compress, retain, and aggregate your data - with alerts when one fails, crashes, or falls behind, or when a server stops reporting. Works for self-hosted TimescaleDB and Tiger Cloud.

!!! info "What this integration does"
    It provisions **dashboards** and **alert rules**. It does not collect anything itself - **Grafana Alloy** gathers what TimescaleDB knows about its hypertables, columnstore, and background jobs by running a few queries against each database where TimescaleDB is installed. This works for self-hosted TimescaleDB 2.17 and later and for Tiger Cloud services. For the PostgreSQL server itself - connections, cache, locks - install the [PostgreSQL integration](postgres.md) as well. Until Alloy is collecting, the dashboards are empty.

Navigate to **Integrations** from the left-hand sidebar, then select **TigerData**.

---

## Permission tiers

TigerData runs **Read-only**, the default. It requires a database user Alloy can log in as - it needs no privileges - and an **OpsPilot API key**.

Its **capabilities** are **Dashboards** and **Alerts**.

Grafana's own docs cover the exporter in full: see [`prometheus.exporter.postgres`](https://grafana.com/docs/alloy/latest/reference/components/prometheus/prometheus.exporter.postgres/) for every option, and [install Alloy](https://grafana.com/docs/alloy/latest/set-up/install/) anywhere that can reach the database.

---

## 1. Create a monitoring user

Connect as an administrator - on Tiger Cloud, `tsdbadmin` - and create a user for Alloy:

```sql
CREATE USER opspilot_monitor WITH PASSWORD '<password>';
```

It needs no other privilege: TimescaleDB's information views and size functions are readable by any user who can connect, and show sizes and job status, never data.

---

## 2. Save the queries

Save this as `timescaledb-queries.yaml` beside Alloy's config file:

```yaml
timescaledb_extension:
  query: |
    SELECT current_database() AS datname, extversion AS version, 1 AS info
    FROM pg_extension WHERE extname = 'timescaledb'
  metrics:
    - datname: {usage: LABEL, description: "Database"}
    - version: {usage: LABEL, description: "TimescaleDB version"}
    - info: {usage: GAUGE, description: "TimescaleDB is installed in this database"}

timescaledb_hypertable:
  cache_seconds: 300
  query: |
    SELECT current_database() AS datname, h.hypertable_schema AS schema, h.hypertable_name AS hypertable,
      h.num_chunks AS chunks,
      h.compression_enabled::int AS columnstore_enabled,
      hypertable_size(format('%I.%I', h.hypertable_schema, h.hypertable_name)::regclass) AS size_bytes,
      coalesce(cs.number_compressed_chunks, 0) AS columnstore_chunks,
      coalesce(cs.before_compression_total_bytes, 0) AS columnstore_before_bytes,
      coalesce(cs.after_compression_total_bytes, 0) AS columnstore_after_bytes
    FROM timescaledb_information.hypertables h
    LEFT JOIN LATERAL hypertable_compression_stats(format('%I.%I', h.hypertable_schema, h.hypertable_name)::regclass) cs ON true
  metrics:
    - datname: {usage: LABEL, description: "Database"}
    - schema: {usage: LABEL, description: "Hypertable schema"}
    - hypertable: {usage: LABEL, description: "Hypertable"}
    - chunks: {usage: GAUGE, description: "Chunks"}
    - columnstore_enabled: {usage: GAUGE, description: "1 if the columnstore (compression) is enabled"}
    - size_bytes: {usage: GAUGE, description: "Total size, tables, indexes and TOAST"}
    - columnstore_chunks: {usage: GAUGE, description: "Chunks in the columnstore (compressed)"}
    - columnstore_before_bytes: {usage: GAUGE, description: "Size of the columnstore chunks before conversion"}
    - columnstore_after_bytes: {usage: GAUGE, description: "Size of the columnstore chunks after conversion"}

timescaledb_job:
  query: |
    SELECT current_database() AS datname, j.job_id::text AS job_id, j.proc_name AS proc,
      coalesce(ca.view_name, j.hypertable_name, '') AS relation,
      j.scheduled::int AS scheduled,
      extract(epoch FROM j.schedule_interval) AS schedule_interval_seconds,
      coalesce((s.last_run_status = 'Failed')::int, 0) AS last_run_failed,
      coalesce((s.job_status = 'Running')::int, 0) AS running,
      s.total_runs AS runs_total, s.total_failures AS failures_total,
      coalesce(st.consecutive_failures, 0) AS consecutive_failures,
      coalesce(st.total_crashes, 0) AS crashes_total,
      coalesce(st.consecutive_crashes, 0) AS consecutive_crashes,
      CASE WHEN s.last_successful_finish > '-infinity' THEN extract(epoch FROM s.last_successful_finish) END AS last_success_timestamp_seconds
    FROM timescaledb_information.jobs j
    JOIN timescaledb_information.job_stats s USING (job_id)
    LEFT JOIN _timescaledb_internal.bgw_job_stat st USING (job_id)
    LEFT JOIN timescaledb_information.continuous_aggregates ca
      ON ca.materialization_hypertable_schema = j.hypertable_schema AND ca.materialization_hypertable_name = j.hypertable_name
  metrics:
    - datname: {usage: LABEL, description: "Database"}
    - job_id: {usage: LABEL, description: "Job id"}
    - proc: {usage: LABEL, description: "The job's procedure: a policy, or a user action"}
    - relation: {usage: LABEL, description: "The hypertable or continuous aggregate the job works on"}
    - scheduled: {usage: GAUGE, description: "1 if the job is scheduled, 0 if paused"}
    - schedule_interval_seconds: {usage: GAUGE, description: "How often the job runs"}
    - last_run_failed: {usage: GAUGE, description: "1 if the job's last run failed"}
    - running: {usage: GAUGE, description: "1 while the job is running"}
    - runs_total: {usage: COUNTER, description: "Runs"}
    - failures_total: {usage: COUNTER, description: "Failed runs"}
    - consecutive_failures: {usage: GAUGE, description: "Failed runs since the last success"}
    - crashes_total: {usage: COUNTER, description: "Runs whose background worker crashed"}
    - consecutive_crashes: {usage: GAUGE, description: "Crashed runs since the last success"}
    - last_success_timestamp_seconds: {usage: GAUGE, description: "When the job last finished successfully"}
```

Sizes are re-read every five minutes rather than every scrape, since they walk every chunk. Alloy reads this file only when it starts.

---

## 3. Configure Alloy

Alloy's config file is in a different place on each system:

| OS | Config file | After a change |
|---|---|---|
| **Linux** | `/etc/alloy/config.alloy` | `sudo systemctl restart alloy` |
| **Windows** | `C:\Program Files\GrafanaLabs\Alloy\config.alloy` | restart the Alloy service in `services.msc` |
| **macOS** | `$(brew --prefix)/etc/alloy/config.alloy` | `brew services restart grafana/grafana/alloy` |

Put the monitoring user's password in a file beside the config, readable only by Alloy, written without a trailing newline, and add:

```river
local.file "timescaledb_password" {
  filename  = "/etc/alloy/timescaledb-password"
  is_secret = true
}

prometheus.exporter.postgres "timescaledb" {
  data_source_names = ["postgresql://opspilot_monitor:" + local.file.timescaledb_password.content + "@db.example.com:5432/tsdb?sslmode=require"]
  disable_default_metrics    = true
  disable_settings_metrics   = true
  custom_queries_config_path = "/etc/alloy/timescaledb-queries.yaml"

  autodiscovery {
    enabled            = true
    database_allowlist = ["tsdb"]
  }
}

discovery.relabel "timescaledb" {
  targets = prometheus.exporter.postgres.timescaledb.targets

  rule {
    target_label = "job"
    replacement  = "integrations/timescaledb"
  }
}

prometheus.scrape "timescaledb" {
  targets         = discovery.relabel.timescaledb.output
  scrape_interval = "60s"
  forward_to      = [prometheus.remote_write.opspilot.receiver]
}
```

A few things worth understanding:

- **List every database that has TimescaleDB in `database_allowlist`, and connect to one of them.** The queries run in each; in a database without TimescaleDB they fail on every scrape. On Tiger Cloud the database is `tsdb` and the host and port are the service's, from the Console.
- **URL-encode the password** if it contains `@`, `:`, `/`, `?`, `#`, or `%` - it is part of a URL.
- **Keep the relabel rule.** Alloy gives every PostgreSQL exporter the same `job`, so without it these series would land beside the PostgreSQL integration's, and the dashboards select on the `job` it sets.
- **For more than one server,** repeat the exporter for each under a name of its own (letters, digits, and underscores), and list their targets together: `targets = array.concat(prometheus.exporter.postgres.one.targets, prometheus.exporter.postgres.two.targets)`.

---

## 4. Send data to OpsPilot

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
    Environment variables work in place of files if you already manage Alloy's settings that way: write `sys.env("TIMESCALEDB_PASSWORD")` in place of `local.file.timescaledb_password.content`, and `sys.env("OPSPILOT_API_KEY")` for the key. Alloy reads its environment from `/etc/default/alloy` (Debian, Ubuntu), `/etc/sysconfig/alloy` (RHEL, SUSE), `$(brew --prefix)/etc/alloy/config.env` (macOS), or on Windows the `Environment` value of the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\GrafanaLabs\Alloy`.

---

## 5. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
timescaledb_extension_info
```

You should get one series per database, carrying its TimescaleDB version. If nothing comes back, run `pg_up{job="integrations/timescaledb"}`: `0` means Alloy cannot connect or log in, and the Alloy log for `prometheus.exporter.postgres` says why; no result at all means Alloy is not sending.

Once data is flowing, the **Dashboard data** column on **Your installation** links straight to the provisioned dashboards.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
