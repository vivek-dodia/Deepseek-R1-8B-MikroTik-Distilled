Okay, let's craft a comprehensive technical document on configuring a MAC server on a MikroTik RouterOS device. We'll target RouterOS 7.12, focus on a basic configuration for an SMB network, and use a subnet of 86.29.97.0/24, with interface `vlan-35` as the target interface.

## Scenario Description

This scenario involves setting up a MikroTik device as a MAC server.  A MAC server allows devices on a specific network segment to be managed based on their MAC addresses. This is useful for implementing access control, such as limiting access to only known devices, enforcing specific policies, or simplifying network administration by associating IP addresses with specific devices. It primarily works with DHCP. This scenario aims to enable basic MAC address control on the 86.29.97.0/24 network segment via the `vlan-35` interface.

## Implementation Steps

Here is a step-by-step guide on how to configure the MAC server functionality.

### Step 1: Ensure VLAN Interface is Configured

*   **Description:** The `vlan-35` interface must be properly configured and ready for use. This includes assigning it to a parent interface and setting a VLAN ID if necessary. It is assumed for simplicity that this is already configured.

*   **Before Configuration:**
    *  We will assume your `vlan-35` interface is configured and enabled. You can verify this using:

    ```mikrotik
    /interface vlan print
    ```

    Example Output:
    ```
    Flags: X - disabled, R - running
     #    NAME   MTU  MAC-ADDRESS       VLAN-ID INTERFACE
     0  R vlan-35 1500 00:0C:29:F9:75:BB 35      ether1
    ```

*   **Action**: If it doesn't exist or needs adjustment configure it. This part is specific to your network topology and is not part of the MAC server config directly, but required for this config to function.

    ```mikrotik
    /interface vlan add name=vlan-35 vlan-id=35 interface=ether1
    ```

    *   **Explanation**: This step is **crucial** since the MAC server config in the later steps *needs* this interface.
        * `name=vlan-35`: Creates a new interface named `vlan-35`.
        * `vlan-id=35`: Sets the VLAN ID to 35.
        * `interface=ether1`: Sets the parent interface to `ether1`. Change this to the appropriate parent interface for your setup.

*   **After Configuration:** `vlan-35` should appear in the interfaces list as an active interface. You can use `/interface print` to verify.

### Step 2: Configure IP Address on the VLAN Interface

*   **Description:** Assign the IP address for the subnet to the `vlan-35` interface. This is required for the network to communicate.

*   **Before Configuration:**
     ```mikrotik
    /ip address print
    ```
    ```
    Flags: X - disabled, I - invalid, D - dynamic
     #   ADDRESS            NETWORK         INTERFACE
     0   192.168.88.1/24    192.168.88.0    ether2
    ```

*   **Action:**
    ```mikrotik
    /ip address add address=86.29.97.1/24 interface=vlan-35
    ```

    *   **Explanation**:
        * `address=86.29.97.1/24`: Sets the IP address and subnet mask on the `vlan-35` interface. `86.29.97.1` is the gateway IP, and you can modify this to your needs.
        * `interface=vlan-35`: Applies this IP address to the `vlan-35` interface.

*   **After Configuration:** You should see the new IP address associated with `vlan-35`.
    ```mikrotik
    /ip address print
    ```
    ```
    Flags: X - disabled, I - invalid, D - dynamic
     #   ADDRESS            NETWORK         INTERFACE
     0   192.168.88.1/24    192.168.88.0    ether2
     1   86.29.97.1/24     86.29.97.0      vlan-35
    ```

### Step 3: Configure DHCP Server on VLAN Interface

*   **Description:** A DHCP server is essential for IP assignment to devices on the network which the MAC Server can control.

*   **Before Configuration:**
     ```mikrotik
     /ip dhcp-server print
    ```
    ```
    Flags: X - disabled, I - invalid
    ```

