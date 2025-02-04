---
generated_at: 2025-02-03T20:57:38.669099
topic: IP Addressing (IPv4 and IPv6)
category: Core Networking
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

```markdown
# MikroTik RouterOS Documentation: IP Addressing (IPv4 & IPv6) - SOHO (Basic)

**RouterOS Version:** 6.x
**Network Scale:** Small Office/Home Office (SOHO)
**Complexity Level:** Basic

## 1. Architecture Diagram Requirements

For a SOHO environment, a common architecture involves a single MikroTik router acting as the gateway between the home/small office network and the internet.  The router typically has:

*   **WAN Interface:** Connects to the Internet Service Provider (ISP).  This interface usually gets a dynamic IPv4 address via DHCP or a static IPv4/IPv6 address.
*   **LAN Interface:** Connects to the local network devices (computers, printers, etc.). This is often a bridge interface encompassing multiple Ethernet ports and Wi-Fi. The LAN interface acts as the default gateway for local devices and provides DHCP services.

```mermaid
graph LR
    A[Internet] --> B(MikroTik Router);
    B --> C{LAN Devices};
    B -- WAN Interface (e.g., ether1) --> A;
    B -- LAN Interface (e.g., bridge1) --> C;
    C -- Device 1 (PC);
    C -- Device 2 (Printer);
    C -- Device 3 (Laptop - Wireless);
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style A fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#eee,stroke:#333,stroke-width:1px
```

**Requirements based on Diagram:**

*   **WAN Interface IP:** Configuration for obtaining an IP address from the ISP (DHCP Client or Static IPv4/IPv6).
*   **LAN Interface IP:** Configuration for a static IPv4 and optionally IPv6 address for the internal network.
*   **DHCP Server:** Configuration for automatically assigning IPv4 addresses to devices on the LAN.
*   **IPv6 Support:** Configuration for IPv6 addressing if provided by the ISP.

## 2. CLI Configuration with Inline Comments

This section provides CLI commands to configure IPv4 and IPv6 addressing on a MikroTik Router in a SOHO setup.

### 2.1 IPv4 Configuration

```routeros
# --- IPv4 Configuration ---

# 1. Set Interface Names (Optional, for clarity)
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN1
/interface ethernet set ether3 name=LAN2
/interface wireless set wlan1 name=WiFi

# 2. Create a Bridge Interface for LAN (if not already existing)
/interface bridge add name=bridge-LAN protocol-mode=rstp # RSTP for loop prevention, optional
/interface bridge port add bridge=bridge-LAN interface=LAN1
/interface bridge port add bridge=bridge-LAN interface=LAN2
/interface bridge port add bridge=bridge-LAN interface=WiFi

# 3. Configure WAN Interface for DHCP Client (Dynamic IP from ISP)
/ip dhcp-client add interface=WAN disabled=no comment="Get WAN IP from ISP"

#    Alternatively, for Static WAN IP (if provided by ISP):
# /ip address add address=203.0.113.2/24 interface=WAN network=203.0.113.0 comment="Static WAN IP"
# /ip route add dst-address=0.0.0.0/0 gateway=203.0.113.1 comment="Default route via ISP gateway"
# /ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes  # Set DNS servers, optional here if DHCP provides DNS

# 4. Configure LAN Bridge Interface with Static IPv4 Address
/ip address add address=192.168.88.1/24 interface=bridge-LAN network=192.168.88.0 comment="LAN Bridge IP"

# 5. Configure DHCP Server on LAN Bridge
/ip pool add name=dhcp_pool_lan ranges=192.168.88.10-192.168.88.254 comment="DHCP Pool for LAN"
/ip dhcp-server add name=dhcp_server_lan interface=bridge-LAN address-pool=dhcp_pool_lan lease-time=10m comment="DHCP Server on LAN" # Lease time adjusted for SOHO - 10 minutes
/ip dhcp-server network add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1 comment="DHCP Network Settings for LAN"
```

### 2.2 IPv6 Configuration (Assuming ISP provides IPv6 via DHCPv6-PD)

```routeros
# --- IPv6 Configuration (Optional - if ISP provides IPv6) ---

