Okay, let's dive into configuring PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik RouterOS v7.12 (also considering 6.48 and 7.x compatibility) router for a SOHO network, focusing on the specific subnet 237.223.252.0/24 and interface wlan-83. This will be an expert-level configuration, so we'll delve into the details.

## Scenario Description:

We're setting up a scenario where PPP connections (e.g., PPPoE, PPTP, L2TP) initiated on the `wlan-83` interface require authentication, authorization, and (optionally) accounting. We will utilize a RADIUS server to handle the authentication, and potentially authorization and accounting. This setup is typical for providing controlled network access for wireless clients using an access point on `wlan-83`.

## Implementation Steps:

Here's a step-by-step guide to configure PPP AAA using a RADIUS server:

**1. Step 1: Pre-Configuration Status.**
   - Before we begin, let's check if a PPP server already exists and the state of our `wlan-83` interface.

      *   **CLI Command:**
            ```mikrotik
            /interface/print
            /ppp/server/print
            ```
      *   **Expected Output (Example):**
            ```
            /interface/print
             Flags: D - dynamic, X - disabled, R - running, S - slave
             #    NAME                                TYPE        MTU L2MTU
             0  R  ether1                            ether     1500  1598
             1  R  wlan1                             wlan      1500  1598
             2  R  wlan-83                           wlan      1500  1598
             ...
            /ppp/server/print
             Flags: X - disabled
            ```
     *   **Explanation:** The `/interface/print` command shows all the interfaces and their status.  We see `wlan-83`. The `/ppp/server/print` command shows that no PPP servers are configured.
     *   **Action:** Note down your interfaces.

**2. Step 2: Adding a RADIUS Server Configuration.**
   - We'll define the RADIUS server details. Replace the placeholders with your actual server information.
   *   **CLI Command:**
            ```mikrotik
            /radius add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=3 authentication-port=1812 accounting-port=1813
            ```
     *   **Winbox GUI**: Go to `RADIUS` in the left menu, click the `+` button and fill the needed information.
     *   **Explanation:**
         * `address`: The IP address of your RADIUS server (e.g. 192.168.88.10).
         * `secret`: The shared secret key configured on your RADIUS server. **This must match the configuration on the RADIUS server exactly.**
         * `service`:  Indicates that this RADIUS server will be used for PPP service authentication.
         * `timeout`: How long the MikroTik will wait for a response from the RADIUS server (default is 3 seconds).
         * `authentication-port`: UDP port for authentication (default 1812).
         * `accounting-port`: UDP port for accounting (default 1813).
   *   **Expected Output:** No output will be returned, if the command is successful the new entry will be available on `/radius/print`.
   *   **Action:** Verify with ` /radius print` that the entry was properly created.

**3. Step 3: Enabling and Configuring a PPP Server (e.g., PPPoE).**
    - Let's configure a PPPoE server. Since we have specified the `wlan-83` interface, clients should only connect through this interface.
   *   **CLI Command:**
            ```mikrotik
            /ppp/server/pppoe add service-name=my-pppoe-service interface=wlan-83 max-mtu=1480 max-mru=1480 keepalive-timeout=60 use-encryption=required default-profile=default disabled=no
            ```
       *   **Winbox GUI**: Go to `PPP` > `PPP Server` > `PPPoE Server`, click the `+` button and fill the needed information.
   *   **Explanation:**
        *   `service-name`:  A unique name for the PPPoE service (e.g., "my-pppoe-service").
        *   `interface`: The interface on which to listen for PPPoE connections (`wlan-83`).
        *  `max-mtu`: Maximum Transmission Unit.
        * `max-mru`: Maximum Receive Unit.
         *   `keepalive-timeout`: Interval (in seconds) to check for connection activity.
         *  `use-encryption`: `required` means all connections must be encrypted with MPPE.
        *   `default-profile`: The default profile for new PPP connections (we will assume 'default').
        *   `disabled`: Set to `no` to enable the server.
    *   **Expected Output:** No output will be returned, if the command is successful the new entry will be available on `/ppp/server/pppoe/print`.
    *   **Action:** Verify with `/ppp/server/pppoe/print` that the entry was properly created.

**4. Step 4:  Enabling RADIUS for PPP.**
   - Configure the router to use the RADIUS server for PPP authentication. This step may already be set by default.
    * **CLI Command**
          ```mikrotik
          /ppp/authentication set use-radius=yes
          ```
    * **Winbox GUI**: Go to `PPP` > `Secrets` > `Authentication` and click the `Use Radius` box.
    * **Explanation:** The command enables RADIUS based authentication for all PPP protocols.
    * **Expected Output:** No output will be returned, if the command is successful the changes will be available on `/ppp/authentication/print`.
    * **Action:** Verify with `/ppp/authentication/print` that the entry was updated.

