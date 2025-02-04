Okay, let's dive into configuring PPP AAA (Authentication, Authorization, and Accounting) on MikroTik RouterOS 7.11 for an ISP environment, focusing on the subnet 4.46.20.0/24 and the interface `bridge-81`. We'll aim for an advanced configuration level.

## Scenario Description:

We are setting up a PPP server on a MikroTik router within an ISP infrastructure. This server will handle incoming PPP connections, typically from customer premises equipment (CPE) like home routers or modems. The PPP server will authenticate users via RADIUS, assign IP addresses from the 4.46.20.0/24 subnet, and track usage for billing and reporting. We will utilize `bridge-81` as the interface where the PPP connections are established.

## Implementation Steps:

Here's a detailed step-by-step guide:

**Detailed Explanation of Topic: PPP AAA**

PPP AAA stands for Point-to-Point Protocol Authentication, Authorization, and Accounting.  It is a core function for controlling user access and tracking resources.

*   **Authentication:** This is the process of verifying the identity of the user trying to connect. PPP typically uses protocols like PAP (Password Authentication Protocol) or CHAP (Challenge Handshake Authentication Protocol). For stronger security, EAP (Extensible Authentication Protocol) is often combined with RADIUS servers.
*   **Authorization:** Once authenticated, authorization determines what resources the user is allowed to access, such as specific IP addresses, bandwidth limitations, etc. This is also usually handled by a RADIUS server.
*   **Accounting:** Accounting tracks the resources a user consumes, like connection time and data transferred. This data is stored and used for reporting, billing, and monitoring. RADIUS servers are typically used to manage this.

**Detailed Explanation of Trade-offs**

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Simple to set up, suitable for small deployments, but not scalable or manageable for large ISP networks. Doesn't provide centralized management of users and policies. Can use PPP profiles that define the IP addresses, DNS settings and other user settings.
    *   **RADIUS:** Complex to set up, highly scalable, allows centralized management of users, policies and accounting. It enables dynamic user management, easy changing of policies and integration with billing/monitoring platforms.

*   **PAP vs. CHAP vs. EAP:**
    *   **PAP:** Sends passwords in plain text, highly insecure and should never be used for production environments.
    *   **CHAP:** Sends a hash of the password and a challenge, more secure than PAP but not as secure as EAP.
    *   **EAP:** Uses secure encryption methods, most secure option, and provides support for more advanced authentication mechanisms such as token-based, digital certificate based, etc. It's the preferred method for secure environments like ISPs.
*   **IP Address Allocation:**
    *   **Static IP Pools:**  Easy to set up, useful when using local user authentication or using RADIUS with statically assigned IPs. Not efficient for dynamic networks as it requires allocating an IP address for each subscriber.
    *   **Dynamic IP Pools with RADIUS:** The preferred way for ISPs where RADIUS provides IP assignment to connected PPP clients dynamically, ensuring maximum efficiency of IP addresses.

*   **Accounting:**
    *   **No Accounting:** Simpler setup but no visibility on usage or ability to charge users. Only useful in situations that don't require it.
    *   **RADIUS Accounting:** Detailed logs, enables usage-based billing, essential for ISP environments.
*   **Bridge Mode vs. Routing Mode:**
    *   **Bridging:** The router acts as a bridge, and the customer router obtains the public IP address. Easier setup, more direct, but harder for an ISP to manage traffic.
    *   **Routing:** The router terminates the PPP connection, and the ISP manages the user's routing directly. Provides more control for the ISP, and ability to manage the traffic. Requires a higher level of configuration and more complex management, but the most common one in ISP networks.

**Pre-configuration State**
Before beginning, let's assume that the following state is present on the router. We have `bridge-81` already created without an IP address assigned to it.

