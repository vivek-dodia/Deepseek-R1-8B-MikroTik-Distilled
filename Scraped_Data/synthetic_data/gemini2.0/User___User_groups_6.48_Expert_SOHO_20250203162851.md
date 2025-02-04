Okay, let's craft some expert-level MikroTik RouterOS documentation on users and user groups, specifically tailored to a SOHO environment using a /24 subnet and a bridge interface.

## Scenario Description

This scenario focuses on configuring users and user groups on a MikroTik router to manage access and permissions for different types of users, within a SOHO network. We'll create users with varying levels of access, organizing them into logical groups to simplify permission management. The network will use subnet `200.30.219.0/24`, and our main interface will be `bridge-99`.

## Implementation Steps

### Step 1: Verify Existing Setup and Interface

Before making changes, let's verify our current setup. We'll confirm our interface `bridge-99` exists and is configured, and get a baseline state of existing user configurations.

**CLI Command (Before):**

```mikrotik
/interface/print
/user/print
/user/group/print
```

**Explanation:**

*   `/interface/print`: This shows the list of all interfaces on the router. We need to confirm that `bridge-99` exists.
*   `/user/print`: This lists all the configured users.
*  `/user/group/print`: This lists all the configured user groups.

**Expected Output (Example - may vary on your system):**

```
Flags: X - disabled, R - running
 #    NAME                                TYPE    MTU  L2MTU
 0 R  ether1                              ether  1500  1598
 1 R  ether2                              ether  1500  1598
 2    bridge-99                           bridge  1500  1598
     ...

  #   NAME                      GROUP       DISABLED
  0 admin                    full          no
  ...

 #   NAME                                         POLICY
  0  full                                         all
  1  read                                         read
  2  test                                         test
```

**Action:**
We confirm `bridge-99` exists, and we note the presence of the default `admin` user and any groups that exist. We also confirm that `admin` is a full policy group user.

### Step 2: Create User Groups

We'll start by creating user groups with specific policies to control what members can do on the router. We'll create two groups: `monitor` for read-only access and `support` for basic troubleshooting.

**CLI Command:**

```mikrotik
/user/group/add name=monitor policy=read
/user/group/add name=support policy="read,write,test"
```

**Explanation:**

*   `/user/group/add name=monitor policy=read`: This creates a user group named `monitor` with the `read` policy, meaning the user in this group will only be able to monitor the router.
*   `/user/group/add name=support policy="read,write,test"`: This creates a group named `support` with `read,write,test` policies. These users have the ability to read, write and test some router functions. Note that policy items are comma-separated within quotes.

**Winbox GUI:**
Go to *System* > *Users* > *Groups* tab and use the *Add New* button.

**CLI Command (After):**

```mikrotik
/user/group/print
```

**Expected Output:**

```
#   NAME                                         POLICY
 0  full                                         all
 1  read                                         read
 2  test                                         test
 3  monitor                                      read
 4  support                                     read,write,test
```

**Action:** We created two user groups: `monitor` and `support`.

### Step 3: Create Users

Now, let's create user accounts and assign them to the newly created groups. We will create users called `readonlyuser` and `troubleshootuser`.

**CLI Command:**

```mikrotik
/user/add name=readonlyuser group=monitor password=MonitorPassword
/user/add name=troubleshootuser group=support password=SupportPassword
```

**Explanation:**

*   `/user/add name=readonlyuser group=monitor password=MonitorPassword`: This creates a user named `readonlyuser` and assigns it to the `monitor` group.  It also sets a password. Replace `MonitorPassword` with an actual secure password.
*   `/user/add name=troubleshootuser group=support password=SupportPassword`: This creates a user named `troubleshootuser` and assigns it to the `support` group.  It also sets a password. Replace `SupportPassword` with an actual secure password.

**Winbox GUI:**
Go to *System* > *Users* and use the *Add New* button.

**CLI Command (After):**

```mikrotik
/user/print
```

**Expected Output:**

```
 #   NAME               GROUP       DISABLED
  0 admin              full          no
  1 readonlyuser       monitor       no
  2 troubleshootuser   support       no
```

**Action:**
We have created two new users, `readonlyuser` assigned to the `monitor` group and `troubleshootuser` assigned to the `support` group.

### Step 4: Test User Access

