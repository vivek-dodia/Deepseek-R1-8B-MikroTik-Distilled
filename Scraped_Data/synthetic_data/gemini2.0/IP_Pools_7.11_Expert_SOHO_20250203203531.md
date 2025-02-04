Okay, let's dive into creating a detailed technical document for IP Pools on MikroTik RouterOS 7.11, focusing on a specific subnet and interface within a SOHO environment.

## Scenario Description:

We will configure a MikroTik router to manage a pool of IP addresses specifically for devices connected to a bridge interface. This will allow for the assignment of dynamic IP addresses within a designated subnet to devices connected to the bridge-44 interface. The subnet will be 235.17.167.0/24, and we will create a DHCP server to distribute these addresses automatically. This setup is typical for small office networks where devices need IP addresses assigned dynamically.

## Implementation Steps:

1.  **Step 1: Create the IP Pool.**

    *   **Purpose:** Define the range of IP addresses that will be available for assignment by the DHCP server.
    *   **CLI Command:**
        ```mikrotik
        /ip pool add name=pool-235-17-167 ranges=235.17.167.2-235.17.167.254
        ```
    *   **Winbox GUI:**
        1.  Navigate to `IP` -> `Pool`.
        2.  Click the `+` button.
        3.  Enter `pool-235-17-167` for the `Name`.
        4.  Enter `235.17.167.2-235.17.167.254` in the `Ranges` field.
        5.  Click `Apply` and `OK`.
    *   **Before:** There are no IP pools for this subnet
    *   **After:** The IP pool `pool-235-17-167` exists and contains IPs from 235.17.167.2 to 235.17.167.254
    *   **Explanation:**
        *   `/ip pool add`:  Creates a new IP address pool.
        *   `name=pool-235-17-167`: Assigns a descriptive name to the pool.
        *   `ranges=235.17.167.2-235.17.167.254`:  Specifies the usable range of IP addresses from .2 to .254 of the 235.17.167.0/24 subnet. We exclude the .1 to use for gateway and .255 because it is the broadcast address.
        *   **Note:**  The pool is not yet used by anything.

2. **Step 2: Create an IP Address on the Bridge Interface.**
   * **Purpose:** Assign an IP address to the bridge-44 interface. This will serve as the gateway address for devices using the DHCP service on this interface.
   * **CLI Command:**
    ```mikrotik
    /ip address add address=235.17.167.1/24 interface=bridge-44 network=235.17.167.0
    ```
   * **Winbox GUI:**
        1.  Navigate to `IP` -> `Addresses`.
        2.  Click the `+` button.
        3.  Enter `235.17.167.1/24` in the `Address` field.
        4.  Select `bridge-44` in the `Interface` dropdown.
        5.  Click `Apply` and `OK`.
   * **Before:** The bridge interface does not have an IP Address configured from this range.
   * **After:** The bridge-44 interface has the IP 235.17.167.1/24 configured.
   * **Explanation:**
        *   `/ip address add`:  Adds a new IP address to an interface.
        *   `address=235.17.167.1/24`:  Assigns the IP address 235.17.167.1 with a /24 subnet mask.
        *   `interface=bridge-44`: Specifies the interface to apply the IP address to.
        *   `network=235.17.167.0`: Automatically calculates the network address from the IP and subnet mask.

