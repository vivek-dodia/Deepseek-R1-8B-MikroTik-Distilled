Okay, let's dive into a detailed configuration for user management on a MikroTik router, targeting RouterOS 7.12, within an enterprise context, using a specific VLAN interface, and exploring relevant features.

## Scenario Description:

We need to implement user management on our MikroTik router, primarily for controlling access to resources within the 60.220.223.0/24 subnet, which is connected to the `vlan-36` interface. This includes creating user groups with specific permissions and assigning users to those groups. We'll focus on local user management rather than external RADIUS authentication. This scenario helps manage access for network administrators and other staff who need specific permissions on devices within this VLAN.

## Implementation Steps:

Here's a step-by-step guide, with CLI examples and explanations, plus Winbox GUI instructions where appropriate:

### Step 1: Review Current User Configuration

**Goal:** Inspect existing users and groups. This is crucial before making changes to avoid accidental lockouts or permission issues.

**CLI Command:**

```mikrotik
/user print
/user group print
```

**Winbox GUI:**
* Navigate to "System" > "Users".
* The "Users" tab shows the configured users.
* The "Groups" tab shows the configured groups.

**Explanation:**
* `user print` displays a list of all users, including the default "admin" user. Important information like enabled status, group membership, and creation dates are listed.
* `user group print` shows configured user groups and their permissions.

**Expected output:** The command displays the initial users and groups. Take note of the super administrator user and any additional users configured before moving to the next step.

### Step 2: Create User Groups

**Goal:** Define new user groups based on access needs.

**CLI Command:**

```mikrotik
/user group add name=net-admin policy=read,write,test,password,reboot,policy
/user group add name=net-view policy=read,test
```

**Winbox GUI:**
* Navigate to "System" > "Users".
* Select the "Groups" tab.
* Click the "+" button to add a new group.
* Set the name and policy.
* Click "Apply" and then "OK".

**Explanation:**

*   `/user group add name=net-admin policy=read,write,test,password,reboot,policy`: Creates a group called "net-admin" with full access except for `ftp` and `ssh` policies, allowing access to all configurations of the router, testing tools, and password settings, and router rebooting.
*   `/user group add name=net-view policy=read,test`: Creates a group called "net-view" with read-only access and access to testing tools (like ping, traceroute), suitable for monitoring but not modifying configurations.

**Before:**
* No additional user groups other than defaults.

**After:**
* "net-admin" and "net-view" user groups are created.

### Step 3: Add Local Users and Assign Groups

**Goal:** Create new users and assign them to the groups created in the previous step.

**CLI Command:**

```mikrotik
/user add name=john group=net-admin password=StrongPass1!
/user add name=jane group=net-view password=WeakPass2@
```
**Winbox GUI:**
* Navigate to "System" > "Users".
* Select the "Users" tab.
* Click the "+" button to add a new user.
* Set the name, group, and password.
* Click "Apply" and then "OK".

**Explanation:**
*   `/user add name=john group=net-admin password=StrongPass1!`: Creates a user named "john", assigns them to the "net-admin" group, and sets the password to `StrongPass1!`. **Use complex passwords for security reasons.**
*   `/user add name=jane group=net-view password=WeakPass2@`: Creates a user named "jane", assigns them to the "net-view" group, and sets the password to `WeakPass2@`.
*   **Note:** The user's password must meet the following minimum requirements:
    * It must contain at least eight characters.
    * It must contain at least one uppercase letter.
    * It must contain at least one lowercase letter.
    * It must contain at least one digit.
    * It must contain at least one special character.

**Before:**
* Only the default or previously created users exist.

**After:**
* "john" (net-admin) and "jane" (net-view) users are created with their assigned groups.

### Step 4: Optionally Disable or Modify the Default "admin" User

**Goal:**  For enhanced security, it's often best to rename the default "admin" user or disable it and create a new superuser.

**CLI Command:**

