Okay, let's dive into crafting a detailed MikroTik RouterOS configuration for user and user group management within the specified context.

## Scenario Description:

We're setting up a basic point-to-point network on a MikroTik router using RouterOS 7.11 (though compatibility with 6.48 and 7.x is considered). The network will operate on the 112.84.224.0/24 subnet and utilize the `bridge-58` interface for its connections. Our primary focus is on creating and managing users and user groups to control access to router resources, specifically for admin and read-only access.

## Implementation Steps:

Here's a step-by-step guide to implement the user and user group configuration:

### **Step 1: Initial State and Planning**

*   **Before Configuration**: Initially, your MikroTik router has a default `admin` user (typically without a password or with a default password). It's crucial to *change this default password immediately*.
*   **Planning**:
    *   We will create a `readonly` user group for users with limited access.
    *   We will create `adminuser` user with full access.
    *   We will create `guestuser` with read-only access.
    *   We will *disable* the default `admin` user (or change its name).

### **Step 2: Creating the `readonly` User Group**

*   **Why?**: This group will have read-only access, essential for monitoring and basic troubleshooting without granting write permissions.
*   **CLI Command**:
    ```mikrotik
    /user group add name=readonly policy=read
    ```
    **Explanation:**
        * `/user group add`: Creates a new user group.
        * `name=readonly`: Assigns the name "readonly" to the group.
        * `policy=read`:  Sets the group's access policy to read-only.
*   **Winbox GUI**:
    1. Navigate to **System > Users > Group**.
    2. Click the **+** button.
    3. In the new group properties window:
        * Set **Name** to `readonly`.
        * In the **Policies** field check the `read` permission.
        * Click **Apply** and **OK**.
*   **Result**: You now have a new user group called `readonly` with read-only privileges.

### **Step 3: Creating the `adminuser` User with Full Access**

*   **Why?**: This user will have full administrator access for making configuration changes.
*   **CLI Command**:
    ```mikrotik
    /user add name=adminuser group=full password=YourSecurePassword
    ```
    **Explanation:**
        * `/user add`: Creates a new user.
        * `name=adminuser`: Assigns the username "adminuser."
        * `group=full`: Assigns the "full" group, which has full permissions by default.
        * `password=YourSecurePassword`: Sets a password for this user (replace `YourSecurePassword` with a strong one).
*   **Winbox GUI**:
    1. Navigate to **System > Users**.
    2. Click the **+** button.
    3. In the new user properties window:
        * Set **Name** to `adminuser`.
        * Set **Group** to `full`.
        * Set the **Password** and **Confirm Password** fields with your chosen password.
        * Click **Apply** and **OK**.
*   **Result**: You have a user called `adminuser` with full access.

### **Step 4: Creating the `guestuser` User with Read-Only Access**

*   **Why?**: This user will be part of the `readonly` group.
*   **CLI Command**:
    ```mikrotik
    /user add name=guestuser group=readonly password=AnotherSecurePassword
    ```
    **Explanation:**
        * `/user add`: Creates a new user.
        * `name=guestuser`: Assigns the username "guestuser."
        * `group=readonly`: Assigns this user to the previously created `readonly` group.
        * `password=AnotherSecurePassword`: Sets a password for this user.
*   **Winbox GUI**:
    1. Navigate to **System > Users**.
    2. Click the **+** button.
    3. In the new user properties window:
        * Set **Name** to `guestuser`.
        * Set **Group** to `readonly`.
        * Set the **Password** and **Confirm Password** fields with another secure password.
        * Click **Apply** and **OK**.
*   **Result**: You have a user called `guestuser` with read-only access.

### **Step 5: Disabling the Default `admin` User**

*   **Why?**: Disabling the default admin user is crucial for security.
*   **CLI Command**:
    ```mikrotik
    /user set admin disabled=yes
    ```
    **Explanation:**
        * `/user set admin`: Selects the user named "admin."
        * `disabled=yes`: Disables the selected user.
*   **Winbox GUI**:
    1. Navigate to **System > Users**.
    2. Select the `admin` user.
    3. Uncheck the **Enabled** checkbox.
    4. Click **Apply** and **OK**.

*   **Result**: The default `admin` user is now disabled, greatly improving the security posture.

### Step 6: Testing the changes

*  **CLI Command**:
    ```mikrotik
    /user print
    ```
*   **Winbox GUI**:
    1. Navigate to **System > Users**.

You can see a full list of users, and the state of each.

## Complete Configuration Commands:

```mikrotik
/user group add name=readonly policy=read
/user add name=adminuser group=full password=YourSecurePassword
/user add name=guestuser group=readonly password=AnotherSecurePassword
/user set admin disabled=yes
```

**Parameter Explanation:**

| Command | Parameter        | Description                                                      |
|---------|------------------|------------------------------------------------------------------|
| `/user group add` | `name`            | The name of the user group being created                                     |
| | `policy`       | A comma-separated list of access policies (e.g., read, write, test, etc.) |
| `/user add` | `name`            | Username                                                        |
| | `group`           | The user group this user belongs to                                      |
| | `password`        | Password for the user                                                |
| `/user set` | (username)     | The username of the user to modify                             |
| | `disabled`     | `yes` to disable the user, `no` to enable the user                      |

## Common Pitfalls and Solutions:

1.  **Forgetting Passwords**:
    *   **Problem**: It’s a common mistake to forget passwords you’ve set, resulting in locked-out access.
    *   **Solution**: Store passwords in a password manager. If you lose all access, you may need to reset the router to factory defaults.
2.  **Using Weak Passwords**:
    *   **Problem**: Using weak passwords can expose your router to security risks.
    *   **Solution**: Always use strong, unique passwords.
3.  **Not Disabling Default `admin` User**:
    *   **Problem**: The default `admin` user is a well-known target, leaving your router vulnerable.
    *   **Solution**: Disable or rename the default admin user as soon as possible.
4.  **Incorrect Group Permissions**:
    *   **Problem**: Setting the wrong group permissions can lead to either excessive or insufficient access.
    *   **Solution**: Double-check the policy for each group and ensure they have appropriate access levels.
5.  **Not Testing Users**:
   *   **Problem**: If you don't test with other users you may think the configuration works, but it may have some problems.
   *   **Solution**: Test all users and groups before deploying the configuration.
6.  **High CPU or Memory Usage**:
    *   **Problem**: While this setup won't directly cause resource issues, monitoring is good practice.
    *   **Solution**: Use `/system resource print` or check in Winbox under **System > Resources** to monitor CPU and memory usage.

## Verification and Testing Steps:

1.  **Login Test:**
    *   **adminuser**: Attempt to log in using the `adminuser` account via Winbox, SSH, or the web interface. Verify you can perform any router action without restriction.
    *   **guestuser**: Attempt to log in with the `guestuser` account. You should have read-only access to the router’s information but should not be able to make any changes. If you attempt to modify any settings, it should return a "permission denied" error.
2. **CLI Verification**
    * After log in with each user, check what commands they have available.
    * Try to change router configuration while logged in with the `guestuser` account.
3.  **Check Users**: In CLI, use `/user print` to list all users and their respective groups. In Winbox, go to **System > Users** and verify the correct users and groups are listed and enabled (or disabled).
4.  **Check Groups**: In CLI, use `/user group print`. In Winbox, go to **System > Users > Group** and verify the `readonly` group and other groups, and their permissions.
5.  **Test Permissions:**
    *   After logging into the router, try changing a setting using the `guestuser` account to check for "permission denied" error.

## Related Features and Considerations:

1.  **User Limits**:
    *   You can restrict the number of concurrent connections for users using the `max-concurrent-connections` option in `/user` settings.

2.  **RADIUS Server Integration**:
    *   For larger deployments, you can use a RADIUS server to manage users centrally. MikroTik supports RADIUS for authentication.

3.  **API Access Control**:
    *   The MikroTik API can also be controlled by user and group permissions, but this is more complex and requires additional configuration.

4. **Interface security**:
    * When you have a user configured with access to the router it's important to be certain that each of the interfaces has the correct permission set. For example, if you don't want the guest user to be able to access the API on all interfaces, you can restrict it.
     * **CLI Command**:
    ```mikrotik
        /ip service set api address=127.0.0.1,::1
    ```
     * This will restrict the API to localhost, and it won't be possible to access via the public internet.

## MikroTik REST API Examples (if applicable):

While you can manage users and groups through the API, it's **strongly discouraged** to directly create users with passwords over insecure connections. Therefore, I'll focus on listing existing user accounts and getting information about the groups.

