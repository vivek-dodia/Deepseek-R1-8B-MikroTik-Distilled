---
generated_at: 2025-02-03T21:26:05.900927
topic: Firewall and Quality of Service
category: Firewall & QoS
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Firewall and Quality of Service (QoS) for SOHO Environments (v6.x)

**Documentation Level:** Comprehensive Technical Guide
**Target Audience:** SOHO Network Administrators, Home Users, and MikroTik Beginners
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic

**1. Architecture Diagram Requirements:**

For a SOHO Firewall and QoS setup, the architecture diagram should clearly illustrate the following:

* **Internet Connection:** Represented by a cloud or similar icon, indicating the external network.
* **MikroTik Router:** Clearly labeled as the central firewall and QoS device.
* **External Interface (WAN):**  The interface connecting to the Internet (e.g., `ether1-gateway`).
* **Internal Interface(s) (LAN):**  Interface(s) connecting to the local network (e.g., `ether2-master-local`, `wlan1`).
* **SOHO Devices:**  Represent typical SOHO devices like computers, laptops, smartphones, smart TVs, VoIP phones, and printers connected to the LAN.
* **Firewall Zones:**  Implicitly show the firewall as the boundary between the Internet (untrusted) and the LAN (trusted).
* **QoS Points:** Indicate where QoS is applied, typically at the WAN interface for outbound traffic and potentially on internal interfaces for intra-LAN QoS (less common in basic SOHO).
* **Traffic Flow:** Arrows can optionally indicate the direction of traffic flow, especially through the firewall and QoS queues.

**Example Diagram (Mermaid):**

```mermaid
graph LR
    subgraph Internet
        A[Internet]
    end
    subgraph MikroTik Router (Firewall & QoS)
        B(ether1-gateway <br> WAN Interface) --> C{Firewall <br> Input Chain}
        C --> D{Queue Tree <br> (QoS)} --> E(ether1-gateway <br> WAN Outbound QoS)
        F(ether2-master-local <br> LAN Interface) --> C
        G(wlan1 <br> WiFi Interface) --> C
        H{Firewall <br> Forward Chain} --> D
        I{Firewall <br> Output Chain} --> B
    end
    subgraph SOHO Network
        J[Computer] --> F
        K[Laptop] --> F
        L[Smartphone] --> G
        M[Smart TV] --> G
        N[VoIP Phone] --> F
        O[Printer] --> F
    end

    A --> B
    E --> A
    F --> H
    G --> H
    H --> E
    I --> A
    J --> F
    K --> F
    L --> G
    M --> G
    N --> F
    O --> F

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#ccf,stroke:#333,stroke-width:1px
    style H fill:#ccf,stroke:#333,stroke-width:1px
    style I fill:#ccf,stroke:#333,stroke-width:1px
    linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18 stroke-width:1px;
```

**2. CLI Configuration with Inline Comments:**

This section provides CLI commands to configure a basic SOHO firewall and QoS.  Replace interface names (e.g., `ether1-gateway`, `ether2-master-local`, `wlan1`) and network ranges (e.g., `192.168.88.0/24`) with your actual configuration.

