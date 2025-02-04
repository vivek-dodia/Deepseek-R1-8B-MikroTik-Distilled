Okay, let's dive into a detailed exploration of user and user groups on MikroTik RouterOS, focusing on your specific scenario.

**Scenario Description:**

We will configure user accounts and groups on a MikroTik router connected to a network via the interface `wlan-20` which is assigned the subnet `197.218.102.0/24`. Our goal is to create different user roles with varying levels of access to the router. This is common in an enterprise environment where different staff may need access to different features of the router (monitoring, basic troubleshooting, configuration etc.) but not access to everything.

**Implementation Steps:**

Before beginning, it is good to remember that best practice is to keep the username, password, and other data in a password manager. It is important to keep all passwords secure.

1.  **Step 1: Initial RouterOS State**

    *   **Description:** Before making any changes, let's assess the current user configuration to know the starting point.
    *   **Action:** Use the CLI command `/user print` to display existing users.
    *   **Example CLI Command:**
        ```mikrotik
        /user print
        ```
    *   **Expected Output:** You'll typically see the default `admin` user, often without any assigned group.
        ```
        Flags: * - disabled
         #   USERNAME  GROUP           
         0   admin     full  
        ```
    *   **Explanation:** `admin` is the default user, that should usually be disabled in enterprise settings.

2. **Step 2: Create User Groups**

    *   **Description:** We will create specific user groups with defined permissions. We'll make a 'monitoring' group, with access to monitoring features only and then another group with more privileges called 'support'.
    *   **Action:** Use the command `/user group add`.
    *   **Example CLI Commands:**
        ```mikrotik
        /user group add name=monitoring policy=read,test
        /user group add name=support policy=read,write,test,password
        ```
    *   **Explanation:** The `policy` parameter defines what actions users within that group can perform.
        * `read` allows viewing of information.
        * `write` allows making changes.
        * `test` allows running diagnostics.
        * `password` allows password changes.
    *   **Effect:** Two new groups, `monitoring` and `support` will be available for assigning users to.
    * **Winbox GUI**: Open Winbox and go to `/System/Users/Groups` and add the groups as above.
    *   **Verification CLI Command:**
        ```mikrotik
        /user group print
        ```
    *   **Expected Output:**
        ```
        Flags: * - disabled
         #   NAME       POLICY
         0   full       read,write,test,password
         1   monitoring read,test
         2   support    read,write,test,password
        ```

3.  **Step 3: Create New User Accounts**

    *   **Description:** Create specific users and assign them to the groups created in step 2. We will create a `monitor1` user in the `monitoring` group and then another user called `support1` in the `support` group.
    *   **Action:** Use the command `/user add`.
    *   **Example CLI Commands:**
        ```mikrotik
        /user add name=monitor1 group=monitoring password=monitorpass
        /user add name=support1 group=support password=suppass
        ```
    *   **Explanation:** We create the users `monitor1` and `support1` with the passwords `monitorpass` and `suppass` respectively and assign them to different groups.
    *   **Effect:** The new users will be created and associated to the correct groups.
    *   **Winbox GUI:** Open Winbox and go to `/System/Users` and add users with the appropriate parameters.
    *   **Verification CLI Command:**
        ```mikrotik
        /user print
        ```
    *   **Expected Output:**
        ```
        Flags: * - disabled
         #   USERNAME  GROUP           
         0   admin     full
         1   monitor1   monitoring
         2   support1   support
        ```

4. **Step 4: Disable Default Admin Account**

   * **Description:** In most cases the default admin account should be disabled due to security risks.
   * **Action:** Use the command `/user disable`.
   * **Example CLI Command:**
     ```mikrotik
     /user disable admin
     ```
    * **Effect:** The `admin` account is disabled.
    *   **Winbox GUI:** Open Winbox and go to `/System/Users`, right click on the admin account and select `disable`.
    * **Verification CLI Command:**
     ```mikrotik
     /user print
     ```
   * **Expected Output:**
      ```
      Flags: * - disabled
      #   USERNAME  GROUP
      0 * admin     full
      1   monitor1  monitoring
      2   support1  support
      ```
      Notice the `*` next to the admin user name.

