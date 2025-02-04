Okay, let's craft a comprehensive guide to RADIUS authentication on MikroTik RouterOS 7.11 (also considering 6.48 and general 7.x compatibility) within a SOHO network context, focusing on a specific VLAN interface.

## Scenario Description:

We are configuring a MikroTik router in a Small Office/Home Office (SOHO) environment to authenticate network clients connected to VLAN 87 (interface name: `vlan-87`, subnet: 241.174.160.0/24) via a RADIUS server. This setup will control access to the network, ensuring that only users with valid credentials on the RADIUS server can obtain IP addresses and access the internet. This scenario can be used for simple authentication, but also for complex use cases such as limiting users by time, data usage, and/or specific VLANs.

## Implementation Steps:

Here’s a step-by-step guide, explaining each action and providing examples in both CLI and Winbox GUI.

**1. Step 1: VLAN Interface Configuration:**

   * **Action:** Ensure that the `vlan-87` interface exists and is configured correctly with VLAN ID 87. This step assumes the underlying physical interface (e.g., `ether1`) is already set up and can carry VLAN traffic.
   * **Before Configuration:** Let's say the router has an interface named `ether1`. It might be carrying default traffic. Let's check that the `ether1` interface exists.
    ```mikrotik
    /interface print
    ```
     *Example Output*
    ```
     Flags: D - dynamic; X - disabled, R - running
      #     NAME             TYPE      MTU   MAC-ADDRESS       ARP      INTERFACE
      0  R  ether1           ether     1500  00:0C:42:XX:YY:ZZ  enabled
    ```
   * **Configuration (CLI):**
      ```mikrotik
      /interface vlan
      add name=vlan-87 vlan-id=87 interface=ether1
      ```
   * **Configuration (Winbox GUI):**
      1. Navigate to *Interface* > *VLAN*.
      2. Click the "+" button to add a new VLAN interface.
      3. Set `Name` to `vlan-87`.
      4. Set `VLAN ID` to `87`.
      5. Set `Interface` to `ether1`.
      6. Click "Apply" and "OK".
   * **After Configuration:**
       ```mikrotik
    /interface print
       ```
        *Example Output*
       ```
       Flags: D - dynamic; X - disabled, R - running
        #     NAME             TYPE      MTU   MAC-ADDRESS       ARP      INTERFACE
        0  R  ether1           ether     1500  00:0C:42:XX:YY:ZZ  enabled
        1  R  vlan-87         vlan      1500  00:0C:42:XX:YY:ZZ  enabled  ether1
      ```
   * **Effect:** A new VLAN interface, `vlan-87`, is created on top of the physical interface `ether1`. All traffic with VLAN tag 87 will be processed by this interface.

**2. Step 2: IP Address Configuration:**

   * **Action:** Assign an IP address to the `vlan-87` interface. This is the gateway IP for clients on this VLAN.
   * **Before Configuration:**
      ```mikrotik
     /ip address print
     ```
      *Example Output*
    ```
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS            NETWORK         INTERFACE
    ```
   * **Configuration (CLI):**
     ```mikrotik
     /ip address
     add address=241.174.160.1/24 interface=vlan-87
     ```
   * **Configuration (Winbox GUI):**
      1. Navigate to *IP* > *Addresses*.
      2. Click the "+" button to add a new IP address.
      3. Set `Address` to `241.174.160.1/24`.
      4. Set `Interface` to `vlan-87`.
      5. Click "Apply" and "OK".
  * **After Configuration:**
     ```mikrotik
      /ip address print
     ```
      *Example Output*
     ```
     Flags: X - disabled, I - invalid, D - dynamic
      #   ADDRESS            NETWORK         INTERFACE
      0   241.174.160.1/24   241.174.160.0  vlan-87
     ```
   * **Effect:** The `vlan-87` interface is now configured with an IP address, allowing routing and DHCP services on the subnet 241.174.160.0/24.