# 1. Enable IPv6 Package (if not already enabled)
/system package enable ipv6
/system reboot # Reboot required after enabling IPv6 package

# 2. Configure WAN Interface for DHCPv6-Client with Prefix Delegation (PD)
/ipv6 dhcp-client add interface=WAN request=prefix prefix-hint=::/56 pool-name=ipv6_pool_lan pool-length=64 comment="DHCPv6-PD Client on WAN"
#   - request=prefix: Request IPv6 prefix delegation
#   - prefix-hint=::/56: Request a /56 prefix (common for home users, adjust if ISP specifies)
#   - pool-name=ipv6_pool_lan: Pool to store delegated prefixes
#   - pool-length=64:  Subnet prefix length to assign to LAN interfaces from the delegated pool

# 3. Create IPv6 Pool for LAN Subnets (if not already created by DHCPv6-Client)
/ipv6 pool add name=ipv6_pool_lan prefix-length=64 comment="IPv6 Pool for LAN Subnets" # Usually created automatically by DHCPv6-Client

# 4. Configure LAN Bridge Interface to get IPv6 Address from the delegated pool
/ipv6 address add interface=bridge-LAN from-pool=ipv6_pool_lan eui-64=no advertise=yes comment="IPv6 on LAN Bridge from delegated pool"
#   - from-pool=ipv6_pool_lan: Get address from the delegated prefix pool
#   - eui-64=no: Use simpler address assignment, not EUI-64
#   - advertise=yes: Enable Router Advertisement for clients to get IPv6 addresses automatically

# 5. Configure IPv6 ND (Neighbor Discovery) settings on LAN Bridge (Defaults are usually fine for SOHO)
/ipv6 nd set bridge-LAN advertise-dns=yes managed-address-configuration=other-configuration comment="IPv6 ND settings on LAN"
#   - advertise-dns=yes: Advertise DNS server information
#   - managed-address-configuration=other-configuration: Clients get addresses via Router Advertisement (SLAAC) and other config via DHCPv6 (if needed, can be 'stateless-dhcpv6' or 'managed')

# 6. (Optional) Configure IPv6 DNS Servers (If not advertised by ISP via DHCPv6)
# /ipv6 dns set servers=2001:4860:4860::8888,2001:4860:4860::8844 allow-remote-requests=yes
```

## 3. REST API Implementation (Python Code)

This Python script uses the MikroTik RouterOS REST API to configure basic IPv4 addressing.  You need to install the `requests` library (`pip install requests`).

```python
import requests
import json

ROUTER_IP = "192.168.88.1"  # Replace with your Router IP
USERNAME = "admin"         # Replace with your Router Username
PASSWORD = ""            # Replace with your Router Password

BASE_URL = f"http://{ROUTER_IP}/rest"

def api_request(endpoint, data=None, method='GET'):
    """Sends API request to MikroTik RouterOS."""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method == 'GET':
            response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False) # verify=False for self-signed certs in RouterOS
        elif method == 'POST':
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, auth=(USERNAME, PASSWORD), headers=headers, data=json.dumps(data), verify=False)
        else:
            print(f"Unsupported method: {method}")
            return None

        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        if method == 'GET':
            return response.json()
        else:
            return response.text # For POST, return text response (or check status code)

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        if response is not None:
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
        return None

def configure_ipv4_address(interface_name, ip_address_cidr):
    """Configures a static IPv4 address on an interface."""
    interface_id = get_interface_id(interface_name)
    if not interface_id:
        print(f"Interface '{interface_name}' not found.")
        return False

    data = {
        "address": ip_address_cidr,
        "interface": interface_id,
        "network": ip_address_cidr.split('/')[0][:- (len(ip_address_cidr.split('/')[1]) + (1 if '/' in ip_address_cidr else 0))] + ".0" # Basic network calculation, adjust if needed
    }
    response = api_request("/ip/address", data=data, method='POST')
    if response is not None:
        print(f"IPv4 address configured on '{interface_name}'.")
        return True
    else:
        return False


