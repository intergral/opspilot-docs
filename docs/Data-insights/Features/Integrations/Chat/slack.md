# Slack Integration

Talk to OpsPilot from Slack - mention it in a channel or DM it directly.

The Slack integration brings OpsPilot to where your team already talks. Invite the bot to a channel and switch posting on, and the alerts, situations, and digests the coworker surfaces land there as they happen. Mention it there or message it directly and you get the same coworker you use in the app, so you can ask about what it just posted without switching tools.

DMs are personal: each person links their own account.

Navigate to **Integrations** from the left-hand sidebar, then select **Slack**.

---

## Permission tiers

| Tier | Description |
|---|---|
| **Read-only** | The default. Requires nothing to supply - it is granted with your plan. OpsPilot answers questions in Slack from what the organisation can already see |
| **Read + Act** | Requires Read, plus a plan that includes assistant actions. Lets Slack users act on the organisation's behalf - acknowledging alerts, silencing, and triggering runbooks - subject to their own account link |

---

## Connecting your workspace

1. In OpsPilot, go to **Integrations** and click **Slack**.
2. Click **Add to Slack**. A Slack window opens asking you to sign in to your workspace.
3. Enter your workspace's Slack URL (for example, `your-workspace.slack.com`) and click **Continue**. If you don't know it, use **Find your workspaces**.
4. Sign in to the workspace. The method depends on how your workspace is configured - many require a Google account or another single sign-on provider on your organisation's domain.
5. On the **Allow the "OpsPilot" app to access Slack** screen, choose the **Workspace** to install into, review the permissions OpsPilot is asking for, and click **Allow**.

!!! note "Permissions OpsPilot requests"
    Slack asks you to approve what OpsPilot can do in your workspace:

    | | Permission |
    |---|---|
    | **View** | Content and info about channels and conversations |
    | **View** | Content and info about your workspace |
    | **Act** | Perform actions in channels and conversations |

    Expand **More permissions** to see the full list, or click **Manage permissions** to change them. Slack shares the permissions you grant with OpsPilot.

---

## Inviting OpsPilot to a channel

Connecting the workspace posts nothing anywhere. OpsPilot waits to be invited, so you choose which channels it appears in.

In the channel you want situations in, run:

```
/invite @OpsPilot
```

OpsPilot introduces itself and waits. Situation posting is off until someone turns it on - tap **Enable situation posting** on the welcome card, or run:

```
/opspilot unmute
```

Situations at **warning** severity or above then land in that channel.

---

## Connecting your own account

Direct messages are personal, so each person links their OpsPilot account once before DMing the bot. Message it and it hands you the link.

Channel mentions need no linking - only DMs.

---

## What OpsPilot reads

OpsPilot only reads messages that mention it. Background reading is off in every channel until someone turns it on:

```
/opspilot listen passive
```

`/opspilot status` shows where a channel stands, and `/opspilot listen off` stops it again.

---

## Checking it works

In a channel OpsPilot is in, ask *"what situations are active right now?"*. An answer means the workspace is connected and the bot can reach your data.

---

## Slash commands

| Command | Description |
|---|---|
| `/invite @OpsPilot` | Add OpsPilot to the channel |
| `/opspilot unmute` | Turn situation posting on for the channel |
| `/opspilot mute` | Stop the posts again, without removing the bot |
| `/opspilot route` | Narrow what is posted by service, severity, or category |
| `/opspilot listen passive` | Turn on background reading of the channel |
| `/opspilot listen off` | Turn background reading off again |
| `/opspilot status` | Show where the channel stands |

---

## Using Slack with alerts

You can also select Slack as a contact point when configuring alert notification policies.

Navigate to **Alerting > Notifications**, open the **Contact Points** tab, and choose Slack as the integration type. See [Contact Points](../../New-alerting/contact-points.md) for the full setup.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
