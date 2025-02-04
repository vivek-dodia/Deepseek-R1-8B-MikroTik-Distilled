Okay, let's dive into configuring RADIUS authentication on a MikroTik router with a focus on a SOHO environment, targeting RouterOS 6.48, and using a specific bridge interface and subnet.

## Scenario Description:

We're setting up a MikroTik router in a Small Office/Home Office (SOHO) environment to authenticate users via a RADIUS server.  Users connected to the `bridge-2` interface, which operates on the 159.81.121.0/24 subnet, will need to be authenticated via a RADIUS server before gaining full network access. This is useful for restricting access to a network, giving controlled and managed access to particular users.

## Implementation Steps:

Here's a step-by-step guide with CLI commands and Winbox GUI guidance:

### 1. Step 1: Configure the Bridge Interface

*   **Description:**  We'll start by ensuring our `bridge-2` interface is properly configured, along with its assigned subnet, before implementing RADIUS. This step is crucial to ensuring that later steps in the implementation process function as expected.
*   **Pre-Configuration:**  Let's assume `bridge-2` and the subnet `159.81.121.0/24`  exist.  If not, follow the instructions below.
*   **Action:** First, check if a bridge named "bridge-2" already exists.
    ```mikrotik
    /interface bridge print
    ```
*   **Example Output Before:**
   ```
    Flags: X - disabled, R - running
    0  R name="bridge1" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled mac-address=A0:B1:C2:D3:E4:F5
         protocol-mode=rstp priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6
    1    name="bridge-vlan" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled mac-address=A0:B1:C2:D3:E4:F6
        protocol-mode=rstp priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6
   ```
* **Action:**  If `bridge-2` doesn't exist, create it. Otherwise, make sure that the bridge is enabled.
   ```mikrotik
    /interface bridge add name=bridge-2
    /interface bridge enable bridge-2
    ```
*   **Example Output After:**
    ```
    Flags: X - disabled, R - running
    0  R name="bridge1" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled mac-address=A0:B1:C2:D3:E4:F5
         protocol-mode=rstp priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6
    1    name="bridge-vlan" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled mac-address=A0:B1:C2:D3:E4:F6
        protocol-mode=rstp priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6
    2 R  name="bridge-2" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled mac-address=A0:B1:C2:D3:E4:F7
        protocol-mode=rstp priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6
   ```
*   **Action:** Assign an IP address from our defined subnet to the bridge interface.
    ```mikrotik
    /ip address add address=159.81.121.1/24 interface=bridge-2
    ```
*   **Winbox GUI:** Navigate to `Interface -> Bridge -> Add (+)`. Enter `bridge-2` in `Name` then select `OK`. Now navigate to `IP -> Addresses -> Add (+)`. Assign the address `159.81.121.1/24` and select `bridge-2` under `Interface`, then select `OK`.
*   **Effect:** The bridge interface `bridge-2` is now created, running, and has an IP address.

### 2. Step 2: Configure the RADIUS Server

*   **Description:**  Now, we need to add the details of our RADIUS server to the MikroTik configuration, so it knows where to send authentication requests.
*   **Pre-Configuration:** You need the IP address or hostname of your RADIUS server, the port (usually 1812 for authentication), and the secret key that both the MikroTik and the RADIUS server share.
*   **Action:** Add the RADIUS server.
    ```mikrotik
    /radius add address=192.168.88.10 secret=your_radius_secret service=ppp,hotspot,login,wireless,dhcp-server timeout=10
    ```
    Replace `192.168.88.10` with your RADIUS server's address and `your_radius_secret` with your shared secret.
*   **Winbox GUI:** Navigate to `RADIUS -> Add (+)`. Enter the following:
    *   **Address:** `192.168.88.10`
    *   **Secret:** `your_radius_secret`
    *   **Service:** Ensure `ppp`, `hotspot`, `login`, `wireless`, and `dhcp-server` are checked.
    *   **Timeout:** `10`
    *   Select `OK`.
