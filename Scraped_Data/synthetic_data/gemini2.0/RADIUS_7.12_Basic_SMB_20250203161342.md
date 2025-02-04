Okay, let's dive into configuring RADIUS on MikroTik RouterOS 7.12 for a basic SMB network scenario, targeting the provided subnet and interface.

## Scenario Description:

We are setting up a MikroTik router to authenticate users connecting to the network using RADIUS.  This is commonly used for wireless access points, VPN servers, or other services that require user authentication. We'll configure the MikroTik router to communicate with a RADIUS server to validate user credentials. The connection will be initiated from the interface `bridge-95`, which resides on the `112.40.168.0/24` subnet. The authentication requests will be sent to a RADIUS server with the IP address `192.168.88.10` and secret `my_secret_radius`.

## Implementation Steps:

Here's a step-by-step guide, including CLI examples and explanations, to configure RADIUS on your MikroTik router:

**1. Step 1: Create the `bridge-95` interface and configure IP address.**

   *   **Purpose:** We'll first ensure that the interface `bridge-95` exists and is assigned an IP address within the subnet. This is necessary for the MikroTik router to be reachable on the network.

   *   **Before:** We assume `bridge-95` may or may not exist. If it exists, it may have a different IP configuration.

   *   **CLI Example (Create bridge interface if it doesn't exist):**
        ```mikrotik
        /interface bridge
        add name=bridge-95
        ```

   *   **CLI Example (Set an IP Address on bridge-95):**
        ```mikrotik
        /ip address
        add address=112.40.168.1/24 interface=bridge-95
        ```
    *  **Explanation:**
       *   `/interface bridge add name=bridge-95` : Creates a new bridge interface named `bridge-95` if it doesn't already exist.
       *   `/ip address add address=112.40.168.1/24 interface=bridge-95` assigns the IP address `112.40.168.1` with a subnet mask of `/24` to the `bridge-95` interface. You may need to adjust if you have a different existing IP setup.

   *  **After:**
        *   The interface `bridge-95` will be created if it did not exist.
        *   The `bridge-95` interface will have the IP `112.40.168.1/24` assigned to it.
        *   The interface will be active.
   *   **Winbox GUI:** This can be done under `Bridge` and `IP/Addresses`.  If `bridge-95` does not exist create it in `Bridge`, then in `IP/Addresses`, press the "+" button, add the address and select the `bridge-95` interface.

**2. Step 2: Configure the RADIUS Server.**

   *   **Purpose:** This step defines the RADIUS server details that the MikroTik will use for authentication.

   *   **Before:** No RADIUS server is configured.

   *   **CLI Example:**
      ```mikrotik
      /radius
      add address=192.168.88.10 secret=my_secret_radius service=ppp,login,hotspot,wireless
      ```
   *   **Explanation:**
        *  `/radius add`: Starts the RADIUS server configuration.
        *   `address=192.168.88.10`: Specifies the IP address of the RADIUS server.
        *   `secret=my_secret_radius`: Sets the shared secret key used to authenticate the MikroTik router with the RADIUS server. Ensure this matches the secret configured on your RADIUS server.
        *  `service=ppp,login,hotspot,wireless`: Defines the services for which this RADIUS server will be used. Here we configure it for common uses such as `ppp` for PPPoE, `login` for router login, `hotspot` for Hotspot functionality, and `wireless` for wireless user authentication. You can restrict this to only the needed services.

   *  **After:** The MikroTik router now has a defined RADIUS server.

   *  **Winbox GUI:** You can perform this under `RADIUS` menu. Press the "+" button to add a new RADIUS server, then fill in `Address`, `Secret` and select the services.

**3. Step 3: Configure a service to use RADIUS (Example: PPP).**

   *   **Purpose:** Here, we will demonstrate how to use this RADIUS configuration in the PPP service for demonstration.

   *   **Before:** PPP authentication is using local users or no authentication.

   *   **CLI Example:**
       ```mikrotik
       /ppp profile
       set default use-radius=yes
       ```
   *   **Explanation:**
      *   `/ppp profile`: Selects the PPP profile settings.
       *   `set default use-radius=yes`: Modifies the default PPP profile to use RADIUS for authentication.

   *   **After:** PPP connections using the default profile will attempt to authenticate against the configured RADIUS server.

   *   **Winbox GUI:** Navigate to `PPP/Profiles`. Select the `default` profile and enable the `Use RADIUS` option.

**Important Note:** This step uses the default profile. In a real world application, you will likely want to create a specific profile for RADIUS authentication and attach the profile to your desired PPP server. This provides flexibility in applying specific settings to a particular group of users.

**4. Optional Step: RADIUS Accounting**

  * **Purpose:** If you want to track user connection information such as session start, stop, and data usage you can enable accounting.
  * **Before:** RADIUS Accounting is not used.
  * **CLI Example:**
    ```mikrotik
    /radius
    set [find address="192.168.88.10"] accounting=yes
    ```
   * **Explanation:**
       *  `/radius set [find address="192.168.88.10"] accounting=yes`: Enables accounting for the RADIUS server with the address `192.168.88.10`.
  *  **After:** The MikroTik router will now send accounting information to the RADIUS server when authentication occurs. This assumes that the RADIUS server is configured to accept such data.
  *  **Winbox GUI:** Select the added server in the `Radius` menu, click `Advanced` and check `Accounting`.

## Complete Configuration Commands:

```mikrotik
/interface bridge
add name=bridge-95
/ip address
add address=112.40.168.1/24 interface=bridge-95
/radius
add address=192.168.88.10 secret=my_secret_radius service=ppp,login,hotspot,wireless
/ppp profile
set default use-radius=yes
/radius
set [find address="192.168.88.10"] accounting=yes
```

## Common Pitfalls and Solutions:

*   **Incorrect Secret:** The most common issue is an incorrect secret shared between the MikroTik and the RADIUS server.
    *   **Solution:** Double-check that the `secret` configured in `/radius` matches the RADIUS server's shared secret exactly.
*   **Firewall Blocking RADIUS:**  MikroTik firewall might block UDP ports `1812` and `1813` (authentication and accounting respectively).
    *   **Solution:** Add firewall rules to allow communication to the RADIUS server IP address on UDP ports `1812` and `1813`. Example:

        ```mikrotik
        /ip firewall filter
        add chain=output dst-address=192.168.88.10 protocol=udp dst-port=1812,1813 action=accept
        ```
*  **RADIUS Server Not Reachable:** The MikroTik router cannot reach the RADIUS server due to a routing issue, connectivity problem, or firewall in between.
     *  **Solution:** Verify network connectivity using `ping 192.168.88.10` and `traceroute 192.168.88.10`. Check firewall rules on the MikroTik router and any devices between the router and the RADIUS server.
*  **Incorrect Service Selection:** Selecting the wrong `service` parameter in the `/radius` configuration can prevent authentication for certain user requests.
    * **Solution:** Ensure the `service` parameter contains all relevant services using the RADIUS server for authentication.
* **RADIUS server is misconfigured**
    * **Solution:** Check the RADIUS server logs for errors or misconfiguration.
* **High CPU or Memory usage:**
     *  **Solution:**  RADIUS itself does not require high CPU usage unless there is an unusually high number of authentication requests in a short period of time. If there is, investigate further using `/tool profile` or `/system resource monitor`. Memory usage should also be observed for the service and optimized where needed.

## Verification and Testing Steps:

1.  **Ping the RADIUS Server:** Ensure basic connectivity.
    ```mikrotik
    /ping 192.168.88.10
    ```

2.  **Monitor Logs:** Check the MikroTik logs for authentication attempts and errors related to RADIUS.
    ```mikrotik
     /log print follow-only where topics~"radius"
    ```
3.  **Test with a PPP Connection:** Try to establish a PPP connection using the default profile. If you setup a specific profile, ensure you use it here.  If the authentication is successful you will see logs on the router (via the previous step), and hopefully on your radius server logs.
    *   **Note:** You will need a RADIUS server configured with valid usernames and passwords matching the used for the test. You can create these in a variety of RADIUS management interfaces and databases.
    *   **Winbox:** The output from the log is viewable under the `Log` window.
4. **RADIUS Client testing tools:** Several tools such as `radtest` can be used to simulate a RADIUS authentication and account request.

## Related Features and Considerations:

*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy, specifying priorities for failover using the `priority` argument in `/radius`.
*   **RADIUS Attributes:** MikroTik supports many RADIUS attributes that can be used to pass back settings to the user/client or for more specific authentication or authorization.
*   **Dynamic VLAN Assignment:** RADIUS can be used to dynamically assign VLANs based on the user’s identity. This provides an extra layer of network security by isolating devices in specific networks based on their users.
*   **Hotspot integration:** MikroTik hotpsots integrate well with RADIUS servers.
*   **Rate Limiting:** RADIUS can provide per user rate limits to enforce bandwidth consumption restrictions.
*   **Authentication Methods:** MikroTik supports various authentication methods (PAP, CHAP, MSCHAPv2) for PPP connections, in conjunction with RADIUS.

## MikroTik REST API Examples:

These examples assume that the router is reachable on `https://192.168.88.1` and you have API credentials. Adjust as necessary for your specific environment.

**Example 1: Get RADIUS Server List**

*   **Endpoint:** `https://192.168.88.1/rest/radius`
*   **Method:** GET
*   **Request Body:** None
*   **Expected Response:** JSON array of RADIUS server configurations.
    ```json
    [
      {
        ".id": "*1",
        "address": "192.168.88.10",
        "secret": "my_secret_radius",
        "service": "ppp,login,hotspot,wireless",
        "timeout": "3000",
        "accounting": "yes"
      }
    ]
    ```

**Example 2: Create a new RADIUS server**

*   **Endpoint:** `https://192.168.88.1/rest/radius`
*   **Method:** POST
*   **Request Body:**
    ```json
    {
        "address": "192.168.88.20",
        "secret": "new_secret",
        "service": "ppp,hotspot",
        "timeout": "3000",
        "accounting": "no"
    }
    ```
* **Expected Response:**
    ```json
    {
      ".id": "*2"
    }
    ```
* **Explanation:**
    * `.id`: The ID of the new radius server.
* **Error Handling:** Check HTTP error codes for errors, such as `400 Bad Request` for invalid parameters, or `401 Unauthorized` for missing or bad credentials. Catch exceptions and print the errors.

**Example 3: Modify an existing RADIUS server**

*   **Endpoint:** `https://192.168.88.1/rest/radius/*1`
*   **Method:** PATCH
*   **Request Body:**
    ```json
    {
      "secret": "new_secret_radius",
      "timeout": "5000"
    }
    ```
*   **Expected Response:** Empty body `204 No Content`.
*   **Explanation:**  Uses the `.id` from Example 1 to identify the server to be modified.
* **Error Handling:** Check HTTP error codes for errors, such as `400 Bad Request` for invalid parameters, or `401 Unauthorized` for missing or bad credentials. Catch exceptions and print the errors.

**Example 4: Delete a RADIUS server**
* **Endpoint:** `https://192.168.88.1/rest/radius/*2`
* **Method:** DELETE
* **Request Body:** None
* **Expected Response:** Empty body `204 No Content`.

**Note:**  Ensure you are using the correct API user, password, and ports. The API requires HTTPS by default. You can set the `ssl-certificate` under `/certificate`

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a strong, complex shared secret.
*   **Restrict RADIUS Access:** If possible, configure ACLs on your RADIUS server to only allow access from the specific MikroTik router IPs.
*   **Use TLS for RADIUS:** If supported by your RADIUS server, consider using TLS to encrypt communication between the router and server. This is configurable in `/radius` under the `tls-version` and `certificate` arguments.
*   **Monitor Authentication Attempts:** Review the logs to identify suspicious authentication activity or failures.
*   **Keep RouterOS Updated:** Apply regular RouterOS updates to patch security vulnerabilities.

## Self Critique and Improvements:

This configuration provides a solid base for RADIUS authentication on MikroTik. Improvements include:

*   **Fine-grained Services:** Instead of applying RADIUS to all listed services, consider creating specific RADIUS servers with services tailored to individual needs, using the `service` parameter.
*   **Profile Management:** Instead of modifying the default PPP profile, use new ones which should be selected for users of a particular configuration. This makes configuration more manageable and modular.
*   **Dynamic IP assignment:** Add DHCP server setup and dynamic IP assignment to this example.
*   **Error Handling:** Error handling for RADIUS request failures can be improved by checking the logs and implementing specific retry strategies or user notifications.
*   **Advanced Features:** Implement the use of RADIUS attributes and dynamic VLAN assignment for better security control.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to a network. It works with a client-server model, where a client (like a MikroTik router) sends authentication requests to a RADIUS server. The RADIUS server verifies the credentials against a user database and responds with access permissions.

**Key Concepts:**

*   **Authentication:** Verifies the identity of a user trying to access the network.
*   **Authorization:** Determines what a user is allowed to do on the network, after being authenticated.
*   **Accounting:** Tracks user activities like connection time and data usage.
*   **Shared Secret:** A pre-shared key used between the client (MikroTik) and server for security.
*   **Attributes:** Standard and vendor-specific attributes that are passed between the client and server, which could include username, password, and other configuration data.

## Detailed Explanation of Trade-offs:

*   **Local User Management vs. RADIUS:** Local user management on a MikroTik router is simpler for small setups, but RADIUS offers scalability, centralization, and more complex authorization schemes for larger networks.
*   **PAP vs. CHAP/MSCHAPv2:** PAP transmits passwords in plain text, which is not secure, but compatible with many systems. CHAP and MSCHAPv2 are more secure but may not be compatible with all RADIUS servers.
*   **Multiple RADIUS Servers:** Using multiple RADIUS servers provides redundancy, but requires careful configuration of priorities and potentially increased configuration complexity of the overall network.
*   **Accounting On vs Off:** Using accounting can overload your RADIUS server with data if there are too many users or the RADIUS server does not perform well. This is not needed by most general use-cases.

## Configuration for Specific RouterOS Versions:

This documentation targets RouterOS 7.12, but the general concepts and commands are compatible with previous version 6.48. The commands such as `/interface bridge`, `/ip address`, `/radius` and `/ppp` have remained largely consistent over these versions. There may be slight differences or additions in parameters, so always consult the official MikroTik documentation for the specific version you are using, especially on more obscure parameters. The REST API may also have differences in behaviour, or features, always consult the documentation.
