Okay, let's dive into crafting a comprehensive documentation for IP routing on MikroTik RouterOS 7.12, specifically for a point-to-point link using the subnet 202.149.90.0/24 on interface `ether-20`. This configuration is targeted at an expert level, assuming familiarity with core networking concepts.

**Scenario Description:**

We're setting up a basic point-to-point link between two MikroTik routers using a dedicated interface (`ether-20`). Both routers will reside on the 202.149.90.0/24 network. This is a common scenario for connecting buildings or extending a network across a relatively short distance with a dedicated connection. We'll focus on basic IP routing configuration - assigning IP addresses to interfaces and establishing reachability between the two endpoints. This is not about any routing protocol like OSPF/BGP; it's simple point to point configuration.

**Implementation Steps:**

Here’s a step-by-step guide for configuring IP routing in this scenario:

**Router 1 Configuration**
1.  **Step 1: Interface Identification & Enablement**
    *   **Purpose:** Identify the target interface (`ether-20`) and ensure it is enabled. By default, interfaces are enabled on MikroTik RouterOS. However, confirming the status and enablement is always a best practice.
    *   **Before Configuration:** Assuming a fresh setup, verify the interface status.
         *   **CLI:**
            ```mikrotik
            /interface print
            ```
        *   **Winbox GUI:** Navigate to `Interfaces` and observe `ether-20`. It should have an "R" for running status.

    *   **Configuration:** Enable the interface (if not already enabled).
         *   **CLI:**
            ```mikrotik
            /interface set ether-20 enabled=yes
            ```
         *   **Winbox GUI:** Select the interface, then check "Enabled" checkbox.

     *  **After Configuration:** Verify the interface is enabled.
        *   **CLI:**
           ```mikrotik
           /interface print where name=ether-20
           ```
        *   **Winbox GUI:** `Interfaces` list, should have an "R" for running status in its flag column.
    *   **Effect:** The interface `ether-20` is now ready for IP addressing.

2.  **Step 2: Assign IP Address**
    *   **Purpose:** Assign a static IP address to `ether-20` from the 202.149.90.0/24 subnet, using the first address in the range: 202.149.90.1/24.
    *   **Before Configuration:** There should be no IP address assigned to the interface.
       *   **CLI:**
            ```mikrotik
             /ip address print where interface=ether-20
            ```
         *   **Winbox GUI:** Navigate to `IP` -> `Addresses`, no entry should exist for `ether-20`.

    *   **Configuration:**
        *   **CLI:**
            ```mikrotik
            /ip address add address=202.149.90.1/24 interface=ether-20
            ```
        *   **Winbox GUI:** Navigate to `IP` -> `Addresses`, click `+`, set `Address` as `202.149.90.1/24` and `Interface` to `ether-20`, then click `Apply` and `OK`.

    *   **After Configuration:** Verify that the IP address is assigned to the interface.
        *   **CLI:**
            ```mikrotik
             /ip address print where interface=ether-20
             ```
        *   **Winbox GUI:** Navigate to `IP` -> `Addresses`, a new entry should exist with `202.149.90.1/24` for `ether-20`.

    *   **Effect:** The router now has an IP address on the specified interface and the interface is part of the `202.149.90.0/24` network.

**Router 2 Configuration**
1. **Step 1: Interface Identification & Enablement**
    *   **Purpose:** Similar to Router 1, ensure the interface (`ether-20`) is enabled.
    *   **Before Configuration:**
        *   **CLI:** `/interface print` (Check if ether-20 is in the list and running)
        *   **Winbox GUI:**  Check the interface status in the `Interfaces` list.
    *   **Configuration:**
        *   **CLI:** `/interface set ether-20 enabled=yes`
        *   **Winbox GUI:**  Select the interface and check the `Enabled` box.
    *   **After Configuration:**
         *  **CLI:** `/interface print where name=ether-20`
         *  **Winbox GUI:** The interface should show `R` (Running) in the `Flags` column
    *   **Effect:** The interface `ether-20` is now enabled.
