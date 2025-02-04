Okay, let's dive into configuring RADIUS authentication for a wireless network on MikroTik RouterOS 7.11, targeting an enterprise environment.

## Scenario Description:

We will configure a MikroTik router to authenticate wireless clients connecting to the `wlan-81` interface using a RADIUS server. This scenario is common in enterprise environments where centralized authentication and authorization are required for user access to the network. The router will act as a RADIUS client, forwarding authentication requests to the designated RADIUS server. Our subnet is `109.176.88.0/24` and the interface name is `wlan-81`.

## Implementation Steps:

Here's a detailed, step-by-step guide on configuring RADIUS authentication for your MikroTik:

### 1. Step 1: Configure the Wireless Interface

*   **Description:** We need to ensure the `wlan-81` wireless interface is properly configured, including the SSID and security settings. This step assumes you have basic wireless setup done, and we are changing the security settings only.
*   **Before:** Let's assume `wlan-81` is running with a basic setup using WPA2 PSK, we can check current config using this command:
    ```mikrotik
    /interface wireless print detail where name=wlan-81
    ```
    The output will include entries such as `mode=ap-bridge`, `ssid=your_ssid`, `security-profile=default`, `band=2ghz-b/g/n` and other parameters.
*   **Action:** We will configure the wireless interface to use WPA2 enterprise and assign a profile.
    ```mikrotik
    /interface wireless security-profiles add name=radius-profile mode=dynamic-keys authentication-types=wpa2-psk,wpa2-eap eap-methods=eap-tls,eap-peap,eap-mschap2
    /interface wireless set wlan-81 security-profile=radius-profile
    ```
*   **After:** The wireless interface `wlan-81` should now be using the new security profile which utilizes RADIUS. Now if we use the same command as before:
     ```mikrotik
    /interface wireless print detail where name=wlan-81
    ```
    We will see that the `security-profile` parameter has changed to `radius-profile`.
*   **Explanation:** The `security-profiles` command creates a new profile called `radius-profile` that utilizes WPA2 with both PSK and EAP authentication mechanisms. The `eap-methods` specifies the specific methods that will be used. This profile is then assigned to the `wlan-81` interface.

### 2. Step 2: Configure the RADIUS Client

*   **Description:** Now we must configure the RADIUS client on the MikroTik router to point to your RADIUS server.
*   **Before:** No radius clients are present if it is a fresh config. You can verify this using the command
    ```mikrotik
    /radius print
    ```
    If the output is empty, no radius clients have been configured yet.
*   **Action:** Add a new RADIUS client entry pointing to the RADIUS server IP address, secret, and the required service.
    ```mikrotik
    /radius add address=192.168.1.10 secret=mysecret service=wireless called-id-format=mac-address
    ```
*   **After:** The RADIUS client should now be present in the configuration. Running the command
    ```mikrotik
    /radius print
    ```
    should return an output containing the radius configuration we just added.
*   **Explanation:**
    *   `address=192.168.1.10`:  Specifies the IP address of your RADIUS server. Replace this with your actual RADIUS server's IP.
    *   `secret=mysecret`: Specifies the shared secret used to authenticate the MikroTik router to the RADIUS server.  Replace `mysecret` with the actual shared secret configured on your RADIUS server.
    *   `service=wireless`: Indicates that this RADIUS server is for wireless client authentication.
    *   `called-id-format=mac-address`: This specifies how the called-station-id RADIUS attribute will be formatted.

### 3. Step 3: Enable EAP on the Wireless Interface

*   **Description:** Enable EAP on the `wlan-81` interface to use the new radius profile.
*   **Before:** Check the current configuration for the radius profile used by `wlan-81`
    ```mikrotik
    /interface wireless security-profiles print detail where name=radius-profile
    ```
    It should already show `authentication-types=wpa2-psk,wpa2-eap`, and `eap-methods=eap-tls,eap-peap,eap-mschap2`
*   **Action:** We will verify again if EAP is enabled, as it should be due to our actions in Step 1.
    ```mikrotik
    /interface wireless security-profiles print detail where name=radius-profile
    ```
*   **After:** The profile configuration is still the same, because no changes have been made.
*   **Explanation:** Since we already configured `wpa2-eap` in the security profile and added EAP authentication methods in Step 1, EAP is already enabled on the wireless interface. We are verifying this here to highlight it is an important step.

### 4. Step 4: Configure IP Address for Wireless Clients

*   **Description:** If your DHCP server is not running on the MikroTik itself, ensure the wireless clients will get an IP address. We are not focusing on this so we will skip this step.

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands:

```mikrotik
/interface wireless security-profiles add name=radius-profile mode=dynamic-keys authentication-types=wpa2-psk,wpa2-eap eap-methods=eap-tls,eap-peap,eap-mschap2
/interface wireless set wlan-81 security-profile=radius-profile
/radius add address=192.168.1.10 secret=mysecret service=wireless called-id-format=mac-address
```

