Okay, let's dive into configuring users and user groups on MikroTik RouterOS 7.11, tailored for an ISP-like environment. This configuration will focus on providing different levels of access to different administrators using local authentication.

## Scenario Description

We aim to create different user accounts with varying privileges on our MikroTik router for staff administration. Instead of giving the same full admin privileges, we create specific users within groups that have specific read or write permissions. This approach aligns with the principle of least privilege, improving security and reducing the risk of accidental or malicious misconfigurations.

## Implementation Steps

Here's a step-by-step guide with CLI examples, explanations, and before/after effects:

**1. Step 1: Initial User State (Before Configuration)**

* **Description:** Before starting, let's verify the current list of users on the router. Usually, there's only the default 'admin' user.
* **CLI Command:**

```mikrotik
/user print
```
* **Example Output (Before):**
```
 #   NAME        GROUP    DISABLED LAST-LOGIN-FROM        
 0   admin       full     no       192.168.88.1
```

* **Explanation:** The output shows one user named "admin" belonging to the "full" group with no last login time.
* **Winbox GUI:** Navigate to *System* -> *Users* to view the same information.

**2. Step 2: Create a Read-Only User Group**

* **Description:** We will create a new user group, named "readonly", that has limited read-only access to the router.
* **CLI Command:**

```mikrotik
/user group add name=readonly policy=read
```

* **Explanation:**
    * `add name=readonly`: Creates a new user group named "readonly".
    * `policy=read`:  Specifies the group's access policy as "read" , limiting access to read only functions.
* **CLI Command:**

```mikrotik
/user group print
```

* **Example Output (After):**
```
#   NAME      POLICY        
0   full      local,telnet,ssh,reboot,read,write,test,password
1   readonly  read
```
* **Effect:** A new group named "readonly" is created with only read permissions.
* **Winbox GUI:** Navigate to *System* -> *Users* -> *Groups* to view the changes.

**3. Step 3: Create a Read-Write User Group with specific permissions**

* **Description:** Now we will create a new user group that has read/write access with a more specific set of permissions.
* **CLI Command:**

```mikrotik
/user group add name=support policy="read,write,test,password"
```

* **Explanation:**
    * `add name=support`: Creates a new user group named "support".
    * `policy="read,write,test,password"`: Grants the support group read, write, test, and password changing permissions, while excluding other sensitive permissions like reboot.
* **CLI Command:**
```mikrotik
/user group print
```
* **Example Output (After):**
```
#   NAME      POLICY
0   full      local,telnet,ssh,reboot,read,write,test,password
1   readonly  read
2   support   read,write,test,password
```
* **Effect:** A new group named "support" is created with only read, write, test, and password change permissions.
* **Winbox GUI:** Navigate to *System* -> *Users* -> *Groups* to view the changes.

**4. Step 4: Create a User in the Read-Only Group**

* **Description:** We will create a user named "monitor" and assign them to the "readonly" group with a password.
* **CLI Command:**

```mikrotik
/user add name=monitor group=readonly password="your_read_only_password"
```

* **Explanation:**
    * `add name=monitor`: Creates a new user named "monitor".
    * `group=readonly`: Assigns the user to the "readonly" group.
    * `password="your_read_only_password"`: Sets the user's password. **Replace `"your_read_only_password"` with a strong, unique password.**
* **CLI Command:**
```mikrotik
/user print
```
* **Example Output (After):**
```
#   NAME      GROUP    DISABLED LAST-LOGIN-FROM
0   admin     full     no       192.168.88.1
1   monitor   readonly no
```
* **Effect:** A new user called "monitor" has been created and belongs to the readonly group.
* **Winbox GUI:** Navigate to *System* -> *Users* to view the changes.

**5. Step 5: Create a User in the Support Group**

* **Description:** Create a new user named "techsupport" and assign it to the "support" group with a password.
* **CLI Command:**

```mikrotik
/user add name=techsupport group=support password="your_support_password"
```

* **Explanation:**
    * `add name=techsupport`: Creates a new user named "techsupport".
    * `group=support`: Assigns the user to the "support" group.
    * `password="your_support_password"`: Sets the user's password. **Replace `"your_support_password"` with a strong, unique password.**