2.  **Step 2: Assign IP Address**
    *   **Purpose:** Assign a different static IP address to `ether-20` from the same subnet. Using 202.149.90.2/24
    *   **Before Configuration:** There should be no IP address assigned to the interface.
        *   **CLI:** `/ip address print where interface=ether-20`
        *   **Winbox GUI:** No entry in `IP` -> `Addresses` for `ether-20`.
    *   **Configuration:**
        *   **CLI:** `/ip address add address=202.149.90.2/24 interface=ether-20`
        *   **Winbox GUI:**  Add a new address `202.149.90.2/24` to `ether-20` in the address list.
    *   **After Configuration:**
        *   **CLI:** `/ip address print where interface=ether-20`
        *  **Winbox GUI:** Verify the new entry for the IP address.
    *   **Effect:** The router now has a unique IP address within the 202.149.90.0/24 network on its ether-20 interface.

**Complete Configuration Commands:**
Here’s a consolidated set of commands for both Router 1 and Router 2.

**Router 1**

```mikrotik
/interface set ether-20 enabled=yes
/ip address add address=202.149.90.1/24 interface=ether-20
```

**Router 2**
```mikrotik
/interface set ether-20 enabled=yes
/ip address add address=202.149.90.2/24 interface=ether-20
```

**Parameter Explanation:**

| Command | Parameter | Description |
| ------------- | ------------------------ | ----------- |
| `/interface set`  | `ether-20` | Target interface. |
|             | `enabled=yes` | Enables the specified interface. |
| `/ip address add`  | `address=202.149.90.1/24` |  The IPv4 address and subnet mask for the interface on Router 1 |
| | `address=202.149.90.2/24` |  The IPv4 address and subnet mask for the interface on Router 2 |
|        | `interface=ether-20`  | The interface to apply the IP address to.  |

**Common Pitfalls and Solutions:**

*   **Incorrect Subnet Mask:** Misconfiguring the subnet mask will prevent proper communication. For example, using /30 instead of /24. **Solution:** Always verify subnet masks on both sides.
*   **Firewall Blocking:** RouterOS firewall rules could block ICMP (ping) or other traffic. **Solution:** Check firewall rules under `/ip firewall filter`. Allow established/related traffic and ping if required for troubleshooting. If there is a filter rule blocking everything - remove it. `/ip firewall filter remove [find action=drop chain=forward]`
*   **Disabled Interface:** If the interface is disabled, the IP address won't be active. **Solution:** Always verify the interface status under `/interface print`. Ensure the `enabled` flag is set to `yes`.
*   **Duplicate IPs:** Using the same IP address on both routers will cause conflicts. **Solution:** Ensure unique IP addresses within the same subnet on each interface.
*   **Cable Issues:** Physical layer problems (bad cabling/SFP modules etc.) can lead to connectivity issues. **Solution:** Check cables and connections.
*   **Resource Issues:** While unlikely with just this simple configuration, high CPU/memory can cause issues. **Solution:** Use the `system resource monitor` to track resource usage if experiencing issues.

**Verification and Testing Steps:**

*   **Ping Test:**
    *   **Router 1:** `ping 202.149.90.2` (Should be successful)
    *   **Router 2:** `ping 202.149.90.1` (Should be successful)
    *   **Winbox:** `Tools->Ping`
*   **Traceroute Test:**
     *   **Router 1:** `traceroute 202.149.90.2` (Should show a single hop to the IP on router 2)
    *   **Router 2:** `traceroute 202.149.90.1` (Should show a single hop to the IP on router 1)
    *   **Winbox:** `Tools->Traceroute`
*   **Torch:** (for advanced troubleshooting)
    *   **Router 1:** `/tool torch interface=ether-20` and `/tool torch interface=ether-20 address=202.149.90.2` - to verify traffic to the other end.
   *  **Router 2:** `/tool torch interface=ether-20` and `/tool torch interface=ether-20 address=202.149.90.1` - to verify traffic from the other end.
   *   **Winbox:** No direct GUI, CLI only.

**Related Features and Considerations:**

*   **VLANs:** If you need multiple logical networks over a single physical link, configure VLANs on `ether-20` on both routers.
*   **Link Aggregation (Bonding):** If you have multiple physical links, you can create a bonding interface for redundancy and increased bandwidth.
*   **Static Routes:** For more complex networks you will be adding static routes for other networks beyond this subnet.
*   **Routing Protocols:** For more complex networks use routing protocols like OSPF/BGP to dynamically learn routes.
*   **Quality of Service (QoS):** Implement QoS policies to prioritize specific traffic if needed.

**MikroTik REST API Examples (if applicable):**

This is a very basic setup, and REST API interaction isn't particularly advantageous here; CLI or Winbox are sufficient. However, for completeness, let’s see an example of adding an IP address via the REST API.

