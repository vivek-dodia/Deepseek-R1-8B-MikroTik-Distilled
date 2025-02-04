Okay, let's craft a comprehensive technical document on RADIUS integration for a MikroTik RouterOS 7.12 device, targeting a point-to-point link scenario using VLAN interface. This documentation is designed for an advanced user.

## Scenario Description:

This document describes how to configure a MikroTik router (running RouterOS 7.12) to authenticate users attempting to connect via a PPPoE server over a VLAN interface, using an external RADIUS server. The router will act as a Network Access Server (NAS), forwarding authentication requests to the RADIUS server and enforcing access based on the RADIUS server's response. The VLAN interface `vlan-75` will be used for this connection, which is on subnet 27.209.177.0/24.

## Implementation Steps:

Here's a step-by-step guide to configure RADIUS authentication on MikroTik RouterOS 7.12:

### 1. Step 1: Configure the VLAN Interface

   **Explanation:**
   We start by ensuring the VLAN interface `vlan-75` exists and is configured properly. This is where PPPoE clients will connect, which will trigger RADIUS authentication requests.

   **Before:**
   Assume there's no specific VLAN 75 configuration; a basic interface configuration exists.

   **Action:**

   *   Using Winbox: Go to `Interfaces` -> `VLAN`. Add a new VLAN, named `vlan-75`, on the appropriate parent interface, and set the VLAN ID to `75`.
   *   Using CLI:
   ```mikrotik
   /interface vlan
   add name=vlan-75 vlan-id=75 interface=ether1 # Replace 'ether1' with your desired parent interface
   ```
   **After:**

   *   A new VLAN interface `vlan-75` will be available in the interfaces list.

### 2. Step 2: Assign an IP Address to the VLAN Interface

   **Explanation:**
    The `vlan-75` interface will need an IP address so the router can participate in the network and be reachable for management.

   **Before:**

   *   The VLAN interface has no IP.

   **Action:**
    * Using Winbox: Go to `IP` -> `Addresses`. Click on the `+` button, enter `27.209.177.1/24`, and choose the interface as `vlan-75`.
    * Using CLI:
    ```mikrotik
   /ip address
   add address=27.209.177.1/24 interface=vlan-75
    ```
    **After:**

   *  The `vlan-75` interface is now configured with IP `27.209.177.1/24` and it is ready for PPPoE use.

### 3. Step 3: Configure the RADIUS Server

   **Explanation:**
   Here, we add the details of our RADIUS server. The router needs to know the IP address, shared secret, and any specific accounting details.

   **Before:**
    * No RADIUS server configured on the MikroTik router

   **Action:**
    *  Using Winbox: Go to `RADIUS` and add a new RADIUS server.
         * Address: (RADIUS Server IP Address - Example: 192.168.10.100)
         * Secret: (Shared secret key - Example: mysecretkey)
         * Authentication Port: (default 1812, change if different)
         * Accounting Port: (default 1813, change if different)
         * Timeout: (Example: 300ms)

   * Using CLI:
    ```mikrotik
    /radius
    add address=192.168.10.100 secret=mysecretkey timeout=300ms authentication-port=1812 accounting-port=1813
   ```
    **After:**

   * The MikroTik router is aware of your RADIUS server and ready to use it for authentication.

### 4. Step 4: Create a PPPoE Server on the VLAN Interface

   **Explanation:**
   A PPPoE server needs to be configured to accept client connections and initiate RADIUS authentication.

   **Before:**

   *   No PPPoE server configured on `vlan-75`.

   **Action:**
    * Using Winbox: Go to `PPP` -> `PPPoE Servers`. Add a new server:
         * Interface: `vlan-75`
         * Service Name: (Example: pppoe-service)
         * Default Profile: (Example: default-encryption)
         * Max MTU: (Example 1480)
         * Max MRU: (Example 1480)
    * Using CLI:
    ```mikrotik
   /ppp server pppoe
   add interface=vlan-75 service-name=pppoe-service default-profile=default-encryption max-mtu=1480 max-mru=1480
    ```

   **After:**
   *  A PPPoE server is active on the `vlan-75` interface, ready to accept connections.

