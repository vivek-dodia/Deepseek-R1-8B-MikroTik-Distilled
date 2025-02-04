Okay, here's the detailed documentation for managing users and user groups on a MikroTik RouterOS device, specifically focusing on your provided context:

**Context:**

*   **RouterOS Version:** 6.48 (compatible with 6.48 and 7.x)
*   **Configuration Level:** Expert
*   **Network Scale:** ISP
*   **Subnet:** 139.153.41.0/24
*   **Interface Name:** wlan-63

**Scenario Description:**

This configuration focuses on setting up a secure user management system within an ISP environment. We'll create different user groups with specific access levels and individual user accounts assigned to these groups, all linked to the specified subnet and interface (as relevant in real world scenarios). This would be used, for instance, to manage access to different network resources based on user roles, or to configure specific permissions on hotspot services.

**Implementation Steps:**

1.  **Step 1: Initial State Verification and Assumptions**
    *   **Action:**  We start by verifying the initial state of user configurations. This includes checking for existing users, groups, and their associated settings.
    *   **Command (CLI):**
        ```mikrotik
        /user print
        /user group print
        ```
    *   **Expected Output:** This output will display current users and groups, which should likely be minimal in a fresh router. In a real ISP environment, you may have existing infrastructure, and it's important to note any conflicts.
    *   **Explanation:** This step is crucial for understanding the current setup, preventing accidental overwriting of important data. We should also assume that the interface `wlan-63` has already been set up (it is not shown as part of this procedure, only used as an element of the configuration). The subnet `139.153.41.0/24` is also assumed to be configured in the IP space, although it will not be directly used.
    *   **Winbox GUI:** Navigate to `System` -> `Users` and `System` -> `Groups`.

2.  **Step 2: Create User Groups**
    *   **Action:** We create user groups with different access levels to control their privileges. For example:
        *   `full-access`: Users with full RouterOS privileges.
        *   `read-only`: Users that can only view the configuration.
        *   `hotspot-manager`: Users with access to hotspot configuration.
    *   **Command (CLI):**
        ```mikrotik
        /user group add name=full-access policy=write,test,password,read,ftp,reboot,policy,winbox,web,local,dude,ssh,api
        /user group add name=read-only policy=read
        /user group add name=hotspot-manager policy=write,test,read,winbox,local
        ```
    *   **Expected Output:**  New user groups `full-access`, `read-only`, and `hotspot-manager` are created and will be visible in `user group print`.
    *   **Explanation:** We explicitly define permissions each user group will have by configuring the `policy` parameter. This is a critical step in a multi-user environment.
    *   **Winbox GUI:** Navigate to `System` -> `Groups` -> `+` to create new groups, adding the policy permissions for each group by clicking the checkboxes under the `Policies` tab.

3.  **Step 3: Create User Accounts**
    *   **Action:** We now create individual user accounts and assign them to relevant groups.
        *   `admin`: Full-access user.
        *   `monitor`: Read-only user.
        *   `hotspot-user`: User with only hotspot access.
    *   **Command (CLI):**
        ```mikrotik
        /user add name=admin group=full-access password="SecurePassword1!"
        /user add name=monitor group=read-only password="ReadOnlyPassword2!"
        /user add name=hotspot-user group=hotspot-manager password="HotspotPassword3!"
        ```
    *   **Expected Output:** New user accounts `admin`, `monitor`, and `hotspot-user` are created with passwords and associated to their configured groups. These will be visible in `user print`.
    *   **Explanation:** We are creating the actual user accounts linked to the groups defined before. This step finalizes the separation of permissions.
    *   **Winbox GUI:** Navigate to `System` -> `Users` -> `+` to create new users, select the group for each user in the `Group` dropdown.

