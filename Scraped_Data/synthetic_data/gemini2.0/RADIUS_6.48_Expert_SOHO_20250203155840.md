Okay, let's dive into configuring RADIUS authentication on a MikroTik router running RouterOS 6.48, specifically for VLAN 44 (interface `vlan-44`) within a SOHO environment.

## Scenario Description:

This scenario focuses on implementing RADIUS (Remote Authentication Dial-In User Service) authentication for clients connecting to the `vlan-44` interface. We'll assume that the VLAN is used for wired clients, and their access needs to be controlled via a RADIUS server. The IP range used by this VLAN will be `140.57.236.0/24`, and client’s will access resources by being authenticated against a RADIUS server.

## Implementation Steps:

Here's a step-by-step guide to configure RADIUS authentication for VLAN 44.

**1. Step 1: Adding RADIUS Server Configuration**
   *   **Purpose:** Define the RADIUS server parameters including its IP address, secret key, and port.
   *   **Before:** No RADIUS configuration exists.
   *   **Action:** Use the MikroTik CLI to add the RADIUS server information. This can also be done via the GUI in *RADIUS* section.
   *  **CLI Example:**

      ```mikrotik
      /radius add address=192.168.88.100 secret="your_radius_secret" timeout=3
      ```
      *  `address`: IP address of your RADIUS server (Replace `192.168.88.100` with the correct IP.)
      *  `secret`: The shared secret key used by the router and RADIUS server. (Replace `your_radius_secret` with your actual shared secret key).
      *  `timeout`: Time in seconds to wait for a response from the RADIUS server, useful for troubleshooting.

    *  **Winbox GUI:**
       Navigate to `RADIUS` in the left side menu and press the `+` button to add a new Radius server.
       * Address: `192.168.88.100`
       * Secret: `your_radius_secret`
       * Timeout: `3`
    *  **After:** The RADIUS server is now defined in the router configuration.
      * You can verify by issuing this command
         ```mikrotik
         /radius print
         ```

**2. Step 2: Configuring the PPP Secret or User Profile**
   *   **Purpose:** To define how the router will interact with the RADIUS server for authentication on the specified vlan. It can be used for hotspot, or PPP users. In this case, we will use it for PPP.
   *   **Before:** No PPP secrets configured.
   *   **Action:** Create a profile which uses radius authentication. Note that in this case, we are assuming there is no accounting, so no specific accounting service will be configured.
   *  **CLI Example:**

      ```mikrotik
      /ppp profile add name="radius_vlan44" use-radius=yes
      ```

     * `name`: `radius_vlan44` name of the PPP profile, must be unique.
     * `use-radius`:  `yes` to use RADIUS for authentication and authorization.
    *  **Winbox GUI:**
       Navigate to `PPP` -> `Profiles` in the left side menu and press the `+` button to add a new profile.
       * Name: `radius_vlan44`
       * use Radius: `Yes`

    *  **After:** The PPP profile with RADIUS integration is now configured. You can verify by issuing this command:
       ```mikrotik
      /ppp profile print
      ```

**3. Step 3: Creating a PPP Secret (User) using that profile.**
   *   **Purpose:** To define a user which uses the newly created profile, and that will make use of the previously defined Radius Server.
   *   **Before:** No PPP users configured.
   *   **Action:** Define a user and assign the profile to it.
   *  **CLI Example:**

       ```mikrotik
      /ppp secret add name="user1" service=ppp  profile="radius_vlan44" local-address=140.57.236.2  remote-address=140.57.236.3
       ```

      *  `name`:  `user1` Name of the user. This is the name that needs to be present on the RADIUS server.
      *  `service`:  `ppp` Specify ppp as service that will use the user.
      *  `profile`:  `radius_vlan44` PPP Profile used by this user.
      *  `local-address`:  `140.57.236.2` Local IP address for this user's PPP interface.
      *  `remote-address`:  `140.57.236.3` Remote IP address for this user's PPP interface.

     *  **Winbox GUI:**
         Navigate to `PPP` -> `Secrets` in the left side menu and press the `+` button to add a new secret.
          * Name: `user1`
          * Service: `ppp`
          * Profile: `radius_vlan44`
          * Local Address: `140.57.236.2`
          * Remote Address: `140.57.236.3`
    *  **After:** The PPP user is now defined in the router configuration. You can verify by issuing this command:
          ```mikrotik
          /ppp secret print
         ```

