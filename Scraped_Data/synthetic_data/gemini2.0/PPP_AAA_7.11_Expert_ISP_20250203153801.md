Okay, let's dive deep into configuring PPP AAA with MikroTik RouterOS for an ISP environment, targeting RouterOS 7.11. This will be an expert-level configuration with a focus on the `wlan-50` interface and subnet `149.99.72.0/24`.

**Scenario Description:**

We are setting up a PPP server on a MikroTik router that will authenticate users connecting via the `wlan-50` interface using a RADIUS server for authentication, authorization, and accounting (AAA). This is common for ISPs providing wireless internet access to customers where granular control over access, usage, and billing is required.

**Implementation Steps:**

1. **Step 1: Disable Default PPP Server (if any)**

   *   **Purpose:** Ensure no default or pre-existing PPP configurations interfere with our new setup. We must ensure that no unexpected connections or behavior occur during our setup, to not disrupt existing services.
   *   **Before:**
        *   Check if any PPP servers are already running
       ```
       /ppp server print
       ```
        *   If found, take a note of existing configurations, and then disable them
   *   **Action:** Disable any existing PPP server instances.
       ```
       /ppp server disable [server name]
       ```
        *  Replace `[server name]` with the name or number of the server you want to disable
   *   **After:**
        *  Verify no PPP servers are active
       ```
       /ppp server print
       ```
        *  There should be no server listed

2.  **Step 2: Create a PPP Profile**
    * **Purpose:** Define the settings that will be applied to each connecting client, such as IP addressing, DNS servers, and any specific route information. This profile is crucial for PPP connections.
    * **Before:**
        *   Check for existing profiles
        ```
        /ppp profile print
        ```
    *   **Action:** Create a new profile named "isp-pppoe".
        ```
        /ppp profile add name=isp-pppoe local-address=149.99.72.1 remote-address=149.99.72.2-149.99.72.254 dns-server=8.8.8.8,8.8.4.4
        ```
        * **Explanation of parameters:**
            *   `name=isp-pppoe`: The name of the profile.
            *   `local-address=149.99.72.1`: The IP address of the router interface.
            *   `remote-address=149.99.72.2-149.99.72.254`: IP range for PPP clients.
            *   `dns-server=8.8.8.8,8.8.4.4`: DNS servers to assign to clients.
    *   **After:**
        *   Verify the new profile has been created:
        ```
        /ppp profile print
        ```

3.  **Step 3: Create a PPP Secret (for local authentication - optional for RADIUS setups)**
    *   **Purpose:** If local authentication is desired, a secret for users. Often, with RADIUS this is omitted.
    *   **Before:**
        *   Check for any configured PPP secrets
        ```
        /ppp secret print
        ```
    *   **Action:** Create a new secret for user "testuser" with password "testpass", using profile `isp-pppoe` created in Step 2
        ```
        /ppp secret add name=testuser password=testpass service=pppoe profile=isp-pppoe
        ```
        * **Explanation of parameters:**
            *   `name=testuser`: The username.
            *   `password=testpass`: The user password.
            *   `service=pppoe`: Specify PPP over Ethernet (pppoe).
            *   `profile=isp-pppoe`: Assign to the created profile.
        *   *Note:* For RADIUS setups, secrets might be managed entirely by the server, therefore this step is optional.
    *   **After:**
        *  Verify the user "testuser" has been created.
       ```
       /ppp secret print
       ```

4.  **Step 4: Configure the PPP Server (PPPoE in this case)**
    *   **Purpose:**  Enable the PPP service on the selected interface `wlan-50` and apply our newly created profile.
    *   **Before:**
        * Check to ensure that the `wlan-50` interface is active
        ```
        /interface print
        ```
    *   **Action:** Create a PPPoE server on `wlan-50` using the `isp-pppoe` profile.
        ```
        /ppp server add name=pppoe-server1 interface=wlan-50 service=pppoe max-mru=1492 max-mtu=1492 profile=isp-pppoe
        ```
        * **Explanation of parameters:**
            *   `name=pppoe-server1`: Name of the server.
            *   `interface=wlan-50`: Interface to listen on.
            *   `service=pppoe`: PPP service type (PPPoE).
            *   `max-mru=1492 max-mtu=1492`: Ensure that the MRU and MTU are set correctly.
            *   `profile=isp-pppoe`:  Assign to the created profile.
    *   **After:**
        *   Verify the server has been added and enabled
        ```
         /ppp server print
        ```
        *   You should see the server `pppoe-server1` listed in the results

