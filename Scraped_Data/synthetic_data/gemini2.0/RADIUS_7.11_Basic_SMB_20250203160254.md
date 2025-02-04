Okay, let's craft a comprehensive documentation for configuring RADIUS authentication on a MikroTik router, targeting RouterOS 7.11 within an SMB network context.

## Scenario Description

This scenario outlines the configuration of a MikroTik router to use a RADIUS server for authentication of wireless clients connecting to the network on VLAN 60. This would be a common use case in a small business where you want more control over user authentication and access than simply using a pre-shared key.

## Implementation Steps

Here’s a detailed, step-by-step guide to configure RADIUS on the designated interface:

**Prerequisites:**
*   You have a working RADIUS server setup, and know its IP address, shared secret, and the port used for authentication.
*   You have basic network connectivity from the MikroTik router to the RADIUS server.
*   Your router has a configured VLAN interface, named `vlan-60`, on which you will have wireless clients connecting.

**1. Step 1:  Add a RADIUS Server Configuration**

*   **Explanation:**  This step configures the MikroTik router to communicate with the specific RADIUS server. We define its address, secret, and authentication port.
*   **Before:** You have no RADIUS settings defined in the router.
*   **CLI Command:**
    ```mikrotik
    /radius add address=192.168.10.10 secret="your_radius_secret" service=wireless,ppp,login,hotspot,dhcp authentication-port=1812 timeout=3
    ```
    *   `/radius add`: Creates a new RADIUS server configuration.
    *   `address=192.168.10.10`: The IP address of your RADIUS server. Replace with your actual IP.
    *   `secret="your_radius_secret"`: The shared secret used to authenticate communication between the MikroTik and the RADIUS server.  **Important:** Replace `"your_radius_secret"` with your actual secret.
    *   `service=wireless,ppp,login,hotspot,dhcp`: Specifies what services should use this RADIUS configuration. This allows multiple use cases on the same server. Here, we're enabling it for `wireless`. Additional options are: `ppp` (for PPP connections), `login` (for router login), `hotspot` (for hotspot), `dhcp` (for dhcp-related auth).
    *   `authentication-port=1812`: The authentication port on the RADIUS server (default 1812).
    *   `timeout=3`:  Sets the timeout for RADIUS communication (in seconds).

*   **After:** The router has the RADIUS server details configured.
*   **Winbox GUI:**
    1.  Navigate to *Radius* in the left-hand menu.
    2.  Click the plus (+) button to add a new RADIUS server.
    3.  Fill in the fields:
        *   *Address*: 192.168.10.10
        *   *Secret*: your\_radius\_secret
        *   *Service*: Check the `wireless` checkbox.
        *   *Authentication Port*: 1812
        *   *Timeout*: 3
    4.  Click *Apply* and then *OK*.

**2. Step 2: Configure Wireless Interface (on the VLAN)**

*   **Explanation:** This step will modify the wireless interface attached to `vlan-60` to use the newly created RADIUS server.
*   **Before:** Wireless interface is using WPA2-PSK authentication.
*   **CLI Command:**
    ```mikrotik
    /interface wireless security-profiles
    add name=radius-auth mode=dynamic-keys authentication-types=wpa2-psk,wpa2-eap eap-methods=eap-peap,eap-tls \
    radius-accounting=no radius-mac-format=XX:XX:XX:XX:XX:XX,upper-case
    /interface wireless set vlan-60 security-profile=radius-auth mode=ap
    ```
   * `/interface wireless security-profiles add name=radius-auth`:  Creates a new security profile called 'radius-auth'
   * `mode=dynamic-keys`: Use dynamic keys to encrypt wireless traffic.
   * `authentication-types=wpa2-psk,wpa2-eap`: Allows users to connect with wpa2-psk fallback or via WPA2-Enterprise.
   * `eap-methods=eap-peap,eap-tls`:  Specifies that we'll be using EAP-PEAP or EAP-TLS authentication (based on the config on your radius server)
   * `radius-accounting=no`:  Disables accounting (can be `yes` if you require accounting on the radius server).
   * `radius-mac-format=XX:XX:XX:XX:XX:XX,upper-case`: Sets format of MAC address for RADIUS server
   * `/interface wireless set vlan-60 security-profile=radius-auth mode=ap` Sets the interface and mode to AP mode, and attaches the previously created security profile to the `vlan-60` interface.

