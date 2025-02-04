Okay, let's dive into configuring PPP AAA (Authentication, Authorization, and Accounting) on MikroTik RouterOS v6.48 for a point-to-point link scenario, utilizing VLAN 16 on subnet 91.57.53.0/24. This configuration will focus on RADIUS authentication as it's the most common AAA method with PPP.

## Scenario Description:

We have a point-to-point link between two MikroTik routers, where one acts as a server and the other as a client. We want to establish a secure PPP connection over VLAN 16 (vlan-16).  To enhance security, instead of using simple passwords, we will authenticate PPP connections against a RADIUS server. This provides centralized user management and accounting features. We assume we already have VLAN interface vlan-16 configured on both routers.

## Implementation Steps:

Here, we will configure the server-side router to accept PPP connections and authenticate them via a RADIUS server. We'll focus on the server side configuration for brevity and clear steps, the client side is significantly simpler.

**Assumptions:**
1. VLAN 16 Interface `vlan-16` is already configured on both server and client-side routers with an IP address in 91.57.53.0/24. We will assume the server address is `91.57.53.1/24`.
2. A RADIUS server is available at `192.168.10.10` with a shared secret of `supersecret`.
3. The client will be configured with username 'clientuser' and password 'clientpassword', which exist within the RADIUS server.
4. We will not delve into the specifics of RADIUS server configuration; we will assume it is correctly set up.

**1. Step 1: Configure the PPP Interface (Server Side)**

*   **Before:** Initially, you will have an existing ethernet interface and a VLAN interface. No PPP interface configured yet.
*   **CLI Command:**
    ```mikrotik
    /interface ppp add name=ppp-server service=pptp disabled=no
    /interface ppp set ppp-server keepalive-timeout=30 max-mtu=1480 max-mru=1480
    /interface ppp profile add name=ppp-profile-radius local-address=91.57.53.1 remote-address=91.57.53.2 use-encryption=yes change-tcp-mss=yes
    /interface ppp secret add name=clientuser profile=ppp-profile-radius service=pptp
    /interface ppp set ppp-server user=clientuser
    ```
*   **Winbox:**
    *   Go to *Interface* -> *PPP* tab.
    *   Click the blue "+" and choose *PPTP Server*.
    *   Enter `ppp-server` as the name, ensure `enabled` is checked, and click `Apply`.
    *   Go to *PPP* -> *Profiles* tab and click the "+". Enter the profile name `ppp-profile-radius`. Set  `Local Address` as `91.57.53.1` and `Remote Address` as `91.57.53.2`. Check `Use Encryption` and `Change TCP MSS`.  Click `Apply`.
    *   Go to *PPP* -> *Secrets*. Add a new secret, username as `clientuser`, profile `ppp-profile-radius`, and service as `pptp`, and click Apply
    * Go back to Interface -> PPP and choose the ppp-server interface, then set the User option to `clientuser` click Apply.
*   **Explanation:**
    *   `/interface ppp add`: Creates a PPP interface for PPTP service.
    *   `name=ppp-server`: Specifies the name of the interface as 'ppp-server'.
    *   `service=pptp`: Indicates this interface is for PPTP.
    *   `disabled=no`: Enables the interface.
    *   `/interface ppp set ppp-server ...`: Configure Keepalive and MTU/MRU settings.
    *    `keepalive-timeout`: how often the server will send an echo request to verify the connection.
    *   `max-mtu` `max-mru`: Maximum transfer unit and maximum receive unit.
    *   `/interface ppp profile add ...`: Creates a PPP profile for authentication and IP addressing.
    *    `name=ppp-profile-radius`: Specifies the name of the profile.
    *    `local-address=91.57.53.1`: The IP address assigned to the server.
    *    `remote-address=91.57.53.2`: The IP address assigned to the client.
    *   `use-encryption=yes`: Enables encryption for the PPP connection.
    *   `change-tcp-mss=yes`: Forces changes in the tcp mss value to be adjusted to the new MTU.
    *   `/interface ppp secret add ...`: Add a user and assign it to a profile.
    *    `name=clientuser`: The user to allow a PPP connection.
    *    `profile=ppp-profile-radius`: The ppp profile to be used for this user.
    *  `service=pptp`: Restricts this secret to be used with pptp connections only
    *   `/interface ppp set ppp-server user=clientuser` Restricts the pptp server to be used with the user clientuser

