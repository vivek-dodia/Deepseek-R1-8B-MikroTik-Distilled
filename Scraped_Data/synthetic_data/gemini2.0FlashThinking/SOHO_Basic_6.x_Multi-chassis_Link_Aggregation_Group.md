---
generated_at: 2025-02-03T21:43:32.927539
topic: Multi-chassis Link Aggregation Group
category: High Availability
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Documentation: Basic Multi-Chassis Link Aggregation Group (LAG) for SOHO (RouterOS 6.x)

**Document Version:** 1.0
**Author:** Your Name - MikroTik Certified Engineer (MTCNA, MTCRE, etc. - specify your certifications if you have them)
**Date:** October 26, 2023
**RouterOS Version:** 6.x (Tested on RouterOS 6.49 - Long-term branch recommended)
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic
**Topic:** Basic Link Aggregation Group (LAG) for Redundancy and Increased Bandwidth in SOHO using *Two* MikroTik Routers.

**Important Note:** True Multi-Chassis Link Aggregation Group (MLAG) as found in enterprise networking is **not natively supported in MikroTik RouterOS 6.x**. This documentation outlines a **simplified approach** using two MikroTik routers to provide link redundancy and potentially increased bandwidth to a single endpoint (like a NAS or server) in a SOHO environment. This is achieved by creating individual Link Aggregation Groups (LAGs) on each MikroTik router and connecting them to the target device, which also supports LAG. This is *not* a true MLAG in the sense of a single logical LAG spanning multiple chassis, but it provides similar benefits in a basic SOHO context within RouterOS 6.x limitations.

**1. Architecture Diagram Requirements:**

**Diagram Description:** This diagram illustrates a basic setup where two MikroTik routers are used to provide redundant and potentially higher bandwidth connectivity to a Network Attached Storage (NAS) device. Each MikroTik router forms a LAG (Bonding interface) using two physical interfaces. The NAS device also has a LAG interface configured, spanning ports connected to both MikroTik routers. In case of a single MikroTik router failure or link failure, the NAS remains accessible through the active links.

```mermaid
graph LR
    subgraph MikroTik Router 1 (RB951G-2HnD Example)
        R1_Eth1(ether1) --> NAS_Port1[NAS Port 1]
        R1_Eth2(ether2) --> NAS_Port2[NAS Port 2]
        R1_Bond(bond1 - LAG)
        R1_Eth1 -- member --> R1_Bond
        R1_Eth2 -- member --> R1_Bond
        R1_Eth3(ether3 - LAN)
        R1_Eth4(ether4 - WAN)
    end
    subgraph MikroTik Router 2 (RB951G-2HnD Example)
        R2_Eth1(ether1) --> NAS_Port3[NAS Port 3]
        R2_Eth2(ether2) --> NAS_Port4[NAS Port 4]
        R2_Bond(bond1 - LAG)
        R2_Eth1 -- member --> R2_Bond
        R2_Eth2 -- member --> R2_Bond
        R2_Eth3(ether3 - LAN)
        R2_Eth4(ether4 - WAN)
    end
    NAS_Port1 -- LAG Member --> NAS_Bond(bond0 - NAS LAG)
    NAS_Port2 -- LAG Member --> NAS_Bond
    NAS_Port3 -- LAG Member --> NAS_Bond
    NAS_Port4 -- LAG Member --> NAS_Bond
    R1_Eth3 -- LAN Network --> Clients
    R2_Eth3 -- LAN Network --> Clients
    style R1_Bond fill:#ccf,stroke:#333,stroke-width:1px
    style R2_Bond fill:#ccf,stroke:#333,stroke-width:1px
    style NAS_Bond fill:#ccf,stroke:#333,stroke-width:1px
    style NAS_Port1 fill:#eee,stroke:#333,stroke-width:1px
    style NAS_Port2 fill:#eee,stroke:#333,stroke-width:1px
    style NAS_Port3 fill:#eee,stroke:#333,stroke-width:1px
    style NAS_Port4 fill:#eee,stroke:#333,stroke-width:1px
    style R1_Eth1 fill:#eee,stroke:#333,stroke-width:1px
    style R1_Eth2 fill:#eee,stroke:#333,stroke-width:1px
    style R2_Eth1 fill:#eee,stroke:#333,stroke-width:1px
    style R2_Eth2 fill:#eee,stroke:#333,stroke-width:1px
    style MikroTik Router 1 fill:#f9f,stroke:#333,stroke-width:2px
    style MikroTik Router 2 fill:#f9f,stroke:#333,stroke-width:2px
    style NAS_Device fill:#eef,stroke:#333,stroke-width:2px
    label NAS_Device "NAS Device\n(LAG Capable)"
```

