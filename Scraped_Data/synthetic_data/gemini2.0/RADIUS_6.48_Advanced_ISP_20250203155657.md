Okay, let's dive into a comprehensive guide on configuring RADIUS authentication on a MikroTik router, specifically for the scenario you've outlined, targeting RouterOS 6.48 (while considering 7.x compatibility), at an ISP network scale, using subnet 246.171.79.0/24 and interface `bridge-44`.

## Scenario Description:

This scenario involves configuring a MikroTik router to authenticate users via a RADIUS server before granting them access to the network. We'll assume the users are connecting to the network via the `bridge-44` interface, which could be a wired or wireless bridge. The primary purpose is to centrally manage user authentication and potentially accounting data on a dedicated RADIUS server. We'll be focusing on the initial setup and basic functionality.

## Implementation Steps:

Here’s a step-by-step guide on how to configure RADIUS on your MikroTik router, with explanations and examples using both CLI and Winbox GUI:

### 1. Step 1: Define RADIUS Server Settings
   * **Purpose**: This step involves telling the MikroTik router the address and shared secret of your RADIUS server.
   * **CLI Command Example**:

     ```mikrotik
     /radius add address=192.168.10.10 secret="your_radius_secret" service=ppp,hotspot,login timeout=3
     ```
   * **Explanation**:
       * `/radius add`: Command to add a new RADIUS server configuration.
       * `address=192.168.10.10`: IP address of your RADIUS server. Replace with your server's IP.
       * `secret="your_radius_secret"`: The shared secret key for RADIUS authentication. Replace with the actual secret. *Note: this secret must match the one configured in the RADIUS Server*.
       * `service=ppp,hotspot,login`: Specifies which services on the Mikrotik should use this RADIUS server. For this example, we are using ppp (PPPoE/PPTP/L2TP etc), hotspot (for captive portals), and login (for router login)
       * `timeout=3`: The connection timeout in seconds before retrying (3 seconds in this case)
   * **Winbox GUI**:
     1. Go to `RADIUS` under `PPP`.
     2. Click on `Add (+)`.
     3. In the `New Radius` window, fill the following fields:
          * `Address`: `192.168.10.10`
          * `Secret`: `your_radius_secret`
          * Check `ppp`, `hotspot`, `login` under the `Services` Tab.
          * `Timeout` : `3` seconds
     4. Click `Apply` and `OK`.
   * **Before Configuration**: No RADIUS server is configured.
   * **After Configuration**: MikroTik will now know how to communicate with the RADIUS server. No actual users will be authenticated with RADIUS at this stage, but the settings for authentication are present.

### 2. Step 2:  Enable RADIUS for PPP
  * **Purpose**:  Enable RADIUS as the authentication method for specific PPP services. In this scenario we will target an example, and assume that PPPoE will be used to connect the users on the network.
  * **CLI Command Example:**

    ```mikrotik
    /ppp profile set default use-radius=yes
    ```
  * **Explanation:**
      * `/ppp profile set default`: Modifies the default PPP profile.
      * `use-radius=yes`: Enables RADIUS authentication for all PPP connections using this profile.
  * **Winbox GUI**:
     1. Go to `PPP` -> `Profiles`.
     2. Double-click `default` profile
     3. Under the General Tab, check the `Use Radius` box.
     4. Click `Apply` and `OK`.
   * **Before Configuration**: PPP authentication is not set to use radius.
   * **After Configuration**: New PPP connections will attempt authentication via the configured RADIUS server.
     * **Note:** If your profile is not the "default", the command needs to be `/ppp profile set <profile-name> use-radius=yes`
   * **Note:** `default` profile is *not* used for PPPoe server created via `/interface pppoe-server`. If you use `pppoe-server`, a profile must be specified when it is created. You must make sure to set `use-radius=yes` in that profile.

### 3. Step 3: Enable RADIUS for Hotspot

  * **Purpose:** If using Hotspot for user management and authentication, RADIUS can be used to manage the hotspot users.
  * **CLI Command Example:**
  ```mikrotik
   /ip hotspot profile set hsprof1 use-radius=yes
  ```
  * **Explanation:**
    * `/ip hotspot profile set hsprof1`: This sets the profile called `hsprof1`. Replace with your hotspot profile name.
    * `use-radius=yes`: Enable Radius for the hotspot profile.
    * **Note:** It is assumed you already have a hotspot server and profile.
  * **Winbox GUI**:
    1. Go to `IP` -> `Hotspot` -> `Hotspot Profiles`
    2. Select your profile.
    3. Under `General` tab, check the `Use Radius` checkbox.
    4. Click `Apply` and `OK`.
    * **Before Configuration**: Hotspot authentication does not use RADIUS.
    * **After Configuration**: New hotspot authentications will go via the configured RADIUS server.

