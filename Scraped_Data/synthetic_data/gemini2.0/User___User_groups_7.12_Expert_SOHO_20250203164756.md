Okay, let's dive into configuring users and user groups on MikroTik RouterOS 7.12, focusing on expert-level implementation within a SOHO network context. We'll be using the example subnet 207.126.131.0/24 and interface `wlan-20`.

## Scenario Description:

This scenario outlines how to create and manage users and user groups on a MikroTik router. This is particularly useful for access control, logging, and different levels of administrative privileges.  We'll focus on creating a 'support' user group with limited read-only access, and two users, one in the admin group and one in the support group. This could be used, for example, to grant junior staff the ability to view the router configuration without making changes. We will then show how to disable and enable a user and how to disable user groups.

## Implementation Steps:

1.  **Step 1: Initial State - Verify Existing Users and Groups**

    *   **Explanation:** Before making changes, it's important to know the existing user and group setup. This prevents unintended configuration conflicts or loss of access.
    *   **CLI Command (Before):**
        ```mikrotik
        /user print
        /user group print
        ```
    *   **Expected Output (Example):**
        ```
        /user print
        Flags: * - disabled
        #   NAME     GROUP       PASSWORD  ADDRESS            LAST-LOGGED-IN
        0   admin    full                                     never

        /user group print
        # NAME     POLICY
        0  full  read,write,test,password,web,api,ftp,reboot,local,winbox,console
        ```
     * **Winbox GUI:**  Navigate to System > Users and System > User Groups. Review the existing list.
    *   **Effect:** This step provides a baseline view of the current user and group configuration.

2.  **Step 2: Create the 'support' User Group**

    *   **Explanation:** We'll create a new user group called 'support' with specific read-only permissions. This group will be used to limit access for the `support` user we create in a later step.
    *   **CLI Command (Configuration):**
        ```mikrotik
        /user group add name=support policy=read
        ```
    *   **CLI Command (After):**
        ```mikrotik
        /user group print
        ```
    *   **Expected Output (After):**
        ```
        /user group print
        #   NAME     POLICY
        0   full     read,write,test,password,web,api,ftp,reboot,local,winbox,console
        1   support  read
        ```
    *   **Winbox GUI:** Navigate to System > User Groups and click the '+' to add a new user group.  Set the name to 'support' and select the 'read' policy.  Click Apply then OK.
    *   **Effect:** A new user group with limited access policies is created.

3.  **Step 3: Create the 'admin' User**

    *  **Explanation:** We will create a new administrative user as good practice instead of using the default user.
    * **CLI Command (Configuration):**
        ```mikrotik
        /user add name=admin2 group=full password="SuperSecretPassword123!"
        ```
   * **CLI Command (After):**
       ```mikrotik
        /user print
       ```
   * **Expected Output (After):**
        ```
        /user print
        Flags: * - disabled
        #   NAME     GROUP       PASSWORD  ADDRESS            LAST-LOGGED-IN
        0   admin    full                                     never
        1   admin2   full                                     never
        ```
    * **Winbox GUI:** Navigate to System > Users and click the '+' to add a new user. Set the name to 'admin2', select the 'full' group, and set the password to "SuperSecretPassword123!". Click Apply then OK.
    * **Effect:** A new administrative user is created.

4.  **Step 4: Create the 'support' User**

    *   **Explanation:** We'll create a new user called 'support' and assign it to the 'support' group.
    *   **CLI Command (Configuration):**
        ```mikrotik
        /user add name=support group=support password="SupportPassword123!"
        ```
    *   **CLI Command (After):**
        ```mikrotik
        /user print
        ```
    *   **Expected Output (After):**
        ```
        /user print
        Flags: * - disabled
        #   NAME     GROUP       PASSWORD  ADDRESS            LAST-LOGGED-IN
        0   admin    full                                     never
        1   admin2   full                                     never
        2   support  support                                  never
        ```
    *   **Winbox GUI:** Navigate to System > Users and click the '+' to add a new user.  Set the name to 'support', select the 'support' group, and set a password to 'SupportPassword123!'. Click Apply then OK.
    *   **Effect:** A new user with limited read-only access is created.

