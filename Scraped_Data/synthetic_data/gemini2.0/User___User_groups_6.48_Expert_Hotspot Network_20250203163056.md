Okay, let's craft some comprehensive documentation for managing users and user groups in a MikroTik Hotspot network, specifically using RouterOS 6.48 and targeting an expert configuration level.

## Scenario Description:

We are configuring a MikroTik router for a hotspot network within a small business environment. The network is using the 220.159.183.0/24 subnet, and the primary network interface is connected to a bridge named "bridge-92". We aim to implement user authentication and authorization using user groups, allowing for different access levels and potential rate limiting for users.

## Implementation Steps:

### 1. Step 1: Initial Interface and Addressing Setup

*   **Description:**  Before setting up users and user groups, it’s vital to have the basic network configuration in place. This includes defining the interface, the IP address on the interface, and basic network connectivity.

*   **Before Configuration:** Assume bridge-92 exists and may or may not have an IP address.
    *   In Winbox: Interfaces listed, but without address.
    *   In CLI: Basic interface configurations may be present, but without an address.

*   **Configuration:** Add an IP address to interface `bridge-92`.

    *   **CLI:**
        ```mikrotik
        /ip address add address=220.159.183.1/24 interface=bridge-92
        ```
        *   `address=220.159.183.1/24`: Specifies the IPv4 address and subnet mask to be assigned.
        *   `interface=bridge-92`: The interface this address is assigned to.
    *   **Winbox:**
        *   Go to `IP` -> `Addresses` -> `+`
        *   Address: `220.159.183.1/24`
        *   Interface: `bridge-92`
        *   Click `Apply` then `OK`

*   **After Configuration:** `bridge-92` has a valid IP Address.
    *   In Winbox: Interface `bridge-92` shows the assigned address.
    *   In CLI: `/ip address print` shows an entry with our address.

*   **Effect:** The router's interface `bridge-92` now has an IP address within the defined subnet, allowing communication on that network.

### 2. Step 2: Create User Groups

*   **Description:**  Define user groups to enable differentiated access control.

*   **Before Configuration:** No user groups are defined.
    * In Winbox: No user groups listed.
    * In CLI: `/user group print` shows default groups only

*   **Configuration:** We'll create two groups: "standard" and "premium".
    *   **CLI:**
        ```mikrotik
        /user group add name=standard
        /user group add name=premium
        ```
        *   `name=standard`: Creates the group named "standard".
        *   `name=premium`: Creates the group named "premium".
    *   **Winbox:**
        *   Go to `System` -> `Users` -> `User Groups` -> `+`
        *   Name: `standard`
        *   Click `Apply` then `OK`
        *   Repeat for `premium`

*   **After Configuration:** The user groups "standard" and "premium" are created.
     * In Winbox: "standard" and "premium" groups are listed.
     * In CLI: `/user group print` shows the new groups.

*   **Effect:** Two user groups are available for assigning users.

### 3. Step 3: Create Users and Assign them to User Groups

*   **Description:**  Create user accounts and assign them to the appropriate user groups.

*   **Before Configuration:**  No user accounts exist (beyond admin).
    *   In Winbox: Only default user(s) are listed.
    *   In CLI: `/user print` shows default users only.

*   **Configuration:** Create two new users: "user1" (standard) and "user2" (premium).
    *   **CLI:**
        ```mikrotik
        /user add name=user1 password=password1 group=standard
        /user add name=user2 password=password2 group=premium
        ```
        *   `name=user1`: Username is "user1".
        *   `password=password1`: Password for "user1". **Note: Use strong passwords in production.**
        *   `group=standard`: Assign user to the "standard" group.
         * `name=user2`: Username is "user2".
        *   `password=password2`: Password for "user2". **Note: Use strong passwords in production.**
        *   `group=premium`: Assign user to the "premium" group.
    *   **Winbox:**
         *  Go to `System` -> `Users` -> `+`
         *  Name: `user1`
         *  Group: `standard`
         *  Password: `password1`
         *  Click `Apply` then `OK`
         *  Repeat for `user2` with group `premium` and `password2`

