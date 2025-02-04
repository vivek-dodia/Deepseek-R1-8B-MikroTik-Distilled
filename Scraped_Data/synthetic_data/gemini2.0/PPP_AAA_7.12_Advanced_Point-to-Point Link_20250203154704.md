Okay, let's dive deep into a PPP AAA (Authentication, Authorization, and Accounting) implementation on a MikroTik RouterOS device, specifically for a point-to-point link using the provided subnet and interface.

## Scenario Description:

This scenario involves setting up PPP (Point-to-Point Protocol) authentication using a RADIUS server for a wireless point-to-point link between two MikroTik routers. The `wlan-63` interface will be the basis of the PPP tunnel, and we'll focus on the router acting as the PPP server. This setup ensures that only authorized peers can connect and provides auditing capabilities through accounting. We are focusing on **Advanced** configuration, assuming the user has intermediate networking experience.

## Implementation Steps:

Here's a step-by-step guide, explained using both CLI and Winbox where relevant:

**Before we start:**
* Make sure your router is accessible via CLI or Winbox.
* Ensure that you have a RADIUS server already configured and reachable from your MikroTik.
* The remote side (the PPP client) also needs appropriate settings to connect to this PPP server.

**1. Step 1: Configure the WLAN Interface**

* **Objective**: Ensure the `wlan-63` interface is configured for the point-to-point connection. This includes setting the mode, frequency, and security. The assumption is that this interface already exists and is enabled. This is **not** a step to define the specifics of a wireless link - only that one exists.
* **CLI Example Before:**

```mikrotik
/interface wireless print
```
   You should see the `wlan-63` listed among your interfaces.  If it does not exist, you must create and configure this interface first.
   
* **CLI Example After:**
   
   We will not reconfigure the wireless interface in this example since this isn't a wireless topic. It must exist, be configured, and be active.
   

**2. Step 2: Configure the RADIUS Client**

* **Objective**: Tell the router how to communicate with the RADIUS server for authentication and accounting.
* **CLI Example Before:**

```mikrotik
/radius print
```
   (Expect no configured RADIUS servers)

* **CLI Example After:**
   
   * Replace `your_radius_server_ip`, `your_shared_secret` and `your_radius_accounting_port` with the appropriate values for your environment.
   

```mikrotik
/radius add address=your_radius_server_ip secret=your_shared_secret service=ppp timeout=10s accounting-port=your_radius_accounting_port
```
   * **Explanation:**
    * `add`: Creates a new RADIUS client entry.
    * `address`: Specifies the IP address or hostname of the RADIUS server.
    * `secret`: The shared secret configured on both the RADIUS server and MikroTik.
    * `service`: Specifies the service type; `ppp` is needed for our point-to-point case.
    * `timeout`: Sets the maximum time to wait for a response from the RADIUS server.
    * `accounting-port`: Sets the port used for accounting packets (typically different from the authentication port).
    
* **Winbox GUI:** Navigate to `RADIUS` in the left sidebar. Click the plus sign `+` to add a new RADIUS entry. Fill out the address, secret, service (select `ppp`), timeout, and accounting port.

**3. Step 3: Create a PPP Secret (Optional, but Recommended for Local Back-Up)**

* **Objective:** If the radius server is unavailable (or failing), configure local secrets for authorization
* **CLI Example Before:**

```mikrotik
/ppp secret print
```
(Expect no PPP Secrets defined)

* **CLI Example After:**

```mikrotik
/ppp secret add name="test_user" password="test_password" service=any profile=default
```

* **Explanation:**
    * `add`: Creates a new PPP secret entry.
    * `name`: The username that can be used by the client to connect
    * `password`: The password that will be required by the client
    * `service`: The service type; `any` allows the user to connect to any ppp service
    * `profile`: PPP profile to assign to the user

* **Winbox GUI:** Navigate to `PPP -> Secrets` in the left sidebar. Click the plus sign `+` to add a new secret. Fill out the name, password, service (select `any`), and profile.

**4. Step 4: Configure PPP Server**
   
* **Objective**: Configure the router to act as a PPP server, specify the interface to use for PPP, and enable authentication/authorization.
   
* **CLI Example Before:**
   
```mikrotik
/interface ppp-server print
```
   (Expect no PPP Servers defined)
   
* **CLI Example After:**

