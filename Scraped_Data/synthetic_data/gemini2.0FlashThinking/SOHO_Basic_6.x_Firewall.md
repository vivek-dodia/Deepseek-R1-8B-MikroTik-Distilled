---
generated_at: 2025-02-03T21:28:27.068204
topic: Firewall
category: Firewall & QoS
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS Firewall Documentation (Basic - SOHO)

**Document Version:** 1.0
**Date:** October 26, 2023
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic

**1. Introduction**

This document provides a comprehensive guide to configuring a basic firewall on a MikroTik RouterOS device, specifically tailored for SOHO environments running RouterOS version 6.x. We will cover fundamental firewall concepts, practical CLI and API configurations, debugging techniques, security hardening, and performance optimization, along with considerations for SOHO deployments including scalability, monitoring, disaster recovery, and automated backups.

**Target Audience:** SOHO network administrators, home users, and IT professionals managing small networks using MikroTik RouterOS.

**Prerequisites:**

*   Access to a MikroTik RouterOS device (physical or virtual) running version 6.x.
*   Basic understanding of networking concepts (IP addressing, TCP/IP, firewall principles).
*   Access to the RouterOS interface (WinBox, WebFig, or SSH).
*   Python 3.x installed for API examples.

**2. Firewall Architecture Diagram Requirements**

For a SOHO environment, the firewall typically sits at the edge of the network, protecting the internal LAN from the external WAN (Internet). The diagram below illustrates this basic architecture:

```mermaid
graph LR
    A[Internet] --> B(MikroTik Router <br/> Firewall);
    B --> C[LAN Network <br/> (PCs, Printers, etc.)];
    style B fill:#f9f,stroke:#333,stroke-width:2px
```

**Diagram Explanation:**

*   **Internet:** Represents the external network, the source of potential threats.
*   **MikroTik Router (Firewall):**  The central point of security, inspecting and controlling traffic flow between the LAN and WAN.
*   **LAN Network:** Represents the internal trusted network containing devices needing protection.

**Firewall Zones (Implicit):**

In this basic SOHO setup, we implicitly define two zones:

*   **WAN Zone (Untrusted):**  Interface connected to the Internet (e.g., `ether1`, often renamed to `WAN`).
*   **LAN Zone (Trusted):** Interface connected to the internal network (e.g., `ether2`, often renamed to `LAN`).

**3. CLI Configuration with Inline Comments**

The following CLI configuration sets up a basic, yet effective, firewall for a SOHO network.

```routeros
# --- Firewall Basic Configuration for SOHO ---

# 1. Default Deny Policy: Drop all new incoming and forwarded connections by default.
/ip firewall filter
add chain=input action=drop connection-state=new comment="Default deny input - new connections"
add chain=forward action=drop connection-state=new comment="Default deny forward - new connections"

# 2. Allow Established and Related Connections: Essential for allowing responses to initiated connections.
add chain=input action=accept connection-state=established,related comment="Allow established/related input"
add chain=forward action=accept connection-state=established,related comment="Allow established/related forward"

# 3. Allow Input from LAN to Router (Essential services like Winbox, SSH - consider disabling in production if not needed externally)
add chain=input action=accept src-address-list=LAN_NET comment="Allow LAN input to router for management"

# 4. Allow Outbound Traffic from LAN to WAN (Internet Access)
add chain=forward action=accept in-interface=LAN out-interface=WAN comment="Allow LAN to WAN forward"

# 5. Allow DNS Resolution from LAN to WAN (UDP port 53)
add chain=forward action=accept protocol=udp dst-port=53 in-interface=LAN out-interface=WAN comment="Allow DNS (UDP) from LAN to WAN"

# 6. Allow DNS Resolution from LAN to WAN (TCP port 53 - less common but sometimes used)
add chain=forward action=accept protocol=tcp dst-port=53 in-interface=LAN out-interface=WAN comment="Allow DNS (TCP) from LAN to WAN"

# 7. Allow DHCP Client to WAN (UDP ports 67 & 68 for DHCP client on WAN interface)
add chain=input action=accept protocol=udp dst-port=67,68 in-interface=WAN src-port=68 comment="Allow DHCP client input on WAN"
add chain=output action=accept protocol=udp src-port=67,68 out-interface=WAN dst-port=67 comment="Allow DHCP client output on WAN"

# 8. Drop Invalid Connections: Important for security.
add chain=input action=drop connection-state=invalid comment="Drop invalid input connections"
add chain=forward action=drop connection-state=invalid comment="Drop invalid forward connections"

# 9. Define Address List for LAN Network (Replace with your actual LAN network)
/ip firewall address-list
add list=LAN_NET address=192.168.88.0/24 comment="SOHO LAN Network"

# 10. Logging (Optional - Enable for debugging and monitoring - can be resource intensive if overused)
# Example: Log dropped input packets - consider logging only specific types of traffic for performance in production
# /ip firewall filter
# add chain=input action=log log-prefix="FW-DROP-INPUT" comment="Log dropped input" log=yes
# add chain=forward action=log log-prefix="FW-DROP-FORWARD" comment="Log dropped forward" log=yes
# add chain=input action=drop connection-state=new log=no comment="Default deny input - new connections" # Move drop after log if logging is enabled for default drop

# --- End of Firewall Configuration ---
```

