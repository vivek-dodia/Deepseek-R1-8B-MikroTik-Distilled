Okay, let's dive into configuring PPP AAA on a MikroTik router running RouterOS 6.48, focusing on a Hotspot network scenario. This configuration will specifically use RADIUS for authentication, accounting, and authorization (AAA) over our specified interface and subnet.

## Scenario Description:

We have a Hotspot network using interface `wlan-75`, operating on the subnet `239.181.159.0/24`. We will be implementing PPP (Point-to-Point Protocol) AAA using RADIUS to centralize user authentication, accounting, and authorization for any clients connecting via a PPP tunnel on this network. This configuration ensures that users must authenticate against a RADIUS server before they can access the network through a PPP connection. This is useful for managing user access, monitoring usage, and enhancing security for the hotspot network.

## Implementation Steps:

### Step 1: Configure RADIUS Server Information

*   **Explanation:** We first define the RADIUS server details, including its IP address, secret, port, and service type, which is `ppp` in this case.
*   **CLI Command Example (Before):**

    ```mikrotik
    /radius print
    # No radius config currently
    ```
*   **CLI Command Example (After):**

    ```mikrotik
    /radius add address=192.168.88.100 secret=your_radius_secret service=ppp timeout=10
    ```
    *   `address=192.168.88.100`: Specifies the IP address of the RADIUS server. Replace with your actual RADIUS server IP.
    *   `secret=your_radius_secret`:  The shared secret key used to authenticate between the router and RADIUS server. This should match the secret configured on the RADIUS server.
    *   `service=ppp`: Specifies that this RADIUS configuration is for PPP connections.
    *    `timeout=10`: Specifies the timeout in seconds that the RouterOS will wait for a response from the RADIUS server.
*   **Effect:** This step adds the RADIUS server information to RouterOS. The router will now know where to send authentication, accounting, and authorization requests for PPP users.
*   **Winbox GUI:**
    * Go to: `Radius`.
    * Click the `+` button to add a new RADIUS configuration.
    * Enter the `address`, `secret`, and choose `ppp` from the `service` dropdown.
    * Click `OK`.

### Step 2: Configure PPP Profile

*   **Explanation:** Now we create a PPP profile that will use RADIUS for authentication. The profile defines PPP settings that will be assigned to connected clients.
*   **CLI Command Example (Before):**

    ```mikrotik
    /ppp profile print
    # No profiles set
    ```
*   **CLI Command Example (After):**

    ```mikrotik
    /ppp profile add name=radius_ppp use-encryption=yes only-one=no local-address=239.181.159.1 remote-address=239.181.159.2-239.181.159.254  use-radius=yes
    ```
    *   `name=radius_ppp`: Name of the profile.
    *   `use-encryption=yes`: Requires encryption for PPP connections.
    *    `only-one=no`: Allows multiple PPP sessions using this profile.
    *    `local-address=239.181.159.1`:  IP address of the router for the PPP tunnel.
    *   `remote-address=239.181.159.2-239.181.159.254`: The IP address range that will be assigned to connected clients.
    *   `use-radius=yes`: Indicates that this profile will use RADIUS authentication.
*   **Effect:** The router has a new profile for PPP connections that uses RADIUS. Any PPP connection using this profile will go through RADIUS for user validation.
*  **Winbox GUI:**
    * Go to: `PPP` -> `Profiles`
    * Click the `+` button to add a new profile.
    * Name the profile `radius_ppp`.
    * Check `Use Encryption`.
    *  Set `Local Address` to `239.181.159.1`.
    * Set `Remote Address` to `239.181.159.2-239.181.159.254`.
    * Check the box `Use Radius`.
    * Click `OK`.

### Step 3: Configure PPP Secret and Link to Profile

*   **Explanation:** Finally, we set up a PPP secret that utilizes the RADIUS authentication, but we are not going to use the router's internal secrets. We only want authentication through RADIUS server.
*   **CLI Command Example (Before):**
    ```mikrotik
    /ppp secret print
    # No ppp secrets
    ```
*   **CLI Command Example (After):**

    ```mikrotik
    /ppp secret add service=pptp profile=radius_ppp
    ```
    * `service=pptp`: Specifies the service (PPTP/L2TP/etc) for this secret.
    * `profile=radius_ppp`: Assigns the secret to our RADIUS-enabled profile. Note that no password is set since we will be using RADIUS server.
*   **Effect:** Now, when a user connects via PPTP to the MikroTik, their username/password will be passed to the configured RADIUS server for authentication.
*   **Winbox GUI:**
    * Go to: `PPP` -> `Secrets`
    * Click the `+` button to add a new secret.
    * Leave the `Name` blank. We are using RADIUS for authentication, so local secrets are not used.
    * Select the correct `service` i.e., `pptp`.
    * Choose the `profile` from the dropdown i.e., `radius_ppp`.
    * Click `OK`.

