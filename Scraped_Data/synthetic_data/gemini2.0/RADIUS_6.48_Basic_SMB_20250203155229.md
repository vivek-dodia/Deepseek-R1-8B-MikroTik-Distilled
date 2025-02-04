Okay, let's craft some detailed documentation on RADIUS configuration for MikroTik RouterOS v6.48, targeting an SMB environment and utilizing the `wlan-2` interface within the subnet `180.229.142.0/24`.

## Scenario Description:

This scenario involves configuring a MikroTik router to authenticate wireless clients connecting to the `wlan-2` interface using a RADIUS server. This setup will provide centralized authentication and authorization for wireless access, allowing for more granular control over user access. We assume the RADIUS server is already set up and reachable from the MikroTik device. This is common in small to medium businesses, where a dedicated RADIUS server (such as FreeRADIUS or a cloud-based solution) manages user authentication for various services.

## Implementation Steps:

**Note:** We will use CLI examples primarily, but also mention the equivalent steps using Winbox.

**1. Step 1: Prepare the Wireless Interface**

*   **Before Configuration:** Check the status of the `wlan-2` interface.

    ```mikrotik
    /interface wireless print
    ```

    You should see the `wlan-2` interface listed. Note its current configuration.

*   **Configuration:** Ensure `wlan-2` is enabled and configured with a suitable SSID, band, and mode. This step is specific to your wireless infrastructure needs. For this example, we assume a basic setup and the `wlan-2` is enabled. If not, activate it with the command below:

    ```mikrotik
    /interface wireless enable wlan-2
    ```
    *  **winbox** use the `/Interfaces` window and click on `wlan2` and enable it if is not already.
* **After Configuration:** Verify the status of the `wlan-2` interface with same `/interface wireless print` command. It should indicate that the interface is enabled.

**2. Step 2: Add RADIUS Server Configuration**

*   **Before Configuration:** No RADIUS server is configured by default, so no pre-existing RADIUS entries in `/radius` are expected
    ```mikrotik
     /radius print
    ```
    This command should not return any records.
*   **Configuration:** Add the RADIUS server information using `/radius add`.

    ```mikrotik
    /radius add address=192.168.10.10 secret="supersecret" service=wireless timeout=3
    ```
    *  `address`: IP address of the RADIUS server (replace with your actual RADIUS server IP).
    *   `secret`: Shared secret configured on the RADIUS server (replace with your actual secret).
    *   `service`: Specifies that this RADIUS server is for wireless authentication.
    *  `timeout`: specifies how long the router will try to reach a server before failing over to the next one on the list, or failing completely.

*   **Winbox**: Go to `/Radius` and add a new record. Configure the parameters accordingly in the `New Radius Server` window and click `OK`.
*   **After Configuration:** Verify the RADIUS server configuration.

    ```mikrotik
    /radius print
    ```

    You should see the added RADIUS server details printed.

**3. Step 3: Configure Wireless Security for RADIUS**

*   **Before Configuration:** The wireless security profile is most likely using a basic WPA2 key.
*   **Configuration:** Modify the wireless security profile used by `wlan-2` to use WPA2 Enterprise and specify the previously configured RADIUS server using `/interface wireless security-profiles`. Assuming you have only one profile, edit that profile, if you have more than one, change the one associated with the wireless interface `wlan-2`.
    ```mikrotik
    /interface wireless security-profiles set [ find default=yes ] authentication-types=wpa2-eap mode=dynamic-keys eap-methods=passthrough radius-accounting=yes radius-mac-format=XX:XX:XX:XX:XX:XX
    ```
    *   `authentication-types=wpa2-eap`: Enables WPA2 Enterprise authentication.
    *   `mode=dynamic-keys`: Uses dynamically generated keys.
    *   `eap-methods=passthrough`: Allows for any EAP method from the client
    *  `radius-accounting=yes`: Enables accounting for the radius service.
    *  `radius-mac-format`: Sets the format of the calling station id to a standard MAC format.

