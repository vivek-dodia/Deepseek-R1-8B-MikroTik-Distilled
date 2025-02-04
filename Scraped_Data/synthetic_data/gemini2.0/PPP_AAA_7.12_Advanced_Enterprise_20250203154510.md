Okay, let's dive into a detailed exploration of PPP AAA (Authentication, Authorization, and Accounting) on MikroTik RouterOS 7.12, specifically within an enterprise environment and utilizing the 237.86.193.0/24 subnet on the interface "ether-82".  We'll provide practical examples, configurations, troubleshooting, and best practices. This is an advanced topic, so a good understanding of MikroTik basics is assumed.

## Scenario Description:

We are setting up a PPP (Point-to-Point Protocol) server on a MikroTik router. This server will authenticate clients using a RADIUS server for AAA, allowing remote access to the 237.86.193.0/24 subnet via PPP connections over interface "ether-82". The PPP connections will be used for secure remote access, and potentially as a VPN solution, giving users access to the network behind the MikroTik router. RADIUS is used to centralize user authentication, access, and accounting.

## Implementation Steps:

Here's a step-by-step guide with CLI and Winbox instructions, before and after each step, and the intended effect:

**1. Step 1: Configure the PPP Interface:**

   *   **Goal:** Enable and configure the PPP interface for our server. We will start by configuring a basic PPP profile and a PPP server.
   *   **Before:** There are no PPP profiles configured (except for a default) nor are there any PPP server configurations.
    *   **CLI:**

        ```mikrotik
        /ppp profile
        print
        ```
        (Output will only show default profile, we'll add a profile called "radius-ppp")
        ```mikrotik
        /ppp server
        print
        ```
        (Output will be empty)

   *   **CLI Commands:**

        ```mikrotik
        /ppp profile add name=radius-ppp use-encryption=yes local-address=237.86.193.1 remote-address=237.86.193.2-237.86.193.254
        /ppp server add name=ppp-server interface=ether-82 profile=radius-ppp enabled=yes
        ```
   *   **Winbox GUI:**
        1.  Navigate to PPP -> Profiles. Add a profile named "radius-ppp", enable encryption, set a local and a remote address.
        2.  Navigate to PPP -> Servers. Add a server named "ppp-server", select interface "ether-82", set the profile to "radius-ppp" and enable it.
   *   **After:**
    *   **CLI:**
       ```mikrotik
           /ppp profile print
           /ppp server print
       ```
       (Output should now show our added profile "radius-ppp" and server "ppp-server" )
   *   **Effect:** The `radius-ppp` profile is created to handle the PPP parameters. We've enabled a PPP server named `ppp-server` on interface `ether-82` using the created profile. Users who authenticate with this server will get an address from within the 237.86.193.0/24 range.

**2. Step 2: Configure RADIUS Settings:**

   *   **Goal:** Configure the MikroTik router to communicate with your RADIUS server for authentication, authorization, and accounting.
   *   **Before:** The router has no RADIUS client configured
        * **CLI:**
            ```mikrotik
            /radius
            print
            ```
            (Output will be empty)
   *   **CLI Commands:**
        ```mikrotik
        /radius add address=192.168.100.100 secret=mysecret service=ppp timeout=30
        ```
        **Replace** 192.168.100.100 with the actual IP address of your RADIUS server and `mysecret` with your shared secret.
   *   **Winbox GUI:**
        1.  Navigate to Radius. Add a new Radius server, setting address, secret and service to ppp.
   *   **After:**
        * **CLI:**
            ```mikrotik
            /radius
            print
            ```
            (Output should now show the radius configuration)
   *   **Effect:** We configured our router to connect to the given RADIUS server, we configured `ppp` to use the configured RADIUS server, and set up a timeout.

**3. Step 3: Configure PPP to use RADIUS for AAA:**
  *   **Goal:** Enable the usage of our defined RADIUS server on the PPP profile.
    *   **Before:** Our PPP profile does not yet use the RADIUS server.
        * **CLI:**
            ```mikrotik
            /ppp profile print detail
            ```
            (Output should show `use-radius=no`)
    *   **CLI Commands:**
      ```mikrotik
       /ppp profile set radius-ppp use-radius=yes
      ```
    *   **Winbox GUI:**
        1.  Navigate to PPP -> Profiles. Select "radius-ppp" profile.
        2.  Check the box 'Use Radius'
    *   **After:**
        * **CLI:**
            ```mikrotik
            /ppp profile print detail
            ```
            (Output should now show `use-radius=yes`)
    *   **Effect:** The `radius-ppp` profile now uses the configured RADIUS server for authentication, authorization, and accounting when a user connects to the PPP server.

**4. Step 4: (Optional) Enable Accounting:**
    *   **Goal:** Set up RADIUS accounting for the PPP server, enabling tracking of connection duration, and bandwidth consumption.
    *  **Before:** Accounting is not enabled on the PPP profile
        * **CLI:**
            ```mikrotik
            /ppp profile print detail
            ```
            (Output should show `only-one=yes` or `no`)
     * **CLI Commands:**
          ```mikrotik
          /ppp profile set radius-ppp accounting=yes only-one=no
          ```
     * **Winbox GUI:**
        1.  Navigate to PPP -> Profiles. Select "radius-ppp" profile.
        2.  Check the box 'Accounting' and 'one session per user'.
    *   **After:**
         * **CLI:**
            ```mikrotik
            /ppp profile print detail
            ```
             (Output should show `accounting=yes`)
    *   **Effect:**  We configured the radius profile to include accounting for the connection sessions. This will enable tracking of bandwidth and connection times for the ppp connections.

## Complete Configuration Commands:

```mikrotik
# Step 1: Configure PPP Interface
/ppp profile add name=radius-ppp use-encryption=yes local-address=237.86.193.1 remote-address=237.86.193.2-237.86.193.254
/ppp server add name=ppp-server interface=ether-82 profile=radius-ppp enabled=yes

# Step 2: Configure RADIUS Settings
/radius add address=192.168.100.100 secret=mysecret service=ppp timeout=30

# Step 3: Configure PPP to use RADIUS for AAA
/ppp profile set radius-ppp use-radius=yes

# Step 4: (Optional) Enable Accounting
/ppp profile set radius-ppp accounting=yes only-one=no
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Verify the RADIUS server IP address is correct.
        *   Check network connectivity using ping or traceroute from the MikroTik.
        *   Verify that the firewall on your Mikrotik or the RADIUS server are not blocking communication on UDP ports 1812 and 1813 (or 1645, 1646 for older RADIUS servers).
*   **Shared Secret Mismatch:**
    *   **Problem:** The shared secret configured on the MikroTik does not match the RADIUS server.
    *   **Solution:** Ensure that the configured secret is identical on both the MikroTik and RADIUS server.
*   **Authentication Failures:**
    *   **Problem:** Users are unable to authenticate.
    *   **Solution:**
        *   Verify that the user exists in the RADIUS server.
        *   Check if the RADIUS server logs any error messages related to the user’s authentication.
        *   Enable RADIUS debugging on the MikroTik for detailed error messages (`/system logging add topics=radius action=memory prefix="RADIUS:"`)
*   **IP Address Conflicts:**
    *   **Problem:** IP Address conflicts due to dynamic allocation.
    *   **Solution:** Ensure that there are no overlapping address ranges with existing dhcp or other ppp servers. Adjust local and remote ip range of ppp profile to prevent conflicts.
*   **No Accounting Data:**
    *   **Problem:** The RADIUS server does not receive accounting data.
    *   **Solution:** Ensure accounting is enabled on both the MikroTik PPP profile and on the RADIUS server. Review RADIUS server logs for errors.
*   **Performance:**
    *   **Problem:** High CPU or memory usage due to many active PPP connections.
    *   **Solution:**
        *   Upgrade the MikroTik hardware.
        *   Limit the number of concurrent connections.
        *   Optimize the configuration by removing uneeded features and logging.
*   **Security:**
    *   **Problem:** Weak encryption settings can be a security risk, especially in public networks.
    *   **Solution:** Force encryption for all connections by setting the `use-encryption` parameter on the ppp profile. This could be `yes`, `mppe`, or `require` depending on the type of encryption you require. Use strong shared secrets for RADIUS.

## Verification and Testing Steps:

1.  **PPP Connection:**
    *   Attempt to connect to the PPP server from a remote client.
    *   Verify the client receives an IP address within the configured range (237.86.193.2 - 237.86.193.254).
2.  **Authentication:**
    *   On successful connection, verify that the RADIUS server logs the authentication event with a successful status.
    *   On failed connection, check the logs on the RADIUS server.
3.  **Accounting (If Enabled):**
    *   On disconnection, verify that the RADIUS server records the connection session information (start time, stop time, bandwidth usage).
4.  **MikroTik Logs:**
    *   Use MikroTik's logging to identify the status of each authentication.
        ```mikrotik
        /log print where topics~"radius"
        ```
5.  **Ping and Traceroute:**
    *   Once connected, from the remote client, use `ping` to check connectivity to other devices on the 237.86.193.0/24 subnet.
        * Use `traceroute` to verify the network path.
6.  **Torch (MikroTik Tool):**
    *   Use the `torch` tool on `ether-82` to monitor traffic on the interface and analyze the communication with the RADIUS server.
        ```mikrotik
        /tool torch interface=ether-82
        ```

## Related Features and Considerations:

*   **Firewall Rules:** You need to configure firewall rules on the MikroTik to allow traffic between the PPP clients and other parts of your network, and to ensure that traffic is going through the ppp tunnels.
*   **Virtual Routing and Forwarding (VRF):** For more complex setups, VRF can be used to isolate traffic from different PPP clients.
*   **Bandwidth Limiting:** Use MikroTik queues to control the bandwidth consumed by the PPP connections.
*   **User Profiles:** Use RADIUS attributes to configure custom settings for individual users or groups of users.
*   **VPN (L2TP/IPsec, PPTP):** PPP can be combined with other VPN technologies for enhanced security and functionality, such as L2TP, or even IPSec
*   **MikroTik's Hotspot:** PPP can be integrated with a hotspot feature for controlled access.
*   **Real World Impact:** A properly configured PPP server with AAA provides a secure method to allow users secure remote access to your private network, enabling employees to securely work from home or on the road. Additionally, this can be used to provide access to remote resources without having to expose them to the internet.

## MikroTik REST API Examples (if applicable):

While MikroTik's REST API might not directly handle all PPP operations with the same granularity as the CLI, we can use it to automate some of the configurations.  Here are example calls that might be used:

**1. Create a PPP Profile:**

*   **Endpoint:** `/ppp/profiles`
*   **Method:** `POST`
*   **Payload (JSON):**
    ```json
    {
        "name": "radius-ppp",
        "use-encryption": "yes",
        "local-address": "237.86.193.1",
        "remote-address": "237.86.193.2-237.86.193.254"
    }
    ```
*   **Expected Response (201 Created):** A JSON object containing the newly created profile's details.
*   **Error Handling:**
    *   A 400 (Bad Request) might be returned if the payload has an invalid parameter
    *   A 500 (Internal Server Error) could indicate a configuration or system error

**2. Create a PPP Server:**

*   **Endpoint:** `/ppp/servers`
*   **Method:** `POST`
*   **Payload (JSON):**
    ```json
    {
        "name": "ppp-server",
        "interface": "ether-82",
        "profile": "radius-ppp",
        "enabled": "yes"
    }
    ```
*   **Expected Response:** A JSON object containing the newly created server's details.

**3. Enable RADIUS on a PPP Profile:**

*   **Endpoint:** `/ppp/profiles/radius-ppp`
*   **Method:** `PATCH`
*   **Payload (JSON):**
    ```json
    {
        "use-radius": "yes"
    }
    ```
*   **Expected Response:** A JSON object reflecting the updated profile's details.

**4. Enable Accounting on a PPP Profile:**

*   **Endpoint:** `/ppp/profiles/radius-ppp`
*   **Method:** `PATCH`
*   **Payload (JSON):**
    ```json
    {
       "accounting": "yes",
       "only-one":"no"
    }
    ```
*   **Expected Response:** A JSON object reflecting the updated profile's details.

**5. Create a Radius Server Configuration:**

*   **Endpoint:** `/radius`
*   **Method:** `POST`
*    **Payload (JSON):**
    ```json
    {
       "address": "192.168.100.100",
       "secret": "mysecret",
       "service": "ppp",
       "timeout": "30"
    }
    ```
*   **Expected Response:** A JSON object reflecting the created Radius client settings

**Note:** To perform these API calls, you need to:
* Have your Mikrotik device configured to listen to api calls, by enabling `api` or `api-ssl` under `/ip service`.
* Ensure you have proper credentials for authentication via the header of the API call.
* Ensure you have your device accessible via a network, and have the capability to send HTTP requests to it.

## Security Best Practices:

*   **Use Strong RADIUS Shared Secret:**  Make sure the shared secret between the MikroTik and the RADIUS server is long, complex and difficult to guess.
*   **Force Encryption:** Enable and force encryption on the PPP profile to prevent eavesdropping on the connection (as included in the example) by setting the `use-encryption` property.
*   **Secure RADIUS Communication:** Encrypt communication between the MikroTik and the RADIUS server by enabling RADIUS over TLS (RadSec). This can be done by adding a certificate to the radius configuration, and by configuring TLS on your RADIUS server.
*   **Implement Strong User Passwords:** Ensure the passwords of your PPP users are strong.
*   **Regularly Review Access:** Review active users on the ppp server and also on the radius server, and disable any uneeded users.
*   **Monitor Logs:** Set up adequate logging to monitor for any abnormal activity and to ensure proper functionality.
*   **Update RouterOS:** Keep your RouterOS and any associated packages up-to-date to patch any security holes.

## Self Critique and Improvements:

This configuration provides a solid foundation for a secure PPP server with RADIUS AAA, suitable for enterprise use.

Here's what could be improved or further modified:

*   **More Granular Access Control:** RADIUS vendor specific attributes (VSA) can be used to enforce stricter policies on each user.
*   **Enhanced VPN Security:** While PPP is a standard, consider transitioning to more robust and modern VPN options such as WireGuard or L2TP/IPsec.
*   **Dynamic QoS:** Implement dynamic QoS based on RADIUS attributes to prioritize traffic for certain users.
*   **Failover Redundancy:** Multiple RADIUS servers can be added for failover, but only if you can assure there is synchronization between the databases.

## Detailed Explanations of Topic

**AAA (Authentication, Authorization, and Accounting):**
    *   **Authentication:** Verifying the user's identity. In our scenario, the PPP server sends user credentials to the RADIUS server, which checks the provided username and password against its user database.
    *   **Authorization:** Deciding whether a user can use a specific service or resource after they have been authenticated. In the context of PPP, this can mean if the user is allowed to connect to the server, as well as attributes such as maximum session time, or bandwidth control.
    *   **Accounting:** Logging the usage of resources by users, used for tracking time spent on the network, bandwidth usage and data consumption. This is useful for billing purposes, and to audit user activity.

**PPP (Point-to-Point Protocol):**
    *   A layer 2 data link protocol used to establish direct connections between two nodes.
    *   It is commonly used to establish dial-up internet connections, and also for creating virtual point to point links over an ethernet network.
    *   PPP is commonly used for VPN implementations (PPTP, L2TP).

**RADIUS (Remote Authentication Dial-In User Service):**
    *   A network protocol for centralized Authentication, Authorization, and Accounting (AAA) of users connecting to network services.
    *   It is a widely used standard, supported by many network devices and operating systems.
    *   RADIUS servers are scalable, and can support large user databases.

## Detailed Explanation of Trade-offs

*   **Local User Authentication vs. RADIUS Authentication:**
    *   **Local:** Simpler to set up for smaller environments with few users. It is not scalable, and each device will have to be configured manually.
    *   **RADIUS:** More complex to set up initially, but it is much more scalable, and offers centralized user management, as well as advanced policies and user management.

*   **PPTP vs. L2TP/IPsec vs. WireGuard:**
    *   **PPTP:** Easy to setup, but is considered insecure. Not recommended for environments with security concerns.
    *   **L2TP/IPsec:** Provides a more secure connection compared to PPTP, but has higher overhead due to the usage of two protocols.
    *   **WireGuard:** The newest of the 3 VPN protocols, and provides a good balance between security and performance, also offers cross-platform support, and has a simplified configuration method.

*   **Dynamic IP vs. Static IP:**
    *   **Dynamic:** Simplifies IP management, reducing the chance of address conflicts and is recommended for PPP users.
    *   **Static:** Guarantees the same IP for a specific user, which can be necessary in certain implementations, but increases the complexity of configuration.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 7.12 but will mostly work on RouterOS 7.x.  It might require slight adjustments in earlier versions (7.0-7.11):

*   Older versions might lack the same specific options for accounting or encryption in the PPP profile. Ensure to consult the RouterOS documentation for your specific version.
*   Make sure to verify that the RADIUS package is installed and running, older versions may require to have this package explicitly installed.
*   The `/system logging add topics=radius action=memory prefix="RADIUS:"` command may behave differently in older versions. If it fails to log, verify that the syntax for logging is correct for your version.

This detailed explanation provides a comprehensive approach for setting up PPP AAA on MikroTik RouterOS using RADIUS with specific subnet and interface information. Remember to adjust the configuration to your environment.
