Okay, let's dive into a detailed technical documentation for configuring a MAC server on MikroTik RouterOS 7.12, specifically focusing on a SOHO environment, the subnet 141.5.98.0/24, and interface `ether-27`.

## Scenario Description:

This document details setting up a MAC server on a MikroTik router. This server will listen on interface `ether-27` for MAC address-based requests. This is particularly useful for scenarios where devices need to obtain IP addresses or be identified by their MAC addresses rather than just IP addresses, possibly alongside or instead of DHCP. This is useful for assigning static IP addresses to devices based on MAC address, for rate limiting, or other services where devices need to be distinguished by their MAC addresses. In a SOHO environment, this might be used for simplifying the management of devices with known MAC addresses.

## Implementation Steps:

### Step 1: Verify Interface Status

Before configuring the MAC server, it’s crucial to verify that interface `ether-27` exists and is in the correct state (e.g., enabled).

*   **Before:** No MAC server configuration exists.
    ```
    /interface print
    ```
*   **Explanation:** We're using the `/interface print` command to list all network interfaces. We'll confirm that `ether-27` is present, enabled and ready for the MAC server to listen on it.
*   **CLI Example:**
    ```
    /interface print
     Flags: D - dynamic ; X - disabled
      #    NAME                                TYPE      MTU  L2MTU   MAX-L2MTU
      0  R ether1                              ether     1500  1598    10236
      1    ether2                              ether     1500  1598    10236
      ...
     26    ether27                             ether     1500  1598    10236
    ```
*   **Winbox GUI:** Navigate to *Interfaces*. Look for interface `ether-27` and make sure it's enabled (no "X" flag).
*   **After:**  Interface `ether-27` exists, is enabled and ready to accept connections.

### Step 2: Enable MAC Server on the Interface

Now, we enable the MAC server functionality on the specified interface.

*   **Before:** MAC server is disabled.

*   **Explanation:** We are going to use the `/interface mac-server` command to enable MAC server on ether-27. The command's `add` function adds a new interface for the mac-server to listen on, and the `interface=ether-27` parameter specifies that we only care about MAC requests coming in over interface ether-27.

*   **CLI Example:**
    ```
    /interface mac-server add interface=ether-27
    ```
*   **Winbox GUI:** Go to *Interfaces* -> *MAC Server*, click the '+' button. Select `ether-27` under the "Interface" dropdown menu.
*   **After:** The MAC server is enabled on interface `ether-27` but with no specific rules yet.
*   **Note:** This command activates a MAC server on the interface, but does not define any service, therefore any incoming MAC requests will be rejected.

### Step 3: Configure Allowed MAC Addresses

We will now set a rule to only allow devices with a specific MAC address to use the MAC server, providing a basic security measure.

*   **Before:**  MAC server is enabled on ether-27, but there are no specific rules for allowing or denying MAC addresses.
*   **Explanation:** The `/interface mac-server mac-address` command is used to manage the MAC address filtering, the `add` function specifies that we are adding a new entry to this rule set. The `mac-address=00:11:22:33:44:55` specifies that we are targeting MAC address `00:11:22:33:44:55` and the `action=allow` parameter will allow requests from that MAC address.

*   **CLI Example:**
    ```
    /interface mac-server mac-address add mac-address=00:11:22:33:44:55 action=allow
    ```
*   **Winbox GUI:** In *Interfaces* -> *MAC Server* -> *MAC Address*, click the '+' button. Enter `00:11:22:33:44:55` for MAC Address, choose `allow` for Action.
*   **After:** Only devices with MAC address `00:11:22:33:44:55` will be allowed.
*   **Note:** Use a different MAC address to test, as you might need to generate a fake MAC address on a device to test properly.

### Step 4: Adding IP assignment

We will now set a rule that assigns a specific IP address to that given MAC address when requested.

*   **Before:** The MAC Server is enabled and can receive requests, and devices with mac address `00:11:22:33:44:55` are allowed.
*   **Explanation:** We are going to use the `/ip mac-server` command to manage the relationship between MAC addresses and IP addresses that are handed out by the server, with the `add` function to add a new entry. The `mac-address=00:11:22:33:44:55` parameter is the key that this rule looks for, the `address=141.5.98.200` specifies the IP address that will be assigned, and the `server=ether-27` param specifies the target server.
*   **CLI Example:**
    ```
    /ip mac-server add mac-address=00:11:22:33:44:55 address=141.5.98.200 server=ether-27
    ```

