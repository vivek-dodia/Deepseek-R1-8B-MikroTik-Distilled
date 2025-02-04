Okay, let's craft some detailed documentation for managing users and user groups in MikroTik RouterOS, specifically targeting version 6.48 with a focus on an ISP-scale environment.

## Scenario Description

This document details how to create, manage, and organize users within a MikroTik RouterOS environment using user groups. This setup is critical for ISPs to manage access control for administrative tasks or for providing access to customer-specific services. We'll focus on the `vlan-70` interface and the subnet `159.135.87.0/24` as an example context, although the user management principles apply across different interfaces and networks. The goal is to establish a structured approach to user permissions, granting different levels of access based on group membership. This would enable easier management of several administrators with different access levels.

## Implementation Steps

Here's a step-by-step guide to implementing users and user groups using both CLI and Winbox.

### Step 1: Verify Existing Users and Groups

*   **Purpose:** Before creating new users and groups, it's good practice to see what's already configured, to avoid overwriting.
*   **CLI Command:**
    ```mikrotik
    /user print
    /user group print
    ```

    **Explanation:**
    *   `/user print` - displays all current users.
    *   `/user group print` - displays all current user groups.

*   **Winbox:**
    1.  Navigate to "System" -> "Users" to see the user list.
    2.  Navigate to "System" -> "Users" -> "Groups" tab to see user groups.

*   **Before:**
    ```
    # /user print
    0   name="admin" group=full disabled=no
    # /user group print
    0   name="full"  policy=write,test,password,read,reboot,ftp,sniff,romon
    ```
    **Effect:** The output confirms an initial admin user with full permissions, and a single group which grants all permissions.

### Step 2: Create a New User Group (Read-Only Operators)

*   **Purpose:** To establish a specific access level for read-only operators.
*   **CLI Command:**
    ```mikrotik
    /user group add name=operators-readonly policy=read,test
    ```

    **Explanation:**
    *   `/user group add` - Creates a new group.
    *   `name=operators-readonly` - Sets the group's name.
    *   `policy=read,test` - Grants only read and test permissions.

*   **Winbox:**
    1.  Navigate to "System" -> "Users" -> "Groups" tab.
    2.  Click the "+" button.
    3.  Set "Name" to `operators-readonly`.
    4.  In the "Policy" section, check "read" and "test", and no others.
    5.  Click "OK".

*   **After:**
    ```mikrotik
    # /user group print
    0   name="full"  policy=write,test,password,read,reboot,ftp,sniff,romon
    1   name="operators-readonly"  policy=read,test
    ```
    **Effect:** The new `operators-readonly` group is created with specified access.

### Step 3: Create a New User (read-operator) and Add to the Group

*   **Purpose:** To add a user that belongs to the new group, thus inheriting the group’s permission.
*   **CLI Command:**
    ```mikrotik
    /user add name=read-operator group=operators-readonly password=SecurePassword123
    ```

    **Explanation:**
    *   `/user add` - Creates a new user.
    *   `name=read-operator` - Sets the username.
    *   `group=operators-readonly` - Assigns the user to the `operators-readonly` group.
    *   `password=SecurePassword123` - Sets the initial password (always use a strong one in production).

*   **Winbox:**
    1.  Navigate to "System" -> "Users".
    2.  Click the "+" button.
    3.  Set "Name" to `read-operator`.
    4.  Set "Group" to `operators-readonly`.
    5.  Set "Password" to `SecurePassword123`.
    6.  Click "OK".

*   **After:**
    ```mikrotik
    # /user print
    0   name="admin" group=full disabled=no
    1   name="read-operator" group=operators-readonly disabled=no
    ```
    **Effect:** A new user `read-operator` is created and assigned to the read-only group.

### Step 4: Testing User Login

*   **Purpose:** To verify the user can login and has correct access rights.
*   **CLI Command:** Log in with the new user via SSH, winbox or any other allowed method.
*   **Winbox:** Try connecting to the router with `read-operator` user credentials.
*   **Verification:** After logging in with read-operator user, attempt to run configuration write command such as `/system clock set time=13:00:00`, which should return an error of `not enough rights`.

