Okay, let's dive deep into creating a detailed configuration for user and user groups on MikroTik RouterOS 6.48, targeting an advanced user with a point-to-point link scenario and a specific subnet on interface `ether-13`.

## Scenario Description:

This configuration focuses on managing user access on a MikroTik router (Router A), utilizing user groups for centralized management.  We'll configure users with specific privileges, controlling their access to the router's resources and functionalities. This is a common practice for both security and ease of administration when multiple administrators require access to a router. Our target interface is `ether-13`, which will be considered the interface connected to a network that includes devices that might need specific access or where the administrators are accessing the router from. The management will be done directly from the router itself, but in another example I'll provide one done via external Radius authentication.

## Implementation Steps:

### Step 1: Initial Router State (Pre-Configuration)

*   **Description:** Before any changes are made, let's establish the current state of the router and the target interface (ether-13).
*   **CLI Example (Read-Only):**
    ```mikrotik
    /interface print
    /ip address print
    /user print
    /user group print
    ```
*   **Winbox Example:**
    *   Navigate to `Interfaces` to see existing interfaces.
    *   Navigate to `IP` -> `Addresses` to see assigned IP addresses.
    *   Navigate to `System` -> `Users` to see existing user accounts and groups.
*   **Expected Output:** This will list existing interfaces, addresses, users, and user groups. Initially, you should see the default `admin` user and possibly a few default groups like `read`, `write`, and `full`.
*   **Effect:** This step is purely observational, showing the state before we apply the changes.
*   **Note:** This is important to revert changes if needed.

### Step 2: Creating a New User Group - 'limited-access'

*   **Description:** We will create a new group called `limited-access` and specify its policies. This group will later be associated with new users.
*   **CLI Command:**
    ```mikrotik
    /user group add name=limited-access policy=read,test,winbox
    ```
*   **Parameter Explanation:**
    *   `name`: Specifies the name of the new user group (`limited-access`).
    *   `policy`: Defines the permissions granted to this group. `read` allows viewing configurations, `test` allows basic testing like ping, and `winbox` allows access via the Winbox GUI.
*   **Winbox Example:**
    *   Navigate to `System` -> `Users` -> `Groups`.
    *   Click the `+` (Add New) button.
    *   Enter the group name: `limited-access`.
    *   Check the boxes for `read`, `test`, and `winbox` policies.
    *   Click `Apply` and then `OK`.
*  **CLI Example (After Command):**
    ```mikrotik
        /user group print
    ```
* **Expected Output:** The CLI should list the new `limited-access` group and its configured policies.
*   **Effect:** This step creates a user group, allowing for centralized management of permissions.

### Step 3: Creating a User - 'user-one' with limited access

*   **Description:** We will create a user named `user-one` and assign this user to the `limited-access` user group, ensuring they only have access to the policies defined in the group.
*   **CLI Command:**
    ```mikrotik
    /user add name=user-one password=StrongPassword group=limited-access
    ```
*   **Parameter Explanation:**
    *   `name`: Specifies the username (`user-one`).
    *   `password`: Sets the password for this user (replace `StrongPassword` with a real password).
    *   `group`: Assigns the user to the `limited-access` user group.
*   **Winbox Example:**
    *   Navigate to `System` -> `Users`.
    *   Click the `+` (Add New) button.
    *   Enter the username: `user-one`.
    *   Enter and confirm a password.
    *   Select `limited-access` from the `Group` dropdown menu.
    *   Click `Apply` and then `OK`.
*   **CLI Example (After Command):**
    ```mikrotik
        /user print
    ```
*   **Expected Output:** The CLI should list the `user-one` and its assigned group.
*   **Effect:** This creates a new user with controlled privileges.

### Step 4: Creating a User - 'admin-user' with full access

*   **Description:** We will create another user named `admin-user` who will have full administrative access to the router.
*   **CLI Command:**
    ```mikrotik
    /user add name=admin-user password=AnotherStrongPassword group=full
    ```
*   **Parameter Explanation:**
    *   `name`: Specifies the username (`admin-user`).
    *   `password`: Sets the password for this user (replace `AnotherStrongPassword` with a real password).
    *   `group`: Assigns the user to the `full` user group.
*   **Winbox Example:**
    *   Navigate to `System` -> `Users`.
    *   Click the `+` (Add New) button.
    *   Enter the username: `admin-user`.
    *   Enter and confirm a password.
    *   Select `full` from the `Group` dropdown menu.
    *   Click `Apply` and then `OK`.