*   **Action:**
    ```mikrotik
    /ip dhcp-server add name=dhcp_vlan-35 interface=vlan-35 address-pool=default lease-time=10m
    /ip dhcp-server network add address=86.29.97.0/24 gateway=86.29.97.1 dns-server=8.8.8.8,8.8.4.4
    ```
    *   **Explanation**:
        *   `/ip dhcp-server add`: Creates a new DHCP server instance.
            *   `name=dhcp_vlan-35`: Assigns a name for easy reference.
            *   `interface=vlan-35`: Specifies the interface on which the DHCP server operates.
            *   `address-pool=default`: Uses the default address pool configuration (which needs to be configured if not used).
            *   `lease-time=10m`: Sets the lease time to 10 minutes.
        *   `/ip dhcp-server network add`: Creates a DHCP network configuration:
            *   `address=86.29.97.0/24`: Specifies the network range.
            *   `gateway=86.29.97.1`: Specifies the gateway IP, generally your router's IP on this subnet.
            *   `dns-server=8.8.8.8,8.8.4.4`: Sets DNS servers to Google's Public DNS. You can modify these.

*   **After Configuration:** The DHCP server is configured.
    ```mikrotik
    /ip dhcp-server print
    ```
    ```
    Flags: X - disabled, I - invalid
     #   NAME        INTERFACE ADDRESS-POOL LEASE-TIME ADD-ARP
     0   dhcp_vlan-35 vlan-35   default      10m       no
    ```

    ```mikrotik
    /ip dhcp-server network print
    ```
    ```
    Flags: X - disabled, I - invalid
     #   ADDRESS         GATEWAY        DNS-SERVER       DOMAIN
     0   86.29.97.0/24   86.29.97.1     8.8.8.8,8.8.4.4
    ```

### Step 4: Enable and Configure MAC Server

*   **Description:** This step activates the MAC server and configures its behavior.

*   **Before Configuration:**
    ```mikrotik
    /ip mac-server print
    ```
    ```
    Flags: X - disabled, I - invalid
    ```

*   **Action:**
    ```mikrotik
    /ip mac-server add interface=vlan-35 enabled=yes use-dhcp-server=yes
    ```

    *   **Explanation:**
        *   `/ip mac-server add`: Creates a new MAC server instance.
            *   `interface=vlan-35`: Specifies the interface to monitor for MAC addresses.
            *   `enabled=yes`: Enables the MAC server.
            *  `use-dhcp-server=yes`: Ties this to a DHCP server on this interface

*   **After Configuration:** The MAC server should be active.
    ```mikrotik
     /ip mac-server print
    ```
    ```
    Flags: X - disabled, I - invalid
     #   INTERFACE  ENABLED  USE-DHCP-SERVER
     0   vlan-35    yes      yes
    ```

### Step 5:  Example of a Static DHCP Leases (Optional)

*   **Description:**  You can manually add static leases based on MAC addresses for specific devices.

*  **Before Configuration:**
    ```mikrotik
   /ip dhcp-server lease print
   ```
   ```
    Flags: X - disabled, I - invalid, D - dynamic, B - backup
   ```

*   **Action:**

   ```mikrotik
    /ip dhcp-server lease add address=86.29.97.100 mac-address=00:0C:29:AA:BB:CC server=dhcp_vlan-35
    /ip dhcp-server lease add address=86.29.97.101 mac-address=00:0C:29:DD:EE:FF server=dhcp_vlan-35
   ```
   *   **Explanation:**
        *  `/ip dhcp-server lease add`: Adds a new static DHCP lease
            * `address=86.29.97.100`: the IP address to assign.
            *  `mac-address=00:0C:29:AA:BB:CC`: the MAC address of the client you want to have the assigned IP
            * `server=dhcp_vlan-35`: The DHCP server on which this rule applies
*   **After Configuration:** You can see that these rules have been added using:
    ```mikrotik
   /ip dhcp-server lease print
   ```
   ```
    Flags: X - disabled, I - invalid, D - dynamic, B - backup
    #   ADDRESS          MAC-ADDRESS       SERVER    HOSTNAME
    0  86.29.97.100    00:0C:29:AA:BB:CC    dhcp_vlan-35
    1  86.29.97.101    00:0C:29:DD:EE:FF    dhcp_vlan-35
   ```
   *  Note, The DHCP service *must* be configured prior to adding static leases.