### Step 5: Create a New User Group (Full Access Operator)

*   **Purpose:** To create a user with full access with the exception of password and user permissions.
*   **CLI Command:**
     ```mikrotik
     /user group add name=operators-full policy=write,test,read,reboot,ftp,sniff,romon
    ```
    **Explanation:**
    *   `/user group add` - Creates a new group.
    *   `name=operators-full` - Sets the group's name.
    *   `policy=write,test,read,reboot,ftp,sniff,romon` - Grants all read, write, and other privileges except users and password change.

*   **Winbox:**
    1.  Navigate to "System" -> "Users" -> "Groups" tab.
    2.  Click the "+" button.
    3.  Set "Name" to `operators-full`.
    4.  In the "Policy" section, check "write", "read", "test", "reboot", "ftp", "sniff", "romon", and no others.
    5.  Click "OK".

*   **After:**
    ```mikrotik
    # /user group print
    0   name="full"  policy=write,test,password,read,reboot,ftp,sniff,romon
    1   name="operators-readonly"  policy=read,test
    2   name="operators-full"  policy=write,test,read,reboot,ftp,sniff,romon
    ```
    **Effect:** The new `operators-full` group is created with specified access.

### Step 6: Create a New User (full-operator) and Add to the Group

*   **Purpose:** To add a user that belongs to the new group, thus inheriting the group’s permission.
*   **CLI Command:**
    ```mikrotik
    /user add name=full-operator group=operators-full password=SecurePassword124
    ```

    **Explanation:**
    *   `/user add` - Creates a new user.
    *   `name=full-operator` - Sets the username.
    *   `group=operators-full` - Assigns the user to the `operators-full` group.
    *   `password=SecurePassword124` - Sets the initial password (always use a strong one in production).

*   **Winbox:**
    1.  Navigate to "System" -> "Users".
    2.  Click the "+" button.
    3.  Set "Name" to `full-operator`.
    4.  Set "Group" to `operators-full`.
    5.  Set "Password" to `SecurePassword124`.
    6.  Click "OK".

*   **After:**
    ```mikrotik
    # /user print
    0   name="admin" group=full disabled=no
    1   name="read-operator" group=operators-readonly disabled=no
    2   name="full-operator" group=operators-full disabled=no
    ```
    **Effect:** A new user `full-operator` is created and assigned to the full-access operator group.

### Step 7: Testing User Login

*   **Purpose:** To verify the user can login and has correct access rights.
*   **CLI Command:** Log in with the new user via SSH, winbox or any other allowed method.
*   **Winbox:** Try connecting to the router with `full-operator` user credentials.
*   **Verification:** After logging in with full-operator user, attempt to run configuration write command such as `/system clock set time=13:00:00`, which should apply the change. Then, attempt to execute `/user set password=` or `/user add`, which should return `not enough rights`.

## Complete Configuration Commands
```mikrotik
/user group add name=operators-readonly policy=read,test
/user add name=read-operator group=operators-readonly password=SecurePassword123

/user group add name=operators-full policy=write,test,read,reboot,ftp,sniff,romon
/user add name=full-operator group=operators-full password=SecurePassword124
```

| Command                       | Parameter               | Explanation                                                                           |
|-------------------------------|-------------------------|---------------------------------------------------------------------------------------|
| `/user group add`            | `name`                 | The name of the user group.                                                                 |
|                               | `policy`               |  Comma-separated list of permissions for this group (e.g., `read`, `write`, `test`, `password`, etc.). |
| `/user add`                   | `name`                 | The username for the new user.                                                        |
|                               | `group`                | The user group to which the user belongs.                                            |
|                               | `password`             | The user's password.                                                                  |

## Common Pitfalls and Solutions

