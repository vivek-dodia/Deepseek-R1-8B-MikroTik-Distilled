Okay, let's dive into a detailed technical document for setting up a MAC server on a MikroTik router, targeting RouterOS 6.48 with an SMB network scale, and using the subnet 21.189.236.0/24 on interface `wlan-94`.

## Scenario Description:

We will configure a MikroTik router to act as a MAC server, specifically listening for MAC authentication requests on the `wlan-94` interface. This setup is often used to control network access based on the MAC addresses of devices, allowing granular control over who can connect to the network. This can be used to build a whitelist, a black list, or both.

## Implementation Steps:

Here's a step-by-step guide to implement the MAC server configuration:

### Step 1: Check Interface Status

*   **Before:** Ensure the `wlan-94` interface is enabled and configured correctly. It should have an IP address assigned within the 21.189.236.0/24 subnet (or be set up as a bridge for layer2 switching) and be up and running.
*   **Action:** Use the following command to check the interface status via CLI:

    ```mikrotik
    /interface wireless print where name="wlan-94"
    /ip address print where interface="wlan-94"
    ```
*   **Expected Result:** You should see output showing the `wlan-94` interface details and associated IP address. If the interface is disabled, use command `/interface wireless enable wlan-94`

### Step 2: Enable the MAC Server on the WLAN Interface

*   **Before:** The MAC server is disabled by default, we must enable it for the target interface.
*   **Action:** Enable the MAC server on the `wlan-94` interface.
    ```mikrotik
    /interface wireless set wlan-94 mac-address-server=yes
    ```
*   **Expected Result:** After this command, the router will now listen for MAC address authentication requests on `wlan-94`. You can verify this using the command `/interface wireless print where name="wlan-94"` and observe the change in the `mac-address-server` flag.

### Step 3: Configure Access List (Optional, but recommended)

*   **Before:** Without a configured access list, the MAC server doesn't filter access. We are going to use a list of permitted addresses.
*   **Action:** Create a whitelist for allowed MAC addresses. You can use this command to add one MAC at the time.

    ```mikrotik
    /interface wireless access-list add mac-address=XX:XX:XX:XX:XX:XX interface=wlan-94
    ```
    *Where `XX:XX:XX:XX:XX:XX` represents the desired MAC address*. Repeat the command for every allowed device.
*   **Expected Result:** Only the MAC addresses you added to the access list will be allowed to connect to your access point via `wlan-94`.
*   **GUI Instruction** You can also do this via Winbox, by opening Wireless, click on the Wireless tab, double click your wlan interface, click on the "Access List" tab, then click the "+" button to add the MAC address.

### Step 4: Monitor Connections (Optional)

*   **Before:** You want to see that the MAC authentication is working
*   **Action:** Monitor the active wireless registrations on the `wlan-94` interface.
    ```mikrotik
    /interface wireless registration-table print where interface="wlan-94"
    ```

*   **Expected Result:** Output should show the MAC address of the currently connected devices. If you are not using a whitelist, all authenticated devices will show up. If you are, only the devices on the access list will show up.

## Complete Configuration Commands:

Here's the complete set of commands to implement the configuration:

```mikrotik
# Ensure wlan-94 is enabled and an IP is assigned
/interface wireless print where name="wlan-94"
/ip address print where interface="wlan-94"
# Enable MAC Server on wlan-94
/interface wireless set wlan-94 mac-address-server=yes
# Add MAC Addresses to the Access List (repeat for each device)
/interface wireless access-list add mac-address=00:11:22:33:44:55 interface=wlan-94
/interface wireless access-list add mac-address=AA:BB:CC:DD:EE:FF interface=wlan-94

# (Optional) Check the wireless table to see active connection
/interface wireless registration-table print where interface="wlan-94"
```

**Parameter Explanations:**

