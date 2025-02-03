Okay, let's dive into configuring a MAC Server on MikroTik RouterOS, specifically for your Hotspot network using VLAN interface `vlan-8` and subnet `82.74.234.0/24`, targeting RouterOS 7.11 (and applicable to 6.48 and 7.x versions).

## Scenario Description:

We are setting up a MAC Server on a MikroTik router to provide IP addresses to clients based on their MAC addresses. This is particularly useful in Hotspot environments where you might want to assign static or persistent IP addresses to specific devices, or offer specific services based on a user’s device MAC address. This configuration aims to allow DHCP to issue specific IP addresses based on MAC address identification, and can also be used for other features that rely on MAC identification, such as radius services.  We will use a specific VLAN interface `vlan-8`, which is part of the 82.74.234.0/24 subnet. This is a basic configuration, and can be enhanced.

## Implementation Steps:

Here's a step-by-step guide to configure the MAC server, along with explanations, examples and troubleshooting.

### 1.  Initial State Check:
*   **Description**:  Before we make changes, let's check the existing IP configuration of `vlan-8` (assuming it's already configured and has an IP address). This is important to know the existing configuration, especially if this is not a new router.
*   **Action**: Use the following CLI command to show the current IP address and VLAN configuration. We'll use the Winbox GUI for similar steps.
*   **CLI command**:

    ```mikrotik
    /ip address print where interface=vlan-8
    /interface vlan print where name=vlan-8
    ```
*   **Expected Output (Example)**:

    ```
    /ip address print where interface=vlan-8
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS            NETWORK         INTERFACE        
    0   82.74.234.1/24     82.74.234.0      vlan-8    
    /interface vlan print where name=vlan-8
    Flags: X - disabled, R - running
    #    NAME    MTU   MAC-ADDRESS       VLAN-ID INTERFACE
    0  R vlan-8    1500   00:11:22:33:44:55 8     ether1
    ```
* **Winbox GUI:** You can find this information by navigating to "IP -> Addresses" and "Interface -> VLAN" respectively.  Clicking on the `vlan-8` entry in both locations will reveal the same information.

### 2. Enable and Configure DHCP Server:

*   **Description**: We need a DHCP server running on the `vlan-8` interface to provide addresses to clients. If you don't already have one set up, this is necessary before using the mac-server.
*   **Action**: Create a new DHCP server on vlan-8.  If a server exists on the interface, modify it. We also need a DHCP network configuration.
*   **CLI Command**:

    ```mikrotik
    /ip dhcp-server
    add address-pool=default interface=vlan-8 name=dhcp-vlan-8 disabled=no
    /ip dhcp-server network
    add address=82.74.234.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=82.74.234.1
    ```

*   **Expected Output (Example)**: After running these commands, verify that they were added and the DHCP is enabled with:
    ```mikrotik
    /ip dhcp-server print
    /ip dhcp-server network print
    ```
    ```
     /ip dhcp-server print
     Flags: X - disabled, I - invalid
     #   NAME          INTERFACE  ADDRESS-POOL LEASE-TIME ADD-ARP  AUTHORITATIVE
     0   dhcp-vlan-8   vlan-8     default      10m        yes      yes
     /ip dhcp-server network print
     Flags: X - disabled, D - dynamic
     #   ADDRESS        DNS-SERVER        GATEWAY        DOMAIN   
     0   82.74.234.0/24 8.8.8.8,8.8.4.4   82.74.234.1 
    ```

*   **Winbox GUI:** Navigate to "IP -> DHCP Server" and "IP -> DHCP Server Network" to create and view these settings.
* **Note:** We've set lease time to 10 minutes. You may want a longer lease time depending on your network. We've also set the DHCP to be authoritative, which means it is allowed to provide lease information.  This can be disabled for redundancy purposes if you have more than one DHCP server.

### 3.  Configure MAC Server:
*   **Description**: Here's where we activate the MAC Server and define static MAC-to-IP mappings for specific devices.
*   **Action**:  Add a new static entry to the MAC server which will specify an IP address for a particular MAC address when they request an IP via DHCP.
*   **CLI Command**:

    ```mikrotik
     /ip dhcp-server lease add address=82.74.234.10 client-id=1A:2B:3C:4D:5E:6F mac-address=1A:2B:3C:4D:5E:6F server=dhcp-vlan-8
    ```

    **Important**: Ensure that the `mac-address` matches the `client-id`, as the `mac-address` is used for MAC filtering if this device is already connected with an IP not included in the static mappings.