*   **After:** The `vlan-60` wireless interface will use RADIUS authentication when a client connects.
*   **Winbox GUI:**
    1. Navigate to *Wireless*
    2. On the *Security Profiles* tab, click on the `+` button, add a profile and name it `radius-auth`.
    3.  Set the *Mode* to `dynamic keys`.
    4. Check the `WPA2 PSK` and `WPA2 EAP` boxes, and check `EAP-PEAP` and `EAP-TLS` in the *EAP Methods* box.
    5.  Disable accounting for this example.
    6.  Set *Radius Mac Format* to `XX:XX:XX:XX:XX:XX,upper-case`.
    7.  Click *Apply* and then *OK*.
    8. Go back to *Interfaces*, click on the `wireless-vlan-60` Interface and select the new security profile, `radius-auth`, in the `security profile` dropdown.
    9. Set the *Mode* to `ap`.
    10. Click *Apply* and then *OK*.

**3. Step 3 (Optional):  Test with a Client Device**

*   **Explanation:** This step involves connecting a client device (like a laptop or phone) to the configured wireless network.
*   **Before:** You have only done config work.
*  **Action:**
    1. On your client, attempt to connect to the wireless network associated with the `vlan-60` interface.
    2.  If prompted, provide the username and password configured on your RADIUS server for your user.

*   **After:**  The client either connects successfully and gets an IP address, or fails and there are errors to troubleshoot.

## Complete Configuration Commands

Here are the complete MikroTik CLI commands to implement the entire setup:

```mikrotik
/radius
add address=192.168.10.10 secret="your_radius_secret" service=wireless,ppp,login,hotspot,dhcp authentication-port=1812 timeout=3
/interface wireless security-profiles
add name=radius-auth mode=dynamic-keys authentication-types=wpa2-psk,wpa2-eap eap-methods=eap-peap,eap-tls \
radius-accounting=no radius-mac-format=XX:XX:XX:XX:XX:XX,upper-case
/interface wireless set vlan-60 security-profile=radius-auth mode=ap
```

**Detailed Parameter Explanation:**

| Command               | Parameter             | Description                                                                                                  | Example                       |
|-----------------------|-----------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------|
| `/radius add`         | `address`             | IP address of the RADIUS server.                                                                            | `192.168.10.10`               |
|                       | `secret`              | Shared secret used for communication with the RADIUS server.                                             | `"your_radius_secret"`        |
|                       | `service`             | Services that use this RADIUS configuration.                                                                | `wireless,ppp,login,hotspot,dhcp`|
|                       | `authentication-port`| UDP port for authentication requests on the RADIUS server.                                                  | `1812`                         |
|                       | `timeout`             | Timeout (in seconds) for RADIUS communication.                                                              | `3`                           |
| `/interface wireless security-profiles add` | `name` | The security profile name for easy reference                               | `radius-auth`             |
|                       | `mode`                | Wireless security mode, selects dynamic encryption key settings.             | `dynamic-keys`             |
|                       | `authentication-types`| Enabled authentication types, PSK fallback or EAP for authentication via RADIUS server      | `wpa2-psk,wpa2-eap`             |
|                       | `eap-methods`            | Enabled EAP methods, to connect using the configured RADIUS server method             | `eap-peap,eap-tls`             |
|                       | `radius-accounting`   | Enable or Disable RADIUS accounting.                                                                        | `no`                            |
|                       | `radius-mac-format`   | Specifies how mac addresses will be formatted during RADIUS communication                                       | `XX:XX:XX:XX:XX:XX,upper-case`       |
| `/interface wireless set`   | `vlan-60`              | The interface to configure                                                                 | `vlan-60`    |
|                       | `security-profile`    | Security profile to use.       |  `radius-auth`                          |
|                       | `mode`       | The mode this wireless interface will operate as | `ap`      |

## Common Pitfalls and Solutions

*   **Incorrect Shared Secret:** If the secret on the MikroTik doesn't match the RADIUS server, authentication will fail.
    *   **Solution:** Double-check the secret in both the MikroTik configuration and on the RADIUS server.
*   **Incorrect RADIUS Server IP or Port:** If the IP address or port is wrong, the MikroTik will not communicate with the RADIUS server.
    *   **Solution:** Verify the IP and port using `ping 192.168.10.10` (replace with your RADIUS IP). Also check firewall settings on the router and server to make sure that traffic is not blocked.
*   **EAP Configuration Mismatch:** If the MikroTik is configured for `eap-peap` and the server is using `eap-tls`, it won't work.
    *   **Solution:** Ensure the `eap-methods` on the Mikrotik match the method configured on your RADIUS server.
