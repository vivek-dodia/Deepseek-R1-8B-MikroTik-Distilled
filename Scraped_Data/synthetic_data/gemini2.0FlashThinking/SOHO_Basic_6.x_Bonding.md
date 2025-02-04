---
generated_at: 2025-02-03T21:40:01.204974
topic: Bonding
category: High Availability
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Bonding Documentation (v6.x, SOHO)

**Topic:** Bonding
**RouterOS Version:** 6.x
**Network Scale:** SOHO
**Complexity Level:** Basic

**1. Introduction to Bonding**

Bonding, also known as link aggregation or port trunking, combines multiple network interfaces into a single logical interface. This enhances network performance by increasing bandwidth, providing link redundancy for fault tolerance, and improving network resilience. In a SOHO (Small Office/Home Office) environment, bonding can be particularly useful for:

*   **Increased Bandwidth:**  Aggregating bandwidth from multiple internet connections or local network links.
*   **Link Redundancy:** Ensuring network connectivity even if one link fails, crucial for reliable internet access or critical internal services.
*   **Improved Throughput:** Enhancing data transfer speeds for bandwidth-intensive applications like media streaming, file sharing, or online gaming.

This document focuses on basic bonding configurations suitable for SOHO networks using MikroTik RouterOS v6.x.

**2. Architecture Diagram Requirements**

For a typical SOHO bonding setup, we will consider bonding two Ethernet interfaces to increase bandwidth or provide redundancy for a LAN connection.

```mermaid
graph LR
    A[MikroTik Router (RouterOS)] --> B{Bonding Interface (bond1)};
    B -- Member Interface (ether2) --> C[Switch/LAN Devices];
    B -- Member Interface (ether3) --> C;
    D[Uplink Interface (ether1 - WAN)] --> A;

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#eee,stroke:#333,stroke-width:1px
    style D fill:#ddd,stroke:#333,stroke-width:1px

    subgraph SOHO LAN Network
        C
    end

    subgraph WAN Connection
        D
    end

    linkStyle 0,1,2,3 stroke-width:2px,stroke:#555;
```

**Diagram Explanation:**

*   **MikroTik Router (RouterOS):** Represents the MikroTik device running RouterOS.
*   **Bonding Interface (bond1):** The logical bonded interface created on the MikroTik router.
*   **Member Interface (ether2, ether3):** Physical Ethernet interfaces (e.g., `ether2` and `ether3`) that are members of the `bond1` interface.
*   **Switch/LAN Devices:** Represents the network switch and devices connected to the LAN side of the MikroTik router.
*   **Uplink Interface (ether1 - WAN):**  Represents the interface connected to the upstream network (e.g., internet modem).

**3. CLI Configuration with Inline Comments**

This section provides CLI commands to configure a basic Active-Backup bonding setup. Active-Backup mode provides redundancy; one link is active while the other is in standby, taking over if the active link fails.

```routeros
# 1. Create the bonding interface
/interface bonding add name=bond1 mode=active-backup primary=ether2 slaves=ether2,ether3

# Explanation:
# /interface bonding add: Command to create a new bonding interface.
# name=bond1:  Assigns the name 'bond1' to the bonding interface.
# mode=active-backup: Sets the bonding mode to Active-Backup for redundancy.
# primary=ether2:  Specifies 'ether2' as the primary (active) interface initially.
# slaves=ether2,ether3:  Adds 'ether2' and 'ether3' as member interfaces (slaves) of the bond.

# 2. Assign an IP address to the bonding interface (e.g., for the LAN network)
/ip address add address=192.168.88.1/24 interface=bond1 network=192.168.88.0

# Explanation:
# /ip address add: Command to add an IP address.
# address=192.168.88.1/24:  Assigns the IP address 192.168.88.1 with a /24 subnet mask to the bond1 interface.
# interface=bond1:  Applies the IP address to the 'bond1' interface.
# network=192.168.88.0:  Specifies the network address.

# 3. Disable IP addresses on the member interfaces (ether2 and ether3) if they had any previously.
/ip address remove [find interface=ether2]
/ip address remove [find interface=ether3]

# Explanation:
# /ip address remove: Command to remove an IP address.
# [find interface=ether2]:  Dynamically finds and selects IP addresses associated with interface 'ether2'.
# [find interface=ether3]:  Dynamically finds and selects IP addresses associated with interface 'ether3'.
# It's important to remove IP addresses from member interfaces to avoid routing conflicts.

# 4. (Optional) Configure monitoring for link status (for faster failover)
/interface bonding set bond1 primary-port-override=no link-monitoring=yes mii-interval=100 mii-cycles=1

# Explanation:
# /interface bonding set bond1: Command to modify settings of bonding interface 'bond1'.
# primary-port-override=no:  Allows automatic failover to the backup link.
# link-monitoring=yes: Enables link monitoring to detect link failures.
# mii-interval=100:  Sets the MII monitoring interval to 100 milliseconds (faster detection).
# mii-cycles=1:  Number of MII cycles to consider a link down before failover (1 cycle for fast reaction).

# Verification:
# Check bonding status:
/interface bonding print detail name=bond1

# Monitor interface status:
/interface ethernet print stats numbers=ether2,ether3
```

