Okay, let's craft some detailed technical documentation for managing users and user groups on a MikroTik RouterOS 7.12 device, specifically within the context of a Hotspot network using VLAN 64 (98.251.184.0/24).

## Scenario Description:

This document focuses on configuring user groups and users on a MikroTik router that is acting as a hotspot gateway for a network connected via VLAN 64. We aim to create different user groups with varying access policies, such as limited bandwidth, time quotas, and more. These policies are designed to control access and ensure fair usage of the network resources. This would be very common in public facing hot spot systems, such as coffee shops, hotels, or other similar scenarios.

## Implementation Steps:

Here's a step-by-step guide on how to set up user groups and users. We will provide the CLI commands alongside explanations for each step:

### Step 1: Configure the VLAN Interface (Assumed Already Created)

*   **Pre-Step State**: Assume that `vlan-64` is already configured in `/interface vlan` with a VLAN ID of 64 and the underlying interface.
*   **Action**: Verify the VLAN is properly configured and enabled. If not, create and enable it.
    *   **CLI Command:**
        ```mikrotik
        /interface vlan print
        /interface vlan enable vlan-64 # enable vlan, if needed
        /interface vlan monitor vlan-64
        ```
    *   **Winbox GUI**: Navigate to `Interfaces` > `VLAN`. Ensure `vlan-64` is present and enabled (check mark is in the enabled column). If the interface does not exist, click `+` to create one, select the appropriate parent interface, set the `VLAN ID` to `64` and then click `OK`.
    *   **Effect**: Ensure the VLAN is created and enabled, providing a dedicated logical interface for the Hotspot network.

### Step 2: Configure the IP Address for the VLAN Interface

*   **Pre-Step State**: No IP address is set for `vlan-64`.
*   **Action**: Assign an IP address from the 98.251.184.0/24 subnet to the `vlan-64` interface.
    *   **CLI Command:**
        ```mikrotik
        /ip address add address=98.251.184.1/24 interface=vlan-64
        /ip address print
        ```
    *   **Winbox GUI**: Navigate to `IP` > `Addresses`, click `+` to create a new address, enter `98.251.184.1/24` in the address field, select `vlan-64` from the interface drop down, click `OK`.
    *   **Effect**: The router can now communicate on the VLAN 64 network. The default gateway will be set on the upstream side of the network, and not on this interface.

### Step 3: Create User Groups

*   **Pre-Step State**: No user groups are defined.
*   **Action**: Create the user groups required.
    *   We'll define two groups: `free_users` and `premium_users`.
    *   **CLI Command**:
        ```mikrotik
        /user group add name=free_users
        /user group add name=premium_users
        /user group print
        ```
    *   **Winbox GUI**: Navigate to `Users` > `Groups`. Click `+` and add the two groups, `free_users` and `premium_users`. Click `OK` on each group creation.
    *   **Effect**: The groups are now created and can be referenced when adding users.

### Step 4: Configure User Group Profiles

*   **Pre-Step State**: No profiles are configured, and no limits are placed on the groups.
*   **Action**: Define access policies for the created groups.
    *   For `free_users`:
        *   Limit bandwidth to 1 Mbps up/down.
        *   Allow 1 hour of total use.
        *   Limit idle time to 5 minutes.
    *   For `premium_users`:
        *   Limit bandwidth to 10 Mbps up/down.
        *   Allow 10 hours of total use.
        *   Limit idle time to 30 minutes.
    *   **CLI Command**:
        ```mikrotik
        /ppp profile add name=free_profile local-address=98.251.184.1 remote-address=98.251.184.0/24  rate-limit=1M/1M  session-timeout=1h idle-timeout=5m
        /ppp profile add name=premium_profile local-address=98.251.184.1 remote-address=98.251.184.0/24 rate-limit=10M/10M  session-timeout=10h idle-timeout=30m
        /ppp profile print
        ```
        *   `local-address`: The local address to use for user profiles, will usually be the router IP, however you can specify a /32 or pool for additional complexity.
        *   `remote-address`: The address or pool the client will get, use `/24` to allow IPs from the subnet of the interface.
        *   `rate-limit`: Upload / Download limit for this profile.
        *   `session-timeout`: Maximum user login session length
        *   `idle-timeout`: Maximum time a user can be inactive before being disconnected.
    * **Winbox GUI**: Navigate to `PPP` > `Profiles`. Click `+` to create a profile. Add the following configurations.
        *   `name` to `free_profile`, `Local Address` `98.251.184.1` and `Remote Address` `98.251.184.0/24`. Click on the `Limits` tab and configure `Rate Limit (rx/tx)` to 1M/1M, `Session Timeout` to `1h` and `Idle Timeout` to `5m`.
        *   Click `OK` to save the profile, and repeat this process for a profile named `premium_profile`, `Local Address` `98.251.184.1` and `Remote Address` `98.251.184.0/24`, setting the values as: `Rate Limit (rx/tx)` to 10M/10M, `Session Timeout` to `10h` and `Idle Timeout` to `30m`.
    *   **Effect**: User profiles are now created with limits.

