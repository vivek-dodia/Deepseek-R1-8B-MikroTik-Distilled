Okay, let's dive deep into configuring RADIUS authentication on a MikroTik router, focusing on practical implementation within an SMB network, targeting RouterOS 6.48. We'll use a specific subnet, interface, and provide all the necessary configuration, verification, and troubleshooting details.

## Scenario Description:

We aim to implement RADIUS authentication for clients connected to the `ether-68` interface on a MikroTik router. This setup will offload authentication responsibilities to an external RADIUS server, providing centralized user management and security. The network segment for clients will be 160.147.80.0/24. This setup is common in SMB environments requiring a higher degree of user control and audit logging for network access, especially when providing Wi-Fi access or VPN connections.

## Implementation Steps:

Here's a step-by-step guide to implement RADIUS authentication on the specified interface, targeting advanced configurations for RouterOS 6.48:

1.  **Step 1: Configure the Interface (Ethernet)**

    *   **Explanation:** We ensure the interface we'll use for client connectivity is properly configured with an IP address within the specified subnet. We'll also set a simple default DHCP server if there are no clients using static ips.

    *   **Before Configuration:** Assume the `ether-68` interface is unconfigured.
    *   **CLI Command:**
        ```mikrotik
        /ip address
        add address=160.147.80.1/24 interface=ether-68
        /ip dhcp-server
        add address-pool=default disabled=no interface=ether-68 lease-time=3h name=dhcp-ether-68
        /ip dhcp-server network
        add address=160.147.80.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=160.147.80.1
        ```
    *   **Winbox GUI:**
        *   Navigate to *IP* -> *Addresses*. Add a new address `160.147.80.1/24` to `ether-68`.
        *   Navigate to *IP* -> *DHCP Server*. Click the '+' button. Select `ether-68` in *Interface*, click the DHCP button, add a *Name*.
        *   Navigate to *IP* -> *DHCP Server* -> *Networks*. Add a new network, specify `160.147.80.0/24` for *Address*, `160.147.80.1` for *Gateway*, and `8.8.8.8,8.8.4.4` for *DNS Servers*.
    *   **After Configuration:** The `ether-68` interface will have an IP address and DHCP services and clients connected to it will be able to receive an IP.
    *   **Effect:** Clients connected to `ether-68` can now communicate within the subnet and have basic internet access.

2.  **Step 2: Configure the RADIUS Server**

    *   **Explanation:** Here, we configure the RADIUS server settings on the MikroTik, including IP address, secret, and any other parameters if any.

    *   **Before Configuration:** No RADIUS server configured.
    *   **CLI Command:**
        ```mikrotik
        /radius
        add address=192.168.100.100 secret="your_radius_secret" service=ppp timeout=10
        ```
    *   **Winbox GUI:**
        *   Navigate to *RADIUS*. Click the '+' button.
        *   In the new window fill the fields with the values:  `Address` with `192.168.100.100`, `Secret` with `"your_radius_secret"`, and `Service` with `ppp`.
    *   **After Configuration:** The MikroTik router is now configured to use the specified RADIUS server.
    *   **Effect:** The router will attempt to communicate with this server when RADIUS authentication is triggered.

3.  **Step 3: Configure PPP Profile with RADIUS Authentication**

    *   **Explanation:**  We will create a PPP profile that enables RADIUS authentication to control which users can connect via PPP on the network.

    *   **Before Configuration:** Assume no PPP profiles exist with RADIUS enabled.
    *   **CLI Command:**
        ```mikrotik
        /ppp profile
        add name="radius-profile" local-address=10.255.255.1 remote-address=10.255.255.2 use-encryption=yes use-mpls=no only-one=yes change-tcp-mss=yes
        set "radius-profile" use-radius=yes
        ```
    *   **Winbox GUI:**
        *   Navigate to *PPP* -> *Profiles*. Click the '+' button.
        *   Fill the fields with the values: `Name` with `radius-profile`, `Local Address` with `10.255.255.1`, `Remote Address` with `10.255.255.2`, and Check `Use Encryption`, `Only One`, `Change TCP MSS`.
        *   Click on tab *Limits*, and enable *Use Radius* option.
    *   **After Configuration:** A PPP profile using RADIUS is created.
    *   **Effect:** Any PPP connections using this profile will have their authentication requests handled by the RADIUS server.

4. **Step 4: Enable PPP Server for Testing**

    * **Explanation:** Enable the PPP server to test with the given profile. We use a PPP server over an ethernet interface, however, this is just an example.
    * **Before Configuration:** Assume that the PPP interface is unconfigured
    * **CLI Command:**
        ```mikrotik
        /interface ppp server
        add name=ppp-ether-68 interface=ether-68 profile=radius-profile service=any enabled=yes
        ```
    * **Winbox GUI:**
       * Navigate to *PPP* -> *Interface*. Click the `PPP server` tab.
       * Click the '+' button and fill the fields with the values: `Name` with `ppp-ether-68`, `Interface` with `ether-68`, `Profile` with `radius-profile`,  and ensure that `Enabled` checkbox is marked.
    * **After Configuration:** The PPP server is now enabled using the radius profile.
    * **Effect:** Any incoming connection will now be authenticated using the radius server.

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to implement the setup:

