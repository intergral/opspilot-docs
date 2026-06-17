# Runbooks

Runbooks are step-by-step response playbooks you build once and reuse across incidents. Attach a runbook to specific services and severities and it surfaces automatically on any matching incident, ready to guide your team through the response.

## Creating a runbook

Navigate to **Incidents > Runbooks** and click **+ New runbook**.

| Field | Description |
|---|---|
| **Title** | A descriptive name for the runbook (e.g. Checkout 5xx spike) |
| **Steps** | One or more titled steps, each with a description of what to do. Drag steps to reorder them. |
| **Services** | The catalog services this runbook applies to (optional) |
| **Severities** | The severity levels this runbook applies to (optional) |
| **Tags** | Additional tags to control when the runbook surfaces (optional) |

Click **Create** to save the runbook.

When an incident is declared, any runbooks whose services, severities, and tags match the incident automatically appear in the incident's sidebar. The more specific the attachment, the more targeted the suggestions.

## Using a runbook during an incident

Runbooks that match an incident's services and severity appear automatically in the incident sidebar. Expand a runbook to view its steps, or click to convert all steps into tasks on the incident in one click - each step becomes a task assigned to the incident, ready to be worked through and tracked.

## Managing runbooks

All runbooks are listed on the **Incidents > Runbooks** page. From here you can edit or delete any runbook at any time. Changes take effect immediately on any future incidents that match.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
