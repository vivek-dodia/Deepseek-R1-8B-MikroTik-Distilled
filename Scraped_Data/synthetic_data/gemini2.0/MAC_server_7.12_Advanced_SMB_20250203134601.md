Okay, let's dive into a comprehensive guide for setting up a MAC Server on a MikroTik RouterOS device, specifically targeting version 7.12, within the context of a subnet 61.249.70.0/24 on interface `vlan-68` and at an Advanced configuration level for an SMB network.

## Scenario Description:

This scenario focuses on implementing a MAC Server on a MikroTik router. A MAC server is a specialized DHCP server that provides IP addresses based on the client's MAC address. This is useful for scenarios where you want to assign static IPs to devices, but without the complexity of configuring static DHCP leases. In this example, the MAC server will serve IP addresses within the 61.249.70.0/24 subnet and listen on the `vlan-68` interface. This configuration is particularly useful in an SMB environment where you need a predictable IP addressing scheme for specific devices based on their hardware address.

## Implementation Steps:

Here's a step-by-step guide, including CLI examples and explanations:

**1. Step 1: Ensure Interface is Configured**

*   **Purpose**: Before configuring the MAC server, ensure that the `vlan-68` interface is correctly configured and active.
*   **Before Configuration**: Assuming `vlan-68` is already created on your router, this step verifies that it's enabled. For this example, we assume that vlan-68 is a child of ether1, is tagged with VLAN ID 68, and has an IP Address configured.

*   **CLI Commands:**
    ```mikrotik
    /interface vlan
    print
    /interface ethernet
    print
    /ip address
    print
    ```
*   **Winbox GUI**: Check "Interfaces" and "IP" > "Addresses" to verify interface status and IP configuration.
*   **Explanation**: The `print` command displays the current interface and IP address configuration. We need to confirm that `vlan-68` exists and has an IP address configured, because a MAC server must be associated with an interface that has an assigned IP address. This example assumes you have already configured vlan-68 with an IP address of 61.249.70.1/24

*   **Expected Output**: We expect to see `vlan-68` listed in the output of the `/interface vlan print` command, an entry of `/interface ethernet print` showing that ether1 exists, and and an entry in `/ip address print` showing `61.249.70.1/24` is assigned to the `vlan-68` interface.

**2. Step 2: Configure the DHCP MAC Server**

*   **Purpose:** Add a new DHCP server instance and configure it to use the `vlan-68` interface and act as a MAC server.
*   **Before Configuration**: No specific MAC server is configured.
*   **CLI Command:**
    ```mikrotik
    /ip dhcp-server
    add address-pool=default interface=vlan-68 lease-time=1d name=mac-server-vlan68 server-type=mac
    ```
*   **Winbox GUI**: Navigate to "IP" > "DHCP Server" and add a new DHCP server entry. Set the "Interface" to `vlan-68`, "Server Type" to `mac`, "Name" to `mac-server-vlan68` and Lease Time to 1 day. Other settings can use default values.
*   **Explanation**:
    *   `add`: Creates a new DHCP server instance.
    *   `address-pool=default`: Specifies that it uses the default address pool for DHCP. While not explicitly required for MAC servers, it is a good practice to use the 'default' for simplicity.
    *   `interface=vlan-68`: Binds this server to the `vlan-68` interface.
    *   `lease-time=1d`: Specifies that leases are valid for 1 day.
    *    `name=mac-server-vlan68`: Assigns a name to the DHCP server instance for easy identification.
    *    `server-type=mac`: Sets the DHCP server type to MAC mode.

*   **After Configuration**: A new MAC server will be active on `vlan-68`.

* **Expected Output**: If we run the print command:
    ```mikrotik
    /ip dhcp-server print
    ```
    We should now see a new entry:
    ```mikrotik
    Flags: X - disabled, I - invalid
     0   name="mac-server-vlan68" interface=vlan-68 lease-time=1d address-pool=default
         authoritative=yes server-type=mac
    ```
**3. Step 3: Configure MAC Address to IP Mapping**

