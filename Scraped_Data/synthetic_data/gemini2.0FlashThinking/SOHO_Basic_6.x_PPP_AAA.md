---
generated_at: 2025-02-03T21:15:24.155790
topic: PPP AAA
category: Security Services
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Documentation: PPP AAA for SOHO Environments (v6.x)

**Document Version:** 1.0
**Author:** [Your Name/Company Name], MikroTik Certified Engineer
**Date:** October 26, 2023
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic
**Topic:** PPP AAA (Authentication, Authorization, and Accounting)

**Introduction:**

This document provides a basic guide to implementing PPP (Point-to-Point Protocol) AAA (Authentication, Authorization, and Accounting) on MikroTik RouterOS version 6.x for Small Office/Home Office (SOHO) environments. PPP AAA is crucial for controlling access to your network via PPP connections, ensuring only authorized users can connect and potentially tracking their usage. This documentation will cover configuration using both the Command Line Interface (CLI) and a Python-based API example, along with practical considerations for SOHO deployments.

**1. Architecture Diagram Requirements:**

For a basic SOHO PPP AAA setup, we will consider a scenario where remote users (e.g., teleworkers, mobile users) connect to a MikroTik router acting as a PPP server (e.g., PPPoE Server, L2TP Server, SSTP Server). The MikroTik router will handle authentication against a local user database.

```mermaid
graph LR
    A[Remote User 1] --> B(MikroTik Router);
    C[Remote User 2] --> B;
    D[Remote User N] --> B;
    subgraph SOHO Network
    B;
    end
    B -- PPP Interface (PPPoE/L2TP/SSTP) --> "AAA (Local User Database)";
    B --> E[Internal Network / Internet];
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style A fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#ccf,stroke:#333,stroke-width:1px
    style D fill:#ccf,stroke:#333,stroke-width:1px
    style E fill:#eee,stroke:#333,stroke-width:1px

    classDef client fill:#ccf,stroke:#333,stroke-width:1px;
    class A,C,D client;
```

**Diagram Explanation:**

* **Remote Users (A, C, D):** Represent users connecting remotely to the SOHO network.
* **MikroTik Router (B):**  The MikroTik device acting as the PPP server and AAA server.
* **PPP Interface (PPPoE/L2TP/SSTP):**  The type of PPP server interface configured on the MikroTik.
* **AAA (Local User Database):**  Indicates that authentication will be performed against a locally configured user database on the MikroTik router.
* **Internal Network / Internet (E):** Represents the SOHO's internal network and connection to the internet, accessible to authenticated PPP users.

**2. CLI Configuration with Inline Comments:**

This example will configure a basic PPPoE server with local user authentication.

