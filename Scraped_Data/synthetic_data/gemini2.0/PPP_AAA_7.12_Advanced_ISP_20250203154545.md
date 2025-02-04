Okay, let's dive into a detailed technical documentation for PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik router, specifically targeting a configuration for an ISP-like scenario.

## Scenario Description:

This scenario focuses on implementing PPP (Point-to-Point Protocol) authentication, authorization, and accounting for clients connecting to a MikroTik router over the `ether-14` interface. The router will act as a PPP server, managing client connections, authenticating them via a RADIUS server, assigning IP addresses from the subnet `211.236.234.0/24`, and keeping track of session usage (accounting). This setup is typical for an ISP or any environment where you need to manage individual user connections and usage. We are targeting RouterOS v7.12, as well as ensuring compatibility with v6.48 and other v7.x releases as needed.

## Implementation Steps:

Here's a step-by-step guide to setting up the PPP AAA configuration.

**1. Step 1: Configure the IP Pool**

   * **Description:** We need to define an IP address pool that will be used to assign IP addresses to connecting PPP clients.
   * **Before:** No IP pool exists.
   * **Action:** We create an IP pool named `ppp-pool` with the range `211.236.234.2-211.236.234.254`.
   * **CLI Command:**

     ```mikrotik
     /ip pool
     add name=ppp-pool ranges=211.236.234.2-211.236.234.254
     ```
   * **Winbox:**
        * Navigate to `IP` -> `Pool`
        * Click the "+" button to add a new pool
        * `Name`: `ppp-pool`
        * `Ranges`: `211.236.234.2-211.236.234.254`
        * Click `Apply` then `OK`
   * **After:** The `ppp-pool` IP pool is created.

**2. Step 2: Configure the PPP Secret Profile**

   * **Description:**  We need to set up a PPP secret profile to define the general settings for PPP user connections. This profile links users to the IP pool and also configures the allowed protocols.
   * **Before:** No PPP secret profiles are configured.
   * **Action:** We create a profile named `ppp-profile` that uses the `ppp-pool` IP pool and enables local and remote IPv4 addressing.  We will not configure authentication locally, as that will be handled by RADIUS.  We will, however, set up a basic profile to ensure connectivity if the RADIUS server were to fail.
   * **CLI Command:**
     ```mikrotik
      /ppp profile
      add name=ppp-profile local-address=211.236.234.1 remote-address=ppp-pool use-encryption=yes
     ```
   * **Winbox:**
        * Navigate to `PPP` -> `Profiles`
        * Click the "+" button to add a new profile
        * `Name`: `ppp-profile`
        * `Local Address`: `211.236.234.1`
        * `Remote Address`: `ppp-pool`
        * `Use Encryption`: `yes`
        * Click `Apply` then `OK`
   * **After:**  A `ppp-profile` is created and its settings are defined.

**3. Step 3: Configure the RADIUS Server**

   * **Description:** We configure the connection to the RADIUS server that will perform AAA. We must configure at least one RADIUS server, with a backup.
   * **Before:** No RADIUS servers are configured.
   * **Action:** We add a RADIUS server with IP `192.168.88.100`, secret `radiussecret`, and set the port to 1812 for authentication and accounting on port 1813. We also add a backup server at 192.168.88.101 and use the `ppp-profile` for all PPP users that connect via the radius server.
   * **CLI Command:**
     ```mikrotik
     /radius
     add address=192.168.88.100 secret=radiussecret service=ppp timeout=30s accounting-port=1813
     add address=192.168.88.101 secret=radiussecret service=ppp timeout=30s accounting-port=1813
     /ppp aaa
     set use-radius=yes accounting=yes interim-update=1m
     ```
     *Note: The 'interim-update' should be adjusted to your preference.*
   * **Winbox:**
        * Navigate to `RADIUS`
        * Click the "+" button to add a new RADIUS server
        * `Address`: `192.168.88.100`
        * `Secret`: `radiussecret`
        * `Service`: `ppp`
        * `Timeout`: `30s`
        * `Accounting Port`: `1813`
        * Click `Apply` then `OK`
        * Repeat to create a second RADIUS server with IP `192.168.88.101`.
        * Navigate to `PPP` -> `AAA`
        * Check `Use Radius` and `Accounting` checkboxes
        * Set `Interim Update` to `1m`
        * Click `Apply` then `OK`
   * **After:** The router is configured to use the RADIUS server(s) for PPP authentication and accounting.