```
/interface bridge print
Flags: X - disabled, R - running
 0  R name="bridge-81" mtu=1500 l2mtu=1596 arp=enabled
      auto-mac=no admin-mac=F4:E9:D4:XX:XX:XX protocol-mode=rstp
      priority=0x8000 max-message-age=20s forward-delay=15s
      transmit-hold-count=6 ageing-time=300s
```
*Note: In the configuration above, the mac-address F4:E9:D4:XX:XX:XX would be the device's MAC address.*

**1. Configure the PPP Secret (Local User - Example):**

*   This step demonstrates a basic local user setup, which is rarely used in ISP environments.
*   **CLI:**

    ```mikrotik
    /ppp secret
    add name=testuser password=testpass service=ppp comment="Test user"
    print
    ```
*   **Winbox:** Navigate to `PPP > Secrets`, add a new secret with username `testuser`, password `testpass`, service `ppp`, and a comment "Test user".
*   **Explanation:** This creates a local user for authentication. This is for demonstration purposes and should not be used in production ISP environments with many users.  The `name` parameter is the username, `password` is the user's password, `service` determines what service will use it (in this case "ppp") and `comment` is simply descriptive text.

*   **After Configuration Result:**

    ```mikrotik
    /ppp secret print
    Flags: X - disabled, I - invalid
     #   NAME      SERVICE PROFILE   CALLER-ID  PASSWORD  LOCAL-ADDRESS  REMOTE-ADDRESS
     0   testuser   ppp     default  none      testpass    0.0.0.0     0.0.0.0
        COMMENT
        Test user
    ```

**2. Configure PPP Profile (Local IP Pool - Example):**

*   This step configures a PPP profile that defines how to manage the PPP connections.

*   **CLI:**

    ```mikrotik
    /ppp profile
    add name=testprofile local-address=4.46.20.1 remote-address=4.46.20.2-4.46.20.254 use-encryption=yes dns-server=8.8.8.8,8.8.4.4 comment="Test Profile"
    print
    ```
*   **Winbox:** Navigate to `PPP > Profiles`, add a new profile called `testprofile`. Set `local-address` to `4.46.20.1`,  `remote-address` to `4.46.20.2-4.46.20.254`, `use-encryption` to `yes` and `dns-server` to `8.8.8.8,8.8.4.4`, and add a comment "Test Profile".
*   **Explanation:**
    *   `name=testprofile`:  Name of the profile.
    *   `local-address`: The IP address the router will use for the connection. In a more complex environment this could also be an IP Pool, but here we provide a single one.
    *   `remote-address`: The IP range used for dynamic assigning of user IP addresses, or a fixed one for a specific user.
    *   `use-encryption`: If encryption should be enabled, as security is important, it's `yes` by default.
    *   `dns-server`: The DNS servers to provide to the client.
    *   `comment`: Descriptive text.

*   **After Configuration Result:**

    ```mikrotik
    /ppp profile print
    Flags: X - disabled, * - default
     #   NAME         LOCAL-ADDRESS  REMOTE-ADDRESS     BRIDGE      USE-ENCRYPTION  USE-COMPRESSION DNS-SERVER
     0   default      0.0.0.0        0.0.0.0              none                no              no
     1   testprofile 4.46.20.1      4.46.20.2-4.46.20.254 none                yes              no           8.8.8.8,8.8.4.4
         COMMENT
         Test Profile
    ```

**3. Configure PPP Server (Basic):**

*   This step sets up the PPP server on the specified interface.

*   **CLI:**
    ```mikrotik
    /interface ppp server
    add name=pppserver1 interface=bridge-81 profile=testprofile enabled=yes comment="Test PPP server"
    print
    ```
*   **Winbox:** Navigate to `PPP > Server`, add a new server, `name` is `pppserver1`, set `interface` to `bridge-81`, `profile` to `testprofile` enable it by setting `enabled` to `yes`, add a comment "Test PPP server".
*   **Explanation:**
    *   `name=pppserver1`: Name for the PPP server.
    *   `interface=bridge-81`: The interface on which the PPP server will listen for connections.
    *   `profile=testprofile`: The PPP profile to use.
    *   `enabled=yes`: Whether the server is enabled or not.
    *   `comment`: Descriptive text.

