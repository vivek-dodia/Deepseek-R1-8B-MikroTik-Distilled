Okay, let's dive into a comprehensive RADIUS configuration for a MikroTik router, targeting RouterOS v6.48 and the specified parameters.

## Scenario Description:

We are configuring a MikroTik router to authenticate wireless clients connecting to the `wlan-69` interface using a RADIUS server. This setup is common in small to medium-sized businesses (SMBs) or enterprise networks where centralized authentication and authorization are required for security and user management. The `wlan-69` interface will provide Wi-Fi access to users, and their login credentials will be verified against the RADIUS server.  The subnet `197.74.134.0/24` is not directly relevant in the RADIUS setup, but we assume it will be used in our local network for our internal machines, in a typical router setup.

## Implementation Steps:

Here’s a step-by-step guide to configure RADIUS authentication for the `wlan-69` interface on a MikroTik router.

**1. Step 1: Configure the RADIUS Server Definition**

*   **Goal:** Define the RADIUS server details on the MikroTik router so it can communicate and authenticate users.
*   **Why:**  The MikroTik needs the IP address, secret, and other crucial parameters to contact the RADIUS server.
*   **Before:**
    *   No RADIUS server configured on the router.
*   **CLI Command Example:**
    ```mikrotik
    /radius add address=192.168.88.100 secret=sharedsecret service=wireless timeout=3
    ```
*   **Winbox GUI:**
    *   Go to `RADIUS` under `PPP`.
    *   Click the `+` button to add a new server.
    *   Enter the `Address`, `Secret`, and select `wireless` for `Service`. Adjust `Timeout`.
*   **After:** A new RADIUS server entry is added to the router.
*   **Effect:** The router is now aware of a specific RADIUS server and how to connect to it.

**2. Step 2: Configure Wireless Interface for RADIUS Authentication**

*   **Goal:** Modify the wireless interface to use RADIUS authentication for connecting clients.
*   **Why:** We need to tell the `wlan-69` interface to send authentication requests to the defined RADIUS server.
*   **Before:**
    *   The `wlan-69` interface is likely configured with another method of authentication, like a simple password or no authentication.
*   **CLI Command Example:**
    ```mikrotik
    /interface wireless security-profiles set [find name=default] authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys radius-mac-accounting=yes radius-eap-accounting=yes eap-methods=peap
    /interface wireless set wlan-69 security-profile=default
    /interface wireless set wlan-69 disabled=no
    ```
*  **Winbox GUI:**
   * Go to `Wireless` under `Interface`.
   * Double click on `wlan-69` interface.
   * Select the `Security Profile` tab.
   * Open `default` security profile.
   * Set `Authentication Types` to include `wpa-psk` and `wpa2-psk` at minimum.
   * Set `Mode` to `dynamic-keys`.
   * Check the `Radius MAC Accounting` and `Radius EAP Accounting` checkboxes.
   * Add `peap` to `EAP Methods`.
   * Back on the main `Wireless Interface` tab, set the correct profile from the `Security Profile` dropdown box.
*   **After:**  The `wlan-69` interface now uses the configured RADIUS server.
*   **Effect:**  Clients connecting to this interface will be authenticated via the configured RADIUS server.

**3. Step 3: (Optional) Configure RADIUS Accounting**

*   **Goal:**  Enable RADIUS accounting to track user sessions and resource usage.
*   **Why:**  Allows logging of connection times, bandwidth consumption, and other user-specific data.
*   **Before:**
    *   Accounting might not be configured.
*   **CLI Command Example:**
    ```mikrotik
    /radius set [find service=wireless] accounting=yes interim-update=5m
    ```
*   **Winbox GUI:**
    *   Go to `RADIUS` under `PPP`.
    *   Double-click the previously added RADIUS server.
    *   Check the `Accounting` checkbox.
    *   Adjust the `Interim Update` interval, if needed.
*   **After:**  RADIUS accounting is enabled for the wireless service.
*   **Effect:** The RADIUS server will receive accounting packets with user data.

