Okay, let's dive into a detailed PPP AAA implementation on a MikroTik RouterOS 7.12 device, focusing on expert-level configuration for an ISP-like environment.

## Scenario Description:

This scenario involves setting up a MikroTik router to act as a PPP server (PPPoE or PPTP) and authenticating users via a Radius server for the subnet 43.185.222.0/24. The interface `vlan-94` will be used for termination of the PPP connections. This ensures that PPP clients are authenticated and authorized based on a centralized database. This setup is common in ISP environments for subscriber management and accounting.

## Implementation Steps:

Before we begin, please note that this implementation uses Radius as the authentication source. Therefore, you will need to have a Radius server deployed and configured to work with your MikroTik router. We will not be covering the configuration of your radius server in this documentation.

### Step 1: Prepare the Interface and IP Addressing

*   **Objective**: Assign an IP address to the `vlan-94` interface and ensure it's operational. This interface is where PPP connections will terminate.

*   **Before Configuration:**

    *   The `vlan-94` interface should exist. It might be a VLAN interface or any type of Ethernet interface.
    *   No IP address should be assigned to it.

*   **MikroTik CLI Instructions:**

    ```mikrotik
    # Check the current interfaces
    /interface print

    # Assign an IP address to vlan-94
    /ip address add address=43.185.222.1/24 interface=vlan-94

    # Check the IP address configuration
    /ip address print
    ```
*  **Winbox Instructions:**
  * Navigate to IP-> Addresses.
  * Click the `+` sign.
  * For the address field, enter `43.185.222.1/24`.
  * For the interface dropdown, select `vlan-94`.
  * Click OK

*   **Expected Result:** The `vlan-94` interface will have the IP address `43.185.222.1/24`, and be marked as enabled and operational.

### Step 2: Configure the PPP Server

*   **Objective:** Enable the PPPoE or PPTP server. Here, we'll use PPPoE for demonstration purposes.

*   **Before Configuration:**
    *   No PPP server should be configured on the interface.

*   **MikroTik CLI Instructions:**

    ```mikrotik
    # Check existing PPP server configurations
    /ppp server print

    # Enable the PPPoE server on vlan-94
    /ppp server pppoe add service-name=isp-pppoe interface=vlan-94 enabled=yes

    # Check PPP server configuration
    /ppp server print
    ```
 * **Winbox Instructions:**
    * Navigate to PPP-> PPP Server
    * Click the `+` sign and select the type of connection you want to allow. In this case, we are doing a PPPoE.
    * Fill out the service name to be `isp-pppoe`
    * Select `vlan-94` for the interface
    * Check the enabled box.
    * Click OK

*   **Expected Result:** The PPPoE server is listening on `vlan-94`.

### Step 3: Configure RADIUS Client

*   **Objective:** Add the Radius server details and enable RADIUS authentication.

*   **Before Configuration:**
    *   No RADIUS client should be configured.

*   **MikroTik CLI Instructions:**
    ```mikrotik
    # Check current radius settings
    /radius print

    # Add a radius client
    /radius add address=192.168.88.10 secret=radiussecret service=ppp timeout=30

    #Verify configuration
    /radius print
    ```

    *   **Note:** Replace `192.168.88.10` with the actual IP address of your RADIUS server and `radiussecret` with the shared secret. The `service=ppp` specifies that this Radius server will be used for PPP authentication.

 * **Winbox Instructions:**
    * Navigate to Radius
    * Click the `+` sign.
    * Fill out the address field with the IP address of your radius server `192.168.88.10`
    * Fill out the secret field with your radius shared secret. `radiussecret`
    * Select the service `ppp`
    * Click OK.

*   **Expected Result:** The MikroTik router is configured to communicate with the RADIUS server.

### Step 4: Enable RADIUS for PPP Authentication

*   **Objective:** Configure the PPP profile to use RADIUS for authentication and accounting.

*   **Before Configuration:**
    *   A default PPP profile exists or create a new one for this use case.

*   **MikroTik CLI Instructions:**

    ```mikrotik
    # Check existing PPP profiles
    /ppp profile print

    # Add a new PPP profile or Modify the default
    /ppp profile set default use-radius=yes
    
    #Verify
    /ppp profile print
    ```
 * **Winbox Instructions:**
    * Navigate to PPP-> Profiles
    * Double click the default profile
    * Check the `Use Radius` box
    * Click Ok.

    *   **Note:** Alternatively you can create a new profile and attach it to each connection as needed. For the simplicity of this demo, we will use the default.

*   **Expected Result:** All PPP connections will now be authenticated and accounted for using the Radius server configured in the last step.

## Complete Configuration Commands:

Here's a complete set of MikroTik CLI commands:

```mikrotik
# Configure vlan-94 IP address
/ip address add address=43.185.222.1/24 interface=vlan-94

# Enable PPPoE server on vlan-94
/ppp server pppoe add service-name=isp-pppoe interface=vlan-94 enabled=yes

# Add Radius Client
/radius add address=192.168.88.10 secret=radiussecret service=ppp timeout=30

# Enable Radius for PPP Authentication
/ppp profile set default use-radius=yes
```

## Common Pitfalls and Solutions:

*   **Radius Communication Issues**:
    *   **Problem**: Router cannot communicate with the radius server.
    *   **Solution**: Verify the Radius server address, secret, and firewall rules. Use tools like `torch` to analyze network traffic and the `/radius print` command to ensure the configuration is correct. Run `/tool sniffer quick interface=vlan-94 filter="port 1812 or port 1813"` to see if the packets are even reaching the interface, make sure no firewall is blocking the packets.
*   **Incorrect shared secret**:
    *   **Problem**: Clients fail to authenticate due to an incorrect shared secret
    *   **Solution**: Ensure the radius secret matches on both the router and radius server.
*   **No Profile Set**:
    * **Problem**: When setting a profile on each user, no default profile is set, leading to dropped connections.
    * **Solution**: Make sure that the default profile has `use-radius=yes`, or that your users have a profile set that has `use-radius=yes`

*   **Firewall Blocking RADIUS traffic**:
    *   **Problem**: Firewall rules might be blocking traffic to UDP ports 1812 and 1813 (the radius ports).
    *   **Solution**: Verify that your firewall allows traffic to and from the RADIUS server.
*   **Radius Server Issues**:
    *   **Problem**: The RADIUS server might be down, not functioning correctly, or not configured for PPP authentication.
    *   **Solution**: Verify the status and configuration of the RADIUS server using its logs. Ensure the server is listening on the expected ports and that the shared secret is correct.
*   **Resource Issues**:
    *   **Problem**: High CPU or memory usage due to many concurrent PPP connections, which can cause failures.
    *   **Solution**: Monitor resource usage and consider using a more powerful router if needed. Optimize firewall rules and configuration to reduce overhead. Adjust the timeouts to make them lower, this way you will get a disconnect faster.

## Verification and Testing Steps:

1.  **Connect a PPP Client:** Connect a client device to the network that supports PPPoE or PPTP (depending on what was configured), and enter the credentials that match those configured on your radius server.
2.  **Check PPP Active Connections:**

    ```mikrotik
    /ppp active print
    ```
    You should see the connected client.
3.  **Verify RADIUS Logging**: Check the RADIUS server logs for successful authentication and accounting records.
4.  **Test Network Connectivity:** Once connected, test connectivity using `ping` and `traceroute`:

    ```mikrotik
    /ping address=8.8.8.8
    /tool traceroute address=8.8.8.8
    ```
    From the PPP client device, confirm it can also reach these resources.
5.  **Traffic Monitoring:** Use `torch` to monitor the traffic going to and from the Radius server.

    ```mikrotik
    /tool torch interface=vlan-94 port=1812 or port=1813
    ```
6. **Radius Debugging**: Enable debugging on the radius server for additional context on any authentication errors or issues.

## Related Features and Considerations:

*   **PPP Profiles**: Different profiles can be assigned to users for different bandwidth limits, QoS policies, and more.
*   **Hotspot**: Combined with the Hotspot feature for more advanced user management.
*   **IP Pools**: Dynamic IP address allocation using IP pools specific to the PPP clients.
*   **Scripting**: Automation of tasks using scripts, such as dynamically adding users based on API calls or other external factors.
*   **VRFs**: Virtual Routing and Forwarding instances to separate different client networks.
*   **MPLS**: For more advanced Layer 2 and 3 services.
*   **BGP**: For peering with other networks, once the PPP clients are routed and working.

## MikroTik REST API Examples (if applicable):

Here's an example using the MikroTik API to add a PPP secret (user):

**Request:**

*   **Endpoint:** `/ppp/secret`
*   **Method:** `POST`
*   **Payload (JSON):**

```json
{
  "name": "user123",
  "password": "password123",
  "profile": "default",
  "service": "pppoe",
  "remote-address": "43.185.222.100"
}
```

**Description:**

*   `name`: The username.
*   `password`: The password.
*   `profile`: The PPP profile to use. Use `default` if you don't need one
*   `service`: Specifies the service type, in this case `pppoe`
*   `remote-address`: Sets a static IP address for this user

**Example `curl` command**

```bash
curl -k -u admin:yourpassword -H "Content-Type: application/json" -X POST -d '{"name": "user123", "password": "password123", "profile": "default", "service": "pppoe", "remote-address": "43.185.222.100"}' https://your.mikrotik.ip/rest/ppp/secret
```

