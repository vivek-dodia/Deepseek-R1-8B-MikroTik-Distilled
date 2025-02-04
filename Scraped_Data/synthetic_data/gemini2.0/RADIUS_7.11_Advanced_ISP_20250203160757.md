Okay, let's craft a comprehensive and expert-level documentation for RADIUS authentication on a MikroTik router, focusing on the specified context.

## Scenario Description

This document details the configuration of a MikroTik RouterOS device (version 7.11, but adaptable to 6.48 and other 7.x versions) operating in an ISP environment. Specifically, we will configure the router to utilize a RADIUS server for authenticating users connecting to the 'wlan-94' interface, operating on the 10.238.253.0/24 subnet.  This configuration is crucial for centralizing user authentication and management in a controlled network environment, often found in ISP setups. We'll be covering the required steps for successful RADIUS interaction, along with security considerations.

## Implementation Steps

Here's a step-by-step guide to configure RADIUS authentication for the 'wlan-94' interface:

**1. Check and Prepare the Interface:**

*   **Before:** Ensure the 'wlan-94' interface is configured for the intended operation.
    *   **CLI Example:**
        ```mikrotik
        /interface wireless print where name=wlan-94
        ```
    *   **Winbox:** Navigate to `Wireless > Interfaces` and select the `wlan-94` interface.
    *   **Expected Output:** Review the interface’s current configuration, including its mode (e.g., AP Bridge), SSID, and IP address. Note down the current interface configuration.

*   **Why?**  This ensures that you start from a known state. It is not strictly required for RADIUS, but is good practice.

*   **Action:** No changes are required if interface is configured as desired. For example, ensure the interface is enabled and functioning.

**2. Add a RADIUS Server Configuration:**

*   **Before:** No RADIUS server configuration exists.
    *   **CLI Example:**
        ```mikrotik
        /radius print
        ```
    *   **Winbox:** Navigate to `Radius`. You'll see an empty list (if no RADIUS configuration exists yet.)
    *   **Expected Output:** Nothing, if this is a new setup.

