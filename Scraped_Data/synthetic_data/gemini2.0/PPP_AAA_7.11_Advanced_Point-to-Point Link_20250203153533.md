Okay, let's dive into creating detailed technical documentation for implementing PPP AAA (Authentication, Authorization, and Accounting) on a MikroTik RouterOS device (specifically v7.11, with notes for v6.48 and 7.x) for a point-to-point link using a `/24` subnet on a wireless interface. This will be an advanced level configuration.

## Scenario Description

This scenario outlines configuring a MikroTik router acting as a Point-to-Point link server using PPP with AAA, specifically authenticating users via RADIUS (for example, a FreeRADIUS server). The network will utilize the subnet `46.214.129.0/24`, and the wireless interface acting as the point-to-point interface will be `wlan-87`. All connections over the `wlan-87` interface will be authenticated by the defined RADIUS server with user specific access. We will be using a secure CHAP authentication, since password based authentication is generally insecure.

## Implementation Steps

Here’s a step-by-step guide to configure PPP AAA using a RADIUS server, focusing on a Point-to-Point link.

**Assumptions:**

*   You have a basic understanding of MikroTik RouterOS.
*   You have a functioning RADIUS server with the IP `192.168.88.100` (change it to match your setup).
*   You have a secret shared between the MikroTik and the RADIUS server. (We will use 'supersecret' for this example).
*   You have basic knowledge of PPP.

### Step 1: Configure the Wireless Interface

**Description:** We start by configuring the wireless interface to operate in station mode, creating a basic point to point link.

**Before:**
```
/interface wireless print
```
**Output (Example):**

```
Flags: X - disabled, R - running
 0  R name="wlan1" mtu=1500 mac-address=D4:CA:6D:12:34:56 arp=enabled
      mode=ap-bridge ssid="MyAP" frequency=2437 band=2ghz-b/g/n channel-width=20mhz
      wireless-protocol=802.11
...
```
**Action:** Configure the wireless interface as a station to connect to the remote access point. Replace the values with your own, especially the `ssid` and `master-interface`. If no interface exists, you will need to add one.
```
/interface wireless
set wlan1 mode=station
set wlan1 ssid="RemoteAP"
set wlan1 master-interface=wlan-87
set wlan1 security-profile=default
```
**After:**

```
/interface wireless print
```
**Output (Example):**

```
Flags: X - disabled, R - running
 0  R name="wlan1" mtu=1500 mac-address=D4:CA:6D:12:34:56 arp=enabled
      mode=station ssid="RemoteAP" frequency=2437 band=2ghz-b/g/n channel-width=20mhz
      wireless-protocol=802.11 master-interface=wlan-87
...
```
**Explanation:**
*   `mode=station`:  Configures the interface to connect to another access point.
*   `ssid="RemoteAP"`:  The SSID of the access point it's connecting to. Replace with the correct one.
*   `master-interface=wlan-87`: We map the logical `wlan-87` interface to the actual physical interface `wlan1`. We will configure the PPP setup on the `wlan-87` interface instead of `wlan1`
* `security-profile=default`: Use the default security profile for now, modify it later if required.

### Step 2: Create a PPP Server Interface

**Description:**  Create the PPP server interface. This will manage the PPP connections initiated from the connected station.

**Before:**
```
/interface ppp server print
```

**Output:**
```
Flags: X - disabled, R - running
```

**Action:** Create the PPP server.

```
/interface ppp server
add name=ppp-server-wlan interface=wlan-87 service=pptp enabled=yes
```
**After:**

```
/interface ppp server print
```
**Output:**
```
Flags: X - disabled, R - running
 0   name="ppp-server-wlan" max-mtu=1480 max-mru=1480 mrru=disabled
      interface=wlan-87 service=pptp profile=default keepalive-timeout=10
      max-sessions=0 authentication=pap,chap,mschap1,mschap2
      enabled=yes
```
**Explanation:**

*   `add name=ppp-server-wlan`: Adds a PPP server interface named `ppp-server-wlan`.
*   `interface=wlan-87`: Binds the PPP server to the `wlan-87` interface.
*   `service=pptp`: Sets the service to PPTP. This can be changed to `pppoe-server` if necessary. You must be careful to only pick one service. It is not possible to serve both at the same interface.
*   `enabled=yes`:  Enables the PPP server.

### Step 3: Configure RADIUS Settings

