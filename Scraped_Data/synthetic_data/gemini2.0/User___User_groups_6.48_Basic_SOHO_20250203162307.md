Okay, let's create some detailed documentation for managing users and user groups on a MikroTik router running RouterOS 6.48 (compatible with 7.x), focusing on a basic SOHO setup with VLAN 99.

## Scenario Description:

We'll configure a simple user and user group on a MikroTik router to manage login access. We will have a user with restricted access and a user with full access to the system. This is a very basic and common practice in a SOHO setting. The router will have a VLAN interface called `vlan-99` configured, although that is not directly relevant to user/group management. We will focus on creating users and groups and assigning the proper permissions to each.

## Implementation Steps:

### Step 1: Verify Initial User Configuration

*   **Explanation:** Before making changes, let's see the existing users. The default user "admin" usually exists with full permissions.  This step helps us understand the current state.
*   **CLI Command (Before):**
    ```mikrotik
    /user print
    ```
*   **Expected Output (Example):**
    ```
    0    admin   active  group=full    
    ```
*   **Winbox GUI:** Go to *System* -> *Users* - look at the users list.
*   **Effect:** Displays a list of all configured users and their basic properties.

### Step 2: Create a User Group

*   **Explanation:** We'll create a user group named "limited-access" with restricted permissions. This helps group users and apply permissions in a more scalable way.
*   **CLI Command:**
    ```mikrotik
    /user group add name=limited-access policy=read,write,test
    ```
* **Winbox GUI:** Go to *System* -> *Users* -> *Groups* and click "+". Type in the name `limited-access` and check the appropriate boxes (`read`, `write`, `test`).
*   **Effect:** This command creates a new user group named `limited-access` with a subset of permissions.

### Step 3: Create a Restricted User

*   **Explanation:** We'll create a new user named "limiteduser" and associate it with the `limited-access` group. This user will not have full control.
*   **CLI Command:**
    ```mikrotik
    /user add name=limiteduser password=SecurePassword group=limited-access
    ```
    *Replace `SecurePassword` with a strong password.*
*  **Winbox GUI:** Go to *System* -> *Users* and click "+". Type in the name `limiteduser`, select the `limited-access` group and provide a `Password`.
*   **Effect:** A new user is created with the specified credentials and group membership.

### Step 4: Create a User with Full Access

*   **Explanation:** We'll create a new user named "fullaccessuser" and associate it with the full group (usually created by default).
*   **CLI Command:**
    ```mikrotik
    /user add name=fullaccessuser password=AnotherStrongPassword group=full
    ```
    *Replace `AnotherStrongPassword` with a strong password.*
* **Winbox GUI:** Go to *System* -> *Users* and click "+". Type in the name `fullaccessuser`, select the `full` group and provide a `Password`.
*   **Effect:** A new user is created with the specified credentials and full group membership.

### Step 5: Verify User Configuration (Post-Changes)

*   **Explanation:** Let's see the current user configuration after applying the changes.
*   **CLI Command (After):**
    ```mikrotik
    /user print
    ```
*   **Expected Output:**
    ```
     0    admin        active  group=full     
     1    limiteduser    active  group=limited-access
     2    fullaccessuser active  group=full
    ```
*   **Winbox GUI:** Go to *System* -> *Users* - check the users list.
*   **Effect:** Displays the current users, showing that "limiteduser" belongs to the "limited-access" group and "fullaccessuser" belongs to the "full" group.

### Step 6: Verify User Group Configuration

*   **Explanation:** Let's see the current user group configuration after applying the changes.
*   **CLI Command:**
    ```mikrotik
    /user group print
    ```
*   **Expected Output:**
    ```
    0    full     policy=read,write,test,password,web,api,ftp,reboot,romon,winbox,local,telnet,ssh
    1    limited-access policy=read,write,test
    ```
*   **Winbox GUI:** Go to *System* -> *Users* -> *Groups* - check the list of groups.
*   **Effect:** Displays the current user groups, and permissions.

## Complete Configuration Commands:

```mikrotik
/user group
add name=limited-access policy=read,write,test

/user
add name=limiteduser password=SecurePassword group=limited-access
add name=fullaccessuser password=AnotherStrongPassword group=full

/user print
/user group print
```

