Okay, let's dive into creating detailed documentation for PPP AAA on a MikroTik router, targeting RouterOS 7.11 within a Hotspot network context. This will be an advanced configuration focusing on user authentication and authorization via a RADIUS server.

## Scenario Description

We are setting up a Hotspot network using a MikroTik router.  Users will connect to the network via PPPoE (Point-to-Point Protocol over Ethernet), and their authentication and authorization will be handled by an external RADIUS server. This setup is ideal for providing controlled access to the internet for multiple users, often used in hotels, cafes, or small businesses. Our specific subnet will be `195.174.73.0/24`, and the VLAN interface used for this service is `vlan-71`.

## Implementation Steps

Here's a step-by-step guide to configure PPP AAA with RADIUS authentication. We'll provide both CLI examples and WinBox guidance where applicable.

### Step 1: Configure the VLAN Interface

First, we need to ensure that the VLAN interface exists and is configured with the correct IP address.

**Before:**
*   No VLAN interface `vlan-71` exists.

**Action (CLI):**

```mikrotik
/interface vlan
add name=vlan-71 vlan-id=71 interface=ether1
/ip address
add address=195.174.73.1/24 interface=vlan-71
```

**Action (WinBox):**
*   Navigate to `Interfaces` -> `VLAN`. Add a new VLAN interface, named `vlan-71`, VLAN ID of 71, and attached to the appropriate interface (e.g., `ether1`).
*   Navigate to `IP` -> `Addresses`. Add a new IP address, `195.174.73.1/24`, to the `vlan-71` interface.

**After:**
*   VLAN Interface `vlan-71` is created.
*   IP address `195.174.73.1/24` is assigned to `vlan-71`.

### Step 2: Configure the PPPoE Server

Next, we configure a PPPoE server on the VLAN interface.

**Before:**
*   No PPPoE server is running on `vlan-71`.

**Action (CLI):**

```mikrotik
/interface pppoe-server server
add service-name=hotspot interface=vlan-71 max-mru=1480 max-mtu=1480 default-profile=default
```

**Action (WinBox):**
*   Navigate to `PPP` -> `PPPoE Servers`.
*   Click the `+` to add a new PPPoE server. Set the `Interface` to `vlan-71`, `Service Name` to `hotspot`, `Max MRU` to `1480` and `Max MTU` to `1480`. The `Default Profile` can be left as `default` for now.

**After:**
*   A PPPoE server is running on `vlan-71`.

### Step 3: Configure the RADIUS Client

Now, we configure the RADIUS client to communicate with the external RADIUS server.

**Before:**
*   No RADIUS client is configured.

**Action (CLI):**
```mikrotik
/radius
add address=192.168.88.10 secret=mysecret service=ppp timeout=3
```

**Action (WinBox):**
*   Navigate to `RADIUS`.
*   Click `+` to add a new RADIUS server entry.
*   Set `Address` to the IP address of your RADIUS server (e.g., `192.168.88.10`).
*   Set `Secret` to the shared secret configured on your RADIUS server (e.g., `mysecret`).
*   Ensure `Service` is set to `ppp`.
*   Set `Timeout` to `3`.

**After:**
*   The RADIUS client is configured.

### Step 4: Configure PPP Profile to Use RADIUS

Now we configure the PPP profile to use the RADIUS server for authentication and accounting. We'll create a new profile instead of modifying the default one.

**Before:**
*   The default PPP profile is in use and we will create a new one for this purpose.

**Action (CLI):**

```mikrotik
/ppp profile
add name=hotspot-radius use-encryption=yes local-address=195.174.73.2 remote-address=195.174.73.254 dns-server=8.8.8.8,8.8.4.4 change-tcp-mss=yes only-one=no address-list=hotspot-users
/interface pppoe-server server set 0 default-profile=hotspot-radius
```

**Action (WinBox):**
*   Navigate to `PPP` -> `Profiles`.
*   Click `+` to add a new profile, name it `hotspot-radius`
*   Set `Local Address` to `195.174.73.2`, and `Remote Address` to `195.174.73.254`
*   Set `DNS Server` to `8.8.8.8,8.8.4.4`
*   Enable `Use Encryption`, `Change TCP MSS`, `Only One` should be set to `no`.
*   Add to Address List `hotspot-users`
*   Navigate back to `PPP` -> `PPPoE Servers`, select the PPPoE server configured in Step 2, and change the `Default Profile` to `hotspot-radius`.

