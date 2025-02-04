Okay, let's dive into creating detailed technical documentation for user management on MikroTik RouterOS, specifically focusing on a point-to-point link scenario with subnet 126.144.113.0/24 on interface `ether-87`. We'll target RouterOS 6.48 while also keeping 7.x considerations in mind.

## Scenario Description:

We are setting up user and user group management on a MikroTik router that serves as part of a point-to-point link.  While this link itself might not directly require user authentication for data transit, we are focusing on local router access. In a point-to-point scenario, it is critical to manage router access tightly for security. This includes defining different access levels for different users. The interface `ether-87` will serve as our primary interface. The given subnet will be assigned to the interface.

## Implementation Steps:

Here's a step-by-step guide with both CLI and Winbox instructions where applicable.

### **Step 1: Initial Router Setup and Interface Configuration**

   * **Goal:** Ensure basic connectivity and assign the subnet to the interface `ether-87`.

   * **Before:** Router likely has a default configuration.

   * **Action (CLI):**

     ```mikrotik
     /ip address
     add address=126.144.113.1/24 interface=ether-87
     ```
    * **Action (Winbox):**
       1. Navigate to IP -> Addresses.
       2. Click the "+" button.
       3. In the Address field enter "126.144.113.1/24"
       4. In the Interface field select "ether-87"
       5. Click "Apply" and then "OK"

   * **Explanation:**
     - This command adds IP address `126.144.113.1` with a subnet mask of `/24` to the interface `ether-87`. The first usable IP address in the subnet is `126.144.113.1`
     - In a real-world PTP link, you would set the IP address according to your network plan.

   * **After:** Interface `ether-87` is assigned the IP address and is part of the subnet.

   * **Impact:** The router is now reachable on the specified IP within the subnet, assuming there is another device on the same subnet to communicate with.

### **Step 2: Create User Group**

   * **Goal:**  Establish a user group for administrative access. We'll call it "admins."

   * **Before:**  Only default users exist (typically 'admin').

   * **Action (CLI):**
      ```mikrotik
      /user group
      add name=admins policy=read,write,test,password
      ```
    * **Action (Winbox):**
       1. Navigate to System -> Users -> Groups.
       2. Click the "+" button.
       3. In the Name field enter "admins"
       4. In the Policies field enter "read,write,test,password"
       5. Click "Apply" and then "OK"

   * **Explanation:**
     - Creates a user group named "admins."
     - The `policy` parameter defines the permissions associated with the group. In this case:
       - `read`: Allows reading configurations.
       - `write`: Allows modifying configurations.
       - `test`: Allows executing test commands.
       - `password`: Allows changing user passwords.
   * **Note:** Other available policies include `ftp`, `reboot`, `policy` and more.

   * **After:**  A new user group `admins` is available for assigning users.

### **Step 3: Create a User and Assign to the Group**

   * **Goal:** Create a user called `adminuser` and assign to the `admins` group.
   * **Before:** User group `admins` exists.

   * **Action (CLI):**
      ```mikrotik
      /user
      add name=adminuser group=admins password=SecurePassword123
      ```

    * **Action (Winbox):**
       1. Navigate to System -> Users.
       2. Click the "+" button.
       3. In the Name field enter "adminuser"
       4. In the Group field select "admins"
       5. In the Password field enter "SecurePassword123"
       6. Click "Apply" and then "OK"

   * **Explanation:**
     - Creates a user named `adminuser`.
     - Assigns the user to the `admins` group.
     - Sets the initial password to `SecurePassword123`. (Remember to use a strong and secure password in a real-world setting).
   * **Note:**  Make sure to use a secure password.

   * **After:** User `adminuser` is created with `admins` group privileges.

### **Step 4: Disable the Default 'admin' User**
   * **Goal:** Disable the default 'admin' user to enhance security.
   * **Before:** Default 'admin' user is enabled.

   * **Action (CLI):**
      ```mikrotik
      /user disable admin
      ```
    * **Action (Winbox):**
        1. Navigate to System -> Users.
        2. Select the "admin" user.
        3. Uncheck the box labeled "Enabled."
        4. Click "Apply" and then "OK".

   * **Explanation:** Disables the default "admin" user which significantly increases the security of the router.
   * **After:** Default user 'admin' is disabled.

