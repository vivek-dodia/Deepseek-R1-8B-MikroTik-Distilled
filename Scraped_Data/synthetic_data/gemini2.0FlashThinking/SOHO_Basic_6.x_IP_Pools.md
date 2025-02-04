---
generated_at: 2025-02-03T21:04:02.674936
topic: IP Pools
category: Core Networking
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Documentation: IP Pools (v6.x - SOHO)

**Document Version:** 1.0
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic

**1. Introduction to IP Pools**

In MikroTik RouterOS, IP Pools are essential for dynamic IP address allocation. They define a range of IP addresses that can be assigned to network devices, primarily through DHCP servers or PPP profiles.  For SOHO environments, IP Pools simplify network management by automating IP address assignment and preventing IP address conflicts.

**Key Benefits in SOHO:**

* **Simplified IP Management:** Automatic IP assignment reduces manual configuration on end devices.
* **Centralized Control:** Manage IP address ranges from a single MikroTik router.
* **Efficient Address Utilization:** Dynamic allocation ensures IP addresses are used only when needed.
* **Scalability:** Easily expand or modify IP address ranges as the network grows.

**2. Architecture Diagram Requirements**

This diagram illustrates a typical SOHO network utilizing IP Pools for DHCP address assignment to LAN clients.

```mermaid
graph LR
    Internet --> Router(MikroTik RouterOS)
    Router -- WAN Interface --> Internet
    Router -- LAN Interface --> Switch
    Switch --> Client1(Client Device 1)
    Switch --> Client2(Client Device 2)
    Switch --> ClientN(Client Device N)

    subgraph SOHO Network
        Router
        Switch
        Client1
        Client2
        ClientN
    end

    subgraph IP Pool Configuration
        IPPool(IP Pool: SOHO_LAN_Pool)
        DHCP_Server(DHCP Server on LAN)
        DHCP_Server --> IPPool
        DHCP_Server --> Switch
    end

    style Router fill:#f9f,stroke:#333,stroke-width:2px
    style IPPool fill:#ccf,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5
    style DHCP_Server fill:#cfc,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5

    linkStyle 0,1,2,3,4,5 stroke:#333,stroke-width:2px;
    linkStyle 6,7,8 stroke:#777,stroke-width:1px,stroke-dasharray: 5 5;

    classDef routerStyle fill:#f9f,stroke:#333,stroke-width:2px;
    class Router routerStyle;
```

**Diagram Explanation:**

* **Internet:** Represents the external network.
* **MikroTik RouterOS:** The central router managing the SOHO network.
* **WAN Interface:** Connects the router to the internet.
* **LAN Interface:** Connects the router to the internal SOHO network.
* **Switch:**  A network switch distributing network connectivity within the LAN.
* **Client Devices:** End-user devices (computers, smartphones, etc.) within the SOHO network.
* **IP Pool (SOHO_LAN_Pool):**  Defines the range of IP addresses to be assigned to LAN clients.
* **DHCP Server on LAN:**  Service running on the MikroTik router that uses the IP Pool to dynamically assign IP addresses to devices connected to the LAN interface.

**3. CLI Configuration with Inline Comments**

This section provides CLI commands to create and manage IP Pools.