5.  **Step 5: Disable User and User Group**
    *   **Explanation:** We will show how to disable the admin user, and the support group to temporarily remove all access.
    *   **CLI Command (Configuration):**
        ```mikrotik
        /user disable admin2
        /user group disable support
        ```
    * **CLI Command (After):**
         ```mikrotik
        /user print
        /user group print
         ```
    *   **Expected Output (After):**
        ```
        /user print
        Flags: * - disabled
        #   NAME     GROUP       PASSWORD  ADDRESS            LAST-LOGGED-IN
        0   admin    full                                     never
        1   *admin2   full                                     never
        2   support  support                                  never

        /user group print
        #   NAME     POLICY
        0   full     read,write,test,password,web,api,ftp,reboot,local,winbox,console
        1   *support  read
        ```
    * **Winbox GUI:** To disable, navigate to System > Users select the admin2 user and click 'disable'. Navigate to System > User Groups select 'support' user group and click disable.
    *   **Effect:** The user and group are disabled and access is revoked.

6.  **Step 6: Enable User and User Group**
    *   **Explanation:** We will show how to re-enable the admin user, and the support group to restore access.
    *   **CLI Command (Configuration):**
        ```mikrotik
         /user enable admin2
         /user group enable support
        ```
    *  **CLI Command (After):**
          ```mikrotik
         /user print
        /user group print
         ```
    *   **Expected Output (After):**
          ```
        /user print
        Flags: * - disabled
        #   NAME     GROUP       PASSWORD  ADDRESS            LAST-LOGGED-IN
        0   admin    full                                     never
        1   admin2   full                                     never
        2   support  support                                  never

        /user group print
        #   NAME     POLICY
        0   full     read,write,test,password,web,api,ftp,reboot,local,winbox,console
        1   support  read
         ```
    * **Winbox GUI:** To enable, navigate to System > Users select the admin2 user and click 'enable'. Navigate to System > User Groups select 'support' user group and click enable.
    *   **Effect:** The user and group are enabled and access is restored.

## Complete Configuration Commands:

```mikrotik
# Create the 'support' user group
/user group add name=support policy=read

# Create the 'admin2' user
/user add name=admin2 group=full password="SuperSecretPassword123!"

# Create the 'support' user
/user add name=support group=support password="SupportPassword123!"

# Disable the user 'admin2'
/user disable admin2

# Disable the group 'support'
/user group disable support

# Enable the user 'admin2'
/user enable admin2

# Enable the group 'support'
/user group enable support
```

| Parameter       | Explanation                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------|
| `/user group add` | Creates a new user group.                                                                             |
| `name`          | Specifies the name of the user group (e.g., 'support').                                             |
| `policy`        | Defines the permissions for the group. Options include `read`, `write`, `test`, `password`, `web`, `api`, `ftp`, `reboot`, `local`, `winbox`, `console`. |
| `/user add`      | Creates a new user.                                                                                   |
| `name`          | Specifies the username (e.g., 'support').                                                               |
| `group`         | Assigns the user to a specific user group (e.g., 'support').                                           |
| `password`      | Sets the password for the user.                                                                       |
| `/user disable`  | Disables the user. |
| `/user enable`   | Enables the user. |
| `/user group disable` | Disables the group. |
| `/user group enable` | Enables the group. |

## Common Pitfalls and Solutions:

*   **Lost Access:** Forgetting the admin password or disabling the admin account is a common mistake.

    *   **Solution:** Use a secure password manager, and keep a backup copy of admin credentials (if feasible, outside of the router). If you lose access you can reset the router with the reset button (losing all configuration). You can also try to access it via mac address and Winbox or serial cable.

*   **Insufficient Permissions:** Incorrect user group policy can prevent access to necessary features.

    *   **Solution:** Carefully plan user groups with appropriate permissions. Start with the least privileged needed and expand as required. Test the configuration before deploying in production.

*   **Overly Complex User Groups:** Too many user groups can be difficult to manage and audit.

    *   **Solution:** Keep the user group structure as simple as possible. Use a clear naming convention to avoid confusion. Document the purpose of each group.

*   **Weak Passwords:** Easy-to-guess passwords pose a security risk.

    *   **Solution:** Use strong, complex passwords, and consider regularly changing them. Enforce password complexity requirements.

*   **Resource Issues:** In large networks with many users the authentication process might use a lot of resources.

    *   **Solution:** Monitor CPU and memory usage. Consider using an external radius server, or user caching.

## Verification and Testing Steps:

1.  **Login as 'support' User:**
    *   Use Winbox, SSH, or the WebUI to attempt to login as 'support' using the credentials you configured.
    *   Verify that you can access the router (according to your access level). Try to make write operations to the router, and verify that you can't.
    *   **Expected Result:**  Successful read-only login.

