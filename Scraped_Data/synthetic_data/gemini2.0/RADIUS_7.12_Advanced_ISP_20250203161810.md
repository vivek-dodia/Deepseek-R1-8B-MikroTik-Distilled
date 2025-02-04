Okay, let's craft a comprehensive, advanced-level documentation for implementing RADIUS authentication on a MikroTik router, specifically within the context of an ISP, using VLAN 51 (122.79.51.0/24) and targeting RouterOS 7.12 (compatible with 6.48 and 7.x).

## Scenario Description:

This scenario addresses the need for centralized authentication and authorization of users connecting to the network through VLAN 51, typically used for broadband subscriber access. The MikroTik router will act as a Network Access Server (NAS), forwarding authentication requests to a RADIUS server. This setup enables granular control over user access, billing, and potentially other services. We assume the existence of an already-setup VLAN interface named `vlan-51`, which is outside the scope of this document.

## Implementation Steps:

Here’s a step-by-step guide to configure RADIUS on the MikroTik, with detailed explanations and examples:

**Pre-Requisite:**

*   An already existing and correctly configured VLAN interface named `vlan-51` on the Router.
*   A functional RADIUS server, reachable by the MikroTik router. (e.g., FreeRADIUS, Cisco ISE, or other compatible server.)
*   Basic RouterOS understanding.
*   IP connectivity from the Mikrotik to the RADIUS server.

**Step 1: Add RADIUS Server Configuration**

*   **Why?** This step defines the connection parameters to your RADIUS server.
*   **Before:** The MikroTik router has no information about the RADIUS server.
*   **Action:** Add a new RADIUS configuration.
*   **MikroTik CLI Command:**

    ```mikrotik
    /radius add address=192.168.88.100 secret="your_radius_secret" service=ppp timeout=3s
    ```

    *   `address`: IP address of your RADIUS server (replace with the actual address).
    *   `secret`: Shared secret used for secure communication with the RADIUS server (replace with the actual secret). This is crucial for security.
    *   `service`: Specifies the type of service that uses this RADIUS server, in this case, `ppp`.
    *   `timeout`: Sets the timeout for RADIUS requests, in this case `3s`.

*   **Winbox Equivalent:**
    *   Go to `RADIUS` under the `PPP` menu on the left side. Click the `+` button.
    *   Enter the IP Address, Secret, `ppp` service, timeout settings. Click `OK`.
*   **After:** The MikroTik router is now aware of how to connect to the RADIUS server.
*   **Effect:** The router can now attempt to communicate with the RADIUS server.

**Step 2: Configure PPP Profile with RADIUS Authentication**

*   **Why?** This step links the RADIUS configuration to a specific profile used for incoming user connections.
*   **Before:** The `default` profile is set to `local` authentication only.
*   **Action:** Configure the profile to use RADIUS for authentication.
*   **MikroTik CLI Command:**

    ```mikrotik
    /ppp profile set default use-radius=yes only-one=yes
    ```
    * `use-radius`: Enables RADIUS authentication. This is the main command setting up the RADIUS authentication process for PPP connections.
    * `only-one`: Ensures that the user can only have one active connection with the profile.
*   **Winbox Equivalent:**
    *   Go to `PPP` -> `Profiles`. Double-click the `default` profile.
    *   Check the `Use Radius` checkbox.
    *   Check the `Only One` checkbox.
    *   Click `OK`.
*   **After:** The default profile uses RADIUS authentication for incoming connections.
*   **Effect:** Any incoming PPP connection using the default profile will now be sent to the RADIUS server for authentication.

**Step 3: Enable PPP Server for VLAN 51**

*   **Why?** This step activates the PPP server on the VLAN 51 interface, which will listen for incoming connection requests.
*   **Before:** PPP server is not accepting new connection on VLAN 51
*   **Action:** Enable the PPP server on the VLAN 51 interface.
*   **MikroTik CLI Command:**
    ```mikrotik
    /interface pppoe-server server add interface=vlan-51 service-name="isp-service" max-mtu=1480 max-mru=1480 default-profile=default disabled=no
    ```

    *   `interface`:  Specifies the interface where the PPPoE server listens for incoming connections, in this case, vlan-51.
    *   `service-name`: This will be visible on the customer-end PPPoE client. This should be set to what the ISP provides to the user.
    *   `max-mtu`: Maximum Transmissible Unit for this server. Usually 1492 or less on PPP connections, 1480 here as an example, taking into account overhead.
    *    `max-mru`: Maximum Received Unit for this server. Usually 1492 or less on PPP connections, 1480 here as an example, taking into account overhead.
    *   `default-profile`: The profile to use for incoming connections, referring to the profile modified in step 2 (`default`).
    *   `disabled=no`: Ensures the server is enabled.

