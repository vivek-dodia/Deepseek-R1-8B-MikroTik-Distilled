Okay, let's craft a detailed technical document for PPP AAA on MikroTik RouterOS 7.11, within the context of a point-to-point link using the specified parameters.

## Scenario Description:

We are setting up a simple Point-to-Point (P2P) link between two MikroTik routers. We'll focus on the authentication and authorization part on a single router, using a PPP server (PPPoE in this example) and local user database using MikroTik’s `/ppp secret`. This configuration illustrates a basic AAA setup. We are not covering RADIUS here, but rather the simplest setup possible with local authentication. The server will be on the router with the ether9 interface. Client can be a MikroTik or another device that is using PPPoE to access our network. Our PPPoE server will be configured to allow the client a /24 range, within the specified subnet: 197.158.57.0/24. Our network is on the interface `ether-9`.

## Implementation Steps:

### 1. Configure the Interface and IP Address
- **Before:** The interface `ether-9` has no IP configuration.

- **Action:** Assign an IP address to the `ether-9` interface. This interface is the one connecting us to our client.

- **CLI Command:**
```mikrotik
/ip address
add address=197.158.57.1/24 interface=ether-9 network=197.158.57.0
```
    - `add`: Specifies the operation - adding a new IP address
    - `address=197.158.57.1/24`: Assigns the IP address 197.158.57.1 with a /24 subnet mask.
    - `interface=ether-9`: Applies the address to the `ether-9` interface.
    - `network=197.158.57.0`: explicitly defines the network address.
- **After:** `ether-9` is configured with a static IP. In Winbox, you can go to `IP -> Addresses` to verify.

### 2. Create a PPP Profile
- **Before:** There is no PPP profile configured.

- **Action:** Create a PPP profile. This profile will dictate the allowed DNS server, and the allowed MTU. Note that for our purposes, the local address will be the same as our local IP, since it is a point-to-point link.

- **CLI Command:**
```mikrotik
/ppp profile
add name="pppoe-profile" local-address=197.158.57.1 remote-address=197.158.57.2 dns-server=1.1.1.1,8.8.8.8 mtu=1492
```
  - `add`: Add a new entry
    - `name="pppoe-profile"`:  Name of the profile
    - `local-address=197.158.57.1`: The local IP address for the PPP interface which is our server endpoint.
    - `remote-address=197.158.57.2`: The remote IP address for the PPP interface which will be assigned to our client upon connection.
    - `dns-server=1.1.1.1,8.8.8.8`:  Specifies the DNS servers that will be provided to clients.
    - `mtu=1492`:  Maximum Transmission Unit of the PPP interface.
- **After:** A new PPP profile named `pppoe-profile` exists. This can be verified in Winbox `PPP -> Profiles`

### 3. Add a PPP Secret
- **Before:** No PPP secrets are configured.

- **Action:** Create a PPP secret (user/password) for our client to use, associating it with the profile we just created.

- **CLI Command:**
```mikrotik
/ppp secret
add name="client1" password="strongpassword" service=pppoe profile="pppoe-profile"
```
- `add`: Add a new entry
    - `name="client1"`: Username for the PPP client
    - `password="strongpassword"`: Password for the user. Use a strong, unique password.
    - `service=pppoe`: We are specifying this secret is for PPPoE access.
    - `profile="pppoe-profile"`: Specifies the PPP profile this secret will use.

- **After:** A user is configured with the associated password. You can verify this under `PPP -> Secrets` in winbox.

### 4. Enable PPPoE Server
- **Before:** No PPPoE Server is running

- **Action:** Enable the PPPoE server on `ether-9`.

- **CLI Command:**
```mikrotik
/ppp server pppoe
set enabled=yes interface=ether-9 max-mru=1492 max-mtu=1492
```
   - `set`: Sets configuration of the command
    - `enabled=yes`: Enables the PPPoE Server.
    - `interface=ether-9`: Specifies that the PPPoE server listens on the `ether-9` interface.
    - `max-mru=1492`: Maximum Receivable Unit for the PPPoE.
     - `max-mtu=1492`: Maximum Transmission Unit for PPPoE connections.
