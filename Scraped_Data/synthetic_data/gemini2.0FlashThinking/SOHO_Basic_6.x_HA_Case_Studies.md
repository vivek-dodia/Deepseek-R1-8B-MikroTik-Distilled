---
generated_at: 2025-02-03T21:42:14.628249
topic: HA Case Studies
category: High Availability
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

```markdown
## MikroTik RouterOS High Availability (HA) Case Studies for SOHO (Basic) - RouterOS 6.x

**Document Version:** 1.0
**Date:** October 26, 2023
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic
**Author:** [Your Name/Organization] - MikroTik Certified Engineer

---

### 1. Architecture Diagram Requirements

For a basic SOHO HA setup, we will implement an **Active-Passive** architecture using **VRRP (Virtual Router Redundancy Protocol)**. This is a cost-effective and relatively simple solution suitable for environments where minimal downtime is desired, but complex failover scenarios are not critical.

```mermaid
graph LR
    subgraph Internet
        ISP["Internet Service Provider"]
    end

    subgraph SOHO Network
        subgraph Router-A (Primary)
            RA-WAN[WAN Interface (ether1)]
            RA-LAN[LAN Interface (ether2-etherX)]
            RA-VRRP[VRRP Instance]
            RA-Conf["Configuration"]
        end

        subgraph Router-B (Secondary/Backup)
            RB-WAN[WAN Interface (ether1)]
            RB-LAN[LAN Interface (ether2-etherX)]
            RB-VRRP[VRRP Instance (Backup)]
            RB-Conf["Configuration"]
        end

        SW[Switch (LAN)] --> Devices[LAN Devices (PCs, Printers etc.)]
        SW --> RA-LAN
        SW --> RB-LAN

        ISP --> RA-WAN
        ISP --> RB-WAN

        RA-VRRP -- Virtual IP --> SW
        RB-VRRP -. Backup -.-> RA-VRRP

        style RA-VRRP fill:#ccf,stroke:#333,stroke-width:2px
        style RB-VRRP fill:#eee,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5
        style RA-Conf fill:#fff,stroke:#333,stroke-width:1px
        style RB-Conf fill:#fff,stroke:#333,stroke-width:1px

    end

    classDef boxStroke stroke:#333,stroke-width:2px
    class Router-A,Router-B boxStroke
```

**Diagram Explanation:**

* **Active-Passive Setup:** Router-A is the primary (active) router handling all traffic under normal conditions. Router-B is the secondary (passive/backup) router, standing by.
* **VRRP:**  VRRP is used to create a virtual IP address shared between Router-A and Router-B. This virtual IP acts as the default gateway for LAN devices.
* **Virtual IP:**  The virtual IP is configured on the VRRP interface and is initially owned by the primary router (Router-A).
* **Failover:** If Router-A fails, VRRP will detect the failure and transition Router-B to the Master state, taking over the virtual IP and routing responsibilities.
* **WAN & LAN Interfaces:** Each router has a WAN interface connected to the ISP and LAN interfaces connected to the local network switch.
* **Configuration Synchronization (Implicit):** In this basic setup, configuration synchronization is typically manual.  We assume configurations are kept as similar as possible on both routers. More advanced HA solutions in RouterOS (not covered in this basic SOHO document) can automate configuration synchronization.

### 2. CLI Configuration with Inline Comments

This configuration assumes:

* **Router-A:** Primary Router. IP address for management: `192.168.88.10/24`
* **Router-B:** Secondary Router. IP address for management: `192.168.88.11/24`
* **Virtual IP (VRRP IP):** `192.168.88.1`
* **LAN Network:** `192.168.88.0/24`
* **WAN Interface:** `ether1` (connected to ISP modem, DHCP client for WAN IP)
* **LAN Interface:** `ether2` (connected to LAN switch)
* **VRRP Interface:** We will bind VRRP to the LAN interface (`ether2`).

**Configuration on Router-A (Primary):**

```routeros
# --- Interface Configuration ---
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN

# --- IP Address Configuration ---
/ip address add address=192.168.88.10/24 interface=LAN comment="Router-A Management IP"
/ip address add address=192.168.88.1/24 interface=LAN comment="VRRP Virtual IP" # Virtual IP, owned by Primary

# --- DHCP Client on WAN ---
/ip dhcp-client add interface=WAN disabled=no

