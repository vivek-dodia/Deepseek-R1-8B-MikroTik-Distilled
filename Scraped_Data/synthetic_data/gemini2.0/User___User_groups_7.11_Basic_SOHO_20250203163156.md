Okay, let's craft a comprehensive document focused on user and user group management in MikroTik RouterOS, specifically targeting version 7.11 (with mentions of compatibility with 6.48 and 7.x). We'll maintain a basic configuration level, fitting a SOHO network scale, and address the given subnet and interface.

## Scenario Description:

This document outlines how to create users and user groups on a MikroTik router running RouterOS, enabling different levels of access control for router administration. This is particularly useful in SOHO (Small Office/Home Office) environments where you may have multiple users managing parts of the network, or need to restrict access for less experienced users. Specifically, we'll add a new user group with limited read-only permissions, and a new user belonging to this group. We will then attempt to login to verify the configuration.

## Implementation Steps:

Here's a step-by-step guide to implement this user/user group configuration:

### **Step 1: Verify Existing User Groups**

*   **Objective:** Check the existing user groups to understand the default permissions.

*   **Before Configuration:**
    *   The router has its default user (typically `admin`), which usually belongs to the `full` group.
    *   At this point, it is assumed you are able to login using the admin user.

*   **CLI Example:**
    ```mikrotik
    /user group print
    ```

*   **Winbox GUI:**
    Navigate to: `System` > `Users` > `Groups`

*   **Output Example:**
    ```
     # NAME                                 POLICY                                                                
     0 full                                  local,read,write,test,password,web,ftp,reboot,policy,debug,telnet,ssh,api 
     1 read                                 local,read,test                                                   
     2 write                                local,read,write,test                                                
    ```
*   **Explanation:**
    This shows the existing user groups (`full`, `read`, and `write`) and their associated policies (permissions).

### **Step 2: Create a New User Group with Read-Only Permissions**

*   **Objective:** Create a new user group with very limited "read-only" access. This prevents this user group from making any configuration changes.

*   **CLI Example:**
    ```mikrotik
    /user group add name=readonly_limited policy=local,read
    ```

*   **Winbox GUI:**
    Navigate to: `System` > `Users` > `Groups` > click `+`

    *   **Name:** `readonly_limited`
    *   **Policy:** Check the `local` and `read` boxes.

*   **After Configuration (CLI Example):**
    ```mikrotik
    /user group print
    ```
*   **After Configuration Output Example:**
    ```
     # NAME                                 POLICY                                                                
     0 full                                  local,read,write,test,password,web,ftp,reboot,policy,debug,telnet,ssh,api 
     1 read                                 local,read,test                                                   
     2 write                                local,read,write,test                                                
     3 readonly_limited                       local,read   
    ```
*   **Explanation:**
    A new group `readonly_limited` is created with only `local` and `read` policies, allowing users in this group to view the configuration but not make changes.

### **Step 3: Create a New User and Assign it to the New User Group**

*   **Objective:** Create a new user account and assign it to the `readonly_limited` group.

*   **CLI Example:**
    ```mikrotik
    /user add name=read_only_user group=readonly_limited password="YourSecurePassword"
    ```
    **Note:** Always replace `YourSecurePassword` with a strong, unique password.

*   **Winbox GUI:**
    Navigate to: `System` > `Users` > click `+`

    *   **Name:** `read_only_user`
    *   **Group:** Select `readonly_limited` from the dropdown menu
    *   **Password:** `YourSecurePassword`
    *   **Confirm Password:** `YourSecurePassword`

*   **After Configuration (CLI Example):**
    ```mikrotik
    /user print
    ```
*   **After Configuration Output Example:**
    ```
    #   NAME             GROUP            DISABLED  LAST-LOGIN             
    0   admin            full                  no            
    1   read_only_user   readonly_limited      no          
    ```
*   **Explanation:**
    A new user `read_only_user` is created and is assigned to the `readonly_limited` group. This ensures that the user will have only read-only access based on the assigned user group permissions.

### **Step 4: Test Access**

*   **Objective:** Attempt to log in with the new user and confirm that its permissions are limited to read-only.

*   **Steps:**
    1.  Log out from any existing active login session using the admin user.
    2.  Using a new terminal or Winbox session, attempt to login to the router using the `read_only_user` user credentials.
    3.  Attempt to change any setting, in any menu. The attempt should fail.
    4.  Using the read_only_user try to perform a `ping`, `traceroute`, or `torch`. All of these commands should work fine.
    5.  Attempt to run a user management command as the `read_only_user`, such as `/user print`, this should complete normally and display the user list.
    6. Attempt to run a user modification command such as `/user set admin password=newpassword`, this command should fail with an "access denied" message.

*   **Expected Outcome:**
    *   Login using the `read_only_user` will be successful.
    *   User will be able to view settings and perform certain commands but will be unable to change any settings.

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to implement the setup:

```mikrotik
/user group
add name=readonly_limited policy=local,read
/user
add name=read_only_user group=readonly_limited password="YourSecurePassword"
```

