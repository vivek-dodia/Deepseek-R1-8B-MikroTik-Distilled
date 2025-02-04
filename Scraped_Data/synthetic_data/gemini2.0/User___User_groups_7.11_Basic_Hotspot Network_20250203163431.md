Okay, let's craft a comprehensive technical document for managing users and user groups on a MikroTik router running RouterOS 7.11, within a hotspot network context.

## Scenario Description:

This configuration focuses on managing user access within a hotspot environment, utilizing MikroTik's user management features. Specifically, we will:

*   Create user groups with different access privileges.
*   Assign users to these groups.
*   Implement basic user management for authentication in a hotspot setup, potentially for limited time or data access.
*   This configuration will utilize `ether-37` as the interface facing the hotspot clients and a subnet of `214.168.249.0/24`.

## Implementation Steps:

Here's a step-by-step guide with explanations, CLI examples, and Winbox GUI instructions where applicable.

**1. Step 1: Verify Initial Configuration and Identify Interface**

*   **Explanation:** Before any modifications, it's crucial to know the existing setup.  We need to confirm our target interface `ether-37` exists and has no existing configuration related to hotspot or IP addressing within our target subnet.
*   **Before Configuration:**
    ```mikrotik
    /interface print
    /ip address print
    ```
*   **Expected Output (Example):**
    ```
    # INTERFACE                                  TYPE      MTU    L2 MTU    MAX-L2 MTU MAC-ADDRESS       
     0 ether1                                    ether    1500      1598    1598    00:00:5E:00:53:01
     1 ether2                                    ether    1500      1598    1598    00:00:5E:00:53:02
     2 ether3                                    ether    1500      1598    1598    00:00:5E:00:53:03
    ...
     37 ether-37                                  ether    1500      1598    1598    00:00:5E:00:53:25
    ...

    #   ADDRESS          NETWORK         INTERFACE          ACTUAL-INTERFACE
    0 192.168.88.1/24    192.168.88.0    ether1             ether1
    ```
    _Note:_ `ether-37` should be in the list, and we expect it to not have any addresses in our target subnet `214.168.249.0/24`

*   **Winbox:** Navigate to `Interfaces` to verify the existence of the interface. Then go to `IP -> Addresses` to verify there is no address configuration for `214.168.249.0/24`.
*   **Action:** We now know that the interface is available and is safe to use.

**2. Step 2: Configure IP Address on Interface**

*   **Explanation:** Assign an IP address to the interface. This is the gateway address for the subnet and will act as the IP of the hotspot.
*   **Command:**
    ```mikrotik
    /ip address add address=214.168.249.1/24 interface=ether-37 network=214.168.249.0
    ```
*   **Winbox:** Navigate to `IP` > `Addresses`, click the `+` button, and fill in `Address: 214.168.249.1/24`, `Interface: ether-37`, `Network: 214.168.249.0`, then click `Apply`, then `OK`.
*   **After Configuration:**
    ```mikrotik
    /ip address print
    ```
*   **Expected Output:**
    ```
    #   ADDRESS          NETWORK         INTERFACE          ACTUAL-INTERFACE
    0 192.168.88.1/24    192.168.88.0    ether1             ether1
    1 214.168.249.1/24    214.168.249.0    ether-37         ether-37
    ```

**3. Step 3: Create User Groups**

*   **Explanation:** Create two user groups: `premium` and `standard`. We will not be setting up any custom profile policies here.
*   **Commands:**
    ```mikrotik
    /user group add name=premium
    /user group add name=standard
    ```
*   **Winbox:** `System > Users > User Groups` click the `+` button, fill in `Name: premium` or `Name: standard`, then click `Apply` then `OK`.
*   **After Configuration:**
    ```mikrotik
    /user group print
    ```
*   **Expected Output:**
    ```
    #   NAME      POLICY      
    0 premium   
    1 standard  
    ```

**4. Step 4: Add Users**

