Okay, let's dive into configuring a MAC Server on MikroTik RouterOS 7.12, focusing on the provided scenario.

## Scenario Description

We need to configure a MAC server on the `wlan-10` interface, operating on the subnet `93.212.63.0/24`. The MAC server will respond to MAC address requests on this interface and should be used for DHCP lease management, with a focus on a typical ISP-like scenario where certain devices may require static IP addresses based on their MAC address. This setup will allow for assigning specific IP addresses based on MAC address through DHCP.

## Implementation Steps

Here's a step-by-step guide on how to configure the MAC server:

### Step 1: Verify the Interface and IP Configuration

Before proceeding, let's confirm the current status of the `wlan-10` interface and ensure that it has an IP address on the correct subnet.

**CLI Before:**

```
/interface print
/ip address print
```

**Example Output:**

```
# /interface print
Flags: D - dynamic, X - disabled, R - running, S - slave
 #     NAME                                TYPE       MTU  L2MTU  MAX-L2MTU
 0  R   ether1                              ether      1500  1598    1598
 1  R   wlan1                               wlan       1500  1598    1598
 2     wlan-10                              wlan       1500  1598    1598


# /ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24    192.168.88.0    ether1
```
**GUI Before (Winbox):**
- In Winbox, go to `/Interfaces` to see the interface list, and to `/IP/Addresses` to view the configured IP addresses.

**Explanation:**

*   We use `/interface print` to check that wlan-10 exists, and `/ip address print` to see if there are any addresses configured on the interface. In this example, we need to make sure `wlan-10` is active and has an IP address in the desired range of 93.212.63.0/24.

**CLI Action:**
If there is no IP address on the `wlan-10` interface, we need to configure it. We'll assign a static IP of 93.212.63.1/24:

```
/ip address add address=93.212.63.1/24 interface=wlan-10
/interface set wlan-10 enabled=yes
```

**CLI After:**
```
# /ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24    192.168.88.0    ether1
 1   93.212.63.1/24     93.212.63.0     wlan-10

# /interface print
Flags: D - dynamic, X - disabled, R - running, S - slave
 #     NAME                                TYPE       MTU  L2MTU  MAX-L2MTU
 0  R   ether1                              ether      1500  1598    1598
 1  R   wlan1                               wlan       1500  1598    1598
 2  R   wlan-10                              wlan       1500  1598    1598
```
**GUI After (Winbox):**
- In Winbox, you will now see that `wlan-10` is active, and the configured IP address under `/IP/Addresses`.

**Explanation:**

*   We added an IP address to the `wlan-10` interface on our desired subnet.

### Step 2: Configure the MAC Server

Now, let's configure the MAC server to listen on the `wlan-10` interface.

**CLI Before:**
```
/ip dhcp-server mac-server print
```

**Example Output:**
```
Flags: X - disabled, I - invalid
 #   INTERFACE                   DHCP-SERVER  USE-DHCP-LEASE
```

**Explanation:**
* We use the `/ip dhcp-server mac-server print` command to verify if a mac-server already exists and what settings are configured.

**CLI Action:**
```
/ip dhcp-server mac-server add interface=wlan-10 use-dhcp-lease=yes
```

**CLI After:**
```
# /ip dhcp-server mac-server print
Flags: X - disabled, I - invalid
 #   INTERFACE                   DHCP-SERVER  USE-DHCP-LEASE
 0   wlan-10                     yes          yes
```

**GUI After (Winbox):**
- You'll find this configuration under `/IP/DHCP Server/MAC Server` in Winbox. You should see that `wlan-10` is now included in this list.

**Explanation:**

*   We've created a new MAC server entry, binding it to the `wlan-10` interface.
*   `use-dhcp-lease=yes` makes the MAC server respect existing leases and provide consistent IP addresses.

### Step 3: Configure DHCP Server for Static Leases (Optional, Recommended)

While not strictly necessary for the MAC server itself, configuring a DHCP server for the subnet allows for automatic lease assignment, and allows setting static leases based on mac address.
**CLI Before:**
```
/ip dhcp-server print
```

**Example Output:**
```
Flags: X - disabled, I - invalid
 #   NAME                 INTERFACE                 RELAY  ADDRESS-POOL       LEASE-TIME
```

**Explanation:**
* We use the `/ip dhcp-server print` command to verify if a dhcp-server already exists.

