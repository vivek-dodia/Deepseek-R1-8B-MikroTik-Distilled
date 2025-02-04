Okay, let's craft detailed documentation for managing users and user groups on a MikroTik RouterOS device, specifically targeting RouterOS 7.12 (and acknowledging 6.48/7.x compatibility), for a SOHO environment, using the provided subnet (158.6.16.0/24) and interface (wlan-90).

## Scenario Description:

This scenario focuses on creating a basic user management setup for a SOHO network. We will create user groups to define permissions and then create users within those groups, allowing for granular access control on the router. This is particularly useful when managing access for different users or limiting administration to certain functions. We'll focus on read-only and full-access user groups for demonstration purposes.

## Implementation Steps:

### Step 1: Verify Initial Router Configuration
**Before:** We need to assume a basic functioning RouterOS installation. We check if a basic wireless interface is available to be configured, even if it has no IP assigned:
```
/interface wireless print
```
**Example output:**
```
Flags: X - disabled, R - running
 #    NAME                 MTU MAC-ADDRESS       ARP        SSID                MODE        BAND            CHANNEL-WIDTH
 0  R wlan1                1500 00:00:00:00:00:00 enabled    MikroTik            ap-bridge   2ghz-b/g/n      20mhz  
```
**Why it's needed:** This ensures we understand what interface (wlan1) we need to configure.
We also check if any users or user groups exists already. If a RouterOS device is reset with no configuration, there will be a single user `admin` with full access.
```
/user print
/user group print
```

**Example output before any user creation:**
```
[admin@MikroTik] > /user print
Flags: * - disabled
 #   NAME    GROUP      LAST-LOGIN           
 0   admin   full
[admin@MikroTik] > /user group print
 #   NAME     POLICY                       
 0   full     write,password,test
```
**Why it's needed:** This is done to clear the ground and start from the bare minimum of an out-of-the-box configuration.

### Step 2: Create a "Read-Only" User Group
**Before:** The user group list is as in Step 1.
**CLI Command:**
```
/user group add name=read-only policy=read
```
**Why it's needed:** We're creating a new group with minimal privileges.
**After:**
```
/user group print
```
**Example output after command:**
```
 #   NAME        POLICY                       
 0   full        write,password,test           
 1   read-only   read
```
**Effect:** This creates a user group named "read-only" which, as the name implies, will only be able to read the router's configuration, not make changes.

### Step 3: Create a "Full-Access-User" User Group
**Before:** The user group list is as in Step 2.
**CLI Command:**
```
/user group add name=full-access-user policy=write,password,test
```
**Why it's needed:** We're creating another new group with full administrative privileges, for more specialized user accounts. This is usually not recommended to be shared.
**After:**
```
/user group print
```
**Example output after command:**
```
 #   NAME               POLICY                       
 0   full               write,password,test           
 1   read-only          read                         
 2   full-access-user   write,password,test           
```
**Effect:** This creates a user group named "full-access-user" which can make changes to the router's configuration. It's best to restrict the use of full access to only a few known individuals.

### Step 4: Create a "read-only" user.
**Before:** The user list is as in Step 1
**CLI Command:**
```
/user add name=guest group=read-only password=guest123
```
**Why it's needed:** This creates a new user with limited access to the router.
**After:**
```
/user print
```
**Example output after command:**
```
Flags: * - disabled
 #   NAME    GROUP        LAST-LOGIN           
 0   admin   full                              
 1   guest   read-only
```
**Effect:** This creates a user called "guest", with the password "guest123", associated with the "read-only" user group. This user will only have the ability to read router configurations, and not make changes.

### Step 5: Create a "full-access-user" User
**Before:** The user list is as in Step 4
**CLI Command:**
```
/user add name=john group=full-access-user password=securePassword123
```
**Why it's needed:** This creates a new administrative user.
**After:**
```
/user print
```
**Example output after command:**
```
Flags: * - disabled
 #   NAME    GROUP              LAST-LOGIN           
 0   admin   full                              
 1   guest   read-only                              
 2   john    full-access-user
```
**Effect:** This creates a user called "john", with the password "securePassword123", associated with the "full-access-user" user group. This user will have full access to the router configuration.

## Complete Configuration Commands:

```
/user group add name=read-only policy=read
/user group add name=full-access-user policy=write,password,test
/user add name=guest group=read-only password=guest123
/user add name=john group=full-access-user password=securePassword123
```

| Command                      | Parameter    | Explanation                                                                                                                                                                 |
|------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/user group add`          | `name`       | Sets the name of the new user group.                                                                                                                                          |
|                              | `policy`     | Defines the permissions for users within this group (e.g., `read`, `write`, `password`, `test`).                                                                                                     |
| `/user add`                  | `name`       | Sets the username for the new user.                                                                                                                                     |
|                              | `group`      | Assigns this user to a specific user group, determining its permissions.                                                                                                      |
|                              | `password`   | Sets the password for the user. **Important**: Use strong passwords.                                                                                                                                |

## Common Pitfalls and Solutions:

*   **Mistyped User Group or User Names:**  Double-check the spelling of group names and user names during creation. Use `/user group print` and `/user print` to see existing user and group names.
*   **Weak Passwords:** Never use default or obvious passwords. Always choose strong, unique passwords, especially for administrative accounts. Consider using password managers.
*   **Conflicting Policies:**  If a user belongs to multiple groups, permissions are additive. Be careful not to grant more permissions than intended through complex group assignments.
*   **Forgetting Usernames and Passwords:** Keep a secure record of usernames and passwords used, especially for administrative access.
*   **Lockout:** Repeated failed login attempts may lead to temporary IP address blocking by the RouterOS. Ensure that your login procedure is correct. If locked out, you may need to access the router via MAC address or through console.
*   **API Issues:** Incorrect formatting when using the MikroTik REST API can result in errors. Debug using `/tool fetch url="..."` from the MikroTik to test your configuration.

## Verification and Testing Steps:

1.  **Login as `guest`:**  Try to log in to the router via Winbox or SSH using the `guest` username and `guest123` password.
    *   **Expected Result:** You should be able to log in, but will be limited to read-only configuration. You will not be able to add, remove or change any configuration.
2.  **Login as `john`:** Try to log in via Winbox or SSH using `john` as the username and `securePassword123` password.
    *   **Expected Result:** You should be able to log in and have full administrative access.
3.  **Login with a non-existent User:** Try logging in with a username that does not exist in your router configuration
    *   **Expected Result:** Access is denied. RouterOS will not leak if a user exists or not.
4. **Test API access:**  Attempt a REST API call with a `read-only` account to make a change.
    * **Expected Result:** The change request will fail with a permission error.

## Related Features and Considerations:

*   **User Logging:** RouterOS logs user login attempts. Enable logging if you need to track user activity or troubleshoot issues using `/system logging add action=memory topics=user,debug`.
*   **Remote API Access:** If you expose the MikroTik REST API, secure it with strong authentication and potentially restrict access based on the source IP address using `/ip firewall filter` rules.
*   **SSH Key Authentication:** Consider using SSH key-based authentication for enhanced security over password-based authentication.
*   **RADIUS Authentication:** For larger environments, centralize user management using a RADIUS server for authentication and authorization.
*   **Change Logging:** If you enable it, RouterOS also logs configuration changes made by users. Enable it via `/system logging add action=memory topics=configuration,debug`

## MikroTik REST API Examples:

**Example 1: Create a read-only user via API**
```
# API endpoint: /user
# Method: POST
# JSON Payload:
{
    "name": "api-guest",
    "group": "read-only",
    "password": "api-guest-password"
}
#Expected Response:
#Success: status 201 Created
#Failure: status 400 Bad Request (Check the error details) or 401 Unauthorized if not authenticaed correctly
```
**Example with CURL**
```
curl -k -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <your_api_token>" -d '{ "name": "api-guest", "group": "read-only", "password": "api-guest-password" }' https://<router_ip>/rest/user
```

**Example 2: Attempt to change configuration using a "read-only" user via API**

```
# API endpoint: /interface/wireless
# Method: PATCH
# JSON Payload:
{
    "0": {
	    "disabled": "yes"
	}
}
#Expected Response:
#Failure: Status 403 Forbidden (Permission denied)
```
**Example with CURL**
```
curl -k -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <read-only_api_token>" -d '{"0": {"disabled": "yes"}}' https://<router_ip>/rest/interface/wireless
```

| Parameter   | Explanation                                                                 |
|-------------|-----------------------------------------------------------------------------|
| `name`    | The username of the user being created or modified.                       |
| `group`    | The user group to which the user belongs.                                    |
| `password` | The password of the user (for create and change password operations) |

**Note:** The API token needs to be generated on the router via `/user api print` and use the `token=` parameter, it will not work with username/password authentication.

## Security Best Practices

*   **Strong Passwords:** Employ long, complex passwords and avoid using common words or personal information. Use a password manager.
*   **API Authentication:** If using the REST API, always employ a generated token, and do not pass the username and password in the URL.
*   **Principle of Least Privilege:** Grant only the necessary permissions to each user. Avoid unnecessary use of administrative accounts.
*   **Regular Auditing:** Review user accounts and groups periodically. Remove inactive accounts and unnecessary user permissions.
*   **Lockout Mechanisms:** Be aware of RouterOS lockout mechanisms, such as automatic IP blocking for repeated failed login attempts. Consider locking out local addresses for remote attempts with repeated failed logins.
*   **Limit Admin Access:** Restrict access to the router only to trusted and known personnel. Restrict access to the administrative interface by specific IP addresses using `/ip service`.

## Self Critique and Improvements:

This configuration provides a basic yet practical user management framework. Here are some areas for improvement:

*   **Granular Policies:** We can create more fine-grained policies than just "read" or "write". For example, a policy that allows changing the wireless interface but not the firewall.
*   **SSH Key Authentication:** Implementing SSH keys instead of passwords for administrative users will greatly improve security.
*   **RADIUS Integration:** For larger SOHO networks, integrating with a RADIUS server would provide centralized user management and potentially support multiple user authentication methods.
*   **API Rate Limiting:**  Implement API rate limiting to mitigate brute-force attacks.
*   **Password Complexity:** Implement password complexity rules to ensure that users choose a strong password.

## Detailed Explanations of Topic

**User Management** in MikroTik RouterOS allows administrators to control access to the router's configuration. By creating users and assigning them to user groups, you can provide granular control over who can perform what tasks on the device.

**User Groups** define permissions sets. They simplify the process of managing multiple users who have the same or similar permissions. User groups have policies such as `read`, `write`, `password`, `test` that grant specific access rights. Users are then associated with these groups, inheriting the permissions.

**Policies** are predefined sets of access rights. For example, `read` allows a user to see the configuration, `write` allows a user to change the configuration, `password` allows a user to change the password, `test` allows a user to run the test tool. There are more policies, check the official documentation for more information. These are not directly customizable, but can be combined.

## Detailed Explanation of Trade-offs

*   **Read-only vs. Full Access:**
    *   **Read-only:** Enhances security by limiting users to view the configuration. It's good for monitoring, auditing, or troubleshooting without accidentally changing something. Trade-off: Users cannot make necessary configuration changes, and need to relay any needed change to a user with the necessary permissions
    *   **Full Access:** Provides complete control over the device. Trade-off: Higher security risk if given to untrusted users. Best limited to experienced administrators.

*   **Granular Policies vs. Basic Policies:**
    *   **Granular:** Allows precise control over access rights. Trade-off: More complex to configure and maintain. Use for complex and high-security networks
    *   **Basic:** Easier to manage, but less control over specific functions. Trade-off: Less secure than very granular access rights. Used for smaller and less demanding deployments.

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Simpler to set up for small networks, all users are managed locally on the router. Trade-off: Can be difficult to manage and scale as number of users grow, with higher configuration overhead.
    *   **RADIUS:** Centralizes user management. Trade-off: Requires setting up an external RADIUS server. More complex to implement, but recommended for larger networks with a great number of users.

## Configuration for Specific RouterOS Versions:

The commands and configurations shown above are compatible with RouterOS 6.48 and RouterOS 7.x versions, including our target version of 7.12. The user and user group structure and commands remain largely consistent across these versions. If you're using a much older version of RouterOS, be aware of potential slight syntax variations.
If you are running RouterOS before version 7, the command `user api` to generate the API tokens does not exist.

This comprehensive documentation provides a solid foundation for user and user group management on MikroTik RouterOS. It includes detailed steps, practical examples, and security considerations to ensure a robust and secure network setup. Remember to tailor the configurations to your specific environment and security needs.
