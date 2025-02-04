Okay, let's craft a comprehensive guide to PPP AAA using MikroTik RouterOS, focusing on the 6.48 and 7.x versions. We'll aim for an "Advanced" level configuration suitable for an enterprise environment.

## Scenario Description:

This scenario involves setting up a Point-to-Point Protocol (PPP) server on a MikroTik router. The router will authenticate connecting clients using a RADIUS server for AAA (Authentication, Authorization, and Accounting). This provides centralized user management and access control for PPP connections. We will be using the subnet 85.152.190.0/24 for assigning IP addresses to the PPP clients and the physical interface `ether-64` will act as our external facing interface.

## Implementation Steps:

Here’s a step-by-step guide to configure this scenario:

**1. Step 1: Configure the RADIUS Server Settings**

*   **Action:** Configure the router to communicate with the RADIUS server. This involves specifying the server's IP address, secret, and port.
*   **Why:** Without this, the router won't be able to authenticate users against the RADIUS database.
*   **Before Configuration:**
    *   No RADIUS configuration exists on the router.
*   **CLI Example:**

    ```mikrotik
    /radius
    add address=192.168.10.10 secret=MyRadiusSecret service=ppp timeout=30s
    ```

    *  `add` : Adds a new RADIUS server entry
    *  `address`: The IP address of the RADIUS server. In this case it's `192.168.10.10`.
    *  `secret`: The shared secret key used to authenticate the router with the RADIUS server. This is a critical value and should be treated as a password. Here, it's set to `MyRadiusSecret`.
    *  `service`: Specifies the services using this radius server. `ppp` in this case, so this radius server will only be used for ppp connections.
    * `timeout`: Sets the timeout for communication with the radius server in seconds. In this case set to `30s`.
*   **Winbox Example:**
    * Go to `Radius` menu.
    * Click on `+` to add a new server.
    * Enter the address, shared secret, service, and timeout.
    * Click `Apply` or `OK`.
*   **After Configuration:**
    * The router will now have the RADIUS server configured, ready to be used for authentication.
*   **Effect:** This step ensures the MikroTik router can communicate with the RADIUS server for authentication, authorization, and accounting purposes.

**2. Step 2: Create a PPP Profile for RADIUS Authentication**

*   **Action:** Create a PPP profile that specifies RADIUS as the authentication method and configures IP addressing for clients.
*   **Why:** The PPP profile dictates how PPP connections will be handled, including what methods to use for authentication and what IP settings are given to the connecting client.
*   **Before Configuration:**
    *   No PPP profile specifically for RADIUS exists.
*   **CLI Example:**

    ```mikrotik
    /ppp profile
    add name=radius-ppp use-encryption=yes local-address=85.152.190.1 remote-address=85.152.190.2-85.152.190.254 only-one=yes dns-server=8.8.8.8,8.8.4.4
    set radius-ppp authentication=pap,chap,mschap1,mschap2
    set radius-ppp change-tcp-mss=yes
    ```
    * `add`: Adds a new PPP profile.
    *  `name`: Sets the name of the PPP profile, here it's set to `radius-ppp`.
    * `use-encryption`: Sets whether encryption is required on the connection. Here it's set to `yes`.
    *  `local-address`: The IP address of the MikroTik router on the PPP interface, set to `85.152.190.1`.
    *  `remote-address`: The IP range that will be assigned to connecting clients, it is set from `85.152.190.2` to `85.152.190.254`.
    * `only-one`: Allows only one connection with this profile for a user, set to `yes`.
    *  `dns-server`: The DNS servers that will be assigned to clients. Set to Google's public DNS servers here.
    *  `authentication`: Sets which authentication methods are used.
    * `change-tcp-mss`: Forces tcp-mss clamping on the ppp connection.
*   **Winbox Example:**
    * Go to the `PPP` menu and then the `Profiles` tab.
    * Click on `+` to add a new profile.
    * Enter the profile name (`radius-ppp`).
    * Configure the `Local Address`, `Remote Address`, `DNS Servers` and select the required `authentication` options.
    * Enable `Use Encryption` and `Only One`.
    * Click `Apply` or `OK`.
*   **After Configuration:**
    * A new PPP profile, `radius-ppp`, is created that’s ready to be used for PPP connections with RADIUS authentication.
*   **Effect:** This step defines the parameters for PPP connections that will be authenticated via RADIUS.

**3. Step 3: Create a PPP Secret using the `radius` service.**

*   **Action:** Create a new secret with `service=radius` in the ppp secrets tab.
*   **Why:** This tells the router to use radius for authentication of this user/service.
*   **Before Configuration:**
    *   No secrets that use `radius` service.
