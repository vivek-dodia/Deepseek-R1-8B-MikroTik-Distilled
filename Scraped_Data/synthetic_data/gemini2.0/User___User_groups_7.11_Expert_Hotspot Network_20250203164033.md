Okay, let's dive into a comprehensive guide for configuring user and user groups on MikroTik RouterOS 7.11 (and relevant older versions) for a hotspot network scenario, focusing on expert-level configurations.

## Scenario Description:

We're building a hotspot network using a MikroTik router with the `bridge-98` interface. The subnet is `164.88.96.0/24`. We need to create users with varying levels of access, implement user groups for efficient management, and ensure secure authentication. We will focus on using local user profiles, not remote AAA.

## Implementation Steps:

Here's a step-by-step guide to configure users and user groups, along with detailed explanations, examples, and before/after configurations:

**1. Step 1: Initial Setup and Interface Verification**

*   **Description:** This step ensures the `bridge-98` interface exists and is properly configured. We'll check the interface status and ensure it has an IP address in our target subnet if you want to connect via IP.
*   **CLI Before Step:**

    ```mikrotik
    /interface bridge print
    /ip address print
    ```
    You should see a bridge interface, but no users configured at this time.

*   **CLI Commands:**

    ```mikrotik
    /ip address add address=164.88.96.1/24 interface=bridge-98
    /interface bridge set bridge-98 arp=enabled
    ```
    These commands assign an IP address to the bridge and enable ARP. If you are using DHCP make sure you configure it properly.
*   **CLI After Step:**

    ```mikrotik
    /interface bridge print
    /ip address print
    ```
    You should now see `bridge-98` with an IP address and ARP enabled.

*   **Winbox GUI Instructions:**
    *   Navigate to *IP > Addresses*.
    *   Click the "+" button to add a new IP.
    *   Enter `164.88.96.1/24` in the address field.
    *   Select `bridge-98` as the interface.
    *   Click "OK".
    *   Navigate to *Bridge > Bridges* and click on your bridge. Make sure ARP is enabled.
*   **Effect:** `bridge-98` has an IP address and is ready for hotspot users.

**2. Step 2: Creating User Groups**

*   **Description:** We'll define user groups with specific profiles, such as "basic" and "premium," to manage users efficiently.
*   **CLI Before Step:**

    ```mikrotik
    /user group print
    ```
    You should only see default groups at this time.
*   **CLI Commands:**

    ```mikrotik
    /user group add name=basic comment="Basic access"
    /user group add name=premium comment="Premium access"
    ```
*   **CLI After Step:**

    ```mikrotik
    /user group print
    ```
    You should see "basic" and "premium" user groups added.
*    **Winbox GUI Instructions:**
    * Navigate to *System > Users > Groups*.
    * Click the "+" button to add a new group.
    * Enter `basic` as the group name, add an optional comment, click "Ok".
    * Add the `premium` group in the same way.
*   **Effect:** We have "basic" and "premium" user groups created, ready for user assignments.

**3. Step 3: Creating User Profiles**

*   **Description:** Create profiles to define the limitations, such as rate limits and uptime for users.
*   **CLI Before Step:**

    ```mikrotik
    /user profile print
    ```
    You should only see default profiles at this time.
*   **CLI Commands:**

    ```mikrotik
    /user profile add name=basic-profile rate-limit="1M/1M"  address-list=basic-users comment="Basic profile"
    /user profile add name=premium-profile rate-limit="10M/10M" address-list=premium-users comment="Premium profile"
    ```
     *  `rate-limit` sets the upload and download speed limits.
     *  `address-list` creates a dynamic list of IP addresses assigned to users with these profiles, these are used to give them priority or other special treatment.

*   **CLI After Step:**

    ```mikrotik
    /user profile print
    ```
    You should see "basic-profile" and "premium-profile" user profiles added.
*  **Winbox GUI Instructions:**
    *   Navigate to *System > Users > Profiles*.
    *   Click the "+" button to add a new profile.
    *   Enter `basic-profile` as the profile name.
    *   Enter `1M/1M` as Rate Limit.
    *   Enter `basic-users` as the Address List.
    *   Add the optional comment and click "Ok".
    *   Add the `premium-profile` profile in the same way.
*   **Effect:** We have rate limits and dynamic IP address lists associated with profiles.

**4. Step 4: Creating Users and Assigning Groups and Profiles**

*   **Description:** Create actual user accounts and assign them to the defined groups and profiles.
*   **CLI Before Step:**

    ```mikrotik
    /user print
    ```
    You should only see the admin user by default.
*   **CLI Commands:**

    ```mikrotik
    /user add name=user1 password=pass1 group=basic profile=basic-profile comment="Basic user"
    /user add name=user2 password=pass2 group=premium profile=premium-profile comment="Premium user"
    ```