*   **CLI Example (After Command):**
    ```mikrotik
        /user print
    ```
*   **Expected Output:** The CLI should list the `admin-user` and its assigned group.
*   **Effect:** This creates a new user with full access.

### Step 5: Logging in as 'user-one' and testing limited access

*   **Description:** Log out from the current user, then log in as `user-one`.  Attempt to perform an action, such as accessing a configuration in `IP -> Addresses` to verify that their read-only privileges are working as expected. Then attempt an action which they do not have permission to, like configuring IP addresses.
*   **Winbox Example:**
    *   Log out of the current Winbox session.
    *   Log in using the username `user-one` and the password created earlier.
    *   Navigate to `IP` -> `Addresses` and attempt to change a value (this should be denied).
    *   Verify you are able to look at the configuration without any issues.
* **Expected Output:** `user-one` should be able to access the router via winbox, see the configuration but not change it. When attempting to modify configuration it should be denied.
* **Effect:** This test confirms that the defined group policies are working properly.

### Step 6: Logging in as 'admin-user' and testing full access

*   **Description:** Log out from the current user, then log in as `admin-user`.  Attempt to perform an action, such as adding an IP address or user to verify that they have full admin access.
*   **Winbox Example:**
    *   Log out of the current Winbox session.
    *   Log in using the username `admin-user` and the password created earlier.
    *   Navigate to `IP` -> `Addresses` and add a new address (this should work).
    *   Verify you are able to make configuration changes.
* **Expected Output:** `admin-user` should be able to access the router via winbox and make any configuration changes.
* **Effect:** This test confirms that the defined group policies are working properly for the full access admin.

## Complete Configuration Commands:

```mikrotik
/user group
add name=limited-access policy=read,test,winbox

/user
add name=user-one password=StrongPassword group=limited-access
add name=admin-user password=AnotherStrongPassword group=full
```

*   `/user group add`: Command to add a new user group
    *   `name`: The name of the new user group
    *  `policy`:  Defines permissions granted to the group (read, write, test, winbox, etc)
*   `/user add`: Command to add a new user
    *   `name`: The name of the new user
    *   `password`: The password for the new user
    *   `group`:  The user group this user belongs to.

## Common Pitfalls and Solutions:

*   **Problem:** Forgetting to assign a user to a group.
    *   **Solution:**  Always double-check the user's `group` field after creating a user. Use the `/user print` command to review user details.
*   **Problem:** Using weak passwords.
    *   **Solution:** Enforce the use of strong, complex passwords using a combination of letters, numbers, and special characters. Do not use password examples like I've provided, always use a secure password generation tool to create them.
*  **Problem:** Overly permissive user groups.
    *   **Solution:** Follow the principle of least privilege, only granting the required permissions. Start with minimal policies and add more as necessary.
*   **Problem:**  Lockout due to incorrect group policies.
    *   **Solution:**  Always have a backup, default admin user with full access that you can use in the event you accidentally lock yourself out of the router via incorrectly configured user groups. This will allow you to restore the proper access.
*   **Problem:**  API user misconfiguration.
    *   **Solution:** Be sure to understand each policy that you are granting access too. There are often subtle differences which can cause unexpected issues.

## Verification and Testing Steps:

*   **Login and functionality test:** Log in with each user to Winbox or via SSH and test what you can access.
*   **`ping` command:** For the `limited-access` user, you should be able to use the `ping` command (due to the `test` policy) but not the `/interface print` command.
*   **User List:** Use `/user print` command to verify all users and their assigned groups.
*   **Group List:** Use `/user group print` command to verify all groups and their assigned policies.

## Related Features and Considerations:

*   **Radius Authentication:** Instead of local users, you can authenticate users against a RADIUS server for centralized management. This is especially useful in larger networks or when using a centralized authentication database.
*   **API Users:** RouterOS also allows for API-specific users that can be used for configuration management via API.
*   **User Profile:** You can further configure user profiles for specific resource allocation, such as bandwidth management. This will allow you to further fine tune each user's access to the network.

## MikroTik REST API Examples (if applicable):

While directly creating users and groups via the REST API is possible, it is generally not recommended for highly sensitive configurations like user management, because there is no encryption for passwords. However, for completeness, here is an example:

**Creating a User Group via API**
* Endpoint: `/user/group`
* Method: `POST`
* JSON Payload:
```json
{
  "name": "api-limited-access",
  "policy": "read,test,winbox"
}
```

