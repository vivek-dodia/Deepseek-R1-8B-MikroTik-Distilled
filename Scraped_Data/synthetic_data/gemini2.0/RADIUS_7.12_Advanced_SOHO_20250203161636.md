Okay, let's dive into a comprehensive documentation for implementing RADIUS authentication on a MikroTik router, targeting RouterOS 7.12, within a SOHO network, using a VLAN interface `vlan-30` and the subnet `121.250.68.0/24`.

## Scenario Description:

This scenario involves configuring a MikroTik router to use a RADIUS server for authentication of users connecting to the `vlan-30` interface, which will have the subnet `121.250.68.0/24`. This approach is commonly used for managing access control to a network segment, enabling centralized authentication and authorization, often in conjunction with technologies like Hotspot or VPN.

## Implementation Steps:

Here's a step-by-step guide to set up RADIUS authentication for your MikroTik on interface `vlan-30`:

1.  **Step 1: Create VLAN Interface `vlan-30`**

    *   **Explanation:** First, we need to create the VLAN interface on which the RADIUS authentication will be applied. It's assumed that a physical interface (e.g., `ether1`) is configured with the appropriate VLAN tag. We are using VLAN ID `30`.

    *   **Before:** No VLAN interface `vlan-30`.
    *   **CLI Command:**
        ```mikrotik
        /interface vlan
        add interface=ether1 name=vlan-30 vlan-id=30
        ```
    *   **Winbox GUI:**
        Navigate to `Interfaces -> VLAN` tab. Click `+` button. Enter `vlan-30` for name, select `ether1` for `Interface`, enter `30` for `VLAN ID`.
    *   **After:** VLAN interface `vlan-30` exists, but without an IP address.

2.  **Step 2: Assign IP Address to `vlan-30`**

    *   **Explanation:** Assign a static IP address from the 121.250.68.0/24 range to the newly created `vlan-30` interface. This will be the gateway for clients on this VLAN.

    *   **Before:** `vlan-30` interface has no IP address.
    *   **CLI Command:**
        ```mikrotik
        /ip address
        add address=121.250.68.1/24 interface=vlan-30
        ```
    *   **Winbox GUI:**
        Navigate to `IP -> Addresses`. Click `+` button. Enter `121.250.68.1/24` for address, and select `vlan-30` for `Interface`.
    *   **After:** `vlan-30` interface has IP address `121.250.68.1/24`.

3.  **Step 3: Configure RADIUS Server Settings**

    *   **Explanation:** Now we need to configure the MikroTik router to communicate with the RADIUS server. This includes defining the server's IP address, shared secret, and other related settings.
    *   **Before:** No RADIUS server configuration exists.
    *   **CLI Command (Example):**
        ```mikrotik
        /radius
        add address=192.168.10.10 secret=radius_secret service=ppp timeout=30
        ```
        *  `address`:  IP address of the RADIUS server (`192.168.10.10` in the example).
        *  `secret`: The shared secret key that is shared between the MikroTik router and RADIUS server (`radius_secret` in the example). Ensure this matches the RADIUS server settings.
        *  `service`: The service that will use this RADIUS server, here we're using `ppp` as an example which covers most use cases (PPP, PPPoE, Hotspot, VPN etc.). If needed, can add service types such as: hotspot, login.
        *  `timeout`: Timeout value for the RADIUS server to respond, in seconds (30 seconds in this example).
    *   **Winbox GUI:**
        Navigate to `RADIUS`. Click `+` button and enter the settings as stated in the CLI example.
    *   **After:** RADIUS server entry is configured in the `/radius` configuration.

