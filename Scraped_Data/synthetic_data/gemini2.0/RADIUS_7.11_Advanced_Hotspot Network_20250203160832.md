Okay, let's dive into creating detailed documentation for RADIUS authentication on a MikroTik RouterOS 7.11 device within a hotspot network using the specific subnet and interface you've provided.

## Scenario Description

We're setting up a hotspot network that uses RADIUS authentication for client access. This means that users attempting to connect to the hotspot will have their credentials verified against a RADIUS server. Our MikroTik router, running RouterOS 7.11, will act as the NAS (Network Access Server) that communicates with the RADIUS server. The hotspot will operate on subnet `61.173.55.0/24`, using the interface `ether-14` for client connections. We'll focus on a practical, real-world configuration suitable for a small to medium-sized hotspot environment.

## Implementation Steps

Here’s a step-by-step guide to configuring RADIUS for your hotspot:

### Step 1: Initial Setup and Interface Configuration

**Goal:** Ensure our interface is ready and confirm basic network settings.

*   **Before:** The interface `ether-14` is assumed to be in a default state, potentially unconfigured, or part of a bridge already.
*   **Action:** Assign an IP address to the interface and make sure it is enabled.
    ```mikrotik
    /interface ethernet
    print where name="ether-14"
    # If not enabled, enable the interface
    /interface ethernet enable ether-14

    /ip address
    add address=61.173.55.1/24 interface=ether-14
    ```
    *   `interface ethernet print where name="ether-14"`: This command prints out the configuration of `ether-14`, this will be useful to make sure it was the correct interface before making changes.
    *   `interface ethernet enable ether-14`: This ensures that the interface is enabled and capable of transmitting data.
    *   `ip address add address=61.173.55.1/24 interface=ether-14`: This assigns the static IP address 61.173.55.1 to `ether-14` and enables clients to connect via this address. This will also allow the router to communicate to a radius server on the network.
*   **After:** The interface `ether-14` is enabled, has IP address `61.173.55.1/24` set, and is ready for hotspot configuration.

### Step 2: Hotspot Configuration

**Goal:** Create a basic hotspot server and profile.

*   **Before:** There is no hotspot server created.
*   **Action:** Add a hotspot server and a hotspot profile. Configure the local address (ip address assigned in the previous step) and name the server. In addition, ensure the profile is setup to use RADIUS.
    ```mikrotik
    /ip hotspot
    add name=hotspot1 interface=ether-14 address-pool=none profile=default
    /ip hotspot profile
    add name=hsprof1 use-radius=yes
    /ip hotspot set hotspot1 profile=hsprof1
    ```
    *   `/ip hotspot add name=hotspot1 interface=ether-14 address-pool=none profile=default`: This sets up the hotspot server. `address-pool=none` is used here as the router is not acting as the DHCP server for clients, and is being used to authenticate via the radius server instead.
    *   `/ip hotspot profile add name=hsprof1 use-radius=yes`: This sets up the hotspot profile and importantly enables RADIUS authentication.
    *   `/ip hotspot set hotspot1 profile=hsprof1`: This command applies the newly created profile to the hotspot server we created previously.
*   **After:** A hotspot server named `hotspot1` is running on `ether-14` using a profile named `hsprof1` that uses RADIUS authentication.

### Step 3: RADIUS Server Configuration

**Goal:** Add RADIUS server details.

*   **Before:** No RADIUS server is configured on the router.
*   **Action:**  Configure the router with the RADIUS server IP address, secret, and other specific parameters.
    ```mikrotik
    /radius
    add address=192.168.88.100 secret="radius_secret" service=hotspot timeout=3
    ```
    *   `/radius add address=192.168.88.100 secret="radius_secret" service=hotspot timeout=3`:
        *   `address=192.168.88.100`: Replace this with the actual IP address of your RADIUS server.
        *   `secret="radius_secret"`: Replace `radius_secret` with the actual shared secret configured on the RADIUS server.
        *   `service=hotspot`: Specifies that this RADIUS server configuration is for the hotspot service.
        *  `timeout=3`: Sets the timeout, in seconds, for a response from the RADIUS server before the authentication is considered a failure.

