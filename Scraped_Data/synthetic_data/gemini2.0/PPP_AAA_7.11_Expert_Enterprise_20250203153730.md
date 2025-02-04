Okay, let's dive into a detailed technical documentation for PPP AAA on a MikroTik router, specifically for the provided subnet and interface within an enterprise environment. We will use RouterOS 7.11 as the primary target, but note relevant differences for 6.48 and other 7.x versions where appropriate. We will configure a PPP server for authentication, authorization, and accounting (AAA).

## Scenario Description

We will configure a MikroTik router as a PPP server using RADIUS authentication, authorization, and accounting. Clients connecting to the `vlan-68` interface (on subnet 219.189.28.0/24) will establish a PPP connection and their authentication, authorization, and accounting will be handled by a RADIUS server. This setup is ideal for a controlled network access for employees or customers.

## Implementation Steps

Here’s a step-by-step guide, including CLI and Winbox instructions:

### Step 1:  Configure the VLAN interface

*   **Description**: Before setting up PPP, we must ensure the underlying VLAN interface exists and is configured properly.
*   **CLI Instructions**
   *   **Before:**  Assuming VLAN 68 is not yet configured:

        ```mikrotik
        /interface vlan print
        ```

   *   **During Configuration:** Create the vlan interface.  We will assume it will be based on a physical interface `ether1`.  Adapt this if your physical interface is different.

        ```mikrotik
        /interface vlan
        add interface=ether1 name=vlan-68 vlan-id=68
        ```
   *   **After:** Check the interface:

        ```mikrotik
        /interface vlan print
        ```

        Output should show vlan-68 enabled and pointing to `ether1`.
* **Winbox Instructions:**
    *   Navigate to **Interfaces**
    *   Click on the **"+"** button to add a new interface.
    *   Select **VLAN**.
    *   Under the **General** tab, set:
        *   Name: `vlan-68`
        *   VLAN ID: 68
        *   Interface: `ether1` (or your desired physical interface)
    *   Click **Apply** and then **OK**.

### Step 2: Configure IP Address for the VLAN interface

*   **Description**: Assign an IP address to the VLAN interface within the subnet.
*  **CLI Instructions**
   *   **Before:** Ensure that there is not a conflicting address already setup for the subnet.

       ```mikrotik
        /ip address print
        ```
    *   **During Configuration:** We will assign IP address `219.189.28.1/24` to `vlan-68`

        ```mikrotik
        /ip address
        add address=219.189.28.1/24 interface=vlan-68 network=219.189.28.0
        ```

    *   **After:** Check IP address.

        ```mikrotik
        /ip address print
        ```
         Output should show `219.189.28.1/24` on `vlan-68`.
*   **Winbox Instructions:**
    *   Navigate to **IP** -> **Addresses**.
    *   Click on the **"+"** button to add a new IP address.
    *   Set:
        *   Address: `219.189.28.1/24`
        *   Interface: `vlan-68`
    *   Click **Apply** and then **OK**.

### Step 3: Configure RADIUS Server

*   **Description:** Define the RADIUS server that will handle AAA.
*   **CLI Instructions:**
    * **Before:** Ensure that there are no conflicting radius entries.

      ```mikrotik
      /radius print
      ```
    *   **During Configuration:** Assuming our RADIUS server is on IP `192.168.88.100` with a secret of `secret123`

        ```mikrotik
        /radius
        add address=192.168.88.100 secret=secret123 service=ppp timeout=3
        ```
         *  `address` : IP Address of the radius server.
         *  `secret` : Shared secret for communication with the radius server.
         * `service` : Service type for Radius - `ppp`, `hotspot`, `dhcp`, `wireless` etc.
         *  `timeout` : Time to wait for a response from the radius server.
    *  **After:** Confirm the radius server entry

      ```mikrotik
      /radius print
      ```
        The new entry should be listed with the set parameters.
