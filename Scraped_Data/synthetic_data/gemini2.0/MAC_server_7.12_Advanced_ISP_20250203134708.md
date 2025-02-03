Okay, let's dive into a detailed technical document on configuring a MAC Server on MikroTik RouterOS, focusing on advanced scenarios relevant to an ISP environment, and targeting RouterOS 7.12 (with considerations for 6.48 and general 7.x).

## Scenario Description:

This document outlines how to configure a MikroTik router to act as a **MAC Server** on the `bridge-12` interface within the 235.5.185.0/24 subnet. A MAC server is a feature typically used to dynamically manage IP addresses for devices based on their MAC address, often in scenarios where DHCP is not the preferred method (e.g., pre-provisioned devices, static-IP management with MAC based filtering).  We will configure this router to learn and assign IPs via MAC and be the primary authority of who has what IP on the configured subnet.  This method provides a less common, but powerful way to manage devices, especially in ISP and large-scale enterprise situations.

**Configuration Level**: Advanced
**Network Scale**: ISP

## Implementation Steps:

This configuration will enable a `MAC Server` which will allow dynamic assignment of IP addresses to clients based on their MAC address.

1.  **Step 1: Verify and Create the Bridge Interface**

    *   **Purpose**: Ensure the bridge interface exists and is configured correctly. The MAC server will operate on this bridge.
    *   **Before**:  Check if `bridge-12` exists. If not, we'll create it.
    *   **CLI Example - Check**:
        ```mikrotik
        /interface bridge print
        ```
    *   **Expected Output (if not present)**: A list of existing bridges, likely without `bridge-12`.
    *   **CLI Example - Create (if needed):**
        ```mikrotik
        /interface bridge add name=bridge-12
        ```
    *   **After**: The bridge interface `bridge-12` should be present in the list of interfaces.
    *   **GUI Winbox**: Go to *Bridge*, click the *+* button and add `bridge-12`.
    *   **Effect**: The creation of the logical bridge interface.

2. **Step 2: Add Bridge Ports**
    *   **Purpose**: Add the desired ports to your bridge.
    *   **Before**:  The `bridge-12` exists but does not have any member ports.
    *  **CLI Example - Add port**:
        ```mikrotik
        /interface bridge port add bridge=bridge-12 interface=ether2
        /interface bridge port add bridge=bridge-12 interface=ether3
        ```
    * **After**: The bridge interface `bridge-12` should have it's member ports.
    * **GUI Winbox**: Go to *Bridge*, select the *Ports* tab, click the *+* button and add your desired interfaces.
    *   **Effect**: Allows traffic to flow through the bridge.

3.  **Step 3: Configure IP Address on the Bridge**

    *   **Purpose**: Assign an IP address to the bridge interface, needed for routing and the operation of the MAC server.
    *   **Before**: The `bridge-12` interface exists, but does not have an IP address assigned.
    *   **CLI Example**:
        ```mikrotik
        /ip address add address=235.5.185.1/24 interface=bridge-12
        ```
    *   **After**: The bridge `bridge-12` will have an IP address.
    *   **GUI Winbox**: Go to *IP* -> *Addresses*, click the *+* button, and add `235.5.185.1/24` to interface `bridge-12`.
    *   **Effect**: Allows the router to communicate within the specified subnet.

4. **Step 4:  Enable MAC Server**

    *   **Purpose**: Activate the MAC server functionality on the specified bridge interface.
    *   **Before**: The MAC server is inactive.
    *   **CLI Example**:
        ```mikrotik
        /ip mac-server add interface=bridge-12 disabled=no
        ```
    *   **After**: The MAC server is now active on the specified bridge interface.
    *   **GUI Winbox**: Go to *IP* -> *MAC Server*, click the *+* button, select interface `bridge-12`, and uncheck the `Disabled` checkbox.
    *   **Effect**: Begins listening on the specified interface for MAC addresses and potentially assigns IP addresses based on configuration.