**4. Step 4: Assign a PPP interface to vlan-44**
   *   **Purpose:** To associate the PPP client with the vlan interface.
   *   **Before:** No PPP interfaces are configured.
   *   **Action:** Create a PPP client using the previously configured user, and assign the interface.
   *  **CLI Example:**

      ```mikrotik
      /interface ppp-client add name="ppp-vlan44" user="user1" interface=vlan-44 disabled=no
      ```

      * `name`: `ppp-vlan44` name of the PPP client.
      * `user`:  `user1` the username to connect with.
      * `interface`:  `vlan-44` the interface that is to be used by the client.
      * `disabled`:  `no` start it right away.

    *  **Winbox GUI:**
        Navigate to `Interfaces` -> `PPP` in the left side menu and press the `+` button and select `Add New PPP Client`.
           * Name: `ppp-vlan44`
           * User: `user1`
           * Interface: `vlan-44`
           * Uncheck "Disabled"

    *  **After:** The PPP interface is now defined in the router configuration. You can verify by issuing this command:
          ```mikrotik
          /interface ppp-client print
         ```

**5. Step 5: Add a static DHCP client, in order to assign address dynamically for clients that do not authenticate via radius**
   * **Purpose**: Allows client that are not authenticated via RADIUS to still obtain IP address on the network.
   * **Before**: No DHCP client is configured.
   * **Action**: Configure the DHCP client.
   * **CLI Example**

       ```mikrotik
        /ip dhcp-client add interface=vlan-44 disabled=no
       ```

        *  `interface`:  `vlan-44` the interface to run on.
        * `disabled`:  `no` Start it right away.

    * **Winbox GUI:**
        Navigate to `IP` -> `DHCP Client` and add a new DHCP client.
        * Interface: `vlan-44`
        * Uncheck "Disabled"

    * **After**: The DHCP client is now configured and running. You can check the state of it with the following command:
        ```mikrotik
        /ip dhcp-client print
        ```

**6. Step 6: Firewall rule to forward authenticated user connections**
   * **Purpose**: Allows client connected to vlan-44 to route to the desired destination. In this example we will allow access to internet.
   * **Before**: No firewall rules to route the client.
   * **Action**: Create a simple NAT rule.
   * **CLI Example**
        ```mikrotik
        /ip firewall nat add chain=srcnat action=masquerade out-interface=ether1 src-address=140.57.236.0/24
        ```
      * `chain`:  `srcnat` NAT chain where to add the rule.
      * `action`: `masquerade` IP masquerade action.
      * `out-interface`: `ether1` the internet facing interface. Change it if needed.
      * `src-address`:  `140.57.236.0/24` the network that needs to be natted.
    * **Winbox GUI:**
        Navigate to `IP` -> `Firewall` and go to the `NAT` tab. Then add a new rule.
        * Chain: `srcnat`
        * Action: `masquerade`
        * Out. Interface: `ether1`
        * Src Address: `140.57.236.0/24`

    * **After**: The firewall rule is configured. It can be verified with the following command:
      ```mikrotik
      /ip firewall nat print
      ```
   **Important Notes:**
    - Ensure your RADIUS server is configured to accept requests from the MikroTik router's IP address.
    - Make sure the shared secret (`secret` in step 1) matches exactly on both the MikroTik and RADIUS server.
    - Configure a firewall rule to allow UDP port `1812` and `1813` from the router's IP address to the RADIUS server. This example uses the ports 1812 and 1813, make sure to check your RADIUS server settings.
    - The `user1` account must exist on the RADIUS server and be associated with a valid password.
    - Ensure `vlan-44` is configured in the interfaces menu (this is outside the scope of this specific document), with correct parent interface.

## Complete Configuration Commands:

Here are all the commands together for quick implementation:

```mikrotik
/radius add address=192.168.88.100 secret="your_radius_secret" timeout=3
/ppp profile add name="radius_vlan44" use-radius=yes
/ppp secret add name="user1" service=ppp  profile="radius_vlan44" local-address=140.57.236.2  remote-address=140.57.236.3
/interface ppp-client add name="ppp-vlan44" user="user1" interface=vlan-44 disabled=no
/ip dhcp-client add interface=vlan-44 disabled=no
/ip firewall nat add chain=srcnat action=masquerade out-interface=ether1 src-address=140.57.236.0/24
```
## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router cannot connect to the RADIUS server.
    *   **Solution:** Verify the IP address and secret are correct. Double check firewall rules. Use the `ping` command from the MikroTik router to test network connectivity to the RADIUS server. You can also use tools like *torch* to verify traffic from the router towards the radius server.
