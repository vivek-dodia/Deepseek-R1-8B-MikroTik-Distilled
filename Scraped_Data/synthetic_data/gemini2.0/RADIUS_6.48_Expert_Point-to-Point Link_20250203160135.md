Okay, let's dive into creating a detailed technical document for implementing RADIUS authentication on a MikroTik router, specifically within the context of a point-to-point link using bridge-34, with the target subnet 2.169.37.0/24. This configuration is designed for an Expert level user on RouterOS 6.48 and 7.x.

## Scenario Description:

This scenario involves configuring a MikroTik router acting as a bridge between two network segments connected over a point-to-point link, where access to the network behind the bridge is controlled using a RADIUS server. Clients connected to bridge-34 interface will have their authentication requests forwarded to the RADIUS server before gaining access to the network. This is useful for centralized authentication and accounting in more controlled environments.

## Implementation Steps:

Here's a step-by-step guide, explaining each action and providing CLI examples, along with how to accomplish tasks with Winbox, where relevant.

1. **Step 1: Verify Existing Interface Configuration**
   - **Purpose:** Ensure the `bridge-34` interface exists and is configured appropriately before adding RADIUS configuration.
   - **Action:** List all bridges and interfaces to check for the existence and configuration of `bridge-34`.
   - **CLI Command (Before):**
     ```mikrotik
     /interface bridge print
     /interface ethernet print
     ```
   - **Example Output (Before):**
    ```
    /interface bridge print
    Flags: X - disabled, R - running
     #    NAME                                   MTU  MAC-ADDRESS         ADMIN-MAC        LAST-CHANGE
     0    bridge-local                           1500 D4:CA:6D:XX:XX:XX   D4:CA:6D:XX:XX:XX 13m55s
     1    bridge-guest                           1500 D4:CA:6D:XX:XX:XX   D4:CA:6D:XX:XX:XX 7m30s

    /interface ethernet print
    Flags: X - disabled, R - running
     #    NAME                                   MTU   MAC-ADDRESS         RX-ALL-FRAMES
     0    ether1                                 1500  D4:CA:6D:XX:XX:XX   no
     1    ether2                                 1500  D4:CA:6D:XX:XX:XX   no
    ```
   - **CLI Command (After - if needed, add the bridge and interface)**

     ```mikrotik
     /interface bridge add name=bridge-34
     /interface bridge port add bridge=bridge-34 interface=ether2
     /ip address add address=2.169.37.1/24 interface=bridge-34
     ```
   - **Winbox GUI:** Navigate to `Bridge` and `Interfaces` to verify the interface. If not present, add a new bridge (e.g `bridge-34`) and then add `ether2` as a port member. Then navigate to IP -> Addresses and add the ip address.
   - **Effect:** Ensures `bridge-34` exists, has an IP, and is ready for RADIUS implementation.

2. **Step 2: Configure RADIUS Server**
   - **Purpose:** Define the RADIUS server details. This configuration specifies the server IP, secret, and connection parameters.
   - **Action:** Add a new RADIUS server configuration.
   - **CLI Command (Before):**
     ```mikrotik
     /radius print
     ```
   - **Example Output (Before):**
     ```
      Flags: X - disabled
      #   ADDRESS       SECRET            SERVICE  TIMEOUT ACCT-TIMEOUT
     ```
   - **CLI Command (After):**
     ```mikrotik
     /radius add address=192.168.100.10 secret=MySecretKey service=ppp,login timeout=3 accounting-timeout=3
     ```

   - **Winbox GUI:** Navigate to `Radius`, click `+`, and fill in the appropriate fields for `Address`, `Secret`, `Service`, `Timeout`, and `Accounting Timeout`.
   - **Effect:** Establishes the connection parameters to communicate with the RADIUS server.
      - `address=192.168.100.10`: IP address of your RADIUS server
      - `secret=MySecretKey`: Shared secret between MikroTik and the RADIUS server.
      - `service=ppp,login`: Indicates the services that will use this RADIUS server. In this case PPP (for PPPoE, PPPTP, etc.) and Login (for hotspot login and other internal authentication).
      - `timeout=3`:  Timeout for RADIUS requests in seconds.
      - `accounting-timeout=3`: Timeout for RADIUS accounting requests in seconds.

