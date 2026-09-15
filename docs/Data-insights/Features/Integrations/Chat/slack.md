# Slack Integration

Connect OpsPilot to Slack to receive alert notifications and incident updates directly in your Slack channels. You can also talk to OpsPilot from Slack - mention it in a channel, or DM it directly.

Navigate to **Integrations** from the left-hand sidebar, then select **Slack**.

---

## Setup

1. In OpsPilot, go to **Integrations** and click **Slack**.
2. Click **Add to Slack**. A Slack window opens asking you to sign in to your workspace.
3. Enter your workspace's Slack URL (for example, `your-workspace.slack.com`) and click **Continue**. If you don't know it, use **Find your workspaces**.
4. Sign in to the workspace. The method depends on how your workspace is configured - many require a Google account or another single sign-on provider on your organisation's domain.
5. On the **Allow the "OpsPilot" app to access Slack** screen, choose the **Workspace** to install into, review the permissions OpsPilot is asking for, and click **Allow**.
6. Select the default channel you want notifications sent to.
7. Click **Save**.

!!! note "Permissions OpsPilot requests"
    Slack asks you to approve what OpsPilot can do in your workspace:

    | | Permission |
    |---|---|
    | **View** | Content and info about channels and conversations |
    | **View** | Content and info about your workspace |
    | **Act** | Perform actions in channels and conversations |

    Expand **More permissions** to see the full list, or click **Manage permissions** to change them. Slack shares the permissions you grant with OpsPilot.

---

## Using Slack with Alerts

Once connected, you can select Slack as a contact point when configuring alert notification policies.

Navigate to **Alerts > Contact Points** and choose Slack as the delivery method. You can specify a channel per contact point to route different alerts to different channels.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
