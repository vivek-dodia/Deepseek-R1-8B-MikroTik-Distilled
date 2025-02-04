Okay, let's delve into configuring RADIUS authentication on a MikroTik router, targeting RouterOS 6.48, within an enterprise environment. We'll focus on practical implementation, detailed commands, troubleshooting, and security considerations.

## Scenario Description:

This scenario involves configuring a MikroTik router to act as a RADIUS client. We aim to authenticate users accessing the network via the `bridge-31` interface using an external RADIUS server. The IP subnet for clients is 62.0.71.0/24. This setup is common in enterprise environments for centralized user authentication and authorization, as well as accounting.

## Implementation Steps:

Here's a step-by-step guide to configure RADIUS authentication on our MikroTik router. This guide will use both CLI and Winbox instructions.

**1. Step 1: Access RouterOS and Verify Default Configuration**

   *   **Explanation**: First, you need to gain access to your MikroTik router. Use Winbox or SSH. Before making changes, it's good practice to check the existing IP configuration on the `bridge-31` interface.

   *   **CLI Instructions:**
      ```mikrotik
      /ip address print where interface=bridge-31
      ```
   *   **Winbox Instructions:**
      *   Connect to the router using Winbox.
      *   Go to *IP* -> *Addresses*.
      *   Locate `bridge-31` in the interface list. Verify if there is any IP address configured on the bridge.
   *   **Example Before:**

      ```
      [admin@MikroTik] > /ip address print where interface=bridge-31
      Flags: X - disabled, I - invalid, D - dynamic
      [admin@MikroTik] >
      ```
      **Note:** In this example, there are no IP addresses assigned to `bridge-31`. An IP address will need to be assigned to the bridge.

   *   **Example After:** (This assumes that no IP is configured on bridge-31):
      Let's assign the address `62.0.71.1/24` to the `bridge-31`. This is required so that the router can provide network access. This will not enable routing just yet.

      * **CLI Command:**
        ```mikrotik
         /ip address add address=62.0.71.1/24 interface=bridge-31
         ```
      *   **Winbox Instructions:**
          *  In Winbox go to IP -> Addresses.
          *  Click on +.
          *  Enter `62.0.71.1/24` for Address.
          *  Select `bridge-31` for Interface.
          * Click OK.
        ```
        [admin@MikroTik] > /ip address print where interface=bridge-31
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   62.0.71.1/24      62.0.71.0        bridge-31
        ```
   *   **Effect:** The `bridge-31` interface now has an IP address within the 62.0.71.0/24 subnet.

**2. Step 2: Add RADIUS Server Configuration**

   *   **Explanation**: We will add the configuration for the RADIUS server including IP, secret and service.
   *   **CLI Instructions:**

      ```mikrotik
      /radius add address=192.168.1.100 secret="supersecret" service=ppp timeout=5
      ```

      **Winbox Instructions:**
       *  Go to RADIUS -> click "+".
       *  Enter `192.168.1.100` for Address.
       *  Enter `supersecret` for Secret.
       *  Select `ppp` for Service.
       *  Enter `5` for Timeout.
       *  Click Apply and OK.
      *   **Explanation of Parameters:**
        *  `address`: IP address of your RADIUS server. (Replace with the real IP)
        *   `secret`: Shared secret between the router and RADIUS server. **Important**: *This must match on both devices.*
        *   `service`: Which service is utilizing the RADIUS server (e.g `ppp`, `hotspot`). For our configuration, the service needs to match the profile that we are using for authentication. Since in this case we are configuring a bridged network, we will use `ppp`.
        *  `timeout`: How long to wait for a response from the RADIUS server before failing, in seconds.

   *   **Example Before:**
      ```
      [admin@MikroTik] > /radius print
      Flags: X - disabled, I - invalid
      [admin@MikroTik] >
      ```

   *   **Example After:**
      ```
      [admin@MikroTik] > /radius print
      Flags: X - disabled, I - invalid
      #   ADDRESS         SECRET  SERVICE   TIMEOUT
      0   192.168.1.100   ******** ppp       5
      [admin@MikroTik] >
      ```
   *   **Effect:** The router is now aware of your RADIUS server and is configured to communicate with it using the defined parameters.
