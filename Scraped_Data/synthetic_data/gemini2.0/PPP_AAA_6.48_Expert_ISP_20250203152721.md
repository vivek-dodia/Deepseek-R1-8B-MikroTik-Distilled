Okay, let's craft some detailed technical documentation for PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik RouterOS 6.48 (also valid for 7.x) device, targeted for an ISP environment with a specific focus on the given subnet and interface.

**## Scenario Description:**

We're building an ISP environment where subscribers connect via PPP (Point-to-Point Protocol) over a physical interface (`ether-33`) connected to a DSLAM or similar access network. We will provide an IP address, and other parameters through a Radius Server, and keep accounting records for proper management and billing. All clients will be within the `120.238.76.0/24` subnet. We'll leverage MikroTik's built-in PPP server capabilities and interface with a RADIUS server for authentication, authorization, and accounting (AAA).

**Configuration Level:** Expert

**Network Scale:** ISP

**## Implementation Steps:**

**Detailed Explanation of Topic:**

PPP (Point-to-Point Protocol) is a common method for establishing direct connections between two network nodes. When using AAA in a PPP environment, authentication verifies the user's identity, authorization determines what network resources they can access, and accounting tracks their usage (e.g., time connected, data transferred). This is crucial for ISPs to control access and bill subscribers accurately. We will use an external Radius server for the AAA functionality.

**1. Step 1: Configure the RADIUS Client.**

*   **Purpose:** This step defines the communication parameters for the MikroTik router to interact with the external RADIUS server.

*   **Before Configuration:**  Ensure you have your RADIUS server's IP address, secret key, authentication port, and accounting port handy.
*   **CLI Instruction:**

    ```mikrotik
    /radius add address=192.168.1.100 secret="your_radius_secret" service=ppp timeout=10 authentication-port=1812 accounting-port=1813
    ```

*   **Explanation of Parameters:**
    | Parameter             | Description                                                        |
    | --------------------- | ------------------------------------------------------------------ |
    | `address`             | The IP address of the RADIUS server.                               |
    | `secret`              | The shared secret key used for communication with the RADIUS server.|
    | `service`             | The service for which this RADIUS server is used (ppp in our case). |
    | `timeout`             | The timeout in seconds before considering the RADIUS server unreachable.  |
    | `authentication-port` | The UDP port used for authentication requests (default is 1812).     |
    | `accounting-port`    | The UDP port used for accounting requests (default is 1813).        |

*   **Winbox GUI:** `Radius` menu item, `+` button.

*   **After Configuration:** The MikroTik router can now attempt to communicate with the RADIUS server for authentication and accounting purposes.  You can verify this with a simple ping from the router to the RADIUS server or by watching the `Radius` menu. No authentication will happen yet.

**2. Step 2: Create a PPP Profile.**

*   **Purpose:** A PPP profile sets the default parameters for PPP connections. This step defines the local address pool and interface type for PPP.
*   **Before Configuration:** Understand the different PPP profile parameters.
*   **CLI Instruction:**

    ```mikrotik
    /ppp profile add name="ppp-profile-radius" local-address=120.238.76.1 remote-address=120.238.76.0/24 use-encryption=yes only-one=no
    ```
*   **Explanation of Parameters:**
    | Parameter           | Description                                                                                                     |
    | ------------------- | --------------------------------------------------------------------------------------------------------------- |
    | `name`              | The name for the PPP profile.                                                                                  |
    | `local-address`     | The local IP address used in the PPP connection.                                                              |
    | `remote-address`    | The pool (or range) of addresses that the remote client will be assigned from.  The radius server can override this.   |
    | `use-encryption`    | Requires the use of encryption on the PPP link, which is strongly recommended for security.                                                               |
    | `only-one`          | If set to yes, only one active connection can use this profile at any time; otherwise, multiple connections are allowed.     |

*   **Winbox GUI:** `PPP -> Profiles` menu, `+` button.
*   **After Configuration:** A PPP profile named "ppp-profile-radius" exists that can now be applied to PPP connections.
    This profile defines basic parameters that are default for all connections using it.

**3. Step 3: Enable PPP Server and Attach it to `ether-33`**.

*   **Purpose:** This step enables a PPP server that will listen on `ether-33` for incoming PPP connections.
*   **Before Configuration:** `ether-33` should be properly configured and active with access to the access network.
*   **CLI Instruction:**

    ```mikrotik
    /interface pppoe-server server add service-name=pppoe-radius-service interface=ether-33 authentication=pap,chap,mschap1,mschap2 profile=ppp-profile-radius max-mtu=1480 max-mru=1480 keepalive-timeout=10
    ```
*  **Explanation of Parameters:**
    | Parameter             | Description                                                                                |
    | --------------------- | ------------------------------------------------------------------------------------------- |
    | `service-name`      | The name of this PPPoE server instance.                                                     |
    | `interface`           | The physical interface to listen on (`ether-33` in our case).                                |
    | `authentication`     | The authentication protocols allowed for clients connecting (PAP, CHAP, MSCHAP1, MSCHAP2 are allowed).  |
    | `profile`            | The PPP profile to apply to connections using this server instance (`ppp-profile-radius` in our case).  |
    |`max-mtu`            | The maximum transmission unit (MTU), which specifies the largest data packet size allowed on the PPP link.   |
    |`max-mru`           | The maximum receive unit (MRU), which specifies the largest packet size the receiving end can handle. |
    |`keepalive-timeout`   | The timeout in seconds for detecting a disconnected PPP link.  |
    
