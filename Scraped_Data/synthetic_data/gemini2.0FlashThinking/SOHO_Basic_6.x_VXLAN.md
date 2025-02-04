---
generated_at: 2025-02-03T21:24:51.183262
topic: VXLAN
category: Bridging & Switching
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS VXLAN for SOHO Environments (v6.x) - Basic Configuration

**Document Version:** v1.0
**Date:** October 26, 2023
**Author:** Your Name (MikroTik Certified Engineer)

### 1. Introduction to VXLAN in SOHO

VXLAN (Virtual eXtensible Local Area Network) is a network virtualization technology that allows you to extend Layer 2 networks over Layer 3 infrastructure. In SOHO (Small Office/Home Office) environments, VXLAN can be beneficial for:

*   **Extending LAN across locations:** Connect geographically separated offices or home offices as if they are on the same local network.
*   **Simplified network segmentation:** Create isolated network segments without complex VLAN configurations across multiple locations.
*   **Overcoming geographical limitations:** Bridge networks even when physical cabling is not feasible.

This document will guide you through setting up a basic point-to-point VXLAN tunnel between two MikroTik routers in a SOHO environment using RouterOS version 6.x. We will cover configuration via both Command Line Interface (CLI) and REST API, debugging, security, and basic optimization.

### 2. Architecture Diagram Requirements

For a basic SOHO VXLAN setup, we envision connecting two separate locations (e.g., Home Office and Small Office) over the internet.

```mermaid
graph LR
    subgraph Location A (Home Office)
        A[MikroTik Router A]
        APCs[PCs/Devices Location A]
        A -- APCs
        subgraph LAN A (192.168.1.0/24)
            style LAN A fill:#f9f,stroke:#333,stroke-width:2px
            APCs
        end
    end
    subgraph Internet
        INT[Internet]
    end
    subgraph Location B (Small Office)
        B[MikroTik Router B]
        BPCs[PCs/Devices Location B]
        B -- BPCs
        subgraph LAN B (192.168.2.0/24)
            style LAN B fill:#f9f,stroke:#333,stroke-width:2px
            BPCs
        end
    end

    A -- INT -- B
    A -- VXLAN Tunnel --> B

    style MikroTik Router A fill:#ccf,stroke:#333,stroke-width:2px
    style MikroTik Router B fill:#ccf,stroke:#333,stroke-width:2px
    linkStyle 2 stroke-dasharray: 5 5;
    linkStyle 3 stroke:#007bff, stroke-width:2px;  // VXLAN Tunnel
```

**Diagram Explanation:**

*   **Location A (Home Office):** MikroTik Router A with connected PCs in LAN A (192.168.1.0/24).
*   **Location B (Small Office):** MikroTik Router B with connected PCs in LAN B (192.168.2.0/24).
*   **Internet:** Represents the public internet connecting Location A and Location B.
*   **VXLAN Tunnel:**  The logical VXLAN tunnel established between Router A and Router B over the internet, enabling Layer 2 bridging between LAN A and LAN B.

### 3. CLI Configuration with Inline Comments

We will configure VXLAN on both Router A and Router B.

#### 3.1. Router A Configuration (Home Office)

Assume:

*   **Router A Public IP:** `203.0.113.1`
*   **Router A LAN Interface:** `ether2` (connected to LAN A switch)
*   **Router B Public IP:** `198.51.100.1`
*   **VXLAN VNI (VXLAN Network Identifier):** `100`
*   **VXLAN Interface Name:** `vxlan1-to-B`
*   **VXLAN Bridge Name:** `br-vxlan`
*   **VXLAN Interface IP (for management within VXLAN):** `172.16.100.1/30`

