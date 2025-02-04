Okay, here's a detailed technical documentation for setting up RADIUS authentication on a MikroTik RouterOS device, specifically targeting version 6.48 (with considerations for 7.x) in a point-to-point link scenario using VLAN 36.

## Scenario Description:

This configuration establishes RADIUS (Remote Authentication Dial-In User Service) authentication for users connecting through a specific VLAN interface (`vlan-36`) on a MikroTik router. The router will act as a Network Access Server (NAS), forwarding authentication requests to a centralized RADIUS server. This setup is common in situations where you need centralized user management and potentially accounting (e.g., for Wi-Fi hotspots, VPN access, or even managed ethernet links). For this example, the RADIUS server will be located on the `192.168.88.10` address.

## Implementation Steps:

### Step 1: Create the VLAN Interface

Before configuring RADIUS, we need to ensure the VLAN interface exists.

*   **Action:** Create a VLAN interface named `vlan-36` on the relevant physical interface (e.g., `ether1`).
*   **Reason:** This is where traffic that needs RADIUS authentication will enter the router.

**Before:** (Assuming `ether1` is your intended interface)

```
/interface print
Flags: X - disabled, R - running
 #    NAME                                  TYPE       MTU L2MTU  MAX-L2MTU
 0  R ether1                                 ether    1500  1598      1598
 1  R ether2                                 ether    1500  1598      1598
 2  R ether3                                 ether    1500  1598      1598
```

**CLI Command:**
```
/interface vlan add name=vlan-36 vlan-id=36 interface=ether1
```
**Winbox GUI:** Go to *Interfaces*, click the blue "+" button, and choose "VLAN." Then fill in the name (vlan-36), VLAN ID (36), and the parent interface (ether1).

**After:**

```
/interface print
Flags: X - disabled, R - running
 #    NAME                                  TYPE       MTU L2MTU  MAX-L2MTU
 0  R ether1                                 ether    1500  1598      1598
 1  R ether2                                 ether    1500  1598      1598
 2  R ether3                                 ether    1500  1598      1598
 3  R vlan-36                                vlan    1500  1598      1598
```

### Step 2: Assign an IP Address to the VLAN Interface

*   **Action:** Assign an IP address from the provided subnet (`185.63.65.0/24`) to the `vlan-36` interface. We will use `185.63.65.1/24` for the router's IP.
*   **Reason:**  The router needs an IP address within this subnet to communicate with clients connected on this VLAN.

**Before:**
```
/ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
```

**CLI Command:**
```
/ip address add address=185.63.65.1/24 interface=vlan-36
```
**Winbox GUI:** Go to *IP* -> *Addresses*, click the blue "+" button, enter the address (`185.63.65.1/24`), and select the interface (`vlan-36`).

**After:**

```
/ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0  185.63.65.1/24      185.63.65.0     vlan-36
```

### Step 3: Configure the RADIUS Server

*   **Action:** Add the RADIUS server configuration, including the IP address, shared secret, and authentication port.
*   **Reason:** This tells the router where to send authentication requests.

**Before:**

```
/radius print
Flags: X - disabled, I - invalid
```

**CLI Command:**
```
/radius add address=192.168.88.10 secret=your_secret_here service=ppp,hotspot,login,wireless,other timeout=2s
```
*Replace `your_secret_here` with your actual RADIUS shared secret.*
**Winbox GUI:** Go to *RADIUS*, click the blue "+" button, fill in the address, secret, service, and timeout.

**After:**

```
/radius print
Flags: X - disabled, I - invalid
 #   ADDRESS          SECRET     TIMEOUT      SERVICES
 0   192.168.88.10    ********      2s   ppp,hotspot,login,wireless,other
```

**Parameter Explanation for `/radius add` Command:**

