Okay, let's dive into a detailed technical document for configuring a MAC Server on a MikroTik router running RouterOS 6.48 (applicable to 7.x as well).

**Scenario Description:**

We aim to configure a MAC Server on a MikroTik router with the subnet 140.195.233.0/24 assigned to the bridge interface named `bridge-21`. This setup allows us to provide specific services based on MAC addresses, most commonly to authenticate clients and deliver specific configurations (IP address assignment, etc.) via protocols like DHCP. While MAC servers can exist independently, they are more often a component of a DHCP server, so this is where the focus will lie, but with some additional considerations for MAC-based security.

**Implementation Steps:**

Here's a step-by-step guide, incorporating CLI and Winbox GUI where it provides a good example:

1.  **Step 1: Verify the Existence of the Bridge Interface**
    *   **Description:** Before configuring anything, ensure the bridge interface `bridge-21` exists and is correctly configured.
    *   **CLI (Before):**
        ```mikrotik
        /interface bridge print
        ```
    *   **Expected Output (Example):** This output should show a bridge interface in the table with a name that exists in the system, preferably `bridge-21`. If it does not exist, it will need to be created.
        ```
        Flags: X - disabled, R - running
         0  R name="bridge1" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled
            mac-address=xx:xx:xx:xx:xx:xx protocol-mode=rstp priority=0x8000
            auto-mac=no admin-mac=xx:xx:xx:xx:xx:xx
            fast-forward=yes
        ```
     *   **Winbox GUI:** Navigate to `Bridge` -> `Bridge` tab. Verify if the `bridge-21` interface is listed.
    *   **CLI (After Creation if it doesn't exist, or modifications needed):**
        ```mikrotik
         /interface bridge add name="bridge-21" protocol-mode=none
         /ip address add address=140.195.233.1/24 interface="bridge-21" network=140.195.233.0
        ```
    *   **Effect:** Ensures that the necessary bridge interface exists and if not, creates it with a basic configuration and an address assigned to it.

2.  **Step 2: Configure the DHCP Server on the Bridge Interface**
    *   **Description:**  We now set up the DHCP server that will use our MAC Server to provide client configurations.
    *   **CLI (Before):**
        ```mikrotik
        /ip dhcp-server print
        ```
    *   **Expected Output:**  Will show existing DHCP servers. There will not be one associated with `bridge-21`
    *   **CLI (After):**
        ```mikrotik
        /ip dhcp-server
        add address-pool=dhcp_pool interface=bridge-21 name=dhcp-bridge21
        /ip dhcp-server network
         add address=140.195.233.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=140.195.233.1
         /ip pool add name="dhcp_pool" ranges=140.195.233.2-140.195.233.254
        ```
    *   **Winbox GUI:** Navigate to `IP` -> `DHCP Server`. Create a new server for `bridge-21`, configuring the pool as `dhcp_pool`, the network as `140.195.233.0/24`, and a gateway of `140.195.233.1` with appropriate DNS servers.
    *   **Effect:** Creates a DHCP server associated with the `bridge-21` interface and the necessary network configuration.

3.  **Step 3: Configure MAC Binding**
    *   **Description:** Now, this is where the MAC Server comes into play. We will create a static MAC binding. We will also configure the MAC server to use "only-static" mode for example.
    *   **CLI (Before):**
        ```mikrotik
        /ip dhcp-server lease print
        ```
    *   **Expected Output:** Will show existing leases, and likely none.
    *   **CLI (After):**
        ```mikrotik
        /ip dhcp-server lease add address=140.195.233.10 mac-address=AA:BB:CC:DD:EE:FF client-id=AA-BB-CC-DD-EE-FF server=dhcp-bridge21
        /ip dhcp-server set dhcp-bridge21 always-broadcast=yes authoritative=yes use-radius=no
        /ip dhcp-server set dhcp-bridge21  mac-server-mode=only-static
        ```

    *   **Winbox GUI:** Navigate to `IP` -> `DHCP Server` -> `Leases` tab. Add a new static lease. Set the `Mac Address`, the assigned `Address`, and ensure `Server` is set to `dhcp-bridge21`.
    *   **Effect:** When a client with MAC address `AA:BB:CC:DD:EE:FF` requests an IP via DHCP, the DHCP server will always assign it the IP address `140.195.233.10` while in 'only-static' mac-server-mode . If a client with any other mac-address requests an IP via DHCP, it will receive nothing in this specific configuration.

4.  **Step 4: Testing (See Verification Steps)**

**Complete Configuration Commands:**

```mikrotik
# Create the bridge interface (if it doesn't exist, adapt if modification only is needed)
/interface bridge add name="bridge-21" protocol-mode=none
/ip address add address=140.195.233.1/24 interface="bridge-21" network=140.195.233.0

# Configure the DHCP Server
/ip dhcp-server add address-pool=dhcp_pool interface=bridge-21 name=dhcp-bridge21
/ip dhcp-server network add address=140.195.233.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=140.195.233.1
/ip pool add name="dhcp_pool" ranges=140.195.233.2-140.195.233.254

# Configure Static MAC Binding
/ip dhcp-server lease add address=140.195.233.10 mac-address=AA:BB:CC:DD:EE:FF client-id=AA-BB-CC-DD-EE-FF server=dhcp-bridge21

# Configure mac-server-mode
/ip dhcp-server set dhcp-bridge21 always-broadcast=yes authoritative=yes use-radius=no
/ip dhcp-server set dhcp-bridge21 mac-server-mode=only-static
```

**Parameter Explanations:**

| Command             | Parameter       | Description                                                                                                                              |
| :------------------ | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| `/interface bridge add`    | `name`          | Name of the bridge interface.                                                                                                       |
|                     | `protocol-mode` | STP protocol mode. `none` disables STP.                                                                                                       |
| `/ip address add`    | `address`       | IP address and subnet mask in CIDR notation.                                                                                              |
|                     | `interface`     | The interface on which the IP address will be assigned.                                                                                 |
|                     | `network`       | The network address of the IP.                                                                                                          |
| `/ip dhcp-server add`| `address-pool`  | The name of the IP address pool to be used by this DHCP server.                                                                     |
|                     | `interface`     | The interface on which the DHCP server will be active.                                                                                   |
|                     | `name`          | The name of the DHCP server.                                                                                                             |
| `/ip dhcp-server network add`   | `address`      | The DHCP network address and mask.                                                                                                   |
|                     | `gateway`       | The default gateway for clients.                                                                                                       |
|                     | `dns-server`    | The DNS server(s) for clients.                                                                                                       |
| `/ip pool add`      | `name`          | Name of the IP address pool.                                                                                                           |
|                     | `ranges`        | Range of IP addresses within the pool (e.g., first-last).                                                                                |
| `/ip dhcp-server lease add`| `address`       | Static IP address to assign.                                                                                                           |
|                     | `mac-address`   | The MAC address of the client to match.                                                                                                |
|                     | `client-id`   | The DHCP client id of the client, typically will be the MAC address.                                                                                                |
|                     | `server`   |  The name of the dhcp server this lease belongs to.                                                                                                  |
| `/ip dhcp-server set`     | `mac-server-mode` |  Mode of the MAC server. Options: `disabled`, `enabled`, `only-static` (only use static leases based on MAC address)                             |
|                     | `always-broadcast`| Always broadcast DHCP replies (needed for clients that don't support unicast replies).                 |
|                     | `authoritative`   | Force authoritative responses.                                                                                                        |
|                     | `use-radius`   | Whether to use RADIUS for authentication and accounting.                                                                                                        |

**Common Pitfalls and Solutions:**

*   **Problem:** Clients not getting IP addresses:
    *   **Solution:** Ensure the bridge interface is up and enabled. Check that there are no conflicting IP addresses assigned. Verify the DHCP server is enabled and correctly assigned to the `bridge-21` interface.  Double-check the MAC address in the lease is correct.
*   **Problem:** DHCP server not responding:
    *   **Solution:** Check the firewall if it might be blocking DHCP ports (67/68 UDP). Ensure the DHCP server is configured on the correct interface and network. Use the `/ip dhcp-server monitor` command to see server activity.
*   **Problem:** MAC address mismatch:
    *   **Solution:** Verify that the MAC address configured in the static lease matches exactly the MAC address of the device requesting the IP.
* **Problem:** `mac-server-mode=only-static` blocks all non-static devices.
    *   **Solution:** Understand that in `only-static` mode, only clients with assigned static leases will obtain IP addresses. Change the mode to `enabled` to allow dynamic address assignment.
* **Security Risk**: DHCP server is unencrypted and susceptible to MITM attacks.
    *   **Solution:** Implement port security with trusted ports, use DHCP snooping on switches, and consider alternatives like 802.1X or Radius if security is a primary concern.

**Verification and Testing Steps:**

1.  **Verify Interface and Address:**
    *   Use `ip address print` to confirm the IP address 140.195.233.1/24 is assigned to `bridge-21`.
2.  **Verify DHCP Server:**
    *   Use `ip dhcp-server print` to ensure that DHCP is running on `bridge-21` and the pool is named `dhcp_pool`.
3.  **Verify Static Lease:**
    *   Use `ip dhcp-server lease print` to verify the static lease for MAC address `AA:BB:CC:DD:EE:FF` exists and has the address `140.195.233.10`.
4.  **Client Testing:**
    *   Connect a client to the same network. If using a computer, set its network configuration to use DHCP. The client with `AA:BB:CC:DD:EE:FF` as its MAC address should always obtain the `140.195.233.10` address, and all others will not get an IP if the `mac-server-mode` is `only-static`.
5.  **Use Torch to monitor DHCP requests**:
    * Use the `/tool torch interface=bridge-21 protocol=udp port=67,68` to monitor DHCP requests and replies to troubleshoot any issues.

**Related Features and Considerations:**

*   **DHCP Options:** You can configure DHCP options for clients such as default gateway, DNS servers, and other settings. These can be set globally or per lease.
*   **RADIUS:** For more advanced scenarios, integrate the DHCP server with a RADIUS server for authentication and accounting of connected clients.
*   **Firewall Rules:** Implement firewall rules to restrict DHCP traffic to specific ports and trusted devices, further enhancing the security of the network.
*   **VLANs:** If your network uses VLANs, ensure the DHCP server is correctly configured on each VLAN using bridge interfaces for VLAN tagging.
*   **Alternative Mac Address Based Authentication:** Consider integrating with a system like 802.1x for security, as the dhcp-server MAC server is a less secure method for client identification.
* **Rate limiting**: Use the traffic shaping to limit bandwidth for clients if this is required.

**MikroTik REST API Examples (if applicable):**

While the direct manipulation of DHCP leases via REST API is possible, it might be more practical to interact with the underlying MikroTik CLI system through an API call. This means we could execute CLI command using an API call.
* **API endpoint**:  `/rest/system/script`
* **Method**:  POST

* **Example JSON Payload for creating a static MAC binding:**
```json
{
    "command": "/ip/dhcp-server/lease/add",
    "params": {
        "address": "140.195.233.10",
        "mac-address": "AA:BB:CC:DD:EE:FF",
        "server": "dhcp-bridge21",
        "client-id": "AA-BB-CC-DD-EE-FF"
    }
}
```
* **Expected Successful Response (Example):**
```json
{
    "status": "success",
     "details": { "message": "lease added" }
}
```

* **Example JSON Payload for setting the mac-server mode:**
```json
{
    "command": "/ip/dhcp-server/set",
    "params": {
        ".id":"dhcp-bridge21",
        "mac-server-mode": "only-static"
    }
}
```
* **Expected Successful Response (Example):**
```json
{
    "status": "success",
     "details": { "message": "dhcp server configured" }
}
```

*   **Error Handling:**  Any error that arises from the command execution will be reported in the `status` field.  For example, a permission denied error might look like:
```json
{
  "status": "error",
  "details": {
    "message": "failed to set, permission denied"
  }
}
```

**Security Best Practices:**

*   **Limit Access:** Ensure only authorized users can access the MikroTik Router. Use strong passwords and consider two-factor authentication.
*   **Firewall:** Implement firewall rules to allow only necessary traffic. Protect the router from external access.
*   **Regular Updates:** Keep the RouterOS software up to date to fix security vulnerabilities.
*   **MAC Filtering:** Use MAC filters or access lists to limit what devices can connect to the network. While the MAC server itself provides some control over IP addressing, also limit which devices can be on the layer-2 bridge.
*   **Secure Protocols**: Use secure protocols such as SSH over Telnet, and HTTPS over HTTP where relevant, particularly for API access.
*   **Audit Logs:** Regularly review audit logs for unauthorized activity and suspicious behavior.

**Self Critique and Improvements:**

*   **Improvement:** Using a separate bridge interface dedicated to the DHCP server offers better control, and isolation for specific devices, this also makes monitoring easier, and easier to implement specific firewall rules.
*   **Improvement:** For larger environments, integrating with a RADIUS server for more advanced client authentication and authorization can add a layer of security, especially in environments where there is a need to implement advanced security.
*   **Improvement**: It may be better practice to use specific pools for each category of client, allowing better control over allocated IPs.

**Detailed Explanations of Topic:**

A MAC server, in the context of MikroTik RouterOS, is a feature that allows a DHCP server to behave differently based on the MAC address of the requesting client. While not a dedicated service on its own, its typically a feature that belongs to the DHCP server. It's not a 'server' in the traditional sense, but more a mode or filter through which DHCP servers operate. It comes in handy for setting up static IP assignments using the `only-static` mode, but can also be used to offer different pools and/or options for various classes of client MAC address. The way it works is when a client performs a DHCP request, the DHCP server checks the client's MAC address against any defined policies and/or static leases.

**Detailed Explanation of Trade-offs:**

*   **Static Leases with `only-static`:** In `only-static` mode, you have complete control over IP assignments, ensuring specific devices always get the same IP. However, it's not practical for very large, dynamic environments. The trade-off here is control and predictability against ease of deployment and management. It also may prevent new clients connecting to a network if the mode is misconfigured.
*   **Dynamic Allocation:** Using the DHCP server without MAC address binding is easier to manage in large dynamic environments, but you lose the predictability of IP address assignments. This is more scalable, but less controllable.
* **Security Implications**:
    * The MAC server is not secure by itself, it only acts as a filter based on layer-2 information. It does not protect against man-in-the-middle attacks, DHCP spoofing or other attack vectors.
    * MAC address can be easily spoofed, and therefore, this method should not be used as a primary means of secure access control.
    * Implement additional security measures, such as DHCP snooping, port security, firewall rules, and, more importantly, client authentication such as 802.1x or Radius, to secure the network.

**Configuration for Specific RouterOS Versions:**

The commands used are compatible with both RouterOS 6.48 and 7.x. There should not be any issue running the listed commands and configuration in either version. Please note that some additional features may only be available for one of the mentioned versions, but those have been omitted in favor of using features available for both.
