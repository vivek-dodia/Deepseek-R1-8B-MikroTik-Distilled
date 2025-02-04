Okay, let's craft a comprehensive technical document for RADIUS authentication on a MikroTik router, focusing on an ISP-level configuration, targeting RouterOS 7.11 and utilizing a specific VLAN interface and subnet.

## Scenario Description:

This document details the implementation of RADIUS authentication for clients connecting to a VLAN interface on a MikroTik router. The scenario assumes an ISP environment where client authentication is handled by a centralized RADIUS server. Clients connecting via `vlan-77` (IP subnet `124.225.212.0/24`) will be authenticated against a RADIUS server before being granted network access. The RADIUS server will provide authentication (verifying credentials) and authorization (assigning specific IP addresses and policies). This setup is essential for managing user access, enforcing policies, and tracking network usage in an ISP setting.

## Implementation Steps:

### Step 1: Verify VLAN Interface
*   **Purpose:**  Ensure that the VLAN interface `vlan-77` is correctly configured and operational.
*   **Before Configuration:** We assume that interface `vlan-77` exists, however its configuration may not be correct.

    ```mikrotik
    /interface vlan print
    ```
    **Expected output**:
    ```
    Flags: X - disabled, R - running
    #   NAME    MTU  MAC-ADDRESS       VLAN-ID INTERFACE
    0   vlan-77 1500 XX:XX:XX:XX:XX:XX     77    ether1
    ```

*   **Action:** If it's not defined, create `vlan-77` on the parent interface.
    ```mikrotik
    /interface vlan add name=vlan-77 vlan-id=77 interface=ether1
    ```

*   **Explanation:** This command adds a VLAN interface named `vlan-77` with VLAN ID 77 on the physical interface `ether1`. Replace ether1 with your desired physical interface.
*   **After Configuration:** Verify that `vlan-77` now exists and has a running status if the parent interface is enabled:

    ```mikrotik
    /interface vlan print
    ```
    **Expected output**:
    ```
    Flags: X - disabled, R - running
    #   NAME    MTU  MAC-ADDRESS       VLAN-ID INTERFACE
    0   vlan-77 1500 XX:XX:XX:XX:XX:XX     77    ether1
    ```

    *Note: Ensure your physical interface is properly configured.*

### Step 2: Assign an IP Address to VLAN Interface
*   **Purpose:** Configure an IP address for the VLAN interface so the router can communicate on this subnet, even though DHCP will provide user addresses.
*   **Before Configuration:** The `vlan-77` interface may not have an IP address assigned.

    ```mikrotik
    /ip address print where interface=vlan-77
    ```
    **Expected Output:**
    ```
    # ADDRESS             NETWORK         INTERFACE
    ```
    (The above output shows that there is no IP on this interface)
*   **Action:** Add an IP address to the `vlan-77` interface. Choose a suitable IP for this router in that subnet. We'll use 124.225.212.1/24.

    ```mikrotik
    /ip address add address=124.225.212.1/24 interface=vlan-77
    ```

*   **Explanation:**  This command assigns the IP address `124.225.212.1/24` to the `vlan-77` interface. This IP will act as the default gateway for clients connecting to this VLAN.
*   **After Configuration:** Verify the IP address assignment.

    ```mikrotik
    /ip address print where interface=vlan-77
    ```
    **Expected Output:**

    ```
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS         NETWORK         INTERFACE
    0   124.225.212.1/24 124.225.212.0  vlan-77
    ```

### Step 3: Configure the RADIUS Server
*   **Purpose:**  Add the RADIUS server details to the router for authentication.
*   **Before Configuration:** There are no RADIUS servers configured in MikroTik.

    ```mikrotik
    /radius print
    ```
    **Expected Output:**
    ```
    #   ADDRESS        SECRET             SERVICE     TIMEOUT
    ```

*   **Action:** Add your RADIUS server.  Replace the IP `192.168.10.100` and `mysecret` with your specific RADIUS server IP and shared secret.

    ```mikrotik
     /radius add address=192.168.10.100 secret=mysecret service=ppp,login,hotspot timeout=3
    ```

*   **Explanation:**
    *   `address`: The IP address of the RADIUS server.
    *   `secret`: The shared secret used for communication with the RADIUS server.
    *   `service`: The services that will use this RADIUS configuration (we are using 'ppp' and 'login', and 'hotspot', but may change based on your use case).
    *   `timeout`: The timeout (in seconds) before a RADIUS request is considered failed.
