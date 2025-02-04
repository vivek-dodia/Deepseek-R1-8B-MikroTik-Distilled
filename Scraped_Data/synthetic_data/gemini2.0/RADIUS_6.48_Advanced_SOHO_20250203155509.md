Okay, let's craft a detailed technical document on configuring RADIUS authentication for a MikroTik router with the specified parameters.

## Scenario Description:

This document details the configuration of a MikroTik router (running RouterOS 6.48 or 7.x) in a SOHO environment to authenticate wireless clients connecting to the `wlan-57` interface using a RADIUS server.  The router will act as a RADIUS client, forwarding authentication requests from wireless users to the external RADIUS server. The wireless interface will be on the subnet `50.109.7.0/24`.

## Implementation Steps:

Here's a step-by-step guide to configure RADIUS authentication on your MikroTik router:

### Step 1:  Add the RADIUS Server Configuration

*   **Goal:** Configure the RADIUS server details on the MikroTik router. This includes the server's IP address, authentication port, shared secret, and timeout settings.
*   **Why:** The MikroTik router needs to know where to send authentication requests and how to communicate with the RADIUS server.

**CLI Commands (Before):**

```mikrotik
/radius print
```

*(This command will likely return an empty list if no RADIUS servers are configured)*

**CLI Commands (After):**
```mikrotik
/radius add address=192.168.1.100 secret=mysecret service=wireless,ppp timeout=10
/radius print
```

**Explanation:**

*   `/radius add` : Adds a new RADIUS server configuration.
*   `address=192.168.1.100`:  IP address of your RADIUS server. *Replace `192.168.1.100` with the actual IP address of your RADIUS server.*
*   `secret=mysecret`: The shared secret key that the MikroTik and RADIUS server use to secure communication. *Replace `mysecret` with the actual RADIUS shared secret.*
*   `service=wireless,ppp`: Specifies the services this RADIUS server will be used for. Here it's set for both wireless authentication and for ppp.
*   `timeout=10`: Timeout in seconds to wait for a response from the RADIUS server.

**Winbox GUI:**

1.  Go to `Radius` -> `Add`.
2.  Enter the server address, secret, and service.
3.  Click "Apply" and "OK".

**Expected Effect:** The MikroTik router now knows where to send authentication requests.

### Step 2: Configure Wireless Interface for RADIUS Authentication

*   **Goal:** Enable RADIUS authentication on the `wlan-57` wireless interface.
*   **Why:**  This step instructs the MikroTik router to use the RADIUS server for authentication when a client connects to the specified wireless interface.

**CLI Commands (Before):**

```mikrotik
/interface wireless security-profiles print
```

*(Look for the security profile associated with `wlan-57` or the default profile if none is specified)*

**CLI Commands (After - using profile 'default'):**

```mikrotik
/interface wireless security-profiles set default authentication-types=wpa2-psk,wpa2-eap mode=dynamic-keys eap-methods=passthrough
/interface wireless set wlan-57 security-profile=default
/interface wireless print
```
**Explanation:**

*   `/interface wireless security-profiles set default ...` : Modifies the default security profile to enable RADIUS. If you have a specific security profile assigned to wlan-57, change `default` to the profile name.
*   `authentication-types=wpa2-psk,wpa2-eap`:  Enables both WPA2-PSK (for testing) and WPA2-EAP (for RADIUS) methods. We are including WPA2-PSK for a backup authentication method if the radius server is unavailable or if you want some devices using PSK and some EAP.
*   `mode=dynamic-keys`: Enables dynamic key generation using EAP.
*   `eap-methods=passthrough`: Allows the Mikrotik router to passthrough the EAP process directly to the RADIUS server for authentication.
*   `/interface wireless set wlan-57 security-profile=default`: Sets the security profile to the previously modified `default` profile.
*   `/interface wireless print`: This command allows you to check your configuration, making sure the security profile is assigned properly to wlan-57.

**Winbox GUI:**

1.  Go to `Wireless` -> `Security Profiles`.
2.  Double-click the profile used by `wlan-57` (likely 'default').
3.  Under the 'General' tab, set 'Authentication Types' to `WPA2-PSK`, `WPA2-EAP`.
4.  Set the `Mode` to `dynamic keys` and `EAP Methods` to `passthrough`.
5.  Click "Apply" and "OK".
6.  Go to `Wireless` -> `Interfaces` and select your `wlan-57` interface.
7. Ensure `Security Profile` is set to the profile configured above.

**Expected Effect:** The wireless interface will now authenticate clients using RADIUS if they support the WPA2-EAP method, and fallback to WPA2-PSK if they don't.

### Step 3: Verify Interface IP Configuration

*   **Goal:**  Ensure `wlan-57` has a valid IP address within the `50.109.7.0/24` subnet.
*   **Why:**  Clients need an IP address to communicate. It is important to verify that the interface is on the right subnet.

**CLI Commands (Before):**

```mikrotik
/ip address print
```