*   **After:** The MikroTik router is now configured to communicate with the RADIUS server at 192.168.88.100, using shared secret `radius_secret`, for hotspot authentication.

### Step 4: Enable the Hotspot

**Goal:** Ensure the hotspot is enabled.

*   **Before:** The hotspot is created but may not be running.
*   **Action:** Enable the hotspot service.
    ```mikrotik
    /ip hotspot set hotspot1 enabled=yes
    ```
    *   `/ip hotspot set hotspot1 enabled=yes`: Enables the configured hotspot server.

*   **After:** The hotspot server is active and will try to authenticate clients via the RADIUS server.

## Complete Configuration Commands

Here is the complete set of MikroTik CLI commands:

```mikrotik
# Step 1: Initial Interface Configuration
/interface ethernet
print where name="ether-14"
/interface ethernet enable ether-14
/ip address
add address=61.173.55.1/24 interface=ether-14

# Step 2: Hotspot Configuration
/ip hotspot
add name=hotspot1 interface=ether-14 address-pool=none profile=default
/ip hotspot profile
add name=hsprof1 use-radius=yes
/ip hotspot set hotspot1 profile=hsprof1

# Step 3: RADIUS Server Configuration
/radius
add address=192.168.88.100 secret="radius_secret" service=hotspot timeout=3

# Step 4: Enable the Hotspot
/ip hotspot set hotspot1 enabled=yes

```

## Common Pitfalls and Solutions

*   **RADIUS Secret Mismatch:**
    *   **Problem:** If the RADIUS secret in the MikroTik configuration doesn’t match the secret on the RADIUS server, authentication will fail.
    *   **Solution:** Double-check the secret in both MikroTik and your RADIUS server configuration. Use the command `/radius print` in MikroTik to verify the configured secret is correct.

*   **Network Reachability:**
    *   **Problem:** The MikroTik router cannot reach the RADIUS server.
    *   **Solution:** Verify network connectivity using `ping <radius_server_ip>` from the MikroTik terminal. Check firewall rules on the router and any other network devices that may be blocking the traffic.

*   **Incorrect RADIUS Attributes:**
    *   **Problem:** The RADIUS server might be expecting certain attributes that are not being sent by MikroTik or are being sent in the wrong format.
    *   **Solution:** Use the `/tool torch` utility on MikroTik to inspect the RADIUS packets sent by the router to diagnose which attributes are being sent. Refer to your RADIUS server's documentation to ensure compatibility. Verify that the MikroTik router has been configured to send the appropriate attributes using the commands under `/ip hotspot profile`.