```mikrotik
/interface ppp-server add authentication=pap,chap,mschap1,mschap2 default-profile=default enabled=yes interface=wlan-63 max-mru=1480 max-mtu=1480 name=ppp-server-1 service=async
```
* **Explanation:**
    * `add`: Creates a new PPP server entry.
    * `authentication`: Specifies the allowed authentication methods. `pap,chap,mschap1,mschap2` specifies a list of common auth types, RADIUS will use its own methods, and this can be omitted for a Radius-only approach.
    * `default-profile`: Sets the default PPP profile.
    * `enabled`: Enables the server.
    * `interface`: Specifies the interface to bind the PPP server to, which is `wlan-63`.
    * `max-mru`: The maximum receive unit.
    * `max-mtu`: The maximum transmission unit.
    * `name`: Gives a logical name to the interface.
    * `service`: The service being used, `async`.

* **Winbox GUI:** Navigate to `PPP -> PPP Server` in the left sidebar. Click the plus sign `+` to add a new server. Fill out the interface (`wlan-63`), profile (select `default` or your own), authentication methods, and enable the server.

**5. Step 5: Configure a PPP profile (if needed)**
   
* **Objective**: Define specific profile options for the PPP tunnel, this will define the IP ranges the server will provide, and DNS servers that will be sent to clients, among other settings.
   
* **CLI Example Before:**
   
```mikrotik
/ppp profile print
```
   (Expect only the `default` profile)

* **CLI Example After:**

```mikrotik
/ppp profile add dns-server=8.8.8.8,8.8.4.4 local-address=247.103.81.1 name=pppoe-profile-1 remote-address=247.103.81.2-247.103.81.254 use-encryption=yes
```

* **Explanation:**
    * `add`: Creates a new PPP profile entry.
    * `dns-server`: Sets the DNS server that will be passed to connected clients.
    * `local-address`: The IP that will be assigned to the PPP server interface.
    * `name`: Assign a logical name to this profile.
    * `remote-address`: The range of IPs that will be assigned to clients from this profile.
    * `use-encryption`: If the PPP link should use encryption

* **Winbox GUI:** Navigate to `PPP -> Profiles` in the left sidebar. Click the plus sign `+` to add a new profile. Fill out the `local-address`, `remote-address`, and DNS servers.

**6. Step 6: (Optional) Create a firewall rule for traffic within the tunnel**
   
* **Objective**: Create a firewall rule that permits traffic from the PPP server and connected peers to route traffic.
   
* **CLI Example Before:**
   
```mikrotik
/ip firewall filter print
```
   (Expect your current filter rules)

* **CLI Example After:**

```mikrotik
/ip firewall filter add action=accept chain=forward comment="Accept forwarding from PPP" in-interface=ppp-server-1
```

* **Explanation:**
    * `add`: Creates a new firewall rule.
    * `action`: Accept traffic matching these criteria
    * `chain`: The specific chain for matching the criteria, `forward` implies traffic from one interface to another
    * `comment`: A string comment for easy identification.
    * `in-interface`: The interface that this traffic should be coming in from.

* **Winbox GUI:** Navigate to `Firewall -> Filter Rules` in the left sidebar. Click the plus sign `+` to add a new rule. Set the `chain` as `forward`, `in-interface` as the ppp server interface and the action to `accept`.

## Complete Configuration Commands:

Here are the complete MikroTik CLI commands:

```mikrotik
/radius add address=your_radius_server_ip secret=your_shared_secret service=ppp timeout=10s accounting-port=your_radius_accounting_port
/ppp secret add name="test_user" password="test_password" service=any profile=default
/interface ppp-server add authentication=pap,chap,mschap1,mschap2 default-profile=default enabled=yes interface=wlan-63 max-mru=1480 max-mtu=1480 name=ppp-server-1 service=async
/ppp profile add dns-server=8.8.8.8,8.8.4.4 local-address=247.103.81.1 name=pppoe-profile-1 remote-address=247.103.81.2-247.103.81.254 use-encryption=yes
/ip firewall filter add action=accept chain=forward comment="Accept forwarding from PPP" in-interface=ppp-server-1
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable**:
    *   **Problem**: The router cannot communicate with the RADIUS server.
    *   **Solution**: Verify network connectivity, firewall rules, and RADIUS server settings (IP, shared secret, service port). Use the MikroTik `ping` tool and `torch` for troubleshooting connection issues to the RADIUS server. Check the RADIUS server logs for connection attempts from the MikroTik device.
*   **Incorrect Shared Secret**:
    *   **Problem**: The shared secret on the MikroTik and the RADIUS server do not match.
    *   **Solution**: Double-check the shared secret on both sides.
*   **Authentication Failures**:
    *   **Problem**: Client fails to authenticate against the RADIUS server, or no local fallback
    *   **Solution**: Ensure the username/password exists in the RADIUS server or in the local ppp secret, and is allowed to connect via PPP. Use the MikroTik `log` facility to view failed authentication attempts. Enable verbose RADIUS logging on the MikroTik by setting the topic to `radius,debug` to troubleshoot client authentication.
*   **Incorrect PPP Profile**:
     *   **Problem**: The client receives a non-routable IP from the server.
     *   **Solution**: The profile needs to define proper server, client and DNS IPs.
*  **MTU/MRU Mismatches**:
   *   **Problem**:  PPP connection is established but traffic may be dropped due to an MTU/MRU mismatch between client and server.
   *   **Solution**:  Ensure the client and server are configured for the same MTU/MRU values.  The values may need to be lowered if the ppp connection has additional overhead, such as encryption.
*   **High CPU Usage**:
    *   **Problem**:  Encryption or heavy traffic can lead to high CPU utilization, especially on lower-end MikroTik devices.
    *   **Solution**:  Enable hardware encryption offloading where possible on MikroTik devices that support it. Avoid over-subscribing the link.
*   **Security Issues**:
    *   **Problem**:  Using weaker authentication methods (PAP).
    *   **Solution**:  Prefer CHAP, MSCHAP1, MSCHAP2 or EAP over PAP if you must use PPP secrets for authentication and do not have a RADIUS server.

## Verification and Testing Steps:

1.  **Monitor Interface Status:**
    *   Check the `interface ppp-server` to see if a peer connects successfully.
    *   Use `/interface ppp-server monitor [ppp-server-1 name]` to see real-time information.
2.  **Ping:**
    *   From the client, ping the local address you specified in the PPP profile (`247.103.81.1`). If this works, the basic tunnel setup is working
    *   Ping other addresses on the connected side to verify routing via PPP.
3.  **Traceroute:**
    *   Use `traceroute` to trace the path to destinations on the network to which your tunnel is connecting.
4.  **Torch:**
    *   Use the `torch` command on your PPP server interface, to see if there is traffic being routed across the link (`/tool torch interface=ppp-server-1`).
    *  Use `torch` on your RADIUS server interface to see traffic between the router and the radius server.
5.  **Log Review:**
    *   Check the router's logs (`/log print`) for any errors related to authentication, PPP, or RADIUS.
    *   Enable more detailed RADIUS logging by setting the topic to `radius,debug`. This might cause higher CPU utilization if not handled by the device properly.

## Related Features and Considerations:

*   **PPP Profiles**: Use profiles to manage different PPP settings such as IP addressing, DNS settings, and compression on a per-user basis.
*   **VPN Options**: Consider other VPN protocols (e.g., L2TP, IPSec) depending on security needs and client compatibility.
*   **Policy-Based Routing**: Use policy-based routing to route specific traffic through the PPP tunnel.
*   **Bandwidth Control (Queues)**: Apply QoS rules to manage traffic over the PPP link.
*  **RADIUS Attributes**: Utilize RADIUS attributes for more granular control, such as VLAN assignments and other per-user settings.

## MikroTik REST API Examples (if applicable):

Here are a few examples of how to use the REST API for the above settings. In RouterOS, all calls are GET methods. The following examples should be treated as pseudo-code, and might need additional authentication for proper use.

**1. Adding a RADIUS Server:**

*   **API Endpoint:** `/ip/radius`
*   **Request Method:** GET
*   **Example JSON Payload (As a Query Parameter)**:

```json
 {
    "address": "your_radius_server_ip",
    "secret": "your_shared_secret",
    "service": "ppp",
    "timeout": "10s",
    "accounting-port": "1813"
}
```
*   **Expected Response (Successful Creation):**

```json
{
    "message": "Added radius",
    "id": "*3"
}
```

* **Explanation**: The api call is a GET call and has a query parameter. The parameters match the ones used in the CLI. If an error occurs, the server will return an error message.

**2. Getting RADIUS Server Configuration:**

*   **API Endpoint:** `/ip/radius`
*   **Request Method:** GET
*   **Example Request:** No payload

*   **Expected Response (Successful Retrieval):**

```json
[
    {
        ".id": "*3",
        "address": "your_radius_server_ip",
        "secret": "your_shared_secret",
        "service": "ppp",
        "timeout": "10s",
        "accounting-port": "1813",
        "authentication-port": "1812",
        "disabled": "false"
    }
]
```

* **Explanation**: This call returns an array of objects, with each object representing a RADIUS configuration.  A single entry is returned in this example.

**3. Getting a list of all existing PPP-Server configs**

*   **API Endpoint:** `/interface/ppp-server`
*   **Request Method:** GET
*   **Example Request:** No payload

* **Expected Response (Successful Retrieval):**
```json
[
   {
      ".id": "*1",
      "name": "ppp-server-1",
      "comment": "",
      "max-mru": "1480",
      "max-mtu": "1480",
      "interface": "wlan-63",
      "user": "",
      "password": "",
      "service": "async",
      "default-profile": "default",
      "authentication": "pap,chap,mschap1,mschap2",
      "keepalive-timeout": "60",
      "use-mpls": "no",
      "disabled": "false"
   }
]
```

* **Explanation**: This call returns an array of objects, with each object representing a PPP server configuration. A single entry is returned in this example.

**Error Handling:**

*   API errors are typically returned with a non-200 HTTP status code along with a JSON object describing the error.
*   Always check the status code of API responses.
*   Look at the `message` field in the error response for details about the failure.

## Security Best Practices:

*   **Shared Secret**: Use a strong, randomly generated shared secret for RADIUS. Change it periodically.
*   **Authentication**: Avoid PAP (Password Authentication Protocol) as it's not secure. Prefer CHAP, MSCHAPv2, or EAP.
*   **Encryption**: Use encryption on the PPP link (MPPE) to protect traffic from eavesdropping.
*   **Access Control**: Implement proper access control lists on your firewall to limit access to the PPP servers.
*   **Logging:** Keep detailed logs of authentication attempts to track potential issues and security incidents.
*   **Firmware**: Regularly update the MikroTik RouterOS firmware to the latest version to patch security vulnerabilities.

## Self Critique and Improvements:

*   **Abstraction:** While this implementation is detailed and specific, it can be made more robust with abstractions such as defining user groups, IP ranges or even custom policies. These could be handled within the RADIUS server itself to manage the network more dynamically.
*   **Dynamic DNS:** Dynamic DNS could be set up for situations where IP addresses are not static.
*   **Automation:** This manual process can be automated using scripts or configuration management tools (e.g., Ansible).
*   **Scalability:** While this setup works well for a point-to-point link, more advanced features would be needed to handle multiple concurrent connections, which could be handled via radius authentication and/or VRFs.

## Detailed Explanations of Topic:

**PPP AAA (Authentication, Authorization, and Accounting):**

*   **Authentication:** Verifies the identity of the user or device attempting to connect.
*   **Authorization:** Determines what resources or services the authenticated user is allowed to access.
*   **Accounting:** Tracks resource usage (e.g., connection time, bandwidth) for billing, auditing, or security purposes.
*   **RADIUS (Remote Authentication Dial-In User Service)**: A standard networking protocol used for AAA. A centralized server manages user credentials, simplifying user management and network security.
*   **PPP Secret**: A mechanism to allow connections based on a local account.  This is useful for situations where radius is not needed or unavailable.
*   **PPP Profile**: Defines parameters for ppp connections.  The profile specifies things like the range of remote IPs given to clients, DNS servers and other protocol settings.

## Detailed Explanation of Trade-offs:

*   **Local Secrets vs RADIUS**: Local secrets are easier to set up, but less scalable and not as secure for multiple connections. RADIUS provides greater security, centralized management, and advanced authorization features, but requires more complex setup and a separate server.
*   **Authentication methods (PAP,CHAP,etc)**: PAP is the least secure, since it sends the password in plain text. CHAP is more secure, as it uses a hash, making it harder to intercept credentials. MSCHAPv2 and EAP are even better for more security-sensitive situations.
*   **Encryption**: Encryption has a processing and overhead cost, but it ensures privacy and confidentiality over the wire.
* **MTU/MRU**: MTU/MRU has an important trade-off with regards to protocol overheads.  The MTU must be large enough to fit a data payload and protocol headers, such as for IPv4, PPP, and any encryption.
*   **CPU Utilization vs. Features**: The more features that are used (encryption, complex rules, advanced authentication), the higher the CPU utilization will be. It is a trade-off between complexity, performance and cost.
*  **Firewall rules**: Without firewall rules, traffic would not be allowed to flow from the PPP clients to the internet.  Each firewall rule adds additional processing overhead, so only rules that are necessary should be in place.

## Configuration for Specific RouterOS Versions:

The configurations provided here are compatible with RouterOS versions 6.48, 7.x and 7.12. MikroTik strives to provide a consistent configuration experience across versions, so that a command issued on RouterOS 6.x will largely have the same effect on 7.x.

This detailed documentation should give you a strong understanding of implementing PPP AAA using RADIUS on a MikroTik router. Be sure to test thoroughly in a lab environment before deploying any configuration changes to production networks. Remember to always adapt these examples to the specifics of your environment.
