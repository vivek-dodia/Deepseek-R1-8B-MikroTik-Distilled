Okay, let's dive deep into configuring PPP AAA on a MikroTik router, focusing on a SOHO environment with the specified subnet and interface.

## Scenario Description:

This scenario focuses on enabling PPP (Point-to-Point Protocol) authentication, authorization, and accounting (AAA) using a local user database on a MikroTik router. We will be using a VLAN interface (`vlan-75`, 190.173.141.0/24) for PPP connections. This setup is suitable for managing dial-in users or VPN connections where user authentication and connection tracking are required.

## Implementation Steps:

Here's a step-by-step guide for configuring PPP AAA:

### Step 1: Create the VLAN Interface

* **Purpose:** We first need to have the VLAN interface created and correctly configured.
* **CLI Example:**
    ```mikrotik
    /interface vlan
    add name=vlan-75 vlan-id=75 interface=ether1 disabled=no
    /ip address
    add address=190.173.141.1/24 interface=vlan-75
    ```
    *  **`interface vlan add`:** Adds a new VLAN interface.
        *   `name=vlan-75`: Sets the name of the VLAN interface.
        *   `vlan-id=75`: Sets the VLAN ID.
        *   `interface=ether1`:  Assigns the VLAN to the physical interface `ether1`.
        *   `disabled=no`: Enables the interface.
    *   **`/ip address add`:** Adds an IP address to the VLAN interface.
        *   `address=190.173.141.1/24`: Configures the interface IP.
        *   `interface=vlan-75`: Assigns IP to vlan-75.
* **Winbox GUI:** Navigate to `Interface` and select the `VLAN` tab, then click the `+` button and configure as above. Then navigate to `IP` -> `Addresses` and click the `+` button to add the IP Address.
* **Before:** No `vlan-75` interface, and no IP address assigned to `vlan-75`.
* **After:**  The `vlan-75` interface is created and has the IP address 190.173.141.1/24.

### Step 2: Enable PPP Server (PPPoE in this Example)
*   **Purpose:** Configure the PPPoE server, which will use AAA. This example uses PPPoE but it can be L2TP, PPTP, etc.
* **CLI Example:**
    ```mikrotik
    /interface pppoe-server server
    add service-name=pppoe-vlan-75 interface=vlan-75 max-mru=1480 max-mtu=1480 keepalive-timeout=10 authentication=pap,chap,mschap1,mschap2 one-session-per-host=yes
    ```
    *   **`interface pppoe-server server add`:**  Adds a new PPPoE server.
        *   `service-name=pppoe-vlan-75`: The name of the PPPoE service.
        *   `interface=vlan-75`: Binds the server to the `vlan-75` interface.
        *   `max-mru=1480` & `max-mtu=1480`: Sets the Maximum Receive Unit and Maximum Transmission Unit.
        *   `keepalive-timeout=10`: Sets the timeout for keepalive packets.
        * `authentication=pap,chap,mschap1,mschap2`: Enables different authentication methods.
        *   `one-session-per-host=yes`: Allows only one connection per user.
* **Winbox GUI:** Go to `PPP` -> `PPPoE Servers` and click `+`. Fill in the configuration, ensuring the correct `interface` is selected and all required protocols are selected in the `Authentication` menu.
* **Before:** No PPPoE server configured.
* **After:** PPPoE server `pppoe-vlan-75` is enabled and listening for connections.

### Step 3: Create Local PPP User(s)

* **Purpose:** Define users in RouterOS with PPP access credentials.
* **CLI Example:**
    ```mikrotik
    /ppp secret
    add name=user1 password=password1 service=pppoe profile=default
    add name=user2 password=password2 service=pppoe profile=default
    ```
    *   **`/ppp secret add`:** Adds a new PPP user.
        *   `name=user1/user2`: Username for PPP authentication.
        *   `password=password1/password2`: Password for the PPP user.
        *   `service=pppoe`: Specifies this user is for PPPoE.
        *   `profile=default`:  Assigns the default profile, which handles the address pool assigned for the connecting PPP client (more on this later).
* **Winbox GUI:** Navigate to `PPP` -> `Secrets` and add users with the `+` button, selecting `PPPoE` as the `Service`.
* **Before:** No PPP users configured.
* **After:** `user1` and `user2` have been created and are ready for authentication.

### Step 4: (Optional) Configure Address Pool for PPP

