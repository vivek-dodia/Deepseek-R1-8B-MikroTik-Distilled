Okay, let's dive into a detailed RADIUS configuration on MikroTik RouterOS 7.11 (compatible with 6.48 and other 7.x versions) for an SMB network, specifically focusing on the given parameters.

## Scenario Description:

This configuration aims to set up a MikroTik router as a RADIUS client, authenticating user access for a specific network segment.  The router, using the `ether-76` interface (connected to the 158.131.196.0/24 subnet) will forward authentication requests to a RADIUS server. We will configure the router to use RADIUS for user authentication before allowing access on the 158.131.196.0/24 network. This setup is ideal for scenarios where access control and user accounting are necessary, such as in small to medium sized businesses with wireless networks, and in certain segments where user control and login is important.

## Implementation Steps:

Here's a step-by-step guide to configuring RADIUS on your MikroTik router:

### Step 1: Initial Router State Check and Interface Details

*   **Action:** Verify the current state of the `ether-76` interface and ensure it is configured with an IP address in the 158.131.196.0/24 range.
*   **Why:**  Ensures the interface is enabled and ready for further RADIUS related configurations.
*   **CLI Example (Before):**
    ```mikrotik
    /interface ethernet print where name="ether-76"
    /ip address print where interface="ether-76"
    ```
*   **Expected Output (Before):**  Output should show the `ether-76` interface details, and possibly IP addresses. If there are no IP addresses, you'll need to add one within the 158.131.196.0/24 range. Let's assume that there's no IP address assigned and let's assign the 158.131.196.1/24 as an example.
*   **CLI Command to Assign Address:**
    ```mikrotik
    /ip address add address=158.131.196.1/24 interface=ether-76
    ```

*   **CLI Example (After):**
    ```mikrotik
    /interface ethernet print where name="ether-76"
    /ip address print where interface="ether-76"
    ```
*   **Expected Output (After):**
    Should show `ether-76` interface details with an IP address configured.

### Step 2: Add RADIUS Server Configuration

*   **Action:** Define the RADIUS server details, including IP address, secret, and port.
*   **Why:**  This step establishes the link between the MikroTik router and the RADIUS server for authentication purposes.
*   **CLI Example (Before):**
    ```mikrotik
    /radius print
    ```
*   **Expected Output (Before):**
    Should show nothing or existing RADIUS entries.
*   **CLI Command:** (Assuming RADIUS server IP is 192.168.88.100, shared secret is "mysecret" and default auth and accounting port)
    ```mikrotik
    /radius add address=192.168.88.100 secret=mysecret timeout=10
    ```
   **Explanation of parameters:**

    | Parameter | Description                                                            |
    | :-------- | :--------------------------------------------------------------------- |
    | address   | The IP address or hostname of the RADIUS server.                      |
    | secret    | The shared secret key used for authentication with the RADIUS server. |
    | timeout   | The time (in seconds) the router waits for a response from the RADIUS server before timing out. |
    | service (Optional) | Services for which the server is used, i.e. ppp, hotspot, wireless |
    | accounting (Optional)| Enables accounting requests to be sent to the radius server |
    | domain (Optional)   | Domain of the users being authenticated.                     |
    | authentication-port (Optional)| The port used for authentication, defaults to 1812, but may vary. |
    | accounting-port (Optional)   | The port used for accounting, defaults to 1813, but may vary.    |
*   **CLI Example (After):**
    ```mikrotik
    /radius print
    ```
*   **Expected Output (After):**
    Should show the new RADIUS server configuration.

### Step 3: Enable RADIUS Authentication for the Desired Service

*   **Action:** Configure the service ( in this case, general `ppp`) to use RADIUS for authentication.
*   **Why:** Tells the router that any authentication requests from the given service/feature should be handled via RADIUS. This step is crucial as you must activate RADIUS for the feature of interest.
*   **CLI Command:**
   ```mikrotik
    /ppp profile set default use-radius=yes
    ```