```routeros
# --- 1. Enable PPPoE Server Interface ---
/interface pppoe-server server
add service-name=pppoe-soho interface=ether1 enabled=yes # Replace 'ether1' with your WAN interface

# --- 2. Create a PPP Profile for AAA ---
/ppp profile
add name=pppoe-profile local-address=192.168.88.1 remote-address=ppp-pool use-encryption=required only-one=yes # Basic profile settings
#   - name: Profile name for easy reference
#   - local-address: IP address of the PPP server interface on the SOHO network
#   - remote-address: IP pool to assign to PPP clients
#   - use-encryption: Require encryption for PPP connections (important for security)
#   - only-one: Allow only one connection per username (optional for security in SOHO)

# --- 3. Create an IP Address Pool for PPP Clients ---
/ip pool
add name=ppp-pool ranges=192.168.88.100-192.168.88.199 # Define a range of IP addresses for PPP clients
#   - name: Pool name for easy reference
#   - ranges: IP address range to be assigned

# --- 4. Create Local PPP User Accounts ---
/ppp secret
add name=user1 password=password1 service=pppoe profile=pppoe-profile # Create user 'user1'
add name=user2 password=password2 service=pppoe profile=pppoe-profile # Create user 'user2'
#   - name: Username for PPP authentication
#   - password: Password for the user (use strong passwords in real scenarios)
#   - service: Specifies the PPP service type (pppoe, l2tp, etc.)
#   - profile: Links the user to the PPP profile we created

# --- 5. Apply the PPP Profile to the PPPoE Server Interface ---
/interface pppoe-server server set pppoe-soho profile=pppoe-profile # Link the profile to the PPPoE server
#   - pppoe-soho: Name of the PPPoE server interface we created
#   - profile: Assign the 'pppoe-profile' for AAA

# --- 6. (Optional) Enable Accounting (Basic Logging) ---
/log
add topics=ppp action=memory # Log PPP related events to memory
/system logging action add name=ppp-log target=disk file-name=ppp.log topics=ppp # (Optional) Log PPP events to disk for more persistent records
#   - topics=ppp:  Specify PPP related events to be logged
#   - action=memory/disk: Choose logging target (memory for basic, disk for persistent logs)

# --- 7. (Optional) Firewall Rules (Example - Allow PPP traffic) ---
/ip firewall filter
add chain=input protocol=tcp dst-port=1723 action=accept comment="Allow L2TP" disabled=yes # Example for L2TP (port 1723) - Enable if using L2TP
add chain=input protocol=udp dst-port=1701 action=accept comment="Allow L2TP" disabled=yes # Example for L2TP (port 1701) - Enable if using L2TP
add chain=input protocol=tcp dst-port=443 action=accept comment="Allow SSTP" disabled=yes # Example for SSTP (port 443) - Enable if using SSTP
add chain=input protocol=tcp dst-port=8291 action=accept comment="Allow Winbox" disabled=yes # (Optional - For remote Winbox access - consider security implications)
add chain=input action=drop comment="Drop other input" # Drop all other input traffic for security
```

**3. REST API Implementation (Python Code):**

This Python example uses the `routeros_api` library to configure the same PPPoE server and AAA setup as in the CLI example.

```python
import routeros_api

HOST = 'your_router_ip'  # Replace with your router's IP address
USERNAME = 'your_username'  # Replace with your router's username
PASSWORD = 'your_password'  # Replace with your router's password

try:
    # Connect to MikroTik Router
    api = routeros_api.RouterOsApiPool(HOST, username=USERNAME, password=PASSWORD, port=8728, use_ssl=False)
    connection = api.get_connection()

    # --- 1. Enable PPPoE Server Interface ---
    pppoe_server_path = '/interface/pppoe-server/server'
    connection.path(pppoe_server_path).add(
        service_name='pppoe-soho',
        interface='ether1',  # Replace 'ether1' with your WAN interface
        enabled=True
    )
    print("PPPoE Server 'pppoe-soho' enabled.")

    # --- 2. Create PPP Profile ---
    ppp_profile_path = '/ppp/profile'
    connection.path(ppp_profile_path).add(
        name='pppoe-profile',
        local_address='192.168.88.1',
        remote_address='ppp-pool',
        use_encryption='required',
        only_one='yes'
    )
    print("PPP Profile 'pppoe-profile' created.")

    # --- 3. Create IP Address Pool ---
    ip_pool_path = '/ip/pool'
    connection.path(ip_pool_path).add(
        name='ppp-pool',
        ranges='192.168.88.100-192.168.88.199'
    )
    print("IP Pool 'ppp-pool' created.")

    # --- 4. Create PPP User Accounts ---
    ppp_secret_path = '/ppp/secret'
    connection.path(ppp_secret_path).add(
        name='user1',
        password='password1',
        service='pppoe',
        profile='pppoe-profile'
    )
    connection.path(ppp_secret_path).add(
        name='user2',
        password='password2',
        service='pppoe',
        profile='pppoe-profile'
    )
    print("PPP Users 'user1' and 'user2' created.")

    # --- 5. Apply Profile to PPPoE Server ---
    connection.path(pppoe_server_path).set(
        numbers='pppoe-soho', # Use 'numbers' to target the specific interface
        profile='pppoe-profile'
    )
    print("Profile 'pppoe-profile' applied to PPPoE Server 'pppoe-soho'.")

    # --- 6. (Optional) Enable Basic Logging (Memory Log) ---
    log_path = '/log'
    connection.path(log_path).add(topics='ppp', action='memory')
    print("Basic PPP logging to memory enabled.")


    print("\nPPP AAA configuration completed successfully via API.")

except routeros_api.exceptions.RouterOsApiError as e:
    print(f"Error configuring MikroTik via API: {e}")
finally:
    if 'api' in locals() and api:
        api.close() # Close the API connection
```