*   **Winbox GUI:** Go to *IP* -> *MAC Server*, click the '+' button. Under 'Mac Address' specify `00:11:22:33:44:55`, under 'Address' specify `141.5.98.200`, under 'Server' specify `ether-27`.
*   **After:** The MAC Server will now return the IP address 141.5.98.200 to clients who request it with MAC address `00:11:22:33:44:55`.

## Complete Configuration Commands:

```
/interface print
/interface mac-server add interface=ether-27
/interface mac-server mac-address add mac-address=00:11:22:33:44:55 action=allow
/ip mac-server add mac-address=00:11:22:33:44:55 address=141.5.98.200 server=ether-27
```

### Parameter Explanations:

| Command Parameter        | Explanation                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| `/interface print`        | Shows a list of all existing interfaces in the MikroTik.                    |
| `/interface mac-server add interface=ether-27`    | Enables the MAC server on interface `ether-27`.                                   |
| `/interface mac-server mac-address add mac-address=00:11:22:33:44:55 action=allow` | Adds a MAC address filter rule allowing only devices with MAC `00:11:22:33:44:55`.  |
| `/ip mac-server add mac-address=00:11:22:33:44:55 address=141.5.98.200 server=ether-27` | Assigns the IP address 141.5.98.200 to the MAC address `00:11:22:33:44:55` when requested from `ether-27`. |

## Common Pitfalls and Solutions:

1.  **Interface Not Enabled:**  If `ether-27` is not enabled, the MAC server won't function.
    *   **Solution:** Enable the interface via `/interface enable ether-27` or in Winbox.
2.  **Incorrect MAC Address:** Typos in the MAC address will cause the device to be rejected.
    *   **Solution:** Double-check the MAC address using `/interface mac-server mac-address print` or Winbox to make sure that the mac addresses you have specified are correct.
3.  **Conflicting DHCP Configuration:**  A DHCP server on the same subnet might conflict with MAC server address assignments.
    *   **Solution:** If using both DHCP and MAC servers, manage IP ranges carefully to avoid overlap. Ensure MAC assigned IP addresses are out of DHCP's scope.
4.  **Firewall Rules:**  Firewall rules might block the MAC server responses.
    *   **Solution:** Make sure that the firewall rules do not block traffic coming from or going out on the interface on which you enabled the mac server.

## Verification and Testing Steps:

1.  **Check MAC Server Status:**
    *   Use `/interface mac-server print` to confirm the MAC server is enabled on `ether-27`.
    *   Winbox GUI: Check *Interfaces* -> *MAC Server*.
2.  **Verify MAC Address Filter:**
    *   Use `/interface mac-server mac-address print` to check the MAC filter rules.
    *   Winbox GUI: Check *Interfaces* -> *MAC Server* -> *MAC Address*.
3.  **Verify IP Assignment:**
    *   Use `/ip mac-server print` to confirm IP assignments.
    *   Winbox GUI: Check *IP* -> *MAC Server*.
4.  **Testing with a Device:**
    *   Using a test device, configure its MAC address to be `00:11:22:33:44:55`.
    *   Request a new IP, ideally using the MAC address, instead of sending DHCP requests or similar.
    *   Check if the device gets IP address `141.5.98.200`. If the device is not capable of requesting using its MAC address directly, then verify that the server returns the correct IP address to the client via tcpdump or similar.

## Related Features and Considerations:

*   **DHCP Server:** MAC server works well with DHCP but it should be configured carefully to avoid IP address conflicts.
*   **Radius Server:** Use a RADIUS server to manage MAC address-based access control and IP assignment for more complex environments.
*   **Scripting:** Use MikroTik's scripting language to create dynamic MAC address management tools.
*   **ARP Table:** The assigned IP addresses won't appear in the ARP table until they are actually used.

## MikroTik REST API Examples:

Note: MikroTik's REST API is generally available on version 6.48 and newer.

### Get Interface Information:

*   **Endpoint:** `/interface`
*   **Method:** `GET`
*   **Request Body:** None
*   **Response Example (JSON):**

```json
[
    {
        "id": "*1",
        "name": "ether1",
        "type": "ether",
        "mtu": 1500,
        "l2mtu": 1598,
        "max-l2mtu": 10236,
        "enabled": true,
        "running": true
    },
    {
        "id": "*27",
        "name": "ether27",
        "type": "ether",
        "mtu": 1500,
        "l2mtu": 1598,
        "max-l2mtu": 10236,
        "enabled": true,
        "running": true
    }

]
```

