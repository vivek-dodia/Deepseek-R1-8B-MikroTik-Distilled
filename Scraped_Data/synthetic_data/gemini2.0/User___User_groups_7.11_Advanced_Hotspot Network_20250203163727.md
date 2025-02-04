Okay, let's craft a comprehensive guide to managing users and user groups in a MikroTik Hotspot environment, focusing on RouterOS 7.11 (and compatible with 6.48+). We will use the provided subnet `238.112.16.0/24` and interface `bridge-54`. We'll assume the hotspot setup itself is already in place.

## Scenario Description:

This document outlines how to create and manage users and user groups within a MikroTik hotspot environment. Specifically, we will:

1.  Create user groups with specific profiles, such as bandwidth limits and time quotas.
2.  Create users and assign them to these groups, allowing for differentiated access.
3.  Demonstrate how to monitor and manage users and groups.

This configuration is geared towards advanced users looking to implement fine-grained control over hotspot access, which is common in SOHO, SMB, and Hotspot Network environments.

## Implementation Steps:

Here's a step-by-step guide using both the CLI and Winbox GUI, demonstrating the configuration process.

### Step 1: Create a User Group

*   **Why:** User groups allow us to apply common settings to multiple users at once, simplifying administration.
*   **How:** We'll create a group named "premium-users" with specific bandwidth limits.

**Before:**
```
/user group print
Flags: * - default
 #   NAME                             
```

**CLI Configuration:**

```
/user group add name=premium-users comment="Users with premium access"
/user group set premium-users rate-limit=10M/10M
```

**Winbox GUI:**
1. Navigate to `Users > User Groups`.
2. Click the `+` button.
3. In the window that opens, enter `premium-users` in the `Name` field.
4. Go to the `Limit` Tab.
5. Enter `10M/10M` in the `Rate Limit` Field.
6. Add a Comment: `Users with premium access`.
7. Click `Apply` and `OK`.

**After:**
```
/user group print
Flags: * - default
 #   NAME              RATE-LIMIT COMMENT
 0   premium-users     10M/10M    Users with premium access
```

*   **Explanation:**
    *   `name=premium-users`: Specifies the name of the new user group.
    *  `comment="Users with premium access"`: Adds a comment for better understanding.
    *  `rate-limit=10M/10M`: Sets the download and upload rate limit to 10Mbps for users in this group.

### Step 2: Create Another User Group

*   **Why:** To create a user group with less access.
*   **How:**  We'll create a group named "basic-users" with specific bandwidth limits.

**Before:**
```
/user group print
Flags: * - default
 #   NAME              RATE-LIMIT COMMENT
 0   premium-users     10M/10M    Users with premium access
```
**CLI Configuration:**

```
/user group add name=basic-users comment="Users with basic access"
/user group set basic-users rate-limit=2M/2M
```
**Winbox GUI:**
1. Navigate to `Users > User Groups`.
2. Click the `+` button.
3. In the window that opens, enter `basic-users` in the `Name` field.
4. Go to the `Limit` Tab.
5. Enter `2M/2M` in the `Rate Limit` Field.
6. Add a Comment: `Users with basic access`.
7. Click `Apply` and `OK`.

**After:**
```
/user group print
Flags: * - default
 #   NAME              RATE-LIMIT COMMENT
 0   premium-users     10M/10M    Users with premium access
 1   basic-users       2M/2M     Users with basic access
```

*   **Explanation:**
    *   `name=basic-users`: Specifies the name of the new user group.
    *   `comment="Users with basic access"`: Adds a comment for better understanding.
    *  `rate-limit=2M/2M`: Sets the download and upload rate limit to 2Mbps for users in this group.

### Step 3: Create Hotspot Users

*   **Why:** We need to add actual users that will connect to the hotspot.
*   **How:** We'll create two users, one in each of the groups.

**Before:**
```
/user print
Flags: X - disabled, P - plaintext-passwords
 #   NAME                GROUP             
```

**CLI Configuration:**
```
/user add name=john password=securepass group=premium-users comment="John Doe premium user"
/user add name=jane password=weakpass group=basic-users comment="Jane Doe basic user"
```
**Winbox GUI:**
1. Navigate to `Users > Users`.
2. Click the `+` button.
3.  In the window that opens, enter `john` in the `Name` field, `securepass` in the `Password` field, and choose the `premium-users` group from the `Group` dropdown menu.
4.  Add a Comment: `John Doe premium user`.
5. Click `Apply` and `OK`.
6.  Click the `+` button again to add `jane`.
7.  In the window that opens, enter `jane` in the `Name` field, `weakpass` in the `Password` field, and choose the `basic-users` group from the `Group` dropdown menu.
8. Add a Comment: `Jane Doe basic user`.
9. Click `Apply` and `OK`.