*   **Explanation:** Create users and assign them to the created groups.
*   **Commands:**
    ```mikrotik
    /user add name=user1 password=password1 group=premium
    /user add name=user2 password=password2 group=standard
    /user add name=user3 password=password3 group=premium
    ```
*   **Winbox:** `System > Users` click the `+` button, fill in `Name: user1`, `Password: password1`, click on the `Group` dropdown menu, select `premium`, then click `Apply` then `OK`. Repeat this for the other two users.
*   **After Configuration:**
    ```mikrotik
    /user print
    ```
*   **Expected Output:**
    ```
    #   NAME      GROUP    DISABLED    COMMENT  
    0 user1     premium  no        
    1 user2     standard no        
    2 user3     premium   no        
    ```
*   **Action:** User groups and users are now created.

**5. Step 5: Verify DHCP Server is setup (if needed)**

* **Explanation:** You can configure a DHCP Server on your MikroTik router if your hotspot clients need IP addresses. In a basic hotspot configuration, clients connect to the hotspot wifi and are then redirected to a login page to authenticate. In this scenario, the DHCP server is assigned to the interface `ether-37`
* **Command:**
    ```mikrotik
    /ip dhcp-server add address-pool=default disabled=no interface=ether-37 name=dhcp1
    /ip pool add name=dhcp_pool ranges=214.168.249.10-214.168.249.250
    /ip dhcp-server network add address=214.168.249.0/24 dns-server=8.8.8.8 gateway=214.168.249.1
    ```
*   **Winbox:**
    * Go to `IP` -> `DHCP Server`.
    * Click the `+` button, Set `Name` to `dhcp1`, `Interface` to `ether-37`. Leave all other settings as default. Then click `Apply` then `OK`.
    * Go to `IP` -> `Pool`.
    * Click the `+` button, set `Name` to `dhcp_pool`, `Ranges` to `214.168.249.10-214.168.249.250`, then click `Apply` then `OK`.
    * Go to `IP` -> `DHCP Server` and click `Networks`.
    * Click the `+` button, set `Address` to `214.168.249.0/24`, `Gateway` to `214.168.249.1`, `DNS Servers` to `8.8.8.8`. Click `Apply` then `OK`.
* **After Configuration:**
    ```mikrotik
    /ip dhcp-server print
    /ip pool print
    /ip dhcp-server network print
    ```
* **Expected Output:**
    ```
    #   NAME     INTERFACE     LEASE-TIME ADD-ARP ADDRESS-POOL  DISABLED
    0 dhcp1    ether-37      3d        yes     default          no

    #  NAME     RANGES                                                              
    0 dhcp_pool  214.168.249.10-214.168.249.250
    
    #   ADDRESS         DNS-SERVER    GATEWAY         
    0 214.168.249.0/24   8.8.8.8      214.168.249.1
    ```

## Complete Configuration Commands:

```mikrotik
/ip address
add address=214.168.249.1/24 interface=ether-37 network=214.168.249.0

/user group
add name=premium
add name=standard

/user
add name=user1 password=password1 group=premium
add name=user2 password=password2 group=standard
add name=user3 password=password3 group=premium

/ip dhcp-server
add address-pool=default disabled=no interface=ether-37 name=dhcp1
/ip pool
add name=dhcp_pool ranges=214.168.249.10-214.168.249.250
/ip dhcp-server network
add address=214.168.249.0/24 dns-server=8.8.8.8 gateway=214.168.249.1
```

*   **/ip address add**: Adds an IP address to the specified interface.
    *   `address`: The IP address and subnet mask in CIDR notation (e.g., 214.168.249.1/24).
    *   `interface`: The name of the interface where the address will be applied (e.g., ether-37).
    *   `network`: Network address of subnet this IP address is in.
*   **/user group add**: Adds a new user group.
    *   `name`: The name of the user group.
*   **/user add**: Adds a new user.
    *   `name`: The username.
    *   `password`: The user's password.
    *   `group`: The group to which the user belongs.
