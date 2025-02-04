Okay, let's craft a comprehensive guide to setting up PPP AAA on a MikroTik router running RouterOS 7.11, targeting an SMB network environment with a subnet of 115.113.134.0/24 on interface ether-0.

## Scenario Description:

This document describes how to configure PPP Authentication, Authorization, and Accounting (AAA) on a MikroTik router. We will use a RADIUS server for handling user authentication for PPPoE connections.  This configuration is relevant for Small to Medium Businesses (SMBs) who want to offer controlled and logged internet access, often seen in scenarios such as guest networks, or managed user access to specific resources, or to connect to an ISP via PPPoE. By using a RADIUS server, we offload authentication and accounting to a central system, improving manageability and scalability. This configuration will be implemented on interface ether-0 with an IP Subnet of 115.113.134.0/24.

## Implementation Steps:

### 1. Step 1: Initial Router Setup and Interface Configuration.

*   **Description**: Before configuring AAA, ensure the router has a basic configuration. This includes a functional interface with the correct IP address and basic network connectivity.
*   **Before Configuration (Assumption):**
    *   RouterOS is freshly installed or has default configurations.
    *   `ether-0` is connected to the network where PPPoE clients will be connecting.
*   **MikroTik CLI Example:**
    ```mikrotik
    /interface ethernet
    set ether-0 name="ether-0"
    /ip address
    add address=115.113.134.1/24 interface=ether-0 network=115.113.134.0
    ```
*   **Winbox GUI:**
    *   Navigate to *Interfaces*.
    *   Select `ether-0`, and rename it to `ether-0`.
    *   Navigate to *IP* -> *Addresses*.
    *   Add `115.113.134.1/24` on `ether-0`.
*   **Effect:**  The `ether-0` interface is prepared with an IP address to host a PPP connection and have general network connectivity. The IP address `115.113.134.1/24` will also be used as a local address for the PPP connection.
*   **After Configuration**: `ether-0` has the IP address 115.113.134.1/24 assigned to it.

### 2. Step 2: Configure the RADIUS Client.

*   **Description:** Configure the MikroTik router as a RADIUS client, pointing to your RADIUS server.
*   **Before Configuration:** No RADIUS server configuration is present.
*   **MikroTik CLI Example:**
    ```mikrotik
    /radius
    add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=30s
    ```
    **Explanation of parameters:**
        *  **`address`**: The IP address of your RADIUS server. Replace `192.168.88.10` with the actual address.
        *  **`secret`**: The shared secret configured on both the RADIUS server and the MikroTik router. Replace `"your_radius_secret"` with the actual secret.
        *  **`service`**: Specifies which service will use this RADIUS server, it should be set to `ppp` here.
        *  **`timeout`**: How long the router will wait for a response from the RADIUS server.
*   **Winbox GUI:**
    *   Navigate to *RADIUS*.
    *   Add a new entry.
    *   Fill in: Address `192.168.88.10`, Secret `"your_radius_secret"`, Service `ppp`, Timeout `30s`
*   **Effect:** The router can now communicate with the RADIUS server for authentication.
*   **After Configuration:** A RADIUS entry is configured, ready to perform AAA.

### 3. Step 3: Configure the PPP Profile for RADIUS.

*   **Description**: Create a PPP profile to use RADIUS for authentication and accounting.
*   **Before Configuration**: No PPP profiles are configured to use RADIUS.
*   **MikroTik CLI Example:**
    ```mikrotik
    /ppp profile
    add name="radius-ppp-profile" use-encryption=yes only-one=no local-address=115.113.134.1 remote-address=115.113.134.2-115.113.134.254 use-radius=yes dns-server=1.1.1.1,8.8.8.8
    ```
    **Explanation of Parameters**
        * **`name`**: A human readable name for the profile, such as `radius-ppp-profile`.
        * **`use-encryption`**: Set to `yes` to enforce encryption for the PPP connection.
        * **`only-one`**: `no` to allow a single user to have multiple connections simultaneously.
        * **`local-address`**:  The local IP address used for the PPP connection; the same IP used for `ether-0`.
        * **`remote-address`**: A pool of IP addresses to be given to the clients on the PPP network.
        * **`use-radius`**: Set to `yes` to use RADIUS for authentication and accounting.
        * **`dns-server`**:  A comma-separated list of DNS servers provided to PPP clients.
