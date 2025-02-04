Okay, let's craft a detailed technical document for setting up PPP AAA on a MikroTik router (RouterOS 7.12), with a focus on an ISP-like scenario, and using `wlan-85` interface on the `109.23.129.0/24` subnet.

## Scenario Description:

This document describes the configuration of a MikroTik router, running RouterOS 7.12, as a PPP server (for example, PPPoE or PPTP), where user authentication and authorization are handled by a RADIUS server. The `wlan-85` interface, operating within the `109.23.129.0/24` subnet, will be the interface where clients connect and establish PPP connections. This setup is typical for ISPs, Hotspot networks, or environments requiring centralized authentication for PPP users. The authentication will happen against a RADIUS server using the PAP, CHAP and MSCHAP protocols. This implementation is of Basic configuration level.

## Implementation Steps:

Here is a step-by-step guide, explaining each step, the reason for it, and providing MikroTik CLI/Winbox examples:

**Before We Begin**

Before any configuration, make sure you:
1. Know the IP address of your RADIUS server.
2. Know the secret key used for communication with the RADIUS server.
3. Have a basic understanding of network interfaces on MikroTik.

**Step 1: Configure the WLAN Interface**

*   **Description:** This step is to ensure the interface used for PPP connections is properly configured. In this case, we are assuming an active wireless interface with appropriate settings (Mode, Frequency, Channel Width, etc.) already in place. The only change we need to make is to add the proper IP Address.
*   **Why:** The interface needs to have an IP address within the subnet where the clients will connect.
*   **CLI Example (Before):**
    ```mikrotik
    /interface/print
    # Output (example):
    # 0   name="wlan1" type=wlan mtu=1500 l2mtu=1600 mac-address=AA:BB:CC:DD:EE:FF ...
    # ... other interfaces ...
    ```

*   **CLI Example:**
    ```mikrotik
    /ip address
    add address=109.23.129.1/24 interface=wlan-85 network=109.23.129.0
    ```
*   **Winbox Example:** Navigate to `IP -> Addresses`, click the "+", add the IP `109.23.129.1/24`, choose `wlan-85` as the interface, and click "Apply".
*   **CLI Example (After):**
    ```mikrotik
    /ip address/print
    # Output (example):
    # 0 address=109.23.129.1/24 interface=wlan-85 network=109.23.129.0
    # ... other interfaces ...
    ```

*   **Effect:** The `wlan-85` interface will now have the IP address `109.23.129.1/24` associated with it.

**Step 2: Configure RADIUS Server Settings**

*   **Description:** Define the connection parameters to your RADIUS server.
*   **Why:**  The router needs to know how to communicate with the RADIUS server for authentication.
*   **CLI Example (Before):**
    ```mikrotik
    /radius/print
    # Output (example):
    #
    ```
*   **CLI Example:**
    ```mikrotik
    /radius add address=192.168.100.1 secret="YOUR_RADIUS_SECRET" service=ppp timeout=3
    ```
    **Note:** Replace `192.168.100.1` with your RADIUS server IP and `YOUR_RADIUS_SECRET` with the shared secret.
*   **Winbox Example:** Go to `RADIUS` under the `PPP` menu, Click the "+", fill in the `Address`, `Secret` and ensure `ppp` is enabled in `Service` and click "Apply".

*   **CLI Example (After):**
    ```mikrotik
    /radius/print
    # Output (example):
    # 0 address=192.168.100.1 secret="YOUR_RADIUS_SECRET" service=ppp timeout=3
    ```

*   **Effect:** The MikroTik router is configured to contact the RADIUS server at the specified IP address using the shared secret.

**Step 3: Enable PPP Authentication and Authorization**

*   **Description:** Configure the PPP profile to use RADIUS for authentication and accounting.
*   **Why:** This enables authentication of PPP users via RADIUS. The authentication can be set by a default value or, better yet, we can specify which authentication types are allowed on a per profile basis.
*   **CLI Example (Before):**
    ```mikrotik
    /ppp profile/print
    # Output (example)
    # 0   name="default" use-encryption=yes change-tcp-mss=yes  ...
    ```
*  **CLI Example**
    ```mikrotik
        /ppp profile set default use-radius=yes only-one=no authentication=pap,chap,mschap1,mschap2
    ```
*   **Winbox Example:** Navigate to `PPP` -> `Profiles`, double-click on `default`, check `Use Radius` and select the authentication types under `Authentication`. Press "Apply" button.
*   **CLI Example (After):**
    ```mikrotik
    /ppp profile/print
    # Output (example):
    # 0   name="default" use-encryption=yes use-radius=yes only-one=no authentication=pap,chap,mschap1,mschap2
    ```

