
### Incidents

A single page for declaration, coordination, and post-incident review.

- Declare an incident in seconds with a title, severity, affected services, and assigned roles
- Work through a triage, respond, and resolve lifecycle with timestamps at every stage
- SLA targets per severity show at a glance whether you are on track or slipping
- Add notes and @mention teammates on a live activity timeline, leaving a complete record of what happened
- Runbooks matching the affected services and severity surface automatically - convert steps to tasks in one click
- Write the post-mortem in Markdown from a template, then export to PDF, Markdown, or HTML
- Analytics shows MTTA, MTTM, time to post-mortem, and which services keep coming back as repeat offenders
- Severities, statuses, SLA targets, and roles are all configurable in **Administration > Preferences > Incidents**

### Services

Improvements to the Services overview, logs, and traces views.

- Interactive service graph with node tooltips showing throughput, latency, errors, inbound, and outbound connections
- Focus mode isolates a selected service and its direct connections
- Group peers by name similarity to reduce clutter in large environments
- Seven layout options including hierarchy, force-directed, circle, concentric, and radial tree
- 3D view and full-screen expand for complex environments
- Configure warning and critical thresholds for span throughput, latency, and error rate
- Logs tab: log rate chart with severity colour coding, per-severity badge filters, and keyword search
- Traces tab: P50 and P95 latency charts, span status, top throughput, and expanded trace view with waterfall timeline

### Jira integration
OpsPilot now integrates directly with Jira Cloud and Data Center, enabling you to:

- Create and track issues directly through OpsPilot.
- Search and comment on existing tickets.
- Manage tickets across your selected projects.



### Explore: Servers 
The new Servers tab in Explore provides enhanced server monitoring capabilities:

- Real-time metric tiles with traffic light status indicators.
- Key performance metrics including CPU, memory, and throughput.
- Detailed performance graphs for trend analysis.
- Advanced filtering by client ID and server groups.
- Customizable time ranges for precise monitoring.

### Explore: Metrics
A powerful new addition to the Explore suite that will revolutionize how you visualize and analyze your Prometheus-compatible metrics:

- Browse metrics without writing complex queries.
- Interactive metric previews with real-time graphs.
- Advanced filtering and labeling capabilities.
- Customizable time ranges and view options.
- Unified search across all metric names.



### OpsPilot 1.3.0

Introducing OpsPilot Hub: Your centralized knowledge repository for enhanced operational efficiency available in the OpsPilot 1.3.0 release. This new feature serves as the backbone for the OpsPilot AI Assistant, allowing you to store and manage critical operational information. With OpsPilot Hub, you can document your services, add custom metadata, and upload various types of knowledge through snippets and files. The intuitive interface includes progress tracking for service documentation, tagging for easy organization, and powerful filtering options. By centralizing your organization's information, OpsPilot Hub empowers the AI Assistant to provide more accurate, context-aware solutions to your team's operational challenges.


!!! info "Learn more"
    [OpsPilot Hub](/Data-insights/Features/OpsPilot/OpsPilot-Hub/Knowledge/)


### FusionReactor 12.1

#### Java 21 Support

- Full support for applications running on Java 21

- Ability to track transactions and requests on Java 21

- Seamless performance monitoring for applications upgraded to Java 21


#### Cloud UI WebSocket Tunnel

- Browse on-premises agent's UI directly through the FusionReactor Cloud website

- Seamless navigation between cloud and on-premises resources

- Reduced need for port connections or complex networking setups


#### Cloud Credentials for Agent Login

- Log into on-premise FusionReactor agents using FR Cloud credentials

- Centralized user management through the FR Cloud platform

- Enhanced security with cloud-based authentication

- Simplified login process for teams managing multiple agents


### Custom Detectors

FusionReactor Cloud has been upgraded with new Custom Detectors, enhancing its anomaly detection capabilities. This feature allows for more precise monitoring and diagnostics of your application's performance. While setting up Custom Detectors requires manual input and some knowledge of PromQL, they offer exceptional customization, letting you set specific conditions or thresholds that match your application's particular requirements. To help you begin, FusionReactor Cloud provides three pre-configured custom detectors specifically designed for Java and ColdFusion users. It's important to note that if you're not using Java or ColdFusion, these default detectors may not be directly applicable to your environment. However, regardless of your technology stack, you have the freedom to create your own custom detectors for monitoring CPU, memory, or any other crucial resources relevant to your specific application. This flexibility enables accurate identification of performance bottlenecks and potential issues across various technologies, helping maintain your application's efficiency and reliability.