*   **Incorrect Shared Secret:**
    *   **Problem:** The shared secret key does not match on the MikroTik router and RADIUS server.
    *   **Solution:** Ensure the secrets are identical. Re-enter the secret on both devices.
*   **User Not Found/Password Incorrect:**
    *   **Problem:** The user configured on the router does not exist on the RADIUS server, or the password doesn't match.
    *   **Solution:** Verify the user exists, it has the correct password, and the right attributes are being returned to the router. Check the RADIUS server logs for authentication errors.
*   **Timeout Issues:**
    *   **Problem:**  The MikroTik router times out while waiting for a response from the RADIUS server.
    *   **Solution:** Increase the `timeout` value in the radius configuration. Verify that the network connection to the RADIUS server is stable.
*   **Missing Firewall Rules:**
    *  **Problem**: Clients are not able to access the internet or other resources.
    *  **Solution:** Make sure there are the appropriate firewall rules, and routing configured.
*   **CPU or Memory Overload:**
    *   **Problem:**  Excessive radius requests might impact the router's CPU.
    *   **Solution:** Monitor system resource consumption. Optimize RADIUS server performance, if needed. Consider a more powerful router if necessary.

## Verification and Testing Steps:

1.  **Ping the RADIUS Server:**
    *   Use: `ping 192.168.88.100` (Replace with your RADIUS server IP) to ensure connectivity.
2.  **Check the Radius status:**
    *   Use `/radius print` to check if the server is enabled.
3.  **Check PPP status**
    *   Use `/interface ppp-client monitor ppp-vlan44` (replace the interface name). Check the output status and see if a connection has been established.
4.  **Connect a Client to `vlan-44`:**
    *   Connect a client device to the VLAN. The client should not get an IP assigned via DHCP.
5.  **Monitor RADIUS Logs:**
    *   Check the RADIUS server's logs for authentication attempts and errors. This is crucial to identify any issues in RADIUS negotiation.
6.  **Check router's logs**
    * Check `/log print` to see any error or problems in relation to ppp and radius.
7.  **Check Firewall Rules:**
    * Verify if NAT rule, has been applied using `/ip firewall nat print`
8.  **Test Connectivity:**
    * Once a connection is established, try to ping resources on the internal network and external networks using tools like `ping 8.8.8.8`.

## Related Features and Considerations:

*   **Accounting:** Implement RADIUS accounting to track user session usage time. This involves configuring the MikroTik router to send accounting requests to the RADIUS server.
*   **Hotspot:** Use the RADIUS setup to authenticate users on a hotspot network. This will require a modified user configuration and profile.
*   **VRF:** If using VRF (Virtual Routing and Forwarding), ensure the RADIUS and PPP connections are properly mapped to the relevant VRF instance.
*   **Backup RADIUS:** Configure a backup RADIUS server for redundancy in case the primary server fails. This requires multiple RADIUS server entries in MikroTik.
*   **User Profiles:** Define custom user profiles, including firewall rules and specific resource access via the RADIUS server.
*  **DHCP Server**: In the case the router acts as a DHCP server on the network, make sure it excludes the local and remote IP used by the PPP client.

## MikroTik REST API Examples (if applicable):

Mikrotik does not have an easy way to manage radius via REST API, but here is an example using *ppp secrets* and *ppp profiles*:

**1. Adding a PPP Profile**

*   **API Endpoint:** `/ppp/profile`
*   **Request Method:** `POST`
*   **JSON Payload:**
    ```json
    {
      "name": "radius_vlan44_api",
      "use-radius": true
    }
    ```
*   **Expected Response (Success - Status 200):**
    ```json
    {
        "message": "added"
    }
    ```
*   **Error Handling (Example - Status 400):**
    ```json
    {
        "message": "already exists"
    }
    ```
    This means a profile with the same name already exists.

**2.  Adding a PPP Secret**