* **CLI Command:**
```mikrotik
/user print
```
* **Example Output (After):**
```
#   NAME         GROUP    DISABLED LAST-LOGIN-FROM
0   admin        full     no       192.168.88.1
1   monitor      readonly no
2   techsupport  support  no
```
* **Effect:** A new user called "techsupport" has been created and belongs to the support group.
* **Winbox GUI:** Navigate to *System* -> *Users* to view the changes.

**6. Step 6: Disable the Default `admin` User**

* **Description:** For security purposes it is recommended to disable the default 'admin' user, and create another full user. Create a user named *superadmin* and assign it to the "full" group, setting its password and disabling the old *admin* user.
* **CLI Command:**

```mikrotik
/user add name=superadmin group=full password="your_full_admin_password"
/user disable admin
```

* **Explanation:**
    * `add name=superadmin group=full password="your_full_admin_password"`: Create a new user with a complex password and assign the user to the *full* group. **Replace `"your_full_admin_password"` with a strong, unique password.**
     * `disable admin`: Disables the "admin" user.
* **CLI Command:**
```mikrotik
/user print
```
* **Example Output (After):**
```
#   NAME        GROUP    DISABLED LAST-LOGIN-FROM
0   admin       full     yes       192.168.88.1
1   monitor     readonly no
2   techsupport support  no
3   superadmin  full    no
```
* **Effect:** The default *admin* user is disabled and a new administrator user *superadmin* has been created.
* **Winbox GUI:** Navigate to *System* -> *Users* to view the changes.

## Complete Configuration Commands

```mikrotik
/user group add name=readonly policy=read
/user group add name=support policy="read,write,test,password"
/user add name=monitor group=readonly password="your_read_only_password"
/user add name=techsupport group=support password="your_support_password"
/user add name=superadmin group=full password="your_full_admin_password"
/user disable admin
```

## Common Pitfalls and Solutions

* **Forgotten Passwords:** Implement a password recovery process. MikroTik doesn't offer direct password recovery; a hard reset or Netinstall might be required. Note that the password can be changed from another user, but that user will need higher privileges to do so.
* **Overly Permissive Groups:** Review group policies carefully. Do not provide users with more access than necessary.
* **Account Lockouts:** If a user enters an invalid password multiple times, their login attempt may be rejected for some time to prevent brute-force attacks. This behaviour is controlled by the `/system security` settings. Check that your IP address is not blocked for SSH access in `/ip firewall address-list`.
* **Insecure Passwords:** Use complex, unique passwords for all user accounts.
* **Resource Issues:**  Creating a large number of users doesn't generally lead to significant resource usage unless the number of connected users is very high. If you are having performance issues, review the active connections and log output in the terminal.
* **Security Issues:**  Exposing your admin interface through the internet can be dangerous. Limit access to the interface using firewall rules and VPN connections.

## Verification and Testing Steps

1.  **Login with `monitor` user:**
    *   Attempt to log in via Winbox or SSH with the `monitor` user and its password.
    *   Verify the user cannot make any changes or view any settings that are not permitted through the read-only access.
2.  **Login with `techsupport` user:**
    *   Attempt to log in via Winbox or SSH with the `techsupport` user and its password.
    *   Verify the user can modify settings as per the assigned permissions (read/write/test/password)
3.  **Login with `superadmin` user:**
    *   Attempt to log in via Winbox or SSH with the `superadmin` user and its password.
    *   Verify the user has full administrative privileges.
4.  **Login with `admin` user:**
    *   Attempt to log in via Winbox or SSH with the `admin` user.
    *   Verify login fails due to disabled account.
5. **CLI User Verification**
    *   Run `/user print` to show the configured user information.
    *   Run `/user group print` to show the configured group information.

## Related Features and Considerations

*   **RADIUS Authentication:** For larger networks, use RADIUS for centralized user management. Use `/radius` and `/ppp secret` menus for its configuration.
*   **Remote Access Control:** Configure firewall rules to limit access to the router management interface (Winbox, SSH, WebFig). The `/ip firewall filter` and `/ip firewall address-list` menu items are of help.
*   **Logging:** Enable logging for user actions to audit and identify potential issues. Use `/system logging` for configuration.

