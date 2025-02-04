Okay, let's dive into a detailed configuration of PPP AAA with a MikroTik router, focusing on practical implementation and addressing your specific requirements.

## Scenario Description:

This scenario focuses on setting up a MikroTik router (running RouterOS 7.11) as a PPP server using RADIUS authentication for clients connecting over a bridge interface (`bridge-12`). This is a common requirement in environments where you need centralized user management and accounting for PPP connections, often seen in ISP, corporate VPN, and hotspot networks. The subnet being used is 44.246.45.0/24.

## Implementation Steps:

Here’s a step-by-step guide to configure PPP AAA with RADIUS authentication:

### 1.  Create a Bridge Interface:

* **Purpose**: We'll use `bridge-12` as the interface through which PPP connections will be established.
* **Before**: Assuming no existing bridge interface with the same name.
* **Action**: We will add the bridge.

**CLI Example:**

```mikrotik
/interface bridge add name=bridge-12
```
**Winbox Example:**

Go to: `Bridge` menu -> `+` Button -> set `name` field to `bridge-12` ->  Click `Apply` and then `OK`.

* **After**: A new bridge interface `bridge-12` will be present in the list of interfaces.
* **Result**: This creates a basic bridge interface but does not add it to the existing interfaces or bridge any interfaces. It just exists.

### 2. Add Interface to the Bridge
* **Purpose**: Now, we need to add an interface to our bridge so we can listen for packets and route them.

**CLI Example:**

```mikrotik
/interface bridge port add bridge=bridge-12 interface=ether1
```
* **Winbox Example:**

Go to `Bridge` menu -> `Port` Tab -> `+` button -> Select `bridge` to `bridge-12`, `interface` to `ether1` -> Click `Apply` and then `OK`.

* **After**: `ether1` interface will be added to `bridge-12`.
* **Result**: The bridge is now functional.

### 3. Configure the PPP Secret

*   **Purpose:** We need to create a profile with which PPP secrets will be used. These secrets contain usernames and passwords for authentication.
*   **Before**: Before creating the profile, we assume that no profiles are created.
*   **Action**: Add a new ppp secret profile.

**CLI Example:**

```mikrotik
/ppp profile add name=radius-profile use-encryption=yes
```

**Winbox Example:**

Go to `PPP` menu -> `Profiles` Tab -> `+` Button -> set `name` field to `radius-profile` and set `use encryption` to `yes` -> Click `Apply` and then `OK`.

*   **After:** A new profile will be present in the profiles list.
*   **Result**: We have created a profile to use for ppp authentication using radius.

### 4.  Set Up RADIUS Client Configuration

*   **Purpose**: Define the RADIUS server details (IP, secret, port) so MikroTik can communicate with it.
*   **Before**: No RADIUS client is configured.
*   **Action**: Configure the RADIUS client settings. Replace `192.168.88.10` with the actual RADIUS server IP, `mysecret` with the RADIUS secret and `1812` with the port if needed.

**CLI Example:**

```mikrotik
/radius add address=192.168.88.10 secret=mysecret service=ppp timeout=30ms
```

**Winbox Example:**

Go to `RADIUS` menu -> `+` Button -> Set `address` to `192.168.88.10`, `secret` to `mysecret`, and `service` to `ppp`,  `timeout` to `30ms` -> Click `Apply` and then `OK`.

*   **After**: A RADIUS client entry with the specified settings will be created.
*   **Result**: MikroTik can now communicate with the RADIUS server.

### 5. Configure the PPP Server Interface

*   **Purpose**: Configure the PPP server on the bridge interface so that the users can log in and be assigned an IP Address.
*   **Before**: No PPP server is configured on the bridge.
*   **Action**: Add an `enable` the PPP server on the bridge interface.

**CLI Example:**
```mikrotik
/interface ppp server add interface=bridge-12 enabled=yes profile=radius-profile
```
**Winbox Example:**
Go to `PPP` menu -> `Server` tab -> `+` Button -> Set `interface` to `bridge-12` and `profile` to `radius-profile` and `enabled` to yes -> Click `Apply` and then `OK`.

* **After:** The PPP server is enabled on `bridge-12`.
* **Result:** The MikroTik router is listening for new ppp connections on bridge-12.

### 6. Configure the Local Address Pool

*   **Purpose:** Define an IP pool for PPP client addresses.
*   **Before**: No IP pool is configured for PPP clients.
*   **Action**: Configure a new IP address pool.

**CLI Example:**

```mikrotik
/ip pool add name=ppp-pool ranges=44.246.45.10-44.246.45.250
```

**Winbox Example:**

