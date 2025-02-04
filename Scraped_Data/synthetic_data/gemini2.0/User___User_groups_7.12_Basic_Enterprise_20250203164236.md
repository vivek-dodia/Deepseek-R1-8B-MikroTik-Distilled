Okay, let's craft a detailed technical document on user and user group management in MikroTik RouterOS, targeting version 7.12, with a focus on an Enterprise scale network and a specific subnet and interface.

## Scenario Description:

This scenario addresses the need to control access to a MikroTik router by creating different user accounts with varying levels of permissions. We will create a basic user with limited access and a more privileged administrative user group. This is commonly required in enterprise environments for security, auditing, and separating operational responsibilities. We will apply these users to the 'wlan-51' interface.

## Implementation Steps:

Here's a step-by-step guide to configuring users and user groups, with examples of both CLI and Winbox GUI instructions:

**1. Step 1: Understand Default User & Groups**

*   **Explanation:** Before creating new users, it's important to know the existing default user and user groups.
*   **CLI Example (Before):**
    ```mikrotik
    /user print
    /user group print
    ```
*   **Expected Output (Before):** You should see the default 'admin' user and group(s).
*   **Winbox GUI:**
    *   Navigate to "System" -> "Users" to view users.
    *   Navigate to "System" -> "Users" -> "Groups" to view user groups.
*   **Effect:** This step provides baseline information.

**2. Step 2: Create a New User Group - "LimitedAccess"**

*   **Explanation:** We will create a new group called "LimitedAccess" with minimal permissions.
*   **CLI Example:**
    ```mikrotik
    /user group add name=LimitedAccess policy=read
    ```
    *   `name=LimitedAccess`: Assigns the name "LimitedAccess" to the new group.
    *   `policy=read`: Grants only read permissions.
*   **Winbox GUI:**
    1.  Navigate to "System" -> "Users" -> "Groups".
    2.  Click the "+" button.
    3.  In the "Name" field, enter "LimitedAccess".
    4.  In the "Policy" field, select "read".
    5.  Click "Apply" or "OK".
*   **CLI Example (After):**
    ```mikrotik
    /user group print
    ```
*   **Expected Output (After):** You should see the newly created "LimitedAccess" group in the list with read-only permissions.
*   **Effect:** A user group with restricted permissions is created.

**3. Step 3: Create a New User - "monitor-wlan" and assign it to the "LimitedAccess" group**

*   **Explanation:** A user named "monitor-wlan" will be created and assigned to the "LimitedAccess" group for restricted access to the router. We will also specify that this user is allowed to log in only through the "wlan-51" interface.
*   **CLI Example:**
    ```mikrotik
    /user add name=monitor-wlan group=LimitedAccess password="StrongPassword123!"  address=177.47.48.0/24 allowed-address=177.47.48.0/24
    ```
    *   `name=monitor-wlan`: Assigns the username "monitor-wlan".
    *   `group=LimitedAccess`: Assigns the user to the "LimitedAccess" user group.
    *   `password="StrongPassword123!"`: Sets a password for the user (replace with a strong password).
    *   `address=177.47.48.0/24`: Limits login to clients within the 177.47.48.0/24 subnet.
     *   `allowed-address=177.47.48.0/24`: Limits access from clients on the 177.47.48.0/24 subnet.
*   **Winbox GUI:**
    1.  Navigate to "System" -> "Users".
    2.  Click the "+" button.
    3.  In the "Name" field, enter "monitor-wlan".
    4.  In the "Group" field, select "LimitedAccess".
    5.  Enter a strong password in the "Password" and "Confirm Password" fields.
    6.   Enter 177.47.48.0/24 in "Address"
   7.   Enter 177.47.48.0/24 in "Allowed Address"
    8.  Click "Apply" or "OK".
*   **CLI Example (After):**
    ```mikrotik
    /user print
    ```
*   **Expected Output (After):** You will see the new "monitor-wlan" user listed with the "LimitedAccess" group and address restrictions.
*   **Effect:** A user with limited rights can connect only from a specified subnet, enhancing security.