```mikrotik
/ip address
add address=160.147.80.1/24 interface=ether-68
/ip dhcp-server
add address-pool=default disabled=no interface=ether-68 lease-time=3h name=dhcp-ether-68
/ip dhcp-server network
add address=160.147.80.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=160.147.80.1
/radius
add address=192.168.100.100 secret="your_radius_secret" service=ppp timeout=10
/ppp profile
add name="radius-profile" local-address=10.255.255.1 remote-address=10.255.255.2 use-encryption=yes use-mpls=no only-one=yes change-tcp-mss=yes
set "radius-profile" use-radius=yes
/interface ppp server
add name=ppp-ether-68 interface=ether-68 profile=radius-profile service=any enabled=yes
```

**Parameter Explanation:**

| Command                      | Parameter         | Description                                                                                                                                   |
| :--------------------------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `/ip address add`            | `address`         | The IP address and subnet mask for the interface.                                                                                           |
|                              | `interface`        | The name of the interface to assign the IP address to.                                                                                          |
| `/ip dhcp-server add`       | `address-pool`    | DHCP address pool.                                                                                                       |
|                              | `disabled`        | Whether the DHCP server is enabled or not.                                                                                        |
|                              | `interface`       | The interface for DHCP server.                                                                                                        |
|                              | `lease-time`      | IP lease time assigned by DHCP Server.                                                                                                     |
|                              | `name`            | DHCP server name.                                                                                                           |
| `/ip dhcp-server network add` | `address`       | DHCP network address range.                                                                                                 |
|                              | `dns-server`     | DNS servers assigned by DHCP server.                                                                                                         |
|                              | `gateway`        | Default Gateway assigned by DHCP Server.                                                                                                 |
| `/radius add`                | `address`         | The IP address of the RADIUS server.                                                                                                         |
|                              | `secret`          | The shared secret key used to communicate with the RADIUS server. **MUST match the RADIUS server configuration.**                     |
|                              | `service`         | The service type that RADIUS will be used for (e.g., ppp, hotspot).                                                                                   |
|                              | `timeout`         | The timeout for communication with RADIUS server, in seconds                                                                                   |
| `/ppp profile add`           | `name`            | The name of the PPP profile.                                                                                                                  |
|                              | `local-address`   | The local IP address assigned to a PPP connection.                                                                                              |
|                              | `remote-address`  | The remote IP address assigned to a PPP connection.                                                                                              |
|                              | `use-encryption`  | Enable/disable encryption for the PPP connection.                                                                                                 |
|                              | `use-mpls`        |  Enable/disable mpls for the PPP connection.                                                                                                 |
|                              | `only-one`        | Allow only one connection per user.                                                                                             |
|                              | `change-tcp-mss`  | Enable/disable change tcp mss for the PPP connection.                                                                                            |
| `/ppp profile set`           | `use-radius`      | Enable or disable RADIUS authentication for the profile.                                                                                     |
| `/interface ppp server add` | `name`            | The name of the PPP server interface.                                                                                                                  |
|                             | `interface`       | The ethernet interface that the ppp server is going to use.                                                                                              |
|                             | `profile`        | The profile to be used by the server.                                                                                              |
|                             | `service`         | The service type to be used by the server.                                                                                              |
|                             | `enabled`         | Enable/disable the ppp server                                                                                              |

## Common Pitfalls and Solutions:

