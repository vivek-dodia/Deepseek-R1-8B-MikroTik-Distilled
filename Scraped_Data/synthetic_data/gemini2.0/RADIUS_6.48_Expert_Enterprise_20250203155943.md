Okay, let's dive into configuring RADIUS authentication for a MikroTik router on a bridge interface, tailored for an Enterprise network scale using RouterOS 6.48. We'll prioritize detailed explanations and practical examples, ensuring everything is actionable and verifiable.

## Scenario Description:

We aim to configure a MikroTik router (running RouterOS 6.48) to use a RADIUS server for authentication of users connecting via the `bridge-43` interface. This setup is common in enterprise environments where centralized user management and access control are required.  The router will send authentication requests to a specified RADIUS server, and access will be granted or denied based on the RADIUS server's response.  This is a crucial step in providing secure network access and user accountability.

## Implementation Steps:

Here's a detailed step-by-step guide to implementing RADIUS authentication on bridge-43:

**1. Step 1: Configure RADIUS Server Details**

   *   **Goal:** Define the RADIUS server's IP address, shared secret, and authentication port.
   *   **Why:**  The MikroTik router needs to know how to reach the RADIUS server to send authentication requests. The shared secret is used for secure communication between the router and server.
   *   **Action:**
       *   **CLI:**

            ```mikrotik
            /radius add address=192.168.10.10 secret="my_secret_key" service=ppp,hotspot timeout=30s authentication-port=1812
            ```
       *   **Winbox:** Go to `Radius` menu, Click `Add` and fill the form.

       *   **Explanation of parameters:**
            *   `address`: The IP address of the RADIUS server (e.g. `192.168.10.10`).
            *   `secret`: The shared secret key configured on the RADIUS server (e.g., `my_secret_key`). This must match exactly.
            *    `service`: specifies which services should use the RADIUS.  Common options include `ppp` (for PPPoE and PPTP), `hotspot`, `dhcp`. Here we use both `ppp` and `hotspot`. If you need to use this radius server for multiple types of authentication, add all of them as comma-separated values.
            *    `timeout`: specifies how long should the router wait for the RADIUS server to respond (e.g., 30 seconds).
            *    `authentication-port`: the port used for authentication (typically 1812).

       *   **Before:** No RADIUS servers are configured.
       *   **After:** The MikroTik router will have a RADIUS server defined. The router will send an authentication request to the RADIUS server using this address, secret, port, and service.