*   **After:** You'll have the new `ppp-server` interface listed in the interface list and a profile called `ppp-profile-radius`, and a secret for the user `clientuser` within the PPP menu.

**2. Step 2: Configure RADIUS Client**

*   **Before:** No RADIUS client is configured.
*   **CLI Command:**
    ```mikrotik
    /radius add address=192.168.10.10 secret=supersecret service=ppp timeout=30
    ```
*   **Winbox:**
    *   Go to *RADIUS* menu.
    *   Click the blue "+".
    *   Enter the IP address `192.168.10.10`
    *   Enter the `secret` as `supersecret`.
    *   Select `ppp` as the `service`
    *   Set `timeout` to 30
    *   Click `Apply`.
*   **Explanation:**
    *   `/radius add ...`: Adds a new RADIUS client configuration.
    *   `address=192.168.10.10`: IP address of the RADIUS server.
    *   `secret=supersecret`: Shared secret configured on the RADIUS server.
    *   `service=ppp`: Specifies that this RADIUS client is for PPP authentication.
    *   `timeout=30`: The RADIUS server timeout in seconds.
*   **After:** You'll have a RADIUS client entry with the configured server address and secret.

**3. Step 3: Enable RADIUS Authentication on PPP (Server Side)**
    
*  **Before:** The PPP server will authenticate with local secrets
*  **CLI Command:**
    ```mikrotik
   /interface ppp set ppp-server use-radius=yes
    ```
*  **Winbox:**
    * Go to `Interface -> PPP` menu.
    * Select the `ppp-server` interface, click on it.
    * Check the `Use Radius` box
    * Click `Apply`.
* **Explanation:**
  * `use-radius=yes`: Enables RADIUS server use for authentication.
*  **After:** The `ppp-server` interface will now try to authenticate using RADIUS

**4. Step 4: Configure Client side**

* **Before**: No PPP client interface
* **CLI Command**:
    ```mikrotik
    /interface pptp-client add connect-to=91.57.53.1 name=pptp-client1 user=clientuser password=clientpassword profile=ppp-profile-radius disabled=no
    ```
* **Winbox**
    *  Go to `Interface -> PPP` menu
    *  Click on the `+` and choose `PPTP Client`
    *  Name it `pptp-client1`
    *  Set `connect-to` to `91.57.53.1`
    *  Set `user` to `clientuser`
    *  Set `password` to `clientpassword`
    *  Set `profile` to `ppp-profile-radius`
    *  Uncheck `disabled` and click `Apply`
* **Explanation:**
    * `/interface pptp-client add`: Creates a new pptp client interface
    * `connect-to=91.57.53.1`: Specifies the ip address of the server
    * `name=pptp-client1`: The name of the client interface
    * `user=clientuser`: The username to use when connecting to the server
    * `password=clientpassword`: The password to use when connecting to the server
    * `profile=ppp-profile-radius`: The ppp profile
    * `disabled=no`: Enables the client
* **After:** A `pptp-client1` interface will be present in the `Interface -> PPP` menu and should try to connect to the server

## Complete Configuration Commands:

Here's a consolidated set of CLI commands for the server side configuration:

```mikrotik
/interface ppp
add name=ppp-server service=pptp disabled=no
set ppp-server keepalive-timeout=30 max-mtu=1480 max-mru=1480 user=clientuser use-radius=yes
/interface ppp profile
add name=ppp-profile-radius local-address=91.57.53.1 remote-address=91.57.53.2 use-encryption=yes change-tcp-mss=yes
/interface ppp secret
add name=clientuser profile=ppp-profile-radius service=pptp
/radius
add address=192.168.10.10 secret=supersecret service=ppp timeout=30
```

And here are the commands for the client:

```mikrotik
/interface pptp-client
add connect-to=91.57.53.1 name=pptp-client1 user=clientuser password=clientpassword profile=ppp-profile-radius disabled=no
```

## Common Pitfalls and Solutions:

1.  **RADIUS Server Unreachable:**
    *   **Problem:** The router cannot reach the RADIUS server.
    *   **Solution:** Verify network connectivity to the RADIUS server using `/ping 192.168.10.10` . Check firewall rules. Ensure RADIUS server is operational.
2.  **Incorrect RADIUS Secret:**
    *   **Problem:** The secret on the router does not match the RADIUS server's secret.
    *   **Solution:** Double-check the `secret` in `/radius print` and on the RADIUS server.
3.  **Incorrect Username/Password on RADIUS:**
    *   **Problem:** The credentials provided by the client doesn't match the RADIUS server.
    *   **Solution:** Verify user credentials on the RADIUS server.
4.  **Incorrect IP Addresses:**
    * **Problem:** The local and remote addresses on the ppp profiles don't match.
    * **Solution:** Double-check the addresses are set correctly on both server and client.
5.  **Firewall Blocking PPP:**
    *   **Problem:** Firewalls may be interfering with the PPTP connections.
    *   **Solution:** Add rules to allow PPTP traffic through the firewall. This might involve allowing GRE protocol. Example: ` /ip firewall filter add chain=input protocol=gre action=accept`.
6.  **MTU/MRU Issues:**
    *   **Problem:** Large packets may be fragmented.
    *   **Solution:** Adjust MTU and MRU on the `ppp-server` interface and profile. Match them on both sides. `max-mtu=1480 max-mru=1480` should be fine for general use.
7. **Resource Usage:**
    * **Problem:** High CPU usage if many users are connected.
    * **Solution:** Monitor CPU usage with `/system resource print`. Consider using less resource-intensive authentication methods like simpler passwords if you run into this.

## Verification and Testing Steps:

1.  **Check PPP Interface Status:**
    *   Use: `/interface ppp print`
    *   Verify that the `ppp-server` interface is enabled.
    *   Verify that the `pptp-client1` on the client side is also enabled and is connected.
2.  **Check RADIUS status:**
    *   Use: `/radius print`
    *   Verify that the status of the RADIUS server is `working`
    *   Check the last fail time, if the RADIUS is failing to authenticate the requests.
3.  **Monitor PPP Logs:**
    *   Use: `/log print topic=ppp`
    *   Check for authentication messages, errors, and connection status. Useful to pinpoint issues.
4.  **Ping the Remote Address:**
    *   After the client connects, ping the assigned remote IP `91.57.53.2` from the server `ping 91.57.53.2` and ping the server `91.57.53.1` from the client `ping 91.57.53.1`
5.  **Torch Utility:**
    * Use `/tool torch interface=vlan-16` on the client and the server to ensure that the packages are traveling correctly over the specified VLAN.

## Related Features and Considerations:

1.  **IP Pools:**  You can configure IP address pools on the server side so that you don't have to set a specific IP address on the profiles. Use `/ip pool add` and `/interface ppp profile set ... local-address=pool-name`.
2.  **Accounting:**  RADIUS accounting can be enabled for usage tracking, though it's beyond the scope of this basic configuration.
3.  **VPN:**  Consider replacing PPTP with a more secure VPN protocol like L2TP/IPsec if security is a key concern, but this is more complex.
4.  **Hotspot:** You can also use RADIUS AAA for hotspot configurations for user authentication on guest networks.
5.  **Multiple Radius Servers:** You can configure multiple radius servers to have failover capabilities. Use `/radius add address=... secondary-secret=...`

## MikroTik REST API Examples (if applicable):
*Note: RouterOS API is enabled in /ip service, we are going to assume it's enabled for the following examples.*

Here are some examples of MikroTik REST API calls:

1.  **Add a RADIUS Client:**

    *   **Endpoint:** `/radius`
    *   **Method:** `POST`
    *   **JSON Payload:**
        ```json
        {
            "address": "192.168.10.10",
            "secret": "supersecret",
            "service": "ppp",
            "timeout": "30"
        }
        ```
    *   **Expected Response (200 OK):**
        ```json
        {
            ".id": "*0",
            "address": "192.168.10.10",
            "secret": "supersecret",
            "service": "ppp",
            "timeout": "30"
        }
        ```