### 4. Step 4: Testing and Validation:

   * **Purpose:** Test the connection with RADIUS by connecting to the MikroTik with a user already setup in the RADIUS server. In this example, we will connect with a PPPoE client.
   * **CLI Instruction:** You'll need a client device to initiate a PPPoE or hotspot connection.
   * **Description:**
     1. Configure a PPPoE client, using the Mikrotik as a server. Use a username and password that exists in the RADIUS server.
     2. Attempt a connection.
   * **Expected Result**:
     * Successful Connection: If the credentials are correct on the RADIUS server and the server is reachable, the client should get an IP address.
     * Failed Connection: If credentials are wrong on RADIUS, or the RADIUS server cannot be contacted, the client should fail to get an address. Check RouterOS logs for specific error messages.

## Complete Configuration Commands:

Here are all the commands together, with full explanations.

```mikrotik
# --- Configure RADIUS Server ---
/radius add \
    address=192.168.10.10 \
    secret="your_radius_secret" \
    service=ppp,hotspot,login \
    timeout=3

# --- Enable RADIUS for PPP Default Profile ---
/ppp profile set default use-radius=yes

# --- Enable RADIUS for Hotspot Profile hsprof1 ---
/ip hotspot profile set hsprof1 use-radius=yes

# Explanation of Parameters:
# /radius add: Adds a new RADIUS server configuration.
#     address: The IP address of the RADIUS server.
#     secret: The shared secret used to authenticate the router against the RADIUS server.
#     service: Comma-separated list of services using this RADIUS server (ppp, hotspot, login).
#     timeout: The timeout in seconds for connecting to the RADIUS server.
# /ppp profile set: Modifies settings of a PPP profile.
#     default/profile-name: The name of the PPP profile to modify (default or a named profile).
#     use-radius: Enables RADIUS authentication for PPP connections using this profile.
# /ip hotspot profile set: Modifies the settings of a hotspot profile.
#      hsprof1: The name of the hotspot profile to modify.
#      use-radius: Enable RADIUS authentication for hotspot users.

```

## Common Pitfalls and Solutions:

*   **Incorrect Shared Secret:** This is the most common issue. The shared secret on the MikroTik *must* exactly match the secret configured on the RADIUS server. Double-check and copy/paste if possible.
*   **RADIUS Server Unreachable:** Ensure your MikroTik can reach the RADIUS server. Test connectivity with `ping 192.168.10.10` (or your RADIUS server IP). Also check firewall rules, they may be blocking access to RADIUS.
*   **Incorrect Service Configuration**: Ensure you've selected the appropriate services under `/radius` settings (ppp, hotspot etc).
*   **RADIUS Server Logs**: If you're having issues, examine your RADIUS server logs for clues. They will indicate why the authentication failed (e.g. bad username/password, bad secret).
*   **MikroTik Logs**: Use `/log print topics=radius` on the MikroTik to see logs related to RADIUS communications. Look for error messages indicating what went wrong.
*   **Timeout Issues**: If requests time out regularly, either the RADIUS server is slow or there is a network issue. Check the RADIUS server health and network connectivity between MikroTik and RADIUS.
*   **CPU/Memory Overload**: In very high-volume authentication environments, RADIUS can cause higher CPU usage. If you see high load, investigate why. Try to improve hardware if necessary. Make sure the router is properly sized for the intended usage.
*   **Security**: The RADIUS shared secret is crucial. Make sure it is very strong and never exposed. Using IPsec to communicate with the radius server may further help security.

## Verification and Testing Steps:

1.  **Ping Test:** `ping 192.168.10.10` (or your RADIUS server IP). This checks basic IP connectivity. If this fails, focus on network issues.
2.  **RADIUS Logs**: Check your RADIUS server logs for successful or failed authentication attempts.
3.  **MikroTik Logs**: Use `/log print topics=radius` to view RADIUS-specific logs on the MikroTik router.
4.  **PPPoE Client Test:** Configure a client to connect via PPPoE, using credentials configured on the RADIUS server. Check for IP address assignment and connectivity.
5.  **Hotspot User Test:** If using Hotspot, attempt to authenticate through the hotspot portal using credentials configured in the RADIUS server.
6.  **Torch Tool:** If further investigation is needed, you can run `/tool torch interface=bridge-44` or any other relevant interface, and select "radius" in the filter to see the RADIUS communication in real-time.

## Related Features and Considerations:

*   **Accounting:** You can enable RADIUS accounting to track user session times, bandwidth usage, etc. Use `/radius set 0 accounting=yes` (assuming `0` is your RADIUS server ID). Also, make sure to enable accounting in the radius server configuration.
*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy. The MikroTik will try them in the order listed until one works.
*   **Dynamic Authorization:** The MikroTik supports RADIUS CoA (Change of Authorization) which allows the RADIUS server to make changes to active sessions (like disconnecting users) after they are already connected.
*   **IP Binding:** For static IP assignments, RADIUS can be used to send IP addresses to the client. You must setup radius to handle the IP address attribution.
*   **RADIUS Attributes:** You may need to work with specific RADIUS attributes to customize your setup, such as setting VLAN tags and bandwidth limits.

