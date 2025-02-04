Okay, let's craft a detailed documentation for PPP AAA on a MikroTik RouterOS 7.12 (and mostly compatible with 6.48 and other 7.x releases), focusing on an SOHO environment with a 2.177.86.0/24 subnet on interface ether-36. This will be an advanced configuration, not for novices.

## Scenario Description:

We will configure a MikroTik router to act as a PPP server, providing secure access to the 2.177.86.0/24 network via PPPoE or PPTP. We will implement RADIUS-based AAA (Authentication, Authorization, and Accounting) using a separate RADIUS server, allowing us to centrally manage user credentials and track usage. This setup is often used in SOHO environments to provide VPN access to resources on the LAN while ensuring proper authorization and accounting.

## Implementation Steps:

### **Step 1**: Configure the IP Address on ether-36.

Before anything else, let’s make sure the interface you will assign clients is correctly configured.

*   **Initial state**: We assume the interface *ether-36* is either not configured or has an unrelated IP address.
*   **Goal**: Assign IP address 2.177.86.1/24 to the interface *ether-36* to use as the gateway for the PPP clients.

**CLI Instructions:**
    
    ```mikrotik
    /ip address
    add address=2.177.86.1/24 interface=ether-36
    ```

**Winbox GUI:**
   
    * Navigate to "IP" -> "Addresses".
    * Click the "+" button to add a new address.
    * In the "Address" field, enter 2.177.86.1/24.
    * Select "ether-36" in the "Interface" dropdown.
    * Click "OK".

**Expected Output:**

*   `ip address print` before: No address on ether-36 or an unrelated address
*   `ip address print` after:
    ```
    #   ADDRESS            NETWORK       INTERFACE
    0   2.177.86.1/24       2.177.86.0    ether-36
    ```

### **Step 2**: Configure a RADIUS Server Connection

*   **Initial state:** No RADIUS server is configured.
*   **Goal**: Add a RADIUS server configuration for AAA.

**CLI Instructions:**

    ```mikrotik
    /radius
    add address=192.168.88.100 secret=mysecret service=ppp timeout=3
    ```

**Winbox GUI:**

* Navigate to "RADIUS".
* Click the "+" button to add a new RADIUS entry.
* In the "Address" field, enter 192.168.88.100.
* In the "Secret" field, enter `mysecret`.
* In the "Service" select `ppp`.
* Set the "Timeout" field to `3`.
* Click "OK".

**Expected Output:**
*   `radius print` before: No RADIUS server configured
*   `radius print` after:
    ```
    # ADDRESS        SECRET    SERVICE     TIMEOUT
    0 192.168.88.100 mysecret  ppp         3
    ```
**Explanation**
   * `address=192.168.88.100`: This specifies the IP address of your RADIUS server. Replace with the actual IP.
   * `secret=mysecret`: This sets the shared secret key used for communication between the MikroTik router and the RADIUS server. Replace `mysecret` with a strong, secure password. This must match the shared secret on the RADIUS server.
   * `service=ppp`: Specifies that this RADIUS server configuration is to be used for PPP services (PPPoE, PPTP).
   * `timeout=3`: Sets the maximum time (in seconds) to wait for a response from the RADIUS server before considering the server unavailable.
   
**Note:** The RADIUS server will need to have users configured, and be able to process accounting messages.
   
### **Step 3**: Configure a PPP Profile

*   **Initial state:** No PPP profile exists that uses RADIUS for authentication.
*   **Goal**: Create a PPP profile to define settings for PPP clients including local address pool and RADIUS-based authentication.

**CLI Instructions:**

    ```mikrotik
    /ppp profile
    add name=pppoe-radius use-encryption=yes local-address=2.177.86.2 \
    remote-address=2.177.86.0/24 \
    use-radius=yes
    ```

**Winbox GUI:**
* Navigate to "PPP" -> "Profiles" tab
* Click the "+" button to add a new profile.
* In the "Name" field, enter "pppoe-radius".
* Check "Use Encryption".
* In the "Local Address" field, enter 2.177.86.2.
* In the "Remote Address" field, enter 2.177.86.0/24
* Check "Use Radius".
* Click "OK".

**Expected Output:**

*   `ppp profile print` before: No profile for RADIUS auth
*   `ppp profile print` after:
    ```
    # NAME         USE-ENC LOCAL-ADDRESS   REMOTE-ADDRESS      USE-RADIUS
    0 pppoe-radius yes     2.177.86.2     2.177.86.0/24         yes
    ```
