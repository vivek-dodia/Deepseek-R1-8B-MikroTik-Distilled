---
generated_at: 2025-02-03T21:40:56.598889
topic: Bonding Examples
category: High Availability
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

Okay, here is comprehensive documentation on MikroTik RouterOS Bonding Examples for SOHO environments using version 6.x, covering CLI and API configurations, debugging, security, performance, and SOHO-specific considerations, formatted in Markdown as requested.

---

## MikroTik RouterOS Bonding Examples for SOHO (v6.x)

**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic

### 1. Overview of Bonding

Bonding, also known as link aggregation or NIC teaming, combines multiple network interfaces into a single logical interface. This provides several benefits, especially in a SOHO environment:

*   **Increased Bandwidth:**  Aggregate the bandwidth of multiple links for faster data transfer.
*   **Link Redundancy (Failover):**  Maintain network connectivity even if one or more links fail.
*   **Load Balancing:** Distribute network traffic across multiple links for better performance.

In RouterOS, bonding is configured through the `/interface bonding` menu. This document focuses on basic bonding configurations suitable for SOHO setups using RouterOS v6.x.

### 2. Architecture Diagram Requirements

For a SOHO environment, a typical bonding setup might involve combining two or more WAN links (e.g., DSL, Cable) to increase internet bandwidth or provide redundancy.  Another scenario could be bonding LAN interfaces for increased bandwidth to a NAS or server within the SOHO network.

**Diagram using Mermaid Syntax:**

```mermaid
graph LR
    subgraph SOHO Network
        RouterOS -- "Bonding Interface (bond1)" --> NAS/Server
        RouterOS -- "Bonding Interface (bond2)" --> Internet
        Interface1(ether1) -- bond1
        Interface2(ether2) -- bond1
        Interface3(ether3) -- bond2
        Interface4(ether4) -- bond2
    end
    Internet -- ether3 & ether4 --> RouterOS
    NAS/Server -- ether1 & ether2 --> RouterOS
    style RouterOS fill:#f9f,stroke:#333,stroke-width:2px
    style NAS/Server fill:#ccf,stroke:#333,stroke-width:1px
    style Internet fill:#eee,stroke:#333,stroke-width:1px
    style Interface1 fill:#ddd,stroke:#333,stroke-width:1px
    style Interface2 fill:#ddd,stroke:#333,stroke-width:1px
    style Interface3 fill:#ddd,stroke:#333,stroke-width:1px
    style Interface4 fill:#ddd,stroke:#333,stroke-width:1px
```

**Diagram Description:**

*   **RouterOS:** Represents the MikroTik router acting as the central network device.
*   **NAS/Server:**  A Network Attached Storage or server within the SOHO network benefiting from increased bandwidth via bonding.
*   **Internet:** The external network connection.
*   **Interface1 (ether1), Interface2 (ether2), Interface3 (ether3), Interface4 (ether4):** Physical Ethernet interfaces on the MikroTik router.
*   **bond1:**  A bonding interface created by aggregating `ether1` and `ether2` for connecting to the NAS/Server.
*   **bond2:** A bonding interface created by aggregating `ether3` and `ether4` for connecting to the Internet.

### 3. CLI Configuration with Inline Comments

Here are CLI examples for configuring two common bonding modes: `balance-rr` (Round Robin) and `active-backup`.

#### 3.1. Balance-RR (Round Robin) Bonding

`balance-rr` distributes packets in sequential order across the bonded interfaces. This mode aims to increase throughput but might not be ideal for all applications due to potential out-of-order packet delivery.

```routeros
# Create the bonding interface
/interface bonding add name=bond1 mode=balance-rr transmit-hash-policy=layer2

# Add physical interfaces to the bonding interface
/interface bonding master=bond1 interface=ether1
/interface bonding master=bond1 interface=ether2

# Configure IP address for the bonding interface (if needed)
/ip address add address=192.168.10.1/24 interface=bond1 network=192.168.10.0

# Optional: Disable individual interfaces to manage them only through the bond
/interface disable ether1
/interface disable ether2

# Verify bonding status
/interface bonding print detail
```

**Inline Comments Explanation:**