*   **Effect:** All new PPP connections using the `default` profile will now authenticate via the configured RADIUS server.

**Step 4: Enable and Configure PPP Server (PPPoE Example)**

*   **Description:** Enable PPPoE server on the `wlan-85` interface and assign the profile to be used by the clients.
*   **Why:** This enables clients to connect via PPPoE protocol and authenticate using the defined RADIUS.
*   **CLI Example (Before):**
    ```mikrotik
        /ppp server pppoe print
        # Output (example)
        # Flags: X - disabled, I - invalid
        #
    ```
*   **CLI Example:**
    ```mikrotik
        /ppp server pppoe add disabled=no interface=wlan-85 service-name=pppoe-service-1 profile=default
    ```
*  **Winbox Example:** Navigate to `PPP` -> `PPPoE Server`, click the "+" to add a new entry, select the interface `wlan-85`, set the service name and select `default` in the profile field. Ensure it is not disabled and press "Apply" button.
*   **CLI Example (After):**
    ```mikrotik
        /ppp server pppoe print
        # Output (example)
        # Flags: X - disabled, I - invalid
        # 0   interface=wlan-85 service-name=pppoe-service-1 profile=default disabled=no max-mtu=1480 max-mru=1480
    ```

*   **Effect:** Clients will now be able to connect via PPPoE on the `wlan-85` interface, authenticating via RADIUS.

## Complete Configuration Commands:

```mikrotik
/ip address
add address=109.23.129.1/24 interface=wlan-85 network=109.23.129.0

/radius
add address=192.168.100.1 secret="YOUR_RADIUS_SECRET" service=ppp timeout=3

/ppp profile
set default use-radius=yes only-one=no authentication=pap,chap,mschap1,mschap2

/ppp server pppoe
add disabled=no interface=wlan-85 service-name=pppoe-service-1 profile=default
```
**Parameter Explanation:**
| Command | Parameter | Value | Description |
|-----------------|----------------|--------------------------------------|-------------------------------------------------------------------------------|
|`/ip address add` |`address` | `109.23.129.1/24` | IP address and subnet mask to assign to the interface.|
|`interface`| `wlan-85`| The target interface.
|`network` | `109.23.129.0` | The network address of the subnet
|`/radius add` |`address`| `192.168.100.1` | IP address of the RADIUS server.|
| |`secret`| `"YOUR_RADIUS_SECRET"`| Shared secret used for RADIUS communication.|
| |`service`| `ppp` | Specifies that this RADIUS server is for PPP connections.|
|  | `timeout` | `3` | The timeout, in seconds, to wait for a response from the RADIUS server.|
|`/ppp profile set default` |`use-radius`| `yes` | Enables RADIUS authentication for this profile.|
|  |`only-one`|`no`|Allows multiple connections by the same user on different interfaces.|
|  | `authentication`|`pap,chap,mschap1,mschap2`|The accepted authentication protocols.
|`/ppp server pppoe add`| `disabled` | `no` | Enables the PPPoE server.|
|  | `interface` | `wlan-85` | Interface where the PPPoE server listens for connections.|
| | `service-name`| `pppoe-service-1` | The name of the service, shown to the clients
| | `profile` | `default` | The PPP profile to be used for new connections.|

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router can't communicate with the RADIUS server.
    *   **Solution:**
        *   Verify the RADIUS server IP address is correct (`/radius print`).
        *   Check for network connectivity between the MikroTik and the RADIUS server (use `ping 192.168.100.1`).
        *   Ensure the shared secret is identical on both devices.
        *   Firewall rules may be blocking RADIUS traffic (UDP port 1812 and 1813 by default, check `/ip firewall filter print`).
*   **Authentication Failures:**
    *   **Problem:** Clients fail to authenticate with the RADIUS server.
    *   **Solution:**
        *   Verify RADIUS logs on the server side for any errors.
        *   Make sure the user credentials exist and are correct on the RADIUS server.
        *   Check the allowed authentication methods in the PPP profile `/ppp profile print` .
        *   Ensure there is no configuration error on the MikroTik RADIUS client.
*   **PPP Profile Configuration Issues:**
    *   **Problem:** Incorrect settings in the PPP profile lead to connection issues.
    *   **Solution:**
        *   Verify all settings in `/ppp profile print`, specifically `use-radius` and `authentication`.