*   **Detailed Parameter Explanation:**

    | Command          | Parameter         | Description                                                                    |
    | :--------------- | :---------------- | :----------------------------------------------------------------------------- |
    | `/interface wireless security-profiles add` | `name`            |  The name of the security profile.                                            |
    |                   | `mode`            | The security mode of the profile.                                                |
    |                   | `authentication-types`    | Which types of authentication is allowed:  WPA2 PSK or EAP                          |
    |                   | `eap-methods`    | Which EAP methods can be used.                               |
    | `/interface wireless set` | `wlan-81`      |  The name of the wireless interface to apply the profile to.              |
    |                   | `security-profile`| The name of the security profile we created.                 |
    | `/radius add`       | `address`         | The IP address of the RADIUS server.                                          |
    |                   | `secret`          | The shared secret key between the MikroTik and the RADIUS server.             |
    |                   | `service`         | The service type associated with the RADIUS server (e.g., wireless).         |
    |                   | `called-id-format`    | The format used for called-station-id RADIUS attribute: MAC address is common.    |

## Common Pitfalls and Solutions:

*   **Incorrect Shared Secret:**  The most common issue. Verify that the shared secret on the MikroTik and the RADIUS server are *exactly* the same.
    *   **Solution:** Double-check and re-enter the shared secret on both devices. Use a simple, clear secret during testing, then change it to a complex secret after.
*   **RADIUS Server Unreachable:** The MikroTik must be able to communicate with the RADIUS server over the network.
    *   **Solution:** Use the `ping` tool on the MikroTik to verify connectivity to the RADIUS server. Check for any firewall rules that may be blocking traffic on UDP ports 1812 and 1813.
        ```mikrotik
        /ping 192.168.1.10
        ```
        If it fails check your router's firewall rules.
        ```mikrotik
        /ip firewall filter print
        ```
*   **Incorrect RADIUS Configuration on the Server:** The RADIUS server must be configured to accept authentication requests from the MikroTik's IP address.
    *   **Solution:** Verify your RADIUS server settings; verify that the MikroTik IP address is added to the list of clients, and the shared secret matches the MikroTik configuration.
*   **EAP Method Mismatch:** The EAP method selected on the MikroTik needs to match the supported EAP method on the RADIUS server.
    *   **Solution:** Check the MikroTik security profile EAP methods and ensure the RADIUS server supports one of them. Start with PAP/MSCHAPv2 for testing, then use more robust EAP methods.
*   **Debug Logging:** MikroTik's logging can be invaluable for debugging. Use the following command to enable detailed RADIUS debugging:
    ```mikrotik
    /system logging add topics=radius action=memory
    ```
    Then check logs with:
    ```mikrotik
    /log print
    ```
    Remember to remove the debug logging once the issue is resolved.

## Verification and Testing Steps:

1.  **Connect a Wireless Client:**  Attempt to connect a wireless device to the `wlan-81` network.
2.  **Verify RADIUS Logs:** If using Linux RADIUS servers like FreeRADIUS: Tail the RADIUS log files on your RADIUS server to check if the authentication request is received and processed.
    ```bash
    tail -f /var/log/freeradius/radius.log
    ```
3.  **Check MikroTik Logs:** Check the MikroTik logs for any radius-related errors:
    ```mikrotik
    /log print
    ```
4.  **Use Torch Tool:** Use the MikroTik's `torch` tool to capture and analyze network traffic between the MikroTik router and RADIUS server, specifically focusing on UDP ports 1812 and 1813.
    ```mikrotik
    /tool torch interface=ether1 port=1812,1813
    ```
    Replace `ether1` with your relevant interface.
5.  **Packet Capture:** Use a packet capture tool on a computer connected to the same network to capture the communication between the client, the router and the RADIUS server.
6.  **Enable Debug logging:** As described in the common pitfalls section.

## Related Features and Considerations:

*   **Accounting:**  RADIUS accounting can be enabled to track user sessions and resource usage. This is often desired in enterprise networks.
*   **VLAN Assignment:** RADIUS can also be used to dynamically assign VLANs to wireless clients based on user credentials.
*   **User Profiles:** You may have different user profiles that might require different authentication methods. The router can support different profiles using RADIUS and authentication settings.
*  **Centralized User Management**:  RADIUS allows you to centrally manage users, without having to configure users on a device-by-device basis.

## MikroTik REST API Examples (if applicable):

While MikroTik doesn't have extensive dedicated REST API endpoints for RADIUS configuration, you can use the generic command API to accomplish this.

```
# Example: Add a RADIUS client
# API endpoint: /rest/system/script
# Method: POST

{
    "command": "/radius/add",
    "parameters": {
        "address": "192.168.1.10",
        "secret": "mysecret",
        "service": "wireless",
        "called-id-format": "mac-address"
    }
}

# Response:
# If the command is executed successfully, you will see an ID being returned.
{
   ".id": "*4"
}

# Example: Retrieve RADIUS clients
# API endpoint: /rest/system/script
# Method: POST

{
    "command": "/radius/print",
        "parameters": {
        "detail": "true"
    }
}
# Expected Response:
# This would return all radius configuration.
[
  {
    ".id": "*1",
    "address": "192.168.1.10",
    "secret": "mysecret",
    "service": "wireless",
    "timeout": "3",
    "accounting": "no",
    "authentication": "yes",
    "called-id-format": "mac-address",
    "domain": ""
  }
]

# Example: Delete a RADIUS client
# API endpoint: /rest/system/script
# Method: POST
{
    "command": "/radius/remove",
    "parameters": {
        ".id": "*4"
    }
}

# Response:
# Empty response indicating removal.
{}
```