*   **Effect:** The MikroTik now knows how to communicate with the RADIUS server for authentication.

### 3. Step 3: Configure Hotspot Profile

*   **Description:** To enable RADIUS authentication on the bridge interface, we'll leverage the hotspot feature on RouterOS, but without enabling the actual hotspot. A hotspot profile provides the basis for user authentication.
* **Action:** Create a hotspot profile.
    ```mikrotik
    /ip hotspot profile add name=radius-auth hotspot-address=159.81.121.1 dns-name=radius-auth use-radius=yes
    ```
* **Winbox GUI:** Navigate to `IP -> Hotspot -> Hotspot Profiles -> Add (+)`. Enter the following:
    *   **Name:** `radius-auth`
    *   **Hotspot Address:** `159.81.121.1`
    *   **DNS Name:** `radius-auth`
    *   Check **Use Radius**
    * Select `OK`
*   **Effect:** We created a hotspot profile which uses radius authentication to authenticate connecting clients.

### 4. Step 4: Configure Hotspot Interface Binding

*   **Description:**  This is where we connect the `bridge-2` interface to the `radius-auth` hotspot profile, enabling the bridge to use radius for authentication.
* **Action:** Configure the hotspot interface.
    ```mikrotik
    /ip hotspot add name=radius-hotspot interface=bridge-2 profile=radius-auth address-pool=none disabled=no
    ```
* **Winbox GUI:** Navigate to `IP -> Hotspot -> Hotspot -> Add (+)`. Enter the following:
    *   **Name:** `radius-hotspot`
    *   **Interface:** `bridge-2`
    *   **Profile:** `radius-auth`
    *   **Address Pool:** `none`
    *   Ensure **Disabled** is unchecked.
    *  Select `OK`.
*   **Effect:** Now devices connecting to the bridge interface will be authenticated via the radius server configured.

## Complete Configuration Commands:

Here's the entire configuration using CLI:

```mikrotik
/interface bridge
add name=bridge-2
/interface bridge enable bridge-2
/ip address
add address=159.81.121.1/24 interface=bridge-2
/radius
add address=192.168.88.10 secret=your_radius_secret service=ppp,hotspot,login,wireless,dhcp-server timeout=10
/ip hotspot profile
add name=radius-auth hotspot-address=159.81.121.1 dns-name=radius-auth use-radius=yes
/ip hotspot
add name=radius-hotspot interface=bridge-2 profile=radius-auth address-pool=none disabled=no
```

**Parameters:**

| Command          | Parameter        | Explanation                                                                                                                                     |
|------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `/interface bridge add`  | `name` | Name of the bridge interface                                                                |
| `/interface bridge enable`  |  `bridge-2` | Enables the bridge interface identified by its name                                                                |
| `/ip address add` | `address`        | IP address and subnet mask for the interface (e.g., `159.81.121.1/24`)                                                                    |
| `/ip address add` | `interface`      | The interface this IP address is assigned to (e.g., `bridge-2`)                                                                              |
| `/radius add`     | `address`        | IP address or hostname of the RADIUS server.                                                                                                 |
| `/radius add`     | `secret`         | Shared secret key used for communication between MikroTik and RADIUS server.                                                                    |
| `/radius add`     | `service`        | Services using RADIUS for authentication (e.g., `ppp,hotspot,login,wireless,dhcp-server`).                                                       |
| `/radius add`     | `timeout`        | How long the MikroTik waits for a RADIUS server response in seconds.                                                                          |
| `/ip hotspot profile add` | `name` | Name of the hotspot profile.                                                                                                      |
| `/ip hotspot profile add` | `hotspot-address` | IP address of the hotspot service. Usually same address that is assigned to the interface using the service                                                                                       |
| `/ip hotspot profile add`| `dns-name` | A DNS name that clients will be redirected to. Generally a captive portal, or redirect page.  |
| `/ip hotspot profile add`| `use-radius` | Enables radius authentication on the hotspot profile.                                                                                              |
| `/ip hotspot add`| `name`  | The name of the hotspot instance. |
| `/ip hotspot add` | `interface` | The interface the hotspot instance uses. |
| `/ip hotspot add` | `profile`  | The hotspot profile the instance uses. |
| `/ip hotspot add` | `address-pool`  | The address pool used to issue IP address to clients. By selecting "none" the client will be expected to have a static IP address in this situation. |
| `/ip hotspot add` | `disabled` | Whether the hotspot service is disabled. Should be set to no. |

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** MikroTik can't connect to the RADIUS server due to firewall rules, IP address errors, or the server being down.
    *   **Solution:** Verify the IP address of the RADIUS server, check firewall rules on both the MikroTik and the RADIUS server, and ping the RADIUS server from the MikroTik using:
        ```mikrotik
        /ping 192.168.88.10
        ```
        If that fails, test the connection to the RADIUS server using another device.