**Explanation**
*   `name=pppoe-radius`: The descriptive name for your profile.
*   `use-encryption=yes`: Enables encryption for the PPP connection (MPPE for PPTP, or encryption offered by the client).
*   `local-address=2.177.86.2`: The IP address that will be assigned to the MikroTik PPP interface (not the client). This IP is used as the next hop on the client network.
*   `remote-address=2.177.86.0/24`: The IP address pool or range that will be allocated to the connecting PPP clients. The MikroTik router will pull addresses from this range for clients connecting with this profile.
*   `use-radius=yes`:  Enables the use of RADIUS server for authenticating users.

### **Step 4**: Configure a PPP Server (PPPoE)

*   **Initial state:** No PPPoE server is active.
*   **Goal**:  Enable the PPPoE server on interface *ether-36*, using the *pppoe-radius* profile.

**CLI Instructions:**
```mikrotik
/ppp server pppoe
add service-name=pppoe-radius-service interface=ether-36 profile=pppoe-radius max-mru=1480 max-mtu=1480 enabled=yes
```

**Winbox GUI:**
* Navigate to "PPP" -> "PPPoE Servers" tab
* Click the "+" button to add a new PPPoE server.
* In the "Service Name" field, enter "pppoe-radius-service".
* Select "ether-36" in the "Interface" dropdown.
* Select "pppoe-radius" in the "Profile" dropdown.
* Set "Max MRU" to `1480`.
* Set "Max MTU" to `1480`.
* Check the "Enabled" box.
* Click "OK".

**Expected Output:**
*   `/ppp server pppoe print` before: No PPPoE service is active
*   `/ppp server pppoe print` after:
    ```
    #   INTERFACE  SERVICE-NAME     PROFILE     MAX-MTU  MAX-MRU  MRU    MRRU  ONE-SESSION
    0 ether-36   pppoe-radius-service pppoe-radius    1480     1480   1480  1600      no
    ```

**Explanation**
    * `service-name=pppoe-radius-service`: The name of this service, as advertised to PPPoE clients.
    * `interface=ether-36`: The interface on which the PPPoE service listens for new client connections.
    * `profile=pppoe-radius`: The PPP profile defined in Step 3 to be used.
    * `max-mru=1480`, `max-mtu=1480`: These settings ensure correct and consistent packet size, and avoids fragmentation in most cases. MTU/MRU are usually configured to be just under the maximum of 1500 bytes for common ethernet networks.
    * `enabled=yes`: Enables the server to accept new connections.

**Note**: if you need to support PPTP for legacy clients, you would add similar configuration under `/ppp server pptp`.

### **Step 5**:  (Optional) Add a firewall rule for PPP connections

*   **Initial state**: You may or may not have rules in place allowing the PPP connections,
*   **Goal**: Allow PPP connections

**CLI Instructions**
```mikrotik
/ip firewall filter
add chain=input connection-type=pptp action=accept comment="Allow PPP" disabled=no
add chain=forward connection-type=pptp action=accept comment="Allow PPP" disabled=no
add chain=input protocol=tcp dst-port=1723 action=accept comment="Allow PPTP" disabled=no
add chain=forward protocol=gre action=accept comment="Allow GRE" disabled=no
add chain=input protocol=tcp dst-port=8291 action=accept comment="Allow Winbox" disabled=no
```

**Winbox GUI:**

* Navigate to IP -> Firewall -> Filter Rules
* Click the "+" button to add a new rule.
    * Chain: input
    * Connection Type: pptp
    * Action: accept
    * Comment: Allow PPP
    * Disabled: No
* Click the "+" button to add a new rule.
    * Chain: forward
    * Connection Type: pptp
    * Action: accept
    * Comment: Allow PPP
    * Disabled: No
* Click the "+" button to add a new rule.
    * Chain: input
    * Protocol: tcp
    * Dst Port: 1723
    * Action: accept
    * Comment: Allow PPTP
    * Disabled: No
* Click the "+" button to add a new rule.
    * Chain: forward
    * Protocol: gre
    * Action: accept
    * Comment: Allow GRE
    * Disabled: No
* Click the "+" button to add a new rule.
    * Chain: input
    * Protocol: tcp
    * Dst Port: 8291
    * Action: accept
    * Comment: Allow Winbox
    * Disabled: No

**Expected Output:**

*   `/ip firewall filter print` before: Your current firewall rules.
*   `/ip firewall filter print` after: Added rules as above.

