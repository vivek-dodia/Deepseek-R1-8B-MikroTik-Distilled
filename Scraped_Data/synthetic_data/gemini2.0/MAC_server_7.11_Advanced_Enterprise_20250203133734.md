Okay, let's dive into a detailed configuration for a MAC server on a MikroTik router, specifically targeting RouterOS 7.11 with an enterprise-level network in mind.

## Scenario Description:

This scenario involves setting up a MAC server on a MikroTik router (RouterOS v7.11) connected to a VLAN interface (vlan-29) within the enterprise network. The MAC server will allow MAC addresses to be used as an authentication method for network access, in conjunction with the specified subnet 91.237.222.0/24. This is typically useful for systems where traditional usernames/passwords might be cumbersome, or to restrict access by MAC address (similar to MAC filtering on a switch but implemented on the router itself, to be useful, the clients using the MAC authentication must be in a directly connected network segment).  This approach is primarily used in hot-spot environments, or in less common cases for point-to-point links or other specific network use cases.

## Implementation Steps:

Here is a step-by-step guide on how to configure the MAC server:

1.  **Step 1: Configure the VLAN Interface**

    *   **Explanation:** We assume that you already have VLAN tagging configured on the parent interface for `vlan-29` which is typically used on an enterprise infrastructure. Before we begin, we need to check the existence and status of the `vlan-29` interface and the interfaces connected to it. If the vlan interface does not exist, create it. We must also confirm that there is a physical interface associated with this vlan.

    *   **Before:** (Example of checking existing interfaces)

        ```mikrotik
        /interface print
        ```
        *Example output*

        ```
        Flags: D - dynamic ; R - running
        #    NAME                                TYPE      MTU   L2MTU MAX-L2MTU
        0  R ether1                              ether     1500  1598   4076
        1  R ether2                              ether     1500  1598   4076
        2  R ether3                              ether     1500  1598   4076
        3  R ether4                              ether     1500  1598   4076
        4    ether5                              ether     1500  1598   4076
        ```

        If `vlan-29` is not present, we will proceed to create it. If the interface exists we can move to the next step.
    *   **Command:** (CLI - Creating vlan interface - we will assume `ether1` is our parent interface)

        ```mikrotik
        /interface vlan add interface=ether1 name=vlan-29 vlan-id=29
        ```
    *   **After:**
        ```mikrotik
         /interface print
        ```
        *Example output*

        ```
        Flags: D - dynamic ; R - running
        #    NAME                                TYPE      MTU   L2MTU MAX-L2MTU
        0  R ether1                              ether     1500  1598   4076
        1  R ether2                              ether     1500  1598   4076
        2  R ether3                              ether     1500  1598   4076
        3  R ether4                              ether     1500  1598   4076
        4    ether5                              ether     1500  1598   4076
        5  R vlan-29                             vlan      1500  1598   4076
        ```
        This confirms the vlan interface was correctly created.

    *   **GUI:** Navigate to `Interfaces`, then `+` and choose `VLAN`. Configure parent interface (e.g. ether1) and vlan id to 29 and give it the name `vlan-29`.
2.  **Step 2: Configure IP Address on VLAN Interface**

    *   **Explanation:**  The MAC server needs an IP address on the same subnet it will be serving. We assign an IP address from the 91.237.222.0/24 subnet to the vlan-29 interface.
    *   **Before:**

        ```mikrotik
        /ip address print
        ```
        *Example output*:

        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        ```
        We can see there are no IP addresses configured on any interfaces.

    *   **Command:** (CLI)

        ```mikrotik
        /ip address add address=91.237.222.1/24 interface=vlan-29
        ```
    *   **After:**

        ```mikrotik
        /ip address print
        ```
        *Example output*

        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   91.237.222.1/24    91.237.222.0    vlan-29
        ```
        We can confirm that the address was assigned correctly to the vlan interface.
    *   **GUI:** Navigate to `IP`, then `Addresses`. Click `+` and add the IP address `91.237.222.1/24`, choosing `vlan-29` as the interface.
