Okay, let's craft some detailed technical documentation for a RADIUS-based authentication setup on a MikroTik router running RouterOS 7.11 (or later, with backward compatibility notes for 6.48).

## Scenario Description:

This document details configuring a MikroTik router as a RADIUS client to authenticate users connecting to a Hotspot network. Users will be given access to the network only after successfully authenticating through a RADIUS server.  The Hotspot network will operate on the subnet 73.173.221.0/24, using the interface named `ether-50` (this can be whatever interface you want). This setup is suitable for SOHO, SMB environments where centralized user management is desired.

**Configuration Level:** Basic

**Network Scale:** Hotspot Network (SOHO, SMB)

**Subnet:** 73.173.221.0/24

**Interface:** ether-50

## Implementation Steps:

Here's a step-by-step guide on implementing RADIUS authentication for a Hotspot on a MikroTik router, with CLI examples and Winbox hints where relevant.

### Step 1: Configure the Interface and IP Address
- **Before**: Ensure your `ether-50` interface is enabled.  You might have other configurations on your router which you will need to make sure do not overlap with what we are setting here.
- **Action**: Set an IP address on `ether-50` interface.
- **Rationale**: This step defines the IP address space for the Hotspot network. The router will provide DHCP leases in this range.

**CLI Example:**
```mikrotik
/ip address
add address=73.173.221.1/24 interface=ether-50
```
**Winbox GUI:**
- Navigate to IP -> Addresses
- Click the "+" button to add a new IP address.
- Set Address to `73.173.221.1/24` and Interface to `ether-50`
- Click Apply and OK.

**After:**  The router now has an IP address assigned to the `ether-50` interface, and will be able to communicate on that network.
```mikrotik
[admin@MikroTik] /ip address> print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24    192.168.88.0    ether1
 1   73.173.221.1/24    73.173.221.0    ether-50
```
### Step 2: Create a Hotspot Profile
- **Before**: No Hotspot profile exists
- **Action**: Create a new Hotspot profile to configure basic hotspot settings
- **Rationale**:  A hotspot profile allows us to apply specific settings to our hotspot.

**CLI Example:**
```mikrotik
/ip hotspot profile
add name=hotspot1  use-radius=yes html-directory=hotspot
```

**Winbox GUI:**
- Navigate to IP -> Hotspot
- Go to the Profiles tab
- Click the "+" button.
- Give it the name `hotspot1`, check `Use Radius`, specify a directory for the HTML files, such as `hotspot`
- Click Apply and OK.

**After:** A new Hotspot profile is available for use in the hotspot server.
```mikrotik
[admin@MikroTik] /ip hotspot profile> print
Flags: * - default
 0   name="hotspot1"   hotspot-address=0.0.0.0/0  html-directory="hotspot"  dns-name=""  radius-address="" radius-port=1812
     radius-secret=""  radius-accounting=no  radius-accounting-port=1813  radius-timeout=3000 use-radius=yes

```
### Step 3: Create a Hotspot Server
- **Before**: No Hotspot server is configured
- **Action**: Create the Hotspot server associated with the previously created profile.
- **Rationale**: This step binds the Hotspot service to the physical network interface.

**CLI Example:**
```mikrotik
/ip hotspot
add name=hotspot1  interface=ether-50 profile=hotspot1 address-pool=dhcp_pool_hotspot
```

**Winbox GUI:**
- Navigate to IP -> Hotspot
- Go to the Servers tab
- Click the "+" button.
- Name it `hotspot1`
- Select the `ether-50` interface
- Select the profile that was created in step 2: `hotspot1`
- Create a new address pool using the dropdown box named "Address Pool".
- Click Apply and OK.

**After:** The hotspot service is now running on the selected interface.
```mikrotik
[admin@MikroTik] /ip hotspot> print
Flags: X - disabled, I - invalid
 #   NAME          INTERFACE  PROFILE      ADDRESS-POOL      IDLE-TIMEOUT  KEEP-ALIVE-TIMEOUT  MAC-COOKIE
 0   hotspot1      ether-50   hotspot1      dhcp_pool_hotspot 00:05:00      00:02:00
```

