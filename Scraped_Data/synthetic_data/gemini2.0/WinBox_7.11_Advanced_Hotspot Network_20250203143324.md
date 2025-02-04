Okay, let's dive into configuring a MikroTik hotspot network using WinBox, specifically focusing on the provided subnet and interface. We'll aim for an advanced configuration, keeping in mind the potential for larger deployments. This documentation will cover RouterOS 7.11 (and be compatible with 6.48 and 7.x), focusing on the specified requirements.

## Scenario Description:

This scenario addresses the configuration of a basic hotspot network using MikroTik RouterOS. We'll configure the `wlan-30` interface (assuming it is a wireless interface) to serve clients within the `155.114.175.0/24` subnet.  The hotspot will provide IP address assignment and basic user authentication. The goal is to demonstrate the basic configuration necessary to get the Hotspot up and running, while also covering advanced concepts like proper IP address assignment.

## Implementation Steps:

Here's a step-by-step guide to configure the hotspot using WinBox and CLI commands:

### 1. Step 1: Configure IP Address on the Interface

*   **Description:**  First, we need to assign an IP address to the `wlan-30` interface. This IP will act as the gateway for the clients connected to this interface.
*   **Why:**  Without an IP address on the interface, the hotspot cannot function or assign IP addresses to clients.

#### WinBox GUI Instructions:

1.  Navigate to `IP -> Addresses`.
2.  Click the `+` button to add a new address.
3.  In the `Address` field, enter `155.114.175.1/24`.
4.  In the `Interface` dropdown, select `wlan-30`.
5.  Click `Apply` then `OK`.

#### CLI Instructions:

```
/ip address
add address=155.114.175.1/24 interface=wlan-30
```

#### Before Configuration:

Assume no IP address is configured on the `wlan-30` interface.  You can view this using the following command:

```
/ip address print where interface=wlan-30
```