*   **Winbox GUI:**  `PPP -> PPPoE Servers` menu, `+` button.
*  **After Configuration:** The MikroTik device is now listening for incoming PPP connections on the specified interface, using the configured profile and authentication protocols.

**4. Step 4: Configure PPP Secret.**

*   **Purpose:**  We don't want to add the users locally, as we are using a Radius server, so this step is more of a placeholder and fallback method. It will always authenticate the user with the radius server first, before it checks locally defined secrets. If the Radius server fails, the user may be able to connect locally, but we can avoid this.
*   **Before Configuration:** Choose a fallback user/password.
*   **CLI Instruction:**

    ```mikrotik
        /ppp secret add name=fallback_user password=fallback_password service=pppoe profile=ppp-profile-radius disabled=yes
    ```
*   **Explanation of Parameters:**
     | Parameter           | Description                                                                                                     |
    | ------------------- | --------------------------------------------------------------------------------------------------------------- |
    |`name`          |  Username of the user.
    |`password`          | Password of the user.
    |`service`          | Service type of the user.
    |`profile`          |  The profile for this user.
    |`disabled`          | If set to `yes` the local secret will not be used for authentication, making the user only useable via radius.

*   **Winbox GUI:** `PPP -> Secrets` menu item, `+` button.
*  **After Configuration:** A local fallback user has been added.

**5. Step 5: Enable RADIUS for PPP Authentication**

*   **Purpose:** Direct MikroTik to use the RADIUS server for PPP user authentication.
*   **Before Configuration:** Ensure the RADIUS server is reachable and configured.
*   **CLI Instruction:** No specific command needed.
*   **Winbox GUI:** No specific GUI configuration needed.
*  **After Configuration:** PPP connections will be authenticated against the configured RADIUS server.

**## Complete Configuration Commands:**

```mikrotik
/radius add address=192.168.1.100 secret="your_radius_secret" service=ppp timeout=10 authentication-port=1812 accounting-port=1813
/ppp profile add name="ppp-profile-radius" local-address=120.238.76.1 remote-address=120.238.76.0/24 use-encryption=yes only-one=no
/interface pppoe-server server add service-name=pppoe-radius-service interface=ether-33 authentication=pap,chap,mschap1,mschap2 profile=ppp-profile-radius max-mtu=1480 max-mru=1480 keepalive-timeout=10
/ppp secret add name=fallback_user password=fallback_password service=pppoe profile=ppp-profile-radius disabled=yes
```

**## Common Pitfalls and Solutions:**

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router cannot connect to the RADIUS server.
    *   **Solution:** Check network connectivity (ping), ensure the correct IP address, ports and secret are configured on both sides. Ensure firewall isn't blocking the RADIUS ports.
*   **Authentication Failures:**
    *   **Problem:** Users cannot authenticate even with valid credentials.
    *   **Solution:** Check the RADIUS server logs for errors, verify the username and password are correct on both sides. ensure the user is allowed in the Radius Server.
*   **IP Address Assignment Failures:**
    *   **Problem:** Users connect, but don't get an IP address.
    *   **Solution:** Confirm the remote-address parameter is correctly configured in the profile and also that the RADIUS server is providing an address, check the logs for debug.
*   **MTU/MRU Mismatch:**
    *   **Problem:**  Connection is established, but data transfer is slow or not working.
    *   **Solution:** Ensure the MTU and MRU values in the PPPoE server profile match the values expected by the client. Try 1492.

* **Security Issue:**
    *   **Problem:** PAP is not secure.
    *   **Solution:** Ensure CHAP is available on both sides, and remove PAP from the accepted protocols.
*   **Resource Issues:**
    *   **Problem:** High CPU usage and memory due to many active PPP connections.
    *   **Solution:** Ensure that you are using the correct hardware for your number of users, monitor system resource and consider disabling unnecessary packages. Also, use more efficient authentication protocols.

**## Verification and Testing Steps:**

1.  **RADIUS Server Reachability:**
    *   **CLI:** `/ping 192.168.1.100`  (or your radius server) should work.
2.  **Authentication Success:**
    *   Connect a PPP client (e.g., a computer using a PPPoE client) with valid credentials from your radius server.
    *   **Winbox:** Check `/ppp active` menu for active connections, if authentication fails, you may be able to see why in the logs.
3.  **IP Address Assignment:**
    *   Once a connection is established, check the client's assigned IP address. It should be within the subnet `120.238.76.0/24`, or as sent by the Radius server.
4.  **Accounting Data:**
    *   Check your RADIUS server for accounting records which may be logged to a database or a log file.
