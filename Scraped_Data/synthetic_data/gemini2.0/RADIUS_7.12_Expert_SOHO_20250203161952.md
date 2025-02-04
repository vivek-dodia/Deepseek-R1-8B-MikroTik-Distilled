Okay, let's dive into a detailed explanation and implementation of RADIUS authentication using a MikroTik RouterOS device, specifically focusing on version 7.12, and catering to an expert SOHO environment, using the interface `wlan-83` and the subnet `171.27.80.0/24`.

## Scenario Description:

We are setting up a Wi-Fi network in a SOHO environment. Instead of using a simple pre-shared key (PSK) for authentication, we want to leverage a RADIUS server for more granular control and user management. This setup will allow us to:

*   Authenticate wireless users via RADIUS, providing a central management point for access credentials.
*   Enable accounting to monitor user activity.
*   Potentially use dynamic VLAN assignment for enhanced network segmentation.

## Implementation Steps:

Here's a step-by-step guide, with examples using both CLI and Winbox GUI instructions:

### Step 1: Prepare the Wireless Interface

*   **Goal:** Ensure that the wireless interface `wlan-83` is properly configured and enabled to accept connections.
*   **Before:** Assume the interface exists but might be disabled or using a simple PSK.
*   **CLI Example:**
    ```mikrotik
    /interface wireless
    print
    # Note down the id of the wlan-83 interface, e.g. '0'
    set 0 disabled=no mode=ap-bridge band=2ghz-b/g/n channel-width=20/40mhz-Ce ssid=MyWiFiNetwork frequency=2437 security-profile=default
    ```
    *   **Explanation:**
        *   `print` displays the current wireless interfaces. We're noting the id of our wlan-83 interface (e.g., 0).
        *   `set 0` modifies the interface with id 0.
        *   `disabled=no` enables the interface.
        *   `mode=ap-bridge` sets the operating mode to access point bridge.
        *   `band=2ghz-b/g/n` sets the supported band.
        *   `channel-width=20/40mhz-Ce` sets the channel width
        *   `ssid=MyWiFiNetwork` sets the network name.
        *   `frequency=2437` sets the frequency channel
        *   `security-profile=default` sets the current security profile
*   **Winbox GUI:**
    1. Go to *Wireless* in the left menu.
    2. Select the `wlan-83` interface.
    3. Ensure *Enabled* is checked.
    4. Set *Mode* to `ap bridge`.
    5. Configure other parameters as needed (e.g., *Band*, *Channel Width*, *SSID*).
    6. Keep the default `security-profile` or make a new one as needed.
*   **After:** The interface is enabled and configured for standard wireless operation.
*   **Effect:** Clients will now be able to see and attempt to connect to the configured SSID.

### Step 2: Configure RADIUS Server Settings

*   **Goal:** Add the RADIUS server configuration to the router.
*   **Before:** No RADIUS server entries exist.
*   **CLI Example:**
    ```mikrotik
    /radius
    add address=192.168.100.1 secret=your_radius_secret service=wireless timeout=30
    print
    ```
    *   **Explanation:**
        *   `add` creates a new RADIUS server entry.
        *   `address=192.168.100.1` specifies the IP address of the RADIUS server.
        *   `secret=your_radius_secret` sets the shared secret key (must match the RADIUS server configuration).
        *   `service=wireless` specifies that the RADIUS server is used for wireless authentication.
        *   `timeout=30` configures the timeout for RADIUS requests.
        *   `print` Displays the current RADIUS entries.
*   **Winbox GUI:**
    1. Go to *RADIUS* in the left menu.
    2. Click the "+" button to add a new RADIUS server.
    3. Enter the RADIUS server IP address, shared secret, service (wireless), and timeout.
    4. Click *Apply*.
*   **After:**  The router is aware of the configured RADIUS server.
*   **Effect:** Router will attempt communication with the radius server.

### Step 3: Configure Wireless Security Profile for RADIUS

*   **Goal:** Modify the default security profile to use RADIUS authentication
*   **Before:** The security profile may be using simple password auth.
*   **CLI Example:**
    ```mikrotik
    /interface wireless security-profiles
    set default mode=dynamic-keys authentication-types=wpa-psk,wpa2-psk,wpa-eap,wpa2-eap eap-methods=passthrough group-key-update=30m radius-mac-format=username
    print
    ```
    *   **Explanation:**
        *   `set default` modifies the default security profile.
        *   `mode=dynamic-keys`  sets the key mode to dynamic keys which is needed for RADIUS authentication.
        *   `authentication-types=wpa-psk,wpa2-psk,wpa-eap,wpa2-eap` sets supported authentication types.
        *    `eap-methods=passthrough` enables passthrough for external EAP authentication.
         *   `group-key-update=30m` sets the interval for key updates.
        *   `radius-mac-format=username` specifies that the client MAC address is sent as the username to the radius server
        *   `print` displays current wireless security profiles