*   `/interface bonding add name=bond1 mode=balance-rr transmit-hash-policy=layer2`: Creates a new bonding interface named `bond1` using `balance-rr` mode. `transmit-hash-policy=layer2` is a common setting for `balance-rr` in SOHO environments, using MAC addresses for load balancing.
*   `/interface bonding master=bond1 interface=ether1` & `/interface bonding master=bond1 interface=ether2`:  Adds physical interfaces `ether1` and `ether2` as slaves to the `bond1` master interface.
*   `/ip address add address=192.168.10.1/24 interface=bond1 network=192.168.10.0`: Assigns an IP address to the logical bonding interface `bond1`.
*   `/interface disable ether1` & `/interface disable ether2`:  Disables the individual physical interfaces to ensure traffic only flows through the bonding interface. This is optional but recommended for cleaner management.
*   `/interface bonding print detail`:  Shows detailed information about the bonding interface, including its mode, slaves, and status.

#### 3.2. Active-Backup Bonding

`active-backup` provides redundancy. One interface is active, and the others are in standby mode. If the active interface fails, a standby interface becomes active. This mode does not increase bandwidth but ensures high availability.

```routeros
# Create the bonding interface
/interface bonding add name=bond2 mode=active-backup primary=ether3 transmit-hash-policy=layer2

# Add physical interfaces to the bonding interface
/interface bonding master=bond2 interface=ether3
/interface bonding master=bond2 interface=ether4

# Configure IP address for the bonding interface (if needed)
/ip address add address=203.0.113.5/24 interface=bond2 network=203.0.113.0 gateway=203.0.113.1

# Optional: Disable individual interfaces to manage them only through the bond
/interface disable ether3
/interface disable ether4

# Verify bonding status
/interface bonding print detail
```

**Inline Comments Explanation:**

*   `/interface bonding add name=bond2 mode=active-backup primary=ether3 transmit-hash-policy=layer2`: Creates a bonding interface `bond2` in `active-backup` mode. `primary=ether3` sets `ether3` as the initial active interface.
*   `/interface bonding master=bond2 interface=ether3` & `/interface bonding master=bond2 interface=ether4`: Adds `ether3` and `ether4` as slaves to `bond2`.
*   `/ip address add ... gateway=...`:  Configures an IP address, network, and default gateway for the bonding interface `bond2`, typically for a WAN connection.
*   `/interface disable ether3` & `/interface disable ether4`:  Optional disabling of physical interfaces for cleaner management.
*   `/interface bonding print detail`:  Verifies the bonding configuration and status.

### 4. REST API Implementation (Python Code)

Here's a Python script using the `routeros_api` library to configure `balance-rr` bonding.  Ensure you have the library installed (`pip install routeros_api`).

```python
import routeros_api
import routeros_api.exceptions

# RouterOS connection details
HOST = 'your_router_ip'
USERNAME = 'api_user'
PASSWORD = 'your_api_password'

try:
    # Connect to RouterOS API
    api = routeros_api.RouterOsApiPool(HOST, username=USERNAME, password=PASSWORD, plaintext_login=True)
    connection = api.get_connection()

    # Get the 'interface bonding' resource
    bonding_resource = connection.get_resource('/interface/bonding')

    # Create bonding interface 'bond1' in balance-rr mode
    bonding_resource.add(name='bond1', mode='balance-rr', transmit_hash_policy='layer2')
    print("Bonding interface 'bond1' created in balance-rr mode.")

    # Get the 'interface' resource
    interface_resource = connection.get_resource('/interface')

    # Add ether1 and ether2 to bond1
    interface_resource.set(id='ether1', master='bond1')
    interface_resource.set(id='ether2', master='bond1')
    print("Interfaces ether1 and ether2 added to bond1.")

    # Get the 'ip address' resource
    ip_address_resource = connection.get_resource('/ip/address')

    # Add IP address to bond1
    ip_address_resource.add(address='192.168.10.1/24', interface='bond1', network='192.168.10.0')
    print("IP address configured on bond1.")

    # Disable individual interfaces (optional)
    interface_resource.set(id='ether1', disabled=True)
    interface_resource.set(id='ether2', disabled=True)
    print("Individual interfaces ether1 and ether2 disabled (optional).")

except routeros_api.exceptions.RouterOsApiError as e:
    print(f"RouterOS API Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'api' in locals() and api:
        api.close()
```

**Python Code Explanation:**

