Okay, let's dive into a comprehensive guide on configuring a MAC server on a MikroTik RouterOS device, specifically targeting version 7.12 (and noting compatibility with 6.48 and other 7.x versions).

## Scenario Description:

We're configuring a MikroTik router as a MAC server to provide IP address leases to devices on a point-to-point link. This link is assumed to be on the `ether-76` interface and uses the subnet `148.22.30.0/24`. The MAC server will only offer IP addresses based on device's MAC address. This setup is useful for tightly controlling IP allocations, ensuring only authorized devices get an address, and simplifies long-term IP address management.

## Implementation Steps:

Here's a step-by-step guide to implement the MAC server functionality:

**1. Step 1: Create an IP Pool for the MAC Server**

*   **Explanation:** We need to define an IP pool for the MAC server to allocate addresses from. This pool will be within the subnet `148.22.30.0/24`.
*   **Before:** No IP pool defined.
*   **Action:** Create a new IP pool named `mac-server-pool`.
*   **CLI Example:**

    ```mikrotik
    /ip pool
    add name=mac-server-pool ranges=148.22.30.10-148.22.30.254
    ```

*   **Winbox GUI:** Navigate to IP -> Pool, click the plus (+) button, enter the name `mac-server-pool`, the range `148.22.30.10-148.22.30.254`, and click OK.
*   **After:** IP pool `mac-server-pool` is created, now available for use.
*   **Expected Effect:** The IP Pool is created and available for use with a MAC Server.
*   **Specific Output:**
    ```
    [admin@MikroTik] > /ip pool print
     # NAME             RANGES                                                 
     0 mac-server-pool  148.22.30.10-148.22.30.254
    ```

**2. Step 2: Define the MAC Server Configuration**

*   **Explanation:** We'll create the MAC server, specifying the interface (`ether-76`), the address pool (`mac-server-pool`), and other parameters.
*   **Before:** No MAC server configured.
*   **Action:** Create a new MAC server instance.
*   **CLI Example:**

    ```mikrotik
    /ip mac-server
    add disabled=no interface=ether-76 pool=mac-server-pool
    ```
*   **Winbox GUI:** Navigate to IP -> MAC Server, click the plus (+) button. Select the appropriate interface `ether-76`, set the pool to `mac-server-pool`, and uncheck disabled. Click OK.
*   **After:** The MAC server is active on `ether-76` using the `mac-server-pool` IP addresses.
*   **Expected Effect:** A MAC server is active and listening for DHCP requests, assigning IPs from the pool only when a matching MAC address is found.
*   **Specific Output:**

    ```
    [admin@MikroTik] > /ip mac-server print
     Flags: X - disabled, I - invalid, D - dynamic 
     #   INTERFACE         POOL            
     0   ether-76          mac-server-pool
    ```
    
**3. Step 3: Add MAC Address Bindings**

*   **Explanation:**  Now we need to create bindings between MAC addresses and specific IP addresses. This ensures only pre-approved devices get IP addresses, and they always get the same IP.
*   **Before:** No MAC address bindings defined.
*   **Action:** Add MAC address bindings.
*   **CLI Example:**
    ```mikrotik
     /ip mac-server binding
     add address=148.22.30.100 mac-address=AA:BB:CC:DD:EE:01 server=0
     add address=148.22.30.110 mac-address=AA:BB:CC:DD:EE:02 server=0
    ```
*   **Winbox GUI:** Navigate to IP -> MAC Server -> Bindings. Click the plus (+) button. Add the MAC address, and the static address (IP) you want to bind to that MAC address. Then click OK. Add a second entry for other devices that you want to grant access to.
*   **After:** Specific MAC addresses are associated with specific IP addresses. The device with matching MAC address `AA:BB:CC:DD:EE:01` will always receive `148.22.30.100` and the device with matching MAC address `AA:BB:CC:DD:EE:02` will receive `148.22.30.110`
*    **Expected Effect:** Only the devices with specified MAC address will receive the specified IP address. 
*   **Specific Output:**
    ```
    [admin@MikroTik] > /ip mac-server binding print
    Flags: X - disabled, I - invalid, D - dynamic 
     #   MAC-ADDRESS       ADDRESS         SERVER 
     0   AA:BB:CC:DD:EE:01  148.22.30.100    ether-76 
     1   AA:BB:CC:DD:EE:02  148.22.30.110    ether-76
    ```
    

**4. Step 4: Configure the interface IP address.**

*  **Explanation:** It is mandatory to have a valid IP address set on the interface. This will be set to the first IP of the subnet. 
*  **Before:** Interface does not have IP address set.
*  **Action:** Add an IP address to the interface.
*  **CLI Example:**
    ```mikrotik
    /ip address
    add address=148.22.30.1/24 interface=ether-76
    ```
*  **Winbox GUI:** Navigate to IP -> Addresses. Click the plus (+) button. Add the interface and IP address. 
*  **After:** Interface has a valid IP address.
*  **Expected Effect:** The router will be able to communicate on the specified subnet.
*  **Specific Output:**
    ```
    [admin@MikroTik] > /ip address print
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS            NETWORK         INTERFACE
    0   148.22.30.1/24     148.22.30.0       ether-76
    ```