## MikroTik REST API Examples (if applicable):

MikroTik doesn't fully expose RADIUS management through its REST API, but you can *read* the configured radius settings. You can't add or modify them.

```
# Example 1: GET Request to Retrieve RADIUS Settings

# API Endpoint: /ppp/radius

# Request Method: GET

# Example Response (JSON)
[
    {
        "id": "*0",
        "address": "192.168.10.10",
        "secret": "your_radius_secret",
        "timeout": "3",
        "domain": "",
        "accounting": "no",
        "service": "ppp,hotspot,login"
    }
]
# Error handling is done by HTTP codes and responses, such as 401 Unauthorized, 404 Not Found etc.
```

*   **API Notes**: Remember to use proper authentication headers with your REST API calls, and replace `192.168.10.10` and other configuration parameters with actual values for your environment.

## Security Best Practices

*   **Strong Shared Secret:** Use a complex, randomly generated shared secret for RADIUS.
*   **Secure Channel:** If possible, use IPsec for encrypting communication between the MikroTik router and RADIUS server.
*   **Restrict Access:** Limit access to the MikroTik and RADIUS server to only authorized administrators.
*   **Monitor Logs:** Regularly monitor MikroTik and RADIUS server logs for suspicious activity.
*   **Software Updates**: Always keep MikroTik RouterOS updated to the latest stable version.
*   **Physical Security:** Secure the physical access to your router.

## Self Critique and Improvements:

*   **Complexity Management:**  For a larger environment, consider creating specific profiles for different types of users/services for better management instead of using the default profiles.
*   **Redundancy:** For a high availability environment, adding more RADIUS servers for failover is essential.
*   **Advanced Features:**  This guide provides only a basic configuration. Consider advanced features such as dynamic VLAN assignment, bandwidth shaping, or RADIUS COA.
*   **Automation:** For large environments, scripting or using a network management system to manage the configuration may be useful.
*   **Logging:** While basic logging is covered, more robust logging to a syslog server might be helpful for security and troubleshooting.

## Detailed Explanations of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for network access. Here's a breakdown:

*   **Authentication:** Verifies a user's identity by checking the username and password against a database (or other system configured on the RADIUS server).
*   **Authorization:** Determines what resources the user is allowed to access once authenticated, by returning attributes to the router (such as VLAN ID, bandwidth limits, etc).
*   **Accounting:** Tracks user sessions, such as start and end times, data usage, etc., for billing and monitoring.
*   **How it Works:**
    1.  The MikroTik acts as the *RADIUS client*.
    2.  When a user attempts to connect, the router sends the user's credentials to the RADIUS server.
    3.  The RADIUS server authenticates the user against its database.
    4.  The RADIUS server sends a reply back to the router with an `Accept` or `Reject`. It may include attributes for authorization.
    5.  If the user is accepted, access is granted based on the returned attributes. If accounting is enabled, session information will also be sent to the radius server.

## Detailed Explanation of Trade-offs

*   **Local vs RADIUS Authentication**:
    *   **Local:** Easier to set up for simple scenarios but harder to scale. It requires managing user credentials locally on the router. Less secure as credentials are stored in the router, and the router itself becomes a single point of failure.
    *   **RADIUS:** More complex to set up initially, but provides central user management, scalability, and better security since credentials aren't stored in the router. Introduces a dependency to the RADIUS server, but this can be mitigated by having multiple RADIUS servers.
*   **Default vs Named PPP Profile**:
    *   **Default**: Easy to use but less flexible, as every PPPoE connection will use the same settings.
    *   **Named**: Can create multiple profiles, each with different settings, such as bandwidth limits, accounting, etc.
*   **Accounting Enabled**:
    *   **Pros:** Provides detailed usage tracking, useful for billing and resource management.
    *   **Cons:** Can increase network traffic and resource utilization on both the router and the radius server.
*   **Single vs Multiple RADIUS Servers**:
    *   **Single:** Simpler to set up but a single point of failure.
    *   **Multiple:** Provides redundancy, but adds complexity to both the radius server configuration and client configuration.

## Configuration for Specific RouterOS Versions:

The above commands work consistently between RouterOS 6.48 and 7.x. However, always refer to the specific documentation for your version. The API responses might change between different versions of the RouterOS.

This documentation should give you a solid start with setting up RADIUS authentication in your MikroTik environment. Remember to test each step thoroughly and adapt the configuration to the unique needs of your network!