**Explanation of Rules:**

*   **Default Deny:**  The first two rules establish a "default deny" policy. Any new connection that doesn't explicitly match an "accept" rule will be dropped. This is a fundamental security principle.
*   **Established/Related:**  These rules are crucial. They allow return traffic for connections initiated from inside the LAN or the router itself. Without these, internet browsing and many other functions would break.
*   **LAN Input to Router:** Allows management access (Winbox, SSH, etc.) from the LAN network to the router itself. **Caution:** In a more secure environment, restrict this further or disable it if not needed.
*   **LAN to WAN Forward:**  Enables devices on the LAN to access the internet.
*   **DNS and DHCP:** Explicitly allows DNS and DHCP traffic to ensure name resolution and automatic IP address assignment work correctly for LAN clients.
*   **Invalid Connections:** Drops packets that are malformed or don't fit within valid TCP/IP connection states.
*   **Address List:**  `LAN_NET` address list simplifies rule management by grouping your LAN network range. Replace `192.168.88.0/24` with your actual LAN network.
*   **Logging (Optional):**  Logging dropped packets can be helpful for debugging and security monitoring, but can consume resources if overused.  Enable selectively for specific rules or debugging phases.

**4. REST API Implementation (Python Code)**

This Python script uses the `routeros_api` library to configure the same firewall rules as the CLI example.

```python
from routeros_api import RouterOsApiPool
from routeros_api.exceptions import RouterOsApiError

ROUTER_HOST = '192.168.88.1'  # Replace with your RouterOS IP
ROUTER_USER = 'admin'         # Replace with your RouterOS username
ROUTER_PASSWORD = ''          # Replace with your RouterOS password (or use token-based auth in production)
LAN_NETWORK = '192.168.88.0/24' # Replace with your LAN network

try:
    api_pool = RouterOsApiPool(ROUTER_HOST, username=ROUTER_USER, password=ROUTER_PASSWORD, plaintext_login=True)
    api = api_pool.get_api()

    # --- Firewall Configuration using API ---

    # 1. Default Deny Input & Forward
    api.path('/ip/firewall/filter').add(chain='input', action='drop', connection_state='new', comment='Default deny input - new connections')
    api.path('/ip/firewall/filter').add(chain='forward', action='drop', connection_state='new', comment='Default deny forward - new connections')

    # 2. Allow Established/Related
    api.path('/ip/firewall/filter').add(chain='input', action='accept', connection_state='established,related', comment='Allow established/related input')
    api.path('/ip/firewall/filter').add(chain='forward', action='accept', connection_state='established,related', comment='Allow established/related forward')

    # 3. Allow LAN Input to Router (Management)
    api.path('/ip/firewall/filter').add(chain='input', action='accept', src_address_list='LAN_NET', comment='Allow LAN input to router for management')

    # 4. Allow LAN to WAN Forward
    api.path('/ip/firewall/filter').add(chain='forward', action='accept', in_interface='LAN', out_interface='WAN', comment='Allow LAN to WAN forward')

    # 5. Allow DNS (UDP) from LAN to WAN
    api.path('/ip/firewall/filter').add(chain='forward', action='accept', protocol='udp', dst_port=53, in_interface='LAN', out_interface='WAN', comment='Allow DNS (UDP) from LAN to WAN')

    # 6. Allow DNS (TCP) from LAN to WAN
    api.path('/ip/firewall/filter').add(chain='forward', action='accept', protocol='tcp', dst_port=53, in_interface='LAN', out_interface='WAN', comment='Allow DNS (TCP) from LAN to WAN')

    # 7. Allow DHCP Client on WAN
    api.path('/ip/firewall/filter').add(chain='input', action='accept', protocol='udp', dst_port='67,68', in_interface='WAN', src_port=68, comment='Allow DHCP client input on WAN')
    api.path('/ip/firewall/filter').add(chain='output', action='accept', protocol='udp', src_port='67,68', out_interface='WAN', dst_port=67, comment='Allow DHCP client output on WAN')

    # 8. Drop Invalid Connections
    api.path('/ip/firewall/filter').add(chain='input', action='drop', connection_state='invalid', comment='Drop invalid input connections')
    api.path('/ip/firewall/filter').add(chain='forward', action='drop', connection_state='invalid', comment='Drop invalid forward connections')

    # 9. Define Address List for LAN Network
    try:
        api.path('/ip/firewall/address-list').add(list='LAN_NET', address=LAN_NETWORK, comment='SOHO LAN Network')
    except RouterOsApiError as e:
        if 'already exists' in str(e):
            print(f"Address list 'LAN_NET' already exists, skipping creation.")
        else:
            raise e # Re-raise other errors


    print("Basic Firewall configuration applied successfully via API.")

except RouterOsApiError as e:
    print(f"Error configuring firewall via API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'api_pool' in locals() and api_pool:
        api_pool.disconnect()
```

