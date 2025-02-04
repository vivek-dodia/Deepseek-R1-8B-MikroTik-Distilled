---
generated_at: 2025-02-03T21:37:58.797774
topic: High Availability Solutions
category: High Availability
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

```markdown
## MikroTik RouterOS High Availability for SOHO Environments (v6.x)

**Documentation for MikroTik Certified Engineers**

This document provides a comprehensive guide to implementing a basic High Availability (HA) solution using MikroTik RouterOS v6.x, specifically tailored for Small Office/Home Office (SOHO) environments. We will focus on simplicity, cost-effectiveness, and ease of management, leveraging readily available RouterOS features.

### 1. Architecture Diagram Requirements

For a basic SOHO HA setup, the most suitable and cost-effective architecture is **Active-Passive using VRRP (Virtual Router Redundancy Protocol)**.

**Diagram (Mermaid Syntax):**

```mermaid
graph LR
    subgraph Internet
        I[Internet]
    end

    subgraph "Router 1 (Master)"
        R1-WAN[WAN Interface] --> I
        R1-LAN[LAN Interface] --> SW
        R1-VRRP[VRRP Interface (Virtual IP)]
    end

    subgraph "Router 2 (Backup)"
        R2-WAN[WAN Interface] --> I
        R2-LAN[LAN Interface] --> SW
        R2-VRRP[VRRP Interface (Virtual IP)]
    end

    subgraph "Local Network"
        SW[Switch] --> PC1[PC 1]
        SW --> PC2[PC 2]
        SW --> ...
    end

    R1-VRRP --- SW
    R2-VRRP --- SW

    style R1-VRRP fill:#ccf,stroke:#333,stroke-width:2px
    style R2-VRRP fill:#eee,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5

    I --> R1-WAN & R2-WAN
    SW --> R1-LAN & R2-LAN

    linkStyle 0,1,2,3,4,5,6 stroke:#333,stroke-width:2px;
    linkStyle 7,8 stroke:#333,stroke-width:1px;

    classDef primary fill:#ccf,stroke:#333,stroke-width:2px
    classDef secondary fill:#eee,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5
```

**Diagram Explanation:**

*   **Two Identical MikroTik Routers (Router 1 and Router 2):** For simplicity and easier management, it's recommended to use identical models.
*   **Active-Passive Setup:** Router 1 is the **Master** and actively handles network traffic. Router 2 is the **Backup** and remains in standby mode.
*   **VRRP Interface:** Both routers participate in a VRRP group, sharing a **Virtual IP Address**. This VIP is configured on the LAN side and becomes the default gateway for devices on the local network.
*   **Shared Switch (SW):** Both routers are connected to the same LAN switch. This switch is where the local network devices connect.
*   **WAN Interfaces:** Each router has its own WAN interface connected to the Internet.
*   **Failover Mechanism:** In case of a failure on Router 1 (Master), Router 2 (Backup) will take over the VRRP Virtual IP and become the new Master, ensuring continuous network connectivity.

### 2. CLI Configuration with Inline Comments

This configuration assumes:

*   **Router 1 (Master):**
    *   Hostname: `Router-1-Master`
    *   WAN Interface: `ether1` (connected to Internet)
    *   LAN Interface: `ether2` (connected to LAN switch)
    *   Router ID: `1` (VRRP identifier)
    *   Priority: `110` (Higher priority to be Master initially)
    *   Virtual IP: `192.168.88.1/24` (LAN side VIP)
    *   Real IP (Router 1 on LAN): `192.168.88.2/24`
*   **Router 2 (Backup):**
    *   Hostname: `Router-2-Backup`
    *   WAN Interface: `ether1` (connected to Internet)
    *   LAN Interface: `ether2` (connected to LAN switch)
    *   Router ID: `1` (VRRP identifier - must be the same as Master)
    *   Priority: `100` (Lower priority to be Backup initially)
    *   Virtual IP: `192.168.88.1/24` (LAN side VIP - same as Master)
    *   Real IP (Router 2 on LAN): `192.168.88.3/24`
*   **LAN Network:** `192.168.88.0/24`

**Configuration on Router 1 (Master):**

```routeros
# System Identity - Set hostname for Router 1
/system identity set name=Router-1-Master

# Interface Configuration - Rename interfaces for clarity
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN

# IP Address Configuration - Set IP addresses for Router 1
/ip address add address=192.168.88.2/24 interface=LAN network=192.168.88.0 comment="Router 1 LAN IP"
/ip dhcp-client add interface=WAN disabled=no comment="WAN DHCP Client - Adjust if needed"

# VRRP Configuration - Configure VRRP on LAN interface
/interface vrrp add name=vrrp1 interface=LAN priority=110 virtual-address=192.168.88.1/24 authentication=none preempt=yes sync-connection=yes sync-group=vrrp-group1 comment="VRRP Master"

# IP Route Configuration - Default route via WAN interface - Adjust gateway if needed
/ip route add dst-address=0.0.0.0/0 gateway=WAN routing-mark=main

# DHCP Server Configuration - Configure DHCP server on LAN interface
/ip pool add name=dhcp_pool ranges=192.168.88.10-192.168.88.254 comment="DHCP Pool"
/ip dhcp-server add name=dhcp_server interface=LAN address-pool=dhcp_pool lease-time=10m comment="DHCP Server"
/ip dhcp-server network add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=8.8.8.8,8.8.4.4 comment="DHCP Network Settings"

# NAT Configuration - Masquerade for internet access
/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade comment="NAT Masquerade"

# Firewall - Basic security rules (same as in basic setup, adapt as needed)
/ip firewall filter
add chain=forward connection-state=invalid action=drop comment="Drop invalid connections"
add chain=forward connection-state=established,related action=accept comment="Allow established/related"
add chain=forward action=drop comment="Default deny forward chain"
add chain=input action=accept protocol=icmp comment="Allow ICMP"
add chain=input action=drop comment="Default deny input chain"
```

**Configuration on Router 2 (Backup):**

```routeros
# System Identity - Set hostname for Router 2
/system identity set name=Router-2-Backup

# Interface Configuration - Rename interfaces for clarity
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN

# IP Address Configuration - Set IP addresses for Router 2
/ip address add address=192.168.88.3/24 interface=LAN network=192.168.88.0 comment="Router 2 LAN IP"
/ip dhcp-client add interface=WAN disabled=no comment="WAN DHCP Client - Adjust if needed"

# VRRP Configuration - Configure VRRP on LAN interface
/interface vrrp add name=vrrp1 interface=LAN priority=100 virtual-address=192.168.88.1/24 authentication=none preempt=yes sync-connection=yes sync-group=vrrp-group1 comment="VRRP Backup"

# IP Route Configuration - Default route via WAN interface - Adjust gateway if needed
/ip route add dst-address=0.0.0.0/0 gateway=WAN routing-mark=main

# DHCP Server Configuration - **DISABLE DHCP SERVER ON BACKUP ROUTER**
/ip dhcp-server disable dhcp_server comment="Disable DHCP on Backup"

# NAT Configuration - Masquerade for internet access
/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade comment="NAT Masquerade"

# Firewall - Basic security rules (same as in basic setup, adapt as needed)
/ip firewall filter
add chain=forward connection-state=invalid action=drop comment="Drop invalid connections"
add chain=forward connection-state=established,related action=accept comment="Allow established/related"
add chain=forward action=drop comment="Default deny forward chain"
add chain=input action=accept protocol=icmp comment="Allow ICMP"
add chain=input action=drop comment="Default deny input chain"
```

**Important Notes:**

*   **VRRP Router ID (`router-id`):** Must be the **same** on both routers for them to participate in the same VRRP group. It's implicitly set by `sync-group` but good to be aware.
*   **VRRP Priority (`priority`):** Router 1 has a higher priority (110) than Router 2 (100). The router with the highest priority becomes the Master.
*   **VRRP Virtual Address (`virtual-address`):**  Must be the **same** on both routers. This is the VIP that will be used as the default gateway.
*   **VRRP Authentication (`authentication=none`):** For simplicity in SOHO, authentication is set to `none`. For more secure environments, consider using `ah` or `passphrase`.
*   **VRRP Preempt (`preempt=yes`):** If a higher-priority router comes online, it will preempt the current Master and take over.
*   **VRRP Sync Connection & Group (`sync-connection=yes sync-group=vrrp-group1`):**  Enables state synchronization for VRRP. This is crucial for seamless failover, especially for stateful services (though basic SOHO setups might not heavily rely on stateful services in the router itself).
*   **DHCP Server:**  **Crucially, the DHCP server is DISABLED on the Backup router.** Only the Master router should run the DHCP server to avoid IP address conflicts.
*   **NAT and Firewall:** NAT and basic firewall rules are configured on both routers for redundancy. In a failover scenario, the Backup router will take over these functions.

### 3. REST API Implementation (Python Code)

Since RouterOS v6.x does not have a native REST API, we will use the standard RouterOS API (binary protocol) and the `routeros_api` Python library to interact with the routers.

**Python Code for Monitoring VRRP Status:**

```python
import routeros_api
import time