**After:**
*   New PPP profile is created and set for use on PPPoE server.
*   PPPoE will use the new radius profile

### Step 5: (Optional) Add a Firewall Filter

Optionally, add a firewall filter to only allow the desired traffic to and from this interface.

**Action (CLI):**
```mikrotik
/ip firewall filter
add chain=forward action=accept in-interface=vlan-71 out-interface=!vlan-71
add chain=forward action=drop in-interface=vlan-71
```
This firewall rule will allow traffic going out of the vlan-71 interface to any other interface, and drop all the other traffic.

**Action (WinBox):**
*   Navigate to `Firewall` -> `Filter Rules`.
*   Click `+` to add new rules.
*   Create a rule to `Accept` forward traffic with `in-interface` as `vlan-71` and `out-interface` as anything other than `vlan-71`.
*   Create a rule to `Drop` any traffic coming into `vlan-71` after.

**After:**
*  Firewall rules have been added.

## Complete Configuration Commands

```mikrotik
/interface vlan
add name=vlan-71 vlan-id=71 interface=ether1
/ip address
add address=195.174.73.1/24 interface=vlan-71
/interface pppoe-server server
add service-name=hotspot interface=vlan-71 max-mru=1480 max-mtu=1480 default-profile=default
/radius
add address=192.168.88.10 secret=mysecret service=ppp timeout=3
/ppp profile
add name=hotspot-radius use-encryption=yes local-address=195.174.73.2 remote-address=195.174.73.254 dns-server=8.8.8.8,8.8.4.4 change-tcp-mss=yes only-one=no address-list=hotspot-users
/interface pppoe-server server set 0 default-profile=hotspot-radius
/ip firewall filter
add chain=forward action=accept in-interface=vlan-71 out-interface=!vlan-71
add chain=forward action=drop in-interface=vlan-71
```

**Parameter Explanation:**

| Command               | Parameter             | Description                                                                                                                                                                     |
| :-------------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `/interface vlan add`   | `name`                | The name of the new VLAN interface                                                                                                                                             |
|                       | `vlan-id`            | The VLAN ID for this interface                                                                                                                                               |
|                       | `interface`          | The physical interface to which this VLAN interface is associated                                                                                                            |
| `/ip address add`      | `address`            | The IP address and subnet mask for the interface                                                                                                                               |
|                       | `interface`          | The interface to which this IP address is assigned                                                                                                                           |
| `/interface pppoe-server server add` | `service-name`      | The service name for the PPPoE server (e.g., "hotspot").                                                                                                      |
|                                   | `interface`        | The interface on which the PPPoE server is listening                                                                                                                     |
|                                   | `max-mru`           | Maximum receive unit for the PPPoE connection.                                                                                                                            |
|                                   | `max-mtu`            | Maximum transmit unit for the PPPoE connection.                                                                                                                              |
|                                  | `default-profile`   | The default PPP profile to use when establishing a PPPoE connection.                                                                                                           |
| `/radius add`         | `address`            | IP address of the RADIUS server.                                                                                                                                             |
|                       | `secret`              | The shared secret key used between the MikroTik router and the RADIUS server.                                                                                                 |
|                       | `service`            | The service for which the RADIUS server will be used (ppp, hotspot)                                                                                                          |
|                       | `timeout`           | RADIUS timeout                                                                                                                                              |
| `/ppp profile add` | `name`             | Name for the profile                                                                                                                             |
|                      | `use-encryption`        | Enable encryption                                                                                                                            |
|                      | `local-address`       | IP for local address                                                                                                                             |
|                      | `remote-address`         | IP for remote address                                                                                                                            |
|                       | `dns-server`         | The DNS servers to assign to clients                                                                                                                              |
|                       | `change-tcp-mss`         | Adjust TCP MSS to match MTU                                                                                                                              |
|                       | `only-one`         | Allows only one instance of the connection                                                                                                                             |
|                       | `address-list`         | List that the clients will be added to                                                                                                                             |
| `/interface pppoe-server server set` | `default-profile`         | Sets the ppp profile to be used                                                                                                                             |
| `/ip firewall filter add` | `chain` | Firewall chain to add rule to                                                                                                                        |
|  | `action`   | Action to apply to matching traffic. `accept` allows it, `drop` blocks it.                                                                                         |
| | `in-interface` | The interface the traffic enters from.                                                                                         |
|  | `out-interface` | The interface that the traffic exits from. `!vlan-71` means any other interface except for vlan-71                                                                                         |

