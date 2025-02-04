Okay, let's craft a detailed and expert-level documentation for configuring RADIUS authentication on a MikroTik router within a Hotspot environment, targeting RouterOS 7.12 (with some backward compatibility notes).

**Scenario Description:**

We are setting up a RADIUS server to handle authentication and authorization for clients connecting to our Hotspot network. This is a common setup for managed Wi-Fi environments, guest networks, or controlled access points. The Hotspot network uses a bridge interface (`bridge-33`) on the subnet `51.171.254.0/24`. User authentication requests will be sent to the specified RADIUS server, which we will also need to configure.

**Implementation Steps:**

1.  **Step 1: Configure the RADIUS Server Settings**
    *   **Purpose:**  Define the RADIUS server's IP address, authentication secret, and other related settings on the MikroTik router. This tells the router where to send authentication requests.
    *   **CLI Instructions (Before):**
        ```mikrotik
        /radius print
        ```
        This command should show that no RADIUS server is currently configured.
    *   **CLI Instructions (After):**
        ```mikrotik
        /radius add address=192.168.10.10 secret=your_radius_secret timeout=30s accounting-port=1813 authentication-port=1812 service=hotspot
        ```
    *   **Winbox GUI Instructions:**
        1. Navigate to `Radius` in the left sidebar.
        2. Click the `+` button to add a new entry.
        3. Fill in the fields:
            *   `Address`: 192.168.10.10 (Replace with your RADIUS server IP)
            *   `Secret`: your\_radius\_secret (Replace with your shared secret)
            *   `Timeout`: 30s
            *   `Accounting Port`: 1813
            *   `Authentication Port`: 1812
            *   `Service`: hotspot
        4. Click `Apply` and `OK`.
    *   **Explanation:**
        *   `address=192.168.10.10`: The IP address of the RADIUS server.
        *   `secret=your_radius_secret`: The shared secret used to authenticate the MikroTik with the RADIUS server (must match on both sides).
        *   `timeout=30s`: The timeout for RADIUS requests (30 seconds). Adjust as needed for your network latency.
        *   `accounting-port=1813`:  The UDP port for accounting requests.
        *   `authentication-port=1812`: The UDP port for authentication requests.
        *   `service=hotspot`:  Specifies that this RADIUS server is to be used by the Hotspot service.

2.  **Step 2: Enable RADIUS Usage on the Hotspot Instance**
    *   **Purpose:** We link the Hotspot instance on the `bridge-33` interface to our configured RADIUS server. This tells the Hotspot instance to use RADIUS for authenticating users.
    *   **CLI Instructions (Before):**
        ```mikrotik
        /ip hotspot print
        ```
        This will output information of currently configured hotspots. We'll need to identify our target hotpot based on `interface` property. Let's assume the existing hotspot uses the name `hotspot-bridge-33`.
    *   **CLI Instructions (After):**
        ```mikrotik
        /ip hotspot profile set hotspot-bridge-33 use-radius=yes radius-accounting=yes
        ```
    *   **Winbox GUI Instructions:**
        1.  Navigate to `IP` -> `Hotspot` -> `Server Profile` tab.
        2.  Double-click the server profile associated with the `bridge-33` (e.g., `hotspot-bridge-33`).
        3.  Check the `Use Radius` box.
        4.  Check the `Radius Accounting` box.
        5. Click `Apply` and `OK`.
    *   **Explanation:**
        *   `use-radius=yes`: Enables RADIUS authentication for this Hotspot.
        *   `radius-accounting=yes`: Enables RADIUS accounting, which reports session start, stop, and data usage to the RADIUS server.

