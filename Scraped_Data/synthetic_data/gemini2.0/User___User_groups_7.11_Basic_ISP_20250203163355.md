Okay, let's dive into creating detailed documentation for managing users and user groups on a MikroTik router, specifically within the context of a basic setup, using RouterOS 7.11 (and generally applicable to 6.48 and 7.x). We'll focus on a scenario where we're using the provided subnet and interface and will implement a simple user group-based access control scheme.

## Scenario Description:

We'll be setting up user groups and users on a MikroTik router operating on the 202.51.131.0/24 subnet, connected to the bridge interface called `bridge-4`.  The goal is to create a scenario where certain users have specific access privileges. We'll create a simple example: we will have one group called "read-only" and a user that has read access.

## Implementation Steps:

Here's a step-by-step guide to implement user groups and user management on your MikroTik router:

**1. Initial State Check (Before)**

*   **CLI:** Let's begin by confirming the current user list and group list.

    ```mikrotik
    /user print
    /user group print
    ```

*   **Winbox:**
    *   Go to "System" -> "Users". Observe the initial user list (usually just the `admin` user)
    *   Go to "System" -> "Users" and then click "Groups". Observe that there is normally only a `full` group.

*   **Expected Output:**  You should see only the default `admin` user (and possibly other default users you may have set up), and potentially only the `full` group.

**2. Create a New User Group:**
    *   **Goal:** Create a new user group for users with restricted access. We will create a group named `read-only`.
    *   **CLI:**

        ```mikrotik
        /user group add name=read-only policy=read
        ```

    *   **Winbox:**
        1.  Go to "System" -> "Users" and then click "Groups".
        2. Click on the "+" button to add a new group.
        3. Set "Name" to `read-only` and select `read` from "Policy" dropdown and click "Apply" and then "Ok".

*   **Explanation:**
    *   `/user group add`: Adds a new user group.
    *   `name=read-only`:  Sets the name of the new group to "read-only".
    *   `policy=read`: Assigns the "read" policy to the group, which limits users to view-only access.
*   **After:**
*   **CLI Output after adding a group:**
        ```mikrotik
        /user group print
        ```

    *   **Example Output:**
        ```
        Flags: * - default
         #   NAME      POLICY     
         0 * full      full       
         1   read-only read  
        ```
    *   **Winbox:** Now when you look at "System" -> "Users" and then click "Groups" you will see the new group and the assigned policy.

**3. Create a New User and Add to Group:**
    *   **Goal:**  Create a new user named `viewer` and add it to the `read-only` group.
    *   **CLI:**

        ```mikrotik
        /user add name=viewer password=mysecretpassword group=read-only
        ```
    * **Winbox**
        1. Go to "System" -> "Users".
        2. Click on the "+" button to add a new user.
        3. Set "Name" to `viewer`, set a password using the "Password" field and select `read-only` from "Group" dropdown and click "Apply" and then "Ok".

    *   **Explanation:**
        *   `/user add`:  Adds a new user.
        *   `name=viewer`: Sets the username to "viewer".
        *   `password=mysecretpassword`: Sets the user's password (replace with a strong password).
        *   `group=read-only`: Assigns the user to the "read-only" group.
    *   **After:**
*   **CLI Output after adding a user**
        ```mikrotik
        /user print
        ```
*   **Example Output**
        ```
        Flags: * - default
         #   NAME   GROUP     
         0 * admin  full
         1    viewer  read-only
        ```

    *   **Winbox:**  Now when you look at "System" -> "Users" you will see the new user, and the assigned group.

**4. Test the user:**

*   **Goal**: Using a second device, log in to the Mikrotik router as the newly created `viewer` user, and verify that they only have read access.
*   **Steps**: Connect using Winbox or SSH, entering the username `viewer` and the password `mysecretpassword`. Attempt to make changes. You should see that you are unable to make any changes and only have read access.

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to set up the user group and user, with explanations:

```mikrotik
# Create a user group with read-only access
/user group add name=read-only policy=read

# Create a user with the specified name, password, and group.
/user add name=viewer password=mysecretpassword group=read-only
```

*   **`/user group add name=read-only policy=read`**
    *   **`/user group add`**: Command to add a new user group.
        *   `name=read-only`: Sets the name of the group to "read-only".
        *   `policy=read`: Specifies the permissions policy assigned to this group. In this case `read` means the users in this group can only view configuration and settings.

*   **`/user add name=viewer password=mysecretpassword group=read-only`**
    *   **`/user add`**: Command to add a new user.
        *   `name=viewer`: Sets the username to "viewer".
        *  `password=mysecretpassword`: Sets the password for this user. It is highly recommended that a secure password be used.
        *   `group=read-only`: Assigns the newly created user to the existing `read-only` group.

## Common Pitfalls and Solutions:

*   **Problem:** Incorrect Password for User
    *   **Solution:** You can reset the user's password using the command `/user set viewer password=newpassword`. Make sure that you use the correct username. If you are logged in with this user, and you want to change your password you can use `/user set [find name=viewer] password=newpassword`. If you don't know the username, you can use this command `/user set [find where disabled=no] password=newpassword`, but keep in mind you can potentially change the password of a user you did not intend to change.

