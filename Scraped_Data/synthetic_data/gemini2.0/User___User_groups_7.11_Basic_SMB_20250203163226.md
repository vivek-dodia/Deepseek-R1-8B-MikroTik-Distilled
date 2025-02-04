Okay, let's dive deep into managing users and user groups on MikroTik RouterOS 7.11 (and generally applicable to 6.48 and 7.x). We will focus on a basic implementation suitable for an SMB environment, utilizing a subnet of 56.5.112.0/24 and an interface named `bridge-94`.

## Scenario Description:

This scenario focuses on creating and managing users on a MikroTik router. We aim to establish a basic user management system, including defining user groups and assigning specific permissions. This could be used for managing access to the router via Winbox or SSH, or for specific applications that utilize user authentication. While this example is based on router access, the concepts can be applied to other services like PPPoE or hotspot users.

## Implementation Steps:

Here's a detailed step-by-step guide for configuring users and groups on your MikroTik router.

### 1. Create User Groups

Before creating users, let's define the user groups. We will create two groups: "admin-group" and "read-only-group".

*   **Step 1.1: Create `admin-group`**

    *   **CLI Command:**
        ```mikrotik
        /user group add name=admin-group policy=write,test,password,read,reboot,policy,ftp,winbox,web,local,ssh
        ```

    *   **Explanation:**
        *   `/user group add`:  Adds a new user group.
        *   `name=admin-group`:  Sets the group name to `admin-group`.
        *   `policy=...`: Defines the group's permissions using a comma-separated list:
            *   `write`: Allows write access to configuration.
            *   `test`: Permits test functionality.
            *   `password`: Allows changing user passwords.
            *   `read`: Allows reading configuration.
            *   `reboot`: Allows router reboots.
            *   `policy`: Allows changing policies.
            *   `ftp`: Allows FTP access.
            *   `winbox`: Allows access via Winbox.
            *   `web`: Allows access via Webfig.
            *   `local`: Allows local access.
            *   `ssh`: Allows SSH access.
    *   **Before:** No user groups exist (or only default).
    *   **After:** The user group `admin-group` with full admin permissions is created.

    *   **Winbox GUI:** Navigate to `/Users` -> `Groups`, click `Add New` and fill the fields with the respective information and check the checkboxes you want to allow.

*   **Step 1.2: Create `read-only-group`**

    *   **CLI Command:**
        ```mikrotik
        /user group add name=read-only-group policy=read,local,test,web,winbox
        ```
    *   **Explanation:**
        *   `name=read-only-group`: Sets the group name to `read-only-group`.
        *   `policy=read,local,test,web,winbox`: Allows only read-only access, local access, test functionality, and access via Webfig and Winbox.
    *   **Before:** Only `admin-group` exists.
    *   **After:** The user group `read-only-group` is created with limited permissions.

    *   **Winbox GUI:** Navigate to `/Users` -> `Groups`, click `Add New` and fill the fields with the respective information and check the checkboxes you want to allow.

### 2. Create Users

Now let's create users and assign them to their respective groups.

*   **Step 2.1: Create User `admin-user`**

    *   **CLI Command:**
        ```mikrotik
        /user add name=admin-user group=admin-group password="StrongPassword1!"
        ```
    *   **Explanation:**
        *   `/user add`: Adds a new user.
        *   `name=admin-user`: Sets the username to `admin-user`.
        *   `group=admin-group`: Assigns the user to the `admin-group`.
        *   `password="StrongPassword1!"`: Sets the user password.
    *   **Before:** No custom users exist (or only default).
    *   **After:** The user `admin-user` is created with full admin access.
    *   **Winbox GUI:** Navigate to `/Users`, click `Add New` and fill the fields with the respective information, pick a group, set a password and click `OK`.

*   **Step 2.2: Create User `monitor-user`**

    *   **CLI Command:**
        ```mikrotik
        /user add name=monitor-user group=read-only-group password="ReadOnlyPassword2!"
        ```
    *   **Explanation:**
        *   `name=monitor-user`: Sets the username to `monitor-user`.
        *   `group=read-only-group`: Assigns the user to the `read-only-group`.
        *   `password="ReadOnlyPassword2!"`: Sets the user password.
    *   **Before:** Only `admin-user` exists.
    *   **After:** The user `monitor-user` is created with read-only access.
     *   **Winbox GUI:** Navigate to `/Users`, click `Add New` and fill the fields with the respective information, pick a group, set a password and click `OK`.

### 3. Test User Access

At this point, you can test user access via Winbox or SSH to confirm user permissions are set correctly.

