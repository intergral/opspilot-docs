# PostgreSQL

Monitor PostgreSQL databases - connections, throughput, cache efficiency, and locks.

Your database shows up alongside the rest of your telemetry, on a dashboard that is already built. You can see how Postgres is behaving - how many connections are in use, how much work it is doing, how well its cache is serving reads, and what is waiting on locks - next to the applications running against it.

!!! info "What this integration does"
    It provisions a **dashboard**. It does not collect anything itself and never connects to your database - the metrics come from **Grafana Alloy**, which has `postgres_exporter` built in. Until Alloy is collecting them, the dashboard is empty.

Navigate to **Integrations** from the left-hand sidebar, then select **PostgreSQL**.

---

## Permission tiers

PostgreSQL runs **Read-only**, which is the default and requires nothing - the metrics endpoint and signing key come from the service environment.

Its one **capability** is **Dashboards**: installing it provisions the dashboard and nothing else.

---

## 1. Create a monitoring role

The exporter only ever reads. Give it its own role rather than reusing an application login, and grant it `pg_monitor` - a built-in role that carries exactly the read access the statistics views need and nothing else:

```sql
CREATE USER opspilot_exporter WITH PASSWORD 'a strong password';
GRANT pg_monitor TO opspilot_exporter;
```

Run that once per database server, not once per database.

---

## 2. Configure Alloy

If you have no collector yet, the [Grafana Alloy guide](../../../../Monitor-your-data/OpenTelemetry/Shipping/Collector.md) covers installing one and getting an API key. That guide configures Alloy for OTLP; these metrics are Prometheus-format, so the components below are different, but the install and the API key are the same.

```river
prometheus.exporter.postgres "db" {
  data_source_names = [
    "postgresql://opspilot_exporter:PASSWORD@localhost:5432/postgres?sslmode=disable",
  ]
}

prometheus.scrape "db" {
  targets = prometheus.exporter.postgres.db.targets

  scrape_interval = "30s"

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

A few things in there are worth understanding before you change them.

**One connection string per server, not per database.** The exporter reports on every database on the server it connects to, so `postgres` as the connection database is conventional and sufficient. Listing several servers here gives you several instances on the dashboard; listing several databases on the same server gives you the same metrics several times over.

**Put the password in an environment variable rather than the file.** Alloy reads the config in plain text, so:

```river
data_source_names = [
  "postgresql://opspilot_exporter:" + sys.env("PG_EXPORTER_PASSWORD") + "@localhost:5432/postgres?sslmode=disable",
]
```

`sslmode=disable` is for a local socket or a trusted network only. If Alloy reaches the database across anything else, use `sslmode=require` at minimum.

**There is no `job_name` above, deliberately.** Alloy's built-in postgres component labels its own metrics `job="integrations/postgres"`, taking the name from the component, and setting `job_name` on the scrape does not override it. The dashboard reads that label, and also accepts `postgres` and `postgresql` for anyone scraping a standalone `postgres_exporter`. If you rename the component from `db` the label changes with it and the dashboard stops matching, so leave the name alone or add a relabel rule.

**The instance label is the connection string, minus the credentials.** A server appears on the dashboard as `postgresql://host:5432/postgres` rather than as a hostname. The exporter strips the username, password, and query parameters before labeling, so nothing secret reaches your metrics store.

---

## 3. Confirm the data arrived

In OpsPilot, open **Explore**, select the **Metrics** data source, and run:

```promql
pg_up
```

You should get one series per server, reading `1`. If that returns data, the dashboard will too.

---

## Troubleshooting

**`pg_up` is 0.** Alloy is reaching the exporter but the exporter cannot reach Postgres. Check the credentials, that the host and port are right from where Alloy runs, and that `pg_hba.conf` allows the connection.

**Nothing in Explore at all.** Check the Alloy UI on port `12345` - a failing component shows there with the error.

**Permission errors in the Alloy log.** The role is missing `pg_monitor`. Some statistics views return no rows rather than failing, so the dashboard may be partly populated rather than empty.

**The dashboard shows more databases than you expected.** Postgres' own `template0`, `template1`, and `postgres` databases are excluded from every panel. Anything else on the server appears, because the exporter reports on all of them.

**Nothing about individual tables.** `pg_stat_user_tables` only covers the database the connection string names, which is why there is no per-table panel - see the integration's README for the detail.

---

## What is not here

A few things this dashboard deliberately does not show:

**Database uptime.** It needs the `postmaster` collector, which is off by default. There is a `process_start_time_seconds` in the exporter's output, but that is the exporter's own start time rather than the database's, so the dashboard reads neither.

**Query-level statistics.** Which queries are slow, and how often they run, comes from the `pg_stat_statements` extension and a collector that is off by default. It is worth having when you are investigating something, but it is a diagnostic tool rather than a health signal, and it costs a series per distinct query shape.

**Replication.** The metrics exist but need a replica to mean anything, and what you want to see differs enough between streaming replication, logical replication, and a managed service that one generic panel would mislead.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