*   **Problem:** User Not Added to Correct Group
    *   **Solution:** You can modify a user's group membership using the command `/user set viewer group=new-group-name`.
*   **Problem:** "read" Policy Not Limiting Access Correctly
    *   **Solution:** In rare cases, the "read" policy might not fully limit the user to view-only.  Verify that no additional specific policies are assigned to the user. Also, double check which other user groups the user is part of, and verify that they do not have other policies. It may be necessary to use more granular permissions using specific access policies if the `read` policy does not provide sufficient security.

*   **Problem:** User is locked out
    *   **Solution:** You must log in with admin access to reset the password. You can do so with the command described above under "Incorrect password for user".
*   **Security Issue:** Using default admin account for general purposes.
    *   **Solution:** Create specific admin users with different levels of access. Disable the default `admin` account when no longer needed. Do this using `/user disable admin`.
*   **Resource Issue:** Very large number of users.
    *   **Solution:** This can potentially lead to slower processing times for configuration. It is recommended to keep the total user count to only what is necessary for your specific use case. This also makes it easier to monitor and maintain the list.

## Verification and Testing Steps:

1.  **Log in as `viewer`:** Attempt to log into the router using Winbox or SSH as the new user "viewer" with the corresponding password.
2.  **Test Read-Only Access:**
    *   Once logged in as the `viewer` user, attempt to perform actions that require write access such as:
        * Add a new interface: `/interface ethernet add name=test`
        * Change the name of an interface: `/interface ethernet set ether1 name=test`
    * You will notice that you get error messages informing you that you do not have permission.
    * Using Winbox, attempt to make a change to the configuration. You will notice that you are unable to.
3.  **Verify user group:** Use the following command to verify that the user group is configured as expected.

    ```mikrotik
        /user group print
    ```
4.  **Verify User configuration:** Use the following command to verify that the user is configured as expected

    ```mikrotik
        /user print
    ```

## Related Features and Considerations:

*   **User Profiles:** RouterOS allows you to define user profiles with more granular access policies. User profiles can also be added to groups, instead of just directly to users.
*   **API User:**  For automated access, create users specifically for API access with very limited permissions. Be careful how you store the API credentials.
*  **RADIUS Server:** For a larger network it is preferable to use a RADIUS server for centralized user management and authentication.
*  **Disable Default Admin Account:** When possible, it is a good practice to disable the default admin account after setting up users with administrator access.
*  **Logging:**  Enable logging for user logins and failed logins for audit trail purposes.

## MikroTik REST API Examples (if applicable):

Here are some examples of REST API calls for managing users and user groups:

**Create a User Group:**

*   **Endpoint:** `/user/group`
*   **Method:** `POST`
*   **JSON Payload:**

    ```json
    {
      "name": "api-group",
      "policy": "write"
    }
    ```
*   **Expected Response (200 OK):**

    ```json
    {
      ".id": "*12",
      "name": "api-group",
      "policy": "write"
    }
    ```
*   **Explanation:**
    *   The `name` field sets the group name to `api-group`.
    *  The `policy` field sets the access permissions for users in the group to `write`.
*   **Error Handling:** If the group already exists, you'll get a 400 (Bad Request). Catch and handle such errors in your API client. Also be aware that this could return a different error if not all mandatory fields are provided.

**Create a User:**

*   **Endpoint:** `/user`
*   **Method:** `POST`
*   **JSON Payload:**

    ```json
    {
      "name": "api-user",
      "password": "supersecretpassword",
      "group": "api-group"
    }
    ```
*   **Expected Response (200 OK):**

    ```json
      {
        ".id": "*13",
        "name": "api-user",
        "group": "api-group"
        }
    ```
*   **Explanation:**
    * The `name` field sets the username to `api-user`.
    * The `password` field sets the user's password.
    * The `group` field sets the group membership to `api-group` that we created in the previous step.
*   **Error Handling:** If the group does not exist or a user with that username already exists, you will receive an error. Handle these errors in your API client.

**Get a User by ID:**

*   **Endpoint:** `/user/*13` (assuming the user with `.id` as `*13`)
*   **Method:** `GET`
*   **Expected Response (200 OK):**

    ```json
    {
      ".id": "*13",
      "name": "api-user",
      "group": "api-group"
    }
    ```
*   **Error Handling:** A 404 error will be returned if the user ID does not exist.

**Update a user (e.g., to change the password)**

*   **Endpoint:** `/user/*13`
*   **Method:** `PATCH`
*   **JSON Payload:**
    ```json
        {
        "password": "newsupersecretpassword"
        }
    ```
*   **Expected Response (200 OK):**

    ```json
        {
        ".id": "*13",
        "name": "api-user",
        "group": "api-group"
        }
    ```
*   **Explanation:**
     * The `password` field sets the user's password.
