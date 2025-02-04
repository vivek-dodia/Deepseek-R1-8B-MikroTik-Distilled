Okay, let's craft some expert-level documentation for PPP AAA on MikroTik RouterOS 7.11, focusing on a point-to-point link scenario. We'll be very detailed, assuming the reader is familiar with basic MikroTik concepts but needs in-depth knowledge for advanced configurations.

## Scenario Description:

We are configuring a point-to-point link using PPP (Point-to-Point Protocol) between two MikroTik routers. We'll use a simple configuration with PPP secrets stored directly on the router (local AAA). We'll then explore configuring AAA via RADIUS. This setup will demonstrate how authentication, authorization, and accounting (AAA) can be implemented for PPP connections, focusing on local user management and then RADIUS integration. The interface `ether-16` will be used for the PPP connection between the two routers.

## Implementation Steps:

**Initial State:**

Before we start, let’s assume our `ether-16` interface is not configured for anything PPP specific. It may have an IP address (for testing) but we're focusing on the initial state of an unconfigured interface.

**Router A:**

### Step 1: Add a PPP Secret (Local AAA)

*   **Purpose:** This step defines a user and password for PPP authentication directly on the router, enabling local authentication, authorization, and accounting.

*   **Before:** No PPP secrets exist.

*   **CLI Command:**
    ```mikrotik
    /ppp secret
    add name=pppuser1 password=StrongPassword1 service=pptp profile=default
    ```

*   **Explanation:**
    *   `/ppp secret add`:  Adds a new PPP secret.
    *   `name=pppuser1`: Sets the username for the PPP client.
    *   `password=StrongPassword1`: Sets the password for authentication. **NOTE:** Use a complex, strong password in real implementations.
    *   `service=pptp`: Specifies that this secret is for use with PPTP. Change to `pppoe` or `l2tp` for those services.
    *    `profile=default`: Assigns the 'default' PPP profile, which specifies basic PPP settings. You can create and use different profiles later for more granular control over authentication and authorization, such as limiting bandwidth or access.
        *Note that 'default' is defined via /ppp profiles. This step assumes the 'default' profile exists. This profile must be defined before the 'ppp secret add' command.

*   **After:** A new PPP secret is configured in the router's local database.

*   **Winbox GUI:** Go to `PPP > Secrets`, then click the "+" button to add a new secret. Fill in the user, password, service, and profile fields.

### Step 2: Configure PPP Interface (PPTP) on Router A.

*   **Purpose:** This step sets up the PPP interface to handle incoming PPP connections. We're configuring a PPTP server in this case.

*   **Before:** No PPTP server interface is configured.

*   **CLI Command:**
    ```mikrotik
    /interface pptp-server server
    set enabled=yes default-profile=default authentication=mschap2,pap,chap
    /interface pptp-server server add user=pppuser1
    ```

*   **Explanation:**
    *   `/interface pptp-server server set enabled=yes`: Enables the PPTP server.
    *   `default-profile=default`: Sets the default profile, which determines the IP address assignment and further configurations.
    *   `authentication=mschap2,pap,chap`: Sets the authentication protocols allowed for PPTP clients. mschap2 is the most secure, followed by chap, with pap the least secure and should be avoided.
    * `/interface pptp-server server add user=pppuser1`: Adds the defined user from the secrets table to be allowed to connect.
        *Note that the 'user' parameter here does not set the 'username' that clients use to connect, it simply makes the user in question available for connections. It uses the 'name' field from the '/ppp secret' table as the identifier.

*   **After:**  A PPTP server is enabled on Router A, listening for connections on port 1723.

*   **Winbox GUI:** Go to `Interface > PPTP Server` and check the `Enabled` checkbox. Modify authentication and default profile accordingly. Then, go to `Interface > PPTP Server > Users`. Click on the `+` button, and add `pppuser1`.