# --- DHCP Server on LAN ---
/ip pool add name=dhcp_pool_lan ranges=192.168.88.100-192.168.88.200
/ip dhcp-server add name=dhcp_server_lan interface=LAN address-pool=dhcp_pool_lan
/ip dhcp-server network add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=8.8.8.8,8.8.4.4

# --- NAT (Masquerade) ---
/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade

# --- VRRP Configuration ---
/interface vrrp add name=vrrp1 interface=LAN virtual-address=192.168.88.1/24 priority=110 \
    authentication=none preempt=yes comment="VRRP Instance - Primary Router"

# --- Basic Firewall (Same as in Basic Router Config) ---
/ip firewall filter
add chain=input connection-state=invalid action=drop comment="Drop Invalid Connections"
add chain=input connection-state=established,related action=accept comment="Allow Established/Related"
add chain=input in-interface=WAN action=drop comment="Drop New WAN Input"
add chain=forward connection-state=invalid action=drop comment="Drop Invalid Forward"
add chain=forward connection-state=established,related action=accept comment="Allow Established/Related Forward"
add chain=forward src-address=192.168.88.0/24 action=accept comment="Allow LAN to Forward Out"
add chain=forward action=drop comment="Drop All Other Forward"

# --- System Identity for easy identification ---
/system identity set name=Router-A-Primary
```

**Configuration on Router-B (Secondary/Backup):**

```routeros
# --- Interface Configuration ---
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN

# --- IP Address Configuration ---
/ip address add address=192.168.88.11/24 interface=LAN comment="Router-B Management IP"

# --- DHCP Client on WAN ---
/ip dhcp-client add interface=WAN disabled=no

# --- NAT (Masquerade) -  Enabled, but only active when Router-B becomes Master ---
/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade disabled=yes comment="NAT - Disabled until Master"

# --- VRRP Configuration ---
/interface vrrp add name=vrrp1 interface=LAN virtual-address=192.168.88.1/24 priority=100 \
    authentication=none preempt=yes comment="VRRP Instance - Secondary Router (Backup)"

# --- Basic Firewall (Same as in Basic Router Config) ---
/ip firewall filter
add chain=input connection-state=invalid action=drop comment="Drop Invalid Connections"
add chain=input connection-state=established,related action=accept comment="Allow Established/Related"
add chain=input in-interface=WAN action=drop comment="Drop New WAN Input"
add chain=forward connection-state=invalid action=drop comment="Drop Invalid Forward"
add chain=forward connection-state=established,related action=accept comment="Allow Established/Related Forward"
add chain=forward src-address=192.168.88.0/24 action=accept comment="Allow LAN to Forward Out"
add chain=forward action=drop comment="Drop All Other Forward"

# --- System Identity for easy identification ---
/system identity set name=Router-B-Secondary
```

**Key Points in CLI Configuration:**

* **VRRP Priority:** Router-A has a higher priority (110) than Router-B (100), making Router-A the preferred Master.
* **Virtual IP on VRRP Interface:**  The virtual IP `192.168.88.1/24` is configured on the VRRP interface (`vrrp1`) on both routers.
* **Preempt:** `preempt=yes` ensures that if a router with higher priority comes online, it will take over as Master.
* **Authentication:** `authentication=none` is used for simplicity in this basic example. For production environments, consider using `authentication=ah` or `authentication=password` for security.
* **NAT on Secondary Disabled Initially:** NAT on Router-B is disabled (`disabled=yes`). It will be enabled when Router-B becomes Master (see debugging and automation sections).
* **Management IPs:**  Each router has a unique management IP (`192.168.88.10` and `192.168.88.11`) on the LAN network for direct access.

### 3. REST API Implementation (Python Code)

This Python code demonstrates how to use the MikroTik REST API to:

1. **Check VRRP Status:**  Get the state of the VRRP interface (Master or Backup).
2. **Enable/Disable NAT on Router-B:**  This is crucial for failover automation. When Router-B becomes Master, NAT needs to be enabled.

**Prerequisites:**

* Install the `requests` library: `pip install requests`
* Enable REST API on MikroTik Routers: `/ip service enable api-ssl` (or `/ip service enable api` for non-SSL, but SSL is recommended).
* Configure API user with necessary permissions (read for status, write for configuration changes).

```python
import requests
import json

ROUTER_A_IP = "192.168.88.10"
ROUTER_B_IP = "192.168.88.11"
API_USER = "api_user" # Replace with your API username
API_PASSWORD = "api_password" # Replace with your API password

