Okay, let's craft a detailed technical document for managing users and user groups on a MikroTik RouterOS device, focusing on the provided scenario.

## Scenario Description:

We need to create and manage user accounts with specific permissions to access the MikroTik router for administrative purposes. Specifically, we'll establish two user groups: `readonly` which will have limited access and `fullaccess` which will have complete control. We will then create two users, one belonging to each group. This approach allows for a more structured and secure administration of the router, especially in environments where multiple individuals may require access. The target interface for these users is the network segment connected to `ether-15`, with an address on the `195.229.117.0/24` subnet.

## Implementation Steps:

Here's a step-by-step guide to implement user and group management on your MikroTik device, covering CLI and Winbox GUI equivalents.

### **Step 1: Create the User Groups**

*   **CLI:**
    ```mikrotik
    /user group add name=readonly policy=read
    /user group add name=fullaccess policy=write,test,password,reboot,read,policy
    ```
    *   **Explanation:**
        *   `/user group add`:  Creates a new user group.
        *   `name=readonly`: Assigns the name "readonly" to this group.
        *   `policy=read`:  Sets the access policy for this group to read only.
        *   `name=fullaccess`: Assigns the name "fullaccess" to this group.
        *   `policy=write,test,password,reboot,read,policy`: Grants all common permissions to the `fullaccess` group.  This is equivalent to full admin access.

*   **Winbox:**
    1.  Navigate to `System` -> `Users` -> `Groups`.
    2.  Click `Add New`.
    3.  Enter `readonly` as the name, check the `read` permission and click `Apply`.
    4.  Click `Add New` again.
    5.  Enter `fullaccess` as the name, check all permissions (write, test, password, reboot, read, policy) and click `Apply`.

*   **Before:** The router has no custom groups, default user groups like `read` and `write` will be present.
*   **After:** Two new groups are available: `readonly` and `fullaccess`.

### **Step 2: Create User Accounts**

*   **CLI:**
    ```mikrotik
    /user add name=viewer group=readonly password=SecurePassword123
    /user add name=admin group=fullaccess password=AnotherSecurePassword456
    ```

    *   **Explanation:**
        *   `/user add`:  Creates a new user account.
        *   `name=viewer`: Assigns the username "viewer".
        *   `group=readonly`: Adds this user to the `readonly` group.
        *   `password=SecurePassword123`: Sets the password for the user "viewer". **Remember to use strong passwords in a real-world environment**.
        *   `name=admin`: Assigns the username "admin".
        *   `group=fullaccess`:  Adds this user to the `fullaccess` group.
        *   `password=AnotherSecurePassword456`: Sets the password for user "admin".

*   **Winbox:**
    1.  Navigate to `System` -> `Users`.
    2.  Click `Add New`.
    3.  Enter `viewer` as the name, select `readonly` as the group, and enter the password `SecurePassword123`. Click `Apply`.
    4.  Click `Add New` again.
    5.  Enter `admin` as the name, select `fullaccess` as the group, and enter the password `AnotherSecurePassword456`. Click `Apply`.

*   **Before:** The router has only default users, likely including the `admin` user with default settings.
*   **After:** Two new users are present `viewer` and `admin` with the specified group memberships.

### **Step 3: (Optional) Disable the default admin user**

For security, it is recommended to disable the default admin user.
*   **CLI:**
    ```mikrotik
    /user disable admin
    ```
*   **Winbox:**
    1. Navigate to `System` -> `Users`
    2. Select the `admin` user
    3. Uncheck the `Enabled` checkbox.

*   **Before:** The default `admin` user is enabled and potentially vulnerable to attacks.
*   **After:** The `admin` user is disabled, making it more secure. Ensure you have created at least one other administrative user with full access before taking this step.

## Complete Configuration Commands:

```mikrotik
/user group add name=readonly policy=read
/user group add name=fullaccess policy=write,test,password,reboot,read,policy
/user add name=viewer group=readonly password=SecurePassword123
/user add name=admin group=fullaccess password=AnotherSecurePassword456
/user disable admin
```

## Common Pitfalls and Solutions:

*   **Lost Access:** If you lock yourself out (e.g., disabling all admin users), you may need to use Netinstall to reset the router. Be sure to have a working full access user before you disable all other administrative user accounts.
*   **Weak Passwords:** Use strong, unique passwords to protect user accounts, and ideally set a complex password policy. MikroTik does not provide a built in password policy engine.
*   **Incorrect Permissions:** Double check the user group permissions. Incorrectly assigned policies can hinder the operations of each user.
*   **Disabled Accounts:** Ensure that the appropriate user accounts are enabled if they need to be used.
*   **Resource Issues:**  User management on its own does not usually cause resource issues (CPU or memory). However, If the router is under a DDOS attack, multiple concurrent logins could impact resources.
*   **Security Issues:** Using default credentials is a massive security issue. Always change these, and disable default user accounts.
*   **IP Address Issues:** While users are being created, no IP address is being configured. As long as there is an IP on `ether-15`, the user can connect over the network to manage the device via Winbox, SSH, or the web interface. If no address is configured, users will not be able to access the router remotely. You should configure an address on interface `ether-15`.
    ```mikrotik
    /ip address add address=195.229.117.1/24 interface=ether-15
    ```
*   **Solution:** Ensure the router is set up with the correct address on the desired interface, ensure proper permissions are granted, and enable appropriate user accounts. If you lose access, reset the router.

## Verification and Testing Steps:

1.  **Login Test:** Use Winbox, SSH, or the web interface to attempt to log in as both the `viewer` and the `admin` users.
    *   `viewer` should be able to view configuration but not modify it.
    *   `admin` should be able to modify configurations.
2.  **Try read-only access with the `viewer` user.** Log in using Winbox, and try to add or modify configurations. You should be blocked.
3. **Try full-access with the `admin` user.** Log in using Winbox, and modify configurations. You should be able to do so.
4.  **CLI access testing:** Log into a terminal emulator with SSH and try to execute commands that require write permissions as `viewer`. You should get a permission denied error. Log in as `admin` and execute the same commands. You should be successful.
5.  **Log Analysis:** Check the MikroTik logs (`/log print`) for login and authentication events. Pay attention to failed login attempts. This is valuable for security auditing.

## Related Features and Considerations:

*   **API Access:** Consider restricting API access using user groups and policies.
*   **Radius Authentication:** Use RADIUS for centralized authentication if needed for larger deployments.
*   **SSH Keys:** Use SSH keys for password-less authentication, which can improve security.
*   **User Monitoring:** Monitor user sessions and activity. Use logging to your advantage.
*   **Specific Policies:** The `policy` parameter can take a variety of flags. For example `ftp` would be used for FTP access to the router.

## MikroTik REST API Examples (if applicable):

While not a core focus for user and user group management, you can use the REST API to create users, groups, and manage authentication. Here are example API calls:

**API Endpoint**: `/user`

**Create a User**

*   **Request Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
      "name": "apiuser",
      "group": "fullaccess",
      "password": "AnotherSecurePassword789"
    }
    ```
*   **Expected Response (200 OK):**
    ```json
    {
      ".id": "*2",
      "name": "apiuser",
      "group": "fullaccess",
       "disabled": "false"
    }
    ```
*   **Error Handling:** If the name already exists or an invalid policy is set, the API will return a 400 error with a corresponding message. Example:
    ```json
    { "message": "already have user with name apiuser",
      "error": true
    }
    ```

**Get User List**
*   **Request Method:** `GET`
*   **No Payload:**
*    **Example Response (200 OK)**
  ```json
[
    {
        ".id": "*1",
        "name": "viewer",
        "group": "readonly",
        "disabled": "false"
    },
    {
        ".id": "*2",
        "name": "admin",
        "group": "fullaccess",
        "disabled": "false"
    },
    {
        ".id": "*3",
         "name": "apiuser",
        "group": "fullaccess",
        "disabled": "false"
    }
]
  ```
**API Endpoint**: `/user/group`

**Create a Group**
*   **Request Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
        "name": "apigroup",
        "policy": "read"
    }
    ```
*   **Expected Response (200 OK):**
    ```json
    {
        ".id": "*2",
        "name": "apigroup",
        "policy": "read"
    }
    ```