*   **Import libraries:** Imports `routeros_api` and exception handling.
*   **Connection details:** Defines variables for RouterOS IP, username, and password. **Replace placeholders with your actual credentials.** `plaintext_login=True` is used for simplicity but consider secure authentication in production.
*   **Connect to API:** Establishes a connection to the RouterOS API using `RouterOsApiPool`.
*   **Get resources:** Obtains resources for `/interface/bonding`, `/interface`, and `/ip/address`.
*   **Create bonding interface:** Uses `bonding_resource.add()` to create `bond1` in `balance-rr` mode.
*   **Add interfaces to bond:** Uses `interface_resource.set()` to set `master='bond1'` for `ether1` and `ether2`, making them slaves of `bond1`.
*   **Configure IP address:** Uses `ip_address_resource.add()` to assign an IP address to `bond1`.
*   **Disable individual interfaces (optional):** Uses `interface_resource.set()` to disable `ether1` and `ether2`.
*   **Error handling:** Includes `try...except` blocks to catch `RouterOsApiError` and general exceptions, printing error messages.
*   **Close API connection:** Uses `api.close()` in the `finally` block to ensure the API connection is closed.

**To use this script:**

1.  Install `routeros_api`: `pip install routeros_api`
2.  Replace placeholders in the script with your RouterOS details.
3.  Run the script: `python your_script_name.py`

### 5. Common Debugging Scenarios

*   **Bonding Interface Not Active:**
    *   **Check Physical Links:** Verify that all physical cables are properly connected and functional. Check interface status in `/interface ethernet print`.
    *   **Interface Status in Bonding:** Use `/interface bonding print detail` to check the status of the bonding interface and its slaves. Look for "slaves" and "status" fields. Ensure slaves are "enabled" and "active".
    *   **Configuration Errors:** Double-check the bonding mode, slave interfaces, and IP address configurations.
    *   **Mismatched Bonding Modes (if connecting to another bonded device):** If bonding with another device, ensure both sides use compatible bonding modes.

*   **Slow Throughput with `balance-rr`:**
    *   **Packet Reordering:** `balance-rr` can lead to out-of-order packets, which might impact performance for some applications. Consider `balance-xor` or `active-backup` if this is suspected.
    *   **Incorrect `transmit-hash-policy`:** Experiment with different `transmit-hash-policy` values (layer2, layer23, layer34) to find the best distribution for your traffic.
    *   **Underlying Link Issues:** Individual links might have issues (e.g., speed mismatch, errors) affecting overall performance. Test each link individually.

*   **Failover Issues in `active-backup`:**
    *   **Link Monitoring:** Ensure link monitoring is enabled and configured correctly. RouterOS uses link monitoring by default.
    *   **Primary Interface Failure Detection:** Test failover by physically disconnecting the primary interface. Monitor the bonding interface status to see if failover occurs.
    *   **Configuration Errors:** Verify `primary` interface setting and that standby interfaces are correctly configured.

**Debugging Commands:**

*   `/interface bonding print detail`:  Detailed bonding interface information.
*   `/interface ethernet print stats`:  Ethernet interface statistics (errors, drops).
*   `/ping <destination>`:  Test connectivity through the bonding interface.
*   `/tool sniffer quick interface=bond1`:  Capture packets on the bonding interface to analyze traffic distribution.

### 6. Version-Specific Considerations (v6.x)

*   **Limited Bonding Modes:** RouterOS v6.x supports a subset of bonding modes compared to Linux bonding. Common modes like `balance-rr`, `active-backup`, `balance-xor`, `broadcast`, `802.3ad`, `balance-tlb`, and `balance-alb` are available, but newer modes might be missing.
*   **Driver Compatibility:** Ensure the Ethernet interfaces you are using are well-supported in RouterOS v6.x. Check the MikroTik documentation for compatible hardware.
*   **API Version:** The REST API in RouterOS v6.x might have slight differences compared to newer versions. Refer to the RouterOS v6.x API documentation if encountering API-related issues.
*   **Software Updates:** RouterOS v6.x is older. Consider upgrading to a stable v7 release for bug fixes, security updates, and potentially improved bonding features and performance, if hardware permits. However, always test upgrades in a non-production environment first.

### 7. Security Hardening Measures