Go to `IP` menu -> `Pool` Tab -> `+` Button -> set `name` field to `ppp-pool` and `ranges` to `44.246.45.10-44.246.45.250` -> Click `Apply` and then `OK`.

*   **After**: An IP address pool named `ppp-pool` is created with the specific IP ranges.
*   **Result**: When users connect via PPP, the router will hand out IPs from the address pool.

### 7.  Configure the PPP Profile (Assigning the Local Address Pool)

* **Purpose**: Assign the IP address pool to the PPP Profile.
* **Before**: The PPP profile is not using any IP address pool.
* **Action**: Assign the IP address pool `ppp-pool` to the `radius-profile`.

**CLI Example:**
```mikrotik
/ppp profile set radius-profile local-address=44.246.45.1 remote-address=ppp-pool
```

**Winbox Example:**
Go to `PPP` menu -> `Profiles` Tab -> Select the `radius-profile`-> Set `local address` to `44.246.45.1` and `remote-address` to `ppp-pool` -> Click `Apply` and then `OK`.

*   **After**: The PPP `radius-profile` will assign IPs from the ppp-pool.
*   **Result**: When a user connects via PPP with this profile, they will be assigned an IP from the pool and the server will have `44.246.45.1` as its local IP address.

## Complete Configuration Commands:

```mikrotik
/interface bridge add name=bridge-12
/interface bridge port add bridge=bridge-12 interface=ether1
/ppp profile add name=radius-profile use-encryption=yes
/radius add address=192.168.88.10 secret=mysecret service=ppp timeout=30ms
/interface ppp server add interface=bridge-12 enabled=yes profile=radius-profile
/ip pool add name=ppp-pool ranges=44.246.45.10-44.246.45.250
/ppp profile set radius-profile local-address=44.246.45.1 remote-address=ppp-pool
```

## Common Pitfalls and Solutions:

1.  **RADIUS Server Unreachable:**
    *   **Problem**: MikroTik cannot communicate with the RADIUS server.
    *   **Solution**: Check network connectivity, firewall rules, RADIUS server status, and shared secret consistency. Use `/tool ping` from MikroTik to verify connectivity to the RADIUS server. Also verify the radius logs on the radius server.
2.  **Authentication Failures**:
    *   **Problem**: Users cannot authenticate.
    *   **Solution**: Verify the username and password, ensure the RADIUS server has the user defined, confirm the user has the correct permissions and make sure the RADIUS logs do not show any errors.
3.  **IP Address Conflicts**:
    *   **Problem**: Clients get no IP address, or conflicting IPs.
    *   **Solution**: Verify the pool, make sure that there are enough addresses in the pool, and that there is no overlapping of address space with your current network. Use `/ip address print` to see what IPs are configured. Also verify that there are no more IPs configured than in your pool range.
4.  **PPP Profile Settings**:
    *   **Problem**: Issues with DNS or route propagation.
    *   **Solution**: Double-check profile configurations, like DNS server settings, and firewall rules.
5.  **Resource Issues**:
    *   **Problem**: High CPU or memory usage on the MikroTik.
    *   **Solution**:  Monitor resource usage via `/system resource monitor` and `top` command via console. Optimise firewall rules, reduce connection numbers. If needed upgrade to a higher performance device.

## Verification and Testing Steps:

1.  **Ping RADIUS Server**: Use `/tool ping 192.168.88.10` to check connectivity to the RADIUS server.
2.  **Connect with a PPP Client**: Use a PPP client (like dial-up on Windows or Linux ppp client) and connect to the MikroTik. Verify that it receives an IP address.
3.  **Monitor PPP Connections**: Use `/interface ppp active print` to see connected PPP users.
4.  **Check Radius Logs**: Examine the RADIUS server logs to verify successful authentications.
5.  **Verify Assigned IP**: On the connected client, check that the assigned IP address is from the configured pool (44.246.45.0/24).
6.  **Ping Internal IP's**: After a client successfully connects via PPP, verify if the IP Address from the pool can reach other IP's. Example: ping the gateway address of the MikroTik Router: `ping 44.246.45.1`.

## Related Features and Considerations:

*   **Accounting**: Enable RADIUS accounting to track connection times and data usage. `/radius set use-accounting=yes`
*   **Hotspot**: For a larger public network, consider implementing the MikroTik Hotspot feature for user management.
*   **Firewall Rules**: Make sure your firewall rules allow forwarding and input to the PPP interface for proper access.
*   **Mangle Rules**: Can be used to mark packets for QoS or other specific processing.
*   **VPN**: The same concepts used for PPP can also be used for IPSec VPN tunnels.

## MikroTik REST API Examples:

These calls are specific to MikroTik's API, and will not work with standard REST clients. The `token` parameter needs to be set to a login token that is retrieved from the api. See MikroTik docs for more information.

### Add a RADIUS Server
**Endpoint**: `/radius`
**Method**: POST
**Example Payload:**

```json
{
    "token": "YOUR_AUTH_TOKEN",
    "address": "192.168.88.10",
    "secret": "mysecret",
    "service": "ppp"
}
```

**Expected Response (Success - 200 OK):**

```json
{
    "message": "radius server added successfully",
    "id": "*0",
    "address": "192.168.88.10",
    "secret": "mysecret",
    "service": "ppp"
}
```

**Error handling:**
If `address`, `secret`, or `service` parameters are omitted, the API would return an error indicating required field missing. The error will be a 400 error. Other errors can arise if the token is not valid. Always check the response code and the `message` field of the json body. If you receive a 403, the user does not have the required permissions.

### Retrieve PPP Server Configurations

**Endpoint:** `/interface/ppp/server`
**Method:** GET
**Example Payload:**

```json
{
	"token": "YOUR_AUTH_TOKEN"
}
```

**Expected Response (Success - 200 OK):**
```json
[
	{
	  ".id": "*0",
		"disabled": "no",
		"keepalive-timeout": "30",
		"max-mru": "1500",
		"max-mtu": "1500",
		"mrru": "disabled",
		"name": "ppp-server-1",
		"one-session-per-host": "no",
		"profile": "radius-profile",
		"service-name": "ppp-server",
		"interface": "bridge-12",
		"comment": ""
	}
]
```

## Security Best Practices

1.  **Strong RADIUS Secret**: Use a strong, long, and complex shared secret for RADIUS communication.
2.  **Secure RADIUS Server**: Protect your RADIUS server with strong access controls, and only permit access from the MikroTik.
3.  **PPP Encryption**: Use encryption on PPP connections, such as MPPE to protect sensitive data from eavesdropping.
4.  **Firewall Rules**: Implement strict firewall rules to protect the router and connected users. Do not allow external access to the router from the ppp interface.
5.  **Monitor Logs**: Check logs regularly for suspicious activity.

## Self Critique and Improvements

This configuration provides a solid foundation for PPP AAA using RADIUS. However, it can be further improved by:

*   **Detailed Accounting**: Setting up more detailed RADIUS accounting for better monitoring.
*   **User Grouping**: Implement RADIUS attributes for specific user groups with different access levels or bandwidth control.
*   **Dynamic Allocation of VLANs**: Implement RADIUS attributes to dynamically allocate VLANs to users.
*   **Optimizing performance**: Review and optimizing firewall rules and mangle rules.
*   **Rate limiting**: Set up rate limiting on a per user basis using radius attributes.
*   **Automated fail-over**: Setting up a backup radius server in case the primary fails.

## Detailed Explanations of Topic

**PPP (Point-to-Point Protocol)**: A data link layer protocol commonly used to establish a direct connection between two nodes. PPP is frequently used for internet dial-up connections and VPNs.

**AAA (Authentication, Authorization, and Accounting)**: A security framework that controls who can access a network, what they can do, and how their activity is recorded. AAA plays a critical role in network security and management.

**RADIUS (Remote Authentication Dial-In User Service)**: A networking protocol that provides centralized AAA for users attempting to access a network or service. RADIUS is used in large networks where there are many users and access needs to be managed in a central location.

**MikroTik Implementation**: MikroTik provides support for PPP AAA over RADIUS in various service interfaces like PPP, wireless, and hotspot.

## Detailed Explanation of Trade-offs

*   **Local vs RADIUS Authentication**:
    *   **Local**: Simple to set up but lacks scalability. User management is local to the router. Good for smaller networks or testing.
    *   **RADIUS**: More complex setup but scalable, centralized user management, supports accounting. Necessary for large networks and multiple devices.

*   **PPP Server on Bridge vs Physical Interface**:
    *   **Bridge**: Allows multiple types of interfaces to be part of the same network, but might need more complex routing and rules.
    *   **Physical Interface**: Simpler routing, but limits connectivity options.

*   **IP Address Pool Management**:
    *   **Static IP Assignments**: Requires manually defining IP's for users. Hard to manage for larger networks.
    *   **Dynamic IP Assignments**: More flexible, but requires a DHCP or IP pool to allocate addresses.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 7.11 and is valid for RouterOS 6.48, and 7.x series. It avoids any commands that are specific to older or newer versions.

That covers all aspects of PPP AAA with RADIUS authentication in your specified scenario, and it provides a comprehensive guide for implementation and troubleshooting.