4. **Step 4: Verifying the User Access**
    *   **Action**: We verify the access level for each user. This would involve, for example, login in with a given user and verifying the permissions each user is able to execute.
    *   **Commands (CLI):** To test user access, you will need to connect to the router via ssh or telnet, using the configured username and password. For example:
      ```bash
       ssh monitor@<router_ip>
      ```
      And then, run a command to verify the permissions (for example, to change a config setting). You will see an error if the user does not have the permissions to execute a given command.
    *   **Expected Output:** A `permission denied` message will appear if the user does not have the right permissions, while commands with permissions would be successfully executed.
    *   **Explanation:** This step ensures that the previous configuration is working as designed, preventing over privileged accounts.
     *  **Winbox GUI:** Open Winbox and attempt login using the different user created credentials. Only users with write access will be able to change configurations via Winbox. Users with only `read` access will be only able to monitor router parameters and logs.

**Complete Configuration Commands:**

```mikrotik
# Initial State Check
/user print
/user group print

# Create User Groups
/user group add name=full-access policy=write,test,password,read,ftp,reboot,policy,winbox,web,local,dude,ssh,api
/user group add name=read-only policy=read
/user group add name=hotspot-manager policy=write,test,read,winbox,local

# Create User Accounts
/user add name=admin group=full-access password="SecurePassword1!"
/user add name=monitor group=read-only password="ReadOnlyPassword2!"
/user add name=hotspot-user group=hotspot-manager password="HotspotPassword3!"

# Verification (using commands)
# Connect using ssh with user monitor
# attempt to execute  /ip address add address=10.0.0.1/24 interface=wlan-63
# Check that you get an error message:  "failure: can't add - read only access"
```

**Parameter Explanation:**

| Command       | Parameter      | Description                                                                                                                               |
|---------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `/user group add` | `name`         | The name of the user group.                                                                                                           |
|               | `policy`       | A comma-separated list of permissions that users in this group have (e.g., `read`, `write`, `reboot`, `ftp`, etc.).   |
|`/user add`     | `name`         | The username of the user.                                                                                                               |
|               | `group`        | The user group to which this user belongs.                                                                                           |
|               | `password`     | The password for the user account.                                                                                                      |

**Common Pitfalls and Solutions:**

*   **Pitfall:** Forgetting or misconfiguring the `policy` parameter during user group creation can result in users having unwanted levels of access, which is a security concern.
    *   **Solution:** Carefully review the policies set for each group and use the least privilege principle. Verify that user accounts have the correct level of access.
*   **Pitfall:**  Weak or easily guessable passwords.
    *   **Solution:** Enforce strong password policies (complex passwords).  Consider using secure authentication methods such as public keys where possible.
*   **Pitfall:**  Accidentally giving a user account full admin privileges when it wasn't intended.
    *   **Solution:** Double-check group assignments and policies, and use the principle of least privilege.
*   **Pitfall:** High CPU or memory usage due to too many user sessions.
    *   **Solution:** Regularly monitor router resource usage, use connection limits per user if needed, and ensure the router has sufficient resources to handle the load.
*   **Pitfall:** Incorrect user group assignation.
    *   **Solution:** Double check group configurations and user membership.

**Verification and Testing Steps:**

1.  **Login via Different Accounts:** Try logging into the RouterOS device using the credentials of different user accounts (admin, monitor, hotspot-user) via SSH, Telnet, Winbox, or Webfig.
2.  **Test Permissions (CLI):** Once logged in, try performing actions that should be permitted or denied based on the assigned group permissions. For example, logged in as `monitor`, try to modify IP addresses or user configurations.
3.  **Test Permissions (Winbox):** Login to Winbox with `monitor` account, you will find most of the configuration options disabled.
4.  **Check Logs:** Review system logs for any access denials or errors to ensure the configuration is working correctly. (`/log print`)
5.  **Monitor resource usage:** While users are logged, monitor CPU and memory (`/system resource print`). High usage may indicate that the system is being over used.

**Related Features and Considerations:**

