Okay, let's dive into configuring RADIUS authentication on a MikroTik router, specifically within the context of a point-to-point link using RouterOS 7.12. This documentation aims to provide expert-level guidance and assumes a solid understanding of networking concepts.

## Scenario Description:

This scenario involves setting up a MikroTik router acting as a RADIUS client to authenticate users attempting to connect to the network. Specifically, the router will utilize the bridge interface `bridge-42` to allow access to the 36.58.136.0/24 network.  Clients will need to provide credentials that will be verified against a remote RADIUS server, enhancing security and potentially enabling user-specific access policies. The RADIUS server is assumed to exist elsewhere and is reachable by the MikroTik router. This configuration will also be an example of using multiple authentication methods.

## Implementation Steps:

### Step 1: Pre-Configuration Check and Initial Setup

Before starting, ensure the following:
*   The MikroTik router has IP connectivity to the RADIUS server.
*   You have the RADIUS server's IP address, secret key, and a configured user profile on the RADIUS server.
*   The `bridge-42` interface is created and configured with the 36.58.136.0/24 subnet (or you are fine with a new IP address for this documentation).

**Initial Router State (CLI - before configuration):**
```
/interface bridge print
# Shows existing bridges, ensure bridge-42 isn't present with a conflicting config.
/ip address print
# Shows assigned IP addresses, ensuring we don't override other existing configs.
/radius print
# Shows if any radius servers are already configured.
```

**Initial Router State (WinBox):**
*   Check `/Interface/Bridge` for bridge-42.
*   Check `/IP/Addresses` for IP configuration.
*   Check `/Radius` for existing configurations.

### Step 2: Configure RADIUS Server Settings on the MikroTik Router

We'll now configure the MikroTik router as a RADIUS client, instructing it to communicate with the specific RADIUS server.

**CLI Command:**
```
/radius add address=192.168.88.100 secret="MyRadiusSecret" service=ppp timeout=10
/radius add address=192.168.88.101 secret="MyRadiusSecret" service=ppp timeout=10
```

**Explanation:**

| Parameter | Description |
| ------------- | ----------- |
| `address` | The IP address of the RADIUS server. |
| `secret`  | The shared secret key used for authentication between the router and the RADIUS server. |
| `service` | The type of service (in this case, `ppp` which is used for authentication, authorization, and accounting). |
| `timeout` | The timeout (in seconds) for the router to wait for a response from the RADIUS server. |

**Winbox GUI:**
Navigate to `/Radius` and click the `+` button. Populate the required fields.

**Effect:**
The router will now have the configuration to communicate with the specified RADIUS server. This allows the router to offload authentication tasks to this server.

### Step 3: Create PPP Profile and Configure PAP or CHAP
Here, we create a PPP profile which will be used later for local users or to force clients to authenticate before being allowed access to the bridge.

**CLI Command:**
```
/ppp profile add name=radius-ppp-profile use-encryption=no local-address=36.58.136.254 remote-address=36.58.136.0/24 use-mpls=no
/ppp profile set radius-ppp-profile authentication=pap,chap
```

**Explanation:**

| Parameter | Description |
| ----------- | ------------- |
| `name`   | The name of the profile we are creating. |
| `local-address`  | The IP address of the client-side of the connection. |
| `remote-address`   | The IP address range clients will be in when connected. |
| `use-encryption`   | Boolean to enable or disable encryption (in this example we have disabled for simplicity) |
| `use-mpls` | Boolean to enable or disable mpls (disabled in this example) |
| `authentication` | The list of allowed authentication types.  |

**WinBox GUI:**
Navigate to `/PPP/Profiles` and click the `+` button. Populate the required fields.

**Effect:**
The router now has the configuration to authenticate remote clients using PAP and CHAP protocols, with or without RADIUS.

### Step 4:  Apply the RADIUS Authentication to Bridge Interface

Now, we apply the previously defined RADIUS settings in the new PPP profile. The RADIUS server will be responsible for verifying the credentials of any user trying to connect, even if they have an IP address in the subnet.

**CLI Command:**
```
/interface bridge port add bridge=bridge-42 interface=ether1 ppp-profile=radius-ppp-profile
/interface bridge port add bridge=bridge-42 interface=ether2 ppp-profile=radius-ppp-profile
```

**Explanation:**
| Parameter | Description |
| ----------- | ------------- |
| `bridge`   | The name of the bridge we are creating the port on. |
| `interface` | The physical interface we are adding to the bridge.  |
| `ppp-profile`   | The name of the profile we defined earlier which contains our RADIUS settings. |

**Winbox GUI:**
Navigate to `/Interface/Bridge/Ports` and click the `+` button. For each interface you wish to have RADIUS authentication, select the bridge and the interface you want, and select your PPP profile for RADIUS authentication.

**Effect:**
Traffic that attempts to traverse the bridge on the specified interfaces will now be required to authenticate against the configured RADIUS servers using the specified PPP profile and its authentication methods.