## Complete Configuration Commands:

```mikrotik
# Step 1: Define RADIUS Server
/radius add address=192.168.88.100 secret=sharedsecret service=wireless timeout=3

# Step 2: Configure Wireless Interface for RADIUS
/interface wireless security-profiles set [find name=default] authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys radius-mac-accounting=yes radius-eap-accounting=yes eap-methods=peap
/interface wireless set wlan-69 security-profile=default
/interface wireless set wlan-69 disabled=no

# Step 3 (Optional): Enable RADIUS Accounting
/radius set [find service=wireless] accounting=yes interim-update=5m

# Explanation of Parameters
# /radius add
#   address:      IP address of the RADIUS server
#   secret:       Shared secret used to authenticate communication between the router and the RADIUS server
#   service:     Indicates the service for which the RADIUS server is used. In this case, 'wireless'. Other options are 'ppp', 'hotspot', 'dhcp'.
#   timeout:      Timeout for the connection attempt to the RADIUS server (in seconds)
# /interface wireless security-profiles set
#   name:          Name of the security profile
#   authentication-types:  Which types of authentication will be allowed on this interface, comma separated.
#   mode:          Mode of the security profile, in this case `dynamic-keys` to work with radius authentication.
#   radius-mac-accounting: Enables RADIUS MAC address-based accounting.
#   radius-eap-accounting: Enables RADIUS EAP accounting.
#   eap-methods:    Which eap methods to use
# /interface wireless set
#   name:          Name of the wireless interface to modify
#   security-profile:  Assign the configured security profile to the wireless interface
#   disabled:      Disable or enable the given interface.
# /radius set
#   accounting:  Enable RADIUS accounting
#   interim-update: Interval for interim accounting updates (e.g., every 5 minutes).
```

## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Secret:** If the secret on the router does not match the secret on the RADIUS server, authentication will fail.
    *   **Solution:** Double-check the secret on both the router and the RADIUS server, making sure there are no leading or trailing spaces.

*   **RADIUS Server Unreachable:**  The router might be unable to communicate with the RADIUS server due to network issues or firewall rules.
    *   **Solution:** Verify network connectivity using `ping <RADIUS server IP>` from the router's terminal. Check firewall rules on the MikroTik and any intermediary devices.

*   **Misconfigured Authentication Types:** If the authentication methods don't match between the router and the wireless clients, connections will fail.
    *   **Solution:** Make sure the `authentication-types` and the methods configured in security profile are compatible with client devices.

*   **RADIUS Timeout:** The timeout might be too short if the RADIUS server is taking longer to respond.
    *   **Solution:** Increase the `timeout` value in the `/radius` configuration.

*   **Incorrect Service Type:**  If the `service` is not specified correctly in the `/radius` configuration, connections might fail.
    *   **Solution:**  Make sure the `service` is `wireless` in this case.

*   **Missing EAP method:** Ensure that the EAP method configured on the wireless interface matches the one configured on the RADIUS server.
     *  **Solution:** Make sure that the `eap-methods` is correctly configured on both the server and on the router.

*   **Resource Issues:** If the MikroTik router is heavily loaded, RADIUS authentication may become slow or unreliable.
    *   **Solution:** Monitor CPU and memory usage using `/system resource print` or from Winbox GUI. If resources are exhausted, consider upgrading the router or optimizing its configuration.

*   **Security Issues:** Using weak shared secrets or unencrypted communication with RADIUS could be exploited.
    *   **Solution:** Use strong, unique shared secrets, and consider enabling RADIUS over TLS (RadSec) for enhanced security.

## Verification and Testing Steps:

1.  **Wireless Client Connection:** Attempt to connect a wireless client device to the `wlan-69` network.
2.  **MikroTik Logs:** Check the MikroTik logs (`/log print`) for any RADIUS-related errors or authentication messages.
3.  **RADIUS Server Logs:** Check the RADIUS server logs for authentication attempts and any errors.
4.  **Ping Test:** If the client authenticates successfully, attempt to ping a device on the network to verify connectivity.
5.  **Torch:** Use MikroTik's torch tool (`/tool torch interface=wlan-69`) to monitor network traffic and ensure RADIUS packets are being transmitted and received.