*   **Password Complexity:** Using weak or default passwords leads to security vulnerabilities. Always use strong, unique passwords. **Solution:** Implement a strong password policy.
*   **Overly Permissive Groups:** Granting overly broad permissions (like `full` for all users) can cause unwanted configuration changes. **Solution:** Implement the principle of least privilege. Grant access only as needed.
*   **Forgetting Passwords:** If the only admin is locked out, a hard reset might be necessary. **Solution:** Keep a backup of passwords in a secure place, or consider using RADIUS for centralized authentication.
*   **User Lockout:** If users attempt too many failed logins, they can be locked out depending on your `/ip ssh settings`. **Solution:** Monitor login attempts and adjust lockout settings as needed.
*   **Incorrect Group Assignment:** Ensure users are assigned to the correct groups for appropriate access rights. Double-check before applying. **Solution:** Be very careful when selecting user groups, or consider an API that allows more automated assignment of users to groups.
*   **Lost access** If you lock yourself out of your router, you might need to reset it with the "netinstall" procedure, which might lead to data loss. **Solution**: Plan ahead for password changes and do not make changes that are hard to recover from during production hours.

## Verification and Testing Steps

*   **Log in with Different Users:** Attempt to log in via SSH or Winbox with each user to verify their access level.
    *   `read-operator` should have read-only rights.
    *   `full-operator` should have full rights except for user creation and password changing.
*   **CLI Testing:**
    *   Log in as `read-operator` and try commands like `/ip address print` (should work) and `/ip address add address=192.168.1.1/24 interface=vlan-70` (should fail with "not enough rights").
    *   Log in as `full-operator` and try the same commands (should work).
*   **Winbox Testing:** Same functionality can be verified using the winbox GUI.
*   **Activity Logging:** Review the RouterOS log (`/system logging print`) for successful and failed login attempts.

## Related Features and Considerations

*   **RADIUS Authentication:** Use a RADIUS server to authenticate users for increased security and centralized user management.
*   **User Profiles:** Profiles can define resource usage limitations such as bandwidth limits, and are applied per user. This is relevant to Hotspot configurations.
*   **SSH Keys:** Configure SSH key-based authentication for more secure access, instead of passwords.
*   **API Access Control:** Control API access with the correct user permissions.
*   **Scripting:** Automation of user creation and maintenance can be achieved by using Mikrotik scripting capabilities.

## MikroTik REST API Examples

**Note:** While user and group management *can* be done via the API, it is strongly discouraged in production environments due to the sensitive nature of credentials. API endpoints should always be protected with strong authentication and authorization. **Use with caution.**

These examples assume you are using a MikroTik RouterOS with API enabled and proper authorization via user and password or token:
```
# Create a user group named 'api-readonly'
# API endpoint: /user/group
# Request Method: POST
curl -k -u 'api_user:api_password' -X POST -H "Content-Type: application/json" -d '{
  "name": "api-readonly",
  "policy": "read,test"
}' https://your-router-ip/rest/user/group

# Expected Response (Success)
# 201 Created with a JSON body
# {"id": "*1"}

# Create a user named 'api-user' in the 'api-readonly' group.
# API endpoint: /user
# Request Method: POST
curl -k -u 'api_user:api_password' -X POST -H "Content-Type: application/json" -d '{
  "name": "api-user",
  "group": "api-readonly",
  "password": "SecureAPIUserPassword123"
}' https://your-router-ip/rest/user

# Expected Response (Success)
# 201 Created with a JSON body
# {"id": "*2"}

# Retrieve the list of user groups
# API endpoint: /user/group
# Request Method: GET
curl -k -u 'api_user:api_password' https://your-router-ip/rest/user/group

# Expected Response (Success)
# 200 OK with a JSON array
# [
#   {"id":"*0","name":"full","policy":"write,test,password,read,reboot,ftp,sniff,romon"},
#   {"id":"*1","name":"api-readonly","policy":"read,test"}
#  ]

# Handle Errors
# If an error happens during API call, such as "not enough rights", it returns an http status code such as 403, along with a json error description
# {"message":"not enough rights"}

```

**Parameter Explanation:**

| Parameter            | Description                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------|
| `name`               | The name of the user or user group.                                                                                  |
| `group`              | The user group to which the user belongs. (For user creation)                                                        |
| `password`           | The password for the user. (For user creation)                                                                      |
| `policy`             | Comma-separated list of permissions for the user group (For user group creation)                                    |

## Security Best Practices