```routeros
# Create VXLAN interface
/interface vxlan
add name=vxlan1-to-B vni=100 remote-address=198.51.100.1 interface=ether1 # ether1 is assumed to be the WAN interface

# Create a bridge for VXLAN and LAN interface
/interface bridge
add name=br-vxlan

# Add VXLAN interface to the bridge
/interface bridge port
add bridge=br-vxlan interface=vxlan1-to-B

# Add LAN interface to the bridge
/interface bridge port
add bridge=br-vxlan interface=ether2 # ether2 is the LAN interface

# Assign IP address to the bridge interface (optional, for management within VXLAN L2 segment)
/ip address
add address=172.16.100.1/30 interface=br-vxlan network=172.16.100.0

# Optional: Enable ARP proxy if needed (for simpler L2 adjacency in some scenarios)
/interface bridge settings
set use-ip-firewall=no use-ip-firewall-for-vlan=no use-ip-firewall-for-pppoe=no arp-proxy=yes

# Optional: Configure firewall to allow VXLAN traffic (UDP ports 4789) if needed.
# Default firewall usually allows established/related, but verify if you have restrictive rules.
# Example rule to explicitly allow VXLAN from Router B's IP:
/ip firewall filter
add chain=input protocol=udp dst-port=4789 src-address=198.51.100.1 action=accept comment="Allow VXLAN from Router B"
add chain=forward protocol=udp dst-port=4789 src-address=198.51.100.1 action=accept comment="Allow VXLAN forward from Router B"
```

#### 3.2. Router B Configuration (Small Office)

Assume:

*   **Router B Public IP:** `198.51.100.1`
*   **Router B LAN Interface:** `ether2` (connected to LAN B switch)
*   **Router A Public IP:** `203.0.113.1`
*   **VXLAN VNI (VXLAN Network Identifier):** `100` (must match Router A)
*   **VXLAN Interface Name:** `vxlan1-to-A`
*   **VXLAN Bridge Name:** `br-vxlan` (can be the same name for simplicity)
*   **VXLAN Interface IP (for management within VXLAN):** `172.16.100.2/30`

```routeros
# Create VXLAN interface
/interface vxlan
add name=vxlan1-to-A vni=100 remote-address=203.0.113.1 interface=ether1 # ether1 is assumed to be the WAN interface

# Create a bridge for VXLAN and LAN interface
/interface bridge
add name=br-vxlan

# Add VXLAN interface to the bridge
/interface bridge port
add bridge=br-vxlan interface=vxlan1-to-A

# Add LAN interface to the bridge
/interface bridge port
add bridge=br-vxlan interface=ether2 # ether2 is the LAN interface

# Assign IP address to the bridge interface (optional, for management within VXLAN L2 segment)
/ip address
add address=172.16.100.2/30 interface=br-vxlan network=172.16.100.0

# Optional: Enable ARP proxy if needed (for simpler L2 adjacency in some scenarios)
/interface bridge settings
set use-ip-firewall=no use-ip-firewall-for-vlan=no use-ip-firewall-for-pppoe=no arp-proxy=yes

# Optional: Configure firewall to allow VXLAN traffic (UDP ports 4789) if needed.
# Example rule to explicitly allow VXLAN from Router A's IP:
/ip firewall filter
add chain=input protocol=udp dst-port=4789 src-address=203.0.113.1 action=accept comment="Allow VXLAN from Router A"
add chain=forward protocol=udp dst-port=4789 src-address=203.0.113.1 action=accept comment="Allow VXLAN forward from Router A"
```

**Explanation:**

*   **`/interface vxlan add ...`**: Creates the VXLAN interface.
    *   `name`:  Descriptive name for the VXLAN interface.
    *   `vni`: VXLAN Network Identifier. Must be the same on both routers to bridge the same L2 segment.
    *   `remote-address`: Public IP address of the peer router.
    *   `interface`:  The WAN interface used to reach the remote router.
*   **`/interface bridge add ...`**: Creates a bridge interface.
*   **`/interface bridge port add ...`**: Adds interfaces (VXLAN and LAN) to the bridge. Bridging creates a Layer 2 connection between the LAN and the VXLAN tunnel.
*   **`/ip address add ...`**: Assigns an IP address to the bridge interface. This is optional but useful for managing the VXLAN segment itself (e.g., pinging across the VXLAN).
*   **`/interface bridge settings set arp-proxy=yes`**:  ARP proxy can simplify the L2 adjacency across the VXLAN tunnel in some scenarios, especially in simpler SOHO setups.  Use with caution and understand its implications.
*   **`/ip firewall filter add ...`**: Optional firewall rules to explicitly allow VXLAN traffic (UDP port 4789). In most SOHO setups, default firewall rules might suffice, but explicit rules provide better control and documentation.

### 4. REST API Implementation (Python Code)

This Python script uses the `requests` library to configure VXLAN on a MikroTik router via its REST API.  **You need to enable the REST API on your MikroTik router first (`/ip service enable api`).**

