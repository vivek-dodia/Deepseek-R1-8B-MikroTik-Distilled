Okay, let's dive into creating a detailed technical document for a MikroTik MAC server configuration targeting RouterOS 7.12 within an ISP network environment, specifically focusing on subnet 22.101.190.0/24 on the interface `vlan-66`.

## Scenario Description:

This scenario addresses the requirement of a MikroTik router to act as a MAC server for a specific VLAN. This is typical in ISP networks where the router needs to respond to MAC address discovery requests (like ARP requests) within the specified subnet. This service can be used to implement DHCP relay, proxy ARP or other applications. Our example scenario focuses on the ISP providing an ip via DHCP with the need to listen for the DHCP request over an already configured VLAN.

## Implementation Steps:

Here is a step-by-step guide to configuring the MAC server:

1. **Step 1: Verify the VLAN interface and IP configuration**

    *   **Goal:** Ensure the `vlan-66` interface exists and has a correctly configured IP address in the specified subnet (22.101.190.0/24).
    *   **Before:** Assume the VLAN interface is already created and potentially unconfigured.
    *   **Action:** We'll verify and add the IP address to the `vlan-66` interface if necessary.

    *   **CLI Commands:**

        ```mikrotik
        /interface vlan print
        /ip address print
        ```

        **Example Output (Before)**
         ```
        Flags: X - disabled, R - running
         0  R name="vlan-66" mtu=1500 l2mtu=1598 vlan-id=66 interface=ether1
            
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        ```

        **Note:** Based on the above output, there is no ip address associated with the vlan interface.

    *   **CLI Command (Adding IP Address):**

        ```mikrotik
        /ip address add address=22.101.190.1/24 interface=vlan-66
        ```
    *   **After:** The output will show a new entry with the IP address assigned to the vlan interface

        **Example Output (After)**
         ```
        Flags: X - disabled, R - running
         0  R name="vlan-66" mtu=1500 l2mtu=1598 vlan-id=66 interface=ether1
        
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   22.101.190.1/24    22.101.190.0     vlan-66
        ```
    *   **Winbox GUI:** Navigate to `IP` -> `Addresses` and add a new address.
        *   Address: 22.101.190.1/24
        *   Interface: `vlan-66`

2. **Step 2: Configure the MAC server on the vlan interface.**

    *   **Goal:** Enable the MAC server functionality on the `vlan-66` interface.
    *   **Before:** The MAC server is not active on the interface.
    *   **Action:** Use the `/interface vlan set mac-server` command to enable the mac server on our interface.

    *   **CLI Command:**

        ```mikrotik
        /interface vlan set vlan-66 mac-server=yes
        ```

    *   **After:** The mac-server property will now be set to yes, indicating that the mac server is active on the `vlan-66` interface.

        **Example Output:**
        ```
        Flags: X - disabled, R - running
         0  R name="vlan-66" mtu=1500 l2mtu=1598 vlan-id=66 interface=ether1 mac-server=yes
        ```

    *   **Winbox GUI:** Navigate to `Interfaces`, double-click on `vlan-66`, and enable `MAC Server`

## Complete Configuration Commands:

```mikrotik
/ip address add address=22.101.190.1/24 interface=vlan-66
/interface vlan set vlan-66 mac-server=yes
```

**Parameter Explanations:**

| Command           | Parameter           | Explanation                                                                |
| ----------------- | ------------------- | -------------------------------------------------------------------------- |
| `/ip address add` | `address`           | IP address and subnet mask in CIDR notation (e.g., 22.101.190.1/24)         |
|                   | `interface`         | The interface this IP address is assigned to (`vlan-66`)                   |
| `/interface vlan set` | `mac-server` | Enable MAC server on the interface. Values:  `yes` or `no`.         |
|                   | `vlan-66` | The specific vlan interface to apply the changes to.         |

## Common Pitfalls and Solutions:

*   **Problem:**  IP address is not on the interface, or is incorrectly configured.
    *   **Solution:** Double-check the `/ip address print` output and correct any mistakes using `/ip address set`.
*   **Problem:** The interface is disabled.
    *   **Solution:** Enable the interface by using the CLI command `/interface enable vlan-66`, or via the Winbox GUI, under the Interface menu.
*   **Problem:** MAC server does not respond.
    *   **Solution:** Ensure the interface is active, and confirm that other networking devices are correctly configured to send requests to this subnet. Review firewall rules.

## Verification and Testing Steps:

1.  **Check interface status:** Use `/interface print` to confirm the `vlan-66` interface is running (`R` flag) and mac-server is enabled.
2.  **Monitor ARP table:** You should be able to see the router in the client ARP table, with the associated ip address.
    *   Use `/ip arp print`
    *  You might not see the server's mac address in the arp table if no request has been sent for this device's ip. Send a ping to 22.101.190.1 and then verify the arp table.
3.  **Ping Test:** If you have a device on the same VLAN, ping the router's IP address. If the ping works, the mac server is functioning correctly.
    *   Use `/ping 22.101.190.1`