We will test the user access by logging into the router through the CLI using SSH using both the `readonlyuser` and `troubleshootuser` credentials. We will then attempt to run commands that are prohibited by the permissions, then run commands that are allowed.

**Action:**
We will attempt the following:
1. Log into the router using the `readonlyuser` account and attempt to add a route. It should fail.
2. Log into the router using the `readonlyuser` account and attempt to print the interface list. It should succeed.
3. Log into the router using the `troubleshootuser` account and attempt to add a route. It should succeed.

**CLI Commands and expected behaviour:**

*   **Test User: `readonlyuser`:**
    *   Log in using SSH: `ssh readonlyuser@<router_ip_address>`
    *   Try to add an IP address: `/ip/address/add address=192.168.1.1/24 interface=bridge-99`. **Expected Result: Access denied**
    *   Print the interface list: `/interface/print`. **Expected Result: successful output of interface list.**
*   **Test User: `troubleshootuser`:**
    *   Log in using SSH: `ssh troubleshootuser@<router_ip_address>`
    *   Try to add an IP address: `/ip/address/add address=192.168.2.1/24 interface=bridge-99`. **Expected Result: Command successful**.

## Complete Configuration Commands

Here's the complete set of MikroTik CLI commands to implement the setup, with parameter explanations:

```mikrotik
# Create user groups
/user/group/add name=monitor policy=read
  # name: The name of the user group (e.g., "monitor").
  # policy: A comma-separated list of policies assigned to this group (e.g., "read").
/user/group/add name=support policy="read,write,test"
  # name: The name of the user group (e.g., "support").
  # policy: A comma-separated list of policies assigned to this group (e.g., "read,write,test").

# Create user accounts
/user/add name=readonlyuser group=monitor password=MonitorPassword
  # name: The username for the new user (e.g., "readonlyuser").
  # group: The name of the user group the user should belong to (e.g., "monitor").
  # password: The password for the user account (e.g., "MonitorPassword").
/user/add name=troubleshootuser group=support password=SupportPassword
  # name: The username for the new user (e.g., "troubleshootuser").
  # group: The name of the user group the user should belong to (e.g., "support").
  # password: The password for the user account (e.g., "SupportPassword").
```

## Common Pitfalls and Solutions

*   **Typographical errors in usernames, passwords, or group names:** This can lead to failed login attempts or unexpected permission issues. Double-check all entries. Use the `print` command to verify your configurations.
*   **Forgotten passwords:** If a password is forgotten, you can reset it via the admin user. Securely store passwords, or use a password management solution.
*   **Incorrect permissions:** Check carefully the permissions applied to the user groups. Double-check `policy` values in group configurations. Use `print` to review current configurations, and review the documentation of user policies for further explanation of access level.
*  **Permissions with side effects:** `test` permission is used for the `/tool` commands. Be careful not to give access to users that can change system configurations unintentionally.  Also be mindful of what is included in `write` permission.
*   **Resource Issues:** If you have a large number of users, or extensive logging, this can put pressure on CPU and memory usage, especially on lower powered router. Monitor the router using tools like *System > Resources* in Winbox and the `/system/resource/print` in CLI. This will help identify any issues.

## Verification and Testing Steps

1.  **Login Verification:** Attempt to log in via SSH or Winbox with each created user. Confirm they can successfully authenticate.
2.  **Permission Verification:**
    *   Log in as `readonlyuser` and try to modify settings. It should not work.
    *   Log in as `troubleshootuser` and verify they can perform allowed actions.
3.  **Use `/user/active/print`:** Check current active sessions to ensure each user connection is listed correctly.

    ```mikrotik
    /user/active/print
    ```
4.  **Use `/log/print`:** Check logs to see the authentication events for the different users.
    ```mikrotik
    /log/print
    ```

## Related Features and Considerations

*   **RADIUS Integration:** For larger networks, consider using a RADIUS server for user authentication and authorization. This can simplify user management and implement more advanced policies.
*   **User Policies:** MikroTik has a comprehensive user policy system, you can learn more about all user access policy options from the MikroTik documentation.
*   **API users:** You can also configure user access to the API.

## MikroTik REST API Examples

While user management is possible via the REST API, the following example is a demonstration only, as it is not common to do this programmatically.

**Example 1: Retrieve User List**

*   **API Endpoint:** `/user`
*   **Request Method:** `GET`
*   **JSON Payload:** None
*   **Expected Response:** A JSON array of user objects, including properties like `name`, `group`, `disabled`.

