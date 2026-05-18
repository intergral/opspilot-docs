# What endpoints need to be exposed for the FusionReactor Agent to connect to the Cloud?

FusionReactor requires outbound connections to specific endpoints to communicate with OpsPilot. You have two primary options for configuring your firewall: using DNS names (recommended) or static IP addresses.

### Option 1: Using DNS Firewall Rules (Recommended)

This method allows for automatic updates to IP addresses and is the most flexible. You need to allow outbound SSL traffic to the following services:

* **`wss://cc.fusionreactor.io`** – port `tcp/2804` (for FusionReactor 12 and below)
* **`https://api.fusionreactor.io`** – port `tcp/443`

When configuring your firewall rules, it's recommended to use the DNS names directly. If your firewall requires IP addresses, you should verify the current values using `nslookup` and add *all* returned IP addresses to your firewall rules (typically two per service).

### Option 2: Using Static IP Addresses 

If you are unable or unwilling to use dynamic DNS rules, you can use the following static IP address for all services:

* **`46.137.127.35`** – port `tcp/443` and port `tcp/2804`

After enabling this firewall rule, you **must** apply the following JVM arguments to your environment to instruct FusionReactor to use this single address:

```
-Dfr.gcs.client.endpoint=wss://cc-static.fusionreactor.io:2804/
-Dfr.cloud.endpoint=https://api-static.fusionreactor.io
```

### Locked-Down Environments (Java Security Policy)

If you are operating in a non-standard Java security policy environment, you may need to add specific `SocketPermission` rules to allow FusionReactor to connect to these services. The form of these rules is:

```
permission java.net.SocketPermission "cc-static.fusionreactor.io:2804", "connect, accept, resolve";
permission java.net.SocketPermission "api-static.fusionreactor.io:443", "connect, accept, resolve";
permission java.net.SocketPermission "46.137.127.35:443", "connect, accept, resolve";
permission java.net.SocketPermission "46.137.127.35:2804", "connect, accept, resolve";
```

!!! note
    If you are using the static IP address configuration, you will also need to apply the `-Dfr.gcs.client.endpoint` and `-Dfr.cloud.endpoint` JVM options as listed under "Using Static IP Addresses" above, in addition to the Java security policy permissions.