*   **Action:** Add a RADIUS server entry.
    *   **CLI Example:**
        ```mikrotik
        /radius add address=192.168.88.100 secret=radiussecret service=ppp timeout=3 comment="Main RADIUS Server"
        ```
    *   **Winbox:** Navigate to `Radius`, then click the `+` button, and add:
      *   `Address`: `192.168.88.100` (Replace with your RADIUS server's IP)
      *   `Secret`: `radiussecret` (Replace with your shared secret)
      *   `Service`: `ppp`
      *   `Timeout`: `3` (Seconds)
      *   `Comment`: `Main RADIUS Server`
    *   **Why?** This command configures the connection details to the RADIUS server which allows the MikroTik device to make authorization and authentication requests.
*   **After:** The RADIUS server is configured and should be visible in the `/radius print` command and winbox.
     * **CLI Example:**
        ```mikrotik
        /radius print
        ```
     * **Winbox:** Navigate to `Radius`. You will now see the added entry.

**3. Configure PPP Profile for RADIUS Authentication:**

*   **Before:** Existing PPP profiles do not necessarily use radius.
    *   **CLI Example:**
        ```mikrotik
        /ppp profile print
        ```
    *   **Winbox:** Navigate to `PPP > Profiles`.
    *   **Expected Output:** Observe existing profiles.

*   **Action:** Create or modify a PPP profile to use RADIUS.
    *   **CLI Example (Create a new profile):**
        ```mikrotik
        /ppp profile add name=radius_profile use-radius=yes comment="RADIUS Authentication Profile" local-address=10.238.253.1
        ```
    *   **CLI Example (Modify an existing profile):**
       ```mikrotik
       /ppp profile set radius_profile use-radius=yes
       ```
    *   **Winbox:**
        *   Create a profile by pressing the `+` sign in `PPP>Profiles` window, and fill the following
           *  `Name`: `radius_profile`
           *  Check the `Use Radius` checkbox.
           *  Add `Local Address`: `10.238.253.1`
          *   `Comment`: `RADIUS Authentication Profile`
       * Or, select an existing profile and check the `Use Radius` checkbox and set the local address.

    *   **Why?** This configures PPP to use RADIUS for authentication, enabling communication with the RADIUS server on a per user basis.
*   **After:** PPP Profile has been created and linked to radius authentication.
    * **CLI Example:**
        ```mikrotik
        /ppp profile print where name=radius_profile
        ```
    * **Winbox:** Check PPP > Profiles and ensure radius is enabled for the profile.

**4. Associate the PPP Profile with the Wireless Interface:**

*   **Before:** The 'wlan-94' interface is not yet using the RADIUS-enabled PPP profile.
    *   **CLI Example:**
        ```mikrotik
        /interface wireless print where name=wlan-94
        ```
     *   **Winbox:** `Wireless > Interfaces`, select `wlan-94`.
     *   **Expected Output:** The interface settings.

*   **Action:** Specify the PPP profile on the wireless interface.
    *   **CLI Example:**
        ```mikrotik
        /interface wireless set wlan-94 mode=ap-bridge security-profile=default ssid="your-ssid"  default-forward=no  ppp-profile=radius_profile
        ```
    *   **Winbox:**
      *   Navigate to `Wireless > Interfaces`, and double-click on `wlan-94`.
      *   Under the `General` tab, select `Mode`: `ap-bridge`
      *   Under the `Wireless` tab, configure `SSID`:`your-ssid`.
      *   Set `Security Profile` to `default`.
      *   Under the `General` tab, Set `Default Forward` to `no`.
      *   Under the `PPP` tab set the `PPP Profile` to `radius_profile`

    *   **Why?** This associates the wireless interface with the RADIUS authentication through the created profile. This will ensure that clients connected through wlan-94 are validated using the defined radius parameters.
*   **After:** Users connecting to 'wlan-94' will be authenticated by the RADIUS server.
    *   **CLI Example:**
        ```mikrotik
         /interface wireless print where name=wlan-94
        ```
    *   **Winbox:** Check the `Wireless` interface in the list.

**5. (Optional) Configure Accounting (If Required):**

*   **Before:** Accounting is disabled.
    *   **CLI Example:**
        ```mikrotik
        /radius print
        ```
    *   **Winbox:** `Radius`
    *   **Expected Output:** Settings under Accounting.
*   **Action:** Enable accounting, if required.
    *   **CLI Example:**
        ```mikrotik
        /radius set [find address=192.168.88.100] accounting=yes interim-update=5m
        ```
    *   **Winbox:**
        *   Navigate to `Radius`
        *   Select the Radius entry.
        *   Check the `Accounting` checkbox and set the `Interim Update` value to `5m`
    *   **Why?**  Accounting allows the RADIUS server to keep track of user sessions for usage tracking and billing purposes.
*   **After:** Accounting is active.
     *   **CLI Example:**
        ```mikrotik
         /radius print
        ```
    *   **Winbox:** Check the `Radius` settings.

## Complete Configuration Commands

Here's the full set of CLI commands:

```mikrotik
# Add RADIUS server configuration
/radius add address=192.168.88.100 secret=radiussecret service=ppp timeout=3 comment="Main RADIUS Server"

# Create a PPP profile for RADIUS authentication
/ppp profile add name=radius_profile use-radius=yes comment="RADIUS Authentication Profile" local-address=10.238.253.1

# Configure the wireless interface to use the PPP profile and mode ap-bridge
/interface wireless set wlan-94 mode=ap-bridge security-profile=default ssid="your-ssid"  default-forward=no  ppp-profile=radius_profile

# (Optional) Enable accounting on the RADIUS server config
/radius set [find address=192.168.88.100] accounting=yes interim-update=5m

# Example showing how to configure a security profile
/interface wireless security-profiles add name=default mode=dynamic-keys authentication-types=wpa2-psk,wpa-psk group-encryption=aes-ccm  unicast-encryption=aes-ccm wpa-pre-shared-key=your_wpa_key wpa2-pre-shared-key=your_wpa_key
```

**Parameters Explanation:**

| Command        | Parameter            | Description                                                                                                      |
|----------------|---------------------|-------------------------------------------------------------------------------------------------------------------|
| `/radius add`   | `address`           | IP address of the RADIUS server.                                                                                    |
|                | `secret`            | Shared secret between the router and the RADIUS server.                                                            |
|                | `service`           | RADIUS service being used, usually `ppp`.                                                                           |
|                | `timeout`           | Timeout in seconds for RADIUS communication.                                                                     |
|                | `comment`           | Optional descriptive comment for this RADIUS server entry.                                                        |
| `/ppp profile add` | `name`            | Name of the PPP profile.                                                                                          |
|                | `use-radius`        | Enables RADIUS authentication for this profile.                                                                      |
|                | `local-address`    | Specifies a static local IP address for ppp connections.                                                                |
|                | `comment`       | Optional descriptive comment for this PPP profile.                                                               |
| `/interface wireless set`| `wlan-94`    | Specific interface name.                                                                                          |
|                | `mode`              | Wireless mode (e.g., `ap-bridge` for access point).                                                               |
|                | `security-profile` | Security Profile to use for wireless security.                                                                 |
|                | `ssid`              | Service Set Identifier (SSID) for the wireless network.                                                            |
|                | `default-forward`              | Do not route packets for non-authorized clients.  Must be disabled.                                                            |
|                | `ppp-profile`       | Links the wireless interface to a specific PPP profile.                                                             |
| `/radius set`| `accounting`       | If set to yes, accounting packets are sent. |
|                | `interim-update`    | Periodic update interval, in minutes, to the accounting server. |
| `/interface wireless security-profiles add` | `name`       | Security Profile Name.                                                               |
|                | `mode`    | Authentication mode.                                                               |
|                | `authentication-types` | authentication types.                                                            |
|                | `group-encryption` | group encrtyption.                                                            |
|                | `unicast-encryption` | Unicast encryption.                                                                  |
|                | `wpa-pre-shared-key` | wpa pre-shared key.                                                             |
|                | `wpa2-pre-shared-key` | wpa2 pre-shared key.                                                             |


## Common Pitfalls and Solutions

1.  **RADIUS Server Unreachable:**
    *   **Problem:** Router cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Check IP reachability: Use `ping <radius-server-ip>` from the MikroTik CLI.
        *   Ensure firewall rules on the router or network are not blocking traffic to the RADIUS server on UDP ports 1812 (Authentication) and 1813 (Accounting).
        *   Verify the correct IP address and secret on both the router and RADIUS server configuration.
    *   **MikroTik specific tool:** Torch `/tool torch interface=<interface-connected-to-radius-server> port=1812,1813` to view packets.

2.  **Incorrect Shared Secret:**
    *   **Problem:** Authentication fails even if communication is established.
    *   **Solution:** Double-check the shared secret on both the MikroTik router and RADIUS server. They *must* match.
        *   Re-enter the secret in both the MikroTik configuration and the Radius server configuration.

3.  **Incorrect RADIUS Profile Settings:**
    *   **Problem:**  The PPP profile is not correctly configured, leading to issues when user authentication fails.
    *   **Solution:** Check the PPP profile to make sure the `use-radius=yes` is enabled. Double check the PPP local address to make sure it is a valid address on the 10.238.253.0/24 subnet.

4.  **Firewall Rules:**
   *   **Problem:** Firewall rules blocking Radius communication on the MikroTik device itself, or on upstream devices.
   *   **Solution:** Check the firewall rules to make sure that communication with the RADIUS server is allowed on the relevant ports.
   *  **MikroTik specific tool:** Use the `/ip firewall filter print` to view firewall rules.

5.  **High CPU or Memory:**
    *   **Problem:** If there is a high number of concurrent clients, the authentication process may cause high CPU usage on the router, causing delays or errors.
    *   **Solution:** Monitor the resource usage using `/system resource monitor`. Consider using more powerful router, offload the authentication to a separate server, or limit the number of allowed concurrent connections.

## Verification and Testing Steps

1.  **Check RADIUS Server Connectivity:**
    *   Use the `ping` tool:
        ```mikrotik
        /ping 192.168.88.100 count=3
        ```
        Successful ping means the router can reach the server.
2.  **Monitor the Router Logs:**
    *   Check system logs for RADIUS-related events. Specifically look for successful or failed authentication attempts in the logs. Use `/log print topic=radius` to see those messages, or navigate to `System>Logs`.

3.  **Test Connection with a Client:**
    *   Connect a client device to the 'wlan-94' SSID.
    *   Attempt to authenticate with valid RADIUS credentials on the device.
    *   If all is well, the device will connect to the network.
    *   Check MikroTik logs to confirm authentication success.

4.  **Use Torch to Monitor Traffic**
    *  Use `/tool torch interface=<interface-connected-to-radius-server> port=1812,1813` to view packet flow to the radius server.

## Related Features and Considerations

1.  **Hotspot:** The described configuration can integrate with a Hotspot setup for captive portal functionalities. User can be redirected to a login page, and then authentication through RADIUS can be performed once the user enters credentials.

2.  **User Manager:** MikroTik's User Manager can be used as a simple RADIUS server, although often a more robust server is used in an ISP environment.

3.  **Advanced Accounting:** More advanced accounting features are available to generate reports and detailed statistics regarding usage.

4.  **Security Profile configuration:** Use a more secure authentication method if necessary, as well as increase the encryption strength by modifying the security profile, for example WPA2, AES.

## MikroTik REST API Examples

(Note: These examples assume you have the API service enabled on your MikroTik)

**1. Add a RADIUS Server Entry:**

*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **Request Payload (JSON):**
    ```json
    {
      "address": "192.168.88.100",
      "secret": "radiussecret",
      "service": "ppp",
      "timeout": 3,
      "comment": "Main RADIUS Server"
    }
    ```
*   **Expected Response (JSON):**
    ```json
    {
      ".id": "*1234" ,
      "address": "192.168.88.100",
      "secret": "radiussecret",
      "service": "ppp",
      "timeout": 3,
       "comment": "Main RADIUS Server"
     }
    ```
    (Note: `.id` will be different every time the command is issued)
*   **Error Handling:** If the parameters are invalid, the response will contain an `error` key with an error message. Check the errors and try again.

**2. Modify a RADIUS Server Entry**

*   **Endpoint:** `/radius/{id}`  (replace `{id}` with the actual id)
*   **Method:** `PUT`
*  **Request Payload (JSON):**
    ```json
    {
       "address": "192.168.88.100",
      "secret": "anothersecret",
      "service": "ppp",
       "timeout": 3,
       "comment": "Main RADIUS Server Modified"
    }
   ```
*   **Expected Response (JSON):**
   ```json
     {
      ".id": "*1234" ,
       "address": "192.168.88.100",
       "secret": "anothersecret",
       "service": "ppp",
        "timeout": 3,
        "comment": "Main RADIUS Server Modified"
    }
   ```

**3. List all RADIUS server entries:**

*   **Endpoint:** `/radius`
*   **Method:** `GET`
*   **Request Payload:** None
*   **Expected Response:** A JSON array of RADIUS server objects.

**4. Error Handling**
   * The API uses a standard error response, usually with a 4xx status code if the request failed because of client error. For example, trying to delete an item that does not exist will yield a `404 Not Found` message and corresponding error payload in JSON.
   * To understand the API response, you can read the detailed error message in the JSON payload.

## Security Best Practices

1.  **Strong Shared Secret:** The RADIUS shared secret must be complex and different from other secrets used on the network. A simple or commonly used secret can be vulnerable to a man-in-the-middle attack. Use a combination of characters, numbers and symbols.

2.  **Restrict RADIUS server access:** Limit access to the RADIUS server via firewall rules to only the necessary interfaces and IP addresses. This will mitigate a Denial of Service attack.

3.  **Encrypt Communication:** Use IPSEC or other types of encryption to protect the communication between the MikroTik and the RADIUS server if the network can be compromised.

4.  **Regular Audits:** Perform regular audits of both the MikroTik and the RADIUS server configuration to ensure everything is set up correctly and securely.

5.  **Limit Access to the Router:** Limit physical and remote access to the router through strong passwords, and by using MikroTik's user management system. Also disable all services that are not necessary.

## Self Critique and Improvements

This configuration is a good starting point for RADIUS integration.

*   **Improvements:**
    *   Implementing RADIUS accounting, particularly for ISP environments, to track bandwidth consumption.
    *   Using more sophisticated security measures like 802.1X authentication instead of pre-shared keys for added security, if devices connected to the network support it.
    *   Consider using a backup RADIUS server in case the primary RADIUS is not accessible.
    *   Monitor the MikroTik's performance to make sure it is handling the load imposed by all concurrent users.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**
RADIUS is a network protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network. The RADIUS server acts as a central repository for user credentials and network policies. The MikroTik device forwards the login information of each client to the radius server, which validates the credentials and replies with a success or a failure. RADIUS is a common protocol in ISP and Enterprise environments where authentication and usage tracking is critical.

**PPP (Point-to-Point Protocol):**
PPP is a data link protocol used to establish a direct connection between two nodes. The MikroTik router uses PPP as the basis for setting up authenticated connection, using RADIUS as an authentication method.

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:** Local authentication (e.g., using MikroTik's local user database) is simpler to configure but has less flexibility. RADIUS enables central user management and more complex user policies. The trade off is in complexity; you must set up a radius server separately.

*   **Accounting:** Enabling accounting increases the load on the MikroTik router and the RADIUS server, but it allows for detailed usage tracking and billing. This trade off is only relevant when accounting data is needed.

*   **Security:** Using less secure or shared passwords is easier but less safe. Using WPA3, WPA2 with enterprise mode, and 802.1x provides better security but requires more complex configuration and hardware support. The trade off is security vs user convenience and supported hardware.

## Configuration for Specific RouterOS Versions

This guide targets RouterOS 7.11, 6.48 and most 7.x versions. It uses commands that are available across these versions.

*   If using older versions (below 6.48), double-check command availability and syntax, since some parameters may be different. Some functions may not be available.

This detailed document should provide a comprehensive guide for configuring RADIUS on MikroTik, tailored for an ISP environment. Remember to replace placeholders with your actual network details and RADIUS server configuration.
