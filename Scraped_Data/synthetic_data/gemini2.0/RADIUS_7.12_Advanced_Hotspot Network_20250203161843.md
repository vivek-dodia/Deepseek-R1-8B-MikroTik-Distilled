Okay, let's craft a comprehensive guide for implementing RADIUS authentication within a MikroTik Hotspot network using RouterOS 7.12, along with considerations for older versions.

## Scenario Description:

We are setting up a Hotspot network using the `bridge-27` interface with a subnet of `189.130.59.0/24`.  Instead of relying on the MikroTik's built-in user management, we will leverage a RADIUS server for authentication and authorization. This approach provides centralized user management, advanced accounting, and better scalability.

## Implementation Steps:

### Step 1: Setting up the Bridge Interface

* **Goal:**  Create a bridge interface and assign the Hotspot IP range to it.
* **Before:** The router has its default configuration.
* **Action (CLI):**
```mikrotik
/interface bridge
add name=bridge-27
/ip address
add address=189.130.59.1/24 interface=bridge-27 network=189.130.59.0
```
* **Winbox GUI:**
  1.  Navigate to `Bridge` under `Interfaces`.
  2.  Click the `+` button.
  3.  Set `Name` to `bridge-27` and click `Apply`.
  4.  Navigate to `IP` > `Addresses`.
  5.  Click the `+` button.
  6.  Set `Address` to `189.130.59.1/24`, `Interface` to `bridge-27` and click `Apply`.

* **After:** A new bridge interface is created, and the specified subnet is assigned to it.
* **Effect:**  Network devices connected to the bridge will be within the 189.130.59.0/24 subnet.

### Step 2: Configuring the Hotspot Server

* **Goal:** Create and configure the Hotspot server on the created bridge interface.
* **Before:** The bridge is created, but the hotspot is not yet configured.
* **Action (CLI):**
```mikrotik
/ip hotspot
add name=hotspot1 interface=bridge-27 address-pool=pool-1 profile=hsprof1 disabled=no
/ip pool
add name=pool-1 ranges=189.130.59.10-189.130.59.254
/ip hotspot profile
add name=hsprof1 html-directory=hotspot default-server=all
```
* **Winbox GUI:**
  1.  Navigate to `IP` > `Hotspot`.
  2.  Click the `+` button.
  3. Set `Name` to `hotspot1`, `Interface` to `bridge-27`, `Address Pool` to `default`, `Profile` to `default` and click `Apply`.
  4.  Navigate to `IP` > `Pool` click the `+` button.
  5.  Set the name to `pool-1`, set the ranges to `189.130.59.10-189.130.59.254` and click `Apply`.
  6. Go back to `IP` > `Hotspot` click on `hotspot1` and set the address pool to `pool-1`.
  7. Navigate to `IP` > `Hotspot` then on `Hotspot Profiles` Click `default`
  8.  Set the name to `hsprof1`, then on the General tab select default `HTTP`, `HTTPS` and click `Apply`.
    *Note:  the winbox will automatically change the hotspot name to `hsprof1` if you made a mistake setting up the hotspot name.*

* **After:** A new Hotspot instance is created on `bridge-27`, using the address pool `pool-1` with an empty profile.
* **Effect:**  The Hotspot service is active, and new connections will trigger the Hotspot login page.

### Step 3: Configuring RADIUS Server Connection

* **Goal:** Add the RADIUS server configuration so the hotspot can communicate with it.
* **Before:** The hotspot is running but only uses the default user database.
* **Action (CLI):**
```mikrotik
/radius
add address=192.168.88.100 secret=secret123 service=hotspot timeout=30s
/ip hotspot profile set hsprof1 use-radius=yes accounting=yes
```

  * **Note:** *Replace `192.168.88.100` with your RADIUS server's IP address and `secret123` with the shared secret.*

* **Winbox GUI:**
  1. Navigate to `RADIUS` from the main menu.
  2. Click the `+` button.
  3. Set `Address` to your RADIUS server's IP, `Secret` to the shared secret, and `Service` to `hotspot`, `Timeout` to `30s` and click `Apply`.
  4. Navigate to `IP` > `Hotspot` click on `Hotspot Profiles`.
  5. Click on `hsprof1` go to the `Radius` tab, set `Use Radius` to `yes`, `Accounting` to `yes` and click `Apply`.

* **After:** The MikroTik is configured to send authentication requests to the configured RADIUS server.
* **Effect:** Users connecting to the hotspot will be authenticated through the RADIUS server.

### Step 4: Configuring User Accounting

* **Goal:** Send accounting information to the RADIUS server for tracking usage.
* **Before:** The RADIUS authentication is working, but accounting is not being sent. (we already set this up in Step 3, so no action needed)
* **Action (CLI):**
   *This was already enabled via `accounting=yes` in Step 3, so no further configuration is needed.*
* **Winbox GUI:**
    *This was already enabled via `accounting=yes` in Step 3, so no further configuration is needed.*
* **After:** The MikroTik will send accounting data (start, interim, stop) to the RADIUS server.
* **Effect:**  The RADIUS server can track the usage of each authenticated user.