### Step 5: Create Users and Assign Them to Groups and Profiles

*   **Pre-Step State**: No users are defined.
*   **Action**: Create users and assign them to the correct groups with the correct profiles.
    *   Create `free_user1` (password `free123`) to `free_users` with `free_profile`, and `premium_user1` (password `premium123`) to `premium_users` with `premium_profile`.
    *   **CLI Command**:
        ```mikrotik
         /user add name=free_user1 password=free123 group=free_users profile=free_profile
         /user add name=premium_user1 password=premium123 group=premium_users profile=premium_profile
        /user print
        ```
        *   `name`: Username.
        *   `password`: Password.
        *   `group`: User Group.
        *   `profile`: PPP profile.
    *   **Winbox GUI**: Navigate to `Users`. Click `+` to create a new user.
        *   Enter `free_user1` in the `Name` field, `free123` as the `Password`, select `free_users` from the `Group` dropdown and `free_profile` from the `Profile` dropdown. Click `OK`.
        *   Click `+` again to create another user, name it `premium_user1`, with password `premium123`, group `premium_users` and profile `premium_profile`. Click `OK`.
    *   **Effect**: Users are now configured and are associated with their profiles for access.

### Step 6: Configure the Hotspot Server

*   **Pre-Step State**: No Hotspot server is created.
*   **Action**: create a Hotspot server, set authentication method, and assign profile for it to use.
    *   **CLI Command**:
        ```mikrotik
        /ip hotspot add name="hotspot1" interface=vlan-64 address-pool=none  profile=default
        /ip hotspot profile set "default" use-radius=no
        /ip hotspot user profile set "default"  keepalive-timeout=30s shared-users=1
        /ip hotspot print
        /ip hotspot user print
        /ip hotspot user profile print
        ```
        *   `name`: Hotspot server name.
        *   `interface`: VLAN interface.
        *   `address-pool`: Set to `none` as we use static addresses or DHCP in the local area network.
        *   `profile`: Set the hotspot to use the 'default' profile.
        *   `use-radius`: Set to `no` as we do not use Radius server authentication.
        *   `keepalive-timeout`: Set to `30s` for automatic logout if a client is not responding.
        *   `shared-users`: Allow just one user to log in per hotspot profile.
    *   **Winbox GUI**: Navigate to `IP` > `Hotspot`.
        *   In `Server`, click `+` and set the values: `Name` as `hotspot1`, `Interface` to `vlan-64` and `Address Pool` to `none`. Select the `default` `Profile`. Click `OK`
        *   Click the `Hotspot Profiles` tab, select `default` profile, click on the settings. Set `Use Radius` to `no` and click on the `General` tab, set `Keepalive Timeout` to `30s`, and `Shared Users` to `1`. Click `OK`.
    *   **Effect**: Hotspot server is configured and ready to authenticate users.

## Complete Configuration Commands:

```mikrotik
/interface vlan
add interface=ether1 name=vlan-64 vlan-id=64
/interface vlan enable vlan-64
/ip address
add address=98.251.184.1/24 interface=vlan-64
/user group
add name=free_users
add name=premium_users
/ppp profile
add name=free_profile local-address=98.251.184.1 remote-address=98.251.184.0/24  rate-limit=1M/1M  session-timeout=1h idle-timeout=5m
add name=premium_profile local-address=98.251.184.1 remote-address=98.251.184.0/24 rate-limit=10M/10M  session-timeout=10h idle-timeout=30m
/user
add group=free_users name=free_user1 password=free123 profile=free_profile
add group=premium_users name=premium_user1 password=premium123 profile=premium_profile
/ip hotspot
add address-pool=none interface=vlan-64 name=hotspot1 profile=default
/ip hotspot profile set "default" use-radius=no
/ip hotspot user profile set "default"  keepalive-timeout=30s shared-users=1
```