```python
import requests
import json

ROUTER_IP_A = "203.0.113.1" # Replace with Router A's IP or hostname
ROUTER_IP_B = "198.51.100.1" # Replace with Router B's IP or hostname
ROUTER_USERNAME = "admin" # Replace with your RouterOS username
ROUTER_PASSWORD = ""    # Replace with your RouterOS password (or use API token for better security in production)

VXLAN_VNI = 100
VXLAN_IFACE_NAME_A = "vxlan1-to-B"
VXLAN_IFACE_NAME_B = "vxlan1-to-A"
BRIDGE_NAME = "br-vxlan"
LOCAL_LAN_IFACE = "ether2" # Assuming ether2 is LAN interface on both routers
WAN_IFACE = "ether1"      # Assuming ether1 is WAN interface on both routers

VXLAN_IP_A = "172.16.100.1/30"
VXLAN_IP_B = "172.16.100.2/30"
VXLAN_NETWORK = "172.16.100.0"

def configure_vxlan(router_ip, remote_ip, vxlan_iface_name, vxlan_ip):
    base_url = f"http://{router_ip}/rest"
    auth = (ROUTER_USERNAME, ROUTER_PASSWORD)
    headers = {'Content-Type': 'application/json'}

    try:
        # Create VXLAN interface
        vxlan_data = {
            "name": vxlan_iface_name,
            "vni": VXLAN_VNI,
            "remote-address": remote_ip,
            "interface": WAN_IFACE
        }
        response = requests.post(f"{base_url}/interface/vxlan", auth=auth, headers=headers, data=json.dumps(vxlan_data), verify=False) # verify=False for SOHO, consider certificate verification in production
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        print(f"Router {router_ip}: VXLAN interface created successfully.")

        # Create bridge interface if it doesn't exist (check first for robustness in real scripts)
        bridge_data = {"name": BRIDGE_NAME}
        response = requests.post(f"{base_url}/interface/bridge", auth=auth, headers=headers, data=json.dumps(bridge_data), verify=False)
        if response.status_code == 409: # 409 Conflict - Bridge already exists (assuming name collision)
            print(f"Router {router_ip}: Bridge '{BRIDGE_NAME}' already exists.")
        else:
            response.raise_for_status()
            print(f"Router {router_ip}: Bridge '{BRIDGE_NAME}' created successfully.")


        # Add VXLAN interface to bridge
        bridge_port_vxlan_data = {
            "bridge": BRIDGE_NAME,
            "interface": vxlan_iface_name
        }
        response = requests.post(f"{base_url}/interface/bridge/port", auth=auth, headers=headers, data=json.dumps(bridge_port_vxlan_data), verify=False)
        response.raise_for_status()
        print(f"Router {router_ip}: VXLAN interface added to bridge.")

        # Add LAN interface to bridge
        bridge_port_lan_data = {
            "bridge": BRIDGE_NAME,
            "interface": LOCAL_LAN_IFACE
        }
        response = requests.post(f"{base_url}/interface/bridge/port", auth=auth, headers=headers, data=json.dumps(bridge_port_lan_data), verify=False)
        response.raise_for_status()
        print(f"Router {router_ip}: LAN interface added to bridge.")

        # Assign IP address to bridge interface
        ip_address_data = {
            "address": vxlan_ip,
            "interface": BRIDGE_NAME,
            "network": VXLAN_NETWORK
        }
        response = requests.post(f"{base_url}/ip/address", auth=auth, headers=headers, data=json.dumps(ip_address_data), verify=False)
        response.raise_for_status()
        print(f"Router {router_ip}: IP address assigned to bridge.")

        # Optional: Enable ARP Proxy (simplified - directly setting interface property)
        bridge_settings_data = {"arp-proxy": "yes"}
        response = requests.put(f"{base_url}/interface/bridge/{BRIDGE_NAME}", auth=auth, headers=headers, data=json.dumps(bridge_settings_data), verify=False)
        response.raise_for_status()
        print(f"Router {router_ip}: ARP Proxy enabled on bridge.")


    except requests.exceptions.RequestException as e:
        print(f"Error configuring Router {router_ip}: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
        return False
    return True

if __name__ == "__main__":
    print("Configuring Router A...")
    config_a_success = configure_vxlan(ROUTER_IP_A, ROUTER_IP_B, VXLAN_IFACE_NAME_A, VXLAN_IP_A)
    print("\nConfiguring Router B...")
    config_b_success = configure_vxlan(ROUTER_IP_B, ROUTER_IP_A, VXLAN_IFACE_NAME_B, VXLAN_IP_B)

    if config_a_success and config_b_success:
        print("\nVXLAN configuration completed successfully on both routers.")
    else:
        print("\nVXLAN configuration failed on one or both routers. Check error messages.")
```

