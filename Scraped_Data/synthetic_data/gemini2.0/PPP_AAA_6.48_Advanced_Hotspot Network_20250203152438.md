Okay, let's craft some detailed documentation on configuring PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik RouterOS device (version 6.48 and compatible with 7.x) within a hotspot network context, focusing on the specified subnet and interface.

## Scenario Description:

We are setting up a hotspot network where users connect via PPP (Point-to-Point Protocol), typically using PPPoE (Point-to-Point Protocol over Ethernet). To manage and control access, we need to implement AAA. This will involve authenticating users against a RADIUS server, authorizing them for access, and potentially accounting for their session usage. Our hotspot network will be operating on the 174.107.110.0/24 subnet, and we'll configure the PPP services to use the `ether-15` interface as the primary point of contact. This setup is typical for managed Wi-Fi access points, internet kiosks or hospitality businesses.

## Implementation Steps:

Here's a step-by-step guide to configure PPP AAA on your MikroTik router:

### 1. Step 1: Configure the IP Address on the Interface

* **Before:** The interface `ether-15` may or may not have an IP address. We want it to belong to our desired subnet.
* **Action:** We need to assign an IP address within our subnet to the `ether-15` interface. This is going to be our interface for all PPPoE client sessions, this IP can be the gateway for the subnet we are working on.

   * **CLI Command:**
     ```mikrotik
     /ip address add address=174.107.110.1/24 interface=ether-15 network=174.107.110.0
     ```
     *   **Parameter Explanation:**
         *   `address`: IP address and subnet mask for the interface.
         *   `interface`: The name of the interface to configure.
         *   `network`: The network address. This field will be automatically set if not provided.
   * **Winbox GUI:**
       * Go to "IP" -> "Addresses"
       * Click the "+" button.
       * In the "Address" field, enter `174.107.110.1/24`.
       * Select `ether-15` in the "Interface" dropdown.
       * Click "Apply" and "OK".
* **After:** The interface `ether-15` has IP address `174.107.110.1/24` assigned.
* **Effect:** The router can now send and receive packets on the 174.107.110.0/24 subnet via `ether-15`.

### 2. Step 2: Configure PPP Server (PPPoE)

* **Before:** The PPP server is not configured, and no users can connect.
* **Action:** We will enable a PPPoE server on the interface `ether-15`.

   * **CLI Command:**
      ```mikrotik
      /ppp server pppoe set enabled=yes interface=ether-15 service-name="MyHotspot"
      ```
      *   **Parameter Explanation:**
        *   `enabled`: Whether the PPPoE server is enabled.
        *   `interface`: The interface on which the PPPoE server will listen.
        *   `service-name`: The service name of the PPPoE server, clients should configure this in their configuration to connect.
   * **Winbox GUI:**
        *  Go to "PPP" -> "PPPoE Servers"
        *  Click the "+" button.
        *  Check "Enabled".
        *  Select `ether-15` in the "Interface" dropdown.
        *  Add a service name to the "Service Name" field (e.g. `MyHotspot`).
        *  Click "Apply" and "OK".
* **After:** A PPPoE server listens for incoming connections on `ether-15`.
* **Effect:** Clients can now attempt to establish PPPoE sessions with the router. Note, they will not be authorized until the next step.

### 3. Step 3: Configure RADIUS Client

* **Before:** The router is not connected to a RADIUS server for authentication.
* **Action:** We need to configure the router as a RADIUS client, to authorize our users.

    * **CLI Command:**
       ```mikrotik
       /radius add address=10.10.10.1 secret="sharedsecret" service=ppp timeout=30
       ```
       *  **Parameter Explanation:**
           *   `address`: IP address of the RADIUS server.
           *   `secret`: Shared secret between the router and the RADIUS server. This needs to match the configuration on the RADIUS server.
           *   `service`: The service that will use this RADIUS server for authentication (in this case `ppp`).
           *  `timeout`: Amount of time the router will wait for a RADIUS response.

    * **Winbox GUI:**
        * Go to "RADIUS"
        * Click "+" to add new RADIUS client configuration
        * Add the IP address in the "Address" field (e.g. 10.10.10.1).
        * Add the password into the "Secret" field.
        * Ensure that the Service matches `ppp`
        * Add a timeout (default 30s)
        * Click "Apply" and "OK".
