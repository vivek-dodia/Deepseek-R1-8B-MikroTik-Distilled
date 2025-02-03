Okay, let's dive deep into RoMON configuration for a point-to-point link using RouterOS 7.11, focusing on practical, real-world implementations.

## Scenario Description:

We will configure RoMON (Router Management Overlay Network) on two MikroTik routers connected via a wireless point-to-point link using interface "wlan-77". These routers are within the 177.69.46.0/24 subnet. RoMON will allow us to manage either router from the other router. RoMON facilitates simplified management of interconnected MikroTik devices, offering features such as neighbour discovery and secure communication via layer 2.

## Implementation Steps:

### Step 1: Enable RoMON on Both Routers

*   **Description:** We must enable the RoMON service on each router. This is the foundation of RoMON functionality. Without it, no RoMON communication can be achieved.
*   **Before:** No RoMON service active. The router will not respond to RoMON discovery.
*   **Action (Router 1 and Router 2):**
    *   **CLI:**
        ```mikrotik
        /tool romon set enabled=yes
        ```
    *   **Winbox:** Navigate to `Tools` -> `RoMON`. Check the "Enabled" box.
*   **After:** RoMON service is enabled and actively listening for RoMON packets.
*   **Expected Effect:** The router will now listen for RoMON packets.

### Step 2: Setting RoMON Interfaces

*   **Description:** We need to specify the interfaces on which RoMON will listen and send packets. In this case, it's "wlan-77". This is necessary to constrain RoMON traffic to the appropriate network. If an interface is not specified, RoMON will use all network interfaces.
*   **Before:** RoMON is enabled, but is not yet configured for the target interface.
*   **Action (Router 1 and Router 2):**
    *   **CLI:**
        ```mikrotik
        /tool romon interface add interface=wlan-77
        ```
    *   **Winbox:** In the `Tools` -> `RoMON` interface, add a new record. Use `wlan-77` as the interface.
*  **After:** RoMON is enabled only on interface `wlan-77`.
*   **Expected Effect:** RoMON packets are only sent and received on the specified wireless interface. RoMON will not be active on any other interface.

### Step 3: Setting a RoMON Secret (Optional, but Highly Recommended)

*   **Description:** To secure RoMON, a shared secret can be set. This prevents unauthorized devices from joining the RoMON network. This adds an additional layer of security over basic functionality. Without the secret, any device can participate in the network.
*   **Before:** RoMON is enabled and is using the wireless interface. There is no security.
*   **Action (Router 1 and Router 2):**
    *   **CLI:**
        ```mikrotik
        /tool romon set secret="MySuperSecret"
        ```
    *   **Winbox:** In `Tools` -> `RoMON`, input a secret in the "Secret" field.
*   **After:** RoMON is using the shared secret.
*   **Expected Effect:** Only devices using the same secret will be able to communicate via RoMON.

### Step 4: Testing RoMON Connectivity

*   **Description:** After configuration, we must verify that the RoMON setup is functioning correctly. This is critical to ensure reliable management of all the interconnected routers.
*   **Before:** RoMON configuration is completed.
*   **Action (Router 1):**
    *   **CLI:**
        ```mikrotik
        /tool romon neighbours print
        ```
    *   **Winbox:** In the `Tools` -> `RoMON` window, open the `Neighbours` tab.
*   **Expected Effect:** Router 2 is listed as a neighbour, with the correct MAC address. The router will discover its peer router.

## Complete Configuration Commands:

**Router 1 & 2 (Identical):**

```mikrotik
# Enable RoMON
/tool romon set enabled=yes

# Set RoMON interface
/tool romon interface add interface=wlan-77

# Set RoMON Secret (optional, but highly recommended)
/tool romon set secret="MySuperSecret"
```

**Parameter Explanations:**

| Command                | Parameter       | Value         | Description                                                                     |
| :--------------------- | :-------------- | :------------ | :------------------------------------------------------------------------------ |
| `/tool romon set`     | `enabled`       | `yes`         | Enables the RoMON service globally on the router.                              |
| `/tool romon set`     | `secret`        | `"MySuperSecret"` | Specifies the shared secret for RoMON authentication. Ensure it is the same on all routers.  |
| `/tool romon interface add`  | `interface`     | `wlan-77`      | The interface on which RoMON will operate.                                    |

## Common Pitfalls and Solutions:

*   **Problem:** No RoMON neighbours are discovered.
    *   **Solution:**
        *   Verify the `enabled` status on both routers.
        *   Check interface configuration (`/tool romon interface print`).
        *   Ensure the secret is identical (`/tool romon print`).
        *   Check the wireless connection between routers is stable.
        *   Check for any firewalls that may be interfering.
        *   Ensure that no network bridges are interfering with the communications.
*   **Problem:** RoMON is unstable or slow.
    *   **Solution:**
        *   Ensure the interface is set correctly and is stable.
        *   Check the CPU and memory usage on both routers.
        *   If using a large number of RoMON devices, consider using a designated management interface to reduce noise.
*   **Problem:** Mismatched secrets.
    *   **Solution:** Double check that the secret is correct on both devices.

## Verification and Testing Steps:

1.  **RoMON Neighbours Check:** On either router, execute `/tool romon neighbours print`. This will display discovered neighbours, including their MAC address and other information.
2.  **RoMON Connection Test (CLI):** SSH into Router 1. Then connect to router 2 using RoMON with the following command: `/tool romon ssh <router2-mac-address>`. This will establish an SSH connection to the remote router without going through IP layer.
3.  **RoMON Connection Test (Winbox):** In Winbox, connect to Router 1. In the `Tools -> RoMON -> Neighbours` window, right click the neighbour device (router 2). Click the `Connect to device` option.
4.  **Torch (on RoMON Interface):** On each router, execute `/tool torch interface=wlan-77`. Confirm the presence of RoMON traffic. Use the filter `ether proto 0x88bb` to only show RoMON traffic.
5.  **Ping (via RoMON):** Ping the other router's RoMON address using `/ping <router2-romon-address>` (or similar).
6.  **Traceroute (via RoMON):** Traceroute to the other router using `/traceroute <router2-romon-address>`.

## Related Features and Considerations:

*   **Management VLAN:** For larger networks, consider running RoMON on a dedicated management VLAN. This can separate management traffic from user traffic for security.
*   **Multiple RoMON interfaces:** RoMON can operate over multiple interfaces, though this can complicate management. Ensure the interfaces configured are only those required.
*   **SNMP:** RoMON can be used in conjunction with SNMP to monitor devices.
*   **Netwatch:** RoMON could be used as an additional network health and management interface if required.
*   **Traffic Engineering:** RoMON does not contribute directly to any traffic engineering. It simply provides a separate management network.

## MikroTik REST API Examples (if applicable):

RoMON has limited API capabilities. There are no API endpoints to manage the configuration itself. However, you can retrieve neighbor information. Here is an example:

**Retrieve RoMON Neighbours:**

*   **Endpoint:** `/tool/romon/neighbours`
*   **Method:** `GET`
*   **Request:** (No payload)
*   **Response (Example):**

```json
[
  {
    ".id": "*1",
    "interface": "wlan-77",
    "mac-address": "AA:BB:CC:DD:EE:01",
    "version": "7.11",
    "uptime": "5m30s",
    "cpu-load": "5",
    "memory-usage": "35%",
     "board-name": "RB951G-2HnD"
  },
  {
    ".id": "*2",
    "interface": "wlan-77",
    "mac-address": "AA:BB:CC:DD:EE:02",
    "version": "7.11",
    "uptime": "10m20s",
    "cpu-load": "3",
    "memory-usage": "30%",
    "board-name": "RB951G-2HnD"
  }
]
```

*   **Error Handling:** If the API call fails, the server returns an error message. Check the HTTP status code in your application or client to diagnose the error.

## Security Best Practices

*   **Strong Secret:** Always use a strong, unique secret for RoMON. Ensure no devices use any default secret.
*   **Interface Control:** Limit the RoMON interface to only the required interfaces. Avoid running it on interfaces exposed to the public internet.
*   **Network Segmentation:** Isolate the management network using VLANs. Ensure a firewall is in place for additional security.
*   **Monitor RoMON Traffic:** Regularly monitor RoMON packets for unusual behaviour with tools like "torch".
*  **Regular Updates:** Keep the RouterOS software updated to the latest version. Apply relevant patches.
* **Disable RoMON When Not Required**: If the RoMON function is not currently required, it should be disabled on each device.

## Self Critique and Improvements

*   **Improvement:** This configuration does not include traffic prioritization using QoS. QoS configuration should be added in order to prioritise management packets over user traffic.
*   **Improvement:** There is no log configuration to report changes in RoMON or network topology. These should be added to a remote syslog server for long-term archival.
*   **Improvement:** The security could be improved by implementing a network-wide firewall rule that restricts RoMON traffic to the internal network only.
*   **Improvement:** The configuration is suitable for a small-to-medium-size network, but not for a very large network. A larger network would require additional planning.
*   **Improvement:** The configuration does not include a secure way to transmit the RoMON secret. This should be handled outside the router itself, to minimise the chance of the secret being compromised.

## Detailed Explanations of Topic

RoMON is a proprietary MikroTik protocol, designed for device discovery and management of interconnected routers. It is layer-2, not layer-3, meaning that routing rules are not required to use RoMON. It creates an overlay network, which operates in parallel with the existing IP network. This means that the network does not need to be routed for RoMON to function.

RoMON uses a discovery protocol that allows devices to locate each other on the same layer-2 broadcast domain. The devices will exchange information about their status, such as uptime, version and CPU load. These data points are useful for maintenance and monitoring.

RoMON is very low overhead. Because it is layer 2, there is no routing, thus reducing the complexity of the network. This can have a positive impact on network stability.

## Detailed Explanation of Trade-offs

*   **Security:** Using RoMON without a secret is simpler to set up, but poses a security risk. If using an encrypted management network or a secure environment, the overhead of the secret might be unnecessary. However, in an environment where there may be security risks, a shared secret is highly recommended.
*   **Complexity:** Running RoMON on multiple interfaces increases complexity, but it does allow more versatility. Using only a single management interface reduces the complexity, and the likelihood of misconfiguration.
*   **Traffic Overload:** Running RoMON on a busy interface could add to existing overhead, but this overhead is usually low. If RoMON is used on a particularly busy interface, this could degrade performance of other services. Running RoMON on a dedicated management VLAN is preferable for large networks, however it adds a layer of complexity.
*   **Functionality:** RoMON offers direct management and monitoring without having to rely on IP. However, tools such as The Dude or similar can also be used, and offer more features at the expense of more resources.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 7.11. All of the commands are available from version 6.48 upwards, including 7.x. As such, it should work on all modern versions of RouterOS.