3.  **Step 3:  Configure Hotspot Bindings (Optional)**
    *   **Purpose:** If not already done you must create the hotspot instance itself and bind it to your interface. If you have an already existing instance move to the next step.
    *   **CLI Instructions (Before):**
        ```mikrotik
        /ip hotspot print
        ```
    *   **CLI Instructions (After):**
        ```mikrotik
        /ip hotspot add address-pool=hotspot-pool disabled=no interface=bridge-33 name=hotspot-bridge-33 profile=default
        /ip hotspot user profile add name=default
        /ip pool add name=hotspot-pool ranges=51.171.254.100-51.171.254.200
        ```
    *   **Winbox GUI Instructions:**
        1.  Navigate to `IP` -> `Hotspot` -> `Hotspots` Tab.
        2.  Click the `+` button to add a new entry.
        3.  Fill in the fields:
            *   `Name`: `hotspot-bridge-33`
            *   `Interface`: Select `bridge-33`.
            *   `Address Pool`: Select an address pool or create one. For example we created a pool called `hotspot-pool` in the cli example.
            *   `Profile`: Select `default` or create one. For example, the CLI example creates a `default` user profile.
        4.  Click `Apply` and `OK`.
    *   **Explanation:**
         *   `/ip hotspot add address-pool=hotspot-pool disabled=no interface=bridge-33 name=hotspot-bridge-33 profile=default`:
              Creates a new hotspot instance using `bridge-33` as interface, `hotspot-pool` as the address pool (range), using the default profile.
        *  `/ip hotspot user profile add name=default`:
             Creates the default hotspot user profile.
         * `/ip pool add name=hotspot-pool ranges=51.171.254.100-51.171.254.200`:
              Creates a new ip pool for use by hotspot.

4. **Step 4: Configure Walled Garden (Optional, but Recommended)**
    *   **Purpose:** Allows access to certain URLs without authentication, commonly used for redirection to the login page.
     *   **CLI Instructions (Before):**
        ```mikrotik
        /ip hotspot walled-garden print
        ```
     *   **CLI Instructions (After):**
        ```mikrotik
        /ip hotspot walled-garden add dst-host=your_radius_server_dns.com
        /ip hotspot walled-garden add dst-host=login.domain.com
        ```
    *   **Winbox GUI Instructions:**
        1.  Navigate to `IP` -> `Hotspot` -> `Walled Garden` Tab.
        2.  Click the `+` button to add a new entry.
        3.  Fill in the fields:
            *   `Dst. Host`: `your_radius_server_dns.com`
            *   Click `Apply` and `OK`.
        4.  Repeat the same process for `login.domain.com`.
    *   **Explanation:**
        *   `dst-host=your_radius_server_dns.com`: Allows the router to connect to your radius server to perform authentication. You may also want to include the login pages here. Replace `your_radius_server_dns.com` with the actual DNS name of your RADIUS server.
        *   `dst-host=login.domain.com`: You should include the domain that is hosting your hotspot login page, if this is located on a remote server.

**Complete Configuration Commands:**

```mikrotik
/radius
add address=192.168.10.10 secret=your_radius_secret timeout=30s accounting-port=1813 authentication-port=1812 service=hotspot
/ip hotspot profile
set hotspot-bridge-33 use-radius=yes radius-accounting=yes
/ip hotspot
add address-pool=hotspot-pool disabled=no interface=bridge-33 name=hotspot-bridge-33 profile=default
/ip hotspot user profile
add name=default
/ip pool
add name=hotspot-pool ranges=51.171.254.100-51.171.254.200
/ip hotspot walled-garden
add dst-host=your_radius_server_dns.com
add dst-host=login.domain.com
```

**Common Pitfalls and Solutions:**

*   **RADIUS Secret Mismatch:** The most common issue is a mismatch between the secret configured on the MikroTik and the RADIUS server.
    *   **Solution:** Double-check the secret on both sides. Use the exact same secret.
*   **Incorrect RADIUS Server IP/Port:** Incorrect IP address or UDP ports will prevent the MikroTik from connecting to the RADIUS server.
    *   **Solution:**  Verify the IP address and ports on the MikroTik and RADIUS server configuration. Use `ping` and `traceroute` from MikroTik to diagnose.
*   **Firewall Issues:** A firewall on the RADIUS server or on the path between the MikroTik and the RADIUS server might block the communication.
    *   **Solution:** Check firewalls along the path, make sure ports 1812/1813 (or whatever you configured) are open. Use `torch` on the MikroTik to capture and view the traffic to and from your RADIUS server, to see if packets are being received.
*   **RADIUS Service Not Running:** If the RADIUS service is not running or is not configured correctly on the RADIUS server, it will not respond to authentication requests.
    *   **Solution:** Verify that the RADIUS server is properly configured and running. Check the RADIUS logs.
