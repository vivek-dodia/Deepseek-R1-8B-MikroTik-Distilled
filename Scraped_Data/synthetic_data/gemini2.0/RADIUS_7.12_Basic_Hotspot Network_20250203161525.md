Okay, let's craft some detailed documentation for configuring RADIUS on a MikroTik router in a hotspot network, targeting RouterOS 7.12 (but also taking 6.48 & other 7.x versions into account). This will be a basic configuration with advanced concepts hinted at for future expansion.

## Scenario Description:

We are configuring a MikroTik router acting as a hotspot access point. Users connecting to the `vlan-8` interface, which operates on the `50.130.255.0/24` subnet, will be authenticated against a RADIUS server before being granted internet access. This basic setup will focus on authentication only and does not include accounting.

## Implementation Steps:

**Detailed Explanation of Topic: RADIUS**

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users who connect to a network. In our scenario, we'll be using it solely for authentication: verifying if the user's credentials are valid. RADIUS generally communicates using UDP on ports 1812 (authentication) and 1813 (accounting), though this is configurable. RADIUS relies on the exchange of attribute-value pairs which define user and network parameters.

**1. Step 1: Add a RADIUS Server Configuration**

   *   **Explanation:** Before anything, we need to tell the MikroTik router how to reach our RADIUS server, including the IP address, shared secret (used for secure communication), and service port.

   *   **CLI Example (Before):**
       ```
       /radius print
       ```
       *Expected Output: Empty table*

   *   **CLI Example (After):**
        ```
        /radius add address=192.168.10.10 secret=mySecret auth-port=1812 timeout=3
        ```
       *Explanation of Parameters:*
       
         | Parameter  | Explanation                                                     |
         |--------------|-----------------------------------------------------------------|
         | address      | IP address of the RADIUS server.                 |
         | secret        | Shared secret for RADIUS communication.                |
         | auth-port    | UDP port for authentication requests.                       |
         | timeout      | Time in seconds to wait for a RADIUS response.  |

     *   **Winbox GUI:** Go to `Radius` in the left menu and click the `+` icon to add a new RADIUS configuration.

   *   **Effect:** The router is now configured to communicate with the specified RADIUS server.

**2. Step 2: Configure a Hotspot Profile to Use RADIUS**

   *   **Explanation:** We modify the hotspot profile (which controls user access in the hotspot) to use RADIUS for authentication. We also add a new user profile for our hotspot, which enables rate limiting (if needed). We also ensure that there's an IP pool that is assigned to hotspot users.
   *  **CLI Example (Before):**
       ```
       /ip hotspot profile print
       /ip pool print
        /ip hotspot user profile print
       ```
      *Expected Output: Default tables and potentially one default user profile.*

   *  **CLI Example (After):**
        ```
        /ip pool add name=hotspot_pool ranges=50.130.255.2-50.130.255.254
        /ip hotspot profile add name=radius_hotspot_profile hotspot-address=50.130.255.1/24 use-radius=yes pool=hotspot_pool
        /ip hotspot user profile add name=limited_access rate-limit=10M/10M
        /interface vlan add name=vlan-8 vlan-id=8 interface=ether1
        /ip address add address=50.130.255.1/24 interface=vlan-8
        /ip hotspot add address-pool=hotspot_pool disabled=no interface=vlan-8 name=hotspot1 profile=radius_hotspot_profile
        ```
     *Explanation of Parameters:*
      
        | Parameter  | Explanation                                                     |
        |--------------|-----------------------------------------------------------------|
        | `name`    | Name of the hotspot profile.                               |
        | `hotspot-address` | IP address and mask of the hotspot network.   |
        | `use-radius`      | Specifies whether to use RADIUS for authentication.              |
        | `pool` | The IP pool the hotspot users use when assigned an IP. |
        | `rate-limit`    | Limit the upload/download speed for users.                                          |
        | `vlan-id`  | VLAN ID                                            |
        | `interface` | Interface for the VLAN                               |
        | `address` | IP address of the interface                            |
        | `disabled` | Is the hotspot disabled?                            |
        | `address-pool`  | Specifies the IP address range to be assigned to clients. |

    * **Winbox GUI:**
       1.  Go to `IP` > `Pool`, click the `+` icon and add an IP pool, `hotspot_pool`, with ranges `50.130.255.2-50.130.255.254`.
       2. Go to `IP` > `Hotspot` > `Profiles`, select the profile you want to modify (or add new one) and enable the `Use RADIUS` checkbox. Select `hotspot_pool` as the IP Pool
       3. Add the VLAN interface via `Interface > + > VLAN` and set up the necessary settings.
       4.  Go to `IP` > `Address`, click the `+` icon and add an address of `50.130.255.1/24` to `vlan-8`
       5. Go to `IP` > `Hotspot`, add a new hotspot interface, using the VLAN interface and the hotspot profile created.

   *   **Effect:** Users connecting to the hotspot will now be redirected to the RADIUS server for authentication before being granted access.