```routeros
/ip pool
# Add a new IP Pool named 'soho_lan_pool'
add name=soho_lan_pool ranges=192.168.88.10-192.168.88.254
# Explanation:
# - /ip pool:  Navigates to the IP Pool configuration menu.
# - add:       Command to add a new IP Pool.
# - name=soho_lan_pool:  Sets the name of the IP Pool for easy identification.
# - ranges=192.168.88.10-192.168.88.254: Defines the IP address range.
#                                       This pool will provide addresses from 192.168.88.10 to 192.168.88.254 inclusive.

# View the configured IP Pools
print
# Explanation:
# - print: Displays the list of configured IP Pools with their properties.

# Remove an IP Pool (use with caution!)
# remove soho_lan_pool
# Explanation:
# - remove soho_lan_pool: Deletes the IP Pool named 'soho_lan_pool'.
#                          Replace 'soho_lan_pool' with the name or number of the pool you want to remove.

# Modify an existing IP Pool - Example: Change the range
set soho_lan_pool ranges=192.168.88.20-192.168.88.200
# Explanation:
# - set soho_lan_pool:  Selects the IP Pool named 'soho_lan_pool' for modification.
# - ranges=192.168.88.20-192.168.88.200: Updates the IP address range of the 'soho_lan_pool'.

# Add multiple ranges to a single IP Pool
set soho_lan_pool ranges=192.168.88.20-192.168.88.200,192.168.88.220-192.168.88.240
# Explanation:
# - You can specify comma-separated ranges to include multiple non-contiguous address blocks in a single pool.

# Check IP Pool usage (shows allocated addresses)
print detail
# Explanation:
# - print detail:  Displays detailed information about each IP Pool, including allocated addresses and their leases (if associated with DHCP).
```

**4. REST API Implementation (Python Code)**

This Python script demonstrates how to manage IP Pools using the MikroTik RouterOS REST API.  It assumes you have the `requests` library installed (`pip install requests`).

```python
import requests
import json

ROUTER_IP = "your_router_ip"  # Replace with your Router IP Address
ROUTER_USER = "api_user"      # Replace with your API username
ROUTER_PASSWORD = "api_password" # Replace with your API password

BASE_URL = f"https://{ROUTER_IP}/rest"
HEADERS = {'Content-Type': 'application/json'}

def api_request(method, endpoint, data=None):
    """Handles API requests and error handling."""
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, headers=HEADERS, auth=(ROUTER_USER, ROUTER_PASSWORD), json=data, verify=False) # verify=False for self-signed certs in SOHO, consider cert verification in production
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        if response.text: # Check if response has content before trying to parse JSON
            return response.json()
        else:
            return None # For requests that don't return JSON content (e.g., delete)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.text:
            print(f"Error details: {response.text}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None

def create_ip_pool(pool_name, ip_range):
    """Creates a new IP Pool."""
    data = {
        "name": pool_name,
        "ranges": ip_range
    }
    result = api_request("POST", "/ip/pool", data=data)
    if result:
        print(f"IP Pool '{pool_name}' created successfully.")
    else:
        print(f"Failed to create IP Pool '{pool_name}'.")

def get_ip_pools():
    """Retrieves a list of all IP Pools."""
    pools = api_request("GET", "/ip/pool")
    if pools:
        print("List of IP Pools:")
        for pool in pools:
            print(f"- Name: {pool['name']}, Ranges: {pool['ranges']}")
    else:
        print("Failed to retrieve IP Pools.")

def delete_ip_pool(pool_name):
    """Deletes an IP Pool by name."""
    pools = api_request("GET", "/ip/pool") # Get list to find the .id based on name
    if pools:
        pool_id_to_delete = None
        for pool in pools:
            if pool['name'] == pool_name:
                pool_id_to_delete = pool['.id']
                break
        if pool_id_to_delete:
            result = api_request("DELETE", f"/ip/pool/{pool_id_to_delete}")
            if result is None: # DELETE often returns no content on success
                print(f"IP Pool '{pool_name}' deleted successfully.")
            else:
                print(f"Failed to delete IP Pool '{pool_name}'.")
        else:
            print(f"IP Pool '{pool_name}' not found.")
    else:
        print("Failed to retrieve IP Pools to perform deletion.")


if __name__ == "__main__":
    # Example Usage:
    create_ip_pool("soho_vpn_pool", "10.10.10.10-10.10.10.50")
    get_ip_pools()
    # delete_ip_pool("soho_vpn_pool") # Uncomment to delete the pool after testing
```

**To run this script:**

1.  **Install `requests`:** `pip install requests`
2.  **Replace placeholders:** Update `ROUTER_IP`, `ROUTER_USER`, and `ROUTER_PASSWORD` with your MikroTik router's details.
3.  **Execute the script:** `python your_script_name.py`

