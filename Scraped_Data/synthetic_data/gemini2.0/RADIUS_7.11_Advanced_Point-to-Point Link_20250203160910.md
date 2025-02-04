Okay, let's dive into a comprehensive guide for configuring RADIUS authentication on a MikroTik router running RouterOS 7.11 (also suitable for 6.48 and 7.x) for a point-to-point link, specifically using the `wlan-50` interface on the 176.25.247.0/24 subnet. This is an advanced configuration designed for users who are familiar with basic networking and MikroTik concepts.

## Scenario Description:

We are setting up RADIUS authentication for wireless clients connecting to a MikroTik router acting as an access point using the `wlan-50` interface. The IP subnet for this interface is 176.25.247.0/24. All wireless clients will authenticate against a RADIUS server before being granted access to the network. This setup is common in small to medium businesses, public Wi-Fi hotspots, and even more complex point-to-point links when higher levels of security or accounting are needed.

## Implementation Steps:

Here's a detailed, step-by-step guide:

### 1. **Step 1: Initial Interface Configuration**

*   **Explanation:** Before configuring RADIUS, we need to ensure our wireless interface is operational and has a basic configuration, such as IP address, SSID, and security. We'll assume you have basic wireless config already.
*   **CLI Before:**
    ```
    /interface wireless print
    ```
    You'll see your wireless interface, likely disabled.

    ```
    /ip address print
    ```
    You likely won't see an IP assigned yet for wlan-50.
*   **CLI Configuration:**
    ```
    /interface wireless
    set wlan-50 disabled=no mode=ap-bridge band=2ghz-b/g/n channel-width=20mhz frequency=2437 ssid="my-wifi" security-profile=default
    /ip address add address=176.25.247.1/24 interface=wlan-50
    ```
    *   `set wlan-50 disabled=no`: Enables the wireless interface named `wlan-50`.
    *   `mode=ap-bridge`: Sets the interface to function as an access point.
    *   `band=2ghz-b/g/n`: Sets 2.4GHz band.
    *   `channel-width=20mhz`: Sets the width of the channel.
    *   `frequency=2437`: Sets the channel to frequency 2437 (Ch6).
    *   `ssid="my-wifi"`: Sets the SSID for the wireless network.
    *   `security-profile=default`:  Assuming the default (pre-shared-key) securety, this is important to initially let the client connect for a moment.
    *   `/ip address add address=176.25.247.1/24 interface=wlan-50`: Assigns an IP address to the interface
*   **Winbox GUI:** Navigate to *Interfaces* -> *Wireless* select the wlan-50 interface and configure the general wireless settings and select *Apply*. Then navigate to *IP* -> *Addresses* and add the 176.25.247.1/24 address on wlan-50.
*   **CLI After:**
    ```
    /interface wireless print
    ```
    You'll see `enabled=yes`.

    ```
    /ip address print
    ```
     You'll see 176.25.247.1/24 on wlan-50.
*   **Effect:** The wireless interface is now up and running with a basic configuration. Clients can connect using the specified SSID and Security profile.

### 2. **Step 2: Configure RADIUS Server Settings**

*   **Explanation:** We need to configure the MikroTik to communicate with the RADIUS server. This includes the server IP address, secret, and port (typically 1812 for authentication and 1813 for accounting, though we will not cover accounting).
*   **CLI Before:**
    ```
    /radius print
    ```
    You likely won't see any configured RADIUS servers.
*   **CLI Configuration:**
    ```
    /radius add address=192.168.88.100 secret="your_radius_secret" service=wireless protocol=udp timeout=200ms
    ```
    *   `address=192.168.88.100`:  Replace `192.168.88.100` with the actual IP address of your RADIUS server.
    *   `secret="your_radius_secret"`: Replace `your_radius_secret` with the shared secret configured on your RADIUS server.  **This is critical for security**.
    *   `service=wireless`:  Specifies that this RADIUS server is used for wireless authentication.
    *    `protocol=udp`: Specifies the protocol for RADIUS communication (UDP is the default)
    *   `timeout=200ms`: Specifies the timeout for RADIUS requests (200 milliseconds).
*   **Winbox GUI:** Navigate to *Radius* and click "+". Add the relevant address, secret and other parameters and click *OK*.
*   **CLI After:**
    ```
    /radius print
    ```
    You'll see the new configured RADIUS server.
*   **Effect:**  The MikroTik router is now configured to communicate with the specified RADIUS server.

### 3. **Step 3: Enable RADIUS Authentication on Wireless Interface**

