Okay, let's dive into a detailed RADIUS configuration on a MikroTik router (RouterOS 7.11, but largely applicable to 6.48 and 7.x). We'll focus on the basics, using your provided subnet and interface.

## Scenario Description:

This configuration will set up a MikroTik router to act as a RADIUS client, forwarding authentication requests to a RADIUS server for users attempting to access resources on the subnet `139.16.121.0/24`. We will configure the router to use the `ether-57` interface as the connection to the RADIUS server and also assume we will be doing PPPoE authentication from the given subnet. This setup is typical in a small to medium-sized ISP or a network where centralized authentication is desired, and we are using PPPoE for a very basic access scenario.

## Implementation Steps:

Here's a step-by-step guide, with examples, explanations, and effects of each step:

### Step 1: Add RADIUS Server Configuration

*   **Purpose:** Define the RADIUS server's IP address, secret, and port. This is essential for the router to communicate with the server.
*   **Before Configuration:**
    ```
    [admin@MikroTik] > /radius print
    Flags: X - disabled
    #   ADDRESS         SECRET           SERVICE     AUTHENTICATION    ACCOUNTING       TIMEOUT   SRC-ADDRESS
    ```
    (Typically, no RADIUS servers are configured by default.)
*   **MikroTik CLI Command:**
    ```mikrotik
    /radius add address=192.168.88.10 secret="ThisIsMySecret" service=ppp timeout=10 src-address=139.16.121.1
    ```
    *   `address`: The IP address of your RADIUS server (replace `192.168.88.10` with the actual address).
    *   `secret`: The shared secret used for communication between the router and the RADIUS server (replace `ThisIsMySecret` with your actual secret).
    *   `service`: The service type for which RADIUS will be used (`ppp` in this case for PPPoE).
    *   `timeout`: The time (in seconds) the router will wait for a response from the RADIUS server before considering it unreachable.
    *   `src-address`: The source IP address used to send requests to the RADIUS server. This can be a specific IP address or the IP of a chosen interface.
*   **Winbox GUI Equivalent:**
    *   Go to `RADIUS` in the left menu.
    *   Click the `+` button to add a new entry.
    *   Enter the RADIUS server `Address`, `Secret`, and set `Service` to `ppp`.
    *   Set the `Timeout` and `Source Address` in the `General` tab.
*   **After Configuration:**
    ```
    [admin@MikroTik] > /radius print
    Flags: X - disabled
    #   ADDRESS         SECRET           SERVICE     AUTHENTICATION    ACCOUNTING       TIMEOUT   SRC-ADDRESS
    0   192.168.88.10  *               ppp         yes               no               10s        139.16.121.1
    ```
*   **Effect:** The router now knows where to send RADIUS authentication requests.

### Step 2: Enable and Configure PPPoE Server Interface

*   **Purpose:** Set up the PPPoE server on the `ether-57` interface. This will be the endpoint for PPPoE clients requesting access, which will then have the authentication forwarded to RADIUS.
*   **Before Configuration:**
    ```mikrotik
    /interface pppoe-server print
    Flags: X - disabled, D - dynamic
    #    NAME                                   INTERFACE       MAX-MTU MAX-MRU KEEP-ALIVE  SERVICE-NAME
    ```
    (By default, no PPPoE server configurations exist.)
    ```mikrotik
    /interface print
    Flags: D - dynamic, X - disabled, R - running, S - slave
     #    NAME                                TYPE         MTU   L2MTU   MAX-L2MTU
     ...
     57   ether-57                            ether        1500  1598  10238
     ...
    ```
    (The `ether-57` interface is assumed to be present)
*   **MikroTik CLI Command:**
    ```mikrotik
    /interface pppoe-server add interface=ether-57 service-name=pppoe-access default-profile=default-encryption
    ```
    *   `interface`: The interface on which to create the PPPoE server (`ether-57`).
    *   `service-name`: A name for the PPPoE server (e.g., `pppoe-access`).
    *   `default-profile`: The profile that will be assigned to the users authenticated via PPPoE. The profile `default-encryption` is a reasonable default to start with for simplicity and will be explained in `Common Pitfalls and Solutions`.