### **Step 5: Verification**
   * **Goal:** Ensure the configuration works as intended.
   * **Before:** User `adminuser` and group `admins` are set up.

   * **Action (CLI):**
        * Connect to the router using the newly created user.
        ```bash
        ssh adminuser@126.144.113.1
        ```
        * Check the active users logged in
        ```mikrotik
        /user active print
        ```
    * **Action (Winbox):**
        * Try to login to the router using user 'adminuser' and the configured password. If succesful you should be logged in.

   * **Explanation:**
       * The first CLI step opens an SSH session, if successful the user `adminuser` is authorized to connect to the router.
       * The second CLI command displays active logged in users. This should show the current active session for `adminuser`
   * **After:** Successful login is achieved via the newly created user.

## Complete Configuration Commands:
```mikrotik
/ip address
add address=126.144.113.1/24 interface=ether-87

/user group
add name=admins policy=read,write,test,password

/user
add name=adminuser group=admins password=SecurePassword123

/user disable admin
```

## Common Pitfalls and Solutions:

*   **Pitfall:** Forgetting the password for the new user or group.
    *   **Solution:** Use the `/user password` command with another user that has rights. Or use winbox and the appropriate user to change the password. Ensure to store passwords securely.
*   **Pitfall:** Locking yourself out by disabling the only admin user.
    *   **Solution:** RouterOS has a safe mode (accessible through serial console) that can be used to recover from misconfigurations.
*   **Pitfall:**  Incorrect group permissions.
    *   **Solution:** Double-check the `policy` parameter when creating or editing user groups. Use `read,write,test,password` for standard administrative access or limit the policy as needed.
*   **Pitfall:**  Weak passwords.
    *   **Solution:** Always use strong, complex passwords. Consider using a password manager.

## Verification and Testing Steps:

1.  **Ping:**  Verify basic connectivity using `ping 126.144.113.1`.
2.  **SSH/Winbox Login:** Try logging in with the new user (`adminuser`) and the configured password.
3.  **Check active sessions**: Use `/user active print` to confirm that your user is correctly logged in.
4.  **Check Configuration**: Use `/user group print` and `/user print` to ensure the configurations are correct.
5. **Torch**: If you suspect traffic is going to a different interface than the one configured, you can use `/tool torch interface=ether-87` to monitor traffic on `ether-87`.

## Related Features and Considerations:

*   **User Profiles:** Use RouterOS' user profiles in hotspot environments or VPN configurations to give users different bandwidth or time limits.
*   **Remote Authentication:** For large scale networks, consider using RADIUS for centralized user authentication and authorization.
*   **Scripting**: You can further automate creation of users or the management of user groups using MikroTik scripting.
*   **API**: You can manage users and user groups through the MikroTik API, as described further down.

## MikroTik REST API Examples:

These examples assume the API is enabled on the router and that you are sending requests from a system with access.

**Example 1: Creating a User Group**

   *   **Endpoint:** `/user/group`
   *   **Method:** `POST`
   *   **JSON Payload:**
        ```json
        {
          "name": "network_admins",
          "policy": "read,write,test,password,ftp,reboot"
        }
        ```
    * **Explanation:**
       - This POST request creates a new user group called `network_admins`. The policy parameter sets the appropriate access rights for the group.
    *   **Expected Response (Success):**
        ```json
        {
          "id": "*123",
          "name": "network_admins",
          "policy": "read,write,test,password,ftp,reboot"
        }
        ```
    * **Error Handling:**  An error such as a `duplicate group` would be returned if the group already exists. Check the HTTP error code and the message returned from the api.
