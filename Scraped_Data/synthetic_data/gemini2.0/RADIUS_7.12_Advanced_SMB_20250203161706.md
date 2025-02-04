Okay, let's dive into configuring RADIUS authentication on a MikroTik router, focusing on RouterOS 7.12, within an SMB environment, specifically targeting the 45.66.74.0/24 subnet on the `bridge-83` interface.

## Scenario Description:

We will configure the MikroTik router (RouterOS 7.12) to authenticate network clients using a RADIUS server. This configuration will be applied to the `bridge-83` interface which is connected to our internal network (45.66.74.0/24). This means any device attempting to connect to the network on `bridge-83` will need to authenticate against the defined RADIUS server first. We will use MAC-based authentication for this configuration.

## Implementation Steps:

Here's a step-by-step guide to set up RADIUS authentication for the bridge interface.

### Step 1: Add a RADIUS Server Configuration

* **Goal:** Define the connection details for your RADIUS server.
* **Why:** This tells the MikroTik router where to send authentication requests.
* **CLI Instructions:**

   Before:
    ```
    /radius print
    ```
   *Output:*
   ```
    Flags: X - disabled
    #   ADDRESS          SECRET             TIMEOUT   ACCOUN    SERVIC    USAGE
   ```
   After:
    ```
    /radius add address=192.168.1.100 secret=testing123 timeout=3 accounting=yes service=login,ppp,wireless,hotspot,dhcp usage=authentication
    ```
    *Output:*
    ```
    Flags: X - disabled
    #   ADDRESS          SECRET             TIMEOUT   ACCOUN    SERVIC                         USAGE
    0   192.168.1.100   testing123         3         yes      login,ppp,wireless,hotspot,dhcp   authentication
    ```
*   **Winbox GUI:** Navigate to `RADIUS` in the left menu. Click the `+` button and add your server.

| Parameter      | Description                                                                                                   | Example Value       |
|-----------------|---------------------------------------------------------------------------------------------------------------|---------------------|
| `address`      | The IP address or hostname of the RADIUS server.                                                                | `192.168.1.100`     |
| `secret`       | The shared secret key used to encrypt communication with the RADIUS server. **Keep this secure!**          | `testing123`        |
| `timeout`      |  The time in seconds to wait for a response from the RADIUS server before considering the request timed out.  |  `3`                |
| `accounting`   | Enables RADIUS accounting.                                                                                 | `yes`              |
| `service`      | Services that will use RADIUS authentication.                                                               | `login,ppp,wireless,hotspot,dhcp`        |
| `usage`        |  Specifies that this RADIUS server is used for authentication.                                            |  `authentication`    |

* **Effect:** Adds the RADIUS server details to the MikroTik router, enabling it to communicate with the server.
* **Explanation:**
  - We define the address, secret, timeout, and services that will use this server.
  - The `usage` parameter is set to authentication, meaning this server will only be used for authentication requests.

### Step 2: Configure Bridge to use RADIUS MAC Authentication

* **Goal:** Enable MAC authentication on the `bridge-83` interface.
* **Why:** This makes the bridge use RADIUS to authorize clients attempting to connect.
* **CLI Instructions:**
   Before:
   ```
   /interface bridge port print
   ```
   *Output:*
   ```
    Flags: X - disabled, I - inactive, H - hw offload
    #   INTERFACE         BRIDGE     PRIORITY PATH-COST  HORIZON   PVID  FRAME-TYPES      
   0   ether1             bridge-83     0        10    none       1      admit-all         
   1   wlan1              bridge-83    0        10     none       1    admit-all
   ```
    After:
    ```
    /interface bridge port set [find interface=ether1] authentication=mac-radius
    ```
    *Output:*
   ```
    Flags: X - disabled, I - inactive, H - hw offload
    #   INTERFACE         BRIDGE     PRIORITY PATH-COST  HORIZON   PVID  FRAME-TYPES         AUTHENTICATIO
   0   ether1            bridge-83    0        10    none       1      admit-all          mac-radius
   1   wlan1              bridge-83    0        10     none       1    admit-all
   ```
*  **Winbox GUI:** Go to `Bridge` -> `Ports`, select the port(s) on your `bridge-83` interface. Open the properties and change the `Authentication` to `mac-radius`.
   
| Parameter         | Description                                                                      | Example Value    |
|-------------------|----------------------------------------------------------------------------------|------------------|
| `authentication` |  The authentication method for the bridge port.  mac-radius uses the mac as username and password and contacts the radius server to validate it.| `mac-radius`     |
| `interface`       | The interface on which mac-radius auth will be enabled.      |   `ether1`           |
* **Effect:**
  - Enables MAC-based RADIUS authentication on the bridge port `ether1`.
  - Clients connecting to this bridge port will now require authentication against the RADIUS server before gaining network access.

