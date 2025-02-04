Okay, let's craft some detailed, expert-level documentation for integrating RADIUS authentication into a MikroTik Hotspot network using VLAN 43 and the subnet 204.247.115.0/24, targeting RouterOS 6.48 (and relevant for 7.x).

## Scenario Description:

This scenario involves configuring a MikroTik router acting as a hotspot controller. Users connecting to the hotspot will be authenticated against a RADIUS server before they're granted network access.  The hotspot interface will be tagged with VLAN ID 43, meaning all hotspot traffic will flow via this specific VLAN. The IP subnet for the hotspot will be 204.247.115.0/24. This setup could be used in a SOHO, SMB, or even a more extensive enterprise or hotspot network.

## Implementation Steps:

Here's a step-by-step guide to implementing the RADIUS setup on your MikroTik router:

**1.  Initial Router State & Interface Setup:**

*   **Initial State:** We assume the router is in a basic, routable configuration.  Before this step, no hotspot is configured on vlan-43, and there are no RADIUS settings.
*   **Interface Creation (if needed):** If `vlan-43` doesn't exist, create the VLAN interface.  We assume an existing interface, let's say `ether1` is used for trunking. If not, you must create an appropriate physical link.

    ```mikrotik
    # CLI Example: (If vlan-43 does not exist)
    /interface vlan
    add interface=ether1 name=vlan-43 vlan-id=43
    ```

    *   **Explanation:** This command creates a new VLAN interface named `vlan-43` on the physical interface `ether1`, assigning it the VLAN ID of 43. This is the core of using VLANs on a Mikrotik.

*   **Winbox Equivalent:** Go to `Interface` -> `+` -> `VLAN`.  Set `Name` to `vlan-43`, `Interface` to `ether1` and `VLAN ID` to `43`.
    *  **Verification:** Check in `Interface`, if `vlan-43` exists and is up.

**2.  IP Address Assignment:**

*   **Configuration:** Assign an IP address to the `vlan-43` interface.
*    **Example:**

    ```mikrotik
     /ip address
     add address=204.247.115.1/24 interface=vlan-43
    ```

    *   **Explanation:** This command assigns the static IP address `204.247.115.1/24` to the `vlan-43` interface. This is the gateway address for the hotspot users.
*   **Winbox Equivalent:** Go to `IP` -> `Addresses` -> `+`. Set `Address` to `204.247.115.1/24` and `Interface` to `vlan-43`.
    *  **Verification:** Go to `IP` -> `Addresses` verify `204.247.115.1/24` with interface `vlan-43`.

**3.  RADIUS Server Configuration:**

*   **Configuration:** Configure the MikroTik router to communicate with the RADIUS server.  For this example, we will use the IP address `192.168.88.10` and a shared secret of `radiussecret`.
*   **Example:**

    ```mikrotik
    /radius
    add address=192.168.88.10 secret=radiussecret service=hotspot timeout=30
    ```

    *   **Explanation:** This command adds a new RADIUS server configuration.
        * `address` specifies the IP address of the RADIUS server.
        * `secret` is the shared secret between the MikroTik and the RADIUS server, crucial for security.
        * `service` specifies `hotspot` so the radius server can be used for the specific hotspot feature.
        * `timeout` is the time to wait for the RADIUS server response.
*   **Winbox Equivalent:** Go to `RADIUS` -> `+`. Configure the parameters as described above.
    *  **Verification:** Go to `RADIUS` verify the newly created entry.

**4. Hotspot Configuration:**

*   **Configuration:** Set up the Hotspot server on the `vlan-43` interface.
*   **Example:**

    ```mikrotik
    /ip hotspot
    add address-pool=dhcp-pool1 disabled=no interface=vlan-43 name=hotspot1 profile=hsprof1
    /ip hotspot profile
    add dns-name=hotspot.example.com html-directory=hotspot login-by=http-chap name=hsprof1 radius-interim-update=30s
    ```

    *   **Explanation:**
        * The first command adds the Hotspot server itself. It links the interface to a hotspot name, with an IP pool that we'll create in the next step, and a profile that we will create in step 2.
        * The second command creates a profile:
            *   `dns-name` defines a DNS name that will be used to forward the users to an specific web address.
            *   `html-directory` is used to store the login page.
            *   `login-by=http-chap` specifies the method used to authenticate the users.
            * `radius-interim-update` the interval time in which the Mikrotik send status updates to the radius server.
        * **Important Note:** This will create the necessary initial configuration, but the address-pool will be created in the next step.