**4. Common Debugging Scenarios:**

| Scenario | Possible Cause | Debugging Steps | CLI/Tools |
|---|---|---|---|
| **Authentication Failure** | Incorrect username/password, User disabled, Profile mismatch | 1. Verify username and password are correct. 2. Check if user is enabled (`/ppp secret print`). 3. Ensure user's profile is correctly assigned (`/ppp secret print`). 4. Check PPP logs for authentication errors (`/log print topics=ppp`). | `/ppp secret print`, `/ppp profile print`, `/log print topics=ppp` |
| **No IP Address Assigned** | IP pool exhausted, Profile misconfiguration, DHCP server issues (if using DHCP relay) | 1. Check IP pool availability (`/ip pool print`). 2. Verify `remote-address` in PPP profile points to a valid pool (`/ppp profile print`). 3. If using DHCP relay, check DHCP server and relay configuration. | `/ip pool print`, `/ppp profile print`, `/ip dhcp-server print` |
| **PPP Connection Instability/Disconnects** | Network congestion, MTU issues, Encryption problems, Keepalive timeout | 1. Monitor network for congestion. 2. Adjust MTU (try lowering it). 3. Try different encryption settings (if possible, but encryption is recommended). 4. Check and adjust keepalive settings in PPP profile (if needed for specific scenarios). 5. Review PPP logs for disconnect reasons. | `/interface pppoe-server server print`, `/ppp profile print`, `/log print topics=ppp` , `ping` , `traceroute` |
| **Slow PPP Connection Speed** | Router CPU/Memory overload, Bandwidth limitations, Encryption overhead, QoS configuration | 1. Monitor router CPU and memory usage (`/system resource print`). 2. Check internet bandwidth capacity. 3. Consider hardware acceleration for encryption (if available and applicable). 4. Review QoS configurations that might be limiting PPP traffic. | `/system resource print`, `/interface monitor-traffic`, `/queue simple print` |

**5. Version-Specific Considerations (RouterOS v6.x):**

* **Feature Stability:** RouterOS v6.x is a mature and stable version. Basic PPP AAA functionality is well-established.
* **Security Patches:** Ensure you are running the latest v6.x release to benefit from security patches available for this branch.
* **Feature Limitations (compared to v7.x):**  v6.x lacks some newer features present in v7.x (e.g., WireGuard VPN, some advanced routing protocols). For basic SOHO PPP AAA, v6.x is generally sufficient.
* **API Library Compatibility:** The `routeros_api` Python library is generally compatible with RouterOS v6.x.

**6. Security Hardening Measures:**

* **Strong Passwords:** Enforce strong and unique passwords for all PPP user accounts. Regularly review and update passwords.
* **Encryption:** Always enable and require encryption for PPP connections (`use-encryption=required` in PPP profile).  AES-based encryption is recommended for good security and performance.
* **`only-one=yes`:** In the PPP profile, using `only-one=yes` prevents multiple concurrent logins with the same username, enhancing security in SOHO environments.
* **Firewall Rules:** Implement strict firewall rules to control access to the MikroTik router and the internal network from PPP clients. Only allow necessary ports and services. (Example firewall rules provided in CLI config section).
* **Disable Unused Services:** Disable any unused services on the MikroTik router (e.g., Telnet, FTP if not needed).
* **Regular Updates:** Keep RouterOS updated to the latest stable version within the v6.x branch to patch security vulnerabilities.
* **Logging and Monitoring:** Enable PPP logging to monitor connection attempts and potential security incidents. Regularly review logs.
* **Rate Limiting (Optional):** Consider implementing rate limiting on PPP profiles to restrict bandwidth usage per user if needed.
* **Consider RADIUS (For larger SOHO or future growth):** While local user database is suitable for basic SOHO, for larger deployments or if you anticipate growth, consider migrating to RADIUS server for centralized user management and more advanced AAA features.