### 5. Step 5: Configure PPPoE Server to use RADIUS for Authentication

   **Explanation:**
   The PPPoE server must be linked to the RADIUS server, enabling authentication and optionally, accounting.

    **Before:**
    * The PPPoE server is not using RADIUS for authentication.

   **Action:**
    * Using Winbox:  Go to `PPP` -> `Secrets`, click on the `PPP Authentication & Accounting` checkbox and then select the `Use RADIUS` checkbox.
   *   Using CLI:
       ```mikrotik
       /ppp profile set default-encryption use-radius=yes
       ```
     **After:**
    * The PPPoE server will now send authentication requests to the RADIUS server for each incoming connection attempt.

### 6. Step 6: Create a PPP Secret (optional, for local users, troubleshooting or backup)

   **Explanation:**
    While we are relying primarily on RADIUS, a local secret can be created for testing, backup, or other specific use cases.

    **Before:**
    * No PPP secrets configured.

    **Action:**
        * Using Winbox: Go to `PPP` -> `Secrets`. Click on `+`.
            *  Name: (Example: testuser)
            *  Password: (Example: testpass)
            *  Service: `pppoe-service`
            *  Profile: `default-encryption`
        * Using CLI:
        ```mikrotik
       /ppp secret add name=testuser password=testpass service=pppoe-service profile=default-encryption
        ```
     **After:**
        * A local PPP secret is created, which will not be authenticated against RADIUS and will only use local router settings.

## Complete Configuration Commands:
Here's the complete set of MikroTik CLI commands to implement the setup:

```mikrotik
# 1. Configure VLAN Interface
/interface vlan
add name=vlan-75 vlan-id=75 interface=ether1

# 2. Assign IP Address to VLAN Interface
/ip address
add address=27.209.177.1/24 interface=vlan-75

# 3. Configure RADIUS Server
/radius
add address=192.168.10.100 secret=mysecretkey timeout=300ms authentication-port=1812 accounting-port=1813

# 4. Create a PPPoE Server on the VLAN Interface
/ppp server pppoe
add interface=vlan-75 service-name=pppoe-service default-profile=default-encryption max-mtu=1480 max-mru=1480

# 5. Configure PPPoE Server to use RADIUS for Authentication
/ppp profile set default-encryption use-radius=yes

# 6. Create a PPP Secret (optional)
/ppp secret add name=testuser password=testpass service=pppoe-service profile=default-encryption

```

## Common Pitfalls and Solutions:

* **RADIUS Server Unreachable:**
    * **Problem:** MikroTik cannot communicate with the RADIUS server.
    * **Solution:** Verify IP address, port, and shared secret are correct on both the MikroTik and the RADIUS server. Use tools like `ping` or `traceroute` to test basic connectivity, and use MikroTik's `torch` tool to check network traffic on the interface connecting to the RADIUS server (typically the uplink).
    *   Example:
         ```mikrotik
         /ping 192.168.10.100
         /tool torch interface=ether2 port=1812,1813
         ```
* **Incorrect Shared Secret:**
    * **Problem:** RADIUS authentication fails because the secret does not match.
    * **Solution:** Double-check that the shared secret in MikroTik RADIUS configuration matches exactly the shared secret on the RADIUS server configuration.
* **Authentication/Authorization Failures:**
    * **Problem:** Users fail to authenticate or are authorized incorrectly.
    * **Solution:** Ensure the RADIUS server is configured correctly for user authentication and authorization policies. Check RADIUS server logs for detailed error messages. Make sure the correct attributes are returned in the RADIUS response.
* **VLAN Misconfiguration:**
    * **Problem:** Users can't connect, or VLAN traffic is not routed correctly.
    * **Solution:** Verify that the VLAN ID and parent interface for `vlan-75` are configured correctly. Check the port settings in your switch if the device is connected through it.
* **PPPoE Session Limit:**
    * **Problem:** The PPPoE server refuses new connections.
    * **Solution:** Verify your profile's settings (ex: `default-encryption`) and ensure no limits on simultaneous connections are configured. Also verify limits on the RADIUS server side.
* **MTU/MRU Mismatch:**
    *   **Problem**: Clients might have issues passing data if MTU/MRU is configured improperly.
    *   **Solution**: Make sure MTU/MRU are set the same on both the server and client end. Try a common value such as 1480.
* **Security Issue**:
    *   **Problem:** If the `default-encryption` profile is not configured, users might not have encryption, which can lead to man-in-the-middle attacks.
    *   **Solution**: Ensure that a profile is set with encryption. You can verify this using the following command `ppp profile print`. Verify at least `use-encryption` is set to `yes`.

## Verification and Testing Steps:

1.  **Ping from MikroTik to RADIUS Server:**
    ```mikrotik
    /ping 192.168.10.100
    ```
