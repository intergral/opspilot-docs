# FAQ

## Incidents

**What is the difference between severity and status?**
Severity describes the impact level of an incident (SEV-1 through SEV-4). Status describes where it sits in the response lifecycle (Triage, Investigating, Mitigated, Resolved). Both are independent - a SEV-1 incident can be in Triage, and a SEV-4 can be Resolved.

**Can I customise severities and statuses?**
Yes. Both are fully configurable in **Administration > Preferences > Incidents**. You can rename, reorder, add, and delete severities and statuses, and assign colours and slugs. Investigator and Commander are the only built-in roles that cannot be removed.

**How do I run a practice drill?**
Add a custom severity called Drill (or similar) in **Administration > Preferences > Incidents > Severities**. Use this severity when declaring a test incident so it is clearly identifiable to everyone on the team.

**What is the post-mortem gate?**
The post-mortem gate blocks an incident from reaching a terminal (closed) status until its post-mortem has been published. It is on by default but can be toggled per severity in **Administration > Preferences > Incidents**.

**What is the difference between tags and services on an incident?**
Services link the incident to specific entries in your service catalog, enabling runbook matching and catalog analytics. Tags are free-text labels for categorisation and filtering - they do not link to catalog entries.

**How do I set SLA targets?**
Navigate to **Administration > Preferences > Incidents**, open a severity, and toggle on **SLA budget**. You can then set time targets for acknowledging, mitigating, and publishing a post-mortem for incidents at that severity.

**What are MTTA and MTTM?**
MTTA is Mean Time to Acknowledge - the average time from an incident being declared to it first reaching an acknowledged status. MTTM is Mean Time to Mitigate - the average time from declaration to first reaching a mitigated status. Both are driven by the `ack` and `mitigated` flags on your configured statuses.

**Can I link related incidents together?**
Yes. Open an incident, go to the **Scope** tab, search for the related incident, and click **Link**. You can specify the relationship type (for example, Related or Duplicate).

---

## Runbooks

**How do runbooks surface on an incident?**
Runbooks are attached to services, severities, and tags when you create them. When an incident is declared, any runbooks whose attachment criteria match the incident's services and severity automatically appear in the incident sidebar.

**Can I convert a runbook into tasks?**
Yes. Open a runbook from the incident sidebar and convert its steps into incident tasks in one click. Each step becomes a task assigned to the incident and visible on the Tasks board.

---

## Post-mortem templates

**How do I use a template on an incident?**
Once an incident is ready for a post-mortem, open the **Post-mortem** tab on the incident detail page and click **Choose a starting point**. Your saved templates appear as options alongside a blank page.

**What formats can I export a post-mortem to?**
Post-mortems can be exported as PDF, Markdown, or HTML.

---

## Tasks

**What is the difference between Incident tasks and General tasks?**
Incident tasks are linked to a specific incident - they appear both on the incident detail page and on the Tasks board. General tasks are standalone and not tied to any incident. Both types appear on the Tasks board.

**Where do I assign a task?**
Tasks can be assigned when creating them from an incident sidebar, or after creation from the Tasks board. When a task is assigned to someone, they receive a notification.

---

## Notifications

**Which notifications can I turn off?**
Most notifications can be toggled off in **Administration > Preferences > Notifications**. The only notifications that cannot be silenced are escalations and SLA breaches.

**How do I get notified about a specific service?**
Add the service to your watched services list in **Administration > Preferences > Services**. You will then be notified any time that service is directly affected by an incident or falls within its blast radius.

**Where do I find my notifications?**
Click the bell icon in the top navigation bar. From the notifications panel, click the gear icon to go directly to your notification preferences.

---

## Service Catalog

**Why use a catalog if I already have a Services overview?**
The Services overview only shows services that are currently sending telemetry. The catalog tracks services whether they are active or quiet, giving you a complete and persistent record of your system regardless of its current state.

**What is a slug and why does it matter?**
A slug is a unique identifier for a catalog entry, using lowercase letters, numbers, and hyphens only. It is used by alert labels, runbook attachments, and incident service links to connect to the correct catalog entry. Choose something stable - changing a slug can break existing connections.

**What is the difference between Active and Deprecated?**
Active entries are services currently in use. Deprecated entries are retired services that are kept in the catalog for historical reference. Deprecated entries do not appear in the default catalog view but can be shown by switching the status filter to All entries or Deprecated only.

**Can I add catalog entries from outside Administration?**
Yes. In the Services overview, any service appearing in your telemetry that is not yet catalogued shows a **Create** button in the Catalog column of the Service Table. Click it to register the service without leaving the Services page.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