## Complete Configuration Commands

Here is the complete set of MikroTik CLI commands to implement the setup, with parameter explanations:

```mikrotik
# VLAN Configuration
/interface vlan add name=vlan-35 vlan-id=35 interface=ether1

# IP Address Configuration
/ip address add address=86.29.97.1/24 interface=vlan-35

# DHCP Server Configuration
/ip dhcp-server add name=dhcp_vlan-35 interface=vlan-35 address-pool=default lease-time=10m
/ip dhcp-server network add address=86.29.97.0/24 gateway=86.29.97.1 dns-server=8.8.8.8,8.8.4.4

# MAC Server Configuration
/ip mac-server add interface=vlan-35 enabled=yes use-dhcp-server=yes

# Example Static Leases
/ip dhcp-server lease add address=86.29.97.100 mac-address=00:0C:29:AA:BB:CC server=dhcp_vlan-35
/ip dhcp-server lease add address=86.29.97.101 mac-address=00:0C:29:DD:EE:FF server=dhcp_vlan-35
```

*   **`interface vlan add`**: Creates a new VLAN interface
    *   `name`: The name of the interface
    *   `vlan-id`: VLAN ID
    *   `interface`: Parent interface to the vlan
*   **`ip address add`**: Adds an IP address to an interface.
    *   `address`:  IP address in CIDR notation (e.g., 192.168.1.1/24).
    *   `interface`: The interface this IP address is assigned to.
*   **`ip dhcp-server add`**: Configures the DHCP server.
    *   `name`: A user-defined name for the DHCP server.
    *   `interface`: The interface where the DHCP server is active.
    *   `address-pool`: Which pool of addresses to provide, `default` will be used if not defined explicitly
    *   `lease-time`:  Duration the leases are active, in minutes, hours, etc.
*   **`ip dhcp-server network add`**:  Configures DHCP network options.
    *   `address`: IP subnet in CIDR notation (e.g., 192.168.1.0/24)
    *   `gateway`: Gateway address for clients on the network.
    *   `dns-server`: DNS server addresses assigned to DHCP clients
*   **`ip mac-server add`**: Enables the MAC server feature.
    *   `interface`: Interface to monitor for MAC addresses
    *   `enabled`: Turn the MAC Server on or off
    *   `use-dhcp-server`: Ties the mac-server to a DHCP server on the selected interface
*    **`ip dhcp-server lease add`**: Configures a static DHCP lease.
    *   `address`: The IP address to assign.
    *   `mac-address`: The MAC address for which to assign this address
    *   `server`: The DHCP server instance for which this static assignment applies.

## Common Pitfalls and Solutions

*   **Pitfall:** Incorrect Interface Configuration: If `vlan-35` is not configured correctly or the parent interface is wrong, the MAC server and DHCP will not work.
    *   **Solution:** Double-check the `vlan-35` interface settings, especially the parent interface, `vlan-id`, and ensure it is enabled. Use `/interface print` to verify the status of your interfaces.
*   **Pitfall:** DHCP server not configured or misconfigured. This can lead to network devices not getting IP addresses.
    *   **Solution**: Verify the `ip dhcp-server` configuration using `/ip dhcp-server print` and `ip dhcp-server network print`.  Check that the interface and address pool are correctly set, and that the `dns-server` entries are valid for your network. Also verify the gateway ip.
*   **Pitfall:** Incorrect MAC Addresses in Static Leases:  Typographical errors in MAC addresses will cause the wrong devices to get the static IP or not get an IP at all if using static assignments.
    *   **Solution:** Double-check the static lease entries in `/ip dhcp-server lease print` and verify them against your connected devices, you can use `/tool mac-scan` to get the mac addresses of clients on the network.