*   **Winbox Equivalent:** Go to `IP` -> `Hotspot` -> `Hotspot Servers` -> `+`. Set `Name` to `hotspot1`, `Interface` to `vlan-43` and select or create the needed `Profile`. Go to `IP` -> `Hotspot` -> `Profiles` and select or create the needed `Profile`.
    *  **Verification:** In `IP` -> `Hotspot` -> `Hotspot Servers` a new server with interface `vlan-43` exists. In `IP` -> `Hotspot` -> `Profiles` a new profile `hsprof1` exists.

**5. DHCP Server Configuration:**

*   **Configuration:** Set up the DHCP server to distribute IP addresses for the hotspot clients.
*   **Example:**

    ```mikrotik
    /ip pool
    add name=dhcp-pool1 ranges=204.247.115.10-204.247.115.254
    /ip dhcp-server
    add address-pool=dhcp-pool1 disabled=no interface=vlan-43 lease-time=30m name=dhcp1
    /ip dhcp-server network
    add address=204.247.115.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=204.247.115.1
    ```

    *   **Explanation:**
        *   The first command creates a new IP pool named `dhcp-pool1` to allocate addresses for the hotspot clients.
        *   The second command creates a DHCP server instance on `vlan-43`, using the pool `dhcp-pool1`.
        *   The third command creates a network entry that will be used for the dhcp server, assigning a gateway and dns-server to clients when receiving an IP address.
*   **Winbox Equivalent:** Go to `IP` -> `Pool` -> `+`.  Set `Name` to `dhcp-pool1`, and `Ranges` to the appropriate range. Go to `IP` -> `DHCP Server` -> `+`.  Set `Interface` to `vlan-43`, `Address Pool` to `dhcp-pool1`. Go to `IP` -> `DHCP Server` -> `Networks` and add the corresponding network parameters.
    *  **Verification:** Go to `IP` -> `Pool` verify the new pool `dhcp-pool1`. Go to `IP` -> `DHCP Server`, verify the new entry for `dhcp1`. Go to `IP` -> `DHCP Server` -> `Networks`, and verify the corresponding network parameters.

**6.  Enable RADIUS Authentication for Hotspot:**

*   **Configuration:** Enable RADIUS authentication in the Hotspot profile.
*   **Example:**

    ```mikrotik
     /ip hotspot profile
     set hsprof1 use-radius=yes
    ```

    *   **Explanation:** This command activates RADIUS authentication for the Hotspot profile `hsprof1`. Now all authentication will be done by the RADIUS server configured before.
*   **Winbox Equivalent:** Go to `IP` -> `Hotspot` -> `Profiles`.  Select `hsprof1` and check the `Use RADIUS` box.
    * **Verification:** Go to `IP` -> `Hotspot` -> `Profiles` verify that `use-radius` is checked.

## Complete Configuration Commands:

```mikrotik
# Create VLAN interface if it doesn't exist:
/interface vlan
add interface=ether1 name=vlan-43 vlan-id=43

# Assign IP address to the VLAN interface:
/ip address
add address=204.247.115.1/24 interface=vlan-43

# Configure RADIUS server:
/radius
add address=192.168.88.10 secret=radiussecret service=hotspot timeout=30

# Configure Hotspot server:
/ip hotspot
add address-pool=dhcp-pool1 disabled=no interface=vlan-43 name=hotspot1 profile=hsprof1
/ip hotspot profile
add dns-name=hotspot.example.com html-directory=hotspot login-by=http-chap name=hsprof1 radius-interim-update=30s

# Configure DHCP server:
/ip pool
add name=dhcp-pool1 ranges=204.247.115.10-204.247.115.254
/ip dhcp-server
add address-pool=dhcp-pool1 disabled=no interface=vlan-43 lease-time=30m name=dhcp1
/ip dhcp-server network
add address=204.247.115.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=204.247.115.1

# Enable RADIUS authentication for the Hotspot profile:
/ip hotspot profile
set hsprof1 use-radius=yes
```

## Common Pitfalls and Solutions:

1.  **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik can't reach the RADIUS server due to firewall rules, incorrect IP address, or a network issue.
    *   **Solution:**
        *   Check network connectivity using `ping 192.168.88.10` from the MikroTik.
        *   Verify that any firewalls between the MikroTik and RADIUS are allowing communication on UDP ports 1812 and 1813.
        *   Double-check the RADIUS server IP address and shared secret.
2.  **Incorrect Shared Secret:**
    *   **Problem:** If the shared secret on the MikroTik and the RADIUS server doesn't match, authentication will fail.
    *   **Solution:** Ensure the same secret is configured on both sides.
