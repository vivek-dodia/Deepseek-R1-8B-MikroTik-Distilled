---
generated_at: 2025-02-03T21:05:18.739138
topic: IP Routing
category: Core Networking
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS IP Routing Documentation (v6.x - SOHO)

**Document Version:** 1.0
**Author:** [Your Name/MikroTik Certified Engineer]
**Date:** October 26, 2023
**Target Audience:** SOHO Network Administrators, MikroTik Users
**RouterOS Version:** 6.x
**Complexity Level:** Basic
**Topic:** IP Routing

---

**1. Introduction to IP Routing in MikroTik RouterOS (SOHO)**

This document provides a basic guide to IP routing in MikroTik RouterOS version 6.x, specifically tailored for Small Office/Home Office (SOHO) environments.  It covers essential routing configurations, debugging techniques, security considerations, and practical examples for typical SOHO setups.

**2. Architecture Diagram Requirements**

For basic SOHO IP routing, the network architecture diagram should clearly illustrate:

*   **MikroTik Router:** Central device performing routing functions.
*   **WAN Interface:** Interface connecting to the Internet (e.g., `ether1`, `pppoe-out1`).
*   **LAN Interface:** Interface(s) connecting to the local network (e.g., `ether2`, `bridge1`).
*   **IP Address Ranges:**  Subnets used for WAN and LAN interfaces.
*   **Default Gateway:**  The next-hop IP address for reaching networks outside the LAN.
*   **Connected Devices:**  Simplified representation of computers, printers, and other devices on the LAN.

**Example Diagram (Mermaid Syntax):**

```mermaid
graph LR
    subgraph Internet
        A[Internet Cloud]
    end
    subgraph MikroTik Router (RouterOS v6.x)
        B[ether1 (WAN)] --> C(RouterOS Routing Engine);
        C --> D[ether2 (LAN)];
    end
    subgraph Local Network (LAN - 192.168.88.0/24)
        D --> E[PC 1];
        D --> F[PC 2];
        D --> G[Printer];
        D --> H[Wi-Fi AP];
    end
    A --> B;

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#eee,stroke:#333,stroke-width:2px
    style F fill:#eee,stroke:#333,stroke-width:2px
    style G fill:#eee,stroke:#333,stroke-width:2px
    style H fill:#eee,stroke:#333,stroke-width:2px

    direction LR
    WANInterface[ether1 (WAN) - Public IP] --> B
    LANInterface[ether2 (LAN) - 192.168.88.1/24] --> D
    RouterCore[RouterOS Routing Engine] --> C
    LocalDevices[Local Network Devices] --> D

    linkStyle 0,1,2,3,4,5,6,7,8 stroke:#333,stroke-width:1px;
```

**3. CLI Configuration with Inline Comments**

This section demonstrates basic IP routing configuration using the MikroTik CLI.

```routeros
# --- Interface Configuration ---
/interface ethernet
set [ find name=ether1 ] name=ether1-wan comment="WAN Interface - Connects to Internet"
set [ find name=ether2 ] name=ether2-lan comment="LAN Interface - Connects to Local Network"

# --- IP Address Configuration ---
/ip address
# WAN Interface (Assuming DHCP Client for dynamic IP from ISP)
add interface=ether1-wan address=0.0.0.0/0 comment="WAN IP - DHCP Client will assign IP" disabled=no
/ip dhcp-client
add interface=ether1-wan disabled=no

# LAN Interface (Static IP for internal network)
add interface=ether2-lan address=192.168.88.1/24 network=192.168.88.0 comment="LAN IP - Gateway for local network" disabled=no

# --- Default Route Configuration ---
/ip route
# Default route to the Internet via the WAN interface
add gateway=ether1-wan distance=1 comment="Default Route to Internet via WAN"

# --- Enable NAT Masquerade for Internet Access from LAN ---
/ip firewall nat
add chain=srcnat out-interface=ether1-wan action=masquerade comment="NAT for LAN to Internet"

# --- Optional: DNS Configuration (If not provided by DHCP from ISP) ---
/ip dns
set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes

# --- Optional: DHCP Server Configuration for LAN Clients ---
/ip pool
add name=dhcp_pool_lan ranges=192.168.88.10-192.168.88.254 comment="DHCP Pool for LAN"
/ip dhcp-server
add name=dhcp_server_lan interface=ether2-lan address-pool=dhcp_pool_lan lease-time=10m disabled=no
/ip dhcp-server network
add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1 comment="DHCP Network for LAN"
```

**Explanation:**