def get_vrrp_status(router_ip):
    """Retrieves VRRP status from a MikroTik router."""
    try:
        response = requests.get(
            f"https://{router_ip}/rest/interface/vrrp",
            auth=(API_USER, API_PASSWORD),
            verify=False # Disable SSL verification for simplicity in SOHO, consider proper certs for production
        )
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        vrrp_data = response.json()
        if vrrp_data: # Check if VRRP interface exists
            return vrrp_data[0]['state'] # Assuming only one VRRP instance 'vrrp1'
        else:
            return "VRRP Interface Not Found"
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {router_ip}: {e}")
        return "Error"

def enable_nat_on_router_b(router_ip):
    """Enables NAT masquerade on Router-B."""
    try:
        response = requests.put(
            f"https://{router_ip}/rest/ip/firewall/nat/0", # Assuming NAT rule is the first one (index 0), adjust if needed
            auth=(API_USER, API_PASSWORD),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({"disabled": "no"}),
            verify=False # Disable SSL verification for simplicity in SOHO, consider proper certs for production
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"NAT enabled successfully on {router_ip}")
        else:
            print(f"Failed to enable NAT on {router_ip}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error enabling NAT on {router_ip}: {e}")


def disable_nat_on_router_b(router_ip):
    """Disables NAT masquerade on Router-B."""
    try:
        response = requests.put(
            f"https://{router_ip}/rest/ip/firewall/nat/0", # Assuming NAT rule is the first one (index 0), adjust if needed
            auth=(API_USER, API_PASSWORD),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({"disabled": "yes"}),
            verify=False # Disable SSL verification for simplicity in SOHO, consider proper certs for production
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"NAT disabled successfully on {router_ip}")
        else:
            print(f"Failed to disable NAT on {router_ip}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error disabling NAT on {router_ip}: {e}")


if __name__ == "__main__":
    # Check VRRP Status
    router_a_status = get_vrrp_status(ROUTER_A_IP)
    router_b_status = get_vrrp_status(ROUTER_B_IP)

    print(f"Router-A VRRP Status: {router_a_status}")
    print(f"Router-B VRRP Status: {router_b_status}")

    # Example: Enable/Disable NAT on Router-B based on VRRP status (Illustrative logic, needs refinement for real automation)
    if router_b_status == "Master":
        enable_nat_on_router_b(ROUTER_B_IP)
    elif router_b_status == "Backup":
        disable_nat_on_router_b(ROUTER_B_IP)
