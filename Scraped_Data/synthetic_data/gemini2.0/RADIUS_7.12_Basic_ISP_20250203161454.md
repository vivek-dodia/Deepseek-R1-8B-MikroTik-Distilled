Okay, let's craft a comprehensive documentation for RADIUS authentication on a MikroTik router, targeting RouterOS 7.12, within an ISP context, specifically focusing on the given parameters (subnet 21.144.11.0/24 and interface ether-34).

## Scenario Description:

This scenario describes a basic RADIUS setup for authenticating users connecting to the network via interface `ether-34`. The IP addresses assigned to these users will be dynamically assigned from a DHCP server operating on the subnet 21.144.11.0/24. The MikroTik router will act as a RADIUS client, communicating with a separate RADIUS server to validate credentials before allowing network access. This setup is suitable for an ISP environment where user authentication is required before granting internet access.

## Implementation Steps:

**Before Configuration:**
* **Initial Router State:** Assuming a basic MikroTik configuration with IP addresses configured on other interfaces (e.g., WAN interface) and a general router functionality.
* **RADIUS Server:** A functional RADIUS server is assumed to be running and accessible from the MikroTik router. For this example, we will assume an IP address of `192.168.88.100` and a shared secret of `testing123`.
* **DHCP Server:** It's also assumed that a basic DHCP server is available and working on the subnet `21.144.11.0/24`

1.  **Step 1: Configure the RADIUS Client**
    * **Action:** Define the RADIUS server details on the MikroTik router.
    * **CLI Command:**
        ```mikrotik
        /radius add address=192.168.88.100 secret="testing123" service=ppp,hotspot,dhcp timeout=3
        ```
        * **Explanation:**
            * `address=192.168.88.100`:  Specifies the IP address of the RADIUS server.
            * `secret="testing123"`:  Sets the shared secret key used for secure communication with the RADIUS server. **Important: Use a strong, complex secret in production.**
            * `service=ppp,hotspot,dhcp`:  Specifies the services that will use this RADIUS server (PPP, Hotspot, and DHCP, in this case).
            * `timeout=3`: Sets the connection timeout for communication with the RADIUS server in seconds.
    * **Winbox GUI:** Go to *RADIUS* menu, add a new entry and fill out the corresponding fields.
    * **Before:** No RADIUS client configuration.
    * **After:**  The MikroTik router now knows how to communicate with the RADIUS server.
    * **Expected Effect:** The router will attempt to establish a connection (though no authentication is triggered yet).

2.  **Step 2: Configure the DHCP Server to use RADIUS**
    *   **Action:**  Modify the DHCP server settings to enable RADIUS authentication for leases.
    *   **CLI Command:**
        ```mikrotik
        /ip dhcp-server set 0 use-radius=yes
        ```
        * **Explanation:**
            * `set 0`: Select the default DHCP server to edit, which might differ based on the order of creation in your RouterOS configuration. You can use `/ip dhcp-server print` to find the ID of the DHCP server you wish to modify. You should see the following, before running the command:
            ```
              0  name="dhcp1" interface=ether34 address-pool=dhcp_pool1 authoritative=yes lease-time=10m add-arp=yes use-radius=no
            ```
            * `use-radius=yes`: Enables the RADIUS server to handle the authentication of clients who request a DHCP lease.
    *   **Winbox GUI:** Go to *IP -> DHCP Server* and select the dhcp server for interface *ether-34*. On the "General" Tab, enable "Use RADIUS".
    *   **Before:** DHCP server is not configured to use RADIUS.
    *   **After:** DHCP leases will now be authenticated via the RADIUS server.
    *   **Expected Effect:**  Clients requesting DHCP leases on `ether-34` will trigger a RADIUS authentication attempt by the router.