* **After:**  The router will send PPP authentication requests to the specified RADIUS server.
* **Effect:** User login details will be verified by the configured RADIUS server, allowing for centralized authentication.

### 4. Step 4: Enable AAA for PPP

* **Before:** PPP service is not using RADIUS for authentication.
* **Action:** We now configure the router to use RADIUS for authentication.

    * **CLI Command:**
        ```mikrotik
         /ppp profile set default use-encryption=yes only-one=yes local-address=174.107.110.1 remote-address=174.107.110.2-174.107.110.254 use-radius=yes
        ```
        *  **Parameter Explanation:**
            *   `use-encryption`: Enforces encryption in PPP sessions
            *  `only-one`: Only allow one connection per user
            * `local-address`: The address for the client's interface from the server perspective
            * `remote-address`: The dynamic address pool assigned to connected users
            *   `use-radius`: Enables RADIUS for PPP authentication. This is what binds all the other steps together.
   * **Winbox GUI:**
        * Go to "PPP" -> "Profiles"
        * Select the `default` profile.
        * Check `Use Encryption`, check `Only One`.
        * In the "Local Address" field, enter `174.107.110.1`.
        * In the "Remote Address" field, enter `174.107.110.2-174.107.110.254`.
        * Check `Use Radius`.
        * Click "Apply" and "OK".
* **After:** All PPP connections are now authenticated using the RADIUS server.
* **Effect:**  Only users that are configured in the RADIUS server can authenticate and gain access to the network.

## Complete Configuration Commands:

Here are the complete set of commands:

```mikrotik
/ip address
add address=174.107.110.1/24 interface=ether-15 network=174.107.110.0

/ppp server pppoe
set enabled=yes interface=ether-15 service-name="MyHotspot"

/radius
add address=10.10.10.1 secret="sharedsecret" service=ppp timeout=30

/ppp profile
set default use-encryption=yes only-one=yes local-address=174.107.110.1 remote-address=174.107.110.2-174.107.110.254 use-radius=yes
```

## Common Pitfalls and Solutions:

*   **RADIUS Secret Mismatch:**
    *   **Problem:** Clients fail to authenticate because the secret on the router doesn't match the RADIUS server.
    *   **Solution:** Double-check the `secret` parameter in `/radius` configuration. Ensure it's an exact match on both the router and the RADIUS server.
*   **RADIUS Server Unreachable:**
    *   **Problem:** The router cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Verify network connectivity (ping, traceroute).
        *   Check firewall rules on both the router and the server.
        *   Ensure that the RADIUS server is listening on the correct port (usually 1812/udp for authentication).
*   **Incorrect RADIUS Attributes:**
    *   **Problem:**  RADIUS server is configured for different parameters.
    *   **Solution:** Ensure that the RADIUS server is sending the correct attributes for user authorization, like IP address assignments if using DHCP from Radius server.
*  **PPPoE Server Not Listening:**
    * **Problem:** The PPPoE server is enabled but not accepting connections.
    * **Solution:** Verify that the service name matches on both the client and the server and the interface for the PPPoE server is correct. Also ensure that the interface has an IP address assigned to it.
*  **Resource Issues**
    *  **Problem:** Router may be overwhelmed with connections, especially in large hotspots.
    *  **Solution:** Use a more powerful router or introduce connection limits, upgrade router to latest RouterOS version.
*   **Security Issues:**
    *   **Problem:** Weak shared secrets or open access to RADIUS server.
    *   **Solution:** Use strong, randomly generated secrets, limit access to the RADIUS server, and implement strong access control lists on the firewall.

## Verification and Testing Steps:

*   **Connect a PPPoE client:** Attempt to connect from a client device using the service name configured on the router.
*   **Monitor PPP active connections:** Use `/ppp active print` to check active sessions, if a connection is established a new line with the assigned IP should appear.
*   **Use torch tool:** Use `/tool torch interface=ether-15` to verify the communication flow. Check that the router is communicating with the client, and with the RADIUS server.
*   **Use the RADIUS log**: On the RADIUS server side check for authentication successes and failures.
*   **Use the MikroTik Logs:** Verify the logs, `/log print` to check for errors.
*   **Check IP Addresses:** Verify that the clients are getting the configured IP address range from the server, `/ip address print`.

