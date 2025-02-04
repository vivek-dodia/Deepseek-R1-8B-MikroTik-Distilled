Okay, let's dive into configuring PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik router running RouterOS 7.11, targeting a SOHO network using the wlan-51 interface, and the 182.184.73.0/24 subnet. We will use the local user database for authentication.

## Scenario Description

This scenario involves enabling PPP AAA on the `wlan-51` interface. Clients connecting via PPP (specifically PPPoE) to this interface will be authenticated against the local user database of the MikroTik. We will setup a basic PPP profile and assign IP addresses to connected clients. Accounting for connected clients (logging), is also part of this configuration.

## Implementation Steps

Here’s a step-by-step guide, explaining each step with MikroTik CLI and Winbox GUI equivalents. We'll start from a default configuration and make the necessary changes to implement our desired setup.

**Initial State:** We will assume the router is in a default configuration, with the `wlan-51` interface enabled (and configured if needed). Ensure no conflicting configurations exist. It is a good practice to create a backup before making configuration changes.

**Winbox equivalent:** You can verify interface status and basic configuration in the `Interfaces` menu.

1.  **Step 1: Create a PPP Profile**

    *   **Purpose:** A PPP profile defines the settings for PPP connections, including IP addresses and DNS.
    *   **CLI Command:**
        ```mikrotik
        /ppp profile add name=pppoe-profile local-address=182.184.73.1 remote-address=182.184.73.2-182.184.73.254 use-encryption=yes only-one=yes
        ```
    *   **Explanation:**
        *   `add name=pppoe-profile`: Creates a new PPP profile named "pppoe-profile".
        *   `local-address=182.184.73.1`:  The IP address assigned to the router's interface.
        *   `remote-address=182.184.73.2-182.184.73.254`: The range of IP addresses to allocate to connected clients.
        *   `use-encryption=yes`: Encrypts the PPP connection.
        *   `only-one=yes`: Restricts one client to use the same username to log in at the same time.
    *   **Winbox GUI:** Navigate to `PPP` -> `Profiles` and click `Add New`. Fill in the profile settings as described.
    *   **Effect:** This creates the profile required for our PPPoE server.
    *   **Before Step 1 (Example CLI output):**
        ```mikrotik
        /ppp profile print
        Flags: * - default
        #   NAME                      CHANGE-DNS       ONLY-ONE    USE-ENCRYPTION     ADDRESS-LIST
        0   * default               no              no           no
        ```
    *   **After Step 1 (Example CLI output):**
        ```mikrotik
        /ppp profile print
        Flags: * - default
        #   NAME                      CHANGE-DNS       ONLY-ONE    USE-ENCRYPTION      LOCAL-ADDRESS    REMOTE-ADDRESS       ADDRESS-LIST
        0   * default               no              no           no
        1   pppoe-profile           no              yes          yes                182.184.73.1     182.184.73.2-182.184.73.254
        ```

2.  **Step 2: Create a PPP User**

    *   **Purpose:** This creates a local user which PPP client will use for authentication.
    *   **CLI Command:**
        ```mikrotik
        /ppp secret add name=user1 password=password1 service=pppoe profile=pppoe-profile
        ```
    *   **Explanation:**
        *   `add name=user1`: Creates a user named "user1".
        *   `password=password1`: Sets the password for "user1" to "password1".
        *   `service=pppoe`: Specifies this user is for PPPoE connections.
        *   `profile=pppoe-profile`: Assigns the created profile to this user.
    *   **Winbox GUI:** Navigate to `PPP` -> `Secrets` and click `Add New`. Input username, password, service and select profile.
    *   **Effect:** Creates the PPP user which will be used by the client.
    *   **Before Step 2 (Example CLI output):**
        ```mikrotik
        /ppp secret print
        Flags: X - disabled, I - invalid
        #   NAME  SERVICE   PROFILE
        ```
    *   **After Step 2 (Example CLI output):**
         ```mikrotik
        /ppp secret print
        Flags: X - disabled, I - invalid
        #   NAME  SERVICE   PROFILE        LOCAL-ADDRESS   REMOTE-ADDRESS    LIMIT-BYTES
        0   user1 pppoe     pppoe-profile
        ```