## Complete Configuration Commands:

```mikrotik
/user group add name=admin-group policy=write,test,password,read,reboot,policy,ftp,winbox,web,local,ssh
/user group add name=read-only-group policy=read,local,test,web,winbox
/user add name=admin-user group=admin-group password="StrongPassword1!"
/user add name=monitor-user group=read-only-group password="ReadOnlyPassword2!"
```

## Common Pitfalls and Solutions:

*   **Pitfall:** Forgetting passwords.
    *   **Solution:** Use a password manager or record them securely. If completely lost, you might need to reset the router and start again, depending on your specific setup.
*   **Pitfall:** Assigning incorrect permissions to groups.
    *   **Solution:** Double-check group policies before assigning users. Test the group and user access carefully to ensure permissions are appropriate. Use `read` policy for a test user before giving more permissions.
*   **Pitfall:** Locking yourself out of the router.
    *   **Solution:** Always have at least one administrative user with all permissions enabled, or physical access to your router. The `admin` user, that comes by default, is important and you should disable it only if you understand the implications.
*   **Pitfall:** Weak passwords.
    *   **Solution:** Always use strong, unique passwords for all user accounts, even for read-only access. Avoid using common words or patterns.

## Verification and Testing Steps:

1.  **Winbox Access:**
    *   Try to log in to Winbox with `admin-user`. Verify you can change configurations.
    *   Try to log in to Winbox with `monitor-user`. Verify you cannot make changes.

2.  **SSH Access:**
    *   Try to connect to the router via SSH with `admin-user`. Verify you have write access using commands.
    *   Try to connect to the router via SSH with `monitor-user`. Verify you can only read values using `print` commands.
3.  **Webfig Access:**
   *  Try to access the router via Webfig with `admin-user`. Verify you can change configurations.
   *  Try to access the router via Webfig with `monitor-user`. Verify you cannot make changes.

## Related Features and Considerations:

*   **RADIUS Authentication:** For larger setups, consider using RADIUS for centralized user management.
*   **User Specific Policies:** You can assign individual policies to users, overriding the default group policies.
*   **Time Based User Enablement:** You can schedule users to be active only at specific times.
*   **Logging:** Ensure you have logging configured to track user activity.
*   **API Access:** Users with appropriate permissions can access the MikroTik API.
*   **Multi-factor Authentication:** Consider using multi-factor authentication for enhanced security.
*   **Change Tracking:** If you enable change tracking, MikroTik will log which user modified the router's configuration, and which configuration parameters they changed.

## MikroTik REST API Examples:

Below are API calls using MikroTik specific calls. For the sake of simplicity and clarity, I will use curl.

### 1. Creating a User via API:

*   **API Endpoint:** `/rest/user`
*   **Method:** `POST`
*   **JSON Payload:**

    ```json
    {
        "name": "api-user",
        "group": "admin-group",
        "password": "ApiPassword!"
    }
    ```
*   **curl command:**

    ```bash
    curl -k -u "admin:youradminpassword" -H "Content-Type: application/json" \
    -d '{"name":"api-user","group":"admin-group","password":"ApiPassword!"}' \
    "https://192.168.88.1/rest/user"
    ```
*   **Explanation:**
    *   `-k`: Allows insecure connections (use SSL certificates in production).
    *   `-u "admin:youradminpassword"`: Provides authentication using the admin user (you can use a specific API user).
    *   `-H "Content-Type: application/json"`: Sets the content type of the request.
    *   `-d '{"name":"api-user","group":"admin-group","password":"ApiPassword!"}'`: JSON payload for the new user parameters.
    *   `"https://192.168.88.1/rest/user"`: Target endpoint for the user creation.
*   **Expected Response (Success):**

    ```json
    {
        "id": "*10",
        "name": "api-user",
        "group": "admin-group"
    }
    ```

    The `"id"` will vary.

*   **Handling Errors (Example):**
    *  If the response is `HTTP/1.1 400 Bad Request` with:
    ```json
    { "message": "already have user with such name",
    "error": true,
     "details": {
     "name": "already have user with such name"
    }
    }
    ```
     The API returns an error, and the user was not added.

### 2. Getting Users via API:

*   **API Endpoint:** `/rest/user`
*   **Method:** `GET`

*   **curl command:**
    ```bash
    curl -k -u "admin:youradminpassword" "https://192.168.88.1/rest/user"
    ```

*   **Explanation:**
    *   No payload is required for `GET` requests.
    *   The output is an array of JSON documents.