*   **CLI Example:**

    ```mikrotik
    /ppp secret
    add name="my-user-radius" profile=radius-ppp service=radius
    ```

    *   `add`: adds a new PPP secret entry.
    *   `name`: The username for the user which will connect via PPP. Set to `my-user-radius`.
    *   `profile`: The ppp profile to use for this service, set to `radius-ppp`
    *   `service`: Sets which service type this entry is for. Set to `radius`.
*   **Winbox Example:**
    * Go to the `PPP` menu and then the `Secrets` tab.
    * Click on `+` to add a new secret.
    * Enter the username, select `radius` from the service drop-down, and set the correct profile.
    * Click `Apply` or `OK`.
*   **After Configuration:**
    *   A PPP secret is added using `radius` service which lets the router know to authenticate this user using RADIUS.
*   **Effect:** This ensures the router checks with the RADIUS server before authenticating the user.

**4. Step 4: Enable the PPP Server**

*   **Action:** Enable a PPP server that will listen for incoming PPP connections.
*   **Why:** The PPP server is responsible for establishing PPP connections when a client connects.
*   **Before Configuration:**
    *   No PPP server is active.
*   **CLI Example:**
    ```mikrotik
    /interface ppp server
    add name=ppp-server-ether64 interface=ether-64 profile=radius-ppp enabled=yes
    ```
    *   `add`: Creates a new PPP server instance.
    *   `name`: Sets the server's name. It's `ppp-server-ether64` here.
    *   `interface`: Specifies which interface the server listens on, here it is `ether-64`.
    *   `profile`: The PPP profile to use for the connection, set to `radius-ppp`.
    *   `enabled`: Enables the PPP server, setting to `yes` means the server is active.
*   **Winbox Example:**
    * Go to the `PPP` menu and then the `Interface` tab.
    * Click on `+` to add a new server.
    * Choose the `PPP Server` option.
    * Give it a name `ppp-server-ether64`.
    * Choose the interface from the `Interface` dropdown (`ether-64`).
    * Choose the `radius-ppp` from the `profile` dropdown.
    * Ensure `Enabled` is ticked.
    * Click `Apply` or `OK`.
*   **After Configuration:**
    *   The PPP server is now active, listening on the specified interface.
*   **Effect:** Allows clients to connect via PPP.

**5. Step 5 (Optional): Firewall Rules**

*   **Action:** Set firewall rules to control the traffic in and out of the PPP interface.
*   **Why:** Firewall rules enhance security by controlling access to resources.
*   **Before Configuration:**
    * The existing firewall might not be set up for the new ppp connections.
*   **CLI Example:**
    ```mikrotik
    /ip firewall filter
    add chain=forward action=accept in-interface=ppp-server-ether64
    add chain=forward action=accept out-interface=ppp-server-ether64
    ```
* `add`: Adds a new rule to the `filter` section in the `firewall` menu.
*  `chain`: sets the chain of the rule. `forward` in this case because we want to forward traffic from our ppp clients.
* `action`: sets the action of the rule to `accept`, which will allow the traffic.
* `in-interface`: specifies the incoming interface of the rule. `ppp-server-ether64` in this case.
* `out-interface`: specifies the outgoing interface of the rule. `ppp-server-ether64` in this case.

*   **Winbox Example:**
   * Go to the `IP` menu, then the `Firewall` option, and then the `Filter Rules` tab.
   * Add a new rule with `chain=forward`, `in interface=ppp-server-ether64` and `action=accept`.
   * Add another rule with `chain=forward`, `out interface=ppp-server-ether64` and `action=accept`.
*   **After Configuration:**
    *   Firewall rules are configured, allowing traffic to be routed through the PPP interface.
*   **Effect:** This ensures that clients connected via PPP can properly use the network.

## Complete Configuration Commands:

```mikrotik
/radius
add address=192.168.10.10 secret=MyRadiusSecret service=ppp timeout=30s

/ppp profile
add name=radius-ppp use-encryption=yes local-address=85.152.190.1 remote-address=85.152.190.2-85.152.190.254 only-one=yes dns-server=8.8.8.8,8.8.4.4
set radius-ppp authentication=pap,chap,mschap1,mschap2
set radius-ppp change-tcp-mss=yes

/ppp secret
add name="my-user-radius" profile=radius-ppp service=radius

/interface ppp server
add name=ppp-server-ether64 interface=ether-64 profile=radius-ppp enabled=yes

/ip firewall filter
add chain=forward action=accept in-interface=ppp-server-ether64
add chain=forward action=accept out-interface=ppp-server-ether64
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Connectivity Issues:**
    *   **Problem:** Router can't communicate with the RADIUS server.
    *   **Solution:** Verify the RADIUS server's IP address, shared secret, and port are correct. Check firewalls on both devices, and make sure UDP port 1812 or 1813 is open.
    *   **MikroTik Debugging:** Use `/tool sniffer` to capture packets between the router and the RADIUS server. Look for RADIUS Access-Request and Access-Accept messages.
*   **Incorrect Secret/Profile Association:**
    *   **Problem:** Clients can't authenticate or don't get assigned an IP.
    *   **Solution:** Ensure the PPP secret's service is set to `radius` and correct the profile if you added a profile name to the secret. Verify the user exists in the RADIUS server's user database with the correct password.
    *   **MikroTik Debugging:** Check the logs using `/log print` to see any authentication errors.
*   **Firewall Blocking PPP Traffic:**
    *   **Problem:** Clients can connect, but can't access the network.
    *   **Solution:** Ensure that firewall rules allow forward traffic on the PPP interface. Double check any other firewall rules that could be blocking the traffic.
    *   **MikroTik Debugging:** Use `/tool torch` to monitor traffic flow and identify where the packet drop happens.
*   **Mismatched Authentication Methods:**
    *   **Problem:** RADIUS server and MikroTik router do not agree on authentication protocol.
    *   **Solution:** Verify the authentication methods on both router and server are the same.
*   **MTU Issues:**
    *   **Problem:** Clients may experience issues with large packets being dropped, leading to slow or no connectivity.
    *   **Solution:** Ensure the TCP MSS on the profile is enabled.

## Verification and Testing Steps:

1.  **Check RADIUS Connectivity:**
    *   Use `/tool fetch url="http://192.168.10.10/"` to see if you can get to the RADIUS server, it can be any address that exists on the server, which helps you test connectivity.
    *   Use `/ping 192.168.10.10` to verify basic IP connectivity to the radius server.
2.  **Attempt a PPP Connection:**
    *   Connect to the PPP server using a PPP client (e.g., built-in PPP client on Windows, macOS or Linux).
    *   Check for authentication prompts. Verify user/password in the RADIUS server are correct.
3.  **Verify IP Assignment:**
    *   After a successful connection, check that the client receives an IP address from the configured range (85.152.190.2-85.152.190.254).
    *   Use `/ip address print` on the router and also check the client's IP.
4.  **Check Connectivity Through the PPP Interface:**
    *   On the client, try pinging a device on the network or an external website.
    *   Use `/ping` from the Mikrotik terminal and try a ping the same place from the client.
5.  **Monitor Traffic:**
    *   Use `/tool torch interface=ppp-server-ether64` to monitor traffic.
    *   Use the Torch on `ether-64` interface and compare it against the PPP interface to see how traffic flows.
6.  **Monitor Logs:**
    *   Use `/log print` to monitor log entries, particularly for RADIUS related messages or authentication errors.
    *  Add `/log add topics=radius` to make sure all radius related messages are logged.

## Related Features and Considerations:

*   **Dynamic RADIUS Authorization:**
    *   RADIUS can dynamically authorize users based on their group or device. This can be configured on the RADIUS server. This feature allows granular control over access and resources on a per user or group basis.
*   **Accounting:**
    *   RADIUS accounting allows the tracking of connection usage by each user. MikroTik supports accounting through the RADIUS server for all ppp connections. This allows for comprehensive usage monitoring and logging.
*   **Multiple RADIUS Servers:**
    *   MikroTik supports multiple RADIUS servers, which allows for redundancy and load balancing. This improves the reliability of the system.
*   **VRF (Virtual Routing and Forwarding):**
    *   PPP clients can be assigned to specific VRFs, allowing for isolation between different customer traffic. This feature is important in enterprise environments where isolation is required.
*   **IP Pool:**
    *   Instead of using a range, a specific IP Pool can be used. This gives more control over IP allocation and how many IPs are available.

## MikroTik REST API Examples (if applicable):

While direct REST API calls for PPP configurations aren't as detailed as CLI commands, here's an example of enabling a PPP secret using the API.

**Endpoint:** `/ppp/secret`
**Method:** `POST`

**Example JSON Payload (Request):**

```json
{
    "name": "my-api-user",
    "profile": "radius-ppp",
    "service": "radius"
}
```
*  `name`: The username for the user.
*  `profile`: The profile to use for this user.
*  `service`: The service type. In this case `radius`.

**Expected Response (Successful):**

```json
{
  "id": "*1"
}
```

**Error Response (Example - duplicate username):**

```json
{
  "message": "already have secret with such name",
  "code": 5
}
```

**Explanation:**

*   **Request:** The JSON payload specifies the new PPP secret's attributes: username, profile, and service.
*   **Response:** On success, the API returns a JSON object with the `id` of the newly created secret. On a failure, it provides a code and error message.
*   **Error Handling:**  It's important to check the response code for each API call to understand if the operation was successful. MikroTik returns the `code` key which can be mapped to the different error codes.

**Note:**
API calls need an active session, use `/system api user add` to add a user for api access and use `/system api ssh-login <user> <password>` to log in and then use the api token for authentication.

## Security Best Practices

*   **Strong RADIUS Shared Secret:** Use a strong, random secret for RADIUS authentication. Avoid using easily guessed secrets.
*   **Encryption:** Enforce encryption for PPP connections to prevent eavesdropping on user traffic.
*   **Firewall Rules:** Implement strict firewall rules to allow only necessary traffic and block all other.
*   **Regular Updates:** Keep RouterOS and the RADIUS server software up-to-date.
*   **Monitor Logs:** Continuously monitor logs for suspicious activity. Set up a monitoring system to track failed login attempts, unauthorized access, or unexpected traffic.
*   **Secure Router Access:**  Always restrict remote access and use strong passwords.
*   **Limit API Access:** Limit API access to only specific addresses and users using `firewall-address-list` and use a custom port for the API to make it less discoverable.
*   **Use HTTPS:** Always use HTTPS for API access.
* **Use VPN or SSH tunnel:** Always use a VPN or SSH tunnel for secure access to the router from outside the network.

## Self Critique and Improvements:

*   **Improvement:** We could add more granularity for authorization rules in the RADIUS server. By adding custom attributes that control traffic shaping, vlan assignments, etc.
*   **Improvement:** Using IP Pools instead of ranges gives more control, and is also scalable when we need a different ip range for each user.
*   **Improvement:** We could integrate user grouping in the RADIUS server.
*   **Improvement:** The use of VRF to further isolate different users.
*   **Improvement:** Instead of using Google's DNS servers, which can be blocked, using custom, local DNS servers is advised.
*   **Improvement:** A more complex firewall configuration could be added.

## Detailed Explanations of Topic

**PPP (Point-to-Point Protocol):** PPP is a data link layer protocol commonly used to establish a direct connection between two nodes. It's widely used for establishing dial-up, DSL, and VPN connections. In our case, we are setting up a PPP server to handle incoming client connections over an Ethernet interface.

**AAA (Authentication, Authorization, and Accounting):** AAA is a framework for controlling access to computer resources.
    *   **Authentication:** Verifies the identity of a user (e.g., username and password). In our case we are passing this information to a radius server, so it can authenticate the user.
    *   **Authorization:** Determines what the user is allowed to do (e.g., access specific resources, bandwidth limits). This is controlled by a radius server in this configuration.
    *   **Accounting:**  Tracks the resource usage of users (e.g., time of connection, amount of data transmitted). This can be used to implement a usage based system on your users.

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting management. RADIUS clients (like our MikroTik router) send authentication requests to a RADIUS server, which then authenticates the user and returns authorization information. This allows for consistent authentication and authorization across multiple network devices.

## Detailed Explanation of Trade-offs

*   **Local Authentication vs. RADIUS:**
    *   **Local:** Simple to set up but doesn’t scale well for a large network. It is not suitable for enterprise environments because you need to manage every user on the router.
    *   **RADIUS:** More complex to set up but enables centralized user management and authorization. It's ideal for larger environments with dynamic user needs.
*   **Authentication Protocols (PAP, CHAP, MS-CHAP):**
    *   **PAP (Password Authentication Protocol):** Sends the password in clear text, making it highly vulnerable. Should not be used.
    *   **CHAP (Challenge Handshake Authentication Protocol):** Provides better security by using a three-way handshake.
    *   **MS-CHAP (Microsoft CHAP):** Microsoft's version of CHAP, supports more features.
    *   **Trade-off:** MS-CHAP2 is preferred, however, this may not be available in the radius server. CHAP is preferrable over PAP.
*   **Encryption:**
    *   **Enforcing Encryption:** Ensures secure communication of data between the client and the router, but can cause overhead on both client and server.
    *   **Not Enforcing Encryption:** Can reduce overhead but leaves connections vulnerable to attacks.
    * **Trade-off**: It's always better to use encryption, even though this can result in some extra overhead, as it protects user data on the link.
*   **IP Pool vs IP range:**
    *   **IP Range:** Simple to set up, less flexible.
    *  **IP Pool:** More flexible, allows granular control over ip assignment.
    *  **Trade-off**: IP Pool is more scalable and manageable, but IP range is simple to implement and is useful when there is no need for a scalable solution.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with both RouterOS 6.48 and 7.x. If we need to make it compatible to a much earlier version, we may need to remove the use of features such as `timeout` in the `radius` menu, or `change-tcp-mss` in the `ppp profile`.

Let me know if you have any further questions or want to explore specific aspects in more detail!