5.  **Step 5: Configure MAC Server Entries (static IP mapping)**

    *   **Purpose**: Manually add MAC-to-IP mappings. This defines the specific IP address a device is assigned based on the MAC address. For instance, lets assign the IP `235.5.185.100` to `AA:BB:CC:DD:EE:FF`.
    *   **Before**: The MAC server does not have any MAC to IP mappings defined.
    *   **CLI Example**:
        ```mikrotik
        /ip mac-server entry add mac-address=AA:BB:CC:DD:EE:FF address=235.5.185.100 server=0
        ```
     *   **After**: The MAC server will now attempt to give `235.5.185.100` to the client with MAC `AA:BB:CC:DD:EE:FF`.
    *   **GUI Winbox**: Go to *IP* -> *MAC Server*, select the *Entries* tab, click the *+* button, and add the MAC and IP mappings for each entry.
    *   **Effect**: Creates specific IP assignments based on MAC addresses.
    *  **Note**: The `server` parameter needs to match the entry id on the `/ip mac-server` output. In our case since only 1 `MAC Server` is added, it will have `server=0`.  If you have multiple `MAC Server` interfaces, this parameter is mandatory to specify the correct instance.

6. **Step 6: Configure MAC Server Allowed Addresses (Optional)**

  * **Purpose**: Restrict IP addresses that are allocated by the MAC server to a specific range.
  * **Before**: The MAC Server will allow any IP within the IP subnet to be used for dynamic addressing.
  * **CLI Example**:
    ```mikrotik
    /ip mac-server set 0 allowed-addresses=235.5.185.10-235.5.185.254
    ```
  * **After**: Only IPs in the specified range will be used for dynamic assignments.
   *  **GUI Winbox**: Go to *IP* -> *MAC Server*, and set *Allowed Addresses* to `235.5.185.10-235.5.185.254`.
  * **Effect**: Constrains IPs used, avoiding address collisions, or allows for future growth.

## Complete Configuration Commands:

Here are all the commands combined for easy copy-pasting to the MikroTik CLI.
```mikrotik
/interface bridge add name=bridge-12
/interface bridge port add bridge=bridge-12 interface=ether2
/interface bridge port add bridge=bridge-12 interface=ether3
/ip address add address=235.5.185.1/24 interface=bridge-12
/ip mac-server add interface=bridge-12 disabled=no
/ip mac-server entry add mac-address=AA:BB:CC:DD:EE:FF address=235.5.185.100 server=0
/ip mac-server set 0 allowed-addresses=235.5.185.10-235.5.185.254
```

**Parameter Explanation:**

| Command                        | Parameter        | Description                                                                                  |
|--------------------------------|------------------|----------------------------------------------------------------------------------------------|
| `/interface bridge add`        | `name`           | Specifies the name of the bridge interface.                                              |
| `/interface bridge port add`    | `bridge`         | Specifies which bridge this interface will be a member of.                                |
| `/interface bridge port add`    | `interface`      | Specifies the name of the physical or virtual interface to add to the bridge.           |
| `/ip address add`               | `address`        | The IP address and subnet mask for the interface.                                            |
| `/ip address add`              | `interface`      | The interface to assign the IP address to.                                                    |
| `/ip mac-server add`          | `interface`     | The bridge interface that will be monitored by the MAC server.                               |
| `/ip mac-server add`           | `disabled`       |  Set to `no` to enable the MAC server.                                                     |
| `/ip mac-server entry add`     | `mac-address`    | The MAC address to assign an IP address.  Use a colon separated format (eg. `AA:BB:CC:DD:EE:FF`).|
| `/ip mac-server entry add`     | `address`        | The IP address to be assigned.                                                               |
| `/ip mac-server entry add`    | `server`        |  The id of the MAC Server to use. This can be found in the `/ip mac-server print` output.|
| `/ip mac-server set`         | `allowed-addresses`|  The IP range that the MAC server can assign.                                               |

## Common Pitfalls and Solutions:

1.  **Issue:** Clients not getting IP addresses.
    *   **Cause**:
        *   Incorrect interface specified in the MAC server.
        *   MAC address entry is wrong or missing.
        *   No MAC entries defined in the server and no DHCP pool available to assign from.
        *  Client is not configured to request MAC IP address assignments.
    *   **Solution**:
        *  Double check that the bridge interface assigned is correct, as well as the MAC address, and if it is listed in the active lease list.
        *   Check and add the correct MAC address mapping in `/ip mac-server entry` or add a dhcp server pool and server on the interface.
        *   Check to see if the client supports this method of address assignment.