| Parameter | Description |
|---|---|
| `address` | The IP address of the RADIUS server. |
| `secret` | The shared secret key that the MikroTik and RADIUS server use to authenticate each other (keep this very secure). |
| `service` | A comma-separated list of services that will use this RADIUS configuration (options: `ppp`, `hotspot`, `login`, `wireless`, `other`). |
| `timeout` | Time in seconds for the MikroTik to wait for a response from the RADIUS server before considering the request failed. |
| `accounting` | Enables or disables accounting for this radius entry (defaults to `no`). |
| `domain`  | Optional domain name to append to the user name before sending it to RADIUS. |
| `authentication-port` | Port used for authentication by the RADIUS server (defaults to `1812`). |
| `accounting-port` | Port used for accounting by the RADIUS server (defaults to `1813`). |

### Step 4: Enable RADIUS for desired services

*   **Action:**  In this case, for this specific scenario we will enable the radius server to handle PPP authentication requests, specifically to cover any future need. In a basic scenario such as this, the radius configuration can be used as a fallback for the hotspot service.
*  **Reason**: This enables radius authentication on the relevant service.

**Before:**
```
/ppp aaa print
 use-radius: no
```

**CLI Command:**
```
/ppp aaa set use-radius=yes
```
**Winbox GUI:** Go to *PPP*, select the *AAA* tab, and check *Use Radius*.

**After:**
```
/ppp aaa print
 use-radius: yes
```

### Step 5: Configure Hotspot Profile (If needed)
*   **Action**: If using a hotspot, modify an existing hotspot profile or create a new one.
*   **Reason**: Enables RADIUS authentication on the relevant hotspot profile. This also allows you to configure your users by using a captive portal.

**Before:**

```
/ip hotspot profile print
```
**CLI Command:**
```
/ip hotspot profile set [find name="your_hotspot_profile"] use-radius=yes
```
Replace `your_hotspot_profile` with the actual name of your hotspot profile.
**Winbox GUI:** Go to *IP* -> *Hotspot* -> *Profiles*, select your profile, and check *Use RADIUS*.

**After:**
```
/ip hotspot profile print
```

## Complete Configuration Commands:

```
/interface vlan add name=vlan-36 vlan-id=36 interface=ether1
/ip address add address=185.63.65.1/24 interface=vlan-36
/radius add address=192.168.88.10 secret=your_secret_here service=ppp,hotspot,login,wireless,other timeout=2s
/ppp aaa set use-radius=yes
# Optionally, enable for hotspot if needed:
/ip hotspot profile set [find name="your_hotspot_profile"] use-radius=yes

```

## Common Pitfalls and Solutions:

*   **Shared Secret Mismatch:** If the shared secret configured on the MikroTik doesn't match the RADIUS server, authentication will fail.
    *   **Solution:** Double-check the shared secret on both devices.
*   **Firewall Issues:** The MikroTik's firewall may block communication with the RADIUS server.
    *   **Solution:** Ensure that the firewall allows UDP traffic to ports 1812 and 1813 (or the configured ports).
*   **Incorrect IP Address:** If the RADIUS server's IP is misconfigured, the MikroTik won't be able to reach it.
    *   **Solution:** Verify the IP address of the RADIUS server.
*   **Service Selection:** If the correct services aren't checked under the `/radius` configuration, RADIUS will not be used.
    *   **Solution:** Correctly enable all the service parameters to the `/radius` entry.
*   **RADIUS Server Issues:** The RADIUS server might be down or misconfigured.
    *   **Solution:** Test the RADIUS server itself using a dedicated RADIUS client tool. Use a RADIUS debug tool on the RADIUS server for troubleshooting.
*  **Missing Authentication Method:** When authenticating a client, the correct authentication method must be set on the radius server configuration.
    *  **Solution:** Double-check the authentication methods in the RADIUS server. In a hotspot setup, PAP is usually used, as it is the more simple authentication method.

## Verification and Testing Steps:

1.  **Ping the RADIUS Server:** Ensure the MikroTik can reach the RADIUS server.
    ```
    /ping 192.168.88.10
    ```