*   **API Endpoint:** `/ppp/secret`
*   **Request Method:** `POST`
*   **JSON Payload:**
    ```json
    {
        "name": "user_api",
        "service": "ppp",
        "profile": "radius_vlan44_api",
        "local-address":"140.57.236.4",
        "remote-address":"140.57.236.5"
    }
    ```
*   **Expected Response (Success - Status 200):**
    ```json
    {
        "message": "added"
    }
    ```
*   **Error Handling (Example - Status 400):**
    ```json
    {
        "message": "invalid value for argument profile"
    }
    ```
    This usually means that the profile does not exists

**3. Example using `fetch` from the terminal**

Assuming we have a user named `admin` and password `123`, and the router IP is `192.168.88.1`

Add a new profile `radius_vlan44_api`

```mikrotik
/tool fetch url="https://192.168.88.1/rest/ppp/profile" \
    http-method=post \
    http-header-field="Content-Type: application/json" \
    http-header-field="Authorization: Basic $(/tool user get [find name=admin] password | /encode base64)" \
    body='{"name":"radius_vlan44_api", "use-radius":true}'
```

Add a new user `user_api` using the previously created profile.

```mikrotik
/tool fetch url="https://192.168.88.1/rest/ppp/secret" \
    http-method=post \
    http-header-field="Content-Type: application/json" \
    http-header-field="Authorization: Basic $(/tool user get [find name=admin] password | /encode base64)" \
    body='{"name":"user_api", "service":"ppp", "profile":"radius_vlan44_api", "local-address":"140.57.236.4", "remote-address":"140.57.236.5"}'
```

## Security Best Practices:

*   **Strong Secret:**  Use a strong, complex shared secret key for communication between the MikroTik router and RADIUS server. Change the default secret provided in the examples.
*   **Restrict Access:**  Only allow RADIUS traffic from trusted IP addresses on your RADIUS server. Use firewall rules on the RADIUS server and the router to limit access.
*   **Secure Server:** The RADIUS server must be a secure machine, and it needs to be well protected.
*   **Regular Security Audits:** Regularly check the router and server for vulnerabilities and apply security patches.
*  **Limit Router access:** If you will manage the router via winbox or webfig, avoid making it accessible to the public.
*  **Use encryption**: If possible enable encryption on the RADIUS server.

## Self Critique and Improvements:

*   **Complexity:** The current setup is relatively basic. It could be improved by adding accounting functionality, custom user profiles, and backup RADIUS servers for redundancy.
*   **Error Handling:**  More detailed error checking could be implemented on both client and server side. The Mikrotik router provides many tools that are very useful for troubleshooting purposes.
*  **Dynamic User Assignment**: Implement dynamic IP assignment based on RADIUS attributes, which is useful for more complex setups.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network.

*   **Authentication:** Verifies user identities, and if they are valid.
*   **Authorization:** Determines user access rights and permissions.
*   **Accounting:** Tracks user resource usage time and data consumption.

In a MikroTik environment, RADIUS is typically used to centralize user management for various network services, such as:

*   Hotspots
*   PPP (Point-to-Point Protocol)
*   VPN (Virtual Private Networks)
*  Wireless networks (With the aid of other tools like CAPsMAN)

RADIUS servers are separate entities in the network and are not part of the MikroTik router itself.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Easier to set up for a small number of users, but does not scale well. User data is stored on the device.
    *   **RADIUS:** Centralized user management, more secure for a large number of users, but requires an external server. User data is stored on the Radius server, and this can be easily integrated into a more complex network with LDAP integration, for example.
*   **Radius vs local Accounting**:
    * **Local:** Easy to setup, but requires manual analysis of logs, and might not be detailed.
    * **Radius**: Provides more accurate and real time analysis.
*   **Static vs Dynamic IPs**:
    * **Static IPs:** Can be easier to manage on smaller networks. Less error prone.
    * **Dynamic IPs:** Can scale to more clients, but might require more configuration on the server side.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS 6.48. Most commands, with slight variations, will be valid on newer versions.
  * For RouterOS 7+, there might be slight differences in GUI menus, but commands will still work.
  * If you encounter any error due to incompatibility, check the RouterOS documentation, especially the section on PPP, RADIUS, and Interface commands.

This should provide a detailed, actionable guide for implementing RADIUS authentication on your MikroTik router. Let me know if you have other questions!
