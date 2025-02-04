Okay, let's dive into a detailed configuration for PPP AAA on a MikroTik router, specifically targeting a hotspot network scenario on RouterOS 7.11. We'll focus on using RADIUS for authentication, authorization, and accounting.

## Scenario Description:

This scenario involves a hotspot network where users connect to a MikroTik router via PPP (specifically PPPoE or PPTP), and their authentication, authorization, and accounting (AAA) are handled by an external RADIUS server. This allows for centralized user management, accounting, and potentially more complex access control policies. We are configuring this on a router using ether-39 as its WAN interface, serving the subnet 186.132.178.0/24.

## Implementation Steps:

Here's a step-by-step guide, with examples for both the CLI and Winbox GUI, illustrating the before and after state of configuration after each step. We assume your basic network is configured correctly and you have a reachable RADIUS server already set up.

**1. Step 1: Configure the RADIUS Server**

   *   **Purpose:** Add the RADIUS server details to the MikroTik router. This allows it to communicate with the RADIUS server for authentication.
   *   **Before:** The RADIUS server list is empty or does not contain the server we need.
   *   **CLI Example:**

        ```mikrotik
        /radius
        add address=192.168.88.10 secret="supersecret" service=ppp timeout=10s
        print
        ```

    *   **Winbox GUI:** Go to `RADIUS` in the left-hand menu.  Click the plus sign (+).  Enter the server's IP address (`Address`), the shared secret (`Secret`), and select `ppp` for the `Service`. Set the `Timeout` if needed (default is 3 seconds, we set to 10s). Click Apply and OK.

    *   **After:** The RADIUS server is listed in `/radius print`. The configuration will look similar to:

        ```mikrotik
        Flags: X - disabled
        #   ADDRESS         SECRET       SERVICE   TIMEOUT     SRC-ADDRESS  AUTHENTICATION PORT ACCOUNTING PORT
        0   192.168.88.10   supersecret    ppp         10s             <auto>       1812            1813
        ```
    *   **Explanation:**
        *   `address`: The IP address of your RADIUS server.
        *   `secret`: The shared secret key used for communication with the RADIUS server. This MUST match the secret configured on your RADIUS server.
        *   `service`:  Specifies which services should use this RADIUS server. In our case it's 'ppp'.
        *  `timeout`: Time to wait before considering the RADIUS server as unreachable.

**2. Step 2: Enable PPP Server on the Interface**

   *   **Purpose:** Start the PPP server (PPPoE or PPTP, for example) on the interface to accept incoming connections. We'll use PPPoE for this example.

   *   **Before:** No PPP server is configured on the chosen interface.

   *   **CLI Example:**
        ```mikrotik
        /interface pppoe-server server
        add service-name=hotspot-pppoe interface=ether-39 max-mtu=1480 max-mru=1480 disabled=no authentication=pap,chap,mschap1,mschap2 keepalive-timeout=60
        print
        ```

   *   **Winbox GUI:** Go to `PPP` -> `PPPoE Servers` tab. Click the plus sign (+). Choose the interface `ether-39`, and set the service-name (e.g., 'hotspot-pppoe'), and select `pap, chap, mschap1, mschap2` for authentication. Set `max-mtu` and `max-mru`.  Click Apply and OK.
   *   **After:** A PPPoE server instance is active on the specified interface (`ether-39`). A sample result of `print` command would be similar to:

        ```mikrotik
        Flags: X - disabled, I - invalid
        #    INTERFACE   SERVICE-NAME MAX-MTU MAX-MRU KEEP-ALIVE-TIMEOUT  MRU-LIMIT   ONE-SESSION    MAX-VP MAX-VPTS  AUTHENTICATION
        0    ether-39    hotspot-pppoe 1480    1480    60s                 disabled    disabled         2      8     pap,chap,mschap1,mschap2
        ```
   *   **Explanation:**
        *   `interface`: The interface where PPPoE server will listen for incoming connections (in our case, `ether-39`).
        *   `service-name`: The service name clients should use to connect.
        *   `max-mtu`: Maximum Transmission Unit for PPP connections.
        *   `max-mru`: Maximum Receive Unit for PPP connections.
        *  `authentication`: List of authentication methods to use.
        *   `keepalive-timeout`:  Timeout for PPP keepalive messages.