*   **Winbox**: Go to `/Interface/Wireless` window and open the wireless interface `wlan-2` double click it, go to the tab `Wireless` and from the `Security Profile` dropdown menu, select the profile you want to modify, then open the profile from the `Security Profiles` window, configure the settings described above and click `OK`.
*   **After Configuration:** Verify the security profile settings.
    ```mikrotik
    /interface wireless security-profiles print
    ```
    The profile you just modified must have the settings configured before.

**4. Step 4: Apply the Security Profile to the Interface**
*   **Before Configuration:** The wireless interface `wlan-2` is likely using a security profile with a static key or no encryption.
*   **Configuration:** Apply the newly configured security profile to the wireless interface using `/interface wireless set`. Let's assume the security profile you have modified is called `default`
    ```mikrotik
    /interface wireless set wlan-2 security-profile=default
    ```
*   **Winbox:** In the `/Interface/Wireless` window double click on the `wlan-2` interface and in the `Wireless` tab, select the security profile you modified before from the dropdown menu `Security Profile` and click `OK`
*   **After Configuration:** Verify the changes by printing the interface configuration.
    ```mikrotik
    /interface wireless print
    ```
    The `security-profile` for the `wlan-2` interface should be the profile you have modified.

## Complete Configuration Commands:

```mikrotik
# Enable the wireless interface wlan-2 (if it is not already enabled)
/interface wireless enable wlan-2

# Add the RADIUS server
/radius add address=192.168.10.10 secret="supersecret" service=wireless timeout=3

# Configure the wireless security profile to use RADIUS
/interface wireless security-profiles set [ find default=yes ] authentication-types=wpa2-eap mode=dynamic-keys eap-methods=passthrough radius-accounting=yes radius-mac-format=XX:XX:XX:XX:XX:XX

# Apply the security profile to the interface wlan-2
/interface wireless set wlan-2 security-profile=default

# Print current configuration for verifications
/radius print
/interface wireless print
/interface wireless security-profiles print
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot reach the RADIUS server (e.g., incorrect IP address or firewall issues).
    *   **Solution:** Verify the IP address of the RADIUS server and check for firewall rules blocking communication on both the MikroTik and the RADIUS server. Use `ping` or `traceroute` from the MikroTik to the RADIUS server address. Use `/tool torch` to monitor the traffic to and from the RADIUS server. Ensure that the RADIUS server is listening on the UDP port 1812 and 1813 by default.

*   **Incorrect Shared Secret:**
    *   **Problem:** The shared secret configured on the MikroTik does not match the secret on the RADIUS server.
    *   **Solution:** Double-check and ensure the shared secret is exactly the same on both devices. The secret must match exactly, including capitalization.

*   **EAP Configuration Mismatch:**
    *   **Problem:** The EAP methods configured on the client or RADIUS server don't match the MikroTik's settings (e.g., client attempting PAP while the RADIUS requires EAP-TLS).
    *   **Solution:** Ensure that the client device and RADIUS server are using compatible EAP methods, and the correct configuration is in place in the MikroTik device. You can use `/log` to see if there are EAP error messages. Consider allowing `passthrough` EAP methods.

*   **Wireless Interface Issues:**
    *   **Problem:** The wireless interface is not enabled or configured correctly.
    *   **Solution:** Ensure that the `wlan-2` interface is enabled and configured with the correct SSID, band, and mode. Verify that the `frequency` and other wireless settings are configured correctly.

* **Accounting Issues**
    * **Problem:** The RADIUS accounting service is not working, or the accounting packets are not reaching the server.
    * **Solution:** Check that the RADIUS server can receive accounting messages from the router. Verify the shared secret is the same on both sides. Use `/tool torch` to monitor traffic to and from the RADIUS server on port 1813.

*   **Resource Issues:**
    *   **Problem:** High CPU or memory usage on the MikroTik.
    *   **Solution:** Monitor the MikroTik’s resource usage using `/system resource monitor` and `/system resource print`. If usage is high, consider upgrading the hardware or optimizing the router’s configuration. This is usually not an issue on the implementation described in this document.

## Verification and Testing Steps:

1.  **Connect a Wireless Client:** Attempt to connect to the `wlan-2` SSID from a wireless device.
2.  **Check RADIUS Logs:** Examine the logs on the RADIUS server to confirm that the authentication request is received and processed. Check if the client is correctly authorized on the RADIUS server.
3.  **MikroTik Logs:** Check the MikroTik logs ( `/log print topics=radius`) for successful or failed authentication attempts.
4.  **Monitor Torch:** Use `/tool torch interface=wlan-2 protocol=udp port=1812,1813` to monitor traffic going to and from the RADIUS server.
5.  **Ping from Wireless Client:** After successful authentication, try to ping another device on the same network to confirm IP address assignment and connectivity.
6.  **MikroTik Connection Monitoring:** Check the `/interface wireless registration-table print` to see clients and their connection status.
7. **RADIUS Server Tools:** Many RADIUS servers have tools to monitor live requests and responses. Use them to verify the correct operation.

## Related Features and Considerations:

*   **RADIUS Accounting:** Enable RADIUS accounting to track user session data (start, stop, data usage). This is already enabled in our example.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy by adding them with different priorities. The lower the `timeout` value, the higher the priority.
*   **MAC Address Filtering:** Use MikroTik’s Access List to filter clients based on their MAC addresses, in addition to RADIUS authentication.
*   **User Profiles:** Configure user profiles on the RADIUS server to provide different access levels and bandwidth limits.
*   **VLANs:** Assign users to VLANs based on their RADIUS authentication for network segmentation.
* **Hotspot** The MikroTik can be configured as a hotspot gateway, where users can authenticate using a web browser.

## MikroTik REST API Examples:

MikroTik RouterOS v6.48 does not have a comprehensive REST API. While there is a `/rest` endpoint, it's limited and not practical for many operations. For more complex configurations, use the MikroTik API instead. For this exercise, we will assume a newer router OS to show an example API configuration. These API calls are only available on modern RouterOS releases and are not present on the target version.

**Example: Adding a RADIUS Server using REST API**

*   **Endpoint:** `/radius`
*   **Method:** POST
*   **JSON Payload:**

    ```json
    {
    "address": "192.168.10.10",
    "secret": "supersecret",
    "service": "wireless",
        "timeout": 3
    }
    ```
*   **Expected Response (201 Created):**
     ```json
     {
         ".id": "*1234",
         "address": "192.168.10.10",
         "secret": "supersecret",
         "service": "wireless",
        "timeout": 3
     }
     ```
*   **Error Handling:**
    *   If a mandatory field is missing (e.g., "address"), you will get a 400 Bad Request error.
    *   If the provided `service` does not exist, the API will return a 400 Bad Request error.
    *   If the address is not in a valid format, the API will return a 400 Bad Request error.
    *   If the secret is too short, the API will return a 400 Bad Request error.
     *   If the `timeout` parameter is not a valid number, the API will return a 400 Bad Request error.

**Example:  Modifying a RADIUS Server using REST API**

*   **Endpoint:** `/radius/{.id}` replace `{.id}` with the `.id` that was returned by the first example.
*   **Method:** PUT
*   **JSON Payload:**

    ```json
    {
       "secret": "newsecret",
       "timeout": 5
    }
    ```
*   **Expected Response (200 OK):**
     ```json
     {
         ".id": "*1234",
         "address": "192.168.10.10",
         "secret": "newsecret",
         "service": "wireless",
        "timeout": 5
     }
     ```
*   **Error Handling:**
    *   If a mandatory field is missing, you will get a 400 Bad Request error.
    *   If the provided `.id` does not exist, the API will return a 404 Not found error.
    *   If the `timeout` parameter is not a valid number, the API will return a 400 Bad Request error.

**Note:** Ensure that the REST API is enabled on your MikroTik router and you have a valid user with API access to execute the above commands.  This feature is generally more complex to enable and secure, and it is not covered in this scenario description.

## Security Best Practices:

*   **Use a Strong Shared Secret:** The shared secret should be complex and long. Use a random password generator.
*   **Secure RADIUS Server:** Ensure your RADIUS server is protected from unauthorized access and is regularly updated. Limit access to the RADIUS server to the devices that need it.
*   **Firewall Rules:** Implement proper firewall rules on both the MikroTik and the RADIUS server to prevent unauthorized access.
*   **Regular Updates:** Keep your RouterOS and RADIUS server software updated with the latest security patches.
* **Avoid Default Ports:** If possible, do not use default ports for the RADIUS service.
* **Use RADIUS over TLS (radsec):** When possible, use RADIUS over TLS to encrypt traffic to and from the RADIUS server. This is not common, and it is usually unnecessary for internal use, but if your RADIUS server is accessible over the internet, or the client data is very sensitive, consider using it.
*   **Monitor Logs:** Regularly monitor the MikroTik and RADIUS server logs for suspicious activities.

## Self Critique and Improvements:

This configuration provides a basic setup for RADIUS authentication on a MikroTik router. Some potential improvements and considerations are:

*   **Advanced EAP Methods:** We only configured `passthrough` EAP methods. Consider limiting the acceptable EAP methods for better security. If you have the option, use EAP-TLS with certificates instead of password-based authentication methods.
*   **VLAN Tagging:** Implement VLAN tagging to segment traffic based on user roles for enhanced network security.
*   **Dynamic Authorization (CoA):** Implement dynamic authorization through Change of Authorization (CoA) messages for real-time updates to user permissions.
* **Error Handling**: The example in this documentation did not focus in specific error handling. When implementing this in a real system, try to catch specific error messages, like the radius server being unreachable, authentication errors, etc.
* **Redundancy:** This example does not show how to use redundancy. If the Radius server goes down, the devices will not be able to connect. Consider using more than one radius server, so if one fails, the others will continue to function.
*   **Monitoring:** This configuration does not include monitoring with SNMP or other tools, but it would be an enhancement to allow more information to be retrieved about the state of the router, its connections and RADIUS authentications.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network.

*   **Authentication:** Verifies the identity of a user attempting to access a network resource (username and password, certificates, etc.).
*   **Authorization:** Determines what a user is allowed to do on the network after they have authenticated (network access, VLAN assignment, etc.).
*   **Accounting:** Tracks the network resources a user has consumed (session time, data usage).

In a typical setup, a network access server (NAS), like the MikroTik router, communicates with the RADIUS server. When a client attempts to connect, the NAS forwards the authentication request to the RADIUS server. The RADIUS server verifies the credentials, grants or denies access, and sends the response back to the NAS. This centralized approach makes managing user access more efficient and secure than managing individual users on the NAS itself.

## Detailed Explanation of Trade-offs:

*   **Static WPA2 Key vs. RADIUS:**
    *   **Static WPA2:** Easy to set up, but less secure and harder to manage for a large number of users. All users share the same password, and if the password is compromised, all users are affected.
    *   **RADIUS:** More secure and manageable, allowing granular control over user access. Requires a RADIUS server infrastructure. The initial configuration is more complex, but it is more secure.

*   **EAP-TLS vs. Password-based EAP:**
    *   **EAP-TLS:** The most secure EAP method, as it uses certificates for mutual authentication. Requires PKI infrastructure (Certificate Authority, client certificates). This is the preferred option, but it's more difficult to implement.
    *   **Password-based EAP:** Easier to deploy but less secure. Passwords can be stolen or guessed. EAP-TTLS and PEAP are less secure than EAP-TLS but easier to implement.

*   **Centralized vs. Decentralized Management:**
    *   **Centralized (RADIUS):** Easier to manage multiple users and devices from a central point. Requires a RADIUS server and network connectivity.
    *   **Decentralized (Local Users):** Simple and suitable for small networks, but less scalable and harder to manage with an increasing number of users. No external server is required.

* **Accounting:**
    * **Enabled:** Provides useful data about user sessions, that can be used for accounting or data analysis.
    * **Disabled:** Simpler setup, with less information about user sessions. The overhead of processing the accounting is avoided, but no useful information about sessions can be gathered.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeted at RouterOS v6.48.  While it should mostly work on later versions, some new features (like the REST API examples shown above) might not be available on this particular version. Be aware that some of the commands may have slightly different syntaxes or may not be available in older versions. In general, the commands provided should be compatible with 6.48 and above. Always consult the MikroTik RouterOS documentation for your specific version. For example, on later versions of routerOS, the configuration command `security-profiles` has changed significantly.

Let me know if you have any further questions or require adjustments!