## Complete Configuration Commands:
```mikrotik
/interface bridge
add name=bridge-27
/ip address
add address=189.130.59.1/24 interface=bridge-27 network=189.130.59.0
/ip pool
add name=pool-1 ranges=189.130.59.10-189.130.59.254
/ip hotspot
add name=hotspot1 interface=bridge-27 address-pool=pool-1 profile=hsprof1 disabled=no
/ip hotspot profile
add name=hsprof1 html-directory=hotspot default-server=all use-radius=yes accounting=yes
/radius
add address=192.168.88.100 secret=secret123 service=hotspot timeout=30s
```

| **Parameter**        | **Description**                                                     |
|---------------------|---------------------------------------------------------------------|
| `/interface bridge add name=bridge-27` | Creates a bridge interface named `bridge-27`.             |
| `/ip address add address=189.130.59.1/24 interface=bridge-27 network=189.130.59.0`    | Assigns the IP address 189.130.59.1/24 to bridge-27.     |
| `/ip pool add name=pool-1 ranges=189.130.59.10-189.130.59.254` | Creates an IP address pool named `pool-1`.                  |
| `/ip hotspot add name=hotspot1 interface=bridge-27 address-pool=pool-1 profile=hsprof1 disabled=no`   | Creates a hotspot instance on `bridge-27`. |
| `/ip hotspot profile add name=hsprof1 html-directory=hotspot default-server=all use-radius=yes accounting=yes`    | Creates a hotspot profile `hsprof1` with RADIUS & Accounting.   |
| `/radius add address=192.168.88.100 secret=secret123 service=hotspot timeout=30s`| Defines the RADIUS server's address, secret, and service. |

## Common Pitfalls and Solutions:

* **RADIUS Server Unreachable:**
  * **Problem:**  The MikroTik cannot connect to the RADIUS server.
  * **Solution:** Verify the RADIUS server IP, port (1812/1813 by default), shared secret, and network connectivity. Use `/tool ping 192.168.88.100` from the MikroTik CLI to test network reachability. Also, double check your firewall rules.
* **Incorrect RADIUS Secret:**
   * **Problem:** Authentication fails because the shared secret on the MikroTik and RADIUS server do not match.
   * **Solution:** Ensure the secret matches exactly on both devices.
* **RADIUS Response Timeout:**
   * **Problem:**  The MikroTik does not receive a timely response from the RADIUS server.
   * **Solution:** Increase the `timeout` parameter in the RADIUS configuration (e.g., `/radius set [find address=192.168.88.100] timeout=60s`). Also, check the RADIUS server performance and network latency.
* **Missing User on RADIUS:**
   * **Problem:** Users are not authenticated because they are not configured on the RADIUS server.
   * **Solution:** Add the users with appropriate passwords to the RADIUS server.
* **Incorrect or Incomplete RADIUS Attributes:**
  * **Problem:** The user authenticates, but access is not working because attributes returned by the RADIUS server are incomplete or incorrect.
  * **Solution:** Review and adjust the RADIUS server's configuration to send the correct attributes, check the hotspot configuration and settings to make sure they are compatible with your needs.
* **High CPU usage:**
  * **Problem:** The router's CPU usage increases due to complex firewall/hotspot rules.
  * **Solution:** Monitor CPU usage with `/system resource print` and adjust your configuration. Consider using fasttrack and simpler rules to reduce the load. Ensure your router is powerful enough for the workload.

## Verification and Testing Steps:

1. **Connect a client to the Hotspot:**  Connect a device to the `bridge-27` network.
2. **Access a website:** The device should be redirected to the Hotspot login page.
3. **Enter valid RADIUS credentials:** Use valid username and password which exist on the RADIUS server.
4. **Verify successful login:** The device should be allowed to access the internet after successful authentication.
5. **Check logs:**
  * Use `/log print` on the MikroTik to check for RADIUS-related entries. Look for authentication successes and failures.
  * Check the logs on the RADIUS server for authentication requests and responses.
6. **Use Torch:**
   * Use `/tool torch interface=bridge-27` to monitor traffic. Filter traffic to port `1812` and `1813` to confirm RADIUS traffic is being sent and received.
7. **Ping:**
   * Ping to the RADIUS server to verify connectivity: `/tool ping 192.168.88.100`

## Related Features and Considerations:

* **MAC Authentication:** You can add MAC authentication in combination with RADIUS for more secure access control ( `/ip hotspot user add mac-address=xx:xx:xx:xx:xx:xx`).
* **Walled Garden:** Configure `/ip hotspot walled-garden` to allow specific destinations without authentication (e.g., RADIUS server).
* **HTTPS for Hotspot:** Use HTTPS for the Hotspot login page to secure user credentials.
* **Different RADIUS Attributes:** Depending on the RADIUS implementation and need, you can utilize different attributes in the authentication and accounting process (e.g.  User-Name, Calling-Station-Id, Framed-IP-Address).
* **Advanced Queuing**: Implement advanced queuing and traffic shaping based on radius attributes, creating a better user experience.