### Enhanced On-Prem billing experience

We’ve listened to your feedback and are excited to announce that we’ve upgraded to a new billing platform powered by Stripe, designed with your convenience in mind. Enjoy a smoother, more flexible billing experience, addressing challenges with updating credit card details and adjusting product quantities. Managing subscriptions is now really easy in the new billing system, as you can add or remove seats directly within the product without needing to call sales or support. 

### Deep 

FusionReactor's new Deep integration provides AI powered root cause analysis to help solve issues quickly and instantly debug in production with no restart or redeploy required. With Deep, your team are able to concentrate on delivering innovative features rather than spending valuable time debugging.

## OpsPilot 1.2.0

With version 1.2.0, OpsPilot introduces exciting new features and improvements to enhance user experience, streamline workflows, and deliver even more powerful monitoring and management capabilities.


### New feature 

* **OpsPilot Vision**: OpsPilot introduces OpsPilot Vision, a groundbreaking feature that enriches its capabilities by allowing users to upload images for added context to their inquiries. With OpsPilot Vision, users can now provide supplementary visual information alongside their questions, enabling OpsPilot to deliver more comprehensive and tailored responses. This integration enhances the overall user experience, fostering greater clarity and effectiveness in communication. 


* **Updated FR knowledge base**: OpsPilot has undergone a significant upgrade in its FusionReactor knowledge base, resulting in enhanced proficiency in understanding and addressing issues. With this improvement, OpsPilot can now provide more informed and effective responses when dealing with FusionReactor-related tasks. This advancement promises smoother operations and quicker resolutions, ultimately optimizing system performance and minimizing downtime.


* **Continue On Error**: In the event that OpsPilot encounters an issue while responding, users now have the option to choose between retrying the operation or continuing the conversation seamlessly without interruption.



### Improvements

* **Alarm refinement** - In response to user feedback, OpsPilot has undergone optimization to refine its alarm notification system.  With this update, when OpsPilot notifies users of detected alarms during its task list processing, it will no longer repeat identical alarm notifications. This refinement ensures a more focused and efficient user experience by eliminating redundancy and providing clear, actionable notifications when necessary.


* **Time ranges** - OpsPilot now features automatic time range determination, simplifying the process of querying data within FusionReactor Cloud. OpsPilot will intelligently analyze the data and automatically determine the most relevant time range to address user queries. This enhancement saves time, eliminates guesswork, and ensures that users receive actionable insights based on the most pertinent data available.

* **Graph resolutions**: OpsPilot has enhanced the resolution of graphs displayed within the platform, ensuring clearer and more detailed visual representations of data



## FusionReactor 12

We're excited to announce several enhancements in the latest release of FusionReactor 12. First off, we've seamlessly integrated the [Observability Agent](/Monitor-your-data/Observability-agent/overview/) within FRAM, offering enhanced monitoring capabilities for better insights into your applications. Additionally, our system now automatically detects supported application servers within FRAM, streamlining setup and management processes. We've also invested in improving support for Lucee 6 and Tomcat 10 within FRAM, ensuring smoother experiences for users of these technologies. These updates reflect our commitment to empowering developers with robust tools and features to optimize their workflows.