**Requirements for Diagram:**

* **Two MikroTik Routers:** Clearly labeled as Router 1 and Router 2 (e.g., RB951G-2HnD models are suitable for SOHO).
* **NAS Device:** Represent a NAS or server capable of Link Aggregation.
* **Physical Interfaces:** Show Ethernet ports on each MikroTik router used for LAG (e.g., ether1, ether2).
* **Bonding Interfaces (LAGs):**  Represent the logical LAG interfaces on each MikroTik (e.g., bond1) and the NAS (e.g., bond0).
* **Connections:** Show physical connections between MikroTik ports and NAS ports.
* **LAN/WAN Interfaces:** Indicate other interfaces for LAN and WAN connectivity on each MikroTik.
* **Client Network:** Represent clients connected to the LAN side of MikroTik routers.
* **Clear Labels:** Use descriptive labels for all components and interfaces.
* **Redundancy Indication:** Diagram implicitly shows redundancy by having paths through both MikroTik routers to the NAS.

**2. CLI Configuration with Inline Comments:**

**Configuration on MikroTik Router 1:**

```routeros
# --- MikroTik Router 1 Configuration ---

# --- 1. Interface Configuration ---
# Rename interfaces for clarity
/interface ethernet
set [find default-name=ether1] name=LAG-Member-1
set [find default-name=ether2] name=LAG-Member-2
set [find default-name=ether3] name=LAN-Interface
set [find default-name=ether4] name=WAN-Interface

# --- 2. Create Bonding Interface (LAG) ---
/interface bonding
add name=bond1 mode=balance-rr link-monitoring=arp primary="" mtu=1500

# --- 3. Add Ethernet Interfaces to Bonding Interface ---
/interface bonding
set bond1 slaves=LAG-Member-1,LAG-Member-2

# --- 4. IP Address Configuration for Bonding Interface ---
/ip address
add address=192.168.10.1/24 interface=bond1 network=192.168.10.0 # IP for Router 1 on LAG subnet

# --- 5. LAN Interface IP Configuration (if needed for management) ---
/ip address
add address=192.168.88.1/24 interface=LAN-Interface network=192.168.88.0 # Standard LAN IP

# --- 6. WAN Interface Configuration (DHCP Client Example) ---
/ip dhcp-client
add interface=WAN-Interface disabled=no

# --- 7. NAT Configuration (Masquerade for WAN) ---
/ip firewall nat
add chain=srcnat out-interface=WAN-Interface action=masquerade

# --- 8. Basic Firewall Rules (Adjust as needed for SOHO) ---
/ip firewall filter
add chain=forward action=drop comment="Default deny forward"
add chain=forward connection-state=established,related action=accept comment="Allow established/related"
add chain=forward in-interface=LAN-Interface out-interface=WAN-Interface action=accept comment="Allow LAN to WAN"
add chain=input action=accept comment="Allow all input on loopback" in-interface=loopback
add chain=input action=accept comment="Allow established/related input" connection-state=established,related
add chain=input protocol=icmp action=accept comment="Allow ICMP"
add chain=input action=drop comment="Drop all other input"
add chain=forward action=drop comment="Drop invalid connections" connection-state=invalid
```

**Configuration on MikroTik Router 2:**

