Okay, let's dive into configuring RADIUS authentication on a MikroTik RouterOS device within a SOHO environment, specifically focusing on RouterOS 7.11 (though much of this will also work for 6.48 and other 7.x versions). We'll use the provided subnet and interface name for demonstration.

## Scenario Description:

We will configure a MikroTik router to use a RADIUS server for authenticating clients connecting to the network via a bridged interface. This is a common setup for enhanced security and user management, allowing centralized control over network access. Clients connecting to the `bridge-52` interface will need to authenticate via the RADIUS server before gaining network access.

## Implementation Steps:

Here’s a step-by-step guide to implement RADIUS authentication on your MikroTik router:

**1. Step 1: Verify Network Interface and IP Address Configuration**

*   **Explanation:** Before configuring RADIUS, ensure your interface (`bridge-52`) and IP configuration are correct. If you are connecting via a wireless access point, the bridge would be where the wireless interface was connected to, so that the radius request is generated on this bridge.
*   **Before Configuration (Example):**
    ```
    /interface bridge print
    /ip address print
    ```
    **Output:**
    ```
    # /interface bridge print
    Flags: X - disabled, R - running
    0   R name="bridge-52" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled
        auto-mac=02:8E:84:5C:9E:50 admin-mac=02:8E:84:5C:9E:50
    
    # /ip address print
    Flags: X - disabled, I - invalid, D - dynamic
    0   address=192.168.88.1/24 interface=ether1 network=192.168.88.0
    1   address=10.10.10.1/24 interface=bridge-52 network=10.10.10.0 
    ```
*   **Action:** Ensure the bridge exists and has a suitable IP address for your needs. For this setup, we will assume you have an address for the bridge, but the clients connecting to it may be getting a DHCP address from the DHCP server of your choice, or statically configuring the clients with the ip of the bridge set as the gateway. If you do not have an IP for your bridge, set it with:
    ```
    /ip address add address=209.210.129.1/24 interface=bridge-52
    ```
*   **After Configuration:**
    ```
    /ip address print
    ```
    **Output:**
    ```
    Flags: X - disabled, I - invalid, D - dynamic
    0   address=192.168.88.1/24 interface=ether1 network=192.168.88.0
    1   address=209.210.129.1/24 interface=bridge-52 network=209.210.129.0
    ```
    **Winbox GUI:**
        *   Go to `IP > Addresses` to view current addresses.
        *   Click `+` to add a new IP. Select bridge-52 in the `Interface` dropdown and specify `Address` as `209.210.129.1/24`.

**2. Step 2: Configure RADIUS Client Settings**

*   **Explanation:** Add the details for your RADIUS server. The client will send authentication requests to this server.
*   **Before Configuration:** There will be no RADIUS settings in the router's configuration.
    ```
    /radius print
    ```
    **Output:**
    ```
    # /radius print
    #
    ```
*   **Action:** Add a RADIUS server using the following commands. Replace the IP, shared-secret, accounting port and authentication port with your values.
    ```
    /radius add address=192.168.10.100 secret="your_radius_secret" accounting-port=1813 timeout=30 authentication-port=1812
    ```
*   **After Configuration:** The newly created RADIUS server will be visible.
    ```
    /radius print
    ```
    **Output:**
    ```
    Flags: X - disabled, I - invalid
    0  address=192.168.10.100 authentication-port=1812 accounting-port=1813
       timeout=30 secret="your_radius_secret" called-id=""
       framed-mtu=1500 comment=""
    ```
    **Winbox GUI:**
        *   Go to `RADIUS` in the left menu.
        *   Click `+` to add a new RADIUS server.
        *   Fill in the required fields such as `Address`, `Secret`, `Authentication Port`, and `Accounting Port`.

**3. Step 3:  Enable RADIUS Authentication on the Bridge**

*   **Explanation:** This step enables the use of the created RADIUS server for authentication on the `bridge-52` interface.
*   **Before Configuration:** RADIUS is not associated to the bridge.
    ```
    /interface bridge settings print
    ```
    **Output:**
    ```
    Flags: X - disabled, I - invalid
       use-ip-firewall=no use-ip-firewall-for-vlan=no use-mac-firewall=no
    ```
*   **Action:** Set the `use-radius=yes` option to enable the radius authentication.
   ```
    /interface bridge settings set use-radius=yes
    ```
*   **After Configuration:** The setting has been enabled.
    ```
    /interface bridge settings print
    ```
    **Output:**
    ```
    Flags: X - disabled, I - invalid
    use-radius=yes use-ip-firewall=no use-ip-firewall-for-vlan=no
    use-mac-firewall=no
    ```
     **Winbox GUI:**
        *   Go to `Bridge` and then the `Settings` tab.
        *   Enable the `Use RADIUS` checkbox.