*   **Winbox Instructions:**
    *   Navigate to **RADIUS**.
    *   Click on the **"+"** button to add a new RADIUS server.
    *   Set:
        *   Address: `192.168.88.100`
        *   Secret: `secret123`
        *   Service: `ppp`
    * Click **Apply** and then **OK**.

### Step 4:  Configure PPP Secret for fallback

*   **Description:**  Configure a fallback user for authentication in case the RADIUS server is unavailable. It is good practice to setup at least one user locally on the device.
*   **CLI Instructions**
     *  **Before:** Ensure there are no conflicting users.
      ```mikrotik
       /ppp secret print
       ```
    *   **During Configuration:** Add a local secret for testing (optional but highly recommended). This user will have a default profile.
        ```mikrotik
        /ppp secret
        add name=testuser password=testpass service=ppp
        ```
         *  `name` : The username.
         *  `password` : User Password.
         *  `service` : Services that can use this user - `ppp`, `pptp`, `l2tp`, etc.
    *   **After:** check created user.
        ```mikrotik
        /ppp secret print
        ```
        The `testuser` user should be in the list.
*   **Winbox Instructions:**
    *   Navigate to **PPP** -> **Secrets**.
    *   Click on the **"+"** button to add a new secret.
    *   Set:
        *   Name: `testuser`
        *   Password: `testpass`
        *   Service: `ppp`
        *  Profile: `default`
    *   Click **Apply** and then **OK**.

### Step 5: Create a PPP Profile (Optional, but Highly Recommended)

*   **Description:** PPP profiles are used to specify various settings for PPP connections, such as MTU, DNS, and IP addresses. By setting a profile we can avoid setting these settings for every user individually.
*   **CLI Instructions**
     *   **Before:** View existing profiles
      ```mikrotik
      /ppp profile print
      ```
    *   **During Configuration:** Create a new PPP profile named `ppp-profile-radius`. Set the local address to be `219.189.28.254`, assign a DNS and set the MTU/MRU.  Optionally we set up a pool of IP addresses.
        ```mikrotik
        /ppp profile
        add change-tcp-mss=yes dns-server=1.1.1.1 local-address=219.189.28.254 name=ppp-profile-radius remote-address=ppp-pool use-encryption=yes use-mpls=yes
        /ip pool
        add name=ppp-pool ranges=219.189.28.100-219.189.28.200
        ```
      *  `change-tcp-mss`: Whether to change TCP MSS to fit in the MTU or not.
      *  `dns-server`: DNS server address provided to the connecting client.
      *  `local-address`: IP address to be assigned to the PPP server side interface.
      *  `name`: The profile name.
      * `remote-address`: IP address or pool to be assigned to the connecting client.
       * `use-encryption`: Allow encryption.
       * `use-mpls` Use MPLS.
    *   **After:** View profiles to ensure that the new profile exists.
        ```mikrotik
         /ppp profile print
        ```
        The output will display all existing profiles.
*   **Winbox Instructions:**
    *   Navigate to **PPP** -> **Profiles**.
    *   Click on the **"+"** button to add a new profile.
    *   Set:
        *   Name: `ppp-profile-radius`
        * Under **General** Tab set:
           *   Local Address: `219.189.28.254`
           *   Remote Address: `ppp-pool`
        * Under **Protocol** Tab set:
           *  Use Encryption: `yes`
           *  Use MPLS: `yes`
        * Under **DNS** Tab set:
           * DNS Servers: `1.1.1.1`
        * Under **Limits** Tab set:
          *  Change TCP MSS: `yes`
    *   Click **Apply** and then **OK**.
    *   Navigate to **IP** -> **Pools**
    *   Click on the **"+"** button to add a new Pool.
     * Set:
       * Name: `ppp-pool`
       * Ranges: `219.189.28.100-219.189.28.200`
   * Click **Apply** and then **OK**.

### Step 6: Configure PPP Server