* **Resource Issues:**
   *   **Problem**: The router is suffering from resource issues, such as high CPU or RAM usage when many users connect using PPP.
   *  **Solution:** Check the router resource consumption by running `/system resource print`. If the CPU is too high, consider using hardware acceleration for encryption, reducing the number of connected users, or upgrading the hardware itself.

## Verification and Testing Steps:

1.  **Check RADIUS Configuration:**
    *   Use `/radius print` and check that all settings are correct.
    *   Run `/tool sniffer quick interface=wlan-85  filter=port=1812` to see if RADIUS packets are reaching the device. If a packet from the RADIUS server arrives, the client is working and is reachable, the problem might be that the RADIUS server is sending back an ACCESS-REJECT.
2.  **Client Connection:**
    *   Connect a client device (laptop, mobile) to the `wlan-85` network.
    *   Configure the PPPoE client with the required credentials.
    *   Attempt to connect to the `pppoe-service-1` PPPoE service.
3.  **Verify Connection:**
    *   On the MikroTik, run `/ppp active print`. If the user has correctly logged into the system, there should be a new entry under the `active` menu. This will also show the IP address assigned to the user by the RADIUS server, if a framed IP address is used.
    *   Use `/log print` or `/system logging action print` to check for any errors.
    *   If there are authentication failures, it should be logged on the RADIUS server.
4. **Testing using `ping` and `traceroute`**
     * From a client device connected via the PPPoE tunnel, use `ping` and `traceroute` to reach an external server to check if the connection works as expected.

## Related Features and Considerations:

*   **Multiple RADIUS Servers:** Configure backup RADIUS servers for redundancy (`/radius add address=... secret=... service=ppp timeout=3`).
*   **Accounting:**  Enable accounting with `accounting=yes` in `/ppp profile` for usage tracking.
*  **MikroTik Userman:** Use the built-in Usermanager to manage user accounts and profiles.
*   **IP Pools:** Define address pools to be used for the PPP connections (`/ip pool add name=ppp-pool ranges=10.0.0.10-10.0.0.200`).
*  **Traffic Shaping and QoS:** Implement traffic shaping rules to control the bandwidth for specific users connected via PPP.
*   **Firewall Rules:** Secure the network by adding firewall rules (`/ip firewall filter`) to limit access to specific services.

## MikroTik REST API Examples:

Here are some REST API examples using the MikroTik API. Assume the IP of the router is `10.0.0.2`

**1. Get the list of available RADIUS Servers**

*   **Endpoint:** `https://10.0.0.2/rest/ppp/radius`
*   **Method:** `GET`
*   **Request:** No Request Body.
*  **Example `curl` request:**
    ```bash
    curl -k -u user:password  https://10.0.0.2/rest/ppp/radius -H "Content-Type: application/json"
    ```
*   **Expected Response (JSON):**
    ```json
    [
      {
        ".id": "*1",
        "address": "192.168.100.1",
        "secret": "YOUR_RADIUS_SECRET",
        "service": "ppp",
        "timeout": "3",
        "authentication": true,
        "accounting": false
      }
    ]
    ```

**2. Add a new RADIUS Server**

*   **Endpoint:** `https://10.0.0.2/rest/ppp/radius`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
      "address": "192.168.100.2",
      "secret": "ANOTHER_RADIUS_SECRET",
      "service": "ppp",
      "timeout": "5"
    }
    ```
*   **Example `curl` request:**
     ```bash
      curl -k -u user:password -X POST https://10.0.0.2/rest/ppp/radius -H "Content-Type: application/json" -d  '{ "address": "192.168.100.2", "secret": "ANOTHER_RADIUS_SECRET", "service": "ppp", "timeout": "5"}'
     ```
*   **Expected Response (JSON):**
    ```json
    {
        ".id": "*2",
        "address": "192.168.100.2",
        "secret": "ANOTHER_RADIUS_SECRET",
        "service": "ppp",
        "timeout": "5",
        "authentication": true,
        "accounting": false
      }
    ```
* **Error Handling:**
     * If an error occurs, the API will return a JSON payload with a `"message"` field explaining the error
     * The HTTP status code will also reflect the error, such as `400` for bad requests or `500` for internal server errors.

**3. Change the authentication methods of the default ppp profile**
* **Endpoint:** `https://10.0.0.2/rest/ppp/profile/default`
* **Method:** `PATCH`
* **Request Body (JSON)**
    ```json
    {
       "authentication": "chap,mschap2"
    }
    ```