4.  **Step 4: Configure PPP Profile for RADIUS Authentication**

    *   **Explanation:** A PPP profile is needed to enable RADIUS authentication. This profile will be referenced when a user tries to connect. We will configure the authentication to use our newly configured RADIUS server.
    *   **Before:** No relevant PPP profile exists for RADIUS authentication.
    *   **CLI Command:**
        ```mikrotik
        /ppp profile
        add name=radius-profile use-encryption=yes only-one=yes address-list=radius-users local-address=121.250.68.1 remote-address=radius-pool \
         dns-server=8.8.8.8,8.8.4.4 change-tcp-mss=yes
        /ppp profile set radius-profile use-radius=yes
        /ip pool add name=radius-pool ranges=121.250.68.2-121.250.68.254
        ```
        *  `name`: The name of the profile - `radius-profile`.
        *  `use-encryption`: Encrypt user authentication data with CHAP for better security.
        *  `only-one`: Only one connection allowed per username.
        *  `address-list`: Add IP to this address list to be used for user firewall rules `radius-users`
        *  `local-address`: Address that is assigned to this profile for client/router side.
        *  `remote-address`: Pool from which IP's will be assigned to clients.
        *  `dns-server`: Set DNS for clients connecting with this profile.
        *  `change-tcp-mss`: Helps resolve some MSS issues.
        *  `use-radius`: Enable RADIUS authentication on this profile.
        *  `/ip pool add`: Add the pool `radius-pool` to draw IP's from.
    *   **Winbox GUI:**
         Navigate to `PPP -> Profiles` Click the `+` button, enter the `name` and all the values as per the CLI, then select the "Use Radius" option at the bottom.
         Navigate to `IP -> Pool` then click the `+` button and add a new IP pool as per the CLI `radius-pool`.
    *   **After:** A new PPP profile `radius-profile` exists, configured to use RADIUS for authentication.

5. **Step 5: Apply PPP Profile to Interface (PPPoE Server Example)**

    * **Explanation:** To actually use RADIUS authentication, we need a method to authenticate the users. A common one is PPPoE. For other methods, please modify the commands accordingly (Hotspot, VPN etc.).  We will create a PPPoE server on the `vlan-30` interface and configure it to use the RADIUS profile we've just created.
    * **Before:** No PPPoE server configured.
    * **CLI Command:**
        ```mikrotik
        /interface pppoe-server server
        add service-name=pppoe-radius interface=vlan-30 max-mru=1492 max-mtu=1492 keepalive-timeout=30 default-profile=radius-profile
        ```
        *  `service-name`: PPPoE service name, `pppoe-radius` in the example.
        *  `interface`: Interface on which the PPPoE server is running, `vlan-30` here.
        *  `max-mru`: Maximum Receive Unit.
        *  `max-mtu`: Maximum Transmission Unit.
        *  `keepalive-timeout`: Time for connection keepalive, important to use to keep tunnels active.
        *  `default-profile`: The default PPP profile to use for authentication, which should be `radius-profile`.
    *   **Winbox GUI:**
       Navigate to `PPP -> PPPoE Servers`, Click the `+` button. Enable the server, select the interface and enter the remaining values as per the CLI example.
    *   **After:** PPPoE server configured and listening on `vlan-30`, clients connecting will be authenticated via RADIUS.

6. **Step 6: Optional: Configure Firewall Rules for RADIUS Users**

    * **Explanation:** It's often necessary to create specific firewall rules for users authenticated through RADIUS. We can target the address list `radius-users` in the previous step.
    * **Before:** No specific firewall rules for RADIUS authenticated users.
    * **CLI Command (Example):**
        ```mikrotik
        /ip firewall filter
        add chain=forward action=accept src-address-list=radius-users
        add chain=forward action=drop
        ```
        * This example allows any forward traffic from the `radius-users` address list and drops all others.
    * **Winbox GUI:**
        Navigate to `IP -> Firewall -> Filter Rules`. Add a new filter rule, set the chain to `forward`, action to `accept`, then in the `src. address list` select the `radius-users`. Add a second rule with chain to `forward` and the action to `drop`.
    * **After:** Firewall rules are in place for RADIUS users.

## Complete Configuration Commands:

Here's the complete set of CLI commands to implement this setup:

```mikrotik
/interface vlan
add interface=ether1 name=vlan-30 vlan-id=30
/ip address
add address=121.250.68.1/24 interface=vlan-30
/radius
add address=192.168.10.10 secret=radius_secret service=ppp timeout=30
/ppp profile
add name=radius-profile use-encryption=yes only-one=yes address-list=radius-users local-address=121.250.68.1 remote-address=radius-pool \
 dns-server=8.8.8.8,8.8.4.4 change-tcp-mss=yes
/ppp profile set radius-profile use-radius=yes
/ip pool add name=radius-pool ranges=121.250.68.2-121.250.68.254
/interface pppoe-server server
add service-name=pppoe-radius interface=vlan-30 max-mru=1492 max-mtu=1492 keepalive-timeout=30 default-profile=radius-profile
/ip firewall filter
add chain=forward action=accept src-address-list=radius-users
add chain=forward action=drop
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Connectivity Issues:**
    *   **Problem:**  The MikroTik router cannot reach the RADIUS server.
    *   **Solution:** Check the network connectivity between the MikroTik router and the RADIUS server using `ping` from MikroTik CLI (e.g. `/ping 192.168.10.10`). Verify that there are no intermediate firewalls blocking traffic on port 1812 (default RADIUS authentication port).
*   **Incorrect Shared Secret:**
    *   **Problem:** Authentication fails because the shared secret does not match between the MikroTik and the RADIUS server.
    *   **Solution:** Double-check the secret configured in the MikroTik (`/radius print`) and on the RADIUS server. Make sure they are identical.
*   **RADIUS Attributes not correctly configured:**
    *   **Problem:** RADIUS server is sending incorrect attributes.
    *   **Solution:**  Monitor the RADIUS logs on the server to ensure the response from the server is correct. Also check any debugging or log options in MikroTik (e.g `/system logging add topics=radius`).
*   **Firewall Blocking RADIUS traffic:**
    *   **Problem:**  MikroTik's firewall is blocking RADIUS communication.
    *   **Solution:** Verify firewall rules to ensure that UDP traffic to the RADIUS server port (1812 or 1813) is allowed from the MikroTik router.
* **Resource Issues**:
    * **Problem:** High CPU or Memory when a lot of users are authenticating.
    * **Solution:** MikroTik devices, especially low-end ones can have issues with higher number of RADIUS authentications. Upgrading to higher end devices can help, also reducing timeout to a minimum, can also reduce the resource load.
*   **Incorrect PPP Profile Settings:**
    *   **Problem:**  The PPP profile is not configured to use RADIUS or is not configured correctly.
    *   **Solution:** Verify that the `use-radius` parameter is set to `yes` in the PPP profile settings (`/ppp profile print`).

## Verification and Testing Steps:

1.  **Check RADIUS Configuration:**
    ```mikrotik
    /radius print
    ```
    Verify that the RADIUS server is configured correctly with the correct IP, secret, and service.
2.  **Check PPP Profile:**
    ```mikrotik
    /ppp profile print
    ```
    Verify that the RADIUS profile exists and has `use-radius` set to `yes`.
3.  **Check PPPoE Server Status:**
    ```mikrotik
    /interface pppoe-server server print
    ```
    Verify that the PPPoE server is enabled on the correct interface and using the RADIUS profile.
4.  **Attempt Authentication:**
    *   Use a client computer to connect to the PPPoE server with a valid username and password (defined on the RADIUS server).
    *   If the connection is successful, the user should receive an IP address in the `121.250.68.0/24` subnet.
5.  **Check Logs:**
    *   Use `/log print where topics~"radius"` to monitor RADIUS messages on the MikroTik router.
    *   Examine the RADIUS server logs for successful authentication or error messages.
6. **Check Active Connections:**
   * Verify the active connections with `/ppp active print` command.

## Related Features and Considerations:

*   **Hotspot:**  The RADIUS authentication can be extended to the MikroTik hotspot feature.
*   **VPN (L2TP/IPSec, PPTP):** RADIUS can be used to authenticate VPN users.
*   **Dynamic Address Lists:**  MikroTik can use dynamic address lists populated by RADIUS to create specific firewall rules based on users.
*   **Accounting:** RADIUS accounting can be used to track user activity and data usage, and can be used in conjunction with other features for billing and reports.
*   **NAS Identifier:** Set `nas-identifier` for identification of the router on the RADIUS server.
*  **Caller ID / Calling-station-id**: Add the client's MAC address for additional identification.

## MikroTik REST API Examples:

Here are some examples of using the MikroTik REST API for configuring the RADIUS server (assuming you have the MikroTik API enabled and configured):

1.  **Add RADIUS Server:**

    *   **Endpoint:** `/radius`
    *   **Method:** `POST`
    *   **Payload (JSON):**
        ```json
        {
            "address": "192.168.10.10",
            "secret": "radius_secret",
            "service": "ppp",
            "timeout": "30"
        }
        ```
    *   **Expected Response (201 Created):**
        ```json
        {
            ".id": "*1"
            "address": "192.168.10.10",
            "secret": "radius_secret",
            "service": "ppp",
            "timeout": "30"
           "comment": ""
        }
        ```
    *   **Error Handling:** If there are issues like incorrect parameters or duplicate entries, the API will respond with HTTP error codes such as `400 Bad Request` or `409 Conflict`.
        ```json
        {
            "message": "radius with address=192.168.10.10 already exists",
            "error": true
        }
        ```

2.  **Get All RADIUS Servers:**

    *   **Endpoint:** `/radius`
    *   **Method:** `GET`
    *   **Payload:** None
    *   **Expected Response (200 OK):**
        ```json
        [
            {
            ".id": "*1"
            "address": "192.168.10.10",
            "secret": "radius_secret",
            "service": "ppp",
            "timeout": "30"
           "comment": ""
            }
        ]
        ```

3.  **Update a RADIUS Server:**

    *   **Endpoint:** `/radius/*1`
    *   **Method:** `PUT`
    *   **Payload (JSON):**
        ```json
        {
            "timeout": "60"
        }
        ```
    *   **Expected Response (200 OK):**
       ```json
       {
            ".id": "*1"
            "address": "192.168.10.10",
            "secret": "radius_secret",
            "service": "ppp",
            "timeout": "60"
           "comment": ""
       }
       ```

4. **Delete a RADIUS Server**
    *   **Endpoint:** `/radius/*1`
    *   **Method:** `DELETE`
    *   **Payload:** None
    *   **Expected Response (204 No Content):**
        No content returned

## Security Best Practices

*   **Use Strong Shared Secret:** Use a strong, complex, randomly generated shared secret between the MikroTik router and the RADIUS server.
*   **Secure RADIUS Server:** Ensure the RADIUS server is properly secured and updated to prevent unauthorized access.
*   **Encrypt Communication:** Consider using RADIUS over TLS (RadSec) for added security for sensitive data communication.
*   **Principle of Least Privilege:** Give the user the bare minimum required to get online.
*   **Firewall:** Implement strict firewall rules to limit access to the MikroTik router, and protect your network.
*   **Address List Management:**  Use address list for all firewall rules to better manage, track and administer the rules.
*  **Regular Updates**: Keep the MikroTik router's RouterOS up-to-date with the latest security patches and updates.

## Self Critique and Improvements

This is a good implementation of RADIUS for a SOHO environment on MikroTik. However, here are some areas for potential improvements:

*   **Logging**: Better logging needs to be implemented.
*   **RadSec:** Consider using RadSec to encrypt the communication between the MikroTik router and the RADIUS server.
*   **More Specific Firewall Rules:** The current firewall rules are very basic; they could be extended to provide granular access control.
*   **Monitoring:** Implement monitoring of RADIUS authentication attempts (both successful and failed).
*   **NAS Identifier**: Add the NAS identifier to help identify the router on the RADIUS server.
*   **Caller-ID:** Add the caller-id to help identify the user on the RADIUS server.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users who connect to a network. This protocol enables network administrators to manage user access and track network usage from a single point of control. RADIUS works on the client-server model, where a network device (like a router) acts as a client and communicates with a central RADIUS server.

Key aspects of RADIUS:

*   **Authentication:** Verifies a user's identity.
*   **Authorization:**  Grants or denies access to specific network resources based on the user's identity and profile.
*   **Accounting:** Tracks the resources used by the user (session time, data usage etc).
*   **Centralized Management:**  Allows network administrators to manage user access and track network usage from a single point of control.
*   **Flexible Access Control:** Allows for the implementation of a wide range of access policies based on user roles or network resources.
*   **Scalability:** Supports large numbers of users and network devices.

## Detailed Explanation of Trade-offs

*   **RADIUS vs. Local Authentication:**
    *   **Local Authentication:** Simpler for small networks but doesn't scale well. Changes need to be made on every router.
    *   **RADIUS Authentication:** More complex to set up but provides centralized user management, scalability, and better security.
*   **PAP (Password Authentication Protocol) vs. CHAP (Challenge Handshake Authentication Protocol):**
    *   **PAP:** Transmits the password in plain text. Not recommended.
    *   **CHAP:** Provides better security by encrypting passwords during authentication. More complex.
*   **UDP vs. TCP:**
    *   **UDP:** Default for RADIUS, faster but unreliable.
    *   **TCP (RadSec):** Slower but more reliable with TLS encryption.
*   **Specific Service vs `ppp`:**
    *   **Specific Service:** (e.g. hotspot) More specific to that service, and less likely to accidentally allow users to other service types.
    *   **`ppp` service type:** Easier to configure and usually covers most use cases, but might be less granular.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeted for RouterOS 7.12, but it is also applicable to RouterOS 6.48. The core features and commands used here are consistent across these versions. However, if specific features or parameters are not present in older versions, the commands should be adjusted accordingly.  Always consult the RouterOS documentation for specific versions to confirm the availability of certain parameters, and use the correct commands if needed.

This detailed documentation should enable you to implement RADIUS authentication effectively in your SOHO environment using MikroTik RouterOS. Let me know if you have any other questions or need further clarification!