```

**API Code Explanation:**

* **`get_vrrp_status()`:** Sends a GET request to `/rest/interface/vrrp` to retrieve VRRP interface details. Parses the JSON response to extract the `state` (Master/Backup).
* **`enable_nat_on_router_b()` & `disable_nat_on_router_b()`:** Send PUT requests to `/rest/ip/firewall/nat/0` to modify the `disabled` property of the first NAT rule, enabling or disabling NAT.
* **Error Handling:** Basic `try-except` blocks are used to catch `requests.exceptions.RequestException` for connection or HTTP errors.
* **SSL Verification Disabled (`verify=False`):**  For SOHO simplicity, SSL verification is disabled. **For production, obtain and use proper SSL certificates and enable verification.**
* **NAT Rule Index:** The code assumes the NAT masquerade rule is the first rule (`/rest/ip/firewall/nat/0`).  **Verify the actual index of your NAT rule and adjust the code accordingly.**

**Automation Considerations:**

* **Failover Script:** This Python code can be extended to create a more robust failover script.  The script would periodically check the VRRP status of Router-A. If Router-A becomes Backup (indicating a failure), the script could then trigger actions on Router-B to fully take over (e.g., enable NAT, potentially adjust other services).
* **External Monitoring System:** Integrate this API code with an external monitoring system (like Zabbix, Prometheus, or even a simple cron job on a server) to continuously monitor VRRP status and trigger automated actions.

### 4. Common Debugging Scenarios

**Scenario 1: VRRP Not Becoming Master/Backup Correctly**

* **Problem:** Routers are not transitioning to Master/Backup states as expected.
* **Troubleshooting Steps:**
    1. **Check VRRP Interface Status:**
        ```routeros
        /interface vrrp print detail
        ```
        Examine the `state`, `master-router`, `backup-router`, `priority`, `virtual-address`, and `last-state-change` fields.
    2. **Verify Physical Connectivity:** Ensure both routers are connected to the LAN switch and the WAN modem correctly. Check Ethernet cable integrity.
    3. **Firewall Issues:**  Although unlikely in a basic setup, ensure firewall rules are not blocking VRRP traffic (VRRP uses IP protocol 112).  Temporarily disable firewall filters for testing (with caution in a live network).
    4. **Priority Misconfiguration:** Double-check that Router-A has a higher priority than Router-B.
    5. **VRRP Authentication Mismatch:** If authentication is enabled (not in our basic example), ensure the authentication type and key match on both routers.
    6. **Log Analysis:** Check the RouterOS logs (`/log print`) for VRRP-related messages. Look for errors or warnings during VRRP initialization and state transitions.

**Scenario 2: Failover Occurs, but Internet Connectivity is Lost**

* **Problem:** VRRP failover happens, Router-B becomes Master, but LAN devices lose internet access.
* **Troubleshooting Steps:**
    1. **NAT on Router-B Not Enabled:**  Verify that NAT masquerade is enabled on Router-B after failover. Check using CLI (`/ip firewall nat print`) or the API script. If using automation, ensure the NAT enabling script is working correctly.
    2. **WAN Interface on Router-B Not Getting IP:** Check if Router-B's WAN interface (`ether1`) is receiving an IP address from the ISP modem via DHCP (`/ip dhcp-client print`). If not, check modem connectivity and DHCP client configuration.
    3. **Routing Issues:** In a basic SOHO setup, routing is simple (default route via WAN).  However, if you have more complex routing, verify the routing configuration on Router-B is correct after failover.
    4. **ISP Modem Issues:** Sometimes, the ISP modem might have issues with MAC address changes during failover.  Try power-cycling the ISP modem after failover to see if it resolves the connection issue.

**Scenario 3: Split-Brain Scenario (Rare in Basic VRRP)**

* **Problem:** Both Router-A and Router-B might incorrectly become Master simultaneously. This is less common in basic VRRP but can happen in more complex scenarios (e.g., network segmentation issues, VRRP configuration errors).
* **Troubleshooting Steps:**
    1. **Network Segmentation:** Ensure the LAN network is not segmented in a way that prevents VRRP communication between Router-A and Router-B on the LAN.
    2. **VRRP Configuration Errors:** Double-check the VRRP configurations on both routers for any inconsistencies or errors.
    3. **Link Monitoring (Advanced, Not in Basic):**  More advanced HA setups might use link monitoring to track interface status more robustly.  Basic VRRP relies primarily on VRRP hello packets.

**CLI Commands for Debugging:**

* `/interface vrrp print detail` - Detailed VRRP interface status.
* `/log print topics=vrrp` - View VRRP-specific log messages.
* `/ip route print` - Check routing table.
* `/ip dhcp-client print` - DHCP client status.
* `/ip firewall nat print` - NAT rule configuration.
* `/ping <virtual-ip>` - Ping the virtual IP from both routers to check VRRP reachability.
* `/tool sniffer quick interface=LAN protocol=vrrp` - Capture VRRP packets on the LAN interface to analyze VRRP communication (for advanced debugging).

### 5. Version-Specific Considerations (RouterOS 6.x)

* **VRRP Protocol Version:** RouterOS 6.x typically uses VRRPv2.  Be aware of VRRPv2 limitations compared to VRRPv3 (not a major concern for basic SOHO).
* **Configuration Synchronization:** RouterOS 6.x in basic HA setups usually relies on manual configuration synchronization.  RouterOS 7 introduces more advanced configuration synchronization tools within RouterOS itself (like configuration templates and scripting), but for version 6.x, external tools or manual processes are common for keeping configurations consistent.
* **API Features:** The REST API in RouterOS 6.x is functional but might have fewer features and refinements compared to later versions. The API examples provided are compatible with RouterOS 6.x REST API.
* **Resource Limits:** SOHO routers running RouterOS 6.x might have limited resources (CPU, memory).  For very high traffic SOHO environments, ensure the chosen MikroTik hardware is sufficient.

**Comparison Table: RouterOS 6.x vs. Newer Versions (HA Features)**

| Feature                      | RouterOS 6.x (Basic HA) | RouterOS 7+ (Advanced HA) |
|------------------------------|---------------------------|---------------------------|
| VRRP Protocol Version        | VRRPv2 (typically)        | VRRPv3 (typically)        |
| Configuration Synchronization | Manual (or external tools)| Built-in tools, scripting |
| API Features                 | Functional, less feature-rich | More feature-rich, robust |
| HA Automation Complexity     | Requires external scripting | More built-in automation options |
| Advanced HA Features         | Limited to basic VRRP     | BFD, more granular failover triggers, advanced scripting |

**Note:** While RouterOS 6.x is functional for basic HA, upgrading to a newer RouterOS version (if hardware allows) can provide access to improved HA features and management capabilities in the long run. However, for many basic SOHO needs, RouterOS 6.x with VRRP is sufficient.

### 6. Security Hardening Measures

* **Strong Passwords:** Use strong, unique passwords for the `admin` user and any API users. Change default passwords immediately after setup.
* **Disable Default User (Optional):** Consider disabling the default `admin` user and creating a new administrative user with a different username.
* **Secure API Access:**
    * **Use HTTPS (API-SSL):** Always enable API-SSL for encrypted API communication.
    * **Restrict API Access Source:** Use firewall rules to restrict API access to only trusted IP addresses or networks (e.g., your management network).
    * **Role-Based Access Control (RBAC):**  Create API users with minimal necessary privileges.  Avoid giving API users full `admin` rights unless absolutely required.
* **Firewall Protection (Already in Basic Config):** The basic firewall rules provided are a good starting point.  Review and customize them based on your specific security needs.
* **Keep RouterOS Updated:** Regularly update RouterOS to the latest stable version to patch security vulnerabilities. Subscribe to MikroTik security advisories.
* **Disable Unnecessary Services:** Disable any RouterOS services that are not required (e.g., if you are not using FTP, disable the FTP service).
* **SSH Hardening:** If using SSH for management, consider:
    * Changing the default SSH port.
    * Using key-based authentication instead of passwords.
    * Limiting SSH access to trusted IP addresses.
* **Physical Security:** Secure the physical access to your MikroTik routers to prevent unauthorized tampering.

### 7. Performance Optimization Tips

For a basic SOHO HA setup, performance optimization is usually not a primary concern unless the SOHO network handles very high traffic volumes. However, here are some general tips:

* **Hardware Selection:** Choose MikroTik routers with sufficient CPU and memory for your expected traffic load. For basic SOHO, even entry-level MikroTik routers are often adequate.
* **Minimize CPU-Intensive Features:** Avoid enabling unnecessary CPU-intensive features if performance is critical (e.g., complex firewall rules, excessive logging, very deep packet inspection if not needed). The basic firewall rules provided are efficient.
* **FastTrack:** RouterOS FastTrack can significantly improve throughput for established connections. Ensure FastTrack is enabled in your firewall configuration (it is often enabled by default).
* **Interface Configuration:** Ensure interfaces are configured with appropriate MTU (Maximum Transmission Unit) and are running at the correct link speed.
* **VRRP Keepalive and Dead Interval (Advanced):**  For very specific high-performance scenarios, you *could* adjust VRRP keepalive and dead intervals, but for most SOHO setups, the default values are sufficient and reliable.  **Changing these values without careful consideration can lead to instability.**
* **Monitoring Bandwidth Usage:** Use MikroTik's built-in monitoring tools (`/tool profile`, `/interface ethernet monitor-traffic`) to monitor CPU usage and interface traffic to identify any bottlenecks.
* **Regular Configuration Backups:** While not directly performance-related, regular backups are crucial for disaster recovery and can save time in case of configuration issues, indirectly contributing to network uptime and perceived performance.

### SOHO Specific Requirements

#### Real-world Deployment Examples

1. **Home Office Redundancy:** A home office professional working from home relies heavily on internet connectivity for remote work, video conferencing, and cloud services. An HA setup ensures that if the primary router fails, internet access is quickly restored via the backup router, minimizing disruption to work.

2. **Small Business Continuous Internet Access:** A small retail store or cafe relies on internet for point-of-sale systems, customer Wi-Fi, and online ordering. HA ensures that internet connectivity is maintained for business continuity, preventing loss of sales and customer dissatisfaction due to internet outages.

3. **Small Branch Office Connectivity:** A small branch office of a larger company needs reliable internet access for employees to connect to corporate resources and cloud applications. HA provides redundancy to ensure branch office productivity is not impacted by router failures.

#### Scalability Considerations

* **Basic SOHO HA is Limited:** The basic active-passive VRRP setup described is suitable for SOHO environments with relatively simple network requirements and moderate traffic.
* **Not Designed for Large Scale:** This basic setup is not designed for large enterprise networks or environments requiring very high availability, load balancing, or complex failover scenarios.
* **Scalability Bottlenecks:** Scalability limitations primarily come from:
    * **Manual Configuration Sync:**  Configurations need to be manually kept in sync, which becomes cumbersome for larger, more complex networks.
    * **Single Active Router:** Only one router is actively handling traffic at a time.  It does not provide load balancing or increased aggregate bandwidth.
    * **Basic VRRP Limitations:** VRRPv2 itself has limitations in very large or complex networks compared to more advanced HA protocols.

* **For Higher Scalability:** For larger or more demanding networks, consider:
    * **RouterOS 7+ Advanced HA Features:** Explore RouterOS 7's features like configuration templates, scripting for automation, and potentially more advanced HA mechanisms beyond basic VRRP.
    * **Clustering Solutions:** For very high availability and scalability, consider more advanced clustering solutions that might involve multiple active routers and load balancing (beyond the scope of basic SOHO HA).
    * **Hardware Redundancy:** In larger setups, consider redundant power supplies, network interfaces, and even chassis redundancy in the hardware infrastructure itself.

#### Monitoring Configurations

**Basic Monitoring using RouterOS Tools:**

1. **VRRP Status Monitoring (CLI):**
   ```routeros
   /interface vrrp print status
   ```
   This command shows the current status of the VRRP interface (Master, Backup, etc.). You can run this periodically using RouterOS scripting and logging.

2. **Interface Status Monitoring (CLI):**
   ```routeros
   /interface ethernet monitor ether1 once
   ```
   Monitor the status of WAN and LAN interfaces to detect link down events.

3. **Logging VRRP State Changes:** RouterOS automatically logs VRRP state changes to the system log. Review the logs regularly (`/log print topics=vrrp`). Configure log actions (e.g., email notifications) for critical events.

4. **Simple Script for VRRP Status Check and Logging:**
   ```routeros
   /system script add name=vrrp_status_check owner=admin policy=read,write,policy,test-script,password,sensitive,romon source={
       :local vrrp_status [/interface vrrp get vrrp1 state]
       /log info message=("VRRP Status: " . $vrrp_status)
   }
   /system scheduler add name=check_vrrp interval=1m on-event=vrrp_status_check start-time=startup
   ```
   This script checks VRRP status every minute and logs it. You can extend this to send email notifications if the status changes from Master to Backup.

**External Monitoring (Recommended for Production):**

* **SNMP Monitoring:** Configure SNMP on MikroTik routers and use an external SNMP monitoring system (like Zabbix, PRTG, LibreNMS) to monitor VRRP status, interface states, CPU/memory usage, and other relevant metrics.
* **API-Based Monitoring:**  Use the REST API and the Python code examples to build a more sophisticated monitoring system or integrate with existing monitoring platforms.

#### Disaster Recovery Steps

**Failover Scenario (Router-A Failure):**

1. **Automatic Failover:** VRRP will automatically detect the failure of Router-A (primary) if it stops sending VRRP hello packets.
2. **Router-B Takes Over:** Router-B (secondary) will transition to the Master state and take over the virtual IP address (`192.168.88.1`).
3. **LAN Devices Continue Connectivity:** LAN devices, still configured to use `192.168.88.1` as their default gateway, will now route traffic through Router-B.
4. **NAT Enabled on Router-B (If Automated):** If you have automated NAT enabling on Router-B via API or scripting, NAT will be enabled, and LAN devices regain internet access. If manual, you need to manually enable NAT on Router-B.

**Recovery Steps (After Router-A Failure):**

1. **Diagnose and Repair Router-A:** Investigate the cause of Router-A's failure (hardware issue, software problem, etc.) and repair or replace it.
2. **Restore Router-A Configuration (If Necessary):** If Router-A was replaced or its configuration was lost, restore its configuration from a backup. Ensure it is configured as the primary router again (higher VRRP priority).
3. **Reintegrate Router-A:** Once Router-A is repaired and configured, power it on and connect it back to the network.
4. **Preemption (Automatic Take Back):** Because `preempt=yes` is enabled in VRRP, Router-A, with its higher priority, will automatically preempt Router-B and become Master again. Router-B will revert to Backup state.
5. **Verify Normal Operation:** Monitor VRRP status and network connectivity to ensure Router-A is now the Master and everything is functioning correctly.

**Manual Failback (If Preemption is Disabled or Desired):**

If you have disabled `preempt=yes` or prefer manual failback, you can manually trigger failback:

1. **On Router-B (Secondary - Master):**
   ```routeros
   /interface vrrp set vrrp1 priority=90 # Reduce priority of Router-B
   ```
   Lowering Router-B's priority will cause Router-A (if online and configured correctly) to take over as Master.

2. **Verify Failback:** Check VRRP status on both routers to confirm Router-A is Master and Router-B is Backup.

#### Automated Backup Scripts

**RouterOS Script for Local Configuration Backup:**

```routeros
/system script add name=backup_config owner=admin policy=read,write,policy,test-script,password,sensitive,romon source={
    :local backup_file_name ("config_backup_" . [/system clock get date format=yyyy-MM-dd] . "_" . [/system clock get time format=HH-mm-ss] . ".backup")
    /system backup save name=$backup_file_name
    /log info message=("Configuration backup saved to: " . $backup_file_name)
}
/system scheduler add name=daily_config_backup interval=1d start-time=03:00:00 on-event=backup_config
```

**Explanation:**

* This script creates a configuration backup file with a timestamped filename (e.g., `config_backup_2023-10-26_03-00-00.backup`).
* It uses `/system backup save` to save the backup to the router's local storage.
* A scheduler is set up to run this script daily at 3:00 AM.

**Python Script to Download Backups (Example - Needs Further Development for Robustness):**

```python
import requests
import os