*   **After Configuration:** Two new user accounts exist and assigned to groups.
    * In Winbox: New user accounts are listed, showing the group.
    * In CLI: `/user print` shows the new users and their groups.

*   **Effect:** Users are created and assigned to appropriate groups for access control.

### 4. Step 4: Implement basic Hotspot Configuration

*   **Description:** Set up a simple hotspot server on bridge-92.

*   **Before Configuration:** No Hotspot server configured on bridge-92.
    * In Winbox: No Hotspot servers listed.
    * In CLI: `/ip hotspot print` shows nothing configured yet

*   **Configuration:**
    * **CLI:**
        ```mikrotik
        /ip hotspot add name=hotspot-bridge-92 interface=bridge-92 address-pool=dhcp_pool_bridge_92 profile=default
        /ip dhcp-server add address-pool=dhcp_pool_bridge_92 interface=bridge-92 disabled=no
        /ip hotspot profile set default use-radius=no
        ```
        *   `/ip hotspot add`: Enables a hotspot server.
            *   `name=hotspot-bridge-92`: The name of this hotspot server
            *   `interface=bridge-92`: The interface for the hotspot.
            *   `address-pool=dhcp_pool_bridge_92` : Uses the dhcp address pool
             *  `profile=default`: The profile to use
        *   `/ip dhcp-server add` : Adds a dhcp server
             *   `address-pool=dhcp_pool_bridge_92`: Assigns the address pool
             *  `interface=bridge-92`: The interface for dhcp.
             * `disabled=no` : Enables the DHCP server
         *   `/ip hotspot profile set default use-radius=no`: Disables RADIUS server for hotspot testing.
    *   **Winbox:**
        *   Go to `IP` -> `Hotspot` -> `Servers` -> `+`
        *   Name: `hotspot-bridge-92`
        *   Interface: `bridge-92`
        *   Address Pool: create new pool and add appropriate range for this subnet
        *   Profile: `default`
        *   Click `Apply` then `OK`
        *   Go to `IP` -> `DHCP Server` -> `DHCP` -> `+`
        *   Name: `dhcp-bridge-92`
        *   Interface: `bridge-92`
        *   Click `Apply` then `OK`

*   **After Configuration:** A basic hotspot is up and running.
    * In Winbox: A hotspot server for `bridge-92` is listed.
    * In CLI: `/ip hotspot print` shows the hotspot server configuration.

*   **Effect:** Users can now connect to the hotspot but are not yet limited or authenticated based on group.

### 5. Step 5: User Group based limitations (Example - simple rate limiting)

*   **Description:**  Add rate limiting based on the user groups to differentiate the bandwidth available for "standard" and "premium" users.

*   **Before Configuration:**  No user group based limitations are in effect
    * In Winbox: No rate limits by groups configured.
    * In CLI: No rate limiting in place.

*   **Configuration:** Apply a simple rate limit (1Mbps download/upload for `standard`, 5Mbps for `premium` users). This will be applied through the hotspot profile.
    *   **CLI:**
        ```mikrotik
       /ip hotspot profile set default rate-limit=1M/1M
       /ip hotspot user group add name=standard shared-users=1 rate-limit=1M/1M
       /ip hotspot user group add name=premium shared-users=1 rate-limit=5M/5M
        ```
      *   `rate-limit=1M/1M`: Set the default rate for users to 1Mbps download/upload for the default hotspot profile.
      *   `/ip hotspot user group add name=standard shared-users=1 rate-limit=1M/1M` : Adds the standard group with rate limits for hotspot users.
      *   `/ip hotspot user group add name=premium shared-users=1 rate-limit=5M/5M`: Adds the premium group with rate limits for hotspot users.
    *   **Winbox:**
        * Go to `IP` -> `Hotspot` -> `User Groups` -> `+`
        *   Name: `standard`
        *   Shared Users: `1`
        *   Rate Limit: `1M/1M`
        *   Click `Apply` then `OK`
        *  Repeat the same steps with `premium` group, `shared-users` set to 1 and `Rate Limit` set to `5M/5M`