*   **After Configuration Result:**
    ```mikrotik
    /interface ppp server print
    Flags: X - disabled, R - running
     #   NAME       INTERFACE  PROFILE   MAX-MTU   MAX-MRU  MRRU AUTHENTICATION  KEEP-ALIVE   ONE-SESSION  ENABLED  COMMENT
     0   pppserver1 bridge-81 testprofile 1480      1480        disabled   mschap2           10s           no            yes  Test PPP server
    ```

**4. Configure RADIUS Client (ISP Environment - Example):**

*   This step is essential for an ISP environment, where we authenticate users with an external RADIUS server.
*   **CLI:**

    ```mikrotik
    /radius
    add address=192.168.88.1 secret=mysecret service=ppp timeout=1 comment="RADIUS Server 1"
    add address=192.168.88.2 secret=mysecret service=ppp timeout=1 comment="RADIUS Server 2"
    print
    ```
*   **Winbox:** Navigate to `RADIUS`, add two servers, with `address` `192.168.88.1`, and another with `192.168.88.2`. Set `secret` to `mysecret`, `service` to `ppp` and `timeout` to `1`, and comments "RADIUS Server 1" and "RADIUS Server 2" respectively.
*   **Explanation:**
    *   `address`: The IP address of the RADIUS server.
    *   `secret`:  The shared secret used for communication with the RADIUS server.
    *   `service`: The service for which RADIUS will be used (ppp).
    *   `timeout`: The timeout for RADIUS requests.
    *   `comment`: Descriptive text.

*   **After Configuration Result:**

    ```mikrotik
    /radius print
    Flags: X - disabled, I - invalid
     #   ADDRESS         SECRET     SERVICE   TIMEOUT   SRC-ADDRESS
     0   192.168.88.1   mysecret    ppp         1s
        COMMENT
        RADIUS Server 1
     1   192.168.88.2   mysecret    ppp         1s
        COMMENT
        RADIUS Server 2
    ```

**5.  Modify PPP Profile for RADIUS**

*  We change the profile to disable local secrets, and enable RADIUS authentication.
*   **CLI:**
    ```mikrotik
    /ppp profile set testprofile use-radius=yes
    print
    ```

*   **Winbox:** Navigate to `PPP > Profiles`, select `testprofile` , change the value of `use-radius` to `yes`.

*   **Explanation:**
    * `use-radius`: Tells the router to use RADIUS for authentication.

*   **After Configuration Result:**
     ```mikrotik
    /ppp profile print
    Flags: X - disabled, * - default
     #   NAME         LOCAL-ADDRESS  REMOTE-ADDRESS     BRIDGE      USE-ENCRYPTION  USE-COMPRESSION DNS-SERVER    USE-RADIUS
     0   default      0.0.0.0        0.0.0.0              none                no              no
     1   testprofile 4.46.20.1      4.46.20.2-4.46.20.254 none                yes              no           8.8.8.8,8.8.4.4 yes
         COMMENT
         Test Profile
    ```

## Complete Configuration Commands:

```mikrotik
# Configure PPP Secret (for local auth - example)
/ppp secret
add name=testuser password=testpass service=ppp comment="Test user"

# Configure PPP Profile (for local ip pool example)
/ppp profile
add name=testprofile local-address=4.46.20.1 remote-address=4.46.20.2-4.46.20.254 use-encryption=yes dns-server=8.8.8.8,8.8.4.4 comment="Test Profile"

# Configure PPP Server
/interface ppp server
add name=pppserver1 interface=bridge-81 profile=testprofile enabled=yes comment="Test PPP server"

# Configure RADIUS Client
/radius
add address=192.168.88.1 secret=mysecret service=ppp timeout=1 comment="RADIUS Server 1"
add address=192.168.88.2 secret=mysecret service=ppp timeout=1 comment="RADIUS Server 2"

#Modify PPP Profile to use RADIUS
/ppp profile set testprofile use-radius=yes
```