*   **Interface Configuration:** Renames interfaces for clarity.
*   **IP Address Configuration:**
    *   **WAN:** Configured for DHCP client to automatically obtain an IP address from the ISP.
    *   **LAN:** Assigned a static IP address (`192.168.88.1/24`) which acts as the default gateway for the LAN network (`192.168.88.0/24`).
*   **Default Route:** Creates a default route (`0.0.0.0/0`) pointing to the WAN interface (`ether1-wan`) as the gateway. This ensures traffic destined for networks outside the LAN is routed to the Internet.
*   **NAT Masquerade:** Enables Network Address Translation (NAT) using masquerade. This allows devices on the private LAN network to access the Internet using the public IP address of the WAN interface.
*   **DNS Configuration (Optional):** Sets Google Public DNS servers as primary and secondary DNS. `allow-remote-requests=yes` is generally needed for SOHO setups, but consider security implications (see Security Hardening section).
*   **DHCP Server Configuration (Optional):** Configures a DHCP server on the LAN interface to automatically assign IP addresses to devices on the `192.168.88.0/24` network.

**4. REST API Implementation (Python)**

This Python script demonstrates configuring basic routing elements using the MikroTik RouterOS REST API.

```python
import requests
import json

ROUTER_IP = "your_router_ip"  # Replace with your MikroTik router IP
USERNAME = "your_username"      # Replace with your MikroTik username
PASSWORD = "your_password"      # Replace with your MikroTik password

BASE_URL = f"https://{ROUTER_IP}/rest"  # Use HTTPS for security
AUTH = (USERNAME, PASSWORD)
HEADERS = {'content-type': 'application/json'}
VERIFY_SSL = False # Set to True for production with valid SSL certificate

def configure_routing():
    try:
        # 1. Configure Interfaces (Example: Rename ether1 and ether2 - assuming they exist)
        interface_data = [
            {".id": "*1", "name": "ether1-wan", "comment": "WAN Interface - API Configured"}, # Assuming *1 is ether1's ID - adjust as needed
            {"name": "ether2-lan", "comment": "LAN Interface - API Configured"}
        ]
        for data in interface_data:
            response = requests.put(f"{BASE_URL}/interface/ethernet/{data.get('.id', '') if '.id' in data else ''}",
                                    auth=AUTH, headers=HEADERS, json=data, verify=VERIFY_SSL)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            print(f"Interface configuration updated: {data.get('name', 'unknown')}")


        # 2. Configure LAN IP Address
        lan_ip_data = {"interface": "ether2-lan", "address": "192.168.88.1/24", "network": "192.168.88.0", "comment": "LAN IP - API Configured"}
        response = requests.post(f"{BASE_URL}/ip/address", auth=AUTH, headers=HEADERS, json=lan_ip_data, verify=VERIFY_SSL)
        response.raise_for_status()
        print(f"LAN IP address configured: {lan_ip_data['address']}")

        # 3. Configure Default Route
        default_route_data = {"gateway": "ether1-wan", "distance": 1, "comment": "Default Route - API Configured"}
        response = requests.post(f"{BASE_URL}/ip/route", auth=AUTH, headers=HEADERS, json=default_route_data, verify=VERIFY_SSL)
        response.raise_for_status()
        print(f"Default route configured: {default_route_data['gateway']}")

        # 4. Enable NAT Masquerade
        nat_data = {"chain": "srcnat", "out-interface": "ether1-wan", "action": "masquerade", "comment": "NAT - API Configured"}
        response = requests.post(f"{BASE_URL}/ip/firewall/nat", auth=AUTH, headers=HEADERS, json=nat_data, verify=VERIFY_SSL)
        response.raise_for_status()
        print("NAT masquerade configured.")

        print("Basic routing configuration completed via API.")

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    configure_routing()
```

**Explanation:**

*   **Dependencies:** Requires the `requests` library (`pip install requests`).
*   **Credentials:**  Replace placeholders for `ROUTER_IP`, `USERNAME`, and `PASSWORD`.
*   **HTTPS and SSL:** Uses HTTPS for secure communication. `VERIFY_SSL=False` disables SSL certificate verification, **not recommended for production**. For production, set `VERIFY_SSL=True` and ensure your router has a valid SSL certificate.
*   **API Endpoints:** Uses `/rest` API endpoints for interface, IP address, route, and firewall NAT configuration.
*   **JSON Data:** Sends configuration data in JSON format as required by the RouterOS REST API.
*   **Error Handling:** Includes `try-except` blocks to catch potential errors during API requests and print informative error messages.
*   **Interface ID:** In the interface update example, `".id": "*1"` is used to identify the interface to update. You might need to fetch interface IDs first using a GET request to `/rest/interface/ethernet` if you are not sure of the ID.