### Step 3: Optional: Configure RADIUS Fallback

* **Goal:** If RADIUS is unreachable, allow access based on a local allow-list. This is optional but enhances reliability.
* **Why:** Provides a fallback mechanism to ensure network access if the RADIUS server is unavailable.
* **CLI Instructions:**

    ```
    /interface bridge port set [find interface=ether1] auth-mac-list=yes
    ```
* **Winbox GUI:**  Go to `Bridge` -> `Ports`, select the port(s) on your `bridge-83` interface. Open the properties, in the `MAC` tab, enable `Auth MAC List` and add the mac addresses in the `Allowed MAC Addresses` list.
*   **Effect:** If RADIUS is unavailable, access will be granted only to clients whose MAC address is listed in the `Allowed MAC Addresses` list on the bridge port configuration.

    | Parameter      | Description                                                                                                   | Example Value       |
    |-----------------|---------------------------------------------------------------------------------------------------------------|---------------------|
    | `auth-mac-list`      | Enables the allowed MAC address list when the RADIUS server is unavailable.                               | `yes`              |

### Step 4: Troubleshooting RADIUS configuration

If you are encountering issues in reaching your radius server, a good starting point is using the `tool sniffer` to find out the packets being transmitted to the server. For example:
   ```
    /tool sniffer quick ip-address=192.168.1.100
   ```
   This command will output packets sent and received on the specified ip address. This information should help in determining if the connection is being established.

## Complete Configuration Commands:

```
# Add RADIUS Server
/radius add address=192.168.1.100 secret=testing123 timeout=3 accounting=yes service=login,ppp,wireless,hotspot,dhcp usage=authentication

# Enable mac-radius on bridge port
/interface bridge port set [find interface=ether1] authentication=mac-radius

# Optional: Enable RADIUS fallback
/interface bridge port set [find interface=ether1] auth-mac-list=yes
```
## Common Pitfalls and Solutions:

*   **RADIUS Secret Mismatch:**
    *   **Problem:** The secret configured on the MikroTik does not match the secret on the RADIUS server.
    *   **Solution:** Double-check and ensure the `secret` values match exactly on both the MikroTik and RADIUS server.
*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot reach the RADIUS server due to network issues (firewall, routing).
    *   **Solution:** Verify network connectivity using `ping` or `traceroute`. Check firewall rules on the MikroTik and in the path to the RADIUS server.
*   **Incorrect Service Type:**
    *   **Problem:** The RADIUS server isn't configured to handle the specified services (e.g., "login").
    *   **Solution:** Ensure the RADIUS server is configured for the correct services specified in MikroTik RADIUS configuration, such as login,ppp, wireless, hotspot, and dhcp.
*   **Missing RADIUS Attributes:**
    *   **Problem:** The RADIUS server isn't configured to return necessary attributes for the authentication to succeed.
    *   **Solution:** Review your RADIUS server configuration and make sure it sends the necessary attributes such as Framed-IP-Address, Framed-Route, etc.
*   **MAC address format.**
    *   **Problem:** RADIUS server can't recognize the mac address.
    *   **Solution:** Some RADIUS servers are very strict on the mac address formatting, and might require a different format than the one being sent by Mikrotik. Review the formatting guidelines on your radius server.

## Verification and Testing Steps:

1.  **Connect a Client:** Connect a device to the `ether1` interface. The client should try to get an IP address.
2.  **Check the Router:**
    *   Use the `/log print` command or check the logs via Winbox (`Log` menu) to see the messages related to authentication.
    *   Use `/interface bridge port monitor ether1` to see the bridge port state and authentication status.
3.  **RADIUS Server Logs:** Check the RADIUS server's logs. You should see authentication attempts with corresponding accept or reject messages.
4.  **Sniffer tool.** As explained previously, use the `tool sniffer` command to examine the communication between the router and the radius server.
5.  **Winbox Monitor:** The Winbox `Bridge` -> `Ports` menu has an authentication column showing the status for each port that is using mac-radius authentication.

## Related Features and Considerations:

*   **RADIUS Accounting:** Enable RADIUS accounting if you need detailed logging of user sessions.
*   **Hotspot:** This setup can easily be integrated with MikroTik's Hotspot feature for advanced control of user sessions.
*   **VLANs:** If you are using VLANs, ensure that the bridge and RADIUS configuration account for VLAN tagging.
*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy.
*   **Dynamic VLAN:** You can configure radius to assign vlans dynamically to clients by sending the `Tunnel-Private-Group-Id` radius attribute.

## MikroTik REST API Examples:

Here are some REST API examples for managing RADIUS configurations.

**Note:** These API calls are specific to MikroTik and might not be available on all devices or ROS versions.

**1. Add a RADIUS Server:**

*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **Example Request Payload:**
    ```json
    {
      "address": "192.168.1.100",
      "secret": "testing123",
      "timeout": 3,
      "accounting": true,
      "service": "login,ppp,wireless,hotspot,dhcp",
      "usage": "authentication"
     }
    ```
*   **Expected Response (201 Created):**
    ```json
    {
     "id": "*0",
        "address": "192.168.1.100",
        "secret": "testing123",
        "timeout": 3,
        "accounting": true,
        "service": "login,ppp,wireless,hotspot,dhcp",
        "usage": "authentication"
    }
    ```
*   **Error Handling Example (400 Bad Request):**
    If the request has invalid data, like a missing address field, the API will respond with a 400 status code and error message.

**2. Set Bridge Port Authentication:**

*   **Endpoint:** `/interface/bridge/port`
*   **Method:** `PUT`
*   **Example Request Payload:**
    ```json
      {
        ".id": "*0",
        "authentication": "mac-radius"
      }
    ```
*   **Expected Response (200 OK):**
    ```json
    {
        "id": "*0",
        "interface": "ether1",
        "bridge": "bridge-83",
        "priority": 0,
        "path-cost": 10,
        "horizon": "none",
        "pvid": 1,
        "frame-types": "admit-all",
        "authentication": "mac-radius"
    }
    ```
*   **Error Handling Example (404 Not Found):**
     If the specified port does not exist, the API will respond with a 404 status code and error message.

## Security Best Practices:

*   **Secure RADIUS Secret:** The RADIUS secret must be kept secure. Never use a simple or default password.
*   **Network Segmentation:** Isolate the RADIUS server from direct external access using firewall rules.
*   **Strong Passwords:** If using usernames and passwords, enforce strong password policies.
*   **Regular Updates:** Keep both your MikroTik and RADIUS server software updated with the latest patches.

## Self Critique and Improvements:

This configuration is a good start for a basic RADIUS implementation. Some areas for improvement include:

*   **Dynamic VLAN Assignment:** Implement dynamic VLAN assignment based on RADIUS attributes for better network segmentation.
*   **Advanced Accounting:** Utilize RADIUS accounting features to monitor and log user activity.
*   **Redundancy:** Implement multiple RADIUS servers for high availability.
*   **Logging.** While logs can be checked with the commands described, a syslog server can provide more flexibility to the logs storage and analysis.
*   **Pre-authentication rules.** Implement pre-authentication rules to allow certain devices to bypass RADIUS, which could be required to boot up some devices, or to send specific packets.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):**

*   RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users attempting to access a network or other resources.
*   It works on a client-server model:
    *   **Client (NAS):** In our case, the MikroTik router acts as a RADIUS client, requesting authentication from the server.
    *   **Server:** The RADIUS server stores user credentials and policy information and authenticates the user.
*   When a user attempts to access a network, the following occurs:
    1.  The access point requests authentication from the radius server.
    2.  The radius server checks if the user is authorized to gain access to the network, using the username and password provided.
    3.  If it is, the user is granted access. If not, the user is rejected.
*   RADIUS simplifies network management by providing a single point for user management.
*   It enhances security by centralizing authentication controls and not depending on locally stored credentials on each network device.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Simpler to set up and manage for small networks. Less scalable, no central management, potential for inconsistencies between devices.
    *   **RADIUS:** More complex to set up but is highly scalable, offers centralized management, provides detailed logging, enhances security.
*   **MAC vs. Username/Password:**
    *   **MAC-based:** Simple to implement since the MAC address can be used as username and password in many RADIUS servers. Less secure than user/password combinations.
    *   **Username/Password:** More secure. Provides more control over who can access the network. However, users need to be managed in the radius server.
*   **Fallback Mechanism:**
    *   **No fallback:** If RADIUS is down, all users will be blocked. Increased security, but potential for downtime.
    *   **Fallback:** Provides continued access even if RADIUS is down. Reduced security, but increased availability.
*   **Authentication method:**
    *   **mac-radius** Simpler to implement and manage. Can be vulnerable to mac address spoofing.
    *   **802.1x** More robust authentication method which allows for different EAP protocols for security and is not vulnerable to mac address spoofing.

## Configuration for Specific RouterOS Versions:

This configuration is tailored for RouterOS 7.12. Some specific commands, or parameters might differ slightly for older versions. However, the core logic remains the same for versions 6.48 and 7.x. Check your specific version documentation to verify that the commands are available and the parameters available and that their behavior are the same.

Let me know if you need any further assistance or clarification.