**7. Performance Optimization Tips:**

* **FastTrack:** Utilize FastTrack firewall rule to bypass connection tracking for established PPP connections, improving throughput.
    ```routeros
    /ip firewall filter
    add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes comment="FastTrack established connections"
    add action=accept chain=forward connection-state=established,related comment="Accept established,related connections"
    ```
* **Efficient Queues (Simple Queues):** If QoS is needed, use Simple Queues for basic bandwidth management. Avoid complex queue tree configurations for basic SOHO setups unless strictly required.
* **CPU/Memory Monitoring:** Regularly monitor router CPU and memory usage. If resource utilization is consistently high, consider upgrading to a more powerful MikroTik device if performance is critical.
* **Encryption Considerations:** While encryption is crucial for security, it does have a slight performance overhead. AES encryption is generally efficient. Avoid very weak encryption algorithms as they might be easily compromised.
* **MTU Size:** Ensure correct MTU size is configured on PPP interfaces and physical interfaces to avoid fragmentation and performance degradation. Default MTU is usually sufficient, but in some scenarios, adjustments might be necessary.

**SOHO Specific Requirements:**

**Real-World Deployment Examples:**

* **Home Internet Access (PPPoE Client to ISP + PPPoE Server for Remote Access):** A common SOHO setup involves the MikroTik router acting as a PPPoE client to connect to the ISP and simultaneously running a PPPoE server to allow secure remote access for family members or home workers.
* **Small Office VPN Access (L2TP/IPsec or SSTP Server):** For small offices, L2TP/IPsec or SSTP servers can be configured to provide secure VPN access for employees working remotely or traveling. Local AAA on MikroTik is suitable for small teams.
* **Remote Access to Security Cameras/NAS (Port Forwarding + PPP):** In scenarios where remote access to specific devices within the SOHO network (like security cameras or NAS) is needed, PPP VPN can be combined with port forwarding for secure access.

**Scalability Considerations:**

* **Local User Database Limits:** For very small SOHO networks (e.g., < 10-20 users), the local user database in MikroTik is sufficient.
* **Transition to RADIUS (For future growth):** If the SOHO network grows and requires more users, centralized user management, or advanced AAA features (e.g., user groups, policies), consider migrating to a RADIUS server. MikroTik RouterOS supports RADIUS client functionality.
* **Hardware Capacity:** For a significant increase in PPP users and traffic, ensure the MikroTik router hardware (CPU, memory, interfaces) is capable of handling the load. Choose a RouterBOARD model appropriate for the scale of your SOHO network.

**Monitoring Configurations:**

