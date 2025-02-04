Okay, let's create a comprehensive technical documentation for the specified scenario, focusing on a Hotspot network with a dedicated IP subnet on a MikroTik RouterOS device.

**Scenario Description:**

We are setting up a MikroTik router to serve as a gateway for a Hotspot network. All clients connected to the Hotspot will obtain IP addresses from the 90.27.137.0/24 subnet. The Hotspot network is connected via a bridge interface named `bridge-47`. This document will focus on the core IP settings required to make this functional and explain how to handle related configurations, testing, and security practices.

**Target RouterOS Version:** 6.48 (or 7.x as configurations remain largely compatible for this feature). Configuration Level: Advanced. Network Scale: Hotspot Network.

**Implementation Steps:**

1.  **Step 1: Check Existing Interface Configuration:**
    *   **Explanation:** Before making any changes, we need to check the current configuration of the `bridge-47` interface. This step is crucial to understand if any previous settings exist that might interfere with our new configuration.
    *   **CLI Command:**
        ```mikrotik
        /interface bridge print where name="bridge-47"
        ```
    *   **Expected Output (Example - will vary depending on previous config):**
        ```
        Flags: X - disabled, R - running
        0   R name="bridge-47" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled mac-address=00:00:00:00:00:00
            protocol-mode=none priority=0x8000 auto-mac=yes admin-mac=00:00:00:00:00:00
            fast-forward=no igmp-snooping=no
        ```
        *   **Winbox GUI:** Navigate to *Bridge* > *Bridges* and double-click on the `bridge-47` interface, then review parameters.
    *   **Post-Step Effect:** No configuration change happens during this step, only a review of the existing state.

2.  **Step 2: Add IP Address to the Bridge Interface:**
    *   **Explanation:** We need to assign an IP address to the `bridge-47` interface, which will act as the default gateway for our Hotspot subnet.
    *   **CLI Command:**
        ```mikrotik
        /ip address add address=90.27.137.1/24 interface=bridge-47
        ```
    *   **Winbox GUI:** Navigate to *IP* > *Addresses*, click on the "+" button, in the *Address* field enter `90.27.137.1/24`, and in the *Interface* field select `bridge-47`.
    *   **Parameter Explanation:**
        *   `address=90.27.137.1/24`: Specifies the IPv4 address and subnet mask. `90.27.137.1` is the router’s IP and the `/24` indicates a subnet mask of `255.255.255.0`.
        *   `interface=bridge-47`: Defines the interface to which the IP address is assigned.
    *   **Expected Output (via CLI):**
         No output if the command runs successfully.
    *   **Post-Step Effect:** The router is now accessible at the address `90.27.137.1` on the `bridge-47` interface. We can verify this using the following command:
         ```mikrotik
          /ip address print where interface="bridge-47"
         ```
        Example Output:
         ```
            #   ADDRESS            NETWORK         INTERFACE      ACTUAL-INTERFACE
            0   90.27.137.1/24     90.27.137.0     bridge-47      bridge-47
        ```
        We can also see the change reflected in winbox.
3.  **Step 3: Configure DHCP Server for the Subnet:**
    *   **Explanation:** To automatically assign IP addresses to clients connecting to the Hotspot, we need to configure a DHCP server on the `bridge-47` interface.
    *   **CLI Command:**
        ```mikrotik
        /ip dhcp-server add name=dhcp-hotspot interface=bridge-47 address-pool=hotspot-pool disabled=no
        /ip dhcp-server network add address=90.27.137.0/24 gateway=90.27.137.1 dns-server=8.8.8.8,8.8.4.4
        /ip pool add name=hotspot-pool ranges=90.27.137.2-90.27.137.254
        ```
    *   **Winbox GUI:**
        *   Navigate to *IP* > *Pools*, click the "+" button. Enter a `Name` (ex. hotspot-pool) and a `Ranges` (`90.27.137.2-90.27.137.254`). Click OK.
        *   Navigate to *IP* > *DHCP Server*, click the "+" button, in the *Name* field enter `dhcp-hotspot`, in the *Interface* select `bridge-47`, and in the *Address Pool* select `hotspot-pool`. Click OK.
        *   Navigate to *IP* > *DHCP Server* > *Networks* click the "+" button. In the *Address* field enter `90.27.137.0/24`, in the *Gateway* field enter `90.27.137.1` and in the *DNS Servers* enter `8.8.8.8,8.8.4.4`. Click OK.
    *   **Parameter Explanation:**
        *  `/ip dhcp-server add name=dhcp-hotspot`: Defines the name of the DHCP server as `dhcp-hotspot`.
        * `interface=bridge-47`: Selects the interface where DHCP server operates.
        *  `address-pool=hotspot-pool`: Refers to the pool for IP address distribution (see below).
        *  `disabled=no`: Enables the DHCP server.
        *   `/ip dhcp-server network add address=90.27.137.0/24`: Defines the network associated with the DHCP server.
        *   `gateway=90.27.137.1`:  Sets the default gateway IP for the DHCP clients.
        *   `dns-server=8.8.8.8,8.8.4.4`: Specifies Google Public DNS server(s). You can specify your own desired DNS.
        *   `/ip pool add name=hotspot-pool`: Creates an IP address pool named `hotspot-pool`.
        *   `ranges=90.27.137.2-90.27.137.254`: Defines the IP range within the pool that will be assigned to clients, excluding the gateway and broadcast addresses.
    *   **Expected Output (via CLI):** No output if the command runs successfully.
    *   **Post-Step Effect:** Devices connecting to the `bridge-47` interface will now receive IP addresses in the `90.27.137.0/24` subnet, a default gateway, and DNS information.

