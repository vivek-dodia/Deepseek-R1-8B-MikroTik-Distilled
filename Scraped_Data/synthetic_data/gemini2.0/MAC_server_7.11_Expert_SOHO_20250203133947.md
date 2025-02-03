Okay, let's dive into configuring the MAC server on a MikroTik router running RouterOS 7.11 within a SOHO environment, using the specified subnet and interface name. This will be a detailed, expert-level guide.

## Scenario Description:

This scenario addresses the need to implement a MAC server on a MikroTik router. A MAC server, in the context of MikroTik, allows the router to act as a DHCP server that uses MAC addresses as identifiers for assigning IP addresses. This can be useful for static IP address assignment based on a device's hardware address. The specific configuration includes enabling the MAC server functionality on interface `vlan-79`, using the subnet `148.58.14.0/24`, and setting up the server and bindings. This setup will assume that VLAN 79 is configured and functional.

## Implementation Steps:

Before we begin, please ensure that the VLAN interface `vlan-79` exists and is properly configured. If not, create that first.

1.  **Step 1: Configure the DHCP Server Network**

    *   **Purpose:** This step defines the network settings (IP address, gateway, dns) that the DHCP server will use.
    *   **Action:** Using the CLI or Winbox, create the `dhcp-server network` entry.
    *   **CLI Example (Before):**
        ```
        /ip dhcp-server network print
        ```
    *   **CLI Example (After):**
        ```
        /ip dhcp-server network
        add address=148.58.14.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=148.58.14.1
        /ip dhcp-server network print
        ```
    *   **Winbox GUI:**
        Go to IP -> DHCP Server -> Networks tab. Click '+' and add `Address`=148.58.14.0/24, `Gateway`=148.58.14.1 and `DNS Servers`=8.8.8.8,8.8.4.4. Click OK.
    *   **Explanation:** This creates a DHCP network object with the required IP range, default gateway, and DNS servers which is needed by our DHCP server. The network must be defined before any server can use it.
2.  **Step 2: Create a MAC Server**

    *   **Purpose:** This step creates the DHCP MAC server and binds it to `vlan-79`.
    *   **Action:** Use the CLI or Winbox to create the DHCP server entry of type `mac`.
    *   **CLI Example (Before):**
        ```
        /ip dhcp-server print
        ```
    *   **CLI Example (After):**
        ```
        /ip dhcp-server
        add address-pool=default authoritative=yes disabled=no interface=vlan-79 lease-time=1d mac-server=yes name=mac-server-vlan79 network=148.58.14.0/24
        /ip dhcp-server print
        ```
    *   **Winbox GUI:**
        Go to IP -> DHCP Server -> DHCP tab. Click '+' and add `Name`=mac-server-vlan79, `Interface`=vlan-79, and check `MAC Server` and `Authoritative` boxes. Click OK. Then go to Networks Tab and add Network as in previous step.
    *  **Explanation:** This creates a DHCP server that will only respond to DHCP request packets that come from the VLAN 79 interface, and only if the request is from the MAC server's client list. We also set the server to authoritative.
3.  **Step 3: Add MAC Bindings (Optional)**

    *   **Purpose:**  This step adds static IP assignments based on MAC addresses. You can configure these as well in the DHCP bindings section.
    *   **Action:**  Add static DHCP leases with specified IP addresses linked to client MAC addresses.
    *   **CLI Example (Before):**
        ```
        /ip dhcp-server lease print
        ```
    *   **CLI Example (After):**
        ```
        /ip dhcp-server lease
        add address=148.58.14.10 client-id=01:AA:BB:CC:DD:EE:FF mac-address=AA:BB:CC:DD:EE:FF server=mac-server-vlan79
        add address=148.58.14.20 client-id=01:11:22:33:44:55:66 mac-address=11:22:33:44:55:66 server=mac-server-vlan79
        /ip dhcp-server lease print
        ```
    *   **Winbox GUI:**
        Go to IP -> DHCP Server -> Leases tab. Click '+' and add `MAC Address`, `IP Address`, and `Server` values. Click OK for each entry.
    *   **Explanation:** This allows specific devices to always get the same IP address based on their MAC address. Note that `client-id` is automatically generated from mac-address with a prefix of 01. If you don't know the exact client-id from a device that sends a DHCP request you can view it in the DHCP leases section when a device has requested an IP from this server. `server` ensures that the lease belongs to the `mac-server-vlan79` DHCP server. If you have multiple DHCP servers on different interfaces with same network addresses you should configure different static ip leases for each server if you need that functionality.

## Complete Configuration Commands:

```
/ip dhcp-server network
add address=148.58.14.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=148.58.14.1

/ip dhcp-server
add address-pool=default authoritative=yes disabled=no interface=vlan-79 lease-time=1d mac-server=yes name=mac-server-vlan79 network=148.58.14.0/24

/ip dhcp-server lease
add address=148.58.14.10 client-id=01:AA:BB:CC:DD:EE:FF mac-address=AA:BB:CC:DD:EE:FF server=mac-server-vlan79
add address=148.58.14.20 client-id=01:11:22:33:44:55:66 mac-address=11:22:33:44:55:66 server=mac-server-vlan79
```

**Parameter Explanations:**

*   `/ip dhcp-server network add`:
    *   `address`: The network address and subnet mask in CIDR notation. (`148.58.14.0/24`)
    *   `dns-server`: Comma-separated list of DNS servers to provide to clients. (`8.8.8.8,8.8.4.4`)
    *   `gateway`: The default gateway for the network. (`148.58.14.1`)
*   `/ip dhcp-server add`:
    *   `address-pool`:  The DHCP address pool to use. `default` is used when not further specified.
    *   `authoritative`: If `yes`, the DHCP server will send DHCPNAK to a client that has requested an address from a different server.
    *   `disabled`: If `no`, the server is enabled.
    *   `interface`: The interface to listen for DHCP requests (`vlan-79`).
    *   `lease-time`: The DHCP lease time (e.g., `1d` for 1 day).
    *   `mac-server`: If `yes`, DHCP server is running in MAC-server mode.
    *   `name`: A name for this DHCP server (`mac-server-vlan79`).
    *   `network`: The network used by this dhcp server (`148.58.14.0/24`).
*   `/ip dhcp-server lease add`:
    *   `address`: The IP address to assign to the client. (`148.58.14.10`).
    *   `client-id`: DHCP client ID. `01:<MAC-Address>` is a standard ID for DHCP clients that don't provide their own id.
    *   `mac-address`:  The client's MAC address (`AA:BB:CC:DD:EE:FF`).
    *    `server`: The name of the dhcp-server object this lease belongs to (`mac-server-vlan79`).

## Common Pitfalls and Solutions:

*   **Problem:** Clients not receiving IP addresses.
    *   **Solution:** Verify that the `vlan-79` interface is active and correctly configured. Check firewall rules (if they are preventing DHCP traffic) and make sure the client is properly connected to the network where this VLAN is configured. Also, verify the DHCP server and leases settings. Use `torch` on the interface to check for DHCP discovery packets.
*   **Problem:** Incorrect IP addresses assigned.
    *   **Solution:** Check static DHCP bindings and ensure the correct MAC addresses and IPs are configured.  Also check the `client-id` and the used prefix for dhcp requests.
*   **Problem:** DHCP server not running because it cannot find the configured network.
    *   **Solution:** Double check the server's network parameter. It should point to the correct network which must be defined first.
*   **Problem:** Devices receive duplicate IPs
    *   **Solution:** Ensure that all servers on the same network use different IP address pools or different static leases. Use the authoritative DHCP setting to ensure that leases cannot be created from a different DHCP server.

## Verification and Testing Steps:

1.  **Check DHCP Server Status:**
    ```
    /ip dhcp-server print
    ```
    Verify that the MAC server is enabled (`enabled=yes`).

2.  **Check DHCP Leases:**
    ```
    /ip dhcp-server lease print
    ```
    Verify the static leases are present and that the connected clients (if any) have requested and received an IP address.

3.  **Use `torch` to Monitor DHCP Traffic:**

    ```
    /tool torch interface=vlan-79 protocol=udp port=67,68
    ```
    This command shows DHCP client and server communication on vlan-79.

4.  **Client-Side Verification:**
    *   Connect a client to the network that has VLAN 79 configured.
    *   Check if the client gets an IP address. Verify that the IP address is in the correct range (148.58.14.0/24) and that the correct DNS and gateway are assigned.
    *   If using a statically assigned IP address via a binding on the MikroTik router, check that client gets the correct IP.

## Related Features and Considerations:

*   **DHCP Address Pools:** You can configure custom address pools to manage different subnets or types of devices.
*   **DHCP Options:** You can provide additional DHCP options to clients such as NTP servers or custom routes.
*   **DHCP Server Scripting:** Use RouterOS scripting to dynamically manage DHCP leases based on events.
*   **VLAN Tagging**: Ensure that the VLAN is configured properly on the ports and devices connected to this network.
*   **Firewall Rules**: Make sure the client devices are able to communicate through the firewall to get a dhcp address, especially if you've configured more strict rules.

## MikroTik REST API Examples (if applicable):

Here are some API examples related to the MAC server.

