# Getting started with Coworker

## Onboarding

When you first access Coworker, a short guided setup walks you through personalising your experience. You can skip it at any time and still get a working Coworker, though you'll see a broader, less tailored view until you configure your preferences.

The first screen introduces what Coworker does and how it works:

| Stage | What happens |
|---|---|
| **Something fires** | An alert arrives from your observability stack, or a background check finds something worth raising |
| **I investigate** | Coworker works through your metrics, logs, traces, and recent deploys to find what changed |
| **You get a clear story** | One situation thread: what's happening, what's affected, what changed |
| **I keep checking back** | Coworker re-checks on a cadence, flagging changes and resolving when things clear |

Click **Quick start** to begin setup, or **Skip** to go straight to the dashboard.

!!! note "New organisations"
    If your organisation is brand new to Coworker, the onboarding includes two additional steps: connecting your alerts (**Watch all** or **Let me pick** specific rules) and selecting a set of pre-built starter scheduled tasks. These are the fastest way to start seeing value and can be configured at any time from the [Tasks](tasks.md) panel.

---

### Step 1: Your role

Coworker asks which role best describes you. This sets the defaults for which kinds of situations are surfaced to you first:

| Role | Description |
|---|---|
| **Developer** | Building features, owning services |
| **SRE / DevOps** | On-call, infra, reliability |
| **Tech lead** | Leading a team, mostly hands-on |
| **Manager / leadership** | Team or org-level visibility |
| **Something else…** | Describe your role in your own words |

Pick the closest fit. You can refine this at any time. Select **Skip - I'll come back later** to proceed without setting a role.

---

### Step 2: What you want from Coworker

Coworker asks what you want it to help you with. Select as many as apply:

| Option | Description |
|---|---|
| **Surface critical issues** | Stay quiet most of the time; get loud when something's actually breaking |
| **Filter alert noise** | Only surface the alerts that matter from a high-volume feed |
| **Catch cascading issues** | Spot when several small problems are really one big one across services |
| **Run regular checks** | Watch specific services or metrics on a cadence and flag what looks off |
| **Give me regular reports for the team** | Uptime, SLO burn, incident counts, deploy frequency |
| **Verify deploys** | After each deploy, check things look healthy and flag any regressions |
| **Brief me on my shift** | Tell me what happened while I was away, what's still open, what's resolved |
| **Take action on routine stuff** | Automate scripts, jobs, and endpoint checks to reduce context-switching |

Click **Continue** when done, or **Skip** to proceed without selecting any.

---

### Step 3: Your focus areas

Coworker asks which broad domains are yours to care about:

| Area | What it covers |
|---|---|
| **Infrastructure & Platform** | Hosts, containers, Kubernetes, platform health |
| **Cost & Efficiency** | Spend anomalies, quota limits, overprovisioning |
| **Security** | Auth failures, suspicious traffic, IAM, secrets |
| **Observability** | Coverage gaps, telemetry quality, alert rules |
| **Database & Storage** | Queries, connections, replication, cache health |
| **Users & Availability** | Uptime, error rates, latency for end users |

Select as many as apply. These can be updated at any time from Settings.

---

### Step 4: Which services are yours

The final onboarding step. Coworker asks which services you own so it can better filter what reaches your feed.

> *"The more I know what you own, the better I can filter the noise. I'll ask a few questions."*

Click **Sure** to let Coworker ask follow-up questions about your services, or **Skip** to continue with a broader view. This can be configured in detail at any time. See [Configuring your view](#configuring-your-view) below.

---

## Configuring your view

Whether set during onboarding or later from Settings, three controls decide what appears in your Coworker feed:

| Setting | Description |
|---|---|
| **Focus services** | The specific services you own or care about, by name or pattern (e.g. `payments-*`). Situations touching these are treated as your patch and surfaced to you. |
| **Focus areas** | The broad domains you want to see (Infrastructure & Platform, Cost & Efficiency, Security, Observability, Database & Storage, Users & Availability). |
| **Custom keywords** | A free-form list for anything the focus areas don't capture, such as a library, technology, or feature name specific to your stack. |

None of these change what Coworker investigates or raises across your organisation. They only change what reaches your personal feed. You can always switch to the **Team** view to see everything unfiltered.

---

## Settings

Open **Settings** from the Coworker dashboard to access configuration options. The panel is split into two sections:

**You**

| Option | Description |
|---|---|
| **Your preferences** | Adjust your focus services, focus areas, custom keywords, and personal monitoring preferences |
| **Reset onboarding** | Restart the guided onboarding flow from the beginning |

**Your organisation**

| Option | Description |
|---|---|
| **Coworker activity** | View a log of Coworker's background activity across your organisation |
| **Coworker behaviour** | Adjust how Coworker operates: checkup cadence (Aggressive to Minimal), report detail level (Concise, Standard, Detailed), and digest frequency (every 6, 12, or 24 hours) |
| **Allowance & cost** | Set your monthly task allowance, warning threshold and halt threshold. See [Usage](usage.md#allowance) for full details |

You don't need to configure all of this up front, as sensible defaults are in place. You can also ask Coworker directly in any chat to update your preferences; it can read and change your settings conversationally.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