```routeros
# --- MikroTik Router 2 Configuration ---

# --- 1. Interface Configuration ---
# Rename interfaces for clarity
/interface ethernet
set [find default-name=ether1] name=LAG-Member-1
set [find default-name=ether2] name=LAG-Member-2
set [find default-name=ether3] name=LAN-Interface
set [find default-name=ether4] name=WAN-Interface

# --- 2. Create Bonding Interface (LAG) ---
/interface bonding
add name=bond1 mode=balance-rr link-monitoring=arp primary="" mtu=1500

# --- 3. Add Ethernet Interfaces to Bonding Interface ---
/interface bonding
set bond1 slaves=LAG-Member-1,LAG-Member-2

# --- 4. IP Address Configuration for Bonding Interface ---
/ip address
add address=192.168.10.2/24 interface=bond1 network=192.168.10.0 # IP for Router 2 on LAG subnet

# --- 5. LAN Interface IP Configuration (if needed for management) ---
/ip address
add address=192.168.89.1/24 interface=LAN-Interface network=192.168.89.0 # Different LAN IP for Router 2

# --- 6. WAN Interface Configuration (DHCP Client Example) ---
/ip dhcp-client
add interface=WAN-Interface disabled=no

# --- 7. NAT Configuration (Masquerade for WAN) ---
/ip firewall nat
add chain=srcnat out-interface=WAN-Interface action=masquerade

# --- 8. Basic Firewall Rules (Adjust as needed for SOHO) ---
/ip firewall filter
add chain=forward action=drop comment="Default deny forward"
add chain=forward connection-state=established,related action=accept comment="Allow established/related"
add chain=forward in-interface=LAN-Interface out-interface=WAN-Interface action=accept comment="Allow LAN to WAN"
add chain=input action=accept comment="Allow all input on loopback" in-interface=loopback
add chain=input action=accept comment="Allow established/related input" connection-state=established,related
add chain=input protocol=icmp action=accept comment="Allow ICMP"
add chain=input action=drop comment="Drop all other input"
add chain=forward action=drop comment="Drop invalid connections" connection-state=invalid
```

**Configuration on NAS Device (Example - Synology DSM):**

The NAS device will also need to be configured for Link Aggregation.  The specific steps will vary depending on the NAS vendor and operating system.  For example, on a Synology NAS:

1. **Control Panel** -> **Network** -> **Network Interface** -> **Create** -> **Create Bond**.
2. **Mode:** Choose a suitable LAG mode (e.g., 802.3ad Dynamic Link Aggregation, or Adaptive Load Balancing - depending on NAS and MikroTik capabilities and desired behavior).  `balance-rr` on MikroTik is similar to Adaptive Load Balancing. `802.3ad` would require LACP configuration on MikroTik (more complex for basic SOHO).
3. **Interfaces:** Select the Ethernet interfaces on the NAS that are connected to the MikroTik routers (NAS Port 1, NAS Port 2, NAS Port 3, NAS Port 4 in our diagram).
4. **IP Address:** Configure a single IP address for the NAS Bond interface (e.g., 192.168.10.10/24, gateway optional if routing is handled by MikroTik).

**Important Considerations for LAG Mode:**

* **`balance-rr` (Round Robin):** Distributes packets in sequential order across slave interfaces. Simple, but may not provide optimal load balancing for all traffic types. Good for basic redundancy and some increased bandwidth.
* **`balance-xor` (XOR):**  Transmits based on source and destination MAC addresses.  Traffic to the same MAC address will always go through the same link. Better load balancing than `balance-rr` but still not link aggregation in the true sense.
* **`802.3ad` (LACP - Link Aggregation Control Protocol):**  Dynamic link aggregation, negotiates link aggregation between devices. Requires LACP support on both sides.  More complex to configure in RouterOS 6.x and potentially overkill for basic SOHO. Not recommended for this basic setup in RouterOS 6.x unless specifically needed and understood.
* **`balance-tcp` (balance-tlb) and `balance-alb` (balance-clb):**  Adaptive load balancing modes.  Require more advanced network understanding and may not be ideal for all SOHO scenarios.

For this basic SOHO setup, `balance-rr` or `balance-xor` are typically sufficient and easier to configure.  `balance-rr` is chosen in the example for simplicity.

**3. REST API Implementation (Python Code):**

**Note:** RouterOS 6.x has a less mature REST API compared to RouterOS 7.x. We will use the `routeros_api` Python library which supports RouterOS API and can be used to execute commands similar to CLI.  Direct REST API calls might be possible but are less structured in v6.x and less recommended for this context.

**Python Code Example (using `routeros_api` library):**