**Example 1: Get a List of Users**
*   **API Endpoint**: `/user`
*   **Request Method**: `GET`
*   **Example JSON Payload**:  (none, as it's a GET request)
*   **Example Curl Command**:
    ```bash
    curl -k -u "adminuser:YourSecurePassword" "https://your_router_ip/rest/user"
    ```
*   **Example Response**:
    ```json
    [
       {
           "name": "adminuser",
           "group": "full",
           "disabled": "false",
           ".id": "*1"
       },
       {
           "name": "guestuser",
           "group": "readonly",
           "disabled": "false",
           ".id": "*2"
       },
       {
           "name": "admin",
            "group": "full",
            "disabled": "true",
             ".id":"*3"
        }
   ]
   ```
    *   **Parameter Explanation**:
        * `-k` :  Allows curl to do insecure server connections and transfers.
        * `-u` : sets the authentication using the `username:password` format.

        *   `name`: The username.
        *   `group`: The group the user belongs to.
        *   `disabled`: Boolean showing if the user is enabled or disabled.
        *   `.id`: Internal ID for reference.

**Example 2: Get a List of User Groups**
*   **API Endpoint**: `/user/group`
*   **Request Method**: `GET`
*   **Example JSON Payload**: (none)
*   **Example Curl Command**:
    ```bash
    curl -k -u "adminuser:YourSecurePassword" "https://your_router_ip/rest/user/group"
    ```
*   **Example Response**:
    ```json
    [
      {
          "name": "full",
          "policy": "read,write,test,password,reboot,policy,ftp,web,romon,dude,winbox",
          ".id": "*1"
      },
      {
          "name": "readonly",
          "policy": "read",
           ".id": "*2"
      }
  ]
    ```

    *   **Parameter Explanation**:
        *   `name`: The name of the group.
        *   `policy`: A comma-separated list of all the access policies that the group has.
        *    `.id`: Internal ID for reference.
*  **Error Handling:** The error response will return an http error code and some information in the form of a string. Example response:
    ```
        HTTP/2 401
        content-type: application/json
        content-length: 29

        {"message":"Not authorized"}
    ```
   This example was caused by an incorrect user and password combination.

## Security Best Practices

1.  **Strong Passwords**: Always use strong, unique passwords for all users, especially for those with administrative access.
2.  **Disable Default User**: Always disable the default `admin` user or rename it and set a strong password.
3.  **Least Privilege**: Assign only the necessary permissions to each user group. Avoid granting broad access where it’s not needed.
4.  **HTTPS for Web Interface**: Use HTTPS for web access to ensure the password is not sent in plain text over the network.
5.  **SSH Access**: Only enable SSH access if you require it, and restrict access to specific IP addresses or ranges if possible.
6.  **API Security**: Implement strict authentication for any API access.
7.  **Regular Updates**: Always keep the router’s RouterOS software updated to the latest version to patch security vulnerabilities.

## Self Critique and Improvements

*   **Scope**: This configuration is very basic. For a more robust environment, integration with RADIUS servers or more complex user policies might be needed.
*   **API Security:** Using the REST API directly to manage users requires using a secure connection. The example could be improved with a better approach to handling sensitive information (such as using API keys or tokens).
*   **Error Handling:** The API call error handling should be more detailed (e.g. catching the specific error codes).

**Potential improvements:**
1.  Implement more granular user policies for each group.
2.  Set up logging for user login events, including failed attempts.
3.  Implement API keys for secure API access.

## Detailed Explanations of Topic

**Users and User Groups in MikroTik RouterOS:**
*   **Users:** User accounts define who has access to your router for configuration, monitoring, and other tasks. Each user has a username, a password, and a group that dictates its permissions.
*   **User Groups:** User groups provide a way to apply permissions in bulk. Instead of assigning the same permissions to each user, you assign permissions to groups, and then add users to the correct groups. This simplifies management and ensures consistency. Each group can have multiple policies (read, write, full access, etc.).
*   **Policies**: Policies defines what the user or group has access to, a comma separated list of permissions.

## Detailed Explanation of Trade-offs

*   **Individual Users vs. Groups:** Managing individual users can become cumbersome. Using groups simplifies user permission management.
*   **Read-Only Access:** Limiting access is a trade-off between ease of configuration and security. Read-only users are restricted but can monitor. Full access users can make mistakes.
*   **Default `admin` User**: Using the default `admin` user simplifies things initially but creates a major security risk.

## Configuration for Specific RouterOS Versions:

This configuration is written for RouterOS 7.11, but it is backward compatible with RouterOS 6.48 and 7.x versions with minimal differences. The basic `/user` and `/user group` commands are consistently available and functional across these versions. If specific features of more recent versions are used (e.g., newer API endpoints) specific RouterOS version checks might be needed.

That's a complete and detailed configuration example for users and groups on a MikroTik RouterOS device! I have included all the necessary steps, commands, parameter explanations, and important considerations. Let me know if there are any other specific details you would like to add or any other configuration you want to discuss.
