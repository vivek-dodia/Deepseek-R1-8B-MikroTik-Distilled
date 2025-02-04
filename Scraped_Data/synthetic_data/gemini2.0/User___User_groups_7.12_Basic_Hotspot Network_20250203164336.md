Okay, let's dive into a detailed technical documentation for managing users and user groups on a MikroTik router running RouterOS 7.12 (or 6.48/7.x), within the context of a Hotspot network using the specified subnet and interface.

## Scenario Description:

We are setting up a Hotspot network on a MikroTik router. We want to manage user access by creating different user groups with varying permissions and restrictions. This will enable us to apply specific policies to groups of users, instead of individual users. Our network operates on subnet 13.154.78.0/24, and this hotspot interface is named `vlan-4`.

## Implementation Steps:

1.  **Step 1: Create User Groups**

    *   **Purpose**: Defining groups allows us to manage permissions collectively instead of individually for each user. We'll create two groups: 'premium' for high-priority users and 'basic' for standard users.
    *   **Before Configuration**: No user groups exist yet.
    *   **CLI Command:**
        ```mikrotik
        /user group
        add name=premium
        add name=basic
        ```
    *   **Winbox GUI**: Go to `Users > User Groups`. Click the `+` button to add each group. In the dialog box that opens, enter the name of the group (e.g., 'premium', 'basic'). Click `OK` to save.
    *   **After Configuration**: Two user groups, 'premium' and 'basic', are now present.
    *   **Effect**: We can now assign users to these groups.

2.  **Step 2: Create Users and Assign them to Groups**

    *   **Purpose**: To add users that will be granted access to our Hotspot network and associate them with the previously defined groups. We'll create user 'premiumuser1' in the 'premium' group and 'basicuser1' in the 'basic' group.
    *   **Before Configuration**: No specific users exist.
    *   **CLI Command:**
        ```mikrotik
        /user
        add name=premiumuser1 group=premium password="SecurePassword1!"
        add name=basicuser1 group=basic password="SecurePassword2!"
        ```
        **Winbox GUI**: Go to `Users > Users`. Click the `+` button to add each user. In the dialog box that opens, enter the user's `Name`, `Group`, and `Password`. Click `OK` to save.
    *   **After Configuration**: Two users are present: `premiumuser1` in the 'premium' group and `basicuser1` in the 'basic' group.
    *   **Effect**: Users are now created and assigned to the respective user groups.

3.  **Step 3: Enable Hotspot Authentication**
    * **Purpose**: To enable hotspot authentication with the user database we've created. This means only users with valid credentials (i.e., those created in Step 2) can access the network. We'll assume that a hotspot server is already running on `vlan-4`, and the profile has been created.
    * **Before Configuration**: Hotspot is likely using default authentication method, or some previously configured method.
    * **CLI Command:**
        ```mikrotik
        /ip hotspot user profile
        set [find name=default] login-by=pap
        /ip hotspot
        set [find interface=vlan-4] authentication=login
        ```
        **Winbox GUI**:
            *  Go to `IP > Hotspot > User Profiles`, edit the `default` profile, under the `General` tab, set `Login By` to `PAP`.
            *  Go to `IP > Hotspot > Hotspot Servers`, edit the hotspot for `vlan-4`, under the `General` tab, set `Authentication` to `login`.
    *   **After Configuration**: Hotspot authentication is now tied to the local user database, and we are using PAP for login.
    *   **Effect**: Only authenticated users can now access the network through the `vlan-4` hotspot.

## Complete Configuration Commands:

```mikrotik
# Create user groups
/user group
add name=premium
add name=basic

# Create users and assign to groups
/user
add name=premiumuser1 group=premium password="SecurePassword1!"
add name=basicuser1 group=basic password="SecurePassword2!"

# Set the login method for the default hotspot user profile
/ip hotspot user profile
set [find name=default] login-by=pap

# Enable authentication for the hotspot on vlan-4
/ip hotspot
set [find interface=vlan-4] authentication=login

```

**Parameter Explanations:**

| Command        | Parameter        | Explanation                                                                                                                               |
|----------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `/user group`  | `add name=...`    | Creates a new user group with the specified name (e.g., `premium`, `basic`).                                                               |
| `/user`        | `add name=...`    | Creates a new user with the specified name (e.g., `premiumuser1`, `basicuser1`).                                                         |
| `/user`        | `group=...`        | Assigns the user to the specified user group (e.g., `premium`, `basic`).                                                                  |
| `/user`        | `password=...`    | Sets the user's password. **Use strong passwords**.                                                                                   |
| `/ip hotspot user profile` | `login-by`| Configures the login methods, use `pap` for the most basic form of authentication.                                     |
| `/ip hotspot`| `authentication` | Sets the hotspot authentication method, `login` indicates the use of the local user database.|
| `/ip hotspot` | `interface`| The specific interface that the hotspot server is running on. |