**Description:** Configure the router to use the RADIUS server for authentication and accounting.

**Before:**
```
/radius print
```
**Output:**
```
Flags: X - disabled
```

**Action:** Add RADIUS server details.

```
/radius
add address=192.168.88.100 secret=supersecret service=ppp,login,hotspot timeout=10
```
**After:**
```
/radius print
```
**Output:**

```
Flags: X - disabled, R - running
 0   address=192.168.88.100 secret="supersecret" timeout=3 authentication-port=1812
     accounting-port=1813  called-id="" domain="" service=ppp,login,hotspot
     radius-domain="" realm=""  src-address=""
```

**Explanation:**

*   `add address=192.168.88.100`: IP address of your RADIUS server.
*   `secret=supersecret`: The shared secret key used between the MikroTik and RADIUS server, which must match the secret of the server.
*   `service=ppp,login,hotspot`:  Specifies the services that use this RADIUS configuration (this example includes `ppp`, `login` for management login, and `hotspot`).
*   `timeout=10`: Specifies the maximum time to wait for a response from the RADIUS server (10 seconds, or choose the correct value based on server latency).

### Step 4: Set PPP Profile to Use RADIUS

**Description:** Modify the PPP Profile to use RADIUS for authentication and accounting.

**Before:**
```
/ppp profile print
```
**Output:**

```
Flags: * - default
 0   name="default" use-encryption=yes only-one=no change-tcp-mss=yes
     address-list="" local-address=0.0.0.0 remote-address=0.0.0.0
     dns-server=0.0.0.0,0.0.0.0 bridge="" comment=""
     use-compression=no use-vj-compression=no on-up=""
     on-down=""
```

**Action:** Modify the default profile to use RADIUS for authentication and accounting.

```
/ppp profile set default use-radius=yes
/ppp profile set default use-encryption=yes
/ppp profile set default address-list="ppp_clients"
/ppp profile set default local-address=46.214.129.1
/ppp profile set default remote-address=46.214.129.2-46.214.129.254
```
**After:**
```
/ppp profile print
```
**Output:**

```
Flags: * - default
 0 * name="default" use-encryption=yes only-one=no change-tcp-mss=yes
     address-list="ppp_clients" local-address=46.214.129.1
     remote-address=46.214.129.2-46.214.129.254 dns-server=0.0.0.0,0.0.0.0
     bridge="" comment="" use-compression=no use-vj-compression=no
     on-up="" on-down="" use-radius=yes
```

**Explanation:**

*   `use-radius=yes`: Enables the use of RADIUS for authentication and accounting.
*   `use-encryption=yes`: We enforce encryption for connections.
*   `address-list=ppp_clients`:  Add the IP address to the address list 'ppp_clients', allowing for specific firewall rules.
* `local-address=46.214.129.1`: Set the local address for the PPP connections.
* `remote-address=46.214.129.2-46.214.129.254`: Set the IP address range for remote clients.

### Step 5: Enable PPP Server on the Interface

**Description:** Enable the server.

**Before:**

```
/interface ppp server print
```
**Output:**

```
Flags: X - disabled, R - running
 0   name="ppp-server-wlan" max-mtu=1480 max-mru=1480 mrru=disabled
      interface=wlan-87 service=pptp profile=default keepalive-timeout=10
      max-sessions=0 authentication=pap,chap,mschap1,mschap2
      enabled=yes
```
**Action:** Enable the server, as it was enabled on previous step already, and configure the `authentication` to be only `chap`.
```
/interface ppp server set ppp-server-wlan authentication=chap
```
**After:**

```
/interface ppp server print
```
**Output:**

```
Flags: X - disabled, R - running
 0   name="ppp-server-wlan" max-mtu=1480 max-mru=1480 mrru=disabled
      interface=wlan-87 service=pptp profile=default keepalive-timeout=10
      max-sessions=0 authentication=chap
      enabled=yes
```

**Explanation:**

*   `authentication=chap`: Enforce CHAP as authentication method.

## Complete Configuration Commands

```
/interface wireless
set wlan1 mode=station
set wlan1 ssid="RemoteAP"
set wlan1 master-interface=wlan-87
set wlan1 security-profile=default

/interface ppp server
add name=ppp-server-wlan interface=wlan-87 service=pptp enabled=yes

/radius
add address=192.168.88.100 secret=supersecret service=ppp,login,hotspot timeout=10

/ppp profile set default use-radius=yes
/ppp profile set default use-encryption=yes
/ppp profile set default address-list="ppp_clients"
/ppp profile set default local-address=46.214.129.1
/ppp profile set default remote-address=46.214.129.2-46.214.129.254

/interface ppp server set ppp-server-wlan authentication=chap
```