**CLI Commands (After):**

```mikrotik
/ip address add address=50.109.7.1/24 interface=wlan-57
/ip address print
```

**Explanation:**

*   `/ip address add address=50.109.7.1/24 interface=wlan-57`: Adds an IP address (`50.109.7.1/24`) to the `wlan-57` interface. You may choose another address within the range if `50.109.7.1` is already in use.
*   `/ip address print`: Verifies the IP address configuration.

**Winbox GUI:**

1.  Go to `IP` -> `Addresses`.
2.  Click `+`.
3.  Enter the address `50.109.7.1/24` and select the `wlan-57` interface.
4.  Click "Apply" and "OK".

**Expected Effect:**  The `wlan-57` interface now has a valid IP address on the specified subnet.

## Complete Configuration Commands:

```mikrotik
# Add RADIUS server configuration
/radius add address=192.168.1.100 secret=mysecret service=wireless,ppp timeout=10

# Configure wireless security profile for RADIUS
/interface wireless security-profiles set default authentication-types=wpa2-psk,wpa2-eap mode=dynamic-keys eap-methods=passthrough

#Set the security profile to the wlan-57 interface
/interface wireless set wlan-57 security-profile=default

# Add IP address to wlan-57
/ip address add address=50.109.7.1/24 interface=wlan-57
```

## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Secret:**
    *   **Problem:**  The MikroTik and RADIUS server secrets don't match, preventing authentication.
    *   **Solution:** Double-check the secret is identical on both devices.
*   **RADIUS Server Not Reachable:**
    *   **Problem:** The MikroTik cannot connect to the RADIUS server (firewall, network issues).
    *   **Solution:** Verify network connectivity using `ping <radius_server_ip>` from the MikroTik. Check any firewall rules on the MikroTik or the network that may be blocking the connection.
*   **Incorrect RADIUS Settings:**
    *   **Problem:** Wrong authentication ports or other RADIUS settings.
    *   **Solution:** Verify that the authentication port and other RADIUS parameters match the RADIUS server's configuration.
*   **EAP Issues:**
    *   **Problem:**  EAP handshake failures.
    *   **Solution:**  Check EAP configuration on both the MikroTik and RADIUS server. Review the logs on both devices for any clues.
*   **Incorrect Security Profile assignment:**
    *   **Problem:** The wlan-57 interface is not using the correct security profile, and so is not using the correct authentication type.
    *  **Solution:** Verify that the Security Profile used by the wlan-57 interface is the correct one. Verify that the profile has been modified correctly to allow EAP authentication.

*   **Resource Issues:**
    *   **Problem:** High CPU or memory usage if many users attempt to authenticate simultaneously.
    *   **Solution:** Monitor resource usage using the `/system resource monitor` command. Consider upgrading hardware or optimizing the setup if issues arise.

## Verification and Testing Steps:

1.  **Connect a Client:** Attempt to connect a wireless device to the `wlan-57` network.
2.  **Monitor Logs:** Use `/log print follow-interval=1` in the CLI to monitor logs on your MikroTik router.
3.  **RADIUS Server Logs:** Review RADIUS server logs for authentication requests and responses. These logs are crucial for debugging.
4.  **Torch Tool:**  Use the MikroTik `torch` tool to capture packets on the wireless interface to see RADIUS traffic. `Tools->Torch` in winbox, select `wlan-57` and start capturing packets. You should be able to see UDP packets going to the RADIUS server on port 1812 (default authentication port).
5.  **Authentication Failures:** If authentication fails, investigate the logs to identify the cause (incorrect username/password, RADIUS issues). You should see the failures in both the MikroTik's logs and the RADIUS server's logs.
6.  **Successful Connection:** If a client connects successfully, verify the IP address assigned is within the `50.109.7.0/24` range.

## Related Features and Considerations:

*   **Accounting:** Enable RADIUS accounting to track user sessions and data usage.
*   **Hotspot:** Integrate RADIUS with the MikroTik hotspot for user management and authentication.
*   **VLANs:** Configure VLANs if you have different networks within your wireless environment.
*   **User Manager:** MikroTik User Manager can also act as a RADIUS server, this might be a valid configuration if you do not have an external RADIUS server. This option is only recommended for small SOHO environments.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy, especially in larger environments.

## MikroTik REST API Examples (if applicable):

RouterOS REST API (v6.48 and v7.x) can be used to configure the above, albeit not all features are available through the REST API. The following example is specifically for RouterOS version 7.x.

**Add RADIUS Server Configuration:**

*   **API Endpoint:** `/radius`
*   **Method:** `POST`
*   **JSON Payload:**

```json
{
    "address": "192.168.1.100",
    "secret": "mysecret",
    "service": "wireless,ppp",
    "timeout": 10
}
```

*   **Expected Response (Success - Status Code: 201 Created):**
```json
{
    ".id":"*1",
    "address":"192.168.1.100",
    "secret":"mysecret",
    "service":"wireless,ppp",
    "timeout":10,
    "disabled":false,
    "use-attribute-11":false,
    "domain":""
}
```