*   **Winbox GUI:**
    *   Navigate to *PPP* -> *Profiles*.
    *   Add a new entry.
    *   Fill in: Name `radius-ppp-profile`, check `use-encryption`, uncheck `only-one`, Local Address `115.113.134.1`, Remote Address `115.113.134.2-115.113.134.254`, Check `use-radius`, DNS Server `1.1.1.1,8.8.8.8`.
*   **Effect:**  PPP connections using this profile will be authenticated against the RADIUS server.
*   **After Configuration:** The `radius-ppp-profile` profile is set up.

### 4. Step 4: Configure a PPPoE Server Binding.

*   **Description**: Configure a PPPoE server on `ether-0` using the `radius-ppp-profile` profile.
*   **Before Configuration**: No PPPoE server configuration is present.
*   **MikroTik CLI Example:**
    ```mikrotik
    /interface pppoe-server server
    add interface=ether-0 service-name=pppoe-radius profile=radius-ppp-profile max-mru=1480 max-mtu=1480
    ```
    **Explanation of parameters:**
        *  **`interface`**: The interface on which the PPPoE server will listen for connections, `ether-0` here.
        *  **`service-name`**:  A unique name for the PPPoE server.
        *  **`profile`**: The PPP profile to use for new connections, `radius-ppp-profile` here.
        *   **`max-mru`**: The maximum receive unit size for PPP traffic.
        *   **`max-mtu`**: The maximum transfer unit size for PPP traffic.
*   **Winbox GUI:**
    *   Navigate to *PPP* -> *PPPoE Servers*.
    *   Add a new entry.
    *   Fill in: Interface `ether-0`, Service Name `pppoe-radius`, Profile `radius-ppp-profile`, Max MRU `1480`, Max MTU `1480`.
*   **Effect:** The router will now listen for and accept PPPoE connections on `ether-0`, using the `radius-ppp-profile`.
*   **After Configuration**: A PPPoE server is running on `ether-0`, using RADIUS authentication.

## Complete Configuration Commands:

```mikrotik
/interface ethernet
set ether-0 name="ether-0"
/ip address
add address=115.113.134.1/24 interface=ether-0 network=115.113.134.0
/radius
add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=30s
/ppp profile
add name="radius-ppp-profile" use-encryption=yes only-one=no local-address=115.113.134.1 remote-address=115.113.134.2-115.113.134.254 use-radius=yes dns-server=1.1.1.1,8.8.8.8
/interface pppoe-server server
add interface=ether-0 service-name=pppoe-radius profile=radius-ppp-profile max-mru=1480 max-mtu=1480
```

## Common Pitfalls and Solutions:

*   **Problem:** RADIUS server unreachable.
    *   **Solution:**
        *   Check network connectivity between the MikroTik and the RADIUS server (`ping 192.168.88.10`).
        *   Verify the RADIUS server is running and listening on the expected port (usually UDP 1812).
        *   Double-check the `secret` on both the router and RADIUS server.
        *   Ensure that firewalls are not blocking UDP traffic between the router and the RADIUS server.
*   **Problem:** PPP authentication failing.
    *   **Solution:**
        *   Verify RADIUS server logs for authentication errors.
        *   Double-check user credentials on the RADIUS server.
        *   Check for typos in the `secret` on both the router and RADIUS server.
*   **Problem:**  Clients not receiving IP addresses.
    *   **Solution:**
        *   Check the remote address pool in the `radius-ppp-profile` (`115.113.134.2-115.113.134.254`).
        *   Ensure the RADIUS server is sending back IP addresses correctly for authorization.
        *   Check for conflicts with other DHCP servers on the network.
*   **Problem:** Clients are unable to access the internet, after successful connection.
    *   **Solution:**
        *   Verify that the router is able to connect to the internet.
        *   Verify that the client receives DNS servers.
        *   Verify that NAT masquerading is set up correctly.
*   **Security Issues**:
    *   **Insecure Secret:** Using a weak or default secret is a major security risk. The secret must be randomly generated, and kept in a secure location.
    *   **Lack of Encryption**: Connections to the RADIUS server should be encrypted with TLS using a TLS cert.
    *   **RADIUS server vulnerabilities**: Ensure the RADIUS server is updated with the latest security patches.
* **Resource Issues**
  *   **High CPU Usage:** Caused by large amount of simultaneous connections; upgrade to a more powerful device or throttle connections/users.
  * **High Memory Usage:** Caused by large connection and user tables; enable monitoring for early detection of resource limitations.
