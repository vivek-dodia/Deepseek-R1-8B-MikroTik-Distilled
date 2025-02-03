Okay, let's dive deep into configuring a MAC server on a MikroTik router with a focus on practical, real-world implementation for an ISP network, using RouterOS v7.11 (and keeping in mind v6.48 and other v7.x versions).

## Scenario Description:

We need to configure a MAC server on our MikroTik router. A MAC server is used to provide IP addresses, DNS servers, and other network configuration information to devices based on their MAC addresses. This is useful in scenarios where you want to assign static IP addresses to specific devices based on their MAC address, without the complexity of manually managing static IP bindings or relying entirely on DHCP. In an ISP environment, this can be used to provide specific IP addresses for customer routers or other devices for static IP service, such as servers or fixed IPs.

## Implementation Steps:

Here's a detailed step-by-step guide to configuring the MAC server:

### 1. Step 1: Add a DHCP Server for the target subnet

* **Why:** The MAC server needs a DHCP server to hand out leases. It intercepts requests from the DHCP server for MAC addresses that it has configured.
* **Before:** Initially, a DHCP server must be configured for the specified subnet, to establish a baseline.
* **CLI:**
    ```mikrotik
    /ip dhcp-server
    add address-pool=default disabled=no interface=vlan-32 lease-time=1d name=dhcp-vlan-32
    /ip dhcp-server network
    add address=223.203.225.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=223.203.225.1
    ```
* **Winbox:**
    * Navigate to IP -> DHCP Server.
    * Click the "+" button to add a new DHCP server:
        * **Name:** `dhcp-vlan-32`
        * **Interface:** `vlan-32`
        * **Address Pool:** `default`
        * **Lease Time:** `1d`
    * Click "OK".
    * Navigate to IP -> DHCP Server -> Networks tab.
    * Click the "+" button to add a new network configuration:
        * **Address:** `223.203.225.0/24`
        * **Gateway:** `223.203.225.1`
        * **DNS Servers:** `8.8.8.8,8.8.4.4`
    * Click "OK".
* **Effect:** A DHCP server `dhcp-vlan-32` is created, servicing the subnet 223.203.225.0/24 on the interface vlan-32. The server is now ready to be used with the MAC server.
* **After:**
    ```mikrotik
    /ip dhcp-server
    print
    # Flags: X - disabled, I - invalid
    # 0   name="dhcp-vlan-32" interface=vlan-32 address-pool=default lease-time=1d disabled=no
    /ip dhcp-server network
    print
    # Flags: X - disabled, D - dynamic
    # 0   address=223.203.225.0/24 gateway=223.203.225.1 dns-server=8.8.8.8,8.8.4.4 wins-server="" domain=""
    ```

### 2. Step 2: Enable the MAC Server

* **Why:** Enables the MAC server functionality on the router
* **Before:** The MAC server is not active, no MAC address is assigned a static IP.
* **CLI:**
    ```mikrotik
    /ip mac-server
    set enabled=yes
    ```
* **Winbox:**
    * Navigate to IP -> MAC Server
    * Check the box labelled "Enabled"
    * Click "Apply" and "OK"
* **Effect:** The MAC server is now active and listening for DHCP requests. It is however still not doing anything since it has not been configured to manage specific MAC addresses.
* **After:**
    ```mikrotik
    /ip mac-server
    print
    #                enabled: yes
    ```

### 3. Step 3: Add MAC Address Entries

* **Why:** Configure the specific MAC addresses and their associated IP configurations.
* **Before:** The MAC server does not contain entries. Any device connected will get an IP assigned by the DHCP server.
* **CLI:**

    ```mikrotik
    /ip mac-server entry
    add mac-address=00:11:22:33:44:55 address=223.203.225.10 dns-server=1.1.1.1 comment="Device A"
    add mac-address=AA:BB:CC:DD:EE:FF address=223.203.225.20 comment="Device B"
    ```
* **Winbox:**
    * Navigate to IP -> MAC Server -> Entries Tab
    * Click the "+" button to add a new entry:
        * **Mac Address:** `00:11:22:33:44:55`
        * **Address:** `223.203.225.10`
        * **DNS Server:** `1.1.1.1`
        * **Comment:** `Device A`
    * Click "OK"
    * Click the "+" button again to add the next entry:
       *  **Mac Address:** `AA:BB:CC:DD:EE:FF`
       * **Address:** `223.203.225.20`
       * **Comment:** `Device B`
    * Click "OK".

* **Effect:** Devices with the MAC addresses 00:11:22:33:44:55 and AA:BB:CC:DD:EE:FF will receive the specified IP configurations when they perform a DHCP request. If the DHCP server has already leased an address to either device, the MAC server will send a DHCP NAK message and the client will request a new IP.

* **After:**
    ```mikrotik
    /ip mac-server entry
    print
    # Flags: X - disabled
    # 0   mac-address=00:11:22:33:44:55 address=223.203.225.10 dns-server=1.1.1.1 comment="Device A"
    # 1   mac-address=AA:BB:CC:DD:EE:FF address=223.203.225.20 dns-server="" comment="Device B"
    ```

