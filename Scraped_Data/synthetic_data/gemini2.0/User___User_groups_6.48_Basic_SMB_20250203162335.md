Okay, let's dive into a detailed configuration of users and user groups on MikroTik RouterOS, tailored for an SMB environment, focusing on RouterOS 6.48 and 7.x, using the given subnet and interface.

## Scenario Description:

This scenario focuses on creating and managing users and user groups on a MikroTik router for administrative access control, specifically restricting access to the router based on defined roles and preventing unauthorized configuration changes. We'll define a 'read-only' group for monitoring and a 'full-access' group for administrators.

## Implementation Steps:

Here’s a step-by-step guide to configuring users and user groups, including explanations and examples using both CLI and Winbox.

**Before Step 1:**
Let's assume your MikroTik is currently accessible with the default 'admin' user (often with a blank password in a default configuration) and you can access it via Winbox or CLI. We need to secure this first.

**1. Step 1: Change the Default Admin Password**

   * **Explanation:** Changing the default administrator password is crucial for security. Leaving it default is a major vulnerability.
   * **CLI Instructions:**
      ```mikrotik
      /user set admin password=YourNewStrongPassword
      ```
     * **Winbox GUI:**
        1. Go to System -> Users.
        2. Select the `admin` user.
        3. Click "Change Password".
        4. Enter the old and new password, then click "OK".

   * **After Step 1:**
       - The 'admin' user now has a strong password. You will need to use this password for further access.

**2. Step 2: Create a Read-Only User Group**
  *   **Explanation:** This group will have limited permissions, ideal for monitoring without making configuration changes.
   * **CLI Instructions:**
       ```mikrotik
      /user group add name=read-only policy=read
       ```
     * **Winbox GUI:**
          1. Go to System -> Users -> User Groups tab.
          2. Click the "+" button to add a new user group.
          3. Set `Name`: `read-only`.
          4. In the 'Policy' section check the `read` permission.
          5. Click "Apply" then "OK".
  * **After Step 2:**
      - A 'read-only' user group is created. This group only has permissions to read the configuration.

**3. Step 3: Create a Full-Access User Group**
    * **Explanation:** This group will have full access to all router functionality. This group is meant for full administrative access.
   * **CLI Instructions:**
       ```mikrotik
       /user group add name=full-access policy=write,test,password,reboot,read,local,winbox,web,ftp,ssh,api
       ```
     * **Winbox GUI:**
          1. Go to System -> Users -> User Groups tab.
          2. Click the "+" button to add a new user group.
          3. Set `Name`: `full-access`.
          4. In the 'Policy' section check the appropriate permissions: `read`, `write`, `test`, `password`, `reboot`, `local`, `winbox`, `web`, `ftp`, `ssh`, `api`.
          5. Click "Apply" then "OK".
   * **After Step 3:**
      - A `full-access` user group is created with full access rights.

**4. Step 4: Create a New User and Add to the Read-Only Group**
    * **Explanation:**  We create a user account `monitor` and assign it to the `read-only` user group.
   * **CLI Instructions:**
      ```mikrotik
      /user add name=monitor password=ReadOnlyPassword group=read-only
      ```
    * **Winbox GUI:**
        1. Go to System -> Users -> Users tab.
        2. Click the "+" button to add a new user.
        3. Set `Name`: `monitor`.
        4. Set the `Password`.
        5. Set the `Group`: `read-only`
        6. Click "Apply" then "OK".
  * **After Step 4:**
      -  The user `monitor` can now access the router with a `read-only` permission.

**5. Step 5: Create a New User and Add to the Full-Access Group**
    * **Explanation:**  We create a user account `admin2` and assign it to the `full-access` user group.
   * **CLI Instructions:**
      ```mikrotik
      /user add name=admin2 password=AdminPassword group=full-access
      ```
   * **Winbox GUI:**
       1. Go to System -> Users -> Users tab.
       2. Click the "+" button to add a new user.
       3. Set `Name`: `admin2`.
       4. Set the `Password`.
       5. Set the `Group`: `full-access`
       6. Click "Apply" then "OK".
   * **After Step 5:**
       - The user `admin2` can now access the router with full administrative permission.

## Complete Configuration Commands:

Here are all the CLI commands for the setup:

```mikrotik
# Change the default admin password
/user set admin password=YourNewStrongPassword

# Create read-only user group
/user group add name=read-only policy=read

# Create full-access user group
/user group add name=full-access policy=write,test,password,reboot,read,local,winbox,web,ftp,ssh,api

# Create a read-only user
/user add name=monitor password=ReadOnlyPassword group=read-only

# Create a full-access user
/user add name=admin2 password=AdminPassword group=full-access

```
**Parameter Explanations:**
| Command       | Parameter   | Explanation                                                      |
|---------------|-------------|------------------------------------------------------------------|
| `/user set`   | `admin` | Specifies the user account to be modified                                 |
|        | `password`  | New password for the specified user.  |
|`/user group add` | `name` | Specifies the group name to add|
|               |`policy`    | The access control policy for the group.                                   |
|`/user add`     | `name`  | The user name to add.                                 |
|               |`password`  | The password for the new user.                     |
|               | `group` | The user group to which the user should be assigned.  |

## Common Pitfalls and Solutions:

* **Lost Admin Access:** If you forget the new admin password, you might need to reset the MikroTik device, depending on your device model. It is **essential to keep a secure record of the admin passwords** or have an alternative administrative user available.
    * **Solution:** Keep track of all user names and passwords.
* **Incorrect Policy Settings:** Setting wrong policies for user groups might create unintended restrictions or loopholes.
    * **Solution:** Carefully review policy options before applying them. `read` only for read-only users and a comprehensive list of permissions for administrative users.
* **Overly Permissive Policies:** Granting excessive rights could increase security vulnerabilities
    * **Solution:** Use the principle of least privilege: only give necessary permissions.
* **User Lockout:** Incorrect passwords could lead to temporary lockouts for remote logins.
    * **Solution:** Double check the users configuration.
* **Resource Issues:** While not directly caused by user configurations, increased user connections could impact CPU usage, especially if API usage is high.
    * **Solution:** Monitor the router’s resource usage regularly. Consider limiting user connections if necessary.

## Verification and Testing Steps:

1.  **Login with New Users:** Use Winbox or SSH to try logging in with the `monitor` (read-only) and `admin2` (full-access) user credentials.

2.  **Test Read-Only Permissions:** Log in with the `monitor` user. Attempt to make changes via the CLI (e.g., `/ip address add address=192.168.10.1/24 interface=ether1`). You should see an error saying "not allowed".

3.  **Test Full-Access Permissions:** Log in with the `admin2` user and repeat the above test. The command should be successful.

4.  **Check User List:** In Winbox or CLI, use `/user print` to verify all users and group assignments.

5.  **Use `torch` Tool (if applicable)**: Check for unauthorized access by logging activity. `/tool torch interface=ether-42` can be used to verify who is making requests to your device.

## Related Features and Considerations:

*   **API Users:**  You can create users specifically for API access, granting different levels of permission for automated tasks. You can use REST API calls to manage the device.
*   **User-Specific Limitations:**  You can configure specific bandwidth limitations for users accessing the router (if they use the router for internet access) using queues. This should be configured on interfaces like `ether-42`.
*   **Authentication Methods:** Apart from local authentication, you can use RADIUS for more centralized user management.
*   **Logging:** Enable logging for successful and failed login attempts.
*   **Hotspot Users:** If the router is part of a hotspot system, it will use user accounts. This configuration is independent from the administrative user configuration.

## MikroTik REST API Examples (if applicable):

Here are some examples of how to interact with MikroTik’s API using a REST client (like Postman).

**1. Get Users:**

*   **Endpoint:** `/rest/user`
*   **Method:** `GET`
*   **Request Body:** None
*   **Expected Response (JSON):**

```json
[
  {
    ".id": "*1",
    "name": "admin",
    "group": "full-access",
    "disabled": "false",
     "last-logged-in": "1970-01-01T00:00:00+00:00"
  },
  {
    ".id": "*2",
    "name": "monitor",
    "group": "read-only",
    "disabled": "false",
    "last-logged-in": "1970-01-01T00:00:00+00:00"
  },
  {
    ".id": "*3",
     "name": "admin2",
    "group": "full-access",
     "disabled": "false",
    "last-logged-in": "1970-01-01T00:00:00+00:00"
  }
]
```
**Error Handling:**
    - If there is a problem with permissions, the router returns an HTTP error (401 Unauthorized). You need to make sure the user making the request has enough permissions.