**4. REST API Implementation (Python Code)**

This Python script uses the `routeros_api` library to configure Active-Backup bonding via the RouterOS API. Ensure you have the `routeros_api` library installed (`pip install routeros_api`).

```python
import routeros_api
import sys

# RouterOS connection details
HOST = 'your_router_ip'
USER = 'api_user' # Create an API user in RouterOS
PASSWORD = 'your_api_password'

try:
    # Connect to RouterOS API
    api = routeros_api.RouterOsApiPool(HOST, username=USER, password=PASSWORD, port=8728, plaintext_login=True)
    connection = api.get_connection()

    # Create bonding interface
    bonding_interface = connection.path('/interface/bonding')
    bonding_interface.add(name='bond1', mode='active-backup', primary='ether2', slaves='ether2,ether3')
    print("Bonding interface 'bond1' created successfully.")

    # Assign IP address to bonding interface
    ip_address_interface = connection.path('/ip/address')
    ip_address_interface.add(address='192.168.88.1/24', interface='bond1', network='192.168.88.0')
    print("IP address assigned to 'bond1'.")

    # Remove IP addresses from member interfaces (ether2, ether3)
    ip_address_interface.remove(list(ip_address_interface.get(interface='ether2')))
    ip_address_interface.remove(list(ip_address_interface.get(interface='ether3')))
    print("IP addresses removed from 'ether2' and 'ether3'.")

    # Configure link monitoring (optional)
    bonding_interface.update(id=bonding_interface.get(name='bond1')[0]['.id'],
                             primary_port_override='no', link_monitoring='yes',
                             mii_interval='100', mii_cycles='1')
    print("Link monitoring configured for 'bond1'.")

except routeros_api.exceptions.RouterOsApiError as e:
    print(f"RouterOS API Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
finally:
    if 'api' in locals() and api:
        api.disconnect()
```

**Python Script Explanation:**

*   **Import `routeros_api`:** Imports the necessary library to interact with the RouterOS API.
*   **Connection Details:**  Defines variables for RouterOS host, API username, and password. **Replace placeholders with your actual credentials.**  Ensure you've created an API user in RouterOS with appropriate permissions.
*   **Connect to API:**  Establishes a connection to the RouterOS API using `RouterOsApiPool`. `plaintext_login=True` is used as RouterOS v6.x might not support secure API connections by default in all configurations. **For production, consider enabling secure API access if possible.**
*   **Create Bonding Interface (API):** Uses the `/interface/bonding` path and the `add()` method to create the bonding interface with the same parameters as the CLI example.
*   **Assign IP Address (API):** Uses the `/ip/address` path and the `add()` method to assign an IP address to the `bond1` interface.
*   **Remove IP Addresses from Member Interfaces (API):** Uses the `/ip/address` path and `remove()` method combined with `get()` to find and remove IP addresses from `ether2` and `ether3`.
*   **Configure Link Monitoring (API - Optional):** Uses the `/interface/bonding` path and `update()` to modify the bonding interface settings for link monitoring. It retrieves the internal `.id` of the `bond1` interface using `get(name='bond1')[0]['.id']` to correctly identify the interface to update.
*   **Error Handling:** Includes `try...except` blocks to catch `routeros_api.exceptions.RouterOsApiError` for RouterOS API-specific errors and a general `Exception` for other potential errors.  Error messages are printed, and the script exits with an error code.
*   **Disconnect:**  Ensures the API connection is closed in the `finally` block.

**5. Common Debugging Scenarios**

| Scenario                                  | Possible Cause                                    | Debugging Steps                                                                                                                                                                                                                          |
| ----------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bonding interface not created**         | Syntax errors in CLI command or API script.         | - Double-check CLI commands for typos.                                                                                                                                                                                                 |
|                                           | API user permissions incorrect.                    | - Verify API user has write permissions to `/interface/bonding`.                                                                                                                                                                       |
| **Bonding not working after creation**    | Member interfaces not correctly configured.        | - Ensure member interfaces (`ether2`, `ether3`) are enabled (`/interface ethernet print`).                                                                                                                                           |
|                                           | IP address conflicts.                             | - Verify no IP addresses are configured on member interfaces.                                                                                                                                                                        |
|                                           | Incorrect bonding mode or parameters.             | - Check the bonding mode (`/interface bonding print detail name=bond1`).                                                                                                                                                              |
|                                           | Physical link issues on member interfaces.        | - Check cable connections, port status on switches, and interface link status (`/interface ethernet print stats numbers=ether2,ether3`).                                                                                              |
| **Failover not working in Active-Backup** | Link monitoring disabled or incorrectly configured. | - Verify link monitoring is enabled and configured correctly (`/interface bonding print detail name=bond1`).                                                                                                                            |
|                                           | Physical link failure not detected.                | - Test link failure by disconnecting a cable. Monitor bonding status (`/interface bonding print detail name=bond1`) and interface logs (`/log print follow-only topics=interface`). Adjust `mii-interval` and `mii-cycles` if needed. |