2.  **Login as 'admin2' User:**
    *   Use Winbox, SSH, or the WebUI to attempt to login as 'admin2' using the credentials you configured.
    *   Verify that you can make write operations on the router.
    *  **Expected Result:** Successful write access.

3.  **Login using default 'admin' User:**
    *   Use Winbox, SSH, or the WebUI to attempt to login as the default 'admin' user, Verify that it can still be used for administrative tasks.
    *   **Expected Result:** Successful write access.

4. **Check logged in users:**
  *   Use the following command:
        ```mikrotik
        /user active print
        ```
  *   Verify that the users are listed.
  *   **Expected Result:** List of active users with addresses.
5. **Disable user and login again:**
    * Disable a user.
    * Try to log in.
    *  **Expected Result:** Login failed.

6.  **Disable user group and login again:**
    * Disable user group that the user is assigned to.
    * Try to log in using that user.
    *  **Expected Result:** Login failed.

## Related Features and Considerations:

*   **RADIUS Authentication:** For larger networks or centrally managed user accounts, consider using a RADIUS server for authentication. This allows for more advanced authentication methods and user account management.
*   **Logging:** Enable logging for user logins and failed attempts to audit and monitor router access.
*   **Scripting:** Use RouterOS scripting to automate user creation, updates, and password management.
*   **API Access:** If you need programmatic access to your router you will need to enable API or API-SSL access and you will also need a user that can access the API to use the API.
*   **IP Address Restrictions:** The `address` field in the `/user` configuration can be used to restrict login attempts from certain IP ranges.
*   **Hotspot Integration:** User accounts can be linked to the RouterOS hotspot functionality to control access for specific users.
*   **MAC Address Restrictions:** The `mac-address` field in the `/user` configuration can be used to restrict user to a specific client mac address.

## MikroTik REST API Examples:

While specific `user` and `user group` management endpoints aren't directly exposed in the RouterOS REST API, you can use generic commands to achieve similar functionality.

**Important Note:** The MikroTik REST API is typically used for command execution, and there are no direct object specific calls to get or set users. In the examples below we will use the `/system/routerboard/command` endpoint which gives us access to the entire ROS command line, so it must be used very carefully.

**Example 1: Create a User via API**

*   **API Endpoint:** `/system/routerboard/command`
*   **Request Method:** POST
*   **JSON Payload:**

    ```json
    {
        "command": "/user add name=apiuser group=full password=\"StrongApiPassword!\""
    }
    ```

*   **Expected Response (Success):**
    ```json
    {
        "output": [
            "!done"
        ]
    }
    ```
*   **Explanation:** This API call executes the MikroTik CLI command to create a user named 'apiuser' with `full` permissions and a specified password.
*   **Handling Errors:** If the request is not properly formatted or for invalid commands, the response would be different and contain error messages. You must always check the output array for "!done".
*   **Security Concerns:** This endpoint allows unrestricted command execution on the router and must be protected carefully.

**Example 2: Get All Users via API**

*   **API Endpoint:** `/system/routerboard/command`
*   **Request Method:** POST
*   **JSON Payload:**
    ```json
    {
        "command": "/user print"
    }
    ```

*   **Expected Response (Success):**
    ```json
    {
        "output": [
          "Flags: * - disabled",
          "#   NAME     GROUP       PASSWORD  ADDRESS            LAST-LOGGED-IN",
          "0   admin    full                                     never",
          "1   apiuser   full                                     never"
        ]
    }
    ```
*   **Explanation:** This API call executes the MikroTik CLI command to get all users.
*   **Handling Errors:** If the request is not properly formatted or for invalid commands, the response would be different and contain error messages. You must always check the output array for "!done".
*   **Security Concerns:** This endpoint allows unrestricted command execution on the router and must be protected carefully.

**Example 3: Disable a User via API**

*   **API Endpoint:** `/system/routerboard/command`
*   **Request Method:** POST
*   **JSON Payload:**
    ```json
    {
      "command": "/user disable apiuser"
    }
    ```

*   **Expected Response (Success):**
    ```json
    {
        "output": [
            "!done"
        ]
    }
    ```

*   **Explanation:** This API call executes the MikroTik CLI command to disable the user "apiuser".
*   **Handling Errors:** If the request is not properly formatted or for invalid commands, the response would be different and contain error messages. You must always check the output array for "!done".
*   **Security Concerns:** This endpoint allows unrestricted command execution on the router and must be protected carefully.