*   **Physical Security:** Secure the physical access to your MikroTik router and the Ethernet cables used for bonding. Prevent unauthorized physical access that could lead to cable disconnection or tampering.
*   **Access Control:** Implement strong passwords for RouterOS user accounts and restrict API access to authorized users and IP addresses only.
*   **Disable Unnecessary Services:** Disable any RouterOS services or features that are not required for your SOHO environment to reduce the attack surface.
*   **Firewall Rules:** Implement a robust firewall configuration to protect your SOHO network and the MikroTik router itself. Only allow necessary inbound and outbound traffic.
*   **Regular Updates:** Although RouterOS v6.x is older, if you must use it, ensure you apply any available security patches from MikroTik. Upgrading to a newer stable RouterOS version (v7) is generally recommended for better security in the long run.
*   **Monitoring and Logging:** Enable logging for bonding interface events and security-related events. Regularly monitor logs for suspicious activity.

### 8. Performance Optimization Tips

*   **Choose the Right Bonding Mode:** Select the bonding mode that best matches your needs and traffic patterns.
    *   `balance-rr`:  Potentially higher aggregate throughput, but might cause packet reordering. Good for bulk data transfer.
    *   `balance-xor`:  Good balance of load distribution and packet ordering. Suitable for general SOHO use.
    *   `active-backup`:  No bandwidth aggregation, focuses on redundancy. Use when high availability is paramount.
*   **`transmit-hash-policy` Tuning:** Experiment with different `transmit-hash-policy` settings (`layer2`, `layer23`, `layer34`) to optimize load distribution based on your network traffic characteristics. `layer2` is often sufficient for SOHO.
*   **Interface Selection:** Use identical or very similar Ethernet interfaces for bonding in terms of speed, latency, and capabilities for optimal performance.
*   **MTU Configuration:** Ensure consistent MTU (Maximum Transmission Unit) settings across all bonded interfaces and throughout your network to avoid fragmentation and performance degradation.
*   **Queue Configuration:**  Review and optimize RouterOS queue settings (Simple Queues, Queue Tree) to manage traffic flow through the bonding interface, especially if you have bandwidth limitations or need to prioritize certain types of traffic.
*   **CPU Load:** Bonding, especially in more complex modes or with heavy traffic, can increase CPU load on the router. Monitor CPU usage and consider upgrading to a more powerful MikroTik router if CPU becomes a bottleneck.

### 9. SOHO Specific Requirements

#### 9.1. Real-world Deployment Examples

*   **Combining DSL Lines:** In areas with slow DSL speeds, bonding two DSL lines in `balance-rr` or `balance-xor` mode can significantly increase internet download and upload speeds for a SOHO. This is beneficial for online meetings, file sharing, and general internet browsing for multiple users.
*   **Increased LAN Bandwidth to NAS:** Bonding two Gigabit Ethernet interfaces in `balance-rr` or `802.3ad` (if supported by NAS and switch) mode can double the bandwidth between the MikroTik router and a NAS device. This is useful for faster file access, backups, and media streaming within the SOHO network.
*   **Redundant WAN Connection:** Using `active-backup` bonding with two different internet connections (e.g., Cable and DSL) provides redundancy. If the primary connection fails, the backup connection automatically takes over, ensuring continuous internet access for the SOHO.
*   **Wi-Fi Backhaul Improvement (Point-to-Point Wireless Bridge):** In scenarios where a wired connection is not feasible between buildings in a small office, bonding two wireless links in a point-to-point bridge configuration can increase the bandwidth and reliability of the wireless backhaul.

#### 9.2. Scalability Considerations

For a typical SOHO environment, bonding a few interfaces is often sufficient. However, consider these scalability aspects:

*   **Number of Interfaces:**  SOHO routers typically have a limited number of Ethernet interfaces. Bonding is constrained by the available physical interfaces.
*   **Router CPU and Memory:**  Bonding increases the processing load on the router. For very high bandwidth or a large number of bonded interfaces, a more powerful MikroTik router with more CPU and memory might be needed.
*   **Beyond Bonding:** For larger networks or more complex bandwidth requirements, consider other solutions beyond basic bonding, such as:
    *   **Routing Protocols (OSPF, BGP):** For more sophisticated load balancing and path selection across multiple WAN links.
    *   **Load Balancing Appliances:** Dedicated load balancers for advanced traffic distribution and application-aware routing.
    *   **Higher Bandwidth Single Links:** If possible, upgrade to faster single internet connections or LAN infrastructure (e.g., 10 Gigabit Ethernet) instead of relying solely on bonding.