**Explanation of API Script:**

*   **Import Libraries:** Imports `RouterOsApiPool` and `RouterOsApiError` from the `routeros_api` library.
*   **Configuration Variables:** Defines variables for RouterOS IP, username, password, and LAN network. **Replace placeholders with your actual values.**
*   **API Connection:** Establishes a connection to the RouterOS device using `RouterOsApiPool`. `plaintext_login=True` is used for simplicity in this example, but consider more secure methods like token-based authentication in production.
*   **Firewall Rule Creation:** Uses `api.path('/ip/firewall/filter').add(...)` to add each firewall rule, mirroring the CLI configuration.
*   **Address List Creation:**  Creates the `LAN_NET` address list. Includes error handling to avoid issues if the address list already exists.
*   **Error Handling:** Includes `try...except` blocks to catch `RouterOsApiError` (for API-specific errors) and general exceptions, printing informative error messages.
*   **API Disconnection:**  Ensures the API connection is closed in the `finally` block.

**5. Common Debugging Scenarios**

When troubleshooting firewall issues, consider these common scenarios:

| Scenario                               | Possible Cause(s)                                                                | Debugging Steps                                                                                                |
| :------------------------------------- | :--------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **No internet access from LAN devices** | - Incorrect LAN to WAN forward rule. <br/> - DNS resolution blocked.              | - Verify the "Allow LAN to WAN forward" rule is enabled and correctly configured. <br/> - Check DNS settings on LAN devices and RouterOS. <br/> - Ping a public IP (e.g., 8.8.8.8) from a LAN device to check basic connectivity. |
| **Cannot access services on LAN from WAN** | - Default deny input/forward rules blocking incoming connections. <br/> - Missing port forwarding rules (if intentional access is needed). | - Review default deny rules. <br/> - Ensure no rules are accidentally blocking established/related connections. <br/> - For intentional WAN access to LAN services, configure Destination NAT (Port Forwarding). |
| **Specific applications/ports blocked** | - Overly restrictive firewall rules. <br/> - Incorrect port or protocol specified in rules. | - Examine firewall rules, especially those related to `forward` chain. <br/> - Use `/tool torch` or `/tool packet-sniffer` to analyze traffic and identify blocked ports/protocols. <br/> - Check firewall logs (if logging is enabled). |
| **Slow internet performance**           | - Complex firewall rules causing CPU overhead. <br/> - Excessive logging.        | - Review firewall rule complexity. Try to simplify rules. <br/> - Check CPU usage of the router during high load. <br/> - Reduce or disable logging if it's causing performance issues. <br/> - Consider using FastTrack for established connections (RouterOS 6.x and later). |

**Debugging Tools in RouterOS:**

*   **`/ip firewall filter print`:** Displays the current firewall filter rules.
*   **`/log print`:** Shows system logs, including firewall logs if enabled.
*   **`/tool torch`:** Real-time traffic analyzer to inspect packets flowing through the router.
*   **`/tool packet-sniffer`:** Packet capture tool for detailed packet analysis (save to file and analyze with Wireshark for best results).
*   **`/ip firewall connection tracking print`:**  Shows active connections being tracked by the firewall, useful for understanding connection states.

