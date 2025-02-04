Okay, let's craft some in-depth documentation for managing users and user groups on a MikroTik router running RouterOS 6.48 (and compatible with 7.x), targeting an Enterprise network.

## Scenario Description:

We need to manage user access to a specific wireless interface (`wlan-69`) within our enterprise network, using user groups to control access levels. Specifically, we want to create two groups: "staff" with standard access and "admin" with full access. Each group will have users associated with it, and access will be controlled by the group they belong to.  We will create user accounts, assign them to the relevant groups, and then verify the configuration. This setup is useful in environments requiring differentiated permissions based on roles. The network will operate on the `207.2.45.0/24` subnet, and our focus is specifically on access to and interaction with our wifi on `wlan-69`.

## Implementation Steps:

### **Step 1**: Initial Setup and System Preparation

* **Action:** Before we begin, we should ensure that we have a basic network setup, that includes an IP address on the `wlan-69` interface and that we are able to connect to the device via SSH, telnet or Winbox.

* **Winbox GUI Equivalent**: Navigate to `IP` -> `Addresses` and verify an IP address is set on the `wlan-69` interface. Also navigate to `Wireless` and verify that the `wlan-69` interface is enabled, and that a basic config such as frequency and security profile is set. This documentation assumes that this setup is already in place.

* **CLI Example Before:**
```mikrotik
/ip address print
/interface wireless print
```

*   **Output Example:** This command will show your existing IP configuration, and your existing wireless interfaces. Ensure that the `wlan-69` interface exists and is enabled.

* **CLI Example After:** No changes at this step.

*   **Effect:** We are taking a baseline, and ensuring we have a wireless connection.

### **Step 2**: Create User Groups

*   **Action:** Define our two user groups: `staff` and `admin`.

*   **Winbox GUI Equivalent:** `System` -> `Users` -> `Groups` -> `Add` . Repeat once for `staff` and again for `admin`.

*   **CLI Example Before:**
    ```mikrotik
    /user group print
    ```

*   **Output Example:**
    ```
    #   NAME                                       POLICY
    0   read                                       read
    1   write                                      read,write
    2   full                                       read,write,test,password
    ```

*   **CLI Example After:**
    ```mikrotik
    /user group add name=staff
    /user group add name=admin
    /user group print
    ```

*   **Output Example:**
    ```
    #   NAME                                       POLICY
    0   read                                       read
    1   write                                      read,write
    2   full                                       read,write,test,password
    3   staff                                      
    4   admin
    ```

*   **Effect:** We now have two custom groups, `staff` and `admin`, which we will use to group users with specific permissions.

### **Step 3**: Create User Accounts

*   **Action:** Create user accounts and assign them to the groups. We will create `staffuser1` and `staffuser2` as staff users, and `adminuser1` and `adminuser2` as admin users. This example will use password authentication for simplicity.

*   **Winbox GUI Equivalent:** `System` -> `Users` -> `Add` -> Fill out the fields. Repeat as necessary.

*   **CLI Example Before:**
    ```mikrotik
    /user print
    ```

*   **Output Example:**
    ```
    #   NAME       GROUP   DISABLED
    0   admin      full    no
    ```

*   **CLI Example After:**
    ```mikrotik
    /user add name=staffuser1 password=staff1 group=staff
    /user add name=staffuser2 password=staff2 group=staff
    /user add name=adminuser1 password=admin1 group=admin
    /user add name=adminuser2 password=admin2 group=admin
    /user print
    ```

*   **Output Example:**
    ```
    #   NAME       GROUP   DISABLED
    0   admin      full    no
    1   staffuser1 staff   no
    2   staffuser2 staff   no
    3   adminuser1 admin   no
    4   adminuser2 admin   no
    ```

*   **Effect:** We've added four users, each associated with a specific group.

### **Step 4**: Apply User Authentication to Wireless Interface (Example via Hotspot)

*   **Action:**  While user authentication on the MikroTik is useful, its primary purpose is to authorize access to the router itself. We are applying this concept to the wireless, but we need an additional method to control access. We will set up a simple hotspot to manage access to the wireless `wlan-69` interface, so that the user login information applies to wireless access.

* **Winbox GUI Equivalent:** `IP`->`Hotspot` -> `Servers` -> `Add`, then `Hotspot` -> `User Profiles` -> `Add`, then `Hotspot` -> `Users` -> `Add`, and fill out the relevant settings.

* **CLI Example Before:**
    ```mikrotik
    /ip hotspot server print
    /ip hotspot user profile print
    /ip hotspot user print
    ```

*   **Output Example:** We are expecting empty lists in this step.

*   **CLI Example After:**
    ```mikrotik
    /ip hotspot server add name=hotspot1 interface=wlan-69 profile=hsprof1
    /ip hotspot user profile add name=hsprof1 shared-users=1
    /ip hotspot user add name=staffuser1 password=staff1 profile=hsprof1
    /ip hotspot user add name=staffuser2 password=staff2 profile=hsprof1
    /ip hotspot user add name=adminuser1 password=admin1 profile=hsprof1
    /ip hotspot user add name=adminuser2 password=admin2 profile=hsprof1
    ```