## Related Features and Considerations:

*   **Hotspot Server:** You could use the MikroTik hotspot feature to redirect users to a captive portal before they get full internet access. You would still authenticate with PPP and radius, but get a captive portal page.
*   **Accounting:**  Configure the RADIUS server for accounting to track user session durations, data usage, and other statistics. This can be very useful for rate limiting or billing purposes.
*   **Dynamic IP Assignment:**  You can configure the RADIUS server to return IP addresses dynamically instead of defining them on the router.
*   **VLANs:** Implement VLANs to segregate traffic on the network and improve the security and network performance.
*   **QoS (Quality of Service):** Implement QoS to manage bandwidth usage of your clients.
*   **DHCP Server:** You can complement the PPP server by adding a DHCP server, which can be used if there is no PPP authentication required on the local network.

## MikroTik REST API Examples (if applicable):

While the MikroTik REST API might not be the most performant method for high-volume connection configurations, here are some examples to demonstrate API functionality.

*   **Create a new PPPoE Server configuration:**

    *   **API Endpoint:** `/ppp/server/pppoe`
    *   **Request Method:** POST
    *   **Example JSON Payload:**

        ```json
        {
          "enabled": true,
          "interface": "ether-15",
          "service-name": "MyHotspotAPI"
        }
        ```
    *   **Expected Response (Success):**

        ```json
        {
          "id": "*12",
          "enabled": true,
          "interface": "ether-15",
          "service-name": "MyHotspotAPI",
           "max-mru": 1480,
           "max-mtu": 1480,
           "keepalive-timeout": 10,
           "one-session-per-host": "no",
           "default-profile": "default",
           "authentication": "pap, chap, mschap1, mschap2",
           "max-session-timeout": "00:00:00",
          "comment": ""
        }
        ```
    *   **Error Handling:**
        If any field is missing or wrong, the API call will fail and return a non-200 error code, the body of the response will contain more information about the error.

*   **Retrieve all PPP Server Configurations:**
    *   **API Endpoint:** `/ppp/server/pppoe`
    *   **Request Method:** GET
    *   **Example Response:**
       ```json
       [
         {
           "id": "*0",
           "enabled": true,
           "interface": "ether-15",
           "service-name": "MyHotspot",
            "max-mru": 1480,
            "max-mtu": 1480,
            "keepalive-timeout": 10,
            "one-session-per-host": "no",
            "default-profile": "default",
            "authentication": "pap, chap, mschap1, mschap2",
            "max-session-timeout": "00:00:00",
           "comment": ""
         },
          {
           "id": "*1",
           "enabled": true,
           "interface": "ether-16",
           "service-name": "AnotherHotspot",
            "max-mru": 1480,
            "max-mtu": 1480,
            "keepalive-timeout": 10,
            "one-session-per-host": "no",
            "default-profile": "default",
            "authentication": "pap, chap, mschap1, mschap2",
            "max-session-timeout": "00:00:00",
           "comment": "Another hotspot config"
         }
       ]

       ```

*   **Updating existing PPP Server configurations:**
    *   **API Endpoint:** `/ppp/server/pppoe/*0` (*0 is the object id of the pppoe server configuration)
    *   **Request Method:** PATCH
    *   **Example JSON Payload:**
       ```json
        {
          "enabled": true,
          "service-name": "HotspotRenamed"
        }
        ```
    *  **Expected response:**
         *   Success, if operation completed successfully, `200 OK`
    *  **Error Handling:**
        If any field is missing or wrong, the API call will fail and return a non-200 error code, the body of the response will contain more information about the error.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a complex, randomly generated RADIUS shared secret.
*   **Restrict RADIUS Access:** Configure your firewall to only allow access to the RADIUS port (usually 1812/udp and 1813/udp for accounting) from the MikroTik router, and from internal servers.
*   **Usernames and Passwords:** Do not use default usernames and passwords. Use secure passwords. Enforce password complexity on the RADIUS server.
*   **Encryption:** Always use encryption on PPP sessions to protect the credentials of the clients.
*   **Regular Updates:** Keep your RouterOS version updated to address potential security vulnerabilities.

