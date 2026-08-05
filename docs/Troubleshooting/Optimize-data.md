# How to optimize data sent to the FusionReactor Cloud

In certain scenarios, it might be advantageous to optimize the amount of trace data sent to the FusionReactor Cloud to achieve a balance between observability and resource efficiency. All tracing data is sampled, so you get examples of normal transactions as well as error or slow transactions, to compare as required. 

!!! note
    The default sampling ratio for FusionReactor is set to 0.05  or 5% of **all** traces.

FusionReactor provides a flexible solution by allowing users to control the trace sampling ratio using a configuration parameter. The setting can be adjusted as necessary depending on the amount of tracing data your applications generate.

## Configuration parameter

Property: -Dfr.observability.trace.sampling.ratio

This property allows users to specify the sampling ratio for trace data sent to the FusionReactor Cloud. The sampling ratio represents the percentage of traces to be captured. Adjusting this ratio enables users to reduce the volume of trace data transmitted while still maintaining essential insights.

## Benefits of adjusting the sampling ratio

* **Reduced data transmission**  
Lowering the sampling ratio decreases the amount of trace data transmitted to the FusionReactor Cloud. This is particularly useful in scenarios where bandwidth or storage considerations are crucial.

* **Resource optimization**  
By capturing a fraction of traces, users can optimize resource utilization on both the application and FusionReactor Cloud sides, ensuring efficient performance monitoring without excessive data overhead.

* **Cost-efficiency**   
Reduced data transmission can lead to cost savings, especially in cloud environments where data transfer and storage costs are significant factors.

## Example usage

FusionReactor's default sampling ratio is set to **`0.05`**, representing a **5%** sampling rate. Larger companies handling extensive data volumes may consider adjusting this setting to further reduce the transmitted trace data.

To set the trace sampling ratio to **3%**, the following JVM argument can be used:

```
-Dfr.observability.trace.sampling.ratio=0.03
```

In this example, the value **`0.03`** now signifies a **3%** sampling rate. Users can customize this value according to their specific requirements. 

---

!!! question "Need more help?"
    Contact support in the chat bubble and let us know how we can assist.