## Complete Configuration Commands:

```mikrotik
# Configure DHCP Server
/ip dhcp-server
add address-pool=default disabled=no interface=vlan-32 lease-time=1d name=dhcp-vlan-32
/ip dhcp-server network
add address=223.203.225.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=223.203.225.1

# Enable MAC Server
/ip mac-server
set enabled=yes

# Add MAC Server Entries
/ip mac-server entry
add mac-address=00:11:22:33:44:55 address=223.203.225.10 dns-server=1.1.1.1 comment="Device A"
add mac-address=AA:BB:CC:DD:EE:FF address=223.203.225.20 comment="Device B"
```

*   **`/ip dhcp-server add`**: Creates a new DHCP server instance.
    *   `address-pool=default`: Uses the default address pool.
    *   `disabled=no`: Enables the DHCP server.
    *   `interface=vlan-32`: The interface to listen for DHCP requests.
    *   `lease-time=1d`: The DHCP lease time (1 day).
    *   `name=dhcp-vlan-32`: The name for the DHCP server.
*   **`/ip dhcp-server network add`**: Configures the network parameters for the DHCP server.
    *   `address=223.203.225.0/24`: The network address and subnet.
    *   `dns-server=8.8.8.8,8.8.4.4`: The DNS server IP addresses.
    *   `gateway=223.203.225.1`: The gateway IP address.
*   **`/ip mac-server set enabled=yes`**: Enables the MAC server feature globally.
*   **`/ip mac-server entry add`**: Creates an entry in the MAC server table.
    *   `mac-address`: The MAC address of the device.
    *   `address`: The static IP address assigned to the MAC address.
    *   `dns-server`: Optional DNS server for that specific device.
    *   `comment`: Optional comment.

## Common Pitfalls and Solutions:

*   **Problem:** Devices not getting the configured IP, get an address from the DHCP range instead.
    *   **Solution:**
        1.  Ensure the device is using DHCP. Verify that the MAC address of the device is correctly configured in the MAC server.
        2.  Ensure that the device has released any previously obtained DHCP lease, such as by disconnecting and reconnecting or performing an `ipconfig /release` followed by `ipconfig /renew` on the device.
        3.  Double-check the interface on which you have the MAC server activated.
        4.  Review DHCP server logs to check for errors. You can check live logs in the `/log print follow-only file=dhcp` section of the CLI.
*   **Problem:** MAC Server and DHCP server conflicts.
    *   **Solution:** The MAC Server intercepts requests for configured MAC addresses before DHCP. Ensure there are no conflicting manual IP configurations for the same MAC address elsewhere. If there are DHCP leases for the MAC address configured on the server, they will be NAK'ed by the server and will renew with the IP set on the MAC server.
*   **Problem:** Incorrect MAC address entries.
    *   **Solution:** Check your MAC address entries for typos. The MAC addresses should be in the format `XX:XX:XX:XX:XX:XX` (case-insensitive).

## Verification and Testing Steps:

1.  **Device Connection:** Connect a device with one of the configured MAC addresses to the `vlan-32` interface.
2.  **IP Configuration:**
    *   **Windows:** Open Command Prompt and use `ipconfig` to verify if the device has the correct IP (`223.203.225.10` or `223.203.225.20`), DNS, and gateway settings.
    *   **Linux/macOS:** Use `ifconfig` or `ip addr` to check IP and `cat /etc/resolv.conf` to check DNS settings.
3. **Ping Test:** From the device, use the `ping` command to test network connectivity:
    ```bash
    ping 223.203.225.1
    ping 8.8.8.8
    ```
4.  **MikroTik Tools:** On the MikroTik router:
    *   Use `/tool/ping address=223.203.225.10` to ping the device from the router.
    *  Use `/ip dhcp-server lease print` to view the DHCP leases and verify the MAC Server leased address matches the entry made on the MAC server. If there is a discrepancy, the device was likely unable to renew its previous lease and will require disconnection and reconnection to pick up the new settings.
    *  Use `/log print follow-only file=dhcp` to see the live DHCP lease requests.
5.  **Torch:** The `/tool torch` tool can be used on the interface to watch DHCP traffic and verify the client is requesting DHCP information.

## Related Features and Considerations:

*   **DHCP Leases:** The MAC server provides configurations based on DHCP requests. The leases are stored in the `/ip dhcp-server lease` section. If a device with a configured MAC address has a lease already, the MAC server will instruct the client to renew the lease. You can review all active leases in the section.
*   **Address Lists:** You can use address lists and firewall rules to manage traffic from specific MAC-addressed devices for QoS, firewall rules, or other purposes.
*   **User Manager:** If you require complex user management, consider combining this feature with the MikroTik User Manager for more granular control.
*   **DHCP Option Codes:** DHCP options codes can be included in the server configuration to provide additional settings.
*   **Alternative static routes:** If you don't require DHCP but do want a device to receive a specific IP, you can set up the static route on the device itself instead of relying on the MAC Server.