**Python Script Explanation:**

*   **`requests` library:** Used for making HTTP requests to the RouterOS REST API.
*   **Variables:**  Configurable variables for router IPs, usernames, VXLAN parameters, etc.
*   **`configure_vxlan(router_ip, remote_ip, ...)` function:**
    *   Takes router IP, remote IP, and VXLAN interface details as input.
    *   Constructs REST API URLs.
    *   Uses `requests.post` to create VXLAN interface, bridge, bridge ports, and assign IP address.
    *   Uses `requests.put` to enable ARP proxy on the bridge.
    *   Includes basic error handling using `try...except` and `response.raise_for_status()`.
*   **`if __name__ == "__main__":` block:**
    *   Calls `configure_vxlan` for both Router A and Router B.
    *   Prints success or failure messages.

**To use this script:**

1.  **Install `requests` library:** `pip install requests`
2.  **Enable REST API on both MikroTik routers:** `/ip service enable api`
3.  **Update variables:**  Modify `ROUTER_IP_A`, `ROUTER_IP_B`, `ROUTER_USERNAME`, `ROUTER_PASSWORD` and other variables to match your environment.
4.  **Run the script:** `python your_script_name.py`

**Security Note:**  This script uses basic username/password authentication and disables SSL certificate verification (`verify=False`). For production environments, consider using API tokens and enabling certificate verification for enhanced security.

### 5. Common Debugging Scenarios

*   **VXLAN Interface Not Running/Inactive:**
    *   **Check `remote-address`:** Ensure the `remote-address` is correctly configured on both routers and they can reach each other over the internet (ping the remote public IP from each router).
    *   **Firewall Issues:** Verify that UDP port 4789 is allowed in both directions between the routers' public IPs, including any firewalls outside of the MikroTik routers. Use `/ip firewall filter print` on each router to check firewall rules.
    *   **Interface Configuration:**  Double-check the `interface` setting in `/interface vxlan`. It should be the WAN interface connected to the internet.
    *   **MTU Mismatch:**  While VXLAN adds overhead, MTU issues are less common in basic setups. However, if you suspect MTU problems, try lowering the MTU on the WAN interfaces or VXLAN interfaces for testing. Check with `ping <remote_public_ip> size=1400 do-not-fragment` from each router.
    *   **Log Analysis:** Use `/log print` or `/log info` to check for any error messages related to VXLAN, bridge, or interface configuration.

*   **No Connectivity Across VXLAN:**
    *   **Bridge Configuration:** Verify that both the VXLAN interface and the LAN interface are correctly added to the bridge (`/interface bridge port print`).
    *   **IP Addressing:** Check IP address configuration on the bridge interface (`/ip address print`). Ensure IP addresses are in the same subnet if you are using IP addressing on the bridge. However, for basic L2 bridging, IP addresses on the bridge are optional.
    *   **ARP Resolution Issues:** If using ARP proxy, try disabling it temporarily for troubleshooting (`/interface bridge settings set arp-proxy=no`).  If disabling ARP proxy resolves the issue, investigate ARP proxy configuration or network topology.
    *   **MAC Address Learning:**  Use `/interface bridge host print` to see if MAC addresses from the remote LAN are being learned on the bridge. If not, there might be a connectivity problem with the VXLAN tunnel itself.
    *   **Ping Test:** Ping devices on the remote LAN by their IP addresses. If ping fails, use `/tool traceroute <remote_lan_ip>` to trace the path and identify where the connectivity breaks.
    *   **Packet Capture:** Use `/tool sniffer` on both routers to capture traffic on the VXLAN interface and bridge interface. Analyze the captured packets (e.g., with Wireshark) to understand if VXLAN packets are being exchanged and if there are any errors.  Capture filters can be helpful, e.g., `interface=vxlan1-to-B, protocol=udp, port=4789`.

### 6. Version-Specific Considerations (RouterOS 6.x)

