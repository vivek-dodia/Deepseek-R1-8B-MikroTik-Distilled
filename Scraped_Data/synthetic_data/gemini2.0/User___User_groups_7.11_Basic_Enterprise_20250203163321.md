Okay, let's dive into creating detailed documentation for managing users and user groups on a MikroTik RouterOS 7.11 device, specifically focusing on the `wlan-33` interface and the `133.31.173.0/24` subnet. This scenario will be geared towards an enterprise network, but will be kept to a basic configuration to get you started.

## Scenario Description:

We aim to implement basic user authentication and group management for users connecting to the `wlan-33` interface, which will operate on the `133.31.173.0/24` subnet. This will enable us to apply different access policies or resource limitations based on user group membership.  We'll begin with a simple example of how to add users and groups, for this example. We will only use `local` users.  We'll add two users, one in the "admin" group and the other in the "guest" group, but the functionality will be the same on any router that uses RouterOS.

## Implementation Steps:

### Step 1: Adding User Groups

*   **Why?** User groups allow us to manage permissions and resources collectively, rather than individually for each user. This greatly simplifies administration, especially in larger networks.
*   **Before:** No user groups exist by default.
*   **Action (CLI):** We will create two user groups, `admin` and `guest`

    ```mikrotik
    /user group
    add name=admin
    add name=guest
    ```
*   **Action (Winbox GUI):**
    1.  Navigate to `System` > `Users`
    2.  Click the `Groups` tab.
    3.  Click the `Add New` ( + ) button.
    4.  Enter `admin` as the `Name`
    5.  Click `Apply`, then Click `OK`
    6.  Click the `Add New` ( + ) button.
    7.  Enter `guest` as the `Name`
    8.  Click `Apply`, then Click `OK`
*   **After:** The system now contains two user groups: `admin` and `guest`.
* **Expected Output**
    ```mikrotik
    [admin@MikroTik] > /user group print
    Flags  Name
       0   admin
       1   guest
    ```

### Step 2: Adding Local Users and Assigning Groups

*   **Why?**  We need to define the users who will be connecting to the network. We will assign these users to specific groups created in Step 1.
*   **Before:** No custom users have been added.
*   **Action (CLI):** We will add two users: `johndoe` (member of `admin` group) and `janedoe` (member of `guest` group).

    ```mikrotik
    /user
    add name=johndoe password=SecretPassword group=admin
    add name=janedoe password=GuestPassword group=guest
    ```
*   **Action (Winbox GUI):**
    1.  Navigate to `System` > `Users`
    2.  Click the `Users` tab.
    3.  Click the `Add New` ( + ) button.
    4.  Enter `johndoe` as the `Name`.
    5.  Enter `SecretPassword` in the `Password` Field.
    6.  Select `admin` from the `Group` dropdown.
    7.  Click `Apply`, then Click `OK`
    8.  Click the `Add New` ( + ) button.
    9.  Enter `janedoe` as the `Name`.
    10. Enter `GuestPassword` in the `Password` Field.
    11. Select `guest` from the `Group` dropdown.
    12. Click `Apply`, then Click `OK`
*   **After:** Two users have been added, each belonging to a different user group.
*   **Expected Output**
    ```mikrotik
    [admin@MikroTik] > /user print
    Flags  Name      Group    Disabled
    0   admin     admin    no
    1   johndoe   admin    no
    2   janedoe   guest    no
    ```

### Step 3: (Optional) Verifying User Settings

*   **Why?** To confirm that users and groups have been configured correctly.
*   **Action (CLI):** Print user information including group association.

    ```mikrotik
    /user print
    ```
*   **Action (Winbox GUI):**
    1. Navigate to `System` > `Users`
    2. Verify that all groups and users are present and assigned correctly.
*   **After:**  Visual confirmation in the CLI or GUI of the users and their groups.

## Complete Configuration Commands:

```mikrotik
# Add user groups
/user group
add name=admin
add name=guest

# Add users and assign them to groups
/user
add name=johndoe password=SecretPassword group=admin
add name=janedoe password=GuestPassword group=guest

# Verify Users and groups
/user print
/user group print
```

**Parameter Explanation:**

| Command       | Parameter   | Value/Type        | Description                                                     |
|---------------|-------------|-------------------|-----------------------------------------------------------------|
| `/user group add` | name        | string            | The name of the user group.                                     |
| `/user add`    | name        | string            | The username.                                                   |
| `/user add`    | password    | string            | The password for the user.                                      |
| `/user add`    | group       | string (group name)  | The user group to which the user belongs.                     |
| `/user print`| -        |  -          | Print user info                                                    |
| `/user group print`| -        |  -          | Print user group info                                                  |

## Common Pitfalls and Solutions:

*   **Problem:** Forgetting user passwords or having a password policy that is too complex to remember can be a challenge.
    *   **Solution:** Store passwords in a password manager. If users need to reset their passwords, follow these instructions:
        *   **Solution:** CLI: The admin user can reset user passwords with the `/user set <user name> password=<new_password>` command.
        *  **Solution:** Winbox: Go to the `System` > `Users` screen, select the user, and update the `password` field.
*   **Problem:** Assigning users to the incorrect group.
    *   **Solution:** Use the `/user set <user name> group=<new_group_name>` command to reassign a user to a different group. Or, in Winbox, select the user in `System` > `Users` and update the `Group` field.
*   **Problem:** Using weak passwords.
    *   **Solution:** Always use strong, unique passwords, and enable password policies if you are using other authentication mechanisms beyond local.
*   **Problem**: Users are unable to log in, even with the correct credentials.
    *   **Solution**: Ensure that the correct authentication mechanism is configured, such as `local` or other external authentication servers. Double check username and password and verify they do not have leading or trailing spaces.