*  **Description**: Enable the PPP server and assign it to the VLAN Interface and use the PPP Profile we have just configured.
*   **CLI Instructions**
   *  **Before:** Check for any existing ppp server interface.
      ```mikrotik
       /interface ppp-server print
       ```
    * **During Configuration:** Configure the ppp server settings.
        ```mikrotik
        /interface ppp-server server
        set authentication=pap,mschap2,chap enabled=yes interface=vlan-68 max-mru=1492 max-mtu=1492 default-profile=ppp-profile-radius
        ```
      *  `authentication` : Allowable authentication methods.
       *  `enabled`: Whether to enable the ppp server.
      *  `interface`: The interface to start the PPP service.
      *  `max-mru`: Maximum Receive Unit.
       * `max-mtu`: Maximum Transmission Unit.
      *  `default-profile`:  The default PPP profile to use for connections.
    *   **After:** check the server configuration.
        ```mikrotik
        /interface ppp-server server print
        ```
        The new entry should be listed with the set parameters.

*  **Winbox Instructions:**
    *  Navigate to **Interface** -> **PPP Servers**
    * Ensure that the **Enabled** button at the top is checked
    * Set
       * Authentication: `pap, mschap2, chap`
       * Interface: `vlan-68`
       * Maximum MRU: `1492`
       * Maximum MTU: `1492`
       * Default Profile: `ppp-profile-radius`
     * Click **Apply** and then **OK**.

### Step 7: Enable RADIUS on the PPP Server

*   **Description:** Activate the use of RADIUS for the PPP server
*   **CLI Instructions:**
    *  **Before:** Check server configuration.
         ```mikrotik
         /interface ppp-server server print
         ```
    *   **During Configuration:** enable the `use-radius` parameter
        ```mikrotik
        /interface ppp-server server
        set use-radius=yes
        ```
       * `use-radius`: Whether to use radius for authentication, accounting and authorization.
    *   **After:** Check if radius is enabled.
        ```mikrotik
        /interface ppp-server server print
        ```
       The output should show that radius is enabled.

*   **Winbox Instructions:**
     *   Navigate to **Interface** -> **PPP Servers**
    * Ensure that the **Use Radius** button is checked
     *  Click **Apply** and then **OK**.

## Complete Configuration Commands

Here's the complete set of commands:

```mikrotik
/interface vlan
add interface=ether1 name=vlan-68 vlan-id=68

/ip address
add address=219.189.28.1/24 interface=vlan-68 network=219.189.28.0

/radius
add address=192.168.88.100 secret=secret123 service=ppp timeout=3

/ppp secret
add name=testuser password=testpass service=ppp

/ip pool
add name=ppp-pool ranges=219.189.28.100-219.189.28.200

/ppp profile
add change-tcp-mss=yes dns-server=1.1.1.1 local-address=219.189.28.254 name=ppp-profile-radius remote-address=ppp-pool use-encryption=yes use-mpls=yes

/interface ppp-server server
set authentication=pap,mschap2,chap enabled=yes interface=vlan-68 max-mru=1492 max-mtu=1492 default-profile=ppp-profile-radius use-radius=yes

```

## Common Pitfalls and Solutions

*   **RADIUS Server Unreachable:**
    *   **Problem:**  The router cannot communicate with the RADIUS server.
    *   **Solution:** Verify network connectivity (ping), the server IP address, the shared secret, firewall rules (on the router and the RADIUS server), and make sure the service is enabled.
    *   **MikroTik Commands:** `ping 192.168.88.100`, `/tool/torch interface=ether1`
*   **Incorrect Shared Secret:**
    *   **Problem:** If the shared secret on the MikroTik and the RADIUS server do not match, the clients will not authenticate.
    *   **Solution:** Verify the secrets on both the MikroTik and the RADIUS server.
    *   **MikroTik Commands:** `/radius print`
*  **Incorrect User Permissions:**
    *   **Problem:** User may be properly authenticating but not be receiving the correct permissions on the radius.
    *   **Solution:** Check the radius logs and verify that the correct profile and permissions are being sent by the server.