**5. Common Debugging Scenarios**

Here are common routing issues in SOHO environments and debugging steps:

| Scenario                                 | Possible Cause(s)                                    | Debugging Steps                                                                 | CLI Tools                                  |
| :--------------------------------------- | :---------------------------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------------- |
| **No Internet Access from LAN**            | 1.  No Default Route                                  | 1.  Check if a default route exists: `/ip route print`                            | `/ip route print`                          |
|                                          | 2.  Incorrect Default Route Gateway                    | 2.  Verify the default route's gateway points to the correct WAN interface.      | `/ip route print`                          |
|                                          | 3.  NAT Masquerade not configured                      | 3.  Check if NAT masquerade rule is enabled: `/ip firewall nat print`          | `/ip firewall nat print`                  |
|                                          | 4.  Firewall blocking outbound traffic                 | 4.  Review firewall filter rules, especially `forward` chain: `/ip firewall filter print` | `/ip firewall filter print`                |
|                                          | 5.  WAN interface not getting IP from ISP (DHCP issue) | 5.  Check DHCP client status on WAN interface: `/ip dhcp-client print`        | `/ip dhcp-client print`, `/interface print` |
| **Slow Internet Speed**                   | 1.  Incorrect DNS settings                             | 1.  Check DNS server configuration: `/ip dns print`                               | `/ip dns print`                             |
|                                          | 2.  Network congestion (less likely in basic SOHO)    | 2.  Monitor interface traffic: `/interface monitor-traffic ether1-wan interval=5s` | `/interface monitor-traffic`              |
|                                          | 3.  ISP issue                                       | 3.  Test internet speed directly from the router (e.g., using `tool speed-test`). | `/tool speed-test`                        |
| **Cannot access specific websites/services** | 1.  DNS resolution issue                             | 1.  Try pinging website IP address directly (e.g., `ping 8.8.8.8`).               | `ping`                                     |
|                                          | 2.  Firewall blocking specific ports/protocols         | 2.  Review firewall filter rules, especially `forward` chain.                   | `/ip firewall filter print`                |
|                                          | 3.  Website/service issue                             | 3.  Test from another network or device.                                         | N/A                                        |
| **Local Network connectivity issues**     | 1.  Incorrect LAN IP configuration                     | 1.  Verify LAN interface IP address and network: `/ip address print`              | `/ip address print`                         |
|                                          | 2.  DHCP server issues (if used)                       | 2.  Check DHCP server leases: `/ip dhcp-server lease print`                     | `/ip dhcp-server lease print`               |
|                                          | 3.  IP address conflicts                               | 3.  Check for duplicate IP addresses on the LAN.                                  | N/A (manual inspection)                     |

**6. Version-Specific Considerations (RouterOS v6.x)**

*   **Feature Stability:** RouterOS v6.x is a mature and stable version. Basic IP routing features are well-established.
*   **Security Updates:** Check MikroTik's website for any security advisories or critical updates for v6.x, even though it's not the latest version.
*   **REST API:** The REST API in v6.x might have slightly fewer features or different syntax compared to newer versions. Refer to the RouterOS v6.x documentation for API specifics.
*   **Hardware Compatibility:** Ensure your MikroTik hardware is compatible with v6.x if you are deploying on older devices.
*   **Migration Path:** If you are planning for future upgrades, consider the migration path from v6.x to newer versions (v7 or later) as there might be configuration changes required.

**7. Security Hardening Measures for SOHO Routing**

*   **Firewall Rules:** Implement a robust firewall policy:
    *   **Default Deny:**  Set a default deny rule for the `forward` chain to drop all traffic that doesn't explicitly match allow rules.
    *   **Allow Established/Related:** Allow established and related connections to permit return traffic for initiated connections.
    *   **Control Inbound Access:**  Carefully control inbound access from the WAN. Only open ports that are absolutely necessary for services you intend to expose to the internet (e.g., VPN, web server - if any in a SOHO context, which is usually not recommended).
    *   **Limit LAN to WAN:**  Restrict outbound traffic from LAN to WAN if possible (though in SOHO, typically LAN devices need unrestricted internet access).
    *   **Inter-VLAN Firewall (if using VLANs):**  If you use VLANs, implement firewall rules to control traffic between VLANs for segmentation.