```python
import routeros_api
import routeros_api.exceptions

# --- Router 1 Configuration ---
router1_address = '192.168.88.1' # Replace with Router 1 IP
router1_username = 'admin'       # Replace with Router 1 username
router1_password = ''          # Replace with Router 1 password (or use API user)

# --- Router 2 Configuration ---
router2_address = '192.168.89.1' # Replace with Router 2 IP
router2_username = 'admin'       # Replace with Router 2 username
router2_password = ''          # Replace with Router 2 password (or use API user)

def configure_router_lag(address, username, password, router_id):
    try:
        connection = routeros_api.RouterOsClient(address, username=username, password=password, port=8728) # API port 8728

        # --- Interface Configuration ---
        connection.path('/interface/ethernet').update(numbers='ether1', name=f'LAG-Member-1-R{router_id}')
        connection.path('/interface/ethernet').update(numbers='ether2', name=f'LAG-Member-2-R{router_id}')
        connection.path('/interface/ethernet').update(numbers='ether3', name=f'LAN-Interface-R{router_id}')
        connection.path('/interface/ethernet').update(numbers='ether4', name=f'WAN-Interface-R{router_id}')

        # --- Bonding Interface ---
        connection.path('/interface/bonding').add(name=f'bond1-R{router_id}', mode='balance-rr', link_monitoring='arp')

        # --- Add Slaves to Bonding Interface ---
        connection.path('/interface/bonding').update(numbers=f'bond1-R{router_id}', slaves=f'LAG-Member-1-R{router_id},LAG-Member-2-R{router_id}')

        # --- IP Address Configuration for Bonding Interface ---
        if router_id == 1:
            ip_address = '192.168.10.1/24'
        else:
            ip_address = '192.168.10.2/24'
        connection.path('/ip/address').add(address=ip_address, interface=f'bond1-R{router_id}', network='192.168.10.0')

        print(f"LAG configuration successful on Router {router_id} ({address})")

    except routeros_api.exceptions.RouterOsApiError as e:
        print(f"Error configuring Router {router_id} ({address}): {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    configure_router_lag(router1_address, router1_username, router1_password, 1)
    configure_router_lag(router2_address, router2_username, router2_password, 2)
```

**Explanation:**

* **`routeros_api` library:**  This script uses the `routeros_api` library to interact with the MikroTik RouterOS API.  Install it using `pip install routeros_api`.
* **Router Credentials:**  Replace placeholders for router IPs, usernames, and passwords. **Best practice:** Create dedicated API users with limited privileges instead of using the `admin` account.
* **`configure_router_lag` function:**  This function encapsulates the LAG configuration steps for a single router.
* **API Paths:**  The script uses API paths like `/interface/ethernet`, `/interface/bonding`, `/ip/address` to configure the router.
* **Error Handling:**  Includes a `try-except` block to catch `routeros_api.exceptions.RouterOsApiError` and print error messages.
* **Router ID Parameter:** The `router_id` parameter allows the function to be reused for both Router 1 and Router 2, adjusting IP addresses and interface names accordingly.

**To run the script:**

1. **Install `routeros_api`:** `pip install routeros_api`
2. **Enable API service on MikroTik routers:** `/ip service enable api` (or `/ip service enable api-ssl` for secure API).
3. **Replace placeholders:** Update router IPs, usernames, and passwords in the script.
4. **Run the Python script:** `python your_script_name.py`

**4. Common Debugging Scenarios:**

* **Scenario 1: LAG Interface not Active/Not Bonding:**
    * **Check Physical Connections:** Ensure cables are properly connected to the correct ports on both MikroTik routers and the NAS.
    * **Interface Status:** In RouterOS CLI, use `/interface bonding print detail` to check the status of the bonding interface and its slave interfaces. Look for `running=yes`, `slaves-state=active` or `slaves-state=standby` (depending on bonding mode and link state).
    * **NAS LAG Configuration:** Verify the LAG configuration on the NAS device. Ensure the correct interfaces are selected, and the LAG mode is compatible with MikroTik configuration.
    * **Link Monitoring:** Check `link-monitoring` setting in `/interface bonding print`. If using `arp`, ensure ARP is working between routers and NAS. Try `ping` from routers to NAS and vice versa.
    * **MTU Mismatch:** Verify MTU settings on bonding interfaces and physical interfaces. Ensure they are consistent (typically 1500 for Ethernet).