**API Endpoint:** `/ip/address`

**Request Method:** POST

**Example JSON Payload (Router 1):**

```json
{
    "address": "202.149.90.1/24",
    "interface": "ether-20"
}
```

**Request Method:** POST

**Example JSON Payload (Router 2):**

```json
{
    "address": "202.149.90.2/24",
    "interface": "ether-20"
}
```

**Expected Response:**

*   A successful creation will return status 200, and the response will usually contain the newly created entry's ID in the following format:

    ```json
       {
        ".id":"*3"
       }
    ```
*   An error will return an appropriate error message e.g., "interface not found" if the interface was not set before.

**Note on Error Handling:**
Always check the response code (e.g. 200 for success, 400 for bad request etc.). The MikroTik REST API provides detailed error messages to help you diagnose the problem.

**Security Best Practices:**

*   **Secure Router Access:** Change default passwords, use strong passwords, restrict access to management interfaces, disable unused services, enable HTTPS and use certificate on the web interface.
*   **Firewall:** Implement strict firewall rules to block any unnecessary access to the router from the outside.
*   **Regular RouterOS Updates:** Keep the RouterOS version updated to the latest stable version to get security fixes.
*   **Disable Unused Services:** Remove or disable any services that are not needed.
*   **Logging:** Enable logging to monitor the router's activity for suspicious events.
*   **Limit access to the API:** Only allow API access from trusted networks or hosts.

**Self Critique and Improvements:**

*   **Simplicity:** This is a very simple configuration for demonstration. In real-world scenarios, more complex configurations will be required including routing protocols or static routes for more involved network architectures.
*   **Scalability:** This is a point-to-point configuration. If more endpoints are added the complexity increases significantly, and routing protocols like OSPF or BGP would be much more efficient.
*   **Redundancy:** There is no redundancy in this configuration. If the physical link fails, connectivity is lost. Bonding or more complex failover mechanism would be needed.
*   **Security:** The security configuration is left out completely, and would need to be carefully configured on both routers for a real world use case.
*  **Monitoring:** Add monitoring system.

**Detailed Explanations of Topic:**

*   **IP Routing:** At its core, IP routing is the process of selecting paths for network traffic. In this simple example, this is trivial since both devices directly connected to the same segment. In more complex networks, routing involves routing tables and routing protocols for finding the best paths for packets.
*   **Point-to-Point Link:** A point-to-point link is a dedicated connection between two endpoints. It's often used for connecting two routers or devices directly using a dedicated connection.
*  **Subnetting:** The use of a subnet mask, in this case /24, defines the broadcast domain and the number of available host addresses within this segment. /24 means that first 24 bits of IP address define the network and the last 8 bits are for hosts, resulting in 254 usable addresses.
*   **Interface Management:** The `/interface` menu in RouterOS is where you manage your network interfaces (Ethernet, Wireless, etc.). You can enable/disable, monitor status, set MTU values, and other settings.
*   **IP Address Configuration:** The `/ip address` menu is used to assign IP addresses and subnet masks to the interfaces.

**Detailed Explanation of Trade-offs:**

*   **Static vs. Dynamic IP Assignment:** In this example, we used static IP addresses, which are simple for small, unchanging setups. However, DHCP could be used for automatic IP address configuration, but it introduces extra complexity.
*   **Static Routing vs. Dynamic Routing:** Static routing as such, is not used in this example. Since this is a basic configuration, we did not add a static route.  When the number of connected subnets grows, manual management of routes becomes extremely complex, so dynamic routing protocols (OSPF, BGP etc.) are preferred. Dynamic routing automatically adjusts to topology changes.
*   **Direct Link vs. Router-on-a-Stick:** We used a direct link between two routers. With "Router on a stick" topology, both routers would share the same VLAN and would connect to the same switch. This configuration makes network more complicated.
*   **Basic Setup vs. Full Implementation:** We focused on a basic IP address and interface setup. In real world setups, more considerations will be required (NAT, Firewall, Policy Based Routing, QoS etc.).

**Configuration for Specific RouterOS Versions:**

This configuration is compatible with RouterOS 7.12, and the CLI commands and parameters provided here are relevant and applicable to version 7.x and above, as well as some commands work on 6.48. If you use version 6.x, you may need some parameter changes.

This detailed documentation covers the IP routing setup as requested, and provides a solid foundation for further experimentation and study.
