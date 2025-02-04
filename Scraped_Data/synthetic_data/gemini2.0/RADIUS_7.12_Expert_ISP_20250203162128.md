Okay, let's craft a comprehensive guide for implementing RADIUS authentication on a MikroTik RouterOS device, targeting version 7.12 (but with notes for 6.48 and 7.x compatibility), in an ISP-like environment, specifically using the `ether-63` interface and the provided subnet. This will be an "Expert" level implementation, as we will explore more advanced configurations.

## Scenario Description:

This configuration establishes a RADIUS (Remote Authentication Dial-In User Service) client on a MikroTik router for authenticating PPP (Point-to-Point Protocol) connections, such as PPPoE (Point-to-Point Protocol over Ethernet) or PPTP/L2TP (Point-to-Point Tunneling Protocol/Layer 2 Tunneling Protocol) clients.  The router, acting as a Network Access Server (NAS), will send authentication requests to a RADIUS server, granting access based on the server's response. We are using interface `ether-63` and subnet `124.251.72.0/24` to represent the network on which authenticated users would connect.  The aim is to handle a large number of simultaneous connections, as expected in an ISP environment.

## Implementation Steps:

Here's a step-by-step guide, including CLI commands (and Winbox where relevant) and explanations:

1.  **Step 1: Configure the RADIUS Server**

    *   **Before:** Initially, there are no RADIUS settings on the router.
    *   **Action:** Add the RADIUS server configuration to your MikroTik router. This step includes the server's IP address, port, and shared secret.

        ```mikrotik
        /radius add address=192.168.10.10 secret=your_radius_secret service=ppp timeout=300ms
        ```
        *   **address:** IP address of your RADIUS server.
        *   **secret:**  Shared secret used for authenticating communication between the router and the RADIUS server. **Important:** Keep this secret highly secure.
        *   **service:**  The type of service this RADIUS entry is for (in our case "ppp"). Other services include "hotspot" or "dhcp".
        *   **timeout:** How long to wait for a response from the RADIUS server (300ms in this example).

    *   **Winbox GUI:** Navigate to `Radius` in the left menu and then click `Add` to create new radius entry using the values described above.
    *   **After:** The RADIUS server settings are configured.  The router will now send authentication requests to this server.

2.  **Step 2: Enable PPP Authentication to use RADIUS**

    *   **Before:**  The PPP server will have the default configurations for authentications.
    *   **Action:** Configure your PPP interface (in this example, assume we are using PPPoE) to use RADIUS authentication by specifying the default profile to be used (which will also use radius).
        ```mikrotik
        /ppp profile add name=radius_profile use-radius=yes
        /ppp server pppoe set default-profile=radius_profile enabled=yes interface=ether-63 service-name=isp-pppoe
        ```
        *   `/ppp profile add name=radius_profile use-radius=yes` will create a profile that uses radius authentication.
        *   `/ppp server pppoe set default-profile=radius_profile enabled=yes interface=ether-63 service-name=isp-pppoe` will set that default profile for our pppoe server running on interface `ether-63` with a service name of `isp-pppoe` that clients can use to connect.
        *   **Winbox GUI:** Go to `PPP`, then `Profiles`. Create a new profile with `Use RADIUS` checked and configure as needed. Go to `PPP` then `PPPoE Servers` and set the created profile.
    *   **After:** PPP clients connecting through `ether-63` are now authenticated against the configured RADIUS server and the router is now actively a Network Access Server (NAS).

3. **Step 3: Configure Firewall rules for the RADIUS protocol**
  *  **Before:** Depending on existing rules there might be no rules to allow the router to contact the radius server, which would lead to authentication failure.
  * **Action:** Configure a firewall rule to allow the RADIUS server access.
      ```mikrotik
       /ip firewall filter add action=accept chain=output dst-address=192.168.10.10 dst-port=1812,1813 protocol=udp comment="Allow RADIUS"
      ```
      * `/ip firewall filter add action=accept chain=output dst-address=192.168.10.10 dst-port=1812,1813 protocol=udp comment="Allow RADIUS"` this allows all udp traffic from this router that is going to the radius server.
    * **Winbox GUI:** Go to `Firewall` then `Filter Rules`. Click `Add` and configure the rule to allow output to the radius server from the router.
    * **After:** The firewall rules now allow the MikroTik router to connect to the radius server.

## Complete Configuration Commands:

```mikrotik
/radius add address=192.168.10.10 secret=your_radius_secret service=ppp timeout=300ms
/ppp profile add name=radius_profile use-radius=yes
/ppp server pppoe set default-profile=radius_profile enabled=yes interface=ether-63 service-name=isp-pppoe
/ip firewall filter add action=accept chain=output dst-address=192.168.10.10 dst-port=1812,1813 protocol=udp comment="Allow RADIUS"
```