**6. Version-Specific Considerations (RouterOS v6.x)**

*   **API Security:** RouterOS v6.x might have limitations in terms of secure API connections (e.g., TLS).  `plaintext_login=True` in the Python API example might be necessary. For production environments, consider upgrading to a newer RouterOS version if secure API access is critical.
*   **Bonding Algorithm Limitations:** Some advanced bonding algorithms (like 802.3ad LACP) might have specific hardware requirements or limitations in older RouterOS versions. Active-Backup and Balance-RR are generally well-supported and suitable for SOHO.
*   **Firmware Updates:** Ensure your RouterOS v6.x is on a stable and reasonably recent version within the v6.x branch to benefit from bug fixes and stability improvements.

**7. Security Hardening Measures**

*   **API User Security:** Use a dedicated API user with the least privileges necessary for bonding configuration. Avoid using the `admin` user for API access.
*   **API Access Control:** Restrict API access to trusted networks or IP addresses using firewall rules if possible.
*   **Physical Security:** Secure the MikroTik router physically to prevent unauthorized access to interfaces and configuration ports.
*   **Password Security:** Use strong, unique passwords for all RouterOS user accounts, including the API user.
*   **Disable Unnecessary Services:** Disable any RouterOS services that are not required for your SOHO environment to reduce the attack surface.

**8. Performance Optimization Tips**

*   **Choose Appropriate Bonding Mode:** For SOHO Active-Backup provides redundancy, Balance-RR can increase bandwidth but might be less efficient for single-stream applications. Consider your specific needs.
*   **Link Monitoring Tuning:** Adjust `mii-interval` and `mii-cycles` for faster failover detection if needed, but be mindful of CPU usage if set too aggressively.
*   **Hardware Capabilities:** Ensure the member interfaces and the MikroTik router hardware itself are capable of handling the increased traffic load from bonding.
*   **Switch Configuration (if applicable):** If bonding to a managed switch, ensure the switch ports are configured correctly (port-channeling or link aggregation settings are usually not needed for basic modes like Active-Backup or Balance-RR, but may be relevant for 802.3ad).
*   **MTU Considerations:**  Ensure consistent MTU (Maximum Transmission Unit) settings across all bonded interfaces and the network path to avoid fragmentation and performance degradation.

**9. SOHO Real-World Deployment Examples**

*   **Redundant Internet Connection:** Bonding two WAN connections (e.g., DSL and Cable) in Active-Backup mode for continuous internet access even if one ISP has an outage.
*   **Increased LAN Bandwidth to NAS:** Bonding two Ethernet ports connected to a Network Attached Storage (NAS) device to improve file transfer speeds for multiple users accessing the NAS simultaneously.
*   **High-Bandwidth Media Streaming:** Bonding interfaces for a media server to ensure smooth streaming to multiple devices within the SOHO network, especially for 4K or high-definition content.
*   **Reliable Home Office Network:** Bonding interfaces for critical home office devices to ensure stable connectivity for remote work, video conferencing, and online collaboration.

**10. Scalability Considerations**

*   **SOHO Scale Limits:**  For typical SOHO environments, bonding a few interfaces (2-4) is usually sufficient.  Scaling to a very large number of interfaces within a single bond is generally not necessary in SOHO and might be more relevant in enterprise or data center scenarios.
*   **Hardware Limitations:** The number of interfaces available on the MikroTik router itself limits scalability. Choose a MikroTik model with sufficient Ethernet ports for your bonding needs.
*   **CPU Overhead:** Bonding does introduce some CPU overhead, especially in more complex modes or with high traffic volume. For SOHO, this is usually minimal, but consider router CPU performance if you are planning very high bandwidth bonding.
*   **Mode-Specific Scalability:** Active-Backup is highly scalable in terms of redundancy as it's primarily about failover. Bandwidth aggregation modes like Balance-RR scale in terms of aggregated bandwidth but might have limitations in single-session throughput.

**11. Monitoring Configurations**