5. **Step 5: Configure RADIUS Client**
    *   **Purpose:** Configure the MikroTik to communicate with the RADIUS server. This is the heart of AAA.
    *   **Before:**
        *   Check if there are any existing RADIUS configurations
         ```
        /radius print
        ```
    *   **Action:** Configure the RADIUS client.
        ```
        /radius add address=192.168.88.10 secret=supersecret service=ppp timeout=3
        ```
        *  **Explanation of parameters:**
             *   `address=192.168.88.10`: IP address of your RADIUS server. Replace with your actual RADIUS server address.
             *   `secret=supersecret`: Shared secret with the RADIUS server. Must match RADIUS configuration.
             *  `service=ppp`:  Specify PPP service.
             * `timeout=3`: Number of seconds before timeout.
        *  *Note*: It's recommended to enable accounting if your RADIUS server supports it.
    *   **After:**
        * Verify the RADIUS client has been added.
       ```
       /radius print
       ```

6.  **Step 6: Enable RADIUS Authentication and Accounting**
    *   **Purpose:**  Tell the PPP service to use the RADIUS client for authentication and accounting.
    *   **Before:**
        * Check if radius is enabled for PPPoE.
        ```
        /ppp server print
        ```
    *   **Action:** Modify the PPP server to use RADIUS.
        ```
        /ppp server set pppoe-server1 use-radius=yes
        ```
        *  **Explanation of parameters:**
             *   `pppoe-server1`: The name of our PPP server from Step 4.
             *   `use-radius=yes`: Enable RADIUS authentication.
        *   *Note*: you can enable or disable accounting on this step as well
        ```
         /ppp server set pppoe-server1 accounting=yes
         ```
    *   **After:**
        *   Verify that the configuration is set correctly
        ```
        /ppp server print
        ```
         * `use-radius` and `accounting` should both be set to `yes`.

**Complete Configuration Commands:**

```
/ppp server disable [server name] # Disable existing ppp server (if any, replace [server name])
/ppp profile add name=isp-pppoe local-address=149.99.72.1 remote-address=149.99.72.2-149.99.72.254 dns-server=8.8.8.8,8.8.4.4
/ppp secret add name=testuser password=testpass service=pppoe profile=isp-pppoe
/ppp server add name=pppoe-server1 interface=wlan-50 service=pppoe max-mru=1492 max-mtu=1492 profile=isp-pppoe
/radius add address=192.168.88.10 secret=supersecret service=ppp timeout=3
/ppp server set pppoe-server1 use-radius=yes
/ppp server set pppoe-server1 accounting=yes # optional, if RADIUS accounting required
```

**Common Pitfalls and Solutions:**

*   **RADIUS Server Unreachable:**
    *   **Problem:** Router cannot communicate with the RADIUS server.
    *   **Solution:** Verify IP address of the RADIUS server, the shared secret, and network connectivity. Use `ping` and `traceroute` to diagnose network issues.
*   **Incorrect Shared Secret:**
    *   **Problem:** Authentication fails due to a mismatch in the shared secret.
    *   **Solution:**  Double-check that the secret configured on the MikroTik matches the secret configured on the RADIUS server.
*  **Mismatched Attributes in RADIUS Response:**
   *  **Problem:** RADIUS server is configured for some attributes that are not configured in the MikroTik device.
   *  **Solution:** Use Torch or a packet sniffer on the MikroTik to observe the RADIUS responses and check against the user profile, or the router setup, in order to find the missing setting.
*   **MTU/MRU issues:**
    *   **Problem:** Incorrect MTU/MRU can lead to fragmentation issues and poor performance.
    *   **Solution:** Ensure that the `max-mru` and `max-mtu` settings on the PPPoE server are consistent with the network’s overall settings.
*   **Firewall Issues:**
    *   **Problem:** Firewall rules are blocking traffic to the RADIUS server.
    *   **Solution:** Make sure that firewall is not blocking UDP traffic on port 1812 and 1813.
* **Authentication Issues**
   * **Problem**: Users are not authenticating properly and getting rejected
   * **Solution**: On the MikroTik, check the logs `/system logging print` and look for any RADIUS specific messages. If you are unable to determine the root cause from the router logs, consider checking your RADIUS server logs for troubleshooting.

**Verification and Testing Steps:**

1.  **RADIUS Server Reachability:** Use `ping 192.168.88.10` to check if the RADIUS server is reachable.
2.  **Connect a PPPoE Client:** Attempt to connect using a client machine (computer, other router) and the username/password (if local authentication was used, the one from Step 3).
3.  **Check Active PPP Connections:**
   ```
    /ppp active print
    ```
     *  A successful connection should be listed here.
4. **Check RADIUS logs:**
     * Check `/system logging print` for any RADIUS related messages.
5.  **Monitor traffic with Torch:**
     * Use `/tool torch interface=wlan-50` to monitor traffic on the `wlan-50` interface.
6. **Use RADIUS Server logs**
    * If your RADIUS server supports logging, check the logs for any issues, and confirm that requests are being received, and if there is any authorization or authentication issues

**Related Features and Considerations:**