*   **Error Handling:** If the group name exists, it will return a 400 error.

**Delete a Group**
*   **Request Method:** `DELETE`
*   **Example Payload:** (requires the .id value)
    ```json
    {
        ".id": "*2"
    }
    ```
*   **Expected Response (200 OK):**
  ```json
  {
  }
  ```

**Important:**
*   Ensure your RouterOS device has the `api` service enabled and that you have an user with enough privilege to access the API.
*   The API may differ between RouterOS versions. Always check the relevant documentation for your version.
*   When deleting users or groups, it is possible you might run into errors due to dependencies, (user using a group that you are deleting.) Always ensure no other configuration depends on the resource you are deleting.

## Security Best Practices

*   **Strong Passwords:** Implement a policy of enforcing complex, unique passwords.
*   **Least Privilege:** Assign the minimum necessary permissions to user groups.
*   **Disable Default Admin:** Disable the default admin user to prevent unauthorized access.
*   **Limit Access:** Restrict access to management interfaces to trusted IP addresses.
*   **Audit Logs:** Regularly review logs for login attempts and suspicious activity.
*   **Regular Updates:** Keep RouterOS software up-to-date with the latest security patches.
*   **SSH Key authentication:** Implement SSH key authentication to avoid password related attacks.
*   **Change SSH default port:** Change the SSH port to a non standard port.
*   **Use encrypted protocols:** Always use encrypted protocols for accessing the router, such as HTTPS and SSH. Avoid using Telnet.
*   **Use firewall rules:** Implement firewall rules that would block any unauthorized access attempt to ports used for administration.

## Self Critique and Improvements

*   **More complex group policies:**  The `policy` argument of groups could use further refinement, allowing for granular control over specific features. For example, you can create a group with only `sniff` policy if that's necessary.
*   **Dynamic access lists:** Using dynamic lists of IPs to control access can make administration less error prone.
*   **Centralized authentication:** Using RADIUS could improve access control to many devices.
*   **Password complexity:** Implement a strong password complexity and regular change policy.
*   **Multi Factor Authentication:** Implementing multi-factor authentication will significantly improve security, however this would require an external authentication server.

## Detailed Explanations of Topic

**Users:** In MikroTik RouterOS, a user represents an entity that can log into the device for management or other functions. Users are associated with a group, which dictates their capabilities. You can create, modify, and delete user accounts. Each user has a username, password, and group assignment. User accounts control access to management features of the MikroTik router.

**User Groups:** User groups are a way to bundle a set of permissions. By putting user accounts into groups, you avoid the need to configure each user manually. User groups simplify the management of access control. Each group has a policy that defines its members' rights and permissions. User groups enable you to apply consistent policies to multiple users. The `policy` argument within a group allows for specifying particular administrative access such as `read, write, test, password, policy, reboot, ftp, sniff, romon`.

## Detailed Explanation of Trade-offs

*   **Simple vs. Granular Control:** Using simple `readonly` and `fullaccess` groups is easy to manage but less secure. Creating custom groups with specific policies provides better security, but it requires more careful planning and configuration.
*   **Local vs. RADIUS Authentication:** Local user accounts are easy to set up, but they can be harder to manage in large deployments. RADIUS allows for centralized authentication and better security in large networks, but it requires an external server and setup.
*   **API Access vs. GUI:** API access provides automation and programmatic control but requires understanding the API, while GUI access is user-friendly but might not be scalable. The API is much more efficient for large scale management.
*   **Password Complexity vs. User Convenience:** Enforcing complex passwords improves security but makes it harder for users to remember them. The trade-off needs to balance user convenience and security. It may be beneficial to implement a password manager policy, so the burden is taken away from the user.

## Configuration for Specific RouterOS Versions:

The provided commands are valid for RouterOS versions 6.48 and 7.x. However, always consult the specific documentation for your RouterOS version in case of discrepancies. The core commands for user and group management remain mostly unchanged between these versions.

This comprehensive document should provide you with a thorough understanding of how to effectively manage users and user groups on your MikroTik RouterOS device. Remember to adapt the provided examples to your specific needs and security requirements.