*   **Winbox GUI Equivalent:**
    *   Go to `PPP` then `PPPoE Servers`.
    *   Click the `+` button to add a new entry.
    *   Select `ether-57` as the interface, and provide a suitable `Service Name`.
    *   Set the `Default Profile`.
*   **After Configuration:**
    ```mikrotik
    /interface pppoe-server print
    Flags: X - disabled, D - dynamic
    #    NAME                  INTERFACE       MAX-MTU MAX-MRU KEEP-ALIVE  SERVICE-NAME
    0    pppoe-access        ether-57        1480    1480    10             pppoe-access
    ```
*   **Effect:** A PPPoE server is enabled, listening for client requests on `ether-57`.

### Step 3: Configure a PPP Profile with RADIUS Authentication

*   **Purpose:** Modify the `default-encryption` profile to use RADIUS for authentication.
*   **Before Configuration:**
    ```mikrotik
    /ppp profile print
     Flags: * - default
     #   NAME                   LOCAL-ADDRESS REMOTE-ADDRESS   USE-ENCRYPTION  ONLY-ONE    CHANGE-TCP-MSS
     0 * default              10.0.0.1       10.0.0.2-10.0.0.254  no              no          yes
     1 * default-encryption   10.0.0.1       10.0.0.2-10.0.0.254  yes             no          yes
    ```
*   **MikroTik CLI Command:**
    ```mikrotik
    /ppp profile set default-encryption use-radius=yes
    ```
    *   `use-radius`: Enables RADIUS authentication for this profile.
*   **Winbox GUI Equivalent:**
    *   Go to `PPP` then `Profiles`.
    *   Select the `default-encryption` profile.
    *   Check the `Use RADIUS` box in the `General` tab.
*   **After Configuration:**
    ```mikrotik
    /ppp profile print
     Flags: * - default
     #   NAME                   LOCAL-ADDRESS REMOTE-ADDRESS   USE-ENCRYPTION  ONLY-ONE    CHANGE-TCP-MSS
     0 * default              10.0.0.1       10.0.0.2-10.0.0.254  no              no          yes
     1 * default-encryption   10.0.0.1       10.0.0.2-10.0.0.254  yes             no          yes   RADIUS
    ```
*   **Effect:** PPPoE clients connecting with this profile will now be authenticated by the RADIUS server before access is granted.

## Complete Configuration Commands:

Here's a full set of commands for your convenience:

```mikrotik
/radius
add address=192.168.88.10 secret="ThisIsMySecret" service=ppp timeout=10 src-address=139.16.121.1
/interface pppoe-server
add interface=ether-57 service-name=pppoe-access default-profile=default-encryption
/ppp profile
set default-encryption use-radius=yes
```

**Parameter Explanations:**

| Command           | Parameter      | Explanation                                                                        |
|-------------------|----------------|------------------------------------------------------------------------------------|
| `/radius add`       | `address`      | The IP address of the RADIUS server.                                                |
|                   | `secret`       | The shared secret used for authentication with the RADIUS server.                   |
|                   | `service`      | The service type for RADIUS authentication (e.g., `ppp`).                             |
|                   | `timeout`      | The timeout period in seconds for waiting for a response from the RADIUS server.     |
|                   | `src-address`      | The source IP address used for requests to the RADIUS server.                  |
| `/interface pppoe-server add` | `interface`    | The interface on which to create the PPPoE server.                             |
|                                  | `service-name` | A name for the PPPoE server instance.                                         |
|                                  | `default-profile` | The PPPoE profile to use for connecting clients.                                   |
| `/ppp profile set` | `use-radius`   |  Enable RADIUS authentication for this profile (`yes` or `no`).                    |

## Common Pitfalls and Solutions:

*   **Secret Mismatch:**
    *   **Problem:** If the secret on the MikroTik doesn't match the one on the RADIUS server, authentication will fail.
    *   **Solution:** Double-check the secret in both places. Use a strong, complex secret.