**3. Step 3: Configure the PPP Profile for RADIUS AAA**

   *   **Purpose:** Configure a PPP profile that uses RADIUS for authentication, authorization, and accounting.
   *   **Before:** PPP profiles default to local authentication.
   *   **CLI Example:**
        ```mikrotik
        /ppp profile
        add name=radius-ppp-profile use-encryption=yes only-one=yes local-address=186.132.178.1 remote-address=hotspot-pool use-radius=yes change-tcp-mss=yes
        print
        ```

   *   **Winbox GUI:** Go to `PPP` -> `Profiles` tab. Click the plus sign (+). Name the profile `radius-ppp-profile`. Enable `Use Encryption`, `Only One`, set `local-address` to `186.132.178.1`, and `remote-address` to `hotspot-pool`. Tick `Use Radius` and `Change TCP MSS`.  Click Apply and OK.

   *   **After:** A PPP profile named `radius-ppp-profile` is created and ready to be used by the PPP server. The `print` command output should look like:

        ```mikrotik
        Flags: * - default
        #   NAME               USE-ENCRYPTION  ONLY-ONE  ADDRESS-POOL LOCAL-ADDRESS REMOTE-ADDRESS CHANGE-TCP-MSS  USE-RADIUS
        0   default                no         no       <none>        10.0.0.1     <none>          no                no
        1   radius-ppp-profile    yes           yes     <none>      186.132.178.1 hotspot-pool        yes            yes
        ```

   *   **Explanation:**
        *   `name`: The name of the profile.
        *   `use-encryption`: Enables encryption for PPP connections.
        *   `only-one`: Allows only one connection per user.
        *   `local-address`: The IP address assigned to the MikroTik's side of the PPP connection.
        *   `remote-address`: The IP address pool from which the PPP clients will get IP addresses.
        *   `use-radius`: Enables RADIUS for authentication and accounting for this profile.
        *   `change-tcp-mss`: Enables TCP MSS clamping.

**4. Step 4: Assign the PPP Profile to the PPP Server**

   *   **Purpose:** Associate the created PPP profile with the PPPoE server so that all new connections through that server use the configured RADIUS AAA.
    *   **Before:** The PPPoE server is using the default profile
    *   **CLI Example:**
        ```mikrotik
        /interface pppoe-server server
        set 0 profile=radius-ppp-profile
        print
        ```
   *   **Winbox GUI:** Go back to `PPP` -> `PPPoE Servers` tab. Select the PPPoE server instance (usually the first on the list). In the `Profile` dropdown, select `radius-ppp-profile`. Click Apply and OK.
    *  **After:** The PPPoE server is using the radius-ppp-profile profile.
        ```mikrotik
        Flags: X - disabled, I - invalid
        #    INTERFACE   SERVICE-NAME MAX-MTU MAX-MRU KEEP-ALIVE-TIMEOUT  MRU-LIMIT   ONE-SESSION    MAX-VP MAX-VPTS  AUTHENTICATION   PROFILE
        0    ether-39    hotspot-pppoe 1480    1480    60s                 disabled    disabled         2      8     pap,chap,mschap1,mschap2 radius-ppp-profile
        ```
    *  **Explanation:**
        *   `profile`:  The name of the profile to be used for authentication and IP address assignment.

**5. Step 5: Define IP Pool for Hotspot Users**

   *   **Purpose:** Define an IP address pool that will be used to assign IP addresses to the hotspot clients.
   *   **Before:** There is no IP pool for the hotspot clients.
   *   **CLI Example:**
        ```mikrotik
        /ip pool
        add name=hotspot-pool ranges=186.132.178.2-186.132.178.254
        print
        ```

   *   **Winbox GUI:** Go to `IP` -> `Pool`. Click the plus sign (+). Set the `Name` to `hotspot-pool` and the `Ranges` to `186.132.178.2-186.132.178.254`. Click Apply and OK.
   *   **After:** The IP address pool is defined.
        ```mikrotik
        Flags: * - default
        #   NAME         RANGES                                   NEXT-POOL
        0 * default      10.0.0.2-10.0.0.254
        1   hotspot-pool 186.132.178.2-186.132.178.254
        ```
   *   **Explanation:**
        *   `name`:  The name of the IP pool.
        *   `ranges`:  The IP address range assigned from the pool.

## Complete Configuration Commands:
```mikrotik
/radius
add address=192.168.88.10 secret="supersecret" service=ppp timeout=10s
/interface pppoe-server server
add service-name=hotspot-pppoe interface=ether-39 max-mtu=1480 max-mru=1480 disabled=no authentication=pap,chap,mschap1,mschap2 keepalive-timeout=60
/ppp profile
add name=radius-ppp-profile use-encryption=yes only-one=yes local-address=186.132.178.1 remote-address=hotspot-pool use-radius=yes change-tcp-mss=yes
/interface pppoe-server server
set 0 profile=radius-ppp-profile
/ip pool
add name=hotspot-pool ranges=186.132.178.2-186.132.178.254
```

