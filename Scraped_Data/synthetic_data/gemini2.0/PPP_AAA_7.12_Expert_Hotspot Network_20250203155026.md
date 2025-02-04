Okay, let's dive into a detailed exploration of PPP AAA within a MikroTik Hotspot network, specifically targeting RouterOS 7.12. We'll aim for an expert-level understanding and provide practical, actionable configurations.

## Scenario Description:

This scenario focuses on implementing robust PPP authentication, authorization, and accounting (AAA) for a hotspot network. We'll use RADIUS as our AAA server, assuming it exists and is reachable by the MikroTik router. This allows us to centralize user management and enforce access policies. The hotspot network will be served on the `bridge-40` interface, with a subnet of `9.146.232.0/24`.

## Implementation Steps:

Here's a step-by-step guide to implementing PPP AAA with RADIUS on your MikroTik router:

### Step 1: Configure the Bridge Interface

Before configuring PPP, ensure the bridge interface is correctly set up and connected to your physical network. The bridge should include all interfaces that should provide Hotspot services on this subnet (e.g., wired and wireless).

**Before:**

```
/interface bridge print
# No relevant bridges are defined (or do not include the desired interface).
```
**Action:**

Use the following command in the MikroTik CLI to create the `bridge-40` interface and associate relevant interfaces:
```
/interface bridge
add name=bridge-40 protocol-mode=none
/interface bridge port
add bridge=bridge-40 interface=ether2 # Example Ethernet interface for clients
add bridge=bridge-40 interface=wlan1 # Example wireless interface for clients
```

*   `add name=bridge-40`: Creates a new bridge interface named `bridge-40`.
*   `protocol-mode=none`:  Disables Spanning Tree Protocol for this example, as it is not typically needed for a simple hotspot. In more complex situations, it could be beneficial to implement RSTP for redundancy.
*   `add bridge=bridge-40 interface=ether2`: Adds `ether2` to the `bridge-40`. Replace `ether2` with your specific Ethernet interface.
*   `add bridge=bridge-40 interface=wlan1`: Adds `wlan1` to the `bridge-40`. Replace `wlan1` with your specific wireless interface.

**After:**

```
/interface bridge print
Flags: X - disabled, R - running
 #    NAME      MTU   MAC-ADDRESS       ADMIN-MAC       ADDRESS            PROTOCOL PRIORITY
 0  R bridge-40 1500  AA:BB:CC:DD:EE:FF  AA:BB:CC:DD:EE:FF 0.0.0.0/0        none      0x8000

/interface bridge port print
Flags: X - disabled, I - inactive, D - dynamic
 #   INTERFACE     BRIDGE     PRIORITY PATH-COST   HORIZON
 0    ether2       bridge-40  0x80       10     none
 1    wlan1       bridge-40  0x80       10     none
```

**Effect:** Creates a logical bridge `bridge-40` allowing multiple interfaces to communicate with each other within the same subnet.

### Step 2: Configure the PPP Profile

A PPP profile defines the settings for PPP connections.

**Before:**

```
/ppp profile print
# No relevant profiles for our needs.
```

**Action:**

Create a new profile named `hotspot-profile` configured to use RADIUS authentication:

```
/ppp profile
add name=hotspot-profile local-address=9.146.232.1 remote-address=9.146.232.2-9.146.232.254 use-encryption=required only-one=yes use-compression=no change-tcp-mss=yes dns-server=9.146.232.1
```

*   `name=hotspot-profile`: The name of the profile.
*   `local-address=9.146.232.1`: The local address of the PPPoE server interface. This acts as the gateway for the remote connections.
*    `remote-address=9.146.232.2-9.146.232.254`: Defines the range of IP addresses assigned dynamically to clients.
*   `use-encryption=required`: Enforces encryption for all connections.
*  `only-one=yes`: Allows only one active connection per username.
*   `use-compression=no`: Disables compression (recommended as it's often inefficient with today's hardware).
* `change-tcp-mss=yes`: Adjusts the TCP MSS to prevent fragmentation
*  `dns-server=9.146.232.1`: Sets DNS servers assigned to the PPPoE clients.

**After:**

```
/ppp profile print
Flags: X - disabled, * - default
 #   NAME             LOCAL-ADDRESS   REMOTE-ADDRESS      CHANGE-TCP-MSS  USE-ENCRYPTION ONLY-ONE  USE-COMPRESSION
 0   hotspot-profile  9.146.232.1     9.146.232.2-9.146... yes           required      yes       no
```
**Effect:** Defines the IP settings and encryption settings, used when clients connect to the PPP server.