4. **Torch:** You can use `/tool torch interface=vlan-66` to see the ARP traffic on the interface, ensuring that ARP requests are being received and replied to.

## Related Features and Considerations:

*   **Proxy-ARP:** Using Proxy-ARP is not required in this scenario as we only focus on enabling the mac server. In some other cases you might want to combine the mac-server with proxy-arp to be able to resolve mac-addresses for machines outside the local subnet.
*   **DHCP Relay:** This MAC server configuration is typically used in conjunction with a DHCP relay to forward DHCP requests to a DHCP server on another network.
*   **Firewall Rules:** Be mindful of firewall rules that might block ARP traffic or related protocols.
*   **Logging:** Monitor logs for any errors or unexpected behavior relating to mac-server functionality.
*   **Bridge:** The interface in this configuration does not have to be a VLAN interface, it could be a bridge interface. If the interface is a bridge, make sure the correct ports are part of the bridge, as well as the correct interfaces to forward the traffic.

## MikroTik REST API Examples (if applicable):

Here are some examples, using the latest version of RouterOS API.

1.  **Enable MAC Server on a VLAN Interface:**

    *   **API Endpoint:** `/interface/vlan`
    *   **Request Method:** `PATCH`
    *   **Example JSON Payload:**

        ```json
        {
            ".id": "vlan-66",
            "mac-server": "yes"
        }
        ```

    *   **Expected Response (200 OK):** Empty or confirming the change.

    *   **Error Handling:** 400 (bad request), 404 (not found)

2.  **Get information for all interfaces (you can filter for VLANs)**

    *   **API Endpoint:** `/interface/vlan`
    *   **Request Method:** `GET`
    *   **Expected Response (200 OK):**
    ```json
        [
            {
                "name": "vlan-66",
                "mtu": "1500",
                "l2mtu": "1598",
                "vlan-id": "66",
                "interface": "ether1",
                "mac-server": "yes",
                "disabled": "false",
                "actual-mtu": "1500",
                "max-l2mtu": "1598"
            }
        ]
    ```

## Security Best Practices

*   **Limit Interface Access:** Restrict access to the router's management interface, and limit which machines can send arp requests to this interface.
*   **Firewall Rules:** Implement strong firewall rules to prevent unauthorized access to the router's interfaces.
*   **Regular Audits:** Regularly audit and review your network configurations, including this mac-server setup.
*   **Access Control:** Limit access to the router and its configuration using strong passwords and access lists.
*   **Logging:** Enable and monitor logs for any suspicious activity.

## Self Critique and Improvements

This configuration provides a basic MAC server setup. Possible improvements include:
*   **Address List Filtering:** Filter to only respond to arp request from machines in the address-list. This allows only certain devices to be resolved by the mac server
*   **Integration with DHCP:** Integrate with DHCP server for more dynamic IP assignment with the help of dhcp relay functionality.
*   **Monitoring:** Add more detailed monitoring to track traffic patterns related to the mac server.
*   **Documentation:** Document the mac-server usage to reduce confusion when other network changes happen.
*   **Advanced Firewall rules:** More complex rules can be added to prevent unauthorized access to the network.

## Detailed Explanations of Topic

The MAC server in MikroTik RouterOS is a function that listens on the specified interfaces for Ethernet MAC address discovery requests, typically ARP (Address Resolution Protocol) requests. In a standard IP network setup, when a device wants to communicate with another device, it needs to know the destination IP address and the destination MAC address. If the device does not know the destination's MAC address, it sends an ARP request which is a broadcast message asking "Who has this IP address?" The MAC server on the RouterOS device listens for these requests and, if it matches its internal configuration, responds with the appropriate MAC address.

The mac server helps the network devices find the mac address for a given IP address and allows machines to communicate. If a device does not know the MAC address of a destination, it will not be able to properly communicate. The router is acting as a gate keeper, and needs to be configured to respond to these requests to avoid communication issues.

## Detailed Explanation of Trade-offs

*   **mac-server vs. Proxy ARP:**  While both features can serve to resolve mac addresses, they function in different ways. The mac-server functionality responds to arp requests on that interface only. Proxy-arp responds to requests on other interfaces as well. Use cases include: mac-server is usually for an interface/vlan that you want to manage. Proxy-arp is usually used to communicate over different subnets.
* **Complexity vs. Functionality:** Using the mac server adds complexity to the router configuration. If you don't need to use mac server, disabling it simplifies the configuration and could reduce resource utilization.
*   **Security Trade-off:** While the mac server facilitates communication between machines in the same subnet, it is important to apply proper security measures to prevent attacks over the network. Using filtering by address-lists can reduce the attack surface and increase the security.

## Configuration for Specific RouterOS Versions:

This configuration works for RouterOS 7.x and later, including version 7.12. The core functionality and commands for `mac-server` have remained consistent in recent versions. The API calls also work in the latest version of RouterOS.

This detailed documentation should provide a solid foundation for implementing and understanding the MAC server feature on MikroTik RouterOS. Remember to adapt the specifics to your unique network environment and requirements.