**Example 2: Creating a User**

    *   **Endpoint:** `/user`
    *   **Method:** `POST`
    *   **JSON Payload:**
        ```json
         {
          "name": "network_admin",
          "group": "network_admins",
          "password": "StrongPassword!"
        }
       ```
     * **Explanation:**
        - The POST request creates a new user called `network_admin`. The group is specified by name as `network_admins`. Password is set to `StrongPassword!`.
    *   **Expected Response (Success):**
        ```json
         {
           "id": "*124",
           "name": "network_admin",
           "group": "network_admins"
         }
        ```
   * **Error Handling:** An error can occur if the group `network_admins` does not exist.

**Example 3: Disable a User**
    *   **Endpoint:** `/user`
    *   **Method:** `POST`
    *   **JSON Payload:**
       ```json
       {
           "id": "*124",
           "disabled": true
       }
       ```
    * **Explanation:** This POST request changes the user specified by `id` to disabled.
    * **Expected Response (Success):**
       ```json
         {
           "id": "*124",
           "disabled": true
         }
       ```
   * **Error Handling:** An error can occur if user `id` does not exist.

**Note:** You can access the MikroTik API via an HTTP client such as Postman or Curl, or any other language supporting HTTP requests. The `id` field of the user or user group is important when updating or deleting entities.

## Security Best Practices

*   **Strong Passwords:** Mandate and enforce strong passwords.
*   **Disable Default User:** Always disable the default `admin` user.
*   **Least Privilege:** Only assign the necessary permissions to user groups. Do not give write or policy access to users that do not need it.
*   **Regular Auditing:**  Periodically review user and group configurations.
*   **API Access Control:** Secure API access using access lists.
* **SSH/API only on necessary interfaces:** Do not enable SSH or API access on all interfaces. Limit the interfaces with SSH and API access.
* **Always use TLS:** Only use secure connections when accessing the api.

## Self Critique and Improvements

This configuration is a good starting point, but here's what can be improved:

*   **Password Complexity:** We could enforce a password policy via scripts or third-party tools if RouterOS does not have native features for this.
*   **Audit Logs:** Setting up syslog or other logging mechanisms for detailed user access tracking would further improve security and accountability.
*   **RADIUS Integration:** For larger setups, a RADIUS server for authentication would provide scalability and user management.
*   **Multi-Factor Authentication (MFA):**  For critical access, implementing MFA using RADIUS or other solutions would significantly improve security. However this is not supported on RouterOS 6.x
*   **Scripting**: Create reusable scripts to add users and groups, or to manage the rotation of passwords.

## Detailed Explanations of Topic

*   **Users:** MikroTik users are accounts that have access to the router for configuration and monitoring. Users are associated with user groups.
*   **User Groups:** User groups are containers that define what permissions (policies) users have. This simplifies user management when several users have similar permissions.
*   **Policies:**  Policies determine what a user can do. Common policies include `read`, `write`, `test`, `password`, `ftp`, `reboot`, `policy`.
* **Authentication Types:** RouterOS supports various authentication methods including local, radius, and MAC based authentication.

## Detailed Explanation of Trade-offs

*   **Local Users vs. RADIUS:**  Local user management is simple and suitable for small networks but lacks scalability. RADIUS provides central authentication, making it ideal for larger or enterprise environments.
*   **Granular Policies:** Highly granular policies, while offering security, can be complex to manage. Choose a balanced approach.
*   **Complexity vs. Security:** Adding features such as MFA adds complexity but can also greatly improve security. It is critical to balance usability and security.

## Configuration for Specific RouterOS Versions:

While we targeted 6.48, these commands work mostly the same in RouterOS 7.x. Some differences and considerations:

*   **User Profiles:**  RouterOS 7.x has introduced the concept of user profiles which allow more advanced access configuration, specifically related to access time limits and bandwidth quotas.
*   **API Enhancements:** RouterOS 7.x has more API features.
*   **General Command Syntax:** The basic structure of commands and the user management concept remains generally the same between versions.

This comprehensive document should provide a solid foundation for managing users and user groups on your MikroTik RouterOS device. Remember to always test in a controlled environment before deploying these configurations in a live network.