*   **CLI After Step:**

    ```mikrotik
     /user print
     ```
     You should see the two new users configured.
*  **Winbox GUI Instructions:**
    *   Navigate to *System > Users*.
    *   Click the "+" button to add a new user.
    *   Enter `user1` as the name.
    *   Enter `pass1` as the password.
    *   Select `basic` as the group.
    *   Select `basic-profile` as the profile.
    *   Add the optional comment and click "Ok".
    *   Add the `user2` user in the same way using the `premium` group and the `premium-profile` profile.
*   **Effect:** We now have real user accounts with specific access levels.

**5. Step 5: Activating Hotspot (Optional)**

*   **Description:** If a hotspot is desired, we'll activate it. This is an additional step if needed to use hotspot authentication, otherwise this will just be the local user database authentication. We will configure the hotspot on the bridge.
*   **CLI Before Step:**

    ```mikrotik
     /ip hotspot print
     ```
    If you don't have a hotspot it will show empty.
*   **CLI Commands:**

    ```mikrotik
    /ip hotspot add name=hotspot1 interface=bridge-98 address-pool=none profile=default
    /ip hotspot user profile set default transparent-proxy=no
    /ip hotspot profile add name=profile-hotspot  use-radius=no  rate-limit=10M/10M  keepalive-timeout=infinite html-directory=hotspot
    /ip hotspot user profile add name=basic-hotspot-profile  rate-limit=1M/1M  parent-profile=profile-hotspot
    /ip hotspot user profile add name=premium-hotspot-profile  rate-limit=10M/10M  parent-profile=profile-hotspot
    /ip hotspot user set user1 profile=basic-hotspot-profile
    /ip hotspot user set user2 profile=premium-hotspot-profile
    ```
    This will add a basic hotspot to `bridge-98`, configure a non radius, local authentication, and apply it to the users created.
*   **CLI After Step:**

    ```mikrotik
    /ip hotspot print
    /ip hotspot user print
    ```
    This should show the new hotspot configuration, and the users configured to use it.
*  **Winbox GUI Instructions:**
    * Navigate to *IP > Hotspot*.
    * Click the "+" button to add a new hotspot.
    * Enter `hotspot1` as the name.
    * Select `bridge-98` as the interface.
    * Make sure Address Pool is set to `none`.
    * Set profile to `default`, click "Ok".
    * Go to *Hotspot > User Profiles*.
    * Disable transparent proxy for the default user profile.
    * Create the `profile-hotspot` user profile with a rate-limit of `10M/10M` and set keepalive to `infinite`.
    * Create the `basic-hotspot-profile` with `1M/1M` rate limit and select `profile-hotspot` as parent profile.
    * Create the `premium-hotspot-profile` with `10M/10M` rate limit and select `profile-hotspot` as parent profile.
    * Go to *Hotspot > Users*, and for each user created set their profile to their respective hotspot profile.
*   **Effect:** Hotspot is now active and using the defined users and profiles.

## Complete Configuration Commands:

Here's the full set of commands to accomplish this setup:

```mikrotik
/interface bridge add name=bridge-98
/ip address add address=164.88.96.1/24 interface=bridge-98
/interface bridge set bridge-98 arp=enabled
/user group add name=basic comment="Basic access"
/user group add name=premium comment="Premium access"
/user profile add name=basic-profile rate-limit="1M/1M" address-list=basic-users comment="Basic profile"
/user profile add name=premium-profile rate-limit="10M/10M" address-list=premium-users comment="Premium profile"
/user add name=user1 password=pass1 group=basic profile=basic-profile comment="Basic user"
/user add name=user2 password=pass2 group=premium profile=premium-profile comment="Premium user"
/ip hotspot add name=hotspot1 interface=bridge-98 address-pool=none profile=default
/ip hotspot user profile set default transparent-proxy=no
/ip hotspot profile add name=profile-hotspot  use-radius=no  rate-limit=10M/10M  keepalive-timeout=infinite html-directory=hotspot
/ip hotspot user profile add name=basic-hotspot-profile  rate-limit=1M/1M  parent-profile=profile-hotspot
/ip hotspot user profile add name=premium-hotspot-profile  rate-limit=10M/10M  parent-profile=profile-hotspot
/ip hotspot user set user1 profile=basic-hotspot-profile
/ip hotspot user set user2 profile=premium-hotspot-profile
```

**Parameter Explanations:**

