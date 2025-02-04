Okay, let's dive into a detailed RADIUS implementation on MikroTik RouterOS, targeting version 7.12, with an expert configuration for an SMB network.

## Scenario Description:

We are setting up RADIUS authentication for wireless clients connecting to the `wlan-92` interface, using a subnet of 33.135.148.0/24. This setup will require a RADIUS server to handle authentication requests. We will configure the MikroTik router to act as a RADIUS client, forwarding authentication requests from the wireless interface to the specified RADIUS server, and enforcing user access based on the RADIUS response. This assumes the RADIUS server is already set up.

## Implementation Steps:

1. **Step 1: Interface Configuration**

   * **Before:** Initially, the `wlan-92` interface likely has basic settings or is inactive.
   * **Action:** We need to ensure the `wlan-92` interface is correctly configured with a static IP address from the target subnet and is enabled. Additionally, we will set up wireless security profile to enable RADIUS authentication.
   * **MikroTik CLI Command:**
     ```mikrotik
     /interface wireless
     set wlan-92 disabled=no mode=ap-bridge ssid="MyNetwork" band=2ghz-b/g/n channel-width=20/40mhz-Ce frequency=2437 security-profile=default
     /interface wireless security-profiles
     add authentication-types=wpa2-psk,wpa2-eap eap-methods=eap-peap,eap-tls,eap-ttls management-protection=allowed mode=dynamic-keys name=radius-security supplicant-identity=radius
      /ip address
     add address=33.135.148.1/24 interface=wlan-92
     ```
   * **Explanation:**
        *   `/interface wireless set wlan-92 disabled=no ...` Enables and configures basic wireless settings
        *  `/interface wireless security-profiles add ...` Creates a new security profile named radius-security for RADIUS authentication.
        *   `add address=33.135.148.1/24 interface=wlan-92` Assigns an IP address to the wireless interface.
   * **Effect:** The `wlan-92` interface will be enabled, ready to accept wireless connections and with a security profile ready to accept RADIUS authentication.

2. **Step 2: RADIUS Client Configuration**

   * **Before:** No RADIUS client configuration exists on the router.
   * **Action:**  We will add a new RADIUS client entry specifying the IP address, shared secret, and authentication/accounting ports of the RADIUS server.
   * **MikroTik CLI Command:**
     ```mikrotik
     /radius
     add address=192.168.1.100 secret="MySecret" service=wireless timeout=30s
     ```
   * **Explanation:**
        *   `/radius add ...` Adds a new RADIUS client configuration.
        *   `address=192.168.1.100`: The IP address of the RADIUS server.
        *  `secret="MySecret"`: The shared secret between the router and the RADIUS server. *Important: Replace "MySecret" with a strong, unique password.*
        *   `service=wireless`: Specifies that this client is for wireless service.
        * `timeout=30s` Sets a timeout of 30 seconds for the RADIUS server to respond
   * **Effect:** The router can now send authentication requests to the RADIUS server at the specified IP.

3. **Step 3: Linking RADIUS to Wireless Interface**

   * **Before:** The `wlan-92` interface uses default security settings (usually WPA2-PSK) or is set up without RADIUS.
   * **Action:** Now we need to attach the newly create security profile to the wlan-92 interface.
   * **MikroTik CLI Command:**
      ```mikrotik
      /interface wireless
      set wlan-92 security-profile=radius-security
      ```
   * **Explanation:**
        * `/interface wireless set wlan-92 security-profile=radius-security`:  Links the radius-security profile to the wlan-92 interface.
   * **Effect:** The `wlan-92` interface will now use RADIUS authentication as defined in `radius-security` security profile.

4. **Step 4: (Optional) Accounting Configuration**

    * **Before:** Accounting might not be enabled, and will not be required if you are just authenticating with RADIUS.
    * **Action:** If you want usage statistics, we need to enable accounting requests. We will use the same server for accounting.
    * **MikroTik CLI Command:**
        ```mikrotik
         /radius
         set [find address=192.168.1.100] accounting=yes
        ```
   * **Explanation:**
        *  `/radius set [find address=192.168.1.100] accounting=yes`: Enables accounting for the radius server at 192.168.1.100.
   * **Effect:** The Router will send accounting start, interim, and stop messages to the RADIUS server.

## Complete Configuration Commands:

```mikrotik
/interface wireless
set wlan-92 disabled=no mode=ap-bridge ssid="MyNetwork" band=2ghz-b/g/n channel-width=20/40mhz-Ce frequency=2437 security-profile=default
/interface wireless security-profiles
add authentication-types=wpa2-psk,wpa2-eap eap-methods=eap-peap,eap-tls,eap-ttls management-protection=allowed mode=dynamic-keys name=radius-security supplicant-identity=radius
/ip address
add address=33.135.148.1/24 interface=wlan-92
/radius
add address=192.168.1.100 secret="MySecret" service=wireless timeout=30s
/interface wireless
set wlan-92 security-profile=radius-security
/radius
set [find address=192.168.1.100] accounting=yes
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** Router cannot connect to the RADIUS server.
    *   **Solution:**
        *   Verify the IP address of the RADIUS server is correct.
        *   Check network connectivity (ping/traceroute).
        *   Check if the RADIUS server is running and reachable from the network.
        *   Check for firewall rules that might be blocking the connection on the router, or the RADIUS server machine
*   **Incorrect Shared Secret:**
    *   **Problem:** Authentication fails due to incorrect secret.
    *   **Solution:** Ensure that the shared secret on the router matches exactly what is configured on the RADIUS server. This is case sensitive.
*   **Authentication Failures:**
    *   **Problem:** Users cannot authenticate, despite the server being reachable.
    *   **Solution:**
        *   Verify that usernames and passwords match the user database on the RADIUS server.
        *   Check the RADIUS server logs for errors, for example rejected authentications.
        *   Ensure that the correct RADIUS protocol and ports are configured on both the router and RADIUS server
*   **Timeout Issues:**
    *   **Problem:** Long timeouts or dropped packets on authentications.
    *   **Solution:** Try increasing the RADIUS timeout `timeout` parameter. Check for network issues.
*   **Security Profile Issues**
    *   **Problem:** Wireless clients do not connect or get stuck in a connecting loop.
    *   **Solution:** Check that the authentication types in the security profile match the ones enabled in the RADIUS server, and that the eap-methods are supported by your clients.

## Verification and Testing Steps:

1.  **Network Connectivity:**
    *   `ping 192.168.1.100`: Test connectivity to the RADIUS server.
    *   `traceroute 192.168.1.100`: Trace path to ensure there aren't any routing issues.

2. **Authentication Test:**
     *   Attempt to connect a wireless client to the `MyNetwork` SSID.
     *   Monitor RADIUS server logs to verify authentication requests and responses.
     *   Check MikroTik logs for any RADIUS related errors using:
         ```mikrotik
         /log print follow-only file=test.log
         ```
     *   Use torch to inspect packets going to the RADIUS server
          ```mikrotik
          /tool torch interface=wlan-92 port=1812 protocol=udp
          ```

3. **Accounting Test (If Enabled):**
    *   Ensure that accounting messages are being sent to the RADIUS server.
    *  Verify data is captured in the accounting database, if configured on the RADIUS server.

## Related Features and Considerations:

*   **MAC Address Authentication:**  You can configure the RADIUS server to also check MAC addresses, allowing for MAC-based access lists.
*   **VLAN Assignment:** RADIUS can be configured to assign VLANs to clients based on their user credentials.
*   **Dynamic Rate Limiting:**  You can use RADIUS attributes to dynamically limit the bandwidth available to each user.
*   **User Profiles:** You can set user profiles with varying levels of access based on time of the day, day of the week, etc.
*   **External Captive Portal:** You can use a captive portal in combination with the radius server, this will redirect wireless clients to a login page when they connect to the network.

## MikroTik REST API Examples (if applicable):

Here are a few REST API examples using the RouterOS API. Please note that before making any API calls, the `api` service must be enabled on the router using `ip service enable api` (or using Winbox under `IP` > `Services`).

1.  **Add a RADIUS Client:**

    *   **Endpoint:** `/radius`
    *   **Method:** `POST`
    *   **Payload:**
        ```json
        {
            "address": "192.168.1.100",
            "secret": "MySecret",
            "service": "wireless",
            "timeout": "30s"
        }
        ```
    *   **Example Response (Success):**
         ```json
          {
            ".id": "*1",
           "address": "192.168.1.100",
           "secret": "MySecret",
           "service": "wireless",
           "timeout": "30s"
          }
        ```
       Note the `.id` field is the ID of the newly created radius client.

     *   **Error Handling:** If the request is incorrect, for example the address is invalid, the response will contain an error code and message.
        ```json
         {
             "message": "invalid value for argument 'address'",
            "category": 2,
            "code": 9
        }
         ```

2.  **Get RADIUS Clients:**

    *   **Endpoint:** `/radius`
    *   **Method:** `GET`
    *   **Payload:** None
    *   **Example Response:**
      ```json
      [
          {
              ".id": "*1",
              "address": "192.168.1.100",
              "secret": "MySecret",
              "service": "wireless",
              "timeout": "30s",
              "accounting": "no"
          }
      ]
      ```

3.  **Enable Accounting:**

    *   **Endpoint:** `/radius/*1` (Replace `*1` with the `.id` of the RADIUS entry)
    *   **Method:** `PATCH`
    *   **Payload:**
        ```json
        {
            "accounting": "yes"
        }
        ```
     *  **Example Response (Success):**
        ```json
         {
           "message": "property set"
          }
        ```
    *   **Error Handling:** If the  radius id doesn't exists the API will return an error message
        ```json
           {
               "message": "no such item",
                "category": 4,
                "code": 5
             }
        ```
*Note:*
  * Make sure to include an authentication header when sending API requests, if not enabled the request will fail.
  * Always double check your payload before sending it, wrong payloads can introduce configuration errors.

## Security Best Practices

*   **Strong Shared Secret:** Use a long, complex, randomly generated string for the RADIUS secret, and change it periodically.
*   **Restrict Access:** Only allow connections from the MikroTik router IP address to the RADIUS server. Configure firewall rules for the MikroTik to restrict access to the radius port (udp 1812,1813, etc.).
*   **Secure RADIUS Server:**  Ensure your RADIUS server is secured and up to date.
*   **TLS/EAP:** If possible, use EAP-TLS (or a variant of EAP that provides more security). WPA2-PSK is more susceptible to attacks.
*   **Monitor Logs:** Regularly check both MikroTik and RADIUS server logs for any suspicious activity.
*   **Update RouterOS:** Keep your MikroTik RouterOS up to date to patch any security vulnerabilities.

## Self Critique and Improvements

*   **Current configuration:** This configuration is basic and functional for a simple SMB network but can be expanded.
*   **Improvements:**
    *   **VLAN assignment:** The next logical step would be implementing VLAN assignment for users based on their RADIUS login.
    *   **Advanced authentication:** It is recommended to use EAP-TLS as the only authentication method.
    *   **Rate Limiting:** Rate limiting per user can be added to prevent excessive bandwidth usage.
    *   **Monitoring:** Setting up monitoring to track Radius server availability is important for uptime.
    *   **Logging:** Logging must be more detailed for auditing and troubleshooting.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**
RADIUS is a networking protocol used for centralized Authentication, Authorization, and Accounting (AAA) for network access. When a client attempts to access a network resource (like a Wi-Fi network), the router acts as a RADIUS client and sends an authentication request to the RADIUS server. The server checks the credentials and sends back a response to allow or deny the access. This allows for a centralized way of managing user authentication and security policies across different access points. In addition to authentication, RADIUS also handles accounting which provides information on resource usage.

## Detailed Explanation of Trade-offs

*   **WPA2-PSK vs. RADIUS (EAP-PEAP, EAP-TLS, etc.):** WPA2-PSK is simpler to set up, but it uses a single shared key. If a key is compromised, the whole network can be at risk. RADIUS offers user-level authentication, improving security by controlling access on a per-user basis. However, RADIUS requires setting up and maintaining a RADIUS server. EAP-TLS offers the best security but is more complex to configure as it requires certificates.
*   **Plain Secret vs. TLS:**  Using plain text shared secrets is more susceptible to man-in-the-middle attacks. It is recommended to use secure certificates for authenticating the RADIUS server.
*   **Internal RADIUS vs. External RADIUS:** An internal radius server will add CPU and memory load to the device. For larger networks, it is recommended to have a separate machine to act as radius server.
*   **Accounting Data:** Accounting data can help with billing and usage analysis, but it requires storage space and processing power on the RADIUS server. Disabling it will reduce resource consumption.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS versions 7.x and above and tested on 7.12, but can also be used in 6.48, with slight adjustments.

*   **RouterOS 6.48 Differences:**
    *   The `security-profile` configuration might have slightly different options or structure. The core functionalities are the same but parameter names might have slight changes, use the Winbox GUI to help find corresponding parameters.
    *   The REST API might have a different endpoint structure, or some functions might be missing.
    *  The default GUI will be slightly different.

---
This detailed documentation provides a solid foundation for setting up RADIUS authentication on a MikroTik router. Make sure to adjust the settings and configuration to match your specific needs and environment. Always test thoroughly and monitor your configuration for any errors.
