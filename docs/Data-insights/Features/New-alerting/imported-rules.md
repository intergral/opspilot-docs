# Imported Alert Rules

Alert rules you created in FusionReactor Alerts were carried over to OpsPilot Alerting in their original format. They keep working exactly as they always did.

You can leave them alone, or update them to the standard format used by rules created in OpsPilot. Nothing forces the change - this page explains how to tell the two apart, what differs, and how to convert one safely if you decide to.

## Recognizing an imported rule

Two things give an imported rule away:

- **Its query ends in a comparison**, such as `up{job="api"} == 0` or `sum(rate(http_errors_total[5m])) > 5`. The condition that makes the rule fire is part of the query itself.
- **In [Advanced mode](rules.md#advanced-mode), it has a Math step named `prometheus_math`** between the Query step and the Threshold step.

That Math step checks only whether the query returned anything at all. It returns `1` if it did and `0` if it didn't, and the Threshold step then fires on anything above `0`.

!!! note "Why the chart shows a threshold of 0"
    This is why an imported rule's graph draws its threshold line at `0`, even for a rule named something like *CPU Process Usage > 90%*. The real condition is inside the query - the Threshold step is only asking whether the query returned a result.

## Why imported rules keep their original format

Imported rules were not converted automatically, because the standard format behaves slightly differently. Converting them without asking could change when your alerts fire, so the decision is left to you, rule by rule.

| | Imported format | Standard format |
|---|---|---|
| **Where the condition lives** | Inside the query (`... == 0`) | In the Threshold step |
| **What the query returns** | Only the values that already meet the condition | Every value, whether it meets the condition or not |
| **Chart on the alert page** | Shows data only while the rule is firing | Shows the full history, with the threshold drawn on it |
| **Alert instances** | Appear only while firing | Always listed, each in its current state |
| **No data setting** | Must stay at **Normal**, because no data is how the rule reports *all clear* | Your choice: **No Data**, **Alerting**, **Normal**, or **Keep last state** |

## Updating an imported rule

Updating a rule means moving the condition out of the query and into the Threshold step, then removing the `prometheus_math` Math step.

!!! tip "Consider working on a duplicate"
    You can edit the rule directly, but on a rule carried over from the old system it is safer to select **Duplicate** first and change the copy. The original keeps alerting while you confirm the copy behaves the way you want, and you remove the original only once you are sure.

1. Open the rule - or select **Duplicate** and open the copy - and select **Advanced**.
2. In the **Query** step, delete the comparison from the end of the query - for example, change `up{job="api"} == 0` to `up{job="api"}`. Note the comparison and the number you removed.
3. Remove the **Math** step named `prometheus_math`.
4. In the **Threshold** step, set the input to the Query step. Then set the comparison and the number you noted in step 2.
5. Set **No data** and **On error** to what you want the rule to do in those cases. See [What changes after you update](#what-changes-after-you-update).
6. Check the preview chart. It should now show your full data, with the threshold drawn on it.
7. Select **Save rule**.

If you worked on a duplicate, it is saved with *(copy)* at the end of its name. Let both rules run side by side and compare when each one fires - while both are running, you receive notifications from each.

When the copy behaves the way you want, pause or delete the original rule, and rename the copy if you like.

### Choosing a comparison

The Threshold step offers **Is above**, **Is below**, **Is within range**, and **Is outside range**. If your rule used `==`, `!=`, `>=`, or `<=`, choose the closest option and adjust the number.

!!! example
    `up == 0` becomes **Is below** `1`, because `up` is only ever `0` or `1`.

## What changes after you update

An updated rule fires on the same condition, but two edge cases may behave differently than before. Check both before relying on the updated rule.

**No data now means no data.** In the imported format, an empty result meant *inactive* - the rule would not fire. In the standard format, an empty result means the query found nothing at all, for example because a service stopped reporting. You choose what happens then with the **No data** setting: raise a No Data alert, fire the alert, resolve it, or keep its current state.

**NaN and infinite values may not be caught.** The imported rule fired on any value the query returned, including NaN (not a number) and infinity. A Threshold step compares numbers, so a NaN value never crosses it. If your data can produce these values, handle them in the query itself.

These differences are why the update is left to you. If a rule already does what you need, you can keep it in its imported format.

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