**Explanation of each parameter:** (Also found within the steps)

| Command          | Parameter         | Description                                                                             |
|------------------|-------------------|-----------------------------------------------------------------------------------------|
| `/radius add`    | `address`         | IP address of the RADIUS server.                                                         |
|                  | `secret`          | The shared secret key used to authenticate with the RADIUS server.                     |
|                  | `service`         | The service this RADIUS server will be used for (`ppp` in our case).                                  |
|                  | `timeout`         | Time to wait for a RADIUS response before timing out (in seconds).                  |
| `/interface pppoe-server server add`| `service-name` |  The service name advertised by this server. |
|                  | `interface`       | The interface that will listen for PPPoE connections.  |
|                  | `max-mtu`         | Maximum Transmission Unit for PPP connections.                                           |
|                  | `max-mru`         | Maximum Receive Unit for PPP connections.                                            |
|                  | `disabled`        |  Is the server enabled (no/yes).  |
|                  | `authentication`  |  List of supported authentication protocols.  |
|                  | `keepalive-timeout`| Timeout for PPP keepalive messages.              |
| `/ppp profile add`  | `name`            | The name of the PPP profile.                                                            |
|                   | `use-encryption` | Enable or disable encryption.                                                              |
|                   | `only-one`        | Allow only one simultaneous PPP connection per user.                                   |
|                   | `local-address`  | The IP address assigned to the MikroTik's side of the PPP connection.                |
|                   | `remote-address` | IP pool name for assigning IP addresses to the client.                                |
|                   | `use-radius`      | Enable RADIUS for authentication, authorization, and accounting.                    |
|                   | `change-tcp-mss`  | Adjust TCP MSS.                                                                        |
|`/interface pppoe-server server set`| `profile` | Assign the specified profile to this server.  |
| `/ip pool add`     | `name`            | The name of the IP address pool.                                                        |
|                   | `ranges`          | The IP address ranges to assign from this pool.                                         |

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router can't communicate with the RADIUS server due to network issues, incorrect IP address, or firewall rules.
    *   **Solution:**
        *   Verify connectivity with `ping 192.168.88.10` (replace with your RADIUS server IP).
        *   Check firewall rules on both the MikroTik and RADIUS server.
        *   Ensure the RADIUS server is listening on UDP ports 1812 (authentication) and 1813 (accounting).
*   **Incorrect RADIUS Secret:**
    *   **Problem:** The shared secret on the MikroTik and RADIUS server do not match.
    *   **Solution:** Double-check that the secret configured in `/radius` on the MikroTik matches the secret configured on the RADIUS server.
*   **Mismatched Authentication Protocols:**
    *   **Problem:** The authentication methods supported by the MikroTik and RADIUS server may not match.
    *   **Solution:** Check the authentication protocols configured on both devices and ensure they have at least one in common, such as `pap,chap,mschap1,mschap2`.
*   **IP Pool Exhaustion:**
    *   **Problem:** The configured IP pool is exhausted, and new users cannot get an IP address.
    *   **Solution:** Expand the range in the `/ip pool` configuration. Ensure the IP pool range is large enough for the expected number of users.
*   **Incorrect DNS Configuration:**
    *   **Problem:** Users can connect but may not be able to access the internet due to missing or incorrect DNS settings.
    *   **Solution:** Ensure you have proper DNS configuration in `/ip dns` on your MikroTik device, and consider pushing DNS servers to the PPP clients via RADIUS.
*   **Resource issues:** If the number of clients is too high, the device may experience high CPU and/or memory usage.
    *   **Solution:** Monitor CPU and memory usage, and consider upgrading hardware or limiting the number of clients.

*   **Security Issues**: If you enable insecure authentication methods, such as PAP, your credentials are sent in plaintext, and are vulnerable to sniffing.
    *   **Solution:** Use encrypted authentication methods, such as mschap2.

## Verification and Testing Steps:

1.  **RADIUS Server Reachability:** Ping the RADIUS server from the MikroTik router:
    ```mikrotik
    /ping 192.168.88.10
    ```
2.  **PPPoE Server Status:** Check if the PPPoE server is running correctly:
    ```mikrotik
    /interface pppoe-server server print
    ```
3.  **Attempt a PPP Connection:** Try connecting a client using PPPoE credentials configured in the RADIUS server.
4.  **Check Active PPP Connections:**
    ```mikrotik
    /ppp active print
    ```