**Expected Response (Success 200):**

```json
{
  ".id": "*12345",
  "name": "user123",
  "password": "password123",
  "service": "pppoe",
  "profile": "default",
  "remote-address": "43.185.222.100"
}
```

**Error Handling:**

If an error occurs, the API will return a non-200 HTTP status code. The response body will contain a JSON object describing the error. For example:

```json
{
   "message":"Couldn't add New PPP Secret - name already exists",
   "type":"ERROR"
}
```

**Note:**

*   This assumes the MikroTik API is enabled, and you have `admin` or another user with appropriate permissions.
*  The API is different from the CLI. When using the API, it will not check the radius server.

## Security Best Practices

*   **Strong Shared Secret:** Use a strong, long, and complex shared secret between the MikroTik and RADIUS server.
*   **Restrict Access to RADIUS:** Allow traffic only from trusted sources to the RADIUS server.
*   **Regular Audits:** Conduct regular security audits on the MikroTik and RADIUS configurations.
*   **Keep RouterOS Updated:** Ensure your RouterOS is running the latest version to patch known vulnerabilities.
*   **Secure API Access:** Restrict access to the MikroTik API and use strong passwords/certificates for authentication.
*   **Monitor Logs:** Monitor the logs of the MikroTik and Radius server for any unusual activity.
*   **Profile Limits:** Limit maximum sessions, data, and time limits on the profiles.
*   **Disable unused services**: disable any unneeded services for the best security.
*   **Keep the default configurations simple**.

## Self Critique and Improvements:

This implementation provides a good baseline for PPP AAA. Some improvements could include:

*   **User-Specific Profiles:** Implement per-user profiles with specific bandwidth and QoS settings for more granular control.
*   **Scripting for Dynamic User Creation**: Automate the user creation/management using custom scripts.
*   **Rate Limiting:** Implement rate limiting per user for fair usage of resources.
*   **Dynamic Accounting:** Using dynamic accounting on your radius server for more granular usage records.

## Detailed Explanations of Topic:

**PPP (Point-to-Point Protocol):** PPP is a widely used data link layer protocol for establishing a direct connection between two nodes. It provides a standard way to encapsulate data packets over a serial link. In the context of MikroTik, PPP is typically used for establishing connections with remote users or clients using protocols like PPPoE and PPTP.

**AAA (Authentication, Authorization, and Accounting):** AAA is a framework for controlling access to network resources. It consists of:

*   **Authentication:** Verifying the identity of the user or device trying to access the network. In this case, PPP clients' usernames and passwords are verified against the RADIUS server.
*   **Authorization:** Determining what resources the authenticated user is allowed to access. This is configured in RADIUS server profiles and can be used to limit bandwidth, usage, or apply specific QoS policies.
*   **Accounting:** Tracking the usage of network resources by users. The RADIUS server keeps track of session start and end times, data transferred, and other relevant data that can be used for billing and reporting.

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting management for users who connect to a network service. It typically uses UDP ports 1812 (authentication/authorization) and 1813 (accounting). MikroTik uses RADIUS to externalize the AAA process, making it easier to manage a large number of users and enforce consistent policies.

## Detailed Explanation of Trade-offs:

*   **Local Authentication vs. RADIUS:** Local authentication is simple and suitable for small setups but lacks scalability and central management. RADIUS provides scalability and centralized control but adds complexity.
*   **PPPoE vs. PPTP:** PPPoE is more secure and is generally preferred, but PPTP is simpler to set up and compatible with more devices.
*   **Static vs. Dynamic IP Addresses:** Static IP addresses provide predictability but require manual management. Dynamic IP addresses (using DHCP or IP pools) are more scalable but require management of IP address assignments.
*   **Default Profile vs. Per-User Profiles:** Using a default profile is simple but does not allow for granular user management. Per-user profiles provide fine-grained control but require more setup and configuration.

## Configuration for Specific RouterOS Versions:

This document targets RouterOS 7.12. All commands and features are applicable to 7.x. Note that previous versions of RouterOS may have different syntaxes for certain commands. For example, the `/ppp profile set use-radius=yes` command would have been configured differently in version 6.x. For version 6.48 you would have to set `/ppp secret set use-radius=yes`, so you would have to use an approach of creating multiple users or a single user to test the radius. Be sure to always reference the official Mikrotik documentation for all commands on all versions.

By following these steps and explanations, you can implement a robust and scalable PPP AAA solution on your MikroTik router, and have a good understanding of how and why it works. Remember to thoroughly test and monitor your configuration after implementation. If you have any further questions or require more detail on any of these topics, please let me know.