3.  **Step 3: Configure the MAC Server**

    *   **Explanation:** We enable the MAC server on the `vlan-29` interface. This will enable the use of MAC address authentication for the clients connected to this segment.
    *   **Before:**

        ```mikrotik
        /ip hotspot mac-server print
        ```
        *Example output:*

        ```
        Flags: X - disabled, I - invalid
        #   INTERFACE  PROFILE  ADDRESS-LIST
        ```

    *   **Command:** (CLI)

        ```mikrotik
        /ip hotspot mac-server add interface=vlan-29 disabled=no
        ```
    *   **After:**

        ```mikrotik
        /ip hotspot mac-server print
        ```
        *Example output:*

        ```
        Flags: X - disabled, I - invalid
        #   INTERFACE  PROFILE  ADDRESS-LIST
        0   vlan-29    default
        ```

    *  **GUI:** Navigate to `IP` then `Hotspot`. Select the `MAC Servers` tab. Click `+` to add an entry. Select the `vlan-29` interface, and leave the profile set to `default`. Ensure `Disabled` is not selected.

4.  **Step 4: Configure Allowed MAC Addresses**

    *   **Explanation:** We add the MAC addresses that are allowed to connect. We must add these to the `mac-address` list. For example, let's allow two MAC addresses: `00:11:22:33:44:55` and `AA:BB:CC:DD:EE:FF`.

    *   **Before:**

         ```mikrotik
         /ip hotspot mac-address print
         ```
         *Example output:*

         ```
         Flags: X - disabled, D - dynamic
         #   MAC-ADDRESS        SERVER       TO-ADDRESS         COMMENT
         ```
    *   **Command:** (CLI)
        ```mikrotik
        /ip hotspot mac-address add mac-address=00:11:22:33:44:55 server=vlan-29 comment="Device 1"
        /ip hotspot mac-address add mac-address=AA:BB:CC:DD:EE:FF server=vlan-29 comment="Device 2"
        ```
    *   **After:**
        ```mikrotik
        /ip hotspot mac-address print
        ```
        *Example output:*

        ```
        Flags: X - disabled, D - dynamic
        #   MAC-ADDRESS        SERVER       TO-ADDRESS         COMMENT
        0   00:11:22:33:44:55  vlan-29                        Device 1
        1   AA:BB:CC:DD:EE:FF  vlan-29                        Device 2
        ```

    *   **GUI:** Navigate to `IP` then `Hotspot`. Select the `MAC Addresses` tab. Click `+` to add the devices MAC address, select the server to `vlan-29` and add a comment for future reference. Repeat for other MAC addresses allowed.

## Complete Configuration Commands:

Here are the complete MikroTik CLI commands to implement this setup:

```mikrotik
/interface vlan add interface=ether1 name=vlan-29 vlan-id=29
/ip address add address=91.237.222.1/24 interface=vlan-29
/ip hotspot mac-server add interface=vlan-29 disabled=no
/ip hotspot mac-address add mac-address=00:11:22:33:44:55 server=vlan-29 comment="Device 1"
/ip hotspot mac-address add mac-address=AA:BB:CC:DD:EE:FF server=vlan-29 comment="Device 2"

```

## Common Pitfalls and Solutions:

*   **Problem:**  Clients cannot connect even if the MAC address is listed.

    *   **Solution:**  Check that the interface on the client is sending packets with a valid source MAC address (that is included in the list), the IP subnet on the clients interface is within `91.237.222.0/24` and that there are no other access restriction rules active on the router that are preventing the clients from reaching the router. Use the `/tool sniffer quick interface=vlan-29` to view network traffic, and make sure the client MAC address matches the expected. If no packets are seen with the clients MAC address, that means there are issues with the client configuration, not the MikroTik router.

*   **Problem:** `mac-server` settings or `mac-address` settings are not applied or not working.

    *   **Solution:**  If you change the MAC server settings, you can restart the service using command `/ip hotspot mac-server enable numbers=0` and then `disable`. Another workaround is to create a new server with the correct settings. You can verify the settings by inspecting the `/ip hotspot mac-server print` command. Also make sure the client MAC is added on the `mac-address` list, and that the MAC address is correctly entered.

*   **Problem:** IP address conflict

    *   **Solution:** Confirm that the IP address of the vlan interface does not conflict with other devices on the network. If the devices are manually assigned addresses, there is a chance an address conflict can occur if that IP address is not reserved for the router.

*   **Security Issue:**  MAC spoofing.
    *   **Solution:**  MAC address authentication is **not a robust security measure**.  It can be easily bypassed by spoofing MAC addresses. Implement stronger authentication methods if security is critical. This method is best used for devices that are difficult to use with more common methods of authentication, or when there is a desire to ensure only specific devices are able to connect.

