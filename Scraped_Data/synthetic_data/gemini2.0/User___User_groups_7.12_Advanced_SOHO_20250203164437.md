Okay, let's craft some detailed technical documentation for managing users and user groups on a MikroTik RouterOS device, specifically within the context of a SOHO network. We'll target RouterOS 7.12, noting compatibility with 6.48 and other 7.x versions where applicable. We'll use the subnet 118.232.223.0/24 and an interface named 'ether-86' as specified. We'll also focus on advanced concepts.

## Scenario Description:

We are configuring user and user group management on a MikroTik router serving a small office or home network. The goal is to provide differentiated levels of access to the router's administration interface. This involves creating a user with limited privileges, a user with full access, and then assigning these users to their proper groups. This allows for fine-grained control over who can manage the router and what tasks they can perform. We will focus on separating read-only administrative access from full write access.

## Implementation Steps:

Here is a step-by-step guide, along with explanations, before/after examples, and desired effects:

**1. Step 1: Review Existing Users and Groups**

*   **Purpose:** Before making changes, it's crucial to understand the current configuration. This prevents accidental lockouts or conflicts.
*   **CLI Command:**

    ```mikrotik
    /user print
    /user group print
    ```
*   **Before:** Typically, you'll see the default 'admin' user and some pre-configured groups.
    ```text
    /user print
    Flags: X - disabled, I - invalid
    #   NAME      GROUP    
    0   admin     full
    
    /user group print
    Flags: X - disabled
    #   NAME  POLICY                                                                               
    0   full  read,write,test,password,reboot,policy,ftp,web,local,winbox,api,dude,telnet,ssh,snmp 
    1   read  read
    ```
*   **After:** No changes yet, just an observation of the current state.
*   **Winbox GUI:** Use the "Users" and "Groups" options in the left-side menu to view existing users and groups.

**2. Step 2: Create a Read-Only User Group**

*   **Purpose:** We need a group to assign users with read-only permissions.
*   **CLI Command:**
    ```mikrotik
    /user group add name=readonly policy=read
    ```
*   **Before:** The `user group print` output from step 1 will still show only `full` and `read`.
*   **After:**

    ```text
    /user group print
    Flags: X - disabled
    #   NAME  POLICY                                                                               
    0   full  read,write,test,password,reboot,policy,ftp,web,local,winbox,api,dude,telnet,ssh,snmp 
    1   read  read
    2   readonly  read
    ```

*   **Explanation:**
    *   `name=readonly`: Specifies the name of the new group.
    *   `policy=read`:  Sets the access policy of the group to be read-only.

*   **Winbox GUI:** Go to "Users" -> "Groups," click the "+" button, enter "readonly" as the name, select "read" as the policy, then click "Apply" and "OK".

**3. Step 3: Create a Limited Access User**

*   **Purpose:** Creating a user with restricted access.
*   **CLI Command:**
    ```mikrotik
    /user add name=limited_admin password=SecurePassword group=readonly
    ```
*   **Before:** `user print` from step 1 will show only the `admin` user.
*   **After:**
    ```text
    /user print
    Flags: X - disabled, I - invalid
    #   NAME           GROUP   
    0   admin          full
    1   limited_admin  readonly
    ```
*   **Explanation:**
    *   `name=limited_admin`: Sets the username.
    *   `password=SecurePassword`: Sets the user's password. **Replace "SecurePassword" with a strong password.**
    *   `group=readonly`: Assigns this user to the previously created read-only group.
*   **Winbox GUI:** Go to "Users," click the "+" button, enter "limited_admin" as the name, type a password into the "Password" field, select the "readonly" group from the "Group" dropdown, then click "Apply" and "OK".

**4. Step 4: Create a Full Access User**

*   **Purpose:** Creating a secondary full access user (Best practice to not use the default admin account).
*   **CLI Command:**
   ```mikrotik
    /user add name=full_admin password=AnotherSecurePassword group=full
   ```
*  **Before:** Only the user `admin` and the user `limited_admin` exist.
*  **After:**
   ```text
    /user print
    Flags: X - disabled, I - invalid
    #   NAME           GROUP   
    0   admin          full
    1   limited_admin  readonly
    2   full_admin     full
    ```
*  **Explanation:**
     *  `name=full_admin`: Sets the username.
    *   `password=AnotherSecurePassword`: Sets the user's password. **Replace "AnotherSecurePassword" with a strong password.**
    *   `group=full`: Assigns this user to the full access group.

*  **Winbox GUI:** Go to "Users," click the "+" button, enter "full_admin" as the name, type a password into the "Password" field, select the "full" group from the "Group" dropdown, then click "Apply" and "OK".

**5. Step 5: Disable the Default "admin" User (Recommended)**

*   **Purpose:** To improve security, it's best to disable the default "admin" account once you have alternative full access accounts.
*   **CLI Command:**
    ```mikrotik
    /user disable admin
    ```