*   **Purpose:**  Specify the static IP addresses to be associated with particular MAC addresses.
*   **Before Configuration**: No MAC to IP mappings are configured.
*   **CLI Command**:
    ```mikrotik
    /ip dhcp-server lease
    add address=61.249.70.10 mac-address=00:11:22:33:44:55 server=mac-server-vlan68
    add address=61.249.70.20 mac-address=AA:BB:CC:DD:EE:FF server=mac-server-vlan68
    ```
    * Replace `00:11:22:33:44:55` and `AA:BB:CC:DD:EE:FF` with actual MAC addresses.
*   **Winbox GUI**: Navigate to "IP" > "DHCP Server" and go to the "Leases" tab. Click the "+" button to add a new lease, enter the MAC address, static IP address, and select the `mac-server-vlan68` server from the dropdown.
*   **Explanation**:
    *    `add`: Adds a new static MAC-to-IP lease entry.
    *   `address=61.249.70.10`: The IP address to be assigned to the given MAC address.
    *   `mac-address=00:11:22:33:44:55`: The MAC address of the client.
    *   `server=mac-server-vlan68`: Associate this mapping with our previously created mac-server.

*   **After Configuration**: Devices with MAC addresses `00:11:22:33:44:55` will always receive `61.249.70.10`, and devices with `AA:BB:CC:DD:EE:FF` will always receive `61.249.70.20`.

*   **Expected Output**:
    ```mikrotik
    /ip dhcp-server lease print
    ```
    This should output something similar to:
    ```mikrotik
     Flags: X - disabled, D - dynamic, B - bundled
     #   ADDRESS          MAC-ADDRESS       SERVER          HOSTNAME    
     0   61.249.70.10    00:11:22:33:44:55  mac-server-vlan68                       
     1   61.249.70.20    AA:BB:CC:DD:EE:FF  mac-server-vlan68
     ```

## Complete Configuration Commands:

```mikrotik
/interface vlan
add interface=ether1 name=vlan-68 vlan-id=68
/ip address
add address=61.249.70.1/24 interface=vlan-68 network=61.249.70.0
/ip dhcp-server
add address-pool=default interface=vlan-68 lease-time=1d name=mac-server-vlan68 server-type=mac
/ip dhcp-server lease
add address=61.249.70.10 mac-address=00:11:22:33:44:55 server=mac-server-vlan68
add address=61.249.70.20 mac-address=AA:BB:CC:DD:EE:FF server=mac-server-vlan68
```

*   **`/interface vlan add...`**: Creates a VLAN interface.
    *   `interface=ether1`: Specifies the parent interface.
    *   `name=vlan-68`: Assigns a name to the VLAN interface.
    *   `vlan-id=68`: Specifies the VLAN ID.
*  **`/ip address add ...`**: Assigns an IP address to the interface.
    * `address=61.249.70.1/24`: IP address and subnet mask for the interface.
    * `interface=vlan-68`: Specifies the interface to assign the IP to.
    * `network=61.249.70.0`: Specifies the network address.
*   **`/ip dhcp-server add...`**: Creates a DHCP server instance.
    *   `address-pool=default`: Specifies the address pool to use.
    *   `interface=vlan-68`: Specifies the interface the server is listening on.
    *   `lease-time=1d`: Sets the DHCP lease time to one day.
    *    `name=mac-server-vlan68`: Assigns a name to the DHCP server instance for easy identification.
    *    `server-type=mac`: Sets the DHCP server type to MAC mode.
*   **`/ip dhcp-server lease add...`**: Creates a static MAC-to-IP lease entry.
    *   `address=61.249.70.10`: The IP address to be assigned.
    *   `mac-address=00:11:22:33:44:55`: The client's MAC address.
    *   `server=mac-server-vlan68`: The DHCP server to assign it to.

## Common Pitfalls and Solutions:

*   **Incorrect Interface:** If the MAC server is assigned to the wrong interface, clients won't receive addresses. Verify the `interface` parameter in the `/ip dhcp-server` configuration.
*   **MAC Address Mismatches:**  Double-check MAC addresses in `/ip dhcp-server lease`. Typos are common, use copy paste and verify carefully.
*   **Address Conflicts:** If static IPs conflict with other manually assigned IPs or pool ranges on the same network, clients may not be able to connect to the network. Verify address assignments and adjust configurations accordingly.
*  **DHCP Leases Not Appearing**: If the client is already using the network it will have a DHCP lease from a different DHCP server. Clients need to be restarted in order to obtain a DHCP address from the MAC server.
*   **Server Disabled:** Check that DHCP server is enabled and that the `server-type` is `mac`.