## Common Pitfalls and Solutions:

*   **Problem:** Users cannot log in.
    *   **Solution:**
        *   **Check User Credentials:** Ensure the username and password entered by the user are correct.
        *   **Check User Status:** Make sure the user accounts are not disabled or expired.
        *   **Check Hotspot Profile:** Verify that the user profile is set to `login-by=pap`.
        *   **Check Hotspot Server:** Ensure the hotspot server on `vlan-4` has `authentication=login`.
        *   **Check Logs:** Look for relevant errors in the system logs (`/system logging print`).
*   **Problem:** Incorrect group assignments.
    *   **Solution:** Double-check the group assignment for each user in `/user print`. Modify as needed using `/user set [find name=...] group=...`.
*   **Problem:** Hotspot is not working on `vlan-4`.
    *   **Solution**: Ensure that a Hotspot server is correctly configured on the `vlan-4` interface. Check the `/ip hotspot print` output. Also verify that the network interface is active and correctly configured.

**Security Considerations:**

*   **Strong Passwords:** Use strong and unique passwords for all user accounts.
*   **Regular Password Rotation:** Encourage users to change their passwords regularly.
*   **Disable Default User Accounts:** Remove any default user accounts that you do not use.
*   **Monitor Logs:** Monitor the system logs for any suspicious login attempts.
*   **Secure Winbox/API Access:** Limit access to Winbox and the API by IP address.

**Resource Considerations:**

*   **High User Count:**  For very large networks, consider using a RADIUS server for user authentication to offload the load from the MikroTik router.
*   **High User Activity:** Monitor the MikroTik's CPU and memory usage, especially during peak hours. Optimize scripts and configurations to improve performance, if needed.

## Verification and Testing Steps:

1.  **User Login:**
    *   Connect a device to the `vlan-4` network.
    *   Attempt to access a website. The device should be redirected to the hotspot login page.
    *   Login using the created user `premiumuser1` and password `SecurePassword1!`.
    *   After successful login, access the website.
    *   Repeat with `basicuser1` and password `SecurePassword2!`.
2.  **User Logout:**
    *   If a logout mechanism is configured in the hotspot settings, attempt to logout.
    *   Re-attempting to access the internet should redirect to the login page.
3. **Check Logs:**
    *   Use the command `/log print` to view login and logout events.
4. **Check User Status:**
    *   Use the command `/user print` to view the status of all configured users and their group assignments.

## Related Features and Considerations:

*   **Hotspot User Profiles**: Configure different user profiles with bandwidth limitations, session timeouts, etc. Assign user profiles to each user or group.
*   **RADIUS Server**: For larger deployments, use a RADIUS server to centralize user management and authentication, and provide accounting services.
*   **User Manager**:  For complex user management, consider using the MikroTik User Manager, but note that this is not recommended for large networks.
*   **Bandwidth Management:** Combine with `/queue simple` or `/queue tree` rules to limit bandwidth for different user groups.

## MikroTik REST API Examples (if applicable):

**Note:** RouterOS API is complex and needs some familiarity. These examples will need you to first enable the API, configure the router API user (different from the hotspot users), and use a REST client like `curl` or `Postman`.

**Example 1: Get List of User Groups**

*   **API Endpoint**: `/user/group`
*   **Request Method**: GET
*   **Example `curl` command:**
    ```bash
    curl -k -u <api_username>:<api_password> 'https://<router_ip>/rest/user/group'
    ```
*   **Expected Response:** (Example JSON)
    ```json
    [
        {
            ".id": "*1",
            "name": "premium"
        },
        {
           ".id": "*2",
           "name": "basic"
        }
    ]
    ```

**Example 2: Add a New User Group**

*   **API Endpoint**: `/user/group`
*   **Request Method**: POST
*   **Example JSON Payload:**
    ```json
    {
        "name": "new_group"
    }
    ```
*   **Example `curl` command:**
    ```bash
    curl -k -u <api_username>:<api_password> -H "Content-Type: application/json" -d '{"name":"new_group"}' -X POST 'https://<router_ip>/rest/user/group'
    ```
*   **Expected Response:** (Successful Response, JSON)
    ```json
    { ".id": "*3", "name": "new_group"}
    ```
*  **Error Handling:** (Example, JSON)
    ```json
        { "message": "name already exists"}
    ```

**Example 3: Get List of Users**

*   **API Endpoint**: `/user`
*   **Request Method**: GET
*   **Example `curl` command:**
    ```bash
        curl -k -u <api_username>:<api_password> 'https://<router_ip>/rest/user'
    ```