*   **Disable Unnecessary Services:** Disable services you don't need (e.g., Telnet, FTP, API if not used remotely - access API over VPN or local network only). `/ip service disable telnet,ftp,api`
*   **Strong Passwords:** Use strong and unique passwords for the `admin` account and any other user accounts. Change the default password immediately.
*   **Remote Access Security:** If remote access is required, use secure methods like SSH or HTTPS for Winbox/WebFig. Consider using VPN for more secure remote management. Avoid exposing management interfaces directly to the internet if possible.
*   **Regular Updates:** Although v6.x is older, check for and apply any critical security updates released by MikroTik for v6.x. Consider upgrading to a newer stable version if possible for better security and features in the long run.
*   **DNS Security:** Consider using secure DNS resolvers (like Cloudflare DNS 1.1.1.1 or Google Public DNS 8.8.8.8) and disable `allow-remote-requests` for the internal DNS server unless you have a specific need for it. If enabled, consider firewall rules to limit access to the DNS service.
*   **UPnP/Port Forwarding:** Use UPnP (Universal Plug and Play) and port forwarding cautiously. UPnP can introduce security risks if not managed properly. Only enable it if required for specific applications and understand the implications of opening ports.  Prefer manual port forwarding over UPnP if possible for better control.

**8. Performance Optimization Tips for SOHO Routing**

*   **FastTrack:** Enable FastTrack connection tracking for improved throughput. FastTrack bypasses some firewall processing for established connections, significantly increasing speed for common internet traffic. `/ip firewall filter add chain=forward action=fasttrack-connection connection-state=established,related` (Place this rule early in the `forward` chain).
*   **Keep Firewall Rules Simple:**  For basic SOHO setups, keep firewall ruleset relatively simple. Too many complex rules can slightly impact performance.
*   **Hardware Resources:** Ensure your MikroTik router hardware is sufficient for your SOHO needs. For very basic setups, even entry-level MikroTik routers are usually adequate. However, for higher bandwidth internet connections or more demanding routing tasks, consider routers with more powerful CPUs and RAM.
*   **Avoid Unnecessary Features:** Disable or avoid using features that you don't actively need, as some features might consume router resources.
*   **Regular RouterOS Updates:** While on v6.x, ensure you have applied the latest stable release within the v6.x branch for potential performance improvements and bug fixes.  For long-term performance and features, planning an upgrade to a newer RouterOS version might be beneficial eventually.
*   **Queueing (Traffic Shaping):** For basic SOHO, usually, simple queueing is not necessary. However, if you experience bandwidth contention or want to prioritize certain types of traffic, you can explore simple queueing strategies in RouterOS.  Avoid overly complex queue setups unless you have a clear understanding and need for them.

**9. SOHO Real-World Deployment Examples**

*   **Home Internet Sharing:** The most common SOHO scenario. Router connects to ISP via WAN, provides internet access to devices on the LAN (computers, smartphones, smart TVs, etc.) using NAT.  Configuration as shown in CLI example above is sufficient.
*   **Home Office with Remote Access:**  SOHO environment where users need to access the home network remotely (e.g., files, devices).  In addition to basic routing, configure a VPN server (e.g., PPTP, L2TP/IPsec, WireGuard) on the MikroTik router for secure remote access.
*   **Small Business with Guest Wi-Fi:**  Small business needs to provide internet access for employees and separate guest Wi-Fi.  Implement VLANs to separate employee and guest networks logically. Configure separate DHCP servers and firewall rules for each VLAN.  The router acts as the gateway and provides internet access for both networks.
*   **Media Streaming and Gaming Priority:**  Prioritize media streaming and gaming traffic to improve quality and reduce latency. Implement simple queues (e.g., Simple Queues in RouterOS) to give priority to specific traffic types (e.g., based on port numbers or IP addresses).

**10. Scalability Considerations for SOHO Environments**

*   **Basic Routing Scalability:** For basic SOHO routing (as covered in this document), MikroTik routers are generally scalable for typical home or small office network sizes (tens of devices).
*   **Hardware Upgrade:** If the network grows significantly (more devices, higher bandwidth requirements, more complex features needed), you might need to upgrade to a more powerful MikroTik router with better CPU, RAM, and interface capabilities.
*   **Dynamic Routing (Beyond Basic SOHO):** For larger or more complex networks (beyond basic SOHO), static routing might become cumbersome. Consider exploring dynamic routing protocols (like RIP, OSPF, or BGP if connecting to multiple ISPs or larger networks) for more automated route management and scalability. However, dynamic routing is typically not required for basic SOHO scenarios.
*   **VLANs for Segmentation:** As the network grows, consider using VLANs to segment the network into logical subnets for better organization, security, and performance (as demonstrated in the VLAN documentation example).
*   **Wi-Fi Scalability:** For Wi-Fi, ensure your Wi-Fi access point (if separate from the MikroTik router) is capable of handling the number of wireless devices and bandwidth demands. Consider using multiple access points or mesh Wi-Fi systems for larger areas or higher density of wireless clients.