### Step 4: Configure the Interface

*  **Explanation:** Ensure your interface has an appropriate IP address.  If using the interface to service a hotspot network, then a DHCP server on the subnet may be appropriate.
* **CLI Example (Before)**
```mikrotik
/ip address print
# no ip address on wlan-75
```
*   **CLI Example (After)**

```mikrotik
/ip address add address=239.181.159.1/24 interface=wlan-75
```
*   `address=239.181.159.1/24`: Set the interface's IP address and subnet.
*   `interface=wlan-75`: Apply the IP address on the `wlan-75` interface.
*   **Effect:**  The router's wlan-75 interface is now assigned an IP address, and can provide connectivity on the 239.181.159.0/24 network.
*  **Winbox GUI:**
    * Go to: `IP` -> `Addresses`
    * Click the `+` button to add a new address
    * Set the `address` to `239.181.159.1/24`.
    * Choose the correct interface from the dropdown `wlan-75`
    * Click `OK`.
### Step 5: Configure PPTP Server
*   **Explanation:** Enable the PPTP server on the MikroTik router to allow clients to make PPP connections.
*   **CLI Example (Before)**

```mikrotik
/ppp server pptp print
# pptp server disabled
```

*   **CLI Example (After)**

```mikrotik
/ppp server pptp set enabled=yes default-profile=radius_ppp
```
*   `enabled=yes`: Enables the PPTP server.
*   `default-profile=radius_ppp`: Sets the default PPP profile to be used for connections to this server to the one defined earlier.
*   **Effect:** The router is now ready to receive PPTP connections and will apply the given profile for authentication.
*  **Winbox GUI:**
    * Go to: `PPP` -> `Interface`
    * Check the `Enabled` box on the `pptp-server` entry.
    * Set the `Default Profile` to `radius_ppp`.
    * Click `OK`.
## Complete Configuration Commands:

```mikrotik
/radius add address=192.168.88.100 secret=your_radius_secret service=ppp timeout=10
/ppp profile add name=radius_ppp use-encryption=yes only-one=no local-address=239.181.159.1 remote-address=239.181.159.2-239.181.159.254  use-radius=yes
/ppp secret add service=pptp profile=radius_ppp
/ip address add address=239.181.159.1/24 interface=wlan-75
/ppp server pptp set enabled=yes default-profile=radius_ppp
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot communicate with the RADIUS server.
    *   **Solution:** Double-check the RADIUS server IP address, shared secret, and firewall rules. Use `ping` from the MikroTik to the RADIUS server to verify connectivity. Verify RADIUS service is running on the server.
*   **Incorrect RADIUS Secret:**
    *   **Problem:**  The shared secret on the MikroTik does not match the secret on the RADIUS server, or was entered incorrectly.
    *   **Solution:** Ensure the `secret` matches exactly.
*  **Firewall Issues:**
    * **Problem:** Firewall rules on either the MikroTik, or on an intermediary firewall prevent the router from sending/receiving RADIUS requests/responses.
    * **Solution:** Ensure firewall rules permit UDP traffic from the MikroTik to port 1812/1813 (or custom RADIUS ports) on the RADIUS server.
*  **RADIUS Server Not Configured Correctly:**
    * **Problem:** The RADIUS server itself may not be configured correctly for the `service=ppp`.
    * **Solution:** Verify the RADIUS server configuration to ensure it is set to authenticate PPP connections using the shared secret and that it is set to accept requests from the router's IP address.
*   **PPP Profile Mismatch:**
    *   **Problem:** The client may not be using the correct profile when connecting to the PPTP server on the MikroTik.
    *   **Solution:** Double-check the profile specified on the client.

## Verification and Testing Steps:

1.  **Ping Test:** From a client on the `239.181.159.0/24` network, try to ping the MikroTik's IP address of `239.181.159.1`. If it fails, there may be issues with the L2 connectivity.
2.  **PPP Connection Attempt:**
    *   Attempt a PPTP connection from a client (e.g., using Windows' built-in VPN client, a smartphone, or similar device) to the MikroTik's public IP or interface address.
    *   Use a valid username and password configured on the RADIUS server.
3.  **Monitor Logs:** Observe the MikroTik logs for RADIUS authentication and accounting messages.
    *   **CLI Command:** `/log print topics=radius,ppp`
    *   **Expected Outcome:** Logs should show successful authentication or the reason for failed attempts.
4.  **RADIUS Server Logs:** Check the logs of your RADIUS server to see the request received and response sent, which is useful for debugging any problems with the user authentication.
5.  **Interface Activity:** Monitor the `wlan-75` interface traffic using `/interface monitor wlan-75`. Ensure traffic is flowing as expected.
6.  **Torch:** Use `/tool torch interface=wlan-75` to monitor network traffic on the interface.

## Related Features and Considerations:

*   **Hotspot Features:** Integrate this PPP configuration with RouterOS hotspot functionality for a more comprehensive user access management system.
*  **IPsec Tunnels:** Combine with IPsec to establish a VPN with the router and encapsulate your PPP connections for enhanced security.
*   **User Profiles and Bandwidth Management:** Use the RADIUS server to assign specific user profiles and bandwidth limits, or implement QoS on the router.
*   **VPN Types:** Use L2TP or SSTP for a more robust and secure VPN protocol for remote access.
*   **Accounting Logs:** Configure the RADIUS server to send accounting information to a database or other monitoring platform.

## MikroTik REST API Examples:

While not the primary use case for the API, creating and updating PPP secrets or RADIUS servers can be done through the REST API. Let's create a radius configuration with the API.

**API Endpoint:** `/radius`
**Request Method:** `POST`
**JSON Payload:**

```json
{
  "address": "192.168.88.101",
  "secret": "new_radius_secret",
  "service": "ppp",
  "timeout": 5
}
```
*   **address:** IP address of the RADIUS server.
*   **secret:**  Shared secret between the router and RADIUS server.
*   **service:** Specifies the service the radius server is for, `ppp`.
*   **timeout:**  The timeout for how long to wait for a response from the RADIUS server.
**Expected Response:**

```json
{
    "message": "added",
    ".id": "*1"
}
```

**Error Handling:**

If any parameter is missing or incorrect, or a connection to the API cannot be made, the response will be an error. Example:

```json
{
    "message": "input does not match required type",
    "details": {
        "secret": "value is required"
     }
}
```

**Retrieving the list of configured radius servers:**

**API Endpoint:** `/radius`
**Request Method:** `GET`
**JSON Payload:** None
**Expected Response:**
```json
[
    {
        ".id": "*1",
        "address": "192.168.88.101",
        "secret": "new_radius_secret",
        "service": "ppp",
        "timeout": "5",
        "comment": ""
    }
]
```
## Security Best Practices:

*   **Strong RADIUS Secret:** Always use strong and long shared secrets for the RADIUS server.
*   **Secure RADIUS Communication:** Consider using RADIUS over IPSec to prevent man-in-the-middle attacks.
*   **Access Control:** Restrict access to the RADIUS server to only the MikroTik routers that need to access it.
*   **Regular Updates:** Keep the RouterOS software updated with the latest security patches.
*   **Strong Passwords for MikroTik:** Use complex passwords for the MikroTik router and do not use the default password.

## Self Critique and Improvements:

*   **Scalability:** This setup works well for a small to medium network. For larger scale networks a dedicated RADIUS server with more options (such as MySQL backend) is recommended.
*   **Error Handling:** We should set some timeout and retry parameters on the client side connection for added robustness.
*  **Accounting:** Add accounting functionality with the RADIUS server. Accounting can provide valuable usage data for analysis.
*   **Logging:** Add logging capabilities, such as logging to syslog server, to enhance the monitoring and troubleshooting process.
*  **Dynamic IP Assignment:** The current remote IP address assignment is statically defined. A better solution would be to use a radius server that assigns IP addresses dynamically based on the user.

## Detailed Explanations of Topic:

*   **PPP (Point-to-Point Protocol):** PPP is a network protocol used to establish a direct connection between two nodes. In our context, it is used to connect clients to the MikroTik router.
*  **AAA (Authentication, Authorization, and Accounting):** AAA is a framework for securing access to a network.
    *   **Authentication:** Verifies the identity of the user (e.g., username and password).
    *   **Authorization:** Determines what resources or services the authenticated user is allowed to access.
    *   **Accounting:** Tracks user activity for billing or auditing purposes.
*   **RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting for users connecting to a network. It allows the router to offload the AAA process to a dedicated server.

## Detailed Explanation of Trade-offs:

*   **Internal vs. RADIUS Authentication:**
    *   **Internal:** Easy to set up, but does not scale well and is difficult to manage across multiple devices, plus does not have a central repository for data.
    *   **RADIUS:** More complex to set up, but scales much better and is very flexible, allowing better central management of users. However, it requires more hardware, software, and expertise.
*   **PPTP vs. L2TP/IPsec:**
    *   **PPTP:** Easier to configure but less secure. Should be avoided when possible.
    *   **L2TP/IPsec:** More secure but slightly more complex to configure. Use this when you need a VPN connection that is protected against eavesdropping.
*  **Encryption:**
    *   **No Encryption:** Not recommended, and may cause data to be intercepted.
    *   **Encryption:** Secure data in transit, protecting it from eavesdropping.

## Configuration for Specific RouterOS Versions:

This configuration is primarily focused on RouterOS 6.48, but is compatible with version 7.x. Specific command features might vary slightly but the overall principle will remain the same. If using older versions, some specific parameters may be unavailable.
Let me know if you'd like to explore other aspects or different scenarios!