5. **Step 5: Test User Login**

   * **Description:** Attempt to log in with the newly created users to verify access levels
   * **Action:** Use a secure terminal client (e.g. SSH or Winbox) to connect to the device. Try to log in using each user.
   * **Example:** Try logging in using the `monitor1` user and attempt to write a configuration. This should not be possible. Then try logging in with the `support1` user and ensure configuration writes are allowed.
   * **Effect:** User login credentials work as expected. Users have the correct level of access for their group permissions.
   * **Verification:** Log in with `monitor1` and try to issue `/ip address add address=192.168.88.1/24 interface=wlan-20` This should be disallowed. Log in with `support1` and try the same command. This should succeed.

**Complete Configuration Commands:**

```mikrotik
/user group
add name=monitoring policy=read,test
add name=support policy=read,write,test,password
/user
add name=monitor1 group=monitoring password=monitorpass
add name=support1 group=support password=suppass
disable admin
```
**Explanation of parameters:**
*   `/user group add name=<group_name> policy=<policy_list>`:
    *   `name`: The name of the user group.
    *   `policy`: A comma-separated list of permissions. Common options include `read` (view settings), `write` (make changes), `test` (perform diagnostic tests), and `password` (change user passwords).
*   `/user add name=<username> group=<group_name> password=<password>`:
    *   `name`: The username.
    *   `group`: The group the user will belong to.
    *   `password`: The user's password.
*   `/user disable <username>`:
    *   `username`: The username of the user to disable.

**Common Pitfalls and Solutions:**

*   **Incorrect Policy Settings:** Users may not have the required permissions if the policy is incorrect. Double-check the policy assigned to each group using `/user group print`.
*   **Forgotten Passwords:** If a user forgets their password, you'll need to reset it using a user with `write` permissions. Command: `/user set <username> password=<newpassword>`
*   **Confusing Groups:** If groups are assigned with errors, ensure that each user is assigned the correct group using `/user print`.
*   **User Locked Out:** If a user fails to log in multiple times, they may be temporarily locked out. This can be diagnosed using logs `/log print topics=user`.
*   **Resource Issues:** User management in and of itself will not cause high CPU or memory usage. However, if a large number of users are logging in simultaneously, this can potentially cause issues. This should be monitored via the MikroTik monitoring tools such as `/system resource monitor`.
*   **Security Issues:** Users with `full` or `write` access can be a security risk. Limit the number of these users. Always use secure passwords. Never leave default usernames and passwords.

**Verification and Testing Steps:**

*   **Login Verification:** Use SSH, Telnet, or Winbox to log in with each created user. Ensure they can perform actions according to their assigned group policy.
*   **Policy Testing:** Try read and write operations with each user to ensure only allowed actions are possible.
*   **Log Checking:** Monitor logs using `/log print topics=user` to track user login activity.
*   **Access Testing:** Log in with monitor1. This user should not be able to make changes. Log in with support1. This user should be able to make changes.
*   **Winbox GUI**: Test each user's access by logging in with Winbox and attempting to make changes.

**Related Features and Considerations:**

*   **RADIUS Authentication:** Integrate with a RADIUS server for centralized user management and authentication. This is particularly useful for larger networks.
*   **User Sessions:** View logged-in user sessions via `/user active print`. This allows monitoring of active connections.
*   **API Users:** Restrict API access via specific user accounts and assign permissions via groups.
*  **Session Timeout:** User sessions can be set to automatically close if there is a period of inactivity.
*   **User Locking:** Add password lockouts for users that have incorrect password attempts.

**MikroTik REST API Examples:**

While the RouterOS API primarily focuses on device configuration, user management is also available.