*   `/ip dhcp-server add`: Adds a new DHCP server
    *  `address-pool`: Which pool to use
    *  `disabled`: Whether the server is disabled or not
    *  `interface`: Interface where the DHCP server is bound to
    *  `name`: The name of the DHCP server
*   `/ip pool add`: Adds a new IP pool
    *  `name`: The name of the pool
    *  `ranges`: The IP range which will be used by the pool
*   `/ip dhcp-server network add`
    *  `address`: The network address of the DHCP server
    *  `dns-server`: The DNS server to be used
    * `gateway`: The IP address of the gateway.

## Common Pitfalls and Solutions:

*   **Pitfall:** Interface not recognized.
    *   **Solution:** Double-check the interface name. It is case-sensitive.
*   **Pitfall:** IP address conflicts or incorrect subnet mask.
    *   **Solution:** Ensure the IP is not already in use, and the subnet mask matches the intended network.
*   **Pitfall:** Users unable to connect or authenticate.
    *   **Solution:** Verify the user credentials, check the user group configuration, and ensure hotspot settings are correctly configured (not covered here but necessary for complete functionality).
*  **Pitfall:** DHCP Server issues, clients cannot obtain an IP address.
    * **Solution:** Verify the DHCP server is not disabled, and that the ranges are correct, and there is a DHCP network configured. Also ensure the gateway IP address is correct for your subnet.
*   **Security Pitfall:** Basic passwords.
    *   **Solution:** Implement strong password policies for production environments.
*   **Security Pitfall:** Lack of password complexity
    * **Solution:** Add policies to prevent commonly used passwords.
*   **Performance Pitfall:** Large user base with many concurrent connections can lead to high CPU usage if no other restrictions are configured, for example, profile limitations.
    *   **Solution:** Properly manage user connections with custom profiles that limit data or uptime.

## Verification and Testing Steps:

1.  **Check Interface IP Address:**
    ```mikrotik
    /ip address print where interface=ether-37
    ```
    *   Verify that the output shows the correct IP address (`214.168.249.1/24`).
2.  **Check User Groups:**
    ```mikrotik
    /user group print
    ```
    *   Confirm that "premium" and "standard" groups exist.
3.  **Check Users:**
    ```mikrotik
    /user print
    ```
    *   Verify that `user1`, `user2`, and `user3` exist and are assigned to the correct groups.
4. **Check DHCP Server:**
    ```mikrotik
    /ip dhcp-server print
    /ip pool print
    /ip dhcp-server network print
    ```
    * Verify the settings match the expected configuration.
5.  **Connect a client to the network:**
    * Connect a test device to the network through the `ether-37` interface. Make sure the client gets an IP in the range configured in the DHCP pool.
6.  **Ping the router's IP:** From the connected test client, ping the gateway address:
    ```
    ping 214.168.249.1
    ```

## Related Features and Considerations:

*   **Hotspot Server:**  This configuration is a prerequisite for a fully functional hotspot. Setting up the hotspot server is necessary for user authentication. This will require additional configurations in `/ip hotspot`.
*   **User Profiles:** You can create profiles to limit bandwidth, uptime, and other parameters for different user groups. This can be configured in `/ppp profile`.
*   **RADIUS Server:** For more complex setups, RADIUS servers can be used for centralized user authentication.
*   **User Manager:** MikroTik's User Manager is useful for managing large numbers of users and for ticket-based access. This has been deprecated and should not be used.
*   **Firewall Rules:** Implement firewall rules to restrict or allow traffic based on user groups (e.g. limited access for 'standard' users.)

## MikroTik REST API Examples:

These examples assume that the API interface is enabled and reachable.

**1. Create a User Group**

*   **API Endpoint:** `/user/group`
*   **Request Method:** POST
*   **Example JSON Payload:**
    ```json
    {
        "name": "new_group"
    }
    ```
*   **Expected Response (Success):**
    ```json
    {
        "message": "added"
    }
    ```
*   **Error Handling Example:**
    ```json
    {
      "error": "already exists"
    }
    ```
*   **Description of Parameters:**
    *   `name`:  The name of the new user group.