*   **Explanation:** We need to modify the wireless interface configuration to use the configured RADIUS server for authentication.
*   **CLI Before:**
    ```
    /interface wireless security-profiles print
    ```
    You will see a default security profile, probably with an authentication type like WPA2-PSK.
    ```
     /interface wireless print
    ```
    You will see that the `security-profile` is set to "default"
*   **CLI Configuration:**
    ```
    /interface wireless security-profiles add name="radius-security" mode=dynamic-keys authentication-types=eap
    /interface wireless set wlan-50 security-profile=radius-security
    ```
    *   `/interface wireless security-profiles add name="radius-security" mode=dynamic-keys authentication-types=eap`: This creates a new security profile named `radius-security`. It will use EAP for the authentication.
    *   `/interface wireless set wlan-50 security-profile=radius-security`: Updates the wireless interface to use the newly created security profile.
*   **Winbox GUI:** Navigate to *Wireless* -> *Security Profiles* and create a new security profile "radius-security", ensure *Authentication Types* is EAP and click Apply. Navigate back to *Interfaces* -> *Wireless*, select the wlan-50 interface and under *Security Profile* select "radius-security" and click Apply.
*   **CLI After:**
    ```
     /interface wireless print
    ```
    You'll see  `security-profile=radius-security` on the wlan-50 interface.
    ```
     /interface wireless security-profiles print
    ```
    You'll see the new security profile with `authentication-types=eap`.
*   **Effect:** When a wireless client attempts to connect to the `my-wifi` SSID, the MikroTik router will now forward the authentication request to the RADIUS server instead of relying on a pre-shared key.

## Complete Configuration Commands:

Here are all the commands together:

```
/interface wireless
set wlan-50 disabled=no mode=ap-bridge band=2ghz-b/g/n channel-width=20mhz frequency=2437 ssid="my-wifi" security-profile=default
/ip address add address=176.25.247.1/24 interface=wlan-50
/radius add address=192.168.88.100 secret="your_radius_secret" service=wireless protocol=udp timeout=200ms
/interface wireless security-profiles add name="radius-security" mode=dynamic-keys authentication-types=eap
/interface wireless set wlan-50 security-profile=radius-security
```
**Parameters Explanation:**

| Command                     | Parameter        | Description                                                                             |
|-----------------------------|------------------|-----------------------------------------------------------------------------------------|
| `/interface wireless set`   | `disabled`       | Whether to enable/disable the interface.  Must be 'no' for the interface to work. |
| `/interface wireless set`   | `mode`           | The mode of the wireless interface (`ap-bridge`, `station`, etc.).                                                                           |
| `/interface wireless set`   | `band`           | Wireless frequency band to be used, valid options are: `2ghz-b`, `2ghz-g`, `2ghz-n`, `2ghz-b/g`, `2ghz-b/g/n`, `2ghz-g/n`, `5ghz-a`, `5ghz-n`, `5ghz-ac`, `5ghz-a/n`, `5ghz-a/n/ac`.               |
| `/interface wireless set`   | `channel-width`  | The channel width to be used. |
| `/interface wireless set`   | `frequency`      | The specific wireless channel frequency.                                                               |
| `/interface wireless set`   | `ssid`           | The Service Set Identifier for the network.                                            |
| `/interface wireless set`   | `security-profile`| The name of the Security Profile in use.                                               |
| `/ip address add`          | `address`        | IP address and subnet mask (e.g., `176.25.247.1/24`).                                     |
| `/ip address add`          | `interface`      | Interface to assign the IP address to (e.g., `wlan-50`).                                  |
| `/radius add`              | `address`        | The IP address of the RADIUS server.                                                     |
| `/radius add`              | `secret`         | The shared secret between the MikroTik and RADIUS server.                               |
| `/radius add`              | `service`        | Specifies the service where this server will be used: `ppp`, `wireless`, `hotspot`, or `dhcp`.   |
| `/radius add`              | `protocol`       | Protocol to use for RADIUS communication, which is typically `udp`. |
| `/radius add`              | `timeout`        | Maximum time to wait for a RADIUS server response.                                               |
| `/interface wireless security-profiles add` | `name` |  The name of the Security Profile
| `/interface wireless security-profiles add` | `mode` | Specifies the security mode, it can be `static-keys` or `dynamic-keys`. Here, we use `dynamic-keys` for EAP-based authentication.
| `/interface wireless security-profiles add` | `authentication-types` | Defines the authentication types such as `eap` (Extensible Authentication Protocol), `wpa-psk`, `wpa2-psk`. Here, we use `eap` for RADIUS.
| `/interface wireless set`  |  `security-profile`|The name of the Security Profile in use                                                     |
**Important Note:** *Always* use strong, random secrets for your RADIUS server.