2.  **Use the `tool radius` Command:** This command performs radius authentication directly from the MikroTik.
    ```
    /tool radius test user=test password=test address=192.168.88.10 secret=your_secret_here
    ```
    This command will return either `access-accept` or `access-reject` and other RADIUS attributes.
3.  **Test with a Client:** Connect a client to the `vlan-36` interface and attempt authentication. Review the logs on the MikroTik and the RADIUS server.
4.  **Check Logs:** Review the MikroTik logs (`/system logging print`) for any errors related to RADIUS.
    ```
      /system logging print where topics~"radius|ppp|hotspot"
    ```
5.  **Use `torch`:** Use the torch tool to monitor UDP traffic to the radius server's ports
   ```
     /tool torch interface=ether1 port=1812,1813 protocol=udp
   ```

## Related Features and Considerations:

*   **Accounting:** RADIUS accounting can be configured to track user sessions, data usage, and time online. Use the `accounting=yes` flag in the `/radius add` command.
*   **Dynamic VLAN Assignment:** RADIUS can assign VLANs dynamically.
*   **Different RADIUS Servers:** You can configure multiple RADIUS servers for redundancy.
*   **Hotspot Features:** RADIUS is commonly used with hotspot features for user authentication and management.
*   **VPN Services:** RADIUS can be used for authentication in L2TP, PPTP, or IKEv2 VPN setups.
* **Policy Control:** Combined with RADIUS, you can implement policies based on user groups, bandwidth limits, etc.

## MikroTik REST API Examples:

These examples use the REST API available in RouterOS 6.48 and later versions.

**1. Create a RADIUS Server entry:**
*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **Payload:**
```json
{
    "address": "192.168.88.10",
    "secret": "your_secret_here",
    "service": "ppp,hotspot,login,wireless,other",
    "timeout": "2s"
}
```
*   **Success Response:** HTTP 201 Created. JSON response with the newly created RADIUS object.
*   **Error Handling:** If there is an issue with the request, the server returns an HTTP 400 Bad Request or 500 Internal Server Error code with the error details.

**2.  Get all RADIUS server entries:**
*   **Endpoint:** `/radius`
*   **Method:** `GET`
*   **Payload:** none
*   **Success Response:** HTTP 200 OK. JSON array with all existing RADIUS objects.
*    **Error Handling:** If an error occurs the server will return an HTTP error code.

**3. Modify an existing RADIUS server entry:**
*   **Endpoint:** `/radius/<.id>` where `<.id>` is the internal identifier of the RADIUS config.
*   **Method:** `PUT`
*   **Payload:**
```json
{
    "timeout": "3s"
}
```
*   **Success Response:** HTTP 200 OK. JSON response with the modified RADIUS object.
*   **Error Handling:** If there is an issue with the request, the server returns an HTTP 400 Bad Request or 500 Internal Server Error code with the error details.

**4. Delete an existing RADIUS server entry:**
*   **Endpoint:** `/radius/<.id>` where `<.id>` is the internal identifier of the RADIUS config.
*   **Method:** `DELETE`
*   **Payload:** none
*   **Success Response:** HTTP 204 No Content.
*   **Error Handling:** If an error occurs the server will return an HTTP error code.

*Note: For all of these examples, you need to replace `your_secret_here` with your actual secret key.*

*Note: Make sure to enable the API on your router `ip/services/api` and verify that the required port is allowed by your firewall.*

## Security Best Practices