3. **Step 3: Enable PPPoE Server on wlan-51**

   *   **Purpose:** Activates the PPPoE server on the `wlan-51` interface.
   *   **CLI Command:**
        ```mikrotik
        /interface pppoe-server server add interface=wlan-51 service-name=pppoe-server default-profile=pppoe-profile
        ```
    *   **Explanation:**
        *   `add interface=wlan-51`: Specifies the interface on which the server will listen.
        *   `service-name=pppoe-server`: Sets the name for the PPPoE service. This name will be visible to PPPoE clients.
        *   `default-profile=pppoe-profile`: Sets the default profile for incoming connection.
    *   **Winbox GUI:** Navigate to `PPP` -> `PPPoE Servers` and click `Add New`. Select `wlan-51` for the interface, name the service and select default profile.
    *   **Effect:** The router is now listening for PPPoE connections on the specified interface.
    *   **Before Step 3 (Example CLI output):**
        ```mikrotik
        /interface pppoe-server server print
        Flags: X - disabled
        #   INTERFACE SERVICE-NAME        MAX-MTU   MAX-MRU   ONE-SESSION-PER-HOST   AUTHENTICATION DEFAULT-PROFILE
        ```
    *   **After Step 3 (Example CLI output):**
        ```mikrotik
        /interface pppoe-server server print
        Flags: X - disabled
        #   INTERFACE SERVICE-NAME        MAX-MTU   MAX-MRU   ONE-SESSION-PER-HOST   AUTHENTICATION DEFAULT-PROFILE
        0   wlan-51   pppoe-server          1480      1480     no                pap,chap       pppoe-profile
        ```

4.  **Step 4: Enable Logging for PPP:**

    *   **Purpose:** Configure logging to capture PPP events. This is part of accounting and is helpful for debugging.
    *   **CLI Command:**
        ```mikrotik
         /system logging add topics=ppp action=memory
         /system logging add topics=ppp action=disk
        ```
    * **Explanation:**
        * `/system logging add topics=ppp action=memory` Adds the 'ppp' topic to memory logging, so you can see the messages live.
        * `/system logging add topics=ppp action=disk` Adds the 'ppp' topic to disk logging, for persistent logs.
    * **Winbox GUI:** Navigate to System > Logging, add logging actions for topic 'ppp', to memory and disk.
    *   **Effect:**  Enables logging for ppp related activities.
    *   **Before Step 4 (Example CLI Output)**
        ```mikrotik
        /system logging print
        Flags: X - disabled, I - invalid
        #  TOPICS                     PREFIX  ACTION
        0  critical                   ""      echo
        1  error                      ""      echo
        2  warning                    ""      echo
        3  info                       ""      echo
        4  debug                      ""      echo
        ```
    *   **After Step 4 (Example CLI Output):**
        ```mikrotik
        /system logging print
        Flags: X - disabled, I - invalid
        #  TOPICS                     PREFIX  ACTION
        0  critical                   ""      echo
        1  error                      ""      echo
        2  warning                    ""      echo
        3  info                       ""      echo
        4  debug                      ""      echo
        5  ppp                       ""      memory
        6  ppp                       ""      disk
        ```

## Complete Configuration Commands

Here is the full set of CLI commands to implement this configuration:

```mikrotik
/ppp profile
add name=pppoe-profile local-address=182.184.73.1 remote-address=182.184.73.2-182.184.73.254 use-encryption=yes only-one=yes

/ppp secret
add name=user1 password=password1 service=pppoe profile=pppoe-profile

/interface pppoe-server server
add interface=wlan-51 service-name=pppoe-server default-profile=pppoe-profile

/system logging
add topics=ppp action=memory
add topics=ppp action=disk
```

## Common Pitfalls and Solutions

*   **Authentication Failure:**
    *   **Problem:** Clients fail to connect due to invalid username or password.
    *   **Solution:** Double-check the username, password, and profile settings in `/ppp secret`. Ensure the correct credentials are used on the client. Check the logs in `/log` for `ppp` entries, which usually specify the reason for failure.
*   **Address Allocation Issues:**
    *   **Problem:** Clients can connect, but they don't get an IP address or get the same IP address.
    *   **Solution:** Verify the `local-address` and `remote-address` parameters in the PPP profile are correctly configured. Make sure that the allocated address range doesn't conflict with other networks in your setup. Make sure that `only-one=yes` parameter is set for the user to not be able to connect with the same user simultaneously.
*   **Interface Not Active:**
    *   **Problem:** The PPPoE server isn't working because the interface is not operational.
    *   **Solution:** Ensure the `wlan-51` interface is enabled and functioning correctly. If it's a wireless interface, make sure it's configured for AP mode or the appropriate wireless mode. Use `/interface wireless print` to check.
*   **MTU Issues:**
    *   **Problem:** Clients can connect but have issues with speed and packets loss
    *   **Solution:** Make sure client MTU is compatible with the MTU of the PPPoE connection. Check MTU of the PPPoE server configuration (`/interface pppoe-server server print`) and make adjustments on the client side.

**Security Concerns:**