| Command                | Parameter            | Description                                                                                                                                       |
| ---------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/interface bridge add`   | `name`               | Name of the bridge interface.                                                                                                                 |
| `/interface bridge set` | `arp`                | Enables or disables ARP for the specified bridge interface.                                                                                     |
| `/ip address add`      | `address`            | IPv4 address and subnet mask.                                                                                                                   |
|                        | `interface`          | Interface on which the IP is assigned.                                                                                                      |
| `/user group add`      | `name`               | Name of the user group.                                                                                                                         |
|                        | `comment`            | Optional comment for the user group.                                                                                                            |
| `/user profile add`    | `name`               | Name of the user profile.                                                                                                                       |
|                        | `rate-limit`         | Data rate limit in the form `upload/download`.                                                                                                   |
|                        |`address-list`         | Dynamic list name to store IPs assigned to users with this profile.                                                                            |
|                        | `comment`            | Optional comment for the user profile.                                                                                                          |
| `/user add`           | `name`               | Username.                                                                                                                                        |
|                        | `password`           | User's password.                                                                                                                                |
|                        | `group`              | User group to which the user belongs.                                                                                                            |
|                        | `profile`            | User profile assigned to this user.                                                                                                             |
|                        | `comment`            | Optional comment for the user.                                                                                                                |
| `/ip hotspot add`      | `name`               | Name of the hotspot.                                                                                                                            |
|                        | `interface`          | Interface where the hotspot is enabled.                                                                                                         |
|                        | `address-pool`       | IP pool for hotspot users (set to none for local users).                                                                                                                            |
| `/ip hotspot user set` | `user`               | Target user to set parameters.                                                                                                                |
|                      | `profile`                | Hotspot profile assigned to this user.                                                                                                                 |
| `/ip hotspot user profile set`      | `transparent-proxy`       | Enables or disables transparent proxy.                                                                                                        |
|`/ip hotspot profile add`| `name`| Hotspot profile name |
|                        | `use-radius`|Enables or disables the usage of radius server|
|                        |`rate-limit`  | Max download and upload speed|
|                        | `keepalive-timeout`| Time the user will remain active|
|                        |`html-directory`  | Folder with custom hotspot html pages|
| `/ip hotspot user profile add`   | `name` | Hotspot user profile name.                                                                                                                           |
|                        | `rate-limit` | Max download and upload speed for users in this profile.                                                                                             |
|                        | `parent-profile` | Set the parent profile for the user profile.                                                                                                         |

## Common Pitfalls and Solutions:

*   **Pitfall:** Incorrect subnet mask on the bridge.
    *   **Solution:** Double-check the subnet mask and ensure it matches your network. Use the command `/ip address print` to check.
*   **Pitfall:** Users can't authenticate with the Hotspot.
    *   **Solution:** Ensure the users have the correct profiles assigned to them, both in the `/user` section and the `/ip hotspot user` section. Ensure the user profiles on the hotspot have the parent-profile properly set.
*   **Pitfall:** Users are not getting the correct bandwidth.
    *   **Solution:** Confirm user profiles and parent profiles are set correctly, and rate limits are correctly specified.
*   **Pitfall:** Forgotten password of user.
    *   **Solution:** Use command `/user set user1 password=newpass` to change the password. This will overwrite the old password.
*   **Pitfall:** Security risk when passwords are hardcoded.
    *   **Solution:**  Consider using radius authentication to secure your hotspot network. Don't use default passwords, consider using strong complex passwords, and change them regularly.
*   **Pitfall:** High CPU or memory usage from too many users.
    *   **Solution:**  Monitor router's CPU and memory usage with `/system resource monitor`. Implement queues and limit user numbers for performance. Consider upgrading your device for more resources.

## Verification and Testing Steps:

1.  **Verify Interface:**
    *   `ping 164.88.96.1` from a client device on that subnet. If it responds, basic interface is OK.
    *   Use `/ip address print` to verify the IP on the bridge.
2.  **Verify Users and Groups:**
    *   Use `/user print` to verify the new users are added and linked to the correct profiles and groups.
3.  **Verify Rate Limits:**
    *   From a client connected to the hotspot, perform speed tests. User1 should be limited to 1M/1M, and User2 to 10M/10M. Use an online speed test or iperf. Check the `address-list` in `ip firewall address-list` to see if the IP's of the connected users are correctly registered.
4.  **Verify Hotspot Functionality (If Implemented):**
    *   Connect a client to the hotspot, open a browser, check you are redirected to the hotspot login page.
    *   Login using user1 and user2 credentials.
    *   Monitor active hotspot users using `/ip hotspot active print`.
5. **Troubleshoot:**
  * Use the `/tool torch` command on the interface to see if the traffic is arriving correctly.

## Related Features and Considerations:

*   **RADIUS Authentication:** For larger setups, use RADIUS server for centralized user management.
*   **Hotspot Customization:** Customize the hotspot login page for branding.
*   **Queue Trees:** Implement queue trees for advanced bandwidth management per user or groups.
*   **Address Lists:** Use address lists to create different firewall rules or QoS depending on the connected user.
*   **User Manager:** Consider user manager for more advanced user management and voucher generation.
*   **DNS server:** Implement an internal or external DNS server to allow users to access the internet.

## MikroTik REST API Examples:

Here are REST API examples for user management:

*   **API Endpoint:** `/rest/system/user`

*   **Add User (POST):**

    ```json
    {
      "name": "api_user",
      "password": "api_password",
      "group": "basic",
      "profile": "basic-profile",
       "comment": "User created via API"
    }
    ```
    **Request:**
    ```bash
    curl -k -u admin:password -X POST -H "Content-Type: application/json" -d '{"name":"api_user","password":"api_password","group":"basic","profile":"basic-profile","comment":"User created via API"}' https://<router_ip>/rest/system/user
    ```
    **Expected Response (201 Created):**
    ```json
    {
      "id": "*11",
      "name": "api_user",
      "group": "*6",
      "profile": "*8",
       "comment": "User created via API"
    }
    ```
    **Error Example (400 Bad Request):**
    ```json
    {
     "error":"profile not found"
     }
    ```

*   **Get Users (GET):**

    ```bash
    curl -k -u admin:password https://<router_ip>/rest/system/user
    ```
    **Expected Response:**
    ```json
     [
       {
         "id": "*1",
         "name": "admin",
         "group": "*1",
          "disabled": false,
         "api-access": false
       },
       {
         "id": "*11",
         "name": "api_user",
         "group": "*6",
         "profile": "*8",
          "disabled": false,
         "api-access": false,
         "comment": "User created via API"
        }
    ]
    ```

*   **Delete User (DELETE):**

    ```bash
    curl -k -u admin:password -X DELETE https://<router_ip>/rest/system/user/*11
    ```
    **Expected Response (204 No Content):**
    No data in response.
    **Error Example (404 Not found):**
     ```json
    {
    "error":"not found"
     }
     ```

**REST API Notes:**

*   Replace `<router_ip>` with the IP address of your MikroTik router.
*   Use appropriate authentication credentials for the API.
*   ID returned when adding users should be used in API calls when modifying or deleting them.
*   Error handling should be done by checking for HTTP status codes.

## Security Best Practices:

*   **Strong Passwords:**  Use strong, unique passwords for all user accounts.
*   **RADIUS for AAA:** If possible, prefer RADIUS for authentication and accounting.
*   **Rate Limiting:** Implement rate limits to prevent individual users from saturating the network.
*   **Firewall Rules:** Use firewall rules to control traffic and prevent unauthorized access.
*   **Regular Audits:** Regularly audit user accounts and remove inactive or unnecessary users.
*   **Disable Unused Services:** Disable any services that are not needed on the router.
*   **Secure API:** If the API is accessible from the internet ensure to secure it via strong passwords, and firewall rules to limit its access.

## Self Critique and Improvements

*   **Improvement:** This configuration can be improved by adding more sophisticated queue trees to shape traffic for individual users.
*   **Improvement:** The configuration can be further enhanced by including rate limits per user profile and combining user authentication with other security measures.
*   **Improvement:** The configuration can be modified to use address lists with the firewall to give priority or different treatment to different user profiles.
*   **Further modification:** A more sophisticated configuration can implement several subnets and VLAN to better divide the network.

## Detailed Explanations of Topic:

*   **Users:**  Represent individual accounts that can access the network. Each user has a username and password for authentication.
*   **User Groups:**  Organize users with similar access requirements. This simplifies user management by applying group-based permissions and profiles.
*   **User Profiles:**  Define the parameters of the user connection, such as the rate limit and the address-list. This is where the bandwidth limits are set.
*   **Local Authentication:** Using the local database on the router to authenticate users.

## Detailed Explanation of Trade-offs:

*   **Local User Database vs. RADIUS:** Using the local user database is easy to implement and suitable for smaller networks, but it lacks centralized management. RADIUS is better for large-scale networks but is more complex to set up.
*   **Rate Limiting:** This is useful to make sure no single user can saturate the network. Using different profiles for different groups will make sure one user does not hinder the experience of others.
*   **Multiple user profiles:** Creates complexity, but it offers the benefit of different treatments for users.
*  **Hotspot vs local authentication:** Local authentication is easier to setup, but hotspot authentication allows for captive portals and customized login experiences.

## Configuration for Specific RouterOS Versions:

This documentation primarily targets RouterOS 7.11 but is also applicable to older versions, with minor syntax adjustments for older RouterOS versions, like the rate limit syntax. Older versions should support all features, just with potentially slightly different commands. Make sure to check the specific RouterOS documentation for the version in use.

This detailed guide should provide you with a robust and secure way to implement user and user group management in your MikroTik hotspot environment. Feel free to ask if you have further questions or want to refine specific aspects!