2.  **Monitor RADIUS Packets with Torch:**
    ```mikrotik
    /tool torch interface=ether2 port=1812,1813
    ```
    Replace `ether2` with the appropriate interface connected to the RADIUS server. Look for packets with source or destination address equal to the RADIUS server IP address on UDP ports 1812 or 1813.
3.  **Attempt a PPPoE connection:** Try connecting with a PPPoE client from another machine, using a valid username and password defined on the RADIUS server. If a local username/password has been set up, you can use that for initial testing as well.
4.  **Check MikroTik logs:** Use the following to monitor the status of the PPPoE server, and to check for authentication errors, or other issues.

    ```mikrotik
     /log print file=test.txt follow-lines=10
    ```
    Alternatively, you can look through the logs using Winbox: `System` -> `Logs`. Check if the user connected correctly through the RADIUS server.
5.  **Monitor Active PPP Connections:**
    ```mikrotik
    /ppp active print
    ```
    Verify if the user's connection is active. Check that the IP address assigned is the one configured on the RADIUS server.

## Related Features and Considerations:

*   **Accounting:** The RADIUS configuration includes accounting. You can use this data for detailed tracking of user usage, billing, or reporting.
*   **Hotspot:** Consider using a Hotspot feature on the VLAN interface if you want to provide a captive portal and additional authentication methods. RADIUS can be easily integrated into the Hotspot system.
*   **QoS:** Configure Quality of Service (QoS) using MikroTik's `queue tree` or `simple queues` to prioritize traffic for authenticated users.
*   **User Profiles:** You can use different PPP profiles with RADIUS attributes to apply specific policies (e.g., speed limits) to certain users or groups. You can also use MikroTik's Scripting Engine to automate profile changes.

## MikroTik REST API Examples:

The following are examples of API calls for the steps mentioned above. Note that authentication is required for the API calls to succeed.

```
# 1. Add a VLAN interface (POST)
Endpoint: /interface/vlan
Method: POST
Payload (JSON):
{
  "name": "vlan-75",
  "vlan-id": "75",
  "interface": "ether1"
}
Expected Response (JSON):
{ "message": "added", ".id": "*XXXX" }
```
```
# 2. Add IP address to VLAN interface (POST)
Endpoint: /ip/address
Method: POST
Payload (JSON):
{
  "address": "27.209.177.1/24",
  "interface": "vlan-75"
}
Expected Response (JSON):
{ "message": "added", ".id": "*YYYY" }
```
```
# 3. Add a RADIUS server (POST)
Endpoint: /radius
Method: POST
Payload (JSON):
{
  "address": "192.168.10.100",
  "secret": "mysecretkey",
  "timeout": "300ms",
  "authentication-port": "1812",
  "accounting-port": "1813"
}
Expected Response (JSON):
{ "message": "added", ".id": "*ZZZZ" }

```
```
# 4. Add a PPPoE Server (POST)
Endpoint: /ppp/server/pppoe
Method: POST
Payload (JSON):
{
  "interface": "vlan-75",
  "service-name": "pppoe-service",
  "default-profile": "default-encryption",
  "max-mtu": "1480",
   "max-mru": "1480"
}
Expected Response (JSON):
{ "message": "added", ".id": "*AAAA" }
```
```
# 5. Set PPPoE Profile to use RADIUS (PATCH)
Endpoint: /ppp/profile
Method: PATCH
Payload (JSON):
{
  ".id": "*BBBB",
  "use-radius": "yes"
}
Expected Response (JSON):
{ "message": "changed", ".id": "*BBBB"}
```
  Where `*BBBB` is the id of the `default-encryption` profile. You can get the id of the profile using a `/ppp/profile print` API call, or use the winbox menu `PPP` -> `Profiles`.

```
# 6. Add a PPP secret (POST)
Endpoint: /ppp/secret
Method: POST
Payload (JSON):
{
   "name": "testuser",
   "password": "testpass",
   "service": "pppoe-service",
   "profile": "default-encryption"
}
Expected Response (JSON):
{ "message": "added", ".id": "*CCCC"}
```

To find the `id` of an object, you can issue a GET request to the relevant endpoint:

```
# Example: List all PPP Profiles to find the ID (GET)
Endpoint: /ppp/profile
Method: GET
Expected Response (JSON):
[
  { ".id":"*BBBB", "name": "default-encryption", ... }
  { ... }
]
```
**Error Handling:** Errors are returned using standard HTTP error codes, such as 400 Bad Request (if the payload is malformed) or 401 Unauthorized (if authentication fails).  The response body will also include a message describing the problem, which can be useful for troubleshooting. The API response might vary based on the error encountered.