*   **Password Security:** Using weak passwords like "password1" is a security risk. Always choose strong and unique passwords for user accounts.
*   **Encryption:** Make sure to use encryption `use-encryption=yes` to protect data in transit. It is recommended to use more secure encryption protocols than the default.
*   **Unnecessary Services:** Only enable services (like PPPoE) on interfaces where they are needed. This reduces the attack surface.
*  **Client Isolation:** Although not directly in the above configuration, for wireless networks consider client isolation.

**Resource Issues:**

*   **High CPU/Memory:** A high number of PPP connections can impact CPU and memory usage. Monitor `/system resource monitor` in case of high load.
*   **Logging:** Logging can consume disk space. Manage logging files or use an external logging server if necessary.

## Verification and Testing Steps

1.  **Client Connection:**
    *   Configure a client to connect to the PPPoE server on the `wlan-51` interface using the created credentials (`user1` and `password1`).
2.  **Verify IP:**
    *   After successfully connecting, check the client's IP address. It should be in the range `182.184.73.2` to `182.184.73.254` and not `182.184.73.1`.
3.  **Check Active Connections:**
    *   Use the command `/ppp active print` to verify that client is connected and is using the correct PPP interface, username, profile, and assigned IP address
4.  **Test Connectivity:**
    *   Ping the router's IP (182.184.73.1) from the client.
    *   Test Internet access (if applicable) from the connected client.
5.  **Check Logs:**
    *   Check the logs using `/log print` and filter for `ppp` events.
    *   Look for successful authentication messages, IP address assignments, and any errors or warnings.
6.  **Monitor Resources:**
    *   Monitor `/system resource monitor` for any impact on the router's performance while clients are connected.

## Related Features and Considerations

*   **RADIUS Server:** Instead of the local user database, you can use a RADIUS server for more complex AAA, including accounting and authorization based on time, data usage or other parameters.
*   **PPPoE Client on Mikrotik:** You can setup the router as a PPPoE client as well using `/interface pppoe-client`.
*   **Advanced Firewall:** Use the MikroTik firewall to create specific rules for traffic coming from or destined to PPPoE connections. `/ip firewall filter`.
*   **Queues:** Prioritize or limit bandwidth for PPPoE clients using `/queue tree` or `/queue simple`.
*   **Hotspot:** Combine PPPoE with Hotspot functionality for user management and access control.
*   **IP Pools:** Use IP pools to configure separate address ranges for different PPP profiles and clients.
*   **VPN:** PPPoE can be used in combination with VPN tunnels for secure connections.
* **VPN Server:** The router can act as a server with PPTP, L2TP or SSTP VPN protocols for remote access.

**Real-World Scenarios:**
* **Small ISP:** Provides basic Internet connectivity to clients with PPPoE authentication.
* **SOHO Networks:** Securing guest wifi by using PPP.
* **Specific Applications:** When there is a requirement for accounting and control of users connecting to the network.

## MikroTik REST API Examples (if applicable)

Here are REST API examples for creating PPP profiles and secrets. We'll use the default API port (8728). Please note you need to enable the API service first and have the right user credentials to access the API.

**Enable API Service**

```mikrotik
 /ip service enable api
 /ip service enable api-ssl
```

**Create a PPP Profile (API)**

*   **Endpoint:** `/ppp/profile`
*   **Method:** `POST`
*   **JSON Payload:**
    ```json
    {
        "name": "pppoe-profile-api",
        "localAddress": "182.184.73.1",
        "remoteAddress": "182.184.73.2-182.184.73.254",
        "useEncryption": true,
        "onlyOne": true
    }
    ```
*   **Example using `curl`:**

    ```bash
    curl -k -u admin:password -H "Content-Type: application/json" -X POST -d '{ "name": "pppoe-profile-api", "localAddress": "182.184.73.1", "remoteAddress": "182.184.73.2-182.184.73.254", "useEncryption": true, "onlyOne": true }' https://192.168.88.1:8729/ppp/profile
    ```
*   **Expected Response:**
    *   `200 OK` status code with a JSON object containing the created profile data.
    * **Error Handling:** If an error occurs like invalid data or user permissions the request will fail with error code `4xx` or `5xx` and an error message.

**Create a PPP User Secret (API)**

*   **Endpoint:** `/ppp/secret`
*   **Method:** `POST`
*   **JSON Payload:**

    ```json
    {
        "name": "user1-api",
        "password": "password1",
        "service": "pppoe",
        "profile": "pppoe-profile-api"
    }
    ```
*   **Example using `curl`:**

    ```bash
     curl -k -u admin:password -H "Content-Type: application/json" -X POST -d '{"name": "user1-api", "password": "password1", "service": "pppoe", "profile": "pppoe-profile-api"}'  https://192.168.88.1:8729/ppp/secret
    ```
*   **Expected Response:**
    *   `200 OK` status code with a JSON object containing the created secret data.