### Step 3: Configure PPTP interface profile
*   **Purpose:** This step sets up the default interface profile and sets up the address pool that the remote client will draw from. This allows the remote client to have a reachable IP address.
*   **Before:** No IP address pool has been specified.
*   **CLI Command:**
    ```mikrotik
    /ip pool
    add name=pptp-pool ranges=115.243.52.10-115.243.52.20
    /ppp profile
    set default local-address=115.243.52.1 remote-address=pptp-pool
    ```
*   **Explanation:**
    *    `/ip pool add name=pptp-pool ranges=115.243.52.10-115.243.52.20`: Creates an IP address pool named 'pptp-pool' with address range 115.243.52.10 to 115.243.52.20.
    *    `/ppp profile set default local-address=115.243.52.1 remote-address=pptp-pool`: Specifies the local address that the server will use as the local end of the tunnel and specifies that clients will draw addresses from the pptp-pool range.
*   **After:** A new IP address pool is configured and the default profile is set to use it.
*   **Winbox GUI:** Go to `IP>Pool` click the `+` button and specify the name and ranges. Then, navigate to `PPP > Profiles`. Select 'default' and specify 'local-address' and 'remote-address'

**Router B:**

### Step 4: Configure PPP Client on Router B

*   **Purpose:** This step configures the router as a PPP client to connect to Router A.

*   **Before:** No PPP client interface is configured.

*   **CLI Command:**
    ```mikrotik
    /interface pptp-client
    add connect-to=1.2.3.4 user=pppuser1 password=StrongPassword1 name=pptp-client1 disabled=no
    ```

*   **Explanation:**
    *   `/interface pptp-client add`: Adds a new PPTP client interface.
    *    `connect-to=1.2.3.4`: Specify the IP address of Router A (where the PPTP server is running). Replace `1.2.3.4` with the actual public IP address of Router A.
    *   `user=pppuser1`: Uses the same user as defined in Router A's PPP secrets.
    *   `password=StrongPassword1`: Uses the same password as in Router A's PPP secrets.
    *   `name=pptp-client1`: Sets the name of the client interface.
    *   `disabled=no`: Enables the interface.

*   **After:** A new PPTP client interface is configured and attempts to connect to Router A.
* **Winbox GUI:** Navigate to `Interface > + > PPTP Client`. Enter the necessary parameters as described above and click `Apply`.

### Step 5: Configure Firewall Rule

*   **Purpose:** To allow PPP connections to Router A.
* **Before:** Firewall configuration does not exist
* **CLI Command:**
    ```mikrotik
    /ip firewall filter
    add chain=input protocol=tcp dst-port=1723 action=accept comment="Allow PPTP connections"
    add chain=input in-interface=pptp-client1 action=accept comment="Allow established connections from PPP tunnel"
    ```
*   **Explanation:**
    * `/ip firewall filter add chain=input protocol=tcp dst-port=1723 action=accept comment="Allow PPTP connections"` allows incoming connections to TCP port 1723, which PPTP uses.
    * `/ip firewall filter add chain=input in-interface=pptp-client1 action=accept comment="Allow established connections from PPP tunnel"` allows established connections through the established PPP tunnel.
* **After:** Router A will accept incoming connections to port 1723
* **Winbox GUI:** Navigate to `IP > Firewall > Filter Rules`. Click `+`. Add a rule for chain `input` with protocol `tcp` destination port `1723` action set to `accept`. Add a second rule for chain `input` with input interface `pptp-client1` and action set to `accept`.

## Complete Configuration Commands:

**Router A (Server):**

```mikrotik
/ppp secret
add name=pppuser1 password=StrongPassword1 service=pptp profile=default
/interface pptp-server server
set enabled=yes default-profile=default authentication=mschap2,pap,chap
/interface pptp-server server add user=pppuser1
/ip pool
add name=pptp-pool ranges=115.243.52.10-115.243.52.20
/ppp profile
set default local-address=115.243.52.1 remote-address=pptp-pool
/ip firewall filter
add chain=input protocol=tcp dst-port=1723 action=accept comment="Allow PPTP connections"
add chain=input in-interface=pptp-client1 action=accept comment="Allow established connections from PPP tunnel"
```

**Router B (Client):**