3.  **Step 3: Configure the DHCP Server.**

    *   **Purpose:** Create a DHCP server to automatically assign IP addresses from the created pool to devices connecting to the `bridge-44` interface.
    *   **CLI Command:**
        ```mikrotik
        /ip dhcp-server add address-pool=pool-235-17-167 interface=bridge-44 name=dhcp-235-17-167 lease-time=10m
        /ip dhcp-server network add address=235.17.167.0/24 gateway=235.17.167.1 dns-server=8.8.8.8,8.8.4.4
        ```
    *   **Winbox GUI:**
        1.  Navigate to `IP` -> `DHCP Server`.
        2.  Click the `+` button.
        3.  Enter `dhcp-235-17-167` for the `Name`.
        4.  Select `bridge-44` in the `Interface` dropdown.
        5.  Select `pool-235-17-167` in the `Address Pool` dropdown.
        6.  Set `Lease Time` to `10m`.
        7.  Click `Apply`.
        8. Go to the `Networks` tab, and click `+`
        9.  Enter `235.17.167.0/24` in the `Address` field.
        10. Enter `235.17.167.1` in the `Gateway` field.
        11. Enter `8.8.8.8,8.8.4.4` in the `DNS Servers` field.
        12. Click `Apply` and `OK`.
    *   **Before:** There are no DHCP servers configured using the IP pool or the bridge interface.
    *   **After:** A DHCP server exists for the bridge-44 interface and assigns IPs from the pool
    *   **Explanation:**
        *   `/ip dhcp-server add`:  Adds a new DHCP server.
        *   `address-pool=pool-235-17-167`: Specifies the IP address pool to use.
        *   `interface=bridge-44`: Specifies the interface on which to run the DHCP server.
        *   `name=dhcp-235-17-167`:  Assigns a descriptive name.
        *   `lease-time=10m`: Sets the lease time for IP assignments to 10 minutes. This is short to demonstrate the DHCP process, but in a real network, you would set this to a longer value like 1 day.
        * `/ip dhcp-server network add`: Defines the network settings for the DHCP server.
        * `address=235.17.167.0/24`: The network address being managed by this server
        * `gateway=235.17.167.1`: Specifies the gateway address.
        * `dns-server=8.8.8.8,8.8.4.4`: Specifies the DNS servers for clients to use. (Google DNS)

4. **Step 4: Enable the DHCP Server:**
    * **Purpose:** Enable the DHCP server so that it can start assigning IP addresses
    * **CLI Command:**
    ```mikrotik
    /ip dhcp-server enable dhcp-235-17-167
    ```
    * **Winbox GUI:**
        1. Navigate to `IP` -> `DHCP Server`.
        2. Find the server you just configured and make sure the `Enabled` checkbox is checked.
    * **Before:** The DHCP Server service is disabled.
    * **After:** The DHCP Server service is enabled.
    * **Explanation:**
        * `/ip dhcp-server enable`: Enables the DHCP service
        * `dhcp-235-17-167`: The name of the DHCP Server to enable.

## Complete Configuration Commands:

```mikrotik
/ip pool
add name=pool-235-17-167 ranges=235.17.167.2-235.17.167.254
/ip address
add address=235.17.167.1/24 interface=bridge-44 network=235.17.167.0
/ip dhcp-server
add address-pool=pool-235-17-167 interface=bridge-44 name=dhcp-235-17-167 lease-time=10m
/ip dhcp-server network
add address=235.17.167.0/24 gateway=235.17.167.1 dns-server=8.8.8.8,8.8.4.4
/ip dhcp-server enable dhcp-235-17-167
```

## Common Pitfalls and Solutions:

*   **Problem:** DHCP clients not receiving IP addresses.
    *   **Solution:**
        1.  Verify the `bridge-44` interface is up and running and has an IP address assigned.
        2.  Check if the `dhcp-server` is enabled.
        3.  Check that the client is connected to the correct bridge.
        4.  Review the `/ip dhcp-server leases` to see if any leases have been issued, or if any client has requested an IP but not received one.
        5. Check the `/log` for any errors on the DHCP server or related interfaces.
*   **Problem:** IP address conflict.
    *   **Solution:** Check that the IP used on the bridge interface is not used by any other device on the network.  Ensure there is a clear separation of subnets.
*   **Problem:** The assigned gateway address is not correct.
    *   **Solution:** Double-check the gateway address assigned to the DHCP network matches the IP address of the bridge interface.
*  **Problem:** DNS not resolving for DHCP clients
    *  **Solution:** Check that the dns servers provided via the DHCP server are correct. Verify that the clients are able to reach the DNS servers by pinging the address.