*  **Error Handling:** If an error occurs like invalid data or user permissions the request will fail with error code `4xx` or `5xx` and an error message.

**Explanation of parameters in JSON payload:**

* **name:** A string which represents the name of the entity, for example the name of PPP profile or secret
* **localAddress:** An IP address or a range that the router will use, for example `182.184.73.1`.
* **remoteAddress:** A range of IP addresses that the router will assign to connected clients, for example `182.184.73.2-182.184.73.254`.
* **useEncryption:** A boolean, representing if encryption should be used for this connection.
* **onlyOne:** A boolean, which limits the user to only one active connection at the time.
* **password:** The user's password as a plain text string.
* **service:** The service that this secret is designed for, in this case `pppoe`.
* **profile:** The profile used for a certain user, usually by `name`.

## Security Best Practices

*   **Strong Passwords:** Use long, complex passwords.
*   **Encryption:** Enable encryption on all PPP connections.
*   **Regular Audits:** Review your PPP user database regularly.
*   **Limit Access:** Restrict access to the MikroTik router and its API.
*  **Do not expose PPP to the internet:** Be aware that if your wireless is public and PPPoE server is running, it may be possible for remote clients to connect, potentially using up the allocated IPs.
* **Disable unneeded services**: If certain services are not needed (such as api, or telnet) make sure to disable them.
* **Firewall configuration:** Implement strict firewall rules for protecting the router.

## Self Critique and Improvements

**Critique:**

*   The current configuration provides a basic PPPoE setup with local user authentication and does not fully cover more complex use cases such as RADIUS accounting, custom IP pools or advanced traffic shaping.
*   We are using basic passwords which are not secure for production environments.

**Improvements:**

*   **Radius Integration:** Configure a RADIUS server for centralized authentication and accounting.
*   **More Profiles:** Create multiple PPP profiles with different options (like IP pools, encryption, or rate limits)
*   **Dynamic Address Pools:** Implement IP pools instead of using range, for more flexibility.
*   **Advanced Queuing:** Use queues to limit download/upload speed of PPPoE clients.
*   **Custom Scripts:** Create scripts to further customize the connection process.
*   **More secure authentication:** Use certificates instead of username/password.
* **User isolation:** Implement client isolation.

## Detailed Explanation of Topic

PPP (Point-to-Point Protocol) is a data link layer protocol commonly used to establish a direct connection between two nodes. It is used to provide Internet connections in a variety of scenarios, and is mostly used in dialup connections, VPNs and PPPoE. PPP allows devices to authenticate and negotiate IP addresses.

PPP AAA involves:

*   **Authentication:** Verifying the user's identity (e.g., with a username and password or using certificates). In this example we use local database.
*   **Authorization:** Determining what resources the authenticated user is allowed to access. The PPP profile in this example provides basic authorization of access to network resources.
*   **Accounting:** Tracking usage data for billing or logging. This involves log files in our example, but RADIUS provides a more complete accounting framework.

PPPoE (PPP over Ethernet) is a PPP implementation that is used over an Ethernet network. PPPoE is used by ISPs to provide authentication, and control bandwidth usage.

In MikroTik, you configure PPP AAA using profiles, secrets, and the PPPoE server settings.

## Detailed Explanation of Trade-offs

*   **Local User Database vs RADIUS:**
    *   **Local Database:** Simple to set up for basic AAA, but not scalable for larger networks with many clients. Not suitable for complex scenarios, limited in terms of accounting and management.
    *   **RADIUS:** Scalable, provides centralized management, accounting, and advanced features (like dynamic ACLs). The complexity to setup is bigger than the local database, and you have to maintain another server to manage the clients.

*   **Encryption:**
    *   **No Encryption:** Lower overhead but highly insecure, data sent over the network is in plain text.
    *   **Encryption:** Higher overhead but provides confidentiality.

*   **Address Allocation:**
    *   **Fixed IP Range:** Easy to configure but not very dynamic or scalable.
    *   **Dynamic Pools:** More flexible and scalable for handling a large number of clients.

*  **Logging:**
    *   **No logging:** No information on the client activity and potential issues.
    *   **Local Logging:** Logging stored locally on the router, consuming resources.
    *   **Remote Logging:** Logs stored on external server, better suited for big environments.

## Configuration for Specific RouterOS Versions:

This documentation targets RouterOS 7.11, with some details relevant to 6.48 and 7.x. Most of these commands are consistent across versions. If you are using older versions, consult the RouterOS documentation to confirm parameters. Ensure you upgrade your RouterOS versions for security reasons.
For older versions commands for logging might be different, so consult official documentation if needed.

This completes the detailed documentation for implementing PPP AAA with local users on MikroTik RouterOS. Remember to test and adapt these configurations for your specific environment and security needs.