*   **Get Users:**

    *   **API Endpoint:** `/rest/user`
    *   **Method:** `GET`
    *   **Request:** (None)
    *   **Expected Response (JSON Example):**
        ```json
        [
          {
              "id": "0",
              "name": "admin",
              "group": "full",
              "disabled": false
          },
          {
              "id": "1",
              "name": "monitor1",
              "group": "monitoring",
              "disabled": false
          },
          {
              "id": "2",
              "name": "support1",
              "group": "support",
              "disabled": false
          }
       ]
        ```

*   **Create a User:**

    *   **API Endpoint:** `/rest/user`
    *   **Method:** `POST`
    *   **Request Payload (JSON Example):**
        ```json
        {
          "name": "apiuser",
          "group": "monitoring",
          "password": "apipassword"
        }
        ```
    *   **Expected Response (201 Created with Location header or other success code):**
        ```json
         {
          "id": "3"
         }
        ```
    *   **Error Handling:** Handle errors such as `400 Bad Request` for invalid input or `409 Conflict` if the user already exists.
        ```json
         {
          "message": "value already exists",
          "detail": "name"
        }
        ```

*   **Update a User:**

    *   **API Endpoint:** `/rest/user/<user_id>`
    *   **Method:** `PUT`
    *   **Request Payload (JSON Example):**
        ```json
        {
            "group":"support",
            "password":"apipasswordnew"
        }
        ```
    *   **Expected Response (200 OK):**
         ```json
           {}
         ```

* **Delete a User**

    * **API Endpoint:** `/rest/user/<user_id>`
    * **Method:** `DELETE`
    * **Expected Response (204 No Content):**
        ```json
           {}
        ```

**Security Best Practices:**

*   **Strong Passwords:** Always use strong, unique passwords for all user accounts.
*   **Disable Default Accounts:** As demonstrated, disable the default `admin` account.
*   **Principle of Least Privilege:** Only grant users the minimum access required for their role.
*   **Regular Password Changes:** Enforce regular password changes for all users.
*   **Audit Logging:** Enable and monitor user login and configuration changes.
*   **Secure API Access:** When accessing the API, ensure you are using HTTPS, and enforce strict access control for API accounts.
*   **IP Access Lists:** Restrict user login to specific IPs or networks.

**Self Critique and Improvements:**

*   **Scalability:** For larger environments, consider using RADIUS for more complex user management.
*   **Automation:**  Script user creation and updates via the API for easier management.
*   **Granular Permissions:** RouterOS doesn't offer highly granular per-feature permissions. You can use the `policy` argument on group creation to create groups with access to specific features. However, this is not always practical.
*   **Account Lockouts:** Implement password lockout policies to prevent brute-force attacks.
*   **Centralized Management:** Consider MikroTik's "The Dude" monitoring tool for centralized monitoring and user management.

**Detailed Explanations of Topic:**

*   **Users:** RouterOS uses user accounts for authentication and authorization to access the router and its settings via different methods (SSH, Winbox, API, etc).
*   **User Groups:** Groups allow you to define permissions that can be applied to multiple users, simplifying user management and improving security.
*   **Policies:** Policies define what actions users within a group can perform, such as reading configuration, making changes, and running diagnostics.

**Detailed Explanation of Trade-offs:**

*   **Using Groups vs. Per-User Policies:** Groups make management much easier because you don't have to assign individual policies to each user.  While per-user policies would allow more granular control, they would be less practical for even medium size deployments.
*   **Policy Types:** The `read` policy allows information to be viewed, but prevents changes. `write` allows changes to the router's settings. `test` gives access to diagnostic tools, such as ping and traceroute. `password` allows changes to the user's password.
*   **Security vs. Convenience:** Allowing `full` access to multiple users makes management easier, but increases the security risk. It is always best to give users only the minimum set of permissions they need.

**Configuration for Specific RouterOS Versions:**

The commands used in this document are generally compatible with RouterOS 7.11 and 6.48. Minor variations may exist between versions, but the core user and group management functionality is consistent. Always consult the official MikroTik documentation for your specific RouterOS version.

I hope this detailed documentation provides a comprehensive understanding of user and user group management on MikroTik RouterOS.