### Step 3: Configure RADIUS Client

This step involves configuring the MikroTik to communicate with the RADIUS server.

**Before:**

```
/radius print
# No RADIUS clients configured.
```

**Action:**
```
/radius
add address=192.168.100.1 secret="mysecret" service=ppp timeout=30
```
*   `add address=192.168.100.1`: IP address of your RADIUS server.
*   `secret="mysecret"`: Shared secret between the MikroTik and RADIUS server.  **Important**:  Change this to your actual secret.
*   `service=ppp`: Specifies that this RADIUS server is used for PPP service authentication.
* `timeout=30`: Sets the timeout value for RADIUS communication to 30 seconds.

**After:**

```
/radius print
Flags: X - disabled, I - invalid
 #   ADDRESS          SECRET      SERVICE    TIMEOUT
 0   192.168.100.1   xxxxxxxxxxx   ppp        30s
```

**Effect:** Configures the MikroTik to authenticate PPP users through the RADIUS server.

### Step 4: Configure the PPPoE Server

Finally, create the PPPoE server on the bridge interface.

**Before:**

```
/interface pppoe-server print
# No PPPoE servers configured.
```

**Action:**
```
/interface pppoe-server
add interface=bridge-40 service-name=hotspot-service profile=hotspot-profile disabled=no authentication=pap,chap,mschap1,mschap2 max-mtu=1480 max-mru=1480
```
*   `add interface=bridge-40`: Binds the PPPoE server to the bridge interface.
*  `service-name=hotspot-service`: Assigns a service name to the PPPoE server. This name must match the service being request by the PPPoE client.
*   `profile=hotspot-profile`: Associates the PPPoE server with the created profile.
*   `disabled=no`: Enables the PPPoE server.
*   `authentication=pap,chap,mschap1,mschap2`: Allows the specified authentication methods for compatibility.
*  `max-mtu=1480`: Sets the maximum MTU for PPPoE connections. This value is often 1480, as PPPoE adds 8 bytes overhead to the standard Ethernet MTU of 1500.
*  `max-mru=1480`: Sets the maximum MRU for PPPoE connections. This value must be equal or lower than MTU.

**After:**

```
/interface pppoe-server print
Flags: X - disabled, R - running
 #   INTERFACE   NAME             SERVICE-NAME  PROFILE         MAX-MTU MAX-MRU AUTHENTICATION
 0  R bridge-40  pppoe-hotspot  hotspot-service hotspot-profile   1480   1480   pap,chap,mschap1,mschap2
```
**Effect:** Enables the PPPoE server on the specified interface, using the defined profile and RADIUS for authentication.

## Complete Configuration Commands:

Here's a full set of commands to implement the configuration:

```
/interface bridge
add name=bridge-40 protocol-mode=none
/interface bridge port
add bridge=bridge-40 interface=ether2
add bridge=bridge-40 interface=wlan1

/ppp profile
add name=hotspot-profile local-address=9.146.232.1 remote-address=9.146.232.2-9.146.232.254 use-encryption=required only-one=yes use-compression=no change-tcp-mss=yes dns-server=9.146.232.1

/radius
add address=192.168.100.1 secret="mysecret" service=ppp timeout=30

/interface pppoe-server
add interface=bridge-40 service-name=hotspot-service profile=hotspot-profile disabled=no authentication=pap,chap,mschap1,mschap2 max-mtu=1480 max-mru=1480
```

## Common Pitfalls and Solutions:

*   **RADIUS Secret Mismatch:** If the RADIUS secret on the MikroTik doesn't match the one on the RADIUS server, authentication will fail. **Solution:** Double-check the secret on both systems. Use `/radius print` to verify the configured secret.
*   **Firewall Issues:** If a firewall on the MikroTik or on the RADIUS server blocks the communication, authentication will fail. **Solution:** Ensure port 1812/UDP (or 1813/UDP for accounting, if enabled) is open between the router and the RADIUS server. `/tool torch interface=ether1 port=1812` (Replace `ether1` with the relevant interface) can be used to check for RADIUS traffic.
*   **Incorrect RADIUS Server IP:** Ensure the IP address of the RADIUS server is correctly configured on the MikroTik router. **Solution:** Verify the configured IP address with `/radius print`.
*    **Incorrect PPP MTU and MRU:** Problems in clients connecting to the PPP server could be related to the configured MTU and MRU values. **Solution**:  Verify and adjust these parameters according to the network requirements, specifically for VPN or other tunneling protocols.
*   **PPPoE Client Issues:**  PPPoE clients must request the correct service name, as defined on the MikroTik server. **Solution**: Ensure the PPPoE client uses the same service name as specified in the server (`hotspot-service`).
*   **Profile Issues:** If the profile's settings, such as DNS servers, are not configured correctly, the clients will not get the necessary information to work properly. **Solution:** Double-check the profile settings in `/ppp profile print`.
*   **Resource Exhaustion:** A large number of PPP connections can cause high CPU or memory usage. **Solution:** Monitor system resources (`/system resource print`). If necessary, upgrade to a more powerful router or limit the number of concurrent connections.
*  **Security issues**: Using PAP as an authentication protocol for PPP can cause serious security issues. PAP transmits passwords in clear text.  **Solution**: Do not use PAP as an authentication method. Use CHAP or any more secure alternative. Always use the best encryption method supported by both client and server.
* **Accounting**: If accounting isn't implemented, there is no way to track or restrict user resource usage. **Solution**: Enable accounting via the `service` parameter in the `/radius` configuration.
*  **RADIUS Response timeout**: If the RADIUS server has slow response times, the connection can be dropped.  **Solution**: Adjust the timeout value via the `/radius` configuration.

## Verification and Testing Steps:

1.  **Check the PPPoE server is running:** `interface pppoe-server print` should show a status of 'R - running'.
2.  **Attempt a connection from a client:** Use a PPPoE client from another device connected to the bridged interface. The client should connect to the specified service name.
3.  **Verify IP Assignment:** After a successful connection, check the IP address assigned to the client via the MikroTik (`/ppp active print`). Also verify it is within the IP range assigned to the PPP profile.
4.  **RADIUS logs:** Verify the Radius server is receiving the requests and acting on them accordingly.
5.  **Ping Test:** From the connected device, ping the router's address on the PPP network (9.146.232.1). Also, ping an external IP address or hostname to verify Internet access.
6.  **Troubleshooting:** If the connection fails, consult the `/log print` on the MikroTik router for errors.  Use `/tool torch` to verify the traffic is reaching the RADIUS server.
7. **Accounting Verification**: If accounting is enabled, verify the server is receiving the accounting data from the MikroTik.

## Related Features and Considerations:

*   **Hotspot Feature:**  The MikroTik's built-in Hotspot feature provides a web-based login page with more complex user management, and is an alternative to PPPoE connections. However, with a radius server, both options provide the same level of flexibility in terms of AAA.
*   **User Manager:** The User Manager package on MikroTik provides an alternative to a standalone RADIUS server and can be used for less complex AAA implementations.
*   **VRF (Virtual Routing and Forwarding):** For larger networks, VRF can be used to separate traffic flows by network segments, ensuring more security and efficiency.
*   **Traffic Shaping:**  Using MikroTik's powerful Queue Tree or Simple Queue systems, you can limit per-user bandwidth based on a radius configuration.
*   **Scripting:**  You can implement dynamic changes based on RADIUS attributes, using MikroTik's scripting capabilities.

## MikroTik REST API Examples:

Unfortunately, you cannot create or modify all PPP settings directly via MikroTik's REST API. However, we can manage RADIUS settings.

**1. Add a RADIUS Server:**

*   **Endpoint:** `/ip/radius`
*   **Method:** POST
*   **JSON Payload:**

```json
{
    "address": "192.168.100.2",
    "secret": "newsecret",
    "service": "ppp",
    "timeout": "25"
}
```

*   **Expected Response:**

    ```json
    {
        "message": "added",
        "id": "*1" // the internal id of the created object
    }
    ```

    or:

    ```json
    {
        "message": "Error: item with such address already exists"
    }

    ```
*   **Explanation:**
    *   `address`: IP address of the RADIUS server.
    *   `secret`: Shared secret.
    *   `service`: "ppp" in this case
    *   `timeout`: The timeout value for Radius requests

**2. Get RADIUS Server List:**

*   **Endpoint:** `/ip/radius`
*   **Method:** GET
*   **Expected Response:**

    ```json
    [
        {
            ".id": "*0",
            "address": "192.168.100.1",
            "secret": "xxxxxxxxxx",
            "service": "ppp",
            "timeout": "30s",
            "invalid": "false"
        },
         {
            ".id": "*1",
            "address": "192.168.100.2",
            "secret": "xxxxxxxxxx",
            "service": "ppp",
            "timeout": "25s",
            "invalid": "false"
        }
    ]
    ```