**CLI Action:**
```
/ip dhcp-server add address-pool=dhcp_pool_wlan10 interface=wlan-10 name=dhcp_wlan10
/ip pool add name=dhcp_pool_wlan10 ranges=93.212.63.10-93.212.63.254
/ip dhcp-server network add address=93.212.63.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=93.212.63.1
```

**CLI After:**
```
# /ip dhcp-server print
Flags: X - disabled, I - invalid
 #   NAME                 INTERFACE                 RELAY  ADDRESS-POOL       LEASE-TIME
 0   dhcp_wlan10              wlan-10                         dhcp_pool_wlan10     10m
```
**Explanation:**
- We created a new dhcp-server pool and network for wlan-10, which assigns addresses to connected clients and allows us to add static leases via mac address.

### Step 4: Test the Configuration
Make a test connection from a device and verify that it obtains an IP address from the DHCP server.
Check the leases with:
```
/ip dhcp-server lease print
```
If the test device is on the network, it will appear in the DHCP server leases.
You can then configure a static lease for the MAC address of the test device in the leases.

## Complete Configuration Commands

Here's the complete set of CLI commands:

```
/ip address add address=93.212.63.1/24 interface=wlan-10
/interface set wlan-10 enabled=yes
/ip dhcp-server mac-server add interface=wlan-10 use-dhcp-lease=yes
/ip dhcp-server add address-pool=dhcp_pool_wlan10 interface=wlan-10 name=dhcp_wlan10
/ip pool add name=dhcp_pool_wlan10 ranges=93.212.63.10-93.212.63.254
/ip dhcp-server network add address=93.212.63.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=93.212.63.1
```

## Parameter Explanation:

| Command                        | Parameter        | Value                    | Explanation                                                      |
|--------------------------------|------------------|--------------------------|------------------------------------------------------------------|
| `/ip address add`             | `address`        | `93.212.63.1/24`         |  IP address and subnet mask for the interface.                      |
|                                | `interface`      | `wlan-10`                | The interface to assign the IP address to.                      |
| `/interface set`               | `wlan-10`       | `enabled=yes`           | Enable the specified interface.                   |
| `/ip dhcp-server mac-server add`| `interface`      | `wlan-10`                | The interface on which the MAC server listens.                 |
|                                | `use-dhcp-lease` | `yes`                    |  Use the leases from the DHCP server.                             |
| `/ip dhcp-server add`         |`address-pool`  | `dhcp_pool_wlan10`         | The address pool for the DHCP server.                             |
|                               | `interface`  | `wlan-10`       | The interface on which to enable the DHCP server.                               |
|                               | `name`  | `dhcp_wlan10`       | The name of the DHCP server.                               |
|`/ip pool add`               |`name` |`dhcp_pool_wlan10` | The name of the pool to use with the DHCP server.|
|                               |`ranges` | `93.212.63.10-93.212.63.254`   |  The range of IP addresses to assign via DHCP.                      |
|`/ip dhcp-server network add` |`address` |`93.212.63.0/24` | The network address for the DHCP network.|
|                               |`dns-server`|`8.8.8.8,8.8.4.4`| The DNS servers to be provided via DHCP.|
|                               | `gateway`| `93.212.63.1` | The gateway address for the DHCP network.|

## Common Pitfalls and Solutions

*   **Incorrect Interface:** Ensure the MAC server is configured for the correct interface. Check using `/ip dhcp-server mac-server print`. If you need to change the interface, remove the old config and re-add with the correct interface.
*   **DHCP Server Not Enabled**: The MAC server functionality relies on the DHCP server. Verify the DHCP server is running on the target interface with `/ip dhcp-server print`.
*   **Lease Conflict:** Ensure IP leases are not conflicting, especially with static IP assignments.
*   **Firewall Issues:** If the MAC server is not working, check firewall rules, ensure that DHCP traffic can pass for the configured interface.
*   **High CPU/Memory:** If there are many connected clients, monitor the router's CPU and memory usage with `/system resource print`. An overloaded router can impact MAC server performance.

## Verification and Testing Steps