# Router Credentials - Update with your router details
MASTER_ROUTER_IP = '192.168.88.2' # Router 1 IP
BACKUP_ROUTER_IP = '192.168.88.3' # Router 2 IP
USERNAME = 'admin' # Replace with your username
PASSWORD = ''      # Replace with your password

def get_vrrp_status(router_ip):
    try:
        connection = routeros_api.RouterOsApiPool(router_ip, username=USERNAME, password=PASSWORD)
        api = connection.get_api()
        vrrp_interface = api.path('/interface/vrrp').get()

        if not vrrp_interface:
            return "VRRP Interface Not Found"

        vrrp_status = vrrp_interface[0].get('state')
        return vrrp_status

    except routeros_api.exceptions.RouterOsApiError as e:
        return f"Error connecting to {router_ip}: {e}"
    finally:
        if 'connection' in locals() and connection.connected:
            connection.close()

if __name__ == "__main__":
    while True:
        master_status = get_vrrp_status(MASTER_ROUTER_IP)
        backup_status = get_vrrp_status(BACKUP_ROUTER_IP)

        print(f"Master Router ({MASTER_ROUTER_IP}) VRRP Status: {master_status}")
        print(f"Backup Router ({BACKUP_ROUTER_IP}) VRRP Status: {backup_status}")
        print("-" * 30)

        time.sleep(10) # Check status every 10 seconds