*   **Before:**  The `admin` user is enabled.
*   **After:**
    ```text
    /user print
    Flags: X - disabled, I - invalid
    #   NAME           GROUP   
    0  X admin          full
    1    limited_admin  readonly
    2    full_admin     full
    ```
*   **Explanation:** The `X` flag now denotes the `admin` user as disabled.
*  **Winbox GUI:** Select the "admin" user in the "Users" list and uncheck the "Enabled" checkbox, then click "Apply" and "OK".

## Complete Configuration Commands:

Here's a complete set of commands to implement the described setup:

```mikrotik
/user group add name=readonly policy=read
/user add name=limited_admin password=SecurePassword group=readonly
/user add name=full_admin password=AnotherSecurePassword group=full
/user disable admin
```

**Explanation of Parameters:**

| Command        | Parameter       | Description                                                                      |
|----------------|-----------------|----------------------------------------------------------------------------------|
| `/user group add` | `name`         | The name of the user group being created.                                        |
| `/user group add` | `policy`      | Specifies the permissions granted to users within this group (e.g., `read`, `write`, etc.) |
| `/user add`      | `name`        | The username for the new user.                                                    |
| `/user add`      | `password`     | The password for the new user.                                                    |
| `/user add`      | `group`         | The user group to which the new user will be assigned.                           |
| `/user disable`    |  User Name | Disable a User account |

## Common Pitfalls and Solutions:

*   **Problem:**  Forgetting the new password.
    *   **Solution:** Use a password manager or create a secure backup of your password credentials.
*   **Problem:** Accidentally locking yourself out.
    *   **Solution:** Access your router via the console port, serial cable or another interface if possible.
    *   **Solution:** If console access isn't possible you will have to factory reset the router.
*   **Problem:** Incorrect policy settings lead to users not having required access.
    *   **Solution:** Double-check the policy settings for the group and that the user is in the correct group.
*   **Problem:** API calls not authorized.
    *   **Solution:** Ensure the user being used for API access has the `api` permission included in the policy of their group.
*   **Problem:** High CPU usage from many user login attempts (brute force).
    *   **Solution:** Implement firewall rules to limit login attempts based on IP or introduce login delays for suspicious login activity.
*   **Problem:**  Overly complex user management creating unintended access overlaps
    * **Solution:** Keep your user groups simple and avoid overlapping policies.  Regular audits of access control can help manage complexities.

## Verification and Testing Steps:

1.  **Login Test:**
    *   Attempt to log into the MikroTik's web interface (Winbox, webfig, etc.) using the `limited_admin` credentials.
    *   Confirm you can only view configuration and not change it.
    *   Attempt to log into the MikroTik's web interface using the `full_admin` credentials.
    *   Confirm that you can view and modify the router's settings.
2.  **API Test:**
    *   Attempt an API call using both the `limited_admin` and the `full_admin` users. Verify the `limited_admin` cannot make modifications and `full_admin` can. (see REST API section for an example)
3.  **CLI Test:**
    *   Open a new CLI terminal (SSH/Telnet or via Winbox terminal) and log in with both users.
    *   Test the `limited_admin` user to see if it allows modifications. It should not.
    *   Test the `full_admin` user to see if it allows modifications. It should.
4.  **User List Verification:**

    ```mikrotik
    /user print
    ```

    *   Check that your output matches the expected output from step 5.

## Related Features and Considerations:

*   **RADIUS Authentication:** For larger environments, consider using RADIUS for centralized user authentication and authorization.
*   **User Profiles:** Define specific user profiles for more fine-grained controls beyond groups, potentially including bandwidth limiting or other QoS features.
*   **Logging:** Enable logging of user logins and changes to track administrative activities.
*   **Hotspot User Management:** If running a hotspot, consider integrating user management with the hotspot's user database.
*   **Password Complexity:** Implement a minimum password complexity policy for better security.
*   **Two-Factor Authentication:** Consider using two-factor authentication for added security if the risk is high.

## MikroTik REST API Examples:

Here are examples of using the REST API with our configured users:

**Example 1: Fetching User List with Full Access User (Successful)**
* **API Endpoint:** `/user`
* **Request Method:** GET
* **Headers:** `Authorization: Basic <base64-encoded 'full_admin:AnotherSecurePassword'>`
    * Generate Base64 using the string username:password (full_admin:AnotherSecurePassword)

* **CLI Equivalent for Authentication String:** `echo -n "full_admin:AnotherSecurePassword" | base64`
    *Example Output:* `ZnVsbF9hZG1pbjpBbm90aGVyU2VjdXJlUGFzc3dvcmQ=`
* **cURL Example:**
    ```bash
   curl -k -X GET "https://<router_ip_address>/rest/user" -H "Authorization: Basic ZnVsbF9hZG1pbjpBbm90aGVyU2VjdXJlUGFzc3dvcmQ="
    ```