1.  **Device Connection:** Connect a test device to the `wlan-10` interface.
2.  **DHCP Lease Check:** Check for a DHCP lease using `/ip dhcp-server lease print` to verify that the device has received a DHCP address.
3.  **MAC Server Verification:** If the device does not appear in the leases, verify the MAC server config again with `/ip dhcp-server mac-server print`.
4.  **Static Lease Test:** Configure a static DHCP lease for the device's MAC address in `/ip dhcp-server lease`. Disconnect and reconnect the device to verify it obtains the static IP address.
5.  **Ping Test:** Ping a known device within the same network, or external devices (eg: `ping 8.8.8.8`) to test network connectivity.
6.  **Torch Tool:** If there is unexpected traffic, or to verify DHCP requests, use the `/tool torch` on interface `wlan-10`.

## Related Features and Considerations

*   **DHCP Options:** You can configure DHCP options for specific vendor classes by using `/ip dhcp-server option`.
*   **Hotspot:**  This setup can be integrated with a MikroTik Hotspot configuration.
*   **MAC Address Lists:** For more complex management, consider creating MAC address lists. These lists can be applied to firewall rules or other configurations. Use `/interface list member` and `/ip firewall address-list add`.
*   **RADIUS:**  Integrate with a RADIUS server for more advanced user management.

## MikroTik REST API Examples (if applicable):

*   **Add MAC Server:**
    *   **Endpoint:** `/ip/dhcp-server/mac-server`
    *   **Method:** `POST`
    *   **Example JSON Payload:**
    ```json
    {
        "interface": "wlan-10",
        "use-dhcp-lease": "yes"
    }
    ```
    *   **Expected Response (Success 200):**
    ```json
    {
        "message": "added",
        ".id": "*123"
    }
    ```
    * **Error Handling (example - if interface doesn't exist):**
    ```json
    {
        "message": "input does not match any value of interface",
        "error": true
    }
    ```
*   **Get MAC Server List:**
    *   **Endpoint:** `/ip/dhcp-server/mac-server`
    *   **Method:** `GET`
    *   **Expected Response:**
    ```json
    [
      {
        ".id": "*123",
        "interface": "wlan-10",
        "use-dhcp-lease": "yes",
        "dhcp-server": "yes"
      }
    ]
    ```

## Security Best Practices

*   **Secure Wireless:** Ensure the `wlan-10` interface is properly secured using WPA2/WPA3 with strong passwords.
*   **Limit Access:** Restrict access to your MikroTik router via firewalls, securing the management interface (Winbox, SSH, API).
*   **Monitor Logs:** Regularly check MikroTik logs for suspicious activity using `/log print` and `/tool e-mail send`.

## Self Critique and Improvements

*   **More Detailed DHCP Configuration:** The provided configuration could be improved by including additional DHCP server settings like lease time and dynamic DNS.
*   **Logging and Monitoring:** We could add more sophisticated logging mechanisms and alerts to monitor the MAC server's behavior and performance.
*   **Integration with other systems:** For large or production networks, this setup can be integrated with RADIUS authentication, and dynamic DNS.
*   **Further security:** Further security enhancements can be made by implementing firewall rules that restrict access based on the IP ranges.
*   **Redundancy**: This configuration could be improved by implementing additional redundant DHCP servers on secondary devices.

## Detailed Explanations of Topic

The MAC server on MikroTik routers is a DHCP server add-on that serves the purpose of identifying devices on a network based on their MAC addresses. When the MAC server is enabled, devices that connect to an interface associated with the MAC server are tracked. This is generally combined with DHCP to allow the assignment of leases that provide static IP addresses to specific MAC addresses. This is especially helpful in scenarios where certain devices require specific IP addresses and in general facilitates network management by associating IP addresses with specific devices instead of just dynamically assigning IPs.

## Detailed Explanation of Trade-offs

*   **`use-dhcp-lease=yes` vs `use-dhcp-lease=no`:**
    *   `yes`: The MAC server adheres to DHCP leases, so the IP address given is consistent with the configured DHCP lease, even if the device does not specifically send a request for the specified IP. It can also assign static leases.
    *   `no`: The MAC server does not care about DHCP leases, and responds to MAC addresses if the MAC address is in the `/ip dhcp-server lease` list with a static IP.
    *   **Trade-off:** Using `yes` provides better control, more predictability of IP assignments for devices, and better integration with static leases. Using `no` provides less control, and is less predictable.

## Configuration for Specific RouterOS Versions

This configuration is relevant to RouterOS 7.12, 6.48, and 7.x, as the relevant commands for the MAC server and DHCP server are consistent across these versions. All provided commands are available in these versions. If you use different versions, you may need to consult the MikroTik documentation for command changes or compatibility issues.

Let me know if you have any other questions or require modifications to this configuration.