```

**Python Code Explanation:**

1.  **Import Libraries:** Imports `routeros_api` for RouterOS API interaction and `time` for pausing between checks.
2.  **Router Credentials:** Defines variables for Master and Backup router IPs, username, and password. **Replace placeholders with your actual credentials.**
3.  **`get_vrrp_status(router_ip)` function:**
    *   Connects to the RouterOS API of the given `router_ip`.
    *   Retrieves VRRP interface information using `/interface/vrrp`.
    *   Extracts the `state` of the VRRP interface (e.g., "master", "backup", "fault").
    *   Handles potential `RouterOsApiError` exceptions (e.g., connection errors).
    *   Closes the API connection in the `finally` block.
4.  **Main Execution Block (`if __name__ == "__main__":`)**
    *   Enters an infinite loop (`while True`).
    *   Calls `get_vrrp_status()` for both Master and Backup routers to get their VRRP states.
    *   Prints the VRRP status for both routers.
    *   Pauses for 10 seconds using `time.sleep(10)`.

**To Run the Python Script:**

1.  **Install `routeros_api`:**
    ```bash
    pip install routeros_api
    ```
2.  **Replace placeholders:** Update `MASTER_ROUTER_IP`, `BACKUP_ROUTER_IP`, `USERNAME`, and `PASSWORD` in the script.
3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

This script will continuously monitor the VRRP status of both routers and print the output to the console, allowing you to observe the HA setup's behavior and detect failovers.

### 4. Common Debugging Scenarios

Here are common debugging scenarios and troubleshooting steps for SOHO VRRP HA setups:

1.  **VRRP Not Becoming Master/Backup as Expected:**
    *   **Check VRRP Configuration:**
        *   Verify `router-id`, `virtual-address`, `priority` settings on both routers. They must be consistent and correctly assigned.
        *   Ensure the VRRP interface is enabled (`/interface vrrp print`).
        *   Check for any configuration errors in `/interface vrrp print detail`.
    *   **Interface Status:**
        *   Verify that the LAN interfaces (`ether2` in our example) are up and running on both routers (`/interface ethernet print`).
        *   Ensure physical cable connections to the switch are good.
    *   **Network Connectivity:**
        *   Ping the real IP addresses of both routers from a PC on the LAN (`192.168.88.2` and `192.168.88.3` in our example).
        *   Ping the Virtual IP address (`192.168.88.1`). It should respond from the Master router.
    *   **Logs:**
        *   Check RouterOS logs for VRRP-related messages on both routers (`/log print topics=vrrp`). Look for errors or warnings.

2.  **Failover Not Occurring When Master Fails:**
    *   **Simulate Master Failure:** Disconnect the WAN interface of the Master router (`ether1`) or power it off to simulate a failure.
    *   **VRRP State Change on Backup:** Observe the VRRP status on the Backup router (`/interface vrrp print`). It should transition to "master" state.
    *   **Connectivity Check:** Verify that devices on the LAN can still access the internet after the simulated failover. Ping external websites or use `traceroute`.
    *   **Log Analysis:** Review logs on both routers during and after the simulated failure for any error messages or issues.

3.  **Split-Brain Scenario (Rare in Basic VRRP, but possible):**
    *   **Definition:** Both routers mistakenly assume they are the Master simultaneously, leading to IP address conflicts and network instability.
    *   **Causes (Less likely in basic VRRP, more common in complex setups):**
        *   Synchronization issues between routers.
        *   Network segmentation or connectivity problems between VRRP peers.
        *   Configuration errors in VRRP or related settings.
    *   **Detection:**
        *   Monitor VRRP status on both routers simultaneously. If both show "master," it indicates a split-brain.
        *   Check logs for VRRP errors related to communication or synchronization.
    *   **Resolution:**
        *   Carefully review VRRP configurations on both routers to ensure consistency.
        *   Verify network connectivity and ensure VRRP peers can communicate correctly.
        *   In basic SOHO VRRP, split-brain is less likely if configurations are simple and network connectivity is stable.

4.  **DHCP Issues After Failover:**
    *   **DHCP Server on Master Only:** Reconfirm that the DHCP server is **disabled** on the Backup router.
    *   **DHCP Lease Time:** Ensure DHCP lease times are not excessively long. Shorter lease times allow for faster IP address updates during failover.
    *   **DHCP Relay (If applicable):** If your SOHO setup involves VLANs or more complex network segments, and you are using DHCP relay, verify relay configurations are correctly set up on both routers. (This is less common in basic SOHO).

**Debugging Tools:**

*   **RouterOS CLI:** Use `/interface vrrp print`, `/log print`, `/ping`, `/traceroute`, `/interface ethernet print` commands for real-time monitoring and troubleshooting.
*   **WinBox/WebFig:**  Graphical interfaces can be helpful for visually inspecting VRRP status, interface states, and configurations.
*   **Python Monitoring Script:** The Python script provided earlier can be adapted to monitor other aspects of the HA setup beyond just VRRP status (e.g., interface link status, routing table changes).

### 5. Version-Specific Considerations (RouterOS v6.x)

*   **VRRP Protocol Version:** RouterOS v6.x primarily uses VRRPv2. Be aware of potential compatibility issues if interacting with systems using VRRPv3 in more complex environments (unlikely in basic SOHO).
*   **VRRP Synchronization:** VRRP synchronization in v6.x is functional for basic state synchronization. However, for very high-stateful applications, consider RouterOS v7.x and its enhanced features (though that's outside the scope of basic SOHO HA). For SOHO, basic VRRP state sync is generally sufficient.
*   **REST API (Limited):** RouterOS v6.x does **not** have a native REST API. You must use the standard RouterOS API (binary protocol) for programmatic access, as demonstrated in the Python example.
*   **Resource Limitations:** SOHO routers often have limited CPU and RAM. Keep the HA configuration simple and avoid overly complex firewall rules or resource-intensive services running directly on the routers to ensure smooth failover performance.

### 6. Security Hardening Measures

*   **Strong Passwords:** Use strong and unique passwords for router administrative accounts (especially `admin`). Change the default password immediately.
*   **Disable Default `admin` User (Optional):** Consider creating a new administrative user with a different username and disabling the default `admin` account for enhanced security.
*   **Limit Management Access:** Restrict access to WinBox, WebFig, SSH, and API to only trusted networks (e.g., the LAN network). Use firewall rules on the `input` chain to achieve this:

    ```routeros
    /ip firewall filter
    add chain=input protocol=tcp dst-port=8291,80,22,8728 src-address-list=LAN_Network action=accept comment="Allow management from LAN"
    add chain=input action=drop comment="Default deny input chain"

    /ip firewall address-list add list=LAN_Network address=192.168.88.0/24 comment="LAN Network Range"
    ```

*   **Disable Unnecessary Services:** Disable any RouterOS services that are not required for your SOHO setup (e.g., unused protocols, unused wireless interfaces if not needed).
*   **Keep RouterOS Updated:** Regularly update RouterOS to the latest stable version within the v6.x branch to patch security vulnerabilities.
*   **VRRP Authentication (Consider):** While we used `authentication=none` for simplicity, for slightly more secure environments (if you are concerned about VRRP spoofing within your LAN), consider using VRRP authentication with `authentication=ah` or `passphrase`. Choose a strong authentication key/passphrase.
*   **Physical Security:** Secure the physical access to the routers to prevent unauthorized tampering.

### 7. Performance Optimization Tips

*   **Use Identical Router Models:** Using identical models simplifies configuration and ensures consistent performance in both Master and Backup roles.
*   **Keep Configurations Lean:** Avoid overly complex configurations, especially in SOHO routers with limited resources. Only enable necessary features and services.
*   **Fast VRRP Transition:**  VRRP transition times are generally fast. You can fine-tune VRRP parameters like `interval` and `dead-interval` (though defaults are usually suitable for SOHO). Be cautious about making these intervals too aggressive as it can lead to instability.
*   **Offload Resource-Intensive Tasks (If Possible):** If you are running resource-intensive services (e.g., advanced firewalling, VPN services) that significantly impact router performance, consider offloading these tasks to dedicated devices if scalability becomes a major concern in the future (though this is less relevant for basic SOHO HA). For basic SOHO, the router's core function is routing and NAT, which VRRP HA handles efficiently.
*   **Monitor Router Resource Usage:** Monitor CPU and memory usage on both routers (`/system resource print`) to ensure they are not overloaded, especially during failover events.

### Special Requirements for SOHO Environments

#### Real-World Deployment Examples

*   **Home Office with Critical Internet Dependency:** For individuals working from home who rely heavily on a stable internet connection for work (video conferencing, remote access, cloud services). HA ensures minimal downtime during router failures, power outages (if routers are on UPS), or ISP issues (if you have dual WAN - beyond basic scope but can be extended).
*   **Small Business with Point-of-Sale Systems:** Small retail businesses using online Point-of-Sale (POS) systems. Internet downtime can directly impact sales. HA provides business continuity for payment processing and online transactions.
*   **SOHO VoIP Systems:** If using VoIP phone systems that rely on a stable network connection, HA can ensure phone service continuity for business communication.
*   **Remote Monitoring/Security Systems:** For SOHO environments with remote monitoring systems (security cameras, IoT devices), HA ensures continuous connectivity for remote access and alerts.

#### Scalability Considerations

*   **SOHO Scale is Limited:** This basic VRRP setup is designed for SOHO scale. It's not intended for large enterprise environments.
*   **Limited Features:** Basic VRRP HA as described focuses on core routing and NAT failover. More advanced features like stateful firewall synchronization or load balancing are not inherently part of this basic setup.
*   **For Larger Scale:** If your needs grow beyond SOHO, consider:
    *   **More Advanced HA Solutions:** Explore RouterOS v7.x features, more complex VRRP configurations, or other HA technologies (though VRRP remains a foundation).
    *   **Dedicated HA Appliances:** For enterprise-level HA, dedicated hardware appliances might be more suitable.
    *   **Load Balancing (Beyond Basic VRRP):** If you need to handle significantly increased traffic and require load distribution, basic VRRP is not inherently a load-balancing solution. You would need to consider more advanced load balancing techniques.

#### Monitoring Configurations

*   **VRRP Status Monitoring (Python Script):** The Python script provided earlier is a basic monitoring example.
*   **RouterOS Logging:** RouterOS logging (`/log`) is essential for monitoring VRRP events and system health. Configure logging to remote syslog server for centralized logging if needed.
*   **SNMP Monitoring (Optional):** RouterOS supports SNMP. You can use SNMP monitoring tools to track router uptime, interface status, CPU/memory usage, and VRRP state. (Requires SNMP server setup).
*   **The Dude (MikroTik Monitoring Tool - v6.x compatible):** MikroTik's The Dude network monitoring application (v6.x compatible) can be used to visually monitor RouterOS devices, including VRRP status, interface states, and other parameters.
*   **Health Check Scripts (Advanced):** For more sophisticated monitoring, you can create RouterOS scripts that perform health checks (e.g., ping external hosts, check interface status, verify routing) and trigger alerts or actions based on the results. (Beyond basic scope).

#### Disaster Recovery Steps

1.  **Regular Configuration Backups (Automated Script - see below):** This is the most crucial step. In case of router failure or misconfiguration, you can restore from a backup.
2.  **Failover Testing:** Periodically test the failover process (e.g., by disconnecting the Master router's WAN interface) to ensure the Backup router takes over correctly and that you understand the failover behavior.
3.  **Hardware Redundancy:** Ensure you have spare routers available for quick replacement in case of hardware failure beyond repair.
4.  **Document Configurations:** Keep detailed documentation of your HA setup configurations, including IP addresses, VRRP settings, passwords, and recovery procedures.
5.  **Power Redundancy (UPS):** Use Uninterruptible Power Supplies (UPS) for both routers and the switch to protect against power outages and ensure graceful shutdowns.
6.  **Manual Failover/Recovery:** If automated failover fails for some reason, understand how to manually initiate failover (e.g., by disabling the VRRP interface on the Master, or adjusting priorities). Know how to manually restore the Master router to service after a failure is resolved.

#### Automated Backup Scripts

**RouterOS Script for Daily Configuration Backup (Save to Router Flash):**

```routeros
# Script Name: daily_config_backup