## MikroTik REST API Examples

**Note:** The RouterOS REST API requires enabling the API service first (`/ip service enable api`). This section assumes you're familiar with using an HTTP client like `curl` or `Postman`.

**1. Create a User Group**

* **Endpoint:** `https://<router_ip>/rest/user/group`
* **Method:** POST
* **Request JSON Payload:**
```json
{
  "name": "network_admin",
  "policy": "local,read,write,test,password"
}
```
* **Example `curl` Command:**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -u "superadmin:your_full_admin_password" \
  -d '{
  "name": "network_admin",
  "policy": "local,read,write,test,password"
  }' \
  https://<router_ip>/rest/user/group
```
* **Successful Response (200 OK):**
```json
{
    ".id": "*1",
    "name": "network_admin",
    "policy": "local,read,write,test,password"
}
```
* **Error Response Example (Bad Request, missing parameters):**
```json
{
    "message": "invalid value for argument name (missing value)"
}
```

**2. Create a User**
*   **Endpoint:** `https://<router_ip>/rest/user`
*   **Method:** POST
*   **Request JSON Payload:**
```json
{
  "name": "network_admin_user",
  "group": "network_admin",
  "password": "a_strong_password"
}
```
* **Example `curl` Command:**
```bash
curl -X POST \
    -H "Content-Type: application/json" \
    -u "superadmin:your_full_admin_password" \
    -d '{
        "name": "network_admin_user",
        "group": "network_admin",
        "password": "a_strong_password"
    }' \
  https://<router_ip>/rest/user
```
* **Successful Response (200 OK):**
```json
{
    ".id": "*2",
    "name": "network_admin_user",
    "group": "network_admin",
    "password": "a_strong_password",
    "disabled": "no",
    "last-login-from": ""
}
```
* **Error Handling:** Always check the HTTP status code and the JSON response body for errors. Handle specific errors such as `400 Bad Request`, `401 Unauthorized`, etc.

**3. Get a User List**
*   **Endpoint:** `https://<router_ip>/rest/user`
*   **Method:** GET
* **Example `curl` Command:**
```bash
curl -X GET \
  -u "superadmin:your_full_admin_password" \
  https://<router_ip>/rest/user
```
* **Successful Response (200 OK):**
```json
[
  {
    ".id": "*0",
    "name": "admin",
    "group": "full",
    "disabled": "yes",
    "last-login-from": "192.168.88.1"
  },
  {
      ".id": "*1",
      "name": "monitor",
      "group": "readonly",
      "disabled": "no",
      "last-login-from": ""
  },
  {
    ".id": "*2",
      "name": "techsupport",
      "group": "support",
      "disabled": "no",
      "last-login-from": ""
  },
    {
        ".id": "*3",
        "name": "superadmin",
        "group": "full",
        "disabled": "no",
        "last-login-from": ""
    },
    {
       ".id": "*4",
       "name": "network_admin_user",
        "group": "network_admin",
        "disabled": "no",
        "last-login-from": ""
    }
]
```

**4. Get a User Group List**
*   **Endpoint:** `https://<router_ip>/rest/user/group`
*   **Method:** GET
* **Example `curl` Command:**
```bash
curl -X GET \
  -u "superadmin:your_full_admin_password" \
  https://<router_ip>/rest/user/group
```
* **Successful Response (200 OK):**
```json
[
  {
    ".id": "*0",
    "name": "full",
    "policy": "local,telnet,ssh,reboot,read,write,test,password"
  },
  {
    ".id": "*1",
    "name": "readonly",
    "policy": "read"
  },
  {
      ".id": "*2",
      "name": "support",
      "policy": "read,write,test,password"
  },
 {
    ".id": "*3",
    "name": "network_admin",
    "policy": "local,read,write,test,password"
 }
]
```

## Security Best Practices

