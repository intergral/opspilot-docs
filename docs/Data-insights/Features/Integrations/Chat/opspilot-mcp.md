# OpsPilot MCP

Let AI assistants query OpsPilot over the Model Context Protocol (MCP).

OpsPilot MCP brings OpsPilot to where your team already works. An AI assistant there can work with your telemetry and situations the way the OpsPilot coworker does, so you can ask without switching tools.

Navigate to **Integrations** from the left-hand sidebar, then select **OpsPilot MCP**.

---

## What assistants can do

Once connected, an assistant can read your **dashboards**, **metrics**, **logs**, **traces**, and the **situations** your coworker is tracking - and, depending on the permission tier, act on them.

Each person connects their own assistant and signs in as themselves, so there is no key to paste and everyone sees what they can already see in OpsPilot.

OpsPilot MCP declares no **capabilities**, so it provisions no dashboards or alerts of its own. It reads and acts on what is already in your account.

---

## Permission tiers

| Tier | Description |
|---|---|
| **Read + Act** | The default. Assistants may read and act on what they find. Requires nothing - your plan grants it |
| **Read-only** | Assistants may only read. Requires nothing, and holds the whole organisation to reading |

The tier set on the install is the **ceiling for the whole organisation**, whichever address a person connects with. Read-only is enforced by OpsPilot rather than trusted to the client, so an assistant on a read-only connection is never offered the tools that change anything.

---

## Installing

Click **Install** on the **OpsPilot MCP** card in the [integration catalog](../../integrations.md), or from its detail view. The dialog confirms which account the install will serve. Click **Install** to confirm.

Installing makes OpsPilot available. Each person still points their own assistant at it.

---

## Connect your assistant

Open **Connect** on the integration. Choose the address you want, then send it to your client or copy it.

### Which address

| Address | What it gives |
|---|---|
| **Full access** | The default. Read and act |
| **Read-only** | Never offers the tools that change anything |

The choice applies to the **connection**, not the account - so somebody who also adds the full address gets the full surface. To hold everyone to reading whatever they connect with, set the install's permission tier to **Read-only**. Where both apply, the stricter wins.

### Sending it to your client

**Connect** offers a button per client:

| Client | How |
|---|---|
| **VS Code** and **VS Code Insiders** | Click the button to hand the address straight to the editor |
| **Claude Code** | Copy the `claude mcp add` command and run it |
| **Claude desktop and web** | Click **Open**, or copy the address and add it under **Customize → Connectors → Add custom connector** |

!!! note "The address lives on the Connect page"
    OpsPilot runs in more than one environment, so a written-down address names only one of them. Always take the address from **Connect** rather than copying one from documentation.

---

## Setting it up for everyone

If you are an **Owner** of a Claude Team or Enterprise organisation, add it once for everybody: **Organization settings** → **Connectors** → **Add**, and paste the address from **Connect**.

That covers desktop, web, mobile and Claude Code together. It makes OpsPilot available; each person still enables it and signs in as themselves.

---

## Check it works

Ask your assistant:

> *what situations are active right now?*

A list means you are connected.

---

## Troubleshooting

**A VS Code button does nothing.** Those buttons hand the address to the editor through a link the operating system routes, so nothing happens when that editor is not installed on the machine you are reading this on. Copy the address instead and add it from inside the client.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