def get_interface_id(interface_name):
    """Gets the internal ID of an interface by name."""
    interfaces = api_request("/interface/ethernet") # Assuming Ethernet interfaces for simplicity, adjust for other types
    if interfaces:
        for iface in interfaces:
            if iface.get('name') == interface_name:
                return iface.get('.id')
    return None


if __name__ == "__main__":
    lan_interface_name = "bridge-LAN" # Assuming bridge-LAN was created via CLI or already exists
    lan_ip_cidr = "192.168.88.1/24"

    if configure_ipv4_address(lan_interface_name, lan_ip_cidr):
        print(f"Successfully configured IPv4 on {lan_interface_name} to {lan_ip_cidr}")
    else:
        print(f"Failed to configure IPv4 on {lan_interface_name}")
```

**To use the API script:**

1.  **Enable REST API:**  `/ip service enable api-ssl` (or `/ip service enable api` for HTTP - less secure for production).
2.  **Install `requests`:** `pip install requests`
3.  **Run the Python script:** `python your_script_name.py`
4.  **Adjust variables:**  `ROUTER_IP`, `USERNAME`, `PASSWORD`, interface names, IP addresses as needed.

## 4. Common Debugging Scenarios

| Scenario                                 | Possible Cause                                    | Debugging Steps                                                                                                     | CLI Command Examples                                                                    |
| :--------------------------------------- | :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------- |
| **No Internet Connectivity (WAN - DHCP)** | DHCP Client not working, ISP issues                | 1. Check DHCP Client status. 2. Check WAN interface status (link up?). 3. Try releasing and renewing DHCP lease. | `/ip dhcp-client print`, `/interface ethernet monitor WAN`, `/ip dhcp-client release WAN`, `/ip dhcp-client renew WAN` |
| **No Internet (WAN - Static IP)**         | Incorrect static IP settings, gateway, DNS         | 1. Verify static IP, subnet mask, gateway, DNS settings. 2. Ping gateway. 3. Ping public IP (e.g., 8.8.8.8).    | `/ip address print`, `/ip route print`, `/ip dns print`, `ping 203.0.113.1`, `ping 8.8.8.8` |
| **LAN Devices cannot get IP address**    | DHCP Server not running, IP address conflict, pool exhausted | 1. Check DHCP Server status. 2. Check DHCP Server logs. 3. Verify IP pool range and available addresses.       | `/ip dhcp-server print`, `/log print topics=dhcp-server`, `/ip pool print`                        |
| **LAN Devices cannot reach Internet**     | Incorrect default gateway on LAN devices, Firewall | 1. Verify default gateway setting on LAN devices (should be LAN bridge IP). 2. Check firewall rules (NAT, forward). | `ipconfig /all` (Windows), `ifconfig` (Linux/macOS), `/ip firewall nat print`, `/ip firewall filter print`          |
| **IPv6 connectivity issues**              | DHCPv6-PD client issues, Router Advertisement issues | 1. Check DHCPv6-PD client status. 2. Check IPv6 addresses on interfaces. 3. Check IPv6 ND settings.             | `/ipv6 dhcp-client print`, `/ipv6 address print`, `/ipv6 nd print bridge-LAN`                       |

## 5. Version-Specific Considerations (RouterOS 6.x)

*   **IPv6 Package:** In RouterOS 6.x, the IPv6 package is often a separate package that needs to be enabled and might require a reboot after enabling. Ensure the `ipv6` package is enabled in `/system package`.
*   **DHCPv6-PD Prefix Hint:** The `prefix-hint` parameter in DHCPv6-Client is important for requesting a specific prefix size from the ISP. Check ISP documentation for the recommended prefix size.
*   **REST API (v6.x):** The REST API in RouterOS 6.x is functional but might have fewer features and potential bugs compared to later versions. Ensure you are using a stable RouterOS 6.x version.
*   **Bridge VLAN Filtering:**  While VLAN filtering on bridges is available in v6.x, the configuration and features might be less advanced than in RouterOS 7.x. For basic SOHO VLANs, it's usually sufficient.

## 6. Security Hardening Measures

*   **Disable Unused Services:** Disable any unused services like `api` (HTTP API), `telnet`, `ftp` if you are only using `api-ssl` (HTTPS API) or `ssh`. `/ip service disable api,telnet,ftp`
*   **Strong Passwords:** Use strong and unique passwords for the `admin` user and any other user accounts. `/user set admin password=YourStrongPassword`
*   **Limit API Access:** If using the API, restrict access to the API port (8729 for HTTPS API by default) using firewall rules to only allow access from trusted IPs if possible. `/ip firewall filter add chain=input protocol=tcp dst-port=8729 src-address-list=Trusted_IPs action=accept comment="Allow API from Trusted IPs"`. Create address list `/ip firewall address-list add list=Trusted_IPs address=192.168.88.0/24` (example for LAN).
*   **Firewall Rules:** Implement basic firewall rules to protect your network. At minimum, protect against WAN side access to internal services.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version within the 6.x branch to patch security vulnerabilities. `/system package update check-for-updates`, `/system package update install` (carefully review release notes before updating).
*   **Disable Default User (Optional):** If you created a new administrative user, consider disabling the default `admin` user for enhanced security. `/user disable admin`.

## 7. Performance Optimization Tips

*   **FastTrack:** Ensure FastTrack is enabled in firewall filter rules to bypass connection tracking for established/related connections, improving throughput. `/ip firewall filter add chain=forward action=fasttrack-connection connection-state=established,related` (should be placed early in `forward` chain).
*   **Hardware Offloading:** If your MikroTik device supports hardware offloading for bridging and VLANs, ensure it is enabled. This is often automatic but check device documentation for specific settings (e.g., `master-port` for Ethernet ports).
*   **DHCP Lease Time:**  For SOHO environments with many devices joining and leaving frequently (e.g., guest Wi-Fi), consider using shorter DHCP lease times (e.g., 10 minutes as in example) to reclaim IP addresses faster. However, very short lease times can increase DHCP traffic. Balance based on your network usage.
*   **Minimize Bridge Ports:** Only add necessary interfaces to bridge interfaces. Avoid unnecessary bridging.
*   **Queue Management:** If experiencing bandwidth congestion, implement basic queue management (Simple Queues or Queue Tree) to prioritize important traffic and limit bandwidth for less critical traffic.

## 8. Special Requirements for SOHO Environments

### 8.1 Real-world Deployment Examples

*   **Scenario 1: Basic Home Network:**  Single MikroTik router connected to ISP via Ethernet (DHCP WAN), providing Wi-Fi and wired LAN for home devices (computers, phones, smart TVs). DHCP server on LAN bridge assigns IPs. IPv6 is optional if ISP provides it.
*   **Scenario 2: Small Office with Guest Wi-Fi:**  MikroTik router with WAN (DHCP or Static IP), main LAN for office devices, and separate VLAN/Wi-Fi for guests.  DHCP server for each network segment. Firewall rules to isolate guest network.
*   **Scenario 3: Home Office with VPN:**  MikroTik router with WAN, LAN, and VPN client connection to corporate network. Static routing or dynamic routing (if supported by corporate VPN) to access corporate resources.

### 8.2 Scalability Considerations

While SOHO networks are inherently small, consider these scalability aspects:

*   **IP Address Range:**  Choose a sufficiently large IPv4 subnet (e.g., /24) for the LAN to accommodate future device growth. IPv6 provides virtually unlimited addresses.
*   **DHCP Pool Size:**  Configure DHCP pool size within the subnet range, leaving some addresses for static assignments if needed.
*   **Router Hardware:** Select a MikroTik router model with sufficient processing power, RAM, and port density for current and anticipated future needs. For basic SOHO, even entry-level MikroTik devices are often sufficient. For higher bandwidth or more features, consider more powerful models.
*   **VLANs and Subnets:** For future segmentation or expansion, plan for VLANs and separate subnets early on, even if not immediately implemented. This makes future network expansion and management easier.

### 8.3 Monitoring Configurations

Basic monitoring can be done via CLI and RouterOS tools:

*   **Interface Monitoring:** Use `/interface ethernet monitor WAN` or `/interface bridge monitor bridge-LAN` to check interface status, link status, traffic, etc.
*   **DHCP Server Leases:**  `/ip dhcp-server lease print` to see active DHCP leases.
*   **System Resource Monitoring:** `/system resource print` to check CPU, memory, and disk usage of the router.
*   **Logging:** Configure logging to capture important events (DHCP, system errors, etc.) `/system logging add topics=dhcp-server,system,error action=disk` (example to log to disk). Use `/log print` to view logs.
*   **The Dude (MikroTik Monitoring Tool):** For more advanced graphical monitoring, consider using MikroTik's "The Dude" network monitoring application.

### 8.4 Disaster Recovery Steps

*   **Configuration Backup:** Regularly backup your RouterOS configuration using `/system backup save name=config_backup` (CLI) or via WinBox/WebFig. Store backups off-router (e.g., on a computer or cloud storage).
*   **Export Configuration Script:** Export the configuration to a script file: `/export file=config_script` (CLI) or via WinBox/WebFig. This creates a text file that can be easily reviewed and re-imported.
*   **Netinstall:** In case of severe router malfunction or password loss, use MikroTik Netinstall to re-install RouterOS. Download Netinstall and RouterOS `.npk` package from MikroTik website. Follow Netinstall documentation.
*   **Redundancy (Optional for SOHO):** For critical environments, consider a redundant router setup (VRRP or similar) for failover, but this is usually overkill for basic SOHO.
*   **Document Configuration:** Keep documentation of your IP addressing scheme, interface names, passwords, and backup procedures.

### 8.5 Automated Backup Scripts

This is a basic RouterOS script to automate configuration backups and save them to the router's disk. You can schedule this script to run periodically using `/system scheduler`.

```routeros
# --- Automated Backup Script ---
:local backupName ("config_backup_" . [:system clock get date format=yyyy-MM-dd] . "_" . [:system clock get time format=HH-mm-ss])
/system backup save name=$backupName

