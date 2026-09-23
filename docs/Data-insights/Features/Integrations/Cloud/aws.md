# AWS

Connect AWS for EC2, RDS, and other CloudWatch-held metrics.

The AWS integration puts your AWS account's own monitoring data next to everything else you watch. CloudWatch metrics and logs arrive with dashboards for the services you are already paying for, so you can see how an account is behaving without building the views yourself or leaving to go and look.

Navigate to **Integrations** from the left-hand sidebar, then select **AWS**.

---

## Permission tiers

Unlike most integrations, AWS needs credentials you supply - an IAM role or key with the right CloudWatch permissions.

| Tier | Requires |
|---|---|
| **Read-only** | The default. An AWS IAM role or key with `CloudWatch:Get*`, `List*`, and `Describe*` permissions |
| **Read + Write** | The Read permissions, plus `CloudWatch:PutMetricAlarm` and related write actions |

---

## What it provisions

AWS declares four capabilities - **Data Sources**, **Dashboards**, **Recording Rules**, and **Alerts**. The dashboards, alert rules, and recording rules are provisioned as soon as the install succeeds.

The current version installs **16 dashboards**, covering the services CloudWatch reports on.

---

## Working across regions

The dashboards follow the region configured on the installation. If you connect several AWS regions, install the AWS integration **once per region** - each instance gets its own data source, its own dashboards, and its own folder.

Two dashboards are the exception, because AWS only reports their metrics to `us-east-1`. Both pin that region themselves, so they work whatever region an installation uses.

---

## Two dashboards need extra setup

Two of the sixteen dashboards read metrics that AWS does not publish by default.

### AWS Billing

The **AWS Billing** dashboard reads `EstimatedCharges` from the `AWS/Billing` namespace. AWS publishes that metric only if billing alerts are switched on, and only into `us-east-1`. The dashboard queries that region regardless of the region you configured, so no change to the installation is needed.

To switch it on, in the AWS console:

1. Sign in to the **management account** of your organisation. The metric is published for the payer account, not for member accounts.
2. Open **Billing and Cost Management** → **Billing preferences**.
3. Enable **Receive CloudWatch billing alerts**, and save.

!!! note
    The metric starts being published from that point on and is not backfilled. The dashboard stays empty for the first few hours, and shows no history from before you enabled it.

### AWS CloudFront

CloudFront reports its metrics only to `us-east-1` as well. The dashboard pins that region itself, so it works whatever region the installation uses - but the credentials you supplied must be allowed to read CloudWatch in `us-east-1`.

!!! warning
    An IAM policy scoped to a single region will refuse this. If your CloudFront dashboard is empty, check that the credentials can read CloudWatch in `us-east-1`.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
