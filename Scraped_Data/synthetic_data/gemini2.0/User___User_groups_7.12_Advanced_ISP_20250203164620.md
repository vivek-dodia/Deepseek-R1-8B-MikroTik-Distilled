Okay, let's craft a comprehensive technical document for managing users and user groups on MikroTik RouterOS 7.12 (and applicable to 6.48 and 7.x), focusing on an ISP-level scenario with a practical configuration using a /24 subnet and a specific bridge interface.

## Scenario Description:

We're managing an ISP network where we need to create user groups with specific access limitations. We’ll create two user groups: "basic-users" and "premium-users" each with different access privileges. This configuration will be applied to a bridge interface (bridge-28) connected to the downstream customer network (subnet 203.149.152.0/24). The goal is to set up a basic framework for future expansion of user management and access control features. This will be a practical configuration focusing on authentication and basic routing control using user groups.

## Implementation Steps:

Here's a step-by-step guide to configuring user groups and users, with CLI examples and explanations:

**1. Step 1: Verify the Bridge Interface and IP Address Configuration**

   * **Purpose:** Before we start, it’s crucial to verify the configuration of the bridge interface that our users will be connected to, including its IP address and associated network.
   * **Before Configuration:**
      * Open a Terminal in Winbox or use SSH.

   * **CLI Command:**

     ```mikrotik
     /interface bridge print
     /ip address print
     ```
   * **Explanation:**
      * `interface bridge print`: Displays all bridge interfaces, including their name, status, and associated ports.
      * `ip address print`: Shows all configured IP addresses on the router, linked to specific interfaces.
   * **Expected Output:** You should see `bridge-28` listed in the bridge configuration and an IP address within the 203.149.152.0/24 subnet assigned to `bridge-28` interface.
      * Example:
      ```
      /interface bridge print
      Flags: X - disabled, R - running 
      0  R name="bridge-28" mtu=1500 actual-mtu=1500 l2mtu=65535 arp=enabled 
           auto-mac=AA:BB:CC:DD:EE:FF  protocol-mode=none priority=0x8000 
           
      /ip address print
      Flags: X - disabled, I - invalid, D - dynamic 
      #   ADDRESS            NETWORK         INTERFACE      
      0   203.149.152.1/24  203.149.152.0   bridge-28      
      ```

   * **After Configuration:**
      * No changes at this stage. We're just verifying.

**2. Step 2: Create User Groups**

   * **Purpose:**  Define user groups which will hold permissions. We create `basic-users` and `premium-users` with different access levels.
   * **Before Configuration:**  No user groups will exist.
   * **CLI Command:**
     ```mikrotik
     /user group add name="basic-users"
     /user group add name="premium-users"
     ```
   * **Explanation:**
      * `/user group add name="<group_name>"`: Creates a new user group with a specified name.
   * **Expected Output:** User groups `basic-users` and `premium-users` should now be listed.
   * **After Configuration:**
        * Verify the user groups:
            ```mikrotik
            /user group print
            ```
         * Output:
            ```
            # NAME          POLICY              
            0 basic-users   read,write
            1 premium-users read,write
           ```

**3. Step 3: Create Users and Assign them to Groups**

   * **Purpose:** Add the actual user accounts and assign them to their respective groups.
   * **Before Configuration:**  No users with group membership exist.
   * **CLI Command:**
      ```mikrotik
      /user add name="user1" password="password1" group="basic-users"
      /user add name="user2" password="password2" group="premium-users"
      ```
   * **Explanation:**
     * `/user add name="<username>" password="<password>" group="<group_name>"`: Creates a new user with a specified username, password, and group membership.
   * **Expected Output:** The newly created users should appear in the list with their corresponding groups.
   * **After Configuration:**
        * Verify the users:
            ```mikrotik
            /user print
            ```
         * Output:
             ```
             #   NAME    GROUP           DISABLED
             0   user1   basic-users      no
             1   user2   premium-users    no
             ```