## Common Pitfalls and Solutions:

*   **Incorrect Secret:** Ensure the shared secret on the MikroTik router matches the secret configured on the RADIUS server. Double-check and avoid copy-paste errors.
*   **Firewall Issues:** The MikroTik firewall might be blocking traffic to the RADIUS server.
    *   **Solution:**  Verify that the firewall output rules allow traffic to the RADIUS server IP on ports 1812 (authentication) and 1813 (accounting).
*   **RADIUS Server Down:** If the RADIUS server is unavailable or not responding, clients will not be able to authenticate.
    *   **Solution:** Verify the RADIUS server is reachable from the MikroTik router using tools like `ping` and/or `traceroute`. Ensure radius service is running correctly on the RADIUS server, and that the radius server is accessible on the network from the mikrotik router.
*  **IP Address Configuration:** Ensure that the radius server has a reachable IP from the mikrotik router, and that there are no intermediate firewalls blocking the traffic.
* **RADIUS Server Configuration:** The radius server configuration on the other end is crucial. Ensure that NAS is configured correctly, and users/profiles are configured correctly on the server.

## Verification and Testing Steps:

1.  **Monitor RADIUS Logs:** In MikroTik's CLI or Winbox, go to `System > Logs`. Look for authentication requests and responses related to the RADIUS server. Look for keywords like "radius" or "ppp".

2.  **Connect a PPP Client:** Attempt to connect a PPP client (e.g., PPPoE client) to the MikroTik router.
    *   If successful, the client will get an IP address (from the radius server configuration) and be able to access the internet or network as defined on the server side.
    *   If unsuccessful, check the MikroTik logs and the RADIUS server logs for error messages.
3. **Use Torch:** The `torch` tool in MikroTik can be used to analyze live traffic, this can be helpful if no authentication attempts can be observed. In the CLI:
  ```mikrotik
   /tool torch interface=ether-63 protocol=udp
  ```
  This will display the UDP traffic on `ether-63` this could help determine if there are traffic issues.
4.  **Radius Server Tool:** MikroTik has a useful radius test tool, which can be found in `Radius` on the sidebar or in the CLI as `radius test`.

  ```mikrotik
   /radius test address=192.168.10.10 secret=your_radius_secret user=test_user password=test_password service=ppp
  ```
  This will simulate an authentication request to the radius server.

## Related Features and Considerations:

*   **RADIUS Accounting:**  Implement RADIUS accounting to track user sessions, data usage, and other information.
    ```mikrotik
        /radius add address=192.168.10.10 secret=your_radius_secret service=ppp timeout=300ms accounting-port=1813
    ```
    *   **accounting-port:** Specifies the accounting port, defaults to 1813.
    *   You need to ensure the radius server is configured to accept this information.
*   **MikroTik User Manager:** If the user base is small enough, the User Manager package on the MikroTik can act as a basic radius server as well.
*   **Dynamic Address Lists:** Use RADIUS attributes to assign users to specific address lists, facilitating access control and QoS policies.
*   **AAA Framework:** Explore more advanced authentication, authorization, and accounting options using the complete RADIUS protocol capabilities.

## MikroTik REST API Examples:

These examples will require an API user to be configured and enabled on the RouterOS device. These examples are focused on getting specific information, and are therefore GET methods, but the API is used to modify the settings as well using POST, PATCH or DELETE requests.

1.  **Get RADIUS server configurations:**

    *   **API Endpoint:** `/radius`
    *   **Request Method:** `GET`
    *   **Example Request (using curl):**
        ```bash
        curl -k -u api_user:api_password 'https://192.168.1.1/rest/radius'
        ```
    *   **Expected Response (JSON):**
        ```json
        [
            {
                "id": "*1",
                "address": "192.168.10.10",
                "secret": "your_radius_secret",
                "service": "ppp",
                "timeout": "300ms",
                "accounting-port":"1813"
            }
        ]
        ```

2.  **Get PPP server configurations:**

    *   **API Endpoint:** `/ppp/server`
    *   **Request Method:** `GET`
    *   **Example Request (using curl):**
        ```bash
        curl -k -u api_user:api_password 'https://192.168.1.1/rest/ppp/server'
        ```
    *   **Expected Response (JSON):**
        ```json
        [
            {
                "id":"*1",
                "name": "pppoe-server",
                "enabled":"true",
                "interface":"ether63",
                "default-profile":"radius_profile",
                "service-name":"isp-pppoe"
            }
        ]
        ```