```mikrotik
/user set admin disabled=yes comment="Disabled for security reasons"
/user add name=superadmin group=full password=SuperStrongPass3$
```

**Winbox GUI:**
* Navigate to "System" > "Users".
* Select the "Users" tab.
* Select the "admin" user.
* Uncheck the "Enabled" checkbox.
* Optionally, modify or add a comment.
* Optionally, rename the "admin" user.
* Add a new superuser by clicking the + sign and filling the information.

**Explanation:**
* `/user set admin disabled=yes comment="Disabled for security reasons"`: Disables the "admin" user and adds a comment indicating why.
* `/user add name=superadmin group=full password=SuperStrongPass3$`:  Creates a new superuser with the full user group.

**Before:**
* The default "admin" user is active.

**After:**
* The default "admin" user is disabled, and a new superuser is created.

### Step 5: Verify the New Users and Groups

**Goal:** Confirm all configuration is correct.

**CLI Command:**

```mikrotik
/user print
/user group print
```

**Winbox GUI:**
* Navigate to "System" > "Users".
* Review "Users" and "Groups" tabs.

**Explanation:**
* These commands display all users and user groups, verifying that your changes were applied correctly.

**Expected output:** The new users, "john" and "jane", should appear, each with their assigned group, and the original "admin" user will be disabled or renamed.

## Complete Configuration Commands:

```mikrotik
/user print
/user group print
/user group add name=net-admin policy=read,write,test,password,reboot,policy
/user group add name=net-view policy=read,test
/user add name=john group=net-admin password=StrongPass1!
/user add name=jane group=net-view password=WeakPass2@
/user set admin disabled=yes comment="Disabled for security reasons"
/user add name=superadmin group=full password=SuperStrongPass3$
/user print
/user group print
```

## Common Pitfalls and Solutions:

*   **Lockout:** Accidentally disabling all administrative users.
    *   **Solution:** Be cautious when modifying user accounts. Ensure you have at least one active, fully functional user before disabling others. If locked out, netinstall will be required.
*   **Weak Passwords:** Using simple or easily guessable passwords.
    *   **Solution:** Enforce strong password policies for all users, including special characters, upper- and lowercase letters, and numbers.
*   **Incorrect Group Permissions:** Assigning the wrong policies to groups, restricting access unnecessarily or granting too much access.
    *   **Solution:** Carefully review and test the policy settings of each user group. Use the `test` policy to see which permissions are granted.
*   **Forgetting Passwords:**
    *   **Solution:** Keep a record of passwords (using a password manager) or ensure that the users themselves keep their passwords secure. If a password is forgotten, use the `user set password=` command.

## Verification and Testing Steps:

1.  **Login with New Users:**
    *   Attempt to login via SSH, Winbox, or the WebFig using the newly created users ("john" and "jane") to ensure the credentials work and to confirm group permissions.
    *   `john` should be able to make configuration changes.
    *   `jane` should only be able to read information (view), test the router (ping, traceroute).
2.  **`user print` and `user group print`:** Use these commands to check user and group details, ensuring correct assignments.
3.  **`/system resource monitor`:** Monitor CPU, memory, and disk usage to ensure no negative impact from additional users, but usually this is negligible for the type of configuration being built.
4.  **Login attempts and security:** Log the number of attempts to log in and track IP addresses from where the connections come from to keep the router secure.

## Related Features and Considerations:

*   **RADIUS Authentication:** Use RADIUS for external user authentication, allowing centralized user management.
    *   `system radius` commands are used to configure RADIUS servers.
*   **User Certificates:** Enhance security by implementing certificate-based user authentication instead of passwords.
    *   `certificate` commands are used to manage user certificates.
*   **API Users:** Create API-only users for managing the router programmatically.
    *   `user api` commands can manage permissions for API access.
*   **Hotspot:** If a hotspot is used, users can be managed through the hotspot user profile.

## MikroTik REST API Examples (if applicable):