*   **Error Handling:** A 404 error will be returned if the user ID does not exist.

**Delete a user**

*   **Endpoint:** `/user/*13`
*   **Method:** `DELETE`
*   **Expected Response (200 OK):**

    ```json
        {
        "message":"deleted"
        }
    ```
*   **Error Handling:** A 404 error will be returned if the user ID does not exist.

**Note:** Replace  `*13` with the actual `id` of the user or group you want to target in the API call. If using the API, make sure to use secure access controls.

## Security Best Practices

*   **Strong Passwords:** Enforce strong password policies for all users.
*   **Least Privilege:**  Assign users only the permissions they need to perform their tasks. Create granular groups with very specific policies.
*   **Regular Audits:**  Review user lists and group memberships regularly.
*   **Disable Unused Accounts:** Disable user accounts that are no longer in use.
*   **API Security:** Use secure access methods for the MikroTik API.
*   **HTTPS for Winbox/API:** When possible, force HTTPS when using Winbox and the API.
*   **Limited Access:** Restrict the IP addresses that can connect to the router for Winbox and SSH access.
*   **Firewall:** Implement firewalls that restrict access to internal resources.

## Self Critique and Improvements

*   **Current:** This configuration is a basic setup with one additional user group, and a single example user.
*   **Improvement:**
    *   **More Granular Policies:** Implement more specific policies instead of relying only on the predefined `read` or `write` access. This can be achieved by creating custom user policies that more closely define the permissions required for each user. This will provide higher security and control over access.
    *   **User Profiles:** Start using user profiles in addition to user groups to have additional configuration parameters for users.
    *   **RADIUS Integration:** For a larger or more dynamic environment, move towards a RADIUS server for centralized authentication and authorization, instead of relying solely on locally defined users.
    *   **Access Logging:** Implement detailed logging for all user access. This includes user logins, logouts, and failed attempts. Also include which configuration changes are made, by which users and when. This is useful for debugging and security audits.

## Detailed Explanations of Topic

*   **User Management:**  User management in RouterOS is fundamental for securing and controlling access to the device. Users are assigned to groups and policies to limit their access to RouterOS configuration and operation. It is essential to have different accounts for different roles, this avoids all members having access to all settings. Using user management, an administrator can create accounts with very specific access.
*   **User Groups:** User groups simplify the process of managing users by enabling you to assign a set of permissions to multiple users simultaneously. This greatly simplifies administration and reduces error. A user can be a member of more than one user group. User groups are defined by a single policy, such as `read`, `write` or `full`, or any other custom policy.
*   **Policies:**  Policies control what users are allowed to do on the RouterOS system. Predefined policies like `read` and `write` provide basic read or write permissions to the RouterOS configuration.  However, policies can also be granularly defined by the administrator. A custom policy is a more advanced method of controlling exactly which parameters a user can or can not control. It allows for more fine grained control.
*   **API Access:**  The RouterOS API enables programmatic access, ideal for automation and external integration with other systems. API users should be created specifically for API access, and have very restricted access. API users should be provided with strong passwords, and be carefully monitored.

## Detailed Explanation of Trade-offs

*   **Local Users vs. RADIUS:** Local users are simpler to manage for small setups, but RADIUS servers are ideal for scaling large and dynamic environments where central management of user authentication and accounting is crucial. RADIUS simplifies large scale user management, and provides additional security. A disadvantage of using a RADIUS server is that an additional external device is necessary. The router itself also has to be configured to connect and authenticate with the RADIUS server, which requires additional setup.
*   **Basic vs. Custom Policies:**  While basic policies like `read` and `write` are easier to implement, custom policies offer granular control but require more effort to define and manage. If more granular control is necessary, custom policies are the preferred solution. However, they are not necessary for simple cases.
*  **Winbox vs. CLI vs. API:**  Winbox is ideal for novice administrators, providing a graphical interface. The CLI is more efficient for experienced administrators and automation. API access is best suited for integration with other systems and automation. Some configurations and features are only accessible via the CLI. This is also true for the API. While Winbox is very simple to use for most cases, it does not always provide access to all features.
*  **User Groups vs. Individual User Policies:** User groups provide better scalability and maintainability. It is much easier to add users to a user group than to define an individual access policy for each user. However, in certain scenarios, individual policies for specific users are the preferred approach.
*  **Default admin vs. Custom admin account:** Using the default `admin` account is not recommended for security reasons. It is better practice to create specific admin user accounts for the different roles needed.

## Configuration for Specific RouterOS Versions:

This document has been written specifically for RouterOS 7.11, however, the user management functionality has not changed significantly over the past few versions, and most of this configuration will be compatible with RouterOS versions 6.48 and 7.x. However, always refer to the official MikroTik documentation for specific version compatibility information. If using a RouterOS version below 7, the syntax for the API will be different. Refer to the relevant RouterOS documentation for that specific version.

This detailed documentation should give you a solid foundation for managing users and user groups on your MikroTik router. Remember to adjust these configurations based on your specific needs and environment.