| Command                             | Parameter          | Description                                                                                                                                                                                            |
|-------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/interface wireless set`           | `wlan-94`          | Specifies the name of the wireless interface to configure.                                                                                                                                    |
|                                     | `mac-address-server` | Enables or disables the MAC server functionality (`yes` to enable).                                                                                                                                 |
| `/interface wireless access-list add` | `mac-address`      | The MAC address of the device to be added to the access list. Use this to create a whitelist.  It should be in the format XX:XX:XX:XX:XX:XX                                                    |
|                                     | `interface`       | The wireless interface this access list applies to.                                                                                                                                        |
|`/interface wireless registration-table print`    | `where interface` | Filters the output to show registrations only on specified interface                                                                                                                       |

## Common Pitfalls and Solutions:

*   **Problem:** MAC server not working.
    *   **Solution:** Double check that the interface is enabled, and that the flag `mac-address-server` is set to yes.
*   **Problem:** Clients cannot connect.
    *   **Solution:** Verify that the MAC address of the client is in the access list, and that it is typed correctly. Double-check that your client adapter is broadcasting the correct mac address, sometimes clients have multiple mac addresses.
*   **Problem:**  Router CPU/Memory spikes with many connected clients.
    *   **Solution:** The MAC server functionality itself is light. If resource usage increases dramatically, monitor other services like NAT, Firewall rules, or other wireless interfaces. You can also upgrade your router hardware if it is not coping well with the load.

**Security Issues:**
*   MAC addresses can be spoofed. Consider using additional security measures alongside MAC filtering.
*   Expose the access list might allow a hacker to find a MAC address that is on the list, and then use it.

## Verification and Testing Steps:

1.  **Client Connection:** Attempt to connect a client to the `wlan-94` network. Check that only allowed clients (from the access list) can connect.
2.  **Registration Table:** Use `/interface wireless registration-table print where interface="wlan-94"` to verify connected clients and their associated MAC addresses. The table output will show the actual connected devices and their associated MAC Address, allowing you to check if the access list is working as expected.
3.  **Packet Sniffing:** Use Torch (`/tool torch interface=wlan-94`) to capture network traffic and verify that authentication is working correctly. You can capture different authentication packets as clients try to connect.

## Related Features and Considerations:

*   **RADIUS Authentication:** Instead of just MAC authentication, you could use a RADIUS server for a more robust and centralized user management system.
*   **Dynamic Access Lists:** You can script the access lists to dynamically update based on other parameters, such as time, client activity, etc.
*   **Wireless Security:**  MAC filtering should be combined with a strong wireless encryption method (WPA2 or WPA3).

## MikroTik REST API Examples (if applicable):

While MikroTik doesn't offer direct REST API endpoints to manage the MAC server flag in the interface settings. You can manage the access list through the API.

**API Endpoint:**
`/interface/wireless/access-list`

**Example: Adding an entry to the access list:**

*   **Method:** POST
*   **Payload (JSON):**

    ```json
    {
        "mac-address": "00:11:22:33:44:55",
        "interface": "wlan-94"
    }
    ```
*   **Expected Response (Success):**

    ```json
    {
        "message": "added",
        "id": "*1"
    }
    ```
*   **API Call Example with curl:**
    ```bash
    curl -k -u admin:yourpassword -H "Content-Type: application/json" -d '{"mac-address": "00:11:22:33:44:55","interface": "wlan-94"}' https://your_router_ip/rest/interface/wireless/access-list
    ```

**Example: Deleting an entry from the access list:**

*   **Method:** DELETE
*   **Payload (JSON):**

    ```json
        {"id": "*1"}
    ```
*   **Expected Response (Success):**

    ```json
    {
        "message": "removed",
         "id": "*1"
    }
    ```
*   **API Call Example with curl:**
    ```bash
    curl -k -u admin:yourpassword -H "Content-Type: application/json" -X DELETE -d '{"id": "*1"}' https://your_router_ip/rest/interface/wireless/access-list
    ```

**Error Handling:**
*   If you try to add an existing MAC address, the API will return a 400 error.
*   If the API request fails due to authentication, the server will return an HTTP 401 error.
*   Error handling should include looking for HTTP error codes and the `message` field in the response.

**Parameter Explanations:**
*   `mac-address`: This is the Mac Address in the format XX:XX:XX:XX:XX:XX
*   `interface`:  This is the name of the interface that the access list will be applied to.
*  `id`: The unique ID of the record you are going to delete or modify

## Security Best Practices:

*   **Strong Passwords:** Use strong and unique passwords for your router's admin accounts.
*   **Disable Default Accounts:** Disable default accounts like `admin`.
*   **Firewall Rules:** Implement firewall rules to limit access to your router's management interface.
*   **Keep RouterOS Updated:** Keep your router's firmware up to date to patch security vulnerabilities.

## Self Critique and Improvements:

This configuration is a good basic implementation of a MAC server.
*   **Improvements:** For better security, using RADIUS authentication is preferred.
*  **Dynamic Access Lists:** Implementing dynamic access lists can increase security, and create a better user experience.

## Detailed Explanations of Topic

The MAC server functionality in MikroTik routers acts as a basic authentication mechanism at the layer 2 level. When you enable the MAC server on an interface, the router will keep a list of clients connected, and this list can be filtered using the access list. The Router checks the client's MAC address against this list, thus allowing or disallowing network access to specific devices.

## Detailed Explanation of Trade-offs:

*   **MAC Filtering vs. RADIUS:** MAC filtering is simple but easily bypassed by MAC spoofing. RADIUS authentication is more secure and offers better management control. The trade-off is complexity.
*   **Whitelisting vs. Blacklisting:** Whitelisting (allowing specific MAC addresses) is more secure than blacklisting (blocking specific MAC addresses). Blacklisting can be exhaustive and may not stop an attacker if you forget to add their MAC to the list.
*   **Static Access Lists vs. Dynamic Access Lists:** Static access lists are easier to manage, but require manual updates, they are not suitable for a changing environment. Dynamic access lists require scripting but offer more automation, security and flexibility.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS versions 6.48 and 7.x as the core MAC server features haven't changed significantly. However, always check the RouterOS release notes for any specific changes in behaviour or syntax.

This comprehensive document should provide a solid foundation for understanding and implementing MAC server functionality on your MikroTik router.
