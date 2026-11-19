# Audit history

The **Audit history** page shows what OpsPilot audited, suggested, and is still checking in the catalog this billing period - and what it cost. Open it from the [Catalog Overview](catalog-overview.md): the **Recent audit activity** panel's **Full history** link, or the **Audit history** link under **Catalog quality**.

## This period

A summary across the current billing period (with its date range) reports:

- **Services audited** and the **tokens** they used.
- How many entries were **updated** and the tokens that cost - flagged **not counted against the budget** where OpsPilot covers it (your included initial creation).
- **Fields OpsPilot wrote** - a bar splitting the auto-written fields into **confirmed** and **still proposed**.
- Any **aliases no longer seen in telemetry**, so you can spot entries to prune or refresh.

!!! info "What audits cost"
    Your first catalog creation is covered by OpsPilot and does not use your allowance. Audits you trigger afterwards use your [AI Token allowance](../../Data-insights/Features/OpsPilot/Coworker/usage.md#ai-token-allowance). See [Adding a catalog entry](entries.md#adding-a-catalog-entry) for running one.

## Tabs

| Tab | Shows |
|---|---|
| **Activity** | The audits run this period, newest first - what each one updated, when, and its **OpsPilot AI Token** cost |
| **Proposals** | Field changes OpsPilot suggests but has not applied, grouped by entry (a running total, such as *13 on 9 entries*). Each names the field - **Operations**, **Dependencies**, **Identity**, or **Language** - and what to confirm, alongside the entry's tier badge |
| **Being watched** | Dependencies and operations OpsPilot thinks may have gone - **maybe removed** or **maybe shifted**. Each row carries the signal (for example *0 traffic observed over current window*), a seen count, and the date it was last seen |

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