## Self Critique and Improvements:

This configuration is robust but can be enhanced in a real-world scenario. Here are some areas for improvement:

*   **Centralized User Management:** A dedicated user management interface on the RADIUS server would simplify managing user accounts.
*   **Detailed Accounting:** Expand accounting features to provide more specific reports (per user, per day, etc.).
*   **Dynamic Address Pools:** Use RADIUS attributes to assign dynamic address pools to different user groups.
*   **Scalability:** Plan for scalability, using additional routers and load balancing if needed.
*   **Redundancy:** Implement redundant RADIUS servers to provide uninterrupted service.
*   **Rate limiting:** Implement rate limiting to ensure no user overutilizes the network.
*   **Monitoring System:** Implement a monitoring system (like The Dude) to track usage and any issue on the network.

## Detailed Explanations of Topic:

**PPP AAA (Authentication, Authorization, and Accounting):**

*   **Authentication:** Verifies the identity of the user attempting to connect. In this case, the MikroTik device forwards the user credentials to a RADIUS server for authentication.
*   **Authorization:** Determines what level of access the user has to the network. The RADIUS server can send back attributes to define speed limits, VLAN access, and other parameters.
*   **Accounting:**  Logs user connection details, including connection time, data usage and other statistics. This data can be used for billing, auditing, or tracking.

**RADIUS Protocol:**

*   RADIUS (Remote Authentication Dial-In User Service) is a network protocol that provides centralized authentication, authorization, and accounting for users connecting to a network. RADIUS servers are deployed on one or more physical hosts and are accessed by multiple network access devices.

**PPPoE (Point-to-Point Protocol over Ethernet):**

*   PPPoE is a network protocol that encapsulates PPP frames inside Ethernet frames. It's used to provide authentication and session management over Ethernet networks.

## Detailed Explanation of Trade-offs:

*   **Local vs RADIUS Authentication:**
    *   **Local:** Easier for small setups, but harder to manage centrally for numerous users. Best for small private networks.
    *   **RADIUS:** More complex to configure, but provides better user management, accounting, and scalability for larger networks. Best for larger networks and for providing granular control over each user.
*   **Static vs Dynamic IP Assignment:**
    *   **Static:** Simple, but less flexible. Harder to manage if the network grows.
    *   **Dynamic:** Flexible, can accommodate growing networks. Uses a range of addresses assigned to users when they connect, allowing each user a different IP, but using an internal IP range.
*   **Shared Secret:**
    *   **Weak Secret:** Easy to implement but susceptible to security attacks.
    *   **Strong Secret:** Provides stronger security but can be more difficult to manage (if not using a password manager).
*   **Encryption:**
    * **No encryption:** Easier to implement but user's credentials can be intercepted.
    * **Encryption enabled:** More secure but increases computational overhead (small overhead).

## Configuration for Specific RouterOS Versions:

This configuration is compatible with both RouterOS 6.48 and 7.x. The core commands used are consistent across these versions. However, if using version 7.x there are a few extra commands that could be used.

For RouterOS version 7.x, some parameters have slightly different semantics or features are added. For example:

* `/ppp secret` to create users (instead of relying on the RADIUS user).
*  `/ppp profile` introduces a new `idle-timeout` field which can control the session timeout.
*  `/ppp server set` has new options like `fast-path`, which can improve performance.

**Example of commands specific to 7.x**

```mikrotik
/ppp server pppoe
set  max-mru=1492  max-mtu=1492  fast-path=yes
```
This command will enable fast-path (if available), and increase the MTU and MRU values of the pppoe server to 1492 (the standard).

**Note:** Always review the official MikroTik documentation for the specific RouterOS version to ensure all commands are applicable and understand the possible changes between versions.

This documentation provides a very detailed and comprehensive approach to configuring PPP AAA on a MikroTik router, focusing on the specific parameters provided, and addressing real-world scenarios, potential issues, and enhancements. Remember to always test your configurations thoroughly in a development environment before deploying them in production.
