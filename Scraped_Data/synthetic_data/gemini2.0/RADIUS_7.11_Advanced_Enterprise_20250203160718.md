Okay, let's dive into configuring RADIUS authentication on a MikroTik router for a VLAN interface, targeting RouterOS 7.11 with an advanced configuration suitable for an enterprise environment.

## Scenario Description:

We will configure a MikroTik router to authenticate users connecting to VLAN 34 (48.168.79.0/24) against a RADIUS server. This setup allows for centralized user management, authentication, and authorization, enhancing security and control over network access. This could be used for guest wifi or a large enterprise where user access needs to be granularly managed and monitored.

## Implementation Steps:

Here's a step-by-step guide, combining CLI and Winbox examples, focusing on practical actions.

### 1. **Define the VLAN Interface (If Not Already Created)**

*   **Purpose:** Ensures the VLAN interface exists before configuring RADIUS.
*   **Action (CLI):**
    ```mikrotik
    /interface vlan
    add name=vlan-34 vlan-id=34 interface=ether1
    ```
    *   `name=vlan-34`: Assigns the name "vlan-34" to the VLAN interface.
    *   `vlan-id=34`:  Specifies the VLAN ID as 34.
    *  `interface=ether1`: Assigns the VLAN to the interface on which the VLAN will be trunked.
*   **Action (Winbox):**
    1.  Navigate to *Interfaces* -> *VLAN* tab.
    2.  Click the "+" button.
    3.  Enter "vlan-34" in the *Name* field.
    4.  Enter "34" in the *VLAN ID* field.
    5.  Select the desired interface (e.g. ether1) from the *Interface* dropdown.
    6.  Click *Apply*, then *OK*.

*   **Before:** No VLAN interface named "vlan-34" exists.
*   **After:** VLAN interface "vlan-34" is created and can be referenced.

### 2. **Configure IP Address on the VLAN Interface**

*   **Purpose:** Provides an IP address for the VLAN interface.
*   **Action (CLI):**
    ```mikrotik
    /ip address
    add address=48.168.79.1/24 interface=vlan-34
    ```
    *   `address=48.168.79.1/24`: Sets the IP address and subnet mask for the interface.
    *   `interface=vlan-34`: Specifies that the IP address is assigned to the "vlan-34" interface.
*   **Action (Winbox):**
    1.  Navigate to *IP* -> *Addresses*.
    2.  Click the "+" button.
    3.  Enter "48.168.79.1/24" in the *Address* field.
    4.  Select "vlan-34" from the *Interface* dropdown.
    5.  Click *Apply*, then *OK*.
*   **Before:** No IP address assigned to VLAN 34.
*   **After:** The IP address `48.168.79.1/24` is bound to VLAN 34.

### 3. **Configure the RADIUS Client**

*   **Purpose:** Adds the RADIUS server information to the MikroTik router.
*   **Action (CLI):**
    ```mikrotik
    /radius
    add address=192.168.10.1 secret=mysecret service=ppp,hotspot
    ```
     *   `address=192.168.10.1`: IP address of your RADIUS server. **IMPORTANT!** Replace this with your own IP address.
    *   `secret=mysecret`:  The shared secret for communication between the router and the RADIUS server. **IMPORTANT!** Replace with your own.
    *   `service=ppp,hotspot`: Specifies this RADIUS server is to be used for PPP and Hotspot services. If only using hotspot, you may specify just `hotspot`.
*   **Action (Winbox):**
    1.  Navigate to *RADIUS* under the *PPP* menu in the left panel.
    2.  Click the "+" button.
    3.  Enter the RADIUS server's IP address (e.g. "192.168.10.1") in the *Address* field.
    4.  Enter the shared secret (e.g. "mysecret") in the *Secret* field.
    5.  Check *Hotspot* and *PPP* under the *Services* section
    6.  Click *Apply*, then *OK*.
*   **Before:** No RADIUS configuration.
*   **After:** RADIUS client settings for the specified server are configured on the MikroTik router.

