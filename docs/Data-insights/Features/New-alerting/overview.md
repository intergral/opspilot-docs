# Alerting

Alerting tells you when something needs attention - ideally before your users do. It covers the static rules you define, the AI detectors that learn what normal looks like for you, and the notification setup that decides who hears about it and when.

Navigate to **Alerting** in the left-hand menu to open it.

## What's in this section

| Page | Use it to |
|---|---|
| [Status](status.md) | See every alert rule's state at a glance, and find what needs attention first |
| [Alert Rules](rules.md) | Build, manage, and investigate static alert rules |
| [Annotation Templates](annotation-templates.md) | Write alert messages that carry live values from the query that fired |
| [Recording Rules](recording-rules.md) | Pre-compute expensive queries and save the result as a new metric |
| [Service Anomaly Detectors](service-anomaly-detectors.md) | Tune the detectors created automatically for each instrumented service |
| [Custom Anomaly Detectors](custom-anomaly-detectors.md) | Run anomaly detection against your own PromQL series |
| [Contact Points](contact-points.md) | Define where notifications are sent |
| [Notification Policy](notification-policy.md) | Route each alert to the right contact point |
| [Silences](silences.md) | Suppress notifications temporarily |
| [Time Intervals](time-intervals.md) | Suppress notifications on a schedule, such as outside working hours |
| [Troubleshooting](troubleshooting.md) | Diagnose why an alert did or did not fire |

## Rules or detectors?

**Rules** are static checks - they run on a fixed schedule against fixed thresholds, best for known conditions with clear boundaries, like system CPU or allocated memory.

**Detectors** use AI to learn normal behavior and flag anomalies automatically, so they adapt as your system changes. Use them where a fixed threshold would be guesswork - set too tight it produces false alarms, set too loose it misses real problems.

The two are not exclusive. Most environments use both.

## Common controls

Every alerting page shares the same set of controls:

- **Breadcrumbs** at the top of the page - **Alerting › Status**, for example - move between the alerting pages. Each breadcrumb has a dropdown, so you can go directly to another page.
- **An introductory banner** describes what the page does. Click **Dismiss** to hide it.
- **A refresh control** at the right of the toolbar sets how often the page updates (such as, **30s**), with a button beside it to refresh immediately.
- **An OpsPilot dropdown**, on most pages, offers AI shortcuts for the page you are viewing - help writing a rule, an explanation of what is firing, or suggestions for what to add.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