*   **Secure Shared Secret:** Use a strong, complex shared secret for RADIUS communication. Do not use a weak or default password.
*   **Restrict RADIUS Server Access:** Limit access to the RADIUS server to only necessary devices. Firewall rules should block connections from untrusted sources to the RADIUS server ports.
*   **Encrypt RADIUS Traffic (where possible):**  IPsec can secure RADIUS communications, but it adds complexity. The standard for RADIUS is based on UDP, and is usually not encrypted.
*   **Monitor Logs:** Regularly monitor RADIUS and MikroTik logs for suspicious activity.
*   **Disable Unnecessary Services:** Disable any unused services or ports on the router to reduce the attack surface.
*   **Keep RouterOS Updated:** Regularly update RouterOS to the latest stable version to patch any security vulnerabilities.
*   **Apply firewall rules:** Add firewall rules to allow only the necessary ports to connect to the RADIUS server from the MikroTik router.
*   **Limit Access to the MikroTik Router:** Restrict the source IPs that can access the MikroTik router's web interface, Winbox, and SSH.
*   **Use Strong Passwords:** Set strong and unique passwords for all accounts with access to the MikroTik router.
*   **Disable Default Accounts:** Disable any default accounts on the MikroTik router.
*   **Implement Two-Factor Authentication (2FA):** Enable 2FA for accessing the MikroTik router to improve security.

## Self Critique and Improvements

This configuration covers the basic RADIUS setup but could be improved with:

*   **More Robust Error Handling:** Add more specific error handling and logging configurations for RADIUS failures.
*   **Advanced Accounting:** Include a more detailed accounting configuration to track specific user attributes.
*   **Dynamic VLAN Assignment:** Implement the dynamic VLAN assignment process for more specific user segregation.
*   **Multiple RADIUS Servers:** Use multiple RADIUS servers for fault tolerance.
*   **Security Enhancements:** Add more granular firewall rules.
*  **Monitoring:** Incorporate a monitoring system to proactively alert in case of problems with the RADIUS server.
*   **Use Cases:** Provide examples for more specific use cases, such as VPN, hotspot management and other specialized uses cases.

## Detailed Explanation of RADIUS

RADIUS is a client-server protocol that provides centralized Authentication, Authorization, and Accounting (AAA) services for network access.

*   **Authentication:** Verifies a user's identity using credentials.
*   **Authorization:** Determines what resources the authenticated user is allowed to access.
*   **Accounting:** Tracks user activity, including resource usage and time spent online.

RADIUS servers are centralized databases that manage user accounts. This allows for easier administration and enforcement of network policies. A NAS (Network Access Server, like the MikroTik router) forwards authentication requests to the RADIUS server. RADIUS traffic is usually UDP based.

## Detailed Explanation of Trade-offs

*   **RADIUS vs. Local Authentication:**
    *   **RADIUS:** Centralized user management, easier for large networks, greater flexibility. Introduces added complexity.
    *   **Local Authentication:** Simple to configure, suitable for small networks, less scalable, less secure.
*   **UDP vs TCP:** UDP is the recommended protocol for RADIUS. However, TCP is possible.
    *   **UDP:** Faster, connectionless protocol, suitable for large number of requests.
    *  **TCP:** Slower, connection-oriented, better for more reliable but slower communication.
*   **Single vs Multiple RADIUS Servers:**
    *   **Single:** Simpler to manage, single point of failure.
    *   **Multiple:** Redundancy, improved reliability, more complex setup.
*  **PAP vs CHAP vs MSCHAPv2**
    *  **PAP**: Sends the password in clear text. It is not secure, but simple to setup.
    *  **CHAP/MSCHAPv2**: Are more secure methods for authentication. Requires the radius server to support it.
*  **Plain password vs Radius:**
     *  **Plain Password:** Simpler to configure in the router, but it does not provide a centralized way of user management.
     *  **Radius:**  Provides a centralized way to manage users, but it is more complex to configure.

## Configuration for Specific RouterOS Versions:

This documentation is primarily for RouterOS 6.48, but all commands are still valid for RouterOS 7.x. There are minor differences in the web interface, but the core CLI commands will remain the same.  Be sure to check the official MikroTik documentation for any specific version changes. For example, RouterOS 7.x has better support for Radius Attributes.

This completes the in-depth documentation for RADIUS configuration on MikroTik RouterOS.
