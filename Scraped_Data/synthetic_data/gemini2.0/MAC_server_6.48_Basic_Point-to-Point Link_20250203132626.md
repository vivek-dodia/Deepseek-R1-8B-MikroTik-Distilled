Okay, let's craft detailed documentation for configuring a MAC server on a MikroTik router using RouterOS v6.48 (with notes on v7.x differences).

## Scenario Description:

This document details the configuration of a MAC server on a MikroTik router (RouterOS 6.48), specifically on interface `ether-55`, within the subnet `24.240.78.0/24`. This setup enables the router to act as a central authority for providing IP addresses and managing network access based on MAC addresses connected on the specific interface. While MAC servers are often less commonly used, they can be helpful for scenarios involving specific device access or simplified deployments where IP address management is not handled through DHCP. This configuration is at a basic level, suitable for point-to-point links, smaller networks, or specific purpose deployments.

## Implementation Steps:

This configuration involves creating a MAC server and associating it with a specific interface and IP address range. It does **NOT** provide the capabilities of a DHCP server. It is a more basic way of handling IP address allocation based on MAC address.

1.  **Step 1: Check Interface Status and Existing IP Addresses**
    *   **Before Configuration:** Initially, we should verify the state of the `ether-55` interface and any existing IP address configuration.
    *   **CLI Command Example (before):**

        ```mikrotik
        /interface print where name="ether-55"
        /ip address print where interface="ether-55"
        ```
    *   **Explanation:**
        *   `/interface print where name="ether-55"`:  Displays information about the interface named "ether-55", including its status, MTU, and MAC address.
        *   `/ip address print where interface="ether-55"`:  Shows any IP addresses already configured on the interface "ether-55". We need to make sure there isn't an existing IP address conflict before we move forward.
    *   **Expected Output:** Look for an active interface, and for no addresses assigned to the interface.

2.  **Step 2: Configure the Interface with an IP Address**
    *   **Action:** Assign an IP address within our desired subnet (`24.240.78.0/24`) to the `ether-55` interface.
    *   **CLI Command Example:**

        ```mikrotik
        /ip address add address=24.240.78.1/24 interface=ether-55
        ```
    *   **Explanation:**
        *   `/ip address add address=24.240.78.1/24 interface=ether-55`: This command adds an IP address `24.240.78.1` with a `/24` subnet mask to the `ether-55` interface. This IP address will serve as the base for the MAC server.
    *   **Effect:** The `ether-55` interface will now have the IP address `24.240.78.1/24`. Other devices connecting to this interface can be addressed with IP addresses in the `24.240.78.0/24` subnet.
    *   **CLI Command Example (after):**

        ```mikrotik
        /ip address print where interface="ether-55"
        ```
    *   **Expected Output:** An IP address entry should now be present in the output, reflecting the assigned address.

3.  **Step 3: Add the MAC Server**
    *   **Action:** Create a new MAC server, associated with the `ether-55` interface and a name of your choice.
    *   **CLI Command Example:**

        ```mikrotik
         /ip mac-server add interface=ether-55 name="mac-server-ether55"
        ```

    *   **Explanation:**
        * `/ip mac-server add interface=ether-55 name="mac-server-ether55"`:  This command creates a new MAC server instance associated with `ether-55` and with the name "mac-server-ether55".
    *   **Effect:** A new MAC server instance will be created.
        *   **CLI Command Example (after):**
        ```mikrotik
        /ip mac-server print
        ```
        *   **Expected Output:**  The MAC server you just configured should be present in the printout.

4.  **Step 4: Configure MAC Server Settings.**
    *   **Action:** Set the pool of IPs available for allocation by the MAC server. Also assign the valid-for time for the leases.
    *   **CLI Command Example:**
        ```mikrotik
        /ip mac-server set mac-server-ether55 address-pool=24.240.78.2-24.240.78.254 valid-for=10m
        ```
    *   **Explanation:**
        * `/ip mac-server set mac-server-ether55 address-pool=24.240.78.2-24.240.78.254 valid-for=10m`: Assigns the address-pool range to use for assigning IP addresses and sets the amount of time leases are valid for. This means that a client that connects to the server may be allocated an address in this pool. This must be done by specifying a static address for the host first.
    *   **Effect:**  The MAC Server is configured to provide leases for a given time.
        *   **CLI Command Example (after):**
        ```mikrotik
        /ip mac-server print
        ```
        *   **Expected Output:**  The output should now show your configured parameters in the `address-pool` and `valid-for` properties.

