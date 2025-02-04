Okay, let's create a detailed technical document on configuring PPP AAA for a Hotspot network using MikroTik RouterOS v7.12, specifically focusing on a bridge interface and the given subnet. This will be an Advanced configuration, suitable for SOHO, SMB and potentially larger hotspot networks.

## Scenario Description:

This scenario involves setting up PPP authentication, authorization, and accounting (AAA) for users connecting to a hotspot network. The network is served by a MikroTik router with a bridge interface (`bridge-44`) connected to the LAN, and users will connect to this network using PPP over Ethernet (PPPoE) or other PPP protocols. The IP address pool for users will be within the `42.11.170.0/24` subnet. Authentication will be done using a local user database, but we will also show how to adapt it for a RADIUS server, for completeness.

## Implementation Steps:

### 1. **Step 1: Configure the Bridge Interface**

**Before:**

We assume you have basic network configurations set up on your router.  Let's see the initial bridge configuration. In the CLI:
```mikrotik
/interface bridge print
```
This will show any existing bridges, something like:

```
Flags: X - disabled, R - running
 #    NAME                                  MTU   L2MTU  MAC-ADDRESS         ADMIN-MAC-ADDRESS    ARP PROTOCOL
 0  R bridge1                               1500  1598  00:11:22:33:44:55   00:11:22:33:44:55  enabled none
```
Also check for ip addresses with `/ip address print`.  This will return any configured interfaces.  You may or may not have an address assigned to the bridge1 interface.

**Action:**

We will create a new bridge named `bridge-44` and add the desired ethernet interfaces.
Let's assume you have ethernet ports ether1, ether2, ether3 that will participate in the hotspot LAN.

**CLI Commands:**
```mikrotik
/interface bridge
add name=bridge-44
/interface bridge port
add bridge=bridge-44 interface=ether1
add bridge=bridge-44 interface=ether2
add bridge=bridge-44 interface=ether3
```
**Winbox Instructions:**

*   Go to "Bridge" -> "+" and create a new bridge named `bridge-44`.
*   Go to "Bridge" -> "Ports" and add the interfaces (`ether1`, `ether2`, `ether3`) to the `bridge-44` interface.

**After:**
Checking the bridge configuration again
```mikrotik
/interface bridge print
```
You will see the output.
```
Flags: X - disabled, R - running
 #    NAME                                  MTU   L2MTU  MAC-ADDRESS         ADMIN-MAC-ADDRESS    ARP PROTOCOL
 0  R bridge1                               1500  1598  00:11:22:33:44:55   00:11:22:33:44:55  enabled none
 1  R bridge-44                             1500  1598  AA:BB:CC:DD:EE:FF   AA:BB:CC:DD:EE:FF  enabled none
```
Note: A randomly generated MAC address will be created.

This step creates the bridge interface that will serve the hotspot network.

### 2. **Step 2: Configure the IP Address for the Bridge Interface**

**Before:**

The bridge will have no IP address assigned yet.
```mikrotik
/ip address print
```
**Action:**

Assign an IP address to the `bridge-44` interface from your desired subnet.

**CLI Command:**
```mikrotik
/ip address add address=42.11.170.1/24 interface=bridge-44
```

**Winbox Instructions:**

*   Go to "IP" -> "Addresses" -> "+" and add the address `42.11.170.1/24` to the interface `bridge-44`.

**After:**

You'll see the IP address has been assigned when you use
```mikrotik
/ip address print
```

This step enables IP communication on the `bridge-44` interface.

### 3. **Step 3: Configure the PPP Profile**

**Before:**
No profiles exist for ppp.
```mikrotik
/ppp profile print
```
**Action:**

Create a PPP profile named `hotspot-profile` for hotspot users with appropriate settings.
*   local-address= the address that will be assigned to the router ppp interface.
*   remote-address= the range of addresses assigned to client interfaces
*   use-encryption= yes is recommended.
*   dns-server= your chosen dns server.

**CLI Commands:**