*   **Incorrect Shared Secret:**
    *   **Problem:** The secret configured on the MikroTik doesn't match the one on the RADIUS server.
    *   **Solution:** Double-check the secret configured on both devices, they must match exactly.
*   **RADIUS Server Service Not Enabled:**
    *   **Problem:** The RADIUS service for `hotspot` is not enabled on the RADIUS server, or the RADIUS server isn't properly configured to accept RADIUS requests from the client.
    *  **Solution:** Check the RADIUS server logs and ensure that the service type configured on the client (MikroTik) is enabled on the server. Also, confirm that the RADIUS server is accepting requests from the client IP address.
*   **Firewall Issues:**
    *   **Problem:** MikroTik firewall rules are blocking RADIUS authentication.
    *   **Solution:** Verify your firewall rules. Ensure the MikroTik router allows outbound traffic to the RADIUS server on port 1812 (or your configured port) and that the MikroTik is not blocking the RADIUS responses. Use torch to verify connections on this port from the MikroTik to the server, with `/tool torch interface=bridge-2 port=1812`.
*   **Misconfigured Hotspot Profile:**
   * **Problem:** If the hotspot profile `radius-auth` is not properly configured, it might cause authentication problems.
   * **Solution:** Double check if use-radius is correctly configured. Verify that the IP address assigned to the hotspot profile is correct.
*   **Resource Issues:**
    *   **Problem:**  High RADIUS traffic can cause increased CPU usage on the MikroTik.
    *   **Solution:** Monitor the router's CPU usage (`/system resource print`) and memory usage (`/system resource print`) . If high, consider upgrading the MikroTik hardware, limiting the amount of radius authentication (for example, limiting the rate at which users are allowed to authenticate), or optimizing the RADIUS server itself.

## Verification and Testing Steps:

1.  **Connect a Device:** Connect a device to the network connected to the `bridge-2` interface.
2.  **Verify Initial IP Address:** The device will be assigned an IP address as configured by the network device, or it will have a manually set IP address.
3.  **Monitor Logs:** Watch the MikroTik logs (`/log print`) for RADIUS authentication attempts.
4.  **Check RADIUS Server Logs:** Check the RADIUS server logs to see if it's receiving authentication requests and what the response is. Common log locations will include `/var/log/freeradius/radius.log` for FreeRADIUS servers.
5.  **Attempt Authentication:** Try to access the Internet or other network resources. You should be prompted to authenticate via RADIUS. Verify that the username and password matches what has been configured on the RADIUS server.
6.  **Use Torch:** Use MikroTik's Torch tool to verify the traffic on the bridge. Start by opening a new terminal window on the MikroTik.
    ```mikrotik
    /tool torch interface=bridge-2 port=1812
    ```
    This will verify whether any traffic is flowing to the RADIUS server on port 1812.
7.  **Use Ping:**  Use MikroTik's ping tool to verify the connection to the RADIUS server. Start by opening a new terminal window on the MikroTik.
    ```mikrotik
    /ping 192.168.88.10
    ```
     If the ping fails, double check that the IP address you've configured on the MikroTik is correct.

## Related Features and Considerations:

*   **MAC Authentication:** In addition to username/password authentication, you can implement MAC address-based authentication via RADIUS, which is helpful if users are configured with static IP addresses, and only need to be authenticated by MAC addresses.
*   **Accounting:**  Configure RADIUS accounting to track user session times and data usage.
*   **Multiple RADIUS Servers:** Add multiple RADIUS servers for redundancy and load balancing.
*   **Captive Portal:** Implement a captive portal for a more user-friendly authentication experience.  You can achieve this by enabling the hotspot service and modifying the captive portal settings to be user friendly.
*   **Dynamic VLANs:** Use RADIUS to dynamically assign VLANs based on user authentication.
*   **Radius Groups:** Configure the RADIUS server to assign users to specific groups, allowing more granular control over access.
*   **Address Pools:** If you need to assign IP addresses via DHCP in conjunction with radius authentication, you'll need to configure an address pool on the Mikrotik, and then configure DHCP to use the specified address pool.

## MikroTik REST API Examples (if applicable):

While MikroTik's REST API doesn't directly support every command, here are examples of how you can add a RADIUS server and a hotspot using the API:

**Note:** The MikroTik API requires authentication and proper headers for requests. We'll assume a session is already established.  For simplicity, we're using `curl` with the `-k` flag to bypass SSL certificate verification.

### 1. Adding a RADIUS Server via API:

*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **Request JSON Payload:**

    ```json
    {
      "address": "192.168.88.10",
      "secret": "your_radius_secret",
      "service": "ppp,hotspot,login,wireless,dhcp-server",
      "timeout": "10"
    }
    ```

*   **`curl` Command:**
    ```bash
    curl -k -H "Content-Type: application/json" -d '{"address": "192.168.88.10", "secret": "your_radius_secret", "service": "ppp,hotspot,login,wireless,dhcp-server", "timeout": "10"}' https://your_mikrotik_ip/rest/radius
    ```

*   **Example Response (Success 201 Created):**
    ```json
    {
    	".id":"*1",
       "address": "192.168.88.10",
       "secret": "your_radius_secret",
       "service": "ppp,hotspot,login,wireless,dhcp-server",
       "timeout": "10"
    }
    ```

*   **Error Handling:**
    *   If the request fails (e.g., invalid parameters, unauthorized), the API will return a corresponding error message and code (e.g., 400 Bad Request).
    *   Check the API response carefully for error details.
    *   For example, if an invalid IP address is provided, the error response would be similar to:
    ```json
    {
       "message": "Invalid value for address"
    }
    ```

### 2. Adding a Hotspot Configuration via API:
* **Endpoint:** `/ip/hotspot`
* **Method:** `POST`
* **Request JSON Payload:**

```json
{
    "name": "radius-hotspot",
    "interface": "bridge-2",
    "profile": "radius-auth",
    "address-pool": "none",
    "disabled": "false"
}
```
* **`curl` Command:**
```bash
curl -k -H "Content-Type: application/json" -d '{"name": "radius-hotspot", "interface": "bridge-2", "profile": "radius-auth", "address-pool": "none", "disabled": "false"}' https://your_mikrotik_ip/rest/ip/hotspot
```
*  **Example Response (Success 201 Created):**
```json
    {
        ".id": "*1",
        "name": "radius-hotspot",
        "interface": "bridge-2",
        "profile": "radius-auth",
        "address-pool": "none",
        "disabled": "false",
    }
```

* **Error Handling**
    *   If the request fails (e.g., invalid parameters, unauthorized), the API will return a corresponding error message and code (e.g., 400 Bad Request).
    *   Check the API response carefully for error details.
    *   For example, if an invalid parameter is provided, the error response would be similar to:
```json
{
  "message": "invalid value for parameter \"profile\""
}
```

## Security Best Practices:

*   **Strong Shared Secret:** Use a strong, randomly generated secret key for the RADIUS connection. Do not use a dictionary word. Use a long string of random characters, or a password generation tool.
*   **Secure RADIUS Server:** Secure your RADIUS server from unauthorized access.
*   **Firewall Rules:** Limit access to the RADIUS server to the MikroTik router IP address. Ensure that both inbound and outbound connections from the RADIUS server are explicitly allowed.
*   **Monitor Logs:** Regularly monitor the MikroTik logs for failed authentication attempts.
*   **Secure API Access:** Secure your MikroTik API access with a strong password and restrict access to trusted networks. Ensure that API access is not available to external networks without a proper layer of security in place (e.g. a VPN).
*   **Regular Updates:** Keep RouterOS and your RADIUS server software updated to patch security vulnerabilities.
*   **Limit services on interface:** If the interface does not require all services, reduce the services available on the interface using firewall rules. Specifically, if the interface does not require webserver access, create a firewall rule to drop all traffic on the webserver ports.

## Self Critique and Improvements:

*   **Simplicity:** The current configuration is basic and uses Hotspot without a Captive portal for ease of implementation.  A more robust configuration would include a captive portal.
*   **Error Handling:**  Error handling is present but could be expanded. For example, by adding a fall-back mechanism.
*   **Performance:** In a larger-scale deployment, a more in-depth analysis of CPU and memory would be necessary, and resource considerations would have to be taken into account.
*   **Redundancy:** The configuration relies on a single RADIUS server. A failover RADIUS server could be implemented to prevent authentication downtime.
*   **Automation:** The configuration can be further improved by integrating it into a configuration management system (e.g. Ansible, Puppet) to enable automation and rollouts.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users that connect to a network. RADIUS allows for the centralization of user credentials, permissions, and accounting data on a centralized server, instead of having individual routers or switches store this data.

**Key Concepts:**

*   **Authentication:** Verifies a user's identity (e.g., username/password)
*   **Authorization:** Determines the access levels or permissions a user has (e.g., network resources).
*   **Accounting:** Tracks the network usage by each user (e.g., data usage, session time).

**How RADIUS works in our scenario:**

1.  A user connects to the network behind the MikroTik `bridge-2` interface.
2.  The MikroTik, acting as a RADIUS client, sends an authentication request to the configured RADIUS server, including user credentials, if available.
3.  The RADIUS server verifies the credentials against its user database.
4.  The RADIUS server sends back an access-accept or access-reject response, based on whether the authentication was successful.
5.  If access is accepted, the user is granted access. Otherwise, access is denied.
6.  During the user's connection, the MikroTik can also send accounting information to the RADIUS server.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:** Using local authentication on a MikroTik router is simple for small environments but becomes cumbersome to manage as the number of users increases. RADIUS centralizes user management. The trade-off is the added complexity of the RADIUS infrastructure.
*   **Hotspot vs. other methods:**  For simple user based radius authentication, the Hotspot feature in MikroTik provides a very simple method to achieve radius authentication without enabling the full functionality of a captive portal. The trade-off is reduced configuration options, and increased dependencies on using the hotspot feature.
*   **Single vs. Multiple RADIUS Servers:** A single RADIUS server is easier to manage, but represents a single point of failure. Multiple RADIUS servers provide fault tolerance but add to management complexity.
*   **RADIUS vs. Other Authentication Protocols:** RADIUS is widely supported and well-understood.  Alternatives such as TACACS+ exist which can provide more specific control and logging capabilities, however this often requires more complex setup and management.  RADIUS is often chosen for it's simplicity and wide-spread compatibility.

## Configuration for Specific RouterOS Versions:

This configuration is specifically targeted for RouterOS 6.48, but will also work with later versions.  The commands used are not deprecated and are relevant in modern RouterOS versions. There may be extra features available in later versions that are not included in this configuration for the sake of targeting 6.48.

This configuration provides a solid foundation for implementing RADIUS authentication in a SOHO environment.  It demonstrates the flexibility of MikroTik RouterOS and how the hotspot feature can be used in unusual ways to achieve a desired networking outcome. Remember to adjust settings according to your own environment.