*   **Firewall Issues:** A firewall on the MikroTik or the RADIUS server can block the authentication traffic.
    *   **Solution:** Create firewall rules to allow communication between the MikroTik and the RADIUS server on UDP port 1812 (and 1813 for accounting, if enabled).
*   **RADIUS Server Not Responding:** The RADIUS server might be down or overloaded.
    *   **Solution:** Check the RADIUS server logs for errors, check the service is running, and the system resources aren't overloaded.
*   **Incorrect MAC Address format:** If a wrong mac-address format is provided, the server will not understand the request.
    *   **Solution:** Ensure that the correct MAC address format is provided and is consistent between the router and the server.

## Verification and Testing Steps

1.  **Ping the RADIUS Server:**
    ```mikrotik
    /ping 192.168.10.10
    ```
    *   This tests basic IP connectivity to the server.
2.  **Check RADIUS Logs:**
    *  On the Mikrotik Router `/system logging print topics=radius` will output logs from the RADIUS service, which can help find issues if authentication is failing. If it shows a message saying "radius server not responding", review your network connectivity, firewall rules, and that the RADIUS service is running on your server.
    *   Check the RADIUS server logs for authentication attempts.
3. **Connect with a Client:** Attempt to connect a client device to the wireless network `vlan-60`. Monitor server logs and client behaviour.
    *   A successful connection should result in the client obtaining an IP address and the RADIUS server logging a successful authentication attempt. If this doesn't happen, you should receive an "Authentication Error" on the client. In that case, check the logs on the radius server and the router.
4. **Troubleshoot with Torch:** The `torch` command can show you real time network traffic. You can use it to see what traffic is going in and out between the Mikrotik and Radius server.
    ```mikrotik
    /tool torch interface=vlan-60 port=1812
    ```
    *  This can help you verify that RADIUS traffic is flowing and that the client is sending traffic.

## Related Features and Considerations

*   **RADIUS Accounting:** You can enable accounting on the MikroTik router to track the user's session usage. This requires a RADIUS server configured for accounting.
*  **Multiple RADIUS Servers**: You can configure multiple RADIUS servers and specify priorities and fallback mechanisms.
*  **Access Lists on Radius:** RADIUS can control user access based on time, location or device.
*   **VLANs:** Using RADIUS with VLANs enables you to create separate user groups and policies, which enhances network security and organization.
*   **Hotspot:** If you need to provide a landing page for the user authentication you can use hotspot services with RADIUS for extra functionality.
*   **Bandwidth control**: RADIUS servers can define bandwidth limits, which are then enforced by the Mikrotik.
*  **EAP-TLS**: When using certificates, make sure to install a valid certificate on both the radius server and each client.

## MikroTik REST API Examples

To configure the RADIUS server via the REST API, you would use the following:

**1. Add RADIUS Server:**

*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
        "address": "192.168.10.10",
        "secret": "your_radius_secret",
        "service": "wireless,ppp,login,hotspot,dhcp",
        "authentication-port": 1812,
        "timeout": 3
    }
    ```
*   **Expected Response (Success - HTTP 201 Created):**
    ```json
    {
       ".id": "*1" // or the ID number, this is dynamically created
    }
    ```
*   **Example Error Response (HTTP 400 Bad Request):**
    ```json
    {
        "message": "invalid value for argument 'address'",
        "detail": "invalid value for argument 'address' - invalid ip address 192.168.10"
    }
    ```
    *    **Handling Errors**: Always implement error handling in your API client.  Inspect the `message` and `detail` to identify the exact issue. A HTTP status code 4xx means the client request is invalid, while 5xx means there is a server error.

**2. Configure Wireless Interface (Security Profile):**

*   **Endpoint:** `/interface/wireless/security-profiles`
*   **Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
        "name": "radius-auth",
        "mode": "dynamic-keys",
         "authentication-types":"wpa2-psk,wpa2-eap",
        "eap-methods":"eap-peap,eap-tls",
        "radius-accounting": "no",
        "radius-mac-format":"XX:XX:XX:XX:XX:XX,upper-case"
    }
    ```
*   **Expected Response (Success - HTTP 201 Created):**
   ```json
   {
       ".id": "*1" // or the ID number, this is dynamically created
   }
   ```

