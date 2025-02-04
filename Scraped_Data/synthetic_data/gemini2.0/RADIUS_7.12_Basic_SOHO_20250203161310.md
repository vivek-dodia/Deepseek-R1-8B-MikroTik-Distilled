Okay, let's dive into a detailed RADIUS configuration for a SOHO network using MikroTik RouterOS 7.12, focusing on practical implementation, troubleshooting, and security best practices.

## Scenario Description:

This scenario involves configuring a MikroTik router as a RADIUS client to authenticate users connecting to the network via a bridge interface named "bridge-58".  We are using a RADIUS server with IP address 192.168.88.100, secret "radiussecret", authentication port 1812 and accounting port 1813.  The subnet for local network behind bridge-58 is 219.113.174.0/24.  We will implement MAC address authentication, meaning we will use the MAC address of connecting clients as the username and password for RADIUS authentication.  This is commonly used in smaller setups when managing access for known devices.

## Implementation Steps:

### Step 1:  Set up the Bridge Interface

**Before:** Assuming a basic RouterOS setup, we start with a network interface, for the purposes of this example this can be assumed to be `ether1`.

```mikrotik
# Before any bridge configuration
/interface print
```

**Explanation:** This initial command simply shows existing interfaces, ensuring we start with a known configuration. Note that the interface `ether1` in this example needs to be on the local LAN and connected to the network where clients will be connecting to the `bridge-58`.

**Action:**
*   Create a bridge interface named `bridge-58`.
*   Add ether1 to the bridge.

```mikrotik
/interface bridge
add name=bridge-58
/interface bridge port
add bridge=bridge-58 interface=ether1
/ip address
add address=219.113.174.1/24 interface=bridge-58
```

**After:** The `ether1` interface will be included in `bridge-58`, and an IP address of 219.113.174.1/24 is assigned to the bridge interface.
```mikrotik
/interface print
/interface bridge port print
/ip address print
```

**Effect:** We've established the basic interface to which our local clients connect. All traffic will be flowing on bridge-58 and thus be subject to any rules applied to bridge-58.

### Step 2: Configure the RADIUS Server

**Before:** No RADIUS server is configured.

```mikrotik
/radius print
```

**Explanation:** This command shows that no RADIUS servers are configured.

**Action:** Add the RADIUS server details.
```mikrotik
/radius
add address=192.168.88.100 secret="radiussecret" service=ppp,login,hotspot timeout=3s
```

**After:**
```mikrotik
/radius print
```

**Effect:** We have now configured the RADIUS server details within the MikroTik.

### Step 3: Enable MAC Authentication on the Bridge

**Before:** No MAC authentication is in place.

```mikrotik
/interface bridge settings print
```

**Explanation:** This command shows the current bridge settings. We are going to enable MAC authentication for our bridge.

**Action:** Enable MAC authentication and specify the RADIUS service.
```mikrotik
/interface bridge settings set use-radius=yes radius-mac-authentication=yes
/interface bridge set bridge-58 admin-mac=00:00:00:00:00:01
```

**After:** The bridge settings will show the change, and a MAC address will be assigned to the bridge.
```mikrotik
/interface bridge settings print
/interface bridge print
```

**Effect:** MAC address authentication is now enabled on bridge-58. When a new MAC address connects to bridge-58, the MikroTik will attempt RADIUS authentication using the MAC address as username and password.

### Step 4: Configure a DNS Server

**Before:** DNS is likely configured already, but we will confirm.

```mikrotik
/ip dns print
```

**Explanation:** This command shows the current DNS settings. We need to make sure we have DNS set for clients.

**Action:** If DNS is not set, set your DNS servers.

```mikrotik
/ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
```

**After:**
```mikrotik
/ip dns print
```

**Effect:** We have now ensured that clients on bridge-58 can correctly use DNS.

## Complete Configuration Commands:

```mikrotik
/interface bridge
add name=bridge-58
/interface bridge port
add bridge=bridge-58 interface=ether1
/ip address
add address=219.113.174.1/24 interface=bridge-58
/radius
add address=192.168.88.100 secret="radiussecret" service=ppp,login,hotspot timeout=3s
/interface bridge settings set use-radius=yes radius-mac-authentication=yes
/interface bridge set bridge-58 admin-mac=00:00:00:00:00:01
/ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Check network connectivity (ping the RADIUS server from the MikroTik).
        *   Verify the correct RADIUS server IP address.
        *   Confirm the correct RADIUS secret is configured on both the MikroTik and RADIUS server.
        *   Ensure the correct UDP ports (1812,1813) are not blocked.
*   **Authentication Failures:**
    *   **Problem:** Users are not able to authenticate.
    *   **Solution:**
        *   Double check the RADIUS secret.
        *   Enable RADIUS debug logs on both the MikroTik (`/system logging add topics=radius action=memory`) and RADIUS server. This is very useful in pinpointing the reason for failure.
        *   Ensure that the RADIUS server has the correct user configuration - in this case, the MAC address of the connecting devices.
        *  Verify that the RADIUS server is properly configured for MAC address authentication.
*   **Incorrect Service Type:**
    *   **Problem:** Not all RADIUS services can use MAC address authentication on bridges.
    *   **Solution:** Ensure that you are using a RADIUS service that is supported by MAC authentication on the bridge.
*   **High CPU/Memory Usage:**
    *   **Problem:** Increased authentication load leads to high resource consumption.
    *   **Solution:** Monitor CPU and RAM usage (`/system resource print`). Optimize RADIUS server settings if necessary. It is not likely on a SOHO setup that this would be an issue, however, in larger scale setups this should be carefully considered.
*   **Incorrect MAC Address:**
    *   **Problem:** The MAC address is not being received correctly, for instance in a VLAN situation.
    *  **Solution:** Verify the MAC address being sent to the RADIUS server using logging on the MikroTik or RADIUS server. If this does not match the client's MAC address, then the bridge is not using the correct MAC address.

## Verification and Testing Steps:

1.  **Enable RADIUS Logging:** Add the topic `radius` to memory for logging for debugging purposes:

    ```mikrotik
    /system logging add topics=radius action=memory
    ```

2. **Connect a client to `bridge-58`:** Connect a client device to the network connected to the `ether1` interface.

3.  **Monitor Logs:** Watch the MikroTik logs (`/log print`) for RADIUS authentication attempts when a client connects to the bridge. You will see authentication attempts and whether they were successful or not.
    ```mikrotik
    /log print where topics~"radius"
    ```

4.  **Check Client IP Assignment:** If authentication is successful, the client should receive an IP address in the `219.113.174.0/24` subnet from the MikroTik DHCP server. You can use the ping command to verify connectivity.
    ```mikrotik
    /ping 219.113.174.1
    ```

5.  **Test from the client device:** Ping an address such as `8.8.8.8` from the client to verify internet access.

## Related Features and Considerations:

*   **Hotspot:** You could combine this setup with a Hotspot for more advanced user authentication management, including custom login pages, different user profiles, and usage limits. The RADIUS configuration would need to be adapted to handle the Hotspot feature.
*   **VLANs:** This setup can work with VLANs if the bridge is VLAN-aware. Ensure that you are using the correct VLAN ID and tagged ports in your setup. You should ensure the RADIUS server receives and handles the VLAN tag correctly.
*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy and load balancing. Ensure that the first server is reachable to avoid timeouts.
*   **Accounting:** You should also configure the RADIUS server to handle accounting information for resource tracking.
*   **Certificate-Based Authentication:** If the RADIUS server supports certificate-based authentication, consider it for enhanced security. This can include a server and client certificate.
*   **DHCP Server:** Ensure DHCP is set up on the `bridge-58` interface if not already configured.
    ```mikrotik
    /ip dhcp-server add address-pool=default interface=bridge-58 name=dhcp1
    /ip dhcp-server network add address=219.113.174.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=219.113.174.1
    ```

## MikroTik REST API Examples:

Unfortunately, configuring MAC address authentication directly via the REST API for bridge settings is not directly supported. However, you can manage RADIUS server settings via the API.

**Example: Adding a RADIUS Server:**

*   **API Endpoint:** `/radius`
*   **Request Method:** `POST`
*   **Example JSON Payload:**

    ```json
    {
      "address": "192.168.88.100",
      "secret": "radiussecret",
      "service": "ppp,login,hotspot",
      "timeout": "3s"
    }
    ```

*   **Example cURL Request:**
   ```bash
    curl -k -H "Content-Type: application/json" \
    -X POST \
    -d '{
        "address": "192.168.88.100",
        "secret": "radiussecret",
        "service": "ppp,login,hotspot",
        "timeout": "3s"
        }' \
    https://<your-router-ip>/rest/radius
    ```
*   **Expected Response (Successful):** `201 Created` and a JSON representation of the newly created RADIUS server object.

**Example: Getting a list of RADIUS Servers**
*   **API Endpoint:** `/radius`
*   **Request Method:** `GET`
*   **Example cURL Request:**
    ```bash
    curl -k https://<your-router-ip>/rest/radius
    ```
*   **Expected Response (Successful):** `200 OK` and an array of JSON objects representing the RADIUS server settings.

**Example: Handling errors:**
If, for example, the RADIUS address is already configured, the response will be a `409 Conflict` error. You should look for and check the error codes returned from the api, and handle the errors correctly. The error output will be descriptive of the issue in a JSON output.

**Note**:
*   Replace `<your-router-ip>` with the IP address of your MikroTik router.
*  You may require to enable the API service on your MikroTik Router first.
*   The API requires authentication (you might need to set up a user with API access).
*   Remember to handle errors in your scripts or applications that use the API.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a strong, unique secret for RADIUS communication. Do not use the default secrets.
*   **Restrict Access:** Limit network access to the RADIUS server.
*   **Monitor Logs:** Regularly review RADIUS logs for unauthorized access attempts.
*   **Secure API Access:** Enable HTTPS for API access and use strong authentication for API users.
*   **Regular Updates:** Keep your MikroTik RouterOS and RADIUS server software updated to patch any known vulnerabilities.
*   **Change Default Passwords:** Always change default user passwords on the MikroTik router.
*   **Disable Unused Services:** Only enable services that are needed to reduce the attack surface.

## Self Critique and Improvements:

*   **Limited Customization:** The current configuration is very basic and assumes a simple network setup.
*  **Error Handling:** More detailed error handling on the API examples.
*  **User Administration:** It would be preferable to use a dedicated user administration tool.
*   **Scalability:** The configuration is not designed for very large networks, and scaling may require additional optimization.
*   **Logging:** More comprehensive logging could be implemented.
*   **GUI Configuration:** It is important to note how to configure the setting using the GUI as well as the CLI.

**Improvements:**
*   Implement accounting to track usage and for billing purposes.
*   Set up more sophisticated logging for security and debugging purposes.
*   Set up a more comprehensive user administration, for example using the MikroTik user manager.
*   Explore more advanced RADIUS attributes such as VLANs, QoS, and traffic shaping.
*   Use the REST API to automate the configuration.
*   Create a script for backup and restoration.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**
RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for network access. It allows a centralized server to manage users, grant access to network resources, and track usage, rather than having authentication mechanisms local to the device.

**Key Concepts:**

*   **Authentication:** Verifying the identity of a user or device attempting to access the network (e.g., username and password).
*   **Authorization:** Determining the permissions of the authenticated user/device (e.g., what network resources they can access).
*   **Accounting:** Tracking the network usage by the user/device, e.g., time used, and traffic volume.
*   **RADIUS Client:** A network device (like a MikroTik router) that forwards access requests to the RADIUS server.
*   **RADIUS Server:** A centralized server that manages authentication and authorization decisions.
*   **Shared Secret:** A key used to encrypt the communication between the RADIUS client and server. This secret must be identical on both.

**How it works:**

1.  When a user/device connects, the client device sends an authentication request (containing username, password) to the RADIUS server.
2.  The RADIUS server verifies the credentials.
3.  If the authentication is successful, the server returns an accept message with authorized access parameters.
4.  During the network session, the RADIUS server may track usage through accounting messages.
5.  The user/device can access the authorized resources until the session expires or the connection is terminated.

## Detailed Explanation of Trade-offs:

**Local Authentication vs. RADIUS:**

*   **Local Authentication (e.g., MikroTik users):**
    *   **Pros:** Simpler to configure for small setups. No external server required.
    *   **Cons:** Difficult to manage large numbers of users. Limited central control. Lacks accounting capabilities.
*   **RADIUS Authentication:**
    *   **Pros:** Centralized management. More scalable, suitable for larger networks. Better accounting.
    *   **Cons:** More complex to set up. Requires a RADIUS server. Introduces a single point of failure if the RADIUS server is down.
*   **MAC Authentication vs. User Authentication:**
    * **MAC Authentication:**
        *   **Pros:**  Easy to set up for devices that don't have users (e.g., printers, IoT devices). No usernames/passwords required at the client side.
        *   **Cons:** Less secure if MAC addresses can be spoofed. Difficult to track individual users. Cannot use complex authorization or traffic shaping rules based on specific users.
    *   **User Authentication:**
        *   **Pros:** More secure. Provides better control on a per-user basis. Can enforce complex access control policies.
        *   **Cons:**  More complex setup at the client side, especially in a large network. Require a secure method of passing credentials to the client.

**Specific Trade-offs in Configuration:**

*   **`timeout=3s`:**
    *   **Trade-off:** A short timeout can cause authentication failures if the RADIUS server is slow to respond, but a long timeout increases authentication delays and can tie up router resources if RADIUS server connectivity is down.
*   **`service=ppp,login,hotspot`**:
   *   **Trade-off:** Applying the RADIUS server to the `login`, `ppp` and `hotspot` services means that it is available across all of these services. In this case, we have used MAC authentication on bridge, so it is being applied via `login`. This also means that if a Hotspot was created on the bridge, the same RADIUS server would apply. It is beneficial to configure different RADIUS server configuration for each service, if possible.

## Configuration for Specific RouterOS Versions:

This configuration is written for RouterOS 7.12 and is fully compatible with that version. Some minor variations may exist with other version of RouterOS 7, but it should operate in a similar manner. Earlier versions of RouterOS (6.48, for example), use a slightly different way of configuring interfaces, but all other RADIUS configuration elements will work.

This concludes the detailed documentation for the described RADIUS setup using MikroTik RouterOS 7.12. This setup should be suitable for small offices and home environments. Remember to adjust parameters to suit your particular needs and to always follow security best practices.