## Verification and Testing Steps:

1.  **Connect a Client:** Connect a device with a MAC address specified in the leases to the `vlan-68` network. Ensure the device's network configuration is set to obtain an IP address automatically via DHCP.
2. **Verify DHCP Lease** After the client has connected to the network and has obtained an IP address, check `/ip dhcp-server lease print` to ensure that the MAC server lease is correctly listed, that the assigned IP is correct and that it matches the client.
3.  **Ping Test:** Once the device has its IP address, use a `ping` command on the router to verify communication.
    ```mikrotik
    ping 61.249.70.10
    ```
    If you have multiple devices, ping them too to ensure that all MAC server assignments are working correctly.
4.  **Torch Tool:** Use the Torch tool on the `vlan-68` interface on the router to monitor DHCP traffic:

    ```mikrotik
    /tool torch interface=vlan-68 protocol=udp port=67
    ```

    This helps visualize DHCP requests and responses.
5.   **Client IP Check:**  Check the assigned IP address on the client to confirm it received the statically assigned IP.

## Related Features and Considerations:

*   **DHCP Option Sets**: You can use DHCP Options to provide additional information to clients like DNS servers, NTP servers and so on.
*   **Address Pools:** If you need a range of dynamically assigned addresses in addition to the static MAC-based IPs, you could create a specific IP address pool for the `vlan-68` interface and add it to the DHCP Server configuration. Be sure that this pool does not overlap with the assigned static addresses.
*   **RADIUS Integration:** For larger networks with more complex authentication, consider integrating RADIUS with the DHCP server for authorization policies.
*   **Hotspot Feature:**  You can combine the MAC server with Hotspot functionality for specialized client access control.
*   **Multiple MAC servers**: You can have multiple mac servers configured on the same device.

## MikroTik REST API Examples:

Here's how to create a MAC server and lease via the MikroTik REST API:

**1. Create a MAC Server:**

*   **API Endpoint:** `/ip/dhcp-server`
*   **Method:** `POST`
*   **JSON Payload:**
    ```json
    {
      "address-pool": "default",
      "interface": "vlan-68",
      "lease-time": "1d",
      "name": "mac-server-vlan68-api",
      "server-type": "mac"
    }
    ```

*   **Expected Response (Success 201 Created):**
    ```json
    {
      "id": "*1a",
      "address-pool": "default",
      "interface": "vlan-68",
      "lease-time": "1d",
      "name": "mac-server-vlan68-api",
      "server-type": "mac",
      "authoritative":"yes"
    }
    ```
* **Handling Errors**: Check for error status codes and detailed error messages in the response body, such as an `interface` not existing or `name` already being used.

**2. Create a Static MAC to IP Lease:**

*   **API Endpoint:** `/ip/dhcp-server/lease`
*   **Method:** `POST`
*   **JSON Payload:**
    ```json
    {
      "address": "61.249.70.30",
      "mac-address": "00:11:22:33:44:66",
      "server": "mac-server-vlan68-api"
    }
    ```

*   **Expected Response (Success 201 Created):**
    ```json
    {
        "id": "*1b",
        "address": "61.249.70.30",
        "mac-address": "00:11:22:33:44:66",
         "server": "*1a",
    }
    ```
* **Handling Errors**: Check for errors like duplicate MAC addresses, wrong server name, or invalid IPs.

**3. Get Server Information**

*   **API Endpoint**: `/ip/dhcp-server?name=mac-server-vlan68-api`
*   **Method:** `GET`
*   **Expected Response**: A JSON object containing the DHCP server information.

**4. Get Leases Information**

*   **API Endpoint**: `/ip/dhcp-server/lease`
*   **Method:** `GET`
*   **Expected Response**: A JSON array of all leases, including static leases.

## Security Best Practices

*   **MAC Spoofing:** Be aware that MAC addresses can be spoofed. This makes MAC address authentication less secure than other methods like RADIUS. Implement additional access control mechanisms if this is a concern.
*   **Limit Access:**  Restrict access to the router's configuration interface (Winbox, WebFig, SSH) with strong passwords and firewalls.
*   **Regular Updates:** Keep the RouterOS software updated to ensure security patches are applied and bugs are fixed.
*   **Disable Unused Services:** Disable all unused services to reduce attack surface.