**5. Step 5: Setting up a default PPP profile (if you need to override the default).**
     - A default profile for PPP users should be set to apply configurations to PPP clients. In this scenario, we will leave the default.
     *   **CLI Command:**
          ```mikrotik
         /ppp/profile print
         ```
     *   **Winbox GUI**: Go to `PPP` > `Profiles`
    * **Expected output**:
        ```
        /ppp/profile print
         Flags: * - default
         0  * name="default" local-address=0.0.0.0 remote-address=0.0.0.0 use-compression=default
         use-encryption=default only-one=no change-tcp-mss=yes address-list=""
        ```
    * **Explanation:** By default, there is a profile called "default" with a basic configuration. We will not modify it, but if the default was not sufficient, we can create a new one.
    * **Action:** If needed create a new profile using the `add` command.

## Complete Configuration Commands:

```mikrotik
/interface/print
/ppp/server/print
/radius add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=3 authentication-port=1812 accounting-port=1813
/ppp/server/pppoe add service-name=my-pppoe-service interface=wlan-83 max-mtu=1480 max-mru=1480 keepalive-timeout=60 use-encryption=required default-profile=default disabled=no
/ppp/authentication set use-radius=yes
/ppp/profile print
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Not Reachable:**
    *   **Problem:** Router cannot reach the RADIUS server due to network connectivity issues or incorrect IP address.
    *   **Solution:** Verify network connectivity using ping: `/ping 192.168.88.10`. Ensure firewall rules on the MikroTik (if any) are not blocking traffic to the RADIUS server on ports 1812/1813. Check the logs (`/log print`) for RADIUS-related errors.
*   **Incorrect RADIUS Secret:**
    *   **Problem:** Secret on the MikroTik does not match the RADIUS server secret.
    *   **Solution:** Double-check the secret on both the MikroTik and the RADIUS server. They must match *exactly*, including case sensitivity. It is advisable to recreate the secret.
*   **Authentication Failures:**
    *   **Problem:** Clients cannot authenticate with the provided username and password.
    *   **Solution:** Check the RADIUS server logs for specific errors. Ensure the username and password are correct and are configured within the RADIUS server. Make sure that the PAP or CHAP configurations are properly set.
*   **Incorrect PPP MTU/MRU values:**
    *   **Problem:** Clients may have trouble connecting due to the PPP overhead causing fragmentation on the link.
    *   **Solution:** Adjust the `max-mtu` and `max-mru` to accommodate the overhead. Common values are 1480, but sometimes it might be required to lower it.
*   **No Encryption:**
    *   **Problem:** Connection is not encrypted.
    *   **Solution:** Double check that `use-encryption=required` in your PPPoE server configuration.
*   **Resource Issues:**
    *   **Problem:** High CPU usage due to many concurrent PPP sessions or extensive accounting.
    *   **Solution:** Monitor CPU using `/system resource monitor`. Consider enabling connection limits per interface, or optimizing accounting settings.
*   **Security Issues:**
    *   **Problem:** RADIUS secret is insecure, weak passwords, etc.
    *   **Solution:** Keep the radius secret secure and use strong passwords on the RADIUS server. Consider using VLANs to isolate the PPP client connections.

## Verification and Testing Steps:

1.  **Check RADIUS reachability:** `/ping 192.168.88.10`
2.  **Check PPP Server status:** `/ppp/server/pppoe/print` and ensure the server is enabled and listening on the `wlan-83` interface.
3.  **Client Connection:**
    *   Connect a client device to the `wlan-83` interface (using the SSID it is configured to broadcast), and attempt to connect to the PPPoE server using the appropriate client.
    *   Verify that the client is assigned an IP address from the RADIUS server or the configured IP pool, if RADIUS does not assign addresses.
    *   Use `/interface/ppp/active/print` to check active PPP connections.
    *   Use `/log print` to check MikroTik logs for any errors during connection.
4.  **RADIUS Logs:** Review RADIUS server logs for successful authentications and failures. These logs should tell you the details of the connection and any potential reasons for failure.
5.  **Testing Tools:**
     *   Use `/tool/torch interface=wlan-83` to monitor traffic on the interface.
     *   Use `/tool/profile` to monitor CPU usage.

## Related Features and Considerations:

*   **Hotspot:** Consider using the MikroTik Hotspot feature instead of PPPoE for simpler user authentication. But if your network is based on RADIUS, PPPoE is a good choice.
*   **IP Pools:**  If the RADIUS server does not assign IP addresses, configure IP pools to provide addresses for the PPP clients (`/ip/pool`).
*   **Firewall Rules:** Implement firewall rules to control the traffic flow of the PPP clients based on their assigned IP addresses.
*   **Accounting:** Use RADIUS accounting to track usage, bandwidth, or connection time. If you need specific limitations, it is good to utilize the Mikrotik RADIUS attributes as well as the Mikrotik PPP profiles features for more fine grained control.
*   **VPN:**  Consider implementing L2TP/IPsec or other VPN tunnels for more secure remote access.
*   **VLANs:**  Utilize VLANs to isolate client connections.

## MikroTik REST API Examples (if applicable):

This feature is supported via the `/ppp` endpoint, which has sub-endpoints like `/ppp/server/pppoe`, `/ppp/authentication`, and `/radius`. However, you won't be able to create full configurations using only API.

Here's a basic example for creating a RADIUS server entry.

```json
    # POST Request
    Endpoint: /rest/radius
    Method: POST
    Payload:
    {
    	"address": "192.168.88.10",
    	"secret": "your_radius_secret",
    	"service": "ppp",
    	"timeout": 3,
    	"authentication-port": 1812,
    	"accounting-port": 1813
    }
    # Expected response (201 Created):
    {
       "id": "*1"
    }
    # Error Example (400 bad request):
    {
        "message":"invalid value for argument secret"
    }

    # Getting all RADIUS servers:
    Endpoint: /rest/radius
    Method: GET

    # Expected response (200 OK):
    [
    	{
    		"id": "*1",
    		"address": "192.168.88.10",
    		"secret": "your_radius_secret",
    		"service": "ppp",
    		"timeout": "3",
    		"authentication-port": "1812",
    		"accounting-port": "1813",
    		"disabled": "false"
    	}
    ]