!!! info "Learn more"
    [Release notes](//Latest-updates/release-notes//)
    
## Anomaly Detection (Beta)

For users familiar with FusionReactor Cloud (FR Cloud), the latest exciting update is the introduction of the Anomaly Detection component. This new feature enhances FR Cloud by enabling users to track the **probability of anomalies** in critical service metrics, known as RED (Request, Errors and Duration rates). It not only allows for closer monitoring of these key metrics but also provides notifications when they exceed set thresholds, offering a more proactive approach to service management.


## OpsPilot version 1.1.1 

**New features**

* Theme overhaul: OpsPilot now boasts a fresh, modern theme, providing an enhanced visual experience. The revamped theme contributes to a more cohesive and aesthetically pleasing monitoring interface.

* Alert integration: OpsPilot takes a significant step forward in its capabilities by now providing direct access to alerts firing within FusionReactor. This integration enables users to swiftly investigate and respond to alerts, streamlining the troubleshooting process for enhanced system reliability.

**Improvements**

* Graph enhancements: Enjoy a more flexible graphing experience with the ability to add or remove graph series from display using a simple ctrl+click command. This improvement gives users greater control over the visualization of their data, contributing to a more tailored and insightful monitoring experience.

* Graph accuracy: OpsPilot's graphs have undergone refinements to ensure a more accurate reflection of the data received. Users can now rely on the enhanced precision of graphs, facilitating a clearer understanding of the system's response as portrayed by OpsPilot.

**Bug fixes**

* Custom commands (HF): Resolving a bug that previously hindered the creation of custom commands, this update ensures a smoother experience for users looking to customize and optimize their monitoring workflows. With this bug fix, OpsPilot maintains its commitment to providing a robust and reliable monitoring solution.

Stay tuned for more updates and enhancements as OpsPilot continues to evolve, delivering an even more intuitive and powerful monitoring experience.




## FusionReactor 11
FusionReactor, the renowned application performance monitoring (APM) tool, has reached version 11.0.0. This release provides a significant improvement in security updates, reflecting the company's commitment to keeping your applications safe and secure. However, one notable change in this release is the discontinuation of Java 7 support, a decision made to address critical CVEs (Common Vulnerabilities and Exposures). We're also happy to announce integration with the upcoming Deep release as well as support for WebRequest tracking within servers using Jakarta servlet, which includes later versions of Tomcat and Wildfly amongst others.  

## OpsPilot Assistant

At FusionReactor, we're no stranger to the demands of on-call responsibilities because we've encountered those high-pressure situations ourselves. We're also passionate about discovering innovative solutions that enhance an engineer's daily routine, particularly in the realm of incident response management. That's why we're thrilled to unveil OpsPilot, an industry-first, fully launched, and production-ready assistant that serves as the cornerstone of FR Cloud. 

Our trusted assistant is the equivalent to having a team of experts on-call, 24/7. With OpsPilot Assistant the opportunities are endless. Conduct a series of automated system evaluations, promptly bringing potential issues in your entire environment to the surface.  Or simply pose a question, then let OpsPilot delve into the depths of your system, bringing forth insights that are not just data-driven but context-aware.  Armed with the vision provided by OpsPilot, you can swiftly pinpoint the core of any problem and streamline your resolution process for greater efficiency. OpsPilot transforms complex application landscapes into understandable conversations, empowering you with real-time insights at the speed of thought. 



## Enhanced dashboard navigation
We're thrilled to introduce some exciting enhancements to our dashboards providing you with even more powerful data insights! In our latest update,we've improved the user experience by allowing variables and time picker settings to seamlessly pass between dashboards. Our update allows you to move easily between dashboards ensuring you never lose context while exploring your data as all filters and time values are retained as you switch dashboards. To make navigation a breeze, we've improved the search facilities allowing you to effortlessly locate any dashboard you require. The newly incorporated  dropdown dashboard links make it easier than ever to access the information you need. These updates are designed to streamline your dashboard experience and empower you to make data-driven decisions effortlessly.


## Servers update

We're excited to unveil the latest enhancements to FusionReactor's servers view, designed with On-Prem parity to elevate your monitoring and troubleshooting experience. Our team has diligently worked to make the servers view clearer and more accessible than ever before. With a refreshed interface, intuitive navigation, and streamlined information presentation, gaining insights into your server's performance has never been easier. Whether you're a seasoned developer or just starting your journey, you'll appreciate the enhanced visibility into key metrics, real-time updates, and advanced analytics, all thoughtfully organized for effortless comprehension.



## FusionReactor 10.0.2 

**FusionReactor 10.0.2** revolutionizes how you monitor and view your data. Latest updates include cloud support for M1 Macs and new cloud transaction views or filters such as error history, longest transactions, slow transactions and more. Further improvements allow you to configure [Request Content Capture](/Data-insights/Features/Requests/Settings/#request-content-capture) to only capture responses as well as the ability to capture either headers or body only.   

!!! warning
    Cloud data now requires FusionReactor to be running on Java 8 or above. Live data will still work for Java 7.

!!! info "Learn more"
    [Release notes](/Latest-updates/release-notes/)

## Oracle Database Monitor

Introducing the latest advancement in monitoring capabilities - FusionReactor's cutting-edge integration with Oracle Database which uses metrics you can easily send to FusionReactor using the [Observability Agent](/Monitor-your-data/Observability-agent/overview/). Seamlessly embedded within the FusionReactor ecosystem, the Oracle Database Monitor offers comprehensive visibility into critical database metrics, query execution times, resource utilization, and more. Try FusionReactor's Oracle Database integration to collect key performance metrics on databases, tablespaces, and memory by default and experience firsthand the transformative potential of enhanced Oracle monitoring.



## Custom Dashboards

In the latest update of **FusionReactor**, we are excited to introduce our new feature - Custom Dashboards. This powerful tool allows users to create their own personalized dashboards, providing a tailored view of their application's performance metrics. Users can now monitor the metrics that matter most to them, all in one place. The custom dashboards are fully customizable, enabling users to add, remove, and rearrange metrics according to their needs. This feature aims to enhance user experience by providing a more streamlined and efficient way to monitor applications. 

## Redis Dashboard

View your metrics in minutes with **FusionReactor's** new out-the-box Redis Dashboard. Improve visibility into what’s happening in your environment by observing metrics from the Redis exporter. Our Redis Dashboard  uses metrics that can easily be sent to FusionReactor using the [Observability Agent](/Monitor-your-data/Observability-agent/overview/).  It enhances operational efficiency, facilitates troubleshooting, and helps ensure the optimal performance and stability of your Redis infrastructure. 



## Kafka & Elasticsearch integrations

FusionReactor now has Kafka and Elasticsearch integrations which use metrics that you can easily send to FusionReactor using the [Observability Agent](/Monitor-your-data/Observability-agent/overview/). By integrating Kafka with Elasticsearch, you can capture and analyze streaming data from Kafka topics in near real-time, enabling you to monitor the health, performance, and behavior of your Kafka infrastructure effectively. Additionally, Elasticsearch's powerful search and analytics capabilities allow you to visualize and explore the monitored data, gain insights, and detect anomalies or performance bottlenecks.



## OpsPilot AI

OpsPilot AI is an advanced observability
solution that leverages generative AI to provide
powerful insights into the performance of your
applications. By combining real-time data
collection, predictive analytics, and natural
language queries, OpsPilot AI enables you to
identify and resolve issues before they occur,
optimize the performance of your applications,
and reduce downtime.


## Kubernetes cluster monitoring

Kubernetes allows developers to deploy, manage, and scale containerized applications across a cluster of nodes, providing features such as load balancing, automatic scaling, self-healing, and rolling updates.

To make things easier for you, we have introduced Kubernetes monitoring in **FusionReactor Cloud**. With this tool, you can automate many of the manual tasks and focus on getting the most out of your Kubernetes monitoring.



## Observability Agent

The Observability Agent, an [open source](https://github.com/intergral/observability-agent/releases) autoconfiguration and installation tool, is a wrapper for the [Grafana Agent](https://github.com/grafana/agent) that can install the agent,
detect which services are running on your machine, and automatically create a configuration file with integrations for detected services.



## Usage based billing

As a complete observability solution, our usage-based billing plan meets your needs in a diverging technical space and we pride ourselves on offering essential observability at sensible prices. 

## Distributed tracing

We are excited to announce the addition of a new distributed tracing within FusionReactor.  Distributed tracing is a method used in observability to track the flow of requests as they move through a distributed system. It allows you to see a detailed view of the entire request flow, from the time the request was initiated to the time it was completed.  

FusionReactor captures and displays this trace information in a graphical format, so you can visualize the entire request flow and quickly identify any issues or bottlenecks. 



## Log management

Since the release of FusionReactor 9, we are able to ingest and index any log file using [Loki](https://grafana.com/oss/loki/).


FusionReactor uses this powerful capability to make it easy to analyze and track system events. We can also automatically link logs to other events such as distributed traces or errors, providing a complete picture of system activity. This makes investigating problems and identifying issues much faster and more efficient which improves overall performance and reliability.



## Span metrics 

FusionReactor has several new **Span Metrics** dashboards which provide detailed insight into specific parts of a distributed trace through the use of spans. Spans are essentially small pieces of time that represent a specific operation or action within a larger process or transaction. 

Measuring span duration and status codes  allows developers to quickly identify bottlenecks and problem areas in their application's distributed architecture. 
 
With the ability to view 90th and 99th percentile span duration, developers can easily determine areas that need improvement and take action to optimize performance. This new capability is a powerful tool for improving application performance and providing better visibility into distributed architectures.