**4. Step 4: Define Policy for User Groups**

   * **Purpose**: Define the permissions of user groups. `read` and `write` are the most basic, and other policies may be added on top.
   * **Before Configuration:** Groups have default policies
   * **CLI Command:**

    ```mikrotik
    /user group set basic-users policy=read,test
    /user group set premium-users policy=read,write,test
    ```
   * **Explanation:**
    * `/user group set <group_name> policy=<policy_list>`: Change the policy of the group.
        *  `read`: Allows reading configuration.
        *  `write`: Allows writing to the configuration.
        *  `test`: Enables the 'test' policy for group members.

   * **Expected Output:** The `basic-users` group will have the `read,test` policy and the `premium-users` group will have the `read,write,test` policy.
   * **After Configuration:**
        * Verify the user group policies:
            ```mikrotik
            /user group print
            ```
         * Output:
            ```
            # NAME          POLICY              
            0 basic-users   read,test
            1 premium-users read,write,test
           ```
**5. Step 5: Apply Routing Rules Based on User Groups (Example)**

    * **Purpose**: This step shows a simple example of routing based on groups. We'll use a simple firewall rule as an example, allowing premium users to access an admin port, and blocking it for basic users.
    * **Before Configuration:** Firewall will have default setup.

    * **CLI Command:**
      ```mikrotik
      /ip firewall filter add chain=input action=drop protocol=tcp dst-port=22 in-interface=bridge-28 src-address-list=basic-users log=yes comment="Block SSH for basic users"
      /ip firewall filter add chain=input action=accept protocol=tcp dst-port=22 in-interface=bridge-28 src-address-list=premium-users log=yes comment="Allow SSH for premium users"
      ```
    * **Explanation:**
        *   `/ip firewall filter add ...`: Adds a firewall rule.
        *   `chain=input`: Applies to input traffic.
        *   `action=drop`: Drops the packet.
        *   `protocol=tcp`: Applies to TCP traffic.
        *   `dst-port=22`: Applies to SSH traffic.
        *   `in-interface=bridge-28`: Applies to traffic on the `bridge-28` interface.
        *   `src-address-list=basic-users`: Matches traffic coming from addresses associated with user "basic-users".
        *   `src-address-list=premium-users`: Matches traffic coming from addresses associated with user "premium-users".
        *   `log=yes`: Logs matched packets for monitoring.

    * **Expected Output:** Firewall rules are set to block and allow traffic from different groups.
    * **After Configuration:**
      * Verify firewall filter rules:
          ```mikrotik
          /ip firewall filter print
          ```
        * Output:
           ```
           Flags: X - disabled, I - invalid, D - dynamic 
           0   chain=input action=drop protocol=tcp dst-port=22 in-interface=bridge-28 src-address-list=basic-users log=yes comment="Block SSH for basic users" 
           1   chain=input action=accept protocol=tcp dst-port=22 in-interface=bridge-28 src-address-list=premium-users log=yes comment="Allow SSH for premium users" 
          ```
      * Note: This example does not actually use the user group for authentication; that would require a more complex setup. Instead, it uses the fact that the user group can be assigned to address lists (which can also be done with IP binding).

**6. Step 6: Enable User Based Accounting**
    * **Purpose**: To enable accounting based on user login.
    * **Before Configuration:** Accounting is off.
    * **CLI Command:**
     ```mikrotik
     /system accounting set enabled=yes
     ```
     *  **Explanation:** Enables the user based accounting. This step is fundamental when you need to track user activities based on their login.
    * **Expected Output:** System will record user login events.
    * **After Configuration:**
      * Verify accounting enabled:
          ```mikrotik
          /system accounting print
          ```
        * Output:
           ```
           enabled: yes
          ```
**7. Step 7: Test Users**

    * **Purpose**: To test the authentication with the created users.
    * **Before Configuration:** Users are created but not tested.
    * **CLI Command:**
    * There is not CLI command for user login, it would involve connecting via SSH, WebFig, or the API using the created user credentials.
    * **Explanation:** The steps are different depending on your use case:
        * **SSH:** Try to login into the router using the created credentials through SSH.
        * **WebFig:** Try to login into the router using the created credentials through the web interface.
        * **API:** Use a REST client or a SDK to login using the created credentials.
    * **Expected Output:** `user1` login will be denied if trying to access port 22 (based on the firewall rule); `user2` will be accepted with login on all interfaces, but only be able to read/write/test configuration based on its group.

## Complete Configuration Commands:

```mikrotik
# Verify bridge interface and IP address (Step 1 - Verification):
/interface bridge print
/ip address print

# Create user groups (Step 2):
/user group add name="basic-users"
/user group add name="premium-users"

# Create users and assign them to groups (Step 3):
/user add name="user1" password="password1" group="basic-users"
/user add name="user2" password="password2" group="premium-users"

# Define policies for groups (Step 4):
/user group set basic-users policy=read,test
/user group set premium-users policy=read,write,test

# Configure firewall based on group (Step 5):
/ip firewall filter add chain=input action=drop protocol=tcp dst-port=22 in-interface=bridge-28 src-address-list=basic-users log=yes comment="Block SSH for basic users"
/ip firewall filter add chain=input action=accept protocol=tcp dst-port=22 in-interface=bridge-28 src-address-list=premium-users log=yes comment="Allow SSH for premium users"

#Enable Accounting (Step 6):
/system accounting set enabled=yes

#Verify steps (Step 7):
/user group print
/user print
/ip firewall filter print
/system accounting print
```

## Common Pitfalls and Solutions:

*   **Incorrect Group Assignment:** Ensure users are assigned to the correct group; if a user is in the wrong group, their permissions will be incorrect.
    *   **Solution:** Use `/user print` to verify, and `/user set <user_name> group=<new_group>` to correct the group membership.
*   **Missing or Wrong Policy:** If user groups lack specific policy, they might not have proper access levels.
    *   **Solution:** Use `/user group print` and `/user group set <group_name> policy=<policy>` to correct it. Check that you are not missing important policies like `write` to change the configuration.
*   **Firewall Rule Ordering:** If firewall rules are not in the correct order, some users might receive different access permissions than expected.
    *   **Solution:** Always verify the firewall rules ordering using `/ip firewall filter print`, and use `/ip firewall filter move <number> <position>` to change the ordering.
*   **Forgotten Passwords:** Users may forget their passwords.
    *   **Solution:** Use `/user set <username> password=<new_password>` to reset it.
*   **No User Accounting:** If `accounting` is not enabled, user logins will not be logged and will not work with other features that depend on it.
    *   **Solution:** Enable it with `/system accounting set enabled=yes`.

## Verification and Testing Steps:

1.  **User Group Verification:** Run `/user group print` to ensure groups are created correctly with desired policies.
2.  **User Verification:**  Run `/user print` to confirm that users are created and assigned to the right groups with proper status.
3.  **Firewall Verification:** Run `/ip firewall filter print` to see firewall rules that filter based on groups correctly. Use `/tool torch` to see traffic flowing thru an interface and whether it is being blocked or allowed by a filter rule.
4.  **User login:** Try to access the router using the created users and ensure that they have their corresponding group policy. Check if you are correctly logged using the command `/user active print`.

## Related Features and Considerations:

*   **RADIUS Authentication:**  For larger environments, consider using RADIUS to manage user authentication. This can be done by integrating `/ppp profile` with RADIUS services.
*   **Hotspot:** Combine user groups with MikroTik’s Hotspot feature. You can restrict access, apply data limits, or even billing based on user groups. The hotspot feature uses user based accounting to track data.
*   **IP Binding:** Bind user groups to IP addresses or ranges for more granular network control. This functionality can be used to implement routing based on user groups and can be set through `/ip firewall address-list`.
*  **User Profile**: Use user profiles (`/ppp profile`) to further customize user experiences. This can include setting address pools, rate limits, and other parameters.
* **Resource Monitoring:** Keep an eye on CPU and memory usage via `/system resource monitor`.
* **API:** The `/user` and `/user group` resources can be accessed via the API for automation.

## MikroTik REST API Examples:

Here are some API examples to work with users and user groups:

*   **Create a User Group:**
    *   **Endpoint:** `/user/group`
    *   **Method:** `POST`
    *   **Payload (JSON):**
        ```json
        {
            "name": "test-group-api"
        }
        ```
    *   **Expected Response (200 OK):**
        ```json
        {
            ".id": "*12",
            "name": "test-group-api",
            "policy": "read,write",
             "comment": ""
        }
        ```
    *   **Error Handling:** Check for `400 Bad Request` for invalid inputs, or `500 Internal Server Error` for unexpected server-side issues. Use descriptive error messages to fix the problem.