```json
[
    {
        ".id": "*0",
        "name": "admin",
        "group": "full",
        "disabled": false
    },
    {
        ".id": "*1",
        "name": "readonlyuser",
        "group": "monitor",
        "disabled": false
    },
    {
        ".id": "*2",
        "name": "troubleshootuser",
        "group": "support",
        "disabled": false
    }
]
```

**Example 2: Create a User**

*   **API Endpoint:** `/user`
*   **Request Method:** `POST`
*   **JSON Payload:**

    ```json
    {
        "name": "testapiuser",
        "group": "support",
        "password": "APIPassword"
    }
    ```
*   **Expected Response:**
    *   `201 Created` (Success) with user data or a reference to the new user object
    *   Or `400 Bad Request` with an error message if the request is malformed, or parameters are invalid.

**Example 3: Error Handling**
If an error is encountered, check for a response that isn't `200` or `201`, then read the error message in the response body. For example, trying to create a user with a duplicate username:

```json
{
  "message": "failure: name already exists",
    "error": "failure: name already exists",
    "code": 11,
    "data": ""
}
```
Always check the error message and code and adjust your request accordingly.

## Security Best Practices

*   **Strong Passwords:** Always use strong, unique passwords for all user accounts.
*   **Limit User Permissions:** Grant users only the necessary permissions. Use specific user groups with fine-grained policies.
*   **Disable Default Admin:** Create a new administrative user, then disable or rename the default `admin` user. This reduces the risk of exploitation of well-known default accounts.
*   **Regular Password Rotation:** Encourage users to change their passwords regularly. Consider enforcing password complexity policies.
*   **SSH/API Access Control:** Limit which IP addresses can connect via SSH or the API. Use access lists in `/ip/firewall/filter` and `/ip/firewall/address-list` to implement this.
*  **Regularly Review User Accounts:** Remove or disable users that no longer require access.
*   **Monitor User Activity:** Use the RouterOS log to track user activities. Review logs regularly for anomalies.
*   **Use Secure Connections:** Ensure users connect with secure protocols such as SSH, not Telnet.

## Self Critique and Improvements

*   **Scalability:** For larger environments, this configuration could be enhanced by using a RADIUS server to handle user authentication.
*   **Password Complexity:** Could add a password complexity policy for the users.
*   **Logging:** User specific actions can be logged for further monitoring and audit purposes.
*   **Detailed Policies:** Could include more customized policies, and include more specific policies for individual needs.
*   **More Groups:** Could include more granular control through the implementation of more specific user groups with varying policies.
*   **GUI Explanation:** I could include a step-by-step guide for the implementation using the Winbox GUI.

## Detailed Explanations of Topic

**Users and User Groups:** In MikroTik RouterOS, users provide access to the router. User groups are collections of users with similar access privileges and rights. By using user groups, permissions can be managed in logical sets.

**User Policies:** User policies are the access levels assigned to a user group. User policies can allow access to specific router configurations, such as reading, writing, or running specific commands, and are essential for access control and security. MikroTik provides a number of predefined policies, but also can use custom policies.

## Detailed Explanation of Trade-offs

*   **Individual Users vs. User Groups:** Creating individual users with unique permissions offers the most granular control. However, it's cumbersome to maintain for larger user bases. User groups simplify this by grouping users with shared permissions, making administration easier, especially in larger networks.
*   **Granular Policies vs. Broad Policies:** Granular policies offer better security by limiting access to the minimum required level for each user. However, setting them up and maintaining them can be more complex. Broad policies simplify access configuration but can introduce security risks if not implemented carefully.
*   **Local User Management vs. RADIUS:** Local user management is easier for small deployments but it can be difficult to handle for larger numbers of users. RADIUS offers centralized user management and can be scaled for large environments.

## Configuration for Specific RouterOS Versions

This documentation is specific to RouterOS 6.48, and 7.x. The core concepts remain consistent across versions, but there might be minor differences in syntax or new features. Ensure that you use only the relevant commands for the specified version. Older versions of RouterOS might have different command syntax, so you should always consult the MikroTik official documentation for any given RouterOS version.

This documentation provides a robust and secure setup for user management on a MikroTik Router, tailored for a SOHO environment. It explains the reasoning behind each step, the commands required, and best practices to ensure safe and efficient network management.
