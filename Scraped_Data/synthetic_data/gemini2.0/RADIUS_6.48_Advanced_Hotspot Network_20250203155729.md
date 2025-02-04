Okay, let's craft some detailed documentation for integrating RADIUS authentication into a MikroTik Hotspot network using RouterOS 6.48, with an emphasis on practical implementation, troubleshooting, and security.

## Scenario Description:

This document details the setup of a MikroTik router as a Hotspot gateway, using RADIUS for user authentication and authorization.  We will configure the router to use a remote RADIUS server for verifying user credentials before granting network access. The target network is a SOHO Hotspot environment, with a bridge interface "bridge-12" that connects to our user-facing network.

## Implementation Steps:

### Step 1: Initial Router Configuration

**Before:** Assuming a basic MikroTik setup, the router likely has an IP address and basic firewall rules. We are specifically focusing on the Hotspot functionality.

**Action:** No specific configuration changes are needed in this initial step for RADIUS setup. Ensure basic networking and connectivity. We assume bridge-12 exists already and is set up.

**Explanation:** This step sets the stage by confirming the existence of our target interface, `bridge-12`, and we begin from a working router.

**CLI Output (Example, before step 2):**

```
/interface bridge print
Flags: X - disabled, R - running
 0  R name="bridge-12" mtu=1500 actual-mtu=1500 l2mtu=65535 arp=enabled
      arp-timeout=auto mac-address=XX:XX:XX:XX:XX:XX protocol-mode=rstp
      priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6
      
/ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24     192.168.88.0    ether1 
 
/ip route print
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable
    #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
    0  ADC  192.168.88.0/24   192.168.88.1    ether1                     0
```

### Step 2: Configure the RADIUS Server

**Before:** No RADIUS configuration is present on the router.

**Action:** Add the RADIUS server details to the router’s configuration.

**Explanation:** This is essential to point the router to the correct server for user authentication and accounting.

**CLI Command:**
```
/radius add address=192.168.1.100 secret="your_radius_secret" service=hotspot timeout=3
```
**CLI/Winbox GUI:**
*Navigate to:* `RADIUS` under the `PPP` section.
*Click* on the `+` button and provide details.
*`Address`:* `192.168.1.100`
*`Secret`:*  `your_radius_secret`
*`Service:`* `hotspot`
*`Timeout:`* `3`
*Click* `OK`.

**After:** A RADIUS server entry is configured in RouterOS.

**CLI Output (After):**

```
/radius print
Flags: X - disabled, I - invalid
 #   ADDRESS         SECRET      SERVICE  TIMEOUT  AUTHENTICATE  ACCOUNTING  INTERIM-UPDATE
 0   192.168.1.100   your_radius_secret hotspot 3s            yes         yes              no
```

**Parameter Explanation:**

| Parameter | Description |
|---|---|
| `address` | IP address of the RADIUS server. |
| `secret` | Shared secret for RADIUS communication. |
| `service` |  RADIUS service this server will be used for (hotspot, ppp, etc.). |
| `timeout` | How long to wait for a RADIUS response in seconds. |
| `authenticate` | Flag for Authentication requests (`yes`). |
| `accounting` | Flag for Accounting requests (`yes`). |
| `interim-update` |  Flag for Interim Update requests (`no`). |

### Step 3: Configure Hotspot Profile to Use RADIUS

**Before:** The Hotspot profile is not configured to use RADIUS authentication. We are assuming a Hotspot profile exists already with a name `hotspot1`.

**Action:** Modify the existing Hotspot profile to use the configured RADIUS server.

**Explanation:** This tells the Hotspot service to authenticate users via RADIUS.

**CLI Command:**
```
/ip hotspot profile set hotspot1 use-radius=yes
```

**CLI/Winbox GUI:**
*Navigate to:* `IP` -> `Hotspot` -> `Server Profiles` tab.
*Select* the profile name `hotspot1`.
*Check* the `Use Radius` option.
*Click* `OK`.

**After:** The Hotspot profile now uses RADIUS.

**CLI Output (After):**

```
/ip hotspot profile print
Flags: * - default
 0   name="hotspot1" dns-name="" html-directory="hotspot" keepalive-timeout=10m
       status-autorefresh=1m shared-users=unlimited use-radius=yes
       radius-accounting=yes  radius-interim-update=0s
       radius-default-domain="" accounting-backup=no
```

**Parameter Explanation:**

| Parameter | Description |
|---|---|
| `use-radius` | Enable or disable the usage of RADIUS authentication (`yes`). |
| `radius-accounting`| Use RADIUS for accounting as well (`yes`).|
| `radius-interim-update` |  Enable or disable interim updates from Radius (`0s`). |
| `radius-default-domain` | The default domain to use when authenticating (`""` - none).|
|`accounting-backup` | Use local accounting if radius is unavailable. |