4.  **Step 4 (Optional): Enable IP Forwarding:**
    *   **Explanation:**  If you expect this Hotspot network to communicate with networks outside of the `90.27.137.0/24` subnet, make sure IP forwarding is enabled. Most likely, this is a requirement in a typical Hotspot network.
    *  **CLI Command:**
       ```mikrotik
        /ip settings set forwarding=yes
       ```
    *  **Winbox GUI:** Navigate to *IP* > *Settings* and check `Enable Forwarding`.
    *  **Parameter Explanation:**
       *  `forwarding=yes`: Enables IP Forwarding.
    *  **Expected Output (via CLI):** No output if the command runs successfully.
    *  **Post-Step Effect:** Router can route packets between interfaces, allowing communication with external networks, such as the internet.

**Complete Configuration Commands:**

```mikrotik
/interface bridge print where name="bridge-47"
/ip address add address=90.27.137.1/24 interface=bridge-47
/ip pool add name=hotspot-pool ranges=90.27.137.2-90.27.137.254
/ip dhcp-server add name=dhcp-hotspot interface=bridge-47 address-pool=hotspot-pool disabled=no
/ip dhcp-server network add address=90.27.137.0/24 gateway=90.27.137.1 dns-server=8.8.8.8,8.8.4.4
/ip settings set forwarding=yes
```

**Common Pitfalls and Solutions:**

*   **Problem:** DHCP server not assigning IPs.
    *   **Solution:**
        *   Check that the DHCP server is enabled (`/ip dhcp-server print`).
        *   Verify that the interface is set correctly (`/ip dhcp-server print`).
        *   Confirm that the IP pool has sufficient addresses and the ranges are correct (`/ip pool print`).
        *   Ensure the `bridge-47` interface is active and not disabled.
        *   Review the `/log` to see if any errors have been logged by the DHCP Server.
*   **Problem:** Clients cannot reach the internet.
    *   **Solution:**
        *   Verify that IP forwarding is enabled (Step 4).
        *   Ensure that you have a default route to the internet (`/ip route print`).
        *   Check your NAT configuration (out of the scope of this specific document, but you must have a NAT configured to use the Internet).
*   **Problem:** Clients are getting incorrect IP address ranges.
    *   **Solution:** Double-check the IP pool `ranges` parameter.
*   **Problem:** High CPU or Memory usage.
    *   **Solution:**
        *   Monitor the router's resource usage via `/system resource print`.
        *   If the resource usage is high, consider implementing QoS settings to control bandwidth usage.

**Security Best Practices:**

*   **Firewall Rules:**
    *   Implement firewall rules to restrict access to the router from the Hotspot network, as well as access to the Hotspot network from outside.
    *   Specifically, block direct access to the router's management interface(s) from the Hotspot network by adding firewall rules that drop traffic from that subnet directed to the router.
*   **DHCP Security:** Limit the size of DHCP pool range and the lease time if required.
*   **Access Control:** Implement user authentication on your network access. This could be RADIUS, Hotspot with user authentication, or other methods.
*   **Regular Updates:** Keep RouterOS updated to patch security vulnerabilities.

**Verification and Testing Steps:**

1.  **Verify IP Address Assignment:**
    *   Connect a device to the `bridge-47` network. Check the assigned IP address. It should be within the `90.27.137.2-90.27.137.254` range and have `90.27.137.1` as the gateway.
2.  **Test Network Connectivity:**
    *   On the connected device, ping the gateway (`90.27.137.1`).
    *   From the router, ping the connected device, from the router terminal:
         ```mikrotik
          /ping 90.27.137.x
         ```
          Where 90.27.137.x is the ip address of a connected device.
    *   If you have an internet connection, try pinging a public IP, such as 8.8.8.8, or an internet host, such as google.com, on the connected device.
3.  **Use MikroTik Tools:**
    *   `ping`: Use the ping tool on the MikroTik router to test connectivity.
    *   `traceroute`: Use `traceroute` from the client or router to check the path to a destination.
    *  `torch`: Use torch to capture and inspect traffic. This can help identify why devices might not be communicating properly.
      ```mikrotik
        /tool torch interface=bridge-47
      ```
      This command will show you live packet capture data.

