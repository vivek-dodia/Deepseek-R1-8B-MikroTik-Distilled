Okay, let's dive deep into configuring user management and user groups on a MikroTik RouterOS device, specifically for your given subnet and interface, and targeting RouterOS 7.11.

## Scenario Description:

This scenario focuses on creating a user group with specific permissions and then assigning a user to that group. We'll then demonstrate the implications of these permissions. The scenario specifically addresses an SMB network where you might want to delegate specific administration tasks to a team member without providing full administrative access. This can be applied to various roles within an organization. We will create a user with the minimum privileges to change the device's system time.

## Implementation Steps:

Here's a step-by-step guide with detailed explanations for each step:

### Step 1: Initial State and Setup
First, let's ensure we're in a known state. We'll check existing users and groups.

*   **Action:** Check the current users and user groups.
    *   **Command (CLI):**
        ```mikrotik
        /user print
        /user group print
        ```
    *   **Winbox:** Navigate to `System` -> `Users`.
    *   **Expected Output:** Initially you should see at least the `admin` user group and the `admin` user.

*   **Before:** Standard setup, likely with only the default 'admin' user and group.
*   **After:** The output of the commands shows current existing users and user groups.

### Step 2: Create a New User Group

We will create a new group called "time_managers" and assign it very specific permissions.
*   **Action:** Create the user group called 'time_managers' with only the privilege to `write` the `system` namespace, and `read` on all namespaces.
*   **Command (CLI):**
    ```mikrotik
    /user group add name=time_managers policy=read,system
    /user group set time_managers policy=read,system
    /user group set time_managers add-policy=write
    ```
*   **Winbox:**
    *   Navigate to `System` -> `Users` -> `Groups` tab.
    *   Click the `+` button.
    *   Name: `time_managers`.
    *   Policies:
        *   Click `Read`
        *   Click `System`
        *   Click `Write`
    * Click `Apply` and `OK`
*   **Explanation:**
    *   `user group add name=time_managers`: Creates the new user group with the name `time_managers`.
    *   `policy=read,system`: The initial policy is set to grant `read` access to all resources and also grants `read` to the `system` namespace.
    *   `add-policy=write`: Modifies the policy of `time_managers` by adding write access for the system namespace. This allows modification of the time of the device.
*  **Before:** Existing users and groups.
*  **After:** A new group named `time_managers` exists and has restricted privileges.

### Step 3: Create a New User and Assign to User Group

Now we'll create a new user and assign it to our newly created group.

*   **Action:** Create user "time_user" and assign it to the "time_managers" group, with password 'StrongPassword123'.
*   **Command (CLI):**
    ```mikrotik
    /user add name=time_user group=time_managers password=StrongPassword123
    ```
*   **Winbox:**
    *   Navigate to `System` -> `Users`.
    *   Click the `+` button.
    *   Name: `time_user`.
    *   Group: `time_managers`.
    *   Password: `StrongPassword123`.
    *   Click `Apply` and `OK`
*   **Explanation:**
    *   `user add name=time_user group=time_managers`: Creates a new user `time_user` and assigns it to the `time_managers` group.
    *   `password=StrongPassword123`: Sets the user's password. **Remember to use a strong password in a real-world scenario.**
*  **Before:**  Only existing users are present.
*  **After:** A new user `time_user` is available assigned to the group `time_managers`.

### Step 4: Verification of Permissions

Now, we verify the assigned permissions by attempting changes on the device with the new user.

*   **Action:** Connect to the RouterOS device using the `time_user` account and attempt to modify device time.
    *   Connect via SSH or Winbox using the username `time_user` and the password you assigned.
    *   **Command (CLI, logged in as `time_user`):**
        ```mikrotik
        /system clock set time=12:00:00
        ```
    *   **Winbox:** Try to change the system time through the GUI.
*   **Expected Output:** The command should execute successfully. If you try to access anything other than the system clock, you'll see an "access denied" error, verifying our restricted privileges are working.
*  **Before:** No attempts to use the new user on the device.
*  **After:** The new user can change the system time but no other parameters.

### Step 5: Attempting unauthorized access

Now, we try to access areas where we did not grant permission and demonstrate an "access denied" response.

*   **Action:** With `time_user`, attempt to change an interface name.
    *   **Command (CLI, logged in as `time_user`):**
        ```mikrotik
        /interface ethernet set ether-28 name=new-name
        ```
    *  **Winbox:** Attempt to rename an interface using the Winbox GUI, logged in as `time_user`.