3.  **DHCP Server Issues:**
    *   **Problem:** Clients aren't getting IP addresses, or they cannot access the login page.
    *   **Solution:**
        *   Verify the DHCP server is enabled on the correct interface (`vlan-43`).
        *   Ensure that the `address-pool` is correctly configured.
        *   Check the firewall to allow DHCP traffic.
4.  **Hotspot Profile Problems:**
    *   **Problem:** The Hotspot login page does not appear or the radius authentication is not working.
    *   **Solution:**
        *   Verify the hotspot is enabled on the correct interface (`vlan-43`).
        *   Verify the correct profile is configured.
        *   Double check `login-by` configuration.
5.  **Resource Exhaustion:**
    *   **Problem:** High CPU usage due to a large number of hotspot users can impact performance.
    *   **Solution:** Monitor CPU and memory using `system resource print`. Consider using a more powerful router if needed or implementing rate limits for individual users to reduce the processing overhead.
6.  **VLAN Tagging Issues:**
    *   **Problem:** Users not able to get an IP address or not being forwarded to the hotspot page.
    *   **Solution:** Make sure that the interface that will receive the vlan tagged traffic is configured to receive vlan tagged traffic, and not plain untagged traffic. This could imply modifying the switch connected to the Mikrotik.
7. **Radius timeout:**
    * **Problem:** If the radius server is slow, or has too much traffic it might not respond to the authentication attempts, leading to authentication failures.
    * **Solution:** Increase the `timeout` parameter in the radius server config on the Mikrotik.

## Verification and Testing Steps:

1.  **Interface Status:** Verify the `vlan-43` interface is up and has the IP address assigned.
    ```mikrotik
    /interface print
    /ip address print
    ```
2.  **RADIUS Reachability:** Test connectivity to the RADIUS server using `ping 192.168.88.10`. Check if the shared secret is working by enabling debug logging of RADIUS packets in the RADIUS server and performing an authentication attempt from a hotspot client.
3. **DHCP Configuration:** Verify clients are receiving a IP address from the specified pool. Check `IP` -> `DHCP Server` -> `Leases`.
4.  **Hotspot Functionality:**
    *   Connect a client to the `vlan-43` network (Wi-Fi or wired).
    *   Upon connection, the client should automatically be redirected to the hotspot login page.
    *   Attempt to login using credentials defined in your RADIUS server. If successful, the hotspot page will allow you to browse.
5.  **RADIUS Traffic:** Monitor RADIUS traffic using `/tool torch interface=vlan-43 port=1812,1813`. This can help to see packets being sent and received by the Mikrotik.
6.  **System Resource Usage:** Monitor CPU and Memory usage with `/system resource print`.

## Related Features and Considerations:

*   **User Manager:** MikroTik's User Manager package offers a built-in RADIUS server and user management portal, which can be a simpler option if you don't have an external RADIUS server.
*   **Hotspot User Profiles:** Configure user profiles with bandwidth limits, session limits, and other settings.
*   **Walled Garden:** Define specific sites that users can access without authentication. This can be useful for providing free access to certain resources.
*   **Custom Login Page:** Create a custom HTML login page for a branded experience.
*  **Accounting:** Enable RADIUS accounting to record the amount of time and data users are consuming.
*  **Coovachilli:** Use an open-source captive portal solution like Coovachilli to offer a more advanced login page.

## MikroTik REST API Examples:

Here are examples of using the MikroTik REST API to manipulate some of the configuration elements.

*Note:* MikroTik API requires HTTPS and authentication and an active API service configured on the Mikrotik.

**Example 1: Add a RADIUS server**

*   **API Endpoint:** `/radius`
*   **Request Method:** `POST`
*   **JSON Payload:**

    ```json
    {
      "address": "192.168.88.12",
      "secret": "anothersecret",
      "service": "hotspot",
       "timeout": 45
    }
    ```

*   **Expected Response (200 OK):**
    ```json
    {
        ".id": "*<id_generated_by_mikrotik>"
     }
    ```
    *  **Description:** This JSON payload adds a new radius server to the device. The address, secret, service and timeout will be configured.
    *  **Error Handling:** If the configuration is invalid (e.g., missing required fields), the API will return a `400 Bad Request` error with details.

**Example 2: Get RADIUS server list**

*   **API Endpoint:** `/radius`
*   **Request Method:** `GET`
*   **JSON Payload:** None
*   **Expected Response (200 OK):**

    ```json
    [
        {
            ".id": "*1",
             "address": "192.168.88.10",
             "secret": "radiussecret",
             "service": "hotspot",
             "timeout": "30"
        },
         {
            ".id": "*2",
             "address": "192.168.88.12",
             "secret": "anothersecret",
             "service": "hotspot",
             "timeout": "45"
         }
    ]
    ```
   * **Description:** This endpoint returns a list of all radius servers.

