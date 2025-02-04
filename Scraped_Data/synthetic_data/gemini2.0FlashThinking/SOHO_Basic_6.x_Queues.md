---
generated_at: 2025-02-03T21:31:09.237243
topic: Queues
category: Firewall & QoS
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Queues for SOHO Environments (Basic)

**Document Version:** 1.0
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic
**Author:** [Your Name/MTCINE Identifier]
**Date:** October 26, 2023

---

### 1. Architecture Diagram Requirements

For a SOHO environment, queues are typically implemented at the network edge to manage bandwidth usage primarily at the internet connection point. They can also be used internally to prioritize traffic within the local network.

**Diagram:**

```mermaid
graph LR
    A[Internet] --> B(MikroTik RouterOS);
    B --> C[SOHO Devices (PCs, Laptops, Phones)];
    subgraph SOHO Network
        direction LR
        C --> D{Queue - Internet Uplink};
        C --> E{Queue - Internet Downlink};
        F[LAN Devices] --> G{Queue - Internal};
        B --> D;
        B --> E;
        B --> G;
    end
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style A fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#ccf,stroke:#333,stroke-width:1px
    style F fill:#ccf,stroke:#333,stroke-width:1px
    style D fill:#eee,stroke:#333,stroke-width:1px
    style E fill:#eee,stroke:#333,stroke-width:1px
    style G fill:#eee,stroke:#333,stroke-width:1px

    linkStyle 0 stroke-width:2px,stroke:#0f0,color:black;
    linkStyle 0 text: "WAN Interface";
    linkStyle 1 stroke-width:2px,stroke:#0f0,color:black;
    linkStyle 1 text: "LAN Interface";
```

**Diagram Explanation:**

*   **Internet:** Represents the external network.
*   **MikroTik RouterOS:** The central router in the SOHO network, managing internet connectivity and internal network traffic.
*   **SOHO Devices (PCs, Laptops, Phones):** Devices connected to the SOHO network, generating and consuming network traffic.
*   **LAN Devices:**  Devices within the internal network that might require internal queue management (e.g., servers, specific workstations).
*   **Queue - Internet Uplink:** Queues applied to traffic going *from* the SOHO network *to* the internet (upload traffic).
*   **Queue - Internet Downlink:** Queues applied to traffic coming *from* the internet *to* the SOHO network (download traffic).
*   **Queue - Internal:** Queues applied to traffic flowing within the SOHO network, between LAN segments or specific devices.

For basic SOHO setup, we will primarily focus on **Internet Uplink and Downlink queues** to manage bandwidth at the internet gateway.

### 2. CLI Configuration with Inline Comments

We will use **Simple Queues** for basic SOHO queue management. Simple Queues are straightforward to configure and sufficient for most SOHO bandwidth control needs.

```routeros
/queue simple
# -----------------------------------------------------------------------
# 1. Global Settings (Optional, often defaults are fine for SOHO)
# -----------------------------------------------------------------------
# /queue simple set [ find default=yes ] queue=default-small  # Example to change default queue type (not usually needed)

# -----------------------------------------------------------------------
# 2. Create a queue to limit total download bandwidth for the entire SOHO network
# -----------------------------------------------------------------------
add name="download_limit_total" \
    target="<WAN_INTERFACE>"  \  # Replace <WAN_INTERFACE> with your actual WAN interface name (e.g., ether1)
    max-limit="50M/50M" \      # Set maximum download/upload limit (e.g., 50Mbps down/50Mbps up)
    comment="Limit total download/upload bandwidth for WAN interface"

# -----------------------------------------------------------------------
# 3. Create a queue to limit download bandwidth for a specific IP address (e.g., a heavy user's PC)
# -----------------------------------------------------------------------
add name="limit_specific_ip_download" \
    target="<USER_PC_IP>/32" \ # Replace <USER_PC_IP> with the IP address of the PC you want to limit (e.g., 192.168.88.100/32)
    parent="download_limit_total" \ # Apply this limit within the total bandwidth limit
    max-limit="10M/10M" \      # Set maximum download/upload limit for this IP (e.g., 10Mbps down/10Mbps up)
    comment="Limit download/upload for specific PC IP"

# -----------------------------------------------------------------------
# 4. Create a queue to prioritize VoIP traffic (using DSCP marking - Assumes VoIP devices mark packets with DSCP CS5)
# -----------------------------------------------------------------------
add name="prioritize_voip" \
    target="<LAN_NETWORK>" \     # Replace <LAN_NETWORK> with your LAN network address (e.g., 192.168.88.0/24)
    dst-port="5060,5061,10000-20000" \ # Common VoIP ports (SIP, RTP range - adjust as needed)
    protocol=udp \             # VoIP often uses UDP
    priority=1 \               # Set high priority (1 is highest)
    packet-marks="voip_packets" \ # Mark packets for further processing (e.g., in mangle)
    comment="Prioritize VoIP traffic - Marking packets"

# --- (Optional Mangle rule to mark VoIP packets - if DSCP marking not used by VoIP devices) ---
# /ip firewall mangle
# add chain=forward action=mark-packet new-packet-mark=voip_packets passthrough=no \
#     protocol=udp dst-port=5060,5061,10000-20000 in-interface=<LAN_INTERFACE> # Replace <LAN_INTERFACE> with your LAN interface

# --- (Apply priority using packet-mark in the queue) ---
# /queue simple
# set [ find name="prioritize_voip" ] packet-marks="voip_packets"

# -----------------------------------------------------------------------
# 5. View existing queues
# -----------------------------------------------------------------------
/queue simple print
```