*    **Pitfall:** Resource Issues: If the number of managed devices is excessive, this can increase CPU load.
    *   **Solution**: Monitor your routers CPU usage by using `/system resource print`, and consider upgrading the hardware to a more capable router, or reducing the scope of the mac server if the load becomes a problem.
*  **Security Issues**: Ensure DHCP and MAC server configurations don't allow unauthorized devices to obtain IP addresses.
    *  **Solution:** If you are using MAC address based filtering, make sure that the MAC addresses are well controlled, and make sure that all critical devices use static leases.

## Verification and Testing Steps

1.  **Interface Status**: Verify the `vlan-35` interface is running using `/interface print`.
2.  **IP Address**: Check that the correct IP address `86.29.97.1/24` is configured on `vlan-35` using `/ip address print`.
3.  **DHCP Server**: Ensure the DHCP server is enabled using `/ip dhcp-server print` and the associated network config using `/ip dhcp-server network print`.
4.  **MAC Server Status:** Verify the MAC server is enabled using `/ip mac-server print`.
5.  **DHCP Lease**: Connect a client device to the `vlan-35` network. Check the DHCP lease table using `/ip dhcp-server lease print`. If the client receives an IP address that is in the correct subnet, then the basic config is working correctly.
6. **Static DHCP Leases**: Check if the static leases assigned to the configured mac addresses appear in the table with the IP assigned to the MAC address.
7. **Ping Test**: From the MikroTik router (or any device on the same network), try to ping a client on the `86.29.97.0/24` network (`ping 86.29.97.x`). This confirms the basic network connectivity.
8. **Device Ping**: From a client device on the network `86.29.97.0/24`, try to ping the router's IP on this network ( `ping 86.29.97.1`).
9.  **Torch**: Use the `/tool torch` on the `vlan-35` interface to observe DHCP traffic as devices obtain IP addresses.

## Related Features and Considerations

*   **Address Lists:** You can combine MAC server functionality with address lists to create dynamic access rules. For example, you can allow access to specific services only from devices with a known MAC address.
*   **Firewall Rules**: You can use firewall rules with source MAC address filtering, however using the mac server with DHCP provides a simpler way to assign IPs based on MAC addresses.
*  **Hotspot**: This configuration can be adapted for a hotspot environment by extending it to include Hotspot server configurations and associating them with the MAC server rules.
*  **PPPoE Server**: This configuration can be adapted for a PPPoE environment by extending it to include PPPoE server configurations and associating them with the MAC server rules.

## MikroTik REST API Examples

While basic MAC server configuration doesn't have a direct API endpoint for "MAC server", you can access and modify DHCP server and address information:

**1. Get DHCP Server Configuration:**

*   **Endpoint:** `/ip/dhcp-server`
*   **Method:** GET
*   **Example:**

    ```json
    {
      "request": {
        "method": "GET",
         "path":"/ip/dhcp-server"
      }
    }
    ```
*   **Response:**

    ```json
    [
      {
        ".id": "*2",
        "name": "dhcp_vlan-35",
        "interface": "vlan-35",
        "address-pool": "default",
        "lease-time": "10m",
        "add-arp": "no",
        "disabled": "no"
      }
    ]
    ```
*   **Explanation**:
    * Returns all DHCP servers in a JSON list
    * Each parameter represents one configuration option
    * You can get the `ID` to use in subsequent requests.

**2. Add a DHCP Lease:**

*   **Endpoint:** `/ip/dhcp-server/lease`
*   **Method:** POST
*   **Example Request:**

    ```json
    {
      "request": {
        "method": "POST",
        "path":"/ip/dhcp-server/lease",
        "payload":{
                "address":"86.29.97.200",
                "mac-address":"00:0C:29:AA:BB:01",
                "server":"dhcp_vlan-35"
            }
      }
    }

    ```
*   **Expected Response:**
   ```json
     {
        "success": true,
        "message": "Added",
        "id": "*3"
     }
   ```
*   **Explanation:**
    *   This creates a new static lease in the dhcp server
    *   The returned ID can be used for subsequent operations
    * `address` The ip to assign
    * `mac-address` The mac address to use to provide the ip
    * `server`: The server the lease is for

