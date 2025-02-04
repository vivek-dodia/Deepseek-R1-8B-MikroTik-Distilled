Okay, let's dive into a comprehensive guide on configuring RADIUS for a MikroTik hotspot network using RouterOS 7.11, focusing on an expert level of configuration and practical application.

## Scenario Description:

We are configuring a MikroTik router, specifically interface `ether46`, to act as a network access server (NAS) for a hotspot network.  All user authentication and authorization requests will be forwarded to a RADIUS server. This allows us to centrally manage user accounts and access permissions. The subnet `194.166.222.0/24` is the network behind `ether46` that is used in the hotspot.

## Implementation Steps:

### 1. **Initial Router Configuration:**
   * **Goal:** Ensure the `ether46` interface is enabled and properly configured.
   * **Before:** Assume `ether46` is up and running.
   * **Action:** Verify interface settings using the CLI and/or Winbox.

   **CLI:**
   ```mikrotik
   /interface ethernet print where name="ether46"
   ```

   **Winbox:** Navigate to `Interface` -> `ether46`, verify it's enabled and no other critical configurations are missing.

   **Effect:** This step provides a baseline and verifies basic connectivity.
   * **Note:**  If the interface is not enabled, use the CLI command `/interface ethernet enable ether46`.

### 2. **Setting up the RADIUS Client:**
    * **Goal:** Add the RADIUS server's information to the MikroTik router.
    * **Before:**  The RADIUS server needs to be set up beforehand with a shared secret that is known to the router. Let's assume:
        * RADIUS Server IP: `192.168.88.100`
        * Shared Secret: `mysecretkey`
        * RADIUS port (authentication): `1812`
        * RADIUS port (accounting): `1813`
    * **Action:** Use the CLI to add the RADIUS server configuration.

    **CLI:**
    ```mikrotik
    /radius add address=192.168.88.100 secret=mysecretkey service=hotspot timeout=3s accounting-port=1813 port=1812
    ```
    **Winbox:** Navigate to `RADIUS` -> click the "+" button. Fill out the details described above.
    * **Effect:** The MikroTik now has a RADIUS server defined for use with its services.
    * **Note:** The `timeout` parameter specifies how long the MikroTik will wait for a response from the RADIUS server before considering the request as failed.
    * **Note:** It is important to ensure that communication between the MikroTik and RADIUS is allowed with a firewall rule, and reachable via IP.

   **After:**
   ```mikrotik
   /radius print
    #   ADDRESS         SECRET      SERVICE   TIMEOUT ACCOUNTING-PORT PORT
    0   192.168.88.100  mysecretkey hotspot    3s       1813          1812
   ```
   **Winbox:** `RADIUS` window should show your new entry.

### 3. **Configuring Hotspot Server:**
   * **Goal:** Enable the Hotspot server on `ether46` and configure it to use RADIUS.
   * **Before:** Hotspot is not configured yet.
   * **Action:** Create a hotspot server profile and bind it to `ether46`, enable RADIUS authentication.

   **CLI:**
   ```mikrotik
   /ip hotspot profile add name=hotspot-profile use-radius=yes
   /ip hotspot add name=hotspot-server interface=ether46 profile=hotspot-profile address-pool=hotspot-pool disabled=no
   /ip pool add name=hotspot-pool ranges=194.166.222.10-194.166.222.254
   /ip dhcp-server add name=hotspot-dhcp interface=ether46 address-pool=hotspot-pool
   ```

   **Winbox:**
     *  Go to `IP` -> `Hotspot` -> `Profiles`. Click the "+" to create a new profile called `hotspot-profile`, check `Use RADIUS`.
     * Go to `IP` -> `Hotspot` -> `Hotspots` tab. Click the "+". Name it `hotspot-server`, choose `ether46` in the `Interface`, use the profile `hotspot-profile`, and the `address-pool` called `hotspot-pool`.
     * Go to `IP` -> `Pool`, create the `hotspot-pool` with the ranges as specified above.
     * Go to `IP` -> `DHCP Server`, create a new server with the `hotspot-dhcp` name, using the `hotspot-pool` address pool, and the `ether46` interface.

   **Effect:** The MikroTik is now a Hotspot server listening on `ether46`, using RADIUS for authentication.  Users connecting to the hotspot will be redirected to the Hotspot login page and then authenticated via RADIUS.

    * **Note:** If you omit the `/ip dhcp-server add ...` step, devices connecting will not get an IP.
    * **Note:** It is important to set up DNS for the hotspot, if not, devices connecting may have issues. This could be done by `/ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes`.
    * **Note:** The `address-pool` defines the subnet where the hotspot users will be assigned an IP.