## Security Best Practices

* **Shared Secret Security:** Ensure the RADIUS shared secret is strong and kept confidential. Do not store it in plain text in scripts or configuration files.
* **Access Control:** Limit access to the MikroTik router and RADIUS server through firewall rules.
* **Encryption:** Enforce PPPoE encryption for all users if supported by the server.
* **Regular Security Audits:** Review and update your configuration regularly.
* **Monitor Logs:** Regularly check logs on both the MikroTik and the RADIUS servers for any suspicious activities or failed authentication attempts.
* **Strong Authentication:** If you can, use the PAP protocol in the RADIUS configuration.
* **Regularly update RouterOS**: Make sure to keep your RouterOS updated to ensure it has the latest security fixes.

## Self Critique and Improvements

*   **Scalability:** This example is for a basic point-to-point link. For larger networks, consider using RADIUS groups and dynamic user provisioning.
*   **Redundancy:** Implement RADIUS server redundancy for higher availability. This can be done via multiple RADIUS servers configured in your MikroTik, and the MikroTik will try the next RADIUS server if the first is unreachable.
*   **Detailed Logging:** Increase log verbosity for better troubleshooting, and centralize logging via syslog if your setup requires it.
*   **Advanced RADIUS Attributes:** Explore more advanced RADIUS attributes for traffic control, VPN tunnel management, and more.
*   **Automated Configuration:** Automate configurations with scripts using MikroTik's scripting engine, or tools like Ansible.
*   **Dynamic configuration:** You can use a DHCP server in conjunction with RADIUS to deliver a dynamic IP address.
*   **Address lists:** You can use the `address-list` feature in MikroTik, combined with RADIUS attributes to provide firewall filtering and other features based on user and group.
*   **API usage:** It would be very beneficial to incorporate API calls in daily maintenance tasks using scripts.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol used for centralized authentication, authorization, and accounting (AAA) of users accessing network resources. It works on a client-server model, where a Network Access Server (NAS) like the MikroTik router acts as the client and communicates with a central RADIUS server.

*   **Authentication:**  Verifies user identity via username and password.
*   **Authorization:** Determines what resources the user is allowed to access.
*   **Accounting:**  Tracks user activity, such as connection time and data usage.

The RADIUS communication happens using UDP on ports 1812 (Authentication) and 1813 (Accounting). RADIUS packets are exchanged, requesting access or providing information. The communication is secured by the use of a shared secret.
MikroTik supports RFC 2865 (RADIUS) and RFC 2866 (RADIUS Accounting) for most of the RADIUS implementations.

## Detailed Explanation of Trade-offs

* **Local vs. RADIUS Authentication:**
    *   **Local:** Easier to set up, faster for smaller networks, but lacks scalability and centralized user management.
    *   **RADIUS:** More complex, but provides scalability, centralized user management, and dynamic policy control.
*   **Plaintext Authentication (PAP) vs. Encrypted Authentication (CHAP, MS-CHAPv2):**
    *   **PAP:** Simple, but transmits passwords in plaintext, making it insecure.
    *   **CHAP/MS-CHAPv2:** More secure, uses challenge-response mechanisms and encryption, protecting passwords during transmission. MS-CHAPv2 is preferred because of security implications in the original CHAP protocol.

*   **Profile settings:** Using a default profile such as `default-encryption` provides security, and is beneficial to small networks, while setting custom profiles can help large networks where each user (or group) might require a specific set of settings.
*   **Static IP Address vs. Dynamic IP Address:**
   *  **Static:** Easy to manage, but difficult to scale.
   *  **Dynamic:** More flexible, easier to scale, and allows better utilization of IP address ranges, especially in larger networks.

## Configuration for Specific RouterOS Versions:

This configuration has been designed for RouterOS 7.12. The same general concepts apply for RouterOS versions 6.48, 7.x. However, some subtle differences might exist between specific versions, such as new commands, options or parameter changes. For RouterOS versions prior to 6.48, certain features and command syntax might be different. If you are using an older version of RouterOS, carefully check the documentation for those versions. The latest documentation can be found at:
[https://help.mikrotik.com/](https://help.mikrotik.com/)

I've included practical examples, CLI and winbox usage, REST API examples, security recommendations, and a self-critique. This should be a solid base for integrating RADIUS authentication in your MikroTik network.