:log info ("Configuration backup saved as: " . $backupName)

# --- Optional: Cleanup old backups (keep last 7 backups) ---
:local backupCount [/file find name~"config_backup_"]
:local keepCount 7
:if ([ :len $backupCount ] > $keepCount ) do={
    :local backupsToDelete ([/file find name~"config_backup_" count=([:len $backupCount] - $keepCount)])
    :foreach backup in=$backupsToDelete do={
        /file remove $backup
        :log info ("Deleted old backup: " . $backup)
    }
}
```

**To schedule this script:**

```routeros
/system scheduler add name=daily_config_backup start-time=03:00 interval=1d on-event=daily_backup_script policy=ftp,reboot,read,write,policy,test,password,sensitive,romon
```

**Explanation:**

*   `daily_config_script`:  The script code above.
*   `start-time=03:00`: Script will run at 3:00 AM daily.
*   `interval=1d`: Run interval is 1 day.
*   `on-event=daily_backup_script`: Specifies the script to run.
*   `policy=ftp,reboot,read,write,policy,test,password,sensitive,romon`:  Assigns necessary permissions to the scheduler task. Adjust policies as needed for your security requirements.

This documentation provides a comprehensive guide to IP addressing in MikroTik RouterOS 6.x for SOHO environments. Remember to adapt the configurations and scripts to your specific network needs and security requirements. Always test configurations in a lab environment before deploying to production.
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