*   **Feature Stability:** VXLAN in RouterOS 6.x is generally stable for basic configurations like point-to-point tunnels.
*   **Performance:** Performance might be slightly less optimized compared to newer RouterOS versions (v7+), especially for hardware offloading capabilities (which are less relevant for basic SOHO setups).
*   **Feature Set:** RouterOS 6.x has a slightly older feature set compared to v7+. For basic VXLAN bridging, this is not a significant limitation. More advanced VXLAN features or control plane options (like EVPN) are not typically needed in basic SOHO scenarios and are more relevant for larger deployments and RouterOS v7+.
*   **Bug Fixes and Updates:** RouterOS v6.x is in long-term maintenance.  Ensure you are running the latest stable version within the v6.x branch for bug fixes and security updates.

For basic SOHO VXLAN setups, version 6.x is sufficient. If you anticipate needing more advanced VXLAN features or require the latest performance optimizations, consider upgrading to RouterOS v7+ (if your hardware is compatible and you are comfortable with the upgrade process).

### 7. Security Hardening Measures for SOHO

*   **Strong Passwords:** Use strong, unique passwords for the `admin` user and any other user accounts on both MikroTik routers. Change default passwords immediately after installation.
*   **Disable Default Services:** Disable unnecessary services like `telnet`, `ftp`, `www` (if you only use WinBox/API) under `/ip service`. Only enable services you actively use.
*   **Firewall Rules:** Review and tighten the default firewall rules.
    *   **Input Chain:** Limit access to the router's management interfaces (WinBox, API, SSH) to trusted IP addresses or networks. Use `/ip firewall filter add chain=input src-address=<your_trusted_network> action=accept` and then `add chain=input action=drop` as the last rule.
    *   **Forward Chain:**  Carefully consider forwarding rules. For basic VXLAN bridging, you might need to allow forwarding between the bridge interface and the WAN interface if you have restrictive forwarding rules. However, for simple bridging, the bridge itself handles forwarding.
    *   **Output Chain:**  Less critical for basic SOHO security, but you can also restrict outgoing traffic if needed.
*   **Disable Guest Access:** If you don't use guest Wi-Fi, disable the guest wireless interface (if present).
*   **Keep RouterOS Updated:** Regularly update RouterOS to the latest stable version within the 6.x branch to patch security vulnerabilities.
*   **Physical Security:** Secure the physical access to your MikroTik routers to prevent unauthorized physical access and tampering.
*   **Consider IPsec for Control Plane (Optional, for enhanced security):** While basic VXLAN itself encrypts data within the tunnel, the control plane (VXLAN header exchange) is not encrypted by default. For highly sensitive environments, you could consider encapsulating the VXLAN traffic within an IPsec tunnel to encrypt the control plane as well. However, for basic SOHO, this might add unnecessary complexity.

### 8. Performance Optimization Tips for Basic SOHO VXLAN

*   **MTU Optimization:** Ensure optimal MTU settings. VXLAN adds overhead (around 50 bytes).  For standard Ethernet (1500 MTU), consider using an MTU of 1450-1460 on the bridge or VXLAN interface to avoid fragmentation. Test with `ping -s <size> -M do <remote_vxlan_ip_or_device_ip>` (e.g., `ping -s 1400 -M do 172.16.100.2`). Adjust MTU accordingly.
*   **FastTrack (if applicable and safe in your setup):**  FastTrack can improve performance by bypassing connection tracking for established connections. However, use FastTrack cautiously, especially if you have complex firewall rules or need connection tracking for other features. In basic SOHO VXLAN bridging, FastTrack might provide minor improvements but is not critical.  If you decide to use FastTrack, ensure it doesn't interfere with your other firewall rules or desired functionality.
*   **CPU Load Monitoring:** Monitor CPU load on both routers using `/system resource print`. High CPU load can indicate performance bottlenecks. For basic SOHO VXLAN, CPU load should be minimal.
*   **Hardware Offloading (Limited in v6.x for basic VXLAN):** RouterOS v6.x has limited hardware offloading capabilities for VXLAN, especially for basic setups. Hardware offloading is more significant in v7+ and for more complex VXLAN deployments.  For basic SOHO, software processing of VXLAN is usually sufficient.
*   **Minimize Bridge Filtering (Optional):** In basic bridging setups, bridge filtering is often not necessary. Ensure `use-ip-firewall`, `use-ip-firewall-for-vlan`, and `use-ip-firewall-for-pppoe` are set to `no` in `/interface bridge settings` unless you have specific filtering requirements on the bridge itself.

### 9. Special Requirements for SOHO Environments