2.  **Issue**:  Multiple clients having the same IP address.
    *   **Cause**:
        *   IP conflicts occur when using multiple servers that don't understand each other, using a fixed set of IPs, or not correctly using the MAC server for static assignments.
        *   Duplicate MAC addresses in your network.
    *   **Solution**:
        *    Ensure each client has a unique MAC address.
        *   Use a limited range or a static IP address pool defined in the MAC server configuration
        *   Consider DHCP lease times or different dynamic range for different pools.
3. **Issue:** High CPU Usage due to the mac server.
    *   **Cause**:
        *   A high number of MAC entries, or frequent updates.
    * **Solution**
        *  Ensure that the bridge interface only contains the relevant interfaces.
        * Limit the amount of dynamic assignments.
        *  If there are a large amount of static assignment, consider the use of DHCP for dynamic assignments.

**Security Considerations:**

*   **MAC Spoofing**:  MAC addresses can be spoofed.  Implement additional security measures like port security if required.
*   **ARP Spoofing:**  Attackers could use ARP poisoning and act as a Man-in-The-Middle (MitM) since the MAC address is essentially trusted for IPs.
*   **Unauthorized Devices**: Any device with a configured MAC address can obtain an IP, which might lead to unauthorized access.

## Verification and Testing Steps:

1.  **Check MAC Server Status**:
    ```mikrotik
    /ip mac-server print
    ```
    *   Verify that the MAC server is enabled and running on the correct bridge.

2. **Check MAC Server Entries**:
  ```mikrotik
   /ip mac-server entry print
  ```
    *   Verify that the MAC addresses and IP assignments are correct.

3.  **Ping Test**:
    *   From another device on the same network, ping the IP address assigned by the MAC server (e.g., 235.5.185.100) to the client.
    *   From the router, ping an assigned address.
    ```mikrotik
    /ping 235.5.185.100
    ```
    *   Ensure the ping is successful, indicating the IP address was assigned and the device is reachable.

4.  **Monitor Active Leases**:
   ```mikrotik
    /ip mac-server lease print
    ```
    *   Check that the client's MAC and IP are in the active lease list.

5. **Torch Tool**:
    * Use MikroTik's torch tool to see mac activity on the bridge interface.
    * To do this from the terminal type `/tool torch interface=bridge-12`
    * It will display a real time capture of packets and their related MAC addresses. This will allow a deep look into what devices are currently active on the network.

## Related Features and Considerations:

*   **DHCP Server**: You can combine the MAC server with a DHCP server on the same bridge. The DHCP server could act as a backup assignment method when a client's MAC address is not configured in the MAC server entries.
*   **IP Bindings**: The `/ip dhcp-server lease`  feature is very similar to the mac server.
*   **Hotspot**: In hotspot environments, the MAC server can be used for pre-configured devices, providing a more granular control.
*   **API**: The MAC server can be completely managed via the MikroTik API.

## MikroTik REST API Examples:

Here are a few examples for managing mac-server with REST API calls. Replace `your_router_ip`, `your_router_user`, and `your_router_password` with your appropriate values.

**Note**: The MikroTik API works on a session-based system, so this means a login needs to be performed before a command can be called. This example will skip that, as there are security considerations, like handling the session tokens correctly, that should be taken, but are not within the scope of this document. This assumes that a working session is created prior to these calls.

1. **Creating a MAC Server:**

    *   **Endpoint**: `/ip/mac-server`
    *   **Method**: `POST`
    *   **Request JSON Payload:**
        ```json
        {
          "interface": "bridge-12",
          "disabled": false
        }
        ```
    *   **Expected Response (200 OK)**:
        ```json
          {
             "id": "*1",
            "interface": "bridge-12",
             "disabled": false,
             "comment": ""
          }
        ```
2. **Adding a MAC Server Entry:**
    *   **Endpoint**: `/ip/mac-server/entry`
    *   **Method**: `POST`
    *   **Request JSON Payload:**
        ```json
        {
           "mac-address": "AA:BB:CC:DD:EE:FF",
           "address": "235.5.185.100",
            "server": "*1"
        }
        ```
      *  **Note** `server` points to the id of the server we created earlier.
    *   **Expected Response (200 OK)**:
          ```json
          {
            "id": "*2",
             "mac-address": "AA:BB:CC:DD:EE:FF",
             "address": "235.5.185.100",
             "server": "*1",
             "comment": ""
          }
          ```