**2. Step 2: Configure Bridge-43 Interface for Hotspot**

    *   **Goal**: Enable and configure the Hotspot feature on the `bridge-43` interface.
    *   **Why**:  Hotspot is a common way to manage authentication for LAN users. This uses the bridge interface for access.
    *   **Action**:
        *   **CLI:**
            ```mikrotik
            /interface bridge port add bridge=bridge-43 interface=ether1
            /ip hotspot profile add name=hotspot-profile-43  use-radius=yes radius-accounting=yes
            /ip hotspot user profile add name=hotspot-user-profile-43
            /ip hotspot add name=hotspot-43 interface=bridge-43 profile=hotspot-profile-43 address-pool=dhcp_pool-1
            /ip pool add name=dhcp_pool-1 ranges=10.0.0.10-10.0.0.254
            ```
        *   **Winbox:**  `Bridge`->`Ports`-> Click `Add`, Select the interface (e.g. `ether1`), select the bridge (`bridge-43`). `IP` -> `Hotspot` -> `Hotspot Profiles`, Add a new profile, enable the `use radius` and `radius accounting` checkboxes.  Add a new user profile.  Then, `IP` -> `Hotspot` ->  Click `Add`, select the `bridge-43` interface,  and the profile we created earlier. `IP` -> `Pool`, click `Add`, give the pool a name and range.
        *   **Explanation of parameters:**
            *   `/interface bridge port add bridge=bridge-43 interface=ether1`: Adds `ether1` to the `bridge-43`. Change `ether1` to your interface name.
            *    `/ip hotspot profile add name=hotspot-profile-43 use-radius=yes radius-accounting=yes`: Creates a Hotspot profile called `hotspot-profile-43` with RADIUS authentication enabled and accounting.
            *    `/ip hotspot user profile add name=hotspot-user-profile-43`: Creates a user profile called `hotspot-user-profile-43` (we're not configuring much on this, but we still need one)
            *    `/ip hotspot add name=hotspot-43 interface=bridge-43 profile=hotspot-profile-43 address-pool=dhcp_pool-1`: Adds the Hotspot service to the `bridge-43`, associates it with `hotspot-profile-43` and a DHCP pool.
            *    `/ip pool add name=dhcp_pool-1 ranges=10.0.0.10-10.0.0.254`: Creates the IP pool which will be used for DHCP on this interface. Adjust the ranges to your network.
        *   **Before:** The `bridge-43` interface is just a bridge, the hotspot is not enabled.
        *   **After:** The `bridge-43` interface will now provide a hotspot, forcing users to authenticate with the RADIUS server before receiving access to the network.

**3. Step 3: (Optional) Customize Hotspot Login Page**

    *   **Goal:** Customize the Hotspot login page
    *   **Why:** Customize the login page with your brand, specific terms of service, etc.
    *   **Action:**
        *   **CLI**
            ```mikrotik
            /file upload file=login.html
            /ip hotspot profile set [find name="hotspot-profile-43"] html-directory=hotspot
            ```
        *   **Winbox:** Copy the `login.html` file to your Router. Go to `Files` -> Drag the file into the window. Go to `IP` -> `Hotspot` -> `Hotspot Profile` and set the `HTML Directory` of the relevant profile to `hotspot`
       *   **Explanation of parameters:**
            *   `/file upload file=login.html` upload your custom html page
            *   `/ip hotspot profile set [find name="hotspot-profile-43"] html-directory=hotspot` set the folder for the login page. The file should be called `login.html` in this directory.
        *   **Before:** The hotspot uses the default html page.
        *   **After:** The hotspot uses the custom login page.

## Complete Configuration Commands:

Here's the full set of commands to implement the setup:

```mikrotik
/radius add address=192.168.10.10 secret="my_secret_key" service=ppp,hotspot timeout=30s authentication-port=1812
/interface bridge port add bridge=bridge-43 interface=ether1
/ip hotspot profile add name=hotspot-profile-43 use-radius=yes radius-accounting=yes
/ip hotspot user profile add name=hotspot-user-profile-43
/ip hotspot add name=hotspot-43 interface=bridge-43 profile=hotspot-profile-43 address-pool=dhcp_pool-1
/ip pool add name=dhcp_pool-1 ranges=10.0.0.10-10.0.0.254
/file upload file=login.html
/ip hotspot profile set [find name="hotspot-profile-43"] html-directory=hotspot
```

## Common Pitfalls and Solutions:

*   **Problem:**  RADIUS server unreachable.
    *   **Solution:**
        *   Verify the RADIUS server's IP address, that it is up and running, and accessible from the router. `ping 192.168.10.10`.
        *   Check the firewall on both the router and server. Use `/tool torch interface=ether1 port=1812` to check traffic on the router to see if traffic is being sent on that interface and to that port.
        *   Ensure the secret matches exactly between router and server.
        *   Use `/radius print` to check the radius configuration.
*   **Problem:** Users can't authenticate with the RADIUS server.
    *   **Solution:**
        *   Verify the usernames and passwords are correct on the RADIUS server.
        *   Review RADIUS logs on the server for authentication failures and other errors.
        *   Check the RADIUS service list and ensure `hotspot` or `ppp` is configured and enabled on the radius server.
*   **Problem:** Hotspot not presenting a login page.
    *   **Solution:**
        *   Verify the hotspot is enabled correctly with `/ip hotspot print`
        *   Ensure the html-directory is correctly configured.
*   **Problem:**  High CPU/memory usage.
    *   **Solution:**
        *   Monitor CPU and memory usage using `/system resource print`. If high, consider reducing logging verbosity, or upgrading the router.

## Verification and Testing Steps:

1.  **Ping Test:**
    *   `ping 192.168.10.10` from the router to confirm reachability to the radius server.
2.  **Torch tool:**
    *   Use `/tool torch interface=ether1 port=1812` to confirm RADIUS traffic is being sent and received between the router and the RADIUS server
3.  **Client Connection Test:**
    *   Connect a client to the `bridge-43` network. You should be redirected to the hotspot login page.
    *   Try logging in with RADIUS credentials. If the authentication passes you should get access to the internet.
4.  **RADIUS Logs:**
    *   Check the RADIUS server logs for successful or failed authentication attempts. The exact location of the logs will vary depending on your server, but are often found in `/var/log/freeradius/`.
5.  **MikroTik Logs:**
    *   Use `/log print where topics~"radius"` or `/log print where topics~"hotspot"` to check Mikrotik logs for authentication or hotspot errors.

## Related Features and Considerations:

*   **RADIUS Accounting:** We've already enabled accounting in this setup, which is essential for tracking user sessions and data usage. The RADIUS server needs to be setup to handle accounting packets.
*   **Hotspot Customization:** Customize the hotspot login page with your logo, terms, and other content.
*   **Multiple RADIUS Servers:** Add redundancy by configuring multiple RADIUS servers.
*   **MAC Address Authentication:** Consider MAC authentication before RADIUS authentication for devices where no user login is required, such as VoIP Phones.
*   **Address Lists:** Use address lists to manage access control more granularly.
*   **VLANs:** Implement VLANs on the bridge and hotspot for better network segmentation.
*   **RouterOS 7.x:** Many of the commands will remain unchanged, however, there are differences in the way Hotspot is configured, so you may need to adjust the hotspot-related commands. Be sure to use the relevant documentation to ensure your configuration is relevant to your RouterOS version.

## MikroTik REST API Examples (if applicable):

While the RouterOS API covers the core functions of RADIUS and Hotspot, configuration of these through the API can be complex, because it involves managing multiple areas. Here's an example of *reading* RADIUS configuration and adding a new one using the API, which can be generalized for other Hotspot related configuration:

**1. Fetching RADIUS Servers**

*   **Endpoint:** `/radius`
*   **Method:** GET
*   **Request:** No payload needed
*   **Expected Response (JSON):**
    ```json
    [
      {
        "id": "*1",
        "address": "192.168.10.10",
        "secret": "my_secret_key",
        "service": "ppp,hotspot",
        "timeout": "30s",
        "authentication-port": "1812"
      }
    ]
    ```
*   **Error Handling**: A 401 or 403 error means you have an issue with the API credentials, or lack permission to get this information. A 500 error means the api encountered a problem processing your request and the response data should contain more information.  A 200 response code means the request succeeded.
*   **Description:** This is an example of getting all radius servers that are configured in the router.

**2. Adding a new RADIUS Server**

*   **Endpoint:** `/radius`
*   **Method:** POST
*   **Request (JSON Payload):**
    ```json
    {
        "address": "192.168.10.11",
        "secret": "another_secret",
        "service": "ppp",
        "timeout": "60s",
        "authentication-port": "1812",
        "accounting-port": "1813"
    }
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "message": "added",
        "id": "*2"
    }
    ```
*   **Error Handling:**
    *   A 400 error means that there is an error in the payload, and the response body should contain detailed information about the error.
    *   A 401 or 403 error means you have an issue with the API credentials, or lack permission to get this information.
    *   A 500 error means the api encountered a problem processing your request.
*   **Description:** This is an example of creating a new radius server.  `id` is a unique id that you can use to update or delete the radius server later.

**Note:**  Remember to use proper API authentication to secure API access. Please note that you also need to have a user with api permission before you can successfully use the API.

## Security Best Practices:

*   **Strong Secrets:** Use complex, randomly generated shared secrets for RADIUS.
*   **Secure Server:** Ensure the RADIUS server is on a hardened system and is properly secured.
*   **Firewall:** Restrict access to the RADIUS server's ports (1812/1813) to the necessary sources.
*   **TLS:** If possible, configure RADIUS over TLS (RadSec) for encrypted communication.
*   **Rate Limiting:** Use rate limiting on the router to mitigate brute-force attacks on RADIUS authentication.
*   **Access Control:**  Limit who can access the Mikrotik Router.
*   **Regular Updates:** Keep both the RouterOS and RADIUS server software up to date.

## Self Critique and Improvements:

This configuration provides a functional RADIUS setup. However, improvements can be made by:

*   **Centralized User Management:** Integration with a user directory service such as Active Directory for better user and group management.
*   **More Granular Access Control:** Implement more detailed access policies based on user groups and network segments.
*   **Real-time Monitoring:** Deploy monitoring tools for RADIUS and network performance for a quick response to issues.
*   **Automation:** Use scripting or configuration management tools to automate router configuration and reduce human error.
*   **Proper VLAN Configuration:** We did not configure VLANs here, but on real-world enterprise networks VLANs are a must to ensure proper network segmentation.
*   **Address Lists:** Implement address lists to manage what services are available to each subnet.
*   **Detailed Logging:** Configure more detailed logging on the Mikrotik to better debug any issues that might arise.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):**