3.  **Step 3: Enable RADIUS for Bridge Interface Authentication**
    - **Purpose:** Enable RADIUS authentication on the `bridge-34` interface, indicating that authentication for access through this bridge will rely on RADIUS.
    - **Action:** Modify bridge port settings to use RADIUS for authentication.
    - **CLI Command (Before):**
      ```mikrotik
      /interface bridge port print
      ```
    - **Example Output (Before):**
    ```
    Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
    #   BRIDGE                                    INTERFACE
    0   bridge-local                              ether1
    1   bridge-guest                              ether3
    2   bridge-34                                 ether2
   ```

    - **CLI Command (After):**
      ```mikrotik
       /interface bridge port set [find bridge=bridge-34 interface=ether2] authentication=radius
      ```
    - **Winbox GUI:** Navigate to `Bridge` -> `Ports`, select the `ether2` port linked to the `bridge-34` bridge, and enable `Authentication` and set it to `Radius`.
    - **Effect:** Enables RADIUS authentication for all clients attempting to access the network over bridge-34. This triggers the MikroTik to send an authentication request to the configured RADIUS server upon connecting on `bridge-34`.

4. **Step 4: Configure Bridge Firewall (Optional but Highly Recommended)**
   - **Purpose:** Adding firewall rules to drop all traffic initially and only allow traffic after successful RADIUS authentication. This ensures proper control over access.
   - **Action:** Add a firewall rule to drop traffic on bridge-34, then add exceptions for already authenticated traffic.
   - **CLI Command (Before):**
      ```mikrotik
        /interface bridge firewall filter print
      ```
     - **Example Output (Before):**
     ```
        Flags: X - disabled, I - invalid, D - dynamic
      ```
   - **CLI Command (After):**
    ```mikrotik
    /interface bridge firewall filter add chain=forward in-interface=bridge-34 action=drop comment="Drop all traffic on bridge-34"
    /interface bridge firewall filter add chain=forward in-interface=bridge-34 action=accept mac-protocol=ip src-mac-address-list=radius-users comment="Allow radius authenticated traffic"
    /ip firewall address-list add list=radius-users address=00:00:00:00:00:00/FF:FF:FF:FF:FF:FF
    ```
   - **Winbox GUI:** Navigate to `Bridge` -> `Firewall`, add the drop rule and then an accept rule. Then create address-list `radius-users`.
   - **Effect:** All traffic from bridge-34 will be blocked until the client MAC address is authenticated by the RADIUS server. The RADIUS server should push the client's MAC address to the `radius-users` list on successful authentication to allow traffic.

5. **Step 5: Testing and Debugging**

     - **Purpose:** Verify the connection and authentication
     - **Action:** Try to connect from a machine through `ether2` and check the logs.
     - **CLI Command:**

        ```mikrotik
        /log print
        /radius monitor [find address=192.168.100.10]
        ```

      - **Winbox GUI:** Navigate to `Logs` and `Radius`.
      - **Effect:** Check if the RADIUS server receives authentication requests and accepts or rejects them. The logs should show all steps. Monitor the Radius section for live information and troubleshooting.

## Complete Configuration Commands:

```mikrotik
# Step 1: Verify or Add Bridge Interface
/interface bridge print
/interface ethernet print
# If needed, create bridge and port
#/interface bridge add name=bridge-34
#/interface bridge port add bridge=bridge-34 interface=ether2
#/ip address add address=2.169.37.1/24 interface=bridge-34

# Step 2: Configure RADIUS Server
/radius add address=192.168.100.10 secret=MySecretKey service=ppp,login timeout=3 accounting-timeout=3

# Step 3: Enable RADIUS on Bridge Port
/interface bridge port set [find bridge=bridge-34 interface=ether2] authentication=radius

# Step 4: Configure Bridge Firewall (Optional but Highly Recommended)
/interface bridge firewall filter add chain=forward in-interface=bridge-34 action=drop comment="Drop all traffic on bridge-34"
/interface bridge firewall filter add chain=forward in-interface=bridge-34 action=accept mac-protocol=ip src-mac-address-list=radius-users comment="Allow radius authenticated traffic"
/ip firewall address-list add list=radius-users address=00:00:00:00:00:00/FF:FF:FF:FF:FF:FF

# Step 5: Monitoring and Debugging
/log print
/radius monitor [find address=192.168.100.10]

```
## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Secret:** If the shared secret between the MikroTik and RADIUS server does not match, authentication will fail.
    *   **Solution:** Double-check the secret on both the MikroTik and RADIUS server, ensuring they match exactly.