**3. Step 3: Enable Hotspot on VLAN 8**

    *   **Explanation:** Ensure the hotspot server is running on the VLAN interface created earlier. This step is already completed as part of **step 2**.
    
    *   **CLI Example (After):**
        ```
        /ip hotspot print
        ```
    
    * **Winbox GUI:** Verify that hotspot interface is configured in `IP > Hotspot > Servers`

   * **Effect:** Users can now access the hotspot service on the `vlan-8` interface.

## Complete Configuration Commands:

```
/radius
add address=192.168.10.10 auth-port=1812 secret=mySecret timeout=3
/ip pool
add name=hotspot_pool ranges=50.130.255.2-50.130.255.254
/ip hotspot profile
add name=radius_hotspot_profile hotspot-address=50.130.255.1/24 use-radius=yes pool=hotspot_pool
/ip hotspot user profile
add name=limited_access rate-limit=10M/10M
/interface vlan
add name=vlan-8 vlan-id=8 interface=ether1
/ip address
add address=50.130.255.1/24 interface=vlan-8
/ip hotspot
add address-pool=hotspot_pool disabled=no interface=vlan-8 name=hotspot1 profile=radius_hotspot_profile
```
*Explanation of Parameters:* See step-by-step breakdown.

## Common Pitfalls and Solutions:

*   **Problem:** Incorrect RADIUS secret.
    *   **Solution:** Double-check the shared secret on both the MikroTik and RADIUS server.
*   **Problem:** Firewall blocking RADIUS traffic.
    *   **Solution:** Ensure firewall rules allow UDP traffic from the MikroTik to the RADIUS server on ports 1812 and 1813 (for accounting, if applicable).
*   **Problem:** Incorrect IP address of RADIUS server.
    *   **Solution:** Verify that the RADIUS server is reachable from MikroTik router and the IP address of the RADIUS server on the MikroTik is correct.
*   **Problem:** RADIUS server not properly configured or unreachable.
    *   **Solution:** Test connectivity to the RADIUS server from another computer, verify RADIUS server logs, and double-check that RADIUS server is running and listening for RADIUS requests.
*   **Problem:** Hotspot interface not set correctly.
    *   **Solution:** Ensure the hotspot server is enabled on the `vlan-8` interface and the correct profile is attached to the hotspot server.
*   **Problem:** Users failing to authenticate.
    *   **Solution:** Check the user's credentials are valid on the RADIUS server. Check logs on the MikroTik router (`/system logging print`) and the RADIUS server. Enable debug logging on the RADIUS server if available for more detailed information.
*  **Problem:** Users not getting the correct speed.
    *  **Solution:** Ensure the correct `user profile` is being assigned by the RADIUS server. This profile will limit speed and other user settings.

* **Security Issues:**
    *  **Problem:** RADIUS shared secret is weak or exposed.
    *  **Solution:** Use strong, complex secrets, and secure the configuration of the MikroTik and RADIUS server.
    *  **Problem:** User credentials are sent unencrypted.
    *  **Solution:** If possible, use EAP authentication which includes a secure tunnel.

## Verification and Testing Steps:

1.  **Connect a Device to the Hotspot:** Connect a laptop or phone to the `vlan-8` network.
2.  **Attempt to Access a Website:** Try opening a webpage. You should be redirected to the hotspot login page.
3.  **Enter RADIUS Credentials:** Enter a username and password that is configured on your RADIUS server.
4.  **Check for Successful Authentication:**
    *   **MikroTik CLI:**
        ```
        /ip hotspot active print
        ```
        You should see the logged in user.
        ```
        /log print
        ```
    Check for log entries indicating successful RADIUS authentication.
    *   **RADIUS Server:** Check the RADIUS server logs for successful authentication records.
5.  **Troubleshooting:**
    *   Use `/tool torch interface=vlan-8` on the MikroTik to inspect traffic. Ensure you see UDP traffic to port 1812 to the RADIUS server.

## Related Features and Considerations:

*   **Accounting:**  Configure RADIUS accounting to track user session time and data usage.
*   **CoA (Change of Authorization):** Implement CoA to dynamically change user attributes during active sessions.
*   **HTTPS for Login Page:** Secure the hotspot login page using SSL/TLS certificates to protect user credentials.
*   **Walled Garden:** Implement a walled garden to allow access to specific resources (e.g., the login page, specific websites) before authentication.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for failover and redundancy.
*  **User Management:** Set up a user management portal to allow user self registration.
*  **Custom Login Page:** Create a custom login page that is more friendly and branded.
*  **Session Limits:** Limit the time and data usage for each user on the hotspot.
*  **IP binding:** Implement IP binding to lock a particular IP to a MAC address.