Unfortunately, MikroTik's REST API doesn't directly support creating users and groups in a single atomic request. You'd need to use the `/user` and `/user/group` endpoints separately. Also note that user passwords are not retrievable via the API, only settable.

### Example: Creating a User via API (HTTP):

**API Endpoint:** `/rest/user`

**Request Method:** POST

**Example JSON Payload:**
```json
{
  "name": "apiuser",
  "group": "net-admin",
  "password": "SecureApiPass4$",
    "comment":"User created by API"
}
```

**Expected Response (Success - 201 Created):**

```json
{
  ".id": "*1",
  "name": "apiuser",
  "group": "net-admin",
  "last-logged-in": null,
  "disabled": false,
    "comment":"User created by API"
}
```

**Example Response (Error - 400 Bad Request):**
```json
{
    "message":"bad password",
    "error":true
}
```

### Example: Creating a User Group via API (HTTP):

**API Endpoint:** `/rest/user/group`

**Request Method:** POST

**Example JSON Payload:**
```json
{
  "name": "api-group",
  "policy": "read,test"
}
```

**Expected Response (Success - 201 Created):**

```json
{
  ".id": "*2",
  "name": "api-group",
  "policy": "read,test"
}
```

### Important Notes

*   The MikroTik API uses JSON format for request bodies and responses.
*   Error handling involves checking HTTP status codes and the JSON payload for error messages.
*   Authentication for the API should be done with a suitable token that has the permissions to create and modify users.

## Security Best Practices

*   **Disable Default User:** As shown, disabling or renaming the default "admin" account is very important.
*   **Strong Passwords:** Enforce strong password policies.
*   **Limit Permissions:** Follow the principle of least privilege when creating users and assigning them to groups. Give users the bare minimum necessary to do their job.
*   **Regular Reviews:** Periodically review user accounts and group memberships to ensure they are up-to-date.
*   **Secure API Access:** If using the API, ensure only authorized clients have access and implement strong token-based authentication.
*   **Logging:** Monitor logs for any unusual login attempts or unauthorized activity.
*   **Use encrypted channels:** If the router is being managed over a remote connection, secure it with VPN.

## Self Critique and Improvements

*   **Centralized Logging:** Integrate with a centralized logging server for better monitoring and security analysis.
*   **More User Groups:** Create more specific user groups for varied roles.
*   **Automatic User Provisioning:** Automate user provisioning with scripts.
*   **Use of AAA:** Implement the use of a AAA infrastructure, with Radius or TACACS+, to integrate the user management with centralized databases.
*   **Two-Factor Authentication:** Implement 2FA for more security.

## Detailed Explanations of Topic

User management on MikroTik RouterOS is crucial for controlling who has access to router configurations and resources. Users are grouped and assigned access policies to determine which actions can be performed. Local user management provides simple and immediate control, while RADIUS allows for integrating users with larger enterprise authentication systems.

User groups are collections of users with similar permissions. Each group has an associated policy specifying which access rights are granted. These policies include things like `read`, `write`, `test`, `password`, `reboot`, etc.

## Detailed Explanation of Trade-offs

*   **Local Users vs RADIUS:** Local users are simpler to manage but don't scale well. RADIUS provides centralized management and is much more scalable but requires additional infrastructure. Local users may be preferred for a smaller network with few users.
*   **Fine-Grained vs. Broad Groups:** Fine-grained groups are more secure, but they can be complex to manage. Broad groups are easier to maintain, but they may grant too much access.
*   **Password vs. Certificate:** Passwords are easy to configure, but they can be compromised. Certificates are more secure, but they require additional configuration and a PKI system.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 7.12, the latest stable release as of October 26, 2023. All commands should work as expected for this version. Also, since RouterOS 6.48 does not use the same policies, it will not work for older versions.

This documentation provides a detailed, actionable guide for user management on MikroTik routers. By following the steps and considerations outlined, you can securely manage access to your router and network resources effectively.