*   **Expected Response (Success):**

    ```json
    [
        {
            "id": "*0",
            "name": "admin",
            "group": "full",
            "disabled": false,
            "last-logged-in": null
        },
        {
           "id": "*10",
            "name": "api-user",
            "group": "admin-group",
            "disabled": false,
            "last-logged-in": null
        },
        {
           "id": "*11",
            "name": "admin-user",
            "group": "admin-group",
            "disabled": false,
            "last-logged-in": null
        },
        {
            "id": "*12",
            "name": "monitor-user",
            "group": "read-only-group",
            "disabled": false,
            "last-logged-in": null
        }
    ]
    ```

*   **Error Handling:**
    *   HTTP `401 Unauthorized` indicates incorrect authentication credentials.
    *   HTTP `404 Not Found` indicates the API endpoint is incorrect.

### 3. Update a User's Password via API:

*   **API Endpoint:** `/rest/user/{id}` (replace `{id}` with actual user id, e.g., `*11`)
*   **Method:** `PUT`
*   **JSON Payload:**
    ```json
    {
        "password": "NewPassword!"
    }
    ```

*   **curl command:**

    ```bash
    curl -k -u "admin:youradminpassword" -H "Content-Type: application/json" \
    -d '{"password":"NewPassword!"}' \
    "https://192.168.88.1/rest/user/*11"
    ```

*   **Explanation:**
    *   `PUT` method is used to update existing resources.

*   **Expected Response (Success):**
    *  No response is returned if it is a successful update.

*   **Error Handling:**
    *   HTTP `404 Not Found` if the specified user ID does not exist.
    *   HTTP `400 Bad Request` indicates invalid data (e.g., a blank password).

## Security Best Practices:

*   **Password Complexity:** Enforce strong passwords using character sets, length, and uniqueness policies.
*   **Principle of Least Privilege:** Assign only necessary permissions to each user and user group.
*   **Regular Audits:** Review user accounts and their permissions periodically, removing unnecessary accounts.
*   **Disable Default Accounts:** Disable the default `admin` user and create new accounts with different usernames, only if you really know what you are doing.
*   **API Security:** Use HTTPS with valid certificates for all API access. Consider API rate limiting and access control.
*   **Secure Protocols:** Use SSH or HTTPS for router management instead of Telnet or HTTP.
*   **Multi-Factor Authentication:** Where feasible, add MFA for critical accounts.

## Self Critique and Improvements:

This basic configuration provides a solid foundation for user management. However, here are areas for improvement:

*   **Granular Policies:**  For more complex setups, consider creating groups with more granular access controls.
*   **External Authentication:** Integrating with RADIUS or Active Directory for centralized user management is a scalable solution.
*   **Audit Logs:** Implement more robust logging of user activity.
*   **API Rate Limiting:** When exposing the API, implement rate limiting to prevent abuse.
*   **User Change Tracking:** Enable user change tracking, to keep a log of which user changed which parameter.

## Detailed Explanations of Topic:

### MikroTik User Management:

MikroTik RouterOS provides a comprehensive user management system that allows you to control who can access and modify your router's configuration. This system revolves around:

*   **Users:** Individual accounts used for accessing the router and/or using specific services.
*   **Groups:** Collections of users that can be assigned a set of common permissions and policies.
*   **Policies:** A set of actions or operations a user is allowed to perform within the router, such as `read`, `write`, `ssh`, `winbox`, and many others.

These elements work together to give administrators a robust means of delegating control and ensuring security.

## Detailed Explanation of Trade-offs:

When designing your user management strategy, you'll encounter various trade-offs:

*   **Single vs Multiple User Accounts:** Using only one administrative account simplifies access but introduces a single point of failure and doesn't allow individual activity tracking. Using individual accounts increases security but requires managing more credentials.
*   **Granular vs Broad Permissions:** Granular permissions provide higher security but are more complex to set up and maintain. Broader permission sets are simpler, but may grant unnecessary access.
*   **Local vs Centralized Authentication:** Local authentication is simpler for small networks but does not scale. Centralized authentication via RADIUS or LDAP is more complex but scalable.
*   **API Access:** API access enables automation and external management but poses a security risk if not properly secured.

Choosing the right approach depends on your specific requirements, network size, security needs, and administrative capabilities.

## Configuration for Specific RouterOS Versions:

The configurations provided above are compatible with RouterOS versions 7.x and 6.48. If using older RouterOS versions, specific commands and parameters might be slightly different. Consult the specific version's manual if necessary. In most cases, upgrading to at least RouterOS 6.48, or 7.x, is recommended for the most up-to-date security features and patches.
