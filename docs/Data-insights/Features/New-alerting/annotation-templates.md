# Annotation Templates

Alert annotations and labels support **Go template strings**, so the text an alert sends can describe what actually happened rather than repeating a fixed sentence. You can pull in the value that fired the rule, the labels on the series, and the threshold it crossed - and change the wording depending on any of them.

Templates are written in [Go's text/template syntax](https://pkg.go.dev/text/template), the same syntax Prometheus and Grafana use.

!!! info "For advanced users"
    Plain text annotations work perfectly well. Templates are worth reaching for when you want an alert to explain itself - which host, which value, and how far past the limit.

---

## Where templates work

Templates can be used in any annotation on an alert rule - **Summary**, **Description**, **Runbook URL**, and any custom annotation you add with **+ Add annotation** - and in custom labels. See [Rules](rules.md#annotations) for where these sit in the rule editor.

---

## Variables

| Variable | Contains |
|---|---|
| `$labels` | The labels from the query, such as `{{ $labels.instance }}` |
| `$values` | The labels and values of every instant query and expression, indexed by **reference ID** - `{{ $values.query.Value }}` for the value, `{{ $values.query.Labels }}` for its labels |
| `$value` | A single string containing the labels and values of all instant queries, threshold, reduce, and math expressions. Useful for a quick dump, but `$values` is better when you want one specific number |

`$values` is indexed by the **reference ID** of each step in the query chain, so a rule built from the default **Query → Reduce → Threshold** chain exposes `$values.query`, `$values.reduce`, and `$values.threshold`. If you renamed a step, use the name you gave it.

---

## A simple example

```go
Error rate is {{ if $values.query }}{{ $values.query }}{{ else }}returning No Data{{ end }}% on {{ if $labels.instance }}{{ $labels.instance }}{{ else }}an unknown instance{{ end }}
```

The `if`/`else` pairs matter: an alert can fire when a query returns nothing, and a template that assumes a value is present will produce a confusing message when there isn't one.

---

## Functions

Templates can transform values as well as print them.

| Function | Does |
|---|---|
| `humanize` | Abbreviates a decimal number - `1000.0` becomes `1k` |
| `humanize1024` | The same, base 1024 - `1024.0` becomes `1ki` |
| `humanizeDuration` | Seconds to a readable duration - `60.0` becomes `1m 0s` |
| `humanizePercentage` | A 0-1 ratio to a percentage - `0.2` becomes `20%` |
| `humanizeTimestamp` | A Unix timestamp to a readable time |
| `title`, `toUpper`, `toLower` | Change the case of a string |
| `stripPort` | The hostname from a `host:port` string |
| `stripDomain` | Removes the domain, keeping the port |
| `match` | Tests a string against a regular expression |
| `reReplaceAll` | Replaces regular expression matches |
| `parseDuration` | A duration string such as `1h` to seconds |
| `graphLink`, `tableLink` | A link to the graph or table view in Explore |

---

## A worked example

This template reports CPU differently depending on whether the host is above or below its ceiling, names the host when it can, and says so plainly when the query returned nothing:

```go
{{ if $values.query }}{{ $cpu := $values.query.Value }}{{ $host := or $labels.instance "an unidentified host" }}{{ if gt $cpu 80.0 }}{{ $host }} is running hot: CPU sustained at {{ humanize $cpu }}% over the last 5 minutes, past the 80% ceiling.{{ else }}{{ $host }} has settled to {{ humanize $cpu }}% CPU, back inside the 80% ceiling.{{ end }}{{ else }}CPU could not be read for {{ or $labels.instance "this host" }} — the query returned no value.{{ end }}
```

!!! warning "Keep it on one line"
    Go templates print the whitespace between actions, so breaking a template across indented lines puts those line breaks and spaces into the message. Either keep it on a single line, as above, or trim the whitespace with `{{-` and `-}}`.

What it produces:

| Case | Rendered message |
|---|---|
| `87.42` | *web-01 is running hot: CPU sustained at 87.42% over the last 5 minutes, past the 80% ceiling.* |
| `41.66` | *web-01 has settled to 41.66% CPU, back inside the 80% ceiling.* |
| No `instance` label | *an unidentified host is running hot: CPU sustained at 88.1% over the last 5 minutes, past the 80% ceiling.* |
| No data | *CPU could not be read for this host — the query returned no value.* |

Three things are doing the work:

- **`$cpu := $values.query.Value`** assigns the value once, so the rest of the template reads cleanly
- **`or $labels.instance "an unidentified host"`** falls back when the label is missing, instead of printing nothing
- **`gt $cpu 80.0`** branches on the value, so the recovery message reads naturally rather than being a firing message with different numbers

!!! tip
    Write the no-data branch first. It is the case most likely to reach someone at 3am, and the one most often forgotten.

---

## More examples

Patterns worth adapting. Each assumes a query with the reference ID `query` - change that to match your own rule.

### Bytes into something readable

`humanize1024` turns a raw byte count into the units people actually use.

```go
Disk on {{ $labels.instance }} is down to {{ humanize1024 $values.query.Value }}B free.
```

*Disk on web-01 is down to 1.4GiB free.*

### A ratio as a percentage

If your query returns a ratio between 0 and 1, let `humanizePercentage` do the conversion rather than multiplying in PromQL.

```go
Error ratio on {{ $labels.service }} is {{ humanizePercentage $values.query.Value }}.
```

*Error ratio on checkout is 4.2%.*

### Seconds as a duration

```go
{{ $labels.job }} has been degraded for {{ humanizeDuration $values.query.Value }}.
```

*payments has been degraded for 1h 12m 0s.*

### Dropping the port from an instance label

Prometheus targets usually carry `host:port`. `stripPort` gives you just the host.

```go
{{ stripPort $labels.instance }} is not responding to scrapes.
```

*web-01 is not responding to scrapes.*

### A runbook URL built from labels

Annotations that hold URLs can be templated too, so one rule can point at the right runbook per service.

```go
https://runbooks.internal/{{ $labels.service }}/high-latency
```

### Wording that follows severity

```go
{{ if eq $labels.severity "critical" }}Page the on-call now: {{ else }}For review in the morning: {{ end }}{{ $labels.alertname }} on {{ $labels.instance }}.
```

*Page the on-call now: HighLatency on web-01.*

### Showing every value in the chain

Useful while you are building a rule and want to see what each step produced. `$value` prints the labels and values of every instant query and expression in one go:

```go
Debug: {{ $value }}
```

---

## Annotation templates and notification templates

These are two different things, and they have different variables available:

| | Written on | Variables |
|---|---|---|
| **Annotation templates** | An alert rule, in its annotations and labels | `$labels`, `$values`, `$value` - the labels and values of **this** alert instance |
| **Notification templates** | A contact point, to shape the message it sends | `.Alerts`, `.CommonLabels`, and the fields of each alert - so one message can cover **several** alerts |

A rule that produces several series creates a separate alert instance per series, each with its own `$labels` and `$values`. Iterating over a group of alerts belongs in a notification template, not here. See [Contact Points](contact-points.md#notification-templates) for those.

---

## Further reading

- [Go text/template](https://pkg.go.dev/text/template) - the template syntax itself
- [Annotation and label template reference](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/templates/reference/) - the full list of variables and functions
- [Prometheus notification templates](https://prometheus.io/docs/alerting/latest/notifications/) - the values available in notifications

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