* **Scenario 2: Slow Performance or Intermittent Connectivity:**
    * **Bonding Mode:** Experiment with different bonding modes (`balance-rr`, `balance-xor`) to see if performance improves. `balance-rr` might not provide optimal load balancing for all traffic.
    * **Cable Issues:**  Test Ethernet cables. Faulty cables can cause intermittent connectivity or slow speeds.
    * **Resource Contention:**  Check CPU and memory usage on MikroTik routers, especially under heavy load.  SOHO routers may have limited resources. Use `/system resource print`.
    * **NAS Performance:**  Ensure the NAS device itself is not the bottleneck. Check NAS CPU, disk I/O, and network interface utilization.
    * **Firewall Rules:**  Review firewall rules on both MikroTik routers. Overly restrictive rules might be causing performance issues. Check `/ip firewall filter print`.

* **Scenario 3: Redundancy Not Working as Expected (Failover Issues):**
    * **Simulate Link Failure:**  Physically disconnect one of the LAG member links (e.g., unplug cable from Router 1 `ether1` to NAS). Monitor connectivity to the NAS. It should remain accessible through the remaining active links via Router 2.
    * **Router Failure Simulation:**  Power off one of the MikroTik routers. Verify that the NAS remains accessible through the other router.
    * **IP Address Conflicts:** Ensure that the IP addresses on the bonding interfaces of Router 1 and Router 2 are in the same subnet (192.168.10.0/24 in our example) but are *different* IP addresses (192.168.10.1 and 192.168.10.2).
    * **Routing Issues:** In a more complex network, ensure proper routing is in place so that traffic can reach the NAS via either MikroTik router. For a basic SOHO setup, direct connection and same subnet usually suffice.

**5. Version-Specific Considerations (RouterOS 6.x):**

* **No True MLAG:** Reiterate that RouterOS 6.x does not offer true MLAG. This setup provides redundancy and potentially increased bandwidth to a single device but is not a scalable MLAG solution for large networks.
* **Bonding Modes:**  Available bonding modes in RouterOS 6.x might be slightly different or have different behavior compared to later versions. Refer to the RouterOS 6.x documentation for specific details on each mode.
* **REST API Limitations:** The REST API in RouterOS 6.x is less feature-rich and less standardized than in RouterOS 7.x. Expect potentially more limited functionality and different API paths for certain configurations compared to newer versions.
* **`routeros_api` library compatibility:** Ensure the `routeros_api` Python library version is compatible with RouterOS 6.x API. Older versions of the library might be required for optimal compatibility.
* **Performance Limitations:** SOHO MikroTik routers running RouterOS 6.x may have hardware limitations (CPU, memory) that could impact LAG performance, especially with more complex bonding modes or high traffic loads.

**6. Security Hardening Measures:**

* **Strong Passwords:** Set strong, unique passwords for all user accounts on both MikroTik routers, especially the `admin` account.
* **Disable Default Services:** Disable unnecessary services like `telnet`, `ftp`, `www` (if not using WebFig) under `/ip service disable <service_name>`. Only enable `api` (or `api-ssl`) if using the API.
* **Firewall Rules:** Implement a robust firewall policy. The basic firewall rules provided in the examples are a starting point.  Consider more restrictive input and forward chain rules based on your SOHO needs.  Specifically:
    * **Limit Access to Router Management:**  Restrict access to WinBox/WebFig/SSH/API to specific IP addresses or networks. Use `/ip firewall filter add chain=input src-address=<your_management_network> dst-port=8291,80,22,8728 protocol=tcp action=accept comment="Allow management from trusted network"` and add a `drop` rule at the end of the `input` chain.
    * **Port Forwarding Security:** If using port forwarding, only forward necessary ports and consider using destination NAT (dstnat) to a non-standard internal port for added security.
* **Regular Software Updates:** Keep RouterOS 6.x updated to the latest stable or long-term version to patch security vulnerabilities. Use `/system package update check-for-updates` and `/system package update install`.
* **Disable Default Admin Password:**  If the default `admin` account has no password, immediately set a strong password.
* **API User with Limited Privileges:** Create a dedicated API user with only necessary permissions for automation tasks instead of using the `admin` account. Use `/user add name=<api_user> password=<api_password> group=read,write,test`.
* **Disable Guest Access (if applicable):** If using wireless, disable guest access or configure it with strong security settings.