*  **Incorrect IP Addresses:**
    *  **Problem:** Errors can arise if the IP Addresses on the device are incorrectly configured, or there is a conflict between address pools.
    *  **Solution:** Verify the IP address configuration and pools. Make sure that no overlapping ranges are in use.
*  **PPP Profile Errors**
    *   **Problem:** Errors can arise if settings such as MTU/MRU and encryption are not properly configured.
    *   **Solution:** Make sure that the MTU and MRU settings are less than or equal to the interface MTU. Verify any encryption settings.
*  **Authentication Method Issues**
    *  **Problem:** Client fails to authenticate as the authentication method being used is not compatible with the device.
    *  **Solution:** Ensure that the authentication methods on both the client and server match.  It is generally better to choose a more modern authentication method such as MSCHAP2.  The PAP authentication protocol passes the password in plain text, and should only be used if no other authentication method is supported.
*   **High CPU Usage:**
    *   **Problem:** Numerous concurrent PPP connections could lead to high CPU on the router.
    *   **Solution:** Monitor CPU usage `/system resource monitor`. Optimize router resources, consider a higher-powered device.
*  **Router Resource Issues**
    *  **Problem:** Limited memory or storage on the router can affect the performance and reliability.
    *  **Solution:** Check memory and storage usage `/system resource print`. If the device is resource-constrained, consider using a more robust device.

## Verification and Testing Steps

*   **Ping RADIUS Server:** `ping 192.168.88.100` (verify connectivity)
*   **Verify RADIUS Settings:** `/radius print` (check configuration)
*   **PPP Client Connection:** Connect a client using PPP (e.g., Windows built-in VPN client, MikroTik client) with a user that exists on the radius server.
*   **PPP Active Connections:** `/interface ppp active print` (monitor active PPP sessions)
*   **Torch:** `/tool torch interface=vlan-68` (capture and analyze network traffic)
*  **Check logs:** `/log print` or using winbox, review system logs for errors.  RADIUS errors will generally be shown in the log.
*   **PPP Interface Status:** `/interface ppp print` (verify assigned IP and statistics)
*   **RADIUS Server Logs:** Check the RADIUS server logs for successful and failed authentication attempts.

## Related Features and Considerations

*   **Accounting:**  RADIUS accounting allows the monitoring of session usage and statistics, such as how long each user has connected and how much data they have transmitted.
*   **Hotspot:** Combine with Hotspot for captive portal functionality for guest networks.
*   **IPSec/L2TP:**  Use L2TP over IPSec for added security when connecting over the Internet, for example for remote workers.
*   **Multiple RADIUS Servers:** Use multiple RADIUS servers for redundancy and load-balancing in case one fails.
*  **VRF** : Using VRF allows one to isolate different logical networks on the same hardware. This can be useful in larger enterprises where segregation is required.
*  **Firewall:** Ensure the firewall allows only necessary traffic, blocking unsolicited or malicious packets.

## MikroTik REST API Examples

Here are some examples using MikroTik's REST API (assuming you have the API enabled and access):

**1. Create a RADIUS Server:**

*   **Endpoint:** `/radius`
*   **Method:** POST
*   **JSON Payload:**

```json
{
    "address": "192.168.88.100",
    "secret": "secret123",
    "service": "ppp",
    "timeout": 3
}
```

*   **Expected Response (201 Created):** The newly created radius configuration.

**2. Get RADIUS Servers:**

*   **Endpoint:** `/radius`
*   **Method:** GET
*   **JSON Response Example:**

```json
[
  {
    ".id": "*1",
    "address": "192.168.88.100",
    "secret": "secret123",
    "service": "ppp",
    "timeout": "3",
    "disabled": "false"
  }
]
```
**3. Enable PPP Radius Use:**

* **Endpoint:** `/interface/ppp-server/server/0` (Assuming this is the first ppp-server)
* **Method:** PUT
* **JSON Payload:**
```json
{
    "use-radius": true
}
```
*   **Expected Response (200 OK):** The modified interface configuration.

**Error Handling:**