## Common Pitfalls and Solutions

*   **RADIUS Connectivity Issues**:
    *   **Problem**: Router cannot reach the RADIUS server.
    *   **Solution**:
        *   Use `/tool ping` to verify IP connectivity to the RADIUS server.
        *   Check firewall rules on both the router and RADIUS server.
        *   Verify the RADIUS `address` and `secret` are correct.
*   **Authentication Failures**:
    *   **Problem**: Users cannot authenticate.
    *   **Solution**:
        *   Examine RADIUS logs for specific authentication failures.
        *   Ensure the RADIUS server has the correct user credentials.
        *   Verify `authentication` is set correctly on the ppp server, the default is `pap,chap,mschap1,mschap2` but we enforce only `chap` in this example.
*   **Incorrect Profile Settings**:
    *   **Problem**: Client gets connected, but is not able to access the internet.
    *   **Solution**:
         *   Verify that `use-radius`, `use-encryption`, `local-address`, and `remote-address` are configured in the profile.
        *   Ensure the address range of the local interface and the remote address range does not overlap.
*   **Resource Usage**:
    *   **Problem**: High CPU or memory usage due to many PPP sessions.
    *   **Solution**:
        *   Monitor resource usage with `/system resource print`.
        *   Upgrade hardware if necessary.
        *   Implement connection limits with `max-sessions` in `/interface ppp server`.
*  **PPP Interface Not Creating:**
    * **Problem:** The client is correctly authenticating but the PPP interface is not being established
    * **Solution:** Ensure that both the client and the server are not trying to use the same IP address range. This will lead to a conflict. Double check the ranges defined in both client and server.

## Verification and Testing Steps

1.  **RADIUS Connectivity**:
    *   Use `/tool ping 192.168.88.100` to verify the router can reach the RADIUS server.

2.  **PPP Connection**:
    *   Connect to the ppp-server with a client that is configured to authenticate using CHAP.
    *   Observe the client's connection using `/interface ppp active print`

    ```
    /interface ppp active print
    ```
    **Example Output:**
    ```
    Flags: R - running
     0 R name="ppp-user1" mtu=1480 mac-address=XX:XX:XX:XX:XX:XX
          remote-address=46.214.129.2 local-address=46.214.129.1
          encoding=mppe-128 use-encryption=yes profile=default
          uptime=2m33s
    ```

3.  **Authentication**:
    *   Check RADIUS logs on the RADIUS server for successful authentication requests.

4.  **Address List**:
    *   Use `/ip firewall address-list print` and check if the dynamic `ppp_clients` is populated with the IP address of the connected client.

5.  **Traceroute**:
    *   From the client, use `traceroute` to the remote-end of the link to ensure that routing is working as expected.
    *   Use MikroTik's traceroute tool `/tool traceroute <destination_ip>` on the server-side as well.

## Related Features and Considerations

*   **Firewall Rules**: Add firewall rules using the `ppp_clients` address list for granular access control.
*   **Bandwidth Control**: Apply traffic shaping or queues to limit bandwidth per user in `/queue simple`.
*   **Logging**: Enable more detailed logging for debugging purposes using `/system logging`.
*   **User Management**: Use RADIUS to handle advanced user features, such as user-specific bandwidth limits, or access restrictions.
*   **PPPoE vs PPTP**: Use PPPoE server and configure a client, rather than the PPTP example to enhance security, or use a VPN connection to secure the underlying wireless channel, with a technology such as IKEv2 or Wireguard.
* **Routing:** Add specific routing entries for better traffic control.

## MikroTik REST API Examples

*This is a hypothetical example, as we're mostly using system configurations, the API equivalent is not direct. To change these specific parameters, we would have to use the `set` command over the `/system/console` endpoint, and read the state via `get`. For this scenario the REST api usage is not a direct conversion to cli.*

**Example API Request (Hypothetical for modifying ppp profile - Not Directly Applicable)**

*   **Endpoint**: `/ppp/profile/default`
*   **Method**: `PUT`
*   **Request Body (JSON):**