## Related Features and Considerations:

*   **Hotspot:** Consider using the MikroTik hotspot functionality for more advanced user management, session control, and walled garden capabilities.  Hotspot can use the same RADIUS setup.
*   **User Manager:** The MikroTik User Manager package can act as a RADIUS server.  This is useful for small deployments.
*   **VRF (Virtual Routing and Forwarding):** If complex network segmentation is needed, VRF could be used with RADIUS for user-specific routing and access controls.
*   **RadSec:** As mentioned before, for high security situations, enable RadSec for encrypted communication with the RADIUS server, as shared secrets are exposed on clear text otherwise.

## MikroTik REST API Examples (if applicable):

Since RADIUS configuration is often done through CLI or Winbox, here are some REST API examples (assuming you have the API package installed and enabled):

**Example 1: Adding a RADIUS Server (POST)**

*   **Endpoint:** `/ppp/radius`
*   **Method:** POST
*   **JSON Payload:**
    ```json
    {
        "address": "192.168.88.100",
        "secret": "sharedsecret",
        "service": "wireless",
        "timeout": "3"
    }
    ```
*   **Expected Response (201 Created):**
    ```json
    {
      "id": "*0",
      "address": "192.168.88.100",
      "secret": "sharedsecret",
      "service": "wireless",
      "timeout": 3,
      "accounting": false
    }
    ```
*   **Error Handling:**
    *   If `address` or `secret` are missing, the API will return error code `400 Bad Request`.
    *   If the user does not have write access to the path, the API will return `401 Unauthorized`

**Example 2: Getting a List of RADIUS Servers (GET)**

*   **Endpoint:** `/ppp/radius`
*   **Method:** GET
*   **No Payload**
*   **Expected Response (200 OK):**
    ```json
    [
        {
          "id": "*0",
          "address": "192.168.88.100",
          "secret": "sharedsecret",
          "service": "wireless",
          "timeout": 3,
          "accounting": false
        }
    ]
    ```
*   **Error Handling:**
    *   If the user does not have read access to the path, the API will return `401 Unauthorized`

**Example 3: Setting RADIUS Accounting (PUT):**

*   **Endpoint:** `/ppp/radius/*0` (replace `*0` with the actual ID)
*   **Method:** PUT
*   **JSON Payload:**
    ```json
     {
      "accounting": true,
       "interim-update": "5m"
    }
    ```
*   **Expected Response (200 OK):**
    ```json
    {
      "id": "*0",
      "address": "192.168.88.100",
      "secret": "sharedsecret",
      "service": "wireless",
      "timeout": 3,
      "accounting": true,
      "interim-update": "5m"
    }
    ```
*   **Error Handling:**
    *   If the id is invalid, it will return error code `404 Not Found`.
    *   If the user does not have write access to the path, the API will return `401 Unauthorized`

## Security Best Practices

*   **Strong Shared Secret:**  Use a strong, unique shared secret for RADIUS communication and avoid default or easily guessed passwords. Change the shared secret regularly.
*   **RadSec:** Use RadSec (RADIUS over TLS) whenever possible to encrypt all communication between the router and the RADIUS server. This will protect the shared secret and authentication credentials.
*   **Regular Security Audits:** Perform regular security audits of your MikroTik router configuration, including the RADIUS setup, to identify and address any potential vulnerabilities.
*   **Access Control:** Limit access to the MikroTik router's configuration via firewall rules and management interfaces, to avoid a possible man-in-the-middle attack.
*   **Keep RouterOS Updated:** Always keep RouterOS updated to the latest stable version to patch any security vulnerabilities.

## Self Critique and Improvements