*   **400 Bad Request:**  Invalid JSON, missing parameters, type mismatches.
*   **401 Unauthorized:**  Invalid API credentials.
*   **500 Internal Server Error:**  An error on the MikroTik router itself. Check the logs on the router.

## Security Best Practices

*   **Strong RADIUS Secret:** Use long, complex, and hard-to-guess secrets.
*   **Secure RADIUS Server:** Ensure the RADIUS server is protected by firewalls and access controls.
*   **Regular Password Changes:** Enforce regular password updates for PPP accounts.
*   **Limit Access:** Restrict access to the router's configuration interfaces.
*   **Disable Unnecessary Services:** Turn off unused services on the MikroTik router.
*   **Use Encryption:** Always use encryption protocols (e.g., MSCHAP2) if supported.  PAP authentication passes credentials in plain text.
*  **Firewall:** Configure the MikroTik firewall to restrict access to the PPP server.
*  **Rate Limiting:** Use MikroTik's rate limiting options to limit the amount of bandwidth available to each user or user group. This can protect against denial of service attacks and provide fair usage.
* **Regular Audits:** Regularly audit the router settings to identify and fix any configuration weaknesses.

## Self Critique and Improvements

This configuration covers the basics of PPP AAA. However, improvements could be:

*   **Dynamic Rate Limiting:** Implement dynamic rate limiting using RADIUS attributes.
*   **Advanced Firewall Rules:** Create more sophisticated firewall rules based on dynamic address lists from RADIUS accounting.
*   **Centralized Logging:** Configure centralized logging using syslog to capture all relevant system events.
*   **More Complex Profiles:**  Set more sophisticated profiles including specific routing, vlan assignments.
*  **Failover:** Configure for additional radius servers to ensure that authentication is always available.

## Detailed Explanations of Topic

**PPP AAA:**

*   **Authentication:** Verifies the identity of the user. Common authentication methods are PAP, CHAP, and MSCHAP2.
*   **Authorization:** Grants specific privileges and permissions to the user after authentication. Radius will provide the settings and permissions for a user including which profiles to use.
*   **Accounting:** Tracks user session details like connection time, data usage, and other statistics.

**RADIUS (Remote Authentication Dial-In User Service):** A protocol for providing centralized Authentication, Authorization, and Accounting management for users connecting to a network. It is often used by ISPs and large enterprises.

## Detailed Explanation of Trade-offs

*   **PAP vs. MSCHAP2:**
    *   **PAP** is simple but transmits passwords in plaintext, making it very insecure.
    *   **MSCHAP2** is more secure by encrypting the password during the authentication process.  MSCHAP2 is preferred.
*   **Local Secrets vs. RADIUS:**
    *   **Local Secrets** are easy to manage but are not scalable.  They are excellent for testing, or as a backup.
    *  **RADIUS** provides a centralized authentication service and better management and scalability. Radius is preferred for any production network.
*   **Default Profile vs. per-User Profiles:**
    *  **Default profiles** are good for smaller networks where all users will have similar permissions.
    *   **per-User Profiles**  provide more granular control but add complexity.  Radius provides an excellent way to provide profile information.
*   **MTU/MRU Settings:**
    *   Setting MTU/MRU too high can lead to packet fragmentation, lowering performance.
    *  Setting MTU/MRU too low can lead to poor efficiency.
    *  It is important to tune the MTU/MRU to the specific network requirements. 1492 is often a good starting point.

## Configuration for Specific RouterOS Versions

This documentation primarily targets RouterOS 7.11. Most of these commands are similar across 7.x versions. For 6.48 and earlier, some command syntax might be different, especially with the PPP configuration.  It is suggested that you consult the documentation for your specific version.

*   **RouterOS 6.48 and earlier:** Older versions of RouterOS may require more explicit settings in the profile to allocate IP addresses. The PPP servers may also have slightly different parameters.
*   **RouterOS 7.x:** This configuration will work with most 7.x version, but verify commands, especially if using older or newer versions.

Let me know if you have any other requirements or need more detail in any of these sections!
