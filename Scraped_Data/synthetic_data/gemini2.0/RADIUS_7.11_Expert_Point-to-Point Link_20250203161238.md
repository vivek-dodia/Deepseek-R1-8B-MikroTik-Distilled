Okay, let's dive into a detailed RADIUS implementation on MikroTik RouterOS v7.11, focusing on a point-to-point link scenario.

## Scenario Description:

This document outlines how to configure a MikroTik router acting as a RADIUS client, authenticating users connecting to a wireless interface named `wlan-75` within the 129.75.37.0/24 subnet. The router will forward authentication requests to a central RADIUS server. This setup is common in small to medium-sized businesses or ISP environments to manage user access to the network.

## Implementation Steps:

**Prerequisites:**
* You have a MikroTik router running RouterOS v7.11 or later.
* You have a functional RADIUS server (e.g., FreeRADIUS, Microsoft NPS) with a static IP address.
* The `wlan-75` interface is correctly configured and operational.
* Basic networking knowledge.

1.  **Step 1: Define the RADIUS Server:**

    *   **Goal:**  To configure the MikroTik router to know the IP address, port and secret key of the RADIUS server.

    *   **Before:** No RADIUS server configured.
        ```
        /radius print
        Flags: X - disabled
        ```

    *   **CLI Command:**
        ```
        /radius add address=192.168.1.100 secret="your_radius_secret" service=ppp,login,hotspot,wireless timeout=30
        ```
        *   `address`: The IP address of your RADIUS server (change to match).
        *   `secret`: The shared secret used for communication between the router and the RADIUS server (change to match). **Important: Use a strong, complex secret.**
        *   `service`: The service types this RADIUS server will authenticate (we're including wireless, among others).
        *   `timeout`: The maximum time the router will wait for a response from the RADIUS server (in seconds).

    *   **Winbox GUI:** Go to "RADIUS" menu, click on the "+" button to add a new RADIUS server entry and fill out fields in the GUI: Address, Secret, and Services.

    *   **After:** The MikroTik should have a new RADIUS server defined.
        ```
        /radius print
        Flags: X - disabled
          0 address=192.168.1.100 secret="your_radius_secret" timeout=30 service=ppp,login,hotspot,wireless
        ```
        *   **Effect:** The router can now communicate with the specified RADIUS server, if the server is reachable.
2.  **Step 2: Configure Wireless Authentication:**

    *   **Goal:**  To enable RADIUS authentication on the `wlan-75` wireless interface.

    *   **Before:** Default wireless authentication method (probably WPA2-PSK).
        ```
        /interface wireless print
        Flags: X - disabled, R - running
        0   name="wlan-75" mtu=1500 mac-address=XX:XX:XX:XX:XX:XX arp=enabled interface-type=A  mode=ap-bridge ssid="MySSID" frequency=2437 band=2ghz-b/g/n channel-width=20mhz wps-mode=disabled security-profile="default" ...
        ```

    *   **CLI Commands:**
        ```
        /interface wireless security-profiles add name="radius-profile" authentication-types=wpa2-eap
        /interface wireless set wlan-75 security-profile=radius-profile
        ```
        *   `security-profiles add name="radius-profile" authentication-types=wpa2-eap`: Creates a new security profile with WPA2-EAP (which uses RADIUS).
        *   `interface wireless set wlan-75 security-profile=radius-profile`: Applies the new security profile to the `wlan-75` interface.
    *   **Winbox GUI:** Go to "Wireless" and open properties of `wlan-75`, set "Security Profile" to `radius-profile`. Go to "Security Profiles", and click the "+" button to add a new profile called `radius-profile`. Under `Authentication Types` select `wpa2-eap`.

    *   **After:** `wlan-75` is using WPA2-EAP for authentication.
        ```
        /interface wireless print
        Flags: X - disabled, R - running
        0   name="wlan-75" mtu=1500 mac-address=XX:XX:XX:XX:XX:XX arp=enabled interface-type=A  mode=ap-bridge ssid="MySSID" frequency=2437 band=2ghz-b/g/n channel-width=20mhz wps-mode=disabled security-profile="radius-profile" ...
        ```

        ```
        /interface wireless security-profiles print
        Flags: X - disabled, D - dynamic
        0   name="default" mode=dynamic-keys authentication-types=wpa2-psk group-encryption=aes-ccm unicast-encryption=aes-ccm group-key-update=5m
        1   name="radius-profile" authentication-types=wpa2-eap
        ```
     *   **Effect:** Devices connecting to `wlan-75` will now use RADIUS-based authentication.
3. **Step 3: Create a User Profile**:
    *   **Goal:** To ensure that the user has a user profile to be assigned when connected. Note that we can use RADIUS attributes to further configure this
    *   **Before:** No user profile created.
       ```
       /ppp profile print
        Flags: * - default
        #   NAME                 LOCAL-ADDRESS  REMOTE-ADDRESS  ADDRESS-LIST  CHANGE-TCP-MSS   ONLY-ONE     USE-ENCRYPTION
        0 * default            10.0.0.1        10.0.0.2        default                     no             yes
       ```
    *   **CLI Command:**
        ```
        /ppp profile add name="radius-user-profile" local-address=129.75.37.1 remote-address=129.75.37.0/24
        ```
    *   **Winbox GUI:** Go to "PPP", click "Profiles" and add a new profile and fill out `Name`, `Local Address` and `Remote Address`.
    *   **After:** A new user profile is created
        ```
        /ppp profile print
         Flags: * - default
         #   NAME                 LOCAL-ADDRESS  REMOTE-ADDRESS  ADDRESS-LIST  CHANGE-TCP-MSS   ONLY-ONE     USE-ENCRYPTION
         0 * default            10.0.0.1        10.0.0.2        default                     no             yes
         1  radius-user-profile  129.75.37.1     129.75.37.0/24  default                     no             yes
        ```
     *   **Effect:** A user profile to be assigned when the user logs in.

## Complete Configuration Commands:

```
# Configure RADIUS Server
/radius add address=192.168.1.100 secret="your_radius_secret" service=ppp,login,hotspot,wireless timeout=30

# Create Wireless Security Profile for RADIUS
/interface wireless security-profiles add name="radius-profile" authentication-types=wpa2-eap

# Assign the RADIUS security profile to the wlan-75 interface
/interface wireless set wlan-75 security-profile=radius-profile

# Create a User Profile
/ppp profile add name="radius-user-profile" local-address=129.75.37.1 remote-address=129.75.37.0/24
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router cannot communicate with the RADIUS server, authentication fails.
    *   **Solution:** Check network connectivity (ping, traceroute). Ensure the RADIUS server is running and listening on the correct IP and port. Verify firewall rules aren't blocking traffic on either side.
    *  **MikroTik Commands:**  `ping 192.168.1.100`, `/tool traceroute 192.168.1.100`. Check firewall using `/ip firewall filter print`
*   **Incorrect Shared Secret:**
    *   **Problem:** RADIUS authentication fails due to a mismatch in the shared secret between the MikroTik router and the RADIUS server.
    *   **Solution:** Double-check and verify that the `secret` parameter on the MikroTik configuration *exactly* matches the secret configured on the RADIUS server.
*   **Incorrect Authentication Types:**
    *   **Problem:** The client is unable to connect when not using `wpa2-eap`.
    *   **Solution:** Select the correct authentication type. This implementation is using wpa2-eap.
*   **RADIUS Attributes Issues:**
    *   **Problem:** Incorrect RADIUS attributes may prevent the user from receiving the right user profile.
    *   **Solution:** Use the MikroTik command `/radius print detail` and the radius server logs to ensure the correct attributes are received.
*   **MikroTik Logs:** Check the logs for errors: `/system logging print`  (pay attention to topics related to "radius" and "wireless").

## Verification and Testing Steps:

1.  **Connect a client device** to the `wlan-75` wireless network.
2.  **Observe the authentication process** on the client device; you should be prompted for your RADIUS credentials (username and password).
3.  **Check MikroTik logs:**
    ```
    /system logging print where topics~"radius"
    ```
    Look for successful authentication messages from the RADIUS server: `"radius-server: accounting-response: success"` . Check for any failed access requests.
4. **Check for active wireless connections.**
   ```
    /interface wireless registration-table print
    ```
    This will show you all connected stations.
5. **Check `ppp active` for active users.**
  ```
  /ppp active print
  ```
  This will show you all users authenticated by PPP (including wireless clients using RADIUS).
6. **Check logs on your RADIUS server** for successful or failed authentication attempts.

## Related Features and Considerations:

*   **RADIUS Accounting:**  Implement RADIUS accounting for tracking user session usage.  Add accounting to the `service` parameter of the RADIUS configuration on the MikroTik. Example: `service=ppp,login,hotspot,wireless,accounting`
*   **VLAN Tagging:** If required, add VLAN tagging on the wireless interface and the PPP interface created for each RADIUS connection.
*   **Dynamic VLAN Assignment:**  RADIUS can dynamically assign users to VLANs based on user attributes.
*   **Rate Limiting (Traffic Shaping):** RADIUS attributes can be used to dynamically apply rate limits on a per-user basis, using MikroTik queue trees. Example: Use the mikrotik-rate-limit attribute.
*   **Multiple RADIUS Servers (Failover):** Configure multiple RADIUS servers for redundancy using the  `add` command multiple times, or editing the `servers` parameter (comma-separated)

## MikroTik REST API Examples:

**Note:** MikroTik's REST API support for RADIUS is more limited. Direct API control over RADIUS server settings is best done via CLI and can be then read via the API.

**Example 1: Retrieve RADIUS Server Configuration**

*   **Endpoint:** `/radius`
*   **Method:** GET
*   **Response (JSON Example):**
    ```json
    [
        {
            "id": "*0",
            "address": "192.168.1.100",
            "secret": "your_radius_secret",
            "timeout": "30",
            "service": "ppp,login,hotspot,wireless",
            "domain": "",
            "accounting": "no"
        }
    ]
    ```
    *   `id`:  RouterOS unique ID of the radius server instance.
    *   `address`: IP address of the radius server.
    *   `secret`: Shared secret
    *   `timeout`: Timeout in seconds.
    *   `service`: List of services to be authenticated using this radius server.
    *    `domain`: the domain that will be sent to radius server for authentication.
    *    `accounting`: whether this radius server will do accounting.

    **Error Handling:** Standard HTTP errors apply. If an error occurs, the API will return an error code, along with an error message. Check for HTTP 404 (not found), 403 (forbidden).

**Example 2: Retrieve Wireless interface Configuration**

*   **Endpoint:** `/interface/wireless`
*   **Method:** GET
*  **Response (JSON Example):**
    ```json
    [
        {
           "name": "wlan-75",
           "mac-address": "XX:XX:XX:XX:XX:XX",
           "mtu": "1500",
           "arp": "enabled",
           "mode": "ap-bridge",
           "ssid": "MySSID",
           "frequency": "2437",
           "band": "2ghz-b/g/n",
           "channel-width": "20mhz",
           "wps-mode": "disabled",
            "security-profile": "radius-profile"
        }
    ]
    ```
    *   `name`: name of interface.
    *   `mac-address`: MAC address of interface.
    *   `mtu`: interface MTU.
    *   `arp`: whether ARP is enabled.
    *   `mode`: wireless interface mode.
    *   `ssid`: Wireless network SSID.
    *   `frequency`: selected frequency.
    *   `band`: selected band
    *    `channel-width`: selected channel width
    *    `wps-mode`: wps mode
    *    `security-profile`: selected security profile

**Error Handling:** Standard HTTP errors apply. If an error occurs, the API will return an error code, along with an error message. Check for HTTP 404 (not found), 403 (forbidden).

**Example 3: Retrieve PPP profile Configuration**

*   **Endpoint:** `/ppp/profile`
*   **Method:** GET
*  **Response (JSON Example):**
    ```json
        [
        {
            "name": "default",
            "local-address": "10.0.0.1",
            "remote-address": "10.0.0.2",
             "address-list": "default",
             "change-tcp-mss": "no",
             "only-one": "no",
             "use-encryption": "yes"
        },
          {
            "name": "radius-user-profile",
            "local-address": "129.75.37.1",
            "remote-address": "129.75.37.0/24",
             "address-list": "default",
             "change-tcp-mss": "no",
             "only-one": "no",
             "use-encryption": "yes"
        }
      ]
    ```
    *   `name`: the profile name.
    *   `local-address`: the local address assigned to users.
    *   `remote-address`: the network assigned to the users.
    *    `address-list`: the address-list to assign the users.
    *    `change-tcp-mss`: Whether to change MSS.
    *    `only-one`: whether to allow only one connection.
    *    `use-encryption`: whether to use encryption.

**Error Handling:** Standard HTTP errors apply. If an error occurs, the API will return an error code, along with an error message. Check for HTTP 404 (not found), 403 (forbidden).

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a strong, complex, randomly generated secret for the shared secret. Avoid easily guessed passwords.
*   **RADIUS Server Security:** Secure your RADIUS server using firewalls and restricting access to only authorized devices.
*   **Wireless Security:** Ensure WPA2-EAP is configured correctly and avoid using legacy authentication methods.
*   **Access Control:** Implement access control rules and policies to ensure only authorized users can connect to the network. Use role based control through RADIUS attributes.
*   **Regular Audits:** Regularly review and audit your RADIUS server and MikroTik configurations for vulnerabilities.
*   **Use secure connections:** ensure that all communication channels are secure, using TLS or similar.
*   **Monitoring and alerts:** Use logging and monitoring to alert when errors and threats are detected.

## Self Critique and Improvements:

*   **Improvement:** Currently, all user profiles are assigned the same local and remote address. A more secure implementation would be to dynamically assign them to their own network and or use VLANs based on the users.
*   **Improvement:** Implement traffic shaping using RADIUS attributes to allow for greater control and improve QoS.
*   **Improvement:** The router is acting as a simple authenticator, a more powerful implementation would also include Accounting, to monitor user sessions, bandwidth used, and other useful attributes.
*   **Security:** Using shared key, the router is vulnerable to security breaches, ideally, a certificate should be used instead of a shared key.
* **Complexity:** The configuration can become quite complicated when it includes VLANs, and multiple subnets, the implementation can be improved by planning accordingly beforehand, and create proper documentation.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) management for users who connect to a network. It operates on a client-server model, where the network access server (NAS) (in this case, the MikroTik router) acts as a client sending access requests to the RADIUS server. The RADIUS server verifies user credentials against an authentication database, returns authorization policies, and tracks user sessions through accounting.

## Detailed Explanation of Trade-offs:

*   **WPA2-PSK vs WPA2-EAP:**
    *   **WPA2-PSK:** Simpler to set up but uses a shared passphrase, which is less secure for larger networks because users sharing the same passphrase.
    *   **WPA2-EAP:** More secure, uses RADIUS, and allows for individual user authentication with user names and passwords. This allows greater control, like rate limiting, VLAN assignments, or session time.  It is more complex to set up but provides better security and scalability.
*   **Local Authentication vs RADIUS:**
    *   **Local Authentication:** User accounts are managed directly on the router, suitable for small networks with a few users. Easier to set up but doesn't scale well for many users or complex authorization needs.
    *   **RADIUS:** Uses a centralized authentication server, providing scalability and management. Ideal for large networks where centralized user management and accounting is important. Adds complexity but also enhances security.
*   **Centralized RADIUS vs Local User profiles:**
    * **Centralized Radius:** A centralized management and authentication system, ideal for large networks.
    * **Local User profiles:** It's simpler to setup but does not scale well.
*   **Shared secret vs Certificates:**
    * **Shared Secret:** Easy to setup, but vulnerable for eavesdropping and can be hard to manage.
    * **Certificates:** More complex, harder to setup, but way more secure.

## Configuration for Specific RouterOS Versions:

This configuration is specifically for RouterOS v7.11. While most commands will be compatible with RouterOS 6.48 and other 7.x versions, always consult the official MikroTik documentation for any specific differences. Always double-check the parameters and options in the documentation. Be aware that not all features might be available in older versions.
  *  **Pre RouterOS v7** Some settings might use a different path or a different command. Check the RouterOS documentation.

This detailed documentation covers the implementation, configuration, and best practices for RADIUS on MikroTik RouterOS. Remember to adjust parameters like IP addresses, secrets, and interface names to match your specific network setup.