## Common Pitfalls and Solutions:

1.  **Incorrect VLAN ID:** Ensure the VLAN ID in `/interface vlan` matches the ID configured on the switch. *Solution*: Verify your switch configuration.
2.  **IP Address Conflicts:** The router's IP address must be unique. *Solution*: Check for IP conflicts using `/ip address print`. Ensure that other devices on the same network do not use the same IP.
3.  **Incorrect Rate Limits:** Ensure your rate limits are set correctly, and are appropriate to your available internet bandwidth. *Solution*: Recheck the profiles in `/ppp profile print` and match this to your service levels.
4.  **Authentication Issues:** If users cannot log in, check the user profiles and their passwords using `/user print`. *Solution*: Verify that both are set correctly, or attempt a login using the admin account to confirm the hot spot is functioning.
5.  **Idle Timeout Issues:** Users disconnected unexpectedly can be due to a very short idle timeout. *Solution*: Adjust idle timeout as needed in `/ppp profile` using `idle-timeout`.
6.  **Hotspot Configuration:** Ensure that the Hotspot server is enabled, and the profile is set. *Solution*: use `/ip hotspot print` to verify the configurations, and set the profile to `default` using `/ip hotspot set name="hotspot1" profile=default`
7. **Resource Usage:** High CPU or memory can impact performance when many users are connected. *Solution*: Monitor the system resources using `/system resource print`. If you have high CPU usage, ensure the log verbosity is not set too high, which is a very common issue. If your system is too stressed, consider upgrading to a more powerful router.

## Verification and Testing Steps:

1.  **Ping Test:** From a client connected to the VLAN, ping the router's IP (`98.251.184.1`). If you can get a reply, then network connectivity is fine.
    ```mikrotik
    /ping 98.251.184.1
    ```
2.  **Hotspot Login:** Connect to the WiFi (or wired) network associated with the Hotspot. Try logging in with both `free_user1` and `premium_user1` and verifying that the speeds are as expected.
    *   Use web browser to connect to any web address, the hotspot server will present its login page. Login with the correct credentials.
3.  **Active Connections:** Check active Hotspot users using `/ip hotspot active print`.
    *   Verify the assigned user and profile information.
4.  **Torch Tool:** Use `/tool torch` to monitor the traffic on the vlan interface and ensure traffic is flowing as expected.
    *   Filter for source and destination ports to narrow down the data set.
5.  **Interface Monitoring:** Monitor interface traffic using `/interface monitor vlan-64`.
    *   Verify RX/TX speeds are within the configured limits.

## Related Features and Considerations:

*   **Radius Server:** Use RADIUS for centralized user management and accounting.
*   **User Manager:** Use the MikroTik User Manager package for more advanced user management.
*   **Walled Garden:** Allow specific websites or services without login.
*   **IP Binding:** Allow specific devices bypass the login page by using IP binding on the Hotspot server.
*   **Transparent Proxy:** Cache frequently requested content, reducing latency and bandwidth consumption.

## MikroTik REST API Examples (if applicable):

*For RouterOS 7.x+, the API is at `https://<router-ip>/rest`. The username/password used is a valid user account on the device.*

### Example 1: Create a New User

*   **Endpoint:** `/user`
*   **Method:** `POST`
*   **JSON Payload:**

    ```json
    {
        "name": "testuser",
        "password": "testpassword",
        "group": "free_users",
        "profile": "free_profile"
    }
    ```

*   **Example curl Command:**

    ```bash
    curl -k -u <username>:<password> -H "Content-Type: application/json" -X POST -d '{
    "name": "testuser",
    "password": "testpassword",
    "group": "free_users",
    "profile": "free_profile"
    }'  https://<router-ip>/rest/user
    ```
*   **Expected Response (200 OK):**

    ```json
    {
        "id": "*12",
        "name": "testuser",
        "group": "free_users",
        "profile": "free_profile",
        "disabled": false
    }
    ```