2.  **Enable RADIUS Authentication on PPP Interface:**

    *   **Endpoint:** `/interface/ppp/ppp-server`
    *   **Method:** `PUT`
    *   **JSON Payload:**
        ```json
        {
            ".id": "*0",
            "use-radius": "yes"
        }
        ```
       *Note: The `.id` will change, use the specific `.id` of the server.*
    *   **Expected Response (200 OK):**
        ```json
        {
          ".id": "*0",
          "name": "ppp-server",
          "service": "pptp",
          "disabled": "false",
          "keepalive-timeout": "30",
          "max-mtu": "1480",
          "max-mru": "1480",
          "user": "clientuser",
          "use-radius": "yes"
        }
        ```

    **Error Handling (Example):** If there's an error with any API request, the response will have an error status, for example, a `400` or `500` status code with an error message in JSON format. For example a bad request when trying to set the id might return:
    ```json
    {
      "message": "invalid id",
      "code": 400
    }
    ```

## Security Best Practices

1.  **Strong RADIUS Secret:** Use a long, complex, and unique shared secret for RADIUS authentication.
2.  **Firewall Rules:**  Strictly control access to the RADIUS server and the router's interfaces using firewall rules. Allow access to the RADIUS service only from authorized IPs.
3.  **Encryption:** Always enable encryption on the PPP link `use-encryption=yes`.
4. **Use a more secure method**: PPTP should be avoided, consider using L2TP or Wireguard, those use more secure protocols.
5.  **Regularly Update RouterOS:** Keep RouterOS updated to patch vulnerabilities.
6.  **Limit PPP Access:** Limit the number of allowed clients using interface firewall filter or by adding a limited amount of users.
7.  **Monitor Logs:** Regularly review logs for suspicious activity.

## Self Critique and Improvements

This basic configuration provides a starting point, but here are some improvements:

*   **More Robust Security:** Switch to L2TP/IPsec or Wireguard for more secure VPN. PPTP is considered insecure.
*   **IP Pools:**  Use dynamic IP pools instead of static remote addresses.
*   **Accounting:** Implement RADIUS accounting for tracking user activity.
*   **User Profiles:** Use different PPP profiles and RADIUS attributes for different types of users.
*   **Logging:** Configure more robust logging for better tracking and auditing.
*   **API Improvements**: The api commands can be improved by using API calls to obtain the id of the ppp server rather than hardcoding it.
*   **Automation:** This is a good start for automation. A complete setup can be easily done with tools like Ansible or Python and the API.

## Detailed Explanations of Topic

**PPP (Point-to-Point Protocol):** PPP is a data link layer communication protocol used to establish a direct connection between two nodes. It supports authentication, encryption, and IP address negotiation.

**AAA (Authentication, Authorization, and Accounting):**
    *   **Authentication:** Verifies the user's identity (e.g., username/password).
    *   **Authorization:** Determines what a user is allowed to do after authentication (e.g., network access).
    *   **Accounting:** Tracks a user's resource consumption (e.g., session duration, data usage).

**RADIUS (Remote Authentication Dial-In User Service):** A networking protocol that provides centralized authentication, authorization, and accounting for users who connect to a network.

## Detailed Explanation of Trade-offs

*   **PPTP vs L2TP/IPsec or Wireguard:** PPTP is easier to set up but is insecure. L2TP/IPsec and Wireguard are more secure but require more complex configurations. Use L2TP/IPsec or Wireguard for anything other than test setups.
*   **Static IP vs IP Pool:** Static IPs are easier to manage in simple scenarios but don't scale. IP pools allow dynamic allocation and better management in larger networks.
*   **Local Secrets vs RADIUS:** Local secrets are simpler to configure for small setups, but RADIUS provides centralized user management, auditing, and more robust security.
*   **Performance:** Encrypted VPNs have an overhead cost. Make sure to check your hardware resources to make sure the encryption isn't overloading your device.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS 6.48 as requested. Commands are generally forward and backward compatible with 7.x, however, there may be differences in some parameters in newer versions. Always consult the RouterOS manual when upgrading to newer versions. There may be new commands or parameters specific to that version. This configuration should be used as a baseline and adjusted as needed.

Let me know if you'd like any clarification or modifications to this setup!