**3. Step 3: Enable RADIUS on the PPP Profile**

   *   **Explanation:** To use RADIUS authentication, we need to configure the PPP profile that will be used. In this case we will use the default profile.
   *   **CLI Instructions:**
      ```mikrotik
      /ppp profile set default use-encryption=yes only-one=no change-tcp-mss=yes use-radius=yes
      ```
   *   **Winbox Instructions:**
      *   Go to PPP -> Profiles.
      *   Select `default` and click ``.
      *   Select `yes` for `Use Encryption`.
      *   Select `no` for `Only One`.
      *   Select `yes` for `Change TCP MSS`.
      *   Select `yes` for `Use Radius`.
      *   Click Apply and OK.

   *  **Example Before:**
      ```
      [admin@MikroTik] > /ppp profile print
      Flags: * - default
      0 * name="default" use-encryption=no only-one=yes change-tcp-mss=no use-radius=no
      [admin@MikroTik] >
      ```
    * **Example After:**
        ```
        [admin@MikroTik] > /ppp profile print
        Flags: * - default
        0 * name="default" use-encryption=yes only-one=no change-tcp-mss=yes use-radius=yes
        [admin@MikroTik] >
        ```
    *   **Effect**: The `default` PPP profile is now configured to require RADIUS authentication, and enable encryption. `only-one` is set to no allowing multiple concurrent sessions. The MSS is adjusted on TCP connections to avoid fragmented packets.

**4. Step 4: Configure the Interface for Authentication.**

   * **Explanation**: Because we are configuring a bridge, and we need to make use of the PPP profile we have created, we need to configure an authenticator. An authenticator in the RouterOS context can be a PPPoE server, a DHCP server or a virtual server on the bridge. In our case we will choose to use a Virtual interface. A virtual interface is created in the `PPP` menu under `Secrets`. Here is how we can configure it, noting that the `local address` will be the address we want to assign the user accessing the network, and the `remote address` is the address that the router will use to connect to the network.
    *   **CLI Instructions:**
      ```mikrotik
      /ppp secret add name=test_user password=test_password service=any profile=default local-address=62.0.71.2 remote-address=62.0.71.1
      ```

    *   **Winbox Instructions:**
        *   Go to PPP -> Secrets.
        *   Click +.
        *   Add `test_user` for Name.
        *   Add `test_password` for Password.
        *   Add `any` for service.
        *   Add `default` for Profile.
        *   Add `62.0.71.2` for Local address.
        *   Add `62.0.71.1` for Remote address.
        * Click Apply and OK.

     *   **Example Before:**
      ```
      [admin@MikroTik] > /ppp secret print
      Flags: X - disabled, I - invalid
      [admin@MikroTik] >
      ```
    * **Example After:**
        ```
        [admin@MikroTik] > /ppp secret print
        Flags: X - disabled, I - invalid
        #   NAME      SERVICE  PROFILE  LOCAL-ADDRESS   REMOTE-ADDRESS
        0   test_user any      default  62.0.71.2       62.0.71.1
        ```
     *  **Effect**: A virtual interface has been created. When a user tries to connect to the 62.0.71.0/24 network, this virtual interface is invoked. Because the `default` profile was used, RADIUS will now be used for authentication.

**5. Step 5: Verify RADIUS Communication**
   * **Explanation**: With the basic authentication configuration in place, now the user should be able to access the network.
   *   **CLI Instructions:**
      *   On the computer, assign IP address of `62.0.71.2`.
      *   On a terminal, type `ping 62.0.71.1`
      *   The ping should complete successfully if everything is configured correctly.
   *   **Winbox Instructions:**
      *   Assign IP `62.0.71.2` on the computer.
      *   Open Terminal in Winbox.
      *   Type `ping 62.0.71.1`.
      *   The ping should complete successfully if everything is configured correctly.
     *   **Expected Output:**

        ```
        [admin@MikroTik] > ping 62.0.71.1
        SEQ HOST                                     SIZE TTL TIME  STATUS
          0 62.0.71.1                                  56  64 1ms
          1 62.0.71.1                                  56  64 1ms
          2 62.0.71.1                                  56  64 1ms
        sent=3 received=3 packet-loss=0% min-rtt=1ms avg-rtt=1ms max-rtt=1ms
        ```