3. **Getting MAC Server Entries:**

   *   **Endpoint**: `/ip/mac-server/entry`
   *   **Method**: `GET`
   *   **Request JSON Payload:** *(None)*
   *   **Expected Response (200 OK)**:

        ```json
         [
            {
             "id": "*2",
             "mac-address": "AA:BB:CC:DD:EE:FF",
             "address": "235.5.185.100",
             "server": "*1",
             "comment": ""
          }
        ]
        ```

4. **Updating the Allowed Addresses:**
   *   **Endpoint**: `/ip/mac-server/*1`
   *   **Method**: `PUT`
   *   **Request JSON Payload:**
       ```json
       {
         "allowed-addresses": "235.5.185.10-235.5.185.254"
       }
       ```
   *   **Expected Response (200 OK)**:
       ```json
          {
             "id": "*1",
            "interface": "bridge-12",
             "disabled": false,
             "comment": "",
            "allowed-addresses": "235.5.185.10-235.5.185.254"
          }
       ```

5. **Example of Error Handling:**

    *   If you try to add an entry with the same MAC Address, the following response will be given:

          ```json
             {
                "message": "already have entry with mac address",
                "error": true
            }
          ```

## Security Best Practices

* **MAC Address Validation**: Implement external validation to verify the MAC addresses are coming from legitimate sources.
* **Limited IP Pool**: Assign limited ranges to prevent IP exhaustion, which can create issues for your IP assignment mechanisms.
* **Monitoring**: Monitor activity logs for any unusual activity related to the MAC server or abnormal entries.
* **Access Control**: Control access to the router by using strong passwords and access lists.
* **Firewall rules**: Control what traffic is allowed into your network, especially in ISP environments.

## Self Critique and Improvements

This configuration is fairly detailed and targets an ISP environment with specific requirements. Here are some areas for improvement:

*   **Dynamic Assignment**: It would be beneficial to show how to do dynamic assignment, especially when not all devices are pre-configured. This would include enabling the mac server to assign an address automatically from a set pool of IPs.
*   **Integration with AAA**: In ISP environments, integrating the MAC server with AAA (Authentication, Authorization, Accounting) services (e.g., RADIUS) could improve security and manageability.
*   **Detailed Logging**: Show how to monitor and log the activity of the mac-server to detect problems quicker.

## Detailed Explanations of Topic

**MAC Server:**

The MikroTik MAC Server allows IP address assignments based on a device's MAC address. It listens for ARP requests and can respond by providing a pre-configured IP address to a client or dynamically assign an IP address from a specific range. This is particularly useful for networks that need strict control over IP addressing or where DHCP is not ideal. The MAC server assigns addresses within the configured subnet. It is particularly useful for assigning IPs to static devices that do not use the more typical DHCP addressing, such as security cameras. The mac-server acts an IP assignment service based on MAC address.

**Trade-offs:**
*   **Static IP vs. Dynamic IP**: While static assignments provide predicability, dynamic assignments are more convenient and easier to maintain when devices are not known ahead of time.
*   **Complexity**: While MAC servers offer control, they add complexity when compared to normal DHCP setups. Using MAC server combined with DHCP is generally a recommended approach to mitigate its complexity.
*   **Security**: MAC address can be spoofed. This means that security should not solely rely on MAC address filtering. Use a secondary security mechanisms, like firewall rules or port security to restrict access.
*   **Resource Usage**: Large amounts of static assignments can increase resource usage on the router. Use smaller ranges when possible, or use DHCP if this becomes a problem.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeted for RouterOS 7.12 and is generally compatible with RouterOS 7.x and 6.48. However, be aware:

*   **Syntax:** Commands should be identical between 7.x and 6.48.
*   **Features**: Minor feature or interface differences may exist across different RouterOS versions. Always consult the official MikroTik documentation for your specific RouterOS version.
*   **API Changes**: Major RouterOS versions may introduce API endpoint changes. Check the specific API documentation.

This comprehensive guide should provide you with a solid foundation for configuring and managing MAC servers in your MikroTik environment. Always test configurations in a lab environment before applying them to production networks.