- **After:** The PPPoE server is active and listening on `ether-9`. Verify in Winbox under `PPP -> Server`, under the `PPPoE` tab.

## Complete Configuration Commands:

```mikrotik
/ip address
add address=197.158.57.1/24 interface=ether-9 network=197.158.57.0

/ppp profile
add name="pppoe-profile" local-address=197.158.57.1 remote-address=197.158.57.2 dns-server=1.1.1.1,8.8.8.8 mtu=1492

/ppp secret
add name="client1" password="strongpassword" service=pppoe profile="pppoe-profile"

/ppp server pppoe
set enabled=yes interface=ether-9 max-mru=1492 max-mtu=1492
```

## Common Pitfalls and Solutions:

*   **Authentication Failures:**
    *   **Problem:** Incorrect username or password in the client configuration.
    *   **Solution:** Double-check the username and password on both the server and the client.
*   **Profile Mismatch:**
    *   **Problem:** The profile configured for the user on the server does not match the server configuration.
    *   **Solution:** Ensure both the secret and the server are using the same profile.
*   **MTU/MRU Issues:**
    *   **Problem:** Incorrect MTU/MRU settings on the server or client, leading to dropped packets.
    *   **Solution:** Verify the MTU/MRU settings are consistent on both the server and client.  Start with a conservative MTU of 1492 and adjust up if necessary.
*   **IP Conflicts:**
    *  **Problem:** A local IP address conflict where the server's IP is in the same range, or the /24 range is already used in a device in the network.
    *   **Solution:** Ensure the IP address ranges are different and avoid duplicate IP addresses.
*   **Firewall Issues:**
    *   **Problem:** The firewall on the server is blocking PPP traffic.
    *   **Solution:** Make sure the firewall is not blocking the required ports and interfaces.
*   **Resource Issues:**
    *   **Problem:** A large number of PPP clients can cause high CPU load.
    *   **Solution:** Monitor the CPU and memory usage with tools like `/system resource print`.  Consider hardware upgrades if needed or use a simpler authentication methods.

## Verification and Testing Steps:

1.  **Client Connection:**
    *   Use a PPP client on the remote end (e.g. another MikroTik router configured for PPPoE or a computer using the built-in PPPoE client), configure the interface to connect to your `ether-9` interface, with the `client1` username and the password, `strongpassword`.
2.  **Verify Connection Status:**
    *   On the MikroTik server, use the command `/ppp active print` to verify the connection is active.
    *   In winbox go to `PPP -> Active connections`, you should see the user `client1` with an IP address (in our case `197.158.57.2`).
3.  **Ping Test:**
    *   From the client device, ping the server's IP address (`197.158.57.1`) to check connectivity.
    *  From the server, ping the client's PPP assigned address (`197.158.57.2`) to check connectivity.
4. **Torch Utility**
    * On the `ether-9` interface, use `/tool torch interface=ether-9`. You should see the PPP traffic on that interface.

## Related Features and Considerations:

*   **RADIUS Authentication:** For larger environments, consider using RADIUS for centralized user authentication and accounting.
*   **Bandwidth Management (Queues):** Use simple queues or Queue Trees to limit bandwidth for each user.
*   **Firewall Filters:**  Set up firewall rules to control traffic for PPP users.
*   **IP Pools:** Instead of using a single remote IP, you can set up a pool, so each PPP client gets a unique IP from the pool range.
*   **MPPE Encryption:** Enable encryption in the profile settings for a more secure connection, using `use-encryption=yes`.

## MikroTik REST API Examples:

Since we're using CLI commands, a basic use of MikroTik's REST API would be useful. Here's an example for adding a PPP Secret using the REST API:

```json
# API Endpoint: /ppp/secret
# Method: POST
# JSON Payload

{
    "name": "api-client",
    "password": "apipassword",
    "service": "pppoe",
    "profile": "pppoe-profile"
}
```

**Explanation:**