3.  **Step 3:  Create a DHCP Network**
    *   **Action:**  If no DHCP network exists, it must be created, and tied to the desired interface.
    *   **CLI Command:**
        ```mikrotik
        /ip dhcp-server network add address=21.144.11.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=21.144.11.1
        /ip dhcp-server network set 0 domain=local
        /ip dhcp-server set 0 interface=ether-34
        ```
        * **Explanation:**
            *   `add address=21.144.11.0/24`: Defines the network associated to the DHCP server, in this case `21.144.11.0/24`
            *   `dns-server=8.8.8.8,8.8.4.4`: Set's the DNS for all devices that will use this DHCP server, Google's DNS are used as an example.
            *   `gateway=21.144.11.1`: The default gateway for the clients on the network.
            *   `set 0 domain=local`:  Sets the DHCP domain name to `local`
            *   `set 0 interface=ether-34`:  Assigns the DHCP Server to interface `ether-34`.
    *   **Winbox GUI:** Go to *IP -> DHCP Server* and select the "Networks" tab, add an entry.
        After the "Networks" Tab is configured, click on the DHCP Server itself, under the "General" Tab, assign it to the specific interface.
    *   **Before:** DHCP server is not configured with a network configuration.
    *   **After:**  Clients on the specified interface will now obtain leases from the DHCP server, authenticated by the RADIUS server.
    *   **Expected Effect:**  Clients requesting DHCP leases on `ether-34` will receive a valid address within the subnet.

4. **Step 4: Optional - Configure DHCP Leases**
   * **Action:**  Set DHCP leases to a specific address range to improve security and maintain control over IPs being assigned on the network.
   * **CLI Command:**
        ```mikrotik
        /ip pool add name="dhcp_pool1" ranges=21.144.11.20-21.144.11.200
        /ip dhcp-server set 0 address-pool=dhcp_pool1
        ```
        * **Explanation:**
            * `add name="dhcp_pool1" ranges=21.144.11.20-21.144.11.200`: Creates an IP address pool named "dhcp_pool1" with an IP range of 21.144.11.20 to 21.144.11.200.
            * `/ip dhcp-server set 0 address-pool=dhcp_pool1`: Assigns the created pool to the DHCP server.
   * **Winbox GUI:** Go to *IP -> Pool*, and add an address pool, with the desired name and IP range.
      Then go to *IP -> DHCP Server* and on the "General" tab, assign the created address pool under "Address Pool".
   * **Before:** DHCP Server is using the entire subnet for dynamic address allocations.
   * **After:**  DHCP Server is now assigning IPs within the specified range.
   * **Expected Effect:** DHCP Leases will only be assigned within the configured range.

## Complete Configuration Commands:

```mikrotik
/radius add address=192.168.88.100 secret="testing123" service=ppp,hotspot,dhcp timeout=3
/ip dhcp-server set 0 use-radius=yes
/ip dhcp-server network add address=21.144.11.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=21.144.11.1
/ip dhcp-server network set 0 domain=local
/ip dhcp-server set 0 interface=ether-34
/ip pool add name="dhcp_pool1" ranges=21.144.11.20-21.144.11.200
/ip dhcp-server set 0 address-pool=dhcp_pool1
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:**  The MikroTik router cannot communicate with the RADIUS server.
    *   **Solution:** Verify that the RADIUS server IP address is correct. Ensure that there are no firewall rules blocking the traffic between the router and the RADIUS server (e.g., on the router or the network). Double-check that the shared secret is identical on both the RADIUS server and the MikroTik. Use ping or traceroute from the MikroTik to test connectivity to the RADIUS server. Additionally, make sure your RADIUS server has UDP ports 1812 and 1813 (or 1645/1646 for older servers) open and is listening.
    *   **MikroTik Tool:** Use `/ping <RADIUS Server IP>` or `/tool traceroute <RADIUS Server IP>`.
*   **Incorrect Shared Secret:**
    *   **Problem:** The shared secret does not match between the router and the RADIUS server.
    *   **Solution:** Double-check and ensure that the shared secret is identical on both the RADIUS server and the MikroTik client configuration. It's case-sensitive.
*  **Incorrect RADIUS Server Configuration:**
    *   **Problem:** The RADIUS server is not configured to accept requests from this MikroTik client.
    *   **Solution:** Verify the NAS IP address is correctly configured on the RADIUS Server configuration, and that it allows for the configured "shared secret".
*   **RADIUS Authentication Failure:**
    *   **Problem:** The RADIUS server is not accepting or validating the client's credentials.
    *   **Solution:**  Review RADIUS server logs for authentication failures.  Confirm that the client's username and password are valid on the RADIUS server. Ensure that the RADIUS server is configured to handle requests from the MikroTik router with the specific MAC address of the client or the IP address assigned to it. Check your RADIUS configuration, and ensure that you have configured the router as a "NAS" or "RADIUS Client".
*   **DHCP Client Issues:**
    *   **Problem:** Clients are not receiving DHCP leases or are not being authenticated correctly.
    *   **Solution:**  Check MikroTik logs ( `/system logging print where topics~"radius|dhcp"`) for any errors related to RADIUS or DHCP. Ensure clients are using the correct credentials or MAC Address according to your RADIUS server rules. On the MikroTik, use the DHCP-Server logs for more in depth information.
*  **High CPU/Memory Usage:**
    *  **Problem:** A large number of simultaneous RADIUS authentication attempts or a very large DHCP scope and/or number of clients could potentially cause high CPU and/or memory usage, especially on lower end hardware.
    *  **Solution:** Monitor the Router's performance using `/system resource print`. If these usage numbers are high, consider implementing a more robust solution, or even a dedicated RADIUS server.

## Verification and Testing Steps:

1.  **Check RADIUS Status:**
    *   **Action:** Verify that the RADIUS configuration on the router is enabled and reachable.
    *   **CLI Command:** `/radius print`
    *   **Expected Output:** Verify that the `address`, `secret`, and `service` attributes are correct. Also ensure the `invalid` field is `no`.
2.  **Monitor RADIUS Logs:**
    *   **Action:** Watch the MikroTik's system logs for RADIUS-related messages.
    *   **CLI Command:** `/system logging print where topics~"radius"`
    *   **Expected Output:**  Look for messages related to authentication requests and their results (access-accept, access-reject). These messages show you if the router is even trying to communicate with the radius server.
3.  **DHCP Lease Acquisition:**
    *   **Action:** Connect a client to `ether-34` and attempt to get a DHCP lease.
    *   **Method:** A client can be a computer, a phone or a virtual machine.
    *   **Expected Effect:** The client should receive an IP address from the pool `21.144.11.0/24` **ONLY** if it was authenticated successfully.
4.  **Client Ping Test:**
    *   **Action:** Once a lease is acquired, verify that the client can reach the gateway and other networks using `ping`.
    *   **MikroTik Tool:** From the MikroTik, use `/ping <client_IP>`. From the client itself use the `ping` utility.
    *   **Expected Output:** If everything works as expected, the `ping` command should have a successful output, with little to no packet loss.
5.  **RADIUS Server Logs:**
    *   **Action:** Check the logs on the RADIUS server itself to confirm it received and processed the authentication requests.
    *   **Method:** Depends on the RADIUS server being used.
    *   **Expected Output:** Log messages indicating successful (or failed) authentication attempts from the MikroTik router.

## Related Features and Considerations:

*   **Hotspot:**  The RADIUS configuration here can be extended to support Hotspot functionality. When enabling Hotspot, the authentication process can redirect users to a login portal, where they must authenticate with a user and password, or use voucher based authentication, before being granted network access.
*   **Accounting:** RADIUS accounting can be enabled to keep track of user's sessions, usage, bandwidth, and more, and this is often used in conjunction with Hotspot functionality.
*   **User Manager:** MikroTik's User Manager can be used to provide a RADIUS server on the same device or a different one, it also offers a web interface for user management and accounting. This feature can greatly simplify deployments, while improving usability.
*   **VLANs:** RADIUS can be used in combination with VLANs (802.1Q) to provide VLAN assignment based on user credentials or other authentication details.
*   **Multiple RADIUS Servers:** Add multiple RADIUS servers for redundancy and high-availability.
*   **Dynamic DNS:** If the RADIUS server's IP address is not static, consider implementing dynamic DNS to keep the MikroTik informed.
*   **IP Binding:** Use IP Binding (DHCP static leases) to bind certain clients to specific IPs, this feature is compatible with RADIUS.

## MikroTik REST API Examples (if applicable):

While the core RADIUS functionality isn't directly exposed through dedicated REST API endpoints, we can interact with DHCP settings and indirectly influence RADIUS usage through those:

```
## Create/Modify DHCP Server:
   *Endpoint*: /ip/dhcp-server
   *Method*: POST/PUT
   *JSON Payload* (For adding or modifying the DHCP Server):
   ```json
   {
     ".id": "*0",
     "name":"dhcp1",
     "interface": "ether-34",
     "address-pool": "dhcp_pool1",
     "authoritative": true,
     "lease-time":"10m",
     "add-arp": true,
     "use-radius": true
   }
   ```
   *Response (Success - 200 OK)*:

   ```json
    {
     ".id": "*0",
     "name":"dhcp1",
     "interface": "ether-34",
     "address-pool": "dhcp_pool1",
     "authoritative": true,
     "lease-time":"10m",
     "add-arp": true,
     "use-radius": true
    }
   ```

   *Explanation of Parameters*:
      * `id` - The DHCP server ID to update (use * for creating).
      * `name` - The DHCP Server's name.
      * `interface` - The interface which the DHCP Server is tied to.
      * `address-pool` - The address pool being used by this DHCP Server.
      * `authoritative` - True if this is the authoritative DHCP Server for the subnet.
      * `lease-time` - The duration the DHCP leases are issued for.
      * `add-arp` - True to add dynamic ARP entries for DHCP leases.
      * `use-radius` - True to enable RADIUS authentication for the DHCP leases.
   *Error Handling*:
      * 400 Bad Request: If invalid values are provided for any parameters.
      * 500 Internal Server Error: If there are server-side issues processing the request.
      *   If there are any permission related issues, you'll receive a 403 response code.