**Explanation of CLI Commands:**

*   **`/queue simple`**: Navigates to the Simple Queue configuration menu.
*   **`add name="..." target="..." max-limit="..." comment="..."`**: Creates a new simple queue rule.
    *   **`name`**:  A unique name to identify the queue rule.
    *   **`target`**: Specifies the traffic to which the queue applies. Can be:
        *   Interface name (`<WAN_INTERFACE>`) - Applies to all traffic going through that interface.
        *   IP address or network (`<USER_PC_IP>/32`, `<LAN_NETWORK>`) - Applies to traffic to/from the specified IP or network.
    *   **`max-limit`**: Sets the maximum bandwidth limit for the queue in download/upload format (e.g., "10M/10M" for 10Mbps download and 10Mbps upload).
    *   **`comment`**:  Adds a description for the queue rule.
    *   **`parent`**:  Specifies a parent queue. The current queue's bandwidth will be limited by the parent queue's limit.
    *   **`priority`**: Sets the priority of the queue (1 is highest, 8 is lowest). Higher priority queues get bandwidth preference.
    *   **`dst-port`, `protocol`**:  Filter traffic based on destination port and protocol. Useful for prioritizing specific applications like VoIP.
    *   **`packet-marks`**: Associates a packet mark with the queue. This allows for more advanced traffic classification using Mangle rules.
*   **`print`**: Displays the list of configured simple queues.

**Important Notes:**

*   **Interface Names and IP Addresses:**  Replace placeholders like `<WAN_INTERFACE>`, `<USER_PC_IP>`, and `<LAN_NETWORK>` with your actual network configuration.
*   **Bandwidth Units:**  Use `K` for Kbps, `M` for Mbps, `G` for Gbps.
*   **Queue Order:** Simple Queues are processed in order of their appearance in the list. More specific queues should generally be placed before more general queues.
*   **Parent Queues:**  Using parent queues allows for hierarchical bandwidth management.  In the example, `limit_specific_ip_download` is limited *within* the `download_limit_total` queue.

### 3. REST API Implementation (Python Code)

This Python script uses the `routeros_api` library to configure the same Simple Queues as in the CLI example.