```json
{
  "use-radius": true,
  "use-encryption": true,
  "address-list": "ppp_clients",
   "local-address": "46.214.129.1",
   "remote-address": "46.214.129.2-46.214.129.254"
}
```

*   **Expected Response (JSON):**

```json
{
  "message": "Profile 'default' updated successfully"
}
```

*   **API Error Handling**:
    *   If the request fails, the API might return a status code other than 200 or a JSON object with an `error` field, containing a description of the problem and a status code.

## Security Best Practices

*   **Use CHAP**: Avoid PAP, which sends passwords in plaintext, and prefer CHAP as authentication method.
*   **Strong RADIUS Secret**: Use a complex and unpredictable secret for the RADIUS server.
*   **Firewall Rules**: Use firewall rules to limit access to the router's management interfaces and the RADIUS server.
*   **Regular Updates**: Keep RouterOS updated to the latest version to patch known security vulnerabilities.
*  **Access Control:** Restrict access to the router to authorized users only.
* **Disable Unnecessary Services:** Disable all unused services, especially on the public interface of the router.

## Self Critique and Improvements

This configuration covers the basics of PPP AAA using RADIUS.

**Improvements:**

*   **More Advanced User Management**: Implement user-specific attributes via RADIUS to manage bandwidth, service profiles, etc.
*   **VPN Layer**: Consider using a VPN over the PPP link for additional security. This could be done with IKEv2 or Wireguard, providing a tunnel on top of the wireless channel.
*   **Dynamic RADIUS Server**: Enhance the setup to dynamically allocate RADIUS servers depending on location.
*   **Advanced Queueing**: Add more sophisticated queueing based on the `ppp_clients` address list.

## Detailed Explanations of Topic

**PPP AAA (Authentication, Authorization, Accounting)**

*   **Authentication**: Verifying the identity of the user connecting (e.g., username and password via RADIUS).
*   **Authorization**: Determining what resources and services the authenticated user is allowed to access (handled by RADIUS server attributes).
*   **Accounting**: Tracking user activity (e.g., connection time, bandwidth usage) for billing and monitoring purposes.
*   **RADIUS (Remote Authentication Dial-In User Service)**:  A centralized authentication protocol commonly used for network access control. It allows a network to authenticate and authorize users against a central database.

## Detailed Explanation of Trade-offs

*   **PAP vs. CHAP:** PAP is easier to configure but sends passwords in cleartext, making it insecure. CHAP is more secure as it uses a challenge-response method instead of sending the password directly.
*   **Local User Accounts vs. RADIUS**: Local user accounts are simple for small networks but do not scale well. RADIUS provides a centralized, scalable solution.
*   **PPTP vs. PPPoE:** PPTP is easy to configure but less secure than PPPoE. PPPoE can be more resource intensive.
*   **Encryption**: Encryption introduces some overhead but is essential for securing user data and credentials. Not enabling encryption can expose traffic.
*   **Radius vs Local Authorization:** Local authorization can be used for less complex networks, but lacks the advanced options that can be found in RADIUS. RADIUS has extensive capabilities for authorizing and logging sessions.

## Configuration for Specific RouterOS Versions

This configuration is targeted at RouterOS v7.11. It should also work with v7.x versions, since no commands that were introduced after were used. In case you are using v6.48, here are some key differences:

*   **RADIUS Configuration:** The syntax for RADIUS may vary slightly. Verify that all necessary parameters are available. `/radius print detail` may help you verify all the options are available.
*   **PPP Profile Settings**:  Some options within the `/ppp profile` may not be present, such as the `use-encryption` parameter. Verify the options are present.
*  **API Calls:** API usage is slightly different, especially in 6.48 which didn't fully support the REST interface that modern versions offer.

**Example of Specific version check for v6.48**
```
/system routerboard print
```
**Example output:**
```
routerboard: yes
  model: RouterBOARD 951Ui-2nD
  serial-number: xxxxxxxxxxx
  firmware-type: ar7240
  current-firmware: 6.48.6
  upgrade-firmware: 6.48.6
```
If the current-firmware is 6.48, it means we have version 6.48, so we will need to be aware of API differences and other configuration caveats, such as not having modern features. If the version is 7, then we know we can use the newer APIs and features.
That's the detailed documentation for your requested scenario. If you have any more specific use cases or aspects you'd like me to elaborate on, just let me know!