*   **Winbox Equivalent:**
    *   Go to `PPP` -> `PPPoE Servers`. Click `+`.
    *   Select the `vlan-51` interface. Enter `isp-service` as the service name, set MTU and MRU as appropriate for your network, and choose the `default` profile.
    *   Make sure the `Enabled` option is checked. Click `OK`.
*   **After:** The PPP server is actively listening for connection requests on vlan-51.
*   **Effect:** Clients sending PPPoE requests on VLAN 51 can now connect.

**Step 4: Enable Logging (Optional, but highly recommended)**

*   **Why?** Enables debugging logs for authentication problems. This step is very important when troubleshooting RADIUS issues.
*   **Before:** Debugging logs are disabled.
*   **Action:** Enable relevant topics for logging.
*   **MikroTik CLI Command:**

    ```mikrotik
    /system logging add topics=radius,ppp action=memory
    ```

    *   `topics`: Specifies which events to log. Here, we log `radius` and `ppp` related events.
    *   `action=memory`: Stores logs in the router's memory.
*   **Winbox Equivalent:**
    *   Go to `System` -> `Logging`.
    *   Click `+` to add a new rule.
    *   Enter `radius,ppp` in the `Topics` field and choose `memory` for action. Click `OK`.
*   **After:** Debugging logs for RADIUS and PPP are enabled.
*   **Effect:** Detailed logs will be generated, aiding troubleshooting.

## Complete Configuration Commands:

```mikrotik
/radius
add address=192.168.88.100 secret="your_radius_secret" service=ppp timeout=3s
/ppp profile
set default use-radius=yes only-one=yes
/interface pppoe-server server
add interface=vlan-51 service-name="isp-service" max-mtu=1480 max-mru=1480 default-profile=default disabled=no
/system logging
add topics=radius,ppp action=memory
```

## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Secret:** The shared secret on the MikroTik must match the one on the RADIUS server. *Solution*: Double-check and ensure they are identical.
*   **RADIUS Server Unreachable:** Verify network connectivity between the MikroTik and the RADIUS server using ping. *Solution*: Ensure firewall rules do not block the connection and verify IP addresses and routes.
*   **Mismatched Service Type:** The RADIUS server should be configured to accept PPP requests from the MikroTik. *Solution:* Confirm that the service type (`ppp`) matches on both the MikroTik and the RADIUS server.
*   **Firewall issues:** Firewall settings on both the RADIUS server and the MikroTik might block the connection. *Solution:* Check your firewall configuration on both devices. Ensure that the MikroTik can reach the radius server port (typically 1812) and the RADIUS server allows packets from the Mikrotik IP Address.
*   **No RADIUS Attributes Returned:** The RADIUS server might not return necessary attributes for proper functioning (e.g., IP address assignment). *Solution:* Ensure the RADIUS server sends relevant attributes, depending on your configuration needs.
*   **CPU or Memory Overload**: If a lot of users connect using PPP, you can encounter resource issues on the router. *Solution:* Monitor the CPU and RAM usage. If too high, consider more powerful hardware or load balancing.
*   **Incorrect MTU/MRU**: Mismatched MTU/MRU values can cause connectivity issues, especially when using PPPoE. *Solution:* Make sure your MTU/MRU values are the same on both the router and client.
*   **Configuration Conflict:** If there are existing conflicting settings within the router, it might result in connection issues. *Solution:* Clear or override the conflicting configurations.
*   **Incorrect VLAN configuration**: If the VLAN is not set up correctly it will cause connectivity issues. *Solution:* Double check your VLAN config on the interface as well as the switch it connects to.
*   **RADIUS server not responding**: If you are using a remote RADIUS server, it might go down for maintenance or other issues, which results in user unable to connect. *Solution*: Setup redundancy for your RADIUS server so users are always able to authenticate to your network.

## Verification and Testing Steps:

1.  **Check RADIUS server reachability:** Use `ping <RADIUS_SERVER_IP>` from the MikroTik.
2.  **Check Radius Server connectivity using Mikrotik Tool**: Use `/tool radius test <RADIUS_SERVER_IP> secret=<RADIUS_SECRET> username=<TEST_USERNAME> password=<TEST_PASSWORD>`. *Expected Result:* `received reply`.
3.  **Enable logging**: If you have not done it already, enable logging of the ppp and radius topics using `/system logging add topics=radius,ppp action=memory`.
4.  **Review Logs:** After attempting to connect with a client, check the logs using `/system logging print where topics~"radius|ppp"` for any errors. The log should show RADIUS requests and responses.
5.  **PPPoE Connection Test:** Connect a PPPoE client to the `vlan-51` network using valid RADIUS credentials. Verify that the client gets an IP and is able to use the internet.
6.  **Monitor active connections:** View active PPP connections in the `/ppp active print` menu.
7.  **Use Torch**: Use `/tool torch interface=vlan-51 protocol=tcp port=1812` (or other RADIUS port) to see if you can see traffic going to the RADIUS server when a user connects.