## Common Pitfalls and Solutions:

*   **Problem:** RADIUS server unreachable.
    *   **Solution:** Check IP connectivity between MikroTik and RADIUS server. Use `ping` from the MikroTik. Ensure the RADIUS server is running and listening on the configured port. Check firewalls on both ends.
*   **Problem:**  Incorrect RADIUS secret.
    *   **Solution:** Double-check the shared secret on both the MikroTik and RADIUS server. It is case-sensitive and any small mistake will result in failure.
*   **Problem:** Incorrect `service` setting in RADIUS configuration.
    *   **Solution:** Make sure `service=wireless` is specified for wireless authentication.
*   **Problem:** EAP not configured correctly on client.
    *   **Solution:** Ensure clients are correctly configured to use the proper EAP authentication method and their credentials are valid.
*   **Problem:** Authentication timeout on the MikroTik.
    *   **Solution:** Increase the timeout value in the RADIUS server configuration on the MikroTik, or check the performance of the RADIUS server.
*   **Problem:** Log error on MikroTik regarding RADIUS.
    *   **Solution:** Check the `/log print` to determine the specific issue that the Mikrotik encountered.
*   **Security Issue:** Weak RADIUS secret.
    *   **Solution:** Use strong, random, complex secrets for RADIUS.

## Verification and Testing Steps:

1.  **Connect a wireless client:**  Attempt to connect to the `my-wifi` SSID with a client configured for EAP authentication. Ensure the client is configured to request authentication via the RADIUS server using username and password.
2.  **Check RADIUS logs on the MikroTik:** Use `/log print where topics~"radius"` to look for authentication attempts and see if the router sent the authentication request.
3.  **Check RADIUS logs on the RADIUS server:** Use the specific command related to the log files of your RADIUS server to confirm that it is seeing the authentication requests from the MikroTik and how it is responding.
4.  **Use `torch` on the MikroTik:** Run `/tool torch interface=wlan-50` and see if there's traffic between the router and the RADIUS server, this can be used to identify packets being sent or received on the port used by the RADIUS server.
5.  **Verify IP address assignment:** Once authenticated, the client should receive an IP address in the 176.25.247.0/24 subnet if the RADIUS server is correctly configured to allow access. You can check this by using `/ip dhcp-server leases print` and confirm if an address has been assigned.

## Related Features and Considerations:

*   **Accounting:** You could add accounting to the RADIUS setup so that you can log the usage per client via `/radius add service=wireless accounting=yes ...`.
*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy and failover. They will be attempted in order.
*   **Dynamic VLAN Assignment:**  RADIUS can assign clients to different VLANs dynamically based on user authentication. This requires VLAN config and support on your RADIUS server, but it is outside of the scope of this specific topic.
*   **Hotspot/User Manager:** For more complex user management, consider using the MikroTik Hotspot feature or the User Manager package. These can use RADIUS as a backend authentication mechanism. These are both beyond the scope of the current configuration, but they are important in real-world scenarios.
*   **Security Profiles:**  RADIUS can be combined with other security measures like IP filtering, firewall rules, and more.

## MikroTik REST API Examples (if applicable):

Here's a REST API example to add the RADIUS configuration:

**Endpoint:** `/radius`

**Method:** POST

**Request JSON Payload:**
```json
{
  "address": "192.168.88.100",
  "secret": "your_radius_secret",
  "service": "wireless",
  "protocol": "udp",
  "timeout": 200
}
```

**Expected Response (Success):**
```json
{
 "message": "added",
 "id": "*1"
}
```

**Request JSON Payload (Error - invalid parameters):**
```json
{
 "address": "192.168.88.100",
  "secret": "your_radius_secret",
  "service": "wrong_service",
  "protocol": "udp",
  "timeout": 200
}
```

**Expected Response (Error):**
```json
{
 "message": "failure: invalid value for argument service",
 "error": true
}
```

**Explanation:**

*   The MikroTik API accepts JSON objects to represent the properties of the resources you want to create/modify/delete.
*   `address`, `secret`, `service`, `protocol` and `timeout` parameters are mapped to the respective MikroTik CLI parameters for `radius add`.
*   The response `message` contains a success or failure result and the `id` of the created object if the request is successful.
*   The `error` field will be present with a value of `true` when an error occurs, and the `message` field will contain a description of the problem.