*   **Expected Output (Example)**: After running these commands, verify that it was added with:
    ```mikrotik
    /ip dhcp-server lease print
    ```
    ```
    /ip dhcp-server lease print
    Flags: X - disabled, D - dynamic, A - active, B - blocked, R - radius
    #   ADDRESS         MAC-ADDRESS       CLIENT-ID        SERVER       HOSTNAME    
    0   82.74.234.10    1A:2B:3C:4D:5E:6F  1A:2B:3C:4D:5E:6F dhcp-vlan-8     
    ```
    You should see the new entry in the DHCP leases table.
*   **Winbox GUI:** Navigate to "IP -> DHCP Server" and then the "Leases" tab. Click the "+" button to add a new static lease. You can enter the MAC address, IP address and the DHCP server it is associated with.

### 4.  Test the Configuration:

*   **Description**: Connect a client device with the MAC address `1A:2B:3C:4D:5E:6F` and verify that it receives the IP address `82.74.234.10`.
*   **Action**: Observe the DHCP lease entries. The `A` flag should indicate an active lease.
*   **Expected Output**: If your client device with the specified MAC address requests an IP via DHCP, it will receive `82.74.234.10`. This should be visible in the DHCP leases list on the router, as shown in the "Expected Output (Example)" after step 3, with the `A` flag active if the device has requested an IP from the server.
*   **Troubleshooting:** If your client does not receive the expected IP address, double-check that:
    *   The MAC address is entered correctly.
    *   The server in the lease table matches the active DHCP server name.
    *   The client is connected to the correct VLAN.
    *   You do not have conflicting IP ranges.

## Complete Configuration Commands:

Here's the complete set of CLI commands used to implement the setup:

```mikrotik
/ip address print where interface=vlan-8
/interface vlan print where name=vlan-8

/ip dhcp-server
add address-pool=default interface=vlan-8 name=dhcp-vlan-8 disabled=no
/ip dhcp-server network
add address=82.74.234.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=82.74.234.1

/ip dhcp-server lease add address=82.74.234.10 client-id=1A:2B:3C:4D:5E:6F mac-address=1A:2B:3C:4D:5E:6F server=dhcp-vlan-8

/ip dhcp-server lease print
/ip dhcp-server print
/ip dhcp-server network print
```

**Parameter Explanations:**

| Command              | Parameter        | Description                                                                    | Example Value           |
| -------------------- | ---------------- | ------------------------------------------------------------------------------ | ----------------------- |
| `/ip dhcp-server add`| `address-pool`  | The address pool to use for DHCP leases. (Must be created first)               | `default`               |
| `/ip dhcp-server add`| `interface`      | The interface on which to run the DHCP server.                               | `vlan-8`                |
| `/ip dhcp-server add`| `name`           | The name of the DHCP server instance.                                          | `dhcp-vlan-8`           |
| `/ip dhcp-server add`| `disabled`       | Whether to disable the DHCP server.                                            | `no`                    |
|`/ip dhcp-server network add` | `address`     | The network address and subnet mask for DHCP leases.             | `82.74.234.0/24`            |
|`/ip dhcp-server network add` |`dns-server`|The DNS server to use for DHCP clients.  Comma separated values.            |  `8.8.8.8,8.8.4.4`            |
|`/ip dhcp-server network add` |`gateway` |The gateway to use for DHCP clients.             |  `82.74.234.1`            |
| `/ip dhcp-server lease add`| `address`    | The static IP address to assign to the MAC address.                           | `82.74.234.10`          |
| `/ip dhcp-server lease add`| `client-id`   | The client ID associated with the lease (used to ensure that MAC matches).        | `1A:2B:3C:4D:5E:6F`     |
| `/ip dhcp-server lease add`| `mac-address`| The MAC address of the client.                                              | `1A:2B:3C:4D:5E:6F`     |
| `/ip dhcp-server lease add`| `server`      | The DHCP server instance to use for this static entry.                      | `dhcp-vlan-8`           |

## Common Pitfalls and Solutions:

*   **Problem:** Client not getting the static IP address.
    *   **Solution:**
        *   Verify that the MAC address is entered correctly in the DHCP server lease.
        *   Ensure that the `server` field matches the name of the DHCP server you created for the correct interface.
        *   Check for conflicts in IP address allocation, especially if a client previously had a dynamic address outside this range.
        *   Ensure that the client is indeed using the configured DHCP server in the interface where it was configured.