*   **Strong Passwords:** Always use strong, unique passwords for all users.
*   **Limit User Permissions:** Grant users the minimal level of access necessary for their tasks.
*   **HTTPS for API:** If using API access, make sure HTTPS is enabled to encrypt the communication.
*   **Disable Default Admin:** Rename or disable the default admin account when possible (not advisable in some scenarios).
*   **Regular Audits:** Periodically review user accounts and permissions to identify and remove any unnecessary access.
*   **Remote Access:** Limit the IP ranges which can access the router remotely using the `/ip service` configuration settings.
*   **Log Analysis**: Monitor the log files regularly for unusual login attempts, especially for failed login attempts with valid usernames.

## Self Critique and Improvements

This documentation provides a good starting point for user and group management in MikroTik RouterOS. However, some areas could be improved:

*   **More Detailed Troubleshooting:** Provide more granular troubleshooting examples of what could happen in specific scenarios.
*   **API Call Security:** The API security section should be more elaborate and contain additional precautions for a live system.
*   **Real-World Usage:** Add examples of using user groups for different purposes, such as granting restricted access to Hotspot users or for specific network administrators.
*   **RADIUS Integration:** Provide full examples for RADIUS server integration.
*   **User Profiles** Add real world examples that use user profiles, and how user profiles and groups can work together.

## Detailed Explanations of Topic

MikroTik RouterOS user management revolves around the concepts of *users* and *user groups*.

*   **Users:** Represent individual accounts that can log in to the router and interact with it based on their granted permissions.
*   **User Groups:** Define a set of permissions that can be applied to multiple users, making it easier to manage access control. User groups are applied to users, which inherit the permissions.

These two concepts are closely linked as users are assigned to groups, and the user’s permissions are then derived by what is allowed for their respective group.  The groups are defined by their policy, which dictates what a user can and cannot do on the router.

RouterOS permissions:
* **read** – view the router’s configuration.
* **write** – modify the router’s configuration.
* **test** – test some of the network and system tools.
* **password** – change the passwords of other users.
* **reboot** – reboot the router.
* **ftp** – upload/download files to the router.
* **sniff** – use packet sniffer tool.
* **romon** – use Router Management Protocol.

User and group management are core security features of RouterOS, and correctly setting them up is essential to protect the device from misuse or attacks, especially on a public facing system.

## Detailed Explanation of Trade-offs

When designing user and group policies, there are several trade-offs to consider:

*   **Granularity vs. Management Overhead:**  Highly granular permissions can provide the best security but can also increase the management overhead. On the other hand, overly broad permissions make things simpler to administer but may introduce security risks. The key is to find a balance that makes sense for your environment.
*   **Single Group vs. Multiple Groups:**  Using a single, all-encompassing group can simplify user management, but will also provide all users with the same access. On the contrary, multiple groups with different access levels allow better access control but can complicate administration if not organized properly.
*   **Local Users vs. RADIUS:** Local users are easier to configure but might not be suitable for complex environments or for environments that need centralized authentication. RADIUS servers add complexity but are far more scalable, secure and provide greater control over user management.
*   **CLI vs. Winbox:** The CLI provides more control and allows automation via scripts, but it is also more complex to learn. The Winbox GUI is user friendly but may not have all the available options of the CLI, especially for more complex features.
*   **API Management**: While the API provides an automated way of managing users and groups, this is a highly complex configuration to manage. Exposing a public facing API will also open new attack vectors for those looking for vulnerabilites.

## Configuration for Specific RouterOS Versions

This configuration is primarily targeting RouterOS 6.48.  Most commands related to user and group management will work in most RouterOS 6.x versions as well as v7. However, there are some caveats to consider when dealing with specific versions:

*   **Version Differences:** Some minor changes may be found in how certain functions of the API and scripting works.
*   **Security Fixes:** Newer versions might have security fixes, while some older features or functionalities can be deprecated.
*   **Function Deprecation:** Some very old features can be deprecated and not exist in newer versions.

It's always a good idea to consult the specific RouterOS changelogs for the versions you are working with.

This extensive documentation should provide a solid foundation for implementing and managing users and user groups in your MikroTik RouterOS environment. Remember to always test changes in a controlled environment before applying them to a live system and to carefully follow security best practices.