*   **RouterOS Specific:**
    *   Check system logs (`/log`) for detailed errors.
    *   Use `/tool sniffer` to capture and analyze PPP traffic and RADIUS communications.

## Verification and Testing Steps:

1.  **Connect a PPPoE client:** Use a client device (e.g., PC, laptop) and configure a PPPoE connection with valid user credentials configured on the RADIUS server.
2.  **Check PPP status:** In the MikroTik router, navigate to *PPP* -> *Active Connections* to verify the connection status.
3.  **Ping the router:** Once the PPP connection is established from the client, ping the router's local IP address on the PPP interface (`115.113.134.1`).
4.  **Ping external IP addresses:** From the client, ping an external IP address (e.g. 8.8.8.8) to verify internet connectivity.
5.  **Monitor RADIUS logs:** Check the RADIUS server logs for successful authentications and accounting messages.
6.  **Use `/tool torch`:** Use the torch tool to monitor traffic on `ether-0` to verify traffic passing to/from the PPPoE server.

## Related Features and Considerations:

*   **Hotspot:** PPP AAA can be used in conjunction with MikroTik Hotspot for more granular control over network access. The `hotspot` service may use RADIUS or its local users.
*   **VPN:** PPP AAA is also usable for VPN technologies (L2TP, SSTP) for authentication and authorization.
*   **User Profiles:** RADIUS may implement profiles, which allows for dynamic configuration of network limits (such as rate limiting, etc).
*   **Accounting:** RADIUS accounting provides data on connection times and transfer volumes, useful for billing and monitoring.
*   **Scripting:** RouterOS scripting can be used to automate certain aspects of the AAA setup.

## MikroTik REST API Examples (if applicable):

While not all aspects of this setup are directly manipulable through the REST API, you can retrieve relevant configuration data and set some settings with the API.  Note that MikroTik's API can be limited for certain parameters.

**Retrieve RADIUS configuration:**

*   **API Endpoint:** `/radius`
*   **Request Method:** `GET`
*   **Example (using `curl`):**

    ```bash
    curl -k -u "your_username:your_password" -H "Content-Type: application/json" "https://your_router_ip/rest/radius"
    ```

*   **Expected Response (Example JSON):**
    ```json
    [
        {
            "address": "192.168.88.10",
            "secret": "your_radius_secret",
            "service": "ppp",
            "timeout": "30s",
            "disabled": "false",
            ".id": "*0"
        }
    ]
    ```
   **Error Handling:**
    *   If the request fails, check the API documentation for any error codes. Ensure the username/password have API read permissions.
**Modify PPPoE Server Status (Enable/Disable)**

* **API Endpoint:** `/interface/pppoe-server/server`
* **Request Method:** `PATCH`
* **Example (using `curl`):** To enable the pppoe server with `.id` of *0 (you should use the correct id from the get call)

```bash
curl -k -u "your_username:your_password" -H "Content-Type: application/json" -X PATCH -d '{"disabled":"false"}' "https://your_router_ip/rest/interface/pppoe-server/server/*0"
```
*   **JSON Payload:**
    ```json
        {
          "disabled":"false"
        }
    ```
*   **Expected Response (Success):** HTTP 200 OK
   *  **Error Handling:** Check the HTTP status code. An HTTP 400 or 500 indicates failure due to invalid parameters or server errors. A 401 or 403 status indicates authentication issues.

**Parameter Explanation:**
    * **`address`**: The IP address of the RADIUS server.
    * **`secret`**: The shared secret used for RADIUS authentication.
    * **`service`**: The service using the radius, such as `ppp`.
    * **`timeout`**: The timeout in seconds for RADIUS requests.
    * **`disabled`**:  Enable or disable this radius configuration.
    * **`.id`**: The id of the configuration.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a strong, randomly generated secret. Avoid common or easily guessed phrases.
*   **Secure RADIUS Communication:** While not always possible in all RADIUS server configuration (specifically when using very old software), use TLS (with a valid certificate) to encrypt communication between the MikroTik and the RADIUS server.
*   **Firewall Rules:** Limit access to the RADIUS server to only the MikroTik IP, protecting it against unwanted access.
*   **Regular Security Updates:** Ensure both the MikroTik and the RADIUS server are updated with the latest patches.
*   **User/Password Management:** Enforce strong password policies for RADIUS users and regular password changes.
*   **Access Control on the Router:** Only allow administrator access to the router over secure protocols. Disable services which are not needed.