*   **Expected Output:** The command will return an `access denied` error, this is due to the user not having permission to modify interface settings.
* **Before:** No attempts to perform actions out of scope.
* **After:** The user receives an `access denied` response, therefore not modifying the device's configuration.

## Complete Configuration Commands:
```mikrotik
/user group add name=time_managers policy=read,system
/user group set time_managers policy=read,system
/user group set time_managers add-policy=write
/user add name=time_user group=time_managers password=StrongPassword123
```

## Common Pitfalls and Solutions:
*   **Incorrect Policy Assignment:** Incorrect permissions can render the user either with too much access or unable to do necessary tasks. Double-check the policies to avoid granting unnecessary privileges. Use the `print` command to confirm the permissions.
    *   **Solution:** Carefully review the policies using `/user group print detail`. Ensure that only the necessary `read` and `write` options are enabled for the correct namespaces.
*   **Weak Password:** Using a simple or guessable password can easily lead to a security breach.
    *   **Solution:** Always use strong, complex passwords. For automated deployments use encrypted configurations or RouterOS secrets.
*   **User Lockout:** After several failed login attempts, a user may be locked out. This can be difficult to troubleshoot if not expected.
    *   **Solution:** Use the `/user print` command and check the `disabled` column for possible account lockouts. Use the `enable` command to unlock the user, or change the `failed-login-attempts` setting in `/system routerboard settings` to a higher value if required.
*   **Missing Access:** If the user cannot access the resource at all, then you did not give it `read` permission to that namespace.
    *   **Solution:** Make sure the `read` policy exists for the resource, and that the user is in the correct group.

## Verification and Testing Steps:
1.  **User Login:** Connect to the router using the new `time_user` with its password. This verifies the credentials work.
2.  **Permission Testing:** Execute commands like `/system clock print` (read access test), followed by `/system clock set time=10:00:00` (write access test within system namespace).
3.  **Unauthorized Access Testing:**  Try commands that require other policies, like `/interface print`, should return `access denied`.
4. **Group Listing:** List the existing groups and check if the `time_managers` group exists.
    ```mikrotik
    /user group print
    ```
5. **User Listing:** List all users to make sure the `time_user` user has been created and is in the `time_managers` group.
    ```mikrotik
    /user print
    ```
6.  **Winbox Verification:** Connect via Winbox with the `time_user` and verify the access to restricted features.

## Related Features and Considerations:
*   **RouterOS API:** User management can be fully automated via the RouterOS API. This is incredibly useful for managing large deployments.
*   **RADIUS Authentication:** Instead of local users, authenticate users via RADIUS for centralized management.
*   **User Session Monitoring:** Monitor active user sessions via the `/user active print` command.
*   **User Profiles:** You can use user profiles with different policies assigned to specific users without groups.
*   **Time of Day Access Restriction:** This restriction allows granular control over the time during which an account can be used.

## MikroTik REST API Examples:

Here are some API examples for user and group management:

**Example 1: Create a new user group via API**

*   **Endpoint:** `/user/group`
*   **Method:** POST
*   **JSON Payload:**
    ```json
    {
        "name": "api_time_managers",
        "policy": "read,system"
    }
    ```
*   **Expected Response (Success):**
    ```json
    {
        ".id":"*F",
        "name":"api_time_managers",
        "policy":"read,system",
        "comment":""
    }
    ```
*   **Error Handling:** If the name is not unique (e.g., the group already exists), the API returns a 400 status code and error details in JSON format.
    ```json
        {
            "message": "input does not match the expected format: already have such group",
            "error":"already-have-such-group"
        }
    ```

**Example 2: Create a user via API and set it to a group**

*   **Endpoint:** `/user`
*   **Method:** POST
*   **JSON Payload:**
    ```json
    {
        "name": "api_time_user",
        "group": "api_time_managers",
        "password": "AnotherStrongPassword123"
    }
    ```
*   **Expected Response (Success):**
    ```json
    {
        ".id":"*G",
        "name":"api_time_user",
        "group":"api_time_managers",
        "comment":"",
        "last-login":"never"
    }
    ```
* **Error Handling:** Similar to the group add call, the API will return a 400 status code in case of a duplicate user, or a group not existing.
    ```json
        {
            "message": "input does not match the expected format: user exists",
            "error":"user-exists"
        }
    ```

**Example 3: Add a policy to an existing user group using the API**

*   **Endpoint:** `/user/group/*F` (where *F is the ID of the group you want to change, see the response of Example 1)
*   **Method:** PATCH
*  **JSON Payload**
    ```json
        {
            "add-policy":"write"
        }
    ```