### Step 4: Enable the Hotspot Server on the bridge-12 Interface.

**Before:** The Hotspot service is not running on bridge-12. We assume the hotspot server is set up already with a name `hotspot1`.
**Action:** Enable hotspot server to use the previously defined profile and use bridge-12 as the interface.

**Explanation:** This tells the Hotspot service to serve client requests over `bridge-12`

**CLI Command:**
```
/ip hotspot set hotspot1 interface=bridge-12
```
**CLI/Winbox GUI:**
*Navigate to:* `IP` -> `Hotspot` -> `Server` tab.
*Select* the server name `hotspot1`.
*Select* the `Interface` as `bridge-12`.
*Click* `OK`.

**After:** The Hotspot service is now active on `bridge-12`.

**CLI Output (After):**

```
/ip hotspot print
Flags: X - disabled, I - invalid, D - dynamic
 #   NAME      INTERFACE     PROFILE    IDLE-TIMEOUT
 0   hotspot1  bridge-12  hotspot1  5m
```

**Parameter Explanation:**

| Parameter | Description |
|---|---|
| `interface` | The interface on which to run the hotspot service (`bridge-12`).|
| `profile` |  The Profile to use to for configuration. |
| `idle-timeout` | Time of inactivity for session to be closed.|

## Complete Configuration Commands:

```
/radius add address=192.168.1.100 secret="your_radius_secret" service=hotspot timeout=3
/ip hotspot profile set hotspot1 use-radius=yes
/ip hotspot set hotspot1 interface=bridge-12
```
## Common Pitfalls and Solutions:

*   **RADIUS server unreachable:**
    *   **Problem:** The router cannot connect to the RADIUS server.
    *   **Solution:** Verify the RADIUS server IP address, shared secret, and ensure firewall rules on both the router and RADIUS server allow communication on UDP port 1812 (for authentication) and 1813 (for accounting) or any custom port setup. Use `ping` and `traceroute` to check connectivity. Use `/tool torch interface=ether1 port=1812` on Mikrotik to inspect RADIUS traffic.

*   **Incorrect shared secret:**
    *   **Problem:** The shared secret on the router does not match the RADIUS server.
    *   **Solution:** Double-check and ensure the shared secret is identical on both the router and the RADIUS server.

*   **RADIUS server not responding:**
    *   **Problem:** The RADIUS server might be overloaded or has issues.
    *   **Solution:** Monitor the RADIUS server logs for errors. Check server resources. Use another radius server for testing, or temporarily move the user database to Mikrotik Local Authentication.

*   **Hotspot Profile issues:**
    *   **Problem:** Incorrect profile settings lead to user authentication issues.
    *   **Solution:** Check the configured Hotspot profile (name, DNS server, address pool etc.). Make sure `use-radius` is set to `yes`.

*   **Firewall rules blocking RADIUS communication:**
    *   **Problem:** Router firewall is blocking the outbound RADIUS communication to the remote server.
    *   **Solution:** Create a rule in the forward chain to allow outbound connections to the RADIUS server on the specified ports (1812, 1813 or custom).

*   **Resource issues:** High CPU usage may occur with many users, impacting radius communication. Add a more capable device or offload radius authentication. Memory issues are less likely in most environments.

## Verification and Testing Steps:

1.  **Connect a Client:** Connect a client device to the Wi-Fi or network served by the Hotspot on `bridge-12`.
2.  **Hotspot Login:** The client should be redirected to the Hotspot login page.
3.  **RADIUS Authentication:** Enter RADIUS server credentials. The client should be authenticated by the RADIUS server.
4.  **Check Active Users:** In the MikroTik, check `/ip hotspot active print`. A successful authentication will be displayed with the username.
5.  **RADIUS Logs:** Monitor the RADIUS server logs for successful authentication attempts and any errors.
6.  **Mikrotik Logs:** Use `/log print topics=radius,info` to see RADIUS interaction logs, such as "RADIUS: authentication request received", "RADIUS: authentication accepted" or errors.

## Related Features and Considerations:

*   **User Manager:** MikroTik's User Manager can also be used to manage RADIUS user accounts, although it is not a full fledged RADIUS server.
*   **Accounting:** RADIUS accounting can be enabled to track user sessions, bandwidth usage, etc. Use `radius-accounting=yes` in the hotspot profile.
*   **Interim Updates:** Configure `radius-interim-update` to periodically update usage information.
*   **Dynamic DNS:** Use dynamic DNS with the hotspot, updating the client's DNS when they get an ip address.
*   **Walled Garden:** Configure walled garden to allow specific sites to be accessed before authentication.
*   **Custom Login Page:** Customize the Hotspot login page for branding purposes.
*   **Address Pool:** Implement an IP address pool for hotspot users.

## MikroTik REST API Examples:

Since this setup primarily involves configuration and not runtime data, REST API usage here is primarily for scripting and automation of the configuration.

