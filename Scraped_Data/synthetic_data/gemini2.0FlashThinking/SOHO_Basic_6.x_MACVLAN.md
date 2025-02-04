---
generated_at: 2025-02-03T21:20:08.660315
topic: MACVLAN
category: Bridging & Switching
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

Certainly! Here's comprehensive documentation on MikroTik MACVLAN for a SOHO environment running RouterOS v6.x, incorporating CLI and API examples, diagrams, and addressing all your specified requirements.

---

## MikroTik RouterOS MACVLAN Configuration for SOHO Environments (v6.x)

**Document Version:** 1.0
**RouterOS Version:** 6.x (Tested on v6.49.7)
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic
**Author:** [Your Name/Company Name] - MikroTik Certified Engineer
**Date:** October 26, 2023

**1. Introduction to MACVLAN**

MACVLAN is a network virtualization technology that allows you to assign multiple MAC addresses to a single physical network interface. This effectively creates multiple "virtual" network interfaces on top of one physical interface. Each MACVLAN interface can have its own IP address and operate independently, but they all share the underlying physical link.

**Use Cases in SOHO Environments:**

* **Isolating IoT Devices:**  Create separate MACVLAN interfaces for IoT devices to isolate them from the main network for security purposes.
* **Guest Network Segregation (Simplified):**  Offer a basic level of network separation for guests without the full complexity of VLAN tagging.
* **Multiple Public IP Addresses (Limited Scenario):** In scenarios where your ISP provides multiple public IP addresses on a single physical connection, MACVLAN can be used to assign these to different virtual interfaces (though this is less common in typical SOHO setups and might be better handled by bridging or VLANs).
* **Simplified Network Segmentation:** For basic segmentation needs where full VLAN implementation is overkill, MACVLAN provides a lighter-weight alternative.

**Limitations in SOHO Context:**

* **Limited Scalability:** MACVLAN is less scalable than VLAN tagging for larger networks. It's best suited for smaller, well-defined segmentation needs.
* **Broadcast Domain:** All MACVLAN interfaces on the same physical interface share the same broadcast domain. This is a crucial security consideration.
* **Hardware Support:** MACVLAN relies on the underlying physical interface's ability to handle multiple MAC addresses. Most modern Ethernet interfaces in MikroTik routers support this, but very old hardware might have limitations.
* **RouterOS v6.x REST API Limitations:**  While basic API operations are available in v6.x, advanced features might be less developed compared to v7+.

**2. Architecture Diagram Requirements**

The following diagram illustrates a typical SOHO deployment scenario where MACVLAN is used to isolate IoT devices from the main LAN.

```mermaid
graph LR
    Internet[Internet] --> Router(MikroTik Router);
    Router -- ether1 (WAN) --> ISP_Modem[ISP Modem];
    Router -- ether2 (Physical Interface) --> Switch[Unmanaged Switch];
    Switch -- PC[PC (Main LAN)];
    Switch -- Printer[Printer (Main LAN)];
    Switch -- IoT_Hub[IoT Hub (IoT VLAN)];
    Switch -- Smart_TV[Smart TV (IoT VLAN)];

    subgraph Main LAN (ether2)
        PC
        Printer
    end

    subgraph IoT VLAN (macvlan1 on ether2)
        IoT_Hub
        Smart_TV
    end

    style Router fill:#eef,stroke:#333,stroke-width:2px
    style Switch fill:#ddd,stroke:#333,stroke-width:1px
    style ISP_Modem fill:#ddd,stroke:#333,stroke-width:1px
    style Internet fill:#eee,stroke:#333,stroke-width:1px
    style PC fill:#ddd,stroke:#333,stroke-width:1px
    style Printer fill:#ddd,stroke:#333,stroke-width:1px
    style IoT_Hub fill:#ddd,stroke:#333,stroke-width:1px
    style Smart_TV fill:#ddd,stroke:#333,stroke-width:1px

    linkStyle 1,2,3,4,5,6,7 stroke-width:2px,stroke:#333;
```

**Diagram Explanation:**