**4. Step 4: (Optional) Implement a RADIUS Fallback System for Testing**
   *   **Explanation:** If RADIUS authentication fails, devices cannot connect to your network. It is good practice to have some form of access in case RADIUS is unavailable. This can be as simple as a firewall rule that allows all traffic, or a second less secure authentication method like `mac-authentication`.
   *   **Before Configuration:** No fallback rules are set.
   *   **Action:** Set up mac-authentication as a fallback:
    ```
     /interface bridge port set [find bridge="bridge-52"] authentication-type=mac-authentication
     /interface bridge port set [find bridge="bridge-52"] mac-authentication=yes
    ```
   *   **After Configuration:** Mac-authentication is enabled as a fallback.
        ```
      /interface bridge port print where bridge="bridge-52"
        ```
   **Output:**
    ```
    Flags: X - disabled, R - running
    0   R bridge="bridge-52" interface=ether2 priority=0x80
          path-cost=10 authentication-type=mac-authentication
          mac-authentication=yes
    1   R bridge="bridge-52" interface=wlan1 priority=0x80
          path-cost=10 authentication-type=mac-authentication
          mac-authentication=yes
    ```
**Winbox GUI:**
*   Go to `Bridge` > `Ports`.
*   Select the port(s) connected to the desired network (`ether2` and `wlan1` in our example).
*   Set `Authentication Type` to `mac-authentication` and enable `mac-authentication`.

**5. Step 5: Testing RADIUS Authentication**

*   **Explanation:** Connect a client to bridge-52.  If you are connecting via a wireless network, connect to the configured SSID. The client will be blocked until RADIUS authenticates.
*  **Action:** Use `torch` to monitor the traffic to the RADIUS server. If the auth attempt is successful you will see the client get a DHCP address and start communicating.
   ```
    /tool torch interface=bridge-52 duration=60
   ```
* **Winbox GUI:**
    *  Go to `Tools` > `Torch`.
    *  Select `bridge-52` as the interface, check `Display` and `Start`.

## Complete Configuration Commands:

```
# Add a bridge interface. Skip if bridge exists
/interface bridge add name="bridge-52"
# Add IP to the bridge interface.
/ip address add address=209.210.129.1/24 interface=bridge-52
# Add RADIUS server details. Adjust to your server's configuration.
/radius add address=192.168.10.100 secret="your_radius_secret" accounting-port=1813 timeout=30 authentication-port=1812
# Enable RADIUS on bridge
/interface bridge settings set use-radius=yes
#Set mac-authentication as a fallback
/interface bridge port set [find bridge="bridge-52"] authentication-type=mac-authentication
/interface bridge port set [find bridge="bridge-52"] mac-authentication=yes

```

## Common Pitfalls and Solutions:

*   **Problem:** RADIUS server unreachable.
    *   **Solution:** Verify IP, port, and shared secret are correct. Check firewall rules on the MikroTik and RADIUS server. Ensure a route exists between the client and the radius server. Use torch on the interface the client is connected to to check traffic to the radius server.
*   **Problem:** Authentication failures.
    *   **Solution:** Check RADIUS server logs for detailed error messages. Verify the username/password combination. Check `bridge port print` for current status of devices on the bridge.
*   **Problem:** Client can connect but does not get an IP address.
    *   **Solution:** This can indicate that the RADIUS server is not configured to return DHCP address information. A simple test for this is to set a static IP address and try to connect. If the client can connect, the problem is in DHCP.
*   **Problem:** High CPU/Memory Usage.
    *   **Solution:** RADIUS is not generally resource intensive, however,  monitor the router's resource usage (`/system resource print`). If issues are present, consider optimizing RADIUS server configuration. If this problem persists, consider upgrading hardware.

## Verification and Testing Steps:

1.  **RADIUS Server Reachability:** Ping the RADIUS server from the MikroTik router using `/ping <RADIUS_server_IP>`.
2.  **Torch Tool:** Use `torch` to monitor the `bridge-52` interface for RADIUS traffic.
    ```
        /tool torch interface=bridge-52 duration=60
    ```
3.  **RADIUS Server Logs:** Check your RADIUS server logs for authentication attempts, successful and unsuccessful. Common log files:
        *   ` /var/log/freeradius/radius.log` (FreeRADIUS)
4.  **Bridge Port Status:** On the client-connected interface on the router, check the bridge port authentication using
     ```
     /interface bridge port print where bridge="bridge-52"
     ```
     **Output:**
    ```
     Flags: X - disabled, R - running
     0   R bridge="bridge-52" interface=ether2 priority=0x80
           path-cost=10 authentication-type=mac-authentication
           mac-authentication=yes authentication-status=authenticated
    1   R bridge="bridge-52" interface=wlan1 priority=0x80
           path-cost=10 authentication-type=mac-authentication
           mac-authentication=yes authentication-status=authenticated
    ```
     Note: This will show the current authentication status for each port. For successful Radius authentication, the `authentication-status` will be `authenticated` and the `authentication-type` will change to `radius`.