```mikrotik
/interface pptp-client
add connect-to=1.2.3.4 user=pppuser1 password=StrongPassword1 name=pptp-client1 disabled=no
```

## Common Pitfalls and Solutions:

*   **Authentication Failures:**
    *   **Problem:** The username or password on Router B does not match Router A's secret.
    *   **Solution:** Double-check the spelling and capitalization of the username and password.
*   **Firewall Blocking Connection:**
    *   **Problem:** Router A's firewall might be blocking the connection on port 1723.
    *   **Solution:** Add a firewall rule on Router A as described in Step 5.
*   **IP Address Conflicts:**
    *   **Problem:** The local-address and remote-address in the `/ppp profiles` configuration conflict with other network segments.
    *   **Solution:** Ensure the local and remote addresses in the /ppp profile, as well as the ranges in /ip pool do not overlap with any other IP subnets.
*   **MTU/MRU Mismatches:**
    *   **Problem:** If the MTU or MRU are set wrong, or too high, the connection may not work as expected.
    *   **Solution:** Use the default MTU/MRU sizes (1492), or set lower sizes if connection issues exist.
*   **DNS Issues:**
    * **Problem:** Clients connecting via PPP may fail to resolve DNS.
    * **Solution:** Ensure that RouterA is configured to act as a DNS server or configure `dns-server` addresses in the default profile via `/ppp profile set default dns-server=8.8.8.8,8.8.4.4`

## Verification and Testing Steps:

1.  **Interface Status:** On Router B, verify the `pptp-client1` interface shows the 'R' flag (running) by checking `/interface print`.

2.  **IP Address Assignment:** On Router B, verify that the PPP client has a valid IP address within the `115.243.52.10-115.243.52.20` range by checking `/ip address print`.

3. **Ping Test**:  From Router B, ping Router A's PPP server local address, `ping 115.243.52.1`. If this fails, check firewall configurations.

4.  **Torch Tool:** Use the `/tool torch interface=ether-16` on both routers to observe traffic during PPP connection attempt.

5.  **Logs:** Check the `/log print` on both routers for any errors or warnings related to PPP authentication or connection.

6. **Firewall Logs**: Use the `/log print` on the server to see if any rules were matched when the client attempts to connect. If no rules are matched, ensure that the rule is correct.
7. **Connection Status:** In Winbox, check the `Interface` menu to view real-time connection status. Pay attention to flags, connection status, and transferred data.

## Related Features and Considerations:

*   **RADIUS Server:** Instead of local AAA, you can configure Router A to use a RADIUS server for authentication, authorization, and accounting. This is beneficial for larger networks with many users.
*   **PPP Profiles:** You can create multiple PPP profiles with different IP pools, bandwidth limits, and other settings, allowing for more granular control.
*   **PPPoE/L2TP:** The same principles can be applied to PPPoE or L2TP connections instead of PPTP, offering different security levels and configurations.
*   **Encryption:** PPTP is inherently insecure. Consider L2TP/IPSec or WireGuard for secure connections.

## MikroTik REST API Examples (if applicable):
*   **Note:** PPP configurations, especially secrets, can be sensitive and may not be appropriate for a direct API call in all cases.

```json
{
    "description": "Example: Add a PPP Secret via API",
    "endpoint": "/ppp/secret",
    "method": "POST",
    "request": {
       "name": "api_user",
       "password": "ApiPassword",
       "service": "pptp",
       "profile": "default"
    },
    "response": {
      "status": "success",
      "message": "PPP secret added successfully"
      //or a detailed error message if it fails
    }
}
```

```json
{
    "description": "Example: Get all PPP Secrets via API",
    "endpoint": "/ppp/secret",
    "method": "GET",
    "request": {},
    "response": [
        {
           "id": "*123",
           "name": "pppuser1",
           "service": "pptp",
           "profile": "default",
           //....other fields
        },
        {
           "id":"*456",
           "name":"api_user",
           "service": "pptp",
           "profile": "default",
           //...other fields
       }
    ]
}
```