* **Security Issue:** DHCP can be used to assign specific IP addresses to known clients, causing denial of service.
    * **Solution:**  Implement DHCP static leases and/or MAC filtering on the bridge to prevent unknown clients from receiving IP addresses. Review the `/ip dhcp-server lease` for unknown leases. Enable IP firewall rules to block unknown devices from reaching other devices on the network.
* **Resource Issue:** High CPU usage by the DHCP server
    * **Solution:** Monitor CPU usage using `/system resource monitor`. If high usage is observed, review the DHCP leases for unexpected activity. Try to assign static addresses to a majority of the devices to reduce the load from the dhcp server. You might also consider reducing the lease time if you have lots of clients joining and leaving the network.

## Verification and Testing Steps:

1.  **Connect a client to the `bridge-44` interface.** Ensure it is configured to obtain an IP address automatically via DHCP.
2.  **Verify IP Address on the Client:** Check the client device's IP address. It should have received an address from the 235.17.167.0/24 subnet.
3.  **Verify DHCP Lease:** On the MikroTik, use the following command to verify an address was issued:
    ```mikrotik
    /ip dhcp-server lease print where server=dhcp-235-17-167
    ```
    The client MAC address, assigned IP, and other details should appear in the output.
4.  **Test Connectivity:** Ping the gateway address (235.17.167.1) from the client and ensure the reply is successful. Test that internet access is available from the client device.
5.  **Use Torch:** On the MikroTik router, use the following command to monitor DHCP traffic to bridge-44:
    ```mikrotik
    /tool torch interface=bridge-44 protocol=udp port=67,68
    ```
    This will show DHCP discover, offer, request, and ACK messages.

## Related Features and Considerations:

*   **DHCP Static Leases:** Assign specific IP addresses to clients based on their MAC addresses.
    ```mikrotik
    /ip dhcp-server lease add address=235.17.167.50 mac-address=XX:XX:XX:XX:XX:XX server=dhcp-235-17-167
    ```
    This ensures that a specific device always gets the same IP address.
*   **DHCP Option 82:** Use DHCP Relay to support DHCP option 82, and other DHCP options.
*   **Firewall:** Implement firewall rules to control network traffic based on the assigned IP addresses from the pool. `/ip firewall filter add`
*   **VLANs:** Bridge interfaces can also be assigned to VLANs, allowing for more complex and scalable networks.
*  **DHCP Relay:** Configure DHCP relay to allow clients in other subnets to request an IP from the current dhcp server.

## MikroTik REST API Examples:

**Note**: These REST API examples may require that the API is enabled in `/ip service`. For API usage you must log in using a username and password.

1.  **Creating a new IP Pool:**

    *   **API Endpoint:** `/ip/pool`
    *   **Request Method:** POST
    *   **Example JSON Payload:**
        ```json
        {
          "name": "api-pool-235-17-167",
          "ranges": "235.17.167.20-235.17.167.30"
        }
        ```
    *   **Expected Response (Success):**
        ```json
         {
           ".id": "*10"
           "name": "api-pool-235-17-167",
            "ranges": "235.17.167.20-235.17.167.30"
            "next-address" : null,
            "free-address" : 10,
         }
        ```
   * **Error Response**
        ```json
        {
            "message": "already have such pool",
            "error": true
        }
        ```
2.  **Getting DHCP Server Information:**
    *   **API Endpoint:** `/ip/dhcp-server`
    *   **Request Method:** GET
    *   **Example:** Retrieve a specific DHCP server named `dhcp-235-17-167`.
    *   **Expected Response (Success):**
        ```json
        [
        {
            ".id": "*11",
            "name": "dhcp-235-17-167",
            "interface": "bridge-44",
            "address-pool": "pool-235-17-167",
            "lease-time": "10m",
            "authoritative": true,
            "add-arp": false,
            "disabled": false
        }
        ]
        ```
    * **Error Response**
        ```json
        {
            "message": "no such item",
            "error": true
        }
        ```