**5. Real-world SOHO Deployment Examples**

**a) DHCP Server for LAN Clients:**

*   **Scenario:**  Assign IP addresses dynamically to all devices connected to the LAN network (wired and wireless).
*   **IP Pool Usage:** Create an IP Pool (`soho_lan_pool`) covering the desired LAN subnet range (e.g., 192.168.88.10-192.168.88.254). Configure the DHCP server on the LAN interface to use this pool.
*   **CLI Configuration (DHCP Server):**
    ```routeros
    /ip dhcp-server
    add name=dhcp_lan interface=ether2 address-pool=soho_lan_pool lease-time=1d
    /ip dhcp-server network
    add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1
    ```
    *   `ether2` should be replaced with your LAN interface name.
    *   `192.168.88.0/24` and `192.168.88.1` should match your LAN network configuration.

**b) VPN Clients (PPTP/L2TP/OpenVPN):**

*   **Scenario:** Assign IP addresses to clients connecting via VPN.
*   **IP Pool Usage:** Create a dedicated IP Pool (`soho_vpn_pool`) for VPN clients (e.g., 10.10.10.10-10.10.10.50). Configure the PPP profile used for VPN connections to use this pool.
*   **CLI Configuration (PPP Profile - Example PPTP):**
    ```routeros
    /ppp profile
    add name=pptp_profile local-address=192.168.88.1 remote-address=soho_vpn_pool use-mpls=default use-compression=default use-encryption=required only-one=default change-tcp-mss=yes
    /interface pptp-server server
    set enabled=yes default-profile=pptp_profile
    ```
    *   `192.168.88.1` is an example of the local address for the VPN server.
    *   `pptp_profile` is the profile name; adjust as needed.

**6. Scalability Considerations**

For SOHO environments, IP Pools generally provide sufficient scalability.

*   **Pool Size:**  Ensure the IP Pool range is large enough to accommodate the maximum number of devices expected to connect simultaneously. For a typical SOHO, a /24 subnet (254 usable addresses) is often sufficient.
*   **Multiple Pools:** If you have distinct network segments (e.g., guest Wi-Fi, IoT devices), you can create separate IP Pools for each segment to maintain network segmentation and organization.
*   **Address Exhaustion:** In very large SOHO deployments or scenarios with rapidly changing devices (e.g., temporary events), monitor IP Pool usage to prevent address exhaustion. Use longer lease times or expand the pool range if needed.
*   **RouterOS Limitations:** RouterOS can handle a large number of IP Pools and addresses, generally exceeding SOHO needs. However, very complex configurations or extremely large pools might require more powerful hardware.

**7. Monitoring Configurations**

**a) CLI Monitoring:**

*   **Check Pool Usage:** Use `/ip pool print detail` to see the allocated addresses and remaining addresses in each pool.
*   **DHCP Leases:**  View active DHCP leases using `/ip dhcp-server lease print`. This shows which devices have been assigned addresses from the IP Pool.
*   **Logs:** Configure DHCP server logging (`/system logging add topics=dhcp action=memory`) to track DHCP address assignments and potential issues.

**b) SNMP Monitoring (Basic):**

*   MikroTik RouterOS supports SNMP, but detailed IP Pool usage OIDs are not directly available by default. You can monitor overall system resource usage (CPU, memory) which might indirectly reflect IP Pool activity.
*   For more advanced monitoring, consider using MikroTik's The Dude network monitoring tool or other SNMP-based network monitoring systems.

**c) WebFig/Winbox Monitoring:**

*   **WebFig/Winbox GUI:**  Navigate to `IP -> Pools` to view the list of IP Pools and their ranges.  Click on a pool to see basic details. For more detailed usage, CLI is generally more efficient.

**8. Disaster Recovery Steps**

**a) Configuration Backup:**

*   **Automated Backup Script (see section 9):** Regularly back up your RouterOS configuration, including IP Pool settings.
*   **Manual Backup:** Use Winbox or WebFig to export the configuration to a file (`Files -> Backup`). Store backups securely off-router.