### 4. **Configure Hotspot Server (Example)**

*   **Purpose:** Example of how to set up hotspot configuration using this RADIUS server for authentication. **This step is not mandatory**.
*   **Action (CLI):**
     ```mikrotik
        /ip hotspot
        add name=hotspot1 interface=vlan-34 address-pool=pool1 profile=hsprof1
        /ip hotspot profile
        add name=hsprof1 html-directory=hotspot1 login-by=radius use-radius=yes
        /ip pool
        add name=pool1 ranges=48.168.79.100-48.168.79.200
        /ip dhcp-server
        add name=dhcp1 address-pool=pool1 interface=vlan-34
    ```
    *   `/ip hotspot add ...`: Creates a hotspot on the `vlan-34` interface.
    *   `name=hotspot1`: Gives the hotspot configuration the name of 'hotspot1'
    *   `interface=vlan-34`: Attaches the hotspot to the `vlan-34` interface.
    *   `address-pool=pool1`: Specifies the address pool for the hotspot users.
    *   `profile=hsprof1`: Specifies the profile for the hotspot setup.
    *   `/ip hotspot profile add ...`: Adds a hotspot profile
    *   `name=hsprof1`: Give the profile the name of 'hsprof1'.
    *   `html-directory=hotspot1`: Specifies the HTML directory for the hotspot.
    *  `login-by=radius`: Specifies that user authentication will occur via radius.
    *   `use-radius=yes`: Enable radius authentication for the hotspot.
    *   `/ip pool add ...`: Creates an address pool for the hotspot.
    *   `name=pool1`: Name of the pool.
    *   `ranges=48.168.79.100-48.168.79.200`: The range of IP addresses.
    *   `/ip dhcp-server add ...`: Adds a DHCP server for the hotspot on `vlan-34`.
    *   `name=dhcp1`: Name of the DHCP server.
    *  `address-pool=pool1`: Attaches the dhcp server to the address pool.
    *  `interface=vlan-34`: Attaches the DHCP server to the `vlan-34` interface.
*   **Action (Winbox):**
    1.  Navigate to *IP* -> *Hotspot*.
    2.  Click the "+" button on the *Hotspots* tab.
    3.  Enter "hotspot1" in the *Name* field.
    4.  Select "vlan-34" from the *Interface* dropdown.
    5.  Select "hsprof1" from the *Profile* dropdown.
    6. Click *Apply*, then *OK*.
    7.  Navigate to *IP* -> *Hotspot* -> *User Profiles*.
    8.  Click "+" to create a new profile, and name it 'hsprof1'.
    9.  Click the "Radius" tab, and click the *Use Radius* checkbox.
    10. Click *Apply*, then *OK*.
    11. Navigate to *IP* -> *Pools*.
    12. Click the "+" button and add the pool configuration as described above.
    13. Click *Apply*, then *OK*.
    14. Navigate to *IP* -> *DHCP Server*.
    15. Click the "+" button, add the DHCP server to `vlan-34` using the address pool created above.
    16. Click *Apply*, then *OK*.
*   **Before:** No hotspot service configured.
*   **After:** Hotspot service is enabled on `vlan-34`, using RADIUS for authentication.

## Complete Configuration Commands:

```mikrotik
# Create VLAN Interface
/interface vlan
add name=vlan-34 vlan-id=34 interface=ether1

# Assign IP Address
/ip address
add address=48.168.79.1/24 interface=vlan-34

# Configure RADIUS Client
/radius
add address=192.168.10.1 secret=mysecret service=ppp,hotspot

# Configure Hotspot (Example)
/ip hotspot
add name=hotspot1 interface=vlan-34 address-pool=pool1 profile=hsprof1
/ip hotspot profile
add name=hsprof1 html-directory=hotspot1 login-by=radius use-radius=yes
/ip pool
add name=pool1 ranges=48.168.79.100-48.168.79.200
/ip dhcp-server
add name=dhcp1 address-pool=pool1 interface=vlan-34
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** Router cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Verify the RADIUS server IP and secret are correct.
        *   Check for firewall rules blocking traffic between the router and the server (On the MikroTik, and potentially on the RADIUS server).
        *  Ping the server from the MikroTik using `/ping 192.168.10.1` (replace with server IP).
*   **Incorrect Secret:**
    *   **Problem:** The shared secret on the router does not match the RADIUS server.
    *   **Solution:** Double-check the secret on both devices and re-enter it carefully.
*   **Service Type Mismatch:**
    *   **Problem:** RADIUS service type on the router does not match the intended use.
    *   **Solution:** Ensure `service=ppp,hotspot` is appropriate, or specify the correct service (e.g. `hotspot` only if that is what you are using).
*   **Firewall Issues:**
    *   **Problem:** A firewall is blocking radius traffic.
    *   **Solution:** Ensure that outbound traffic from the Mikrotik to the RADIUS server is not being blocked, as well as the reverse. Verify the Mikrotik firewall configuration with `/ip firewall export`.

## Verification and Testing Steps:

1.  **RADIUS Connectivity Check:** Use `/tool radius test address=192.168.10.1 secret=mysecret user=test password=test service=hotspot` (replace with real values) to verify the router can communicate with the RADIUS server.
2.  **Hotspot User Authentication:** Connect a client device to the "vlan-34" network. The client should be redirected to the hotspot login page. Upon login, check if RADIUS server logs receive authentication attempts and check if the user is granted access by viewing the active hotspot users (`/ip hotspot active`).
3.  **Troubleshooting with Torch:** Use `/tool torch interface=vlan-34` to monitor traffic and see RADIUS communication.

## Related Features and Considerations:

*   **Accounting:** RADIUS can be used for accounting, tracking user usage. This is configured on the RADIUS server, and can be logged by the MikroTik.
*   **Dynamic VLAN Assignment:** RADIUS can return a VLAN ID during authentication to dynamically assign users to different VLANs.
*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy (using a `priority` parameter on the `/radius add` command) - the router will try the highest priority server first, and try the next if that fails.
*   **User Profiles:** Different RADIUS users can have different access rights or bandwidth limits.
*   **Coa and DM:** This could allow the radius server to disconnect specific users or change their settings on the fly. These are fairly advanced settings, but they are available on most RADIUS servers.
*   **VPNs:** RADIUS could be used for VPN authentication. In this case the `service` should include `ppp` and be configured on the ppp profiles.

## MikroTik REST API Examples (if applicable):

Here's an example of using the MikroTik REST API to add a RADIUS server configuration. Note that you will need to enable the API and authorize your user in `/user api`.

**API Endpoint:** `/radius`
**Method:** POST

**Example Request (JSON Payload):**
```json
{
    "address": "192.168.10.1",
    "secret": "mysecret",
    "service": "ppp,hotspot"
}
```
**Curl Example:**
```bash
curl -k -u "apiuser:password" -H "Content-Type: application/json" -X POST -d '{"address": "192.168.10.1", "secret": "mysecret", "service": "ppp,hotspot"}' https://your_router_ip/rest/radius
```
*   `address`: RADIUS Server's IP address.
*   `secret`: Shared secret for RADIUS communication.
*   `service`: Specifies services using this server (e.g., `ppp`, `hotspot`).

**Expected Response (201 Created):**
```json
{
    ".id": "*0",
    "address": "192.168.10.1",
    "secret": "mysecret",
    "service": "ppp,hotspot",
    "timeout": "3000",
    "accounting-port": "1813",
    "authentication-port": "1812",
    "realm": "",
    "domain": "",
    "use-accounting": "no",
    "add-mac-to-radius": "no",
    "called-id": "",
    "framed-protocol": "ppp",
    "interim-update": "0s",
    "comment": ""
}
```

**Error Handling:**
If the request fails (e.g., invalid parameters), the API returns an error code (e.g., 400 Bad Request) with an error message. For example,
```json
{
  "message": "input does not match the expected format, check arguments: bad value"
}
```
You should catch these errors in your API client, and display the information to the user.

## Security Best Practices

*   **Strong Shared Secret:** Use a complex and lengthy shared secret for RADIUS communication. Avoid common words or patterns.
*   **HTTPS for API Access:** Always access the MikroTik API via HTTPS with a valid certificate.
*   **Restrict API Access:** Limit API access to trusted networks or IP addresses using firewall rules.
*   **Monitor Logs:** Regularly monitor RADIUS server logs and MikroTik logs for any suspicious activity.
*   **Lock Down Access:** Use ACLs to limit access to the RADIUS server, and lock down any unused ports or features.
*   **Firewall Security:** Enforce a tight firewall policy and use stateful inspection. Ensure all connections coming from the RADIUS server are expected, and only from the expected sources.
*   **Upgrade Regularly:** Maintain the latest version of RouterOS to protect against vulnerabilities.
*   **Regular Audits:** Perform security audits and penetration tests on the router and any supporting infrastructure to ensure no new or existing flaws can be exploited.

## Self Critique and Improvements

This configuration provides a solid foundation for RADIUS authentication with a hotspot setup.

**Potential improvements:**

*   **Detailed User Profiles:** Implement more granular user profiles for different access levels using RADIUS attributes.
*   **Dynamic VLAN Assignments:** Add dynamic VLAN assignment for more flexibility in network management.
*   **More complex firewall rules:** Add more security to the firewall configuration.
*   **Error handling on API calls:** Add more specific error handling on the client side that processes the API calls.
*   **More specific logs:** Add more logging, perhaps to an external logging server, so that log files are centralized.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to network resources. It acts as a centralized database for user credentials and access policies, enhancing security, management, and consistency.

**How it Works:**

1.  **Authentication:** When a user attempts to access a network resource (e.g., connecting to a Wi-Fi hotspot), the network device (MikroTik router in our case) sends an authentication request to the RADIUS server.
2.  **Authorization:** The RADIUS server verifies the credentials and, if valid, returns access permissions (e.g., network access policies, bandwidth limitations).
3.  **Accounting:** The RADIUS server tracks user network usage, enabling reporting and control of resource consumption (e.g., data usage, session time).

## Detailed Explanation of Trade-offs

*   **Centralized vs. Local Authentication:** Centralized authentication using RADIUS simplifies user management, but adds the dependency on the RADIUS server. Local accounts, in contrast, are easier to set up but not suitable for large or complex environments. RADIUS allows for consistency across a whole network, and all authentication, user permissions and accounting can be done from a single location.
*   **Complexity vs. Security:** RADIUS setup is more complex initially but provides greater security and control. Local users are easier to manage but do not offer the same level of security and control, especially for guest networks.
*   **Redundancy:** Using one RADIUS server is simpler, but a single point of failure. Multiple servers adds more complexity, but increases the reliability.
*   **Static IP vs. Hotspot:** Using static IPs does not require RADIUS, or even a DHCP server. But if you want to manage access on a per-user basis, and monitor network activity, then Hotspot with RADIUS provides better security.
*  **Complexity of Radius Attributes:** Some RADIUS servers use attributes to control access, user rights, user limits and other important metrics. These settings are very complex, so using a system with basic auth simplifies configuration and maintenance, however it sacrifices control.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeting RouterOS 7.11 but should also work with 7.x and 6.48. The main difference between 6.x and 7.x is the inclusion of the REST API, which can be useful. If you have a 6.x version, you will not be able to use the REST API commands. The basic Radius and Hotspot setup commands remain the same.

This detailed document should provide a practical and comprehensive guide to configuring RADIUS on your MikroTik RouterOS device, including CLI commands, Winbox examples, API calls, and best practices. Remember to replace the example IP addresses, secrets, and other parameters with your actual values.
