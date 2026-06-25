# OpsPilot Releases

### 25th June, 2026

| Issue Type | Summary |
|---|---|
| New Feature | **Service Catalog** - A persistent record of your services and dependencies with ownership, tiers, runbook attachments, and incident linking |
| New Feature | **Incidents** - Full incident lifecycle management: declaration, triage, coordination, timelines, runbooks, tasks, post-mortems, and analytics |
| New Feature | **Tasks** - A shared board for tracking incident follow-ups and work items across Open, In progress, and Done |
| New Feature | **Notifications** - Alerts for role assignments, @mentions, status and severity changes, SLA breaches, and watched service activity |
| New Feature | **Services graph** - Interactive node tooltips with focus mode, group peers by name similarity, multiple layout options, 3D view, and full-screen expand |
| New Feature | **Services logs** - Log rate chart with severity colour coding, per-severity badge filters, and keyword search |
| New Feature | **Services traces** - Performance charts (P50, P95, span status, throughput), filterable trace list, and expanded trace view with waterfall timeline |
| Improvement | **Thresholds** - Configure warning and critical thresholds for span throughput, latency, and error rate directly from the Services overview |

### OpsPilot  13th January 2025



| Issue Type   | Summary                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------|
| New Feature  | New Metrics AI Agent                        |
|              | We have developed a new AI agent tuned for dealing with metric data. OpsPilot will utilize this new agent to:                                                         |
|              |   - Use a wider selection of metrics for analysis.                                             |
|              |   - Improve response accuracy when dealing with metrics.                                       |
|              |   - Improve response speed when dealing with metrics.                                          |
|              |   - Show graphs more frequently in responses.                                                  |
|              |   - Generate graphs that more accurately reflect the conversation.                    |

### 9th January 2025

| Issue Type   | Summary                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------|
| New feature | Website Knowledge Sources: Scrape websites to ingest their content into your knowledge base. |


### OpsPilot 1.2.3 - 25th July, 2024

| Issue Type | Summary                                                   |
|------------|-----------------------------------------------------------|
| Notes      | No changes, switch to ARM deployments                     |

### OpsPilot 1.2.2 - 12th June, 2024

| Issue Type   | Summary                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------|
| Improvement  | Reduced answer brevity for non-observability questions                                         |
| Improvement  | Reduced references to OpsPilot or FusionReactor in responses                                   |
| Bug Fix      | Stopped OpsPilot from assuming images are from FusionReactor                                   |
| Bug Fix      | Ensured FusionReactor OpsPilot buttons are correctly handled                                   |

### OpsPilot 1.2.1 - 21st May, 2024

| Issue Type  | Summary                                                                                          |
|-------------|--------------------------------------------------------------------------------------------------|
| Improvement | Improved response speed                                                                          |
| Improvement | Enhanced response conciseness to highlight key points                                            |
| Improvement | Updated templates to reflect new OpsPilot functionality                                          |

### OpsPilot 1.2.0 - 16th April, 2024

| Issue Type   | Summary                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------|
| New Feature  | OpsPilot Vision - Upload images for analysis and context                                            |
| New Feature  | Improved FR Knowledge - Enhanced information about FusionReactor                                    |
| New Feature  | Continue On Error - Option to retry or continue after an issue                                      |
| Improvement  | Messages - Reduced repetitive prompts for investigating alerts or issues                            |
| Improvement  | Time Ranges - Automatic determination of optimal time ranges for data analysis                      |
| Improvement  | Graph Resolutions - Enhanced resolution of displayed graphs                                         |

### OpsPilot 1.1.3 - 20th February, 2024

| Issue Type  | Summary                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------|
| Improvement | Active chat removal - Intelligent FusionReactor integration                                         |
| Improvement | Graphs + Queries - Better generation and display of graphs and queries                              |
| Bug Fix     | Correct handling of 24-hour time requests                                                           |

### OpsPilot 1.1.2 - 14th February, 2024

| Issue Type  | Summary                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------|
| Improvement | Increased response accuracy in OpsPilot                                                            |
| Improvement | Enhanced handling of slow performance and error transaction discussions                             |
| Improvement | Prevented repetitive suggestions on the same investigation topics                                   |
| Improvement | Improved generation and display of graphs and queries                                              |

### OpsPilot 1.1.1 - 26th January, 2024

| Issue Type   | Summary                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------|
| New Feature  | New Grafana-matching theme for OpsPilot                                                          |
| New Feature  | Alerts - Access and investigate alerts firing in FusionReactor                                    |
| Improvement  | Graphs - Ability to add/remove series from graphs using ctrl+click                                |
| Improvement  | Enhanced graph accuracy in OpsPilot responses                                                     |
| Improvement  | Improved response accuracy, speed, and formatting                                                 |
| Improvement  | Optimized queries for fetching metrics                                                            |
| Bug Fix      | Fixed bug preventing custom command creation                                                      |

### OpsPilot 1.1.0 - 7th December, 2023

| Issue Type   | Summary                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------|
| New Feature  | Added graph messages to help visualize data                                                      |
| New Feature  | Generates and runs promQL queries to help answer questions                                       |
| New Feature  | Added commands to make repeating prompts easier                                                  |
| New Feature  | Added ability to change preferences with NLP                                                     |
| New Feature  | Added answer detail preference for customizable response detail                                  |
| New Feature  | Added user role preference for tailored information                                              |
| New Feature  | Added ability to create custom commands with NLP                                                 |
| New Feature  | Added auto-complete for services, applications, and commands                                     |
| New Feature  | Added metrics knowledge base for informed graph and query generation                             |
| Improvement  | Provided additional status updates for more user information during request processing           |