## Self Critique and Improvements

*   **Address Pool:** The configuration uses a simple IP address and does not specify an address pool for dynamically assigned addresses. We could improve the example to include the usage of a custom pool for this subnet.
*   **Advanced Logging**: Could be improved by adding more detailed logging to improve fault finding.
*   **More Parameters:** Add a section describing all optional parameters to the command, this is especially useful for more complex features.
*   **Dynamic Leases:**  The configuration only covers static IP assignments with MAC addresses, if there are multiple clients, this may be problematic. Adding a DHCP address pool will allow for dynamic assignments of IPs in addition to MAC to IP assignments.

## Detailed Explanations of Topic

A MAC server, in the context of MikroTik RouterOS, is a specialized type of DHCP server that assigns IP addresses based solely on the client’s MAC address. Unlike a traditional DHCP server that might assign addresses based on a first-come, first-served basis or based on a predefined pool, a MAC server directly maps specific MAC addresses to specific IP addresses.

This is ideal for environments where devices need to always receive the same IP address without relying on static IPs configured at the client or static DHCP leases. MAC servers are typically used in:

*   **Controlled Environments:** Where you want to guarantee the same IP address for specific hardware, such as printers, servers, or IoT devices.
*   **Testing Environments:** Where you need a predictable IP addressing scheme.
*   **Small-Scale Managed Networks:** In SMB or SOHO setups, it simplifies the management of specific devices' network identities.
*   **Access Control**: In conjunction with other features, such as Hotspot, MAC servers can be used for device-based access policies.

Key characteristics of a MikroTik MAC server:

*   **Direct MAC to IP Mapping:** The core function is linking MAC addresses to IP addresses, so a lease is assigned before the DHCP client makes its first request.
*   **No Dynamic IP Assignments:**  Unless you also configure a DHCP address pool, the MAC server only leases IPs based on MAC address.
*   **Configured via CLI or Winbox**: You create and configure it using the MikroTik CLI and Winbox GUI tools.
*   **Lease Management:** The `lease` function of the DHCP server is used to configure the mappings.
*   **Simplicity:** Easier to implement and maintain than many other methods of IP assignment.

## Detailed Explanation of Trade-offs

When choosing to use a MAC server, it's important to understand the trade-offs:

*   **Static vs. Dynamic:**
    *   **MAC Server (Static):** Guarantees the same IP address to a specific MAC address. It's predictable but less flexible. This is generally considered less secure than a proper RADIUS based approach to authentication.
    *   **Traditional DHCP (Dynamic):** Assigns addresses from a pool, making better use of IP address space but less predictable.
    *   **Trade-off:** Choosing between predictability and efficient resource utilization. A combination of these can be used to get the best of both worlds.
*   **MAC Server vs Static IP Assignments on Client:**
    *   **MAC Server:** Centralized and easier to manage, less error-prone as settings are all in the same place. The clients do not need to be aware of settings or have complicated IP assignments.
    *   **Static IPs (Client):** Device specific, may cause address conflicts if not carefully managed, and requires more configuration to be performed by different users.
    *   **Trade-off:** Centralized management with the MAC server vs. local control on individual clients.
*   **Security**:
    *   **MAC Address Based Security:** MAC addresses can be easily spoofed, this makes MAC address based authentication not secure by itself.
    *   **RADIUS Authentication:** RADIUS based authentication is more robust and reliable, especially on bigger networks.
    *   **Trade-off:** Simplicity of MAC based authentication, vs the complexity of other authentication methods such as RADIUS.
*   **Scalability**:
    *   **MAC Server:** The number of MAC addresses must be configured manually, this configuration can be time consuming on bigger networks.
    *   **RADIUS Authentication:** Can be much more scalable and robust than simple MAC address assignments.
    *  **Trade-off:** Simplicity of smaller networks vs. more scalability of bigger networks.

## Configuration for Specific RouterOS Versions:

This documentation targets RouterOS 7.12 (and also applies to 6.48 and other 7.x versions). The basic DHCP server functionality and MAC server type configurations have been relatively consistent across these versions. If, in the future, a new version introduces breaking changes or deprecated commands, those specific changes should be noted and accounted for. The commands here are considered stable and safe in all supported versions.