```

```
## Create/Modify RADIUS Server:
   *Endpoint*: /radius
   *Method*: POST/PUT
   *JSON Payload* (For adding or modifying the RADIUS Server):
   ```json
   {
     ".id": "*0",
     "address": "192.168.88.100",
     "secret": "testing123",
     "service":"ppp,hotspot,dhcp",
     "timeout":3
   }
   ```
   *Response (Success - 200 OK)*:

   ```json
    {
     ".id": "*0",
     "address": "192.168.88.100",
     "secret": "testing123",
     "service":"ppp,hotspot,dhcp",
     "timeout":3
    }
   ```

   *Explanation of Parameters*:
      * `id` - The RADIUS server ID to update (use * for creating).
      * `address` - The RADIUS server IP.
      * `secret` - The RADIUS server shared secret.
      * `service` - The services that will use this RADIUS server.
      * `timeout` - The RADIUS server timeout in seconds.
   *Error Handling*:
      * 400 Bad Request: If invalid values are provided for any parameters.
      * 500 Internal Server Error: If there are server-side issues processing the request.
      *   If there are any permission related issues, you'll receive a 403 response code.

```

## Security Best Practices

*   **Strong RADIUS Secret:** Use a long, complex, and randomly generated shared secret for the RADIUS server and router configurations. Avoid using default or easy-to-guess secrets. Regularly change the shared secret.
*   **Firewall Rules:** Implement firewall rules on both the MikroTik router and RADIUS server to restrict access to RADIUS traffic to only necessary sources (e.g., the MikroTik's IP on port 1812/1813 to the RADIUS server, and only the RADIUS server's IP to the MikroTik).
*   **Secure RADIUS Server:** Keep the RADIUS server's operating system, software, and libraries up to date with the latest security patches.
*   **Use Secure Protocols:** When possible, use TLS or other secure methods for RADIUS communication (EAP). Also ensure that all communications between the RouterOS device and the RADIUS server are over a private, and secure channel.
*   **Monitor Logs:** Regularly review logs on both the MikroTik and the RADIUS server for suspicious activity, especially failed authentication attempts.
*   **Disable Unused Services:** If the MikroTik is not using all services (i.e. PPP or Hotspot) disable them in the RADIUS configuration. Only enable the services required for your network.

## Self Critique and Improvements

This configuration, while functional, is a basic implementation. Improvements could include:

*   **Advanced Authentication:** Implement more advanced authentication protocols like EAP (Extensible Authentication Protocol) for increased security.
*   **Accounting:** Add RADIUS accounting functionality for tracking user sessions and resource usage, and configure the RADIUS server to process these messages.
*   **Load Balancing/Redundancy:** Configure multiple RADIUS servers for fault tolerance and load balancing using a group/pool configuration.
*   **Advanced Policies:** Implement RADIUS attributes to specify user-specific policies, VLAN assignments, bandwidth limits, and QoS.
*   **Testing**: The documentation provides general verification steps. Adding more specific testing scenarios, such as verifying the client's authentication through a tool like `radtest` on the RADIUS server would make this section more complete.
*   **User Manager:** While User Manager was mentioned as a related feature, a small example could be added to exemplify how it can help with management.
*   **Automated Configuration:** Using scripting with a tool such as Ansible to implement this would drastically improve the speed of deployment, and further reduce human error.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**

RADIUS is a network protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users accessing a network. It operates on a client-server model. The RADIUS server maintains a database of valid users, their credentials, and their allowed network access policies. RADIUS works by having clients send authentication requests to the server. The server processes this request, based on a set of rules and configurations, and then responds with a permission grant or denial.

*   **Authentication:** Verifies user identity (typically username/password).
*   **Authorization:** Determines which network resources a user can access based on their authentication.
*   **Accounting:** Tracks user session information (start/stop times, data usage, etc.).

RADIUS uses UDP ports 1812 and 1813 for authentication/authorization and accounting respectively (older servers might use 1645 and 1646).

## Detailed Explanation of Trade-offs

*   **Local vs RADIUS Authentication:**
    *   **Local:**  Simpler for small networks, but difficult to manage for large user bases. User credentials and policies are stored directly on the MikroTik.
    *   **RADIUS:** Centralized management of user accounts and permissions, scalable, and allows for more complex policies. Requires an external RADIUS server.
*   **Plaintext vs EAP/TLS Authentication:**
    *   **Plaintext:** Simple to set up, but not secure (the shared secret and credentials might be exposed, if not in a secure channel).
    *   **EAP/TLS:** Significantly more secure, uses encryption for authentication, but is more complex to configure.
*   **DHCP RADIUS vs Hotspot RADIUS:**
    *   **DHCP RADIUS:** Authenticates users before granting IP leases, allowing control over network entry. It provides a simpler initial configuration process.
    *   **Hotspot RADIUS:** Provides a portal for authentication, allowing custom login pages and additional features (e.g., voucher systems). Requires more advanced setup.
*   **Multiple RADIUS servers:**
    *   **Single Server:** Easier to set up, but presents a single point of failure.
    *   **Multiple Servers:** More complex setup, but improves availability and resilience against server failures.
*  **Using RouterOS as a Radius Server:**
    *   **Using User-Manager:** Easier to set up, as all tools are on the router, but is not suitable for a high demand or highly available infrastructure.
    *   **Using a dedicated Radius Server:** Requires an external server, but presents improved reliability and scalability.

## Configuration for Specific RouterOS Versions:

This documentation targets RouterOS 7.12 (and is generally applicable to 6.48 and 7.x series). Some commands might have slightly different syntax or options on older versions.  If using older versions, you should refer to the respective version's documentation and adjust accordingly. The commands used here are compatible with RouterOS 6.48 and 7.x series. If using a version older than 6.48, you should review the documentation of your RouterOS version.

This complete guide provides detailed instructions, examples, and explanations for implementing RADIUS authentication with a MikroTik router in an ISP environment. Remember to adapt it to your specific needs and always prioritize security.