5.  **Monitor RADIUS Logs:** Use the MikroTik `log` command (or Winbox) to check for RADIUS-related errors, both on the router and on the RADIUS server.
    ```mikrotik
    /log print topic=radius
    ```
6. **Use Torch tool on the interface and the RADIUS server:** Monitor traffic related to RADIUS on the MikroTik:
  ```mikrotik
  /tool torch interface=ether-39 port=1812,1813
  ```
  And monitor traffic received on the RADIUS server to ensure packets are arriving, and the RADIUS server is responding.
7.  **Check assigned IP addresses:** Ensure client is assigned IP addresses from correct pool, and has access to internet, and is assigned correct DNS settings.

## Related Features and Considerations:

*   **Hotspot Feature:** Use MikroTik's Hotspot feature for captive portal functionality, which can be combined with RADIUS for a more comprehensive solution.
*   **User Profiles in RADIUS:** The RADIUS server can return specific user-related attributes like bandwidth limits, QoS policies, and access time.
*   **Rate Limiting:** Combine with `/queue simple` or `/queue tree` to implement rate limiting and QoS for clients based on policies set on the RADIUS server.
*   **Accounting:** Set up proper accounting on the RADIUS server to track client usage and generate reports.
*   **Security:** Implement firewall rules to restrict access to specific network resources after user authentication.
*   **DNS Resolution:**  Ensure clients are correctly resolving hostnames by either configuring the MikroTik router as a DNS server or pushing DNS servers via DHCP or RADIUS.

## MikroTik REST API Examples (if applicable):

While the MikroTik REST API does not have explicit endpoints to manage all components of the configuration we just setup. We can use it to modify some values.

**1. Creating a new Radius Server Entry:**
   *   **API Endpoint:** `/radius`
   *   **Method:** `POST`
   *   **Example JSON Payload:**
        ```json
        {
          "address": "192.168.88.11",
          "secret": "anothersecret",
          "service": "ppp",
          "timeout": "5s"
        }
        ```
   *   **Expected Response (Success):**
        ```json
        {
            "message": "added",
            ".id": "*5"
        }
        ```
   *   **Expected Response (Failure):**
        ```json
        {
            "message": "invalid value of address",
            "error": true,
            "details": "invalid value of address, it should be IP address"
        }
        ```
   *  **Explanation:**
        *   `address`: The IP address of your RADIUS server.
        *   `secret`: The shared secret key used for communication with the RADIUS server.
        *   `service`:  Specifies which services should use this RADIUS server. In our case it's 'ppp'.
        *  `timeout`: Time to wait before considering the RADIUS server as unreachable.

**2. Modifying an existing Radius Server Entry:**

   *   **API Endpoint:** `/radius/*<id>`  (Replace `<id>` with the ID of the RADIUS server you want to modify, e.g. `0` or `*5`)
   *   **Method:** `PUT`
   *   **Example JSON Payload:**
        ```json
        {
          "timeout": "15s"
        }
        ```
   *   **Expected Response (Success):**
        ```json
         {
          "message": "changed",
           ".id":"*5"
         }
        ```
   *   **Expected Response (Failure):**
        ```json
          {
              "message": "invalid value of timeout",
              "error": true,
              "details": "invalid value of timeout, it should be time"
           }
        ```
   *  **Explanation:**
        *   `.id`: ID of the radius entry to be changed.
        *  `timeout`: The timeout for the radius server.
    **3. Delete a Radius Entry**
    *  **API Endpoint:** `/radius/*<id>`  (Replace `<id>` with the ID of the RADIUS server you want to delete, e.g. `0` or `*5`)
    *  **Method:** `DELETE`
    *   **Expected Response (Success):**
         ```json
         {
             "message":"removed",
             ".id":"*5"
         }
         ```
    *  **Expected Response (Failure):**
        ```json
        {
            "message":"not found",
            "error":true,
            "details":"not found"
        }
        ```
        **Explanation:**
          *  `.id`: ID of the entry to be deleted.

**Note:**
* Error handling for the REST API calls should involve checking for the `error` key in the JSON response. If it exists and is `true`, further examine the `details` field.
* These are simplified examples. Always validate input data, check for errors, and potentially retry API calls if they fail due to network issues.

## Security Best Practices