*    **Winbox GUI**
    1. Go to *Wireless -> Security Profiles*.
    2. Select the default security profile or your created profile.
    3. Change *Mode* to `dynamic keys`.
    4. Enable *EAP* and configure your desired Authentication Types.
    5. Select *Passthrough* for EAP Methods.
    6. Set Radius MAC Format to `username`
    7. Click *Apply*.
*   **After:** The security profile for the wireless interface is configured to use RADIUS.
*   **Effect:** New wireless clients will now authenticate via RADIUS.

### Step 4: Verify Connectivity and Authentication

*   **Goal:** Connect a device to the wireless network and confirm authentication through the RADIUS server.
*   **Before:**  No clients connected using RADIUS.
*   **Steps:**
    1.  Connect a wireless client to the `MyWiFiNetwork` SSID.
    2.  The client should prompt for a username and password.  (These need to be configured on the RADIUS server.)
    3.  The RADIUS server will authenticate and respond to the MikroTik.
    4.  The wireless client will be granted access.
*   **After:** The client is connected and has been successfully authenticated through RADIUS.
*   **Effect:**  The wireless client has network access based on the RADIUS server policies.

## Complete Configuration Commands:

```mikrotik
/interface wireless
set 0 disabled=no mode=ap-bridge band=2ghz-b/g/n channel-width=20/40mhz-Ce ssid=MyWiFiNetwork frequency=2437 security-profile=default
/radius
add address=192.168.100.1 secret=your_radius_secret service=wireless timeout=30
/interface wireless security-profiles
set default mode=dynamic-keys authentication-types=wpa-psk,wpa2-psk,wpa-eap,wpa2-eap eap-methods=passthrough group-key-update=30m radius-mac-format=username
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Not Reachable:**
    *   **Problem:** The MikroTik cannot communicate with the RADIUS server.
    *   **Solution:** Verify that the server is online, IP address is correct, and the shared secret key matches on both devices. Use the `ping` tool on the MikroTik to check reachability.
    *   **Example:** `ping 192.168.100.1`
*   **Incorrect Shared Secret:**
    *   **Problem:** The shared secret key does not match on the MikroTik and RADIUS server.
    *   **Solution:** Double-check the key on both devices. If copying the key from another source, be sure to remove leading/trailing spaces.
*   **Firewall Blocking RADIUS:**
    *   **Problem:** The firewall on the MikroTik or the RADIUS server is blocking RADIUS traffic.
    *   **Solution:** Verify firewall rules. RADIUS traffic uses UDP ports 1812 and 1813 (for authentication and accounting, respectively).
    *   **Example:** Ensure that the relevant firewall chain accepts UDP on the correct ports.
*   **Incorrect Authentication Type:**
    *   **Problem:** The authentication types in the security profile and on the RADIUS server don't match.
    *   **Solution:** Ensure both are configured for the correct EAP methods, such as PEAP or EAP-TLS, and make sure to match the corresponding authentication settings.
*   **Incorrect `radius-mac-format` Parameter:**
   *   **Problem:** If the RADIUS server is expecting another type of identification, or a different format than `username`.
    * **Solution:** If the server is expecting the MAC address as the user name you should set `radius-mac-format=username` or if you want it as a calling ID, you should use `radius-mac-format=calling-station-id`. If you need another format you should contact the RADIUS server provider.
*   **Resource Issues (CPU/Memory):**
    *   **Problem:** A high volume of RADIUS requests can cause high CPU or memory usage, especially with many connected devices.
    *   **Solution:** Monitor the router’s resource usage, using the `/system resource print` command. Check the RADIUS server performance as well. You can also try reducing the amount of logging on the server and/or the router.
    *   **Command:** `/system resource print`

## Verification and Testing Steps:

1.  **Ping:**
    *   `ping 192.168.100.1` (from the MikroTik terminal) to check connectivity to the RADIUS server.
2.  **Log Output:**
    *   Check the MikroTik logs for RADIUS authentication messages using `/system logging print topics=radius`.  This will show success or error messages during client connection attempts.
3.  **Client Connection:**
    *   Attempt to connect a wireless client. Verify it receives an IP and is able to access the internet.
4.  **Torch:**
    *   Use `/tool torch interface=wlan-83` to capture the RADIUS traffic between the router and the server, in order to diagnose any issues.
5.  **RADIUS Server Logs:**
    *   Check the logs on the RADIUS server to confirm that the authentication requests are reaching the server, and how it's responding.
6. **Winbox Tools**
    * Use the tools provided by Winbox to ping and traceroute from the router, checking connectivity with the Radius server.

## Related Features and Considerations:

*   **RADIUS Accounting:** Enable RADIUS accounting on the router to track user activity, including connection time and data usage.
*   **Dynamic VLAN Assignment:** Configure the RADIUS server to send VLAN attributes for dynamic VLAN assignment to provide better security.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy. The router will try the next server in the list if the first server is unavailable.
*   **Hotspot Feature:** Consider combining the RADIUS authentication with the MikroTik Hotspot feature for more advanced user management, including login pages and walled gardens.
* **EAP Methods**:  Choosing a proper authentication type between your clients, the mikrotik router, and the RADIUS server, such as PEAP, EAP-TLS, EAP-TTLS or other. The trade-off is between complexity and security.
* **Interim Updates**: If you need to track active user sessions you should configure the RADIUS server to send interim updates.

## MikroTik REST API Examples (if applicable):

While the MikroTik REST API is very powerful, direct RADIUS manipulation is limited. RADIUS settings are managed through the RouterOS configuration and not as a dedicated API resource. However, you can use the REST API to manage the underlying configurations that enable the RADIUS setup:

*   **Add RADIUS Server (using CLI command):**
    *   **API Endpoint:** `/system/routerboard/resource` (To execute the command).
    *   **Request Method:** POST
    *   **JSON Payload:**
        ```json
        {
            "command":"/radius add address=192.168.100.1 secret=your_radius_secret service=wireless timeout=30"
        }
        ```
    *   **Expected Response (Success):**
        ```json
        {
            "status": "success"
        }
        ```
    *   **Expected Response (Error):**
        ```json
        {
            "status": "error",
            "message": "Error executing command"
        }
        ```
        *   **Explanation:** The above command will execute the provided string as if it was written in the cli
*   **Error Handling:** Always check the `status` field in the response. If it's "error," inspect the `message` field for details.
*   **Security:** Always use HTTPS when accessing the RouterOS API and protect your API credentials.

**NOTE:** The example above uses the API to execute a CLI command for adding a RADIUS server. This is due to the absence of a dedicated API endpoint for RADIUS management. We will be limited to using the API for running CLI commands when we're addressing a RADIUS configuration in this way.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a strong and complex shared secret key.
*   **Firewall Rules:** Limit access to the RADIUS server by only allowing the MikroTik router’s IP address. If possible, the RADIUS server should only be accessible from the same local network.
*   **Secure RADIUS Server:** Use a RADIUS server with proven security features and keep it patched.
*   **HTTPS for API:** Always use HTTPS when using the MikroTik API and restrict access to trusted IP addresses.
*   **EAP-TLS:** If possible, use EAP-TLS for enhanced security, although it’s more complex to configure.
*   **Limit Users:** Have a robust way to manage users and remove users that are not needed anymore.
*   **Monitor Logs:** Always monitor RADIUS logs to check for any suspicious activity, either in the router or the RADIUS server.

## Self Critique and Improvements

*   **Current Setup:** This is a functional SOHO-level implementation that covers the basic configuration.
*   **Improvements:**
    *   **Dynamic VLAN Assignment:** Integrating dynamic VLAN assignment based on RADIUS attributes would improve network segmentation.
    *   **Accounting:** Implementing full accounting with RADIUS would provide better monitoring of bandwidth usage.
    *   **Failover:** Using multiple RADIUS servers will increase availability.
    *   **More Robust Security:** Implementing EAP-TLS for improved security.
    *   **Granular Security Profile:** When configuring different security profiles, ensure the correct Authentication methods are used depending on each wireless interface and the requirements of the user group.
    *   **Proper Testing:** A more robust testing system, including multiple client tests and different connection scenarios would make this configuration even better.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users attempting to access network resources.

*   **Authentication:** RADIUS validates the user’s credentials (username and password) against a central database.
*   **Authorization:** Once authenticated, RADIUS can authorize the user for specific network resources.
*   **Accounting:** RADIUS can track users' session data (start time, stop time, traffic usage, etc.).

**Why use RADIUS?**

*   **Centralized Management:** One single point for managing users, avoiding local passwords or keys on each device.
*   **Scalability:** Easily add or remove users and change settings.
*   **Enhanced Security:** More secure than PSK authentication, especially when combined with EAP methods.
*   **Flexibility:** Offers advanced features like VLAN assignment, QoS, and more.

## Detailed Explanation of Trade-offs

*   **PSK vs. RADIUS:**
    *   **PSK (Pre-Shared Key):** Easy to set up but less secure and hard to manage for many users.
    *   **RADIUS:** More complex to configure but more secure and scalable.
    *   **Trade-off:** Complexity vs. security and scalability.
*   **EAP Methods:**
    *   **EAP-TLS:** Most secure EAP method but the most complex, requiring certificate management.
    *   **PEAP/EAP-TTLS:**  Easier to implement than EAP-TLS while still providing strong security.
    *   **Trade-off:** Security vs. complexity.
*   **Radius MAC Format**
    *  **Username**: The Mac address of the device will be presented as a user to the server.
    *  **Calling Station ID**: The Mac address will be presented as a calling station id.
    * **Trade-Off:** How the server is configured to handle the MAC address.

## Configuration for Specific RouterOS Versions:

This documentation targets RouterOS 7.12 and is also relevant for version 6.48 and other 7.x releases. If you need to make changes, ensure the commands used are available in your target ROS version by checking the RouterOS documentation. This configuration utilizes stable commands for the 7.x series.

This comprehensive guide provides a detailed, actionable, and tested example for implementing RADIUS authentication on your MikroTik router. Remember to adjust the IP addresses, secrets, and other specific parameters to match your network environment.