*   **Timeout Settings:**
    *   **Problem:** If `timeout` on the `/radius` settings is too low, you might have authentication failures under high load or a busy network.
    *   **Solution:** Increase the timeout using the `/radius set <radius-id> timeout=<seconds> command, you can list radius settings using `/radius print`.

*   **Hotspot Profiles:**
    *   **Problem:** Incorrect hotspot profile settings may lead to failures.
    *   **Solution:** Make sure the profile being used by the hotspot has `use-radius=yes` enabled. Check under `/ip hotspot profile print` to view the status of the hotspot profile.

*   **Resource Issues**
    *   **Problem:** High CPU or memory usage on your MikroTik router can lead to slower responses or intermittent failures.
    *   **Solution:** Monitor the system resources using `/system resource print` and consider upgrading hardware, reducing hotspot usage or optimizing your configuration if necessary.

## Verification and Testing Steps

1.  **Client Connection:** Connect a client device to the hotspot network via `ether-14`.
2.  **Authentication Attempt:** The hotspot login page should appear. Attempt to log in using valid credentials (credentials configured on your RADIUS server).
3.  **Successful Login:** If authentication is successful, the client should be granted network access.
4.  **Unsuccessful Login:** If login fails, check the MikroTik logs for any RADIUS-related errors using `/log print where topics~"radius"`. Review the server logs on the RADIUS server as well.
5.  **RADIUS Packet Inspection:** Use the `/tool torch` utility on MikroTik (interface: ether-14 or where your RADIUS server is connected) to capture the packets being exchanged between MikroTik and the RADIUS server. Use the filter `dst port 1812` (or port 1813 for accounting) to filter the traffic to/from the radius server. Examine the captured packets in Wireshark or a similar tool to ensure the RADIUS requests and responses are correct.

## Related Features and Considerations

*   **RADIUS Accounting:** Enable RADIUS accounting to track client usage. Use the command `/radius set <radius-id> accounting-backup=yes accounting-interval=30`. Ensure the radius server is configured to handle accounting packets.
*   **MAC Authentication Bypass (MAB):** If you need to bypass RADIUS authentication for specific devices, you can configure MAB in the hotspot settings of the router. This is done under `/ip hotspot user`.
*   **Hotspot Customization:** You can customize the hotspot login page (HTML and CSS files) for branding purposes. This is configured under the `/ip hotspot` section, specifically looking at the `html-directory` attribute.
*   **User Profiles:** You can create user profiles on the RADIUS server for different permissions (e.g., bandwidth limitations). These can be set under the hotspot profile `/ip hotspot profile`.
*   **Multiple RADIUS Servers:** You can configure secondary RADIUS servers as backups, should the primary become unavailable, by adding more entries to the `/radius` section.

## MikroTik REST API Examples

The MikroTik REST API can be used to manage RADIUS configuration.

**Example 1: Add a new RADIUS server**

*   **Endpoint:** `/radius`
*   **Method:** `POST`
*   **JSON Payload:**
    ```json
    {
      "address": "192.168.88.101",
      "secret": "another_radius_secret",
      "service": "hotspot",
      "timeout": 5
    }
    ```
*   **Expected Response:**
    ```json
    {
      "message": "added",
      "id": "*1"
    }
    ```
    *   `address`: IP Address of the radius server.
    *   `secret`: RADIUS shared secret.
    *   `service`: Service the radius server should be used for.
    *   `timeout`: Timeout in seconds before the request to the RADIUS server fails.
*   **Error Handling:** Handle errors like `invalid-value`, or `already-exists`.

**Example 2: Get all RADIUS servers**

*   **Endpoint:** `/radius`
*   **Method:** `GET`
*   **Expected Response:**
    ```json
    [
    {
        ".id": "*0",
        "address": "192.168.88.100",
        "secret": "radius_secret",
        "service": "hotspot",
        "timeout": "3",
        "accounting-backup": "no",
        "accounting-interval": "600",
        "authentication-port": "1812",
        "accounting-port": "1813",
        "called-id": "",
        "framed-address-pool": "",
        "max-sessions": "0",
        "realm": ""
      },
      {
        ".id": "*1",
        "address": "192.168.88.101",
        "secret": "another_radius_secret",
        "service": "hotspot",
        "timeout": "5",
         "accounting-backup": "no",
        "accounting-interval": "600",
        "authentication-port": "1812",
        "accounting-port": "1813",
        "called-id": "",
        "framed-address-pool": "",
        "max-sessions": "0",
        "realm": ""
      }
    ]
    ```
*   **Error Handling:** Handle errors like `not-found`.

**Example 3: Delete a RADIUS server**

*   **Endpoint:** `/radius/*0`  (replace `*0` with the actual `.id` of the radius server)
*   **Method:** `DELETE`
*   **Expected Response:**
    ```json
    {
      "message": "removed"
    }
    ```
*   **Error Handling:** Handle errors like `not-found`.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a strong and complex shared secret. This secret needs to match on both the radius server and the router.
*   **Secure RADIUS Server:** Harden your RADIUS server and keep it up-to-date with the latest security patches.
*   **Firewall Rules:** Implement firewall rules on your MikroTik to restrict access to the RADIUS server only from trusted IP addresses or subnets.
*   **Monitor Logs:** Regularly review the MikroTik logs and RADIUS server logs for any unusual activity or authentication failures.
*   **Secure API access:** When using the REST API, ensure that the API has proper authentication and access control to prevent unauthorized changes to the router.
*   **Avoid clear text credentials:** When using winbox, ensure your username and password is not easily guessed. It is best practice to use SSH/API instead.

## Self Critique and Improvements

This configuration covers the essentials for a RADIUS-backed hotspot. Here are potential improvements:

*   **Dynamic RADIUS Settings:** Instead of hardcoding values such as the IP address, you could implement dynamic DNS lookup via the Mikrotik's `/tool dns` settings.
*   **Advanced RADIUS Attributes:** Explore using advanced RADIUS attributes for more granular control over user sessions (e.g. `Acct-Interim-Interval`). This can be configured under `/ip hotspot profile` with attributes such as `radius-accounting-delay`.
*   **Redundancy:** Implement multiple RADIUS servers in a more elegant fashion, as well as creating specific healthchecks to verify the uptime of these servers.
*   **More fine-grained access control:** Use VLANs to further segment your network or apply more advanced firewalling rules.
*   **Automated Configuration:** Explore tools like Ansible or Terraform to automate the deployment of these settings. This is useful in larger deployments where you have multiple devices to manage.
*   **Security Audits:** Conduct regular security audits and penetration tests to ensure all devices in your network are secure.
*   **Automation of user management:** Look at using tools such as freeradius-web or similar to automate the creation of users and passwords on your RADIUS server.
*   **Documentation**: Documentation such as this should be kept up-to-date to ensure future changes are reflected.
*   **Consider using a dedicated subnet** for managing the Mikrotik and Radius server. This will give you additional flexibility in configuration.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service):**

*   RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users attempting to access a network. It is a client-server protocol.
*   The MikroTik Router in this setup acts as a NAS (Network Access Server), which is the "client" in the RADIUS architecture.
*   The RADIUS server is typically a separate server responsible for verifying user credentials and managing access policies.
*   When a user tries to connect to a hotspot, the MikroTik NAS sends the user’s login credentials to the RADIUS server.
*   The RADIUS server checks the credentials against its database. Upon successful authentication, the RADIUS server instructs the NAS to grant access to the user.
*   RADIUS can handle various authentication methods including username/password, PAP, CHAP, MSCHAP, etc. It is typically configured via the RADIUS Server.

## Detailed Explanation of Trade-offs

*   **Local Hotspot Users vs RADIUS:**
    *   **Local Users:** Easier to configure for small deployments, users and passwords are stored on the router itself.
    *   **RADIUS Users:** Better for medium to large networks because it offers centralized user management and more advanced features like RADIUS accounting and attribute setting. RADIUS also provides better security than local users, and are less vulnerable if the router is comprised.
    *   **Trade-off:** Local users are less complex, but less scalable and less secure. RADIUS is more complex, but scalable, secure, and more feature-rich.

*   **RADIUS Accounting:**
    *   **Enabled Accounting:** Provides detailed usage reports, allows for time or bandwidth limiting and helps in troubleshooting.
    *   **Disabled Accounting:** Simpler to configure, but you will not have usage statistics.
    *   **Trade-off:** Accounting adds overhead but provides insights into the network.

*   **Hardware Requirements:**
    *   **Powerful Router:** Better performance with many clients.
    *   **Less Powerful Router:** May experience slowdowns or instability with many users.
    *   **Trade-off:** Resource-intensive setups, such as a busy hotspot, may need high-end hardware. This is relevant if other resource intensive features are running on the router.

*  **Single vs Multiple Radius Servers**
    *   **Single Server:** Simpler to configure, but causes a single point of failure. If your single server goes down, the entire hotspot service will fail.
    *   **Multiple Servers:** Provides redundancy but requires more complex configuration. The failure of one server will not prevent other servers from processing authentication requests.
    *   **Trade-off**: Single servers are easier to maintain but lack redundancy. Multiple servers provides redundancy but more complex in setup and ongoing maintenance.

## Configuration for RouterOS 7.11

All commands provided are compatible with MikroTik RouterOS 7.11. No specific commands from newer versions or obsolete commands from older versions were included.

This comprehensive guide should give you a strong foundation for implementing RADIUS authentication for your hotspot network. Remember to always test thoroughly in a non-production environment before making changes in a live network.