**b) Restoration Procedure:**

1.  **Router Replacement/Reset:** If the router fails or is reset, perform a factory reset or install a new router.
2.  **Configuration Import:** Import the backup configuration file using Winbox/WebFig (`Files -> Restore`).
3.  **Verification:** After restoration, verify IP Pool configurations using `/ip pool print`. Test DHCP or VPN connections to ensure IP address assignment is working as expected.

**c) Disaster Recovery IP Pool Best Practices:**

*   **Document IP Pool Configuration:** Keep a separate record of your IP Pool names, ranges, and associated services (DHCP, VPN) for easy reference in case of restoration without a backup.
*   **Regular Backups:** Automate configuration backups to minimize data loss in case of failure.
*   **Test Restoration:** Periodically test the backup and restoration process to ensure it works correctly.

**9. Automated Backup Scripts**

This RouterOS script can be scheduled to automatically back up the router configuration, including IP Pool settings.

```routeros
# Script Name: auto_config_backup
# Description: Automates RouterOS configuration backup.

:local backup_filename ("backup_" . [:system clock get date format=yyyy-MM-dd] . "_" . [:system clock get time format=HH-mm-ss] . ".backup")
:local backup_path "/disk1/backups/" # Adjust backup path as needed

# Create backup directory if it doesn't exist (Optional - adjust if needed)
/file print file="$backup_path" do={
    :if ([:len $file] = 0) do={
        /file create directory="$backup_path"
        :log info "Backup directory created: $backup_path"
    }
}

/system backup save name=($backup_path . $backup_filename) dont-encrypt=yes
:log info "Configuration backup saved to: $backup_path$backup_filename"

# Optional: Email notification (configure email settings first - /tool email)
# /tool email send to="your_email@example.com" subject="RouterOS Backup Successful" body="Router configuration backup successful. File: $backup_path$backup_filename"

# Schedule this script to run daily or weekly using /system scheduler
# Example: Run daily at 3:00 AM
/system scheduler
add name="daily_config_backup" start-time=03:00:00 interval=1d on-event=auto_config_backup policy=write,policy,read,test,password,sensitive,romon
```

**To use this script:**

1.  **Copy the script** into the RouterOS terminal.
2.  **Adjust variables:**
    *   `backup_path`:  Change `/disk1/backups/` to your desired backup directory (ensure disk1 is mounted and writable).
    *   Email settings (optional): Configure `/tool email` if you want email notifications.
3.  **Create a scheduler:**  The example scheduler command is included in the script comments. Adapt the `start-time` and `interval` as needed.

**10. Common Debugging Scenarios**

**a) IP Pool Exhaustion:**

*   **Symptom:** Devices fail to get IP addresses via DHCP.
*   **Troubleshooting:**
    1.  Check IP Pool usage: `/ip pool print detail`. Verify if the pool is full (`allocated-addresses` close to `ranges` size).
    2.  Increase pool range or reduce lease time in DHCP server settings.
    3.  Review DHCP leases: `/ip dhcp-server lease print` to identify any long-held leases or potential lease exhaustion.

**b) Incorrect IP Address Assignment:**

*   **Symptom:** Devices get IP addresses outside the expected range or from the wrong pool.
*   **Troubleshooting:**
    1.  Verify DHCP server configuration: `/ip dhcp-server print`. Ensure the `address-pool` setting is correct and the `interface` is the intended LAN interface.
    2.  Check IP Pool ranges: `/ip pool print`. Confirm the IP Pool `ranges` are correctly defined.
    3.  Review network configuration: Ensure there are no overlapping IP ranges or conflicting DHCP servers on the network.

**c) API Connectivity Issues:**

