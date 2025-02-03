Okay, let's dive into configuring a MAC server on a MikroTik router running RouterOS 7.12 (though also relevant for 6.48 and other 7.x versions) within a Hotspot network environment. This will be an advanced configuration, considering the nuances of MAC servers in hotspot deployments.

## Scenario Description:

In a Hotspot network, a MAC server allows you to assign specific IP addresses to clients based on their MAC addresses. This is beneficial for static IP assignments within the hotspot, ensuring certain devices receive consistent IP addresses for various purposes such as gaming, specific applications, or network administration. In this scenario, we're focusing on a Hotspot implementation where specific clients are allocated IP addresses based on the MAC address, using the subnet 177.23.0.0/24 and VLAN interface `vlan-18`.

## Implementation Steps:

**Detailed Explanation of Topic:**
A MAC server in MikroTik RouterOS isn't a separate, standalone service like DHCP. Instead, it leverages the DHCP server functionality. It works by associating specific MAC addresses with pre-defined IP addresses within the DHCP server's address pool. When a device with a matching MAC address requests an IP address via DHCP, the MAC server will provide the static address defined for that MAC rather than a dynamic address. It's important to note that the address pool must include all the static IP addresses you plan to assign via the MAC server functionality.

**Step 1: Configure the VLAN Interface**

*   **Description:** We first ensure the VLAN interface `vlan-18` exists and is properly configured. If it's a new VLAN, we need to create it; otherwise, verify its settings.
*   **Why:** This is essential because the MAC server will be operating within the scope of this interface's network.
*   **Before Configuration:** Assumes the `vlan-18` does not exist, or has default configurations. The specific bridge or physical interface will depend on your specific setup. For this example we will assume that the VLAN exists on `ether1`.
*   **Action:**
    *   **CLI Example:**
        ```mikrotik
        /interface vlan
        add name=vlan-18 vlan-id=18 interface=ether1 disabled=no
        ```
    *   **Winbox GUI:** Navigate to `Interfaces` -> `VLAN` tab. Click `+` to add, enter the name `vlan-18`, VLAN ID `18` select interface `ether1` and click `Apply` then `OK`.
*   **After Configuration:** VLAN `vlan-18` is active on interface `ether1`

**Step 2: Configure the DHCP Server**

*   **Description:** We set up the DHCP server on the `vlan-18` interface.
*   **Why:** The MAC server is a feature of the DHCP server. This allows us to control the pool of IPs being handed out to our clients on `vlan-18`.
*   **Before Configuration:** No DHCP server on `vlan-18`
*   **Action:**
    *   **CLI Example:**
        ```mikrotik
        /ip dhcp-server
        add address-pool=default address-range=177.23.0.2-177.23.0.254 disabled=no interface=vlan-18 name=dhcp-vlan-18
        /ip dhcp-server network
        add address=177.23.0.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=177.23.0.1
        ```

    *   **Winbox GUI:**
        *   Go to `IP` -> `DHCP Server`, click `+`, interface `vlan-18`, click `Apply`, click `OK`
        *   Go to `IP` -> `DHCP Server` -> `Networks` tab, click `+`, enter the address `177.23.0.0/24`, DNS servers and Gateway then click `Apply`, then `OK`.
*   **After Configuration:** DHCP server is running on `vlan-18`, clients can now receive dynamic IPs.

**Step 3: Configure static MAC mappings (MAC server)**

*   **Description:** Define specific MAC addresses and their corresponding IP assignments.
*   **Why:** This is where the MAC server functionality comes into play, assigning specific IP addresses based on MAC.
*  **Before Configuration:** No static IP mappings.
*   **Action:**
    *   **CLI Example:**
        ```mikrotik
        /ip dhcp-server lease
        add address=177.23.0.10 client-id=1 mac-address=00:11:22:33:44:55 server=dhcp-vlan-18
        add address=177.23.0.20 client-id=2 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-vlan-18
        ```

    *   **Winbox GUI:** Go to `IP` -> `DHCP Server` -> `Leases`. Click `+`.  Enter the IP address, MAC address and server.
*   **After Configuration:** Clients with the MAC addresses `00:11:22:33:44:55` and `AA:BB:CC:DD:EE:FF` will get `177.23.0.10` and `177.23.0.20`, respectively, on DHCP renewal.

## Complete Configuration Commands:

```mikrotik
/interface vlan
add name=vlan-18 vlan-id=18 interface=ether1 disabled=no

/ip dhcp-server
add address-pool=default address-range=177.23.0.2-177.23.0.254 disabled=no interface=vlan-18 name=dhcp-vlan-18
/ip dhcp-server network
add address=177.23.0.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=177.23.0.1

/ip dhcp-server lease
add address=177.23.0.10 client-id=1 mac-address=00:11:22:33:44:55 server=dhcp-vlan-18
add address=177.23.0.20 client-id=2 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-vlan-18

```