**2. Create a User:**

*   **Endpoint:** `/rest/user`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
        "name": "apiuser",
        "password": "ApiPassword123",
        "group": "read-only"
    }
    ```
*   **Expected Response (JSON):**
    ```json
    {
        ".id": "*4",
        "name": "apiuser",
        "group": "read-only",
        "disabled": "false",
        "last-logged-in": "1970-01-01T00:00:00+00:00"
    }
    ```

* **Error Handling:**
    - If there is an error such as an invalid group, the router returns an HTTP error (400 Bad Request) along with an error message.
    ```json
     {
        "message": "invalid value for argument group - no such user group",
        "error": true
    }
    ```

**3. Modify an Existing User:**

*   **Endpoint:** `/rest/user/*3` (Replace `*3` with the ID of the user to be modified)
*   **Method:** `PATCH`
*   **Request Body (JSON):**
    ```json
    {
        "group": "read-only"
    }
    ```
*   **Expected Response (JSON):**
  ```json
     {
        ".id": "*3",
        "name": "admin2",
        "group": "read-only",
         "disabled": "false",
        "last-logged-in": "1970-01-01T00:00:00+00:00"
     }
    ```
* **Error Handling:**
    - If the user does not exist (for example, using an invalid user ID), the router returns an HTTP error (404 Not Found).

## Security Best Practices

*   **Use Strong Passwords:**  Always use strong, unique passwords for all user accounts.
*   **Principle of Least Privilege:** Assign users only the necessary privileges.
*   **Regular Password Changes:** Enforce periodic password changes, if possible.
*   **Disable Unused Accounts:** Disable any accounts that are no longer needed.
*   **Monitor Login Attempts:** Regularly check logs for suspicious login attempts.
*   **Secure API Access:** Use HTTPS and secure tokens if using API.
*   **Avoid Default Usernames:** Change default user names as well.
*   **Firewall Access:** Restrict user and admin access from only allowed networks.

## Self Critique and Improvements

This configuration is a good starting point for managing users and groups, but here are some improvements:

*   **More Granular Policy Control:** Explore creating more groups for specific actions (e.g., a group only allowed to view routing, one only allowed to set bandwidth limitations), instead of general `read-only` and `full-access`. This allows for more specific permissions based on job description.
*   **RADIUS Integration:** For a larger network, integrating with a RADIUS server would allow a centralized way to manage users, rather than managing users on every device.
*  **API Access Restrictions:** The API should be only accessible from specific internal IP addresses. You should use firewall rules to restrict access.
*  **Log Auditing:** All administrative changes to the system should be logged and audited periodically.

## Detailed Explanations of Topic

**Users and User Groups** in MikroTik RouterOS are fundamental for managing access control. A user is an entity that can log in to the router and perform actions based on its assigned group's permissions. User groups allow you to bundle permissions and quickly apply them to multiple users, simplifying management and enhancing security.

**User Policies** define what a user can do, such as reading configurations, making changes, running tests, managing passwords, restarting the device, accessing via Winbox, accessing via API, and so on. The `policy` settings in the user group configuration are critical for controlling permissions.

## Detailed Explanation of Trade-offs

*   **Granularity vs. Simplicity:**  Creating a few generic groups (`read-only`, `full-access`) is simpler but less secure. Creating many specific groups is more secure but more complex to manage.
*   **Local vs. RADIUS Authentication:** Local authentication is simple for small setups, but RADIUS is better for large or distributed networks with centralized management. However, RADIUS is more difficult to implement and maintain than local authentication.
*   **API Access vs. CLI/Winbox:** API access allows automation but introduces a new potential security risk if not properly secured.
*   **Resource Consumption:** High number of connected users can increase CPU usage. However, this is only a real concern if many users are actively accessing the device through API, SSH, etc.

## Configuration for Specific RouterOS Versions:
The configuration provided is valid for both RouterOS 6.48 and 7.x. The fundamental user and group management remains consistent between the versions.
The API endpoint also remains the same between both RouterOS versions. If you encounter issues, verify that the user has the correct permissions.

This detailed documentation provides a comprehensive understanding and practical implementation of user and user group management on MikroTik RouterOS.