```mikrotik
/ppp profile
add name=hotspot-profile local-address=42.11.170.1 remote-address=42.11.170.2-42.11.170.254 use-encryption=yes dns-server=8.8.8.8,1.1.1.1
```

**Winbox Instructions:**
* Go to "PPP" -> "Profiles" -> "+"
* Create a new profile with name `hotspot-profile`. Set the "Local Address" to `42.11.170.1`, "Remote Address" to `42.11.170.2-42.11.170.254`, and DNS Servers to `8.8.8.8,1.1.1.1` Check "Use Encryption".

**After:**
Now when you list the profiles you should see `hotspot-profile`.
```mikrotik
/ppp profile print
```
This step sets the parameters for PPP connections.

### 4. **Step 4: Configure PPP Secret (User Authentication)**

**Before:**
No ppp users exist.
```mikrotik
/ppp secret print
```

**Action:**

Create a PPP user named `testuser` with password `testpass` and the `hotspot-profile` we created earlier.

**CLI Commands:**

```mikrotik
/ppp secret
add name=testuser password=testpass service=pppoe profile=hotspot-profile
```
**Winbox Instructions:**

*   Go to "PPP" -> "Secrets" -> "+".
*   Add the name, password, service (e.g., `pppoe`) and profile (`hotspot-profile`).

**After:**
```mikrotik
/ppp secret print
```
You will now see the user named `testuser` with the profile `hotspot-profile`.

This step sets up basic local authentication for PPP users.

### 5. **Step 5: Configure PPP Server (PPPoE Example)**

**Before:**
No ppp server interfaces exist.
```mikrotik
/interface ppp-server print
```

**Action:**

Enable PPPoE server on the `bridge-44` interface.

**CLI Commands:**

```mikrotik
/interface ppp-server pppoe
add service-name=hotspot-pppoe interface=bridge-44 default-profile=hotspot-profile
```

**Winbox Instructions:**

*   Go to "PPP" -> "PPPoE Servers" -> "+".
*   Add a PPPoE server, select `bridge-44` as interface, the `hotspot-profile` as "Default Profile", and give a service name `hotspot-pppoe`.

**After:**
```mikrotik
/interface ppp-server print
```
You will see the ppp-server listening on interface `bridge-44`.

This step allows users to connect using PPPoE over the bridge.

### 6. **Step 6: (Optional) RADIUS Configuration**

**Before:**
You will not see a radius configuration, and you should not create one if you do not intend to use it.
```mikrotik
/radius print
```

**Action:**

(Optional) Configure a RADIUS server if you need external authentication. We assume your RADIUS server address is 192.168.1.100 with secret 'radiussecret'
**CLI Commands:**
```mikrotik
/radius
add address=192.168.1.100 secret=radiussecret service=ppp timeout=3
```
Then modify the ppp profile to use radius
```mikrotik
/ppp profile set hotspot-profile use-radius=yes
```
**Winbox Instructions:**

* Go to "Radius" -> "+"
* Add the radius server address, secret, service (PPP) and timeout.
* Go to PPP -> "Profiles" -> "hotspot-profile", check the box "Use Radius".

**After:**
```mikrotik
/radius print
```
```mikrotik
/ppp profile print
```

This step allows using RADIUS server authentication for more sophisticated setups.

## Complete Configuration Commands:

```mikrotik
# Step 1: Create bridge
/interface bridge
add name=bridge-44
/interface bridge port
add bridge=bridge-44 interface=ether1
add bridge=bridge-44 interface=ether2
add bridge=bridge-44 interface=ether3

# Step 2: Set IP Address for the Bridge
/ip address add address=42.11.170.1/24 interface=bridge-44

# Step 3: Configure PPP Profile
/ppp profile
add name=hotspot-profile local-address=42.11.170.1 remote-address=42.11.170.2-42.11.170.254 use-encryption=yes dns-server=8.8.8.8,1.1.1.1

# Step 4: Configure PPP Secret (User Authentication)
/ppp secret
add name=testuser password=testpass service=pppoe profile=hotspot-profile

# Step 5: Configure PPPoE Server
/interface ppp-server pppoe
add service-name=hotspot-pppoe interface=bridge-44 default-profile=hotspot-profile

# Step 6: (Optional) RADIUS Configuration
/radius
# add address=192.168.1.100 secret=radiussecret service=ppp timeout=3 # Uncomment if needed.
# /ppp profile set hotspot-profile use-radius=yes # Uncomment if needed.
```