*   **Performance:** High CPU usage from the MAC server.
    *   **Solution:** Although not common with a moderate amount of devices, a high number of entries in the `mac-address` list may cause high CPU usage. If you need to configure a large number of devices you should look for an alternative method. Avoid excessive use of this feature.

*  **Resource Issue:** The number of clients is higher than supported.
    * **Solution:** While RouterOS can handle a large amount of clients in general, this particular solution is not optimal for a high number of clients. For a high number of clients, consider a more dedicated solution such as a centralized RADIUS server, or consider using DHCP options, where clients can be assigned static IPs based on their MAC address, without using the mac server.

## Verification and Testing Steps:

1.  **Client Connection:**
    *   Connect a client device with a permitted MAC address to the network behind the `vlan-29` interface.
    *   The client should receive an IP address within the 91.237.222.0/24 subnet.

2.  **Ping Test:**
    *   From the client, ping the router's IP address (91.237.222.1).
        ```
        ping 91.237.222.1
        ```
    *   From the router, use the ping tool to ping the client IP address, the client should be reachable by the router.
        ```mikrotik
        /ping 91.237.222.x count=4
        ```

3.  **Torch:**
    *   Use the Torch tool on the MikroTik router (e.g., `/tool torch interface=vlan-29`) to view traffic from the client's MAC address when the client is attempting to connect, to ensure the packets are being received by the router and processed correctly. If packets are not being received, that can indicate problems with the physical connections, or the client itself.

4.  **Check Active MAC Connections:**
    *   Verify active MAC connections with `/ip hotspot active print`.

5.  **Check MAC Address List:**
    *   Ensure that the allowed MAC address is listed correctly using `/ip hotspot mac-address print`.

## Related Features and Considerations:

*   **Hotspot Profiles:** Although a "default" profile is being used in this example,  the MAC server can use different hotspot profiles which could be used for a more complex configuration, where a RADIUS server can be used for accounting. The default profile does not have any advanced settings configured, but this can be used as a simple MAC address based authentication tool.
*   **Address Lists:** Using the `address-list` parameter on the MAC server allows for more complex ACLs. A named address list can be configured with the permitted MAC addresses, this method is not ideal due to the amount of steps needed to configure it, and it does not improve the overall configuration. This method can only be used when `mac-address` list is not in use.
*   **MAC-address static table**: When MAC address is used to assign IPs via DHCP, use the `ip dhcp-server lease` table to manage DHCP settings with the mac-address, including reservation of IPs.
*   **Static IP Assignment:**  While MAC address authentication can control access, the IP address that clients get can be based on the DHCP server settings. To make sure clients consistently receive the same IP address, consider setting up DHCP static leases based on the MAC address. This will simplify the network addressing for the clients.
*   **IP Bindings:** Similar to a static DHCP assignment, IP addresses can be permanently bound to specific mac addresses. This is often used for non-dhcp services.

## MikroTik REST API Examples (if applicable):

Here are examples using the RouterOS REST API:

*   **Add a MAC address:**

    *   **Endpoint:** `/ip/hotspot/mac-address`
    *   **Method:** `POST`
    *   **Request Body (JSON):**
        ```json
        {
          "mac-address": "00:11:22:33:44:66",
          "server": "vlan-29",
          "comment": "Device 3"
        }
        ```
    *   **Expected Response:**
        ```json
        {
          ".id": "*1",
           "mac-address": "00:11:22:33:44:66",
           "server":"vlan-29",
           "to-address":null,
           "comment":"Device 3"
        }
        ```
    *   **Error Handling:**  If the server name does not exist you will receive a 500 error with message `invalid value for argument server`
*   **Read MAC address configurations:**

    *   **Endpoint:** `/ip/hotspot/mac-address`
    *   **Method:** `GET`

    *   **Request Body (JSON):** (Empty)
    *   **Expected Response:**
      ```json
        [
         {
           ".id": "*1",
           "mac-address": "00:11:22:33:44:55",
           "server":"vlan-29",
           "to-address":null,
           "comment":"Device 1"
         },
         {
           ".id": "*2",
           "mac-address": "AA:BB:CC:DD:EE:FF",
           "server":"vlan-29",
           "to-address":null,
           "comment":"Device 2"
         },
          {
           ".id": "*3",
           "mac-address": "00:11:22:33:44:66",
           "server":"vlan-29",
           "to-address":null,
           "comment":"Device 3"
         }
       ]
      ```