* **Expected Response (Example):**
    ```json
    [
        {
            ".id": "*0",
            "name": "admin",
            "group": "full",
            "disabled": true
        },
        {
            ".id": "*1",
            "name": "limited_admin",
            "group": "readonly",
            "disabled": false
        },
        {
            ".id": "*2",
            "name": "full_admin",
            "group": "full",
            "disabled": false
        }
    ]
    ```

**Example 2: Attempting to Change Setting with Limited Access User (Failed)**

* **API Endpoint:** `/system/identity`
* **Request Method:** PUT
*   **Headers:** `Authorization: Basic <base64-encoded 'limited_admin:SecurePassword'>`, `Content-Type: application/json`
    * Generate Base64 using the string username:password (limited_admin:SecurePassword)
*   **CLI Equivalent for Authentication String:** `echo -n "limited_admin:SecurePassword" | base64`
    *Example Output:* `bGltaXRlZF9hZG1pbjpTZWN1cmVQYXNzd29yZA==`
* **JSON Payload:**
  ```json
  {"name": "ChangedName"}
  ```

* **cURL Example:**
    ```bash
    curl -k -X PUT "https://<router_ip_address>/rest/system/identity" -H "Authorization: Basic bGltaXRlZF9hZG1pbjpTZWN1cmVQYXNzd29yZA==" -H "Content-Type: application/json" -d '{"name": "ChangedName"}'
    ```

*   **Expected Response (Example):**
   ```json
   {
        "message": "not allowed",
        "detail": "write access required",
        "type": "error"
    }
    ```

**Error Handling Notes:**
*   The examples above show how to handle a failed API call based on insufficient user rights. Always verify return codes (403 - Forbidden).
*   The "message" and "detail" fields in the response provide specific error information.
*   Be aware that unauthorized attempts may be logged by the MikroTik, further assisting in security audits.

## Security Best Practices

*   **Strong Passwords:** Always use strong, unique passwords for all user accounts.
*   **Disable Default Account:** Disable the default "admin" account as soon as possible.
*   **Principle of Least Privilege:** Grant users only the necessary privileges to perform their job function.
*   **Audit Logs:** Review logs regularly for any suspicious activity.
*   **API Access Control:**  Secure your router's API with strong passwords and consider restricting access based on IP or network segment.
*  **HTTPS:** Enforce HTTPS for all Winbox and web-based connections.

## Self Critique and Improvements

*   **More Granular Policy Control:**  While the read-only/full-access model is a good start, implementing more fine-grained permission controls is a better idea in larger deployments. Using more policy options like `ftp`, `web`, `api`, `ssh` individually for multiple user groups would help.
*   **RADIUS:** The documentation only briefly touches on RADIUS. Expanding on RADIUS integration would be beneficial, as this would greatly improve user management in larger environments.
*   **Password Reset:** Could add information on password recovery or the user lockout mechanism.
*   **Automated User Provisioning:**  Consider automating user provisioning via scripting or external management systems.
*   **Resource Usage Monitoring:** Further elaborate on monitoring CPU and memory when dealing with many simultaneous user logins.

## Detailed Explanations of Topic

User management on MikroTik RouterOS revolves around two core concepts: **Users** and **User Groups**. Users represent individual accounts, while User Groups define sets of permissions. Each user is a member of a group, and that group's assigned policy defines what actions that user can perform on the router.  MikroTik policies provide very granular levels of access control, allowing for precise assignment of privileges. These policies include but are not limited to: `read`, `write`, `test`, `password`, `reboot`, `policy`, `ftp`, `web`, `local`, `winbox`, `api`, `dude`, `telnet`, `ssh`, `snmp`. Each policy can be applied to different groups allowing the system administrator a very fine grain of access control.

## Detailed Explanation of Trade-offs

The main trade-offs in the described configuration are:

*   **Security vs. Convenience:**  Disabling the default 'admin' account improves security but requires careful management of new accounts. If the passwords of the newly created user are compromised, access is compromised.
*   **Granularity vs. Complexity:** More specific policies and user groups increase security but can be harder to manage.
*   **Manual vs. Automated Management:**  Manual creation and management are simple for a few users but become unwieldy at scale. Automated user provisioning requires more setup but simplifies ongoing management.
*   **Local vs. External Authentication:** Local user accounts are simpler for a single router, while RADIUS provides centralized management for a network of routers.
*   **Read-Only vs. Full Access:** While it is extremely practical to have more granular access controls, there is a trade-off between having many user groups and making it harder to understand who has what access.

## Configuration for Specific RouterOS Versions:

The configuration provided is generally compatible with RouterOS versions 6.48, 7.x, and specifically 7.12. However, it is always a good idea to check the MikroTik changelogs for potential command changes or parameter deprecations.  The main areas to be aware of are the syntax of the user and user group commands and the policies available for a user group in a given version of RouterOS.

This should provide comprehensive documentation for your MikroTik user management needs.
