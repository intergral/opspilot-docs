# Getting started with OpenTelemetry

## What is OpenTelemetry?

OpenTelemetry (OTel) is an industry-standard, open-source observability framework designed to create and manage telemetry data-**Metrics, Traces, and Logs**. It provides a unified set of APIs and libraries that allow you to instrument your applications once and send the data to any backend, such as OpsPilot.

By adopting OpenTelemetry, you avoid vendor lock-in and gain deep visibility into the performance and health of your distributed systems.

### Three steps to seamless integration

OpsPilot has simplified the OTel integration process into three straightforward steps:

1. **[Instrument code](/Monitor-your-data/OpenTelemetry/Instrumentation/Overview/)**: Add OTel to your application (automatically or manually).
2. **[Ship data to OpsPilot](/Monitor-your-data/OpenTelemetry/Shipping/overview/)**: Configure your data flow.
3. **[Visualize data](/Monitor-your-data/OpenTelemetry/Visualize/Metrics/)**: Analyze your performance in the OpsPilot dashboard.

---

## Architecture Overview

OpenTelemetry data flows from your instrumented applications through a telemetry pipeline (Collector) to OpsPilot's observability backends:

```
┌─────────────────────┐
│  Your Application   │
│ (Instrumented with  │
│   OpenTelemetry)    │
└──────────┬──────────┘
           │ OTLP
           ▼
┌─────────────────────┐
│ Telemetry Pipeline  │
│  ┌───────────────┐  │
│  │ OTel Collector│  │
│  │      OR       │  │
│  │ Grafana Alloy │  │
│  └───────────────┘  │
└──────────┬──────────┘
           │ Process & Forward
           ▼
┌─────────────────────┐
│ OpsPilot │
│                     │
│  ┌─────────────┐    │
│  │   Tempo     │    │  ← Traces
│  │   (Traces)  │    │
│  └─────────────┘    │
│                     │
│  ┌─────────────┐    │
│  │   Mimir     │    │  ← Metrics
│  │  (Metrics)  │    │
│  └─────────────┘    │
│                     │
│  ┌─────────────┐    │
│  │    Loki     │    │  ← Logs
│  │   (Logs)    │    │
│  └─────────────┘    │
└─────────────────────┘
```

**Key Components:**

* **Your Application**: Instrumented with OpenTelemetry SDKs to generate traces, metrics, and logs
* **Telemetry Pipeline**: Collector (OpenTelemetry Collector or Grafana Alloy) receives, processes, and forwards telemetry data
* **OpsPilot**: Stores and visualizes your data in purpose-built backends:
    - **Tempo**: Distributed tracing backend
    - **Mimir**: High-performance metrics storage
    - **Loki**: Log aggregation system

---

## Quickstart: Get up and running in 15 minutes

This quickstart provides the fastest path to see OpenTelemetry data flowing into OpsPilot while following production-ready practices.

!!! tip "Production-ready from the start"
    This quickstart uses the OpenTelemetry Collector from the beginning to ensure data reliability and prevent data loss. All production deployments should use a Collector.

### Prerequisites

* **OpsPilot API Key**: Get this from **Account Settings > API Keys** in OpsPilot
* **Docker & Docker Compose**: For running the Collector ([Install Docker](https://docs.docker.com/get-docker/))
* **Your language runtime**: Python, Java, Node.js, Go, .NET, etc.

### Step 1: Set up the OpenTelemetry Collector (5 minutes)

The Collector is a central hub that receives, processes, and forwards your telemetry data to OpsPilot.

**[Follow the Collector setup guide →](/Monitor-your-data/OpenTelemetry/Shipping/Collector/)**

This will walk you through:
- Installing the Collector with Docker Compose
- Configuring it with your OpsPilot API Key
- Verifying it's running correctly

### Step 2: Instrument your application (5 minutes)

Add OpenTelemetry to your application to generate traces, metrics, and logs. Most languages support automatic instrumentation requiring no code changes.

**[Choose your language from the instrumentation guides →](/Monitor-your-data/OpenTelemetry/Instrumentation/Overview/)**

Available languages:
- **Java**, **Python**, **.NET**, **Node.js**, **PHP** (Zero-code instrumentation available)
- **Go**, **Ruby**, **Rust**, **Swift**, **Erlang/Elixir**, **Kotlin**, **C++** (Manual instrumentation)

### Step 3: Verify data in OpsPilot (5 minutes)

Once your application is running and generating traffic, view your telemetry data in OpsPilot.

**[Learn how to visualize your data →](/Monitor-your-data/OpenTelemetry/Visualize/Metrics/)**

You should see:
- **Traces**: Request flows across your services
- **Metrics**: Runtime performance data (CPU, memory, request rates)
- **Logs**: Application logs correlated with traces

!!! success "What's next?"
    Now that you have data flowing, explore these topics:

    - [Configure sampling strategies](/Monitor-your-data/OpenTelemetry/Shipping/Collector/) to manage data volume
    - [Create custom dashboards](/Getting-started/Tutorials/create-dashboard/) to visualize your metrics
    - [Review FAQ](/Monitor-your-data/OpenTelemetry/FAQ/) for common questions
    - [Troubleshooting guide](/Monitor-your-data/OpenTelemetry/Troubleshooting/) if you encounter issues

---

## Core concepts & components

### The signals: Traces, Metrics, and Logs

* **Traces:** Provide a complete map of a request as it moves through your services. They help identify bottlenecks and "hotspots" in your code. OpsPilot uses these to power **Distributed Tracing** visualizations.
* **Metrics:** Numerical data points (such as CPU usage, request rates) used for monitoring trends and setting alerts.
* **Logs:** Structured or unstructured text records that provide context to your traces and metrics, now fully integrated into the OTel standard.

### OTLP (OpenTelemetry Protocol)

OTLP is the standardized language that OpenTelemetry components use to communicate.

!!! note
    OpsPilot is built on OTLP, ensuring high-performance data ingestion and compatibility with the entire OTel ecosystem.

### Instrumentation

Instrumentation is how your application generates telemetry. Over the last two years, **Zero-code injection** (Automatic Instrumentation) has become the standard for most languages (Java, Python, .NET, Go, etc.), allowing you to gather data without changing a single line of your source code.

---

## Shipping telemetry data to OpsPilot

To send data to OpsPilot, you can choose the method that best fits your infrastructure:

* **[OpenTelemetry Collector](/Monitor-your-data/OpenTelemetry/Shipping/Collector/)**: The recommended approach for production. A standalone service that receives, processes, and exports data. It acts as a central hub, offloading telemetry processing from your applications.

* **[Grafana Agent / Alloy](/Monitor-your-data/OpenTelemetry/Shipping/Grafana-agent/)**: A lightweight telemetry collector compatible with OTel and Prometheus ecosystems.

### Why use the OpenTelemetry Collector?

The Collector is the 'Swiss Army Knife' of observability. It allows you to:

* **Aggregate** data from multiple services.
* **Scrub** sensitive data (PII) before it leaves your network.
* **Batch** data to reduce network overhead and improve performance.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.

!!! info "Learn more"
    [Official OpenTelemetry Documentation](https://opentelemetry.io/docs/)