### Step 5: Configure Local User or Allow Direct Access
Now, either configure local users for bridge access, or directly allow them access.

**CLI Command:**
```
/ppp secret add name=testuser1 password=testpass1 profile=radius-ppp-profile service=any local-address=36.58.136.254 remote-address=36.58.136.253
/ppp secret add name=testuser2 password=testpass2 profile=radius-ppp-profile service=any local-address=36.58.136.254 remote-address=36.58.136.252
```
Or you can choose to just allow users access directly by not creating any local users.

**Explanation:**

| Parameter | Description |
| ----------- | ------------- |
| `name`   | The username for the connection. |
| `password` | The password for the user. |
| `profile`   | The name of the ppp profile this user should use. |
| `service`  | The service the user should connect to. |
| `local-address` | The local address of the connection. |
| `remote-address`   | The remote address assigned to the user. |

**Winbox GUI:**
Navigate to `/PPP/Secrets` and click the `+` button. Populate the required fields.

**Effect:**
With local users configured, the router can accept authentications locally. If no local users are configured, then the RADIUS server will handle all authentication. The `/ppp active print` command can be used to see all active user connections.

## Complete Configuration Commands:

```
/radius
add address=192.168.88.100 secret="MyRadiusSecret" service=ppp timeout=10
add address=192.168.88.101 secret="MyRadiusSecret" service=ppp timeout=10
/ppp profile
add name=radius-ppp-profile use-encryption=no local-address=36.58.136.254 remote-address=36.58.136.0/24 use-mpls=no
set radius-ppp-profile authentication=pap,chap
/interface bridge port
add bridge=bridge-42 interface=ether1 ppp-profile=radius-ppp-profile
add bridge=bridge-42 interface=ether2 ppp-profile=radius-ppp-profile
/ppp secret
add name=testuser1 password=testpass1 profile=radius-ppp-profile service=any local-address=36.58.136.254 remote-address=36.58.136.253
add name=testuser2 password=testpass2 profile=radius-ppp-profile service=any local-address=36.58.136.254 remote-address=36.58.136.252
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:** Ensure that the MikroTik router can reach the RADIUS server, verify the IP address, firewall rules and that the port is open between the two systems. Use ping, traceroute, or torch to diagnose.
*   **Incorrect Secret Key:**  The shared secret on the MikroTik and the RADIUS server must be identical. Double-check the secret key for typos.
*   **Incorrect Authentication Configuration:** If authentication fails, verify the authentication methods (`pap,chap`) on the MikroTik and the RADIUS server match.
*   **Firewall Blocking RADIUS:** Make sure that the MikroTik's firewall rules are not blocking the UDP packets to the RADIUS server (Usually port 1812 and 1813).
*   **Timeout Values too Low:** If the connection between the MikroTik router and the RADIUS server is slow, increase the timeout value to a higher amount.
*   **User Profile Issues:** Make sure that the user profile on the RADIUS server matches the settings on the MikroTik router and is not locked.
* **Local Address Configuration:** Ensure that the local address specified in the PPP profile (and optionally local ppp secrets) do not conflict with any other IP address configured on the MikroTik router.

## Verification and Testing Steps:

1.  **Check RADIUS Connectivity:** Use `ping` to ensure the RADIUS server is reachable from the MikroTik router.
    ```
    /ping 192.168.88.100
    ```

2.  **Monitor System Logs:** Check the MikroTik system logs (`/log print`) for authentication attempts and errors. Focus on `radius` related messages.
3.  **Verify PPP Connection:**  Connect a device to the `bridge-42` interface (ether1 or ether2) and attempt to authenticate.
4.  **Check Active PPP Connections:** Use `/ppp active print` to verify active PPP connections and the authenticated usernames.
5.  **RADIUS Accounting:** If accounting is enabled on the RADIUS server, verify that accounting information is being received.
6.  **Torch Tool:** The `/tool torch` is useful for capturing traffic on the router. Use to diagnose communications to the radius server.

## Related Features and Considerations:

*   **RADIUS Accounting:** Enable RADIUS accounting to track user session data and usage.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy. The MikroTik will attempt to connect to each server in the order in which they are listed.
*   **Hotspot:**  Use the RADIUS authentication feature within the MikroTik hotspot functionality for managing access in public or semi-public networks.
*   **User Manager:** Use MikroTik's User Manager for advanced RADIUS user management and billing.
*   **Dynamic DNS:**  In a dynamic IP environment, use dynamic DNS to update the RADIUS server IP address on the MikroTik configuration.
*   **Failover:** If using multiple RADIUS servers, configure connection failover to ensure that service is always available.

## MikroTik REST API Examples:

**Adding a RADIUS Server:**
```
# API Endpoint: /radius
# Method: POST
# Request Body:
{
  "address": "192.168.88.100",
  "secret": "MyRadiusSecret",
  "service": "ppp",
  "timeout": 10
}