**4. Step 4: Configure the PPP Server on Interface `ether-14`**

   * **Description:** We set up the actual PPP server on the `ether-14` interface, enabling it to listen for incoming PPP connections.
   * **Before:** No PPP server is configured.
   * **Action:**  We create a PPP server interface bound to the physical `ether-14` interface.
   * **CLI Command:**
     ```mikrotik
     /interface ppp-server server
     add interface=ether-14 enabled=yes profile=ppp-profile
     ```
   * **Winbox:**
        * Navigate to `Interface` -> `PPP Server`
        * Click the "+" button to add a new server
        * `Interface`: `ether-14`
        * Check `Enabled`
        * `Profile`: `ppp-profile`
        * Click `Apply` then `OK`
   * **After:** A PPP server is active and listening on `ether-14`.

## Complete Configuration Commands:

```mikrotik
/ip pool
add name=ppp-pool ranges=211.236.234.2-211.236.234.254
/ppp profile
add name=ppp-profile local-address=211.236.234.1 remote-address=ppp-pool use-encryption=yes
/radius
add address=192.168.88.100 secret=radiussecret service=ppp timeout=30s accounting-port=1813
add address=192.168.88.101 secret=radiussecret service=ppp timeout=30s accounting-port=1813
/ppp aaa
set use-radius=yes accounting=yes interim-update=1m
/interface ppp-server server
add interface=ether-14 enabled=yes profile=ppp-profile
```

## Common Pitfalls and Solutions:

1.  **RADIUS Server Connectivity Issues:**
    *   **Problem:** The MikroTik router cannot communicate with the RADIUS server, leading to authentication failures.
    *   **Solution:**
        *   Verify IP connectivity using `ping 192.168.88.100` from the router.
        *   Check the firewall settings on both the router and the RADIUS server.
        *   Ensure the shared secret is identical on both devices.
        *   Use the MikroTik's `torch` tool on both the PPP interface and any interfaces leading to the RADIUS server to identify any packet loss/misconfiguration issues. For example,
              ```mikrotik
                /tool torch interface=ether-14 duration=10s src-address=192.168.88.100,192.168.88.101
              ```
2.  **Incorrect IP Pool Configuration:**
    *   **Problem:**  Clients fail to get an IP address or receive an address outside the intended range.
    *   **Solution:** Double-check the IP pool range, and make sure the local address for the PPP profile is correct and does not overlap with the remote address range.
3.  **Incorrect PPP Profile Settings:**
    *   **Problem:** Clients can connect but can not pass any traffic.
    *   **Solution:** Verify the local address, remote address, and encryption settings on the PPP profile.
    *   **Solution:** Remove `use-encryption=yes` if not required by the RADIUS server, especially during debugging.
4.  **RADIUS Accounting Issues:**
    *   **Problem:**  Accounting data is not being sent to the RADIUS server.
    *   **Solution:**
        *   Ensure the RADIUS server is listening on port 1813.
        *   Verify that accounting is enabled in `ppp aaa`.
        *   Check the RADIUS server's logs for any errors.
5.  **Resource Issues:**
    *   **Problem:** High CPU or memory usage due to too many active PPP connections.
    *   **Solution:** Monitor router resources using `/system resource monitor`. Consider upgrading the router if resource usage is consistently high. Implement QoS policies to limit bandwith per user.

**Security Notes:**

*   Use strong RADIUS secrets.
*   Restrict access to the MikroTik router itself.
*   Implement proper firewall rules.
*   Make sure any remote management interfaces are only accessible from specific networks.

## Verification and Testing Steps:

1.  **Basic PPP Connection:**
    *   Connect a test client using PPP over Ethernet (PPPoE) or similar.
    *   Check if the client receives an IP address from the `ppp-pool`.
    *   Verify basic network connectivity using `ping` to a known address on the internet.
2.  **RADIUS Authentication:**
    *   Observe the RADIUS server logs to see if authentication requests are being received and if authentication succeeds or fails.
3.  **RADIUS Accounting:**
    *   Check if accounting data is sent to the RADIUS server when a client connects and disconnects.
    *   Ensure that interim accounting updates are sent at the configured interval.
4.  **MikroTik Interface Status:**
    *   In Winbox, navigate to `Interfaces`. A new virtual interface will be created for every connected PPP user. Examine these interfaces to make sure they have an IP address and the current status is `running`.
    *   Verify with the command `/interface print`, ensuring that the dynamic interfaces have the correct IP address and are `running`.
5.  **MikroTik Logging:**
    *   Enable logging in `/system logging action` and `/system logging`. Verify log output for authentication and connection status.
    *   Use the command `/log print` to view logs for information regarding PPP, RADIUS and connection status.

## Related Features and Considerations:

*   **QoS (Quality of Service):** Implement QoS policies in `/queue tree` to ensure fair bandwidth allocation for all users.
*   **Hotspot:** Instead of using pure PPP, configure the PPP server with the Hotspot functionality for enhanced user management and payment systems.
*   **VRF (Virtual Routing and Forwarding):** Use VRFs to create separate routing tables for different PPP clients if segmentation is required.
*   **BGP (Border Gateway Protocol):** If dealing with large scale networks, consider using BGP to advertise prefixes learned from RADIUS authentication.

## MikroTik REST API Examples:

While the core PPP setup doesn't have dedicated REST API endpoints, we can demonstrate how to retrieve existing PPP server interfaces using the REST API:

**Get all PPP Server Interfaces:**

*   **API Endpoint:** `/interface/ppp-server/server`
*   **Request Method:** `GET`
*   **Example (using a command-line tool like `curl`):**

    ```bash
    curl -k -u admin:password -H "Content-Type: application/json" -X GET https://<your-mikrotik-ip>/rest/interface/ppp-server/server
    ```
*   **Example JSON Response:**
    ```json
    [
      {
        ".id": "*1",
        "interface": "ether-14",
        "profile": "ppp-profile",
        "enabled": true,
        "max-mtu": "1480",
        "max-mru": "1480",
        "keepalive-timeout": "10",
        "authentication": "pap,chap,mschap1,mschap2"
      }
    ]
    ```

   *   **Explanation of the parameters in response**
        *   `.id`: ID of the configuration.
        *   `interface`: Interface the PPP server is attached to.
        *   `profile`: The PPP profile name.
        *   `enabled`:  Status of the PPP server.
        *   `max-mtu`: Maximum MTU allowed on interface.
        *   `max-mru`: Maximum MRU allowed on interface.
        *   `keepalive-timeout`: Time before interface is considered dead.
        *   `authentication`: Supported authentication methods

*   **Error Handling:** In case of an error, the API will return a non-200 status code and often a JSON payload containing the error message.

**Retrieving Radius Servers:**

*   **API Endpoint:** `/radius`
*   **Request Method:** `GET`
*   **Example (using a command-line tool like `curl`):**
    ```bash
    curl -k -u admin:password -H "Content-Type: application/json" -X GET https://<your-mikrotik-ip>/rest/radius
    ```
*   **Example JSON Response:**
    ```json
    [
        {
            ".id": "*1",
            "address": "192.168.88.100",
            "secret": "radiussecret",
            "service": "ppp",
            "timeout": "30",
            "accounting-port": "1813"
         },
         {
           ".id": "*2",
           "address": "192.168.88.101",
           "secret": "radiussecret",
           "service": "ppp",
           "timeout": "30",
           "accounting-port": "1813"
         }
    ]
    ```

   *   **Explanation of parameters in response**
        *   `.id`: ID of the configuration
        *   `address`: IPv4 or IPv6 address of the radius server.
        *   `secret`: Shared secret between the router and radius server.
        *   `service`: Type of service RADIUS is used for.
        *   `timeout`: How long to wait for a reply from the RADIUS server.
        *   `accounting-port`: Port the radius server is listening for accounting requests.

