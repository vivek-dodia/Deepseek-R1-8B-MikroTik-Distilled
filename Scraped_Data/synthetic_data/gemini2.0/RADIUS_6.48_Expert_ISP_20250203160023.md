Okay, let's craft some detailed technical documentation for a RADIUS server integration on a MikroTik router, targeting RouterOS 6.48 (and commenting on 7.x differences), at an ISP level of scale, using the specific subnet and interface provided.

## Scenario Description:

We will configure a MikroTik router, acting as a network access server (NAS), to authenticate users connecting via the `ether-3` interface against a RADIUS server. This will enable centralized authentication, authorization, and accounting (AAA) for users connecting to the network segment served by `ether-3`, with IP addresses in the `45.61.251.0/24` subnet. This is a common scenario for ISPs providing services such as PPPoE, Hotspot, or even static IP leases tied to user accounts.

## Implementation Steps:

1. **Step 1: Basic Interface and IP Configuration**
    *   **Description:** Ensure the `ether-3` interface has an IP address assigned from the target subnet and is enabled.
    *   **Before:** We assume `ether-3` is either unconfigured or has an incorrect IP configuration.
    *   **Action (CLI):**
        ```mikrotik
        /ip address
        add address=45.61.251.1/24 interface=ether-3
        /interface ethernet
        set ether-3 enabled=yes
        ```
    *   **Action (Winbox GUI):** Navigate to `IP -> Addresses`, add a new entry, specify the address `45.61.251.1/24`, select `ether-3` for the interface. Next, go to `Interface` in the left menu, and check the Enabled box for `ether-3`.
    *   **After:** `ether-3` will be enabled with IP `45.61.251.1/24`, the first address in the subnet, acting as the gateway for the connected network segment.
    *   **Output Example (`/ip address print` after config):**
        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   45.61.251.1/24    45.61.251.0       ether-3
        ```

2. **Step 2: Configure the RADIUS Server Connection**
    *   **Description:** We will add the details of the RADIUS server that will be used for authentication.
    *   **Before:**  No RADIUS server configuration exists.
    *   **Action (CLI):**
        ```mikrotik
        /radius
        add address=192.168.10.10 secret=mysecret service=ppp timeout=3
        ```
        **Parameter Explanation:**
        | Parameter    | Explanation                                                                                               | Example      |
        |--------------|-----------------------------------------------------------------------------------------------------------|--------------|
        | `address`    | IP address of the RADIUS server.                                                                         | `192.168.10.10` |
        | `secret`     | Shared secret between the MikroTik router and the RADIUS server.                                        | `mysecret`    |
        | `service`    | Specifies which service types this RADIUS server is to be used for. Supported services are "ppp", "hotspot", "dhcp", and "wireless" | `ppp`          |
        | `timeout`    | Time in seconds to wait for a RADIUS response before considering the server down.                         | `3`           |
    *   **Action (Winbox GUI):** Go to `Radius` in the left menu, click the plus sign to add a new RADIUS server. Fill in the `Address`, `Secret`, set service to `ppp` and `timeout` to `3`.
    *  **After:** The router is aware of the RADIUS server and can attempt communication. It won't be used until tied to a service.
    *   **Output Example (`/radius print` after config):**
       ```
       Flags: X - disabled, I - invalid
       #   ADDRESS          SECRET          TIMEOUT    SERVICE
       0   192.168.10.10    mysecret        3          ppp
       ```

3. **Step 3: Configure a PPP Profile using RADIUS Authentication**
    *   **Description:** We will create a PPP profile configured to use the defined RADIUS server for authentication. This profile will be used by PPP connections on `ether-3`.
    *   **Before:** No specific PPP profile with RADIUS is configured.
    *   **Action (CLI):**
        ```mikrotik
        /ppp profile
        add name=radius-ppp local-address=45.61.251.1 remote-address=45.61.251.2-45.61.251.254 use-encryption=yes only-one=yes change-tcp-mss=yes use-radius=yes
        ```
        **Parameter Explanation:**
         | Parameter             | Explanation                                                                                                                              | Example                   |
         |-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
         | `name`                |  Name of the profile.                                                                                                                     | `radius-ppp`              |
         | `local-address`       | IP address assigned to the local end of PPP interface, will be gateway. | `45.61.251.1`             |
         | `remote-address`      | Pool of IPs assigned to PPP clients from the given subnet.   |  `45.61.251.2-45.61.251.254`|
         | `use-encryption`      | Whether the connection will use encryption (default is `yes`)                                                                                    | `yes`                    |
         | `only-one`             | Whether to allow only one simultaneous connection per user. `yes` is recommended with RADIUS. | `yes`                    |
         | `change-tcp-mss`     |  Adjust TCP MSS to work with PPP overhead.                                                                                                 | `yes`                    |
         | `use-radius`          |  Whether to use RADIUS for authentication.                                                                                               | `yes`                    |
    *   **Action (Winbox GUI):** Navigate to `PPP -> Profiles`, click the plus sign, name the profile `radius-ppp`, set `local-address` to `45.61.251.1`, `remote-address` to `45.61.251.2-45.61.251.254`, check `Use Encryption`, `Only One` and `Use RADIUS`.
    *   **After:** A PPP profile using RADIUS authentication has been created that can be applied to ppp interfaces on the device.
    *   **Output Example (`/ppp profile print` after config):**
       ```
       Flags: * - default
       #   NAME      LOCAL-ADDRESS    REMOTE-ADDRESS    USE-ENCRYPTION    ONLY-ONE   CHANGE-TCP-MSS    USE-RADIUS
       0   radius-ppp 45.61.251.1 45.61.251.2-45.61.251.254    yes            yes          yes           yes
       ```

4. **Step 4: Create a PPP Secret and Interface**
    *   **Description:**  This step sets up a test PPP server to allow local testing.  Note, In a real-world scenario you will most likely not create local users, and all user lookups will be via the radius.
    *   **Before:** No active PPP server on `ether-3` is configured.
    *   **Action (CLI):**
        ```mikrotik
        /ppp secret add name=testuser password=testpass profile=radius-ppp service=pppoe
        /interface pppoe-server server add interface=ether-3 service-name=pppoe-server1 default-profile=radius-ppp
        ```
        **Parameter Explanation for `/ppp secret add`:**
        | Parameter    | Explanation                                                                     | Example        |
        |--------------|---------------------------------------------------------------------------------|----------------|
        | `name`       | Username for the PPP connection.                                               | `testuser`     |
        | `password`   | Password for the PPP connection.                                               | `testpass`     |
        | `profile`    | Name of the PPP profile to use.  (This is our radius profile).                                   | `radius-ppp`    |
        | `service`    |  Service type for this user (pppoe, pptp, etc).                                                 | `pppoe`      |

        **Parameter Explanation for `/interface pppoe-server server add`:**
        | Parameter    | Explanation                                                                     | Example           |
        |--------------|---------------------------------------------------------------------------------|-------------------|
        | `interface`  | Interface on which to listen for PPP connections                                    | `ether-3`         |
        | `service-name`| Service Name to use for this server.                                             | `pppoe-server1`   |
        | `default-profile` | Default profile to apply for all new connections.                                   |  `radius-ppp`   |
    *   **Action (Winbox GUI):**  Go to `PPP -> Secrets`, add a new entry, set name to `testuser`, password to `testpass` profile to `radius-ppp` and service to `pppoe`.
                                      Then go to `Interfaces -> PPPoE Servers` and create a new interface. Set the Interface to `ether-3` and the `service-name` to `pppoe-server1` and the `default-profile` to `radius-ppp`.
    *   **After:** A PPP user account is created and a PPPoE server is enabled, listening for connections on `ether-3`.
     *   **Output Example (`/ppp secret print` and `/interface pppoe-server server print` after config):**
        ```
        Flags: X - disabled, I - invalid
        #   NAME    PROFILE   SERVICE
        0   testuser radius-ppp pppoe

        Flags: X - disabled, I - invalid, R - running
        #   INTERFACE  MAX-M TU  SERVICE-NAME     MAX-MRU   DEFAULT-PROFILE  KEEP-ALIVE-TIMEOUT
        0   ether-3    1480  pppoe-server1          1480      radius-ppp         10
        ```

## Complete Configuration Commands:

```mikrotik
/ip address
add address=45.61.251.1/24 interface=ether-3
/interface ethernet
set ether-3 enabled=yes