*   **Incorrect Profile Selection:** If you configure RADIUS on the wrong hotspot profile, or create a new profile and don't enable radius for that profile, the RADIUS authentication will not work on the interface you are targetting.
    *   **Solution:** Check your configurations, and use the correct profile, or rebind your hotspot instance to the correct profile.
*   **Walled Garden Configuration Issues:** Not including the necessary servers (RADIUS server, login pages) in the walled garden will prevent users from accessing these resources before authenticating.
    * **Solution:** Make sure your radius server and login portal are in the walled garden configuration.
*   **Resource Issues:** Large networks with many concurrent users might strain the MikroTik router's CPU or RAM.
    *   **Solution:**  Monitor system resources (CPU, RAM) using the MikroTik resource monitor or SNMP. Consider using a more powerful MikroTik device, or limiting user sessions.
*  **Hotspot User Profile Errors**: If you try to use a user profile that isn't set, the radius authentication will not work.
     *   **Solution:** Check that the user profile set is configured in the `/ip hotspot user profile` menu. Make sure that you are using the correct profile for your hotspot instance.

**Verification and Testing Steps:**

1.  **Connect a Client:** Connect a device to the Hotspot network. You should be redirected to the Hotspot login page.
2.  **Authenticate via RADIUS:** Enter valid credentials for a user that has been configured on the RADIUS server.
3.  **Check MikroTik Logs:** Check the MikroTik logs for RADIUS related messages:
    ```mikrotik
    /log print topic=radius
    ```
    Look for successful authentication entries, or errors if something fails.
4.  **RADIUS Server Logs:** Examine the logs on your RADIUS server for authentication requests and responses. This is often the best way to figure out why authentication is failing.
5.  **MikroTik Torch Tool:** Use the `torch` tool to capture RADIUS traffic:
    ```mikrotik
    /tool torch interface=bridge-33 protocol=udp port=1812,1813
    ```
    This helps diagnose if traffic is being sent and received.
6. **MikroTik Monitor Tool:** Use the `monitor` tool to view your interfaces:
     ```mikrotik
    /interface monitor numbers=bridge-33
    ```
    Verify that your hotspot bridge is functioning as expected, and that packets are traversing the interface as expected.

**Related Features and Considerations:**

*   **MAC Address Based Authentication:** You can combine RADIUS with MAC address-based authentication to allow some devices automatic access.
*   **Hotspot Customization:**  Customize the login page with the MikroTik built-in Hotspot features or redirect users to an external portal.
*   **Usermanager:** The MikroTik User Manager is a built-in RADIUS server with a web-based interface which can be used to configure user accounts.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy and failover.
*   **VLANs:** The Hotspot setup can be used together with VLANs for network segmentation.
*   **HTTPS Login Pages:** Consider using HTTPS for your login page to avoid transmitting credentials in cleartext.

**MikroTik REST API Examples (if applicable):**

For adding a radius server, the request would be to `/radius`:

*   **Endpoint:** `/radius`
*   **Method:** POST
*   **Request Body (JSON):**
    ```json
    {
      "address": "192.168.10.10",
      "secret": "your_radius_secret",
      "timeout": "30s",
      "accounting-port": 1813,
      "authentication-port": 1812,
      "service": "hotspot"
    }
    ```
*   **Expected Response (JSON - success):**
    ```json
    {
      "message": "added",
      ".id": "*1"
    }
    ```
*   **Error handling:** If the API call fails, you will receive an error object, the most important property is `message`. For example, attempting to add the same entry twice, you may get the following error:

    ```json
    {
       "message": "already have such entry",
       "error": true
    }
    ```

To enable radius on an existing hotspot profile:
* **Endpoint**: `/ip/hotspot/profile/`
* **Method**: PUT
* **Request Body (JSON):**
```json
{
     "use-radius":"yes",
     "radius-accounting": "yes",
     "name": "hotspot-bridge-33"
}
```
* **Expected Response (JSON - success):**
```json
 {
      "message": "changed"
  }
```
*   **Error handling:** If the API call fails, you will receive an error object, the most important property is `message`. For example, trying to use an invalid profile name, you may get the following error:

    ```json
    {
       "message": "no such item",
       "error": true
    }
    ```

**Security Best Practices:**