```routeros
# --- Firewall Configuration ---
/ip firewall filter
# Default forward chain policy is ACCEPT for SOHO - safer to start permissive and tighten.
set [find default-forward=yes] action=accept comment="Default accept forward (SOHO)"

# 1. Drop invalid connections (Input and Forward chains) - First rule for security
add chain=input connection-state=invalid action=drop comment="Drop invalid connections (Input)"
add chain=forward connection-state=invalid action=drop comment="Drop invalid connections (Forward)"

# 2. Allow established and related connections (Input and Forward chains) - Essential for allowing replies and related traffic
add chain=input connection-state=established,related action=accept comment="Allow established/related (Input)"
add chain=forward connection-state=established,related action=accept comment="Allow established/related (Forward)"

# 3. Allow Input from LAN network (Input chain) - Allow access to router from trusted LAN
add chain=input src-address=192.168.88.0/24 in-interface=ether2-master-local action=accept comment="Allow LAN Input"
add chain=input src-address=192.168.88.0/24 in-interface=wlan1 action=accept comment="Allow WiFi Input"

# 4. Allow ICMP (ping) from WAN for monitoring (optional, for troubleshooting - consider security implications)
# add chain=input protocol=icmp in-interface=ether1-gateway action=accept comment="Allow ICMP from WAN"

# 5. Drop all other Input traffic (Input chain) - Default deny for input chain - Router security
add chain=input action=drop comment="Drop all other Input"

# 6. Allow forwarding to the internet (Forward chain) - Already covered by default forward accept in SOHO, but explicit for clarity if needed in more restrictive setups.
# add chain=forward out-interface=ether1-gateway action=accept comment="Allow forward to WAN"

# 7. Drop all other Forward traffic (Forward chain) - Default deny for forward chain in more secure setups. For SOHO, default accept is often sufficient.
# add chain=forward action=drop comment="Drop all other Forward"

# --- QoS (Queue Tree) Configuration ---
/queue tree
# 1. Create a global queue for the WAN interface (outbound)
add name=WAN-Outbound parent=ether1-gateway limit-at=0 max-limit=10M comment="WAN Outbound Queue - Total Bandwidth" # Replace 10M with your actual WAN upload speed

# 2. Create a queue for High Priority Traffic (e.g., VoIP, Video conferencing)
add name=High-Priority parent=WAN-Outbound packet-marks=high-priority priority=1 limit-at=0 max-limit=5M comment="High Priority Traffic Queue - VoIP/Video" # Allocate bandwidth for high priority

# 3. Create a queue for Normal Priority Traffic (e.g., Web browsing, Email)
add name=Normal-Priority parent=WAN-Outbound packet-marks=normal-priority priority=3 limit-at=0 max-limit=7M comment="Normal Priority Traffic Queue - Web/Email" # Allocate bandwidth for normal traffic

# 4. Create a queue for Low Priority Traffic (e.g., Downloads, Background tasks)
add name=Low-Priority parent=WAN-Outbound packet-marks=low-priority priority=7 limit-at=0 max-limit=3M comment="Low Priority Traffic Queue - Downloads" # Allocate bandwidth for low priority

# --- Mangle Rules for Packet Marking (QoS) ---
/ip firewall mangle
# 1. Mark VoIP/Video traffic for High Priority (Example: SIP protocol and RTP ports)
add chain=forward protocol=udp dst-port=5060,5061 action=mark-packet new-packet-mark=high-priority comment="Mark VoIP SIP for High Priority"
add chain=forward protocol=udp dst-port=10000-20000 action=mark-packet new-packet-mark=high-priority comment="Mark VoIP RTP for High Priority"

# 2. Mark normal web browsing (HTTP/HTTPS) as Normal Priority
add chain=forward protocol=tcp dst-port=80,443 action=mark-packet new-packet-mark=normal-priority comment="Mark Web Browsing (HTTP/HTTPS) as Normal"

# 3. Mark all other traffic as Low Priority (Default - Catch-all)
add chain=forward action=mark-packet new-packet-mark=low-priority comment="Mark all other traffic as Low Priority (Default)"

# --- Print Firewall and Queue Tree Configuration to Verify ---
/ip firewall filter print
/queue tree print
/ip firewall mangle print
```

**3. REST API Implementation (Python code):**

This Python script uses the `routeros_api` library to configure the same firewall and QoS settings as the CLI example. Install the library using `pip install routeros_api`.