/radius
add address=192.168.10.10 secret=mysecret service=ppp timeout=3

/ppp profile
add name=radius-ppp local-address=45.61.251.1 remote-address=45.61.251.2-45.61.251.254 use-encryption=yes only-one=yes change-tcp-mss=yes use-radius=yes

/ppp secret add name=testuser password=testpass profile=radius-ppp service=pppoe
/interface pppoe-server server add interface=ether-3 service-name=pppoe-server1 default-profile=radius-ppp

```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot reach the RADIUS server (firewall blocking, incorrect IP, server down).
    *   **Solution:** Use `ping 192.168.10.10` from the MikroTik to check basic connectivity. Check the MikroTik firewall rules and make sure there is no blocking rule. Also, verify the RADIUS server is up and listening on the correct IP/port.  Verify the `secret` matches on the router and radius server.
*   **Incorrect Shared Secret:**
    *   **Problem:** The shared secret configured on the MikroTik does not match the one on the RADIUS server.
    *   **Solution:** Double-check the `secret` parameter in the `/radius` configuration.  Be aware that this is case sensitive.
*   **RADIUS Service Mismatch:**
    *   **Problem:** The `service` parameter in the `/radius` configuration does not match the service used for the authentication, i.e. setting to dhcp instead of ppp.
    *   **Solution:** Ensure `service=ppp` in your RADIUS setup if you are authenticating with a PPP based service like PPPoE.
*   **Profile Settings Mismatch:**
    *   **Problem:** Incorrect profile settings can prevent the authentication flow from working.  Missing `use-radius=yes` will mean the system wont attempt radius authentication.
    *   **Solution:** Review the `ppp profile print` command and ensure that `use-radius=yes` and any specific requirements for your Radius server setup.
*   **Incorrect Radius Attributes**
    * **Problem:** Some radius servers require special vendor specific attributes to allow the connection.
    * **Solution:** Use the `/tool radius print detail` to see what attributes are being sent from the radius server.  Then use the `/ppp profile` advanced attributes setting to setup the attributes from your radius server.
*   **High CPU Usage:**
    *   **Problem:**  Too many simultaneous RADIUS requests or a complex setup can lead to high CPU usage.
    *   **Solution:** Monitor CPU usage via `/system resource monitor`.  Optimize the setup or consider upgrading to a more powerful MikroTik if needed.  Ensure all user connections are correctly closed when not used.
*   **RADIUS server is slow**
    *   **Problem:** If the radius server is slow, this can lead to connections taking a long time.  This is usually a problem on the radius server.
    *   **Solution:** Use the `/tool radius print detail` to identify the round trip time.  Look at performance of the radius server itself.  Use a radius server that is local to the network.
* **Security Issues**
    * **Problem:** Using insecure default settings (like no encryption or shared password) can lead to easy attacks.
    * **Solution:** Be sure to use encryption for all PPP connections, and only store shared passwords securely.

## Verification and Testing Steps:

1.  **Ping Test:** From another host in the `45.61.251.0/24` network, try to ping the MikroTik on `45.61.251.1`. This checks basic network reachability to ensure that at the very basic level, routing is working.
2.  **PPPoE Connection:** Use a PPPoE client (e.g., built-in OS PPPoE client) connected to `ether-3` and try to establish a connection. Use the `testuser` / `testpass` credentials defined earlier. Check if the radius is being used by doing `/tool radius print detail` and attempt a connection, and monitor the output.
3. **View live logs** Use `/log print where topics~"radius,ppp"` to show radius and ppp related logs in real time. This will assist with troubleshooting.
4. **Radius Server logs** Review the logs from the radius server itself, these will show authentication attempts, and any failures.
5.  **`/tool radius print detail`:** This command is very useful to check details about the Radius server, including the last authentication status and round trip time.

## Related Features and Considerations:

*   **Hotspot:** The RADIUS integration can be used with the MikroTik hotspot feature for user authentication in public Wi-Fi networks.
*   **DHCP Server:** The DHCP server can use RADIUS to provide IP address assignments to specific users.
*   **Accounting:** RADIUS can also be used for accounting, allowing you to track usage and statistics.
*   **Dynamic VLANs:** RADIUS can return VLAN information to place users into specific VLANs based on authentication information.
*   **Rate Limiting:** Using RADIUS you can provide per-user rate limiting using RADIUS attributes sent to the MikroTik.
*   **RouterOS 7.x Considerations**:
    *   The CLI syntax and functionality remain very similar. However, RouterOS 7.x introduces significant improvements in areas such as security and logging.
    *   The `/ppp` area received some changes with regards to IP Pools, and you should be aware if you are using those.
    *   The firewall area is significantly improved and more advanced in 7.x.

## MikroTik REST API Examples (if applicable):

While the primary configuration is often done through CLI or Winbox, here's a theoretical example to manage RADIUS servers via MikroTik REST API. This is a simplified example.

*   **API Endpoint:** `/radius`

*   **Request Method:** `POST` (for adding) or `PUT` (for editing), `DELETE` for deleting.

*   **Example JSON Payload (Adding):**

    ```json
    {
      "address": "192.168.10.10",
      "secret": "mysecret",
      "service": "ppp",
      "timeout": "3"
    }
    ```

*   **Request Method:** `GET` (for listing), with optional parameters to select specific radius servers.
 * **Response (Successful addition/edit):**

   ```json
    {
      "message": "Successfully updated radius server",
      "id": 0
    }
   ```
 * **Response (Error):**

    ```json
    {
      "message": "Error: Address already in use",
      "error": true
    }
    ```

*   **Request Method:** `DELETE` (for deleting)
 *   **Example JSON Payload (Delete):**
    ```json
    {
      ".id": "0"
    }
    ```

*   **Response (Successful delete):**

   ```json
   {
    "message": "Successfully deleted radius server",
    "status": "OK"
    }
   ```

*   **Note:**
    *   The API requires proper authentication and authorization (not shown for brevity).
    *   Error handling should check for non-200 responses and parse the JSON for error messages.
    *   The `.id` field is used for editing or deleting radius server entries. Use the GET method to find the `id` first.
   * RouterOS API is constantly being updated, refer to the official documentation for the most up-to-date information.

## Security Best Practices:

*   **Strong Shared Secret:** Use a strong, randomly generated shared secret.
*   **Encryption:** Always enable encryption on the PPP connections for secure data transmission and authentication.
*   **Firewall:** Restrict access to the RADIUS server to only the trusted IPs.
*   **Regular Updates:** Keep your MikroTik RouterOS updated to the latest stable version.
*   **Password Policies:** Enforce strong password policies for users connecting to the network.
*   **Rate Limiting:** Limit connections from each user to mitigate resource exhaustion issues.
* **Monitor** Regularly monitor connections and user logs for any suspicious activity.
* **Access Control** Restrict access to the radius configuration only to trusted users.

## Self Critique and Improvements:

*   **Dynamic Configuration:** This configuration is relatively static.  In a real-world ISP environment you would probably tie this into a database driven config for automated user creations, etc.
*   **Logging:** Detailed logging of RADIUS requests can be more helpful for troubleshooting. Configure separate log files for RADIUS activities.
*   **Advanced RADIUS:** This is a basic setup.  More advanced radius attribute configurations could be included such as CoAs, session management.
*   **Multi Factor Authentication (MFA):** Using MFA can improve the security.  While not directly supported in RouterOS, this could be done at the Radius server itself.
*   **Redundancy:** High availability for the radius server is a must in any real-world isp scenario, consider redundant servers and/or load balancing.
*   **Real-world user management**: This configuration uses a single username/password, in reality this data would come from a central database, with user accounts and details configured there.

## Detailed Explanation of Topic

**RADIUS (Remote Authentication Dial-In User Service):**
RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network.

*   **Authentication:** Verifies the identity of a user.
*   **Authorization:** Determines what resources or services the user is allowed to access.
*   **Accounting:** Tracks usage data, such as connection time, bandwidth, etc.

**How RADIUS Works:**

1.  A user attempts to connect to the network via a NAS (Network Access Server) device (e.g., the MikroTik Router in this scenario).
2.  The NAS sends an `Access-Request` to the RADIUS server with the user's credentials.
3.  The RADIUS server authenticates the user against its database or other sources.
4.  The RADIUS server sends back an `Access-Accept` if the authentication is successful, or `Access-Reject` if it fails.  The `Access-Accept` response may include attributes that specify limits, VLANs, etc.
5. The NAS then either allows or rejects the user's access based on the RADIUS response.
6. The NAS sends accounting messages to the radius server when a connection starts and stops.

## Detailed Explanation of Trade-offs:

* **Local Authentication vs. RADIUS:**
    *   **Local:** Simple setup, but it is hard to scale for more than a few users. Local configuration is only on the local router, which means settings can vary from router to router.
    *   **RADIUS:** More complex setup, more scalable, better security with centralized authentication, but can create a single point of failure for the authentication if not managed correctly. It is ideal for a large number of users and requires the availability of a radius server.
*   **Single RADIUS Server vs. Redundant Servers:**
    *   **Single:** Easier to manage, single point of failure.
    *   **Redundant:**  More complex setup, high availability and improved uptime but potentially increased cost and setup.
*   **PPP Profiles:**
    *   **Using Profiles:** Easier management of multiple users, consistent config with less repetition
    *   **Not Using Profiles:** Difficult to manage and change settings, not recommended.
*   **Encryption vs No Encryption**
    *   **Encryption** More overhead, but much better security.
    *   **No Encryption:** Minimal overhead, very insecure. Not recommended.
* **RADIUS Attributes:**
    * **Using Attributes** Fine-grained control over each user.  Ability to set per user limits, VLANs, etc.
    * **Not Using Attributes:** Less control, all users get same access.

## Configuration for Specific RouterOS Versions:

This configuration is primarily designed for RouterOS 6.48, with notes on 7.x differences.

* **RouterOS 6.48:** All configurations and parameters are fully supported.
*   **RouterOS 7.x:** The commands will generally be the same, but there may be subtle differences in how specific features work or how they are configured. For example, there were changes to the PPP settings, IP pools, firewall and more, if you are running a newer RouterOS you should check these for any possible changes.

This detailed documentation covers RADIUS configuration in a MikroTik environment, with security practices, testing steps, and troubleshooting guides.  It should help you to understand the configuration, and identify any possible issues.