3. **Creating a DHCP Server Network**
    * **API Endpoint:** `/ip/dhcp-server/network`
    * **Request Method:** POST
    * **Example JSON Payload:**
        ```json
        {
          "address": "235.17.167.0/24",
          "gateway": "235.17.167.1",
          "dns-server": "8.8.8.8,8.8.4.4"
        }
        ```
    * **Expected Response (Success):**
        ```json
        {
           ".id": "*13"
            "address": "235.17.167.0/24",
            "gateway": "235.17.167.1",
            "netmask": 24,
            "dns-server": "8.8.8.8,8.8.4.4",
            "wins-server": null,
            "domain": null,
            "bootp-file-name": null,
            "bootp-server-address": null,
            "bootp-next-server": null,
            "dhcp-option": []
        }
        ```
   * **Error Response**
        ```json
        {
           "message": "already have such network",
           "error": true
        }
        ```

## Security Best Practices

*   **MAC Address Filtering:** Implement MAC filtering on the bridge interface to allow only known devices to connect. `/interface bridge port add` then add the mac address to the `/interface bridge host`.
*   **DHCP Snooping:** On more advanced MikroTik devices with switch chips, enable DHCP snooping on the bridge interface to protect from rogue DHCP servers. `/interface ethernet switch`
*   **Firewall Rules:** Configure firewall rules to block unknown devices from accessing internal networks. `/ip firewall`
*   **Static Leases:** Assign static leases to known devices to reduce the attack surface by restricting dynamic IP allocations.
*  **Logging:** Keep the DHCP log level at "info" or higher, allowing for review of unexpected events `/system logging`.

## Self Critique and Improvements

The configuration provides a functional DHCP service on a designated bridge interface. It covers the basic steps required for a SOHO environment.

**Improvements:**

*   **DHCP Options:** Add examples for using DHCP options for custom configuration.
*   **Error Handling:** Provide more detailed error handling examples using the MikroTik CLI (e.g., using `/log` and scripting to handle lease failures).
*   **Advanced Filtering:** Implement more complex firewall examples using address lists and connection tracking for better security.
*   **Multiple VLANs:** Demonstrate how this configuration can be extended to VLANs for segmentation.
* **Cloud Integration:** Explore how this can be tied in to cloud services and remote monitoring.

## Detailed Explanations of Topic

*   **IP Pools:** IP pools define a range of IP addresses used by MikroTik DHCP servers. These pools help to dynamically assign IPs to clients instead of requiring static configurations. This simplifies network management and is easier to scale.
*   **DHCP Server:**  The DHCP server protocol enables a network device to dynamically assign IP addresses to clients. This eliminates the need for manual IP assignment, avoiding IP conflicts and management overhead. DHCP also typically provides DNS server addresses and other parameters such as the default gateway.

## Detailed Explanation of Trade-offs

*   **IP Pool Size:** A larger pool provides more available addresses, but can waste IPs if they are not used. A smaller pool conserves IP addresses, but can cause issues if you run out of addresses. A larger pool might also be subject to more broadcast traffic.
*   **Lease Time:** A shorter lease time frees up IP addresses more quickly, useful in dynamic environments. Longer lease times reduces the frequency of DHCP requests, which results in less broadcast traffic, but will require devices to be configured again when there is a network failure.
*   **Static vs Dynamic:**  Dynamic IPs simplify management but cannot ensure a specific device will always get the same IP. Static IP addresses provide stability and consistency, but are less flexible.
*   **DHCP Relay vs local:** A local dhcp server is the simplest solution for a local network, but a DHCP relay can manage requests from multiple networks in a more scalable way.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS 7.11 and other versions that support `/ip pool`, `/ip address`, and `/ip dhcp-server`. The commands are consistent across these versions. Some advanced features such as the `/interface ethernet switch` and DHCP snooping may not be supported on all RouterOS devices or versions.

This concludes the detailed technical documentation for IP Pools using MikroTik RouterOS 7.11. This setup should be fully operational on a SOHO network. Remember to adapt the specific values to fit your particular environment.