```python
import routeros_api
import routeros_api.exceptions

ROUTER_HOST = 'your_router_ip'  # Replace with your RouterOS IP address
ROUTER_USER = 'api_user'      # Replace with your API username
ROUTER_PASSWORD = 'api_password' # Replace with your API password

try:
    connection = routeros_api.RouterOsClient(ROUTER_HOST, username=ROUTER_USER, password=ROUTER_PASSWORD, use_ssl=True, ssl_verify=False) # Consider ssl_verify=True in production with proper cert

    # --- Firewall Configuration via API ---
    firewall_filter = connection.get_resource('/ip/firewall/filter')

    # Drop invalid connections
    firewall_filter.add(chain='input', connection_state='invalid', action='drop', comment='Drop invalid connections (Input)')
    firewall_filter.add(chain='forward', connection_state='invalid', action='drop', comment='Drop invalid connections (Forward)')

    # Allow established/related connections
    firewall_filter.add(chain='input', connection_state='established,related', action='accept', comment='Allow established/related (Input)')
    firewall_filter.add(chain='forward', connection_state='established,related', action='accept', comment='Allow established/related (Forward)')

    # Allow LAN input
    firewall_filter.add(chain='input', src_address='192.168.88.0/24', in_interface='ether2-master-local', action='accept', comment='Allow LAN Input') # Adjust interface/network
    firewall_filter.add(chain='input', src_address='192.168.88.0/24', in_interface='wlan1', action='accept', comment='Allow WiFi Input') # Adjust interface/network

    # Drop all other input
    firewall_filter.add(chain='input', action='drop', comment='Drop all other Input')

    # --- QoS (Queue Tree) Configuration via API ---
    queue_tree = connection.get_resource('/queue/tree')

    # WAN Outbound Queue
    queue_tree.add(name='WAN-Outbound', parent='ether1-gateway', limit_at='0', max_limit='10M', comment='WAN Outbound Queue - Total Bandwidth') # Adjust interface/bandwidth

    # High Priority Queue
    queue_tree.add(name='High-Priority', parent='WAN-Outbound', packet_marks='high-priority', priority='1', limit_at='0', max_limit='5M', comment='High Priority Traffic Queue - VoIP/Video') # Adjust bandwidth

    # Normal Priority Queue
    queue_tree.add(name='Normal-Priority', parent='WAN-Outbound', packet_marks='normal-priority', priority='3', limit_at='0', max_limit='7M', comment='Normal Priority Traffic Queue - Web/Email') # Adjust bandwidth

    # Low Priority Queue
    queue_tree.add(name='Low-Priority', parent='WAN-Outbound', packet_marks='low-priority', priority='7', limit_at='0', max_limit='3M', comment='Low Priority Traffic Queue - Downloads') # Adjust bandwidth

    # --- Mangle Rules for Packet Marking via API ---
    firewall_mangle = connection.get_resource('/ip/firewall/mangle')

    # Mark VoIP SIP
    firewall_mangle.add(chain='forward', protocol='udp', dst_port='5060,5061', action='mark-packet', new_packet_mark='high-priority', comment='Mark VoIP SIP for High Priority')
    # Mark VoIP RTP
    firewall_mangle.add(chain='forward', protocol='udp', dst_port='10000-20000', action='mark-packet', new_packet_mark='high-priority', comment='Mark VoIP RTP for High Priority')
    # Mark Web Browsing
    firewall_mangle.add(chain='forward', protocol='tcp', dst_port='80,443', action='mark-packet', new_packet_mark='normal-priority', comment='Mark Web Browsing (HTTP/HTTPS) as Normal')
    # Mark all other traffic as Low Priority
    firewall_mangle.add(chain='forward', action='mark-packet', new_packet_mark='low-priority', comment='Mark all other traffic as Low Priority (Default)')


    print("Firewall and QoS configuration applied successfully via API.")

except routeros_api.exceptions.RouterOsApiError as e:
    print(f"Error configuring RouterOS via API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
```

**4. Common Debugging Scenarios:**