*   **Interface Monitoring:** Use RouterOS built-in monitoring tools like:
    *   **`/interface bonding print detail name=bond1`**:  To check the bonding interface status, active slave, and link status.
    *   **`/interface ethernet print stats numbers=ether2,ether3`**: To monitor interface traffic, errors, and link status for member interfaces.
    *   **Graphs in WinBox/WebFig:**  Use the built-in graphing tools in WinBox or WebFig to visually monitor interface traffic over time.
*   **Logging:** Configure logging for interface events to track link up/down events and potential issues:
    ```routeros
    /system logging add topics=interface action=disk
    ```
*   **SNMP Monitoring (Optional):** For more advanced monitoring, configure SNMP on the MikroTik router and use an external SNMP monitoring system (like Zabbix, PRTG, etc.) to monitor bonding and interface status.

**12. Disaster Recovery Steps**

*   **Configuration Backup:** Regularly back up your RouterOS configuration, including bonding settings (see section 13).
*   **Hardware Redundancy (Optional):** For critical SOHO setups, consider having a spare MikroTik router pre-configured with the bonding setup for rapid replacement in case of hardware failure.
*   **Documentation:** Keep clear documentation of your bonding configuration, including interface assignments, bonding mode, and IP addressing.
*   **Testing Failover:** Periodically test the failover mechanism in Active-Backup mode by manually disconnecting the primary link to ensure the backup link takes over as expected.
*   **Rollback Plan:** In case of configuration errors, have a rollback plan to revert to the last known working configuration.

**13. Automated Backup Scripts**

This basic script uses the RouterOS `/export` command to create a backup file and saves it to the router's disk. You can adapt this to save backups to a remote server using scripting and tools like `scp` or `ftp` if needed.

```routeros
# Script to backup RouterOS configuration including bonding settings

:local backup_filename ("backup-" . [:system clock get date format=yyyy-MM-dd] . "-" . [:system clock get time format=HH-mm-ss] . ".rsc")
/export file=$backup_filename

# Optional: Print backup filename to log for confirmation
:log info "RouterOS Configuration Backup created: $backup_filename"

# You can schedule this script to run regularly using /system scheduler
# Example: Run daily at 3:00 AM
# /system scheduler add name=backup_config start-time=03:00:00 interval=1d on-event=backup_script policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive
```

**Script Explanation:**

*   **`backup_filename` Variable:** Creates a filename dynamically using the current date and time to make backups unique and identifiable.
*   **`/export file=$backup_filename`:**  Executes the RouterOS `/export` command to export the entire router configuration to a file with the generated filename. The `.rsc` extension indicates a RouterOS script file.
*   **`:log info ...` (Optional):** Logs an informational message to the RouterOS log to confirm that the backup was created and provide the filename.
*   **`/system scheduler ...` (Example):**  Shows how to use the `/system scheduler` to automate the execution of this script.  You can adjust the `start-time` and `interval` parameters to schedule backups according to your needs. **Remember to enable the scheduler after adding it.**

**Comparative Table for Bonding Modes (SOHO Focus)**

| Bonding Mode         | Description                                                                | Bandwidth Aggregation | Redundancy     | Complexity | SOHO Suitability |
| ---------------------- | -------------------------------------------------------------------------- | --------------------- | -------------- | ---------- | ---------------- |
| **Active-Backup**      | One link active, others in standby. Failover on active link failure.        | No                    | Excellent      | Low        | Excellent        |
| **Balance-RR (Round Robin)** | Packets distributed sequentially across member links.                      | Yes (Potentially)     | Limited        | Low        | Good (for specific needs) |
| **Balance-XOR**        | Traffic distributed based on MAC addresses.                               | Yes (Potentially)     | Limited        | Medium     | Moderate         |
| **Broadcast**          | Transmits every packet on all member interfaces.                            | No                    | High (but inefficient) | Low        | Limited Use      |
| **802.3ad (LACP)**     | Dynamic link aggregation using LACP protocol (requires switch support).      | Yes (Potentially)     | Limited        | Medium     | SOHO - if switch supports |
| **Balance-TCP**        | Traffic distributed based on TCP sessions.                               | Yes (Potentially)     | Limited        | Medium     | Moderate         |
| **Balance-TLB**        | Adaptive transmit load balancing.                                         | Yes (Potentially)     | Limited        | Medium     | Moderate         |
| **Balance-ALB**        | Adaptive load balancing (includes receive load balancing).                 | Yes (Potentially)     | Limited        | High       | Limited for SOHO  |

**Note:** For basic SOHO redundancy, **Active-Backup** is generally the most straightforward and recommended mode. For bandwidth aggregation in a SOHO setting, **Balance-RR** might be considered, but understand its limitations regarding single-stream performance. Modes like 802.3ad and other advanced balancing modes might require more complex configurations and switch support, making them less common in basic SOHO setups. Always choose the mode that best fits your specific SOHO network requirements and capabilities.

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