:local backup_file_name ("backup_" . [:system date format="yyyy-MM-dd_HH-mm-ss"] . ".backup")
:local backup_path ("/disk1/" . $backup_file_name) # Adjust disk name if needed

/system backup save name=$backup_path dont-encrypt=yes

:log info ("Configuration backup saved to: " . $backup_path)

# Optional: You can add commands to export configuration as .rsc as well
# /export file=("config_" . [:system date format="yyyy-MM-dd_HH-mm-ss"] . ".rsc")
# :log info ("Configuration export saved to: config_" . [:system date format="yyyy-MM-dd_HH-mm-ss"] . ".rsc")
```

**Explanation:**

1.  **`daily_config_backup` Script Name:** Assigns a name to the script.
2.  **`backup_file_name` Variable:** Creates a filename based on the current date and time (e.g., `backup_2023-10-27_10-30-00.backup`).
3.  **`backup_path` Variable:** Defines the full path to save the backup file on the router's `disk1` (adjust `/disk1/` if your disk name is different).
4.  **`/system backup save ...` Command:**
    *   `name=$backup_path`: Specifies the full path and filename for the backup.
    *   `dont-encrypt=yes`: Saves the backup unencrypted (for simplicity in SOHO; for higher security, remove `dont-encrypt=yes` to enable encryption with a password – but remember the password!).
5.  **`:log info ...` Command:** Logs a message to the RouterOS log indicating the backup file location.
6.  **Optional RSC Export (Commented Out):** Includes commented-out lines to also export the configuration as a human-readable `.rsc` file.

**To Schedule the Backup Script:**

1.  **Import the script:** Copy and paste the script code into the RouterOS CLI or WinBox Scripting window (`/system script add name=daily_config_backup source=...`).
2.  **Schedule the script to run daily:**
    ```routeros
    /system scheduler add name=daily_backup_scheduler start-time=01:00:00 interval=1d on-event=daily_config_backup policy=write,policy,read,reboot,sensitive,test,winbox,password
    ```
    *   `start-time=01:00:00`: Sets the script to run at 1:00 AM daily.
    *   `interval=1d`: Runs every day (1-day interval).
    *   `on-event=daily_config_backup`: Specifies the script to run.
    *   `policy=...`: Assigns necessary policies for the script to function.

**Important:**

*   **Backup Location:** The script saves backups to the router's local flash storage (`/disk1/`). For better disaster recovery, consider backing up to a **remote location** (e.g., using FTP, SCP, or email – more advanced scripting required).
*   **Backup Encryption:** For sensitive configurations, consider enabling backup encryption by removing `dont-encrypt=yes` and setting a backup password in the `/system backup save` command. **Remember the password!**

This comprehensive documentation provides a solid foundation for implementing a basic VRRP HA solution in a SOHO environment using MikroTik RouterOS v6.x. Remember to thoroughly test your configurations and adapt them to your specific network requirements. Always prioritize security and maintain regular backups for effective disaster recovery.
```

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