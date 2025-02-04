Okay, let's dive into a detailed technical document for implementing RADIUS authentication on a MikroTik router (RouterOS 7.11, specifically) with the given parameters.

## Scenario Description:

This scenario involves configuring a MikroTik router to act as a RADIUS client, authenticating network users against a central RADIUS server. The router, on the `ether-16` interface, will be part of the `130.123.196.0/24` subnet. User authentication requests originating from the `ether-16` subnet will be forwarded to the RADIUS server for authentication. This is a common setup for providing secure network access in an SMB environment.

## Implementation Steps:

**1. Step 1: Define the RADIUS Server**
   - **Explanation:** We first need to tell the MikroTik router about the RADIUS server, including its IP address, shared secret, and authentication/accounting ports.
   - **Before:** The router has no RADIUS server configured yet.
   - **Action:**
      - **CLI:**
         ```mikrotik
         /radius add address=192.168.10.10 secret="MySecretPassword" service=ppp,hotspot,login timeout=30s accounting-port=1813 authentication-port=1812
         ```
      - **Winbox GUI:** Go to `RADIUS` under `PPP` menu or `/radius`, click `+` and fill in the parameters.
   - **After:** The router now knows the details of your RADIUS server, including a shared secret.
   - **Effect:** The router is now able to communicate with the configured RADIUS server.
   - **Details of the command:**
     - `/radius add`: Creates a new radius server configuration.
     - `address=192.168.10.10`: Specifies the IP address of your RADIUS server.
     - `secret="MySecretPassword"`: Specifies the shared secret used for communication with the RADIUS server.
     - `service=ppp,hotspot,login`: Indicates the types of services that will use this RADIUS server (e.g., PPP, Hotspot, system login).
     - `timeout=30s`: Sets a timeout of 30 seconds for responses from the RADIUS server.
     - `accounting-port=1813`: Sets the UDP port used for accounting.
     - `authentication-port=1812`: Sets the UDP port used for authentication.

**2. Step 2:  Configure a User Profile to Use RADIUS**
    - **Explanation:** We need to configure a user profile that utilizes RADIUS for authentication within our given subnet. This is often done within the Hotspot functionality.
    - **Before:** The router doesn't have any user profile utilizing RADIUS.
    - **Action:**
        -   **CLI**
             ```mikrotik
             /ip hotspot user profile add name="radius_profile" use-radius=yes
             ```
        -   **Winbox GUI:** Go to `/ip hotspot user profile` click on `+` and fill in the parameters and check `Use RADIUS`
    - **After:** A new user profile exists, configured to use RADIUS authentication.
    - **Effect:** Users with this profile will have authentication requests forwarded to the RADIUS server.
    - **Details of the command:**
        - `/ip hotspot user profile add`: Creates a new user profile.
        - `name="radius_profile"`: Specifies the name of this profile.
        - `use-radius=yes`: Enables RADIUS authentication for this profile.

**3. Step 3: Configure the Hotspot Server on Interface `ether-16`**

   - **Explanation:** We now need to set up a Hotspot server on the specified interface, which will enforce authentication using our newly created RADIUS profile.
   - **Before:** No Hotspot is active on `ether-16`.
   - **Action:**
      - **CLI:**
         ```mikrotik
         /ip hotspot add name="hotspot_ether16" interface=ether-16 address-pool=130.123.196.10-130.123.196.250 profile=radius_profile disabled=no
         /ip hotspot profile set [find name="radius_profile"] dns-name="hotspot.example.com" html-directory="hotspot"
         ```
     - **Winbox GUI:**  Go to `/ip hotspot servers` click `+`, select `ether-16` for interface, create a `address-pool` of `130.123.196.10-130.123.196.250` click the `Profile` and select `radius_profile`, and uncheck `disabled`. Then, go to `/ip hotspot profile` click on `radius_profile`, and set `dns-name` to `hotspot.example.com` and set the `html-directory` to `hotspot`. You can also create a new profile or edit the default one.
   - **After:** A hotspot is running on interface `ether-16` using RADIUS.
   - **Effect:** Devices connected to `ether-16` will now be redirected to the Hotspot login page and require RADIUS authentication.
   - **Details of the command:**
        - `/ip hotspot add`: Adds a new Hotspot server.
        - `name="hotspot_ether16"`: Specifies the name of the hotspot instance.
        - `interface=ether-16`: Specifies the interface for the hotspot.
        - `address-pool=130.123.196.10-130.123.196.250`: Defines the IP range to be assigned to clients.
        - `profile=radius_profile`: Links this hotspot server to the 'radius_profile' we created.
        - `disabled=no`: Enables the hotspot.
        - `/ip hotspot profile set`: Modifies the existing hotspot profile.
        - `[find name="radius_profile"]`: Finds the profile `radius_profile`.
        - `dns-name="hotspot.example.com"`: sets the DNS name for the hotspot, used during redirection.
        - `html-directory="hotspot"`: sets the directory where hotspot login pages are located.