**3. Error Handling:**

* If the request format is incorrect the API will respond with an HTTP 400, 404, or 500 error.
* Error response is usually in `text/plain` format, and the message will be an error from RouterOS
* You should always validate the inputs provided to the API in your code, and check the response to determine whether the operation was successful.

**NOTE**: MikroTik API is not as RESTful, and is a very thin abstraction layer over the command line. There is a good deal of nuance not immediately obvious, but this is the most complete and correct representation of these operations using the API.

## Security Best Practices

*   **Limit Access:** Restrict access to the MikroTik router using secure passwords, firewall rules, and limited login methods like SSH keys instead of passwords.
*  **Monitor Logs:** Regularly review system logs for any unusual activity related to the DHCP server and MAC addresses.
*  **Avoid Broad Access:** Don't allow direct access to sensitive network components from the broader internet. Use VPNs or other secure methods for remote access.
*  **Keep RouterOS Updated:** Keep the MikroTik RouterOS updated with the latest stable version to patch any security vulnerabilities.
*  **Use VLANs:** Segment your network using VLANs to limit the potential impact of a compromised device.
* **Limit DHCP Scope**: Do not make the DHCP scope any larger than it needs to be.
* **Use Static Addresses:**  If some devices do not move, or require a static ip for a specific service (like a print server), use static DHCP leases.

## Self Critique and Improvements

This configuration provides a basic implementation of a MAC server. Here are some improvements and further modifications:

*   **More Complex Filtering**: Enhance the mac-server to use custom address lists and firewall rules for more fine-grained control.
*   **Logging**: Implement detailed logging for DHCP assignments and MAC address events for audit purposes.
*   **Dynamic Address Lists:** Develop a dynamic system that automatically populates address lists based on MAC address detection by the MAC server.
*   **Scripting**: Implement scripts that will send notifications (emails, SMS, push notifications) on certain events such as rogue devices connecting on the network.
*  **Dynamic DNS updates**: Configure the router to provide DDNS updates for specific addresses that are given based on DHCP and MAC addresses.
*  **Centralized Management:** If operating several Mikrotiks, use a centralized management solution such as The Dude or MikroTik's Cloud Management for managing device configurations.
* **Increase Lease Time**: Increasing lease times will reduce the load on the router, however it might make it harder to remove a client from the network.

## Detailed Explanations of Topic

**MAC Server:**
* A MAC server, in the context of MikroTik RouterOS, is a feature that allows you to monitor and manage network devices based on their MAC addresses.
* The mac-server primarily works with the DHCP server, allowing you to assign static addresses based on a client's MAC address.
* This enables features such as filtering, access control, and easier device management based on network hardware.

## Detailed Explanation of Trade-offs

*   **Static Leases vs. Dynamic Assignments:** Static DHCP leases provide predictable IP address assignments but are more complex to manage. Dynamic leases, while easier to configure, might result in different IP addresses over time if a device isn't static. The Mac Server, working with the DHCP server provides a good balance, allowing the use of static leases while also allowing dynamic IP assignments.
*  **Lease Time**: Longer lease times reduce the amount of work the router needs to perform (renewing leases), but can be problematic if you have to quickly remove a client device, or require that the same device always has a specific ip address.
*   **Overly Strict MAC Filtering vs. Open Access**: Too strict MAC filtering can complicate network usage if new devices need to be added frequently. An overly open configuration risks unauthorized access. The right balance will depend on the requirements of the network.
*   **Router Resource Usage**: Complex MAC address rules can put load on the router, it's essential to evaluate whether the router has the capacity to perform all the needed network functions.

## Configuration for Specific RouterOS Versions

The commands provided in this document are compatible with RouterOS 7.12 (and are generally compatible with 6.48 and 7.x). There are no differences relevant to this config among those versions.

This comprehensive documentation should equip you with the knowledge to configure and manage a basic MAC server on your MikroTik device. Remember to test and verify your configuration in a controlled environment before deploying in a production setting.