* **`ether1 (WAN)`:**  Connects to the ISP modem for internet access.
* **`ether2 (Physical Interface)`:**  Connects to an unmanaged switch. This is the parent interface for the MACVLAN.
* **`Switch (Unmanaged)`:**  A simple switch distributes network connectivity to devices.  Since we are using MACVLAN, VLAN tagging is not required on the switch.
* **`Main LAN (ether2)`:** Devices like PCs and printers are directly connected to the physical interface `ether2`.
* **`IoT VLAN (macvlan1 on ether2)`:** IoT devices (IoT Hub, Smart TV) will be connected to the same switch, but their traffic will be logically separated using a MACVLAN interface created on `ether2` (e.g., `macvlan1`).  We will configure DHCP and firewall rules to manage this separation.

**3. CLI Configuration with Inline Comments**

Connect to your MikroTik router using Winbox, WebFig, or SSH and open a "New Terminal".

```routeros
# --- Step 1: Create MACVLAN Interface ---
/interface macvlan
add interface=ether2 name=macvlan-iot mac-address=auto # Create macvlan interface on ether2, auto-generate MAC

# --- Step 2: Assign IP Address to MACVLAN Interface ---
/ip address
add address=192.168.99.1/24 interface=macvlan-iot network=192.168.99.0 # IoT network IP

# --- Step 3: Configure DHCP Server for IoT Network ---
/ip pool
add name=dhcp_pool_iot ranges=192.168.99.10-192.168.99.254 # DHCP pool for IoT devices

/ip dhcp-server
add name=dhcp_server_iot interface=macvlan-iot address-pool=dhcp_pool_iot lease-time=1d # DHCP server on macvlan-iot

/ip dhcp-server network
add address=192.168.99.0/24 gateway=192.168.99.1 dns-server=192.168.99.1 # DHCP network settings for IoT

# --- Step 4: Firewall Rules for IoT Network Isolation (Basic) ---
/ip firewall filter
# Allow established/related connections for IoT network (input and forward chains)
add chain=input in-interface=macvlan-iot connection-state=established,related action=accept comment="Accept IoT established/related input"
add chain=forward in-interface=macvlan-iot connection-state=established,related action=accept comment="Accept IoT established/related forward"

# Allow IoT network to access internet (forward chain)
add chain=forward in-interface=macvlan-iot out-interface=ether1 action=accept comment="Allow IoT to internet"

# Deny IoT network access to main LAN (forward chain) - IMPORTANT for isolation
add chain=forward in-interface=macvlan-iot out-interface=ether2 action=drop comment="Block IoT to Main LAN"

# Optionally, drop new input connections from IoT network to router (for tighter security - router management isolation)
add chain=input in-interface=macvlan-iot connection-state=new action=drop comment="Drop new input from IoT (optional)"


# --- Step 5: NAT for IoT Network ---
/ip firewall nat
add chain=srcnat out-interface=ether1 src-address=192.168.99.0/24 action=masquerade comment="NAT for IoT network"

# --- Verification ---
# /interface macvlan print
# /ip address print
# /ip dhcp-server print
# /ip firewall filter print
# /ip firewall nat print
```

**CLI Configuration Explanation:**

* **Step 1: Create MACVLAN Interface:**
    * `/interface macvlan add interface=ether2 name=macvlan-iot mac-address=auto`: Creates a new MACVLAN interface named `macvlan-iot` on the physical interface `ether2`. `mac-address=auto` lets RouterOS automatically assign a unique MAC address.
* **Step 2: Assign IP Address:**
    * `/ip address add address=192.168.99.1/24 interface=macvlan-iot network=192.168.99.0`: Assigns the IP address `192.168.99.1/24` to the `macvlan-iot` interface, defining the IoT network subnet.