## Complete Configuration Commands:

```mikrotik
/ip pool
add name=mac-server-pool ranges=148.22.30.10-148.22.30.254
/ip mac-server
add disabled=no interface=ether-76 pool=mac-server-pool
/ip mac-server binding
add address=148.22.30.100 mac-address=AA:BB:CC:DD:EE:01 server=0
add address=148.22.30.110 mac-address=AA:BB:CC:DD:EE:02 server=0
/ip address
add address=148.22.30.1/24 interface=ether-76
```

**Parameter Explanations:**

| Command             | Parameter     | Description                                                                          |
| :------------------ | :------------ | :----------------------------------------------------------------------------------- |
| `/ip pool add`      | `name`         | Name of the IP pool (e.g., `mac-server-pool`).                                       |
|                     | `ranges`       | IP address range (e.g., `148.22.30.10-148.22.30.254`).                              |
| `/ip mac-server add` | `disabled`     | Set to `no` to enable the server.                                                  |
|                     | `interface`    | Interface the server is bound to (e.g., `ether-76`).                                |
|                     | `pool`         | The IP pool to draw addresses from (e.g., `mac-server-pool`).                         |
| `/ip mac-server binding add`| `address`      | Specific IP address to assign to a MAC address (e.g., `148.22.30.100`).             |
|                     | `mac-address`  | MAC address of the client device (e.g., `AA:BB:CC:DD:EE:01`).                        |
|                     | `server`       |  The MAC server ID to which the binding applies to (e.g. `0`, the first MAC server).|
| `/ip address add`   | `address`      | IP address and subnet mask (e.g., `148.22.30.1/24`).                                |
|                     | `interface`    | Interface this IP address is assigned to (e.g., `ether-76`).                        |

## Common Pitfalls and Solutions:

*   **Issue:**  Device not getting an IP address.
    *   **Solution:**
        *   Double-check the MAC address is entered correctly in the binding.
        *   Ensure the device is set to obtain IP via DHCP.
        *   Verify the IP address pool is not exhausted.
        *   Check that the specified interface is active and connected.
        *   Use `torch` on the interface ( `/tool torch interface=ether-76` ) to verify if there are any packets incoming from the device.

*   **Issue:** Duplicate IP addresses assigned.
    *   **Solution:** Ensure a device's MAC address has only one entry in the binding table. The server will not prevent duplicate IP addresses if there are two bindings with the same address set.

*  **Issue:** MAC Server not active.
   *   **Solution:** Verify the disabled flag is set to `no`.

*   **Issue:** Misconfigured subnet mask.
    *   **Solution:** Ensure that IP addresses and subnet masks are correctly configured (e.g., `148.22.30.1/24`).

*   **Issue:** Client device uses static IP Address.
   *  **Solution:** Ensure that all clients are set to acquire the IP address via DHCP.

*   **Resource Issues:** The MAC server, by itself, is not resource intensive.
    *   **Solution:** Keep the number of MAC address bindings under control, and regularly review unused entries.

**Security Considerations:**

*   **MAC Address Spoofing:** MAC addresses can be spoofed. For increased security, combine this with other security measures like firewall rules.
*   **Unauthorized devices:** If a new device with a MAC address that is not listed in the bindings connects to the network, it will not receive any IP address from the DHCP server. If you want an easy way to grant access, set a static IP address for the device and add it to the binding table.
*   **MAC Address Management**: It's crucial to maintain and periodically review the list of MAC addresses to ensure unauthorized access isn't being granted due to stale entries.

## Verification and Testing Steps:

1.  **Connect a device** to the `ether-76` interface.
2.  **Configure the device** to obtain an IP address automatically via DHCP.
3.  **Verify IP assignment:**
    *   On the device, check the assigned IP address. It should match the configured binding (e.g., `148.22.30.100` or `148.22.30.110`).
    *   On the MikroTik, check the leases using the command: `/ip mac-server binding print`