To update the interface via the REST API:

**Endpoint:** `/interface/wireless`

**Method:** PATCH

**Request JSON Payload:**

```json
{
 "=.id":"*1",
 "security-profile":"radius-security"
}
```

**Expected Response (Success):**

```json
{
 "message": "updated"
}
```

*    `.id` specifies the id of the object to update, which can be retrieved by querying the resource `/interface/wireless`.
*   `security-profile` will update the security profile.

To add the security profile via the REST API:
**Endpoint:** `/interface/wireless/security-profiles`

**Method:** POST
**Request JSON Payload:**
```json
{
    "name": "radius-security",
    "mode":"dynamic-keys",
    "authentication-types":"eap"
}
```

**Expected Response (Success):**

```json
{
 "message": "added",
 "id":"*4"
}
```

To add an IP address via REST API:

**Endpoint:** `/ip/address`
**Method:** POST

**Request JSON Payload:**
```json
{
"address":"176.25.247.1/24",
"interface":"wlan-50"
}
```

**Expected Response (Success):**

```json
{
    "message":"added",
    "id":"*1"
}
```

**Handling Errors:**

*   Check the `error` field in the JSON response.
*   Use the `message` field to understand the nature of the error.
*   Double-check parameter values against the CLI documentation.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a long, random, and complex shared secret.
*   **Secure RADIUS Server:** Protect your RADIUS server from unauthorized access.
*   **EAP Type:** When possible, use more secure EAP methods like EAP-TLS (requiring client certificates) instead of EAP-PEAP or EAP-MSCHAPv2 if the clients support them.
*   **Firewall Rules:** Use MikroTik firewall rules to restrict access to the RADIUS server from unwanted networks and restrict access to the router itself.

## Self Critique and Improvements:

*   **Scalability:** This setup works well for a small number of users but may not be optimal for larger deployments. A more robust solution would involve clustering and/or load balancing the RADIUS servers.
*   **EAP Methods:**  EAP-TLS offers a stronger authentication method than EAP. This should be configured based on the clients' capabilities.
*   **Logging:** Proper logging and alerting should be set up for RADIUS authentication failures and successes.
*   **Dynamic VLAN Assignment:** This example can be extended to demonstrate how to dynamically place users on different VLANs.
*   **Configuration Management:** For a large deployment, a more robust configuration management solution (like Ansible or similar) would be preferable to manual CLI commands.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):**

*   RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) for users connecting to a network.
*   It is a client-server protocol where network access devices (like our MikroTik router) act as RADIUS clients and the RADIUS server (which could be a separate server, or a module installed on the MikroTik) acts as the server.
*   When a client tries to connect, the RADIUS client forwards authentication requests to the server, which responds with either acceptance or rejection based on its configuration.
*   RADIUS simplifies user management by allowing the central management of user accounts, passwords, and access privileges.

## Detailed Explanation of Trade-offs:

*   **Pre-Shared Keys (PSK) vs RADIUS:** PSK is simpler to configure for small networks. RADIUS provides more security and centralized management, making it ideal for larger or security-conscious environments.  RADIUS is also significantly more scalable.
*   **EAP-PEAP vs EAP-TLS:**  EAP-PEAP is easier to deploy than EAP-TLS but EAP-TLS provides stronger security by using certificates.  EAP-TLS should be used where the clients support it.
*   **RADIUS Timeout:** A small timeout value can cause failures during high load or slow RADIUS responses. A large timeout can lead to long connection times. The best timeout depends on the environment and should be adjusted based on testing.
*   **UDP vs TCP for RADIUS:** UDP is the standard and the one that is usually used. TCP may have some benefits when dealing with packet loss, but it also adds overhead and complexity.
*   **Local vs Remote RADIUS:**  Local RADIUS can be set up directly on the MikroTik itself using the User Manager Package. This is ideal if the network is small and does not need a very robust and scaled setup. Remote RADIUS is ideal for larger and more critical setups.

## Configuration for Specific RouterOS Versions:

The provided configuration should be compatible with RouterOS 6.48, 7.x, and 7.11. There should be no commands or parameters listed that are specific to just one of these versions, as they are all commonly used. If future changes introduce new features, or deprecate old ones, this specific guidance will have to be reevaluated and updated.

This detailed guide provides a robust starting point for integrating RADIUS authentication into your MikroTik network, including step-by-step configuration, common troubleshooting tips, and real-world security considerations.