**11. Monitoring Configurations**

Basic monitoring for SOHO routing can include:

*   **Interface Monitoring:** Use `/interface monitor-traffic` to observe real-time traffic on WAN and LAN interfaces to identify bandwidth usage and potential bottlenecks.
*   **Resource Monitoring:** Check CPU and memory usage of the MikroTik router using `/system resource print` to ensure the router is not overloaded.
*   **Logging:** Enable basic logging to capture system events and potential issues. Configure logging actions (e.g., `disk`, `memory`, `remote`).  `/system logging add topics=info,warning,error action=disk`
*   **Simple Network Management Protocol (SNMP):** For more advanced monitoring, enable SNMP on the MikroTik router and use SNMP monitoring tools (e.g., Zabbix, PRTG, LibreNMS) to collect performance data and alerts. `/snmp community add name=public addresses=0.0.0.0/0` (configure `addresses` more restrictively for security).
*   **Ping Watchdog:** Use Ping Watchdog to automatically reboot the router if internet connectivity is lost. `/tool ping watchdog set enabled=yes host=8.8.8.8 interval=1m timeout=10s`

**12. Disaster Recovery Steps**

*   **Regular Configuration Backups:** Regularly export the router configuration to a file. Use `/export file=router_config_backup` in the CLI.  Automate this process (see Automated Backup Scripts below).
*   **Offsite Backup Storage:** Store configuration backups offsite (e.g., cloud storage, USB drive kept in a separate location) to protect against local disasters (fire, theft, hardware failure).
*   **Configuration Restoration:** In case of router failure or configuration corruption, you can restore the configuration from a backup file using `/import file=router_config_backup.rsc` in the CLI.
*   **Spare Router (Optional):** For critical SOHO environments where downtime needs to be minimized, consider having a spare MikroTik router pre-configured with the latest backup. In case of primary router failure, quickly replace it with the spare and restore the configuration.
*   **Document Configuration:** Keep a written or digital record of your network configuration (IP addresses, VLAN settings, etc.) in addition to configuration backups, for easier troubleshooting and recovery.

**13. Automated Backup Scripts**

**CLI Script (Scheduled Task):**

```routeros
# Script to export configuration and save to disk (adjust filename and path as needed)
/export file=router_backup_$(/system clock get date format=yyyy-MM-dd)_$(/system clock get time format=HH-mm-ss)
:log info "Router configuration backup completed."
```

Schedule this script to run regularly (e.g., daily) using RouterOS Scheduler:

```routeros
/system scheduler
add name="DailyConfigBackup" interval=1d start-time=03:00:00 on-event="/system script run DailyConfigBackupScript" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
```

**(Replace `DailyConfigBackupScript` with the name you give to the script above).**

**Python API Script (for more advanced backups, e.g., to remote server):**

```python
import requests
import os
from datetime import datetime

ROUTER_IP = "your_router_ip"
USERNAME = "your_username"
PASSWORD = "your_password"
BACKUP_DIR = "/path/to/your/backup/directory" # Local directory to save backups

BASE_URL = f"https://{ROUTER_IP}/rest"
AUTH = (USERNAME, PASSWORD)
HEADERS = {'content-type': 'application/json'}
VERIFY_SSL = False

def backup_configuration():
    try:
        # Get configuration export
        response = requests.get(f"{BASE_URL}/file/export", auth=AUTH, headers=HEADERS, verify=VERIFY_SSL)
        response.raise_for_status()

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"router_config_backup_{timestamp}.rsc"
        backup_filepath = os.path.join(BACKUP_DIR, backup_filename)

        with open(backup_filepath, "wb") as backup_file:
            backup_file.write(response.content)

        print(f"Configuration backed up to: {backup_filepath}")

        # Optional: Implement SCP or other method to copy backup to remote server

    except requests.exceptions.RequestException as e:
        print(f"API request failed during backup: {e}")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    backup_configuration()
```

**(Adjust `BACKUP_DIR` and implement remote backup transfer if needed).**  You can schedule this Python script to run using system schedulers (e.g., `cron` on Linux, Task Scheduler on Windows) or MikroTik's `/system scheduler` if you have Python installed on the router (less common in v6.x).

---

This comprehensive documentation provides a solid foundation for understanding and configuring basic IP routing in MikroTik RouterOS v6.x for SOHO environments. Remember to adapt the configurations and security measures to your specific network needs and always refer to the official MikroTik RouterOS documentation for the most up-to-date and detailed information.

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