*   **RADIUS Server Connectivity Issues:**
    *   **Problem:** The MikroTik router cannot reach the RADIUS server.
    *   **Solution:**
        *   Verify network connectivity using `ping 192.168.100.100` (or your RADIUS server's address). Check for any firewall rules blocking the traffic.
        *   Ensure the RADIUS server is listening on the correct IP address and port (usually UDP 1812 for authentication and 1813 for accounting).
        *   Double-check the shared secret on both the MikroTik and the RADIUS server - capitalization and spacing must be exact.
*   **Authentication Failures:**
    *   **Problem:** Users are unable to authenticate, and no log entries in the RADIUS server.
    *   **Solution:**
        *   Check the MikroTik logs with `/system logging print follow-only where topics~"radius"`. Look for any error messages.
        *   Verify the username and password on the RADIUS server are correct.
        *   Ensure that the RADIUS configuration is correctly set on the RADIUS server.
*  **Incorrect RADIUS Configuration**
    *   **Problem:** The MikroTik router is not communicating with the RADIUS server, and no log entries in the RADIUS server.
    *   **Solution:**
        *   Ensure the service type is correct. For PPP connections use `service=ppp`.
        *   Ensure the secret is matching on both servers.
*   **Resource Issues:**
    *   **Problem:** High CPU usage due to many RADIUS requests or large number of users being connected.
    *   **Solution:**
        *   Monitor CPU usage `/system resource print`.
        *   Optimize the RADIUS server if possible to improve response time.
        *   Consider using a more powerful MikroTik device if high load is expected.

## Verification and Testing Steps:

1.  **Check MikroTik Logs:**
    *   Use `/system logging print follow-only where topics~"radius"` to observe communication with the RADIUS server, including authentication attempts and responses.
2.  **RADIUS Server Logs:**
    *   Check the RADIUS server logs for authentication requests and successes/failures. These logs should provide detailed information, such as the user who attempted the authentication.
3. **Connect with PPP Client:**
    *   Use a PPP client on a machine connected to `ether-68`, and try to connect to the router using a username and password.
    *   The authentication process should be verified using logs from both router and radius.

## Related Features and Considerations:

*   **Accounting:** Configure RADIUS accounting to log user activity (start/stop times, data usage) by adding the `service=ppp,accounting` and enabling accounting.
*   **Dynamic VLANs:** RADIUS can assign VLANs dynamically based on user authentication attributes.
*   **Hotspot:** You can combine RADIUS with the MikroTik hotspot feature, enabling user-based authentication for guest Wi-Fi access.
*   **User Profiles:** Leverage RADIUS attributes to control user's access speed, connection duration, etc.
*   **IP Pool:** You can combine radius with a specific ip-pool for PPP clients.

## MikroTik REST API Examples (if applicable):

MikroTik's REST API is generally more useful for other features than pure RADIUS. However, here's an example of how you might add a new RADIUS entry using the API:

```json
{
 "method": "add",
 "resource": "/radius",
 "data": {
  "address": "192.168.100.100",
  "secret": "your_radius_secret",
  "service": "ppp",
  "timeout": 10
 }
}
```
**Description:**
- `/radius` : The routeros resource.
- `add` : The action to be performed.
- `address` :  The IP address of the RADIUS server.
- `secret` : The shared secret used by RADIUS.
- `service` : The service that this radius will handle (e.g. ppp, hotspot).
- `timeout` : The timeout in seconds.

**Expected Response:**
A successful request will return a JSON object with an "id" key which will be the id assigned to the new radius configuration.

**Error Handling:**
If an error happens, the response json will contain a `message` property describing what went wrong.

## Security Best Practices:

*   **Secure RADIUS Secret:** Use a long, complex, and random shared secret. Avoid default or weak secrets.
*   **Secure Communication:** For sensitive environments, consider using RADIUS over TLS (RadSec) to encrypt communication between the router and the server.
*   **Access Control:** Only allow RADIUS requests from trusted source IPs using firewall rules on the RADIUS server.
*   **Regular Auditing:** Regularly check logs from both MikroTik and RADIUS servers.
*   **Limit PPP users**
    *   Use the `only-one=yes` setting in the ppp profile to limit one session per user.

## Self Critique and Improvements:

This configuration provides a solid base for RADIUS authentication on MikroTik for PPP services, however it can be improved by using more advanced features:

*   **RadSec (RADIUS over TLS):** Implement RadSec to provide an encrypted channel for RADIUS communication, improving security.
*   **Fine-Grained Authorization:** Utilize RADIUS attributes for more complex authorization policies, like specific bandwidth limitations.
*   **Dynamic IP Assignment:** Use a dynamic pool of IPs assigned on the radius.
*   **External Accounting:** Log usage to a dedicated accounting server.
*   **Hotspot:** Use this setup with the hotspot functionality.

## Detailed Explanation of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized authentication, authorization, and accounting for users attempting to access a network. It is widely used in enterprise and carrier networks to manage access control and track user activity. In this context, the MikroTik router acts as a RADIUS client, forwarding authentication requests to a RADIUS server, which determines whether a user should be granted access and what resources they can use. This makes user management scalable and less dependant on the device configuration.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Simpler to configure, but not scalable, harder to administer, and lacks logging for audits. Suitable for small, basic networks.
    *   **RADIUS:** More complex setup but it offers centralized user management, scalability, detailed logging, and advanced authorization options. Suitable for networks that require more control over user management.

*   **Service Type:**
    *   **PPP vs Hotspot:** The service parameter needs to match the authentication type to be performed on the device.
    *   **PPP:** Used for Point-to-Point Protocol (PPP) based connections, like dial-up, L2TP or PPTP VPNs.
    *   **Hotspot:**  Used for web-based authentication often used for guest Wi-Fi networks.

*   **Secret Length & Complexity:**
    *   **Shorter Secrets:** Easier to remember, but vulnerable to brute-force attacks.
    *   **Longer & Complex Secrets:** More secure, but harder to manage. Essential for a secure deployment.

## Configuration for Specific RouterOS Versions:

This documentation specifically targets RouterOS 6.48 and 7.x. The commands used are compatible with these versions, however you should check the manual for exact configuration and options when deploying the configuration for an earlier or later version.

This is a comprehensive implementation of RADIUS authentication on a MikroTik router, providing the detailed steps, configurations, explanations, and security advice needed to successfully deploy this feature within an SMB network.