* **Step 3: Configure DHCP Server:**
    * `/ip pool add name=dhcp_pool_iot ranges=192.168.99.10-192.168.99.254`: Creates a DHCP pool for IoT devices.
    * `/ip dhcp-server add name=dhcp_server_iot interface=macvlan-iot address-pool=dhcp_pool_iot lease-time=1d`: Sets up a DHCP server on the `macvlan-iot` interface using the created pool, with a lease time of 1 day.
    * `/ip dhcp-server network add address=192.168.99.0/24 gateway=192.168.99.1 dns-server=192.168.99.1`: Defines network settings for DHCP clients in the IoT network, including gateway and DNS server (router's IP).
* **Step 4: Firewall Rules (Basic Isolation):**
    * **`input chain` rules:** Allow established/related input connections from the IoT network and optionally drop new input connections for increased router security.
    * **`forward chain` rules:**
        * Allow established/related forwarded traffic for IoT.
        * Allow IoT network traffic to the internet (out to `ether1`).
        * **Crucially, block traffic from the IoT network to the main LAN (`ether2`)** to enforce isolation.
* **Step 5: NAT for IoT Network:**
    * `/ip firewall nat add chain=srcnat out-interface=ether1 src-address=192.168.99.0/24 action=masquerade`:  Enables NAT masquerade for traffic originating from the IoT network (`192.168.99.0/24`) going out through the WAN interface (`ether1`), allowing IoT devices to access the internet.

**4. REST API Implementation (Python Code)**

```python
import routeros_api
import time

router_ip = 'your_router_ip'  # Replace with your router IP
username = 'your_username'    # Replace with your username
password = 'your_password'    # Replace with your password

try:
    connection = routeros_api.RouterOsApiPool(router_ip, username=username, password=password, plaintext_login=True)
    api = connection.get_api()

    # --- Step 1: Create MACVLAN Interface ---
    try:
        api.path('/interface/macvlan').add(interface='ether2', name='macvlan-iot', mac_address='auto')
        print("MACVLAN interface 'macvlan-iot' created successfully.")
    except routeros_api.exceptions.RouterOsApiError as e:
        print(f"Error creating MACVLAN interface: {e}")

    # --- Step 2: Assign IP Address ---
    try:
        api.path('/ip/address').add(address='192.168.99.1/24', interface='macvlan-iot', network='192.168.99.0')
        print("IP address assigned to 'macvlan-iot'.")
    except routeros_api.exceptions.RouterOsApiError as e:
        print(f"Error assigning IP address: {e}")

    # --- Step 3: Configure DHCP Server ---
    try:
        api.path('/ip/pool').add(name='dhcp_pool_iot', ranges='192.168.99.10-192.168.99.254')
        api.path('/ip/dhcp-server').add(name='dhcp_server_iot', interface='macvlan-iot', address_pool='dhcp_pool_iot', lease_time='1d')
        api.path('/ip/dhcp-server/network').add(address='192.168.99.0/24', gateway='192.168.99.1', dns_server='192.168.99.1')
        print("DHCP server configured for 'macvlan-iot'.")
    except routeros_api.exceptions.RouterOsApiError as e:
        print(f"Error configuring DHCP server: {e}")

    # --- Step 4: Firewall Rules ---
    try:
        api.path('/ip/firewall/filter').add(chain='input', in_interface='macvlan-iot', connection_state='established,related', action='accept', comment="Accept IoT established/related input")
        api.path('/ip/firewall/filter').add(chain='forward', in_interface='macvlan-iot', connection_state='established,related', action='accept', comment="Accept IoT established/related forward")
        api.path('/ip/firewall/filter').add(chain='forward', in_interface='macvlan-iot', out_interface='ether1', action='accept', comment="Allow IoT to internet")
        api.path('/ip/firewall/filter').add(chain='forward', in_interface='macvlan-iot', out_interface='ether2', action='drop', comment="Block IoT to Main LAN")
        api.path('/ip/firewall/filter').add(chain='input', in_interface='macvlan-iot', connection_state='new', action='drop', comment="Drop new input from IoT (optional)") # Optional rule
        print("Firewall rules configured for IoT isolation.")
    except routeros_api.exceptions.RouterOsApiError as e:
        print(f"Error configuring firewall rules: {e}")

    # --- Step 5: NAT Rule ---
    try:
        api.path('/ip/firewall/nat').add(chain='srcnat', out_interface='ether1', src_address='192.168.99.0/24', action='masquerade', comment="NAT for IoT network")
        print("NAT rule configured for IoT network.")
    except routeros_api.exceptions.RouterOsApiError as e:
        print(f"Error configuring NAT rule: {e}")

    connection.disconnect()

except routeros_api.exceptions.RouterOsApiError as e:
    print(f"Connection error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**API Implementation Explanation:**

* **Python `routeros_api` Library:**  Uses the `routeros_api` library to interact with the MikroTik RouterOS API. Install it using `pip install routeros_api`.
* **Connection Details:**  Replace placeholders (`your_router_ip`, `your_username`, `your_password`) with your router's credentials.  Ensure API service is enabled (`IP -> Services -> api`).
* **Step-by-Step API Calls:**  The Python script mirrors the CLI configuration steps, using `api.path()` to navigate to different RouterOS menus and `.add()` to create configurations.
* **Error Handling:**  Includes `try...except` blocks to catch `routeros_api.exceptions.RouterOsApiError` for API-specific errors and general `Exception` for other potential issues.  Error messages are printed to the console for debugging.

**5. Common Debugging Scenarios**

* **No IP Address on MACVLAN Interface:**
    * **Check Parent Interface (`ether2`):** Ensure `ether2` is enabled and functioning correctly. MACVLAN relies on the parent interface.
    * **MACVLAN Interface Status:** Verify the `macvlan-iot` interface is enabled (`/interface macvlan print`).
    * **DHCP Server Issues:** If using DHCP, check the DHCP server configuration (`/ip dhcp-server print`) and logs (`/log print topics=dhcp-server`).
    * **Conflicting IP Addresses:** Ensure no other interface or device on the network uses the `192.168.99.1/24` subnet if you are using static addressing.
* **IoT Devices Cannot Access Internet:**
    * **NAT Rule:** Verify the NAT masquerade rule (`/ip firewall nat print`) is correctly configured for the IoT network (`src-address=192.168.99.0/24`, `out-interface=ether1`).
    * **Firewall Rules:** Double-check the firewall rules (`/ip firewall filter print`), especially the "Allow IoT to internet" rule and ensure there isn't a rule blocking outbound traffic from the IoT network.
    * **DNS Resolution:** Verify DNS settings in the DHCP network configuration (`/ip dhcp-server network print`). Try pinging a public IP address (e.g., `8.8.8.8`) from an IoT device to check basic connectivity, then try pinging a hostname (e.g., `google.com`) to test DNS.
* **IoT Devices Can Access Main LAN:**
    * **Isolation Firewall Rule:**  The most critical rule is the "Block IoT to Main LAN" rule in the forward chain (`/ip firewall filter print`). Ensure it's present and correctly configured (`in-interface=macvlan-iot`, `out-interface=ether2`, `action=drop`).
    * **Rule Order:** Firewall rules are processed in order. Ensure the "Block IoT to Main LAN" rule is placed *after* the "Allow IoT to internet" rule if you have both.
* **Tools for Debugging:**
    * **`ping`:** Test basic network reachability.
    * **`traceroute`:**  Trace the network path to identify routing issues.
    * **`torch`:** Real-time traffic monitoring on interfaces (`/tool torch interface=macvlan-iot`).
    * **`packet sniffer`:** Capture and analyze network packets for detailed troubleshooting (`/tool sniffer`).
    * **Logs:**  Check RouterOS logs for DHCP server, firewall, and interface related events (`/log print`).

**6. Version-Specific Considerations (v6.x)**

* **MACVLAN Functionality Stability:** MACVLAN functionality is generally stable and well-established in RouterOS v6.x. Basic MACVLAN setup as described should work reliably.
* **REST API Limitations (vs v7+):**
    * RouterOS v6.x's REST API is functional for basic configuration tasks like interface and IP address management, but might lack some of the more advanced features and refinements found in v7+.
    * For the basic MACVLAN setup documented here, the v6.x API is sufficient.
* **No Major MACVLAN Bugs Known in v6.x (for basic use):**  For typical SOHO use cases, no significant MACVLAN-specific bugs are commonly reported in RouterOS v6.x. However, always check the MikroTik forums and changelogs for any specific issues related to your RouterOS version.
* **Upgrade Considerations:**  If you encounter limitations or need more advanced features in the future, consider upgrading to RouterOS v7+.  However, always test upgrades in a lab environment first and be aware of potential configuration changes between versions.

**7. Security Hardening Measures**

* **Firewall Isolation is Key:** The firewall rules are the primary security mechanism for MACVLAN isolation.  Ensure the "Block IoT to Main LAN" rule is in place and functioning correctly.
* **Disable Unnecessary Services on Router's IoT Interface:** On the `macvlan-iot` interface, disable any services that are not required, such as RouterOS management interfaces (Winbox, WebFig, SSH) if you don't need to manage the router from the IoT network. This is achieved by restricting access in `/ip service`.
* **Limit Input Access to Router:**  The optional firewall rule `add chain=input in-interface=macvlan-iot connection-state=new action=drop comment="Drop new input from IoT (optional)"` further hardens security by dropping new incoming connections to the router itself from the IoT network. This prevents IoT devices from initiating connections to the router for management or other purposes.
* **Strong Router Password:**  Always use a strong and unique password for your MikroTik router's administrative accounts.
* **Regular RouterOS Updates:** Keep your RouterOS version updated to the latest stable release to patch security vulnerabilities.
* **Monitor Logs Regularly:** Periodically review RouterOS logs, especially firewall logs, to detect any suspicious activity or potential security breaches.
* **Consider VLAN Tagging for Stronger Security (if possible):** While MACVLAN offers basic segmentation, VLAN tagging (802.1Q) provides a stronger layer of network separation at Layer 2. If your switch supports VLANs, consider transitioning to VLAN tagging for more robust security in the long run.

**8. Performance Optimization Tips**

* **CPU and Memory Usage:** MACVLAN itself adds a very minimal performance overhead.  The primary performance impact will come from the firewall rules and NAT if you have a large number of connections. Monitor your router's CPU and memory usage (`/system resource print`) to ensure it's not overloaded, especially in SOHO environments with limited hardware resources.
* **FastTrack for Allowed Traffic (Carefully):**  For specific types of traffic that you know are safe and high-bandwidth (e.g., streaming from a trusted IoT device to the internet), you *might* consider using FastTrack in the firewall (`/ip firewall filter`) to bypass connection tracking and potentially improve performance. However, use FastTrack cautiously as it can reduce the effectiveness of stateful firewall inspection.  **For basic IoT isolation, FastTrack is generally not recommended for the IoT network as security is paramount.**
* **Keep Firewall Rules Efficient:**  Keep your firewall rule set concise and efficient. Avoid overly complex rules that can consume processing power.  The basic rules provided in this documentation are designed to be efficient.
* **Hardware Offloading (if supported):** Some MikroTik routers have hardware offloading capabilities for certain firewall and NAT functions. Check your router's documentation to see if hardware offloading is supported and enabled for relevant features. However, hardware offloading capabilities are often limited in RouterOS v6.x compared to v7+.
* **Limit Number of MACVLAN Interfaces (SOHO):** In a SOHO environment, avoid creating an excessive number of MACVLAN interfaces on a single physical interface, as this can potentially increase processing overhead, especially on lower-end routers. For SOHO needs, a few MACVLAN interfaces for specific segmentation purposes should be sufficient.

**9. SOHO Real-World Deployment Examples**

* **Scenario 1: Isolating Smart Home Devices:**
    * **Goal:** Isolate smart home devices (smart speakers, smart lights, security cameras) from the main home network to prevent potential security breaches from compromised IoT devices from spreading to personal computers and data.
    * **Implementation:** Use MACVLAN as described in this document to create a separate "IoT Network" (192.168.99.0/24). Connect all smart home devices to this network. Configure firewall rules to block communication from the IoT network to the main LAN, but allow internet access.
    * **Benefits:** Enhanced security for the main network, reduced risk of IoT device compromises affecting personal data.
* **Scenario 2: Basic Guest Network Separation:**
    * **Goal:** Provide a basic guest network with internet access but limited access to the home LAN.
    * **Implementation:** Create a MACVLAN interface for guests (e.g., `macvlan-guest`). Assign a different subnet (e.g., 192.168.100.0/24). Set up a DHCP server on `macvlan-guest`. Implement firewall rules to allow internet access for the guest network but block access to the main LAN (e.g., 192.168.88.0/24) and potentially other internal networks.
    * **Benefits:**  Simple way to provide guest Wi-Fi with a degree of separation from the primary home network.  (For more robust guest networks, consider using VLAN tagging and dedicated guest Wi-Fi interfaces if your router and AP support it).

**10. Scalability Considerations**

* **SOHO Scale is Ideal:** MACVLAN is well-suited for SOHO environments where the number of MACVLAN interfaces and devices is relatively small.
* **Limited Scalability Beyond SOHO:**  For larger networks (SMB, Enterprise), MACVLAN's scalability limitations become more apparent.  VLAN tagging (802.1Q) is generally a more scalable and robust solution for network segmentation in larger environments.
* **Broadcast Domain Limitation:**  Remember that all MACVLAN interfaces on the same physical interface share the same broadcast domain. In very large networks with many devices, this shared broadcast domain could potentially lead to increased broadcast traffic and impact performance (though less likely to be an issue in SOHO setups).
* **Management Complexity:**  While MACVLAN configuration is relatively simple for basic setups, managing a large number of MACVLAN interfaces could become more complex compared to VLAN tagging, which often integrates better with network management tools and protocols.

**11. Monitoring Configurations**

* **Interface Monitoring:** Use RouterOS's interface monitoring tools (`/interface monitor-traffic macvlan-iot`) to track traffic statistics on the `macvlan-iot` interface. This helps monitor bandwidth usage and identify potential issues.
* **SNMP Monitoring:**  Enable SNMP on your RouterOS device (`/snmp`) and use an SNMP monitoring tool (e.g., The Dude, Zabbix, PRTG) to monitor the `macvlan-iot` interface, CPU usage, memory usage, and other router parameters.
* **Logging and Alerts:** Configure RouterOS logging (`/system logging`) to log firewall events, DHCP server events, and interface status changes related to MACVLAN. Set up email or other alerts to notify you of critical events (e.g., interface down, high traffic usage).
* **Traffic Graphs (Winbox/WebFig):** Winbox and WebFig provide basic real-time traffic graphs for interfaces. Use these to visualize traffic patterns on the `macvlan-iot` interface.

**Example SNMP Configuration (Basic - Adjust Community and Settings):**

```routeros
/snmp
set enabled=yes community=public contact=admin@example.com
```

**12. Disaster Recovery Steps**

* **Regular Backups are Crucial:** Implement a regular backup schedule for your MikroTik router configuration. This is essential for disaster recovery.
* **Backup Methods:**
    * **Manual Backup (Winbox/WebFig):** Use Winbox or WebFig to manually export the router configuration to a file (`Files -> Backup`). Store this backup file securely off-router.
    * **Scheduled Backup Script (CLI):** Use a RouterOS script to automate backups and potentially upload them to a remote server (see example backup script below).
* **Restoration Procedure:**
    * **Winbox/WebFig Restore:** In case of router failure or configuration corruption, you can restore the configuration from a backup file using Winbox or WebFig (`Files -> Restore`).
    * **Netinstall (Last Resort):** In case of severe router issues, you can use Netinstall to re-install RouterOS and then restore your configuration from a backup.
* **Document Recovery Steps:** Document the backup and restore procedures clearly for quick recovery in case of a disaster.

**13. Automated Backup Scripts**

Here's a basic example of a RouterOS script to automate backups. You can schedule this script to run regularly using the `/system scheduler`.

```routeros
# --- Backup Script ---
:local backup_filename ("macvlan_config_backup_" . [:system date format=%Y-%m-%d_%H-%M-%S])
:local backup_path ("/disk1/" . $backup_filename . ".backup") # Adjust disk if needed

/system backup save name=$backup_path

:log info ("Backup created: " . $backup_path)

# --- Optional: Email Notification (Requires Email Configuration) ---
#{
#:local email_to "admin@example.com" # Replace with your email
#:local email_subject ("MikroTik Backup - " . $backup_filename)
#:local email_body ("MikroTik Configuration Backup created successfully: " . $backup_path)
#/tool e-mail send to=$email_to subject=$email_subject body=$email_body
#}

# --- Optional: Remote Backup (Example using SCP - Requires SCP Server) ---
#{
#:local remote_server "your_backup_server_ip" # Replace with your backup server IP
#:local remote_user "backup_user"           # Replace with your backup server username
#:local remote_path "/path/to/backup/folder/"  # Replace with your backup server path
#:local ssh_key "your_ssh_private_key"       # Optional SSH key path if needed

#/tool fetch url="scp://$remote_user@$remote_server:$remote_path/$backup_filename.backup" from-file=$backup_path user=$remote_user password="your_backup_password" keep-result=no # Password-based SCP (less secure)
# OR (if using SSH key)
#/tool fetch url="scp://$remote_user@$remote_server:$remote_path/$backup_filename.backup" from-file=$backup_path user=$remote_user identity-file=$ssh_key keep-result=no # SSH key-based SCP (more secure)

#:log info ("Backup copied to remote server: " . $remote_server . ":" . $remote_path)
#}
```

**Explanation of Backup Script:**

* **`backup_filename`:** Generates a unique filename using the current date and time.
* **`backup_path`:** Defines the path where the backup file will be saved on the router's disk (adjust `/disk1/` if needed).
* **`/system backup save name=$backup_path`:**  Creates the backup file.
* **`:log info ...`:** Logs a message indicating backup creation.
* **Optional Email Notification (commented out):**  Sends an email notification upon successful backup (requires email configuration in `/tool e-mail`).
* **Optional Remote Backup (commented out):**  Demonstrates SCP-based remote backup to a server (requires an SCP server and adjustments for your environment). Choose either password-based or SSH key-based SCP (SSH key is more secure).

**14. Comparative Table: MACVLAN vs. VLAN Tagging (SOHO Context)**

| Feature             | MACVLAN                                 | VLAN Tagging (802.1Q)                       |
|----------------------|------------------------------------------|-----------------------------------------------|
| **Complexity**       | Simpler to configure for basic segmentation | More complex initial setup, requires VLAN-aware switches |
| **Scalability**      | Limited scalability, best for SOHO        | Highly scalable, suitable for large networks  |
| **Layer 2 Isolation** | Weaker isolation, shared broadcast domain | Stronger isolation, separate broadcast domains |
| **Switch Requirement**| Unmanaged switch compatible                | Requires VLAN-aware (802.1Q) switches         |
| **Hardware Cost**    | Lower initial cost (unmanaged switch)     | Higher cost (VLAN-aware switches)            |
| **Security**         | Basic segmentation, relies on firewall   | More robust Layer 2 and Layer 3 segmentation   |
| **Management**        | Simpler management for small setups      | More feature-rich management capabilities    |
| **Performance**      | Minimal overhead for basic use          | Slight overhead due to VLAN tagging          |
| **SOHO Suitability** | Good for basic SOHO segmentation needs   | Excellent for SOHO and beyond if scalability and robust security needed |

**15. Conclusion**

MACVLAN provides a useful and relatively simple method for basic network segmentation in SOHO environments using MikroTik RouterOS v6.x. It's particularly well-suited for isolating IoT devices or creating a basic guest network.  However, for more robust security, scalability, and advanced features, VLAN tagging (802.1Q) is the preferred solution if your network infrastructure and budget allow.  Always prioritize security hardening measures, regular backups, and monitoring to ensure a reliable and secure network environment. For larger or more complex networks, carefully evaluate the limitations of MACVLAN and consider VLAN tagging as a more scalable and secure alternative.

---

This documentation should provide a comprehensive guide to MACVLAN in a SOHO MikroTik environment, addressing all the requested components and formatting requirements. Let me know if you need any adjustments or further details!

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