*   **RADIUS Server Unreachable:**
    *   **Problem:** If the RADIUS server is down or unreachable, users won't be able to authenticate.
    *   **Solution:** Verify network connectivity between the MikroTik and the RADIUS server. Use tools like `ping` or `traceroute`. Ensure that there are no firewalls blocking the connection on the MikroTik side or the server.
*   **Firewall Issues:**
    *   **Problem:** The MikroTik firewall may be blocking RADIUS communication (UDP ports 1812/1813 or 1645/1646).
    *   **Solution:** Add firewall rules to allow traffic to and from the RADIUS server. In a default setup, this is typically not an issue.
    *   **Example:**
    ```mikrotik
    /ip firewall filter
    add chain=input protocol=udp dst-port=1812,1813 action=accept comment="Allow RADIUS auth"
    add chain=output protocol=udp dst-port=1812,1813 action=accept comment="Allow RADIUS auth"
    ```
*   **Incorrect Service Type:**
    *   **Problem:** If the service type in RADIUS configuration doesn't match the service used for connection requests, authentication can fail.
    *   **Solution:** Ensure that the service type in the `radius add` command (`ppp` in this case) matches how you are trying to use RADIUS.
*   **Default Encryption Profile Issues:**
    *   **Problem:** The `default-encryption` profile has a default local address of `10.0.0.1` which might not be appropriate for your needs. Also, the addressing and other settings might not match your requirements.
    *   **Solution:** Create a custom profile (instead of modifying the default) which will allow you to set the local and remote addressing, timeouts, session limits, and other needed values. This can be done by creating a new profile with `add`, and modifying it to your specific requirements.
    *   **Example:**
        ```mikrotik
        /ppp profile
        add name=my-pppoe-profile local-address=192.168.10.1 remote-address=192.168.10.2-192.168.10.254 use-encryption=yes change-tcp-mss=yes only-one=no use-radius=yes
        /interface pppoe-server set 0 default-profile=my-pppoe-profile
        ```
        Here, we have made `my-pppoe-profile`, set up its address range, enabled encryption and enabled RADIUS, then set the pppoe-server to use this profile.
*   **Resource Issues:**
    *   **Problem:** High number of users can lead to high CPU usage, especially if complex filters and configurations are in place.
    *   **Solution:** Monitor router CPU and memory usage. Optimize the router configuration, and potentially consider more powerful hardware if the need requires it.
*   **RADIUS Server not configured for Accounting:**
    *   **Problem:** The current setup does not include RADIUS Accounting configuration. This means the router will not track start/stop of connections.
    *   **Solution:** Enable accounting on the RADIUS Server, and enable it on the MikroTik:
        ```mikrotik
        /radius set 0 accounting=yes
        ```
        On the RADIUS Server, make sure accounting is enabled and will generate logs and/or statistics.

## Verification and Testing Steps:

1.  **Attempt PPPoE Connection:**
    *   Use a client device (computer) configured for PPPoE.
    *   Try to connect using credentials that you've configured on the RADIUS server.
2.  **Monitor Logs:**
    *   Use `/log print follow-only where topics~"radius|ppp"` in the MikroTik CLI to view RADIUS and PPP logs in real-time.
    *   Check the logs on your RADIUS server for successful authentication attempts or errors.
3.  **Check Active Connections:**
    *   Use `/ppp active print` in the MikroTik CLI to verify that the client connected.
4.  **Use `torch` to Monitor RADIUS Traffic:**
    *   Use `/tool torch interface=ether-57 protocol=udp port=1812,1813` to monitor RADIUS traffic flowing on the configured interface.
5.  **Use `/tool/profile`:**
   *   Run `/tool/profile` to check the resource usage for pppoe. This will let you know if this activity is causing a strain on the device.

## Related Features and Considerations:

*   **RADIUS Accounting:** Enable RADIUS accounting to track connection times and data usage. This will add another layer of data. Enable this on the RADIUS configuration using `accounting=yes` on the `/radius set` command.
*   **User Profiles:** Create more detailed user profiles on the RADIUS server for granular control over bandwidth, access times, and more.
*   **VLANs:** Use VLAN tagging on the `ether-57` interface if you need to segregate traffic into multiple networks.
*   **Hotspot:** If you need captive portal functionality, consider using MikroTik's Hotspot feature in combination with RADIUS.
*  **Rate Limiting:** You can use profiles for granular rate limiting, this includes per-user or global limits.

## MikroTik REST API Examples:

While the core RADIUS configuration doesn't directly support advanced REST API operations, we can use the API to retrieve the existing configuration or make basic changes. Here are some examples:

**Get Existing RADIUS Configuration:**

*   **API Endpoint:** `/radius`
*   **Request Method:** `GET`
*   **Example using cURL:**
    ```bash
    curl -k -u 'api:password' https://192.168.88.1/rest/radius
    ```
*   **Example Response:**
    ```json
    [
        {
            ".id": "*0",
            "address": "192.168.88.10",
            "secret": "ThisIsMySecret",
            "service": "ppp",
            "timeout": "10",
             "src-address":"139.16.121.1"
        }
    ]
    ```
    * The parameter `.id` is the unique identifier for this entry.
* **Description of Fields:**
    *   `.id`: Unique ID.
    *   `address`: The IP address of the RADIUS server.
    *   `secret`: The shared secret, will not be shown by default, if you change it via API, use `"secret":"newsecret"`.
    *   `service`: The service type for RADIUS (`ppp`).
    *   `timeout`: Timeout in seconds.
        * `src-address`: The source IP address used to send requests to the RADIUS server.
**Change the Timeout of a RADIUS Server Configuration**

*   **API Endpoint:** `/radius/*0` (or the actual ID you want to modify)
*   **Request Method:** `PUT`
*   **Example using cURL:**
    ```bash
    curl -k -u 'api:password' -H "Content-Type: application/json" -X PUT  -d '{"timeout":"20"}' https://192.168.88.1/rest/radius/*0
    ```
*   **Example Response:**
    ```json
        {
        ".id": "*0",
        "address": "192.168.88.10",
        "secret": "ThisIsMySecret",
        "service": "ppp",
        "timeout": "20",
        "src-address":"139.16.121.1"
       }
    ```
    *   The server sends the object back that was updated.
* **Description of Fields:**
     *   `.id`: Unique ID.
        * `timeout`: Timeout in seconds.
*   **Error Handling:**
    *   If there's an error (e.g., invalid ID or bad JSON), the API will return an HTTP error code and a JSON error response. Make sure to check the HTTP status codes, and if you have trouble finding the source of the error, enable more verbose logging.
**Create a new Radius configuration**
* **API Endpoint:** `/radius`
* **Request Method:** `POST`
* **Example using cURL:**
    ```bash
        curl -k -u 'api:password' -H "Content-Type: application/json" -X POST  -d '{"address":"192.168.88.11","secret":"AnotherSecret","service":"ppp","timeout": "20", "src-address":"139.16.121.1"}' https://192.168.88.1/rest/radius
    ```
* **Example Response:**
     ```json
    {
      ".id": "*1",
      "address": "192.168.88.11",
      "secret": "AnotherSecret",
      "service": "ppp",
      "timeout": "20",
     "src-address":"139.16.121.1"
    }
    ```
    *   The server sends back the object that was created with the .id key that was assigned.

**Note**: Replace `192.168.88.1` with your router's IP address and `'api:password'` with a user that has API access.

## Security Best Practices

*   **Use a Strong RADIUS Secret:** Use a randomly generated, long secret key.
*   **Restrict RADIUS Server Access:** Allow only the MikroTik router(s) to access your RADIUS server via firewall rules.
*   **Monitor RADIUS Traffic:** Implement a monitoring system and regularly review logs for unusual authentication attempts.
*   **Regularly Update RouterOS:** Keep your RouterOS up to date to protect against known vulnerabilities.
*   **Use HTTPS for API access:** When accessing the MikroTik using the API, use HTTPS to ensure confidentiality of data in transit.
*   **API User with limited access:** If an api user is needed, make sure that it does not have full access to the system.