**6. Step 6: Test RADIUS Authentication**
 * **Explanation**: Use the credentials that were configured in the `ppp secret`, and verify that RADIUS authentication is working. The RouterOS logging should show whether the user has successfully authenticated.
    *   **CLI Instructions:**
    *   On the terminal, type `/log print topics=radius`.
    *   The output should show an `accept` message, indicating that the RADIUS server has granted the request. If the authentication fails, a different message will be shown.
   * **Winbox Instructions:**
      * Open Winbox.
      * Go to Logging, and click the `+` button.
      * Select `radius` for the topic.
      * Click Apply and OK.
      * Look at the log entries to verify the authentication is successful.
    * **Example Output (Successful Authentication):**

        ```
        [admin@MikroTik] > /log print topics=radius
        18:23:25 radius,info incoming request id=1 from 192.168.1.100
        18:23:25 radius,debug processing Access-Request
        18:23:25 radius,debug   User-Name   "test_user"
        18:23:25 radius,debug   NAS-Port-Type  =  Virtual
        18:23:25 radius,debug   NAS-Port     =  0
        18:23:25 radius,debug   NAS-Identifier "MikroTik"
        18:23:25 radius,debug   Framed-IP-Address   =  62.0.71.2
        18:23:25 radius,debug   Service-Type = Framed
        18:23:25 radius,debug   calling "check_request"
        18:23:25 radius,debug   calling "authenticate"
        18:23:25 radius,debug calling "authorize"
        18:23:25 radius,debug authorize successful, sending Access-Accept
        18:23:25 radius,info outgoing response id=1 to 192.168.1.100: Access-Accept
        18:23:25 radius,debug   Framed-IP-Address   =  62.0.71.2
        18:23:25 radius,debug   Session-Timeout  = 120
        ```
        *   **Effect:** We can confirm that the router is sending authentication requests to the RADIUS server and is receiving appropriate responses (Access-Accept).

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to implement this setup:

```mikrotik
/ip address add address=62.0.71.1/24 interface=bridge-31
/radius add address=192.168.1.100 secret="supersecret" service=ppp timeout=5
/ppp profile set default use-encryption=yes only-one=no change-tcp-mss=yes use-radius=yes
/ppp secret add name=test_user password=test_password service=any profile=default local-address=62.0.71.2 remote-address=62.0.71.1
```

## Common Pitfalls and Solutions:

*   **Problem:** RADIUS server not reachable.
    *   **Solution:** Verify network connectivity between the MikroTik router and the RADIUS server. Use `ping` and `traceroute`. Double-check the IP address and port number.
    *   **CLI Example:**
        ```mikrotik
        /ping 192.168.1.100
        /traceroute 192.168.1.100
        ```
*   **Problem:**  Shared secret mismatch.
    *   **Solution:** Ensure the RADIUS `secret` on the MikroTik router matches the secret configured on the RADIUS server.
    *   **CLI Example (to reset the secret):**
        ```mikrotik
        /radius set 0 secret="newsecret"
        ```
*   **Problem:** Incorrect `service` type.
    *   **Solution:** Verify that the `service` parameter in the `/radius` configuration matches the type of authentication you are trying to do (e.g `ppp`, `hotspot`).
*  **Problem:** RADIUS server is not accepting the request
    *  **Solution:** Verify that the RADIUS server is configured correctly to accept requests from the MikroTik device.
*   **Problem:** Authentication fails.
    *   **Solution:** Check the logs on both the MikroTik router and the RADIUS server for detailed error messages. The `radius` topic can provide additional details on the RouterOS.
     *  **CLI Example (to print RADIUS logs):**
    ```mikrotik
    /log print topics=radius
    ```
*   **Problem:** Router has high CPU usage
    * **Solution:** If the router has a high CPU usage due to RADIUS requests, it could indicate a poorly configured or overloaded RADIUS server. The Mikrotik router might be trying to authenticate users in rapid succession. This could also be the case when there are a large number of active users at the same time. Consider reducing the authentication timeouts on the router to avoid an overloaded condition on the MikroTik.
     *  **CLI Example (to reduce the timeout):**
     ```mikrotik
     /radius set 0 timeout=2
     ```