ROUTER_A_IP = "192.168.88.10"
API_USER = "api_user"
API_PASSWORD = "api_password"
BACKUP_DIRECTORY = "mikrotik_backups" # Directory to save backups locally

def download_latest_backup(router_ip):
    """Downloads the latest configuration backup from a MikroTik router."""
    try:
        response = requests.get(
            f"https://{router_ip}/rest/file", # List files
            auth=(API_USER, API_PASSWORD),
            verify=False
        )
        response.raise_for_status()
        files_data = response.json()
        backup_files = [f['name'] for f in files_data if f['name'].endswith(".backup") and f['type'] == 'file']
        if not backup_files:
            print(f"No backup files found on {router_ip}")
            return

        latest_backup_file = sorted(backup_files)[-1] # Get the latest backup file (assuming filename sorting works by date)
        print(f"Downloading latest backup file: {latest_backup_file} from {router_ip}")

        download_response = requests.get(
            f"https://{router_ip}/rest/file/{latest_backup_file}", # Download specific file
            auth=(API_USER, API_PASSWORD),
            verify=False,
            stream=True # Stream download for large files
        )
        download_response.raise_for_status()

        os.makedirs(BACKUP_DIRECTORY, exist_ok=True) # Create backup directory if it doesn't exist
        local_backup_path = os.path.join(BACKUP_DIRECTORY, latest_backup_file)
        with open(local_backup_path, 'wb') as f:
            for chunk in download_response.iter_content(chunk_size=8192): # Download in chunks
                f.write(chunk)
        print(f"Backup saved to: {local_backup_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading backup from {router_ip}: {e}")

if __name__ == "__main__":
    download_latest_backup(ROUTER_A_IP)
    download_latest_backup(ROUTER_B_IP) # Download backups from both routers
```

**Explanation:**

* This Python script uses the API to:
    1. List files on the MikroTik router (`/rest/file`).
    2. Filter for `.backup` files.
    3. Sort backup files (assuming filename sorting is chronological) and get the latest one.
    4. Download the latest backup file (`/rest/file/{filename}`) and save it to a local directory (`mikrotik_backups`).

**Important Notes on Backups:**

* **Security:** Securely store backup files. Backups contain sensitive configuration data.
* **Offsite Backups:** For better disaster recovery, store backups offsite (e.g., on a network share, cloud storage, or using a dedicated backup server). The provided Python script is a basic example; for production, consider using more robust backup solutions.
* **Testing Backups:** Regularly test restoring configurations from backups to ensure the backup process is working correctly and that you can recover your configuration in case of a router failure.

---

This documentation provides a comprehensive guide to implementing basic HA for SOHO environments using MikroTik RouterOS 6.x. Remember to adapt the configurations and scripts to your specific network environment and security requirements. For more advanced HA scenarios and larger networks, consider exploring RouterOS 7+ features and more sophisticated HA solutions.
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