4.  **Test Connectivity:** Ping the device from the MikroTik router and vice-versa:
    *   From MikroTik: `ping 148.22.30.100`
    *   From the device, ping `148.22.30.1` (the router's IP)
5.  **Monitoring:** Use `/tool torch interface=ether-76` to check traffic on the interface and see if DHCP request are being received.

## Related Features and Considerations:

*   **DHCP Server:** The MAC server functionality can be used as an alternative to the DHCP server. It provides more control over IP addresses. The DHCP server itself can also be configured to assign static leases based on MAC addresses.
*   **Firewall:** Implement firewall rules to restrict access from unauthorized devices and to secure the network. You may need to allow forwarding traffic to devices on the `ether-76` interface.
*   **VRF (Virtual Routing and Forwarding):** For more complex setups, use VRF to segment the network logically, especially if you have multiple point-to-point links.

## MikroTik REST API Examples:

Here are examples of how to interact with the MAC server using the MikroTik REST API. It's important to note that the RouterOS API is not fully HTTP RESTful in the strict sense.

**Note:** The `/ip/mac-server/` endpoint is used to retrieve or configure mac-server configurations.

**1. Getting the current MAC Servers:**

*   **Endpoint:** `/ip/mac-server`
*   **Method:** `GET`
*   **Example:**

```
curl -k -u admin:password https://<your_router_ip>/rest/ip/mac-server
```

*   **Expected Response (JSON):**

```json
[
  {
    "interface": "ether-76",
    "pool": "mac-server-pool",
    "disabled": "false",
    ".id": "*0"
  }
]
```

**2. Adding a new MAC server**

*   **Endpoint:** `/ip/mac-server`
*   **Method:** `POST`
*   **Request Payload (JSON):**

```json
{
  "interface": "ether-77",
  "pool": "another-pool",
  "disabled": "false"
}
```

*   **Example using `curl`:**

```
curl -k -u admin:password -H "Content-Type: application/json" -X POST -d '{"interface": "ether-77", "pool": "another-pool", "disabled": "false"}' https://<your_router_ip>/rest/ip/mac-server
```

*   **Expected Response (JSON):** The response should return the new mac-server entry. An ID would be returned for the record that was just created.

```json
{
   "interface": "ether-77",
   "pool": "another-pool",
   "disabled": "false",
   ".id": "*1"
}
```

**3. Adding a MAC Binding**

*   **Endpoint:** `/ip/mac-server/binding`
*   **Method:** `POST`
*   **Request Payload (JSON):**

```json
{
  "mac-address": "AA:BB:CC:DD:EE:03",
  "address": "148.22.30.120",
  "server": "*0"
}
```
*   **Example using `curl`:**

```
curl -k -u admin:password -H "Content-Type: application/json" -X POST -d '{"mac-address": "AA:BB:CC:DD:EE:03", "address": "148.22.30.120", "server": "*0"}' https://<your_router_ip>/rest/ip/mac-server/binding
```
*   **Expected Response (JSON):** The response should return the new mac-binding entry. An ID would be returned for the record that was just created.

```json
{
  "address": "148.22.30.120",
  "mac-address": "AA:BB:CC:DD:EE:03",
  "server": "ether-76",
  ".id": "*2"
}
```

**Error Handling:**
*   If there is an error on the API call, a response with HTTP status 400 or 500 will be returned.
*   The response body will contain the error code and message.

## Security Best Practices

*   **Strong Passwords:** Always use strong passwords for your MikroTik router.
*   **Secure API Access:** Restrict API access to specific IP addresses if possible.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version to patch any security vulnerabilities.
*   **Firewall Rules:** Implement appropriate firewall rules to filter traffic.
*   **Disable Unused Services:** Disable any unused services (e.g., telnet, ftp).

## Self Critique and Improvements

The configuration is functional and achieves the objective. However, here are some improvements:

*   **Logging:**  Implement logging for DHCP events to audit connections. ( `/system logging add topics=dhcp action=memory` )
*   **Comments:**  Add comments to the configuration to describe each part (e.g., `/ip pool comment mac-server-pool comment="Pool for MAC server" `).
*   **Dynamic Address Pool:** You can also use a dynamic address pool, instead of statically setting a pool range.
*   **VRF implementation:** Consider using VRF for segmentation of the network, if multiple links are configured.

## Detailed Explanations of Topic

The MikroTik MAC server is a powerful feature designed to allocate IP addresses to clients based on their MAC addresses. It acts like a DHCP server, but only provides IP addresses based on an administrator's predefined MAC address list. This gives more control over the network, and ensures the correct IP address is always assigned to a device. A device with a MAC address that is not listed in the binding list will not receive an IP address.  This approach can improve security and address management, especially when you have devices that require a static IP but you don't want to configure that on each device manually. The MAC server is not a full DHCP server, as it is not sending broadcast messages, but rather it only responds to specific MAC address.

## Detailed Explanation of Trade-offs

*   **MAC Server vs. DHCP Server with Static Leases:**
    *   **MAC Server:** Provides strict control based only on the MAC address. Requires manual entry of devices' MAC addresses.
    *   **DHCP Server with Static Leases:** Still requires MAC address entry, however, the DHCP server acts like a traditional server, listening for client requests via broadcast messages. You can define static leases that only assign the IP address based on a given MAC address.
*   **Static IP vs. MAC Binding:**
    *   **Static IP on Device:** Requires configuring IP on the device.
    *   **MAC Binding on Router:** Provides central management and consistent IP addressing.

    In the specific scenario where you need to ensure that only specific devices get access to the network, MAC bindings provide a more secure and reliable method of controlling network access when compared to just assigning IP addresses to devices directly. MAC bindings provide a level of consistency, and simplifies management.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS versions 6.48 and later 7.x versions, including the target version 7.12. The commands and parameters used are consistent across these versions. No special adjustments are needed for specific versions. All commands, parameters and feature descriptions are valid across all those versions.

This detailed explanation should provide a solid foundation for implementing and understanding the MikroTik MAC server functionality. Remember to adjust IP addresses, interface names, and MAC addresses according to your specific environment.