**Parameter Explanation Table:**
| Command            | Parameter     | Description                                                            |
|--------------------|---------------|------------------------------------------------------------------------|
| `/interface vlan add` | `name`        | Name of the VLAN interface (e.g., `vlan-18`).                        |
|                    | `vlan-id`     | VLAN ID to assign (e.g., `18`).                                       |
|                    | `interface`   | Physical interface on which VLAN is created (e.g., `ether1`).         |
|                    | `disabled`      | Enable/disable the interface |
| `/ip dhcp-server add`| `address-pool`   | DHCP pool name                                                       |
|                    | `address-range`  | IP range to be dynamically assigned.                            |
|                    | `disabled`      | Enable/disable the DHCP server |
|                    | `interface`   | Interface on which the DHCP server will listen (`vlan-18`).         |
|                    | `name`      | DHCP server name |
| `/ip dhcp-server network add`| `address`   | Network IP and subnet mask (e.g., `177.23.0.0/24`).            |
|                    | `dns-server`   | DNS server address (e.g., `1.1.1.1,8.8.8.8`).                        |
|                    | `gateway`       | Gateway IP for the network (e.g., `177.23.0.1`).                |
| `/ip dhcp-server lease add`| `address`       | Static IP to assign (e.g., `177.23.0.10`).                       |
|                    | `client-id`       | Lease number/id                                                      |
|                    | `mac-address` | MAC address of the client (e.g., `00:11:22:33:44:55`).                 |
|                    | `server`      | DHCP server for this lease (`dhcp-vlan-18`).                             |

## Common Pitfalls and Solutions:

*   **Problem:**  Clients not getting the correct static IP.
    *   **Solution:** Verify that the MAC address is correct, ensure the static IP is within the DHCP pool's range, and the DHCP server is enabled on the VLAN interface. Make sure the client sends DHCP request (Release and renew IP). Check the lease entry for errors.
*   **Problem:** Duplicate IP addresses being assigned.
    *   **Solution:**  Ensure that the static IPs assigned are not within the range of dynamically assigned IP addresses, or if so that the address pool does not conflict with static assignments.
*   **Problem:**  DHCP server is not enabled for the correct interface.
    *   **Solution:** Double-check the DHCP server configuration (`/ip dhcp-server print`) and confirm the interface is `vlan-18`.
*   **Problem:** The assigned IPs are outside the subnet.
    *   **Solution:** Verify that the `/ip dhcp-server network` configuration's address is the same as the DHCP server's address range.
*   **Problem:** Resource Issues - High CPU usage on the device.
    *   **Solution:** If the hotspot clients are numerous, it might lead to CPU spikes during DHCP address lease assignment. Monitor CPU usage, consider upgrading the hardware if needed, or reduce lease times. Reduce the address pool size.

## Verification and Testing Steps:

1.  **Client-side testing:**
    *   **Connect a client:** Connect a device with MAC address `00:11:22:33:44:55` to the network. Release and renew IP to trigger the DHCP process. Verify that it receives the IP `177.23.0.10`.
    *   **Connect another client:** Connect a device with MAC address `AA:BB:CC:DD:EE:FF`. Release and renew IP and verify that it receives IP `177.23.0.20`.
    *   **Connect a third client:** Connect any other device, release and renew IP and confirm it receives any IP address other than `177.23.0.10` or `177.23.0.20`, as those addresses are reserved for static leases.
2.  **MikroTik Testing:**
    *   **Check DHCP Leases:** Use `/ip dhcp-server lease print` to verify that the static leases are showing correctly, that IPs are being assigned to corresponding MACs, and that active leases exist.
    *   **Use Torch:** Use the Torch tool (`/tool torch interface=vlan-18`) to monitor DHCP traffic during client connection to observe DHCP discover, offer, request, and ack messages. This can help identify issues with IP assignments.

## Related Features and Considerations:

*   **Hotspot Profiles:** This configuration would often be combined with a MikroTik Hotspot configuration for user authentication.
*   **Address Lists:** For more advanced scenarios, use Address Lists to organize IP addresses for firewall rules or QoS settings.
*   **DHCP Options:** You can set additional DHCP options like NTP servers, domain names, or specific router options for specific clients if needed.
* **DHCP Snooping:** DHCP snooping can be configured to mitigate attacks related to rogue DHCP servers.
* **Lease time:** Adjust lease time to match network requirements.

## MikroTik REST API Examples (if applicable):

While the core functionality isn't directly exposed as a single API endpoint for "MAC server" we can manipulate the DHCP leases using the following examples:

**1. Retrieving DHCP Leases:**
   *   **Endpoint:** `/ip/dhcp-server/lease`
   *   **Method:** `GET`
   *   **Request Example:** (None required for GET requests)
   *   **Response Example:**
       ```json
       [
         {
           "id": "*1",
           "address": "177.23.0.10",
           "mac-address": "00:11:22:33:44:55",
           "server": "dhcp-vlan-18",
           "active-address": "177.23.0.10",
           "client-id": "1",
           "status":"bound"
         },
          {
           "id": "*2",
           "address": "177.23.0.20",
           "mac-address": "AA:BB:CC:DD:EE:FF",
           "server": "dhcp-vlan-18",
           "active-address": "177.23.0.20",
           "client-id": "2",
           "status":"bound"
         }
       ]
       ```