## Verification and Testing Steps:

*   **Step 1:** Use `ping` from the MikroTik to test the network connectivity to the RADIUS server and back.
    ```mikrotik
    /ping 192.168.1.100
    ```
*   **Step 2:** Use `traceroute` to diagnose potential routing issues.
    ```mikrotik
     /traceroute 192.168.1.100
    ```
*   **Step 3:** Monitor the RADIUS logs on the MikroTik Router.
    ```mikrotik
    /log print topics=radius
    ```
*  **Step 4:** Try connecting to the network with a computer that is configured in the range. Monitor the logs on the MikroTik, and verify that authentication is succesfull, or failed as expected.
*   **Step 5:**  Use the MikroTik `torch` tool to examine the traffic between the MikroTik and the RADIUS server.
  ```mikrotik
    /tool torch interface=ether1 port=1812 protocol=udp
    ```
    * **Note**: Replace `ether1` with the interface where traffic to the RADIUS server is going through. `1812` is the default port for RADIUS authentication.

## Related Features and Considerations:

*   **RADIUS Accounting:** Enable accounting to track user usage, bandwidth, and session times by enabling it in `/radius` configuration.
*   **Backup RADIUS Servers:** Configure secondary RADIUS servers in `/radius` for redundancy.
*   **Hotspot and Wireless:** RADIUS is also used heavily for Hotspot and Wireless user authentication in MikroTik.
*   **User Profiles:** Create user profiles in the RADIUS server to restrict user access and bandwidth based on user groups.
*   **Dynamic VLAN assignment:** Using RADIUS, VLAN can be assigned dynamically.

## MikroTik REST API Examples (if applicable):

While there isn't a direct REST API call to configure RADIUS in MikroTik's API, we can use the existing endpoints to manage settings. You must first enable the API in `/ip service`.
Here's an example to query the current radius configuration:
*  **API Endpoint:** `/radius`
*  **Request Method:** GET

*  **Example Request** (using curl):

    ```bash
    curl -u admin:password -H "Content-Type: application/json" "https://192.168.1.1/rest/radius" -k
    ```
*  **Example Response**

   ```json
     [
     {
        ".id": "*0",
        "address": "192.168.1.100",
        "secret": "supersecret",
        "service": "ppp",
        "timeout": "5",
        "domain": null,
        "accounting": false,
        "interim-update": null,
        "authentication-port": "1812",
        "accounting-port": "1813",
        "realm": "",
        "called-id": "",
        "called-id-format": "mac",
        "framed-protocol": "ppp"
      }
    ]
   ```
   *  **Note:**  Replace `admin`, `password` and `192.168.1.1` with the correct credentials and IP address. `-k` is used to ignore the certificate warning. For production purposes, certificates should be properly configured.

* Here is an example to add a new radius server.

    *   **API Endpoint:** `/radius`
    *   **Request Method:** POST
    *   **Example JSON Payload**
       ```json
      {
        "address": "10.0.0.10",
        "secret": "testsecret",
        "service": "ppp",
        "timeout": 10,
        "accounting": true
      }
       ```
    *  **Example Request** (using curl):

    ```bash
    curl -u admin:password -H "Content-Type: application/json" -X POST -d '{"address": "10.0.0.10", "secret": "testsecret", "service": "ppp", "timeout": 10, "accounting": true}' "https://192.168.1.1/rest/radius" -k
    ```

   *  **Example Response**

    ```json
    {
       "message": "added",
       ".id": "*1"
    }
    ```
    *  **Note:** If the `address` field is missing the API call will return the following error.
    ```
    {
        "error": "input does not match expected format: address",
        "message": "input does not match expected format: address"
    }
    ```