*   **Firewall Rules Blocking RADIUS Traffic:** Ensure the MikroTik's firewall isn't blocking access to the RADIUS server.
    *   **Solution:** Add an exception rule on the MikroTik's firewall to allow traffic to and from the RADIUS server or just disable the firewall temporarily for debugging.
*   **RADIUS Server Unavailable or Misconfigured:** Verify the RADIUS server is running and accessible, and properly configured for the clients (NAS) you are using.
    *   **Solution:** Check the RADIUS server logs for connection issues. Check if the MikroTik is configured as a valid NAS on the server. Check that the right authentication method (PAP/CHAP/MS-CHAP/EAP) is configured in the RADIUS server.
*   **Timeout Issues:**  If `timeout` and `accounting-timeout` are too short, connection may drop, or authentication may fail.
    *   **Solution:** Adjust the `timeout` and `accounting-timeout` parameters to give the RADIUS server sufficient time to respond.
*   **Resource Usage:** Continuous authentication requests or an overloaded RADIUS server can cause high CPU usage on the MikroTik, or errors on the RADIUS server.
     *   **Solution:** Monitor MikroTik's CPU and memory usage. Ensure the RADIUS server has enough resources and is not overloaded. Consider rate limiting if needed.
*   **Bridge loop:** If a network is improperly configured, a bridge loop can occur causing the network to crash.
    *   **Solution:** Be very aware of bridge loops. RSTP can help mitigate these issues, but proper planning is still necessary.

## Verification and Testing Steps:

*   **Ping:** Use the `ping` command from a client connected through `bridge-34`. If the traffic is not allowed by the firewall or the client is not authenticated, the ping will not succeed.
    ```mikrotik
    ping 2.169.37.x
    ```
*   **Torch:** Use the `torch` tool on the MikroTik to see the traffic going through the interface, specifically watching for RADIUS requests (port 1812/1813).
    ```mikrotik
    /tool torch interface=ether2 duration=60
    ```
*   **Log:** Check the MikroTik logs for authentication requests and responses from the RADIUS server.
   ```mikrotik
    /log print
    ```
* **Radius Monitor:** Monitor the RADIUS connection in real time.

    ```mikrotik
    /radius monitor [find address=192.168.100.10]
    ```
*   **Radius Server Logs**: Check RADIUS server logs for debugging.

## Related Features and Considerations:

*   **Hotspot:** The configured RADIUS authentication could also be used with MikroTik’s Hotspot feature to allow centralized user management and accounting.
*   **PPPoE:** The same RADIUS configuration can be used for PPPoE (Point-to-Point Protocol over Ethernet) authentication.
*   **Accounting:** By using `service=ppp,login` RADIUS accounting will also be configured. This will allow the RADIUS server to track user's session start, usage and stop.
*   **User Groups:** MikroTik supports RADIUS attributes that can be used to assign policies/profiles dynamically to a client.
*   **VLAN Tagging:** The bridge interface can also be used with VLAN tagging and trunking to pass multiple VLANs on the same physical interface.
*   **Layer2 Security:** Bridge firewall could be extended with DHCP Snooping or IP Source Guard.

## MikroTik REST API Examples (if applicable):

This example demonstrates how to create and read the configured RADIUS server using the REST API:

```
# Example 1: Create RADIUS Server
# URL: https://<mikrotik_ip>/rest/radius
# Method: POST
# Header: Content-Type: application/json
# Payload:
{
  "address": "192.168.100.10",
  "secret": "MySecretKey",
  "service": "ppp,login",
  "timeout": 3,
  "accounting-timeout": 3
}
# Expected Response:
# Status 201 Created
# Response Body
{
 "id": "*12"
}
```
```
# Example 2: Read RADIUS Server
# URL: https://<mikrotik_ip>/rest/radius/*12
# Method: GET
# Expected Response:
# Status 200 OK
{
   "id": "*12",
   "address": "192.168.100.10",
    "secret": "MySecretKey",
   "service": "ppp,login",
   "timeout": 3,
   "accounting-timeout": 3
  }
```
**API Parameter Descriptions:**

*   `address`: The IP address of the RADIUS server.
*   `secret`: The shared secret key used for RADIUS authentication.
*   `service`: Comma separated list of services that will use this RADIUS server.
*   `timeout`: Connection timeout in seconds.
*   `accounting-timeout`: Accounting timeout in seconds.
*   `id`: Internal identifier for this entry.
**API Error Handling:**
If an API call is invalid (wrong or missing parameters, wrong URL, etc) the API will return an HTTP status code different from `200 OK` or `201 Created`. Common status codes are:
* 400 Bad request - invalid parameters
* 401 Unauthorized - missing or invalid credentials.
* 404 Not Found - object with such `id` not found.
* 500 Internal Server Error - internal error on the MikroTik router.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a long, complex, randomly generated shared secret.
*   **Firewall Rules:** Allow only necessary traffic to the RADIUS server.
*   **Use encrypted RADIUS protocols**: Use secure, encrypted protocols (EAP-TLS, PEAP, MSCHAPv2) for authentication. PAP and CHAP are known to be insecure and should be avoided.
*   **Secure Access to RADIUS Server:** Ensure the RADIUS server itself is properly hardened and protected.
*   **Monitor Logs:** Regularly review MikroTik and RADIUS server logs for anomalies.
*   **Implement Rate Limiting:**  Implement rate limiting to prevent denial-of-service attacks on the RADIUS server.
*   **Regularly update:** Update both the MikroTik router and the RADIUS server to the latest stable versions.

## Self Critique and Improvements:

This configuration provides a good start, but can be improved by:
*   Implementing more advanced RADIUS attributes for dynamic VLAN assignments.
*   Adding accounting functionality.
*   Implementing load balancing and failover for RADIUS servers.
*   Adding additional firewall security such as DHCP snooping or IP source guard.
*   Using more secure and stronger authentication methods with RADIUS.

## Detailed Explanations of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users who access a network or service. RADIUS is commonly used in various network environments for security and control.

*   **Authentication:** Verifies the user's identity. This is typically done through username and password, but can use other methods like certificates.
*   **Authorization:** Determines what resources the user is allowed to access once authenticated.
*   **Accounting:** Tracks network resource usage by users, allowing accounting and auditing of network use.

## Detailed Explanation of Trade-offs:

*   **Bridge vs. Routing:** Using a bridge is simpler for extending an existing network segment, but a routed solution is more flexible for larger networks as it can reduce broadcast domains and allow for more advanced traffic control.
*   **RADIUS vs. Local Authentication:** RADIUS offers centralized management and logging, making it easier to manage multiple users. Local authentication is simpler for small networks but more difficult to scale or manage multiple devices.
*   **Firewall Rules:**  Strict firewall rules are more secure but can also be difficult to troubleshoot. Overly permissive firewall rules can create security holes.
*   **Authentication Protocols:** PAP (Password Authentication Protocol) is the simplest but least secure method, transmitting passwords in plaintext. CHAP (Challenge Handshake Authentication Protocol) is more secure but still vulnerable. EAP (Extensible Authentication Protocol) offers the best security with a variety of strong authentication mechanisms.
*   **Static IP on Radius Users list vs Dynamic**: Adding an entire subnet to the allowed list is less secure than adding one user at the time. This also forces the administrator to clean up old or revoked MAC addresses.

## Configuration for Specific RouterOS Versions:

The commands used in this configuration are applicable for RouterOS versions 6.48 and 7.x with minor differences, ensuring broad compatibility. No major changes are needed between the two versions.

This should give you a very solid and complete configuration for your RADIUS setup on MikroTik! Let me know if you have any further questions.