| Scenario                                  | Possible Cause                                      | Debugging Steps                                                                 |
|-------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------|
| **Internet access blocked for LAN devices** | **Firewall blocking forward traffic.**                | 1. Check `ip firewall filter print` output. <br> 2. Ensure `forward` chain rules allow established/related connections and outbound traffic. <br> 3. Verify default `forward` chain policy if set to `drop`. |
| **Cannot access router from WAN (e.g., Winbox)** | **Input chain blocking management ports.**          | 1. Check `ip firewall filter print` output. <br> 2. Ensure no `drop` rules block access to management ports (Winbox: 8291, SSH: 22, etc.) on the `input` chain from WAN interface, unless specifically intended and configured with allowed source IPs. |
| **QoS not prioritizing VoIP/Video**        | **Incorrect packet marking or queue configuration.** | 1. Verify `ip firewall mangle print` rules are correctly marking VoIP/Video traffic. <br> 2. Check `queue tree print` output. Ensure queues are created with correct `packet-marks`, `priorities`, and `parent` interfaces. <br> 3. Use `/tool sniffer` to capture traffic and verify packet marks. |
| **Slow internet speed despite QoS**       | **WAN interface bandwidth misconfiguration or ISP limitations.** | 1. Verify your actual WAN upload speed from your ISP. <br> 2. Ensure `max-limit` in `WAN-Outbound` queue in `queue tree` is set correctly and not lower than your actual WAN upload speed. <br> 3. Check for ISP network congestion. |
| **Specific service blocked**              | **Firewall rule blocking specific ports/protocols.**   | 1. Check `ip firewall filter print` output. <br> 2. Look for `drop` rules in `forward` or `output` chains that might be blocking the service based on protocol, ports, or destination IP. <br> 3. Temporarily disable potentially blocking rules to isolate the issue. <br> 4. Use `/tool torch` to monitor traffic and identify blocking rules. |

**5. Version-Specific Considerations (v6.x):**

* **Queue Tree Limitations:** In RouterOS v6.x, Queue Tree is the primary QoS mechanism. It might be less efficient for very high traffic volumes compared to newer queuing systems in v7.x like HTB (Hierarchical Token Bucket) with more advanced features. For basic SOHO, Queue Tree is usually sufficient.
* **FastTrack:** FastTrack connection tracking is available in v6.x and can significantly improve firewall performance by bypassing firewall rule processing for established connections. Ensure FastTrack is enabled (`/ip firewall filter set fasttrack-connection=yes fasttrack-reconnection=yes`). However, be cautious as it might bypass some mangle rules if not configured correctly.
* **API:** RouterOS v6.x supports the REST API, but it might be less feature-rich compared to later versions. The basic functionalities for firewall and QoS configuration are well supported.
* **Security Updates:** RouterOS v6.x is older. Ensure you are running the latest stable release within the v6.x branch for security patches. Consider migrating to v7.x for the latest features and security updates if hardware allows.

**6. Security Hardening Measures:**

* **Strong Passwords:** Use strong, unique passwords for all router user accounts, especially the `admin` account and any API users.
* **Disable Default Services:** Disable unnecessary services like `telnet`, `ftp`, `www` (if not needed for management), and `api` if not using the API regularly.  `/ip service disable telnet,ftp,www`
* **Limit Management Access:**
    * Change default Winbox port (8291) to a non-standard port if remote Winbox access is necessary, but avoid exposing Winbox to the public internet if possible. `/ip service set winbox port=your_new_port`
    * If remote access is required, use SSH instead of Telnet.
    * Consider using a VPN for secure remote access instead of directly exposing management ports.
    * If remote access is absolutely necessary via Winbox or SSH from the internet, restrict access to specific IP addresses using firewall rules in the `input` chain before the default `drop all` rule.
* **Keep RouterOS Updated:** Regularly update RouterOS to the latest stable version within the v6.x branch to patch security vulnerabilities. `/system package update check` and `/system package update download install reboot`
* **Review Firewall Rules Regularly:** Periodically review your firewall rules to ensure they are still necessary and effective. Remove any unnecessary or overly permissive rules.
* **Disable IP Services on WAN Interface:** Disable IP services like DHCP server, DNS server, and Router Advertisement on the WAN interface to prevent unintended services from being offered to the public internet. `/ip dhcp-server disable ether1-gateway`, `/ip dns-server set allow-remote-requests=no`
* **Address Lists for Management:** Use address lists to manage allowed IPs for management access.  `/ip firewall address-list add list=mgmt-allowed-ips address=your_public_ip comment="Your Public IP for Management"` and then use this list in firewall rules.