## MikroTik REST API Examples (if applicable):

* **Note:** *The MikroTik RouterOS API is a powerful tool to automate configuration, however, it does not offer full parity with the CLI. For this scenario the CLI is preferred, however, the example below shows how you can create a RADIUS entry with the API*
**Create a RADIUS Server:**

* **Endpoint:** `/radius`
* **Method:** `POST`
* **Request JSON Payload:**
```json
{
  "address": "192.168.88.100",
  "secret": "secret123",
  "service": "hotspot",
  "timeout": "30s"
}
```
* **Expected Response (Successful):**
```json
{
  ".id": "*1",
  "address": "192.168.88.100",
  "secret": "secret123",
  "service": "hotspot",
  "timeout": "30s",
  "disabled": "false",
  "authentication-port": "1812",
  "accounting-port": "1813"
}
```
* **Error Handling:** If the request fails the server returns a JSON object with an error code and error messages, for example:
```json
{
    "message": "already have such item",
    "error": 401
}
```
You can handle this error, by checking the `error` and `message` parameters and output it to your users. If the request was completed, the `error` parameter would be missing from the return.

**Explanation:**

| **Parameter**     | **Description**                                                 |
|-------------------|-----------------------------------------------------------------|
| `address`        | IP address of the RADIUS server.                                |
| `secret`         | Shared secret for communication with the RADIUS server.          |
| `service`        | The service type (`hotspot`, `ppp`, etc.).                     |
| `timeout`        | Timeout in seconds for RADIUS requests.                        |
| `.id`            | The internal identifier that RouterOS assigns to this entry   |
| `authentication-port` | the Radius authentication port |
| `accounting-port` | the Radius accounting port |

## Security Best Practices:

* **Strong Shared Secret:** Use a long, complex shared secret for RADIUS communication.
* **Secure Network:** Ensure your network infrastructure is secure to prevent unauthorized access to the RADIUS server.
* **HTTPS for Login:** Use HTTPS for the Hotspot login page to protect user credentials in transit.
* **Rate Limiting:** Implement rate limiting to protect the RADIUS server from denial-of-service attacks.
* **Firewall Rules:** Restrict access to RADIUS ports (1812, 1813) to only necessary hosts.
* **Regular Audits:** Regularly check your RADIUS logs for suspicious activity.
* **Keep RouterOS Updated:** Regularly update your RouterOS to the latest stable version to patch vulnerabilities.

## Self Critique and Improvements:

This configuration provides a good starting point for a RADIUS-based Hotspot. Here are some potential improvements:

*   **Advanced Hotspot Configuration:** Implement features like user profiles, bandwidth control per user or per user group, and custom login page designs.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy and load balancing.
*   **Scripting for Dynamic Configuration:** Use RouterOS scripting for more dynamic and complex scenarios (e.g.  changing policies based on RADIUS attributes).
*   **Integration with Centralized Management System:** Integrate the Mikrotik with a Centralized Management Platform for monitoring and management.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for network users. In a Hotspot environment:

* **Authentication:** Verifies the identity of a user attempting to connect to the network.
* **Authorization:** Determines the level of access a user has on the network.
* **Accounting:** Tracks resource usage by users, such as connection time and data transfer.

RADIUS is a client-server protocol. The MikroTik router acts as the client, sending authentication and accounting requests to the RADIUS server. The RADIUS server then processes these requests and sends back responses with the necessary information. This decoupling of user management from the MikroTik device itself offers much greater flexibility and scalability.

## Detailed Explanation of Trade-offs:

* **Local vs. RADIUS Users:**
    *   **Local Users:**  Easier to set up and manage for small-scale deployments. Suitable if you have few users and don't need advanced accounting.
    *   **RADIUS Users:** More scalable, better for handling numerous users and provides more flexibility for user-specific settings. Requires a RADIUS server but provides centralized control and auditing.
* **Hotspot Authentication Methods:**
    *   **Basic Password:** Simple to set up but offers minimal security.
    *   **HTTP CHAP/PAP:** More secure but is generally considered outdated, should not be used without HTTPS.
    *   **RADIUS:** The most secure and scalable, however, requires more complex configuration.
* **Accounting Features:**
    * **Simple Accounting:** Basic usage data.
    * **Advanced Accounting:** More granular data like, session time, transferred data volume, etc., with the use of RADIUS interim updates, which allows for dynamic control of network resources.

## Configuration for Specific RouterOS Versions:

The provided configuration is primarily focused on RouterOS 7.12. However, the core RADIUS commands and concepts are applicable to older versions like 6.48 or earlier 7.x versions, with very few differences.

*   **Version 6.x:** The `/ip hotspot profile` commands might use `radius-accounting` and `radius-authentication` instead of the more modern `use-radius` and `accounting` parameters.
*   **Version Differences:** Review the documentation for the specific version you're using for any differences in parameters and syntax. The command reference is available at the mikrotik wiki

This detailed guide provides a robust foundation for implementing RADIUS authentication within a MikroTik hotspot network. Remember to adapt the configuration to suit your particular requirements and perform regular testing and monitoring for optimal performance and security.