*   **Parameter Explanation:**

    *   `command`: The MikroTik CLI command to execute.
    *   `parameters`: JSON object containing the parameters for the command.
    *   `.id`: The unique identifier returned by a command. When calling the remove command, you must include the identifier of the object to be removed.
* **Error Handling:**
    * If a request fails, the API will return a JSON object containing an error message and an error code. The error code can be used to determine what has gone wrong.
    * The response is not returned directly by the API, but is contained in a JSON element called `result`, the whole response is also in a JSON object. The success status code is returned in a separate field called `status` in the response.

## Security Best Practices:

*   **Strong Shared Secret:**  Use a strong, randomly generated shared secret that is difficult to guess.
*   **Restrict Access to RADIUS Server:**  Limit access to the RADIUS server to only the necessary devices. Use firewalls and access control lists (ACLs).
*   **Use Encrypted EAP Methods:** When using EAP, use EAP-TLS or EAP-PEAP with strong ciphers to protect user credentials. Avoid using PAP if possible.
*   **Regularly Review RADIUS Configuration:** Regularly check the RADIUS server configuration, the shared secrets, and the allowed clients to ensure there are no unauthorized devices.
*   **Implement Network Segmentation:** Segment your network and place the RADIUS server in a secure area to minimize exposure.
*  **Properly Secure Management Access**: Ensure management access to the Mikrotik router and the RADIUS server is secured with strong passwords and proper access control.

## Self Critique and Improvements:

*   **Error Handling in Examples:**  While I've provided troubleshooting steps, my examples could be improved by including more explicit examples of error handling and error responses within the MikroTik CLI and REST API.
*   **Scripting for Automation:** I could provide scripting examples for automating the configuration deployment, including script exports and imports, and using REST API for automated configuration.
*   **RADIUS Accounting Configuration:** Providing configuration and explanation of RADIUS accounting could improve the depth of this guide.
*   **VLAN Assignment:** Adding configuration of VLAN assignment via radius will make this setup more practical for enterprise users.

## Detailed Explanation of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users who connect to a network. It's commonly used to authenticate wireless users connecting to Wi-Fi networks, VPN connections, and other network access methods.

*   **Authentication:** The process of verifying a user's identity.
*   **Authorization:** The process of determining what a user is allowed to do on the network.
*   **Accounting:** The process of tracking resource usage by users.

A RADIUS system consists of:

*   **RADIUS Client:** The device that initiates the authentication request (e.g., the MikroTik router).
*   **RADIUS Server:** A server that stores user credentials and determines authentication and authorization.

When a user tries to connect to the network, the RADIUS client sends an authentication request to the RADIUS server with the user's credentials. The RADIUS server checks the credentials, and if they're correct, it authorizes network access. The RADIUS server can also keep track of a user's session time and the network resources they use. This enables more advanced security, accountability and monitoring.

## Detailed Explanation of Trade-offs:

*   **EAP Method Selection:** Choosing the right EAP method is crucial for security. EAP-TLS is considered the most secure but requires a complex Public Key Infrastructure (PKI). EAP-PEAP is a common compromise, offering good security and easier configuration. EAP-MSCHAPv2 is easier to configure but offers less security compared to TLS and PEAP. PAP should be avoided if possible because it sends user credentials in clear text.
*   **RADIUS vs. Local Authentication:** RADIUS provides centralized user management and better auditing capabilities, but it introduces dependency on an external RADIUS server. Local authentication is simpler for smaller networks, but it is more difficult to manage and scale.
*   **Centralized vs Distributed Configuration:** Centralized RADIUS configuration enables more efficient management of users and networking devices, but introduces a single point of failure. Distributed configuration may require more maintenance, but is more fault tolerant.
*   **Shared Secret Strength vs Complexity:** A strong shared secret is essential, but complex secrets require more careful management.
* **Centralized vs Local Management**: RADIUS provides centralized authentication and management of users, this approach is more difficult to setup and maintain, but is ideal for larger environments. Locally managed users are easier to setup and maintain, but are more difficult to scale to larger environments.

## Configuration for Specific RouterOS Versions:

This guide specifically targets RouterOS 7.11 and is compatible with 6.48 and 7.x.  All commands and parameters mentioned are available in these versions.  If targeting older versions, ensure the `wpa2-eap` options are valid within your version and note there may be slightly different security-profiles parameter names.

This comprehensive guide should equip you with the necessary knowledge to configure RADIUS authentication on your MikroTik router. Remember to always test your configurations thoroughly in a controlled environment before implementing them in a production network.