* **Explanation of parameters:**
    | Parameter        | Description                                                               |
    | :--------------- | :------------------------------------------------------------------------ |
    | profile          | The specific profile being configured, in this case default profile        |
    | use-radius       | Turns on RADIUS functionality for the service, using all defined RADIUS servers |

    **Note**: The  `/ppp profile set default use-radius=yes` enables the RADIUS authentication for the ppp profiles, this means that for any PPP based service, i.e. PPTP, L2TP, or PPPoe, the authentication will go through RADIUS, and it will use the defined RADIUS servers, in the order they are defined.
*   **CLI Example (After):**
    ```mikrotik
    /ppp profile print where use-radius=yes
    ```
*   **Expected Output (After):**
     Should show the `default` profile has `use-radius=yes`

### Step 4: User Creation and Testing
*   **Action:** create a test user, and then attempt a connection.
*   **Why:**  This step validates the RADIUS server configuration, as well as the user configuration, and the router.
*   **CLI Command:**
   ```mikrotik
   /ppp secret add name=testuser password=testpass profile=default service=pptp
    ```
    **Explanation of Parameters:**
    | Parameter        | Description                                                               |
    | :--------------- | :------------------------------------------------------------------------ |
    | name          | The username to be created        |
    | password      | The user password          |
    | profile       | The profile to be associated with this user        |
    | service       | The service type to which this user belongs        |
*   **Expected Output**
    No output is expected when executing the command above.
*   **Action:** Test with a PPTP connection (from a remote machine or another router)
*   **Expected Output:** On the client attempting the connection, you should be able to connect successfully, and on the router you should be able to view the established connection. On the RADIUS server logs you should be able to see access-request logs.

## Complete Configuration Commands:

```mikrotik
/ip address add address=158.131.196.1/24 interface=ether-76
/radius add address=192.168.88.100 secret=mysecret timeout=10
/ppp profile set default use-radius=yes
/ppp secret add name=testuser password=testpass profile=default service=pptp
```

## Common Pitfalls and Solutions:

*   **Incorrect Shared Secret:** Ensure the secret configured on the MikroTik router matches the secret configured on the RADIUS server. Use `/radius print` to view the current secret. Update the secret using `/radius set <number> secret=<new_secret>`.
*   **Firewall Issues:** Ensure no firewall rules are blocking traffic between the MikroTik router and the RADIUS server. Use `/ip firewall filter print` to review existing filter rules.
*   **RADIUS Server Unreachable:** Check network connectivity between the MikroTik router and the RADIUS server. Use `ping <radius_server_ip>` to verify reachability, as well as `/tool traceroute <radius_server_ip>` to verify reachability and identify potential routing issues. Use `/tool torch interface=<interface_facing_radius_server>` to verify if the router is reaching the radius server.
*   **Incorrect Port:** Verify the RADIUS server is listening on the correct ports (usually 1812 for authentication, 1813 for accounting). The MikroTik command `/radius print` will show the configured ports. Update the ports using `/radius set <number> authentication-port=<new_port> accounting-port=<new_port>`.
*   **RADIUS Server Configuration:** The RADIUS server must be configured to accept requests from the MikroTik router's IP address (or any interface in the case that you are NAT-ing), as well as to properly authenticate the user.
*   **Timeouts:** If the RADIUS server is slow or unresponsive, increase the timeout value using `/radius set <number> timeout=<new_timeout>`. If timeouts persist, address the issue on the RADIUS server.
*   **Configuration Mismatch on the User profile:** Ensure that the user created exists in the RADIUS server with the username/password, otherwise authentication will not work. Check the Radius Server logs to find out specific errors.

## Verification and Testing Steps:

1.  **Check RADIUS Server Status:** Verify the RADIUS server is running and accessible. Check the radius server logs (usually `/var/log/radius/`) to check if the MikroTik router is trying to establish the connection and if there are any specific issues, like invalid user password or other errors.
2.  **Verify RADIUS Configuration:** On the MikroTik device use `/radius print` to ensure the configuration is correct.
3.  **Test RADIUS Connectivity:** Use the `ping` command, and `traceroute` to check IP reachability to the radius server.
4.  **Enable verbose RADIUS logging on the Router:** Use the following command `/system logging add topics=radius action=memory`. This enables debugging for radius related events.
5.  **Verify Authentication Logs:** Check `/log print where topics~"radius"` to check the RADIUS logs, and verify that authentication is actually performed by the RADIUS server. Check on the server logs (usually `/var/log/radius/`) to verify the request and response. You should see `Access-Request`, `Access-Accept`, or `Access-Reject` messages.
6.  **PPTP/L2TP/PPPoE Test:** If applicable, attempt a PPTP, L2TP or PPPoE connection using a RADIUS user.
7.  **Success Criteria:** Successful authentication should show up in the RADIUS logs, and in the router logs as well, and an established tunnel on the router, and the successful connection on the client.

## Related Features and Considerations:

*   **User Manager:** MikroTik's User Manager package provides a more advanced way to manage users, profiles, and sessions, especially in conjunction with RADIUS.
*   **Hotspot:** MikroTik's Hotspot feature can use RADIUS for user authentication and management, which is quite relevant for the given context.
*   **Wireless Security:** When used with wireless, RADIUS provides robust authentication via WPA2/3 Enterprise, which can be easily integrated.
*   **Accounting:** Enable accounting to track user activity and data usage on the router by adding the `accounting` parameter to the `/radius add` command, for example `/radius add address=192.168.88.100 secret=mysecret timeout=10 accounting=yes`. This requires the RADIUS server to be configured for accounting.
*   **Multiple RADIUS Servers:** MikroTik supports configuring multiple RADIUS servers for redundancy. Add multiple `/radius` entries, and they will be used based on the order they are defined on the router.
*   **Custom Attributes:** In some cases, custom attributes may be required (like setting bandwidth limits). You can configure this using MikroTik profiles and RADIUS attribute mappings.

## MikroTik REST API Examples:

Here are some basic REST API examples for managing RADIUS configurations on MikroTik:

**Prerequisites:** The API needs to be enabled, with proper user/permissions configured. The examples assume that there's already an administrator user named `api-user` with password `apipass`, and the API is configured with `https://<router-ip>/rest`.

*   **Adding a RADIUS server:**
    *   **API Endpoint:** `https://<router-ip>/rest/radius`
    *   **Request Method:** `POST`
    *   **JSON Payload:**
        ```json
        {
            "address": "192.168.88.100",
            "secret": "mysecret",
            "timeout": 10
         }
        ```
    *   **Expected Response (Success):**
        ```json
        {
           ".id": "*1",
           "address":"192.168.88.100",
           "secret":"mysecret",
           "timeout":"10",
           "authentication-port":"1812",
           "accounting-port":"1813"
        }
        ```
    *   **Error Handling:** If any field is incorrect or an issue occurred on the router, a suitable error code is returned, for example `{"message":"invalid value for argument 'secret'","error":"invalid-value"}`.

*   **Retrieving RADIUS servers:**
    *   **API Endpoint:** `https://<router-ip>/rest/radius`
    *   **Request Method:** `GET`
    *   **Expected Response (Success):**
        ```json
        [
            {
               ".id": "*1",
               "address":"192.168.88.100",
               "secret":"mysecret",
               "timeout":"10",
               "authentication-port":"1812",
               "accounting-port":"1813"
            }
        ]
        ```

*   **Updating a RADIUS server:**
    *   **API Endpoint:** `https://<router-ip>/rest/radius/*1` (Assuming the RADIUS server `.id` is `*1`, can be retrieved by the `GET` command above. )
    *   **Request Method:** `PUT`
    *   **JSON Payload:**
        ```json
            {
                "secret": "newsecret",
                "timeout": 15
            }
        ```
    *   **Expected Response (Success):**  No body response
    *   **Error Handling:** If the `.id` is not valid, an error code is returned.