*   **After Configuration:** User groups are configured with specific rate limits
    * In Winbox: User groups are listed in hotspot settings.
    * In CLI: `/ip hotspot user group print` shows the configuration.

*   **Effect:**  Users in the "standard" group will be limited to 1Mbps up/down, while "premium" users will have a limit of 5Mbps up/down.

## Complete Configuration Commands:

```mikrotik
/ip address add address=220.159.183.1/24 interface=bridge-92
/user group add name=standard
/user group add name=premium
/user add name=user1 password=password1 group=standard
/user add name=user2 password=password2 group=premium
/ip hotspot add name=hotspot-bridge-92 interface=bridge-92 address-pool=dhcp_pool_bridge_92 profile=default
/ip dhcp-server add address-pool=dhcp_pool_bridge_92 interface=bridge-92 disabled=no
/ip hotspot profile set default use-radius=no
/ip hotspot profile set default rate-limit=1M/1M
/ip hotspot user group add name=standard shared-users=1 rate-limit=1M/1M
/ip hotspot user group add name=premium shared-users=1 rate-limit=5M/5M
```

## Common Pitfalls and Solutions:

*   **Incorrect Interface:** Assigning the hotspot to the wrong interface will prevent users from connecting.
    *   **Solution:** Double-check the `interface` parameter in the `/ip hotspot add` command. Use `/interface print` to ensure you are using the correct name.
*   **Incorrect Subnet:** Assigning IP addresses outside the correct network may cause connection issues.
    *   **Solution:** Double-check the subnet mask in `/ip address add` and ensure the DHCP server provides addresses in the same range. Use `/ip address print` to see current configurations.
*   **Weak Passwords:** Using simple passwords makes accounts vulnerable.
    *   **Solution:** Enforce strong password policies and educate users on best practices. Implement RADIUS authentication where possible.
*   **Missing DHCP Configuration:** If the DHCP server isn't configured, connected clients won't receive IP addresses.
    *   **Solution:**  Make sure `/ip dhcp-server add` command is correctly set. Also, ensure the interface is active with no issues. Use the command `/ip dhcp-server print` to see the dhcp settings.
*   **Incorrect User Group Assignment:** Not assigning users to the correct groups will result in unintended access or limits.
    *   **Solution:** Verify the `group` parameter in the `/user add` command and ensure they are in the correct `hotspot user group`. Use `/user print` to check current settings.
*   **High CPU usage:** If you are using hotspot features, you may see high CPU usage, especially if you do not have a strong CPU in your router.
    *  **Solution:** Consider using hardware offloading if possible. Review other rules that may be adding load to the CPU (NAT rules, queue rules). Consider implementing less CPU intensive functions, such as using a radius server.

## Verification and Testing Steps:

1.  **Connect a Client:** Connect a device to the `bridge-92` network (Wi-Fi or wired) and observe that it receives an IP address.
2.  **Hotspot Login:** Open a web browser on the client, you should be redirected to the hotspot login page. Log in with "user1" and password "password1".
3.  **Test Rate Limits (user1):** Perform a speed test and verify a maximum speed around 1Mbps.
4.  **Login with another user (user2):**  Logout and login as user2 with the password password2.
5.  **Test Rate Limits (user2):**  Repeat a speed test. Ensure user2 has an approximate limit of 5Mbps.
6.  **User List:** In Winbox, go to `IP` -> `Hotspot` -> `Active` to see who is logged on. In the CLI, use `/ip hotspot active print`. This list will show logged on users and their IP addresses.
7. **Ping:** Ping the router address from an attached client to test connectivity. From the client open the CLI (Windows: cmd, Linux/Mac: terminal) and type `ping 220.159.183.1`.
8. **Torch:** Use torch to verify the rate limits. From the router console use `/tool torch interface=bridge-92`.  You can see the data rate when a client is downloading, it will match your rate limits (or less if the bandwidth to your uplink is limited)