# Expected Response (Success - 200 OK):
{
   "message":"added",
   "id":"*1"
}
# Expected Response (Error - 400 Bad Request):
{
    "error": "invalid value for parameter address: 192.168.88.300: not a valid IP address"
}
```

**Retrieving RADIUS Server Configuration:**
```
# API Endpoint: /radius
# Method: GET

# Expected Response:
[
    {
       "address":"192.168.88.100",
        "secret":"MyRadiusSecret",
        "service":"ppp",
        "timeout":"10",
        "id":"*1"
    },
    {
       "address":"192.168.88.101",
        "secret":"MyRadiusSecret",
        "service":"ppp",
        "timeout":"10",
         "id":"*2"
    }
]
```

**Deleting a RADIUS Server:**
```
# API Endpoint: /radius/*1
# Method: DELETE
# Expected Response (Success - 200 OK):
{"message":"removed"}

# Expected Response (Error - 404 Not Found):
{
    "error":"not found"
}
```

## Security Best Practices:

*   **Strong Secret Key:** Use a strong, complex, and unique secret key for the RADIUS server.
*   **HTTPS for API:** When using the MikroTik REST API, always use HTTPS to encrypt the communication.
*   **Firewall Rules:** Ensure that only necessary traffic is allowed in and out of the MikroTik router, especially related to RADIUS.
*   **Access Control:** Limit access to the RADIUS configuration on the MikroTik router to authorized users and devices.
*   **Rate Limiting:** Implement rate limiting to reduce the risk of brute-force attacks against the RADIUS authentication.
*   **Logging:** Configure detailed logging for authentication attempts to enable forensic analysis in case of a security breach.

## Self Critique and Improvements:

This configuration provides a solid starting point for RADIUS authentication on a point-to-point link with a MikroTik router. However, several improvements can be made:

*   **Accounting:** Implement RADIUS accounting for tracking user sessions.
*   **Dynamic Authorizations:** Explore dynamic authorization using attributes sent by the RADIUS server.
*   **User Management:** Integrate with User Manager for more advanced user and role management.
*  **Multiple Profiles:** Add more profiles for different services or users.
* **TLS Support:** Enable TLS for RADIUS communication for enhanced security.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):**

RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) for users trying to access a network. It operates using a client-server model, where network devices (like our MikroTik router) act as clients and send user authentication requests to a central RADIUS server. The RADIUS server then verifies user credentials against a user database, responds with access control policies (if allowed) and can also log accounting data for user sessions.

**How it works (simplified):**

1.  **User Attempts Connection:** A user tries to connect to the network through the MikroTik router.
2.  **Access Request:** The MikroTik router, configured as a RADIUS client, sends an access request to the configured RADIUS server with the user's credentials.
3.  **Authentication/Authorization:** The RADIUS server checks the credentials, and if valid, determines if the user is authorized to access the network based on the policies set.
4.  **Access Response:** The RADIUS server sends an access response back to the MikroTik router.
5.  **Connection Accepted/Denied:** The MikroTik router allows or denies access to the user based on the response received from the RADIUS server.
6.  **Accounting:** If configured, the RADIUS server logs accounting data for the session, like the start and end time, and data usage.

**Why use RADIUS:**

*   **Centralized Authentication:** Manages user access from a single location.
*   **Enhanced Security:** Separates access control from the networking devices.
*   **Policy Enforcement:** Easily implement and manage user-specific access policies.
*   **Auditing:** Log user activity for security and reporting purposes.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local Authentication:** Simpler to configure and suitable for small networks or scenarios where strict access controls are not necessary. However, hard to manage for large networks.
    *   **RADIUS Authentication:** More complex to set up but provides enhanced security, centralized access management, and greater control over user authentication, authorization, and accounting.
*   **Multiple RADIUS Servers:**
    *   **Single Server:** Simple but introduces a single point of failure.
    *   **Multiple Servers:** Adds redundancy and high availability but increases complexity in configuration.
*   **PAP vs. CHAP:**
    *   **PAP (Password Authentication Protocol):**  Sends passwords in plaintext which is insecure.
    *   **CHAP (Challenge Handshake Authentication Protocol):**  More secure than PAP but requires more complex configuration.
*   **Encryption vs. No Encryption:**
     *   **No Encryption:** Simpler to setup but transmits data in plaintext.
    *   **Encryption:** More secure but increases resource use.

## Configuration for Specific RouterOS Versions:

This configuration is targeted at RouterOS 7.12.  While most commands are backwards compatible with 6.48 and other 7.x versions, there might be minor differences in the output of certain commands. Always refer to the official MikroTik documentation for version-specific information. The `ppp-profile` configuration will also work in any recent version of MikroTik.

**Note:** This is a detailed configuration for a specific point to point link scenario.  For more complex scenarios, consider using advanced features such as the MikroTik "Hotspot" feature for public networks, VLANs, or other complex user management strategies.  Always perform a backup before making configuration changes.

This detailed documentation should provide a robust guide for implementing RADIUS authentication within the specific context.  Remember that the best configuration will depend on your specific needs. Adjust this configuration as needed for your environment.