```python
import routeros_api
import routeros_api.exceptions

# RouterOS Connection Details
HOST = 'your_router_ip'      # Replace with your router's IP address
USER = 'api_user'            # Replace with your API username
PASSWORD = 'api_password'      # Replace with your API password
WAN_INTERFACE = 'ether1'      # Replace with your WAN interface name
USER_PC_IP = '192.168.88.100' # Replace with the specific user PC IP
LAN_NETWORK = '192.168.88.0/24' # Replace with your LAN network

try:
    api = routeros_api.RouterOsApiPool(HOST, username=USER, password=PASSWORD, plaintext_login=True)
    connection = api.get_connection()
    queue_simple = connection.get_resource('/queue/simple')

    # -----------------------------------------------------------------------
    # 1. Create a queue to limit total download bandwidth for the entire SOHO network
    # -----------------------------------------------------------------------
    queue_simple.add(
        name='download_limit_total',
        target=WAN_INTERFACE,
        max_limit='50M/50M',
        comment='Limit total download/upload bandwidth for WAN interface'
    )
    print("Queue 'download_limit_total' created.")

    # -----------------------------------------------------------------------
    # 2. Create a queue to limit download bandwidth for a specific IP address
    # -----------------------------------------------------------------------
    queue_simple.add(
        name='limit_specific_ip_download',
        target=f'{USER_PC_IP}/32',  # f-string for IP address formatting
        parent='download_limit_total',
        max_limit='10M/10M',
        comment='Limit download/upload for specific PC IP'
    )
    print("Queue 'limit_specific_ip_download' created.")

    # -----------------------------------------------------------------------
    # 3. Create a queue to prioritize VoIP traffic (using DSCP marking)
    # -----------------------------------------------------------------------
    queue_simple.add(
        name='prioritize_voip',
        target=LAN_NETWORK,
        dst_port='5060,5061,10000-20000',
        protocol='udp',
        priority=1,
        packet_marks='voip_packets',
        comment='Prioritize VoIP traffic - Marking packets'
    )
    print("Queue 'prioritize_voip' created.")

    # -----------------------------------------------------------------------
    # 4. Retrieve and print all simple queues
    # -----------------------------------------------------------------------
    queues = queue_simple.get()
    print("\nList of Simple Queues:")
    for queue in queues:
        print(queue)

except routeros_api.exceptions.RouterOsApiError as e:
    print(f"Error configuring queues via API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'api' in locals():
        api.disconnect()
```

**Explanation of API Script:**

*   **Import Libraries:** Imports `routeros_api` and `routeros_api.exceptions`.
*   **Connection Details:**  Defines variables for router connection parameters and network details. **Replace placeholders with your actual values.**
*   **API Connection:** Establishes a connection to the MikroTik router using `RouterOsApiPool` and `get_connection()`. `plaintext_login=True` is used for simplicity.
*   **`queue_simple = connection.get_resource('/queue/simple')`**: Gets the resource object for `/queue/simple`.
*   **`queue_simple.add(...)`**:  Uses the `add()` method to create new simple queues.  Parameters in `add()` directly correspond to Simple Queue properties in RouterOS.
*   **Error Handling (`try...except...finally`)**: Includes `try...except` blocks to catch `RouterOsApiError` (for API-specific errors) and general `Exception` for other potential issues. The `finally` block ensures the API connection is closed.
*   **`queue_simple.get()`**: Retrieves a list of all simple queues and prints them to the console for verification.

**To run the API script:**

1.  Save the Python code as a `.py` file (e.g., `mikrotik_queues.py`).
2.  Replace the placeholder values with your actual router and network information.
3.  Install the `routeros_api` library: `pip install routeros_api`
4.  Run the script from your terminal: `python mikrotik_queues.py`

### 4. Common Debugging Scenarios

**Scenario 1: Slow Internet Speed for All Devices**

*   **Possible Cause:**  Total bandwidth limit (`download_limit_total` queue) set too low or incorrectly.
*   **Debugging Steps:**
    1.  **Check `download_limit_total` queue:** Verify the `max-limit` is set to the correct value, matching your internet plan's bandwidth.
    2.  **Monitor Queue Statistics:** Use `/queue simple monitor numbers=<queue_number>` (or use WinBox/WebFig Queue Simple monitoring tab) to check the `rate` and `max-limit` values.  Ensure the `rate` is not consistently hitting the `max-limit` if you expect more bandwidth to be available.
    3.  **Bypass Queues (Temporarily):** Disable the `download_limit_total` queue (`/queue simple disable numbers=<queue_number>`) to see if the internet speed improves. If it does, the queue is likely the bottleneck.

**Scenario 2: Specific User Still Experiences Slow Speed Despite Queue Limits**