*   **`POST /ppp/secret`**: The endpoint to create a new PPP secret entry.
*   **`name`**: User name for the client.
*   **`password`**: Password for the user.
*  **`service`**: Type of service to use (`pppoe`, `ppp`, `l2tp`).
*   **`profile`**: The profile name this user will use.

**Example API Response (Successful):**
```json
{
    ".id": "*1",
    "name": "api-client",
    "service": "pppoe",
    "profile": "pppoe-profile",
    "disabled": "false"
}
```
**Example API Response (Error):**
```json
{
    "message": "already have entry with name 'api-client'",
    "error": true
}
```

**Error Handling:**
API responses should be checked for errors.  If there is an error it will be shown as a `message` and `error` equal to true, similar to the example.

## Security Best Practices

*   **Strong Passwords:** Always use strong and unique passwords for PPP secrets.
*   **Limit Access:** Restrict access to your MikroTik router and PPP configuration.  Do not allow external access to the device other than PPPoE traffic.
*   **Encryption:** If security is required, enable MPPE encryption on your profile using `use-encryption=yes`.
*   **Firewall Rules:** Implement strict firewall rules to control access to the PPP server, and prevent any unexpected access to the router.
*   **Regularly Update RouterOS:** Keep your RouterOS updated for security patches.
* **Change Default Username:** Change the default `admin` username and add a strong password, since that is the easiest target for attacks.

## Self Critique and Improvements

This configuration provides a basic Point-to-Point link with PPPoE AAA. Some potential improvements could be:

*   **Add Logging:** Implement detailed logging for PPP connections and authentication attempts for troubleshooting purposes.
*   **Centralized AAA:** Use a RADIUS server for centralized authentication if there are more than a few clients to manage.
*   **IP Pools:** Utilize IP Pools to assign unique dynamic IPs to clients from a specific range instead of a single IP on each client connection.
*   **Scripting:** Add scripting for better management, especially for more dynamic network scenarios.
*   **Advanced Traffic Management**: Implement quality of service (QoS) to prioritize traffic.

## Detailed Explanations of Topic

PPP (Point-to-Point Protocol) provides a standard method for transmitting data over a serial connection or other point-to-point media. It provides authentication, compression, and error detection. PPP uses protocols like PAP and CHAP.

AAA (Authentication, Authorization, and Accounting) is a framework for controlling network access and managing user activities:
    * **Authentication** verifies the identity of the client attempting to access the network. This is achieved using username and password on our example.
    * **Authorization** determines what network resources a user is allowed to use after they have been authenticated. On our example the resource given to the client is the `/24` range of IP addresses, using the PPPoE profile we have created.
    * **Accounting** tracks what resources a user is using. In our case, since this is a small setup, we are not covering accounting here, but it is part of the AAA framework.

## Detailed Explanation of Trade-offs

* **Local vs RADIUS AAA:**
    *   **Local AAA (like this example):** Simple to set up for small networks but not scalable, less secure than RADIUS, and harder to audit.
    *   **RADIUS AAA:** More complex to set up, but offers scalability, centralized management, more secure authentication, and accounting capabilities.
*   **PAP vs CHAP:**
    *   **PAP (Password Authentication Protocol):** Transmits passwords in plaintext, making it vulnerable to eavesdropping. Not advised for production use.
    *   **CHAP (Challenge Handshake Authentication Protocol):** Encrypts the password, making it more secure than PAP. MikroTik uses CHAP by default.
*   **Single IP vs IP Pool:**
    *   **Single Remote IP:** Simple setup but limits each user to the same remote IP.
    *   **IP Pool:** Allows each user to receive a unique IP, offering more flexibility for future network expansion.

## Configuration for Specific RouterOS Versions:

The commands and configuration are valid for RouterOS versions 6.48 and 7.x, however, it is recommended to use the latest stable RouterOS version (7.11) for the best performance and security. All commands used are supported in 6.48 and 7.x.

That completes this detailed configuration for PPP AAA on MikroTik! This guide should provide everything you need to get started. If you have any other questions, feel free to ask.