*  **Example `curl` request:**
    ```bash
     curl -k -u user:password -X PATCH https://10.0.0.2/rest/ppp/profile/default -H "Content-Type: application/json" -d '{ "authentication": "chap,mschap2"}'
   ```
*   **Expected Response (JSON):**
    ```json
       {
        ".id": "*0",
        "name": "default",
        "use-encryption": true,
        "change-tcp-mss": true,
        "use-upnp": false,
        "use-radius": true,
        "only-one": false,
        "authentication": "chap,mschap2",
         ...
      }
    ```

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a complex, long, and unique secret key for RADIUS communication.
*   **Firewall Rules:** Block access to the RADIUS ports (UDP 1812, 1813) from untrusted networks.
*   **Regular Password Rotation:** Encourage strong and frequently rotated passwords for users connecting via PPP.
*   **Encryption:** Enforce encryption using protocols such as `MPPE` or `AES`, depending on the client capabilities.
*  **Monitor the logs:** Setup logging to monitor PPP and RADIUS activity. Pay attention to failed authentication attempts and abnormal connection behavior.
*   **RouterOS Security:** Keep the RouterOS software updated to patch any security vulnerabilities.

## Self Critique and Improvements:

*   **Current:** The configuration is basic and focuses on essential functionality.
*   **Improvements:**
    *   Implement more advanced features like accounting for usage tracking and limits.
    *   Integrate with User Manager for centralized user management.
    *   Explore dynamic IP address allocation through RADIUS.
    *   Configure a more comprehensive firewall to limit access to the internal network.
    *   Implement advanced QoS policies for traffic shaping.
    *   Provide logging and monitoring with tools like The Dude or Grafana.
    *   Setup a backup server or redundant hardware for increased reliability.
    *  Use more complex authentication mechanisms, such as EAP.

## Detailed Explanations of Topic:

**PPP (Point-to-Point Protocol):**

*   A data link layer communication protocol used to establish a direct connection between two nodes.
*   Commonly used for dial-up, DSL, VPNs, and other point-to-point links.
*   MikroTik supports various PPP protocols including PPPoE, PPTP, L2TP, and SSTP.
*   PPP protocols encapsulate data packets and provide authentication, encryption, and compression.

**AAA (Authentication, Authorization, and Accounting):**

*   A framework for controlling access to network resources.
    *   **Authentication:** Verifying the user's identity (username/password, certificates etc.).
    *   **Authorization:** Determining what a user is allowed to do after authentication (access to specific resources, permissions etc.).
    *   **Accounting:** Tracking resource usage, such as data transfer, connection time etc.
*   RADIUS (Remote Authentication Dial-In User Service):
    *   A networking protocol that provides centralized AAA management for users connecting to a network.
    *   Uses a client-server model where the network device (MikroTik) acts as a client, and the RADIUS server handles authentication and authorization.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Simple to set up but difficult to manage in larger networks. Configuration is done directly on the router.
    *   **RADIUS:** More complex to set up, but provides centralized user management and easier scaling. Allows for sophisticated accounting and security policies.
*   **PAP, CHAP, MSCHAP Protocols:**
    *   **PAP (Password Authentication Protocol):** Transmits passwords in clear text, highly insecure.
    *   **CHAP (Challenge Handshake Authentication Protocol):** Provides a hashed password, more secure than PAP, but still vulnerable.
    *   **MSCHAP (Microsoft Challenge Handshake Authentication Protocol):** Microsoft's variant of CHAP, but also vulnerable to attacks. MSCHAP v2 has some improvements but is also susceptible to attacks, therefore using the latest protocols in authentication such as `EAP` is the most secure alternative.
*   **PPPoE vs. Other PPP Protocols (PPTP, L2TP):**
    *   **PPPoE (PPP over Ethernet):** Typically used in DSL networks, provides Ethernet-like access over an existing Ethernet infrastructure, less prone to NAT issues than the other PPP protocols.
    *   **PPTP (Point-to-Point Tunneling Protocol):** Simple and widely supported, but less secure and prone to NAT traversal issues.
    *   **L2TP (Layer 2 Tunneling Protocol):** Generally more secure than PPTP, but also more complex to configure. Can be used for VPNs.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 7.12, and should work without any modification. However, if you are using a version such as 6.48, you might find some minor differences, especially on the WebUI and on parameters names. All the commands provided, however, should work without modification, as well as the APIs provided.

I've tried my best to create a comprehensive, practical, and actionable guide with a clear focus on MikroTik RouterOS, keeping the needs of a reader with basic configuration level in mind. If there are any points I have missed or that need further expansion, please let me know!