**4. Step 4: Create a New Admin User Group - "WLANAdmin"**

*   **Explanation:** We will create a new administrative group with all rights, and then create an admin user assigned to this group and limit its access to the subnet '177.47.48.0/24'.
*   **CLI Example:**
    ```mikrotik
    /user group add name=WLANAdmin policy=write,read,test,password,web,api
    ```
    *   `name=WLANAdmin`: Assigns the name "WLANAdmin" to the new group.
    *   `policy=write,read,test,password,web,api`: Grants all permissions.
*   **Winbox GUI:**
    1.  Navigate to "System" -> "Users" -> "Groups".
    2.  Click the "+" button.
    3.  In the "Name" field, enter "WLANAdmin".
    4.  In the "Policy" field, select "Full".
    5.  Click "Apply" or "OK".
*   **CLI Example (After):**
    ```mikrotik
    /user group print
    ```
*  **Expected Output (After):** You will see the new "WLANAdmin" group.
*   **Effect:** A user group with administrative access is created.

**5. Step 5: Create a New Admin User - "admin-wlan"**

*   **Explanation:** A user named "admin-wlan" will be created and assigned to the "WLANAdmin" group for full access to the router. We will also specify that this user is allowed to log in only through the "wlan-51" interface, represented by the subnet '177.47.48.0/24'.
*   **CLI Example:**
    ```mikrotik
    /user add name=admin-wlan group=WLANAdmin password="AnotherStrongPassword123!" address=177.47.48.0/24 allowed-address=177.47.48.0/24
    ```
    *   `name=admin-wlan`: Assigns the username "admin-wlan".
    *   `group=WLANAdmin`: Assigns the user to the "WLANAdmin" user group.
    *   `password="AnotherStrongPassword123!"`: Sets a password for the user (replace with a strong password).
    *  `address=177.47.48.0/24`: Limits login to clients within the 177.47.48.0/24 subnet.
    *  `allowed-address=177.47.48.0/24`: Limits access from clients on the 177.47.48.0/24 subnet.
*   **Winbox GUI:**
    1.  Navigate to "System" -> "Users".
    2.  Click the "+" button.
    3.  In the "Name" field, enter "admin-wlan".
    4.  In the "Group" field, select "WLANAdmin".
    5.  Enter a strong password in the "Password" and "Confirm Password" fields.
     6.   Enter 177.47.48.0/24 in "Address"
    7.   Enter 177.47.48.0/24 in "Allowed Address"
    8.  Click "Apply" or "OK".
*   **CLI Example (After):**
    ```mikrotik
    /user print
    ```
*   **Expected Output (After):** You will see the new "admin-wlan" user listed with the "WLANAdmin" group and address restrictions.
*   **Effect:** A user with administrative rights can connect only from a specified subnet, enhancing security.

**6. Step 6: Disable Default Admin User (Optional)**

*   **Explanation:** For enhanced security, you may disable the default "admin" user.
*   **CLI Example:**
    ```mikrotik
    /user disable admin
    ```
    *   `disable admin`: Disables the user with the name "admin".
*   **Winbox GUI:**
    1. Navigate to "System" -> "Users".
    2. Select the "admin" user.
    3. Uncheck "Enabled" checkbox.
    4.  Click "Apply" or "OK".
*   **CLI Example (After):**
    ```mikrotik
    /user print
    ```
*   **Expected Output (After):** You will see that the `enabled` column for the admin user indicates "no"
*   **Effect:** The default admin user is deactivated.

## Complete Configuration Commands:

```mikrotik
/user group add name=LimitedAccess policy=read
/user group add name=WLANAdmin policy=write,read,test,password,web,api
/user add name=monitor-wlan group=LimitedAccess password="StrongPassword123!" address=177.47.48.0/24 allowed-address=177.47.48.0/24
/user add name=admin-wlan group=WLANAdmin password="AnotherStrongPassword123!" address=177.47.48.0/24 allowed-address=177.47.48.0/24
/user disable admin
```

## Common Pitfalls and Solutions:

*   **Pitfall 1:** Forgetting user passwords.
    *   **Solution:** Keep passwords in a secure password manager. If lost, you will need to reset the router using the reset button.
*   **Pitfall 2:** Incorrect "address" and "allowed-address" settings.
    *   **Solution:** Double-check IP address and subnet masks carefully. Use "/ip address print" to verify assigned IPs of your client devices.
*   **Pitfall 3:** Overly permissive permissions.
    *   **Solution:** Stick to the principle of least privilege. Grant only necessary permissions to each group. Review the policy parameter for user groups.
*   **Pitfall 4:** Inadvertently locking out all users.
    *   **Solution:** Always test changes from a separate device. Have a backup console available. If locked out, use the reset button procedure.
*   **Pitfall 5:** High CPU or memory usage by large numbers of users with complex permission policies.
    *   **Solution:** Optimize user permissions, and limit the amount of active users. Consider using a Radius server for large user deployments.
*   **Pitfall 6:** The user configuration does not match the network requirements.
    *   **Solution:** Understand what each user requires and how the router is being used. Properly allocate resources to each user.

## Verification and Testing Steps:

1.  **Login with "monitor-wlan":**
    *   Attempt to log into the router using the "monitor-wlan" user credentials from a device within the 177.47.48.0/24 subnet.
    *   Verify that the user can only view configurations but not make changes. You can use the `print` command for checking configuration.
2.  **Login with "admin-wlan":**
    *   Attempt to log into the router using the "admin-wlan" user credentials from a device within the 177.47.48.0/24 subnet.
    *   Verify that the user can access all functionalities, make configurations, and access all RouterOS features.
3.  **Attempt to login with both users from different subnets.**
    * Verify that the users are not allowed access to the router from different subnets.
4.  **Attempt to login with "admin" user.**
    *   Verify that the default admin user can not access the router.
5.  **CLI tools:**
    * Use tools like `ping` to test connectivity from other machines. Use `/tool torch` to verify user traffic.

## Related Features and Considerations:

*   **RADIUS Authentication:** Use a RADIUS server for centralized user management, especially in large networks.
*   **User Logging:** Enable logging to track user activity for audit trails `/system logging add topics=user action=disk`.
*   **Session Timeouts:** Configure session timeouts to automatically log out inactive users.
*   **HTTPS/TLS:** Enforce HTTPS/TLS for secure connections to the router's web interface.
*   **API Access Control:** Configure separate API users with tailored permissions for automation.

In a real-world scenario, these configurations provide granular control over who can access the router, what actions they can take, and from which locations they can do so. This is vital for security, compliance, and network stability.

## MikroTik REST API Examples:

While not specifically for *creating* users, since they are stored locally on the router, the MikroTik API can be used to *view* or *modify* existing users and groups, including their properties. Here's an example of how to retrieve user information.

**API Endpoint:** `/user`
**Request Method:** `GET`

**Example Request (cURL):**
```bash
curl -k -u api-user:api-password https://your-router-ip/rest/user
```
* `-k` disables SSL certificate verification, use this with caution and use proper certificates in a production environment.
* `-u api-user:api-password` authentication credentials, ensure you use a user with API access granted.
**Example JSON Response (Successful):**
```json
[
    {
        ".id": "*1",
        "name": "admin",
        "group": "full",
        "address": "0.0.0.0/0",
        "allowed-address": "0.0.0.0/0",
        "disabled": "true",
        "last-logged-in": "sep/04/2024 17:16:58",
        "comment": ""
    },
        {
        ".id": "*2",
        "name": "monitor-wlan",
        "group": "LimitedAccess",
        "address": "177.47.48.0/24",
        "allowed-address": "177.47.48.0/24",
        "disabled": "false",
        "last-logged-in": "sep/04/2024 17:16:58",
         "comment": ""
    },
       {
        ".id": "*3",
        "name": "admin-wlan",
        "group": "WLANAdmin",
        "address": "177.47.48.0/24",
        "allowed-address": "177.47.48.0/24",
        "disabled": "false",
        "last-logged-in": "sep/04/2024 17:16:58",
        "comment": ""
    }
]
```

