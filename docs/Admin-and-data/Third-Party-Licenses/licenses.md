---
search:
  exclude: true
---


# Licenses

## FusionReactor use of Grafana

Parts of **FusionReactor Cloud** use [Grafana](https://grafana.com/) and other open source software.

### Copyright notice for Grafana

!!! info "Learn more"
    [Grafana project](https://github.com/grafana/grafana)

### Warranty notice for Grafana

There is no warranty for the work (except to the extent that warranties are provided)

### Legal notices and licenses for Grafana

Grafana is distributed under [AGPL-3.0-only](https://github.com/grafana/grafana/blob/main/LICENSE). 

!!! example "Apache-2.0 exceptions"
    [LICENSING](https://github.com/grafana/grafana/blob/HEAD/LICENSING.md)

Licensees may convey the work under these licenses

### Modifications to Grafana

- Removed the footer on the general dashboards page.
- Allow the option to have a configurable application name.
- Allow definition of which kiosk mode is used within Grafana configuration files.
- Added dashboard links to kiosk mode.
- Disabled the button to alter kiosk mode view.
- Removed random walk and list of public files from the default Grafana datasource.

### Source code

[Original Grafana source code](https://github.com/grafana/grafana)

[Modified Grafana source code](https://github.com/intergral/grafana)

---

## Third-party licenses

| Description                      | License type                                                                                               |
|----------------------------------|------------------------------------------------------------------------------------------------------------|
| Grafana	                         | [AGPL-3.0-only](/tpl/AGPL-3_LICENSE/) with some [APACHE LICENSE 2.0](/tpl/APACHE_LICENSE-2.0/) exceptions  |
| Angular	                         | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| Bugsnag	                         | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| @circlon/angular-tree-component	 | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| Fontsource	                      | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| @katoid/angular-grid-layout	     | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| @swimlane/ngx-graph	             | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| angular-split	                   | [APACHE LICENSE 2.0](/tpl/APACHE_LICENSE-2.0/)                                                             |
| bson-objectid	                   | [APACHE LICENSE 2.0](/tpl/APACHE_LICENSE-2.0/)                                                             |
| codemirror	                      | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| d3	                              | [ISC](/tpl/ISC_LICENSE/)                                                                                   |
| lodash	                          | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| moment	                          | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| monaco-editor	                   | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| monaco-promql	                   | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| ngx-color-picker	                | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| ngx-cookie	                      | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| ngx-moment	                      | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| ngx-monaco-editor	               | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| ngx-virtual-scroller	            | [MIT LICENSE](/tpl/MIT-LICENSE/)                                                                           |
| rxjs	                            | [APACHE LICENSE 2.0](/tpl/APACHE_LICENSE-2.0/)                                                             |
|   Google Material Design Icons                         | [APACHE LICENSE 2.0](/tpl/APACHE_LICENSE-2.0/)                                                             |
| yaml	                            | [ISC](/tpl/ISC_LICENSE/)                                                                                   |

---

## FusionReactor Agent licenses

Full third-party license agreements and additional notices for the FusionReactor agent are available on a separate page.

[View third-party license agreements & additional notices](/Admin-and-data/Third-Party-Licenses/Third_Party_License_Agreements/)

---

## EULA

The End User License Agreement (EULA) governs your use of Intergral software products.

[Read the EULA](https://fusion-reactor.com/eula-intergral-software-end-user-license-agreement/)

---

## Legal Notices
This document lists third-party open-source dependencies used in this project that carry license terms with explicit attribution or notice requirements.
All other dependencies use the MIT license, which has equivalent notice requirements but is considered permissive enough that legal teams do not typically require explicit listing for SaaS web applications.

No GPL, LGPL, or AGPL licensed packages are used. There are no source-disclosure obligations.

### Apache License 2.0

The following production dependencies are licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Apache 2.0 requires that a copy of the license and any existing NOTICE files accompany distributions. None of the packages below include a NOTICE file with additional third-party attributions.

| Package | Version | Copyright Holder |
|---|---|---|
| `@aws-sdk/credential-providers` | 3.1034.0 | AWS SDK for JavaScript Team |
| `@grafana/faro-web-sdk` | 2.2.4 | Grafana Labs |
| `@grafana/faro-web-tracing` | 2.2.4 | Grafana Labs |
| `@opentelemetry/api` | 1.9.0 | OpenTelemetry Authors |
| `@opentelemetry/api-logs` | 0.212.0 | OpenTelemetry Authors |
| `@opentelemetry/instrumentation` | 0.212.0 | OpenTelemetry Authors |
| `@opentelemetry/resources` | 2.5.1 | OpenTelemetry Authors |
| `@opentelemetry/sdk-logs` | 0.212.0 | OpenTelemetry Authors |
| `@opentelemetry/sdk-metrics` | 2.5.1 | OpenTelemetry Authors |
| `@opentelemetry/sdk-trace-base` | 2.5.1 | OpenTelemetry Authors |
| `class-variance-authority` | 0.7.1 | Joe Bell |
| `fuse.js` | 7.3.0 | Kiro Risk |
| `launchdarkly-js-client-sdk` | 3.9.0 | Catamorphic, Co. |
| `launchdarkly-node-server-sdk` | 7.0.4 | Catamorphic, Co. |
| `mongodb` | 7.2.0 | The MongoDB NodeJS Team |

### BSD 3-Clause License

The following production dependency is licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

BSD 3-Clause requires that the copyright notice and disclaimer be reproduced in documentation or other materials provided with binary distributions.

| Package | Version | Copyright Holder |
|---|---|---|
| `rrule` | 2.8.1 | Jakub Roztocil, Lars Schoning, and David Golightly |

### ISC License

The following production dependencies are licensed under the [ISC License](https://opensource.org/licenses/ISC), which is functionally equivalent to MIT.

| Package | Version | Copyright Holder |
|---|---|---|
| `d3-force` | 3.0.0 | Mike Bostock |
| `d3-quadtree` | 3.0.1 | Mike Bostock |
| `lucide-react` | 0.576.0 | Cole Bemis (Feather icons, MIT); Lucide Contributors (all other icons) |

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