*   **Possible Cause:**  Incorrect `target` IP address in the user-specific queue (`limit_specific_ip_download`), or the parent queue (`download_limit_total`) is already saturated.
*   **Debugging Steps:**
    1.  **Verify `target` IP:** Double-check that the IP address in `limit_specific_ip_download` is correct for the intended user's device.
    2.  **Check Parent Queue Load:** Monitor the `download_limit_total` queue. If it's consistently at its `max-limit`, even user-specific queues within it will be limited. You might need to increase the total bandwidth limit or adjust other queues contributing to the total usage.
    3.  **Queue Order:** Ensure the `limit_specific_ip_download` queue is placed *after* the `download_limit_total` queue (if it's intended to be a child queue).

**Scenario 3: VoIP Quality Issues (Despite Prioritization Queue)**

*   **Possible Cause:**  Incorrect port ranges or protocol in the `prioritize_voip` queue, or VoIP packets are not being correctly marked (if using packet marks).
*   **Debugging Steps:**
    1.  **Verify VoIP Ports:** Confirm the `dst-port` range in `prioritize_voip` queue matches the ports used by your VoIP service. Check VoIP device documentation.
    2.  **Protocol Check:** Ensure `protocol=udp` is correct if your VoIP uses UDP.
    3.  **Packet Marking (if used):** If using packet marks, verify the Mangle rule (if any) is correctly marking VoIP packets. Use `/ip firewall mangle print` and `/ip firewall mangle monitor numbers=<rule_number>` to check rule effectiveness.
    4.  **Queue Priority:** Confirm `priority=1` is set in the `prioritize_voip` queue to give it the highest priority.
    5.  **Monitor Queue Statistics:** Check the `rate` of the `prioritize_voip` queue to see if it's actually processing VoIP traffic. If the rate is zero, the rule might not be matching any traffic.

**General Debugging Tips:**

*   **Use `/queue simple print` and `/queue simple monitor` commands frequently** to inspect queue configurations and real-time statistics.
*   **Test incrementally:**  Configure queues one by one and test connectivity and bandwidth after each configuration change.
*   **Simplify configuration:** Start with basic queues and add complexity gradually as needed.
*   **Check Router CPU Usage:** Overly complex queues can increase CPU load. Monitor CPU usage (`/system resource print`) to ensure it's not becoming a bottleneck.

### 5. Version-Specific Considerations (RouterOS 6.x)

*   **Simple Queues Limitations:** In RouterOS 6.x, Simple Queues are less flexible than Queue Trees for very complex scenarios. For basic SOHO needs, they are generally sufficient. For more granular control and complex QoS, consider Queue Trees (beyond the scope of "basic" complexity).
*   **HTB (Hierarchical Token Bucket):** Simple Queues in RouterOS 6.x are based on HTB. Understanding HTB concepts can be helpful for advanced queue tuning, but for basic setup, the default HTB behavior is usually adequate.
*   **No REST API Queue Configuration in v6.x WebFig:** In RouterOS 6.x, the WebFig interface may not fully support REST API queue configuration directly. CLI or dedicated API tools (like the Python example) are the primary methods for API-based queue management.
*   **Resource Limits:** Be mindful of the router's hardware resources (CPU, RAM), especially in low-end SOHO routers. Excessive queue complexity can impact performance.

### 6. Security Hardening Measures

While queues themselves are not direct security features, they can contribute to network security in SOHO environments indirectly:

*   **Prevent Bandwidth Hogging:** Queues can prevent a single device or application from monopolizing all the internet bandwidth, ensuring fair access for all users and preventing Denial of Service (DoS) scenarios within the SOHO network (e.g., one PC saturating the internet link and impacting others).
*   **Prioritize Critical Traffic:** By prioritizing essential services like VoIP, queues ensure that these services remain functional even during periods of high network load, which is important for reliable communication.
*   **Limit Guest Network Bandwidth:** If you have a guest Wi-Fi network, queues can be used to limit bandwidth available to guest users, preventing them from impacting the performance of your primary network.
*   **Monitor Queue Usage:** Regularly monitor queue statistics to detect unusual traffic patterns or bandwidth consumption that might indicate security issues or compromised devices.

**Security Best Practices related to Queues:**

*   **Secure Router Access:** Protect your MikroTik router itself with strong passwords and restrict access to management interfaces (WinBox, WebFig, SSH, API). Unsecured router access can lead to queue misconfigurations or other security vulnerabilities.
*   **Regularly Review Queue Rules:** Periodically review your queue configurations to ensure they are still appropriate for your needs and haven't been inadvertently misconfigured or exploited.
*   **Combine with Firewall Rules:** Queues work best in conjunction with firewall rules. Use firewall rules to control *what* traffic is allowed and queues to manage *how much* bandwidth is allocated to that traffic.

### 7. Performance Optimization Tips

*   **Use Simple Queues for Basic Needs:** For most SOHO scenarios, Simple Queues are efficient and sufficient. Avoid overcomplicating with Queue Trees unless absolutely necessary.
*   **Optimize `max-limit` Values:** Set `max-limit` values appropriately based on your internet bandwidth and desired bandwidth allocation. Avoid setting excessively low limits that unnecessarily restrict performance.
*   **Use `priority` Judiciously:** Use `priority` only for truly critical traffic like VoIP. Overuse of high priority can starve lower priority traffic.
*   **Minimize Number of Queues:** While MikroTik routers can handle a reasonable number of queues, excessive numbers can increase processing overhead. Try to consolidate queues where possible.
*   **Monitor CPU Usage:** Regularly check the router's CPU usage, especially after making changes to queue configurations. High CPU usage might indicate that the router is struggling to process the queues efficiently.
*   **Hardware Considerations:** If you experience performance issues with queues, consider upgrading to a more powerful MikroTik router with a faster CPU and more RAM.

### SOHO Specific Requirements

#### Real-world Deployment Examples

1.  **Fair Bandwidth Distribution in a Family Home:**
    *   **Scenario:** Multiple family members using the internet for streaming, gaming, and general browsing. Want to ensure fair bandwidth distribution so that one person's heavy usage doesn't degrade everyone else's experience.
    *   **Queue Configuration:**
        *   Create a `download_limit_total` queue for the WAN interface, setting `max-limit` to the internet plan's bandwidth.
        *   Optionally, create queues for specific devices (e.g., each family member's PC) as child queues of `download_limit_total`, each with a reasonable `max-limit` to prevent any single device from dominating bandwidth.

2.  **Prioritizing Work-from-Home Video Conferencing:**
    *   **Scenario:**  Working from home and relying on video conferencing (e.g., Zoom, Teams). Need to ensure video calls have priority over other traffic to avoid lag and dropped calls.
    *   **Queue Configuration:**
        *   Create a `prioritize_video_conf` queue targeting the LAN network, filtering for common video conferencing ports (e.g., UDP ports used by Zoom, Teams - check application documentation).
        *   Set `priority=1` for this queue.
        *   Optionally, use packet marking (with Mangle rules) based on DSCP or other criteria if your video conferencing application supports it for more accurate prioritization.

3.  **Guest Wi-Fi Bandwidth Limitation:**
    *   **Scenario:** Offering guest Wi-Fi access but want to limit their bandwidth usage to prevent impact on the primary network.
    *   **Queue Configuration:**
        *   Create a separate IP address range and VLAN for the guest Wi-Fi network.
        *   Create a `guest_wifi_limit` queue targeting the guest Wi-Fi network range.
        *   Set a lower `max-limit` for the `guest_wifi_limit` queue compared to the total internet bandwidth.

#### Scalability Considerations

*   **Simple Queues for Small SOHO:** For very small SOHO networks with a few devices and basic bandwidth control needs, Simple Queues are generally scalable enough.
*   **Queue Trees for Growth:** As the SOHO network grows in size and complexity (more devices, more diverse traffic types, more granular control required), Simple Queues might become less manageable. Consider transitioning to **Queue Trees** for more advanced QoS capabilities. Queue Trees offer more hierarchical and flexible bandwidth management and are better suited for larger or more demanding networks. However, Queue Trees are more complex to configure and are beyond the "basic" complexity level of this document.
*   **Router Hardware:**  Scalability is also limited by the router's hardware. For larger SOHO networks or more complex queue configurations, a more powerful MikroTik router model will be necessary to handle the processing load.

#### Monitoring Configurations

**CLI Monitoring:**

*   **Real-time Queue Monitoring:**
    ```routeros
    /queue simple monitor numbers=<queue_number> once
    ```
    Replace `<queue_number>` with the number of the queue you want to monitor. Use `print` command to find queue numbers. This command shows real-time statistics like `rate`, `packet-rate`, `bytes`, `packets`, and `drops`.

*   **Continuous Monitoring (Scripting):**  You can create a RouterOS script to periodically monitor queue statistics and log them or send alerts if certain thresholds are exceeded. (Example Script - Basic Logging):

    ```routeros
    :local queue_number "0" # Replace with your queue number
    :local log_interval 60s  # Logging interval (e.g., every 60 seconds)

    :while (true) do={
        :local queue_stats [/queue simple monitor numbers=$queue_number once]
        :log info ("Queue stats for queue #" . $queue_number . ": " . $queue_stats)
        :delay $log_interval
    }
    ```
    This script continuously monitors a queue and logs its statistics to the RouterOS log every 60 seconds. You can view the log using `/log print`.

**Graphical Monitoring (External Tools - Beyond basic SOHO scope, but mentioned for awareness):**

*   **The Dude:** MikroTik's free network monitoring application can monitor RouterOS devices and provide graphical views of queue statistics and network performance.
*   **SNMP Monitoring:** MikroTik routers support SNMP. You can use SNMP monitoring tools (e.g., Zabbix, PRTG) to collect queue statistics and create dashboards for visualization and alerting.

#### Disaster Recovery Steps

*   **Regular Configuration Backups:** The most crucial step is to perform regular backups of your MikroTik RouterOS configuration. This includes your queue configurations.
    *   **Manual Backup (WinBox/WebFig):** `Files` -> `Backup`. Download the backup file to a safe location.
    *   **CLI Backup:** `/export file=backup_queues_config` (exports configuration to a file named `backup_queues_config.rsc` in the router's files). Download this file using WinBox/WebFig or SCP/FTP.

*   **Automated Backup Script (Example):**

    ```routeros
    /system script
    add name="backup_queues_config_daily" owner=admin policy=write \
        source="/system backup save name=daily_config\r\
        /log info message=\"Daily RouterOS configuration backup completed.\""

    /system scheduler
    add name="daily_config_backup" on-event=backup_queues_config_daily \
        policy=write start-date=jan/01/1970 start-time=03:00:00 interval=1d
    ```
    This script creates a scheduled task that runs daily at 3:00 AM to create a backup of the RouterOS configuration. **Important:** This example saves the backup *on the router itself*. For better disaster recovery, you should download these backup files automatically to an external location (e.g., using SCP/FTP in a script or using the `/export` command with scripting to generate a configuration script file that you can then download).

*   **Restoring Configuration:**
    *   **WinBox/WebFig:** `Files` -> `Restore`. Upload the backup file and restore.
    *   **CLI:** `/import file-name=backup_queues_config.rsc` (for `.rsc` configuration script files) or `/system backup load name=daily_config` (for `.backup` files).

*   **Testing Backups:**  Periodically test your backup and restore process on a test MikroTik router (if possible) or by carefully restoring on your production router during a maintenance window to ensure the process works correctly.

#### Automated Backup Scripts (CLI Example - Export Queues Only)

If you want to backup *only* the queue configuration (instead of the entire router config), you can export the queue configuration to a script file:

```routeros
/system script
add name="export_queues_config_daily" owner=admin policy=write \
    source="/queue simple export file=queues_config_daily.rsc\r\
    /log info message=\"Daily Simple Queue configuration exported to queues_config_daily.rsc\""

/system scheduler
add name="daily_queues_export" on-event=export_queues_config_daily \
    policy=write start-date=jan/01/1970 start-time=03:15:00 interval=1d
```

This script exports only the Simple Queue configuration to a file named `queues_config_daily.rsc` and schedules it to run daily at 3:15 AM. You would then need to download this `.rsc` file to an external location for safekeeping. To restore, you would use `/import file-name=queues_config_daily.rsc`.

---

This documentation provides a basic understanding and practical examples of implementing Simple Queues in a SOHO MikroTik RouterOS environment. For more advanced QoS requirements or larger networks, further exploration of Queue Trees and more sophisticated traffic management techniques will be necessary. Remember to always test your configurations thoroughly and monitor your network performance after implementing queue changes.

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