**Related Features and Considerations:**

*   **Hotspot Feature:** The primary focus of this document was on the IP addressing required for a hotspot.  Consider implementing the built-in MikroTik Hotspot feature for more robust user management.
*   **VLANs:** If you need to isolate Hotspot traffic from other network segments, consider using VLANs.
*   **QoS:** Implement Quality of Service (QoS) to manage bandwidth allocation for your users.
*  **NAT:** NAT configuration is required for this network to reach the internet, however this is outside the scope of this specific document. A basic `/ip firewall nat add chain=srcnat action=masquerade out-interface=[wan-interface]` is usually sufficient, where [wan-interface] is the internet-facing interface of your MikroTik router.

**MikroTik REST API Examples (if applicable):**

This functionality doesn't always have a direct one-to-one mapping in the REST API. However, the following example illustrates how you can add an IP address via the API:

```bash
curl -k -u admin:<password> -H "Content-Type: application/json" \
  -X POST https://<your_router_ip>/rest/ip/address \
  -d '{
        "address": "90.27.137.1/24",
        "interface": "bridge-47"
      }'
```

*   **API Endpoint:** `/rest/ip/address`
*   **Request Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
      "address": "90.27.137.1/24",
      "interface": "bridge-47"
    }
    ```
*   **Expected Response:**
    *   **Success:** HTTP status code `201` or `200` (depending on version).
    *   **Failure:**  HTTP status code `400` or `500`, with error details in the response body.
    *   **Important:** Ensure that the REST API is enabled on your router (`/ip service print` and specifically `/ip service set api enabled=yes`, and `/ip service set api-ssl enabled=yes`).

**Security Best Practices (REST API):**

*   Use HTTPS and a strong username and password or other authentication methods.
*   Restrict API access to specific IPs and/or VLANs using firewall rules.
*   Disable the API if it is not required, and do not expose it to the public internet without additional hardening.

**Self Critique and Improvements:**

*   **Improvements:**
    *   Could add examples for VLAN tagged traffic on `bridge-47` interface.
    *   Could specify more advanced DHCP configurations, such as static leases, or option configuration.
    *   The addition of RADIUS configuration would make this document more useful for real-world large-scale hotspot applications.
*  **Critique:**
     * While this configuration is effective, it needs to be combined with other features (NAT, firewall, internet connectivity) to create a fully functional hotspot solution.
     *  This document provides an excellent starting point for setting up basic IP address management in the context of a hotspot. However, real-world hotspot deployments need to add many additional configurations to ensure smooth operation.

**Detailed Explanations of Topic (IP Settings):**

*   **IP Addresses:** Every device on a network needs a unique IP address for communication. In our case, `90.27.137.1/24` is the IP address assigned to the router on the `bridge-47` interface, which will be the gateway for devices on the Hotspot network.
*   **Subnet Masks:** `/24` means that the first 24 bits of the IP address are used for identifying the network and the remaining bits are used to identify individual hosts on that network. A subnet mask of `/24` translates to `255.255.255.0`.
*   **DHCP Server:** Dynamically assigns IP addresses to client devices, allowing them to connect and use the network without manual IP configuration.
*   **Default Gateway:** The gateway address `90.27.137.1` acts as the door to exit our subnet. All traffic leaving the subnet will pass through the gateway to access the outside world.
*   **DNS Servers:** Translates domain names (like google.com) to IP addresses.

**Detailed Explanation of Trade-offs:**

*  **Static vs Dynamic IP:**
    *   **Static IPs:** Provide predictable addresses, good for servers and devices that require fixed addresses. However, you need manual setup.
    *   **Dynamic IPs (DHCP):** Simplifies network administration but IPs are assigned dynamically and can change.
*   **DHCP Pool Size:**
    *   **Large Pools:** Accommodate many devices, but could also lead to IP exhaustion if the number of devices greatly exceeds pool size.
    *   **Small Pools:** Suitable for networks with fewer devices, but will be problematic if there is a large increase in client devices.
*   **DNS Server Choice:** Using your ISP DNS, Google's Public DNS (8.8.8.8/8.8.4.4), or another provider. Each of these has benefits and draw backs.
    * **ISP DNS:** Can be faster in a region or country, or slower in other regions/countries.
    * **Public DNS:** Often reliable and accessible, but can be slower depending on location and server load.
    * **Local DNS:** If you're hosting your own local services, local DNS can be more efficient.

**Configuration for Specific RouterOS Versions:**

* This configuration is fully compatible with both RouterOS 6.48 and 7.x, which means commands specified in this document will work on both versions.
* If you're using version 7.x the only noticeable differences you may see in the commands are slight changes in the output format.

This documentation is aimed at a seasoned MikroTik user. It's comprehensive, with real-world advice and MikroTik-specific recommendations. It also touches upon essential security aspects of setting up such a network. Remember to adapt it based on your exact requirements, and test the implementation before bringing it live.