*   **Enable or Disable MAC server:**

    *   **Endpoint:** `/ip/hotspot/mac-server`
    *   **Method:** `PATCH`
    *   **Request Body (JSON) Example (Disable):**

        ```json
        {
          ".id":"*0",
          "disabled": true
        }
        ```
    *   **Request Body (JSON) Example (Enable):**

        ```json
        {
          ".id":"*0",
          "disabled": false
        }
        ```
    *   **Expected Response:**
    ```json
       {
           "interface": "vlan-29",
           "profile": "default",
           "address-list": null,
           "disabled": false,
           ".id": "*0"
       }
   ```
    *  **Error Handling:** If you include properties not available to be edited, you will receive a 500 error with a message similar to `property interface is not writable`

## Security Best Practices:

*   **MAC Filtering is Weak:**  As stated before, do not rely solely on MAC address authentication for security. This method is easy to bypass. Always use stronger authentication methods in conjunction with MAC address authentication when necessary.
*   **Regular Review:** Review the MAC address list periodically and remove any MAC addresses that are no longer authorized.
*   **Limit Access:**  Use firewall rules and address lists to further limit access even when clients are successfully connected by the MAC server. The address list feature is less versatile than the MAC address list, it should be avoided when possible.
*   **Physical Security:** Secure your router to prevent physical access, as a compromised router can make all other security measures irrelevant.
*  **RouterOS Updates:** keep your RouterOS version updated, as this will ensure all potential vulnerabilities are resolved and the router operates at optimal levels.

## Self Critique and Improvements

*   **Complexity:** The current solution is very basic and only suitable for a simple use case. For an enterprise environment this can be improved with an external RADIUS server, that can be used to ensure device authentication, accounting, and even more granular access control.
*  **Scalability:** This approach is not scalable. Every new device needs to be added manually, which is not practical for a large deployment. If this must be used, automate it using the API.
*   **Security:** MAC address filtering alone is not a security solution. Combining this with better authentication methods (like 802.1x with a RADIUS server) would be a significant improvement. The current solution should only be used in specific scenarios, or to simply restrict access for a few devices.
*   **Management:** A better management method should be implemented for this solution. For instance, an external database can be used to maintain a list of devices that should be allowed to connect.

## Detailed Explanations of Topic

*   **MAC Server:** A MAC server on a MikroTik router allows devices to connect to a network if their MAC address is configured on the router as an allowed address. It essentially acts as a basic form of device authentication.
*   **Hotspot (MAC Server):** MikroTik's Hotspot functionality includes the MAC server option, although it does not require the other features of the hotspot (such as captive portal and login pages). The MAC server just uses the MAC address as a way to authenticate, and a simple and basic access control measure.
*   **MAC Address List:** The MAC address list on a MikroTik device is where authorized MAC addresses are added that can connect to the network when the MAC server is enabled. Each entry in the MAC address list can be associated with a specific MAC Server.
*  **VLAN interfaces:** VLAN interfaces are used to separate network traffic into different logical segments. Each VLAN interface has its own settings that can be configured.

## Detailed Explanation of Trade-offs

*   **MAC vs. RADIUS Authentication:**  MAC authentication is simpler to set up, but RADIUS is more secure, scalable, and flexible. RADIUS provides advanced accounting and authorization features, while the MAC Server is a simpler and less configurable solution.
*   **Static IPs vs. DHCP:** Static IP assignments can be simpler to manage if the number of devices is small. However, DHCP is better for dynamic network changes, especially in larger environments. Using DHCP will ensure the device receives an IP address, but if static addresses are required, a DHCP reservation is more practical.
*   **Local Authentication vs. External:**  Local authentication on the router is simpler but less scalable. Using an external authentication server such as a RADIUS server can centralize the management and improve the configuration and flexibility, allowing a consistent and manageable authentication process, especially when more complex settings must be applied to the clients.

## Configuration for Specific RouterOS Versions:

The above configuration is for RouterOS 7.11. The same commands are applicable for older versions of 7.x and 6.48.

---

This comprehensive documentation should provide a solid foundation for configuring a MAC server in your MikroTik environment. Let me know if you have any other questions or scenarios you want me to cover!
