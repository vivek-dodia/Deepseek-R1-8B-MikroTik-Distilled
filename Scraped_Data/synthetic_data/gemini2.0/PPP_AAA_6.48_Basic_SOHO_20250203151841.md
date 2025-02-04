Okay, let's dive into setting up PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik RouterOS device (v6.48 and above) with a specific configuration targeting a SOHO environment.

**Scenario Description:**

We'll configure a MikroTik router to act as a PPP server, authenticating users connecting to a specific interface (wlan-44) via PPP using RADIUS. This is a common scenario for providing secure access over wireless or wired connections where users need to log in with usernames and passwords. We'll assume the RADIUS server is already set up and reachable by the MikroTik.

**Implementation Steps:**

Here's a step-by-step guide to implementing PPP AAA using RADIUS authentication on your MikroTik router.

**Step 1: Configure the RADIUS Server**

*   **Purpose:** Add the RADIUS server details to your router. This will be where the authentication request will be sent.
*   **CLI Instructions:**

    ```mikrotik
    /radius add address=192.168.88.10 secret="your_radius_secret" timeout=3
    ```
    * `address`: IP address of your RADIUS server (replace with your actual server IP).
    * `secret`:  Shared secret key configured on both the RADIUS server and MikroTik router. **This is crucial for security. Use a long, complex secret. If this secret does not match your radius server, authentication will fail.**
    * `timeout`:  Timeout value in seconds.

    **Winbox GUI:** Go to RADIUS menu, click +, and fill in the `Address`, `Secret` and `Timeout` fields.
*   **After:**
    * The RADIUS server is now configured on the MikroTik.
    *  If your radius server was not configured properly, you will likely receive a "Timeout" error when a connection is initiated.
*   **Effect:** The router knows where to send authentication requests.

**Step 2: Create a PPP Profile**

*   **Purpose:** Defines the settings for PPP connections, including local address and DNS servers.
*   **CLI Instructions:**

    ```mikrotik
    /ppp profile add name=radius-profile use-encryption=yes local-address=250.198.167.254 remote-address=250.198.167.0/24 dns-server=8.8.8.8,8.8.4.4
    ```

    *   `name`: The name of the profile.
    *   `use-encryption`: Enabling encryption is highly recommended for PPP connections.
    *   `local-address`:  The IP address assigned to the PPP server endpoint on the router itself.
    *   `remote-address`:  The IP range for the connected PPP client.
    *   `dns-server`: The DNS servers the clients will use.

    **Winbox GUI:** Go to PPP -> Profiles, click +, and fill in the fields.
*   **After:**
    * A new PPP profile is created.
*   **Effect:** This profile will be applied to new PPP connections and control IP address and DNS settings.

**Step 3:  Configure the PPP Server Interface**

*   **Purpose:** Activate the PPP server on the specified interface.
*   **CLI Instructions:**

    ```mikrotik
    /interface ppp-server server add name=pppoe-radius interface=wlan-44 profile=radius-profile service-name=ppp-radius disabled=no
    ```

    *   `name`: The name of the PPP server instance.
    *   `interface`:  The interface where the PPP server will listen for connections.
    *   `profile`:  The PPP profile created in the previous step.
    *   `service-name`: Optional name for the server.
    *   `disabled`: Set to `no` to enable the server.

    **Winbox GUI:** Go to PPP -> PPP Server, click +, select the interface (wlan-44), select the profile `radius-profile`, and ensure `disabled` is unchecked.
*   **After:**
    * The PPP server is active on `wlan-44`, using profile radius-profile.
*   **Effect:** The router will accept PPP requests on the given interface and will pass the credentials on to the RADIUS server.

**Step 4: Enable RADIUS Authentication for PPP**

*   **Purpose:** Tell PPP to use RADIUS for authentication and accounting.
*   **CLI Instructions:**

    ```mikrotik
     /ppp aaa set use-radius=yes accounting=yes
     ```
    *   `use-radius`: Enables RADIUS authentication.
    *   `accounting`: Enables RADIUS accounting (optional, but recommended).

     **Winbox GUI:** Go to PPP -> AAA, and check `Use Radius` and `Accounting`.
*   **After:**
    * All new PPP authentications are handled by the radius server.
*   **Effect:** The authentication will be routed to the configured radius server.

**Complete Configuration Commands:**