* **Purpose:** Define IP ranges for PPP clients
* **CLI Example:**
    ```mikrotik
    /ip pool
    add name=ppp-pool ranges=190.173.141.100-190.173.141.200
    /ppp profile
    set default local-address=190.173.141.1 remote-address=ppp-pool
    ```
   * **`/ip pool add`:** Defines an IP pool that will be used to assign addresses to connecting PPP clients.
       * `name=ppp-pool`: Name for the IP pool.
       * `ranges=190.173.141.100-190.173.141.200`: IP range for dynamic allocation.
   * **`/ppp profile set default`:** Changes the default PPP Profile to allocate the created IP Pool
      * `local-address=190.173.141.1`: Configures the local IP for the PPPoE connection.
      * `remote-address=ppp-pool`: Configures the allocated address pool for each user connection.
* **Winbox GUI:** Navigate to `IP`->`Pools` and create an IP Pool by clicking on `+`. Then navigate to `PPP`->`Profiles` select the default profile and configure it accordingly.
* **Before:** The default profile IP pool settings have not been changed.
* **After:** The default profile will allocate addresses to PPP clients from the defined range.

## Complete Configuration Commands:

```mikrotik
/interface vlan
add name=vlan-75 vlan-id=75 interface=ether1 disabled=no
/ip address
add address=190.173.141.1/24 interface=vlan-75
/interface pppoe-server server
add service-name=pppoe-vlan-75 interface=vlan-75 max-mru=1480 max-mtu=1480 keepalive-timeout=10 authentication=pap,chap,mschap1,mschap2 one-session-per-host=yes
/ppp secret
add name=user1 password=password1 service=pppoe profile=default
add name=user2 password=password2 service=pppoe profile=default
/ip pool
add name=ppp-pool ranges=190.173.141.100-190.173.141.200
/ppp profile
set default local-address=190.173.141.1 remote-address=ppp-pool
```

## Common Pitfalls and Solutions:

1.  **Authentication Failures:**
    *   **Problem:** Users fail to connect with "invalid username/password."
    *   **Solution:**
        *   Double-check username/password in `/ppp secret`.
        *   Ensure the correct authentication method is enabled on the PPPoE server (e.g. PAP, CHAP, MSCHAP2).
        *   Make sure the client is configured correctly for the correct auth method.
2.  **IP Address Conflicts:**
    *   **Problem:** PPP clients get the same IP, or there is no connectivity.
    *   **Solution:**
        *   Check the defined IP pool range in `/ip pool`.
        *   Ensure there are no static IP address overlaps on `vlan-75`.
        *   Verify the `local-address` in `/ppp profile` is correct.
3.  **MTU/MRU Issues:**
    *   **Problem:** Slow speeds or connection drops.
    *   **Solution:**
        *   Make sure the `max-mru` and `max-mtu` settings on the server and client match. Generally, they should be set to 1480 for PPPoE.
4.  **Resource Issues:**
    *   **Problem:** High CPU or memory usage, especially with many concurrent connections.
    *   **Solution:**
        *   Monitor resource usage in `/system resource monitor`.
        *   Upgrade the RouterBOARD hardware if necessary.
        *   Adjust the `keepalive-timeout` to reduce unnecessary load.
        *   Disable unecessary logging to disk.
5.  **Security:**
    *   **Problem:** Vulnerability to brute force attacks on PPP.
    *   **Solution:**
        *   Use strong passwords and enforce password complexity for PPP users.
        *   Consider using Radius authentication for advanced security and centralized authentication.
        *   Limit the number of connection attempts per user within a certain time period.
        *   Use certificates for strong encryption (not within the scope of this specific example).

## Verification and Testing Steps:

1.  **Connect a Client:**
    *   Use a client device capable of PPPoE to connect to the router.
    *   Use `user1` or `user2` with the corresponding passwords from the configuration.
2.  **Check Active Connections:**
    *   Use the command `/ppp active print` to verify active connections.
    *   Check the Winbox `PPP`-> `Active Connections` window.
3.  **Ping Test:**
    *   From the connected client, `ping` the router interface (190.173.141.1).
    *   From the router, ping the client IP.
4.  **IP Address Assignment:**
    *   Ensure the client received an IP address from the defined pool range (`190.173.141.100-190.173.141.200`).
    *   Use `/ip address print` to check the assigned address of the PPP interface.
5. **Torch:**
    *   Use torch on `vlan-75` to check traffic flows: `/tool torch interface=vlan-75`

## Related Features and Considerations:

1.  **Radius Authentication:**  For larger deployments, Radius can be used as the backend for AAA. This provides central user management.
2.  **PPP Profile Customization:** PPP profiles can configure idle timeouts, bandwidth limits, and other settings.
3.  **VPN Integration:** PPP can be used to establish VPN tunnels, which can extend the network securely.
4.  **Firewall Rules:** Apply firewall rules to control traffic to/from the PPP clients.
5.  **Logging:** Enable logging for PPP connections for troubleshooting and auditing.
6. **Bandwidth Control:**
    *   Use `/queue tree` to create per user queues and limit up/down speed using the `ppp-out` interface.
7. **Accounting:**
    * Use `/system accounting` to see statistics on the active connections.

## MikroTik REST API Examples:

**Note:** Since MikroTik's API does not directly expose all PPP settings in a way that's conducive to detailed examples, these are limited to creation of users. You must enable the API in `/ip service`.

### Add a PPP Secret via API:

* **Endpoint:** `/ppp/secret`
* **Method:** `POST`
* **Request JSON Payload:**
    ```json
    {
        "name": "api_user",
        "password": "api_password",
        "service": "pppoe",
        "profile": "default"
    }
    ```
* **Expected Response (Success 200 OK):**
   ```json
   {
      "message": "added",
      "id": "*1"
   }
    ```
* **Explanation:**
    *   `name`: Username for the PPP secret.
    *   `password`: User's password.
    *   `service`:  The service the user is for (PPPoE).
    *   `profile`: The user's PPP profile.
* **Error Handling:** A 400 error code will indicate that the user could not be created (possible duplicate user).

### Example API Call (using curl):

```bash
curl -k -X POST -H "Content-Type: application/json" -u api_user:api_password  -d '{
    "name": "api_user",
    "password": "api_password",
    "service": "pppoe",
    "profile": "default"
}' https://<router_ip>/rest/ppp/secret
```

## Security Best Practices:

1.  **Strong Passwords:** Always use strong, unique passwords for PPP users.
2.  **Password Complexity:** Enforce password complexity rules in the user authentication process.
3.  **Disable Unnecessary Services:** Disable unnecessary services like SSH/Winbox from the WAN interface.
4.  **Firewall:** Implement a robust firewall to protect the PPP server from unauthorized access.
5.  **Radius:** Use RADIUS for larger deployments and centralized authentication for more security.
6.  **Keep RouterOS Updated:** Keep your router's RouterOS software updated to protect against vulnerabilities.
7.  **Logging:** Monitor logs and set up alerts for suspicious activity.
8.  **Rate Limiting:** Limit the number of connection attempts per user to mitigate brute force attacks.

## Self Critique and Improvements:

*   **Improvement:** This setup is basic and should be expanded with radius for better security and scalability.
*   **Improvement:** Bandwidth control needs to be set on the client interface in order to manage speeds.
*   **Improvement:** This config uses the "default" profile, which is generally discouraged. Custom profiles should be made.
*   **Improvement:** Consider the type of authentication (CHAP, MSCHAP, etc.) you actually need instead of enabling everything. It's best to limit them to improve security.
*   **Improvement:** This setup could be improved by adding firewall rules to protect the PPP server, preventing clients from connecting to each other, and logging all failed connections.

## Detailed Explanations of Topic:

*   **PPP (Point-to-Point Protocol):** A data link layer protocol used to establish direct connections between two network nodes. It commonly uses protocols like PAP, CHAP, or MSCHAP for authentication. It’s commonly used in VPNs and dial-up connections.
*   **AAA (Authentication, Authorization, and Accounting):** A framework for managing network access.
    *   **Authentication:** Verifies the user's identity before granting network access.
    *   **Authorization:** Specifies what resources a user is allowed to access.
    *   **Accounting:** Tracks network usage, like connection time and data transfer.

## Detailed Explanation of Trade-offs:

*   **Local vs Radius AAA:**
    *   **Local:** Easier to configure but not very scalable. Suitable for smaller SOHO networks.
    *   **Radius:** More complex, but scalable and secure. Suitable for SMB, Enterprise, and ISP scenarios.
*   **Authentication Methods (PAP, CHAP, MSCHAP):**
    *   **PAP:** Sends passwords in plaintext, not secure.
    *   **CHAP:** Uses hashes, more secure than PAP.
    *   **MSCHAPv2:**  Microsoft's proprietary version, with better security, common for Windows clients.
    *   **Tradeoff:** Security vs compatibility with different clients.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS versions 6.48 (6.x) and 7.x. Commands provided are generic to both, although it is always best to stay updated.

---

I hope this provides a thorough and practical guide to PPP AAA on MikroTik! Let me know if you have any further questions or specific scenarios to explore.