*   **Output Example:** The following will be output
```
/ip hotspot server print
#   NAME      INTERFACE   PROFILE   ADDRESS-POOL   PROFILE-COOKIE-LIFETIME  IDLE-TIMEOUT   KEEPALIVE-TIMEOUT  DISABLED
0   hotspot1 wlan-69   hsprof1  default            1d                       none        none          no

/ip hotspot user profile print
#   NAME    SHARED-USERS KEEPALIVE-TIMEOUT TRANSPARENT-PROXY ADDRESS-POOL  RATE-LIMIT  STATUS  ON-LOGIN  ON-LOGOUT   
0   hsprof1  1           none            no                default       none   active    none     none
   
/ip hotspot user print
#   SERVER NAME      PASSWORD   PROFILE   LIMIT-BYTES   MAC-ADDRESS  STATUS
0   hotspot1 staffuser1   staff1      hsprof1     0            00:00:00:00:00:00  active
1   hotspot1 staffuser2   staff2      hsprof1     0            00:00:00:00:00:00  active
2   hotspot1 adminuser1   admin1      hsprof1     0            00:00:00:00:00:00  active
3   hotspot1 adminuser2   admin2      hsprof1     0            00:00:00:00:00:00  active

```
*   **Effect:** Now the hotspot on the wlan-69 interface will use our user accounts, as we have linked our users to the hotspot users database. When users on the wireless try to connect, they will be required to log in with one of these accounts. Note that all users have the same level of access, but you can restrict bandwidth per-profile in the future if desired.

## Complete Configuration Commands:

```mikrotik
/user group add name=staff
/user group add name=admin
/user add name=staffuser1 password=staff1 group=staff
/user add name=staffuser2 password=staff2 group=staff
/user add name=adminuser1 password=admin1 group=admin
/user add name=adminuser2 password=admin2 group=admin
/ip hotspot server add name=hotspot1 interface=wlan-69 profile=hsprof1
/ip hotspot user profile add name=hsprof1 shared-users=1
/ip hotspot user add name=staffuser1 password=staff1 profile=hsprof1
/ip hotspot user add name=staffuser2 password=staff2 profile=hsprof1
/ip hotspot user add name=adminuser1 password=admin1 profile=hsprof1
/ip hotspot user add name=adminuser2 password=admin2 profile=hsprof1
```

**Explanation of Parameters:**

*   `/user group add name=staff`: Creates a user group named "staff".
*   `/user group add name=admin`: Creates a user group named "admin".
*   `/user add name=staffuser1 password=staff1 group=staff`: Creates a user named "staffuser1" with password "staff1" and assigns it to the "staff" group.
*   `/user add ...`: Similar commands to create other users and assign them to the appropriate groups.
*  `/ip hotspot server add name=hotspot1 interface=wlan-69 profile=hsprof1`: Creates a new hotspot server, called hotspot1, tied to the `wlan-69` interface, and connects the server to profile `hsprof1`.
*  `/ip hotspot user profile add name=hsprof1 shared-users=1`: Creates a new hotspot user profile called `hsprof1` which allows 1 user at a time.
*  `/ip hotspot user add...`: Creates a user in the hotspot database linked to the new user profile, `hsprof1`.

## Common Pitfalls and Solutions:

1.  **Incorrect Password:**
    *   **Problem:** Users may mistype passwords.
    *   **Solution:** Double-check passwords. You can reset them using `/user set <username> password=<newpassword>`.
2.  **Incorrect Group Assignment:**
    *   **Problem:** Users might be assigned to the wrong group, leading to incorrect permission levels.
    *   **Solution:** Verify the `group` parameter during user creation or modification, using `/user print` to list the users.
3. **Hotspot Not Working:**
    * **Problem:** The hotspot may not be redirecting the user to a login page when they connect to the network.
    * **Solution:**
        * Confirm that a `wlan-69` interface is properly setup and has an IP address.
        * Confirm that the profile is properly configured.
        * Confirm that the hotspot is bound to the correct interface.
        * Ensure that the `ip dns set allow-remote-requests=yes` command is applied to allow DNS requests via the hotspot.
4. **DNS Resolution Issues:**
    * **Problem:** After successful login users can not resolve DNS queries.
    * **Solution:** Ensure that your routers `IP DNS` config is properly configured.

## Verification and Testing Steps:

1.  **List Users and Groups:** Use `/user print` and `/user group print` to ensure that user accounts and groups have been correctly created.
2. **Connect to the Wireless Interface:** Connect to the `wlan-69` wireless network from a device (e.g., laptop or phone).
3.  **Hotspot Login:**  The device should be redirected to the hotspot login page, if configured. Log in using the usernames and passwords that were created. If not, verify hotspot setup.
4.  **Login Verification:** After a successful login attempt, the user should have the correct level of access. This example provides an equivalent level of access for all users, but could be expanded upon in the future.
5.  **Torch Tool:** Use `/tool torch interface=wlan-69` to monitor traffic on the `wlan-69` interface. Look for traffic from your connected device.