**6. Version-Specific Considerations (RouterOS 6.x)**

*   **FastTrack:** RouterOS 6.x introduced FastTrack, a connection tracking optimization that significantly improves performance for established connections. While not explicitly used in the basic configuration above, it's enabled by default and benefits this setup implicitly by speeding up established LAN to WAN traffic.
*   **Limitations:**  In basic SOHO scenarios, RouterOS 6.x firewall capabilities are generally sufficient. For very high throughput or extremely complex rule sets, more advanced hardware or RouterOS versions might be needed (though unlikely in basic SOHO).
*   **Syntax Compatibility:** The CLI and API commands presented in this document are compatible with RouterOS 6.x.

**7. Security Hardening Measures**

Beyond the basic firewall rules, consider these security hardening measures for a SOHO MikroTik router:

*   **Strong Passwords:** Use strong, unique passwords for the `admin` user and any other user accounts.
*   **Disable Default `admin` User:** Create a new administrator user and disable the default `admin` account for enhanced security.
*   **Limit Access to Management Interfaces:** Restrict access to Winbox, WebFig, and SSH to trusted IP addresses or networks (e.g., only from the LAN).
*   **Disable Unnecessary Services:** Disable any RouterOS services you are not actively using (e.g., unused protocols, services like MAC-Telnet if not needed).
*   **Keep RouterOS Updated:** Regularly update RouterOS to the latest stable version to patch security vulnerabilities. Check the MikroTik website for security advisories.
*   **Consider Address Lists and Groups:**  Utilize address lists (like `LAN_NET` in the example) and potentially address groups for more organized and manageable firewall rules, especially if you have more complex network segments.
*   **Regularly Review Firewall Rules:** Periodically review your firewall rules to ensure they are still necessary and effective. Remove any outdated or redundant rules.

**8. Performance Optimization Tips**

For optimal firewall performance in a SOHO environment:

*   **Keep Rules Simple and Efficient:** Avoid overly complex rules.  Prioritize clear and concise rules that achieve the desired security level.
*   **Leverage Connection Tracking:** RouterOS firewall is connection-stateful. Utilize `connection-state` effectively (like `established,related`) to minimize rule processing for established traffic.
*   **FastTrack (Implicit Benefit in 6.x):** FastTrack automatically accelerates established connections, reducing CPU load. Ensure it's enabled (default setting).
*   **Minimize Logging:** Logging can be resource-intensive. Only log essential traffic for debugging or security monitoring. Avoid logging every dropped packet in high-traffic scenarios unless strictly necessary.
*   **Hardware Considerations:** For very high bandwidth SOHO connections (e.g., Gigabit internet), ensure your MikroTik router hardware has sufficient CPU power to handle the firewall processing load. Entry-level MikroTik routers are often adequate for typical SOHO speeds, but for extreme cases, consider more powerful models.

**9. SOHO Specific Requirements**

**9.1 Real-World Deployment Examples:**

*   **Home Office:** A home user connecting multiple devices (PCs, laptops, smartphones, smart home devices) to the internet. The firewall protects personal devices and data from internet threats.
*   **Small Shop/Cafe:** A small business providing Wi-Fi for customers and managing point-of-sale systems, printers, and staff computers. The firewall separates guest Wi-Fi from the internal business network and protects sensitive business data.

**9.2 Scalability Considerations:**

For basic SOHO needs, the firewall configuration provided is generally scalable within the typical range of SOHO devices (a few to tens of devices).  Scalability in this context means:

*   **Rule Set Growth:** As SOHO needs evolve, you might add more specific firewall rules (e.g., for specific applications, port forwarding). The basic configuration provides a solid foundation for adding more rules.
*   **Device Count:** The router's CPU and RAM should be sufficient for handling traffic from a typical SOHO device count. For significantly larger SOHO deployments or higher bandwidth requirements, consider upgrading to a more powerful MikroTik router.
*   **Network Segmentation (Beyond Basic):** For larger SOHOs with more complex needs, consider VLANs and more advanced firewall zoning, which are beyond the scope of this *basic* document but possible with MikroTik RouterOS.

**9.3 Monitoring Configurations:**