*   **Hotspot:** Combining PPP with MikroTik's Hotspot feature for more advanced portal, captive portal and user management.
*   **Traffic Shaping:** Use the MikroTik Queue Tree to manage bandwidth per user or per profile.
*   **VPNs:** Combining the PPP connection with VPN tunnels (L2TP, IPIP) for security.
*  **VRF:** Virtual Routing and Forwarding can be used to isolate networks for different user groups.

**MikroTik REST API Examples (if applicable):**

While MikroTik's REST API is mostly for configuration, you *could* interact with PPP. Here's how to fetch PPP active connections:

*   **Endpoint:** `/ppp/active`
*   **Method:** `GET`
*   **Payload:** None
*   **Expected Response:**
   ```json
   [
     {
       ".id": "*2",
       "name": "testuser",
       "service": "pppoe",
       "caller-id": "00:00:00:00:00:00",
       "address": "149.99.72.100",
       "encoding": "mppe128",
       "uptime": "00:01:02"
     }
   ]
   ```
*   **Error Handling:** If the API call fails, you'll get an error status in the JSON. You can check the `message` field for details.

To enable RADIUS on a PPPoE server via the REST API:

*   **Endpoint:** `/ppp/server`
*   **Method:** `PATCH`
*   **Payload Example:**
   ```json
      {
        ".id": "*1",  // Use the ID of the PPP server from the `/ppp/server` call
        "use-radius": true
      }
    ```
*   **Expected Response:** `HTTP 200 OK`
*   **Error Handling:** Look for the `message` key in the JSON if an error occurred. The `message` contains specific error details such as an invalid ID.

**Security Best Practices**

*   **Shared Secret Security:** The RADIUS shared secret must be strong and protected. Do not store the secret in the clear.
*   **User Authentication:** Enforce strong user passwords, and consider using PAP, CHAP or MS-CHAPv2, based on your RADIUS server capabilities.
*  **Accounting:** Enable accounting for proper logging of user data and resources.
*   **Rate Limiting:** Implement rate limiting to prevent abuse or denial-of-service attacks.
*   **Firewall:** Restrict access to the RADIUS server from the router (or any other devices) with a firewall.
*   **RouterOS updates:** Keep your RouterOS updated with the latest patches.

**Self Critique and Improvements**

This is a fairly robust PPP AAA configuration. Here are some improvements and considerations:

*   **More advanced RADIUS attributes**:  For a real ISP setup, you should implement more complex RADIUS attributes (e.g. rate-limits, usage limits) based on your system.
*   **Dynamic address allocation:** You can configure RADIUS to dynamically assign IP addresses based on user attributes.
*   **VRF integration**: Using VRF allows you to isolate different types of users. This would prevent them from interacting with each other and provide better performance.
*   **Logging:** Implement more detailed logging (especially for RADIUS failures) for better troubleshooting and audits.

**Detailed Explanation of Topic**

PPP (Point-to-Point Protocol) is a network protocol used to establish direct connections between two nodes. PPP is widely used for Dial-up connections, DSL connections and other types of serial or network-based connections. AAA (Authentication, Authorization, and Accounting) is a framework for controlling access to computer resources, enforcing policies, and tracking resource usage, and it helps to maintain better security, and billing for users. When combined, PPP with AAA allows service providers to securely manage user connections with a central server. When configuring PPP AAA with RADIUS the MikroTik router sends user authentication requests to a RADIUS server, which returns the authorization, and performs accounting.

**Detailed Explanation of Trade-offs**

*   **Local vs. RADIUS Authentication:** Local authentication (using `/ppp secret`) is simple, but lacks scalability and central control. RADIUS authentication provides centralized management and allows more sophisticated attribute handling. The trade-off is complexity versus scalability.
*   **PAP/CHAP/MS-CHAPv2:** PAP sends credentials in cleartext. CHAP and MS-CHAPv2 provide some measure of security with the use of a challenge-response protocol. For real-world deployments it's always recommended to use the most secure method supported by the server and the client, and always secure traffic via IPSec if available.
*   **Static vs Dynamic IP Allocation:** Static allocation can cause a lot of configuration overhead for large networks, while dynamic allocation improves user assignment and allows the router to manage IP space. However, static assignments can be important for specific users or networks. This depends greatly on the needs of the operator.
*   **Performance:** Adding security measures like encryption increases overhead. It is important to carefully select settings that provide an acceptable balance between performance and security.

**Configuration for Specific RouterOS Versions:**

This configuration is designed for RouterOS 7.11 (and should generally be compatible with 6.48 and other 7.x versions). However, check the specific RouterOS documentation for the exact syntax of newer, or older, commands. For example, if you were using RouterOS v6 the command `/ppp server add` was missing the accounting parameter, so this would need to be specified under the `ppp server set` step.

Let me know if you have any specific adjustments or further requirements.