**3. Step 3: RADIUS Server Configuration:**

   * **Action:** Add a RADIUS server to the router's configuration, setting up parameters for communication between the router and the server.
   * **Before Configuration:**
        ```mikrotik
        /radius print
        ```
       *Example Output*
       ```
        Flags: X - disabled
       ```
   * **Configuration (CLI):**
      ```mikrotik
      /radius
      add address=192.168.1.10 secret="mysecret" service=ppp,dhcp,hotspot,wireless timeout=30s accounting-port=1813 authentication-port=1812
      ```
      *Replace `192.168.1.10` with your RADIUS server IP address and `"mysecret"` with your shared secret.*
   * **Configuration (Winbox GUI):**
      1. Navigate to *RADIUS*.
      2. Click the "+" button to add a new RADIUS server.
      3. Set `Address` to `192.168.1.10` (or your server's IP).
      4. Set `Secret` to `mysecret` (or your shared secret).
      5. Set `Service` to `ppp,dhcp,hotspot,wireless`.
      6. Set `Timeout` to `30s`.
      7. Set `Authentication Port` to `1812`.
      8. Set `Accounting Port` to `1813`.
      9. Click "Apply" and "OK".
    * **After Configuration:**
       ```mikrotik
      /radius print
      ```
      *Example Output*
      ```
      Flags: X - disabled
      #   ADDRESS         SECRET  TIMEOUT  AUTHENTICATION-PORT ACCOUNTING-PORT   SERVICE
      0  192.168.1.10   mysecret 30s           1812                 1813  ppp,dhcp,hotspot,wireless
       ```
   * **Effect:** The router now knows how to communicate with the RADIUS server for authentication and accounting. The `service` parameter defines which services will use this RADIUS server. In this case, DHCP will use RADIUS authentication.

**4. Step 4: DHCP Server Configuration (with RADIUS):**

   * **Action:** Set up a DHCP server on `vlan-87` and enable RADIUS authentication for it.
   * **Before Configuration:**
      ```mikrotik
       /ip dhcp-server print
      ```
      *Example Output*
      ```
      Flags: X - disabled, I - invalid
      ```
   * **Configuration (CLI):**
      ```mikrotik
      /ip dhcp-server
      add address-pool=default-dhcp authoritative=yes disabled=no interface=vlan-87 name=dhcp-vlan87 use-radius=yes
      /ip dhcp-server network
      add address=241.174.160.0/24 dns-server=8.8.8.8 gateway=241.174.160.1
      ```
   * **Configuration (Winbox GUI):**
      1. Navigate to *IP* > *DHCP Server*.
      2. Click the "+" button to add a new DHCP server.
      3. Set `Name` to `dhcp-vlan87`.
      4. Set `Interface` to `vlan-87`.
      5. Set `Address Pool` to `default-dhcp`.
      6. Check `Authoritative`.
      7. Check `Use RADIUS`.
      8. Click "Apply".
      9. Navigate to the *Networks* tab and click the "+" button to add a new DHCP network.
     10. Set `Address` to `241.174.160.0/24`.
     11. Set `Gateway` to `241.174.160.1`.
     12. Set `DNS Server` to `8.8.8.8`.
     13. Click "Apply" and "OK".
   * **After Configuration:**
       ```mikrotik
        /ip dhcp-server print
      ```
      *Example Output*
      ```
     Flags: X - disabled, I - invalid
     #   NAME         INTERFACE  RELAY    ADDRESS-POOL  LEASE-TIME ADD-ARP AUTHORITATIVE USE-RADIUS
     0   dhcp-vlan87 vlan-87                  default-dhcp  10m       yes yes
      ```
       ```mikrotik
       /ip dhcp-server network print
       ```
      *Example Output*
      ```
      Flags: X - disabled
      #   ADDRESS        DNS-SERVER      GATEWAY
      0   241.174.160.0/24 8.8.8.8 241.174.160.1
      ```
   * **Effect:** The DHCP server is now operational on VLAN 87. It will contact the configured RADIUS server before assigning an IP address to a client.

## Complete Configuration Commands:

```mikrotik
/interface vlan
add name=vlan-87 vlan-id=87 interface=ether1

/ip address
add address=241.174.160.1/24 interface=vlan-87

/radius
add address=192.168.1.10 secret="mysecret" service=ppp,dhcp,hotspot,wireless timeout=30s accounting-port=1813 authentication-port=1812

/ip dhcp-server
add address-pool=default-dhcp authoritative=yes disabled=no interface=vlan-87 name=dhcp-vlan87 use-radius=yes

/ip dhcp-server network
add address=241.174.160.0/24 dns-server=8.8.8.8 gateway=241.174.160.1
```

**Explanation of Parameters:**

| Command          | Parameter             | Description                                                    |
|-----------------|----------------------|----------------------------------------------------------------|
| `/interface vlan add` | `name`                | Name of the VLAN interface (`vlan-87`).                      |
|                    | `vlan-id`             | VLAN ID (`87`).                                               |
|                    | `interface`           | The physical interface the VLAN uses (`ether1`).               |
| `/ip address add` | `address`            | The IP address and subnet mask (`241.174.160.1/24`).        |
|                    | `interface`           | Interface to apply the IP address (`vlan-87`).                |
| `/radius add`     | `address`            | RADIUS server IP (`192.168.1.10`).                              |
|                    | `secret`             | Shared secret between the router and the RADIUS server.      |
|                    | `service`            | Services that use RADIUS (`ppp,dhcp,hotspot,wireless`).        |
|                    | `timeout`            | Timeout for RADIUS server communication (`30s`).             |
|                    | `authentication-port`| RADIUS authentication port (`1812`).                      |
|                    | `accounting-port`    | RADIUS accounting port (`1813`).                           |
| `/ip dhcp-server add` | `address-pool`      | DHCP address pool to use (`default-dhcp`).                    |
|                    | `authoritative`      | Makes the server the sole DHCP authority on this network (`yes`). |
|                    | `disabled`           | If the DHCP server is enabled or disabled (`no`).          |
|                    | `interface`           | Interface to listen for DHCP requests (`vlan-87`).        |
|                    | `name`                | Name of the DHCP server (`dhcp-vlan87`).                      |
|                    | `use-radius`          | Enables RADIUS authentication for DHCP (`yes`).              |
| `/ip dhcp-server network add`| `address`          | Network and subnet to serve DHCP IP addresses (`241.174.160.0/24`). |
|                    | `dns-server`         | DNS server to provide to clients (`8.8.8.8`).                |
|                    | `gateway`            | Default gateway to provide to clients (`241.174.160.1`).       |

## Common Pitfalls and Solutions:

*   **Incorrect Shared Secret:** If the shared secret on the MikroTik doesn't match the RADIUS server, authentication will fail.
    *   **Solution:** Verify the shared secret on both devices and update it in the MikroTik configuration if needed.
*   **Firewall Issues:** A firewall on either the MikroTik or the RADIUS server might block communication.
    *   **Solution:** Ensure that ports 1812 and 1813 (UDP) are open in the firewalls between the MikroTik router and the RADIUS server.
*   **RADIUS Server Not Reachable:** If the MikroTik cannot reach the RADIUS server, authentication will fail.
    *   **Solution:** Check connectivity using `ping 192.168.1.10` (or the RADIUS IP). If there is a failure, check the network configurations and the status of your RADIUS server.
*   **Invalid RADIUS Configuration on the Server**: If the RADIUS configuration is wrong on the RADIUS server, authentication will fail.
    *   **Solution:** Verify that you have added the MikroTik router as an allowed client on the RADIUS server using the secret configured previously.
*   **Incorrect Service Parameter in RADIUS Configuration:** If the configured service in the RADIUS config doesn't include 'dhcp', dhcp clients will not be authorized via RADIUS.
     *   **Solution:** Verify that the configured `service` parameter in the `/radius` configuration includes `dhcp`.
*   **DHCP Server Errors:** If the `dhcp-server` configuration is wrong, the DHCP service might fail.
    *   **Solution:** Verify the `interface` is set correctly, and that the `address-pool` and `networks` are correct as well.
*   **High CPU Usage:** Can be caused by extensive logging or excessive authentication requests.
    *   **Solution:** Review the logging configuration, consider enabling rate limiting on the DHCP server, and make sure that your MikroTik router has enough resources for the task.
*   **Memory Issues:** Too many DHCP clients can cause the router to run out of memory.
     *   **Solution:** Monitor memory usage. If needed, increase the router's RAM or reduce the number of DHCP clients being served.
*   **RADIUS Server Issues**: If the RADIUS Server is overloaded, it could cause a delay in authentication.
    *   **Solution:** Monitor your RADIUS server performance. If needed, add more capacity for the RADIUS server.

## Verification and Testing Steps:

1.  **Client Connection:** Connect a client device to the VLAN 87 network (ensure the client is configured to obtain an IP address via DHCP).
2.  **RADIUS Logging:** Check the RADIUS server logs for authentication requests from the MikroTik router. Successful authentication should result in an "Access-Accept" message.
3.  **DHCP Lease:** Verify that the client receives an IP address within the 241.174.160.0/24 subnet.
    *   Use the `/ip dhcp-server lease print` command on the MikroTik router to view active DHCP leases.
4.  **MikroTik Router Logging:** Enable RADIUS debugging by using `/system logging add topics=radius action=memory`. Examine the logs via `/system logging print where topics~"radius"`. Check for RADIUS related errors or successes.
5.  **Ping Test:** From the client, ping the router's interface `241.174.160.1`, and then an external IP address to ensure that basic network connectivity is working.
6.  **Torch Tool:** Use MikroTik's `torch` tool on the `vlan-87` interface to capture network traffic and verify that RADIUS communication is taking place. ` /tool torch interface=vlan-87`

## Related Features and Considerations:

*   **User Profiles:** RADIUS can be configured to return specific settings for a user (e.g., bandwidth limits, DNS servers, and VLAN assignments).
*   **Accounting:**  RADIUS accounting can track user session times and data usage.
*   **Multiple RADIUS Servers:** The MikroTik can be configured with multiple RADIUS servers for redundancy.
*   **DHCP Option Sets:** Can be configured to send additional parameters to the client via DHCP, such as the client's VLAN and other options.
*   **Hotspot:** RADIUS authentication in MikroTik is also a key component of the Hotspot feature.
*   **Scripting:**  You can use scripts to automate tasks, such as disabling problematic clients.
*   **Dynamic VLANs:** Using RADIUS with VLANs can dynamically assign clients to different VLANs based on authentication, allowing you to segment traffic.

## MikroTik REST API Examples (if applicable):

MikroTik's REST API can be used to manage the router's configuration, although it's not a direct equivalent to all CLI commands, especially those that directly interact with protocols like RADIUS. However, we can demonstrate how to add a VLAN interface using the API:

**Example: Creating a VLAN Interface via the REST API**

*   **API Endpoint:** `/interface/vlan`
*   **Request Method:** POST
*   **JSON Payload:**
    ```json
    {
        "name": "vlan-87-api",
        "vlan-id": 87,
        "interface": "ether1"
    }
    ```
*   **Expected Response (Success - HTTP 200):**
    ```json
    {
        ".id": "*12"
    }
    ```
    Where `*12` is the auto-assigned id to this VLAN interface. This ID will be needed if you wish to edit or delete this entry.
*   **Expected Response (Failure - HTTP 400 or 500):**
   ```json
   {
     "message": "invalid value",
     "property": "name",
     "details": {
          "value": "vlan-87-api",
          "type": "string",
          "expected-type": null,
          "allowed-values": null
      }
   }
   ```
  This JSON indicates that there was an issue adding the VLAN interface, and that you should check the `property`, `details` parameters to know what happened. In this case, `vlan-87-api` is an invalid name.

**API Explanation:**

| Parameter   | Description                                                  | Type      |
|-------------|--------------------------------------------------------------|-----------|
| `name`      | Name of the VLAN interface.                                  | string    |
| `vlan-id`   | VLAN ID.                                                     | integer   |
| `interface` | The parent interface where the VLAN will be created.  | string    |

**Error Handling:**

When using the MikroTik API, always check the HTTP status code of the response. A code in the `2xx` range indicates success. `4xx` codes usually mean a client-side error (e.g., invalid JSON), while `5xx` indicates a server-side issue. The body of the response typically contains JSON data describing the specific error. Handle errors gracefully by parsing the JSON response.
**Note:** The RADIUS server configuration via API requires using a scripting method in the API. This is outside the scope of this specific implementation.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a long, complex, and random shared secret between the router and the RADIUS server.
*   **Secure RADIUS Server:** Secure the RADIUS server against unauthorized access. Only allow the MikroTik IP to communicate with it.
*   **Firewall Rules:** Implement strict firewall rules on the MikroTik router to control traffic to/from the RADIUS server.
*   **Regular Secret Rotation:** Rotate the RADIUS shared secret periodically.
*   **Limit RADIUS Service Scope:** Limit the services that the RADIUS server provides and only allow it to be used in the services that you want to authenticate.
*   **Monitor Logs:** Regularly monitor MikroTik and RADIUS server logs for suspicious activity.
*   **Use Separate VLAN for RADIUS:** It is recommended to put the router and the RADIUS server into a separate, isolated management VLAN.

## Self Critique and Improvements

This configuration provides a solid baseline for RADIUS authentication within a SOHO network using MikroTik. However, there are a few aspects that could be improved:
*   **Dynamic VLAN Assignment:** Implement dynamic VLAN assignment based on user attributes from the RADIUS server for improved traffic segmentation.
*   **Traffic Shaping Based on RADIUS:** RADIUS information can be used to enforce bandwidth or time limitations on different users.
*   **Multiple RADIUS Servers:** A configuration with multiple RADIUS servers for redundancy would make the system more resilient to failures.
*  **Advanced Logging**: Use `syslog` or other external logging methods to ensure that log files can be stored outside of the MikroTik Router, and improve the logging information.
*   **More Advanced Firewall Rules:** Implement a more comprehensive set of firewall rules specific to this subnet to protect from unauthorized access, even from users that have been authenticated through RADIUS.
*  **Documentation**: Write more comprehensive documentation about the system for future users.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**

RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users attempting to access a network or service. Here's a breakdown:

*   **Authentication:** Verifies the identity of a user. The client sends authentication credentials to the RADIUS server, which validates them against a user database.
*   **Authorization:** Determines what resources a user is allowed to access after successful authentication. This process grants privileges based on the user's profile and settings.
*   **Accounting:** Tracks the resources a user has consumed (e.g., time of connection, data usage). This is used for billing, monitoring, and auditing.
* **How it works**: The MikroTik router acts as a RADIUS client, forwarding authentication requests to the RADIUS server.
* **RADIUS Attributes**: RADIUS exchanges information as a set of attributes. These attributes can specify user login, authentication methods, VLANs, bandwidth limits, and other information needed to control access to the network.

## Detailed Explanation of Trade-offs

*   **Local Authentication vs RADIUS Authentication:** Local authentication is simpler to setup, and good for basic setups. RADIUS is more scalable and provides centralized authentication, and is ideal when you need to manage many users and you need more advanced security features.

*   **RADIUS with Multiple Servers:** This provides more redundancy and better system uptime. However, it adds complexity to the configuration and it might increase costs (if the multiple servers are cloud servers, or servers that are outside your local network).

*   **Static IP vs DHCP with RADIUS:** Static IP addresses are easier to manage and are good for devices that don't require authentication (such as servers). However, DHCP with RADIUS is ideal for devices that require user authentication and dynamic IP allocation (such as user's computers or cellphones).

*   **Basic DHCP vs DHCP with RADIUS:** Basic DHCP configuration is fast to set up and doesn't require additional infrastructure. However, it doesn't offer advanced features for user authentication or access control. DHCP with RADIUS is more complex, but ensures that only authenticated users can access the network.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeted at RouterOS 7.11. However, all mentioned commands are generally compatible with RouterOS 6.48 and other 7.x versions. Some newer versions of RouterOS may include additional RADIUS parameters or features, which are not part of this guide. However, most of these features are also found in older versions and can be configured without issues.

---

This comprehensive guide should give you a solid foundation for implementing RADIUS authentication in your MikroTik environment. Please feel free to ask if you have any more specific questions.