**Example 4: Enable a User via API**

*   **API Endpoint:** `/system/routerboard/command`
*   **Request Method:** POST
*   **JSON Payload:**
    ```json
    {
      "command": "/user enable apiuser"
    }
    ```

*   **Expected Response (Success):**
    ```json
    {
        "output": [
            "!done"
        ]
    }
    ```

*   **Explanation:** This API call executes the MikroTik CLI command to enable the user "apiuser".
*   **Handling Errors:** If the request is not properly formatted or for invalid commands, the response would be different and contain error messages. You must always check the output array for "!done".
*   **Security Concerns:** This endpoint allows unrestricted command execution on the router and must be protected carefully.

**Note**: While this method provides a way to perform almost any ROS function, make sure to check your api security and restrictions.

## Security Best Practices

*   **Principle of Least Privilege:** Always grant users the minimal permissions necessary for their tasks. This reduces the potential damage from compromised accounts.
*   **Strong Passwords:** Enforce strong password policies, including a mix of uppercase, lowercase, numbers, and symbols. Regularly rotate passwords.
*   **Two-Factor Authentication (2FA):** If supported, enable 2FA for admin users for an extra layer of security.
*   **Regular Auditing:** Review user accounts, groups, and policies periodically to ensure they still align with current needs.
*   **API Security:** Secure the MikroTik REST API by limiting access to specific IP addresses, and using strong credentials. Consider disabling it when not needed.
*   **Limit Login Attempts:** Implement a firewall to rate-limit failed login attempts.
*   **Avoid Default Credentials:** Never use default credentials, always change the password for the initial 'admin' user.

## Self Critique and Improvements

The current configuration provides a basic example of user management on a MikroTik device. However, the following improvements are possible:

*   **Advanced Group Policies:** We could use more granular group policies, specifically tailored to roles like monitoring, firewall rule modifications, etc.
*   **Dynamic User Groups:** In complex environments, scripts that automatically assign user groups based on external databases could be used.
*   **User Quotas:** If needed, setting user quotas for hotspot or VPN usage would improve resource management.
*   **Radius Integration:** For a more robust and scalable setup, implement a Radius server for user authentication.
*   **Centralized Logging:** Implement remote logging to a syslog server for auditing and alerting on user activity.
*  **API Command Restrictions:** Implement user specific api command restrictions if needed, as mentioned in the ROS documentation.

## Detailed Explanations of Topic

MikroTik's user and user group management system is built upon a Role-Based Access Control (RBAC) model. Users are assigned to groups which define their permissions, instead of defining permissions per user.
*   **Users:** Each user account represents an identity that can log into the router with specific credentials. Each user belongs to one and only one user group. Users have a username, password, an optional list of IP addresses from which they are allowed to login, and a flag whether is active or disabled.
*   **User Groups:** User groups have associated policies that define what operations group members can perform. For example a read policy allows the user to view the configuration but not modify it.  Groups can also be disabled, which will prevent the members from logging in.

## Detailed Explanation of Trade-offs

*   **Limited User Groups vs. Many User Groups:** Using a minimal set of groups makes it easier to manage but might lead to insufficient granularity for access control. Conversely, many user groups offer great control but introduce complexity in management and auditing.
*   **Local vs. Remote Authentication:** Local user management is simpler to set up, but it does not scale well for larger deployments. RADIUS servers offer centralized management, but introduce additional complexity and dependencies.
*   **Full Access vs. Limited Access:** Granting users full access simplifies configuration, but poses a significant security risk. Limited access follows the principle of least privilege, improving security, but it adds the overhead of proper policy definition.
*   **API Access**: If the API is needed you must have a secure environment, because the api gives complete unrestricted access to the router, if you expose the API to the internet this is a big risk and it is advisable to restrict access to certain IP ranges, or use an SSH tunnel for access. The api user must also have a strong password.

## Configuration for Specific RouterOS Versions:

The commands and configurations provided are compatible with RouterOS versions 7.12 and upwards, as well as versions 6.48 and above. However, slight variations might occur, so it's advisable to refer to the specific version's documentation for the most accurate information. Some commands may have slightly different parameters, or be available in only some versions.
If you are using a RouterOS version earlier than 6.48 you must upgrade your RouterOS to be able to use these commands.

This comprehensive documentation should provide a strong foundation for managing users and user groups on your MikroTik router.