*   **System Logs:** RouterOS system logs (`/log print`) are the primary monitoring tool. Configure logging actions in firewall rules (e.g., `action=log log=yes log-prefix="FW-DROP-INPUT"`) to track specific events (e.g., dropped packets).
*   **Simple Queues (for Bandwidth Monitoring):** While not directly firewall-related, simple queues (`/queue simple`) can be used to monitor bandwidth usage per IP address or network, which can indirectly help identify unusual traffic patterns that might be security-related.
*   **Resource Monitoring:** Monitor the router's CPU, RAM, and interface traffic using `/system resource print` and `/interface ethernet monitor ether1 once`. High CPU usage during periods of low network activity might indicate a security issue or misconfiguration.
*   **Basic Graphs (WebFig/Winbox):** RouterOS WebFig and Winbox offer basic real-time graphs for interface traffic, which can be visually monitored for anomalies.

**9.4 Disaster Recovery Steps:**

*   **Regular Backups:**  The most crucial step is to perform regular backups of your RouterOS configuration.
    *   **Manual Backup (CLI/Winbox):** Use `/export file=firewall_backup` in CLI or "Backup" function in Winbox to create a backup file.
    *   **Automated Backup (Script - see below):** Automate backups using a scheduled script.
*   **Secure Backup Storage:** Store backup files in a safe location, separate from the router itself (e.g., on a local computer, network storage, or cloud storage).
*   **Restoration Procedure:** In case of router failure or configuration corruption:
    1.  Factory reset the MikroTik router (if necessary).
    2.  Use `/import file=firewall_backup.rsc` in CLI or "Restore" function in Winbox to restore the configuration from the backup file.
    3.  Verify the restored configuration and test network connectivity.

**9.5 Automated Backup Scripts**

Here's a simple RouterOS script to automate daily firewall configuration backups:

```routeros
# --- Automated Firewall Backup Script ---
:local backup_file_name ("firewall_backup_" . [:system date format="%Y-%m-%d_%H-%M"]);
/export file=$backup_file_name
:log info "Firewall configuration backed up to file: $backup_file_name.rsc"
# --- End of Backup Script ---
```

**Scheduling the Script:**

1.  Go to `/system scheduler`.
2.  Add a new scheduler entry.
    *   **Name:** `Daily Firewall Backup` (or similar)
    *   **Start Time:** `00:00:00` (or desired backup time)
    *   **Interval:** `1d` (daily)
    *   **On Event:** Paste the script code above into the "On Event" field.
    *   **Start Date:** Set to today's date.
    *   **Enabled:** Yes

This script will run daily at the specified time, creating a backup file in the router's files directory with a filename like `firewall_backup_2023-10-26_00-00.rsc`. You can then download these backup files regularly for off-router storage.

**10. Comparative Table: CLI vs. API Configuration**

| Feature                  | CLI (Command Line Interface)                                   | API (Application Programming Interface)                                  |
| :----------------------- | :------------------------------------------------------------- | :----------------------------------------------------------------------- |
| **Interface**            | Text-based commands, directly typed or pasted into terminal.    | Programmable interface, typically accessed via scripting languages (e.g., Python). |
| **Automation**           | Scripting possible (RouterOS scripting language), but can be less flexible for complex logic. | Highly suitable for automation, integration with other systems, and complex workflows. |
| **Learning Curve**       | Steeper initial learning curve for command syntax.              | Requires understanding of programming concepts and API structure.       |
| **Real-time Interaction** | Excellent for immediate configuration and troubleshooting.      | Can be used for real-time monitoring and control, but typically used for automated configuration and management. |
| **Readability/Maintainability (for complex configs)** | Can become less readable and harder to manage for large configurations. | Well-structured code can be more maintainable for complex setups, especially with comments and modular design. |
| **Error Handling**       | Basic error messages in CLI.                                  | Robust error handling capabilities in programming languages, allowing for better error management and logging. |
| **Example Use Cases**    | Quick configuration changes, basic scripting, troubleshooting.    | Infrastructure as Code (IaC), automated deployments, integration with monitoring systems, bulk configuration changes. |

**11. Conclusion**

This document has outlined the basic firewall configuration for a MikroTik RouterOS device in a SOHO environment. By implementing these rules and security best practices, you can significantly enhance the security of your SOHO network. Remember to regularly review and adapt your firewall configuration as your network needs and security landscape evolve. This basic setup provides a strong foundation upon which you can build more advanced firewall configurations as your expertise and network complexity grow.

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