## Related Features and Considerations:

*   **RADIUS Authentication:** Using a RADIUS server for authentication provides a more robust solution for managing user accounts.
*   **User Profiles:** Instead of rate limits in groups, create user profiles for more complex rate limiting policies or other settings.
*   **Hotspot Usage Quota:** Limit the bandwidth consumption or time spent online.
*   **Hotspot Advertisements and walled garden**: Consider enabling advertisements on your hotspot.
*   **Address Lists and Firewall:** Use address lists to manage firewall rules based on user groups or access policies.
*   **Layer 7 protocols**: You can use Layer 7 protocol matching to perform more intelligent bandwidth management.
*   **Webproxy**: You can use the web proxy for caching.

## MikroTik REST API Examples (if applicable):

While many MikroTik configurations are done via CLI or Winbox, here's how you might interact with user and group settings via the API (Note: API is available on RouterOS 6.43 and up):

*  **Ensure that API access is turned on:** In Winbox, go to `IP` -> `Services` and verify that the `api` and `api-ssl` ports are enabled, by default they are disabled. In the CLI, use `/ip service print`
*   **Note:** The examples below use the `curl` command.  Be sure to use proper API user credentials that have the required permissions on your router.

### Example 1: Create a User Group:
*   **Endpoint:** `/user/group`
*   **Method:** `POST`
*   **Payload:**
    ```json
    {
      "name": "guest"
    }
    ```
    *  `name`: The name for the new group.

*   **Curl Command:**
    ```bash
    curl -k -H "Content-Type: application/json" -u <username>:<password> -d '{"name":"guest"}'  https://<router_ip>/rest/user/group
    ```
   *   Replace `<username>`, `<password>`, and `<router_ip>` with the correct values. `-k` disables SSL verification, you may omit `-k` if your router is properly setup with a certificate.
*   **Expected Response (Success):**
    ```json
    {"id":"*1"}
    ```
    *  The returned `id` can be used to modify or delete the group.

* **Expected Response (Error):**
    ```json
    {"message": "already have such item", "error": true}
    ```
    *  This means that the group already exists, or there was an issue.

### Example 2: Get a List of User Groups:
*   **Endpoint:** `/user/group`
*   **Method:** `GET`
*   **Payload:** None
*   **Curl Command:**
    ```bash
    curl -k -u <username>:<password> https://<router_ip>/rest/user/group
    ```
*   **Expected Response:**
    ```json
    [
        {
            "name":"read",
            "policy":"read",
            "id":"*1"
        },
        {
            "name":"full",
            "policy":"*",
            "id":"*2"
        },
        {
          "name":"guest",
           "policy":"read",
           "id":"*3"
        }
    ]
    ```
   * This returns an array of objects. Each object represents a user group, showing its `name` , `policy` and `id`.
   *  `policy`:  Indicates the access policy (read, write, full, custom).

### Example 3: Create a User:
*   **Endpoint:** `/user`
*   **Method:** `POST`
*   **Payload:**
    ```json
    {
        "name": "testuser",
        "password": "testpassword",
        "group": "guest"
    }
    ```
    * `name`: The username.
    * `password`: The password for this user.
    * `group`:  The name of the group the user is assigned to.

*   **Curl Command:**
    ```bash
    curl -k -H "Content-Type: application/json" -u <username>:<password> -d '{"name":"testuser", "password":"testpassword", "group":"guest"}' https://<router_ip>/rest/user
    ```
*   **Expected Response (Success):**
    ```json
    {"id":"*4"}
    ```
    *  The returned `id` can be used to modify or delete the group.

* **Expected Response (Error):**
    ```json
    {"message": "already have such item", "error": true}
    ```
     * This means that the user already exists, or there was an issue.