*   **Expected Response (Success):**
    ```json
    {
        ".id":"*F",
        "name":"api_time_managers",
        "policy":"read,system,write",
        "comment":""
    }
    ```
*   **Error Handling:** If the `add-policy` property is not valid, or the group with ID `*F` does not exist, the API returns a 400 status code and error details in JSON format.

## Security Best Practices:

*   **Principle of Least Privilege:**  Grant users only the necessary privileges to perform their tasks. Avoid giving admin access unless absolutely required.
*   **Strong Passwords:** Enforce strong password policies.  Use a mix of uppercase, lowercase, numbers, and special characters.
*   **Regular Auditing:** Regularly review user accounts and group memberships to ensure no unauthorized accounts exist.
*   **Secure API Access:** When using the API, secure your keys, avoid exposing these in plaintext, use environmental variables or secrets management systems. Always use a dedicated user for the API calls with only the required permissions.
*   **HTTPS for API Access:**  Always use HTTPS for API access to prevent interception of the credentials and data.
*   **Disable Unused Services:** If you're not using the API, consider disabling the service to minimize security risks.
*   **Audit Logging:** Enable audit logging for user management to detect any unusual activity.
*   **RouterOS Updates:** Keep RouterOS updated to the latest stable version for crucial security patches.

## Self Critique and Improvements:

*   **More Granular Policies:** The `system` policy is broad. We could further break this down to only `system/clock` or similar to isolate the permissions even further, but may make the setup more complex and harder to troubleshoot.
*   **Use of Secrets:** Instead of static passwords, consider using RouterOS secrets (stored using AES encryption) for API authentication or external authentication systems. This would be more secure.
*   **Dynamic IP Restriction:** Further security is added if you restrict login access to the user to specific IP addresses.
*   **Two-Factor Authentication:** For very sensitive environments, use two-factor authentication for enhanced security.

## Detailed Explanations of Topic

### Users:
In MikroTik RouterOS, users are the entities that can access the router via different methods (Winbox, SSH, Telnet, API). Each user has a username, password, and is assigned to a user group or a profile. The group defines their access and permission level.

### User Groups:
User groups are collections of users that share the same policies. Policies define the permissions that group members have, and are granted via namespaces, which provide granular control over what can be done. A user can belong to only one group at a time. This simplifies management of multiple users with similar access permissions.

### Policies:
Policies specify the level of access a user or group has for different namespaces (areas) of the RouterOS device. These are usually configured in the following way:
*   **read:** The user can see data in this area.
*   **write:** The user can write or change data.
*   **test:** The user can perform test operations.
*   **password:** The user can change their own password.
*   **ftp:** The user can access files.
*   **reboot:** The user can reboot the system.
*   **policy:** The user can modify other policies.
*   **api:** The user can execute API requests.

### Namespaces
Namespaces are areas of the RouterOS device. Each area has different commands. A namespace example is:
*   `/interface`: All interfaces configuration such as Ethernet, Wireless, VLAN, etc.
*   `/ip`: All IP configuration, like firewall, address lists, routes, services.
*  `/system`: RouterOS general configuration, such as clock, resources, licensing, logging.

## Detailed Explanation of Trade-offs

*   **Granular Policies vs. Management Complexity:** While granular policies like `/system/clock` give the tightest level of security, they also increase the complexity of your setup, making it harder to manage and troubleshoot, especially if permissions are not well documented.
*   **Local Users vs. RADIUS:** Using local users is simple for small setups, but RADIUS offers centralized user management for larger networks. RADIUS introduces an extra service dependency (RADIUS server), and may add complexity in large deployments.
*   **User Groups vs. User Profiles:** User groups assign the same policies to all their members, while user profiles allow for each user to have different, distinct policies. User profiles are beneficial when very different roles are needed, but will increase setup time. Using groups is a good tradeoff between simplicity and scalability.
*  **Command-line vs. GUI:** While the GUI interface provides an easy to use method for setting parameters, using the command line and scripting allows for more automation, and precise control of your device, but has a steeper learning curve.

## Configuration for Specific RouterOS Versions:

This documentation is targeted for RouterOS 7.11 (6.48, 7.x). Please note that, while most settings are backwards compatible, some new commands may be added, or some commands may behave differently from previous versions. Always test your configurations in a staging environment before production to ensure that the desired result is achieved.

This comprehensive guide should give you a solid foundation for user and group management on your MikroTik device. Always prioritize security, keep your documentation up-to-date, and test your configurations thoroughly.