| Command                   | Parameter         | Explanation                                                                  |
| ------------------------- | ----------------- | ---------------------------------------------------------------------------- |
| `/user group add`         | `name`            | Name of the user group to create                                            |
|                           | `policy`          | Comma-separated list of permissions for the group (e.g., read, write, test)  |
| `/user add`               | `name`            | User login name.                                                             |
|                           | `password`        | User password (store securely).                                               |
|                           | `group`           | Name of the user group to which the user belongs.                             |
| `/user print`             | N/A           | Prints a list of existing users.                                    |
| `/user group print`        | N/A          | Prints a list of existing user groups and their policies.                            |

## Common Pitfalls and Solutions:

*   **Pitfall:** Forgetting a user's password.
    *   **Solution:** Reset the user's password via the admin user or via serial console/netinstall.
*   **Pitfall:** Accidentally assigning incorrect permissions to a user group.
    *   **Solution:**  Carefully review the `policy` parameter. Double check permissions. Test user login and capabilities.
*   **Pitfall:** User locked out due to failed login attempts.
    *   **Solution:** Check `/system resource print` for failed logins in the logs.  Increase the `login-delay-threshold` to avoid lockouts.
*   **Pitfall:** Trying to modify the "admin" user when it is the only way to access the router.
   *  **Solution:**  Create a new admin user, make sure it has all privileges. Test the user account before modifying or disabling the admin user.

## Verification and Testing Steps:

1.  **Login with `limiteduser`:**
    *   Try to login via Winbox or SSH with `limiteduser` credentials. Verify that you have limited options/permissions.
2.  **Login with `fullaccessuser`:**
    *   Try to login via Winbox or SSH with `fullaccessuser` credentials. Verify that you have all the available options/permissions.
3.  **User Print CLI:**
    *   Run `/user print` and check if the user info is displayed correctly.
4.  **User Group Print CLI:**
   *   Run `/user group print` and verify the permissions for each group.
5.  **Resource Monitoring**
    *   Check CPU and memory usage using `/system resource print`. If high usage is detected, check the amount of active sessions and consider increasing the resources or limiting user sessions.

## Related Features and Considerations:

*   **User Sessions:** Limit concurrent user logins using `/user settings set max-user-sessions=X` where `X` is the number of users.
*   **RADIUS Authentication:** For centralized user authentication in larger networks.
*   **User Groups for Hotspots and VPN:** Can use user groups to define specific user access levels within those services.
*   **API Access:** User permissions control access to the RouterOS API, which is critical for automated management.
*   **Logging:** Log user logins/logout, `/system logging add topics=user` to monitor user activity.

## MikroTik REST API Examples (if applicable):

Unfortunately, the MikroTik REST API (introduced in RouterOS 7) is not available in 6.48. We can use command execution via `/tool fetch` and scripting. Here is a way to execute the command with a fetch:

```mikrotik
/tool fetch url="http://192.168.88.1/rest/user" http-method=post \
    http-header-field="Content-Type: application/json,Authorization: Bearer token" \
    http-data="{\"name\":\"apiuser\", \"password\":\"SecurePassword\", \"group\":\"full\"}"
```
*Replace `http://192.168.88.1` with the router's IP and the `token` with an actual api generated token, generated as explained below.*

### API Usage in RouterOS 7:
**Note**: We will give the example of API calls using RouterOS 7.x, as that is when API was implemented.

*   **Endpoint:** `/user`
*   **Method:** POST

**Create a new user:**
```bash
curl -k -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your_api_token" \
-d '{
    "name": "apiuser",
    "password": "SecurePassword",
    "group": "full"
    }' \
    "https://192.168.88.1/rest/user"
```
*   **Explanation:**
    *   `-k`:  (This parameter is important if your API does not have a valid HTTPS certificate. It should be removed for production.)
    *   `-X POST`:  Uses the POST method.
    *   `-H "Content-Type: application/json"`: Sets the content type as JSON.
    *   `-H "Authorization: Bearer your_api_token"`: Sets the API authorization token.
    *   `-d '{...}'`:  JSON data payload with user details.
    *   `"https://192.168.88.1/rest/user"`: API Endpoint (Router IP must be updated)

*   **Example JSON payload:**
    ```json
    {
      "name": "apiuser",
      "password": "SecurePassword",
      "group": "full"
    }
    ```

*   **Expected Response (Success 200 OK):**
    ```json
     {
        ".id": "*2",
        "name": "apiuser",
        "group": "full",
        "disabled": false
     }
    ```

*   **Expected Response (Error 400 Bad Request):**
    ```json
    {
       "error": "group must be a valid reference"
    }
    ```
*   **Handling Errors:** Verify the content of the response, and review the json error message. You must check for common problems with group names, or invalid passwords.

**Generate API Token**:

1.  Go to *System* > *Users* in Winbox or `/user print` in the terminal
2.  Select the user that should be used for API access (e.g. "admin")
3.  Click *Generate API Token*
4.  A token will appear on screen (or terminal output) copy and save this token.
5.  The token must be sent as an "Authorization" header: `"Authorization: Bearer token"`

## Security Best Practices

*   **Strong Passwords:** Always use strong, unique passwords for all user accounts.
*   **API Token Security:** Store API tokens securely and revoke if compromised.
*   **Limit Access:** Grant minimal necessary permissions to users and user groups.
*   **Monitor Logs:** Regularly review user login logs for any suspicious activity.
*   **Disable Unused Users:** If possible disable or remove unused user accounts.
*   **Password Aging:** Implement password aging policies for improved security.
*   **Disable Telnet:** Telnet is not secure and should not be used if possible.
*   **HTTPS API Access:** Configure API access using HTTPS with a valid certificate.
*   **Restricted Access:** Limit API access to trusted networks/IP ranges.

## Self Critique and Improvements

*   **Improvements:**
    *   More advanced user permissions with granular control can be implemented with `/user policy`.
    *   RADIUS integration could be added for centralized user management.
    *   Integration with a logging server could improve monitoring user activity.
    *   More secure authentication mechanisms (like SSH keys) for SSH users.
*   **Critique:**
    *   The configuration is basic and assumes a small number of users.
    *   It lacks the more complex permission control features of MikroTik.
    *   It does not go into very deep into the user rights.
*   **Future Steps**
    *  Add example of using user groups to control vpn access.
    *   Add examples of creating a user with access to only specific router functions.
    *   Add example of how to create a user with only read access to configuration, useful for monitoring.
    *   Add more complex examples of user groups, with more granular permissions.
    *   Add a more complete section regarding how to secure the router and API access.

## Detailed Explanations of Topic

### MikroTik Users
MikroTik users allow for access control to the router's configuration and management. Users can be created with different permission levels. A user can belong to one group which defines its permissions.

### MikroTik User Groups

MikroTik user groups are used to organize users and apply specific policies (permissions) to the group. This avoids configuration duplication. Each user belongs to a specific group, which defines their access rights.

*   `read`: Permits users to view configuration settings.
*   `write`: Allows users to modify configurations.
*   `test`: Allows users to use diagnostic tools such as ping or traceroute.
*   `password`: Allows users to change their own password.
*   `web`: Allows users to access the web interface.
*   `api`: Allows users to access the API.
*   `ftp`: Allows users to access the FTP server.
*   `reboot`: Allows users to reboot the router.
*   `romon`: Allows users to use the RouterBOOT monitor.
*   `winbox`: Allows users to use the Winbox interface.
*   `local`: Allows access to the terminal and scripts on the router.
*   `telnet`: Allows access to the telnet protocol.
*   `ssh`: Allows access to the ssh protocol.
*   `policy`: Allows the user to define a specific permission policy for the user.

## Detailed Explanation of Trade-offs

*   **Granular Permissions vs. Simplified Management:** Creating more specific user groups with fine-grained permissions adds complexity but increases security. Choosing between simplicity and security depends on the network size and security needs.
*   **Local User vs. RADIUS:** Local users are suitable for smaller environments, while RADIUS is better for larger networks requiring centralized authentication. The trade-off is increased complexity for RADIUS setup vs. the manageability and scalability of RADIUS based solutions.
*   **API Access:** API access is very powerful but must be handled with extreme care and can be a big security risk if not secured. The trade-off is between automation and security, with the need to implement strong authentication and authorization mechanisms.
*   **Password Complexity and Rotation:** Longer, more complex passwords are harder to crack but also harder to remember. Implementing password aging policies adds security but can lead to user frustration. The trade-off is ease of use versus security.
*   **Limiting User Sessions:** Limiting the maximum number of concurrent user sessions can prevent resource exhaustion and is important when a large number of concurrent users are expected to access the router. However, it may affect availability if users are frequently connecting and disconnecting.

## Configuration for Specific RouterOS Versions:

This configuration is suitable for RouterOS 6.48 and 7.x. There should be no differences in this configuration between those two versions. RouterOS 6.48 uses `/user` for its user and group management. RouterOS 7 uses the same basic commands, with added functionality.  API is available starting with 7.x.

This documentation should provide a comprehensive guide for basic user and user group management on a MikroTik router using RouterOS 6.48, while also including considerations for newer versions. Remember to replace placeholders like passwords with strong, unique values, and always test changes in a controlled environment before deploying to a production network.