**2. Adding a Static DHCP Lease:**

   *   **Endpoint:** `/ip/dhcp-server/lease`
   *   **Method:** `POST`
   *   **Request JSON Payload:**

        ```json
        {
          "address": "177.23.0.30",
          "mac-address": "12:34:56:78:90:AB",
          "server": "dhcp-vlan-18",
          "client-id": "3"
        }
        ```
   *   **Expected Response:**
        *  On success, a 201 status code is returned along with a JSON body of the newly created lease.
   *   **Error Handling:** If an error occurs, the API will return a non-200 series status code, typically 400 (Bad Request) or 500 (Internal Server Error). The JSON body of the response should contain a `message` key indicating what the problem was, which can be due to a variety of causes, including malformed JSON, missing required keys, duplicate or invalid mac address, and other reasons that the RouterOS could not process the request.
         ```json
        {
            "message": "invalid value for argument mac-address",
            "details": "12-34-56-78-90-AB is not valid mac-address",
            "error": "invalid value"
          }
        ```

**3. Updating a Static DHCP Lease:**

   *   **Endpoint:** `/ip/dhcp-server/lease/<lease-id>` (`<lease-id>` should be substituted for the lease id.)
   *   **Method:** `PUT`
   *  **Request JSON Payload:**
        ```json
        {
          "address": "177.23.0.35",
          "client-id": "3"
        }
        ```
   *   **Expected Response:**
      * On success, a 200 status code with a JSON body that contains the updated lease details.
  *    **Error Handling:** As before, errors will be returned as a non-200 status, with message, details and error key in the response json body.

**4. Deleting a Static DHCP Lease:**

   *   **Endpoint:** `/ip/dhcp-server/lease/<lease-id>`
   *   **Method:** `DELETE`
   *  **Request Example:** (None required for DELETE requests)
   *   **Expected Response:**
      * On success, a 204 status code with no response body.
  *    **Error Handling:** As before, errors will be returned as a non-200 status code with message, details and error key in the response body.

## Security Best Practices:

*   **Limit Access:** Ensure that only authorized users have access to the MikroTik router configuration via strong passwords, SSH access control and/or API access control.
*   **Firewall Rules:** Implement firewall rules to filter traffic coming to and from the hotspot network.
*   **Address Spoofing:** Use DHCP snooping to mitigate any DHCP server attacks.
*   **Regular Updates:**  Keep the MikroTik RouterOS software updated to protect against known vulnerabilities.

## Self Critique and Improvements:

The current configuration is a good start for a basic static IP assignment via MAC addresses in a Hotspot network. However, it could be improved by:
* **Implementing AAA server:** For a proper Hotspot setup, AAA (Authentication, Authorization, Accounting) should be implemented.
* **Address Lists:**  Address Lists for managing IPs for access control, traffic shaping, and more are essential.
* **Dynamic address assignment:** Only assigning static leases to specific clients is not ideal for a normal client pool in a Hotspot, and a combination of static and dynamic assignments is essential for practical networks.
* **Integration with user management:** Combine this with Hotspot user management and user profiles to create a real-world use case.
* **Error handling:** The error handling in the REST API section should include more specific examples for common errors, and also include handling of non-200 http status codes in general.
* **Configuration Management:** It is worth noting that a more sophisticated configuration system could be integrated, to ensure that network documentation and configuration does not diverge, and that configurations can be deployed consistently.

## Detailed Explanation of Trade-offs:

*   **Static vs. Dynamic:** Static IP assignments via the MAC server guarantee a specific device gets the same IP consistently. However, for clients that do not need this feature, it is much simpler to assign dynamic IPs for all devices.
* **Static Lease Scope:** For ease of management, DHCP scope and DHCP client scope should be clearly defined. There must be enough IP addresses for both static and dynamic assignments, and the network scope should be clearly defined.
* **Management overhead:** Static IP assignment requires additional configuration overhead for managing IP mapping with MAC addresses, especially on large networks.
* **Resource Utilization:** While the MAC server itself doesn't consume excessive resources, managing larger lists of MAC mappings on very high-traffic networks could become resource intensive. Be sure to monitor CPU and memory usage.

## Configuration for Specific RouterOS Versions:

The configuration commands provided should work correctly in the mentioned versions of RouterOS (6.48 and 7.x, targeting 7.12). If older versions are considered, pay attention to any syntax changes or feature availability and consult the RouterOS version release documentation.

By following these steps and explanations, you should be able to configure a functional MAC server on your MikroTik router within a Hotspot environment. This implementation gives you better control over IP assignments, adding an extra layer of control to your network. Remember to test everything thoroughly after configuration and to always consult the MikroTik documentation for more specific details.