*   **Error Handling:**
    *   A response of `401 Unauthorized` indicates incorrect credentials.
    *   A `400 Bad Request` indicates an issue with the request, such as missing parameters or incorrect values.

### Example 2: Get All Users

*   **Endpoint:** `/user`
*   **Method:** `GET`

*   **Example curl Command:**

    ```bash
    curl -k -u <username>:<password> https://<router-ip>/rest/user
    ```
*   **Expected Response (200 OK):**

    ```json
    [
    {
      "id": "*12",
      "name": "admin",
      "group": "*0",
      "profile": "default",
      "disabled": false
    },
    {
      "id": "*13",
      "name": "free_user1",
      "group": "free_users",
      "profile": "free_profile",
      "disabled": false
    },
    {
        "id": "*14",
        "name": "premium_user1",
        "group": "premium_users",
        "profile": "premium_profile",
        "disabled": false
      }
    ]
    ```
*   **Error Handling:**
    *   A response of `401 Unauthorized` indicates incorrect credentials.

## Security Best Practices:

1.  **Strong Passwords:** Use strong, unique passwords for user accounts.
2.  **Regular Audits:** Periodically review user accounts and groups.
3.  **Disable Default Accounts:** Disable or change the default `admin` account.
4.  **HTTPS for API:** Always use HTTPS when accessing the RouterOS API.
5.  **Firewall Rules:**  Implement strong firewall rules to limit access to the router itself.
6. **Limit Logins:** Limit the amount of login attempts from a given IP address. Use `/system login` settings.
7.  **Stay Updated:** Ensure your RouterOS is updated to the latest stable version.

## Self Critique and Improvements

This configuration provides a solid foundation for user and group management within a Hotspot setup. However, several improvements could be made:

1.  **Scalability:** As the number of users grows, consider implementing a Radius server for centralized management.
2.  **Dynamic Address Pools:** Rather than fixed IP addresses, explore dynamic address pools using DHCP with the hotspot server. This will be especially useful in larger network installations.
3.  **Customization:** The login page for the Hotspot can be customized.
4.  **Advanced Reporting:** Implement a reporting system to monitor user activity and consumption.
5.  **Multi-factor Authentication:** Add MFA to protect accounts with a higher level of access.

## Detailed Explanations of Topic

**User Management:** MikroTik's user management is handled under `/user`. Users are configured with names, passwords, group assignments, and profiles that determine their access privileges and resource limitations. This is the primary system for authentication.

**User Groups:** User groups allow the logical grouping of users. By assigning a user to a specific group, you can streamline management, and implement policies that apply to the group rather than an individual.

**PPP Profiles:** PPP profiles, configured using `/ppp profile`,  are a key element in controlling user access. These profiles define crucial parameters like rate limits (bandwidth), session timeouts, and idle timeouts. These profiles are attached to individual users for traffic shaping and control purposes.

## Detailed Explanation of Trade-offs

1.  **Simple User Management vs. Radius:** Simple MikroTik user management is easier to set up initially, but is not practical for larger networks with hundreds or thousands of users. RADIUS provides centralized user management, scalability, and accounting but requires a more complex setup.
2.  **Direct IP Assignment vs DHCP:** The use of a static IP address has some advantages, and gives the network administrator more control of the system, but DHCP is preferred in larger installations. DHCP is simpler to manage and configure.
3.  **Basic User Groups vs Advanced User Manager:** Basic user groups are easier to setup initially. They can only control basic parameters. However, the MikroTik User Manager provides advanced features like user templates, voucher generation, and payment integrations but requires more time and effort to configure.
4.  **Bandwidth Limits vs no Bandwidth limits:** Limiting bandwidth ensures equitable resource distribution and prevents individual users from hogging all the resources. It can be complex and time consuming to configure and to make sure the system functions as desired. Not setting any limit can be simpler, however it leads to inconsistent behavior and can allow some users to negatively impact the network.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 7.12, however the core concepts are valid for 6.48 and all versions of RouterOS 7.x. All the commands included are valid on both 6.48 and 7.12 versions. Some commands, such as the user api, are very different on RouterOS6 and 7, so the examples provided here are exclusively valid on version 7.

This comprehensive documentation covers the initial configuration as well as the advanced topics that are required for an enterprise grade implementation of a hot spot network. It includes very specific examples and detailed command explanations.