5.  **Step 5: Configure Static MAC Address Lease**
    *   **Action:** Add a MAC entry to the MAC-server leases so that devices will be statically assigned an IP address on connect.
    *   **CLI Command Example:**
        ```mikrotik
        /ip mac-server lease add mac-address=00:11:22:33:44:55 address=24.240.78.100 server=mac-server-ether55
        ```
    *   **Explanation:**
        * `/ip mac-server lease add mac-address=00:11:22:33:44:55 address=24.240.78.100 server=mac-server-ether55`:  This command creates a static MAC entry for the MAC address of `00:11:22:33:44:55` that will be assigned the address of `24.240.78.100` when the device is connected to the network and using the `mac-server-ether55` server.
    *   **Effect:**  The MAC address `00:11:22:33:44:55` will be assigned the IP address `24.240.78.100`
        *   **CLI Command Example (after):**
        ```mikrotik
        /ip mac-server lease print
        ```
        *   **Expected Output:** The output should include your MAC address entry, address, and the related server.

## Complete Configuration Commands:

```mikrotik
/interface print where name="ether-55"
/ip address print where interface="ether-55"
/ip address add address=24.240.78.1/24 interface=ether-55
/ip mac-server add interface=ether-55 name="mac-server-ether55"
/ip mac-server set mac-server-ether55 address-pool=24.240.78.2-24.240.78.254 valid-for=10m
/ip mac-server lease add mac-address=00:11:22:33:44:55 address=24.240.78.100 server=mac-server-ether55
```

## Common Pitfalls and Solutions:

*   **IP Address Conflicts:**
    *   **Problem:**  Assigning the same IP address to a different interface, device, or assigning an address that conflicts with a network address or broadcast address.
    *   **Solution:** Double-check IP addresses before assignment and review existing configuration before making changes.
*   **Interface Issues:**
    *   **Problem:** `ether-55` is not enabled, or not running.
    *   **Solution:** Ensure that `ether-55` is enabled with the command `/interface enable ether-55` and that the cable is properly connected. Check the link-state. Use the command `/interface monitor ether-55` to view the state of the link.
*   **Incorrect Subnet Mask:**
    *   **Problem:** Using the wrong subnet mask will lead to devices that cannot communicate with each other, or to an improperly configured MAC server.
    *   **Solution:** Verify that you have used the correct subnet mask.
*   **MAC Address Errors:**
    *   **Problem:** Mistyping a MAC address will lead to the device not obtaining an IP address.
    *   **Solution:** Double check and use the command `/ip mac-server lease print` to verify your entries.
*   **RouterOS Version Differences**
    *   **Problem:** Changes in command parameters.
    *   **Solution:** Always check the latest documentation for the version of routeros you are using. Specifically in RouterOS 7, many commands have had their syntax changed.
*   **No Clients Showing Up:**
    *  **Problem:** There are no devices attempting to connect to the interface. The client is not correctly configured, or the MAC server address pool is not correctly configured.
    *  **Solution:** Verify the client is attempting to connect to the correct network and verify that the address pool is correctly configured.

## Verification and Testing Steps:

1.  **Interface Status:**
    *   **Command:** `/interface print where name="ether-55"`
    *   **Expected:**  Status should be "running."
2.  **IP Address:**
    *   **Command:** `/ip address print where interface="ether-55"`
    *   **Expected:** The IP address `24.240.78.1/24` should be present.
3.  **MAC Server Check**
    *   **Command:** `/ip mac-server print`
    *   **Expected:** The server, with associated interface should be present. You should also verify the address pool is correct.
4.  **Lease Check:**
    *   **Command:** `/ip mac-server lease print`
    *   **Expected:** The static MAC address you have entered should be present. If a device has connected to the network using a specified MAC address, then a lease will be visible.
5.  **Client Device Verification**
    *  **Action:** Connect a device to the `ether-55` interface. Verify the client gets an IP address and can communicate with the network.
    *   **Expected:** The client device should receive the IP address associated with the MAC address, and should be able to communicate on the network.
6.  **Ping Test:**
    *   **Action:** From the MikroTik router, ping the device with the IP assigned by the MAC server.
    *   **Command:** `ping 24.240.78.100`
    *   **Expected:** Successful ping response.
7.  **Torch Tool:**
    *   **Action:** Use torch tool on the `ether-55` interface to monitor network traffic for the MAC address you configured.
    *   **Command:** `/tool torch interface=ether-55`
    *   **Expected:** You should see traffic related to the connected client, including ARP requests to identify the device.

## Related Features and Considerations:

*   **DHCP Server:** For more dynamic IP address allocation on a wider scale, consider using a DHCP server instead of a MAC server.
*   **Firewall:** Implement firewall rules to control access for devices using your new address space to isolate the MAC server to a single interface and keep the network secure.
*  **VRF**: If you have a complicated network, consider the use of a VRF for easier network segregation. This may not be necessary for simple point to point link applications.
*   **Hotspot:** MikroTik's hotspot feature can be used in conjunction with a MAC server to implement more sophisticated access control mechanisms.
*   **VLAN:**  You can configure a MAC server for a specific VLAN.
*   **Address List:** You could add client IP addresses allocated via MAC server to an address list for management purposes.

## MikroTik REST API Examples (if applicable):

While not directly applicable for all aspects of MAC server configuration, the REST API can be used to fetch lease information:

**1. Fetching Lease Information:**

*   **API Endpoint:** `/ip/mac-server/lease`
*   **Request Method:** GET
*   **JSON Payload:** (None)
*   **Example Command:**
    ```bash
    curl -k -u 'apiuser:apipassword' https://<your_router_ip>/rest/ip/mac-server/lease
    ```
    *   **Explanation:** `curl` command with `-k` to disable SSL cert verification, `-u` for API user authentication, and `https` URL and `/rest/ip/mac-server/lease` endpoint.
*   **Expected Response:**
    ```json
    [
      {
        ".id": "*6",
        "mac-address": "00:11:22:33:44:55",
        "address": "24.240.78.100",
        "server": "mac-server-ether55",
        "valid-time": "10m",
        "last-seen": "2024-06-26T18:30:00+00:00",
        "status": "bound"
      }
    ]
    ```
*   **Error Handling:** If authentication fails, the API will respond with an error. Catching errors from `curl` is important for monitoring and troubleshooting. You can also use a more powerful HTTP client such as Postman to debug errors.
*  **Note:** When configuring the API, ensure that it is only exposed to trusted management networks.

## Security Best Practices

*   **API Security:** Never expose the API to the public internet.
*   **Firewall Rules:** Add firewall rules to limit access to the MAC server, only allowing necessary traffic through.
*   **Physical Security:** Ensure physical access to the router is limited to prevent unauthorized access.
*   **Router Software:** Keep RouterOS up to date with the latest security patches.
*   **Password Strength:** Use strong passwords for the router and avoid default passwords.

## Self Critique and Improvements

*   **Scalability:** MAC servers are not easily scalable for large networks. DHCP is far better for this.
*   **Static IP Management:** The need to manually add static addresses is time-consuming for a large number of clients. This is very suitable for a small number of statically assigned devices.
*   **Configuration Complexity:** The configuration is simple; however it is not immediately apparent when compared to DHCP.
*   **Monitoring:** More robust monitoring should be configured with tools such as the Dude.
*   **Automation:** The use of scripts could be added to automatically add new MAC entries.

## Detailed Explanations of Topic

**MAC Server:** A MAC server in RouterOS is a very basic method of providing IP addresses based on MAC address. It uses a pool of addresses assigned to a specific interface to provide IP addresses to connecting clients. This can be useful in situations where there needs to be very tightly controlled access based on the MAC address of devices, and is not very scalable. This type of server relies on a previously configured interface IP address, and the client device must be configured to receive an IP address with that configured IP address.

## Detailed Explanation of Trade-offs

*   **MAC Server vs. DHCP Server:** A MAC server provides very basic IP address allocation and is better suited for static devices on a small network. A DHCP server is more dynamic, better suited to large networks, and can provide a range of options to clients. A DHCP server assigns IP addresses based on a lease, and a MAC server assigns IP addresses based on a MAC address list and has a limited number of options.
*   **Static vs. Dynamic IP:** With a MAC server, you are essentially configuring static IP addresses as you manually set each MAC-to-IP pairing. Dynamic IP assignment using a DHCP server allows for devices to automatically receive addresses from a range, with leases that automatically expire and reassign addresses to new or different clients.

## Configuration for Specific RouterOS Versions:

This documentation is primarily written for RouterOS v6.48. In RouterOS v7.x:

*   The command syntax might have slight variations (e.g., some commands are now under `/ip/mac-server` and not `/ip mac-server`). It is important to check the RouterOS documentation for the specific version being used.
*   New features are available in RouterOS 7.X that should be explored, however these commands will still function as expected.

This detailed documentation should provide a solid foundation for configuring and managing a MAC server in your MikroTik router using RouterOS 6.48. Remember to adapt this to your specific network needs and always refer to the official MikroTik documentation.
