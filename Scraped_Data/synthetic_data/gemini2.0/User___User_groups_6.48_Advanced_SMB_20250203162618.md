Okay, let's dive into crafting a comprehensive MikroTik RouterOS user and user group configuration for the specified scenario.

## Scenario Description:

We are tasked with configuring a MikroTik router in an SMB environment. This router will manage users with varying levels of access to specific router functions. We will create user groups with predefined privileges and then assign users to these groups. The network operates on the subnet 101.196.226.0/24, and the management interface is `bridge-81`.

## Implementation Steps:

Here's a step-by-step guide for setting up users and user groups:

### Step 1: Initial Router State

*   **Description:** Before we make any changes, we need to examine the existing user and group configuration. This step helps us understand the current state of the router.

*   **CLI Command:**

    ```mikrotik
    /user print
    /user group print
    ```

*   **Expected Output (Example):**
    ```
    /user print
    Flags: * - disabled
      #   NAME      GROUP      
      0   admin     full 
    
    /user group print
    Flags: * - default
      #   NAME     POLICY
      0 * full     read,write,test,password,web,winbox,api,ftp,reboot,local,telnet,ssh,dude,console
      1   read     read
      2   write    read,write
    ```

*   **Winbox GUI:**  Navigate to *System -> Users* and *System -> User Groups* to view existing users and groups.

### Step 2: Create User Groups

*   **Description:**  We will create two new user groups: `monitoring` with read-only access and `restricted-admin` with limited administrative privileges.

*   **CLI Commands:**

    ```mikrotik
    /user group add name=monitoring policy=read
    /user group add name=restricted-admin policy="read,write,test,password,winbox"
    ```

*   **CLI Output After Configuration:**

    ```
     /user group print
    Flags: * - default
      #   NAME     POLICY
      0 * full     read,write,test,password,web,winbox,api,ftp,reboot,local,telnet,ssh,dude,console
      1   read     read
      2   write    read,write
      3   monitoring read
      4   restricted-admin read,write,test,password,winbox
    ```

*   **Explanation:**
    *   `/user group add name=monitoring policy=read` : This command creates a new user group named "monitoring". Users in this group will only have "read" permissions.
    *   `/user group add name=restricted-admin policy="read,write,test,password,winbox"` : This command creates a user group named "restricted-admin". Users in this group have "read", "write", "test", "password" (for changing their own password), and "winbox" permissions.

*   **Winbox GUI:** Navigate to *System -> User Groups* and click "+" to create new user groups. Set the "Name" and "Policy" accordingly.

### Step 3: Create Users and Assign to Groups

*   **Description:** Now, we'll add two new users: `monitor-user` belonging to the `monitoring` group and `admin-user` belonging to the `restricted-admin` group. We also create a password for the admin user.

*   **CLI Commands:**

    ```mikrotik
    /user add name=monitor-user group=monitoring password=monitorpassword
    /user add name=admin-user group=restricted-admin password=secureAdminPass
    ```

*  **CLI Output After Configuration:**

    ```
    /user print
    Flags: * - disabled
    #   NAME           GROUP
    0   admin          full
    1   monitor-user   monitoring
    2   admin-user     restricted-admin
    ```
*   **Explanation:**
    *   `/user add name=monitor-user group=monitoring password=monitorpassword` : This command creates a user named "monitor-user" with the password `monitorpassword` and assigns this user to the `monitoring` group.
    *   `/user add name=admin-user group=restricted-admin password=secureAdminPass` : This command creates a user named "admin-user" with the password `secureAdminPass` and assigns this user to the `restricted-admin` group.

*   **Winbox GUI:** Navigate to *System -> Users* and click "+" to create new users. Set the "Name", "Group", and "Password" accordingly.

### Step 4: Test User Access

*   **Description:** Now we'll test the access of each new user. Try connecting with each user, using Winbox, SSH, or API.

*   **Actions:**
    *   Attempt to log in to Winbox with `monitor-user`. The user should only be able to view the configuration but not make changes.
    *   Attempt to log in to Winbox with `admin-user`. This user should be able to make changes, but should be unable to access certain configuration options, such as creating new users.
    *    Attempt to access the API with each user.

*  **Verification:**
    * `monitor-user` can only `read` via winbox. This can be tested by attempting to change a parameter via the winbox GUI.
    * `admin-user` can `read,write,test,password,winbox` and can therefore make changes to the configuration via Winbox GUI. This can be tested by changing a parameter via the winbox GUI. Additionally the user can change its own password.
    * Both users can `read` via API requests.

## Complete Configuration Commands:

Here is the full set of commands for this setup:

```mikrotik
/user group add name=monitoring policy=read
/user group add name=restricted-admin policy="read,write,test,password,winbox"
/user add name=monitor-user group=monitoring password=monitorpassword
/user add name=admin-user group=restricted-admin password=secureAdminPass
```

## Common Pitfalls and Solutions:

*   **Problem:** Incorrect policy assignments to user groups.
    *   **Solution:** Double-check the `policy` settings in `/user group print` and correct as necessary. Use specific policies rather than trying to guess what each policy grants.
*   **Problem:** Forgetting passwords.
    *   **Solution:** Use a password manager to store passwords. If a password is lost, it must be reset, which may require console access if user admin rights are unavailable.
*   **Problem:** Overly permissive user groups.
    *   **Solution:** Apply the principle of least privilege. Only grant necessary permissions.
*   **Problem:** Resource issues due to many users.
    *   **Solution:**  Monitor CPU and memory usage via `/system resource print`. If issues persist, reduce the number of users or upgrade hardware.