### Add MAC Server Interface:

*   **Endpoint:** `/interface/mac-server`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
        "interface": "ether-27"
    }
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "message": "added",
        "id": "*1"
    }
    ```
*   **Error Handling:** If the interface doesn't exist or is invalid, the API returns a status code like 400 with a relevant error message.

### Add MAC Address Filter:

*   **Endpoint:** `/interface/mac-server/mac-address`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
        "mac-address": "00:11:22:33:44:55",
        "action": "allow"
    }
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "message": "added",
        "id": "*1"
    }
    ```

### Add IP Assignment:

*   **Endpoint:** `/ip/mac-server`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
      "mac-address": "00:11:22:33:44:55",
      "address": "141.5.98.200",
      "server": "ether-27"
    }
    ```
*   **Expected Response (JSON):**
    ```json
     {
        "message": "added",
        "id": "*1"
    }
    ```

**Notes:**
*   Use the correct content type headers, such as `application/json`.
*   Authentication (e.g., via token) should be configured with your MikroTik REST API.
*   Replace `"id": "*1"` with actual IDs that you get from the RouterOS API.

## Security Best Practices:

1.  **MAC Address Filtering:** Allow only known MAC addresses.
2.  **Limit Access:** Restrict access to the MAC server on the interface by only enabling it on needed interfaces.
3.  **Strong Router Passwords:** Ensure a strong password is used to access your MikroTik router.
4.  **Regular Updates:** Keep RouterOS updated to patch any vulnerabilities.
5.  **API Security:** Secure API access with tokens, restrict access by IPs, or disable the API when it is not needed.

## Self Critique and Improvements:

*   **Scalability:** For a large number of MAC addresses, a database or Radius would be more appropriate.
*   **Dynamic IP:** This setup is static, it could be extended with scripts to dynamically give out an IP address based on user requests.
*   **Logging:** Add logging to track MAC server usage and troubleshoot issues.
*   **Error Handling:** The API examples could be expanded with more error handling scenarios.
*   **Granular Permissions:** Add more granular permissions to the mac server to support more complex configurations.

## Detailed Explanations of Topic

A MAC server in MikroTik provides a mechanism to respond to specific requests based on MAC addresses. Unlike a DHCP server that focuses on IP address assignments to network devices by using DHCP protocol, a MAC server listens for MAC addresses to be presented to it and can, in response, return IP addresses or perform other actions. This is helpful when devices need to be uniquely identified and addressed via IP based on their physical addresses (MAC addresses) rather than just relying on DHCP which can be less predictable.

This is especially useful in environments where you need:
*   **Static IP Assignments by MAC:** When certain devices always require the same IP address, but you do not want to rely on static IP address assignment within their own network configuration.
*   **Access Control:** When only specific devices identified by their MAC are allowed access to certain parts of a network.
*   **Customized Configurations:** When custom actions or configurations need to be applied based on which device is on the network.

## Detailed Explanation of Trade-offs

*   **MAC Server vs. DHCP Server:**
    *   **MAC Server:** Provides static IP allocation based on the MAC address. Useful for devices that always need the same IP or when you want to ensure only specific devices get IP addresses at all.
    *   **DHCP Server:** Provides dynamic IP allocation, and can be useful in scenarios where device allocation changes, or when devices don't require static IPs.
*   **Static Configuration vs. Dynamic Configuration:**
    *   **Static:** Easy to set up for a small network but not scalable.
    *   **Dynamic (using scripting):** Provides a flexible solution but it's more complex to configure.
*   **Simple vs. Radius:**
    *   **Simple:**  Suitable for SOHO environments, easier to manage with a few entries.
    *   **Radius:** Needed for larger, complex networks where a centralized authentication and authorization system is required.

## Configuration for Specific RouterOS Versions:

This configuration is suitable for RouterOS 7.12 and earlier versions of RouterOS 7 (7.x) as well as RouterOS 6.48. The commands `/interface mac-server`, `/interface mac-server mac-address`, `/ip mac-server` were available prior to v7, but some functionality might be slightly different on other versions. Always consult the official MikroTik documentation for the specific RouterOS version you are using to ensure compatibility. Specifically, the REST API examples above might behave differently for older RouterOS versions.

This completes the comprehensive guide. Let me know if you have any other scenarios or MikroTik features you'd like to explore!