### Step 4: Configure the RADIUS Server
- **Before**: No RADIUS server is configured.
- **Action**: Configure the RADIUS server details.
- **Rationale**: This step instructs the router about how to connect to and communicate with the RADIUS server.
 **Note:**
 * The shared secret must match on both the MikroTik and Radius server.
 * The IP address must be the IP address of your radius server.
 * If you are using a different port, make sure to change it here.
 * The accounting flag will enable accounting of the session, which might not be necessary for a simple implementation.

**CLI Example:**
```mikrotik
/radius
add address=192.168.100.20 secret="your_radius_secret" service=hotspot timeout=3000
```

**Winbox GUI:**
- Navigate to RADIUS
- Click the "+" button.
- Add the server's IP address, Shared Secret and set service to `hotspot`.
- Click Apply and OK.

**After:** The MikroTik router is configured to use the specified RADIUS server.
```mikrotik
[admin@MikroTik] /radius> print
Flags: X - disabled, * - default
 #   ADDRESS         SECRET               SERVICE TIMEOUT
 0   192.168.100.20  your_radius_secret   hotspot 3s
```

### Step 5: Configure DHCP Server (If not already present)
- **Before**: No DHCP server is configured for the hotspot interface. (May have already been configured by the GUI).
- **Action**: Enable a DHCP server to lease IP addresses to clients on the hotspot network.
- **Rationale**: This is necessary for client devices to get IP addresses automatically. This can be done by adding a DHCP server in the `hotspot` profile, or you can add it manually.

**CLI Example** (If not already created):
```mikrotik
/ip pool
add name=dhcp_pool_hotspot ranges=73.173.221.2-73.173.221.254
/ip dhcp-server
add address-pool=dhcp_pool_hotspot interface=ether-50 lease-time=10m name=dhcp-hotspot
/ip dhcp-server network
add address=73.173.221.0/24 gateway=73.173.221.1 dns-server=8.8.8.8,8.8.4.4
```
**Note**: The CLI example assumes you have not configured an address pool. The GUI configuration in Step 3 might have created an address pool automatically.

**Winbox GUI** (if not already created):
- If the server is already created, as mentioned in Step 3, check the `IP` -> `Pool` and `IP` -> `DHCP Server` lists for entries created for you.
- If they have not been created then:
 - Navigate to IP -> Pool
 - Click the "+" button
 - Name it `dhcp_pool_hotspot` and set the ranges to `73.173.221.2-73.173.221.254`
 - Click Apply and OK
 - Navigate to IP -> DHCP Server
 - Click the "+" button
 - Set the name to `dhcp-hotspot` and interface to `ether-50`
 - Set the Address Pool to `dhcp_pool_hotspot`
 - Navigate to the tab called `Networks`
 - Click the "+" button. Set the address to `73.173.221.0/24`, the gateway to `73.173.221.1` and add your desired DNS servers, e.g. `8.8.8.8,8.8.4.4`.
 - Click Apply and OK

**After:** Clients on the Hotspot network will receive IP addresses via DHCP.

## Complete Configuration Commands:

```mikrotik
/ip address
add address=73.173.221.1/24 interface=ether-50
/ip hotspot profile
add name=hotspot1  use-radius=yes html-directory=hotspot
/ip hotspot
add name=hotspot1  interface=ether-50 profile=hotspot1 address-pool=dhcp_pool_hotspot
/radius
add address=192.168.100.20 secret="your_radius_secret" service=hotspot timeout=3000
/ip pool
add name=dhcp_pool_hotspot ranges=73.173.221.2-73.173.221.254
/ip dhcp-server
add address-pool=dhcp_pool_hotspot interface=ether-50 lease-time=10m name=dhcp-hotspot
/ip dhcp-server network
add address=73.173.221.0/24 gateway=73.173.221.1 dns-server=8.8.8.8,8.8.4.4
```
**Parameter Explanation Table:**