## Common Pitfalls and Solutions

*   **RADIUS Server Connectivity Issues:** If authentication fails, verify the following:
    *   **Firewall:** Ensure the MikroTik router can reach the RADIUS server (check firewall rules and network connectivity).
    *   **Shared Secret:** Double-check that the secret on the MikroTik and RADIUS server match exactly.
    *   **RADIUS Server Logs:** Review the RADIUS server's logs for any error messages related to authentication attempts.
    * **Timeout:** If there is high network latency, a low timeout will cause the router to declare the radius server as not working and not attempting the authentication. Increase this time in `/radius` if needed.

*   **Incorrect PPP Profile Settings:** Problems with address assignment, DNS, or encryption may stem from a misconfigured profile.
    *   **Double-Check Settings:** Review the profile configuration, focusing on the IP address ranges, DNS servers, and encryption settings.
    *   **Logging:** Ensure `debug` logging is enabled for PPP and Radius, this will help trace down any issues.

*   **MTU/MRU Mismatches:** If users have trouble connecting, make sure the MTU and MRU settings are consistent across the network (1480 is a common value).

*   **Resource Usage:** A large number of concurrent users can stress the CPU and RAM on the router. Monitor resource usage and scale the router accordingly or move the RADIUS server to a dedicated machine.

*  **Security:** The shared secret can be compromised, and this would give an attacker access to the network. Be sure to set a very strong, and hard to guess secret. Limit access to the router to only trusted devices.

*   **RADIUS Accounting:** If RADIUS accounting is important for your environment, you need to configure it on the RADIUS server and in RouterOS (by setting `interim-update` in `/radius`), and also make sure that the correct attributes are being sent and received.

## Verification and Testing Steps

1.  **Connect a Client:** Connect a PPPoE client (e.g., a computer, smartphone, or another MikroTik router) to the network.
2.  **Authentication Test:** Try to authenticate using credentials that exist on the RADIUS server.
3.  **Connectivity Test:** After successful authentication, verify internet connectivity by pinging a public IP address (e.g., `ping 8.8.8.8`) or by using a DNS lookup with `nslookup google.com`.
4.  **Torch:** Use MikroTik's `/tool torch` to capture traffic on the interface `vlan-71` to verify proper data flow.
5.  **RADIUS Logs:** Check the RADIUS server logs to ensure the authentication and accounting processes are working as expected.
6. **PPP Active Connections:** View the PPP connections by going to `/ppp active`.

## Related Features and Considerations

*   **Hotspot Service:** Consider using MikroTik's built-in Hotspot feature for more complex captive portal solutions. This would involve enabling the Hotspot and changing the `ppp profile` to be used by the hotspot profile.
*   **User Management:** Manage users in the RADIUS server instead of the router for greater flexibility.
*   **Policy Based Routing:** Use policy based routing rules to apply different rules to different clients based on their authentication parameters.
*   **Traffic Shaping:** Use Queue Trees to prioritize different types of traffic. This is important in busy networks.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy.
*   **Advanced RADIUS Attributes:** Use specific RADIUS attributes for more advanced configurations (e.g., bandwidth control, VLAN assignment).
*   **Logging:** Enable detailed logging for troubleshooting and security analysis on the router and on the RADIUS server.

## MikroTik REST API Examples (if applicable)

While the MikroTik REST API can be used for many configuration aspects, configuring the PPP AAA is not commonly performed using the API directly, the API will be used to monitor or update specific aspects of the server, however, for our purposes we will provide an example to add a new radius server:

```http
# Example: Add a RADIUS server
POST /rest/radius
Content-Type: application/json

{
    "address": "192.168.88.15",
    "secret": "anothersecret",
    "service": "ppp",
    "timeout": 5
}

# Expected Response (200 OK)

{
  ".id": "*1",
  "address": "192.168.88.15",
  "secret": "anothersecret",
    "service": "ppp",
    "timeout": 5
}

# Example: Update an existing RADIUS server

PUT /rest/radius/*1
Content-Type: application/json

{
  "timeout": 10
}

# Expected Response (200 OK)

{
  ".id": "*1",
  "address": "192.168.88.15",
  "secret": "anothersecret",
  "service": "ppp",
  "timeout": 10
}
```

**API Parameter Explanation:**

*   **`address`:** The IP address of the RADIUS server.
*   **`secret`:** The shared secret key.
*   **`service`:** The service for which the RADIUS server is used, in our case `ppp`.
*   **`timeout`:** The timeout for RADIUS requests.

**Error Handling:**

*   If the payload is invalid, the API will respond with a status code in the 4xx range (e.g., 400 Bad Request).
*   If a server error happens, the API will respond with a status code in the 5xx range.
*   Be sure to inspect the response body for detailed error messages.

## Security Best Practices

*   **Strong Shared Secret:** Use a long and complex shared secret for the RADIUS server.
*   **Secure RADIUS Server:** Ensure the RADIUS server is hardened and kept up to date.
*   **Access Control:** Limit administrative access to the MikroTik router. Use strong passwords and disable unused services.
*   **Monitoring:** Monitor RADIUS logs for unusual activity or authentication failures.
*   **Firewall:** Restrict access to the RADIUS port (usually UDP 1812, 1813) to only trusted networks.

## Self Critique and Improvements

This configuration provides a solid foundation for PPP AAA using a RADIUS server. However, some improvements could be:

*   **Dynamic VLAN Assignments:** Using RADIUS to dynamically assign VLANs to users based on their credentials.
*   **Bandwidth Control:** Integrating RADIUS-based bandwidth limits per user.
*   **Accounting:** Implement full RADIUS accounting with periodic updates for logging and usage tracking.
*   **User Management Tooling:** If the configuration would get very large, consider adding a tool to help the user managament such as freeRADIUS's web interface.
* **Testing and Automation:** Fully test and automate the entire process to make it resilient and easy to reproduce.

## Detailed Explanation of Topic

**PPP (Point-to-Point Protocol):** PPP is a data link layer protocol that establishes a direct connection between two nodes. It's commonly used to establish dial-up or virtual private network (VPN) connections. In our case, we use PPPoE (PPP over Ethernet), which is very common with wired networks, especially with cable and DSL broadband setups.

**AAA (Authentication, Authorization, Accounting):** AAA is a framework for controlling access to computer resources. It's comprised of:

*   **Authentication:** Verifying the identity of a user (e.g., username/password).
*   **Authorization:** Determining what the user is allowed to do (e.g., access to the internet, specific resources).
*   **Accounting:** Tracking what the user has done (e.g., data usage, session duration).

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol used for AAA. It enables centralized authentication and authorization of users connecting to a network. When a user attempts to connect, the access point sends the user's credentials to the RADIUS server, which verifies the user's credentials and grants or denies access.

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:** Local authentication on the MikroTik router is simpler but not scalable for many users. RADIUS offers centralized management but needs an external RADIUS server, which introduces complexity.
*   **Encryption:** Enabling encryption adds security but introduces some overhead. It is advisable to always encrypt the traffic.
*   **PPPoE vs. Other Connection Methods:** PPPoE is reliable, however, it needs a client on the other end, such as a router. Other methods such as `DHCP` might be easier to configure, but the access control needs to be implemented differently.
*   **Profile vs. Default Settings:** Configuring a profile for each type of service gives better control than modifying default settings. It makes troubleshooting and changes easier to make.
*   **Firewall Rules:** Simple firewall rules are easier to implement, but they might not be suitable for the environment, adding more complex rules for different requirements will add more overhead but will make the configuration better.

## Configuration for Specific RouterOS Versions:

This configuration is primarily targeting RouterOS 7.11, however, most of the commands provided are compatible with versions from 6.48 and later, with some differences in the `interface` command.

This detailed documentation provides a comprehensive guide to configuring PPP AAA using RADIUS on a MikroTik RouterOS device. It includes specific steps, detailed commands, troubleshooting, and security considerations, making it a valuable resource for a network administrator or engineer seeking to implement this configuration.