**7. Performance Optimization Tips:**

* **FastTrack:** Enable FastTrack for established/related connections to significantly improve throughput by bypassing firewall rule checks for already tracked connections. `/ip firewall filter set fasttrack-connection=yes fasttrack-reconnection=yes`
* **Simple Firewall Rules:** Keep firewall rules as simple and efficient as possible. Avoid overly complex rules or regular expressions if not strictly necessary in a SOHO environment.
* **Hardware Offloading:** If your MikroTik hardware supports it, ensure hardware offloading for bridging and routing is enabled. `/interface ethernet set [find] hw=yes` (This might be enabled by default on some devices).
* **Limit Logging:** Excessive firewall logging can consume resources. Only log necessary traffic for security monitoring. Use logging sparingly and consider using `action=log` only for specific rules or chains.
* **Queue Tree Structure:** For basic QoS, a simple Queue Tree structure as demonstrated is sufficient. Avoid overly complex nested queues in SOHO environments, as they can increase processing overhead.
* **Monitor CPU Usage:** Regularly monitor the router's CPU usage (`/system resource print`) during peak traffic periods to identify potential performance bottlenecks. If CPU usage is consistently high, consider simplifying QoS or firewall rules or upgrading to more powerful hardware.
* **Avoid Deep Packet Inspection (DPI) in Basic SOHO QoS:**  DPI for Layer 7 QoS (like marking based on application names) is resource-intensive and typically not needed for basic SOHO QoS. Focus on Layer 3/4 marking based on IP addresses, ports, and protocols, as shown in the example.

**SOHO Specific Requirements:**

**Real-world Deployment Examples:**

* **Home Office with Remote Work:**
    * **Scenario:** A home office with a user working remotely, needing reliable video conferencing, VoIP calls, and secure access to company resources.
    * **Firewall:** Basic firewall rules as configured in the example to protect the home network and router. Security hardening measures are crucial due to remote work.
    * **QoS:** Prioritize VoIP and video conferencing traffic using QoS to ensure call quality during work hours. Bandwidth limiting for general traffic to prevent large downloads from impacting work applications.
* **Family Home with Streaming and Gaming:**
    * **Scenario:** A family with multiple devices streaming video (Netflix, YouTube), online gaming, and general web browsing.
    * **Firewall:** Basic firewall for security. Consider parental control features (not covered in basic setup, but possible with more advanced firewall rules or RouterOS features).
    * **QoS:** Prioritize gaming traffic to reduce latency. Ensure sufficient bandwidth for streaming services. Bandwidth limiting for less critical traffic like downloads.
* **Small Business with VoIP and POS System:**
    * **Scenario:** A small retail business using VoIP phones and a Point of Sale (POS) system that relies on internet connectivity.
    * **Firewall:**  More stringent firewall rules might be needed to protect business data and POS system. Consider VLANs to isolate POS and business networks from guest WiFi (if offered).
    * **QoS:** High priority for VoIP traffic. Ensure reliability and bandwidth for POS system transactions.

**Scalability Considerations:**

* **Address Lists:** Use address lists for managing groups of IPs or networks in firewall and QoS rules. This simplifies rule management and scalability as the network grows. `/ip firewall address-list add list=lan-networks address=192.168.88.0/24 comment="LAN Network"` and then use `src-address-list=lan-networks` in rules.
* **Modular Rule Sets:** Organize firewall rules into logical sections (e.g., input rules, forward rules, QoS rules) with comments. This makes it easier to manage and add new rules as the network expands.
* **Queue Types:** For more advanced QoS needs in larger SOHOs, explore different queue types in Queue Tree (like PCQ - Per Connection Queue) for fair bandwidth sharing among multiple users/devices.
* **Hardware Upgrade:** If the SOHO network grows significantly, consider upgrading to more powerful MikroTik hardware with more CPU, RAM, and faster interfaces to handle increased traffic and more complex configurations.