1.  **Get DHCP Server List:**

    *   **Endpoint:** `/ip/dhcp-server`
    *   **Method:** `GET`
    *   **Request Payload:** _None_
    *   **Example (Curl):**
    ```bash
        curl -k -u 'admin:password' https://your_mikrotik_ip/rest/ip/dhcp-server | jq
    ```
    *   **Expected Response:** JSON array containing information about all DHCP servers.
       *Example:*
        ```json
           [
                {
                  ".id": "*12",
                  "address-pool": "default",
                  "authoritative": "yes",
                  "disabled": "no",
                  "interface": "vlan-79",
                  "lease-time": "1d",
                  "mac-server": "yes",
                  "name": "mac-server-vlan79",
                  "network": "148.58.14.0/24",
                  "use-radius": "no"
                }
            ]
        ```

2.  **Add a new MAC Server:**

    *   **Endpoint:** `/ip/dhcp-server`
    *   **Method:** `POST`
    *   **Request Payload (JSON):**
        ```json
          {
            "address-pool":"default",
            "authoritative":"yes",
            "disabled":"no",
            "interface":"vlan-79",
            "lease-time":"1d",
            "mac-server":"yes",
            "name":"new-mac-server-vlan79",
            "network":"148.58.14.0/24"
            }
        ```
    *   **Example (Curl):**
    ```bash
       curl -k -u 'admin:password' -H 'Content-Type: application/json' -d '{
            "address-pool":"default",
            "authoritative":"yes",
            "disabled":"no",
            "interface":"vlan-79",
            "lease-time":"1d",
            "mac-server":"yes",
            "name":"new-mac-server-vlan79",
            "network":"148.58.14.0/24"
            }' https://your_mikrotik_ip/rest/ip/dhcp-server
    ```
    *   **Expected Response:** JSON object containing ID of the created DHCP server.

3.  **Update a MAC server setting:**
    *   **Endpoint:** `/ip/dhcp-server/{id}` Replace {id} with actual ID like `*12`.
    *   **Method:** `PATCH`
    *   **Request Payload (JSON):**
        ```json
        {
            "lease-time": "2d"
        }
        ```
     *  **Example (Curl):**
        ```bash
         curl -k -u 'admin:password' -H 'Content-Type: application/json' -X PATCH -d '{
           "lease-time": "2d"
         }' https://your_mikrotik_ip/rest/ip/dhcp-server/*12
        ```
    *   **Expected Response:** JSON object containing updated DHCP server attributes.

4.  **Get DHCP Leases:**

    *   **Endpoint:** `/ip/dhcp-server/lease`
    *   **Method:** `GET`
    *   **Request Payload:** _None_
    *   **Example (Curl):**
    ```bash
        curl -k -u 'admin:password' https://your_mikrotik_ip/rest/ip/dhcp-server/lease | jq
    ```
    *   **Expected Response:** JSON array containing DHCP leases.
        ```json
        [
             {
              ".id": "*3",
              "address": "148.58.14.10",
              "active-address": "148.58.14.10",
              "active-client-id": "01:aa:bb:cc:dd:ee:ff",
              "active-mac-address": "AA:BB:CC:DD:EE:FF",
              "client-id": "01:aa:bb:cc:dd:ee:ff",
              "mac-address": "AA:BB:CC:DD:EE:FF",
              "server": "mac-server-vlan79",
              "status": "bound"
             }
          ]
        ```
5. **Add Static Lease:**
   * **Endpoint:** `/ip/dhcp-server/lease`
   * **Method:** `POST`
   * **Request Payload (JSON):**
     ```json
       {
          "address": "148.58.14.25",
          "client-id": "01:00:11:22:33:44:55",
          "mac-address": "00:11:22:33:44:55",
          "server": "mac-server-vlan79"
        }
      ```
    *   **Example (Curl):**
    ```bash
      curl -k -u 'admin:password' -H 'Content-Type: application/json' -d '{
         "address": "148.58.14.25",
         "client-id": "01:00:11:22:33:44:55",
         "mac-address": "00:11:22:33:44:55",
         "server": "mac-server-vlan79"
       }' https://your_mikrotik_ip/rest/ip/dhcp-server/lease
    ```
   *  **Expected Response:** JSON object containing ID of the created DHCP lease.

**API Error Handling:**

*   The API will respond with HTTP status codes to indicate success (200, 201) or error (400, 404, 500).
*   Error responses will contain a JSON object with an `error` key providing more details about the issue. For example, if the specified ID does not exist for a `PATCH` call or when creating an object that already exists.
*   Check the response headers and payload for error details.  You can use  `jq` command line tool to parse the JSON and `grep` to filter for specific information if needed.

## Security Best Practices:

*   **Secure Access:** Restrict access to the router's web interface and API using strong passwords and firewall rules.
*   **Interface Access Control:** Limit the interface the DHCP server responds on to only the intended VLAN (vlan-79).
*   **Lease Time:** Set a reasonable DHCP lease time (e.g. 1 day to 1 week depending on your usage) for both security and resource management.
*   **Authoritative DHCP:**  Enable the `authoritative` setting on the DHCP server.
*   **Monitor logs:** Regular log reviews will show any unexpected behavior.
*   **Use firewall rules:** Restrict access to your dhcp server to only devices that need access.
*   **Limit client devices:** With MAC-Server, only devices that have static leases will get an IP address from this server.

## Self Critique and Improvements:

This configuration is good for the described SOHO use case but has room for improvement:

*   **Improvement:** Add more DHCP options, such as NTP servers, or domain name if needed.
*   **Improvement:** Implement DHCP scripting to dynamically manage leases or handle events.
*   **Improvement:** Implement address pools for different network segments within the larger subnet.
*  **Improvement:** Add logging policies to record specific DHCP events
*   **Improvement:** If you need different VLANs for different types of devices you could use a separate MAC server for each interface.
*   **Improvement:** Monitor resource usage, especially if a large number of devices use this MAC server. You can monitor CPU and memory usage via the `/system resource print` command.
*   **Improvement:**  You may want to specify different address pools instead of the default pool to better organize the available IP addresses.

## Detailed Explanations of Topic:

**MAC Server:**

In MikroTik RouterOS, a MAC server is a special type of DHCP server configuration that uses the MAC address of the client as a primary identifier to determine if an IP address should be assigned. This is different from the regular DHCP server operation, where a client's lease request is based on its DHCP client-id and potentially other DHCP options. Here are some key aspects:

*   **MAC address-based assignments:** Instead of relying on DHCP client ID, this server associates IP addresses with the client's MAC address. This is used when assigning static IP addresses based on a hardware identifier.
*  **Static Leases:** The main difference between the DHCP server mode and a MAC-server is that when using a MAC-Server, *only* the devices in the static lease list will get an IP address.
*   **Controlled environment:** It's often used when you want a more controlled network environment where only specific MAC addresses are allowed on the network, and receive an IP address from the local DHCP server.
*   **Use Cases:** Ideal for situations where static IP addresses are needed for specific devices that need to retain the same IP address on the network (for server type devices or services that require a static IP).
*   **Limitations:** The MAC-server mode is not a substitute for Radius authentication for access control. Radius should be used if you need user authentication before handing out an IP.

## Detailed Explanation of Trade-offs:

**Regular DHCP Server vs. MAC Server:**

*   **Regular DHCP Server:**
    *   **Pros:** More dynamic, easy for clients to connect and get IP addresses from available address pools, easy to handle dynamic IP address allocation for new devices on the network.
    *   **Cons:** Less control over which devices get an IP address and what address they get (unless static leases are configured in advance).
*   **MAC Server:**
    *   **Pros:** Strict control on the devices that can get IPs, ensures only devices with pre-defined MAC addresses can get an IP. Static IP leases are easier to implement and manage compared to normal DHCP server as client identification is simple and deterministic.
    *   **Cons:** Requires manual configuration for each device that needs a static IP lease, and can cause problems for new devices that are not pre-configured. Less flexible for dynamic networks with frequent device additions.

**Static Lease vs. Dynamic Lease:**

*   **Static Lease:**
    *   **Pros:** Consistent IP assignment, useful for services that require a specific IP address, easier for network management and troubleshooting of devices.
    *   **Cons:** Requires manual configuration and maintenance, less flexible for dynamic environments.
*   **Dynamic Lease:**
    *   **Pros:** Automatic IP assignment, ideal for frequently changing devices or networks with a lot of devices.
    *   **Cons:** IP addresses can change, potentially causing issues if devices are using a specific IP for services.

**Authoritative DHCP**:

*   **Pros:** The DHCP server will proactively enforce its IP allocation policies, ensuring clients do not accept IPs from other conflicting DHCP servers on the network. This is crucial when more than one DHCP server is present on the network to prevent duplicate IP assignments.
*   **Cons:** Can create issues if there is another DHCP server that can give a valid address but doesn't get to respond first on the network, resulting on DHCPNAK messages from the authoritative DHCP server, preventing clients from getting a valid IP address until they retry.

## Configuration for Specific RouterOS Versions:

The provided commands are compatible with RouterOS 7.11. Ensure that the targeted RouterOS version is 7.x, or 6.48 or later.

This documentation provides an in-depth understanding of the MAC server functionality in MikroTik RouterOS, along with detailed configuration steps, error handling, and advanced usage examples. If you have more questions or scenarios, let me know!