## Related Features and Considerations:

*   **User Profiles:** User profiles can be used to set limits such as bandwidth or access times.
*   **Radius Server:** Integrate with a RADIUS server for centralized user authentication and management.
*   **Web Proxy Authentication:** Combine with the web proxy for content filtering with authentication.
*   **MAC Address Tracking:** Use MAC addresses for additional access control and user tracking.
*   **Password Complexity:** Enforce password complexity policies for enhanced security.

## MikroTik REST API Examples:

*   **Note**: MikroTik's REST API implementation is available starting with RouterOS v6.44, so will work for both v6.48 and v7.x. The API is accessed via `https://<router_ip>/rest`

*   **Example: Create a new user:**

    **API Endpoint:** `https://<router_ip>/rest/user`
    **Method:** `POST`
    **Request Body (JSON):**
```json
{
    "name": "testuser3",
    "password": "testpass3",
    "group": "staff"
}
```

    **Response Body (JSON) Success (201 Created):**
```json
{
    ".id": "*1"
}
```

    **Error Example Response (400 Bad Request):**
```json
{
  "error": "input value already exist"
}
```
    **Description:** Creates a new user named "testuser3" with the password "testpass3" and assigns it to the "staff" group. If a user with that name exists, or the request is otherwise malformed, a bad request error will be returned.  The `.id` value may change depending on your configuration.

*   **Example: Get all users:**

    **API Endpoint:** `https://<router_ip>/rest/user`
    **Method:** `GET`

    **Response Body (JSON):**
```json
[
    {
        ".id": "*0",
        "name": "admin",
        "group": "full",
        "disabled": "false"
    },
        {
        ".id": "*1",
        "name": "staffuser1",
        "group": "staff",
        "disabled": "false"
    },
     {
        ".id": "*2",
        "name": "staffuser2",
        "group": "staff",
        "disabled": "false"
    },
     {
        ".id": "*3",
        "name": "adminuser1",
        "group": "admin",
        "disabled": "false"
    },
    {
        ".id": "*4",
         "name": "adminuser2",
         "group": "admin",
         "disabled": "false"
    }
]
```
    **Description:** Retrieves a list of all configured users along with their properties.
*   **Example: Delete user**
    **API Endpoint:** `https://<router_ip>/rest/user/*1`
    **Method:** `DELETE`

    **Response Body (JSON) Success (204 No Content):**
    Empty Response Body

    **Description:** Deletes a user with the `.id` of `*1`. If the user does not exist, a 404 error will be returned.

## Security Best Practices:

*   **Strong Passwords:** Enforce the use of strong, complex passwords.
*   **Limit Access:** Ensure users have only necessary access. Limit to only the groups they need.
*   **Regular Auditing:** Periodically review user accounts and permissions.
*   **RADIUS for Large Deployments:** Use RADIUS for centralized user management in larger networks.
*   **Secure Access to Router:** Secure management access (SSH, Winbox) with strong passwords and non-default ports.
*   **Regular Software Updates:** Ensure that the router software is updated with the latest patches to avoid known vulnerabilities.

## Self Critique and Improvements:

*   **Current Setup:** While functional, the current setup is fairly basic and does not fully utilize the user group system. All users have the same access to the wifi at this stage.
*   **Improvements:**
    *   **Profile-Based Rate Limiting:**  Configure user profiles within the hotspot to enforce bandwidth limits based on user groups.
    *   **Integration with Radius:** Integrate with a radius server for more advanced user control and authentication.
    *   **Detailed Access Control:**  Use the user groups to provide access to the router, based on their role. (i.e. `staff` could read the config, and `admin` could modify the config)
    *   **Hotspot Customization:** Customize the hotspot login pages for a more professional user experience.
    *   **IP Binding**: Use the `ip hotspot ip-binding` command to tie IPs to users, for more advanced access control.

## Detailed Explanation of Topic:

*   **Users:** In MikroTik RouterOS, user accounts are used for access control. Users can have different levels of permissions by assigning them to different groups. User accounts are primarily used for access to the router and hotspot features.
*   **User Groups:** User groups are a way of managing multiple users with the same set of access rules. By adding users to groups, they can all have their permissions changed at the same time by changing the group properties.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS:** Local user accounts are simpler for smaller setups but lack scalability. RADIUS offers centralized management but requires additional server setup.
*   **Hotspot vs. No Hotspot:** Hotspots provide a captive portal experience, but add some complexity. Without a hotspot, other access control methods must be used.
*   **Simple vs. Complex Groups:** Simple groups offer quick management, while complex group setups require more planning but offer more granular control.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with both RouterOS 6.48 and 7.x. The commands and syntax are consistent between the two versions. If a feature or command is not available in a specific version, it will be noted and an equivalent will be provided. There are not many differences in this area of MikroTik configuration between 6.48 and v7, this configuration works in both versions of RouterOS. The API example will work in any version that is at least 6.44 or greater.

This concludes our detailed documentation for managing users and groups on a MikroTik RouterOS device.  This document provides an overview of how to configure users and groups, as well as an overview of how those users can be used for wireless access.