*   **Error Reporting:**  The current configuration does not include a detailed error handling strategy for the RADIUS server. This could be improved by monitoring logs and setting up notifications for authentication errors.
*   **Dynamic VLAN Assignment:**  The configuration could be expanded to dynamically assign VLANs to wireless clients based on their RADIUS authentication.
*  **Specific User Groups:** The current security profile is assigned to all users. Different user groups can be separated using separate security profiles, each one assigned to a specific group of users.
*   **Monitoring and Alerting:** Implement a robust monitoring and alerting system to detect problems with RADIUS connectivity or authentication failures, allowing for proactive troubleshooting.
*   **Redundancy:** This setup uses only one RADIUS server, which could be a single point of failure. A secondary RADIUS server should be considered.
*   **Specific EAP Methods:** Instead of just including `peap` other EAP methods could be used, depending on the RADIUS server available and the best method to use.
*   **AAA (Authentication, Authorization, and Accounting):** This configuration focuses mostly on authentication, but accounting and authorization, should also be thoroughly implemented.

## Detailed Explanations of Topic

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) for users connecting to a network. Here’s a breakdown:

*   **Authentication:** Verifies the user’s identity by checking their credentials against a central database. This avoids managing user accounts on multiple devices.
*   **Authorization:** Determines what resources a user is allowed to access. After successful authentication, RADIUS can inform the network device about the access rights granted to the user.
*   **Accounting:** Tracks resource usage, such as connection time, bandwidth consumed, and other user session details. This data is useful for reporting, usage analysis, and billing purposes.

RADIUS operates using a client-server model:

*   **RADIUS Client:** A network access device, like a MikroTik router, that sends authentication requests to the RADIUS server.
*   **RADIUS Server:** A server that contains the user database and policies. It authenticates users and responds to access requests.

The RADIUS protocol uses UDP and is often implemented with EAP (Extensible Authentication Protocol) for stronger authentication methods.  EAP is a framework that provides various ways of secure authentication using different methods, like PEAP (Protected Extensible Authentication Protocol), TLS (Transport Layer Security), and others.

## Detailed Explanation of Trade-offs

* **Plain Password vs. EAP Methods:**
    *   Plain password authentication (WPA-PSK/WPA2-PSK) is easier to set up but is less secure. If compromised, the entire network key is exposed.
    *   EAP methods (like PEAP, TLS) provide stronger authentication, as they use an external authentication server and can use certificates or encrypted keys. However, they require more complex configuration on both the client and server.
* **RADIUS MAC Accounting vs. RADIUS EAP Accounting:**
    * RADIUS MAC Accounting keeps track of connections based on the MAC address of the client. This is useful for managing devices rather than users.
    * RADIUS EAP Accounting provides more detailed information about the authenticated user, like username, session time, etc. Use EAP accounting where possible.
* **Single vs. Multiple RADIUS Servers:**
    *   Using a single RADIUS server is easier but creates a single point of failure. If the server is down, no new users can authenticate.
    *   Multiple RADIUS servers configured for redundancy will ensure that authentication can continue if one server fails. The MikroTik will failover to the second RADIUS server.
* **Accounting Updates:**
    *  Frequent interim accounting updates provide more granular data but increase network traffic and processing load on the RADIUS server.
    *  Infrequent updates reduce traffic but provide less real-time data.
* **Timeout Values:**
    * Shorter timeouts can cause authentication failures if the RADIUS server takes longer to respond.
    *  Longer timeouts increase latency for user authentication, and might leave users waiting too long to connect to the network.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS 6.48 and RouterOS 7.x.  The core concepts and commands remain largely the same between these versions.

**Important Note:** Some minor differences can exist in the Winbox GUI menus and presentation details, but the general configuration steps are consistent. However, certain advanced EAP methods, or configuration commands and capabilities may not be available, especially in older versions of RouterOS. Consult the official RouterOS documentation for specifics to each version.

This thorough guide should help you implement and understand RADIUS authentication on your MikroTik router. Let me know if you have any further questions!