**Setting PPP AAA Options**

*   **API Endpoint:** `/ppp/aaa`
*   **Request Method:** `PUT`
* **Example JSON payload:**
    ```json
     {
        "use-radius":"yes",
        "accounting":"yes",
        "interim-update":"1m"
     }
    ```
*  **Example (using a command-line tool like `curl`):**
    ```bash
    curl -k -u admin:password -H "Content-Type: application/json" -X PUT -d '{"use-radius":"yes","accounting":"yes","interim-update":"1m"}' https://<your-mikrotik-ip>/rest/ppp/aaa
    ```
   *   **Explanation of parameters in request:**
        *   `use-radius`: Whether to use RADIUS server for AAA.
        *   `accounting`: Whether to use accounting.
        *   `interim-update`: How often the router should send updates to the RADIUS server.

## Security Best Practices:

1.  **Strong RADIUS Secret:** Use a complex, randomly generated secret for RADIUS communication.
2.  **Restrict Access:**  Do not expose the RADIUS service to the public internet if possible. Use firewalls to ensure only trusted networks can reach the RADIUS server.
3.  **Secure Router Management:** Use strong passwords for the MikroTik router and restrict access to management interfaces.
4.  **Monitor Logs:** Regularly check logs for any suspicious activity or authentication failures.
5.  **Use Encryption:** Ensure that the communication between the MikroTik router and RADIUS server is encrypted with a secure protocol, such as `TLS` if supported.
6.  **Firewall Rules:** Apply firewall rules to restrict access to specific ports and services.
7.  **Regular Updates:** Keep the MikroTik RouterOS software updated to the latest stable version to patch known security vulnerabilities.

## Self Critique and Improvements:

This configuration is a solid foundation for PPP AAA in an ISP environment. However, here are some areas for improvement and modifications:

*   **More Robust Failover:** While we have configured two RADIUS servers, we could implement more sophisticated failover mechanisms using scripts to dynamically change configuration.
*   **Dynamic IP Address Assignment:** Instead of static pools, we could implement RADIUS attributes that will specify an IP address for the user.
*   **Attribute Mapping:** Use RADIUS attributes such as `Framed-Route` or other relevant attributes to control how each user is routed.
*   **Detailed Logging:** Implement detailed logging configuration to gain deeper insights into user connectivity and any issues. Log to a remote server for more persistent storage.
*   **Real-World RADIUS attributes:** Use specific RADIUS attributes to tailor each client's experience.

## Detailed Explanations of Topic:

**PPP (Point-to-Point Protocol):**  PPP is a data link layer protocol used to establish a direct connection between two nodes. It's often used to create a direct, private connection over a physical or virtual interface.

**AAA (Authentication, Authorization, and Accounting):**

*   **Authentication:** Verifying the identity of a user before granting network access (RADIUS with username/password).
*   **Authorization:** Determining what resources or services an authenticated user is allowed to access (RADIUS attributes).
*   **Accounting:** Tracking user activities, such as connection time and data usage (RADIUS accounting packets).

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting management for users connecting to a network.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Simpler to configure but hard to manage for large user bases and lacks advanced features like usage tracking or per-user policies.
    *   **RADIUS:** More complex but highly scalable, offers robust AAA functionalities, centralized management, and better security.
*   **Encryption:**
    *   **No Encryption:** Easier to debug but data is sent unencrypted, leading to security risks.
    *   **Encryption:** More secure but may require additional configuration and overhead.
*   **Interim-Update Interval:**
    *   **Frequent Updates:** Provides more accurate accounting data, but can increase resource usage.
    *   **Infrequent Updates:** Reduced resource overhead but less real-time accounting data.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS v7.12 but remains compatible with v6.48 and other v7.x releases. However, there might be minor differences in feature availability, command syntax, or Winbox layout across versions. Always refer to the official MikroTik documentation for version-specific details.

Let me know if you would like me to elaborate on any of these sections.
