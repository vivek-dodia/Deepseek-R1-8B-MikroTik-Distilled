Okay, let's dive into configuring PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik router running RouterOS 7.12, within the context of a basic SMB network using the specific subnet 114.200.82.0/24 and interface `ether19`. This is a fundamental setup upon which you would build more complex services like PPPoE or PPTP servers.

## Scenario Description:

This configuration demonstrates setting up a basic local user database for PPP authentication on a MikroTik router, specifically for scenarios where a remote user would connect via a PPP protocol such as PPTP or L2TP (though not configured directly here.) While the interface `ether19` is specified, it serves as a placeholder for where these connections might eventually originate. The core of this config is enabling PPP authentication against local user accounts. This example will be used to demonstrate the user database, which is a critical component of AAA. We're focusing on a local database configuration, and we are deliberately *not* setting up a full PPP server or client setup at this point.

## Implementation Steps:

Here’s a step-by-step guide on how to configure PPP AAA using a local user database.

### Step 1: Creating a User

* **Before:** No users exist beyond the default admin user.
* **Action:** Create a user named "testuser" with a password "testpass". We’ll assign this user to the "ppp" group, which gives them the rights to access the PPP functionalities. We're adding a user here to show the local user database functionality - we will *not* use this user directly in PPP connections in this example.
* **Why:**  AAA starts with creating identities that can be authenticated. This step ensures that we can test the user database.
* **CLI Example:**

```mikrotik
/user add name=testuser password=testpass group=ppp
```

* **Winbox GUI:** Navigate to `System > Users` and click the "+" button to add a new user.

* **After:** A user named "testuser" with password "testpass" is added, belonging to the "ppp" group.

### Step 2: Checking the User
*   **Before:** The user "testuser" exists, as created in the previous step
*   **Action:** Verifying that the user has been correctly added
*   **Why:** Verifying the user has been successfully added is a best practice.
*   **CLI Example:**

    ```mikrotik
    /user print
    ```
*   **Winbox GUI:** Navigate to `System > Users` and verify the created user exists.
*   **After:** CLI or GUI displays the newly created user.
    ```
    Flags: * - disabled
     #   NAME     GROUP   
     0   admin    full   
     1   testuser ppp
    ```

### Step 3: Enabling PPP Service and Local User Authentication
*   **Before:** The router does not yet have any explicit PPP configuration, nor a means to enforce authentication.
*   **Action:** Enable local user database authentication for PPP. This setting tells RouterOS to use the locally defined user list for PPP authentication. This is a global setting that will be applied to PPP server interfaces once created.

    ```mikrotik
   /ppp set use-local-user-database=yes
    ```
* **Winbox GUI:** Go to `PPP > Secrets`. The setting is not directly visible in the Secrets window but is controlled in `/ppp settings` instead.
*   **After:** The MikroTik router now authenticates PPP clients using the local user database.

### Step 4: Testing with an Example Secret

* **Before:**  A user and PPP authentication are enabled, but we don't yet have a practical method of using this.
* **Action:** Add a secret using the local "testuser" account, using the name `test` as a service name to test the authentication.
   * This is the beginning of a test setup, we aren't connecting anything to this just yet.
    ```mikrotik
    /ppp secret add name=test service=pptp user=testuser profile=default local-address=114.200.82.254 remote-address=114.200.82.10
    ```
*   **Winbox GUI:** Go to `PPP > Secrets` and click the "+" button to add a secret.
*   **After:** A PPP secret entry is created, associated with the `testuser`. This does *not* open up a service yet, and it needs further configurations to do so, but it does demonstrate using the configured user from the user database in a PPP context.

### Step 5: Verification of the Test Secret

*   **Before:** The secret `test` exists.
*   **Action:** Print the secrets to verify that everything was correctly entered.
*   **Why:** This confirms that the previous step correctly configured the secret.
* **CLI Example:**
    ```mikrotik
    /ppp secret print
    ```
*   **Winbox GUI:** Go to `PPP > Secrets` and observe the newly created secret.
*   **After:** The CLI output or Winbox screen displays the newly created secret.
```
Flags: X - disabled
 #   NAME  SERVICE  USER     PROFILE  LOCAL-ADDRESS    REMOTE-ADDRESS
 0   test  pptp     testuser default 114.200.82.254  114.200.82.10
```

## Complete Configuration Commands:

```mikrotik
/user add name=testuser password=testpass group=ppp
/ppp set use-local-user-database=yes
/ppp secret add name=test service=pptp user=testuser profile=default local-address=114.200.82.254 remote-address=114.200.82.10
```

### Parameters Table:

| Command          | Parameter           | Description                                                                                                                    | Example Value       |
|------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------|
| `/user add`       | `name`              | The username for the user.                                                                                                   | `testuser`           |
| `/user add`       | `password`          | The password for the user.                                                                                                     | `testpass`       |
| `/user add`       | `group`            | The user group the user belongs to (e.g. full, read, ppp) | `ppp`|
| `/ppp set`       | `use-local-user-database`          |Enables local user database for PPP authentication.  | `yes` |
| `/ppp secret add`  | `name`     |  The name of the secret.    | `test`  |
| `/ppp secret add`  | `service`      | The type of PPP service.     | `pptp` |
| `/ppp secret add` | `user` | Username to be used for PPP connections.  Must match the username in the user database.  | `testuser` |
| `/ppp secret add` | `profile`    | PPP profile settings.     | `default` |
| `/ppp secret add`  | `local-address`   | The local IP address when connection is established.  | `114.200.82.254`    |
| `/ppp secret add`  | `remote-address`  | The remote IP address assigned to clients.    | `114.200.82.10`    |

## Common Pitfalls and Solutions:

*   **Problem:**  User cannot authenticate.
    *   **Solution:**
        *   Double-check the username and password.
        *   Ensure `use-local-user-database=yes` is enabled.
        *   Verify the user belongs to the correct group (usually `ppp`).
        *   Check the PPP service configuration (if using PPP interfaces), as a PPP server must be defined and correctly configured.
*   **Problem:**  Incorrectly configured secret settings.
    *   **Solution:**  Use the command `/ppp secret print` to verify all secret settings and correct any errors.
*   **Problem:** High CPU usage when many users are attempting to authenticate.
    * **Solution:** This scenario is more applicable in more complex setups, however be aware of resource limitations on low power devices. Consider using a more efficient authentication method or reduce the number of active users. Review the configured profiles to make sure they do not have unnecessary features enabled that add CPU burden. Monitor with `/system resource monitor`
*   **Security Issue:** Using weak passwords.
    * **Solution:** Enforce strong password policies when creating the users.

## Verification and Testing Steps:

1.  **User Existence:** Check that the user `testuser` is present using the `user print` command.
2.  **PPP Global Setting:** Verify `use-local-user-database` is set to `yes` by using the `ppp print` command.
3.  **Secret Verification:** Verify the secret named `test` was added with correct settings, via the `ppp secret print` command.
4. **Connection Testing:** This example intentionally avoids opening an actual PPP service, but in a future step, we would test with a PPP client by attempting to connect with the configured user `testuser`.
5. **Logging:** Enable detailed logging to see the authentication process. `/system logging add topics=ppp action=memory` Use `/log print` to check these logs.

## Related Features and Considerations:

*   **PPP Profiles:**  Profiles allow customization of PPP connection settings, including DNS servers, idle timeouts, and address pools.
*   **Radius:**  For more advanced setups, a RADIUS server can be used for centralized authentication and accounting. This removes dependency on a local database.
*   **IP Pools:** Assigning dynamic IP addresses using IP pools for PPP connections.
*   **User Groups:** Managing users based on their group membership for granular access control.
*   **PPPoE Server:** This is a common use for PPP authentication and would be the next step if using PPPoE.

## MikroTik REST API Examples:

It is useful to see how these commands would be issued using the MikroTik API.

### 1. Create a User:
* **API Endpoint:** `/user`
* **Request Method:** POST
* **Example JSON Payload:**
```json
{
  "name": "testuser_api",
  "password": "testpass_api",
  "group": "ppp"
}
```
* **Expected Response (Success - HTTP 200 OK):**
```json
{
    "message": "added",
    ".id": "*1"
}
```
*   **Description:** Creates a new user. The `.id` is a unique id for the created object, which is very useful. This could be used to reference the user later, instead of searching by name.
* **Example Failure (Duplicate name - HTTP 400 Bad Request):**
    ```json
   {
    "message": "invalid value for argument name: already present",
        "error": "invalid value for argument name: already present"
   }
    ```

### 2. Get the user list
* **API Endpoint:** `/user`
* **Request Method:** GET
* **Example JSON Payload:** N/A
* **Expected Response (Success - HTTP 200 OK):**
```json
[
    {
        "name": "admin",
        "group": "full",
        "password": "[redacted]",
        "comment": "",
        "disabled": false,
        ".id": "*0"
    },
    {
        "name": "testuser_api",
        "group": "ppp",
        "password": "[redacted]",
        "comment": "",
        "disabled": false,
        ".id": "*1"
    }
]
```

### 3. Get PPP Global Settings:
* **API Endpoint:** `/ppp`
* **Request Method:** GET
* **Example JSON Payload:** N/A
* **Expected Response (Success - HTTP 200 OK):**
```json
{
"use-local-user-database": true,
"accounting": false,
"default-profile": "default",
"enabled": true,
".id": "*0"
}
```
*   **Description:** Gets the current PPP settings, including the `use-local-user-database` value.

### 4. Enable Local User Database:

*   **API Endpoint:** `/ppp`
*   **Request Method:** PATCH
*   **Example JSON Payload:**
```json
{
    "use-local-user-database": true
}
```
* **Expected Response (Success - HTTP 200 OK):**
```json
    {
        "message": "properties changed"
    }
```

### 5. Add a secret

*   **API Endpoint:** `/ppp/secret`
*   **Request Method:** POST
*   **Example JSON Payload:**
```json
{
    "name": "test_api",
    "service": "pptp",
    "user": "testuser_api",
    "profile": "default",
    "local-address": "114.200.82.254",
    "remote-address": "114.200.82.10"
}

```
* **Expected Response (Success - HTTP 200 OK):**
```json
{
    "message": "added",
    ".id": "*1"
}
```

## Security Best Practices

*   **Strong Passwords:**  Always use strong, unique passwords for user accounts. Consider using a password manager and generate a good password.
*   **Least Privilege:**  Grant users only the necessary privileges and avoid overly permissive group memberships.
* **Monitor Logs:** Enable PPP logging to monitor connections and identify any suspicious activity.
* **Remote Access:** Secure remote access to the router and use strong authentication protocols. Limit access via IP addresses as an added layer of security, for example, by limiting access to specific source IP addresses through a firewall or access lists.
* **Regular Updates:** Keep RouterOS up to date to protect against known vulnerabilities.

## Self Critique and Improvements

This is a basic setup of the user database authentication with PPP. The following can be improved and added:

* **PPP Server:** A PPP server would allow connections, so we can see this authentication in action with a client. This would demonstrate a practical use case.
* **Dynamic IP Allocation:**  IP pools would allow a more sophisticated address allocation model instead of using static IPs on a per user basis.
* **RADIUS:**  Using RADIUS would allow us to centralize authentication and accounting. This increases scalability and makes administration easier at the expense of more complexity.
* **More Sophisticated Profiles:** The default profile is minimal and allows basic authentication and connection. More sophisticated profiles can customize the connection significantly.
* **API Error Handling:** Real-world applications must implement proper error handling from the API. This includes handling timeouts, authentication errors and other possible problems.
* **Rate Limiting:** Rate limiting connections per user can help ensure a fair and stable environment.

## Detailed Explanation of Topic

PPP AAA (Authentication, Authorization, and Accounting) is the core security and management framework for Point-to-Point Protocol (PPP) connections, which is the backbone of many network services such as PPPoE, PPTP, and L2TP.

*   **Authentication:** Verifies the identity of the user attempting to connect to the network. Common authentication protocols include PAP, CHAP, and MS-CHAP. In this example, we use the local database for a basic authentication.
*   **Authorization:**  Determines what resources the user is allowed to access. In MikroTik, this can include IP addresses, traffic shaping profiles, and more.
*   **Accounting:**  Tracks the user’s network usage, such as connection time and data consumption. This information is useful for billing purposes or to audit network use.

AAA is a critical part of any network where you need to control access and maintain a record of network activity. For a small home network this may not be necessary, but in larger environments AAA is critical for a manageable and secure network.

## Detailed Explanation of Trade-offs

When configuring PPP AAA, you often face trade-offs:

*   **Local User Database vs RADIUS:**
    *   **Local Database:** Simpler to set up and manage for smaller networks. Less scalable. All authentication information is stored locally on the router. Requires manual user creation and maintenance.
    *   **RADIUS:** More scalable and provides centralized user management. More complex to set up and requires an additional server. Suitable for larger environments with many users.
*   **PPP Authentication Protocols:**
    *   **PAP:** Simplest, but sends passwords in cleartext. Unsafe and rarely used.
    *   **CHAP:** More secure, uses a challenge-response mechanism. Common but can be vulnerable if improperly configured.
    *   **MS-CHAPv2:** Microsoft proprietary version of CHAP, but has known security vulnerabilities.
    * **EAP/TLS:** The most secure option, but significantly more complex to configure. Involves certificate authorities and more involved setup.

*   **Static vs Dynamic IP Addresses:**
    *   **Static:** Easy to configure but inflexible. Can become difficult to manage as the number of users grows. Static IP assignment could be useful for some edge cases where clients need to be identified by the same IP at all times.
    *   **Dynamic:** More flexible and efficient in terms of address management. Simplifies address allocation.

## Configuration for Specific RouterOS Versions:

This configuration is specifically targeting RouterOS 7.12 (although 6.48 and 7.x would be compatible) and assumes that the `/ppp secret`  command exists in the expected form. Older versions of RouterOS may have different command syntax or missing features. If targeting older versions, specific commands must be verified to be compatible, for example, checking documentation, test environments, or older routers.

This completes our detailed explanation for setting up PPP AAA using a local user database on a MikroTik router. This configuration provides a foundation for setting up more complex services such as PPTP or PPPoE. This includes detailed steps, troubleshooting, and API examples.