*   **Hotspot Integration:** User accounts and groups can be directly integrated with MikroTik's Hotspot feature, allowing for different user roles within a hotspot environment.
*   **RADIUS Authentication:** For large-scale deployments, using RADIUS for user authentication and authorization can centralize user management and provide more advanced options.
*   **API Access:** The MikroTik API can be used to manage users, groups, and policies programmatically.
*   **User Limits:** Set session limits per user in the `/user` menu using `session-timeout` parameter to limit active session.
*   **Disable unused services:** To increase security, ensure unused or unnecessary services such as telnet are disabled.
*   **Lockout Policy:** Implement a lockout policy to limit login attempts.
*   **IP access restriction:** Using `/ip service` you can restrict which IPs can access Winbox, SSH, and webfig.
*   **Password complexity:** Use strong passwords and enforce regular updates, especially for privileged accounts.

**MikroTik REST API Examples (if applicable):**

This section would typically be applicable if we were manipulating user groups via API calls, but for basic user creation and access, the API call would be too complex and unnecessary. So I will give a more general example on using the API:

*   **Endpoint:** `/api/user`
*   **Method:** `POST`
*   **JSON Payload (Example to create a user):**
    ```json
    {
        "name": "api_user",
        "group": "full-access",
        "password": "APIUserPassword123!"
    }
    ```
*   **Expected Response (Success 200):**
    ```json
    {
       ".id": "*1",
       "name": "api_user",
        "group": "full-access"
    }
    ```
    **Note:** if there was an error, for example the user already existed, a message would be shown in the form of `{"message": "user already exist"}`. The HTTP response code will be different depending on the error (400 for bad request, etc).

**Security Best Practices:**

*   **Principle of Least Privilege:** Only grant users the necessary permissions.
*   **Strong Passwords:** Enforce strong password policies.
*   **Regularly Review:** Review user accounts and their permissions periodically.
*   **Disable Unused Services:** Disable unnecessary services like Telnet to reduce the attack surface.
*   **IP Restrictions:** Restrict access to administrative services (Winbox, SSH) based on IP address.
*   **Lockout Policy:** Implement a lockout policy to limit login attempts after multiple failures.

**Self Critique and Improvements:**

*   **Improvements:**
    *   **RADIUS Integration:** For more advanced scenarios, integrating with RADIUS would provide better control and scalability.
    *   **Scripting:** Could be improved by automating user creation and group management using RouterOS scripting capabilities.
    *   **More Granular Policies:** We could define more granular policies for each group.
*   **Trade-offs:**
    *   A simple setup like this could be easily managed for small environments, but does not scale well for large ISP networks, where it is preferrable to centralize user management.
    *   Manually creating users is not scalable, requiring more advanced systems for automation.

**Detailed Explanations of Topic**

*   **Users:** User accounts in MikroTik RouterOS are used to grant individuals access to the router's configuration and functionalities. Each user is associated with a group, which determines their level of access.
*   **User Groups:** User groups allow administrators to manage permissions and access levels for multiple users at once. This makes configuration and administration easier, especially in scenarios with a large number of users.
*   **Policies:** These define what actions a user can perform (read, write, etc.) and which parts of the system they can access.

**Detailed Explanation of Trade-offs**

*   **Granular vs. Simple Policies:** More granular policies allow for fine-tuned control over user permissions but increase the complexity of management. Simple policies are easier to manage, but less secure in complex environments.
*   **Local vs. External Authentication:** Local authentication is simpler for small deployments, while external authentication (RADIUS) provides centralized management for large networks.
*   **CLI vs. Winbox vs. API:** CLI is powerful but requires more technical knowledge. Winbox is user-friendly but does not provide the fine-grain control of the CLI. API allows automation but requires programming knowledge.

**Configuration for Specific RouterOS Versions:**

*   The commands used in this document are compatible with RouterOS versions 6.48 and 7.x. There are no significant changes that affect this procedure within these RouterOS versions, with the exceptions of API access which might vary from version to version.
*   If using an older RouterOS version, review the command parameters as they might be slightly different.

This documentation provides a comprehensive guide to user and group management on MikroTik routers, suitable for an expert-level configuration in an ISP environment. Remember to test this in a sandbox environment before applying any modifications to your production network.