*   **Strong RADIUS Secret:** Use a strong, randomly generated secret for RADIUS communication.
*   **HTTPS for Login:** Always use HTTPS for the login page to protect user credentials.
*   **Firewall Rules:** Carefully configure firewall rules to protect the router and the RADIUS server. Only allow necessary traffic between the router and the RADIUS server.
*   **Rate Limiting:** Implement rate limiting to prevent brute-force attacks on the Hotspot service.
*   **Regular Updates:** Keep RouterOS updated to the latest version to patch known security vulnerabilities.
*   **Limit Access to RADIUS Server:** Ensure that your radius server is secured and not accessible from public networks.

**Self Critique and Improvements:**

*   **Improve Error Handling:** The error handling could be further improved by detailing every possible error response from the API and the solutions.
*   **More Advanced Examples:** Provide more advanced configuration examples including MAC based authentication and multiple RADIUS servers.
*   **Detailed Troubleshooting:** Improve on the troubleshooting section. For example, more details regarding the debugging of the RADIUS server using Wireshark or a similar tool, and a more detailed explanation of what kinds of problems you can catch this way.
*   **Scripting Examples:** Provide examples of how to use scripting to make this configuration easier and more scalable for complex environments.
*   **Configuration Management:** Discuss the usage of configuration management tools like Ansible, to manage this configuration across multiple devices.
*   **Monitoring:** Provide details on how to use external monitoring tools and technologies to monitor the status of the hotspot.

**Detailed Explanation of Topic:**

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for network access. In the context of a MikroTik Hotspot, RADIUS is used to offload the authentication process to an external server. Instead of having the MikroTik store all user credentials, the router forwards authentication requests to the RADIUS server, which handles user authentication, authorization and accounting, providing much more scalability and control, compared to handling local user accounts.

*   **Authentication:** Verifies user identity by matching credentials against a central database (often LDAP, SQL).
*   **Authorization:** Determines what resources and permissions are granted to the user.
*   **Accounting:** Tracks user sessions, data usage, and other relevant information for billing or monitoring purposes.

**Detailed Explanation of Trade-offs:**

Using RADIUS over local user management in Hotspot provides several advantages, but also some trade-offs:

*   **Centralized Management:** With RADIUS, user accounts and permissions are managed in one location, making it easier to handle large numbers of users or devices compared to the local user database of the MikroTik. If you have many devices or a large user base, this will save time compared to setting up the same users on every device.
*   **Scalability:** RADIUS servers are built to handle a large amount of authentication requests. They are usually much more performant for this kind of job, compared to the limited resources of the router device.
*   **Flexibility:** RADIUS offers more complex authorization options than local user management, like time-based access, traffic quotas or policies, as well as integration with other systems like billing platforms or active directories.
*   **Complexity:** Setting up and maintaining a RADIUS infrastructure is more complex than managing user accounts on the MikroTik locally, requiring more networking and system administration skills.
*   **Single Point of Failure:** If your RADIUS server becomes unavailable, users will not be able to authenticate until the issue is fixed. This can be mitigated by using multiple RADIUS servers for failover, but this adds complexity.
*   **Increased Network Latency:** The round trip to the RADIUS server may increase the login time, when compared to local user accounts. This can be mitigated by using an optimized RADIUS server on a high performance local server.
* **Additional Costs:** Deploying a RADIUS server might come with additional costs. This might mean that using the MikroTik built-in user database can be more affordable for smaller environments.

**Configuration for Specific RouterOS Versions:**

The commands listed here are valid for RouterOS 7.12 and, with minor syntax changes, should also work on older versions like 6.48 and 7.x, specifically in regards to the `radius` commands. However, the new way of handling hotpot profiles and radius settings has been changed in the 7.x releases, so please double check the documentation when working with those versions. The older versions of RouterOS might use a `hotspot` menu, instead of the `ip hotspot` menu. Always consult the official RouterOS documentation for specifics, as minor differences can exist. You may use the following command to verify that the commands are supported for your ROS version:
```mikrotik
/system resource print
```
This command will output the version that you are running.

This extensive guide should provide a solid foundation for setting up RADIUS authentication on your MikroTik router for a Hotspot network. Remember to adapt the configurations to your specific needs and environment. Always back up your configurations before making major changes!