**Parameter Explanations:**

| Command Parameter | Description                                                                           | Example Value        |
|-------------------|---------------------------------------------------------------------------------------|----------------------|
| `name`             | The name of the object (bridge, profile, secret, etc.).                             | `bridge-44`, `hotspot-profile`, `testuser`        |
| `interface`       | The interface to associate with the object.                                           | `bridge-44`, `ether1` |
| `address`          | The IP address and subnet mask.                                                     | `42.11.170.1/24`, `192.168.1.100` |
| `local-address`   | The local IP address assigned to the PPP connection.                                | `42.11.170.1`        |
| `remote-address`  | The IP address range assigned to connected clients.                                 | `42.11.170.2-42.11.170.254` |
| `password`        | The password for PPP user.                                                          | `testpass`            |
| `service`         | The PPP service type (e.g., `pppoe`).                                              | `pppoe`               |
| `profile`         | The PPP profile name.                                                                 | `hotspot-profile`    |
| `service-name`      | The name of the service for PPP clients to connect to.                               | `hotspot-pppoe`      |
| `default-profile` | The default PPP profile to use.                                                      | `hotspot-profile`    |
| `use-encryption`   | Enables PPP encryption.                                                              | `yes`, `no`         |
| `dns-server`       | DNS server address for clients.                                                    | `8.8.8.8,1.1.1.1`     |
| `secret`          | RADIUS shared secret key.                                                           | `radiussecret`       |
| `timeout`          | RADIUS server timeout in seconds.                                                  | `3`                |
| `use-radius`        | Enable RADIUS for this profile.                                                    | `yes`, `no`         |

## Common Pitfalls and Solutions:

*   **User Fails to Authenticate:** Double check the username and password, ensure the user service type matches the server type, verify the user has the correct profile assigned. Check the logs (`/log`) to see authentication failure messages.  If using radius, check that the router has an IP route to the radius server and ensure the radius server has a correct secret configured.
*   **Users Cannot Obtain IP Addresses:** Ensure that the remote IP address range configured in the ppp profile does not overlap with the LAN IP subnet. Check the IP address pool is large enough for the expected number of concurrent connections. Verify the profile is assigned to the server interface and the user
*   **PPPoE Server Not Responding:** Ensure the `pppoe` server interface is active and bound to the correct bridge or interface. Check firewall rules that could block PPPoE packets on port 1701.
*   **DNS Issues:** Check that the DNS server configured in the PPP profile or Radius is accessible.
*   **Incorrect MTU:** Ensure MTU is correct on the PPP interface.
*   **High CPU Usage:** Check router CPU usage using `/system resource monitor`.  If CPU usage is high, reduce logging, or consider a more powerful router.
*   **RADIUS Errors:** Verify the RADIUS server IP, secret, and timeout settings. Check radius server logs for authentication errors. Make sure that the router and the radius server have time sync enabled.

## Verification and Testing Steps:

1.  **Client Connection:** Use a PPP client (like a computer running windows ppp client) to connect to the `hotspot-pppoe` service using the `testuser` and `testpass` created previously.
2.  **Check IP Assignment:** Once connected, use the command `/ip address print` to see the created ppp interface, which should have the assigned client address.
3.  **Ping:** Ping an external IP (e.g., 8.8.8.8) or a public website address, from the client.
4.  **Traceroute:** Perform a traceroute from the client to verify routing is correct and the packet can reach the destination.
5.  **MikroTik Logs:** Check logs using `/log print` for authentication success/failures and other errors.
6.  **Torch:** Use the MikroTik Torch tool `/tool torch interface=bridge-44` to inspect live network traffic on the bridge interface during client connection and data transfer.

## Related Features and Considerations:

*   **Hotspot Feature:** The MikroTik `hotspot` feature provides a captive portal and advanced user management. It can be used in conjunction with PPP authentication.
*   **Firewall Rules:** Configure firewall rules for traffic originating from the ppp interface.
*   **User Profiles:** Configure bandwidth limits, traffic shaping, and other per-user policies using PPP profiles and firewall queues.
*   **VPN (PPTP, L2TP, OpenVPN):** Consider setting up a VPN server for secure remote access using PPP tunneling protocols.
*   **Accounting:** Enable PPP accounting using `/ppp accounting` to keep records of user usage. This accounting data can be integrated with RADIUS or used internally.
*   **DHCP Server:** If you are not using PPP, you can instead enable a DHCP server on the `bridge-44` interface to serve addresses to clients.
*   **Traffic Shaping:** Set up QoS (Quality of Service) rules using `/queue simple` or `/queue tree` to manage bandwidth usage effectively.
*   **Security:** Use strong passwords and implement firewall rules to limit access to the router. Disable unnecessary services.

## MikroTik REST API Examples:

**Example 1: Create a PPP Profile**
*   **API Endpoint:** `/ppp/profiles`
*   **Request Method:** `POST`
*   **Example JSON Payload:**
    ```json
    {
        "name": "hotspot-api-profile",
        "local-address": "42.11.170.1",
        "remote-address": "42.11.170.2-42.11.170.254",
        "use-encryption": true,
        "dns-server": "8.8.8.8,1.1.1.1"
    }
    ```
*   **Expected Response:**
    ```json
    {
        ".id": "*1",
        "name": "hotspot-api-profile",
        "local-address": "42.11.170.1",
        "remote-address": "42.11.170.2-42.11.170.254",
        "use-encryption": true,
        "dns-server": "8.8.8.8,1.1.1.1"
    }
    ```
*   **Error Handling:** If the profile name already exists or invalid parameters are provided, the API will return a HTTP error code (e.g., 400 Bad Request), along with a JSON body detailing the error message.

**Example 2: Create a PPP Secret**

*   **API Endpoint:** `/ppp/secrets`
*   **Request Method:** `POST`
*   **Example JSON Payload:**

    ```json
     {
        "name": "apiuser",
        "password": "apipassword",
        "service": "pppoe",
        "profile": "hotspot-api-profile"
      }
    ```
*   **Expected Response:**
    ```json
     {
        ".id": "*1",
        "name": "apiuser",
        "password": "apipassword",
        "service": "pppoe",
        "profile": "hotspot-api-profile"
      }
    ```
*   **Error Handling:** The API will return an HTTP error code if the user name already exists or if an invalid profile is used.

**Example 3: Enable PPPoE Server**
* **API Endpoint:** `/interface/ppp-server/pppoe`
* **Request Method:** `POST`
* **Example JSON Payload:**
    ```json
    {
        "service-name": "hotspot-api-pppoe",
        "interface": "bridge-44",
        "default-profile": "hotspot-api-profile"
    }
    ```
* **Expected Response:**
    ```json
    {
        ".id": "*1",
        "service-name": "hotspot-api-pppoe",
        "interface": "bridge-44",
        "default-profile": "hotspot-api-profile"
    }
    ```
*   **Error Handling:** The API will return an HTTP error code if the server name already exists or if an invalid interface or profile is used.

**Note:** The MikroTik REST API requires authentication, usually via session cookies or token-based authentication. Refer to the official documentation for the correct authentication procedure.

## Security Best Practices

*   **Strong Passwords:** Use strong, unique passwords for all PPP users and the router's admin interface.
*   **Encryption:** Always use PPP encryption.
*   **Firewall:** Implement a strict firewall to block unauthorized access to the router and the network.
*   **Limit Access:** Disable unnecessary services and interfaces. Only enable what you need.
*   **Regular Updates:** Keep your RouterOS up to date to patch security vulnerabilities.
*   **Monitor Logs:** Regularly check the logs for suspicious activity.
*   **Rate Limiting:** Limit the number of concurrent login attempts for PPP and other services.
*   **RADIUS Secret:** Ensure the RADIUS secret is very strong and kept confidential.