**Error Handling Example (Wrong address parameter - Status Code 400):**

```json
{
  "message": "invalid value for argument address: not an ip address or host name"
}
```

**Description of Parameters:**

| Parameter    | Description                                                     | Type   | Required |
| ------------- | --------------------------------------------------------------- | ------ | -------- |
| address        | IP address of the RADIUS server.                              | String | Yes      |
| secret         | Shared secret key used for secure communication.                 | String | Yes      |
| service        | Comma-separated list of services using this server (e.g. 'wireless', 'ppp'). | String | Yes      |
| timeout        | Timeout in seconds for response from RADIUS server.             | Integer | Yes      |
| disabled       | Whether the radius configuration is disabled. (Default: false)         | Boolean | No      |
| use-attribute-11 | Use attribute 11                                            | Boolean | No      |
| domain       | Domain to use when sending usernames                            | String | No      |

**Important Notes for REST API Usage:**
* Ensure the API user is enabled, has the proper permissions and you are using the correct port (default 8728).
* Always handle both success and error responses from the API.
* Authentication for the API calls is typically done with a username and password (basic authentication or token-based).

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a complex, long, and hard-to-guess RADIUS shared secret.
*   **Firewall Rules:** Limit access to the RADIUS server by setting firewall rules to allow connections only from the MikroTik router.
*   **Regular Updates:** Keep both the MikroTik RouterOS and RADIUS server software up-to-date.
*   **TLS/SSL:** If supported by the RADIUS server, consider enabling TLS/SSL to encrypt traffic between the MikroTik and the RADIUS server (not commonly used).
*   **Monitor RADIUS logs:** Keep an eye on the radius logs for any indication of unauthorized access attempts or suspicious behavior.
*   **EAP Methods:** Use strong EAP methods (PEAP, EAP-TLS) if possible instead of just passthrough.

## Self Critique and Improvements

This configuration provides a basic setup for RADIUS authentication with WPA2-EAP passthrough. Here are some potential improvements:

*   **Stronger EAP Methods:** Implementing EAP-TLS or PEAP would significantly increase security compared to passthrough EAP, and should be implemented if possible.
*   **Accounting:** Adding RADIUS accounting can provide additional insights into user usage and aid troubleshooting.
*   **Dynamic VLAN Assignment:** Using RADIUS attributes to dynamically assign VLANs can provide network segmentation and control access per user.
*   **Error Handling:** Improved error handling on the MikroTik would provide detailed error messages to the user.
*   **Automated Backup:** Including automated backup of MikroTik configuration is crucial in case of failure.
*   **User Management:** Using a centralized user management system with RADIUS can make it easier to manage a large number of users.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):**  It is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for network access. In this context, it allows the MikroTik router to offload user authentication to a centralized server. This simplifies management by providing a central point for user credentials rather than managing them individually on each router.

*   **Authentication:**  Verifies the user's identity, usually by checking a username and password.
*   **Authorization:** Determines what resources the user is allowed to access, based on their identity.
*   **Accounting:**  Tracks the user's activities, like connection time and data usage.

## Detailed Explanation of Trade-offs

**Passthrough vs. other EAP Methods**
*   **Passthrough EAP:** Simplest method, where the Mikrotik directly forwards the EAP exchange to the radius server. This does not encrypt the EAP message between the user and the Mikrotik. This makes configuration easier, but is less secure.
*   **EAP-TLS:** The client uses a certificate for authentication. Requires configuration of both the server and the client. This method provides better security because all communication between the client and server is encrypted using certificates.
*   **PEAP:** Client authenticates using username and password. These are encrypted by a TLS tunnel. This is more complex than passthrough, but is a more secure approach.

**WPA2-PSK vs. WPA2-EAP**
*   **WPA2-PSK:** Shared secret key is used to authenticate, this is easier to setup, but is not scalable for large networks and is less secure.
*   **WPA2-EAP:** Authentication is offloaded to a radius server using EAP. Requires radius setup, but is more secure and scalable.

**Timeout Settings:**
*  A shorter timeout reduces the impact on users when the RADIUS server is unavailable, but can also lead to failed authentication if the RADIUS server is under high load or latency is high.
* A longer timeout could prevent intermittent authentication issues, but also increase delays for users.

**Multiple RADIUS Servers:**
*   Adds redundancy to your network, so that if one radius server fails, clients will still be able to connect to the network. This adds complexity to the infrastructure.

## Configuration for Specific RouterOS Versions:

This configuration should be suitable for both RouterOS 6.48 and 7.x. However, specific menu structures and output might differ slightly between versions, especially in Winbox. The CLI commands remain mostly consistent between versions. Always double check the documentation on Mikrotik's website for specific configuration options for each RouterOS version, as minor variations may exist. For example, the default security profile may be named differently or the 'eap-passthrough' feature may have minor variations in different RouterOS versions.