**Explanation**
  * This rule allows the establishment of a PPTP connection, as well as allowing the traffic to pass.
  * Note: replace protocol and connection type based on the particular type of PPP server you are using.
  * Note: the last rule is optional and allows winbox access (use only when required).

## Complete Configuration Commands:

Here is the complete set of commands to implement the described setup:

```mikrotik
/ip address
add address=2.177.86.1/24 interface=ether-36
/radius
add address=192.168.88.100 secret=mysecret service=ppp timeout=3
/ppp profile
add name=pppoe-radius use-encryption=yes local-address=2.177.86.2 remote-address=2.177.86.0/24 use-radius=yes
/ppp server pppoe
add service-name=pppoe-radius-service interface=ether-36 profile=pppoe-radius max-mru=1480 max-mtu=1480 enabled=yes
/ip firewall filter
add chain=input connection-type=pptp action=accept comment="Allow PPP" disabled=no
add chain=forward connection-type=pptp action=accept comment="Allow PPP" disabled=no
add chain=input protocol=tcp dst-port=1723 action=accept comment="Allow PPTP" disabled=no
add chain=forward protocol=gre action=accept comment="Allow GRE" disabled=no
add chain=input protocol=tcp dst-port=8291 action=accept comment="Allow Winbox" disabled=no
```

## Common Pitfalls and Solutions:

1.  **RADIUS Secret Mismatch**:
    *   **Problem**: If the shared secret on the MikroTik doesn't match the RADIUS server, authentication will fail.
    *   **Solution**: Double-check the shared secret on both the MikroTik and the RADIUS server.
2.  **RADIUS Server Unreachable**:
    *   **Problem**: The MikroTik cannot communicate with the RADIUS server due to network issues or the server being down.
    *   **Solution**: Verify network connectivity, use `ping` from the MikroTik to the RADIUS server, and ensure the RADIUS server is active and listening on the correct port. Ensure the MikroTik has a gateway configured.
3.  **Firewall Blocks RADIUS or PPP**:
    *   **Problem**: Firewalls on the MikroTik or the RADIUS server prevent communication.
    *   **Solution**: Review your firewall rules. Allow traffic to/from the RADIUS server's IP on the appropriate ports (1812/1813 for auth/accounting). Add rules to allow PPP traffic as per Step 5 above.
4.  **Incorrect PPP Profile Settings**:
    *   **Problem**: If the local/remote address settings in the PPP profile are not appropriate, IP conflicts will arise.
    *   **Solution**: Double-check the local and remote address ranges, and ensure they do not overlap with other networks.
5.  **Resource Exhaustion**:
    *   **Problem**: High number of clients simultaneously can cause memory and cpu issues.
    *   **Solution**: Monitor the system resources (CPU, RAM). For more users consider upgrading the router, or limiting the amount of concurrent connections.

## Verification and Testing Steps:

1.  **RADIUS Server Connectivity**:
    *   Use the MikroTik command `tool fetch url="radius://192.168.88.100" secret="mysecret" username="testuser" password="testpassword" type="radius"`.  You should see an `ok` response if the server is reachable and has been able to authenticate the user. This command does not exist in v6.
2.  **PPP Connection**:
    *   Use a PPP client (e.g. a computer, mobile phone) to connect to the MikroTik router using the configured username, password and service name. Use a client configured to authenticate using PPPoE (or the server you configured)
3.  **Successful Connection**:
    *   Check `/ppp active print` on the MikroTik to see the active PPPoE connections.
4.  **Check IP Addresses**:
    *   Use `ip address print` to make sure the correct address has been assigned to the PPP client. Use `ip route print` to check routing, especially the default route.
5.  **Network Reachability**:
    *   From the PPP client, ping `2.177.86.1`, as well as any local devices on your network to ensure proper routing.
6.  **RADIUS Accounting**:
    *   Monitor accounting records on the RADIUS server. Verify start/stop events and session details are being recorded correctly.

## Related Features and Considerations:

*   **Hotspot**: Consider using MikroTik Hotspot functionality if you need to provide captive portal services.
*   **User Management**: Leverage `/user` command to configure local user accounts as a backup in case of RADIUS server unavailability.
*   **IP Pools**: If you require more complex address management, use `/ip pool` to define specific IP address ranges.
*   **VLANs**: Use VLANs for more complex segmentation by assigning each client/service on a different VLAN.
*   **Queueing/QOS**: Set up QoS rules if you wish to limit or prioritize certain clients.
*   **Security**: Limit access to the winbox service to the IP addresses that need it. Disable services on interfaces they are not required on.