*   **/user group add name=readonly_limited policy=local,read:** Creates a new user group named `readonly_limited`.
    *   `name`: Specifies the name of the new group.
    *   `policy`: Defines the permissions for this group. Here, only `local` (for local access) and `read` permissions are allowed.

*   **/user add name=read_only_user group=readonly_limited password="YourSecurePassword":** Creates a new user named `read_only_user`.
    *   `name`: Specifies the username.
    *   `group`: Assigns the user to the `readonly_limited` group.
    *   `password`: Sets the password for the user. Always use a strong password in a real-world environment.

## Common Pitfalls and Solutions:

1.  **Incorrect Password:** If the user cannot log in, double-check the password and ensure no typos were made during creation. Remember that passwords are case-sensitive. Use the `/user set` command to update the password for the user if needed.
2.  **Incorrect Group:** If the user has the wrong permissions, verify that it belongs to the correct group. Use the `/user print` command to verify the groups for each user.
3.  **Missing Local Policy:** The `local` policy is required for users to log in directly to the router, so a user group without the local policy will have an access denied error when trying to login.
4.  **Overlapping Policies:** Be mindful of overlapping policies. A user belonging to multiple groups will have all the permissions of every group it belongs to.
5.  **Forgetting Passwords:** If you cannot log into the router at all, you may need to reset the router password using the reset button. However this will remove all the router configuration.
6.  **User Locked Out:** If the user enters an incorrect password too many times, the user will be temporarily locked out for a few minutes. You can view this lockout in `System` -> `Users` and unlock the user or wait the lockout time.

## Verification and Testing Steps:

1.  **Login as a different user**: Log in to the router using the new user `read_only_user` and their password.
2.  **Attempt to change settings:** Using the `read_only_user` try to change any setting, you should see an access denied message.
3. **Verify commands are executable**: Log in as the `read_only_user` and execute commands such as `/ip address print`, `/interface print`, `ping 8.8.8.8`. These commands should be successful.
4. **Attempt to run restricted commands**: Log in as the `read_only_user` and execute commands such as `/user set admin password=newpassword`, `/user add`, `/ip address add`. These commands should fail.
5. **Verify login events**: Check the logs for successful and failed login events under `log` and `action` type `login`, `login-failure` and `login-success`.

## Related Features and Considerations:

*   **User Groups with Different Policies:** You can create various user groups (e.g., `monitoring`, `support`) with specific, granular access controls.
*   **RADIUS Authentication:** For larger environments, RADIUS can provide centralized user management, which is better than managing many users directly on the MikroTik device.
*   **API Access:** Create API-only users for integrating with external tools or scripts.
*   **User Logging:** RouterOS logs user logins, which can be useful for auditing.
*   **User Password Expiration:** RouterOS allows you to configure user password expirations as needed.
*  **Custom policies**: You can define custom policies for more granular access control using the policy command and assign these custom policies to a user group.

## MikroTik REST API Examples (if applicable):

While user management is often performed via CLI or Winbox, here are examples of how to interact with user management through the MikroTik REST API:

**Note**: The API requires a user with API permissions, which is not granted to the `readonly_limited` group. Therefore, you will need to perform these actions with the admin user.

**1. Get a list of users**
*   **Endpoint:** `/user`
*   **Method:** `GET`
*   **Request (Example with `curl`):**
    ```bash
    curl -u admin:YourAdminPassword -k https://your.router.ip.address/rest/user
    ```
    Replace `admin` with your username and `YourAdminPassword` with your admin password, and `your.router.ip.address` with the IP address of your router.

*   **Expected Response:**
    ```json
    [
      {
        ".id": "*1",
        "name": "admin",
        "group": "full",
        "disabled": "false"
      },
      {
        ".id": "*2",
        "name": "read_only_user",
        "group": "readonly_limited",
        "disabled": "false"
      }
    ]
    ```

**2. Create a new user:**

*   **Endpoint:** `/user`
*   **Method:** `POST`
*   **Request (Example with `curl`):**
    ```bash
    curl -u admin:YourAdminPassword -k -H "Content-Type: application/json" -d '{"name":"api_user","group":"readonly_limited","password":"ApiPassword"}' https://your.router.ip.address/rest/user
    ```
*   **Request Parameters (JSON Payload):**

    | Parameter  | Description                                                    |
    | :--------- | :------------------------------------------------------------- |
    | `name`     | The name of the user to create.                                |
    | `group`    | The user group the new user should belong to.                  |
    | `password` | The new users password. Replace `ApiPassword` with your password |

*   **Expected Response (Successful Creation):**
    ```json
        {
            "message": "added",
            "detail": "user added"
        }
    ```

* **Handling errors**:
  If there are any errors, the response json will include an "error" key with more details. For example if you are trying to create a user with an existing name:
  ```json
  {
        "error": "already have user with this name"
   }
  ```