## Self Critique and Improvements

*   **Simplicity:** This configuration is basic, and assumes a very simple network with few end users connecting. More advanced configurations will likely involve VLAN tagging, custom user profiles, accounting, and maybe even more complex firewall configurations.
*   **Hardcoded Values:** The IP addresses for the RADIUS server are hardcoded. This should ideally be a dynamic or centralized method of assigning and managing these addresses.
*  **No Real-Time Monitoring:** The configuration relies mostly on static verification. An active monitoring setup should be in place for real-world deployments.
*   **Scalability:** The configuration lacks a discussion of how it might scale up or out. More information could be included on how to manage this setup in a larger network with many devices.
*   **Error Handling:** While some errors were discussed, a deeper approach could be given into error checking for authentication failures.

**Improvements:**

*   Implement more comprehensive security measures such as IPsec between the router and the RADIUS server.
*   Create a setup script or automation for configuring multiple routers in a repeatable way.
*   Add discussion on how to integrate this configuration into a more complex infrastructure.
*   Describe RADIUS attributes that can be passed to the clients.
*   Discuss the process of using more advanced features like RADIUS Proxy.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):**

*   RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users accessing network resources.
*   **Authentication:** Verifying a user's identity by checking their username and password against a database.
*   **Authorization:** Determining what network resources a user is allowed to access after successful authentication.
*   **Accounting:** Tracking network usage, such as connection times and data transfers.
*   **RADIUS Server:** A central server storing user authentication and authorization data.
*   **RADIUS Client:** The device (such as our MikroTik router) that forwards authentication requests to the RADIUS server.
*   **How It Works:** When a user attempts to connect, the client sends authentication credentials to the RADIUS server. If the credentials match the server’s data, the server sends an acceptance back to the router. The router can then grants the user access based on the server's response. RADIUS usually uses UDP on port 1812 for authentication and 1813 for accounting. Sometimes the old ports (1645 and 1646) are used as well, depending on the configuration.

## Detailed Explanation of Trade-offs:

* **Local vs RADIUS Authentication:**
   *   **Local (On MikroTik):** Simple for small networks. User accounts are directly on the router. It's easy to set up, but it does not scale well and you can only use the functions that are offered on the device.
   *  **RADIUS:** Requires a separate RADIUS server. Much better for scalability, central user management, and provides much more flexible options and reporting. There are more points of failure and more complexity to set up and maintain.
* **UDP vs TCP:**
   *   **RADIUS Uses UDP:** UDP is connectionless, and therefore very fast. However, that means that the transport layer does not guarantee delivery. Retries are typically implemented in the RADIUS protocol if a packet is lost.
   *  **Possible Use of TCP:** It is technically possible to use TCP for RADIUS, but is not recommended because of the added overhead and complexity. This might help if UDP gets blocked by a firewall, but it does not solve the issue that the device cannot communicate with the RADIUS server.
* **Default Profile vs Custom Profile:**
    * **Default Profile:** Quick start, good for testing. It has pre-set options that might not be suitable for production.
    *  **Custom Profile:** Allows fine-grained control over settings like local/remote addresses, encryption, connection times and can be assigned per client/user based on RADIUS attributes.
*   **Complexity vs Maintainability:**
    *   A more advanced setup may give you better control and security. However, a more simple solution is more maintainable and easier to troubleshoot.

## Configuration for Specific RouterOS Versions:

The provided commands and configurations are primarily compatible with RouterOS 7.11, but should generally work on versions 6.48 and 7.x. Some older versions of 6.x may have slightly different command syntaxes, but the main concepts remain the same.

*   **For older 6.x versions:** check the documentation as sometimes commands are different from newer versions.

I hope this detailed documentation is helpful! Let me know if you have more questions or need further clarification.