*   **After Configuration:** Verify the RADIUS server has been added correctly.

    ```mikrotik
    /radius print
    ```
    **Expected Output:**

    ```
    Flags: X - disabled, I - invalid
    #   ADDRESS          SECRET       SERVICE        TIMEOUT
    0   192.168.10.100   mysecret     ppp,login,hotspot     3
    ```

### Step 4: Configure PPP Profile for RADIUS Authentication
*   **Purpose:**  Create a PPP profile that enforces RADIUS authentication for our VLAN.
*   **Before Configuration:** No relevant PPP profiles exist.

    ```mikrotik
    /ppp profile print
    ```
    **Expected output:**
    ```
     # NAME        USE-ENCRYPT AUTHENTICATION
    ```
*   **Action:** Create a new PPP profile for RADIUS auth for `vlan-77`:
     ```mikrotik
    /ppp profile add name=radius-vlan-77 use-encryption=yes only-one=no local-address=124.225.212.1 remote-address=pool-vlan-77 use-upnp=no dns-server=1.1.1.1,1.0.0.1 change-tcp-mss=yes address-list=""
    ```
    ```mikrotik
    /ppp profile set radius-vlan-77  authentication=pap,chap,mschap1,mschap2
    ```
    ```mikrotik
    /ip pool add name=pool-vlan-77 ranges=124.225.212.2-124.225.212.254
    ```
*   **Explanation:**
    *   `name`: Name of the PPP profile
    *   `use-encryption`:  Enables MPPE (Microsoft Point-to-Point Encryption) for connection security.
    *   `only-one`: Allows multiple simultaneous connections per user.
    *   `local-address`: the IP address of the local router interface.
    *   `remote-address`: the IP pool from which IPs will be distributed.
    *   `use-upnp`: disables universal plug and play.
    *   `dns-server`: sets DNS server for client connections.
    *   `change-tcp-mss`: enables TCP MSS clamping.
    *  `address-list`: list which can be used to provide additional policy.
    *   `authentication`: Sets the acceptable authentication methods (PAP, CHAP, MSCHAP1, MSCHAP2) for clients

*   **After Configuration:** Verify the new PPP profile was correctly created.

    ```mikrotik
    /ppp profile print
    ```
    **Expected Output:**
    ```
    Flags: X - disabled
     #   NAME           USE-ENCRYPT AUTHENTICATION
    0   radius-vlan-77 yes         pap,chap,mschap1,mschap2
    ```
    ```mikrotik
    /ip pool print
    ```
    **Expected Output:**
    ```
    Flags: X - disabled, I - invalid, D - dynamic
    #   NAME           RANGES
    0   pool-vlan-77   124.225.212.2-124.225.212.254
    ```

### Step 5: Create a PPP Secret that can be triggered by RADIUS auth.

* **Purpose:** A PPP Secret is required, even if RADIUS is used. We will create a default secret, that is not linked to a user.
* **Before Configuration**: No default secret has been configured.

  ```mikrotik
    /ppp secret print
    ```
    **Expected output:**
    ```
    # NAME        PROFILE   SERVICE  LOCAL-ADDRESS
    ```

* **Action**: Create a default secret that allows RADIUS to work on vlan-77:
    ```mikrotik
    /ppp secret add name=radius-default-secret service=ppp profile=radius-vlan-77
    ```
* **Explanation:**
    * `name`: name for this secret, which is not relevant, as RADIUS will provide the actual login information.
    * `service`: service type to which this secret applies.
    * `profile`: profile which will be triggered.
* **After Configuration**: Verify that a default secret was created:
    ```mikrotik
    /ppp secret print
    ```
    **Expected Output:**
    ```
    Flags: X - disabled
    #   NAME               PROFILE        SERVICE
    0   radius-default-secret radius-vlan-77 ppp
    ```

### Step 6: Enable PPP on the VLAN interface
*   **Purpose:** Activate the PPP server on the `vlan-77` interface
*   **Before Configuration:** The PPP interface is not configured.
     ```mikrotik
    /interface ppp server print
     ```
     **Expected Output:**
      ```
        # NAME  INTERFACE SERVICE PROFILE      MAX-MTU MAX-MRU MRRU
      ```