```json
# Example: Adding a RADIUS server

{
    "url": "/radius",
    "method": "POST",
    "payload": {
        "address": "192.168.1.100",
        "secret": "your_radius_secret",
        "service": "hotspot",
		"timeout": "3s",
        "authenticate": "yes",
        "accounting": "yes"
    }
}
```

```json
# Example: Modifying the Hotspot Profile
{
    "url": "/ip/hotspot/profile",
    "method": "PUT",
    "payload": {
         "=.id": "hotspot1",
         "use-radius": "yes",
         "radius-accounting":"yes"
    }
}

```

```json
# Example: Setting the Hotspot Server Interface
{
    "url": "/ip/hotspot",
    "method": "PUT",
    "payload": {
        "=.id": "hotspot1",
        "interface": "bridge-12"
    }
}

```

**Explanation:**

*   `/radius`: The endpoint for managing RADIUS servers.
*   `/ip/hotspot/profile`: The endpoint for managing hotspot profiles.
*   `/ip/hotspot`: The endpoint for managing the hotspot servers.
*   `POST` method: Create a new resource.
*   `PUT` method: Update existing resources, using `.id` to reference the item.
*   The JSON payload includes the parameters as they would be in the CLI.

**Error Handling:**
Mikrotik API will return standard http response codes. Errors can include authentication failure (401), invalid requests (400) or not found (404). You can check the response code to confirm whether a request has been fulfilled successfully, and the body will contain further details if any errors have arisen. For example, if a hotspot name is not found, 404 status code will be returned.
## Security Best Practices

*   **Shared Secret:** Use a strong, randomly generated shared secret and change it periodically. Don't use default values.
*   **RADIUS Ports:** Restrict access to the RADIUS server ports (1812, 1813) on the network by using firewall rules. Only allow traffic from the MikroTik router IPs.
*   **HTTPS Login:** Ensure the Hotspot uses HTTPS for the login page to protect credentials. Enable certificates.
*   **Session Timeout:** Configure appropriate session timeout settings for idle and session users.
*   **Regular Updates:** Keep both the MikroTik RouterOS and the RADIUS server software updated to patch security vulnerabilities.
*   **Access Control:** Limit access to the MikroTik device itself using strong passwords and firewall rules. Disable unused services.
*  **User and Group Management:** Use RADIUS user and group parameters for finer grained control over user access.
*  **Monitoring:** Monitor the radius servers and Mikrotik for unusual patterns, or unusual access attempts.

## Self Critique and Improvements

This setup covers the basic RADIUS implementation for Hotspot on MikroTik. Here are some areas that could be improved:

*   **Dynamic Authorization:** Implementing dynamic authorization changes based on user attributes coming from RADIUS server, such as speed limiting or vlan changes. This requires custom scripts, and is more advanced.
*   **Load Balancing:** Implementing multiple RADIUS servers for redundancy and load balancing using MikroTik failover.
*   **Specific Attributes:** Using specific RADIUS attributes to control user sessions (e.g., `Framed-IP-Address`, `Session-Timeout`, vendor specific attributes).
*   **External Captive Portal:** Integrating the Hotspot with an external captive portal solution, using RADIUS for authentication.
*   **Detailed Logging:** Customizing log outputs with timestamps and details.

## Detailed Explanations of Topic

**RADIUS:** (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network.
*   **Authentication:** Verifies the identity of the user (username and password).
*   **Authorization:** Checks if the user has the necessary permissions for network access.
*   **Accounting:** Tracks the usage of the network by the user, such as time online and data transferred.
In a Hotspot environment, the MikroTik router sends authentication requests to the RADIUS server. If the authentication is successful, the user will be granted access. Accounting is also managed by the radius server, so this can provide a central place to manage usage.

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:** Local authentication in MikroTik is simple, but RADIUS offers scalability, centralized user management, and advanced features. Local authentication is a good fallback if RADIUS servers are unavailable.
*   **Interim Updates:** Using frequent accounting updates can be beneficial for bandwidth reporting and limiting, but also increases server load, as each session is continuously updated in radius.
*   **Shared Secret Strength:** A complex shared secret is more secure but can be more difficult to manage.
*   **Timeout:** A shorter timeout value will fail users faster if radius is not available, but also creates unnecessary retries to radius, leading to higher load. A longer timeout value will reduce server load, but may lead to users being unable to log in temporarily while the router waits for a response.

## Configuration for Specific RouterOS Versions:

The configuration examples provided work in both RouterOS 6.48 and 7.x with minimal adjustments. The core concepts and commands related to RADIUS and Hotspot remain consistent across these versions.
However, it is recommended to always test your setup in a controlled environment to verify all features before deploying it to a live environment.

This detailed documentation provides a solid foundation for setting up RADIUS authentication on a MikroTik Hotspot. Always remember to test all configurations in a lab environment first before applying them to a production network.