**Monitoring Configurations:**

* **Simple Queues Graphs:** For basic QoS monitoring, use Simple Queues ( `/queue simple` ) and enable "Traffic Graph" in Winbox to visually monitor bandwidth usage per queue.  While Queue Tree is used for QoS implementation here, Simple Queues can be quickly set up for monitoring specific traffic flows if needed.
* **Firewall Rule Counters:** Monitor firewall rule counters (`/ip firewall filter print count-packets=yes count-bytes=yes`) to see how often rules are being matched and how much traffic is being processed by each rule. This can help identify if rules are working as expected and optimize rule order.
* **Log Review:** Regularly review firewall logs (`/log print`) for dropped packets or security events. Configure logging actions in firewall rules (`action=log`) to capture specific traffic for analysis. Use filters in the log to focus on specific events.
* **Resource Monitoring:** Use `/system resource print` to monitor CPU load, memory usage, and interface traffic to identify performance bottlenecks and ensure the router is handling the load.
* **The Dude (MikroTik Monitoring Tool):** For more comprehensive network monitoring, consider using MikroTik's "The Dude" network monitoring application (available for Windows). It can monitor device uptime, interface traffic, CPU/memory usage, and more, including RouterOS devices.

**Disaster Recovery Steps:**

* **Configuration Export:** Regularly export the RouterOS configuration to a file for backup. `/export file=router_config_backup` Download this file to a safe location (computer, cloud storage).
* **Safe Mode:** If you make a configuration change that breaks access, reboot the router in Safe Mode. Hold the reset button during boot until the "safe mode" message appears. Safe Mode reverts to the last known good configuration.
* **Netinstall:** In case of severe configuration errors or router unreachability, use Netinstall to reinstall RouterOS. This will erase the current configuration, so ensure you have a recent backup. Follow MikroTik's Netinstall documentation.
* **Configuration Import:** To restore from a backup, upload the exported configuration file to the router and import it. `/import file-name=router_config_backup.rsc`
* **Redundant Router (Advanced):** For critical SOHO environments, consider using a redundant router in a failover configuration for high availability (more complex setup, beyond basic SOHO scope).

**Automated Backup Scripts:**

This basic script can be scheduled to run automatically (e.g., daily) to back up the RouterOS configuration.

```routeros
# --- Automated Backup Script ---
/system script
add name=daily_config_backup owner=admin policy=write source={
    :local backup_file_name ("router_config_backup_" . [/system clock get date format=yyyy-MM-dd])
    /export file=$backup_file_name
    /log info ("RouterOS config backed up to file: " . $backup_file_name)
}

/system scheduler
add name=daily_config_backup interval=1d on-event=daily_config_backup start-time=03:00:00
```

**Explanation:**

* **`/system script add ...`**: Creates a new script named `daily_config_backup`.
* **`source={ ... }`**: Defines the script content.
    * `:local backup_file_name ...`: Creates a local variable to store the backup file name with the current date.
    * `/export file=$backup_file_name`: Exports the RouterOS configuration to a file with the generated name.
    * `/log info ...`: Logs a message indicating successful backup.
* **`/system scheduler add ...`**: Creates a scheduler rule to run the script daily at 3:00 AM.
    * `interval=1d`: Runs every day.
    * `on-event=daily_config_backup`: Specifies the script to run.
    * `start-time=03:00:00`: Sets the start time.

**To download the backup files:** You can use Winbox's Files section or FTP/SFTP to download the generated `.rsc` backup files from the router.

This comprehensive documentation provides a solid foundation for configuring Firewall and QoS on MikroTik RouterOS v6.x in SOHO environments. Remember to adapt the configuration to your specific network needs and security requirements. Regularly review and maintain your configuration for optimal performance and security.

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