*   **Problem**: Resource exhaustion on the router when using a large number of users
    *   **Solution**: Monitor the router's CPU, memory and disk usage and verify they are not running low.

## Verification and Testing Steps:

1.  **Check User Listing:**  Use `/user print` to verify the existence of the created users and their assigned groups.
2.  **Check Group Listing:** Use `/user group print` to confirm the user groups.
3.  **Use Test Authentication (If Applicable):**  If authentication is used, try to log in with test user credentials to verify authentication on `wlan-33`. This will vary based on the authentication method you have set up.
4.  **Monitor Logs:** Review the RouterOS logs in the `System` > `Logs` menu for any authentication-related messages (successful logins, failures, etc.).
5. **Verify user settings**: Review `/user print detail` and `/user group print detail` in the CLI and confirm all parameters are as configured.

## Related Features and Considerations:

*   **User Profiles:** Combine user groups with user profiles to limit bandwidth, data usage, or access to specific resources per user group.
*   **Hotspot:** Integrate user groups with the MikroTik Hotspot feature to manage guest access or paid internet access with customized terms of service.
*   **Radius Authentication:** Use a Radius server to authenticate users instead of local users for more centralized user management.
*   **User Manager:** (Older RouterOS) The User Manager package provides more advanced user management features, but this is older functionality. Radius or locally managed users are generally preferred.

## MikroTik REST API Examples (if applicable):

While the MikroTik API doesn't directly have explicit endpoints for local user management in the same way as CLI commands, you can use it to interact with the `/user` and `/user/group` hierarchies. Here's an example for creating a user using the API:

**Example: Add a New User via API**

*   **API Endpoint:** `/user`
*   **Request Method:** POST
*   **Example JSON Payload:**
    ```json
    {
      "name": "apiuser",
      "password": "ApiPassword123",
      "group": "guest"
    }
    ```
*   **Example CLI call**
    ```bash
     curl -k -u admin:yourpassword -X POST -H "Content-Type: application/json" -d '{"name": "apiuser", "password": "ApiPassword123", "group": "guest" }' https://your-router-ip/rest/user
    ```
*   **Expected Response (Success - Status Code 200):**
    ```json
    {
        ".id": "*0",
        "name": "apiuser",
        "group": "guest",
    }
    ```

*   **Error Handling:** If the request fails (e.g., invalid parameter), a response with a non-200 status code and an error message is provided.

    *   **Example Error JSON:**
        ```json
        {
          "message": "invalid value of group",
           "status": "failure",
           "error": "invalid parameter"
        }
        ```
        *   **Action:** Inspect the error details and correct the request data.

**Example: List Users via API**

*   **API Endpoint:** `/user`
*   **Request Method:** GET
*   **Example CLI call**
    ```bash
    curl -k -u admin:yourpassword https://your-router-ip/rest/user
    ```
*   **Expected Response (Success - Status Code 200):**
    ```json
    [
      {
        ".id": "*0",
        "name": "admin",
        "group": "admin",
        "disabled": false
      },
      {
        ".id": "*1",
        "name": "johndoe",
        "group": "admin",
        "disabled": false
      },
       {
        ".id": "*2",
        "name": "janedoe",
        "group": "guest",
        "disabled": false
      },
      {
       ".id":"*3",
        "name":"apiuser",
        "group": "guest",
        "disabled":false
      }
    ]
    ```

**Note:** Ensure the RouterOS API is enabled in `IP` > `API`. The MikroTik API uses HTTPS by default so verify certificate settings.

## Security Best Practices:

*   **Strong Passwords:** Enforce strong password policies for all user accounts.
*   **Least Privilege:** Assign users to groups that grant them the minimum necessary access.
*   **Disable Default Admin Account:** Create a new administrator account, and disable or rename the default "admin" account.
*   **Regular Monitoring:** Monitor logs for suspicious activities.
*   **API Security:** Limit access to the RouterOS API using IP address filtering (if you intend to use the API).
*   **HTTPS:** Ensure you use HTTPS for all MikroTik API calls.

## Self Critique and Improvements:

This configuration provides a basic framework for managing users and groups. Here are some improvements:

*   **User Profiles:** We should configure User Profiles to apply specific resource limits to different user groups, such as bandwidth limitations for the guest users.
*   **RADIUS:**  Implement RADIUS authentication for a more scalable solution, centralizing authentication to a radius server.
*   **Dynamic User Groups:** For a more complex use case, consider user groups that are dynamically applied based on login criteria (e.g., MAC address, VLAN).
*   **Password Complexity Policy:** Implement a more stringent password policy for added security.

## Detailed Explanations of Topic:

*   **Users:** Users are the individuals or entities that require access to the network. Each user is identified by a username and has a password (or other authentication method).
*   **User Groups:** User groups are collections of users that share common access requirements or resource limitations. This simplifies the administration of permissions for large groups of users. User groups on their own provide no functionality beyond being a means to group users.

## Detailed Explanation of Trade-offs:

*   **Local vs. Radius Authentication:** Local authentication is easier to configure for small networks but is less scalable. RADIUS authentication provides more centralized and scalable user management.
*   **Granular vs. Group Permissions:** Granular permissions provide fine-grained access controls, but can be more difficult to administer. Group permissions simplify administration, but may not always be suitable for users that need different permissions.
*   **Password Complexity vs. User Experience:** Stronger password policies add security, but may also make it more difficult for users to remember passwords.  A balance must be found that balances security and usability.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS versions 6.48, 7.x and 7.11, and will work with many older RouterOS versions. The commands are standard and compatible across these versions.

This document provides an actionable configuration guide for implementing user and user groups on a MikroTik router. Be sure to adapt these instructions based on your specific network requirements, and test thoroughly before deploying in a production environment.