### 4. **Configuring RADIUS for Accounting (Optional):**
    * **Goal:** Enable accounting information to be sent to the RADIUS server.
    * **Before:** RADIUS authentication is set up, but not accounting.
    * **Action:** Enable accounting in the hotspot profile.
    * **CLI:**
       ```mikrotik
       /ip hotspot profile set hotspot-profile accounting=yes
       ```
    * **Winbox:**
       * Go to `IP` -> `Hotspot` -> `Profiles`, edit `hotspot-profile` and check `Accounting`.
    * **Effect:** The MikroTik will now send accounting data (start, stop, interim) to the RADIUS server.
    * **Note:** Accounting is essential for tracking bandwidth usage and billing in many hotspot deployments. The RADIUS server needs to be configured to receive accounting packets.
    * **Note:** There are multiple accounting methods that can be configured.

### 5. **Configure Hotspot walled-garden**
    * **Goal**: Ensure a user can reach the RADIUS server without being authenticated.
    * **Before**: The hotspot is fully functional.
    * **Action**: Add the IP to the walled-garden.
    * **CLI:**
        ```mikrotik
        /ip hotspot walled-garden add dst-host=192.168.88.100
        ```
    * **Winbox**:
      * Go to `IP` -> `Hotspot` -> `Walled Garden` and add the IP to the dst-host.
    * **Effect**: The MikroTik hotspot will now allow access to the RADIUS server without authentication.
    * **Note**: There may be other services required to be added to the walled-garden, such as DNS servers.
### 6. **Verifying Configuration:**
  * **Goal:** Verify RADIUS connectivity and authentication.
  * **Before:** Configured hotspot with RADIUS.
  * **Action:** Connect a client to the hotspot, observe authentication attempts on both the MikroTik and the RADIUS server.

## Complete Configuration Commands:

```mikrotik
/interface ethernet print where name="ether46"
/radius add address=192.168.88.100 secret=mysecretkey service=hotspot timeout=3s accounting-port=1813 port=1812
/ip hotspot profile add name=hotspot-profile use-radius=yes
/ip hotspot add name=hotspot-server interface=ether46 profile=hotspot-profile address-pool=hotspot-pool disabled=no
/ip pool add name=hotspot-pool ranges=194.166.222.10-194.166.222.254
/ip dhcp-server add name=hotspot-dhcp interface=ether46 address-pool=hotspot-pool
/ip hotspot profile set hotspot-profile accounting=yes
/ip hotspot walled-garden add dst-host=192.168.88.100
```

## Common Pitfalls and Solutions:

*   **Problem:** RADIUS server not reachable.
    *   **Solution:**
        *   Verify IP address and port configuration on both devices.
        *   Ensure firewall rules on the MikroTik and any intervening firewalls do not block RADIUS traffic (UDP ports 1812, 1813).  Use `/tool torch interface=ether46 protocol=udp port=1812` to see if traffic is arriving and going out correctly on the device.
        *   Check connectivity with `ping 192.168.88.100`.
*   **Problem:** Incorrect Shared Secret.
    *   **Solution:** Double-check the shared secret on both the MikroTik and RADIUS server.
*   **Problem:** Hotspot users not redirecting to login page.
    *   **Solution:** Ensure that the Hotspot is enabled on the correct interface, and the address pool has been configured properly.
    * **Solution:** Ensure the device is getting an IP address.
    * **Solution:**  Check that DNS is working.
*   **Problem:** Authentication failures.
    *   **Solution:** Examine RADIUS server logs for specific errors and check that the server is configured for the MikroTik as the NAS.
*   **Problem:** RADIUS server timeout.
    *   **Solution:** Increase the `timeout` parameter in the `/radius add` command.
*   **Problem:** Accounting not working.
    *   **Solution:** Ensure the RADIUS server is configured to accept accounting messages.
    *   **Solution:** Ensure that accounting is enabled in the hotspot profile.

## Verification and Testing Steps:

1.  Connect a client device to the hotspot (e.g., via Wi-Fi connected to the same subnet as the `ether46` interface.
2.  Open a web browser. You should be redirected to the Hotspot login page.
3.  Attempt to log in with a valid RADIUS username and password (as set up on your RADIUS server).
4.  On successful authentication, you should have internet access (if no other policies are preventing it).
5.  Check the RADIUS server's logs for successful authentication records.
6.  Use `/log print follow-topic=radius` on the MikroTik to observe RADIUS exchanges.
7.  If accounting is configured, verify accounting packets are received at the RADIUS server.
8.  Use `torch` on MikroTik on interface `ether46` with `udp port 1812` or `1813` to verify that traffic is being received.

## Related Features and Considerations:

*   **Hotspot User Profiles:** Use MikroTik's Hotspot user profiles to limit bandwidth and assign specific permissions to different users and groups, including quotas.
*   **RADIUS Attributes:** Utilize RADIUS vendor-specific attributes (VSAs) to implement advanced features such as VLAN tagging, QoS, and dynamic access lists.
*   **Proxy RADIUS:** For very large networks, consider proxying RADIUS requests to scale the architecture.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy using the `priority` parameter in the `/radius add` command.
*   **SSL/TLS for RADIUS:** In production, strongly consider enabling RADIUS over TLS (radsec) for secure communication.  This needs to be enabled on the RADIUS server, and will require an additional shared secret. This can be configured in the `/radius` commands by specifying the `security=tls-only` or `security=start-tls` and selecting the certificate to use.
*   **Dynamic Hotspot Login Page:** Customize the hotspot login page for a more branded experience. This can be configured in the `/ip hotspot` resources.
*   **Traffic Shaping:** Limit users by traffic using queues. This can be done with MikroTik's queue system.

## MikroTik REST API Examples (if applicable):

While the MikroTik API is very powerful, it's primarily designed around general system configuration, and the implementation of many RADIUS and hotspot features are done through CLI or Winbox.

However, let's consider an example of adding a RADIUS server using the API.

**API Endpoint:** `/radius`

**Request Method:** `POST`

**Example JSON Payload:**

```json
{
  "address": "192.168.88.100",
  "secret": "mysecretkey",
  "service": "hotspot",
  "timeout": "3s",
  "accounting-port": 1813,
  "port": 1812
}
```
* `address`: IP Address of RADIUS server
* `secret`: The RADIUS secret
* `service`: Service this is used for
* `timeout`: How long to wait for a response
* `accounting-port`: RADIUS accounting port.
* `port`: RADIUS authentication port.

**Expected Response (200 OK):**

```json
{
  ".id": "*1",
  "address": "192.168.88.100",
  "secret": "mysecretkey",
  "service": "hotspot",
  "timeout": "3s",
  "accounting-port": 1813,
  "port": 1812
}
```
* `.id` - Is the identifier for the newly created radius configuration.

**Error Handling:**

If the API returns an error, you would get a different error response. For example, if you try to add a RADIUS server with an existing IP address you will get:
```json
{
 "message": "already have such radius server",
  "error": "already have such radius server"
}
```

## Security Best Practices:

*   **Strong Shared Secrets:** Use complex and unique shared secrets for RADIUS communication.
*   **Secure RADIUS Communications:** Implement RADIUS over TLS (radsec) in production networks.
*   **Firewall Rules:** Strictly limit access to the RADIUS server ports to only the necessary devices (MikroTik routers).
*   **Monitor Logs:** Regularly monitor MikroTik and RADIUS server logs for anomalies and security breaches.
*   **User Management:** Ensure that a robust user management process is in place on your RADIUS server.
*   **Access Control:** Consider having different access controls for staff to the RADIUS server, or other components of the network.
* **Update Regularly**: Keep the device and software up to date to reduce any security concerns that may be found.

## Self Critique and Improvements:

*   **Improvement:** This configuration is functional, but should include RADIUS over TLS (radsec) for production environments for enhanced security, and may require a certificate for the server.
*   **Improvement:** Implement more sophisticated error handling in the API.
*  **Improvement:** Add multiple RADIUS servers for redundancy, using the priority option.
* **Improvement:** This can be made more secure by adding an access list and removing the wildcard entries from the walled-garden.
* **Improvement:** Add a certificate for the walled-garden, in order to prevent man-in-the-middle attacks.
*   **Improvement:** Add examples for other components, such as user profiles, queues, and VLANs.

## Detailed Explanations of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) for users connecting to a network. In our case, the MikroTik acts as a NAS that relays user login requests to the RADIUS server. The RADIUS server validates credentials against a user database.  It then either authorizes access or rejects the connection. RADIUS also handles accounting, which provides information about network usage and can be used for billing purposes.

## Detailed Explanation of Trade-offs:

*   **Using local users vs RADIUS:** Using local users in a hotspot is easy for small networks. Using RADIUS allows for more complex user management in large networks with multiple access points.
*   **Hotspot authentication modes:** There are many different authentication modes in a hotspot. RADIUS is very powerful when you need a third-party authentication server. The benefit is that it allows you to have central user management. The trade-off is that it requires additional infrastructure in the form of a RADIUS server and more complex configuration.
*   **Accounting:** It uses extra resources on the router. If you don't need accounting it should be disabled, but there is not much impact on the router. If you need billing or reporting for accounting, enabling it is a necessity.
*   **Radius Timeout:** A low timeout value improves responsiveness if there is an error. A high timeout value increases the chance that a connection will succeed on a busy network, but can cause a delayed user experience. It is a fine balancing act between availability and responsiveness.
*   **Walled-garden:** A larger walled-garden allows for more flexibility, but decreases security. A smaller, more strictly controlled, walled-garden increases security, but may cause connection issues if something is missed.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 7.11 (and will also work on 6.48 and other 7.x). It utilizes features available in these versions, such as standard RADIUS settings and basic hotspot configurations.  All commands used should be backwards compatible with previous RouterOS versions.

This should be a very useful reference for you. Let me know if you have any other questions.