## MikroTik REST API Examples:

Here are some REST API examples.  Note, you must first enable the API on your MikroTik router.

### Example 1: Get MAC Server Configuration

*   **Endpoint:** `/ip/mac-server`
*   **Method:** `GET`
*   **Request:** None
*   **Example using `curl`:**
    ```bash
    curl -u admin:password -k "https://<router_ip>/rest/ip/mac-server"
    ```
*   **Expected Response (JSON):**
    ```json
    [
      {
        "enabled": "true",
         ".id": "*0"
      }
    ]
    ```

### Example 2: Create a MAC Server Entry

*   **Endpoint:** `/ip/mac-server/entry`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
        "mac-address": "00:11:22:33:44:66",
        "address": "223.203.225.11",
        "comment": "New Device C"
    }
    ```
*   **Example using `curl`:**
    ```bash
     curl -u admin:password -k -H "Content-Type: application/json" -d '{"mac-address":"00:11:22:33:44:66","address":"223.203.225.11","comment":"New Device C"}' "https://<router_ip>/rest/ip/mac-server/entry"
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "message": "added",
        "id": "*1"
    }
    ```
* **Error Handling:**
  If the mac-address already exists, the API will return a status code of 400 and a message of `could not add item - item with such MAC address already exists`.

### Example 3: Get MAC Server Entry

*   **Endpoint:** `/ip/mac-server/entry/<entry_id>` where `<entry_id>` is the `.id` field on the mac-server entry from the API
*   **Method:** `GET`
*   **Request:** None
*   **Example using `curl`:**
    ```bash
      curl -u admin:password -k "https://<router_ip>/rest/ip/mac-server/entry/*0"
    ```
*   **Expected Response (JSON):**
    ```json
    [
      {
        "mac-address": "00:11:22:33:44:55",
        "address": "223.203.225.10",
        "dns-server": "1.1.1.1",
        "comment": "Device A",
        ".id": "*0"
      }
    ]
    ```

## Security Best Practices:

*   **API Security:** Secure your MikroTik API with a strong password and enable HTTPS. If your device has been publicly exposed, you should disable the API.
*   **Access Control:** Restrict access to your router. Do not allow access to the router from the public internet.
*   **Firewall:** Implement a strong firewall to protect the router and the network
*   **Monitor Logs:** Monitor logs regularly for any suspicious activity.
*   **Regular Updates:** Keep RouterOS up to date.
*   **Password Policy:** Enforce strong passwords for all users. Do not use default usernames and passwords.
*   **MAC Address Verification:** Ensure the MAC addresses are correct when entering them into the MAC server.

## Self Critique and Improvements:

*   **Improvements:**
    *   **API Integration:** Automate the process of adding MAC address entries through a custom script or tool that integrates with the MikroTik API.
    *   **DHCP Pool Management:** Use multiple address pools instead of the default for more flexible IP addressing.
    *   **Scripting:** Create a custom script that takes a CSV file of MAC addresses and IP addresses and automatically loads them into the MAC server.
    *   **Alerts:** Send an email alert when a new MAC address not configured is assigned an address from the general pool.
*   **Critique:** This configuration is a basic implementation, it lacks more advanced features such as integration with other management systems and more granular IP addressing. In a large environment, a more centralized solution could provide better performance and security. It is vulnerable to errors when adding MAC addresses manually.

## Detailed Explanations of Topic:

A MAC server is used to statically configure network settings such as IP, DNS, and gateway, based on the MAC address of a requesting device. The main distinction compared to a DHCP server with static leases, is that the MAC server only provides the IP settings for a specific MAC, all other DHCP functionality remains. This allows for more granular management of network devices, and prevents accidental IP address conflicts. It is an alternative to DHCP static leases or setting the static IP on the client itself.

The MAC server function in MikroTik intercepts the DHCP requests and, if there is a matching MAC address, it returns the preconfigured IP details instead of relying on the configured address pool in the DHCP Server. It is a static mapping that doesn't change, unlike DHCP leases. It can be very useful in situations where you need specific devices to always have a certain IP, and you do not control the devices' configuration, such as a customer router connected to your ISP network.

## Detailed Explanation of Trade-offs:

*   **MAC Server vs. DHCP Static Leases:**
    *   **MAC Server:** Offers static IP assignment based on MAC address configuration, independent of DHCP leases. Provides more specific assignment based on a list of pre-configured values.
    *   **DHCP Static Leases:** Requires a DHCP server to function, and is a lease that is still managed by the DHCP server. Easier to manage if you don't need a specific list of devices.
*   **Trade-off:** MAC server is very helpful to assign specific IP addresses for a set of devices which you know in advance, DHCP is better if you want to lease IP addresses dynamically, but also statically for devices that you do not know in advance.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS 7.11 and most versions in the 7.x series, as well as 6.48, and should apply without any significant changes to other 6.x versions. Minor differences may exist in Winbox GUI.

This is a comprehensive guide that should be suitable for an ISP environment using the MikroTik RouterOS.