*   **Problem:** Clients not getting any IP address.
    *   **Solution:**
        *   Ensure the DHCP server is enabled.
        *   Check that the interface is up and has an IP address.
        *   Verify that the DHCP network configuration is correct.
*   **Problem:** High CPU usage.
    *   **Solution:**  While DHCP service isn't particularly resource intensive, excessive static lease entries in a very large network can cause it to use more memory and CPU. Try to keep static entries to a manageable quantity.
        *   Check if another process is using excessive resources, and verify that router is not under excessive loads due to other functions.
*   **Problem:** Security Issues
    *  **Solution**: By using MAC server, you’re binding IP addresses to specific physical devices. This is great for management but can also be an issue for devices spoofing MAC addresses. To mitigate:
         *   Combine MAC binding with other security measures like access lists and firewall rules.
         *    Enable DHCP Snooping at the switch level for the connected network.
         *  Monitor the router's logs for suspicious activity.

## Verification and Testing Steps:

1.  **Client Connection:** Connect a device with the specified MAC address (`1A:2B:3C:4D:5E:6F`).
2.  **Verify IP Address:** Check that the device gets the IP address `82.74.234.10` on the device's network settings.
3.  **Router Check:**
    *   Use the `/ip dhcp-server lease print` command on the MikroTik to confirm the active lease with the assigned static IP. The `A` flag in this output should indicate the active lease.
    *   Use the  `/ping 82.74.234.10` to test communication with the specific IP.
4.  **Torch:**  Use `/tool torch interface=vlan-8` on the router to see the DHCP traffic, you'll be able to see if the client sends a DHCP request to the router.

## Related Features and Considerations:

*   **Radius Authentication:**  You can combine MAC address authentication with RADIUS for more robust user management. The MikroTik can use the MAC address to identify the client and then ask the RADIUS for proper authentication. This is common in environments where you want to keep track of users based on the device, and you can track devices on a database.
*   **Hotspot Profiles:** Integrate MAC server settings with Hotspot profiles to provide special services or bandwidth limits for specific MAC addresses.
*   **Address Lists:** Use DHCP leases to populate address lists for firewall rules.  You can create a dynamic address list on lease activation for ease of management.
*   **Queue Trees:** If you need to assign a specific user to a queue for traffic shaping based on IP address, the MAC address can be used to identify clients, which can then be used as filters in queues.
*   **Multiple VLANs:**  This MAC server configuration can be extended to handle different VLANs with different subnets and static mappings. Be careful with multiple DHCP servers, ensure each of them has different subnets, and that you create proper routing configurations.

## MikroTik REST API Examples:

While the core of a MAC Server is through DHCP, the API examples below use the DHCP server functions.

### Example 1: Getting DHCP Leases
**Endpoint:** `/ip/dhcp-server/lease`
**Method:** `GET`
**Request:** Empty
**Expected Response (JSON):**

```json
[
  {
    ".id": "*10",
    "address": "82.74.234.10",
    "mac-address": "1A:2B:3C:4D:5E:6F",
    "client-id": "1A:2B:3C:4D:5E:6F",
    "server": "dhcp-vlan-8",
    "active-address": "82.74.234.10",
    "active-mac-address": "1A:2B:3C:4D:5E:6F",
        "dynamic": "false",
        "status" : "bound",
     "host-name": "client"
  }
]
```

**Explanation:**

*   This retrieves all DHCP leases, including static and dynamic ones.
*   The fields are similar to the output of `/ip dhcp-server lease print`.
*   An error response is usually a JSON object containing a `message` and/or a `code` for HTTP errors.

### Example 2: Adding a New Static Lease

**Endpoint:** `/ip/dhcp-server/lease`
**Method:** `POST`
**Request Payload (JSON):**

```json
{
    "address": "82.74.234.15",
    "mac-address": "00:AA:BB:CC:DD:EE",
    "client-id": "00:AA:BB:CC:DD:EE",
    "server": "dhcp-vlan-8"
}
```

**Expected Response (JSON) - Success:**
```json
{
  "message": "added",
  ".id": "*11"
}
```

**Explanation:**
*   This adds a new static lease using the specified parameters.
*   A successful response typically includes a `.id` for the new lease.

### Example 3: Error Handling