*   **Disable Default `admin`:** As shown in the example, disable the default admin user and use a custom admin account with a strong password.
*   **Strong Passwords:** Enforce the use of strong, unique passwords for all accounts.
*   **Principle of Least Privilege:** Grant users only the minimum permissions necessary to perform their duties.
*   **Regular Audits:** Periodically review user accounts and permissions.
*   **API Access Control:** Restrict API access to specific IP addresses or networks. Use `/ip firewall filter` rules.
*   **Secure Communication:** Use HTTPS for API access to encrypt data transfer.
*   **Firewall:** Implement robust firewall rules to block unauthorized access to the router.
*   **Two-Factor Authentication (2FA):** Use 2FA for additional security, especially for high-privilege accounts. This can be configured in `/user settings` using the `2fa-secret` option.
*   **Password Complexity Rules:** Enforce password complexity using a RADIUS server, if applicable.
*   **Regular Updates:** Keep your RouterOS updated with the latest version to patch security vulnerabilities.
*   **Logging:** Enable user logs and review them regularly to detect any suspicious activity.

## Self Critique and Improvements

*   **User Group Policies:** Currently, group policies are somewhat generic.  For more granular control, it might be beneficial to investigate the use of the `policy` parameter to refine each groups permissions.
*   **RADIUS Integration:** While we used local authentication here, moving to a RADIUS server would provide much more robust management of users, especially at scale.
*   **Audit Logging:** In the current configuration, no detailed audit logging was added. Further implementation using `/system logging` would provide much needed security information.
*   **API Rate Limiting:** The REST API example is open, without rate limiting or authentication restrictions. Adding rate limits or firewall rules to the REST API would be necessary in production environments.
*  **Password Reset:** The only way to reset a user password for now is to either log in with the current username and password, or to log in with a user with the "password" permission. For a more robust password reset strategy, consider an implementation with a script using the MikroTik API.

## Detailed Explanations of Topic

The `user` management features in MikroTik RouterOS allow administrators to create different user accounts with specific sets of permissions. This approach helps implement the principle of least privilege, improving security and manageability.

**User Groups:**

*   User groups allow for the grouping of users with the same sets of permissions.
*   Each group has a `policy` that defines what actions the members of the group can perform.
*   Available policy options include: `read`, `write`, `test`, `password`, `reboot`, `local`, `telnet`, `ssh`, `ftp`, `web`, and `api`.
*   Groups help in providing consistent permission levels to multiple users at once.

**Users:**

*   Users are individual accounts created on the router.
*   Each user belongs to one user group and inherits the privileges of that group.
*   Users have a username and a password for authentication.
*   The administrator can configure additional security options such as two-factor authentication (2FA), and can disable the accounts.

**Configuration:**

*   User and user groups can be created, modified, and deleted through both CLI and Winbox GUI.
*   The API allows for programatic administration of user accounts and groups.
*   For high traffic environments, administrators must pay special attention to the number of concurrently active users, as this affects the resource utilisation in the router.

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:** Local authentication is simpler to set up, suitable for smaller environments but can be difficult to scale. RADIUS authentication is more complex but offers centralized user management and is better suited for larger setups.
*   **Granular vs. General Group Policies:** Creating very granular group policies increases management overhead but improves security. General policies simplify management but can potentially grant users unnecessary privileges. A balance is needed.
*   **CLI vs. Winbox vs. API:** The CLI is powerful but requires technical knowledge. Winbox GUI is user-friendly but can be limiting in advanced scenarios. The API provides the greatest level of control and is suitable for automated deployments but also requires some extra knowledge to setup and test. The choice should be based on the desired complexity of administration.
*   **Multiple vs Single Admin Accounts:** Having multiple admin accounts helps with access auditing and control, but it can also make it difficult to keep track of users with elevated privileges. It is generally better to have multiple restricted users than having fewer unrestricted users.
*  **Password Complexity vs. User Experience:** Requiring complex passwords may add extra complexity for the user, potentially creating friction, but it improves security. This trade-off needs to be evaluated and configured based on organizational needs.

## Configuration for Specific RouterOS Versions:

This configuration is applicable for RouterOS 7.11 (as specified).  Commands and features used are generally available in RouterOS 7.x versions. For older versions (like 6.48), some syntax or features may be different. This configuration is targeted for RouterOS versions 7 and above.
