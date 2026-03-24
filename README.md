# OpsPilot Documentation

This is the repository for [OpsPilot](https://app.opspilot.com) documentation. It contains all the source files used to build the OpsPilot docs site.

## About OpsPilot

OpsPilot is an AI-powered observability platform built for modern engineering teams. It combines metrics, logs, and traces in one place — giving you full-stack visibility with the intelligence to act on it fast.

Key capabilities include:

- **AI-assisted operations** — the OpsPilot Assistant analyses your telemetry and surfaces actionable insights without requiring deep query expertise
- **OpenTelemetry-native** — send data from any language or framework using the OTel Collector, Grafana Alloy, or the FusionReactor Agent
- **Dashboards** — pre-built and custom dashboards combining metrics, logs, and trace data
- **Alerting & Anomaly Detection** — rule-based and AI-driven alerts across your entire stack
- **Integrations** — connect your existing tools including Slack, Jira, Kubernetes, and more

## Running locally

To run the docs locally:

```bash
python -m mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. The site hot-reloads on file save.

## How to Contribute

Contributions are welcome. You can:

- Report documentation issues
- Submit pull requests for improvements
- Suggest new documentation topics

For guidelines, see the [Contributing Guide](docs/Contribute/how-to-contribute.md).

## Support

Reach out via the in-app chat or email [support@fusion-reactor.com](mailto:support@fusion-reactor.com). Support is available Monday to Friday, 08:00–18:00 CET.

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
