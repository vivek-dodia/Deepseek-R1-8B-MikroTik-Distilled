Okay, let's craft detailed documentation for implementing RADIUS authentication on a MikroTik router, targeting RouterOS 7.12, within an enterprise network context, specifically on VLAN interface "vlan-23" with a subnet of 153.59.200.0/24.

## Scenario Description:

This document details the implementation of RADIUS authentication for network access control on a MikroTik router. We will configure the router to act as a RADIUS client, forwarding authentication requests from devices connected to the `vlan-23` interface to a central RADIUS server. This ensures that only users with valid credentials can gain access to the network. This is common in enterprise environments to centrally manage network access policies. The subnet used is 153.59.200.0/24 and will be allocated to the vlan-23 interface.

## Implementation Steps:

Here's a step-by-step guide, including CLI and Winbox instructions:

1.  **Step 1: Configure the VLAN Interface**

    *   **Purpose:** Before configuring RADIUS, we need to make sure the interface and ip address are correctly configured.

    *   **Before Configuration:** Assuming there is no vlan interface with ID 23, there should be no such interface.

    *   **CLI Command:**

        ```mikrotik
        /interface vlan
        add name=vlan-23 vlan-id=23 interface=ether1
        /ip address
        add address=153.59.200.1/24 interface=vlan-23
        ```

    *   **Winbox GUI:**
        *   Navigate to `Interface > VLAN`.
        *   Click the "+" button to add a new VLAN interface.
        *   Set `Name` to `vlan-23`, `VLAN ID` to `23`, and `Interface` to `ether1` or whichever interface is physically connected to the network you want to use for VLAN 23.
        *   Click `Apply` and `OK`.
        *   Navigate to `IP > Addresses`.
        *   Click the "+" button to add a new address.
        *   Set `Address` to `153.59.200.1/24` and `Interface` to `vlan-23`.
        *   Click `Apply` and `OK`.

    *   **After Configuration:** The router now has a VLAN interface named `vlan-23` and an ip address of `153.59.200.1/24`.

2.  **Step 2: Configure the RADIUS Server Settings**

    *   **Purpose:** Define the IP address, port, and secret of the RADIUS server.
    *   **Before Configuration:** RADIUS authentication is not configured.
    *   **CLI Command:**

        ```mikrotik
        /radius
        add address=192.168.100.10 secret=secure_radius_secret service=login,ppp,hotspot,wireless
        ```
      *   **Explanation:**
            *   `address=192.168.100.10`: Specifies the IP address of your RADIUS server. Replace `192.168.100.10` with your RADIUS server's actual IP.
            *   `secret=secure_radius_secret`: Sets the shared secret used for RADIUS authentication. Replace `secure_radius_secret` with the actual secret shared between the router and the RADIUS server. **This is crucial for security and must match the configuration on the RADIUS server**.
            *   `service=login,ppp,hotspot,wireless`: Enables RADIUS authentication for these services. We are only interested in `login` as this allows the use of RADIUS authentication for login to the mikrotik router, and we will focus on this functionality.
    *   **Winbox GUI:**
        *   Navigate to `RADIUS`.
        *   Click the "+" button to add a new RADIUS entry.
        *   Set `Address` to `192.168.100.10`
        *   Set `Secret` to `secure_radius_secret`.
        *   Check the boxes under the `Services` column for `login`.
        *   Click `Apply` and `OK`.

    *   **After Configuration:** The router now knows the address of your RADIUS server and shared secret.

3.  **Step 3: Configure the Router to Use RADIUS for Login**
      *   **Purpose:** Sets the router to use RADIUS authentication before trying the local authentication database.
      *   **Before Configuration:** Login authentication is performed locally on the router.
      *   **CLI Command:**

        ```mikrotik
        /user aaa set use-radius=yes
        ```
        *   **Explanation:**
            *   `use-radius=yes`: Enables RADIUS authentication for logins.
      *   **Winbox GUI:**
        * Navigate to `System > Users`.
        * Click `AAA`
        * Check the box `Use RADIUS`
        * Click `Apply` and `OK`
      * **After Configuration:** The router will now attempt RADIUS authentication before local user authentication.

4.  **Step 4: Testing login through RADIUS**
      *   **Purpose:** Attempt to login to the router using a valid user/password in the RADIUS server.
      *   **Before Configuration:**  We can test via ssh or winbox using a valid RADIUS user. If a login is successful then RADIUS is working.
      *   **CLI Command:**
            * From your workstation, ssh to the mikrotik router using a user/password configured on the RADIUS server.

      *  **Winbox GUI:**
            * From your workstation, launch winbox and attempt to login to the router using a user/password configured on the RADIUS server.
      * **After Configuration:** The router is accessible using RADIUS credentials.

## Complete Configuration Commands:

```mikrotik
/interface vlan
add name=vlan-23 vlan-id=23 interface=ether1
/ip address
add address=153.59.200.1/24 interface=vlan-23
/radius
add address=192.168.100.10 secret=secure_radius_secret service=login,ppp,hotspot,wireless
/user aaa set use-radius=yes
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** Router cannot reach the RADIUS server.
    *   **Solution:**
        *   Verify IP connectivity: `ping 192.168.100.10` from the router.
        *   Check firewall rules on the MikroTik and any intermediate firewalls.
        *   Ensure the RADIUS server is running and listening on the correct port.
*   **Incorrect RADIUS Secret:**
    *   **Problem:** Authentication fails due to a mismatch in the shared secret.
    *   **Solution:** Double-check the secret on the MikroTik and the RADIUS server.
*   **RADIUS Server Configuration:**
    *   **Problem:** Incorrect configurations on the RADIUS server side (wrong nas configuration, username not available).
    *   **Solution:** Review RADIUS server logs for details on why an authentication attempt failed. Ensure the MikroTik router’s IP is a valid NAS client for the RADIUS server.
*  **MikroTik not configured to use the RADIUS server**
    *   **Problem:** RADIUS is configured but not enabled in the `/user/aaa` settings
    *   **Solution:** Ensure `use-radius=yes` in the `/user/aaa` settings.

## Verification and Testing Steps:

1.  **Ping:** `ping 192.168.100.10` on the MikroTik to check if the RADIUS server is reachable.
2.  **Debug:** Enable RADIUS debugging with `/system logging add topics=radius action=memory`
3.  **Attempt login:** Try logging into the MikroTik via SSH or Winbox with RADIUS credentials and observe the logs.
4.  **Logs:** Examine the `/log` for RADIUS-related messages, specifically `RADIUS: ...received Access-Accept/Reject` messages. Ensure that the router received the radius message from the server.  Also check the RADIUS server log for the request being sent by the mikrotik and the response.
5.  **Torch:** use torch on the interface the RADIUS traffic is expected to travel on to capture the RADIUS traffic, verify it is going to the correct location.

## Related Features and Considerations:

*   **Multiple RADIUS Servers:** MikroTik supports multiple RADIUS servers for redundancy. Configure backup servers in the `/radius` menu. If the primary server fails, the router will try the secondary server.
*  **Accounting:** In addition to Authentication MikroTik also support Accounting (start and stop) and can be configured at the same time as Authentication.
*   **RADIUS Attributes:** You can customize RADIUS attributes sent and received, which can be essential for specific RADIUS server configurations. MikroTik specific attributes can be passed along with regular RADIUS attributes.
*  **Framed-IP-Address:** The RADIUS server can return a framed-ip-address and the mikrotik router will assign that ip to the logged in user, overriding the normal DHCP behavior.

## MikroTik REST API Examples (if applicable):

*Note: Due to the nature of RADIUS, direct management of authentication/authorisation via the REST API is not typically performed and is instead managed through the server. The following API example will setup the RADIUS server, along with the enabling of using the RADIUS server.*

*   **Add RADIUS Server:**

    ```http
    POST /radius
    Content-Type: application/json

    {
      "address": "192.168.100.10",
      "secret": "secure_radius_secret",
      "service": ["login"]
    }
    ```

    *   **Parameters:**
        *   `address`: IP address of the RADIUS server. (String)
        *   `secret`: Shared secret between the router and the RADIUS server. (String)
        *   `service`: An array of services using the radius. Possible values: `login`, `ppp`, `hotspot`, `wireless`. (Array of strings)
    *   **Expected Response:** 200 OK with the new RADIUS server configuration, or an error message if there is a failure.
* **Enable Use of RADIUS**

    ```http
    PUT /user/aaa
    Content-Type: application/json

    {
     "use-radius": true
    }
    ```

    *   **Parameters:**
        *   `use-radius`: Enable or disable the use of RADIUS authentication. (Boolean)
    *   **Expected Response:** 200 OK with the modified AAA configuration, or an error message if there is a failure.
* Error Handling:
  *If an error arises from a REST API call, the response will be in JSON format and include an 'message' key indicating the error.

  ```json
    {
       "message": "RADIUS server address already exists"
    }
  ```
  It's important to catch these errors in the calling code and handle them appropriately.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a strong, complex shared secret between the router and RADIUS server.
*   **Secure RADIUS Communication:** If possible, use secure channels (e.g., VPN or IPSec) between the MikroTik router and the RADIUS server.
*   **RADIUS Server Hardening:** Ensure your RADIUS server is secured against unauthorized access and has the latest security patches.
* **Rate Limiting:** If you are worried about denial of service through radius authentication, consider rate limiting to avoid flooding the RADIUS server.
*   **Limit Access:** Restrict access to your RADIUS server only to trusted devices.
*   **Regular Review:** Periodically review the RADIUS configuration for vulnerabilities and update security practices.

## Self Critique and Improvements:

*   **Improvement:** The configuration can be made more robust by implementing multiple RADIUS servers for redundancy.
*   **Improvement:** Add more logging and monitoring for radius transactions, for better visibility.
*   **Improvement:** The addition of detailed accounting parameters can be useful for audit purposes.
* **Improvement:** Rate limiting of RADIUS requests should be done to mitigate DOS attack.

## Detailed Explanations of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to a network. It works by having a Network Access Server (NAS), such as a MikroTik router, forward user authentication requests to a RADIUS server. The RADIUS server then either accepts or rejects the user based on the configured user accounts. This allows for centralized user management.

## Detailed Explanation of Trade-offs:

*   **Local Authentication vs. RADIUS:**
    *   **Local Authentication:** Simple to configure, but lacks centralized management, and can be difficult to maintain in larger networks.
    *   **RADIUS:** Centralized management, better for larger networks with numerous users, provides a single point of authentication, allows for more complex policies, but introduces a single point of failure (if only one radius server is used). RADIUS also requires more configuration and complexity.
*   **Single vs. Multiple RADIUS Servers:**
    *   **Single Server:** Simpler to set up but vulnerable to a single point of failure.
    *   **Multiple Servers:** Higher availability and resilience, but more complex to manage.

## Configuration for Specific RouterOS Versions:

The commands and steps provided are compatible with RouterOS versions 7.12 and later (including 6.48, 7.x series), The specific versions used will be the most recent from the 7.x series.
*For versions below 7.x (such as 6.48) the command for setting use-radius is located at `/ppp aaa`.

This detailed documentation should provide a comprehensive guide for implementing RADIUS authentication on your MikroTik router. Please remember to adjust the IP addresses, secrets, and interface names to match your specific environment.