*   **Symptom:** Python API script fails to connect to the router or execute commands.
*   **Troubleshooting:**
    1.  Verify API service is enabled: `/ip service print`. Ensure `api` and/or `api-ssl` are enabled.
    2.  Check firewall rules: Ensure firewall rules on the router are not blocking API access (port 80 for API, 443 for API-SSL).
    3.  Verify API credentials: Double-check `ROUTER_USER` and `ROUTER_PASSWORD` in the Python script.
    4.  Test connectivity: `ping` the router IP from the machine running the Python script.
    5.  Enable API logging ( `/system logging add topics=api action=memory` ) on the router to check for API access errors in the logs (`/log print`).

**11. Version-Specific Considerations (v6.x)**

*   **Feature Stability:** IP Pool functionality is mature and stable in v6.x.
*   **API Version:** Ensure your API client library (Python `requests` in this example) is compatible with the RouterOS v6.x API. REST API functionality is well-established in v6.x.
*   **Resource Limits:** While v6.x is generally capable for SOHO, older hardware running v6.x might have resource limitations if managing extremely large IP Pools or very high DHCP lease activity. Modern MikroTik hardware easily handles SOHO scale IP Pool needs with v6.x.
*   **Security Patches:** Ensure you are running the latest stable version of v6.x to benefit from any security patches released for the v6 branch.

**12. Security Hardening Measures**

*   **API Access Control:**
    *   Use strong passwords for API users.
    *   Restrict API access to specific IP addresses or networks using firewall rules if possible.
    *   Disable API services (`api` and `api-ssl`) when not actively used for management.
*   **DHCP Security:**
    *   Enable DHCP Snooping on managed switches if available to prevent rogue DHCP servers.
    *   Consider MAC address filtering in DHCP server settings for tighter control (less practical in dynamic SOHO environments).
*   **RouterOS Security:**
    *   Keep RouterOS software updated with the latest stable version.
    *   Disable unnecessary services on the router.
    *   Implement a strong firewall configuration (as documented in separate MikroTik firewall documentation).

**13. Performance Optimization Tips**

*   **IP Pool Size:**  Avoid excessively large IP Pools if not needed.  Smaller, well-defined pools can improve management efficiency.
*   **Lease Time:** Set appropriate DHCP lease times. Shorter lease times can increase DHCP traffic but free up addresses faster. Longer lease times reduce DHCP traffic but might lead to address exhaustion in rapidly changing environments. For typical SOHO, 1 day (1d) is often a good balance.
*   **Hardware Resources:** For very large SOHO environments or high DHCP activity, ensure the MikroTik router has sufficient CPU and memory resources. Modern MikroTik routers generally have ample resources for typical SOHO IP Pool operations.
*   **Minimize API Calls:** When using the API, optimize your scripts to minimize the number of API calls, especially for frequent operations. Batch operations or efficient data retrieval can improve performance.

**Comparative Table: CLI vs. API for IP Pool Management**

| Feature          | CLI (Command Line Interface)          | API (Application Programming Interface)          |
|-----------------|---------------------------------------|-------------------------------------------------|
| **Ease of Use (Interactive)** | Excellent for direct, interactive configuration. | Less intuitive for interactive use; requires scripting. |
| **Automation**   | Limited scripting capabilities (RouterOS script language). | Excellent for automation and integration with other systems. |
| **Scripting Language** | RouterOS script language (simple but limited). | Any language that can make HTTP requests (Python, etc.). |
| **Remote Management** | SSH/Telnet access required.          | HTTP/HTTPS based, more flexible for remote access. |
| **Error Handling** | Basic error messages in CLI.          | More robust error handling possible in scripting. |
| **Bulk Operations** | Can be less efficient for complex bulk operations. | Well-suited for bulk operations and data manipulation. |
| **Learning Curve** | Relatively easy to learn for basic tasks. | Steeper learning curve, requires programming knowledge. |
| **Best Use Case (SOHO Basic)** | Quick, one-off configurations, basic management. | Automation, integration with monitoring/management tools, complex or repetitive tasks. |

This comprehensive documentation provides a solid foundation for understanding and managing IP Pools in MikroTik RouterOS v6.x for SOHO environments. Remember to adapt these configurations and recommendations to your specific network needs and security requirements.

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