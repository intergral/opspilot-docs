OpsPilot integrates with Deep, a dynamic instrumentation tool that enhances observability by collecting application data in real-time — without redeployment. Deep dynamically instruments applications to ensure seamless runtime observability, gathering the data you need precisely when you need it.

At the heart of Deep lies its powerful query language, DeepQL. A monitoring-centric query and command language, that draws inspiration from PromQL, streamlines the real-time addition and manipulation of logs, metrics, traces, and live data snapshots. This empowers users with more effective debugging, heightened system visibility, and improved performance monitoring capabilities.

!!! info "Learn more"
    [Deep documentation](https://intergral.github.io/deep/)



## Benefits

* **Dynamic monitoring**: Deep enables dynamic monitoring of applications, allowing users to gather data precisely when it's needed. This flexibility ensures that critical metrics and insights are available in real-time, facilitating proactive decision-making and issue resolution.

* **Scalability**: Deep is designed to scale effortlessly, accommodating growing data volumes and increasing monitoring requirements without compromising performance. This scalability ensures that the system remains responsive and effective, even as workloads expand.

* **Enhanced observability**: Deep introduces a powerful query language, DeepQL, which simplifies the real-time manipulation of logs, metrics, traces, and live data snapshots. This facilitates comprehensive observability, empowering users to gain insights into system behavior, diagnose issues, and optimize performance effectively.

* **Effective debugging**: By facilitating real-time addition of data, Deep streamlines the debugging process, allowing users to identify and address issues promptly. This reduces downtime, improves system reliability, and enhances overall user experience.

## Deep in FusionReactor

To use **Deep** in OpsPilot, navigate to the **Explore** page and select the Deep datasource.

![!Screenshot](/Monitor-your-data/Deep/images/deep1.png)

### Deep features

#### Search

Use the search function to find triggered snapshots. 

!!! info "Learn more"
    [Search](/Data-insights/Features/Deep/Search/)

#### Tracepoints

The **Tracepoints** section allows you to list existing tracepoints, create new ones by specifying a file and line number, and delete tracepoints using their unique ID.

!!! info "Learn more"
    [Tracepoint](/Data-insights/Features/Deep/Create-Tracepoint/)