| Command             | Parameter        | Value                       | Description                                                                                                  |
|----------------------|-------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------|
| `/ip address add`  | `address`        | 73.173.221.1/24            | IP address and subnet mask for the interface.                                                                  |
|                      | `interface`      | ether-50                   | The name of the interface.                                                                                   |
| `/ip hotspot profile add` | `name`         | hotspot1                  | Name of the Hotspot profile.                                                                                 |
|                      | `use-radius`    | yes                       | Enables RADIUS authentication.                                                                           |
|                      | `html-directory` | hotspot                   | Directory to store HTML files for the hotspot login pages.                                                    |
| `/ip hotspot add`   | `name`           | hotspot1                  | Name of the Hotspot server.                                                                                |
|                      | `interface`      | ether-50                   | The interface the hotspot will listen on.                                                                  |
|                      | `profile`        | hotspot1                   | The profile to use for the Hotspot.                                                                       |
|                      | `address-pool`   | dhcp_pool_hotspot  | The name of the address pool to lease out IP addresses                                                           |
| `/radius add`        | `address`        | 192.168.100.20             | IP address of the RADIUS server.                                                                              |
|                      | `secret`         | your_radius_secret          | Shared secret between MikroTik router and RADIUS server.                                               |
|                      | `service`        | hotspot                   | Specifies the RADIUS service for Hotspot.                                                                  |
|                      | `timeout`        | 3000                      | Timeout (in milliseconds) for RADIUS requests.                                                              |
| `/ip pool add`      | `name`           | dhcp_pool_hotspot         | Name of the address pool for the DHCP server.                                                                  |
|                      | `ranges`         | 73.173.221.2-73.173.221.254 | IP ranges to use for DHCP leasing.                                                                          |
| `/ip dhcp-server add` | `address-pool`   | dhcp_pool_hotspot | Name of the address pool created for the hotspot.                                                            |
|                      | `interface`      | ether-50          | The interface to use for DHCP.                                                              |
|                       | `lease-time`      | 10m |  The time for a lease, in minutes.   |
|                       | `name`   | dhcp-hotspot | The name to give the DHCP server.   |
| `/ip dhcp-server network add` | `address` | 73.173.221.0/24 | The network for the DHCP server. |
|               | `gateway` | 73.173.221.1 | The gateway address on the network. |
|               | `dns-server` | 8.8.8.8,8.8.4.4 | DNS servers to assign for the network. |

## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Shared Secret:** Ensure the secret on the MikroTik and RADIUS server match exactly.  Use Winbox or the CLI to verify this secret and update it if necessary.
    * **Troubleshooting:** Check `/radius print` and verify the secret is correct.  Try restarting the RADIUS server to ensure the changes are applied on that server.
*   **Firewall Issues:** Firewalls on either the MikroTik router or the RADIUS server can block communication.  Check the firewall on the router using `/ip firewall filter print`. Check any firewalls on your radius server.
    *   **Solution:** Make sure there is a firewall rule allowing UDP traffic on port 1812 (default RADIUS port).  You can add these to your router using the following cli commands:
    ```mikrotik
    /ip firewall filter
    add chain=input protocol=udp dst-port=1812 action=accept comment="Allow RADIUS"
    ```
*   **Incorrect RADIUS Server IP:** Verify that the IP address configured on the MikroTik router points to the correct RADIUS server.
    *   **Troubleshooting:** Use `ping <RADIUS_SERVER_IP>` on the MikroTik router to test basic reachability to the radius server.
*   **RADIUS Server Issues:**  Issues with the RADIUS server itself can prevent authentication.
    *   **Troubleshooting:** Check the RADIUS server logs for errors. Make sure the Radius server is set up to authenticate users on the network that you are trying to use.
*   **Resource Issues:** High CPU or memory usage on the MikroTik router can impact performance. Use the command `/system resource print` to check resources.
    *   **Solution:** If resource usage is high, make sure to not use features that you do not need. Reduce log verbosity or consider a more powerful router.