*   **Deleting a RADIUS server:**
    *   **API Endpoint:** `https://<router-ip>/rest/radius/*1` (Again, assuming the RADIUS server `.id` is `*1`)
    *   **Request Method:** `DELETE`
    *   **Expected Response (Success):**  No body response
    *   **Error Handling:** If the `.id` is not valid, an error code is returned.

*   **Authentication:** For all of the API requests you need to include the Authentication information, through the `Authorization` header using the format `Basic <base64 encoded string of username:password>`.

## Security Best Practices:

*   **Strong Shared Secret:** Use a complex, randomly generated shared secret for the RADIUS server.
*   **Restrict Access:** Use firewall rules to restrict access to the RADIUS server to only authorized devices.
*   **Separate Networks:** Place the RADIUS server on a separate, secure network segment, if possible.
*   **Regularly Monitor Logs:** Regularly monitor RADIUS and system logs for any unusual activity.
*   **Use HTTPS:** Always use HTTPS for communication between the router and the RADIUS server using TLS encryption. This is not a MikroTik setting per-se, but rather a RADIUS configuration detail.
*   **Secure API Access:** Use strong authentication for the API, and limit API access to specific IP addresses.
*   **Disable unnecessary services:** Disable unused services on the router and RADIUS server.

## Self Critique and Improvements:

This configuration provides a solid foundation for RADIUS authentication in an SMB environment. However, here are some possible improvements:

*   **User Manager integration:** Moving user management to MikroTik's User Manager is recommended for a more streamlined user management experience.
*   **Attribute Mappings:** Defining attribute mappings is necessary to send custom parameters to the RADIUS server, such as bandwidth limits.
*   **Redundancy:** Implement a secondary RADIUS server for redundancy.
*   **Logging:** Use a dedicated logging server to better store and analyze the router's logs.
*   **Specific Service:** Instead of using the `default` profile, more specific profiles can be configured to avoid potential conflicting settings.

## Detailed Explanations of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to a network or service. RADIUS allows you to centralize authentication instead of configuring users locally on every device. It's an industry standard protocol used extensively in various contexts, including Wi-Fi authentication, VPN access, and network access control.

*   **Authentication:** RADIUS verifies the identity of a user using credentials (username and password) against an authentication database on the RADIUS server.
*   **Authorization:** After successful authentication, RADIUS can also provide authorization, determining what resources the user can access based on predefined policies.
*   **Accounting:** RADIUS can also log user access, keeping track of session start/stop times, and resource usage. This information can be used for billing or usage analysis.

## Detailed Explanation of Trade-offs:

*   **Local User Management vs RADIUS:** Local user management on the router is easier to set up but doesn't scale well, is harder to manage, and does not offer accounting features. RADIUS provides centralized user management, better scalability, and accounting, but requires more complex initial setup, as well as extra maintenance of the RADIUS server.
*   **RADIUS vs Diameter:** RADIUS is a commonly used protocol but is an older protocol. Diameter is the evolution of RADIUS which is more robust and scalable, as well as more modern.
*   **Complexity vs Security:** RADIUS adds complexity to the network setup, and requires additional maintenance and attention to security practices. However, with it comes increased security for user authentication.
*   **Authentication Methods:** RADIUS servers can use a variety of authentication methods (PAP, CHAP, MSCHAPv2, EAP), each with its own security implications. It is recommended to use the most secure method that is compatible with both the router and the RADIUS server. EAP is generally more secure than PAP/CHAP/MSCHAPv2.
*   **Single vs Multiple Servers:** Using a single server is easy to setup but single point of failure, therefore the trade-off here is availability vs ease of implementation.

## Configuration for Specific RouterOS Versions:

This configuration is suitable for RouterOS versions 6.48 and later versions 7.x. The commands used are compatible across these versions. However, it is recommended to always use the latest stable RouterOS version.

This detailed guide should provide you with a comprehensive understanding of how to configure RADIUS on your MikroTik router with a specific example.  Remember to tailor the configurations to your specific environment and requirements.