**Error Handling:**
If there's an error (e.g., invalid credentials), the response will include a `status` field with a code and message. For example:

```json
{"message":"invalid user name or password (6)", "status": 401}
```

**API Endpoint:** `/user/{.id}`
**Request Method:** `PATCH`

**Example Request (cURL) to disable a user:**
```bash
curl -k -X PATCH -H "Content-Type: application/json" -u api-user:api-password -d '{"disabled": "true"}' https://your-router-ip/rest/user/*2
```

**Parameter Explanation:**
* `/user`: The path to access the users.
* `/.id`: The id of the user to modify.
* `name`: (optional) Sets the username.
* `group`: (optional) Sets the user group.
* `address`: (optional) Sets the allowed address for login.
* `allowed-address`: (optional) Sets the allowed address for login.
* `disabled`: (optional) Enables or disables the user

**Important Considerations for the API:**
* Secure your API user accounts.
* Use HTTPS with proper certificates.
* Use the API for automation and monitoring, but be cautious about making critical changes through the API.

## Security Best Practices

*   **Strong Passwords:** Enforce strong and unique passwords for all users.
*   **Least Privilege:** Grant only necessary privileges to each user group.
*   **Address Restrictions:** Limit login IPs for added security and control.
*   **Disable Unused Accounts:** Always disable unused accounts or default accounts.
*   **Regular Review:** Regularly review user permissions to ensure they are still appropriate.
*   **Secure API access:** Implement proper API authentication.
*   **HTTPS:** Access the router via a secure connection with HTTPS

## Self Critique and Improvements:

*   **Current Configuration:** The current configuration provides a solid starting point for managing users in an enterprise environment. It clearly separates user roles and restricts access based on IP address.
*   **Improvements:**
    *   Implement RADIUS for larger user bases.
    *   Add detailed descriptions to each user and group to improve clarity.
    *   Implement user session timeouts.
    *   Enforce user password complexity requirements.
    *   Centralized logging and monitoring for user actions.
    *   Automation of user creation/modification using the API.

## Detailed Explanations of Topic

*   **Users:** A RouterOS user account enables a person to access the router and make changes. They are defined by a username, a password, a group and an access policy.
*   **User Groups:** User groups provide a way to organize multiple users with the same permissions. Each group has a specific access policy attached to it. You assign each user to a particular group based on the access requirements of that person.
*   **Policy:** The policy defines what an user within the given group is allowed to do. Available options are: read, write, test, password, web, and api. The sum of policies define the access rights of each particular user group.
*   **Address:** Allows the definition of an IP address range, from which a user can log into the router.
*    **Allowed-address**: Allows the definition of an IP address range, from which an access to the router is allowed.

## Detailed Explanation of Trade-offs

*   **Granular Permissions vs. Simplicity:** Creating numerous, finely-tuned user groups offers great security but introduces complexity in management. A few high-level groups are simpler but might compromise security if improperly defined.
*   **Local vs. RADIUS Authentication:** Local user management is simpler to set up for smaller networks but lacks scalability and central control. RADIUS offers centralized control and better security for large deployments but adds complexity.
*   **Restricting Access IPs:** Limiting login IP addresses provides extra security by reducing attack surface, but can create issues with users connecting from unexpected locations. It also adds extra management overhead if users frequently change their IPs.
*   **API vs CLI/WinBox:** The API allows automation and monitoring but has a steeper learning curve, while CLI and WinBox are more straightforward for manual configuration. The API might also present vulnerabilities if not properly secured.

## Configuration for Specific RouterOS Versions:

This configuration is specifically targeted for MikroTik RouterOS 7.12, but is applicable to other 7.x releases, as well as to 6.48, with some minor syntax differences.
All commands shown are compliant with versions 6.48 and higher.

This comprehensive documentation should provide a solid understanding of user and user group management in RouterOS, covering practical implementation, troubleshooting, and security best practices. Let me know if you have any further questions!