### Example 4: Get a list of users:
*   **Endpoint:** `/user`
*   **Method:** `GET`
*   **Payload:** None
*   **Curl Command:**
    ```bash
     curl -k -u <username>:<password> https://<router_ip>/rest/user
     ```
*  **Expected Response:**
     ```json
       [
          {
            "name":"admin",
             "group":"full",
             "id":"*0"
          },
          {
             "name":"testuser",
             "group":"guest",
             "id":"*1"
           }
       ]
     ```
   * This returns an array of objects. Each object represents a user, showing its `name`, `group` and `id`.

**Error Handling:** The API will return a JSON error response with a "message" key and `error: true` if something fails. Always check for these errors when working with the API.

**Security Notes:** API access should be carefully controlled, using strong passwords and only enabling it on secure networks.

## Security Best Practices

*   **Strong Passwords:** Enforce strong, unique passwords for all users and the admin account. Use a password generator for stronger passwords.
*   **API Security:** If using the API, use HTTPS/SSL, enforce strong credentials and restrict access. Only allow API access from trusted networks. Do not allow API access from untrusted networks, such as the internet.
*   **Regular Software Updates:** Keep RouterOS updated to the latest version to patch vulnerabilities.
*   **Firewall:** Implement proper firewall rules to restrict access to the router and the network.
*   **Disable Unused Services:** Disable any services that are not needed to reduce the attack surface. (such as the default winbox port, by changing the port).
*   **User Rights and Policies:** Limit user permissions and access to only what is necessary.
*   **Regular Review:** Check the configurations periodically to ensure they meet your current security needs.
*   **Guest network:** Always isolate a guest network from your internal trusted network using a dedicated interface/VLAN and firewall rules.
*   **Use RADIUS Authentication**: Consider using a radius server, instead of using local usernames, as it is more secure, easier to administer, and scalable.

## Self Critique and Improvements

This configuration provides a basic setup for user groups and rate limiting. Here's what could be improved:

*   **More Sophisticated Rate Limiting:** Use PCQ queues for better rate limiting and fair usage.
*   **Advanced Hotspot Features:** Configure walled gardens, usage quotas, and advertisements on your hotspot.
*   **Real-world Security:** Use RADIUS server for user authentication and implement more strict firewall rules.
*   **Monitoring:** Set up monitoring tools to track performance and user activity.
*   **More Comprehensive API:** Add examples of other API calls, especially for more advanced hotspot settings.
*   **Better error handling for API:** Add example error checking and how to fix the error using the API.
*   **Automation:** Create scripts to automatically handle user creation, group assignment and settings.

## Detailed Explanations of Topic

**User Management:** MikroTik’s User management system allows for creating users and assigning them to groups. Users can be used for Hotspot authentication, VPN access, and other services.

**User Groups:** User groups allow you to apply policies and settings (like rate limits, firewall rules) to multiple users with a single configuration. Groups are essential for creating flexible access control for the network.

**Hotspot:** The Hotspot feature enables a secure, controlled access network. Users are prompted to log in before gaining access to the internet or other network resources.

**Rate Limiting:** Controlling bandwidth per user or group is crucial to provide a fair experience. MikroTik’s rate limiting system includes simple rate limits and advanced queues.

## Detailed Explanation of Trade-offs

*   **Local Users vs. RADIUS:** Local users are simpler to set up but harder to manage in large deployments, while RADIUS offers centralized user management.
*   **Simple Rate Limits vs. PCQ:** Simple rate limits are easy to implement, but PCQ queues offer more fair and advanced rate limiting.
*   **Hotspot vs. Regular Network:** Hotspots offer secure user authentication, while regular networks are easier for trusted devices.

## Configuration for Specific RouterOS Versions:

This document specifically targets RouterOS 6.48 and later. Some commands or features (e.g., the REST API) might behave differently or be unavailable on older versions. If your device is running a different RouterOS version, be sure to check the documentation for that specific version. Also, note that API access has changed over different RouterOS versions.