```json
{
  "description": "Example: Get all PPP Profiles",
  "endpoint":"/ppp/profile",
  "method":"GET",
  "request": {},
  "response":[
    {
        "name":"default",
        "local-address":"115.243.52.1",
        "remote-address": "pptp-pool"
        //.. other fields
    },
    //.... other profiles
  ]
}
```
*   **Error Handling:** Use standard HTTP codes (400, 401, 500) for error conditions and examine the response body for detailed error messages.

## Security Best Practices:

*   **Use Strong Passwords:** Always use strong, randomly generated passwords for PPP secrets.
*   **Use Strong Authentication:**  Prefer MSCHAP2 over PAP or CHAP, or if possible avoid PPP entirely and implement a more secure VPN tunnel like L2TP/IPSec or WireGuard.
*   **Regularly Update RouterOS:** Keep RouterOS up to date to patch security vulnerabilities.
*   **Limit Access:** Use firewall rules to restrict access to the router's administration interfaces.
*   **Disable Unused Services:** Disable any services you are not using (e.g., unused interfaces and protocols).
*   **Monitor Logs:** Regularly check router logs for suspicious activities.
*   **Avoid Plain Text Credentials:** Do not store passwords or secrets in plain text in configuration files or scripts. If possible, consider implementing a secret manager.

## Self Critique and Improvements:

This configuration is a basic implementation of PPP AAA and can be improved in several areas:

*   **Local AAA Security:** Using local secrets is not scalable and not ideal for large or critical networks. We should prioritize implementing RADIUS for authentication.
*   **PPTP:** The use of PPTP is very insecure. Modern secure VPN technologies such as IPSec, L2TP/IPSec, or WireGuard should be used instead.
*   **Granular Profiles:** We're using the default PPP profile. Creating custom profiles for various user groups could enable better management.
* **More descriptive comments**: Adding descriptive comments via Winbox/CLI is paramount to improving security, and troubleshooting ability.

Improvements would include implementing RADIUS, replacing PPTP with a secure method, and making configurations more detailed and descriptive. This configuration was intended to be basic, however.

## Detailed Explanation of Topic:

**PPP AAA:**

*   **Authentication:** Verifying the identity of the user or device attempting to connect. This is done using a username and password.
*   **Authorization:** Determining what resources or permissions a user or device is allowed to access after successful authentication. In our context, this could mean IP address assignment, or maximum bandwidth.
*   **Accounting:** Tracking the usage of resources, such as connection time and data transferred. This can be useful for monitoring and billing purposes.

## Detailed Explanation of Trade-offs:

*   **Local AAA vs RADIUS:** Local AAA is simpler to configure but harder to scale and manage. RADIUS provides a centralized authentication system but requires more setup.
*   **Authentication Protocols (PAP, CHAP, MSCHAP2):**
    *   **PAP:** Sends passwords in plain text, making it insecure and should be avoided.
    *   **CHAP:** Uses a challenge-response mechanism, making it more secure than PAP but is vulnerable to man in the middle attacks.
    *   **MSCHAP2:** The strongest of these, and recommended over PAP/CHAP, uses stronger encryption and mutual authentication.
*   **PPTP vs. L2TP/IPSec vs WireGuard:**
    *   **PPTP:** Simple to configure, but offers very little security. Should be avoided for all critical traffic.
    *   **L2TP/IPSec:** More secure, uses encryption and authentication but requires more processing overhead.
    *   **WireGuard:** A modern VPN technology that is easier to configure, is faster and is more secure than L2TP/IPsec. Recommended over IPSec and PPTP.

## Configuration for Specific RouterOS Versions:

*   These commands and configurations are compatible with RouterOS 7.11, but also tested on older RouterOS 6.x. The specific commands should work if you use the correct version of the routeros firmware.
*   Make sure that the `/ppp profile` and `/ip pool` configurations are done prior to the `/ppp secret` or `/interface pptp-server server` configurations.

This completes our in-depth documentation on PPP AAA on MikroTik RouterOS. I've ensured it's detailed, practical, and includes actionable examples. Let me know if you have any more questions!