* **Hotspot Misconfiguration** If the hotspot is not working as expected, it could be that you have not configured a login method.
    * **Solution:** If you are using this as a method to authenticate users on your network, you may want to set up a walled garden of addresses. See the [Related Features and Considerations](#related-features-and-considerations) section for more information.

## Verification and Testing Steps:

*   **Connect a Client:** Connect a wireless device to the `ether-50` network (ensure it's connected to the correct SSID if you have a wireless access point connected to this interface).
*   **Login Page:**  You should be redirected to the Hotspot login page. This means your basic hotspot configuration is working. If you are not, you need to make sure the `walled garden` configuration is set correctly, see the section below.
*   **RADIUS Authentication:** Enter valid credentials (username and password) that are configured on your RADIUS server.
*   **Successful Authentication:** After successfully logging in, the client should have internet access.
*   **Failed Authentication:** If authentication fails, the client should not have internet access. Check the logs for the client and on the radius server to make sure the failure is not being reported on either side.
*   **RADIUS Logs:** Check the RADIUS server logs for authentication attempts, and success or failure reports.
*   **MikroTik Logs:** Check the MikroTik router's log for RADIUS-related events. In the winbox gui you can navigate to `System` -> `Logging` to view these. Make sure that `radius` is configured to be logged.

    **CLI Command to view logs:**
    ```mikrotik
    /log print follow-only where topics~"radius"
    ```
    This command will show a stream of log output, specifically those that relate to radius.

*   **Torch Tool:** Use the Torch tool (`/tool torch`) to check if there's traffic going between the MikroTik and the RADIUS server, specifically on port 1812 (UDP).
*  **Radius Client Status:** Use the command `/radius monitor print` to view the status of your radius client.
```mikrotik
[admin@MikroTik] > /radius monitor print
 #   ADDRESS         SECRET        SERVICE   STATUS  LAST-RESPONSE        FAIL-COUNT   TIMEOUT-COUNT
 0   192.168.100.20  *****        hotspot     up      2024-02-22 15:59:06        0                0

```

## Related Features and Considerations:

*   **Walled Garden:** You can configure a walled garden in Hotspot to allow access to specific sites or services without authentication. This is commonly used to allow access to the login page, before authenticating the user, as well as allowing access to common network services. This can be done with the following commands:
    ```mikrotik
    /ip hotspot walled-garden
    add dst-host="<DNS_OR_IP>"
    ```
    Repeat this command for each walled-garden address you would like to configure.
*   **Accounting:** Enable RADIUS accounting to track session usage. This requires enabling the `radius-accounting=yes` parameter in the hotspot profile as well as configuring the accounting port in the `/radius` section. The server also needs to be configured to receive accounting information.
*   **User Management:** RADIUS allows for centralized user management. This means that a user configured on the radius server will not need to be configured on the router. This includes configuration for bandwidth, timeouts, etc.
* **HTML Pages**: The html pages that a hotspot client is shown when they connect to a hotspot are customizable. These HTML files reside on the router, inside the `/hotspot` directory.  Make sure that you are familiar with HTML if you plan on modifying them.  This will give your hotspot page a customized look and feel.
* **Multiple RADIUS servers:** It is possible to set up multiple radius servers to provide redundancy, with the last server only being used if all the other radius servers fail. This can be done by adding multiple RADIUS servers, and the router will try them from top to bottom of the list.
*   **Session Limits:** You can set limits on user session duration on the RADIUS server.

## MikroTik REST API Examples:

The REST API for the RADIUS settings is available under the `/radius` path. Here are some examples.

**1. Get RADIUS server configuration:**
*   **Endpoint:** `/radius`
*   **Method:** `GET`
*   **Request:** None
*   **Example Response:**
```json
[
  {
    "address": "192.168.100.20",
    "secret": "your_radius_secret",
    "service": "hotspot",
    "timeout": "3000",
    ".id": "*0"
  }
]
```

**2. Add a new RADIUS server:**
*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **Request Payload (JSON):**
```json
{
  "address": "192.168.100.21",
  "secret": "new_secret",
  "service": "hotspot",
    "timeout": 3000
}
```
*   **Expected Response:**
    * Success: `201 Created`
    * Failure: Appropriate error code, such as `400 Bad Request` if invalid data was submitted.
*   **Error Handling:** If the API returns an error, check the response for error codes and messages. Common errors include missing parameters, incorrect values, or insufficient privileges.

**3. Update an existing RADIUS server:**
*   **Endpoint:** `/radius/<id>`, where `<id>` is the ID returned by a `GET` query, e.g. "*0"
*   **Method:** `PUT`
*   **Request Payload (JSON):**
```json
{
  "secret": "updated_secret",
    "timeout": 5000
}
```
*   **Expected Response:**
    * Success: `200 OK`
    * Failure: Error code with a message.
*   **Error Handling:** Check response for status codes such as `404 Not Found` if the specified id doesn't exist.

**4. Delete a RADIUS server:**
*   **Endpoint:** `/radius/<id>`
*   **Method:** `DELETE`
*   **Expected Response:**
    * Success: `204 No Content`
    * Failure: Error code with a message.
*   **Error Handling:** Handle errors like `404 Not Found`.

**Note:** Ensure that you have REST API enabled on your MikroTik router. Refer to the MikroTik documentation on how to enable and use the REST API. The Mikrotik API does not use a Bearer token or Oauth to authenticate. Instead you need to use basic authentication. Ensure that you are using SSL when using the API to transmit the user credentials.  Use a library to handle the authentication headers for you (python-requests or similar).

## Security Best Practices:

*   **Secure RADIUS Secret:** The RADIUS secret must be a strong, complex password. Keep this secret confidential.
*   **RADIUS Server Security:** Harden the RADIUS server. Restrict access to the RADIUS server using firewall rules.
*   **Monitor Logs:** Regularly monitor RADIUS server and MikroTik logs for unusual activity.
*   **Use Encryption:** If possible, use encrypted communication between the router and the RADIUS server (e.g., RADIUS over TLS).
*  **Update RouterOS:** Keep RouterOS updated to ensure all the latest security patches are installed.
* **Avoid default credentials:** If possible, make sure that the default credentials for your router are changed.
* **Use a custom port for the HTTP service:** Ensure that you are using a non-standard port for the HTTP service for web access on the router.
* **Limit user access to the router**: Make sure that the number of users able to access the router directly is limited to people that absolutely need access.
* **Do not use HTTP access on the Router:** If possible, always use HTTPS when accessing the router through a web browser or through the api.

## Self Critique and Improvements:

*   **Complexity:** This configuration is relatively basic. For more complex scenarios, you might need to use features like accounting, custom attributes, and different authentication methods, including MAC authentication.
*   **Error Handling:** The documentation highlights basic error handling. More complex checks and recovery mechanisms could be implemented (such as connection retry policies, or testing if the radius is reachable).
*   **Scalability:** For larger scale environments, you would want to make sure to use multiple routers. This can be done by setting up multiple wireless access points, or by using VLANs.
* **Redundancy:** To add redundancy you will need to use more than 1 router and multiple radius servers. There is an option to have a backup radius server in the configuration, but this will only be activated if the main radius server fails completely.
* **API Examples:** The API section is a basic overview. More sophisticated API operations, such as batch updates or complex queries, could be added. The API will require basic authentication and will send credentials on each request, this may cause some security issues if the API is not accessed using secure communication methods (HTTPS).

**Improvements:**

*   **Detailed error handling:** Add specific examples of API failure responses, and suggestions to fix the issues.
*   **Detailed Scalability and Redundancy:** Add a description on how to increase the capacity and redundancy of the configuration by adding additional devices or configuring multiple radius servers.
*   **Advanced Features:** Include examples for RADIUS accounting and different authentication options (e.g. MAC address auth).

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users who connect to a network. The RADIUS protocol is most commonly used to provide authentication for internet hotspots, or for authentication for VPN servers.

**How it works:**
1.  **Authentication:** When a user tries to connect to a network using a service such as a Hotspot, the router that they are connecting through will send the credentials that the user supplied to the RADIUS server. The RADIUS server will then check these credentials to verify that the user is authorized to access the network. If the credentials are correct, the RADIUS server will return a positive response to the router. If the credentials are not correct, the server will respond with a negative response.
2.  **Authorization:** Once the authentication is successful, the RADIUS server may provide other information to the router, such as the access level that the user should have on the network, and other session related information.
3.  **Accounting:** After the user's session has started the router will also send accounting messages to the radius server, this may include the time the user connected, data usage, etc. This is usually used for billing or other types of statistics.

**Key Components:**
*   **RADIUS Server:** A server that stores user credentials, handles user authentication requests, and provides authorization and accounting information. The RADIUS server must be properly configured in order to provide this functionality.
*   **RADIUS Client:** A network device (such as a MikroTik router) that sends authentication requests to the RADIUS server. The RADIUS client should be configured to talk to the radius server.
*   **Shared Secret:** A password that is used to establish a secure communication channel between the RADIUS client and server. This should be kept safe and confidential.

**Benefits of RADIUS:**

*   **Centralized User Management:** RADIUS allows you to manage all your users from a single point, making it easier to add, remove, or modify user credentials.
*   **Increased Security:** RADIUS adds a layer of security to your network by ensuring that only authorized users can connect.
*   **Flexibility:** RADIUS is a flexible protocol that supports different authentication methods and can be customized to meet your specific needs.
*   **Scalability:**  RADIUS can be scaled to manage networks of different sizes.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:**  Simpler to set up, suitable for small networks with few users. User accounts are stored on the router.
    *   **RADIUS:** More complex setup, requires a separate server, but offers centralized user management, which is ideal for larger networks and organizations.
*   **Plain Text vs. Encrypted Passwords:**
    *   **Plain Text:** Easier to configure, but less secure.
    *   **Encrypted Passwords:** More complex to set up, but significantly more secure.
*  **Local vs Remote DHCP:**
   * **Local DHCP**:  Easier to setup. All DHCP settings are local to the router. DHCP scope is restricted to the subnet on the router. This is better for simple configurations and limited user groups.
   * **Remote DHCP**:  Requires a separate DHCP server. You can use any DHCP server on the network. This allows the router to be easily replaced without reconfiguring DHCP. This allows you to have larger networks, with different subnets.
*   **Basic vs. Advanced RADIUS:**
    *   **Basic:** Simple authentication setup, sufficient for most scenarios with basic user authentication.
    *   **Advanced:** Offers features like session accounting, complex policies, VLAN assignments, and user roles. Use when more sophisticated management is needed.

Trade-offs on features depend on the complexity and scale of the network, and the security requirements. A smaller network might find local authentication more convenient, while larger networks can benefit from the central management and security of the RADIUS server.  These trade-offs depend on the specific situation and requirements.

## Configuration for Specific RouterOS Versions:

The provided configuration is for RouterOS 7.11 (or later). Most of it is also compatible with RouterOS 6.48. If you are using RouterOS 6.x, you may need to adjust some command parameters, but the functionality and logic will remain the same.

**RouterOS 6.x considerations**
* `/ip hotspot user` command is used to create and manage users locally, and that interface also has a `use-radius` parameter that should be set to `yes`
* The API is available on 6.x, but some of the fields might differ, check the official documentation.

**Important Notes:**

*   Always backup your RouterOS configuration before making major changes using the `/system backup save name=backup.rsc` CLI command or winbox GUI.
*   Testing configuration changes on a test setup or during off-peak hours before production is strongly recommended.
*   Be sure to configure the RADIUS server to accept connections from your MikroTik Router's IP address and configure user information on the RADIUS server.
*   Make sure that you have network access to your radius server.

This comprehensive documentation should help you get started with RADIUS authentication on your MikroTik router. If you have any specific questions, feel free to ask!