## Self Critique and Improvements

*   **User Management**: The current setup uses a static list of users. A more robust system could use the Hotspot or User Manager, or delegate to RADIUS.
*   **Bandwidth Control**: There is no bandwidth control set per-user. This is necessary for hotspot deployments.
*   **Accounting**: The current setup does not collect data on the amount of bandwidth consumed by each user. Consider implementing ppp accounting to track usage and implement limits.
*   **Dynamic IP Ranges**: The current setup has all clients on a single /24, which limits scalability. Consider smaller subnets or address pools for larger deployments.
*   **Simplified API access**: Consider using a higher level api, or framework to simplify interaction with the API.

## Detailed Explanations of Topic

**PPP (Point-to-Point Protocol)** is a data link layer communication protocol that establishes a direct connection between two nodes. It is often used for connecting to an ISP using dial-up or broadband connections. PPP provides a mechanism for encapsulating network layer protocols such as IP over a serial or virtual link, providing framing, error detection, authentication, and security. It supports various authentication methods (PAP, CHAP, MS-CHAPv2), and optionally, encryption using protocols like MPPE.

**AAA (Authentication, Authorization, and Accounting)** is a framework for managing access to network resources. It is used to verify user identities (Authentication), control the resources users can access (Authorization), and track user activity (Accounting).
*   **Authentication:** Verifies that users are who they claim to be. This can be done with local usernames/passwords stored on the router or using an external RADIUS server.
*   **Authorization:** Determines which resources or services an authenticated user is permitted to access. In the context of PPP, this may include the IP address range, access to specific networks, or QoS settings.
*   **Accounting:** Tracks user activity and resource usage, such as connection time, data transferred, etc. This allows for monitoring usage and can be used for billing or reporting.

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized AAA for users connecting to a network. It is a client-server protocol where a RADIUS client (in this case the MikroTik router) sends authentication requests to a RADIUS server. The RADIUS server checks the username/password, determines user authorization, and returns accounting data. RADIUS is a powerful tool for handling large numbers of users and complex authorization schemes.

## Detailed Explanation of Trade-offs

*   **Local Authentication vs. RADIUS:**
    *   **Local Authentication:**
        *   **Pros:** Simple to set up, no external dependency, suitable for smaller networks.
        *   **Cons:** Difficult to manage large number of users, limited authorization options, no central accounting.
    *   **RADIUS Authentication:**
        *   **Pros:** Scalable, centralized user management, sophisticated authorization capabilities, detailed accounting.
        *   **Cons:** Requires an external server, more complex to configure, potential point of failure.

*   **PPP Profile Configurations:**
    *   **Static IP vs Dynamic IP:**
        *   **Static IP:** User always gets the same IP, may be needed for services. This will limit scalability.
        *   **Dynamic IP:** Pool of addresses assigned to users as needed. Scalable, easy to implement.
    *   **Encryption**:
        *   **Enabled**: More secure, recommended. May impact performance.
        *   **Disabled**: Less secure, faster. Should not be used in most cases.
    *   **DNS server**:
        *   **Public**: Easy to configure, but can be untrustworthy or slow.
        *   **Private**: Can provide better security or speed, but requires additional effort.

*   **PPPoE vs Other Protocols (e.g., PPTP, L2TP):**
    *   **PPPoE (PPP over Ethernet):** Commonly used for DSL connections, generally straightforward to set up, good performance.
    *   **PPTP/L2TP:** VPN tunneling protocols can be used for remote access and security but have higher overhead. PPTP is considered insecure and not recommended in modern networks.

## Configuration for Specific RouterOS Versions

This configuration specifically targets RouterOS v7.12, but the commands will mostly work for v6.48 and later versions. Some less important features (such as the API or minor command syntax differences) could cause some problems.  If you use a version lower than 6.48, then it is highly recommended you upgrade.

This detailed explanation covers a robust PPP AAA configuration for your MikroTik hotspot network. Remember to customize and test the configuration within a safe environment before deploying to production.