5.  **Logs:**
    *   Check the MikroTik system logs for any authentication or connection errors: `/log print where topics~"ppp"`
    * Enable detailed logging by adding a more verbose entry in the logging config.
6.  **Interface Status:**
    *   Check the status of `ether-33` in `/interface print` and `/interface pppoe-server server print`.  You should see the "running" flag.
7. **Torch:**
     *   Use torch to see if the connection is working, and what is happening in detail `/tool torch interface=ether-33 duration=10`. Make sure you only capture from your router's interface, and not the network.

**## Related Features and Considerations:**

*   **Hotspot:** For more complex user management, the MikroTik Hotspot system can be used in conjunction with PPP.
*   **Firewall:** Make sure that you have proper firewall rules configured for the public IP to protect your network.
*   **Queueing:** Traffic shaping and queueing are very important to provide a good service to each user and limit bandwidth abuse.
*   **DHCP Server:** For more flexibility, you can enable DHCP on the router and forward DHCP requests from your users via the Radius.
*   **User Profiles:** Use different PPP profiles based on a user’s plan for different service settings.
*   **RADIUS Attributes:** Use RADIUS attributes for a fine-grained control over things such as the MTU, IP, DNS, Routes, and more.
* **Bandwidth Limiting:** In the Radius server, you can control each user's bandwidth through Radius attributes, this is preferable to other methods like simple queues, as the bandwidth control will be user specific.

**## MikroTik REST API Examples:**

**Note:** While the core PPP functionality isn't directly exposed through the MikroTik REST API in a way that directly creates the setup, you *can* use the API to manage some aspects of your config.
Here's an example showing how to view the PPPoE servers using the REST API.

*   **Endpoint:** `/interface/pppoe-server/server`
*   **Method:** `GET`
*   **Request (Example - None required):**

    ```
    GET /interface/pppoe-server/server
    ```

*   **Expected Response (Example JSON):**

    ```json
    [
       {
          "service-name": "pppoe-radius-service",
          "interface": "ether33",
          "authentication": "pap,chap,mschap1,mschap2",
          "profile": "ppp-profile-radius",
          "max-mtu": "1480",
          "max-mru": "1480",
          "keepalive-timeout": "10"
        }
    ]
    ```
*   **REST API Explanation:**
    - Use HTTP GET to get the list of configured PPPoE servers.
    - The API will return an array of objects, with all properties of the configured server.
    - Other REST API calls will allow for reading, updating or removing data.
    - For more information about MikroTik's REST API, see the official documentation.

**## Security Best Practices:**

*   **Use Strong RADIUS Secrets:** Use long, complex, and unique secrets for your RADIUS server.
*   **Encrypt PPP Connections:** Require and use PPP encryption on all connections.
*   **Firewall Protection:** Firewall rules should be in place on the MikroTik router and on other devices to prevent unauthorized access to both the router and the users.
*   **Keep RouterOS Updated:** Make sure you keep your RouterOS version up-to-date, to receive the most recent security updates.
* **Disable PAP:** Only use CHAP, and MSCHAP authentication protocols.
* **Do Not Send Passwords:** Disable the possibility of sending clear text passwords over the wire, always opt to use a secure method for authentication.
*   **Logging:** Make sure that you have proper logging configured to see and investigate any security issues.

**## Self Critique and Improvements:**

*   **Improvement:** We could implement per-user rate limiting by pushing specific QoS settings from the RADIUS server for better bandwidth control.
*   **Improvement:**  Using IPv6 would be a good practice, and the setup can be easily extended to it.
*   **Improvement:** Consider a more secure authentication method, such as EAP.
*   **Improvement:** Could include a method to create, update or delete users on the radius server through an API.
*   **Improvement:** Could create a better user monitoring dashboard with the usage information coming from radius.

**## Detailed Explanation of Trade-offs:**

*   **Local vs. RADIUS Authentication:**  Local PPP secrets are less secure and less scalable than using a RADIUS server. RADIUS offers centralized management, accounting, and finer-grained authorization. The trade-off is increased complexity and dependence on a functioning RADIUS server.
*   **PAP vs. CHAP:** PAP sends passwords in clear text and is a huge security risk. CHAP uses a challenge-response mechanism to authenticate users without transmitting passwords directly, making it much safer.
*   **MTU/MRU:** The MTU defines the largest packet size on the data link and must be smaller than or equal to the smallest MTU used anywhere on the path, this affects the performance of the link and the optimal value is defined by the specific environment.
*  **Encryption:** Encryption is strongly recommended, and the trade-off is that some legacy devices may have problems with the encrypted communication, so it may be necessary to disable encryption for them.

**Configuration for Specific RouterOS Versions:**

The provided configuration is compatible with both RouterOS 6.48 and 7.x. The commands and parameters used are consistent across these versions.  If a RouterOS version does not include a command, it will be noted in the documentation, otherwise, the command will work for all version in the scope of this documentation. For instance, the REST API may differ slightly between RouterOS versions, so always refer to the official documentation for specifics on each version.

**Important Note:** This documentation is provided as a starting point. You'll need to tailor the specific RADIUS settings, IP addresses, secrets, and security rules to your own environment and requirements.