**Example 3: Enable RADIUS in a Hotspot Profile**

*   **API Endpoint:** `/ip/hotspot/profile`
*   **Request Method:** `PATCH`
*   **JSON Payload:**
    ```json
    {
      ".id": "*h",
      "use-radius": true
    }
    ```
*   **Expected Response (200 OK):** Empty body
  *  **Description:** This JSON payload modifies an existing profile identified by it's ID. `use-radius` is set to `true`, enabling radius authentication for this profile.
  *  **Error Handling:** Invalid ID or an error in the configuration will result in a `400 Bad Request` or `404 Not Found` error.

## Security Best Practices

1.  **Strong RADIUS Secret:** Use a complex, strong, and unique shared secret for RADIUS communication.
2.  **Secure RADIUS Server:** Ensure the RADIUS server itself is secured with strong passwords and appropriate access controls.
3.  **Firewall Rules:** Implement strict firewall rules on your MikroTik to limit access to the RADIUS server and other critical components.
4.  **Regular Updates:** Keep your MikroTik RouterOS up to date to patch any vulnerabilities.
5.  **Disable Unused Services:** Disable any unneeded services on your MikroTik.
6.  **User Management:** Regularly monitor and manage user accounts to avoid any compromises.
7. **Limit API access:** Only allow api calls from trusted networks, and with encrypted connections.

## Self Critique and Improvements

This configuration covers a fundamental hotspot setup with RADIUS. However, some areas could be improved:

*   **Error Handling:** The documentation could provide more specific error codes and solutions for edge cases.
*   **Advanced RADIUS Attributes:** Examples could include using RADIUS attributes like Framed-IP-Address or setting custom Vendor-Specific Attributes (VSAs) for additional flexibility.
*   **Dynamic VLANs:** Explore RADIUS controlled dynamic VLAN assignment, which allows users to automatically be placed in a specific VLAN based on their user accounts.
*   **Advanced Hotspot Customization:** Expand the explanation of advanced hotspot features like walled gardens, user quotas, and customized login pages.
*  **Load Balancing:** In large setups, explain the benefits of load balancing authentication attempts between multiple radius servers.
*  **Rate limiting:** Add specific configurations for rate-limiting users based on their radius configuration, to help manage resources.

## Detailed Explanations of Topic:

*   **RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users. In this context, it's used to verify user credentials against an external database, allowing network access only to authorized users.
*   **VLAN (Virtual Local Area Network):** VLANs are used to logically segment a network, allowing traffic from different VLANs to be isolated from each other despite using the same physical infrastructure. In this context, VLAN 43 is used to separate hotspot traffic from other traffic on the same physical interfaces.
*   **Hotspot:** A Hotspot is a service on MikroTik that provides a controlled network access point. It forces users to authenticate themselves before granting full network access.
*   **DHCP Server:** A DHCP server dynamically assigns IP addresses to devices that connect to the network. It also provides necessary information like the gateway and DNS server IP addresses.

## Detailed Explanation of Trade-offs

*   **Internal User Manager vs. External RADIUS:**
    *   **Internal User Manager:** Easier to configure for basic scenarios, but lacks advanced features and scalability compared to RADIUS.
    *   **External RADIUS:** More complex to set up, but provides more control, scalability, and integration with other services.
*   **Static vs. Dynamic IP Assignment:**
    *   **Static:** Easier to manage with a small number of users, but complex for larger networks.
    *   **Dynamic:** Easier to manage with a large number of users, more flexible, but less control per specific user.
*   **HTTP-CHAP vs other authentication methods:**
    *   **HTTP-CHAP:** Uses challenge-response, avoiding to send the users password over the wire, but it might be incompatible with some devices.
    *   **Other methods:** Provide more flexibility, but might be less secure.
*   **Using VLANs:** While using VLANs adds more complexity to the configuration it allows for more flexibility and management, improving overall security.

## Configuration for Specific RouterOS Versions:

The commands provided are suitable for RouterOS 6.48 and 7.x.  However, there may be subtle differences in behavior or error messages between versions. The documentation should include specific command-line outputs to verify each step.
   *  For example, the command to add a radius server is the same across those versions, but the printed values in `/radius print` might be slightly different, especially in how they print the `id`.

This detailed documentation should give you a solid starting point for deploying RADIUS authentication in your MikroTik hotspot environment. Remember to test all changes thoroughly before implementing in a production network.
