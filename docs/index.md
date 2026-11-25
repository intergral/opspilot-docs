# Getting started with OpsPilot

OpsPilot is an AI-powered observability and SRE platform. Sign up and it asks three quick questions about what you run, sets up the matching integrations for you, and shows exactly what's left to connect - so you're reading live telemetry in minutes instead of wiring up collectors by hand. The questions take under a minute, and you can change your answers any time.

!!! info "Already have an account?"
    [Sign in](https://app.opspilot.com/auth/login) and head to your dashboard to start exploring your data. If you have an invitation, follow the link in your invitation email to access your organization.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://www.youtube.com/embed/HdiADeq6wlo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="OpsPilot onboarding walkthrough" allowfullscreen></iframe></div>

---

## Step 1 - Tell us your stack

On the welcome screen, choose **Get started**. Tick everything you use on each screen, or skip any question that doesn't apply:

- **Where does your team talk?** Your chat tools.
- **Which databases and data stores do you run?** For example Kafka, MySQL, or Redis.
- **Which languages and runtimes do you use?** For example .NET, Go, Java, Node.js, or Python.

Choose **Finish** on the last question. If you're not ready, choose **Do this later** on the welcome screen.

<!-- SCREENSHOT NEEDED: the languages and runtimes question -> images/onboarding-languages.png -->

---

## Step 2 - Open your Overview

OpsPilot sets up an integration for everything you picked. Choose **Go to Overview**. The [Integrations](/Data-insights/Features/integrations/) panel lists each one with its status:

| Status | Meaning | What to do |
|---|---|---|
| **Not sending data** | Set up, but OpsPilot isn't receiving data from it yet | Choose **Check the install notes** |
| **Not installed** | Not installed yet | Choose **Install** |
| **Healthy** | Connected and sending data | Nothing - you're done |

<!-- SCREENSHOT NEEDED: the Integrations panel -> images/onboarding-integrations.png -->

---

## Step 3 - Connect your integrations

Choose **Check the install notes** next to an integration. Its page opens on the **Installation guide** tab. Follow the steps for your service, then deploy or restart it. Once data arrives, the integration turns green and shows **Healthy**.

Repeat this for each integration in the panel.

<!-- SCREENSHOT NEEDED: an installation guide -> images/onboarding-install-guide.png -->

---

## Step 4 - Set up Coworker

Once data is flowing, set up [Coworker](/Data-insights/Features/OpsPilot/Coworker/getting-started/), the AI SRE built into OpsPilot, to watch the services you care about. Choose **Set up** on the **Coworker** card on your Overview.

---

!!! question "Need help?"
    [Book a demo](https://opspilot.com/book-a-demo/) and we'll walk you through it, or contact support in the chat bubble.