3. **Get Firewall Filter Rules:**
    * **API Endpoint:** `/ip/firewall/filter`
    * **Request Method:** `GET`
    * **Example Request (using curl):**
        ```bash
        curl -k -u api_user:api_password 'https://192.168.1.1/rest/ip/firewall/filter'
       ```
    * **Expected Response (JSON):**
      ```json
       [
         {
           "id": "*1",
           "chain": "output",
           "action": "accept",
           "protocol": "udp",
           "dst-address": "192.168.10.10",
           "dst-port": "1812,1813",
           "comment": "Allow RADIUS"
          }
       ]
      ```

*   **Error Handling:** If a request results in an error, the API will respond with an appropriate HTTP status code (e.g., 404, 400) and a JSON body detailing the error. Check the status code and look for the error messages in the response body. For example, if the user was not authenticated properly or was using the wrong method, an error response would be returned.
*   **Parameter Descriptions:** Please consult the MikroTik API documentation for a complete list of parameters and options for each API endpoint as they may be modified/added as the routeros version changes.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a strong, complex shared secret for RADIUS communication and change this secret frequently, for example using a script and a key manager.
*   **Restrict Access to the Router:** Limit physical access to the MikroTik device and restrict access to the management interface to specific IP addresses.
*   **Firewall Rules:** Create specific firewall rules to only allow RADIUS traffic between the router and the RADIUS server. Do not accept UDP traffic on the RADIUS ports from untrusted networks.
*   **RouterOS Updates:** Regularly update RouterOS to the latest stable version to patch any security vulnerabilities.
*   **Monitoring:** Monitor the system and radius logs for suspicious authentication attempts.
*  **API Security:** If using the API, ensure it is protected and accessible only from trusted networks/devices.

## Self Critique and Improvements:

This configuration covers the basics of implementing RADIUS for PPP on a MikroTik Router. Here are some potential improvements:

*   **Dynamic VLAN Assignment:** Configure RADIUS to dynamically assign VLANs based on user attributes for better network segmentation.
*   **Advanced Attributes:** Use RADIUS attributes to set up policies, bandwidth limits, or specific access permissions.
*   **Load Balancing:** Implement RADIUS load balancing to use multiple servers for redundancy and performance.
*   **Scripting:** Create custom scripts to monitor RADIUS activity, implement failover, or automate account provisioning.
*   **Logging:** Implement more thorough logging of authentication and accounting processes to external systems.
*  **HTTPS for API:** If using the API, ensure to always use HTTPS, and use a valid SSL certificate, preferably issued by a CA.

## Detailed Explanation of Topic: RADIUS

RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network. Here's a detailed breakdown:

*   **Authentication:** Verifies the identity of the user. The NAS sends the credentials (username and password) to the RADIUS server, which checks against its user database.
*   **Authorization:** Determines what network resources a user is allowed to access after successful authentication.
*   **Accounting:** Tracks user activity, such as login time, data consumption, etc.
*   **Protocol:** RADIUS uses UDP ports 1812 (Authentication) and 1813 (Accounting) by default.
*   **NAS:** The Network Access Server (NAS), like our MikroTik router, acts as a client that sends authentication requests to the RADIUS server.
*   **Benefits:** Centralized management of users, ease of administration, consistent policies.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Easier to setup, suitable for small networks, but difficult to manage with many users.
    *   **RADIUS:** Scalable, centralized, and offers advanced options but is more complex to implement initially.
*   **MikroTik User Manager vs. External RADIUS:**
    *   **User Manager:** Easier for small deployments, integrated into MikroTik, but lacks flexibility and scalability.
    *   **External RADIUS:** Scalable, more powerful, offers more advanced features, but requires setting up a dedicated RADIUS server.
*   **UDP vs. TCP:** RADIUS uses UDP, which is connectionless. While this may lead to dropped packets, is more lightweight, but in very problematic network conditions TCP could be preferable.
*   **Shared Secret:** The shared secret is a security vulnerability, if compromised, this would allow malicious entities to impersonate the server or the client, and should be kept securely at all times.

## Configuration for Specific RouterOS Versions:

*   **RouterOS 7.12 (and above):**  All commands provided are compatible.
*   **RouterOS 7.x:** All commands should be the same, but ensure the feature is available.
*   **RouterOS 6.48:** Some commands might have slight syntax differences. For example, PPP profiles might be configured differently. Refer to the RouterOS documentation of the version in question for the exact commands and options.

Let me know if you'd like to explore more advanced RADIUS configurations or have other MikroTik networking scenarios you'd like to examine!