## Self Critique and Improvements:

*   **Improvement:** The configuration could benefit from more detailed user management examples.
*   **Improvement:** The implementation could provide more real-world scenarios in more detail.
*   **Improvement:** Dynamic client IP address allocation through RADIUS could be configured.
*   **Improvement:** Further refinement of the RADIUS attributes for specific user requirements, or a RADIUS dictionary would improve this configuration.
*   **Improvement**: More detailed explanations about the RADIUS protocol would improve the learning experience.
*  **Tradeoff:** RADIUS provides centralized user and authentication, but can become a single point of failure.
*  **Tradeoff:** The configuration does not make use of a backup RADIUS server to maintain connectivity.
*  **Tradeoff:** Using encryption increases overhead on the router and users, but provides much needed security.
*  **Tradeoff:** Setting a larger address pool for a greater amount of users could lead to address exhaustion.
*  **Tradeoff:** Setting an excessive amount of timeout could result in longer delays for the user.

## Detailed Explanations of Topic:

**PPP AAA (Authentication, Authorization, and Accounting)**:
PPP AAA is a framework for managing user access in point-to-point communication. It performs three core functions:

*   **Authentication**: Verifies the user's identity. In this context, it is the comparison of the username/password combination with a remote database on a RADIUS server.
*   **Authorization**: Determines what resources or network features the authenticated user is allowed to access. The RADIUS server may return attributes that may allow or restrict network access (e.g. IP addresses, bandwidth limits, VLANs, etc).
*   **Accounting**: Tracks the user's network usage, including connection duration, data volume. This data is typically used for billing and network monitoring.

**RADIUS (Remote Authentication Dial-In User Service):**
RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) management for users who access a network.  It allows access points or routers to verify user identity against a remote server rather than the device itself, making user management easier.
*   **How it works:** When a client attempts to connect to a network device (e.g., a PPPoE server), the device forwards the authentication request to the RADIUS server.  The RADIUS server validates the user credentials and responds with an authorization decision.
*   **Benefits:**
    *   Centralized user management.
    *   Improved security with centralized authentication.
    *   Detailed accounting of network usage.
    *   Policy-based network access control.

## Detailed Explanation of Trade-offs:

*   **Local vs RADIUS Authentication:**
    *   **Local Authentication:** Easier to configure for smaller setups, but lacks the scalability and centralized management of RADIUS. Each router would have its own user database.
    *   **RADIUS Authentication:** Better for larger networks, offering centralized user management, but requires a separate RADIUS server to manage.

*   **PPPoE vs other connection types (e.g. Hotspot, VPN):**
    *   **PPPoE**: A common method for dial-up type connections over Ethernet. Requires PPPoE compatible clients. Suitable for user networks.
    *   **Hotspot:** Provides a captive portal. Provides a splash page for accepting Terms and conditions. Less suited for managed networks.
    *   **VPN:** For remote connectivity. Better for specific point-to-point connectivity between different locations or for remote access.

*   **Encryption vs no encryption:**
    *   **Encryption (e.g. MPPE):**  Provides data privacy during PPP data transmission, but increases CPU overhead on the client and router.
    *   **No Encryption**: Faster, but offers no data confidentiality, exposing data in transit.

*   **Timeout settings:**
    *   **Low Timeout**: Faster responses, but can lead to authentication failures in congested networks.
    *   **High Timeout**: More tolerant of delays, but may make user connections seem unresponsive when there are issues.

*   **Address Pools:**
    *   **Large Pool:** Can accommodate many users, but may create broadcast domains that consume resources.
    *   **Small Pool:** Conserves IP addresses, but could result in IP address exhaustion when the pool is filled.
* **MRU/MTU**
    * **Setting too high of MTU/MRU:** leads to fragmentation and reassembly of packets, which increases processing overhead, leading to slower speeds or network issues.
    * **Setting too low of MTU/MRU:** decreases the amount of data that can be send in a packet, and this increases overhead.

## Configuration for Specific RouterOS Versions:

This document is targeted for RouterOS 7.11.  If used on older versions (e.g. RouterOS 6.48), you must keep in mind that:
*   Some commands and options may not be available or behave differently, and may be changed.
*   Verify the documentation for specific RouterOS 6.48 syntax.
*   The MikroTik REST API may also differ.

Let me know if you have any other questions or want further clarifications!
