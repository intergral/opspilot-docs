# Services FAQ

## General

### What is the difference between Services, Servers, and Applications?

**Services** shows your instrumented services as reported via OpenTelemetry traces — focusing on request flow, latency, errors, and inter-service dependencies. **Servers** shows the underlying infrastructure (CPU, memory, disk) for the hosts your services run on. **Applications** focuses on JVM and application-level metrics for FusionReactor-monitored apps. Use Services when you want to understand how requests move through your system; use Servers when you want to investigate the health of the infrastructure underneath.

### Why is a service not appearing in the Service Graph or table?

A service only appears if it is sending trace data to OpsPilot. Check that your service is instrumented with OpenTelemetry and that trace data is being received. If the service recently started sending data, try extending the time range to confirm it is visible over a longer period.

---

## Performance

### What is the difference between P50 and P95 latency?

**P50** (median) is the latency that 50% of requests complete within — it represents typical performance. **P95** is the latency that 95% of requests complete within — it highlights slower, tail-end responses that affect a minority of users but often indicate underlying issues. A large gap between P50 and P95 suggests inconsistent performance worth investigating.

### Why does Avg Latency look different from P50?

Average latency is pulled up by outliers — a small number of very slow requests can make the average much higher than the median. P50 is usually a better indicator of the experience most users have.

---

## Traces and spans

### What is the difference between a span and a trace?

A **trace** represents the full journey of a single request through your system, from entry point to completion. A **span** is one unit of work within that trace — for example, a database query or an outbound HTTP call. A trace is made up of one or more spans.

### What do the span status codes mean?

| Status | Description |
|---|---|
| **STATUS_CODE_OK** | The span completed successfully |
| **STATUS_CODE_ERROR** | The span completed with an error |
| **STATUS_CODE_UNSET** | No status was explicitly set — typically treated as successful |

A high proportion of STATUS_CODE_ERROR spans indicates errors worth investigating in the Span Errors table or Traces tab.

---

## Logs and patterns

### Why are no log patterns showing?

Log patterns are detected automatically from log output in the selected time range. If no patterns appear, it may mean logs are not being sent for the selected service, the volume is too low to detect a pattern, or the time range is too narrow. Try extending the time range or verifying that log data is flowing for the service.

### Why are no alerts showing for my service?

The Alerts section only shows alert rules that are associated with the selected service. If no alerts appear, either no alert rules have been configured for that service, or the service name does not match any existing rule conditions. Check your alert rules under the Alerts section.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