* Here is an example to modify an existing entry.
    *   **API Endpoint:** `/radius/<ID>`
    *   **Request Method:** PUT
    *   **Example JSON Payload**
      ```json
        {
          "secret": "newsecret"
        }
       ```
    *  **Example Request** (using curl):
        ```bash
        curl -u admin:password -H "Content-Type: application/json" -X PUT -d '{"secret": "newsecret"}' "https://192.168.1.1/rest/radius/*0" -k
        ```
    *  **Example Response**
        ```json
         {
             "message": "updated",
             ".id": "*0"
          }
       ```

 *  Here is an example to remove an existing entry.
    *   **API Endpoint:** `/radius/<ID>`
    *   **Request Method:** DELETE
    *  **Example Request** (using curl):
         ```bash
        curl -u admin:password -H "Content-Type: application/json" -X DELETE  "https://192.168.1.1/rest/radius/*1" -k
        ```
    *  **Example Response**
        ```json
          {
             "message": "removed"
          }
       ```

## Security Best Practices:

*   **Secure RADIUS Secret:** Use a strong, complex shared secret. Do not use default passwords.
*   **Secure Communication:** Use IPSec or VPN tunnels between the router and RADIUS server, especially if the traffic traverses untrusted networks.
*   **Access Control Lists (ACLs):** Restrict access to the RADIUS server to the MikroTik router's IP address.
*   **Firewall:** Ensure the MikroTik router's firewall is configured to allow access to the RADIUS server only, and block any unsolicited traffic.
*   **Logging:** Monitor the router logs for any anomalies or suspicious activity related to RADIUS.
*   **Password Management:** Enable password complexity policies, and enforce strong authentication methods for administration access.

## Self Critique and Improvements:

*   **Redundancy:**  Implementing a secondary RADIUS server would enhance reliability.
*   **Monitoring:**  Adding monitoring for the RADIUS server would give early warnings on failures.
*  **Optimization:** Reviewing and optimizing the timeout settings in radius configurations, as well as the amount of parallel sessions will be required for peak utilization.
*   **More Specific Configuration**: Use a different profile for Radius authentication instead of the `default` profile.

## Detailed Explanations of Topic

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users who try to access a network service.  The main advantage of using RADIUS is that authentication is handled by an external server instead of the router itself. Here's a detailed breakdown:

*   **Authentication:**  RADIUS verifies a user's identity using credentials (username/password). It checks these credentials against a central database on the RADIUS server.
*   **Authorization:** Once a user is authenticated, RADIUS can authorize access to specific network resources based on predefined policies.
*  **Accounting:**  RADIUS tracks and logs usage information, such as session start and end times, amount of data transferred, etc. This data can be used for billing, reporting, and analyzing user behavior.

In a network environment, a MikroTik router acts as a RADIUS client, which sends authentication requests to the RADIUS server and acts based on the server's responses. The RADIUS server, typically running on a dedicated server or appliance, maintains user databases, policies, and manages authentication, authorization and accounting.

## Detailed Explanation of Trade-offs

*   **Local vs RADIUS Authentication:** Local user authentication on a MikroTik router is suitable for smaller setups with a limited number of users. RADIUS, however, provides centralized authentication and is necessary for more complex scenarios.
*   **Single vs Multiple RADIUS Servers:** A single RADIUS server may create a single point of failure. Multiple RADIUS servers offer redundancy but add complexity.
*  **Number of concurrent sessions**:  If the user count grows too large, a single RADIUS server might not be able to cope with all the requests. In this case either the existing server would need to be scaled up, or additional servers would need to be deployed. There is also a limit on the maximum number of concurrent sessions that the Mikrotik router can handle.
*   **Timeout values:** Very short timeouts can cause requests to fail due to network congestion or latency issues. Conversely, long timeouts may negatively impact the user experience.
*   **Encryption:** Disabling encryption could save system resources, but it can expose the user credentials. Enabling encryption adds a layer of security, but consumes more processing power.
*   **Accounting Data:** While very helpful, accounting information uses processing power to send to the RADIUS server.

## Configuration for Specific RouterOS Versions:

This configuration is designed for MikroTik RouterOS 6.48 (6.48, 7.x), and the commands are compatible with later 7.x versions. Note that older versions of RouterOS may use different syntax for the commands, and they might not be compatible. For RouterOS version 5.x, or earlier it is recommended to upgrade the RouterOS version.

That completes the comprehensive configuration documentation for RADIUS authentication on a MikroTik router. Let me know if you need any further assistance.