**Request Payload (JSON) - Invalid MAC:**
```json
{
    "address": "82.74.234.15",
    "mac-address": "invalid-mac",
    "client-id": "invalid-mac",
    "server": "dhcp-vlan-8"
}
```

**Expected Response (JSON) - Error:**
```json
{
  "message": "invalid value for parameter \"mac-address\"",
  "code" : 10
}
```
**Explanation:**
*   A failed request may return an error code and a message describing the problem.

**Note on API Errors**: The error codes and messages are not standardized in the MikroTik REST API, and they are not exhaustive. Ensure you are handling the error messages in a way that is useful to the application using the API.

## Security Best Practices

*   **MAC Spoofing:** Be aware that MAC addresses can be spoofed. Do not rely solely on MAC filtering for security in sensitive environments. Implement additional security mechanisms like DHCP snooping, IP source guard, firewalls, and user authentication.
*  **Limit Access:** Restrict access to the API and router management functions. Use strong passwords and access control lists.
*   **Monitor Logs:** Regularly check router logs for suspicious activities, particularly around DHCP lease assignments and connections.

## Self Critique and Improvements:

This configuration is basic and functional but can be further improved:

*   **Address Pool Management:**  We only used a default pool for the DHCP server. For complex setups, it's best to use named and more restricted address pools.
*   **Dynamic Leases:** The configuration uses a default pool for dynamic leases. You could set the pool for static leases as well, but keep in mind that by default, any addresses that are not in a static binding, and are within the DHCP scope, will be available to clients.
*   **Logging:** The logging has not been set. Proper logging configurations can help a great deal with troubleshooting.
*   **Monitoring**: Consider implementing a monitoring solution, like SNMP or Dude, to keep track of the router performance and status of DHCP leases.
*   **Further Integration:** Add more advanced features like integration with a RADIUS server for more robust user management, and dynamic address list management.

## Detailed Explanations of Topic:

A MAC server, in the context of networking, is a feature that allows network administrators to assign specific IP addresses to devices based on their Media Access Control (MAC) addresses. This is different from the default dynamic IP assignment from a DHCP server. Instead of providing the next available IP, the DHCP server checks to see if the client’s MAC address has a corresponding IP defined by the server. If it finds a match, the server assigns that specific address to the requesting device. This feature can also be used in combination with other authentication or authorization mechanisms like RADIUS to allow or restrict access based on both device and user authentication, which allows you to manage users based on both authentication and device management.

In MikroTik RouterOS, this is primarily accomplished via the DHCP Server lease table, where you can add static MAC to IP assignments.
This functionality has many uses:
*   **Static IP Assignments:** Ensure certain devices (printers, servers) always receive the same IP.
*  **Hotspot Management**: Control access to the network based on devices.
*   **Device Tracking**: Keep track of network devices via DHCP and MAC identification.
*  **Access Control:** You can combine MAC address identification with other network access controls.

## Detailed Explanation of Trade-offs:

*   **Static vs. Dynamic IP Assignments:** Using static IP assignment via MAC server requires more initial configuration. Dynamic IP assignment is easier to configure, but doesn’t guarantee the same IP for the same device. You will need to manually add the mac address to ip mapping, which can be cumbersome in a very large network, or you will need to use the API for dynamic additions to the static entries. If the device changes it's mac address or if a new device is added, you will need to manually reconfigure.
*   **Security vs. Convenience:** MAC addresses can be spoofed, so static mappings can give you a false sense of security if not combined with other security measures. Dynamic assignments are more fluid, but they can make access control harder. If you rely solely on MAC server for security, malicious users can spoof their MAC address and obtain the static address you configured.
*   **Complexity vs. Control:** Setting up a MAC server adds complexity, especially if you have many devices. However, it also gives you more control and predictability in how IP addresses are assigned. In a small network, this could be beneficial, while in very large networks, manual mac server configuration can be cumbersome and introduce administration overhead.
*  **Single Point of Failure:** Relying solely on the router as the MAC server means that if the router goes down, then no IP allocations will be provided.

## Configuration for Specific RouterOS Versions:

This configuration works for RouterOS versions 6.48, 7.x, and specifically 7.11, with no changes required. The commands and parameters used in this configuration are consistent across these versions for the DHCP server functionality. For more advanced configurations, you should consult the relevant RouterOS documentation if you are using older or very specific RouterOS versions.

Let me know if you'd like to explore any of these advanced topics or have further scenarios you'd like to investigate.