*   **Use Strong Shared Secret:** Use a long, random, and complex shared secret for RADIUS communication. Never use default values.
*   **Encrypt PPP Connections:** Enable encryption (`use-encryption=yes` in PPP profile) to prevent eavesdropping on PPP authentication data and user traffic.
*   **Use MS-CHAPv2:** Prioritize MS-CHAPv2 for authentication, as it offers better security over older methods like PAP and CHAP.
*   **Firewall Rules:** Implement strict firewall rules to control access from the hotspot network to your internal network and other sensitive resources.
*   **Limit Access to RADIUS:**  Restrict access to your RADIUS server to only the necessary IP addresses and ports.
*   **Regularly Review Configuration:** Regularly review your configuration to ensure there are no vulnerabilities or misconfigurations.
*   **Keep RouterOS Updated:** Keep your MikroTik RouterOS updated to patch security vulnerabilities.

## Self Critique and Improvements

*   **Complexity:** This configuration is more complex than basic setups and requires careful planning and a strong understanding of both the MikroTik and RADIUS concepts.
*   **RADIUS Server Configuration:** We assume that the RADIUS server is correctly set up and functioning. In the real world, this is one of the most critical components and can require its own detailed troubleshooting.
*   **Flexibility:** While the current configuration is geared toward PPPoE, we can extend it to PPTP or L2TP as well.
*   **Scalability:** The configuration should scale for smaller and medium networks. For a very large ISP scale setup, additional fine tuning would be needed, especially for resource management.
*   **Logging:**  Detailed logging is crucial for troubleshooting in this setup. We should ensure that all components log their activity, making debugging issues easier.
*   **Advanced RADIUS Attributes:** The setup could be extended further by using more advanced RADIUS attributes (e.g., VLAN assignment, specific QoS settings, etc.).
*   **Automation:** Using tools like Ansible or scripting would greatly help managing and deploying these changes on many routers.

## Detailed Explanations of Topic:

**PPP (Point-to-Point Protocol):**  PPP is a widely used protocol for establishing direct connections between two network nodes. It's commonly used for dial-up, VPN, and direct connections. In the context of MikroTik routers, PPP can be configured via different methods: PPPoE (PPP over Ethernet), PPTP (Point-to-Point Tunneling Protocol), and L2TP (Layer 2 Tunneling Protocol).
* **PPPoE (PPP over Ethernet):**  Encapsulates PPP frames inside Ethernet frames. This is a popular solution, typically used by internet service providers (ISPs).
* **PPTP (Point-to-Point Tunneling Protocol):** Creates an encrypted tunnel over IP. It's an older VPN protocol, with some known security limitations.
* **L2TP (Layer 2 Tunneling Protocol):** Uses UDP to encapsulate PPP frames, and is generally used with IPSec encryption for secure VPN tunnels.
**AAA (Authentication, Authorization, and Accounting):** AAA is a security framework for managing user access.
*   **Authentication:** Verifying the identity of a user trying to connect to the network.
*   **Authorization:** Determining what a user is permitted to do after authentication.
*   **Accounting:** Tracking network usage.
**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a protocol that centralizes AAA functions. It uses a client/server model. The MikroTik acts as a RADIUS client, forwarding AAA requests to the RADIUS server. The RADIUS server, in turn, performs the necessary checks and sends the result back to the client.

## Detailed Explanation of Trade-offs:

* **Local Authentication vs. RADIUS:** Local authentication (configuring users directly on the MikroTik router) is simpler for small deployments. RADIUS is more scalable and easier to manage in larger or more complex networks.
* **Encryption Methods (PAP, CHAP, MS-CHAPv1, MS-CHAPv2):** PAP sends passwords in plaintext, making it insecure. CHAP is more secure but vulnerable to replay attacks. MS-CHAPv1 is also susceptible to weaknesses. MS-CHAPv2 is the most secure and the recommended option.
*   **PPPoE vs. PPTP/L2TP:** PPPoE is generally easier to set up in a LAN-based environment, as it's the native method for many cable and DSL technologies, while L2TP/IPSec is usually preferred for secure VPN connections across the internet. PPTP is very old and is generally not secure to use.
* **Simple Queue vs. Tree Queue:** Simple queues are easier to configure for basic rate limiting. Queue trees offer more control and flexibility for complex QoS requirements but can be more challenging to set up.

By considering these trade-offs, you can tailor your configuration to meet the specific needs of your network.

## Configuration for Specific RouterOS Versions:

This configuration is targeting RouterOS 7.11, but it is broadly compatible with RouterOS 6.48 and 7.x series. Some older commands or parameters might have been deprecated in newer RouterOS versions, but the commands used here are generally stable. If you encounter issues, refer to the MikroTik documentation for your exact RouterOS version to see if there are any syntax changes or deprecated features.

This detailed configuration and explanation should give you a solid starting point for implementing a PPP AAA setup on your MikroTik router. Remember to adjust configurations according to your specific network needs and security policies.