## Common Pitfalls and Solutions:

*   **RADIUS Connectivity Issues:**
    *   **Problem:**  Router cannot reach the RADIUS server.
    *   **Solution:** Verify the RADIUS server IP, shared secret, and network connectivity. Use `/tool ping <radius_ip>` and `/tool traceroute <radius_ip>` for diagnostics. Check firewall rules on the MikroTik and the RADIUS server.
*   **Authentication Failures:**
    *   **Problem:** PPP clients fail to authenticate.
    *   **Solution:** Double-check usernames and passwords on both the MikroTik and the RADIUS server. Check the RADIUS server logs for detailed error messages. Make sure the MikroTik is configured to use the correct authentication protocol (CHAP, EAP). Ensure there are no address conflicts in the IP pool assigned by the RADIUS server.
*   **IP Address Allocation Problems:**
    *   **Problem:** Clients are not receiving IP addresses or receiving incorrect ones.
    *   **Solution:** Verify the `remote-address` parameter in the PPP profile and verify the IP addresses assigned by the RADIUS server. If using local IP pool, ensure that the pool has enough IP address and doesn't clash with existing subnets. Check for any RADIUS attributes related to address allocation.
*   **MTU/MRU Mismatch:**
    *   **Problem:** Packet fragmentation leading to slow connections.
    *   **Solution:** Verify the MTU/MRU settings on both the MikroTik and the client devices. Ensure the values are consistent. The default is 1480 for ppp.
*   **Resource Exhaustion:**
    *   **Problem:** High CPU or memory usage due to numerous PPP connections.
    *   **Solution:** Monitor CPU/memory usage. Optimize the router configuration if needed (fasttrack, optimize firewall rules). Upgrade hardware if needed.
*   **Security:**
    *   **Problem:** Using PAP or weak shared secrets in RADIUS connections.
    *   **Solution:** Never use PAP. Always use strong, random passwords and shared secrets. Enable encryption where applicable (PPP and RADIUS).

## Verification and Testing Steps:

1.  **Connect a PPP client:** Configure a client device (e.g., another router, a computer using PPP) to connect to the MikroTik on `bridge-81`. Set the user/pass to match that configured on the RADIUS server or locally (if configured).
2.  **Monitor Active PPP Connections:** Use `/interface ppp active print` to check if a PPP connection is established. Look for the username and IP address assigned to the client.

    ```mikrotik
    /interface ppp active print
    Flags: R - running
     #   USER         SERVICE  CALLER-ID     ADDRESS   ENCODING
     0 R testuser   ppp      00:00:00:00:00:00 4.46.20.20 mppe128
    ```

3.  **Check RADIUS logs (on RADIUS server):** Look for successful authentication and accounting requests in the RADIUS server's logs. These will help with troubleshooting if required.
4.  **Ping the client IP:** From the MikroTik, ping the assigned IP address of the connected client `tool ping 4.46.20.20`
5.  **Check connectivity from client:** Connect via PPP, check IP, DNS and ensure full connectivity using `ping 8.8.8.8` from the client itself.
6.  **Use Torch:** Use the `/tool torch interface=bridge-81` tool to check the traffic on the bridge. This will show PPP packets.
7.  **Use Monitor:** Use the `/interface ppp monitor <number>` to see details about the specific connection.

## Related Features and Considerations:

*   **IP Pools:** For large deployments, use IP pools for dynamic IP address assignment managed by RADIUS.

    ```mikrotik
    /ip pool
    add name=ppp_pool ranges=4.46.20.2-4.46.20.254
    ```