(Output should be empty or show an existing config that isn't 155.114.175.0/24).

#### After Configuration:
After applying the address, you can verify with:

```
/ip address print where interface=wlan-30
```

(Output should be similar to the example below):

```
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   155.114.175.1/24   155.114.175.0   wlan-30
```

*   **Effect:**  The `wlan-30` interface is now assigned an IP address and is ready for hotspot configuration.

### 2. Step 2: Enable the Hotspot Server

*   **Description:** We enable the Hotspot Server on the selected interface. This is the core of the Hotspot functionality.
*   **Why:** This step enables the listening service, which will intercept incoming traffic for authentication.

#### WinBox GUI Instructions:

1.  Navigate to `IP -> Hotspot`.
2.  Go to the `Servers` tab.
3.  Click the `+` button to add a new server.
4.  In the `Name` field, enter a descriptive name (e.g., `hotspot-wlan-30`).
5.  In the `Interface` dropdown, select `wlan-30`.
6.  Click `Apply` then `OK`.

#### CLI Instructions:

```
/ip hotspot server
add name=hotspot-wlan-30 interface=wlan-30
```
#### Before Configuration:
List configured hotspot servers:
```
/ip hotspot server print
```
(This should be empty or not include an entry called 'hotspot-wlan-30')

#### After Configuration:
List configured hotspot servers again, you will see your new server.
```
/ip hotspot server print
```

(Output should include something like):

```
Flags: X - disabled, I - invalid
 #   NAME             INTERFACE      PROFILE
 0   hotspot-wlan-30  wlan-30        default
```

*   **Effect:**  A new hotspot server is created and bound to the `wlan-30` interface.

### 3. Step 3: Configure the Hotspot Server Profile

*   **Description:** We'll configure a profile to define parameters like DNS, address pools, and more for our Hotspot.
*   **Why:**  The profile defines how the Hotspot server behaves, including how IP addresses are assigned, and which DNS servers the clients will use.

#### WinBox GUI Instructions:

1.  Navigate to `IP -> Hotspot`.
2.  Go to the `Server Profiles` tab.
3.  Select the default profile (or create a new one if desired) and click `Open`.
4.  In the `General` tab:
    -   Set `DNS Name` to a domain name (e.g., `hotspot.example.com`).
    -   Check `Use RADIUS` and leave everything disabled.
    -   For now, let all other settings at their default.
5.  In the `Address Pool` tab:
    - Select the address pool, or create one.
    -   **Create address pool**:
         -   Click the '+' to add new Pool.
         -   Enter a name, for example 'hotspot_pool'
         -   Set address to `155.114.175.2-155.114.175.254`
         -   Click 'Apply' and 'Ok'.
    -   Select the created address pool 'hotspot_pool'
6.  In the `Radius` tab,  Leave all settings disabled.
7.  In the `Login` tab, leave as is.
8.  Click `Apply` then `OK`.

#### CLI Instructions:

```
/ip hotspot profile
set default dns-name=hotspot.example.com use-radius=no
/ip pool add name=hotspot_pool ranges=155.114.175.2-155.114.175.254
/ip hotspot profile set default address-pool=hotspot_pool
```
#### Before Configuration:
Check the existing profile:
```
/ip hotspot profile print where name=default
```
(Output will show default values, typically an empty `dns-name`)

Check the existing address pools:
```
/ip pool print
```
(Output will show any existing pools)

#### After Configuration:
Check the updated profile:
```
/ip hotspot profile print where name=default
```

(Output should include something like):

```
Flags: * - default
 0   * name="default"    dns-name="hotspot.example.com"   address-pool="hotspot_pool"
      use-radius=no   http-proxy=0.0.0.0:0  radius-interim-update=0s  radius-timeout=3s  login-by=cookie,http-chap
      radius-accounting=no
```
And the address pool:
```
/ip pool print
```
(Output should now have your pool with the name 'hotspot_pool'):

```
Flags: X - disabled, D - dynamic
 #   NAME       RANGES                                                         
 0   hotspot_pool   155.114.175.2-155.114.175.254         
```

*   **Effect:** The hotspot server now has a profile that provides a DNS name and IP address range for clients.

### 4. Step 4: Configure User Profiles and First User

*   **Description:** We'll add a user profile (for now a single default user) and a user account.  This allows us to authenticate the user to the hotspot.
*   **Why:** Users need credentials to access the network.

#### WinBox GUI Instructions:

1.  Navigate to `IP -> Hotspot`.
2.  Go to the `Users` tab.
3.  Click the `+` button to add a new user.
4.  Enter a `Name` (e.g., `testuser`).
5.  Enter a `Password` (e.g., `password`).
6. Select the created 'default' user profile.
7.  Click `Apply` then `OK`.

#### CLI Instructions:

```
/ip hotspot user add name=testuser password=password profile=default
```

#### Before Configuration:

List all existing users
```
/ip hotspot user print
```

(Output will be empty).

#### After Configuration:

List all existing users again, it will include the one you just added.
```
/ip hotspot user print
```

(Output should be similar to):

```
Flags: X - disabled
 #   USER            PROFILE              ADDRESS     MAC-ADDRESS       
 0   testuser        default              0.0.0.0    00:00:00:00:00:00
```

*  **Effect:**  A new user with the provided credentials can now authenticate to the hotspot.

## Complete Configuration Commands:

Here's the full set of CLI commands to implement the complete configuration:

```
/ip address
add address=155.114.175.1/24 interface=wlan-30

/ip hotspot server
add name=hotspot-wlan-30 interface=wlan-30

/ip pool add name=hotspot_pool ranges=155.114.175.2-155.114.175.254

/ip hotspot profile
set default dns-name=hotspot.example.com use-radius=no address-pool=hotspot_pool

/ip hotspot user add name=testuser password=password profile=default
```

## Common Pitfalls and Solutions:

*   **Problem:**  Clients cannot get IP addresses.
    *   **Solution:**  Check that the interface has an IP address, the address pool is configured correctly, and the Hotspot Server is running. Verify there is no DHCP server active in the same subnet. Check the `wlan-30` interface is working and connected to an AP.
*   **Problem:** Clients cannot connect to the Hotspot Login page.
    *   **Solution:** Ensure the hotspot server is running and bound to the correct interface. Check the firewall rules to make sure the hotspot page isn't blocked, (make sure you have `/ip firewall filter print` with no rules that interfere).
*   **Problem:**  Slow connection speeds for Hotspot users.
    *   **Solution:**  Check that the Mikrotik is not overloaded, consider adding queues and shaping to manage bandwidth if necessary.
*   **Problem:** Authentication fails for valid users.
     * **Solution:**  Check the user's username and password in the Mikrotik configuration. Verify the user isn't disabled, and is not blocked due to incorrect login attempts.

* **Security Issue**: Using a default password like 'password' is highly insecure, you must use complex passwords that are hard to guess.
* **Resource Issues**: Hotspot networks can use a considerable amount of memory when multiple users are connected. Monitor the RouterOS system using the tool `system resource print`.

## Verification and Testing Steps:

1.  **Connect a Client:** Connect a device (laptop, phone, etc) to the `wlan-30` access point.
2.  **IP Address Check:** The client should receive an IP address in the 155.114.175.0/24 range. Verify this from the device itself.
3.  **Hotspot Page:**  Open a web browser on the client.  You should be redirected to the Hotspot login page.
4.  **Login:** Enter the user credentials (`testuser` and `password`).
5.  **Network Access:** After successfully logging in, verify that the client has access to the internet.
6.  **MikroTik Status Check:** In WinBox, navigate to `IP -> Hotspot -> Active`, verify the client is connected.
7.  **Ping Test:** From the client, ping `155.114.175.1`.  It should respond.  Also attempt to ping an external address (like 8.8.8.8). From Mikrotik CLI, `ping 8.8.8.8` and `ping 155.114.175.1` (this will verify the interface is online and that the DNS is working).

## Related Features and Considerations:

*   **Radius Authentication:** For larger deployments, use RADIUS authentication for centralized user management.
*   **Walled Garden:**  Configure the "Walled Garden" to allow specific sites without login (e.g., for support pages).
*   **Rate Limiting:** Limit the bandwidth available to each Hotspot user with MikroTik Queues.
*   **Logging:** Log Hotspot activity for monitoring and auditing.
*   **HTTPS for Login Page:**  Use HTTPS for the login page to encrypt the credentials sent from the user's browser.
*   **Custom Hotspot Login Page:** Create your own HTML pages for the login.

## MikroTik REST API Examples (if applicable):

Here are some basic examples of using the Mikrotik API to do the same as above:

*   **Enable API:** First make sure you have API or API SSL enabled in `/ip service print`.  Enable them if necessary:
```
/ip service set api disabled=no
/ip service set api-ssl disabled=no
```
*   **Add IP Address:** (Method: POST)
    *   Endpoint: `/ip/address`
    *   Payload:
```json
{
    "address": "155.114.175.1/24",
    "interface": "wlan-30"
}
```

    *   Example using curl (you will need to substitute username, password and the IP address of the mikrotik router):
```bash
curl -k -u 'apiuser:yourpassword' -H "Content-Type: application/json" -X POST  -d '{"address":"155.114.175.1/24","interface":"wlan-30"}'  https://192.168.88.1/rest/ip/address
```

    * Expected Response: 200 OK with JSON that contains id for the new IP address.
    * Error Handling: If interface not found: `400 Bad Request: {"message":"no such item"}` or if the IP is not unique: `400 Bad Request: {"message":"already have such address"}`.

*   **Add Hotspot Server:** (Method: POST)
    *   Endpoint: `/ip/hotspot/server`
    *   Payload:
```json
{
    "name": "hotspot-wlan-30",
    "interface": "wlan-30"
}
```

    *   Example using curl:
```bash
curl -k -u 'apiuser:yourpassword' -H "Content-Type: application/json" -X POST -d '{"name":"hotspot-wlan-30","interface":"wlan-30"}'  https://192.168.88.1/rest/ip/hotspot/server
```

    *   Expected Response: 200 OK with JSON that contains the ID for the created server.
    *   Error Handling:  If the interface doesn't exist the result will be: `400 Bad Request: {"message":"no such item"}`

*   **Configure Hotspot Profile (Modify default):** (Method: PUT)
    *   Endpoint: `/ip/hotspot/profile/0` (Use the ID from your `/ip hotspot profile print` command, likely '0')
    *   Payload:
```json
{
        "dns-name": "hotspot.example.com",
        "use-radius": "no"
}
```
    * Example using curl:
```bash
curl -k -u 'apiuser:yourpassword' -H "Content-Type: application/json" -X PUT -d '{"dns-name":"hotspot.example.com","use-radius":"no"}' https://192.168.88.1/rest/ip/hotspot/profile/0
```
    * Expected response: `200 OK`, an empty message.
    * Error Handling: `404 Not Found` if id does not exist.
*   **Add User:** (Method: POST)
    *   Endpoint: `/ip/hotspot/user`
    *   Payload:
```json
{
    "name": "testuser",
    "password": "password",
        "profile":"default"
}
```

    * Example using curl:
```bash
curl -k -u 'apiuser:yourpassword' -H "Content-Type: application/json" -X POST -d '{"name":"testuser","password":"password","profile":"default"}'  https://192.168.88.1/rest/ip/hotspot/user
```

    *   Expected Response: 200 OK with JSON that contains the ID of the created user.
    *   Error Handling:  If the profile does not exist, the message is: `400 Bad Request: {"message":"no such item"}`

## Security Best Practices

*   **Strong Passwords:** Enforce strong passwords for user accounts and router access.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version.
*   **Firewall:** Implement a strong firewall configuration to limit access to services.
*   **Disable Unused Services:** Disable API, telnet, and other unused services.
*   **Secure Web Interface:** Use HTTPS for WinBox and API access.
*   **Limit Hotspot Login Access:** Use firewall rules to restrict access to the login page from outside your network.

## Self Critique and Improvements

This configuration provides a basic Hotspot setup, but it can be improved by:

*   **RADIUS integration:** Adding RADIUS for user management.
*   **More Robust Queues:** Implement more advanced traffic shaping and QoS policies.
*   **Custom Login Page:** Using a custom login page with branding.
*  **HTTPS**: Using HTTPS for hotspot portal.
*   **SSL/TLS certificates**: Generate and use SSL certificates for HTTPS access.
*   **User Tracking**: Track users via MAC addresses, session information, and timestamps.
*   **Backup**: Regularly back up your configuration so you can revert to a stable state in case of an issue.

## Detailed Explanations of Topic

The topic of this document is specifically focused on setting up a basic MikroTik Hotspot server on a specified wireless interface, wlan-30, within a defined subnet 155.114.175.0/24, using MikroTik RouterOS version 7.11. This functionality allows users connecting to the 'wlan-30' access point to get IP addresses, and get redirected to the hotspot's login page.

## Detailed Explanation of Trade-offs

*   **Using a default profile vs. creating a custom profile:**
    *   **Default Profile**: Easier and faster for quick setups, but limits customization.
    *   **Custom Profile**: Offers more control but requires configuration, like RADIUS configuration or user authentication modes.
*   **Using the default address pool:**
    *   **Default Pool**: It will attempt to use the network's main address pool, which can lead to conflicts.
    *   **Specific Pool**: Allows us to define a separate IP address range specifically for hotspot users, isolating them from other network devices.
*   **Basic password vs more advanced authentication:**
    *   **Basic password**: Easier for testing, but less secure.
    *   **RADIUS**: Allows more complex authentication options, like user time limits and other advanced settings, and is better for large scale deployments.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 7.11, but should also work on 6.48 and 7.x. Older versions (below 6.48) may not support all commands or parameters, and will require you to use legacy configurations. Please check your RouterOS version and the related documentation.

This complete documentation should give you a robust understanding of configuring the Hotspot feature on your MikroTik device. Let me know if you need further clarification.