## Related Features and Considerations:

*   **Accounting:** Configure RADIUS accounting for tracking usage, billing, etc. `radius add service=ppp accounting=yes`
*   **CoA (Change of Authorization):** Implement CoA for dynamic changes, such as limiting bandwidth or disconnecting users.
*   **Multiple RADIUS Servers:** Set up secondary RADIUS servers for redundancy and failover.
*   **Framed-IP-Address Pool:** Configure address assignment pools directly on the MikroTik or use RADIUS to provide them.
*   **Vendor Specific Attributes (VSAs):** Use VSAs to provide customized settings like DNS or other parameters.
*   **Scripting:** Use RouterOS scripting to handle more complex actions before or after the RADIUS authentication/authorization.
*   **QoS:** Apply QoS rules based on authenticated users using mangle rules that mark packets based on user connections, to provide different bandwidth limits to different users.

## MikroTik REST API Examples:

These commands are for the RouterOS API. Ensure the API service is enabled on the router and you have the correct credentials. We will use curl for these examples.

**Example 1: Adding a RADIUS Server**

```bash
curl -k -u admin:your_router_password -H "Content-Type: application/json" -X POST \
  -d '{ "address": "192.168.88.100", "secret": "your_radius_secret", "service": "ppp", "timeout": "3s" }' \
  https://192.168.88.1/rest/ppp/radius
```

*   **Endpoint:** `https://192.168.88.1/rest/ppp/radius` (replace with your router's IP and API endpoint).
*   **Method:** `POST`
*   **Payload:**
    ```json
    {
      "address": "192.168.88.100",
      "secret": "your_radius_secret",
      "service": "ppp",
      "timeout": "3s"
    }
    ```
    *   `address`: IP of the RADIUS server.
    *   `secret`: Shared secret.
    *   `service`:  Service type.
    *   `timeout`: Request timeout.
*   **Expected Response:**
    ```json
    {
        ".id": "*1"
    }
    ```
    The response includes the object id of the newly created object.

**Example 2: Updating a PPP Profile to use RADIUS**

```bash
curl -k -u admin:your_router_password -H "Content-Type: application/json" -X PUT \
 -d '{"use-radius":"yes", "only-one":"yes"}' \
 https://192.168.88.1/rest/ppp/profile/default
```

*   **Endpoint:** `https://192.168.88.1/rest/ppp/profile/default`
*   **Method:** `PUT`
*   **Payload:**
    ```json
    {
        "use-radius": "yes",
        "only-one": "yes"
    }
    ```
    *  `use-radius`: Enables RADIUS authentication.
    *  `only-one`: Ensures only one active connection per user.
*   **Expected Response:**  A JSON response with status code 200.

**Example 3: Error Handling**

If the API call fails, it will return a non-200 status code and a JSON object with an error message. For example, a malformed JSON will return:

```json
{
    "message":"input does not match schema: unexpected token in json at position 2",
    "error":"input does not match schema",
    "code":400
}
```

## Security Best Practices:

*   **Use Strong Shared Secret:** Use a long, complex secret for RADIUS.
*   **Secure API Access:** Protect your MikroTik API by using strong passwords, limiting access to trusted IPs, or disabling it when not needed.
*   **Firewall Rules:** Restrict access to your RADIUS server only to trusted devices.
*   **Monitor Logs:** Regularly check logs for suspicious activities.
*   **RouterOS Updates:** Keep your RouterOS software up-to-date with the latest security patches.
*   **Disable Unused Services:** Disable any unused services on the MikroTik router.
*   **Secure your RADIUS server**: Keep the OS of your RADIUS server up-to-date and follow best practices to secure the server.

## Self Critique and Improvements:

*   **Scalability:** This setup assumes a single MikroTik router. For larger deployments, consider load balancing and redundant routers.
*   **Dynamic VLAN assignment**: Use RADIUS VSA attributes to assign different VLANs to different users based on their plan.
*   **More advanced QoS:** The QoS mentioned before was a basic suggestion; more advanced configurations can be implemented based on user usage, data usage, or other criteria.
*   **Advanced logging:** Use a central log system (syslog) instead of just logging to memory on the Mikrotik, to keep logs for long time periods.
*   **Automated Setup:** For larger scale deployments, consider using the Mikrotik API in conjunction with an automation tool, such as ansible.
*   **Automated Failover:** Implement dynamic routing configuration, so if the current router goes down, an alternative one can takeover.
*   **Documentation:** Keep your configuration documented, so it is easier to troubleshoot when needed.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)**

RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network. The protocol consists of three primary components:

1.  **NAS (Network Access Server):** The client that sends the request for user credentials to the RADIUS Server (in our case, the MikroTik router).
2.  **RADIUS Server:** Central authority to check the user credentials against a database of users. It can also send specific parameters that are applied after authentication (e.g. IP Address, DNS Servers, etc.)
3.  **Users:** Users attempting to connect to the network with their credentials.

**How RADIUS Works:**

1.  **Authentication Request:** When a user tries to connect, the NAS forwards their username and password to the RADIUS server.
2.  **Authentication:** The RADIUS server authenticates the user's credentials against its database.
3.  **Authorization:**  If authentication is successful, the RADIUS server returns an Access-Accept packet, which includes authorization data. This can include IP addresses, bandwidth limits, etc. If not, the RADIUS Server responds with an Access-Reject packet.
4.  **Accounting (Optional):** During the session, the NAS periodically sends accounting information to the RADIUS server, such as user login time, usage duration, and data usage.
5.  **Session Termination:** When the user disconnects, the NAS sends a termination record to the RADIUS server.

**Key Benefits of RADIUS:**

*   **Centralized Management:** All user credentials are managed in one central server.
*   **Enhanced Security:** Use strong encryption for secure communications.
*   **Flexibility:** Allows for custom authorization and accounting attributes.
*   **Scalability:** Can handle a large number of users and devices.
*   **Standard Protocol:** Works with multiple hardware vendors and operating systems.
*   **Billing and Usage tracking:** Use accounting packets to accurately track usage and provide billing functionality for different customers.

## Detailed Explanation of Trade-offs:

**Local Authentication vs. RADIUS Authentication:**

*   **Local Authentication:**
    *   **Pros:** Simpler to configure for small networks, no external server dependency.
    *   **Cons:** Less secure, harder to manage on a large scale, no central accounting system.
*   **RADIUS Authentication:**
    *   **Pros:** Centralized user management, enhanced security, flexible authorization options, scalable, provides tracking for user usage.
    *   **Cons:** More complex to configure, requires a dedicated RADIUS server.

**PPPoE vs. Other Connection Methods (e.g., DHCP, Static IP):**

*   **PPPoE (Point-to-Point Protocol over Ethernet):**
    *   **Pros:** Supports authentication, allows per-user session tracking, can provide a fixed private IP address to the users, can use VLANs for isolation, can provide QoS based on the connection.
    *   **Cons:** More complex to configure, requires compatible client software on the user side.
*   **DHCP:**
    *   **Pros:** Easy to configure, requires no client-side configuration for IP addressing.
    *   **Cons:** No built-in authentication, no session tracking on the router, IP assignment is dynamic, no per user QoS implementation.
*   **Static IP:**
    *   **Pros:** Simple, predictable IP assignments.
    *   **Cons:** Requires manual configuration, no authentication or tracking mechanisms, requires more configuration on the router and client.

**Trade-offs Regarding Attributes Returned by RADIUS:**

*   **Framed-IP-Address Assignment:**
    *   **Pros:** Dynamically assign IP addresses based on user profile, central IP management, more efficient usage of public IP addresses.
    *   **Cons:** Requires more RADIUS server configuration, you need to manage an ip pool on your server.
*   **Framed-Route Assignment:**
     *   **Pros:** You can provide different routes to your customers based on their plan and access level, central routing management.
     *  **Cons:** More configuration needed on the RADIUS server, potential routing issues if not correctly configured.
*   **Framed-MTU Assignment:**
    *   **Pros:** Provide more control to end users and adapt MTU to specific needs.
    *   **Cons:** Can cause problems if the client doesn't support lower MTU. Requires more configuration on the RADIUS server.
*   **Vendor-Specific Attributes (VSAs):**
    *   **Pros:** Provides more control and specific customizations based on your network needs.
    *   **Cons:** Requires deeper understanding of RADIUS, might cause issues if not configured properly on the server and client.
*   **Session Timeout:**
    *   **Pros:** Ability to kill sessions that are not active, helps in saving resources.
    *   **Cons:** Can cause service disruptions if not configured correctly. Requires more configuration on the RADIUS server.

This detailed explanation should give you a solid foundation for understanding and implementing RADIUS on your MikroTik router, with a particular focus on the specifics of your ISP scenario. Remember to always test thoroughly and monitor your systems after implementing any configuration changes.