*  **Routing Protocols:** Use routing protocols like OSPF or BGP to integrate the IP ranges assigned to PPP clients into the overall ISP routing infrastructure.
*   **Firewall:** Configure firewall rules to allow traffic for PPP clients, especially for essential services like DNS, DHCP, and HTTP(S).
*   **Traffic Shaping:** Implement traffic shaping using queues to control bandwidth allocation for individual PPP clients.
*   **VPNs:** Consider using IPsec or L2TP for additional security for the PPP connections.

## MikroTik REST API Examples:

*   **Retrieve PPP Secrets:**

    *   **Endpoint:** `/ppp/secret`
    *   **Method:** GET
    *   **Request:** None
    *   **Response (Example):**

        ```json
        [
            {
                ".id": "*0",
                "name": "testuser",
                "service": "ppp",
                "profile": "default",
                "caller-id": "none",
                "password": "testpass",
                "local-address": "0.0.0.0",
                "remote-address": "0.0.0.0",
                "comment": "Test user"
            }
         ]
         ```

*   **Add a New PPP Secret:**
    *   **Endpoint:** `/ppp/secret`
    *   **Method:** POST
    *   **Request (JSON payload):**
        ```json
            {
                "name": "apiuser",
                "password": "apipass",
                "service": "ppp",
                "comment": "API Created User"
            }
        ```
    *   **Response (Example):**
        ```json
        {
            "message": "added",
            "ret": "*1"
        }
        ```
       *Note: If this returns an error it will be in `{"message": <message>, "error": <error>}`*

* **Modify an Existing PPP Profile**
  * **Endpoint**: `/ppp/profile/<id>` (use the `.id` from the `/ppp/profile` call)
  * **Method**: PUT
  * **Request (JSON Payload):**
        ```json
        {
            "use-radius":"yes"
        }
        ```
    *   **Response (Example):**
        ```json
        {
            "message": "changed",
            "ret": "*1"
        }
        ```
      *Note: If this returns an error it will be in `{"message": <message>, "error": <error>}`*
*   **Error Handling:** Always check the `message` and `error` fields in the API response to handle errors gracefully.

## Security Best Practices:

*   **Use CHAP or EAP:** Avoid PAP as it sends passwords in plain text.
*   **Strong Passwords and Secrets:** Always use strong, randomly generated passwords and RADIUS shared secrets.
*   **Secure RADIUS Communication:** Ensure the communication between the MikroTik and the RADIUS server is secure.  Consider using IPsec to protect this communication.
*   **Firewall Rules:**  Implement strict firewall rules to limit access to the MikroTik management interface and services. Only allow required traffic to the router.
*   **Regular Updates:** Keep RouterOS and the RADIUS server up-to-date to patch any security vulnerabilities.
*   **Monitor Logs:** Regularly check MikroTik and RADIUS logs for any unusual activity.
*   **Traffic Shaping:** Implement traffic shaping with queues to limit per-user resources, to prevent one single user from consuming all bandwidth.
*   **MAC Address Filtering:** If not using RADIUS authentication, use MAC address filtering on PPP secrets to prevent unauthorized access.
*   **Banning Failed login attempts:** Use the MikroTik firewall to ban any IP trying to brute-force the PPP connection.

## Self Critique and Improvements:

*   **Complexity:** The initial setup is basic, but the explanation is detailed and comprehensive.
*   **Flexibility:** The local-user based authentication and ip assignment are not suitable for large ISP environments. They should be removed, in favour of a more scalable solution like RADIUS based authentication.
*   **Scalability:** The example needs to be extended to use IP pools and implement routing protocols.
*   **Automation:** To further improve this config, add automation through the API or configuration management tools.
*   **Security**: Adding firewall examples would improve this document.

## Configuration for Specific RouterOS Versions:
These commands are specifically designed for RouterOS 7.11. The commands will also work on 6.48 and other 7.x versions, but it's always best to consult the documentation if the behaviour of a specific command changes in a newer version. Always check MikroTik's official documentation for your specific router and firmware version.