*   **Explanation:**
    *   `.id`: The internal id of the object
    *   All other parameters are as described above.

**3. Edit a Radius Server:**

*  **Endpoint:** `/ip/radius/*1`
*   **Method:** PUT
*   **JSON Payload:**
```json
{
    "secret": "anothersecret"
}
```

* **Expected Response:**

    ```json
    {
        "message": "updated"
    }
    ```

**Important Notes:**

*   The API is more verbose than the CLI, requiring full names for parameters (e.g. `address`, `secret`).
*   You must authenticate via the API (typically using a token).
*   Error handling is crucial. A response with a "message" other than `added` or `updated` should be handled properly. For example, a duplicate ID error could be handled gracefully.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a long and complex secret.
*   **Restrict RADIUS Access:** Limit which IPs can connect to the RADIUS server.
*   **Encrypt Communications:** Use RADIUS over TLS (`radsec`) for added security, if your RADIUS server supports it.
*  **Disable PAP Authentication**: PAP sends passwords in clear text, and should be avoided.
* **Implement traffic filtering**: The PPP server and other parts of the network should be protected by a proper firewall configuration.
*  **Update RouterOS:** Keep RouterOS up to date to patch security vulnerabilities.
* **Accounting**: Using accounting will allow for more detailed logs and control over client resources.

## Self Critique and Improvements

*   The configuration is currently focused on a simple PPP setup with RADIUS for AAA. There are many other more complex configurations possible, with additional capabilities, such as using multiple radius servers.
*   The MTU and MRU can be dynamically changed and better adjusted, considering the specific network layout.
*   There is a need for better error handling in the RADIUS configuration, ensuring a smooth user experience.
*   Additional considerations must be made with specific authentication/encryption methods, depending on the client's hardware/software capabilities.
*   The use of a web-based authentication method, via a Hotspot interface, could be a more user-friendly approach for some deployments.
*   Scripting could be used to further automate the process and respond to RADIUS attributes and requests.
*  Advanced Queueing configurations can be implemented to enforce more granular bandwidth control.

## Detailed Explanations of Topic

*   **PPP (Point-to-Point Protocol):** PPP is a widely used protocol for establishing direct connections between two network nodes. It provides essential features such as authentication, encryption, and dynamic IP assignment. PPPoE is a variant of PPP, used for running PPP over Ethernet.
*   **AAA (Authentication, Authorization, and Accounting):**  AAA is a security framework that provides three critical functions:
    *   **Authentication:** Verifies the user's identity.
    *   **Authorization:** Determines what resources the user is allowed to access.
    *   **Accounting:**  Tracks resource consumption for monitoring and billing purposes.
*   **RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a widely used protocol that implements AAA services. A central RADIUS server maintains user credentials and access policies.
*   **PPPoE Server:** The PPPoE server accepts connections from PPPoE clients, and handles authentication, authorization and IP allocation.
*   **Bridge Interface:** A bridge interface allows multiple physical interfaces to act as a single logical interface, sharing the same subnet.
* **MTU and MRU:** Maximum Transmission Unit and Maximum Receive Unit, respectively, parameters that control the maximum size of the packets being transmitted in the network.

## Detailed Explanation of Trade-offs

*   **PPPoE vs. Hotspot:**  PPPoE provides direct access to network resources, requiring a client-side configuration. Hotspot utilizes web-based authentication, usually involving a captive portal. The choice depends on the desired user experience and the level of control needed. PPPoE is often used for VPN, or more specific requirements.
*   **RADIUS vs. User Manager:** The MikroTik User Manager is simpler to configure and is easier to manage. However, RADIUS is more scalable, robust, and provides more advanced functionalities, especially if integration with other systems is required.
*   **Authentication Methods:** PAP sends passwords in plain text (insecure), while CHAP/MSCHAP provide more security. Always prioritize stronger encryption methods if available.
*   **Encryption:**  Enable encryption to protect the confidentiality of the data being transmitted over PPP connections.
*  **Connection type limitations**: Not all devices can support PPPoE, so the type of device must be considered when planning a solution.

## Configuration for Specific RouterOS Versions:

This configuration is targeted at RouterOS 7.12, and can work in 7.x. If using other versions, please be mindful of possible differences in features and available settings. However, the basic functionality should remain similar. For example, in ROS 6.x, the command `interface pppoe-server` was located under `/interface ppp`.

This detailed explanation provides a thorough understanding of PPP AAA within a MikroTik Hotspot network, including practical configurations, troubleshooting advice, and API examples. Let me know if you have more questions or want to explore specific aspects further!