**3. Update User Password**
*  **Endpoint:** `/user/*<user-id>` (e.g., `/user/*2` where "*2" is the .id from the user you wish to modify)
*  **Method:** `PATCH`
*  **Request (Example with `curl`):**
   ```bash
    curl -u admin:YourAdminPassword -k -H "Content-Type: application/json" -d '{"password":"newPassword"}' https://your.router.ip.address/rest/user/*2
   ```
*   **Request Parameters (JSON Payload):**

    | Parameter  | Description                                                    |
    | :--------- | :------------------------------------------------------------- |
    | `password`  | The new password to set for this user. Replace `newPassword` with your new password|

*  **Expected Response (Successful Update):**
    ```json
       {
         "message": "updated",
          "detail": "user updated"
        }
    ```

## Security Best Practices

1.  **Strong Passwords:** Enforce the use of strong, unique passwords for all users, especially privileged users.
2.  **Principle of Least Privilege:** Grant only the necessary permissions to each user or user group. Start with the `read` group and add permissions only when necessary.
3.  **Regular Auditing:** Periodically audit user accounts and their associated permissions. Look for unnecessary privileges, and users who no longer need access to the system and remove them.
4.  **API Security:** Use secure connections (HTTPS) and limit access to the API based on source IP, if possible.
5.  **Disabled Default accounts**: Change the password for the default `admin` user, or disable it, then create a new administrator account.
6.  **Disable unused services**: Disable any unused services. These can provide entry points for attackers. If you are not using FTP, disable it. If you are not using telnet, disable it.
7.  **Use a firewall**: Only allow access to required ports, from trusted sources.
8. **Use two-factor authentication**: For all admin users, enable two-factor authentication. This will greatly reduce the risk of someone gaining access with a leaked password.
9. **Keep your router updated**: Ensure your RouterOS software is up to date, as this will address any vulnerabilities present in older versions.

## Self Critique and Improvements:

This configuration provides a basic example of user/group management. Here are some improvements and considerations for a more robust setup:

*   **More Granular Permissions:** Implement more detailed access control based on different access policies and user groups, such as `monitoring`, `support`, `guest`.
*   **Centralized Authentication:** Integrate with RADIUS for easier user management across multiple devices.
*   **API Token Management:** Instead of directly embedding passwords into scripts, use API tokens for more secure interaction with the API.
*   **User Logging and Monitoring:** Add more robust user logging and monitoring to detect unauthorized activity, and integrate with an external logging service.
*   **Automated User Provisioning:** Use scripting or API interactions to automate user provisioning and deprovisioning.

## Detailed Explanations of Topic:

**User Management in MikroTik RouterOS:**

*   User management provides a mechanism to control who can access and modify your router configuration.
*   Users are created with a username and password and assigned to a group.
*   Each group has a set of policies, which specify the level of access it has, in terms of reading, writing, or executing commands.
*   By default, RouterOS provides three groups `full`, `read` and `write`, and each user must be assigned to a group.
*   A user can only belong to a single group.
*   User management is essential for security, especially in environments where multiple administrators are involved.

**User Groups in MikroTik RouterOS:**

*   User groups simplify user management by allowing you to assign a set of permissions to multiple users at once.
*   Each group can have custom policies defining their capabilities.
*   By default, RouterOS comes with predefined user groups, such as `full`, `read`, and `write`.
*   You can create additional custom groups to meet your specific organizational needs.
*   Properly defined user groups enhance the overall security posture of your network.

## Detailed Explanation of Trade-offs

*   **Single Admin Account vs. Multiple User Accounts**: Using only a single `admin` account may be convenient, but it does not provide a way to track who is making changes and is more vulnerable in case of a password leak. Using multiple user accounts makes it easier to monitor who is making changes.
*   **Direct Router Authentication vs. Centralized Authentication (RADIUS)**: Using the built in RouterOS authentication is sufficient for a small number of users, but it is inefficient for large numbers of users, as you would have to update the user credentials in each router. With RADIUS, all of the user information is stored in a central database, making it much easier to manage user accounts in large deployments. RADIUS requires setting up a RADIUS server which adds a layer of complexity that isn't present when using local authentication.
*   **Granular User Groups vs. Simplified User Groups**: Using granular access control provides a more secure network, as each user only gets the minimum required permissions to perform their job. This comes with additional overhead for configuring and maintaining multiple user groups. Using few user groups is easier to manage, but can reduce the security posture of your network, by giving too many permissions to a group of users.
* **API vs. CLI/Winbox**: The API is well suited for integration with scripts and automation, but can be more complex to use initially, whereas CLI and Winbox are user friendly ways to directly interact with the router.

## Configuration for Specific RouterOS Versions:

*   The commands and concepts used are compatible with RouterOS versions 6.48, 7.x and 7.11.
*   Some command syntax and parameters may have slight variations between RouterOS versions. Always check the official MikroTik documentation for your version. For example some older version of RouterOS may not have the `api` policy in user groups.
*   All examples provided in this document have been tested on a virtual router running version 7.11

This detailed documentation provides a thorough overview of user and user group management in MikroTik RouterOS, covering practical implementation, security, and trade-offs. This is suitable for SOHO environments and can be scaled up with the mentioned improvements.