5.  **Client Connectivity:** Connect a client device to the `bridge-52` interface and verify the client is able to get an IP address and can access the network after successful RADIUS authentication.

## Related Features and Considerations:

*   **Hotspot:** RADIUS can be used as the authentication method for MikroTik Hotspot.
*   **Wireless:** For WPA-Enterprise (802.1x), RADIUS is mandatory.
*   **Accounting:** Implement RADIUS accounting to track user session details.
*   **User Manager:** The MikroTik User Manager can be integrated with RADIUS for user management.
*   **VLANs:** RADIUS can assign VLANs dynamically based on user authentication.

## MikroTik REST API Examples:

```
# Example: Add RADIUS Server (POST)
# API Endpoint: /radius
# Method: POST
# JSON Payload:
{
    "address": "192.168.10.100",
    "secret": "your_radius_secret",
    "accounting-port": 1813,
    "timeout": 30,
    "authentication-port": 1812
}
# Expected Response (201 Created):
{
    "id": "*1",
    "address": "192.168.10.100",
    "secret": "your_radius_secret",
    "accounting-port": 1813,
    "timeout": 30,
    "authentication-port": 1812,
    "called-id": "",
    "framed-mtu": 1500,
    "comment": ""
}

# Example: Enable RADIUS on Bridge (PATCH)
# API Endpoint: /interface/bridge/settings
# Method: PATCH
# JSON Payload:
{
    "use-radius": true
}
# Expected Response (200 OK):
{
    "use-radius": true,
    "use-ip-firewall": false,
    "use-ip-firewall-for-vlan": false,
    "use-mac-firewall": false
}
# Example: Get Bridge Port Information
# API Endpoint: /interface/bridge/port
# Method: GET
# Expected Response (200 OK):
# [
# {
# "bridge": "bridge-52",
# "interface": "ether2",
# "priority": 128,
# "path-cost": 10,
# "authentication-type": "mac-authentication",
# "mac-authentication": true,
# "authentication-status": "authenticated"
#   }
# ]
```
*   **Error Handling:** If an error occurs, the API will return a response with an error status code (e.g., 400 Bad Request, 404 Not Found, 500 Internal Server Error) and a JSON payload providing details about the error. Your code should handle these errors gracefully by parsing the JSON payload for relevant error messages. For example:

    ```json
    {
        "message": "invalid input",
        "details": [
            { "param": "secret", "message": "invalid value" }
        ]
    }
    ```

## Security Best Practices

*   **Shared Secret:** Use a strong, randomly generated shared secret for RADIUS.
*   **Secure RADIUS server:** Ensure the RADIUS server is properly secured.
*   **Network Segmentation:** Consider placing RADIUS servers in a separate, secure network segment.
*   **Access Control Lists:** Use firewall rules to restrict access to the RADIUS server.

## Self Critique and Improvements:

*   **Improvement:** The current configuration lacks detailed accounting and logging settings. A full setup would require more advanced RADIUS settings for this.
*   **Improvement:** There is no explicit firewall configuration to filter traffic coming from non-radius authenticated devices. This is important to limit attack surfaces when RADIUS is unavailable.
*   **Improvement:** Implement dynamic VLAN assignments through RADIUS for better traffic segregation.
*   **Improvement:** Add rate limits to devices authenticated through RADIUS, to ensure no single device consumes all available bandwidth.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**
*   RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users attempting to connect to a network.
*   It uses a client-server model where the network access device (MikroTik router in this case) acts as the client, and a RADIUS server manages authentication.
*   RADIUS is commonly used for VPNs, wireless networks, and dial-up connections.
*   *Authentication* verifies the user’s identity.
*   *Authorization* determines what network resources the user is allowed to access.
*   *Accounting* tracks the user’s network usage (session time, data usage).

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:**
    *   *Local*: Simpler to configure but lacks centralized management, making it unsuitable for networks that require user management.
    *   *RADIUS*: More complex but provides centralized user management, better security, and logging capabilities.
*   **Open vs. RADIUS Authentication on Wireless Networks:**
    *   *Open*: Easier to set up but insecure. Anyone can connect.
    *   *RADIUS*: More secure due to credentials required to authenticate.
*   **Mac-Authentication Fallback:**
    *   *Enabled*: Convenient in case RADIUS is not available but less secure.
    *   *Disabled*: More secure but less resilient.

## Configuration for Specific RouterOS Versions:

*  The commands and settings provided in this document are designed for RouterOS 7.11 (and compatible with 6.48, 7.x)
*  In versions prior to 6.48, some features and commands may differ slightly, specifically, the bridge interface settings. Always refer to the RouterOS documentation for the specific version you are using.

Let me know if you'd like to explore any of these aspects in more detail!