## MikroTik REST API Examples:

While most of the above configuration is simpler via CLI or Winbox, here's an example of adding a RADIUS server via the MikroTik REST API (assuming you have it enabled). Note: This feature needs to be enabled on the router first by going to `IP > Services` and setting `api` to enabled.

*   **API Endpoint:** `/radius`
*   **Request Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
      "address": "192.168.10.10",
      "secret": "mySecret",
      "auth-port": 1812,
      "timeout": 3
     }
    ```
*  **Expected Response (Success):**
    ```json
    {
      "id": "*<id>",
      "address": "192.168.10.10",
      "secret": "mySecret",
      "auth-port": 1812,
      "timeout": 3,
        "accounting-port": 1813,
        "service": "ppp",
       "disabled": false
    }
    ```
*   **Error Handling:**
    If the JSON request is invalid or missing parameters, the API will return an HTTP error code (e.g., 400 Bad Request) and a JSON response containing error details. For example:

    ```json
    {
      "message": "invalid value of address",
      "error": "invalid value",
      "code": 202006
    }
    ```
   * **API Error codes**: For more information on error codes, see the MikroTik API documentation.
    *  Always check the HTTP status code and the contents of the response body for errors and take appropriate action.
*   **Parameter Description:**
      *   **`address`**: (string) The IP address of the RADIUS server.
    *   **`secret`**: (string) The shared secret used for RADIUS communication.
    *   **`auth-port`**: (integer) The UDP port for authentication.
    *   **`timeout`**: (integer) Timeout in seconds to wait for a RADIUS response.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a strong and unique shared secret.
*   **EAP Authentication:** When possible, use EAP based authentication methods (EAP-TLS, EAP-TTLS, PEAP) that provide better security over PAP or CHAP.
*   **Firewall Rules:** Only allow RADIUS traffic from trusted interfaces to the RADIUS server.
*   **Regular Auditing:** Check all MikroTik settings periodically, including security settings.
*   **Access Control:** Limit access to the MikroTik configuration to authorized personnel only.

## Self Critique and Improvements

*   **Simplicity:** The current setup is very basic and should be expanded for practical use.
*   **Accounting:** Missing RADIUS accounting, which is important for session management.
*   **Dynamic Profiles:** The configuration could be improved to dynamically assign user profiles (rate limits, etc.) based on RADIUS attributes.
*   **Error Handling:** More advanced error handling and retry mechanisms could be implemented.
*   **Logging:** Need to configure and monitor logging for troubleshooting.
*   **Scalability:**  For very large networks, multiple RADIUS servers and load balancing should be implemented.

This configuration provides a starting point for RADIUS authentication with a MikroTik hotspot. Real-world deployments will often need more advanced configurations and integrations.

## Detailed Explanation of Trade-offs

Here's a breakdown of some trade-offs:

*   **PAP vs. EAP:**
    *   **PAP (Password Authentication Protocol):** Simple, but sends passwords in plain text and is not suitable for public networks.
    *   **EAP (Extensible Authentication Protocol):** Provides secure authentication, but is more complex to implement and requires configuration on both MikroTik and RADIUS server.
        * Trade-off: PAP is simple, but insecure, EAP is secure, but complex.
*   **Basic User Profile vs. RADIUS Assigned Profiles:**
    *   **Basic User Profile:** Easy to set up, but limited in capabilities. All users are treated the same.
    *   **RADIUS Assigned Profiles:** More flexible, where the RADIUS server can assign attributes based on user information.
        * Trade-off: Basic profile is simple, but has limited capabilities. RADIUS can be made more complex, but offers more customization and flexibility.
*   **Single RADIUS Server vs. Multiple RADIUS Servers:**
    *   **Single Server:** Easy to manage, but susceptible to single point of failure.
    *   **Multiple Servers:** More complex to set up, but provides higher availability and load balancing capabilities.
        * Trade-off: A single server is easier to set up and manage, but can fail. Using multiple servers provides redundancy and scalability, but is more complex.
*   **Local Hotspot Page vs. external Login Page:**
    *   **Local Hotspot Page:**  Easy to set up, but limited in features and customizations.
    *   **External login page:** Can be very customized and has more potential features.
        * Trade-off: Local login pages are simple to set up, while external login pages allow for additional flexibility.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 7.12 and can be used on RouterOS 7.x, as well as 6.48.
All the commands used are present in both RouterOS 6.48 and 7.x. There are not significant changes in the way radius, hotspot or interfaces are set up between these versions.
Newer versions of 7.x could have some additional commands, but this basic configuration will work as described on all specified versions.

Let me know if you would like any modifications or further explanation on a specific aspect!