**4. Step 4 (Optional): Enable logging (for troubleshooting)**
   - **Explanation:** For troubleshooting, enabling logging of RADIUS activity is extremely useful.
   - **Before:** No specific logging for RADIUS is enabled.
   - **Action:**
        - **CLI:**
            ```mikrotik
            /system logging add topics=radius,debug action=memory
            ```
        - **Winbox GUI:** Go to `/system logging`, click `+`, select `radius` and `debug` for topics and `memory` for action.
   - **After:** Logs will now be stored in memory for RADIUS traffic.
   - **Effect:** You can inspect logs for RADIUS requests and responses.
   - **Details of the command:**
        - `/system logging add`: Adds a new log action.
        - `topics=radius,debug`: Specifies logging for both radius events and debug information.
        - `action=memory`: Sets the log to the memory.

## Complete Configuration Commands:

```mikrotik
/radius add address=192.168.10.10 secret="MySecretPassword" service=ppp,hotspot,login timeout=30s accounting-port=1813 authentication-port=1812
/ip hotspot user profile add name="radius_profile" use-radius=yes
/ip hotspot add name="hotspot_ether16" interface=ether-16 address-pool=130.123.196.10-130.123.196.250 profile=radius_profile disabled=no
/ip hotspot profile set [find name="radius_profile"] dns-name="hotspot.example.com" html-directory="hotspot"
/system logging add topics=radius,debug action=memory
```

## Common Pitfalls and Solutions:

- **Shared Secret Mismatch:** If the shared secret on the MikroTik does not match the RADIUS server, authentication will fail. Verify that both secrets are identical. The logs will often give an "invalid authenticator" error.
- **Firewall Issues:** Make sure that your router’s firewall allows communication on UDP ports 1812 and 1813 to the RADIUS server’s IP address. Use `/tool torch` to see if packets are being dropped.
- **Incorrect Server IP:** If the RADIUS server IP is wrong, the router won't connect to it. Double-check the IP address.
- **RADIUS Server Unavailable:** If your RADIUS server is down or unreachable, authentication will fail. Verify the server is working.
- **Incorrect Profile Configuration:** The user profile should have `use-radius=yes` set. Also, make sure the Hotspot server is associated with that profile. Use `/ip hotspot print detail` to see the hotspot configuration.
- **DNS and HTTP Redirection:** Ensure that DNS is configured for the router and that HTTP redirection is set up correctly on the Hotspot interface. If a client does not get redirected, the hotspot is not working properly. The logs will often reveal a problem with the hotspot functionality.
- **High CPU/Memory Usage:** A large number of simultaneous RADIUS requests can cause increased resource usage on the router. The `/system resource print` command will be your best friend for this problem, along with the profiling tools of RouterOS. Increase hardware resources if the router cannot keep up.

## Verification and Testing Steps:

1.  **Connect a client:** Connect a laptop or other device to the `ether-16` interface.
2.  **Attempt HTTP access:** Try to open any HTTP website in the client's browser.
3.  **Redirection:** The client should be redirected to the Hotspot login page.
4.  **Enter RADIUS credentials:** Input username and password credentials that are valid on your RADIUS server.
5.  **Successful login:** If configured correctly, the client should be authenticated by the RADIUS server and have internet access.
6.  **MikroTik logs:** Check MikroTik system logs (`/system logging print`) for RADIUS related messages for debugging. The log will tell you exactly what is going on.
7.  **Torch tool:** Use `/tool torch interface=ether-16 src-address=<client IP>` and `/tool torch interface=ether-16 dst-address=<radius server IP>` to see the traffic during the authentication.
8.  **RADIUS Server Logs:** check if the RADIUS server logs have incoming requests.
9.  **Packet Captures:** If everything fails, use packet captures (such as WireShark) on both the MikroTik and RADIUS server to see the packets being transferred.

## Related Features and Considerations:

-   **RADIUS Accounting:** You can enable RADIUS accounting to track user sessions. Add `accounting=yes` parameter to `/ip hotspot user profile`. Use `/radius print detail` to see all parameters related to the server configuration.
-   **MAC Address Authentication:**  You can use MAC addresses in conjunction with RADIUS for authentication, useful for devices with static IP assignments. Add the parameter `mac-cookie=yes` to `/ip hotspot profile`.
-   **Dynamic Authorization (CoA):** RouterOS supports Dynamic Authorization (CoA) allowing the RADIUS server to change user configurations during a session. You can implement this feature on the RADIUS server.
-   **HTTPS for Hotspot Login:** It is important to implement HTTPS redirection for the hotspot login page to avoid man-in-the-middle attacks. Set this option in the `/ip hotspot profile`.
- **Multiple RADIUS Servers:** Implement multiple RADIUS servers in order to provide redundancy in the authentication mechanism. The `/radius` command will take a list of IP addresses if it is configured as such.
- **Load balancing:** With multiple radius servers, load balancing strategies can be implemented in order to distribute the load for authentication between them.

## MikroTik REST API Examples:

**Adding a RADIUS Server:**

```http
POST /radius
Content-Type: application/json

{
  "address": "192.168.10.10",
  "secret": "MySecretPassword",
  "service": "ppp,hotspot,login",
  "timeout": "30s",
  "accounting-port": "1813",
  "authentication-port": "1812"
}
```

**Response (success):**

```http
{
  ".id": "*0",
  "address": "192.168.10.10",
  "secret": "*****",
  "service": "ppp,hotspot,login",
  "timeout": "30s",
  "accounting-port": "1813",
  "authentication-port": "1812"
}
```

**Response (failure):**

```http
{
    "message": "invalid value of timeout",
    "error": "true"
}
```

**Explanation:**

-   **Endpoint:** `/radius`
-   **Method:** POST
-   **Payload:** JSON object with the RADIUS server details.
-   **Parameters:** same as CLI parameters mentioned above.
-   **Response:** JSON object with the server's details if successful; JSON with an error message otherwise.

**Error Handling:** Use the `error` field in the response to check if an error occurred. If there is an error, the `message` field will contain the error message.

**Modifying a Hotspot Profile:**
```http
PUT /ip/hotspot/profile/radius_profile
Content-Type: application/json

{
  "use-radius": "true",
  "dns-name": "hotspot.example.net",
  "html-directory": "my-hotspot"
}
```
**Response (success):**
```http
{
  "name": "radius_profile",
  "use-radius": "true",
  "dns-name": "hotspot.example.net",
  "html-directory": "my-hotspot"
}
```

**Response (failure):**

```http
{
    "message": "invalid value of name",
    "error": "true"
}
```

**Explanation:**
- **Endpoint:** `/ip/hotspot/profile/radius_profile`
-   **Method:** PUT
-   **Payload:** JSON object with the changes you want to make.
-   **Parameters:** same as CLI parameters mentioned above.
-   **Response:** JSON object with the modified hotspot profile details.

## Security Best Practices

-   **Secure Shared Secret:** Use a strong, complex shared secret between the router and the RADIUS server. Keep it confidential.
-   **Firewall Rules:** Restrict access to the RADIUS server ports (1812/1813) only from trusted networks and IPs. Never expose the ports to the public internet.
-   **HTTPS for Hotspot:** Ensure HTTPS is enabled for the Hotspot login page to prevent credential interception.
-  **Regular Auditing:** Regularly check for any vulnerabilities on the router, and update firmware.
-   **Logging:** Regularly monitor your logs for any suspicious activity.

## Self Critique and Improvements

This configuration is a good starting point, but it can be further improved:
-   **More specific firewall rules:** Add specific firewall rules for RADIUS server access, only allowing the specific router IP address to access the server.
-   **Centralized logging:** Route the log events to a centralized server for better monitoring.
-   **Advanced RADIUS Attributes:** Include more advanced RADIUS attributes, such as session timeouts, data limits, and VLAN assignment for more customized control over network access.
-   **Multi-Factor Authentication:** Explore the use of RADIUS-based MFA for an extra layer of security, if the RADIUS server provides it.
- **Dynamic DNS for the RADIUS server:** If the server is not on a static IP, implement a way for the router to automatically update the address of the RADIUS server.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) management for users who access a network. It works on a client-server model:

*   **RADIUS Client:** The device or application requesting authentication (e.g., MikroTik router).
*   **RADIUS Server:** The server which stores user credentials and policies, and performs authentication, authorization and accounting.

The authentication process involves the client sending authentication requests to the server, which then verifies the credentials. The authorization phase involves setting specific access levels. Finally, accounting tracks the user's network usage for statistical purposes.

## Detailed Explanation of Trade-offs

When implementing RADIUS authentication with a hotspot on a MikroTik router, it's essential to understand the trade-offs between different configuration choices:

- **Simple Password vs. RADIUS:** Simple password authentication is easy to implement, but it doesn’t scale and is far less secure. RADIUS provides centralized, robust authentication but adds complexity.
- **Local Hotspot User Profile vs. RADIUS:**  Local profiles are fine for small networks. RADIUS is more beneficial for managing users across a larger network, allowing for centralized management and better reporting.
- **Centralized Logging vs. Local Logging:** Centralized logging requires a separate server but makes management much easier and provides redundancy. Local logging is easier, but has higher risks.
- **No Encryption vs. HTTPS:** Using HTTPS for the Hotspot page adds security, but increases CPU usage. Not using HTTPS creates a big security hole, since user credentials could be harvested during login.

## Configuration for Specific RouterOS Versions:

This configuration is specifically targeted for RouterOS 7.11. The commands used here are common across many versions of RouterOS 7.x and 6.48. If targeting an older version, consult the specific documentation for that version to ensure compatibility. For example, older versions might have slight differences in the way Hotspot commands are structured or how RADIUS servers are configured. Always consult the RouterOS documentation for the specific version you are using.

This is a thorough guide for implementing RADIUS on MikroTik RouterOS 7.11. Let me know if you have any other questions!