*   **Create a User:**
    *   **Endpoint:** `/user`
    *   **Method:** `POST`
    *   **Payload (JSON):**
        ```json
        {
            "name": "api-user",
            "password": "api-password",
            "group": "test-group-api"
        }
        ```
    *   **Expected Response (200 OK):**
        ```json
        {
            ".id": "*13",
            "name": "api-user",
            "group": "test-group-api",
            "disabled": false,
            "comment": ""
        }
        ```
     *   **Error Handling:** Check for `400 Bad Request` for invalid inputs (missing fields, invalid user group, etc), or `500 Internal Server Error` for unexpected server-side issues.

*   **Get All Users:**
    *   **Endpoint:** `/user`
    *   **Method:** `GET`
    *   **Payload:** *(none)*
    *   **Expected Response (200 OK):**
        ```json
        [
            {
                ".id": "*1",
                "name": "admin",
                "group": "full",
                "disabled": false,
                "comment": ""
            },
            {
                ".id": "*13",
                "name": "api-user",
                "group": "test-group-api",
                "disabled": false,
                "comment": ""
            }
        ]
        ```
   *   **Error Handling:** Check for `404 Not Found` (if no users are defined) or `500 Internal Server Error`.

*   **Delete a User Group:**
    *   **Endpoint:** `/user/group/{.id}`
    *   **Method:** `DELETE`
    *   **Payload:** *(none)*
    *   **Expected Response (200 OK):** Empty. The item should no longer exist after successful deletion.
    *   **Error Handling:** Check for `404 Not Found` if the user group doesn't exist or `500 Internal Server Error`.

*   **Set Group Policy:**
    *   **Endpoint:** `/user/group/{.id}`
    *   **Method:** `PATCH`
    *   **Payload (JSON):**
      ```json
      {
        "policy": "read,write"
      }
      ```
    *   **Expected Response (200 OK):** Modified object.
     *   **Error Handling:** Check for `400 Bad Request` for invalid inputs, or `500 Internal Server Error`.

## Security Best Practices:

*   **Strong Passwords:** Always enforce strong, unique passwords for user accounts.
*   **Limit Access:** Only provide necessary permissions to user groups. Avoid over-privileging accounts.
*   **Monitor Activity:** Check logs to detect suspicious or abnormal user activity.
*  **Limit Physical Access:** Lock the router in a secure location to prevent unauthorized access.
* **Secure API Access:** If you are using the API, use strong authentication and secure network channels.
* **Regular Updates:** Keep the RouterOS software updated to the latest version to patch vulnerabilities.

## Self Critique and Improvements:

This configuration provides a basic framework. Here's where it could be improved:

*   **Scalability:** For very large ISP environments, consider implementing RADIUS authentication and centralized user management tools.
*   **Advanced Access Control:** Implement more complex firewall rules and QoS policies based on user groups.
*   **More Sophisticated User Management:** Explore MikroTik user profiles (`/ppp profile`) for individual user customization and quotas.
*   **API Integration:** Use the REST API more extensively for automation, including user provisioning and de-provisioning.
*   **Dynamic User Management:** Use Dynamic Address lists to enable and disable users.

## Detailed Explanations of Topic:

*   **Users:** MikroTik users represent accounts that can log in to access the router’s resources. Each user has a username, password, and is assigned to a user group. These can be used for management purposes, pppoe authentication and hotspot authentication.
*   **User Groups:** User groups are containers that hold sets of permissions or policies. They simplify user management by applying the same permissions to a collection of users.
    * **Policy**: policies define what the users in the group can do. Default policies include `read` and `write`. `read` allows the user to check the configuration, and `write` allows the user to modify the configuration.

## Detailed Explanation of Trade-offs:

*   **Local vs RADIUS:** Local users are simple to set up, but RADIUS offers centralized user management, better scalability, and better integration with other systems.
*   **Basic Policies vs Granular Control:** Default user groups provide a quick start, but for a more complex setup you need to create multiple groups with custom policies. Overly complex policies can become confusing.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS 6.48, 7.x, and 7.12. Basic user and user groups settings have not significantly changed across these versions. Commands used here are compatible among these versions, so there's no special instruction required for other RouterOS versions.