*  **Problem:** Users fail to login via winbox.
    *  **Solution:** Check that `winbox` is enabled on the user group. Check that there are not IP restrictions via `/ip service`.

## Verification and Testing Steps:

1.  **User Login Test:** Attempt to log in with `monitor-user` and `admin-user` via Winbox. Verify access based on the group policies. Attempt to make changes and confirm that user `monitor-user` cannot.
2.  **API Access Test:** Test user access via the MikroTik API using credentials for both users. Confirm that `monitor-user` can read data via the API.
3.  **Policy Verification:** Use the CLI command `/user group print` to verify that each group has the expected policies.
4.  **User Print:** Use the CLI command `/user print` to verify user group assignments.
5.  **SSH Login:** Verify that users can login to the router using ssh.

## Related Features and Considerations:

*   **RADIUS Authentication:** For larger networks, consider using RADIUS server authentication for users. This provides centralized user management.
*   **User Profiles:** MikroTik user profiles can be used to apply rate limiting, firewall rules, and other configuration aspects based on user logins, which would be useful in a hotspot environment.
*   **Read-Only Users:** This setup demonstrates the usefulness of creating read-only user groups to ensure that regular users can access basic monitoring information, without affecting the router configuration.
*   **Session Control:** Use MikroTik session management to view connected users, and terminate unwanted sessions.

## MikroTik REST API Examples:

These examples assume that the router's API service is enabled.

*   **Get User List (GET):**
    *   **Endpoint:** `/rest/user`
    *   **Method:** GET
    *   **Request:** (No payload)
    *   **Example with cURL:**

        ```bash
        curl -u admin:password -k https://<router_ip>/rest/user
        ```
    *   **Expected Response:** JSON array of user objects.

        ```json
        [
          {
            ".id": "*0",
            "name": "admin",
            "group": "full"
           },
           {
            ".id": "*1",
            "name": "monitor-user",
            "group": "monitoring"
           },
           {
           ".id": "*2",
           "name": "admin-user",
           "group": "restricted-admin"
          }
       ]
        ```

*   **Add User (POST):**
    *   **Endpoint:** `/rest/user`
    *   **Method:** POST
    *   **JSON Payload:**
        ```json
       {
         "name": "api-user",
         "group": "monitoring",
         "password": "apiuserpassword"
       }
        ```
    *   **Example with cURL:**
        ```bash
        curl -u admin:password -k -X POST -H "Content-Type: application/json" -d '{"name": "api-user", "group": "monitoring", "password": "apiuserpassword"}' https://<router_ip>/rest/user
        ```
    *   **Expected Response:** JSON object of the added user.

        ```json
        {
        ".id":"*3",
        "name":"api-user",
        "group":"monitoring"
        }
        ```
    *   **Error Handling:** if the user cannot be created, an error message will be shown in the response. for example `{"message":"already have user with that name"}`. Error responses may vary and should be handled gracefully.

## Security Best Practices:

*   **Strong Passwords:** Enforce complex passwords for all user accounts.
*   **Limited Admin Access:** Avoid granting full admin rights unless absolutely necessary.
*   **Regular Audits:** Regularly check user configurations to identify and remove unnecessary accounts.
*  **IP Restrictions:** restrict access to admin services via `/ip service`.
*   **API Security:** Secure the MikroTik API by requiring HTTPS and using complex passwords for API access, restricting by IP address if required.
*  **Firewall Rules:** Use the router firewall to protect the router itself. For example, only allow access via port 8291 (winbox) from trusted IP addresses.

## Self Critique and Improvements:

This configuration provides a basic framework for user management. Here are some improvements:

*   **More Granular Policies:**  We could create more granular policies for each user group to have more fine-grained control over what each user can do. Instead of `read` we could grant specific permissions to each command.
*   **User Profiles for Specific Rate Limits:**  Assign specific user profiles to limit user bandwidth based on their user group.
*   **Automated User Management:**  Implement scripts to automate the creation, modification, and removal of users.
*   **Centralised Logging:** Send audit logs to a syslog server, to track changes made by different users and to identify any suspicious activity.
*   **Monitoring:** Monitor login attempts, and be notified on failed logins.
*   **API Token Authentication:** Consider implementing API Token Authentication instead of basic authentication to increase API security.
* **Role-Based Access Control:** Develop a complete role-based access control framework.

## Detailed Explanations of Topic:

MikroTik's user management system allows you to create accounts with varying levels of access to the router. This is done by combining user accounts, user groups, and policies.

*   **Users:** Represents an individual who logs into the MikroTik RouterOS. Each user can belong to a single user group.
*   **User Groups:** Provide a way to group similar users together, with shared policies.
*   **Policies:** Define the specific permissions granted to users. These permissions allow users to perform a certain action. Some common policies are `read`, `write`, `test`, `password`, `web`, `winbox`, `api`, `ftp`, `reboot`, `local`, `telnet`, `ssh`, `dude`, `console`.

## Detailed Explanation of Trade-offs:

*   **Granular vs. Simple Policies:** Using very granular policies gives very fine-grained control but it can be difficult to maintain. A simpler set of policies such as `read`, `write`, or `full` is easier to understand but provides less control.
*   **Local vs. RADIUS Authentication:** Local authentication is simple to setup, but lacks the features and scalability that a RADIUS based server provides, such as centralised logging, enforcement of password policies, and support for two-factor authentication.
*   **Number of Users:** The more users a router needs to handle, the more resources it will require. It is important to select an appropriate router model for the amount of users planned.

## Configuration for Specific RouterOS Versions:

These instructions are compatible with RouterOS 6.48 and later, including RouterOS 7.x. There are no specific version considerations for this particular configuration. If there are any commands that are version specific they will be mentioned in the relevant section.