#### 9.3. Monitoring Configurations

*   **RouterOS Monitoring:**
    *   **`/interface bonding print detail`:** Regularly check the status of bonding interfaces and their slaves in the CLI or WinBox.
    *   **Resource Monitoring:** Monitor CPU, memory, and interface traffic using RouterOS's built-in monitoring tools (`/tool/profile`, `/interface ethernet monitor`).
    *   **Logging:** Configure logging for bonding interface events (`/system logging`) to track interface status changes and potential issues.
*   **SNMP Monitoring (Optional):** For more advanced monitoring, configure SNMP on your MikroTik router and use an external SNMP monitoring system (e.g., Zabbix, PRTG) to track bonding interface statistics, up/down status, and traffic.

#### 9.4. Disaster Recovery Steps

*   **Active-Backup Failover (Automatic):** In `active-backup` mode, failover is automatic. If the primary interface fails, the backup interface should take over. Verify this by testing primary link failure.
*   **`balance-rr` and `balance-xor` Degradation:** In modes like `balance-rr` or `balance-xor`, if one link fails, the bonding interface will continue to operate with reduced bandwidth. The network will remain functional, but performance will be degraded.
*   **Troubleshooting Link Failures:**
    1.  **Check Physical Connections:**  First, verify all physical cable connections.
    2.  **Interface Status:** Use `/interface ethernet print` and `/interface bonding print detail` to identify failed interfaces.
    3.  **Logs:** Check RouterOS logs for error messages related to interfaces or bonding.
    4.  **Replace Faulty Hardware:** If a physical interface or cable is faulty, replace it.
    5.  **Configuration Review:** Re-examine your bonding configuration to ensure it is correct.

#### 9.5. Automated Backup Scripts

It is crucial to regularly backup your RouterOS configuration. Here's a basic RouterOS script to automate configuration backups and save them to the router's disk:

```routeros
/system script add name=backup_config owner=admin policy=write source={
    :local backup_file ("backup_" . [/system clock get date format=yyyy-MM-dd] . "_" . [/system clock get time format=HH-mm-ss] . ".backup")
    /system backup save name=$backup_file
    :log info ("Configuration backup saved to file: " . $backup_file)
}
/system scheduler add name=daily_config_backup interval=1d start-time=03:00:00 on-event=backup_config policy=write
```

**Script Explanation:**

*   **`/system script add ...`:** Creates a new script named `backup_config`.
    *   `name=backup_config`: Script name.
    *   `owner=admin`: Owner of the script.
    *   `policy=write`: Required policies to execute backup commands.
    *   `source={ ... }`: Script code block.
*   **Script Code:**
    *   `:local backup_file ...`: Creates a local variable `backup_file` with a filename including the date and time.
    *   `/system backup save name=$backup_file`: Executes the backup command and saves the backup to a file with the generated name.
    *   `:log info ...`: Logs an informational message indicating the backup file name.
*   **`/system scheduler add ...`:** Creates a scheduler to run the `backup_config` script daily.
    *   `name=daily_config_backup`: Scheduler name.
    *   `interval=1d`: Run every day.
    *   `start-time=03:00:00`: Run at 3:00 AM daily.
    *   `on-event=backup_config`: Execute the `backup_config` script when the scheduler runs.
    *   `policy=write`: Required policies for the scheduler to execute the script.

**To restore from backup:**

1.  Upload the `.backup` file to your RouterOS (using WinBox Files, WebFig, or FTP).
2.  In RouterOS CLI: `/system backup load name=your_backup_file.backup`
3.  Reboot the router: `/system reboot`

**Important Considerations for Backups:**

*   **Backup Location:** This script saves backups to the router's local disk. For better disaster recovery, consider storing backups remotely (e.g., using FTP, SCP, or cloud storage) using more advanced scripting and tools.
*   **Security of Backups:** Securely store and manage backup files, as they contain sensitive router configuration information.
*   **Testing Backups:** Regularly test your backup and restore process to ensure it works correctly when needed.

---

This comprehensive documentation provides a solid foundation for understanding and implementing basic bonding configurations in a MikroTik RouterOS v6.x SOHO environment. Remember to adapt these examples to your specific network requirements and always test configurations in a non-production environment before deploying them in a live network.

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