RADIUS is a protocol used for centralized authentication, authorization, and accounting (AAA) of users connecting to a network. It allows you to offload user management from the network devices themselves, making network administration much easier.

*   **Authentication:** The router sends user credentials (usually username and password) to the RADIUS server. The RADIUS server verifies these credentials against its database and responds with success or failure.
*   **Authorization:** The RADIUS server can send information back about the level of access for each user.
*   **Accounting:** The RADIUS server can keep track of usage for each user, including connection time and data transferred.

RADIUS is commonly used in:

*   **WiFi Hotspots:** For users logging in to public or guest WiFi.
*   **VPNs:** For authentication of VPN users.
*   **Network Access Control (NAC):** To manage access to wired and wireless network access.
*   **ISP networks:** Used extensively for authentication of clients and for billing purposes.

**Hotspot:**

A Hotspot is a feature of RouterOS that facilitates controlled access to the network. It is particularly useful for managing public or guest access. It usually involves:

*   **Redirecting Users:** Redirects users to a login page before they can access the internet.
*   **Authentication Methods:** It can use various authentication methods, such as RADIUS, local users, or walled garden login.
*   **Session Management:** It can manage user sessions, limiting session time and data transfer.
*   **Customization:** It allows you to customize the login page, logo, terms of service, etc.
*   **Billing:** Hotspot can integrate with billing systems.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:** Local authentication on the Mikrotik is simpler to set up, but doesn't scale well for large networks. It also doesn't allow for centralized user management. RADIUS on the other hand is more complex to set up but is much better suited to managing a lot of users, and allows for centralized management.
*   **Hotspot vs. PPP authentication:** Hotspot is easier to use for users connecting to a network. PPP such as PPPoE is more suitable to authenticate specific clients to a particular service, usually on a client side router connecting to the network.  Both can use RADIUS to perform authentication.
*   **Single vs. Multiple RADIUS Servers:** Having multiple RADIUS servers adds redundancy, making it more reliable, but the setup is more complicated.
*   **RADIUS with or without Accounting:** Accounting is optional but helps with monitoring. If accounting is not needed for reporting it can be turned off. However, if you need to do reporting, it must be turned on.

## Configuration for Specific RouterOS Versions:

This documentation is primarily for RouterOS 6.48 and also works with 7.x. However, newer versions of RouterOS such as 7.x have made changes to the way Hotspot is configured. Please ensure you always use the relevant RouterOS documentation for your current version.
*   **RouterOS 7.x Hotspot changes**: On RouterOS 7.x, Hotspot configurations are handled within `Hotspot Server Profiles` and are configured more like DHCP Servers, and have different settings and menus to configure. This will require you to adapt the steps regarding Hotspot configurations.

By following these detailed steps, you should be able to successfully set up a RADIUS-based authentication system on your MikroTik router, providing a secure and reliable way to manage network access. This explanation should be complete, easy to follow, and give you the knowledge to get started with RADIUS and Hotspot on MikroTik routers.