* Expected Response (Success 200):
```json
{
    ".id": "*10" ,
    "name": "api-limited-access",
    "policy":"read,test,winbox"
}
```
*  Error Handling:
    *  400 Bad Request: Request Body JSON has error. Check Syntax.
    *  500 Internal Server Error: There was an internal error from the router. Review the logs for more information.
   * 409 Conflict: A group with the specified name already exists.

**Creating a User via API**

* Endpoint: `/user`
* Method: `POST`
* JSON Payload:

```json
{
  "name": "api-user",
  "password": "apiStrongPassword",
  "group": "api-limited-access"
}
```

* Expected Response (Success 200):
```json
{
    ".id": "*11" ,
    "name": "api-user",
    "group": "api-limited-access",
    "disabled":false,
    "last-login": "jan/18/2024 21:22:32"
}
```

*  Error Handling:
    *  400 Bad Request: Request Body JSON has error. Check Syntax.
    *  500 Internal Server Error: There was an internal error from the router. Review the logs for more information.
   * 409 Conflict: A user with the specified name already exists.

**Note:**  For security, it's vital to use HTTPS for any API communication.  Direct API user creation is generally considered not as secure as other means, due to the fact the password is sent in plain text. It's far preferable to create user / user groups through the MikroTik's UI / CLI interface.

## Security Best Practices

*   **Strong Passwords:** Always use strong, complex passwords for all user accounts. Use password generators.
*   **Principle of Least Privilege:** Grant the minimal privileges needed for each user and group.
*   **Regular Audits:** Periodically review user accounts and group configurations. Remove or disable unused accounts.
*   **Access Control:** Limit access to the router's web interface and SSH via firewall rules and allowed IP addresses. This should be done separate from user management.
*   **Secure API:** Always use HTTPS when using the API, do not send credentials over insecure connections. Also always treat API access with the utmost caution, as it grants powerful control.
*   **Two-Factor Authentication (2FA):** Where possible and supported, enable 2FA to further secure access.
*   **External Authentication:**  Use an external Radius server for all admin access, where feasible, to prevent local password storage on the router.

## Self Critique and Improvements

*   **Improvement:** Use a Radius Server for user authentication instead of local accounts for production environments.
*   **Improvement:** Set up specific firewalls rules, to further restrict access to the users created.
*   **Improvement:** Setup additional profile settings for the users that have been created.
*   **Further Modifications:** Use a more granular policy model. I used the most basic policies but these can be further subdivided to get more specific access.

## Detailed Explanations of Topic

*   **Users:** RouterOS users are accounts that allow individuals or applications to access the router's configuration and functionality. Each user has a username, password, and group association.
*   **User Groups:** User groups are containers that define a set of policies. Users belonging to a group inherit those policies. This simplifies the management of multiple users with similar access requirements. User groups can provide a more efficient method of managing access privileges and can help maintain security by avoiding the need to individually configure access for each user. By configuring user groups you can easily manage the different permissions within your MikroTik router.
*   **Policies:** Policies determine what a user can do on the router. Common policies are: `read`, `write`, `test`, `winbox`, and `full`. For example, `read` allows viewing, `write` allows modifying, and `test` includes the ability to ping. Understanding what each of these policies do is critical to setting up the right permissions.

## Detailed Explanation of Trade-offs

*   **Local vs Radius Authentication:** Using local accounts simplifies setup but is less secure and scalable. RADIUS authentication provides centralized management, improved security, and scalability, but requires a separate server and adds complexity. There is a definite trade off in ease of set up verses security and scalability.
*   **Granular Policies:** Fine-grained policies enhance security by limiting actions but increase the management overhead. It's a trade-off between security and administration ease. If you are unsure, it's better to start with minimal policies and add more as required.
*   **API Access:** API access provides automation but introduces security risks. Using strong API authentication practices like certificates, as opposed to usernames / passwords, is important and must be done to keep security concerns to a minimum.
* **Multiple Groups vs Single Group:** Using multiple groups provides a higher security configuration but increases management complexity. Single groups provide a simplified configuration, but can potentially reduce security, if a user has access to more policies than required.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 6.48 (as well as 7.x versions). The commands used are valid for both versions. Ensure you double check any documentation on any major version upgrades.

This documentation provides a comprehensive guide, from basic setup to advanced considerations, security practices, and API examples. Remember to always test in a safe environment before implementing changes in production.