*   **Expected Response:** (Example JSON)
    ```json
    [
      {
        ".id": "*1",
        "name": "premiumuser1",
        "group": "premium"
        // ...other fields
      },
      {
        ".id": "*2",
        "name": "basicuser1",
        "group": "basic"
      }
      // ...other users
    ]
    ```

**Example 4: Add a New User**

* **API Endpoint**: `/user`
* **Request Method**: POST
* **Example JSON Payload:**
    ```json
        {
            "name": "newuser",
            "group": "basic",
            "password": "SecureNewPassword!"
        }
    ```
* **Example `curl` command:**
    ```bash
    curl -k -u <api_username>:<api_password> -H "Content-Type: application/json" -d '{"name":"newuser", "group":"basic", "password":"SecureNewPassword!"}' -X POST 'https://<router_ip>/rest/user'
    ```
* **Expected Response:** (Successful Response, JSON)
    ```json
      {
        ".id": "*3",
        "name": "newuser",
        "group": "basic"
         // ...other fields
      }
    ```

**Note:** Replace `<api_username>`, `<api_password>`, and `<router_ip>` with the correct values.  Remember to handle errors in the API responses.

## Security Best Practices

*   **API Security**: Disable the API or restrict API access to certain IPs. Use secure API credentials. Use HTTPS for the API connection.
*   **Hotspot Security**: Use HTTPS for the Hotspot login pages. Avoid using the default login page, create a custom one. Ensure that the default user is not the same as the api user.

## Self Critique and Improvements

*   **Improvements:** This example is basic and can be significantly expanded upon, by adding more features.
    *   **Specific Hotspot User Profiles:** Instead of a generic profile, create user profiles for different groups, to handle different bandwidth limitations.
    *   **Radius Server**: for large deployments, this would be a very important addition.
    *   **Custom login Pages:** Create a login page more unique, and more user-friendly.
    *   **API Rate Limiting**: Rate limiting could be added to the REST API to mitigate the effects of brute force attacks on the login.
*   **Trade-offs**: The current solution is simple but lacks advanced features such as bandwidth limiting, session time-outs, etc, for groups. This trade-off is made to keep the complexity low, but these need to be added in real world scenarios.
*  **Further Modifications**: More complex configurations could include the addition of MAC filtering, RADIUS based accounting, and implementing a more complex custom login page for better security and user experience.

## Detailed Explanation of Topic

*   **Users and User Groups**: In MikroTik RouterOS, users and user groups are used to manage access to resources, primarily through the Hotspot. Users are individual accounts with specific credentials, while user groups are logical containers to apply rules collectively to several users at the same time.
*   **Why use Groups**: Using user groups greatly simplifies administration, by enabling the creation of policies that apply to different groups of users at the same time. Groups allow for easier modifications to settings, as opposed to changing settings on individual users. User groups also permit a better organization of users, with different permissions levels.
*   **Hotspot Users**: Hotspot users are authenticated against the router's internal user database, or against an external RADIUS server. Authentication happens before they are granted access to the internet.

## Detailed Explanation of Trade-offs

*   **Local User Database vs. RADIUS**: Using the local user database is simple for small networks, but it doesn't scale well and lacks features like accounting. RADIUS, while complex to setup, is significantly more powerful, provides centralized authentication, accounting and dynamic authorization for large networks.
*   **User Profiles vs. No User Profiles**: User profiles provide a way to impose bandwidth or time limits on users, but adds complexity to the configuration. For networks where different users require different bandwidth limitations and access schedules, User profiles can be crucial. Without user profiles, all users receive the same network access.
*   **PAP vs. CHAP:** PAP (Password Authentication Protocol) is the most basic login method, sending credentials in clear text, thus making it insecure. CHAP (Challenge Handshake Authentication Protocol) is more secure because it does not send the password itself. For Hotspot, always default to `pap` because it is the default, and it can be the easiest to troubleshoot. In a real world environment, you should consider using more secure protocols.
*   **Local Authentication vs Active Directory**: Local authentication is simple to configure, but requires to manually add, modify, and delete users within the Mikrotik router itself. Integrating with active directory is significantly more complex to set up, but allows you to manage user authentication within the same system you manage the users' computer access.

## Configuration for Specific RouterOS Versions:

The provided configuration is compatible with RouterOS 6.48 and 7.x (including 7.12). All the commands are valid across these versions. If any command was to be version specific, I would have included a note indicating such. If a specific feature is supported only on specific versions, that also would have been noted.

This concludes the detailed documentation.  Remember to test this configuration in a test environment first and adjust it as per your specific needs.