```mikrotik
/radius add address=192.168.88.10 secret="your_radius_secret" timeout=3
/ppp profile add name=radius-profile use-encryption=yes local-address=250.198.167.254 remote-address=250.198.167.0/24 dns-server=8.8.8.8,8.8.4.4
/interface ppp-server server add name=pppoe-radius interface=wlan-44 profile=radius-profile service-name=ppp-radius disabled=no
/ppp aaa set use-radius=yes accounting=yes
```

**Common Pitfalls and Solutions:**

*   **Incorrect RADIUS Secret:**  If the secret doesn't match the RADIUS server, authentication will fail.
    *   **Solution:** Double-check both MikroTik and RADIUS server configurations. Use a complex secret and store it securely.
*   **RADIUS Server Unreachable:** Ensure the MikroTik can reach the RADIUS server.
    *   **Solution:** Check network connectivity with `ping 192.168.88.10` in the terminal. Also verify firewall rules.
*  **Wrong Profile:** If you select the wrong profile on the PPP interface, connectivity and configuration will not function properly.
    *   **Solution:** Verify that you are using the correct profile.
*   **No RADIUS User:** Make sure you have correctly added the PPP users to the RADIUS server
    *   **Solution:** verify your radius server logs.
*   **Encryption Issues:** If `use-encryption` is enabled, make sure client supports it.
    *   **Solution:** Check the client's PPP configuration. You can disable encryption on the profile and server for testing if there are encryption conflicts.
*   **Resource Issues:** Large numbers of concurrent PPP users can cause high CPU usage.
    *   **Solution:** Monitor router resource usage, potentially upgrade the hardware. Also, use queue settings to rate limit each PPP connection.

**Verification and Testing Steps:**

1.  **Connect a PPP client:** Use a computer to connect to the `wlan-44` interface via PPP. This might involve setting up a virtual adapter on your system. Ensure you are using the user created on your RADIUS server.
2.  **Monitor the PPP Logs:** Use the command ` /log print follow-only where topics~"ppp"` to see if the PPP connection succeeds or fails.
3.  **Use Torch:** Use `/tool torch interface=wlan-44` to monitor traffic. If the client connects, you will see traffic in torch.
4.  **Ping:** Attempt to ping the `local-address` (250.198.167.254) and the `dns-server` from the PPP client. If this works, your connectivity is working properly.
5.  **Check Radius Logs:** If the authentication fails, check the logs on the RADIUS server for any errors.
6.  **Verify IP Address:** Ensure the client has received an IP from the `remote-address` range.

**Related Features and Considerations:**

*   **Accounting:** Enabling RADIUS accounting allows you to track PPP connection usage (start/stop times, data transferred).
*   **Multiple RADIUS Servers:** You can configure backup RADIUS servers for redundancy.
*   **User Profiles:** RADIUS can define per-user policies, such as bandwidth limits or VLAN assignments using attributes returned from the RADIUS server. This is done by using Mikrotik attributes.
*   **Hotspot Functionality:** PPP AAA can be combined with MikroTik's Hotspot feature for more advanced guest network controls.

**MikroTik REST API Examples (if applicable):**

The MikroTik REST API can be used to configure the above features. Below are some examples to help understand how to perform the above configurations using a REST API.

* **Add Radius Server**
```bash
curl -k -u admin:yourpassword -H "Content-Type: application/json" -X POST \
-d '{"address": "192.168.88.10", "secret": "your_radius_secret", "timeout": 3}' \
https://your_router_ip/rest/radius
```

* **Response (Successful)**

```json
{
    "id": "*1"
}
```

* **Error (already exists)**
```json
{
    "error": "already have such item",
    "message": "already have such item"
}
```

* **Get Radius Server:**
```bash
curl -k -u admin:yourpassword https://your_router_ip/rest/radius
```

* **Response:**

```json
[
   {
      "id":"*1",
      "address":"192.168.88.10",
      "secret":"your_radius_secret",
      "timeout":"3",
      "authentication-port":"1812",
      "accounting-port":"1813",
      "src-address":"",
      "disabled":"false"
   }
]
```

* **Set PPP AAA use Radius**

```bash
curl -k -u admin:yourpassword -H "Content-Type: application/json" -X PUT \
-d '{"use-radius": "yes", "accounting":"yes"}' \
https://your_router_ip/rest/ppp/aaa
```

*   **Response (Successful):**

```json
{
    "message": "updated"
}
```
* **Error:**
```json
{
    "error":"invalid command",
    "message":"invalid command"
}
```
**Note:** The rest API in MikroTik can return both a successful response, or an error.