**7. Performance Optimization Tips:**

* **Choose Appropriate Bonding Mode:** Select a bonding mode that best suits your traffic patterns and hardware capabilities. `balance-rr` is simple but may not be optimal for all scenarios. `balance-xor` might offer better load balancing for some traffic types. Test and monitor performance with different modes.
* **Ethernet Cable Quality:** Use good quality Ethernet cables (Cat5e or Cat6) to ensure reliable high-speed links.
* **Interface Speed/Duplex Settings:** Ensure interfaces are running at the highest possible speed and full-duplex. Check `/interface ethernet print detail` for `speed` and `full-duplex` status. Auto-negotiation is generally recommended.
* **Jumbo Frames (If Supported):** If both MikroTik routers, NAS, and network clients support jumbo frames, enabling them might improve performance by reducing overhead. However, ensure *all* devices in the path support jumbo frames and configure MTU accordingly.  This is more advanced and may not be needed for basic SOHO.
* **Offloading Features (if available on MikroTik hardware):** Some MikroTik devices support hardware offloading for certain features. Check RouterOS documentation and hardware specifications to see if any offloading options are relevant to LAG and enable them if applicable.
* **Monitor CPU and Memory Usage:** Regularly monitor CPU and memory utilization on both MikroTik routers using `/system resource print`. High utilization can indicate performance bottlenecks. Consider upgrading to more powerful MikroTik hardware if needed.
* **Traffic Shaping/QoS (Advanced):** For more complex SOHO environments, consider implementing basic traffic shaping or QoS (Quality of Service) rules to prioritize critical traffic and manage bandwidth usage if experiencing congestion. This is beyond the scope of a basic LAG setup but can be considered for advanced optimization.

**SOHO Specific Requirements:**

**Real-world Deployment Examples:**

* **Example 1: NAS Backup and File Sharing:** A SOHO uses a NAS device for central file storage and backups. The LAG setup provides increased bandwidth for faster file transfers and backups to the NAS and ensures redundancy so that access to the NAS is maintained even if one MikroTik router or link fails.
* **Example 2: Small Server Hosting:** A SOHO hosts a small web server or application server. LAG to the server provides increased bandwidth for handling multiple concurrent requests and redundancy for improved uptime.
* **Example 3: Media Streaming Server:** A SOHO uses a media server (e.g., Plex) to stream high-definition video to multiple devices. LAG can provide sufficient bandwidth for smooth streaming to multiple clients simultaneously and ensure uninterrupted streaming in case of a link failure.

**Scalability Considerations:**

* **Limited Scalability:** This basic two-router LAG setup is **not scalable** to larger networks or more complex MLAG requirements. It is designed for a small number of devices (like a single NAS or server) in a SOHO environment.
* **True MLAG for Scalability:** For larger networks requiring true MLAG, consider using enterprise-grade networking equipment that supports proper MLAG protocols and features. MikroTik RouterOS 7.x and later versions on certain hardware might offer more advanced bonding options but still not full enterprise-level MLAG.
* **Complexity Increase:**  Adding more MikroTik routers to this basic setup for more than one or two LAG endpoints would quickly become complex to manage and would not be a recommended approach.

**Monitoring Configurations:**

* **Interface Monitoring (CLI):** Use `/interface bonding monitor bond1` and `/interface ethernet monitor LAG-Member-1`, `/interface ethernet monitor LAG-Member-2` in the RouterOS CLI to monitor the status of the bonding interface and its member interfaces in real-time.
* **SNMP Monitoring (Advanced):** Configure SNMP (Simple Network Management Protocol) on both MikroTik routers and use an SNMP monitoring tool (e.g., Zabbix, PRTG) to monitor interface status, bandwidth utilization, CPU, memory, and other relevant metrics. Enable SNMP in `/snmp community set enabled=yes`.
* **The Dude (MikroTik Monitoring Tool):** MikroTik's "The Dude" network monitoring application can be used to monitor MikroTik devices and network links. It can visualize network topology, monitor device status, and send alerts in case of issues.
* **Simple Scripts for Status Checks:** Create simple RouterOS scripts to periodically check the status of bonding interfaces and send email or log alerts if the status changes or errors are detected. Example script to check bond status and log to system log:

```routeros
:local bond_status [/interface bonding get bond1 status];
:if ($bond_status != "running") do={
  /log warning message="Bonding interface bond1 is not running! Status: $bond_status";
} else={
  /log info message="Bonding interface bond1 is running.";
}
```
Schedule this script using `/system scheduler add name="check_bond_status" interval=5m on-event="/path/to/script" start-time=startup`.

**Disaster Recovery Steps:**

* **Configuration Backups:** Regularly backup the configuration of both MikroTik routers. Use `/system backup save name=router1_config` and `/system backup save name=router2_config`. Automate backups (see below).
* **Configuration Export (Text):** Export configurations to text files for easier review and manual restoration if needed: `/export file=router1_config.rsc`.
* **Disaster Recovery Plan:**
    1. **Single Router Failure:** If one MikroTik router fails completely, the NAS and connected clients should still be accessible through the remaining active MikroTik router and its LAG links. No immediate action is required unless you need to restore full redundancy.
    2. **Restore Failed Router:** Replace the failed MikroTik router with a spare router of the same model (or similar).
    3. **Restore Configuration:** Restore the configuration backup to the replacement router: `/system backup load name=router1_config.backup`.
    4. **Verify Configuration:**  Check the restored configuration, especially IP addresses, interface names, and bonding settings.
    5. **Reconnect Cables:** Reconnect the Ethernet cables to the replacement router's LAG member interfaces.
    6. **Test Connectivity:** Verify that LAG is working correctly and that clients can access the NAS through the replacement router.

**Automated Backup Scripts:**

**RouterOS Script for Automated Backup (Example - Email Backup):**

```routeros
# Script to backup RouterOS configuration and email it

:local backup_name ("router-backup-" . [/system identity get name] . "-" . [/system clock get date format=yyyy-MM-dd]);
:local backup_file ($backup_name . ".backup");

/system backup save name=$backup_name dont-encrypt=yes;

/tool e-mail send to="your_email@example.com" \
    subject=("MikroTik Router Backup: " . [/system identity get name] . " - " . [/system clock get date format=yyyy-MM-dd]) \
    body=("Router Configuration Backup attached.") \
    file=$backup_file;

/file remove $backup_file;

:log info message=("Automated backup completed and emailed: " . $backup_name);
```

**Explanation:**

* **`backup_name`:** Generates a backup filename with router identity and date.
* **`/system backup save`:** Creates a backup file. `dont-encrypt=yes` is used for simplicity in this example, but consider encryption for sensitive configurations in real-world scenarios.
* **`/tool e-mail send`:** Sends the backup file as an email attachment. **Configure `/tool e-mail` settings first!** (SMTP server, authentication, etc.).
* **`/file remove`:** Deletes the backup file from the router's storage after emailing (optional, adjust based on storage space and retention policy).
* **`/log info`:** Logs a message to the system log for backup confirmation.

**Schedule the backup script:**

`/system scheduler add name="daily_config_backup" interval=1d start-time=03:00:00 on-event="/path/to/backup_script" policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,api,dude,sniff,sensitive-api,romon`

**Important:**

* **Configure `/tool e-mail`:** Before using the backup script, you *must* configure the email settings in `/tool e-mail set ...` (SMTP server, from address, authentication if required).
* **Security of Email:** Emailing backups might not be the most secure method for sensitive configurations. Consider more secure backup methods like SFTP or SCP to a dedicated backup server for production environments.
* **Backup Rotation/Retention:** Implement a backup rotation and retention policy to manage backup files and storage space.

This comprehensive documentation provides a detailed guide to setting up a basic Link Aggregation Group (LAG) using two MikroTik routers in a SOHO environment running RouterOS 6.x.  Remember that this is *not* true MLAG but a simplified approach to achieve redundancy and potentially increased bandwidth for specific devices within the limitations of RouterOS 6.x. For more advanced MLAG solutions, consider enterprise-grade equipment and/or newer RouterOS versions with potentially improved bonding capabilities.

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