* **Basic Logging (CLI/Winbox):** Enable PPP logging as shown in the CLI and API examples. Monitor logs via CLI (`/log print topics=ppp`) or Winbox (`Logs`).
* **Simple Graphs (Winbox):** Use Winbox's built-in graphing tools (`Tools` -> `Graphing`) to monitor interface traffic, CPU usage, and memory usage.
* **SNMP Monitoring (For more advanced SOHO):** For slightly larger SOHO environments, consider enabling SNMP on the MikroTik router and using an SNMP monitoring tool (e.g., Zabbix, PRTG) to collect performance data and set up alerts.
* **The Dude (MikroTik's Network Monitoring Tool - v6.x compatible):** MikroTik's "The Dude" network monitoring application (v6.x compatible) can be used for basic monitoring of the MikroTik router and connected devices within the SOHO network.

**Disaster Recovery Steps:**

* **Regular Configuration Backups:** Implement a schedule for regular configuration backups of the MikroTik router.
    - **CLI Backup:** `/export file=backup-config` (Creates a backup file named `backup-config.rsc` in the router's files).
    - **Winbox Backup:** `Files` -> `Backup` button.
* **Automated Backup Script (Example - Basic Shell Script):**

```bash
#!/bin/bash
ROUTER_IP="your_router_ip"
USERNAME="your_username"
PASSWORD="your_password"
BACKUP_DIR="/path/to/backup/directory" # Local directory to save backups

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="mikrotik-backup-${TIMESTAMP}.rsc"

/tool fetch url="http://${USERNAME}:${PASSWORD}@${ROUTER_IP}/export" http-method=get http-data="" http-header="" as-value=yes output-file="$BACKUP_FILE"

if [ -f "$BACKUP_FILE" ]; then
  mv "$BACKUP_FILE" "$BACKUP_DIR/$BACKUP_FILE"
  echo "Backup saved to: $BACKUP_DIR/$BACKUP_FILE"
else
  echo "Backup failed!"
fi
```

* **Disaster Recovery Procedure:**
    1. **Hardware Failure:** If the MikroTik router fails, replace it with a new device.
    2. **Factory Reset (if needed):** If you can access the new router, perform a factory reset to ensure a clean configuration.
    3. **Restore Configuration:**
        - **Winbox Restore:** `Files` -> `Restore` button and select the backup `.rsc` file.
        - **CLI Restore:** `/import file-name=backup-config.rsc` (Place the `backup-config.rsc` file in the router's files first).
    4. **Verify Configuration:** After restoring, thoroughly verify the configuration, especially PPP AAA settings, interfaces, and firewall rules.
    5. **Test Connectivity:** Test PPP connections and internet access to ensure the recovery process was successful.

**Comparative Table: Local AAA vs. RADIUS AAA for SOHO:**

| Feature | Local AAA (MikroTik) | RADIUS AAA |
|---|---|---|
| **User Management** | Local database on MikroTik | Centralized user database (e.g., FreeRADIUS, Windows NPS) |
| **Scalability** | Limited to SOHO scale (tens of users) | Highly scalable, suitable for larger deployments |
| **Complexity** | Simpler to configure for basic setups | More complex setup involving a separate RADIUS server |
| **Features** | Basic authentication, authorization | Advanced features like user groups, policies, accounting, dynamic VLAN assignment (depending on RADIUS server) |
| **Cost** | No additional cost (uses built-in MikroTik features) | Requires a RADIUS server (software and potentially hardware) |
| **Best Suited For** | Very small SOHO networks, basic remote access needs | Growing SOHO networks, offices with more users, requirement for centralized user management and advanced AAA features |

**Conclusion:**

Implementing PPP AAA on MikroTik RouterOS for SOHO environments provides essential security and control over remote access. This document has outlined basic configuration steps using both CLI and API, along with practical considerations for SOHO deployments. For basic SOHO setups, local AAA on MikroTik is often sufficient and easy to manage. However, as the network grows or more advanced AAA features are required, transitioning to a RADIUS-based AAA solution should be considered. Remember to prioritize security hardening measures and regular backups to maintain a robust and secure SOHO network.

## API Reference Cheat Sheet
```python
# Universal API Helper Function
def mikrotik_api_call(
    method: str,
    endpoint: str,
    data: dict = None,
    timeout: int = 10
) -> dict:
    '''
    Universal MikroTik API handler with error checking
    '''
    try:
        response = requests.request(
            method,
            f"https://{ROUTER_IP}/rest{endpoint}",
            auth=HTTPBasicAuth(API_USER, API_PASS),
            json=data,
            verify=SSL_VERIFY,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e.response.status_code} - {e.response.text}")
        return {"error": str(e)}
```