*   **Action:** Add ppp on the vlan-77 interface:
    ```mikrotik
    /interface ppp server add name=ppp-vlan-77 interface=vlan-77 service=ppp profile=radius-vlan-77 max-mtu=1500 max-mru=1500
    ```
*   **Explanation:**
    *   `name`: Assigning a name to this server
    *   `interface`:  The VLAN interface to enable PPP.
    *   `service`: The service type for this interface.
    *   `profile`: The PPP profile to be used.
    *   `max-mtu`: Maximum transmission unit.
    *   `max-mru`: Maximum receive unit.
*   **After Configuration:** Verify the PPP server is enabled on the interface.
    ```mikrotik
    /interface ppp server print
    ```
    **Expected Output:**
    ```
    Flags: X - disabled, I - invalid, D - dynamic
    #   NAME      INTERFACE SERVICE PROFILE      MAX-MTU MAX-MRU MRRU
    0   ppp-vlan-77 vlan-77    ppp   radius-vlan-77   1500    1500
    ```

## Complete Configuration Commands:

```mikrotik
# Step 1: Verify/Create VLAN
/interface vlan
add name=vlan-77 vlan-id=77 interface=ether1

# Step 2: Assign IP to VLAN
/ip address
add address=124.225.212.1/24 interface=vlan-77

# Step 3: Configure RADIUS server
/radius
add address=192.168.10.100 secret=mysecret service=ppp,login,hotspot timeout=3

# Step 4: Configure PPP Profile for RADIUS
/ip pool add name=pool-vlan-77 ranges=124.225.212.2-124.225.212.254
/ppp profile
add name=radius-vlan-77 use-encryption=yes only-one=no local-address=124.225.212.1 remote-address=pool-vlan-77 use-upnp=no dns-server=1.1.1.1,1.0.0.1 change-tcp-mss=yes address-list=""
/ppp profile
set radius-vlan-77 authentication=pap,chap,mschap1,mschap2

# Step 5: Add PPP Default Secret
/ppp secret
add name=radius-default-secret service=ppp profile=radius-vlan-77

# Step 6: Enable PPP Server on VLAN interface
/interface ppp server
add name=ppp-vlan-77 interface=vlan-77 service=ppp profile=radius-vlan-77 max-mtu=1500 max-mru=1500
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Verify IP connectivity between the router and the RADIUS server using `ping 192.168.10.100`.
        *   Check firewall rules on the router and on the network to allow RADIUS traffic (UDP ports 1812, 1813 or 1645, 1646).
        *   Confirm the RADIUS server is running and listening on the correct ports.
        *   Double-check the shared secret is identical on both the router and RADIUS server.
*   **Authentication Failures:**
    *   **Problem:** Clients cannot authenticate with the RADIUS server.
    *   **Solution:**
        *   Verify the username and password being sent by the client are correct and match the RADIUS server's database.
        *   Check the RADIUS server logs for more detailed failure information.
        *   Confirm the authentication protocols used in the PPP profile (`pap,chap,mschap1,mschap2`) are supported by the RADIUS server.
*   **IP Address Conflicts:**
    *   **Problem:** The router's IP address conflicts with other devices in the same subnet, or if the pool of addresses is incorrectly configured.
    *   **Solution:** Ensure that your router's IP address `124.225.212.1/24` is not used by another device on your network. Also make sure that your IP pool is large enough to support your clients. Verify IP address ranges in the `pool-vlan-77` configuration, and adjust to avoid overlap with other static IPs or dynamic pools.
*   **High CPU/Memory Usage:**
    *   **Problem:** Too many RADIUS requests cause the router to overload, or a bug in a specific router OS may cause this problem.
    *   **Solution:**
        *   Monitor router resource usage (`/system resource print`).
        *   Consider upgrading your router if resources are insufficient.
        *   If the resource usage is caused by too many clients, you can optimize RADIUS server performance, by limiting the amount of checks it performs. You can also look into upgrading your RADIUS server.
        *   Check that no rogue clients are trying to connect to the network with malicious intentions.
        *   Ensure you are running the latest version of RouterOS.
*   **Security Issue: Insecure Authentication Protocols**
    *   **Problem:** PAP protocol is very insecure, especially in an ISP environment.
    *   **Solution:**  Prioritize stronger authentication methods, such as CHAP and MSCHAP2. You can remove PAP from the list of protocols in the PPP profile `/ppp profile set radius-vlan-77 authentication=chap,mschap1,mschap2`

## Verification and Testing Steps:

1.  **Ping from Router:** Ensure the router can reach the RADIUS server.
    ```mikrotik
    /ping 192.168.10.100 count=4
    ```
    Successful output should show packet loss of 0%.
2.  **Client Connection:**
    *   Connect a client to the VLAN (either directly, or via a switch).
    *   Configure the client to use a PPP client and username and password credentials which are accepted by the radius server.
    *   Monitor the PPP active connections: `/interface ppp active print`
        *   A successful connection will be displayed here with an assigned IP address from `pool-vlan-77`.
    *   On the client device, use `ipconfig` (windows) or `ifconfig` (linux) to verify the IP address is on the correct subnet.
3.  **RADIUS Server Logs:** Check the RADIUS server logs to ensure the client is authenticating against the server. Success and failure logs should be visible.

4.  **Torch Tool:** Use the Torch tool to inspect the traffic for RADIUS communication.
    ```mikrotik
    /tool torch interface=ether1 port=1812,1813 protocol=udp
    ```
     This will display all UDP traffic destined to either RADIUS authentication or accounting ports on the server, this is helpful for debugging communication issues.

## Related Features and Considerations:

*   **RADIUS Accounting:** Configure RADIUS accounting to track client usage and billing. You'll need to configure the `service` parameter in `/radius` to also include `accounting` in addition to `ppp,login,hotspot`.
*   **Hotspot:** Use MikroTik's hotspot feature to enforce authentication for clients connecting via Wi-Fi. This can be coupled with RADIUS authentication for more robust control.
*   **User Manager:** Use MikroTik's User Manager package to manage client accounts and user details. User Manager integrates well with RADIUS and is suitable for smaller ISP implementations that require account self-service.
*   **Policy-Based Routing:** Leverage policy-based routing to apply QoS or other rules based on the user's IP address, especially with the `address-list` functionality on the PPP profile.
*   **Dynamic DNS Updates:** The RADIUS server could be configured to trigger dynamic DNS updates after successful client connections are established.

## MikroTik REST API Examples (if applicable):

The MikroTik REST API can be used to manage RADIUS settings. The following example is based on MikroTik RouterOS 7.11 API syntax:

**Adding a new RADIUS server (POST):**

*   **Endpoint:** `/ip/radius`
*   **Method:** `POST`
*   **JSON Payload (example):**
    ```json
    {
      "address": "192.168.10.100",
      "secret": "mysecret",
      "service": "ppp,login,hotspot",
      "timeout": 3
    }
    ```
    *   `address`: RADIUS server IPv4 address as string (required).
    *   `secret`: Shared secret key as string (required).
    *   `service`: Comma-separated list of service names to use with this RADIUS server: `ppp`, `login`, `hotspot`, `accounting` (required).
    *   `timeout`: Time in seconds to wait for a response from the RADIUS server, as number (required).
*   **Expected Response (200 OK):**
    ```json
    {
      ".id": "*12",
      "address": "192.168.10.100",
      "secret": "mysecret",
       "service": "ppp,login,hotspot",
      "timeout": "3"
    }
    ```
*  **Error Handling:** In case the operation fails, the MikroTik REST API may return a 4xx or 5xx error code with a JSON error description.
   ```json
   {
    "message": "already have radius with such address and secret"
   }
   ```

**Fetching all Radius Servers (GET):**

* **Endpoint:** `/ip/radius`
*   **Method:** `GET`
*   **JSON Payload (example):**
    ```json
    {
    }
    ```
    * No JSON payload required for this request
*   **Expected Response (200 OK):**
   ```json
   [
        {
            ".id": "*1",
            "address": "192.168.10.100",
            "secret": "mysecret",
            "service": "ppp,login,hotspot",
            "timeout": "3"
        }
    ]
   ```
*  **Error Handling:** In case the operation fails, the MikroTik REST API may return a 4xx or 5xx error code with a JSON error description.

**Updating an Existing RADIUS Server (PUT):**

*   **Endpoint:** `/ip/radius/*12`
*   **Method:** `PUT`
*  **JSON Payload (example):**
    ```json
    {
      "timeout": 5
    }
    ```
     *  `.id`: MikroTik ID of the object to update (required).
    *  `timeout`: The new timeout value (in seconds). Only this value will be updated.
*  **Expected Response (200 OK):**
   ```json
    {
        ".id": "*12",
        "address": "192.168.10.100",
        "secret": "mysecret",
        "service": "ppp,login,hotspot",
        "timeout": "5"
    }
    ```
*  **Error Handling:** In case the operation fails, the MikroTik REST API may return a 4xx or 5xx error code with a JSON error description.

**Deleting a RADIUS Server (DELETE):**

*   **Endpoint:** `/ip/radius/*12`
*   **Method:** `DELETE`
*  **JSON Payload (example):**
    ```json
    {
    }
    ```
    *  `.id`: MikroTik ID of the object to delete (required).
*  **Expected Response (200 OK):**
   ```json
    {
     "message": "successfully removed"
    }
    ```
*  **Error Handling:** In case the operation fails, the MikroTik REST API may return a 4xx or 5xx error code with a JSON error description.

*Note: Replace `*12` with the actual ID of the RADIUS server obtained via the API*. Be sure to obtain your router API token before attempting REST calls.

## Security Best Practices

*   **Strong Shared Secret:** Use a complex and unique secret for RADIUS communication. Never use a default or easy-to-guess secret.
*   **Secure RADIUS Server:** Hardening your RADIUS server with regular updates, strong passwords and security best practices are paramount. Ensure that only trusted devices are allowed to communicate with the RADIUS server.
*   **Authentication Protocol Choice:** Always prefer more secure authentication protocols like CHAP and MSCHAP2 over PAP to prevent credential sniffing.
*   **Access Control:**  Implement access lists on the VLAN to restrict access to services on the network to only authenticated users. Use the `address-list` function in the PPP profile to assign clients to address-lists which can then be filtered by the firewall.

## Self Critique and Improvements:

*   **Clarity:** Some explanations could benefit from more specific examples.
*   **Scalability:** The current configuration is for a single VLAN.  Multiple VLANs and their associated profiles, pools and secrets could be added, to expand the flexibility of the configuration.
*   **Documentation:**  Include diagrams showing the network topology.
*   **Advanced features:** Introduce rate limiting for connected users, to prevent over utilization of bandwidth by specific users.
*   **Security:** Include steps for hardening the router itself, not just RADIUS access.

## Detailed Explanation of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to a network. In the context of MikroTik, RADIUS is used to delegate the authentication process of users connecting via PPP, Hotspot or other services. A RADIUS server maintains user credentials and policies which are configured independently of the network infrastructure, making it more flexible and scalable. When a user attempts to connect, the MikroTik router forwards the authentication request to the configured RADIUS server. The server validates the credentials and if successful, provides authorization parameters. RADIUS can return client IP addresses, routes, policies or accounting parameters. This makes RADIUS a vital component for ISP networks and businesses requiring strict control of network access.

## Detailed Explanation of Trade-offs:

*   **PAP vs CHAP/MSCHAP2:**  PAP sends credentials in plain text, which makes it extremely susceptible to interception. CHAP and MSCHAP2 use hashing and challenge-response mechanisms, which are far more secure and should always be preferred.
*   **Local Authentication vs RADIUS:** Local authentication (creating user secrets on the router) is simpler to set up, but becomes impractical for large networks. RADIUS offers centralized management, and simplifies account management, but requires more initial setup.
*   **Single vs Multiple RADIUS Servers:** Using multiple RADIUS servers improves redundancy. If one server fails, the other can take over authentication tasks.
*   **Dynamic Address Allocation vs Static IP Assignment:** In a RADIUS-based system, you can assign static IPs or dynamic IPs. Static IP allocation simplifies things for specific clients which require the same IP, or for specific services that are IP specific. Dynamic assignment is good for situations where the IP of the connecting device is irrelevant.

## Configuration for Specific RouterOS Versions:
This configuration is valid for RouterOS 7.11.  If you are using an earlier version (e.g. 6.x), there might be slight variations in the syntax. Specifically some fields which are named slightly differently. Make sure you are using the latest stable release.

This document provides a comprehensive guide for implementing RADIUS authentication on a MikroTik router within an ISP context. It emphasizes clear instructions, security considerations, and troubleshooting steps, catering to an expert-level user.