#### 9.1. Real-World Deployment Examples

*   **Connecting Two Home Offices:** Imagine two individuals working from separate homes who need to access shared resources (file servers, printers) as if they were in the same office. VXLAN can bridge their home networks, allowing seamless access to these resources.
*   **Home Office to Small Business Office:** A small business with a main office and a remote home office. VXLAN can connect the home office to the main office network, enabling remote employees to access office resources and vice versa.
*   **Branch Office Connectivity (Simplified):** For very small branch offices with minimal IT infrastructure, VXLAN can provide a simple way to extend the main office LAN without complex routing or VLAN configurations at the branch.

#### 9.2. Scalability Considerations

For basic SOHO VXLAN setups as described, scalability is limited but usually sufficient for the intended use cases.

*   **Point-to-Point Nature:**  This configuration is primarily for point-to-point connections. For more complex topologies (hub-and-spoke, mesh), manual configuration becomes less scalable.
*   **Manual Key Distribution (Implicit):** We are manually configuring the `remote-address`. In larger VXLAN deployments, you would typically use a control plane (like EVPN) to automate VTEP discovery and MAC address learning.  For basic SOHO, manual configuration is acceptable.
*   **VNI Limit:** RouterOS supports a large number of VNIs, so VNI exhaustion is not a concern in SOHO.
*   **Performance Limits:** Performance scales with the hardware capabilities of the MikroTik routers. For basic SOHO internet connections, typical MikroTik routers can handle VXLAN encapsulation without significant performance degradation. For very high bandwidth requirements or large numbers of VXLAN tunnels, consider more powerful MikroTik models or RouterOS v7+ with enhanced hardware offloading.

For larger and more dynamic VXLAN environments, consider:

*   **RouterOS v7+ and Hardware Offloading:**  RouterOS v7+ offers improved VXLAN performance and better hardware offloading capabilities on supported hardware.
*   **VXLAN Control Plane (EVPN):** For automated VTEP discovery, MAC address learning, and more scalable VXLAN deployments, explore using EVPN (Ethernet VPN) as a control plane for VXLAN. EVPN is more complex to configure but provides significant scalability and flexibility. However, EVPN is typically not needed for basic SOHO scenarios.

#### 9.3. Monitoring Configurations

*   **Interface Status Monitoring:**
    *   **CLI:** Use `/interface vxlan monitor vxlan1-to-B once` to check the status of the VXLAN interface (running, mtu, remote-address, etc.).
    *   **WinBox/WebFig:**  Go to `Interfaces`, double-click the `vxlan1-to-B` interface, and check the `Status` tab.
    *   **SNMP:**  Monitor the operational status of the VXLAN interface via SNMP (if SNMP is configured). OID for interface operational status is `.1.3.6.1.2.1.2.2.1.8.<interface_index>`. You need to find the interface index of your VXLAN interface using `/interface print`.

*   **Bridge MAC Address Table Monitoring:**
    *   **CLI:** Use `/interface bridge host print bridge=br-vxlan` to view the MAC address table learned on the bridge. This can help verify if devices from the remote LAN are being learned across the VXLAN tunnel.
    *   **WinBox/WebFig:** Go to `Bridge` -> `Hosts` and select `br-vxlan` as the bridge.

*   **Connection Monitoring (Ping):**
    *   Use the `/ping` tool in RouterOS to regularly ping devices on the remote LAN across the VXLAN tunnel to verify connectivity.
    *   Consider using MikroTik's Netwatch tool (`/tool netwatch`) to automatically monitor the reachability of remote devices and trigger notifications or actions if connectivity is lost.

*   **Logging:**
    *   Configure logging for VXLAN related events (`/system logging add topics=vxlan action=disk,echo`). Review logs regularly for any errors or issues.

#### 9.4. Disaster Recovery Steps

For basic SOHO VXLAN recovery, the primary focus is on configuration backup and restore.

1.  **Regular Configuration Backups:**
    *   **Manual Backup (CLI):** Use `/export file=config-vxlan-backup` to export the RouterOS configuration to a file. Download this file and store it securely.
    *   **Automated Backup (Script - see section 9.5):** Use a script to automate configuration backups regularly.
    *   **WinBox/WebFig:** Go to `Files` and drag the `config-vxlan-backup.rsc` file to your computer.