```
*   `id`: RouterOS ID
*   `address`: RADIUS server IP Address
*   `secret`: Secret shared between the router and the radius server
*   `service`: Defines the use case (`ppp` in our case)
*   `timeout`: The timeout value
*   `authentication-port`: UDP port for authentication
*   `accounting-port`: UDP port for accounting
*   `disabled`: Boolean value

Error Handling:  For API errors, check the returned HTTP status code and the JSON error message.

## Security Best Practices

*   **RADIUS Secret:** Use a strong, unique secret that is not easily guessed.
*   **Firewall:** Limit access to the RADIUS ports (1812/1813) only from the MikroTik router.
*   **User Passwords:** Enforce strong password policies in your RADIUS server.
*   **Encryption:** Always use encryption on PPP connections (`use-encryption=required` for PPPoE).
*   **Regular Updates:** Keep your MikroTik RouterOS and RADIUS server software updated with the latest security patches.

## Self Critique and Improvements

This setup provides a robust foundation for PPP AAA. However, several improvements are possible:

*   **Profile Customization**: Create specific PPP profiles for different user groups with different bandwidth limits, IP pools, etc.
*   **Advanced Accounting**: Implement more detailed RADIUS accounting, such as session duration, traffic usage.
*   **IP Address Management:** Implement dynamic IP address assignment through RADIUS attributes.
*   **Multi-Factor Authentication**: Add multi-factor authentication for increased security.
*   **Centralized Configuration:** Use RouterOS's scripting or configuration management tools for more complex deployments.

## Detailed Explanations of Topic

*   **PPP (Point-to-Point Protocol):** A data link layer protocol used to establish a direct connection between two network nodes. It supports various authentication mechanisms, and is commonly used in PPPoE, PPTP and L2TP.
*   **AAA (Authentication, Authorization, and Accounting):**
    *   **Authentication:** Verifies the user's identity (e.g., using a username and password).
    *   **Authorization:** Determines what network resources the user is allowed to access.
    *   **Accounting:** Tracks resource usage (e.g., time, data) by the user.
*   **RADIUS (Remote Authentication Dial-In User Service):** A networking protocol that provides centralized Authentication, Authorization, and Accounting management for users attempting to connect to a network.
*   **MikroTik RouterOS PPP Implementation:**  The RouterOS PPP implementation is flexible and supports various PPP authentication methods. The integration with the RADIUS server gives a very centralized approach to managing user access.

## Detailed Explanation of Trade-offs

*   **Internal Authentication vs. RADIUS:**
    *   **Internal Authentication:** Simpler to set up but lacks flexibility. Configuration is stored locally on the router and doesn't scale well for large networks.
    *   **RADIUS Authentication:** Provides centralized user management and access control. It’s more complex but offers better scalability, security, and features like accounting.
*  **MPPE Encryption vs No Encryption:**
    *   **MPPE Encryption:** Secure data transmission but slightly more CPU intensive and can introduce overhead.
    *   **No Encryption:** Faster processing, but lacks data protection, which is not advised.
*  **PPPoE vs Hotspot:**
    *   **PPPoE:** Generally used for more direct connections, requires a client configuration on the end device, more flexible for controlling access.
    *   **Hotspot:** User friendly web interface for logging in, often used for public access, less control over per-client settings.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeted for RouterOS 7.12. While most of the commands are also available on 6.48 and 7.x, some subtle differences may exist. For example, syntax for encryption might vary slightly. Always refer to the official MikroTik documentation for specific version-related details. For very old versions it is not advised to use this configuration, because they are no longer supported.