**After:**
```
/user print
Flags: X - disabled, P - plaintext-passwords
 #   NAME                GROUP             COMMENT
 0   john                premium-users     John Doe premium user
 1   jane                basic-users       Jane Doe basic user
```

*   **Explanation:**
    *   `name=john`: Specifies the username.
    *   `password=securepass`:  Sets the user's password (Note: consider using a strong, hashed password).
    *   `group=premium-users`:  Assigns the user to the "premium-users" group.
    *   `name=jane`: Specifies the username.
    *   `password=weakpass`: Sets the user's password (Note: consider using a strong, hashed password).
    *   `group=basic-users`:  Assigns the user to the "basic-users" group.

### Step 4: Verify User Access

*   **Why:** To check that users are limited to their respective group limits.
*   **How:** After connecting to the hotspot as each user, verify bandwidth using the `torch` tool on the bridge interface.

**CLI Configuration (example):**

```
/interface bridge torch bridge=bridge-54 filter-user=john
```
*   **Explanation:**
    *   `interface bridge torch bridge=bridge-54`: starts torch on bridge interface bridge-54.
    *   `filter-user=john`: filters by user `john` to confirm if the user is getting the correct limit set by the usergroup.

    Connect using the created accounts. Observe in torch the upload and download traffic. The download traffic should not exceed the limits set in the usergroups.

## Complete Configuration Commands:

Here's the entire configuration in CLI format:

```
/user group
add name=premium-users comment="Users with premium access" rate-limit=10M/10M
add name=basic-users comment="Users with basic access" rate-limit=2M/2M

/user
add name=john password=securepass group=premium-users comment="John Doe premium user"
add name=jane password=weakpass group=basic-users comment="Jane Doe basic user"
```

## Common Pitfalls and Solutions:

*   **Pitfall:** Incorrect `rate-limit` syntax in user group definitions (e.g., `10M/10` instead of `10M/10M`).
    *   **Solution:** Verify the `rate-limit` format carefully. The correct format is download/upload speed.
*   **Pitfall:** Users assigned to the wrong group or not assigned to any group (which defaults to the hotspot profile limits).
    *   **Solution:** Double-check user group assignments and make sure your user is not using the global hotspot profile.
*   **Pitfall:** User authentication not working correctly due to issues with the hotspot profile configuration.
    *   **Solution:** Review your hotspot profile settings to ensure authentication is correctly configured (e.g., radius server, if applicable). Also verify that the `hotspot` service is enabled.
*   **Pitfall:** Hotspot interface misconfiguration, such as incorrect bridge interface.
    *   **Solution:** Verify that the hotspot interface is configured on `bridge-54`. The bridge configuration should include all interfaces you intend to use on the hotspot.
*  **Pitfall:** Users not logging out completely and exceeding group quota.
    *   **Solution:** Review session timeout settings in the hotspot profile settings and make sure you are applying a correct session timeout.

## Verification and Testing Steps:

1.  **Connect as User:** Connect a device to the hotspot and authenticate as each user (john and jane).
2.  **Monitor Traffic:** Use the `/interface bridge torch` command on `bridge-54` while downloading large files to confirm bandwidth limits are correctly applied for each user based on their group settings.
    ```
    /interface bridge torch bridge=bridge-54 filter-user=john
    /interface bridge torch bridge=bridge-54 filter-user=jane
    ```
3. **Check Active User:** Use the `/ip hotspot user active print` command to check active users.
    ```
     /ip hotspot user active print
    ```
4.  **Verify User Settings:** Using `/user print` confirm that the correct user and usergroup configuration is applied.
    ```
     /user print
    ```
5. **Check User Group Settings:** Use `/user group print` to verify user group settings.
```
    /user group print
```
## Related Features and Considerations:

*   **User Profiles:** Can be used in conjunction with user groups to limit user session durations, idle timeouts, and data quotas.
*   **Hotspot Radius:** When you have a large number of users, integrating with a RADIUS server is more efficient for user management.
*   **MikroTik API:** Can be used to automate the user and user group management process.
*   **Hotspot walled garden:** You can create free access (no login needed) to some websites.
*   **Custom Login Page:** You can create your custom login page for your users with a company logo or brand.
*   **Accounting:** You can enable Accounting to log users connection and disconnections to the hotspot.

## MikroTik REST API Examples:

Let's create some examples using the REST API for user management.

**Example 1: Get User Groups:**

*   **Endpoint:** `/user/group`
*   **Method:** `GET`
*   **Request Payload:** (None)
*   **Expected Response (JSON):**
    ```json
    [
        {
          ".id": "*0",
          "name": "premium-users",
          "rate-limit": "10M/10M",
          "comment": "Users with premium access",
          "disabled": "false"
        },
        {
          ".id": "*1",
          "name": "basic-users",
          "rate-limit": "2M/2M",
          "comment": "Users with basic access",
          "disabled": "false"
        }
    ]
    ```
    *   **Explanation:** The response provides an array of user groups with their parameters. The `.id` is a dynamic, system-generated ID.

**Example 2: Add a new User Group:**

*   **Endpoint:** `/user/group`
*   **Method:** `POST`
*   **Request Payload (JSON):**

    ```json
      {
        "name": "guest-users",
        "rate-limit": "1M/1M",
        "comment": "Users with guest access"
      }
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "message": "added",
        ".id": "*2"
    }
    ```
    *   **Explanation:** The response indicates success and provides the newly created `.id`.

**Example 3: Add a new User:**
*   **Endpoint:** `/user`
*   **Method:** `POST`
*   **Request Payload (JSON):**
    ```json
    {
      "name": "peter",
      "password": "newSecurePassword",
      "group": "basic-users",
      "comment": "Peter Test user"
    }
    ```
*   **Expected Response (JSON):**

    ```json
    {
      "message": "added",
      ".id": "*2"
    }
    ```

   *   **Explanation:** The response indicates success and provides the newly created `.id`.

**Example 4: Error Handling**

*   If you try to add a user with an existing `name`, you will receive an error message.
*   **Example Response (JSON):**
    ```json
     {
        "error": "already exists: name",
        "message": "already exists: name"
    }
    ```

## Security Best Practices:

*   **Strong Passwords:** Use strong, unique passwords for all users. Consider using the RouterOS password hashing feature.
*   **Regular Review:** Regularly review and update user group settings and user assignments.
*   **Limit User Permissions:**  Grant the minimum necessary permissions to each user.
*   **Monitor Activity:** Use the `/log` features to monitor user activity and login attempts for suspicious behavior.
*   **Disable Default Users:** If possible, disable or change the default user and password for the router itself.
*  **Do not use clear-text passwords:** Use the hashed password option when adding users via the CLI or API.
* **Do not store clear-text passwords:** Do not store your user information in plaintext documents that can be accessed by anyone. Use password manager tools to safely store sensitive data.

## Self Critique and Improvements:

This configuration provides a solid foundation for managing users in a MikroTik hotspot environment. Here are a few areas for potential improvements:

1.  **Hotspot Profiles:** Integration of hotspot profiles was not included; it can be used to configure different hotspot server parameters (like address pool, authentication methods, and more).
2.  **Radius Server:** Incorporating a RADIUS server would make user management more scalable for a large user base.
3.  **Dynamic User Creation:** Implementing dynamic user creation using a custom login page that interacts with the MikroTik API would be ideal in some scenarios.
4.  **Quota Limits:** Implementing data quotas per user or user group.
5.  **Hashed passwords:** Use hashed password when adding users to increase security.

## Detailed Explanations of Topic:

*   **User Groups:** Groups allow you to bundle users with common attributes such as rate limits, time limits and session limits. You can assign users to these groups, simplifying administration.
*   **Users:** User accounts that authenticate to the hotspot. Each user has a username and password. They can be part of user groups or have individual profiles assigned.

## Detailed Explanation of Trade-offs:

*   **User Groups vs. Individual Profiles:** User groups simplify the management of settings for many users at once, especially if a large number of users require the same access parameters. Individual user profiles are more flexible when very specific settings need to be applied on a per-user basis.
*   **Static vs Dynamic User Management:** If user management is static, the administrator can manually create and maintain the users, as shown in this example. If dynamic creation is needed (like self-registration), a custom solution needs to be developed using the MikroTik API to interact with the router.
* **Hotspot vs User group Limits:** Hotspot limits set a hard limit to your whole hotspot. Using user groups allows you to provide different access to your users and to provide them with a better experience.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeting RouterOS 7.11 but is also compatible with 6.48+. Commands should work as expected on those versions. If for some reason, a specific command is not supported, please refer to the official MikroTik documentation for the exact syntax.

This document provides a comprehensive guide to managing users and user groups in your MikroTik Hotspot. Remember to adapt it to your specific needs.