2.  **Configuration Restore:**
    *   **CLI:** After a router reset or failure, upload the `config-vxlan-backup.rsc` file to the router's `Files` directory. Then, use `/import file-name=config-vxlan-backup.rsc`.
    *   **WinBox/WebFig:** Go to `Files`, upload the `config-vxlan-backup.rsc` file. Then, in the terminal, run `/import file-name=config-vxlan-backup.rsc`.

3.  **Document Configuration:** Keep a separate document (like this one) detailing your VXLAN configuration, including IP addresses, VNI, interface names, and any other relevant settings. This documentation will be invaluable for troubleshooting and recovery.

4.  **Test Recovery Procedure:** Periodically test your backup and restore procedure to ensure it works as expected and you are familiar with the steps.

#### 9.5. Automated Backup Scripts

Here's a basic Python script to automate RouterOS configuration backups using the REST API.  **Ensure REST API is enabled and accessible.**

```python
import requests
import datetime
import os

ROUTER_IP_A = "203.0.113.1" # Router A IP
ROUTER_IP_B = "198.51.100.1" # Router B IP
ROUTER_USERNAME = "admin"
ROUTER_PASSWORD = ""
BACKUP_DIR = "mikrotik_backups" # Directory to store backups locally

def backup_router_config(router_ip):
    base_url = f"http://{router_ip}/rest"
    auth = (ROUTER_USERNAME, ROUTER_PASSWORD)
    headers = {'Content-Type': 'application/json'}
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_filename = f"router_{router_ip.replace('.', '_')}_config_{timestamp}.rsc"
    backup_filepath = os.path.join(BACKUP_DIR, backup_filename)

    try:
        # Export configuration
        response = requests.get(f"{base_url}/system/script/run", auth=auth, headers=headers, params={"name": "export"}, verify=False) # Assuming a script named 'export' exists (or use '/export file=...')
        response.raise_for_status()
        config_content = response.text

        # Save to file
        os.makedirs(BACKUP_DIR, exist_ok=True) # Create backup directory if it doesn't exist
        with open(backup_filepath, "w") as f:
            f.write(config_content)
        print(f"Router {router_ip}: Configuration backed up to '{backup_filepath}'")

    except requests.exceptions.RequestException as e:
        print(f"Error backing up Router {router_ip}: {e}")
        return False
    return True

if __name__ == "__main__":
    print("Backing up Router A...")
    backup_router_config(ROUTER_IP_A)
    print("\nBacking up Router B...")
    backup_router_config(ROUTER_IP_B)
    print("\nBackup process completed.")
```

**Backup Script Explanation:**

*   **`requests`, `datetime`, `os` libraries:** Used for API requests, timestamping, and file system operations.
*   **Variables:** Configurable router IPs, credentials, and backup directory.
*   **`backup_router_config(router_ip)` function:**
    *   Constructs REST API URL.
    *   Uses `requests.get` to execute the `/export` command (assuming you have a script named "export" defined in RouterOS, or you can modify the script to directly use `/export file=...`).  **A better approach is to use `/system/backup save name=backup_name` which creates a binary backup, but for simple SOHO text-based config backups using `/export` is often sufficient and easier to inspect.**
    *   Saves the configuration content to a file with a timestamp in the specified backup directory.
*   **`if __name__ == "__main__":` block:** Calls `backup_router_config` for both routers.

**To use this script:**

1.  **Install `requests` library:** `pip install requests`
2.  **Enable REST API on both MikroTik routers:** `/ip service enable api`
3.  **Update variables:** Modify `ROUTER_IP_A`, `ROUTER_IP_B`, `ROUTER_USERNAME`, `ROUTER_PASSWORD`, and `BACKUP_DIR` as needed.
4.  **Run the script:** `python your_backup_script_name.py`
5.  **Schedule the script:** Use cron (Linux/macOS) or Task Scheduler (Windows) to run the script automatically at regular intervals (e.g., daily or weekly).

**Important Note:** This is a basic backup script. For more robust backup solutions, consider using MikroTik's built-in backup scheduling features (if available in v6.x to the desired extent) or more advanced scripting with error handling, logging, and secure storage of backups. For SOHO, this basic script provides a good starting point for automated backups.

---

This document provides a comprehensive guide to setting up basic VXLAN in a SOHO environment using MikroTik RouterOS v6.x. Remember to adapt the configuration and security measures to your specific needs and environment. Always test your configuration thoroughly and keep your RouterOS software up to date.

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