**2. Create a User**

*   **API Endpoint:** `/user`
*   **Request Method:** POST
*   **Example JSON Payload:**
    ```json
    {
        "name": "new_user",
        "password": "new_password",
        "group": "new_group"
    }
    ```
*   **Expected Response (Success):**
    ```json
    {
      "message": "added"
    }
    ```
*   **Error Handling Example:**
    ```json
    {
      "error": "already exists"
    }
    ```
*   **Description of Parameters:**
    *   `name`: The username.
    *   `password`: The user's password.
    *   `group`: The group to which the user belongs.

**3. Get User list**

*   **API Endpoint:** `/user`
*   **Request Method:** GET
*   **Example Response (Success):**
    ```json
     [
            {
                ".id": "*0",
                "name": "user1",
                "group": "premium",
                "disabled": "false",
                "comment": ""
            },
            {
                ".id": "*1",
                "name": "user2",
                "group": "standard",
                "disabled": "false",
                "comment": ""
            },
            {
                ".id": "*2",
                "name": "user3",
                "group": "premium",
                "disabled": "false",
                "comment": ""
            }
    ]
    ```
*   **Description of Parameters:**
    *   No parameters are required in the request. The response will contain all users configured.

## Security Best Practices:

*   **Strong Passwords:** Enforce strong password policies.
*   **HTTPS for API:** Always use HTTPS for accessing the REST API.
*   **Limit API Access:** Restrict API access to authorized IP addresses only.
*   **Regular Audits:** Regularly audit user accounts and their access permissions.
*   **Firewall Rules:** Use firewall rules to limit access to the hotspot and the router from unauthorized sources.
*  **Monitor Resources:** Monitor the system resources in the router to prevent unexpected high usage scenarios.

## Self Critique and Improvements:

This configuration provides a basic setup. Some improvements include:

*   **User Profiles:** Implementing user profiles with different data and time limitations.
*   **Hotspot Configuration:** This is needed for users to be able to log in and access the internet.
*   **RADIUS Integration:** For more complex setups, using a RADIUS server is essential.
*  **More Sophisticated API:** Using a more sophisticated API setup to retrieve users by filters.
*   **Detailed Logging:** Implementing more detailed logging and monitoring of user authentication.

## Detailed Explanations of Topic

*   **Users:** In MikroTik RouterOS, users are accounts that can be used for authentication to access various services, including hotspot, SSH, and winbox. Users are defined with a username, password, and can be associated with a specific user group. Users are the basis of restricting access to various router features.
*   **User Groups:** User groups allow you to categorize users and assign access policies collectively. This makes managing a large number of users easier. Different groups can have different limitations or settings. Groups can be very granular, and they are necessary for a properly structured network access structure.

## Detailed Explanation of Trade-offs

*   **Local User Database vs. RADIUS:** A local user database, as used in this example, is simpler to set up for smaller networks. However, RADIUS provides centralized user management for larger setups, which is easier to scale and is very flexible.
*   **Simple Grouping vs. Detailed Profiles:** Simple groups offer a very basic level of restriction. Detailed profiles in `/ppp profile` offer granular control over bandwidth, uptime, and other parameters.  The choice depends on the complexity of your desired access policies.
*   **Plaintext Passwords vs. Hashing:** In our basic example, the passwords are saved as a hash. Plaintext passwords are not recommended due to the security risks. Always use at least hashing or preferably a RADIUS server.

## Configuration for Specific RouterOS Versions:

* This configuration is fully compatible with RouterOS 7.11, and it's also compatible with 7.x and most 6.48 installations. The commands provided are supported by these versions. If you are using an older version of RouterOS, please make sure the `/ip dhcp-server` configuration is available and adjust as needed. The `/ip dhcp-server network` syntax in the example was introduced in RouterOS 7.x, it should be reviewed for compatibility with older versions.

This thorough documentation should enable you to understand and implement basic user and user group management in your MikroTik hotspot environment. Remember to adjust and secure these configurations based on your specific requirements.