*   **Example Error Response (HTTP 400 Bad Request):**
      ```json
    {
        "message": "invalid value for argument 'eap-methods'",
        "detail": "invalid value for argument 'eap-methods' - invalid value eap-pep"
    }
    ```
    *  Make sure your eap methods, authentication types, and other values are valid.

**3. Configure Wireless Interface**

* **Endpoint**: `/interface/wireless`
* **Method**: `PATCH`
* **Example JSON Payload**
```json
{
    ".id":"*3",
     "security-profile":"radius-auth",
     "mode":"ap"
}
```
   * `.id`:  This can be found using a `GET` request to this endpoint.
* **Expected Response (Success - HTTP 200 OK):**

```json
{
  "message": "updated"
}
```

* **Example Error Response (HTTP 400 Bad Request):**
   ```json
{
  "message": "invalid value for argument 'security-profile'",
  "detail": "invalid value for argument 'security-profile' - value not found"
}
   ```
   * The ID was not found or the security profile `radius-auth` has not been previously created.

## Security Best Practices

*   **Secure RADIUS Secret:** Use a strong, randomly generated secret. This secret must be kept secure and must match exactly between Mikrotik and RADIUS server.
*   **Access Control:** Restrict access to the MikroTik router using strong passwords and by limiting access from trusted IP addresses via firewall rules. Ensure that the REST API is only accessible from trusted networks.
*   **Encryption:** When possible, use secure EAP methods that support encryption such as EAP-TLS, or EAP-TTLS.
*   **Regular Updates:** Keep both the MikroTik RouterOS and the RADIUS server software updated. This is especially important for security patches.
*   **Disable unnecessary services:** Make sure only necessary services are enabled to minimize the attack surface on the RouterOS device.
*   **Monitor Logs:** Regularly check logs to identify suspicious activity.

## Self Critique and Improvements

This documentation provides a solid base for setting up RADIUS for wireless on a MikroTik. However:

*   **Advanced RADIUS Options:**  More advanced options like VLAN tagging per user, RADIUS CoA (Change of Authorization), and vendor-specific attributes can be included.
*   **EAP Details:**  Specific details on setting up RADIUS for different EAP types such as EAP-TLS with certificate installation can be added.
*   **Error Recovery:** Examples of scripts or automated processes that monitor the radius server and if a problem is detected it can notify the administrator.
*   **Real World Examples**: Detailed examples of how this configuration integrates into specific scenarios, like small offices, remote branches or public hotspots.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**
*   RADIUS is a network protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network.
*   The client (MicroTik router) sends a request to the RADIUS server with authentication credentials, the server then confirms if the user should have access and if so, what level of access.
*   It allows a single server to handle authentication for numerous clients, making it scalable and easy to manage.

## Detailed Explanation of Trade-offs

*   **PSK (Pre-Shared Key) vs. RADIUS:**
    *   PSK is simple and easy to set up but has poor security (if shared with too many people, or is not complex).
    *   RADIUS is more complex to configure but provides centralized, auditable authentication and allows for fine-grained user management.
    *   PSK is good for home use, but not suitable for businesses which require good security.
    *   RADIUS scales well for larger environments, where PSK does not.
*   **Different EAP Methods:**
    *   EAP-PEAP is easier to set up but less secure. EAP-TLS is considered more secure but requires certificate management. EAP-TTLS is a good option as it uses TLS encryption.
    *   The right EAP method for you depends on your security needs, server capability and technical ability to manage.
*   **RADIUS Accounting:**
    *   Enabling accounting provides useful data but requires more configuration.
    *   It's a trade-off between network management and complexity. If you do not require detailed user data it may be best to disable it.
*   **Timeout Settings**: Having the timeout value set too low, can cause issues, and it is recommended to use 3 seconds as the minimum value. Too high and it will cause delays.
* **Wireless interface mode AP or Bridge:** When setting the mode to bridge it requires setting a bridge, with the associated VLANs, which is more complex. Using the mode `ap` is a simpler config, which is suitable for most situations.

## Configuration for Specific RouterOS Versions

This documentation is primarily for RouterOS 7.11. There may be small command changes for older versions, but the core configuration logic should still apply. For RouterOS 6.48 or older, the configuration of security profiles, especially around EAP and dynamic keys, may slightly differ as they have been improved in version 7. If using an older version, always consult the official RouterOS documentation.

This complete guide should equip you with the knowledge and practical steps needed to implement RADIUS authentication on your MikroTik RouterOS 7.11 device. Be sure to test and adapt to suit your specific needs. Remember to always back up your configurations before making any changes.