**Security Best Practices:**

*   **Secure Shared Secret:** The RADIUS secret is critical. Use a long, complex, and unique secret. Securely store it, and do not include it in your code, unless it is securely encrypted using best encryption practices.
*   **Firewall Rules:** Limit access to the router and the RADIUS server to only authorized IPs.
*   **Encryption:** Always use PPP encryption to protect user data transmitted over the network.
*   **Regular Updates:** Keep RouterOS and any related services updated with the latest patches.

**Self Critique and Improvements:**

*   **More Robust Error Handling:**  More detailed error logging and debugging tools could be implemented.
*   **Dynamic Configuration:**  Consider dynamic PPP client configuration using RADIUS attributes to improve flexibility.
*   **Rate Limiting:** Implement queue trees to limit user bandwidth.
*   **Configuration Backup:** Automate regular backups of the configuration in case of failure.
*   **Testing Automation:** Implement scripts for automated connection testing.
*   **Logging:** Create a dedicated log file for all RADIUS events to help in troubleshooting.
*   **VLAN Assignment:** Using Mikrotik Attributes, you can assign VLAN numbers based on radius authentication. This could be useful in a more complex environment.
*   **Port Forwarding:** If the client is behind a firewall, port forwarding must be used to ensure that all traffic goes to the RADIUS server

**Detailed Explanations of Topic:**

*   **PPP (Point-to-Point Protocol):** A data link layer communication protocol used to establish a direct connection between two nodes. Common uses include Dial-up, DSL, and VPN connections. PPP is commonly used in scenarios where a persistent connection is needed.
*   **AAA (Authentication, Authorization, Accounting):** A security framework.
    *   **Authentication:** Verifies user identity using a username and password.
    *   **Authorization:** Grants permissions after the user is authenticated. This can be used to set up access permissions or different rates.
    *   **Accounting:** Tracks resource usage for billing or auditing purposes. This can be used to track the length of the session, or the amount of data used.
*   **RADIUS (Remote Authentication Dial-In User Service):** A protocol to centralize AAA for networks. It uses a client-server architecture, where RADIUS clients send authentication requests to the RADIUS server.
*   **Radius Attributes:** Additional information can be passed from the RADIUS server to the PPP client using RADIUS attributes. These can be used to implement settings on the fly. Examples include Mikrotik specific attributes such as `Mikrotik-Rate-Limit` or `Mikrotik-Vlan-Id`.
*  **Mikrotik Specific Settings:** Mikrotik allows for further configuration through vendor specific attributes.  Specifically, the prefix `Mikrotik-` is used to specify vendor specific settings.

**Detailed Explanation of Trade-offs:**

*   **Local Authentication vs. RADIUS:**
    *   Local authentication is simpler to configure for smaller setups, but RADIUS offers centralized user management and enhanced security and allows for a more dynamic setup.
    *   Local authentication requires you to create and manage all users locally on the Mikrotik Router. RADIUS authentication centralizes the user information to an external server. This is more desirable for larger or more complex networks.
*   **PAP/CHAP/MSCHAP/MSCHAPv2:** These are different authentication protocols within PPP.
    *   **PAP (Password Authentication Protocol):** Transmits passwords in clear text; **do not use this**.
    *   **CHAP (Challenge Handshake Authentication Protocol):** More secure than PAP, but still vulnerable to man-in-the-middle attacks.
    *   **MSCHAP/MSCHAPv2:** Microsoft's version of CHAP, offering better security and more compatibility. The default encryption of MSCHAPv2 should be considered acceptable for most use cases. However, some security experts recommend avoiding it.
*   **Encryption vs. No Encryption:**
    *   Encryption protects user data during transmission, crucial for wireless or untrusted connections.
    *   No encryption reduces overhead, but poses a significant security risk. Always use encryption if you can.
*   **Accounting:**
    *   Accounting provides valuable data for billing or auditing purposes, but uses more resources. It is often desired to enable accounting, however not in all cases.
*   **Complexity:** A more complex setup adds flexibility, but is more difficult to configure.

**Configuration for Specific RouterOS Versions:**

This configuration is applicable to RouterOS 6.48 and later, including versions in the 7.x series. The commands are consistent across these versions. However, always refer to the official MikroTik RouterOS documentation for version-specific notes.

**Note:** You can modify the example to suit your needs.  This configuration is a starting point for a more robust and complex network. Remember to adapt it to your specific environment.