## MikroTik REST API Examples:
**Note:** The MikroTik REST API is introduced in RouterOS v7. Replace your router IP address below. These examples assume the API user is authenticated through a session token.

**Retrieve RADIUS Configuration:**

```json
#Request
GET https://192.168.1.1/rest/radius
```
```json
#Response
[
  {
      ".id": "*0",
      "address": "192.168.88.100",
      "secret": "mysecret",
      "service": "ppp",
      "timeout": "3",
      "authentication": "yes",
      "accounting": "yes",
      "disabled": "no"
  }
]

```

**Add RADIUS Server:**

```json
#Request
POST https://192.168.1.1/rest/radius
Content-Type: application/json

{
  "address": "192.168.88.101",
  "secret": "newsecret",
  "service": "ppp",
  "timeout": "5"
}
```
```json
#Response
{
   "message": "added",
   "id": "*1"
}
```
**Note:**

*  The `id` is always required when updating a specific entry.
* If there is an error when adding/updating a record, it will be included in the JSON response. Handle accordingly.

## Security Best Practices:
   *  Use strong, complex shared secrets for RADIUS communication.
   *  Ensure your RADIUS server is kept secure and up-to-date.
   *  Limit the IP addresses that can access the RADIUS server.
   *  Implement robust firewall rules on your MikroTik router.
   *  Use encryption for PPP connections.
   *  Disable services if not needed.
   *  Use `ssh` for secure management and disable winbox/api on any public facing interfaces if not necessary.

## Self Critique and Improvements:

*   **Scalability:** This configuration is suitable for small networks. For larger networks, consider using a dedicated RADIUS server and more advanced IP address management.
*   **High Availability:** This configuration has no redundancy. For production, ensure redundant hardware and infrastructure for critical services.
*   **Flexibility:** This solution assumes a single type of PPP setup. If a more complex setup with different authentication schemes is needed, use multiple PPP profiles.
*   **Monitoring**: More monitoring such as connection rates, failed connections could be improved.
*   **Logging:** Improve logging in the router.

## Detailed Explanations of Topic

### PPP AAA (Authentication, Authorization, and Accounting):

*   **Authentication:** Verifies the identity of the connecting client. In our case, it’s done via RADIUS where the user's username and password are sent to a centralized server for validation.
*   **Authorization:** Determines what resources and services a user is allowed to access after successful authentication. The RADIUS server can send attributes to the MikroTik router to define these policies.
*   **Accounting:** Tracks the usage of the services by the users, such as connection start/stop time, traffic volume, etc. This data can be used for billing purposes, auditing or usage analysis.

### RADIUS (Remote Authentication Dial-In User Service)
    * Is a protocol to centralize authentication, authorization and accounting.
    * Allows all of those services to be managed from a centralized server.
    * RADIUS clients, such as our MikroTik router, send authentication requests to the RADIUS server.
    * The RADIUS server returns a success/fail message, and additional configuration parameters.
    * RADIUS supports several protocols: PAP, CHAP, EAP

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication**:
    *   **Local:** Simple setup, user accounts are managed on the router itself. Suitable for small, static networks.
    *   **RADIUS**: More complex setup, user accounts managed on a centralized server. Better for larger networks needing centralized user management and potentially billing or quota enforcement.
*   **Encryption**:
    *   **With Encryption**: More secure connection, data is encrypted. Increases CPU load on the router and client.
    *   **Without Encryption**: Less CPU overhead, but less secure, data is sent as plaintext. Only suitable for trusted networks.
*   **MTU/MRU**:
    *   **Higher MTU/MRU**: Potentially better throughput, but may lead to fragmentation issues in the network.
    *   **Lower MTU/MRU**: Avoids fragmentation but might reduce throughput if a too small size is set.

## Configuration for Specific RouterOS Versions:

This configuration was designed for MikroTik RouterOS 7.12. This configuration will be compatible with 6.48 and other 7.x versions.

*   **RouterOS v6**: The primary difference in v6 is that the `/rest` API is not available. You would manage it from command-line or Winbox.
*   **RouterOS v7**: v7 introduced the rest API. Be aware of the changes between minor version updates.

By following these detailed steps and explanations, you should be able to successfully implement a PPP server with RADIUS-based AAA on your MikroTik router. Remember to adapt the configuration to suit your specific network environment and security requirements.
