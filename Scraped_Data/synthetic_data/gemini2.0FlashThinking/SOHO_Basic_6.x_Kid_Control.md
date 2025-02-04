---
generated_at: 2025-02-03T21:33:31.942799
topic: Kid Control
category: Firewall & QoS
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS: Kid Control in SOHO Environments (Version 6.x)

**Document Version:** 1.0
**Date:** October 26, 2023
**Author:** [Your Name/Company Name] - MikroTik Certified Engineer

**1. Introduction**

This document provides a comprehensive guide to implementing "Kid Control" on a MikroTik RouterOS (version 6.x) in a Small Office/Home Office (SOHO) environment. "Kid Control" refers to the ability to manage and restrict internet access for children's devices, ensuring a balanced online experience and parental oversight. This guide will utilize RouterOS's powerful firewall and scheduling features to achieve this, offering both Command Line Interface (CLI) and REST API configuration examples.

**2. Architecture Diagram Requirements**

The Kid Control architecture in a SOHO environment will typically involve:

* **MikroTik Router:** Acting as the central gateway and firewall.
* **Kids' Devices:** Devices used by children (laptops, tablets, smartphones).
* **Parents' Devices:** Devices used by parents for management and unrestricted access.
* **Internet Connection:**  The broadband connection to the outside world.

We will use Firewall rules and Schedules within the MikroTik router to control internet access for devices identified as "Kids' Devices".

```mermaid
graph LR
    A[Internet] --> B(MikroTik Router)
    B --> C{Parents' Network}
    B --> D{Kids' Network}
    C --> E[Parents' Device 1]
    C --> F[Parents' Device 2]
    D --> G[Kids' Device 1]
    D --> H[Kids' Device 2]
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:1px
    linkStyle 1,2,3,4,5,6 stroke-width:2px,stroke:#333;
```

**Diagram Explanation:**

* **Internet:** Represents the external internet connection.
* **MikroTik Router:** The central point of control, implementing Kid Control.
* **Parents' Network:** Network segment for parents' devices with unrestricted access.
* **Kids' Network:** Network segment for children's devices with controlled access.
* **Parents' Device 1/2:** Examples of devices used by parents.
* **Kids' Device 1/2:** Examples of devices used by children.

**Note:**  For simplicity in a SOHO environment, we will often use a single LAN network and differentiate devices using IP addresses or MAC addresses rather than separate VLANs or physical networks.

**3. CLI Configuration with Inline Comments**

This section provides CLI commands to configure Kid Control.

```routeros
# --- Step 1: Create Address List for Kids' Devices ---
# This list will contain the IP addresses or MAC addresses of devices used by kids.
# Using IP addresses is simpler for basic SOHO setups, but consider DHCP reservations for static IPs.
/ip firewall address-list
add list=kids-devices address=192.168.88.100 comment="Kid's Laptop"  # Example IP address
add list=kids-devices address=192.168.88.101 comment="Kid's Tablet"  # Example IP address

# --- Step 2: Create Schedules for Internet Access ---
# Define time intervals when internet access should be restricted/allowed.
/system scheduler
add name=kid-control-off start-time=22:00:00 interval=1d on-event=kid-control-disable policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,romon start-date=nov/01/2023 comment="Disable Kid Control Schedule (e.g., Night)"
add name=kid-control-on start-time=07:00:00 interval=1d on-event=kid-control-enable policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,romon start-date=nov/01/2023 comment="Enable Kid Control Schedule (e.g., Morning)"

# --- Step 3: Create Scripts to Enable/Disable Kid Control Firewall Rules ---
# Scripts triggered by the scheduler to enable and disable firewall rules.
/system script
add name=kid-control-disable source="# Script to disable Kid Control firewall rules\r\
    /ip firewall filter disable numbers=[find comment=\"Kid Control - Block\"]" policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,romon
add name=kid-control-enable source="# Script to enable Kid Control firewall rules\r\
    /ip firewall filter enable numbers=[find comment=\"Kid Control - Block\"]" policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,romon

# --- Step 4: Create Firewall Filter Rules for Kid Control ---
# These rules will block internet access for devices in the 'kids-devices' list during restricted hours.
/ip firewall filter
add chain=forward src-address-list=kids-devices action=drop comment="Kid Control - Block" disabled=yes out-interface=ether1-gateway  # Replace 'ether1-gateway' with your WAN interface name.
# Note: 'disabled=yes' initially, enabled by scheduler. 'out-interface' is important to only block internet traffic.

# --- Step 5: (Optional) Whitelist Websites or Services ---
# If needed, you can create rules to allow access to specific websites or services even during restricted hours.
# Example: Allow access to educational website 'www.example-education.com'
/ip firewall filter
add chain=forward src-address-list=kids-devices dst-address=www.example-education.com action=accept comment="Kid Control - Allow Educational Website" disabled=yes out-interface=ether1-gateway
# Note: Place ALLOW rules BEFORE the BLOCK rule for precedence.

# --- Step 6: (Optional) Logging Kid Control Activity ---
# Log dropped packets to monitor Kid Control effectiveness.
/ip firewall filter
set [find comment="Kid Control - Block"] log=yes log-prefix="KID-CONTROL-BLOCKED"

# --- Verification ---
# Check address lists, schedules, scripts, and firewall rules.
/ip firewall address-list print
/system scheduler print
/system script print
/ip firewall filter print
```

**4. REST API Implementation (Python Code)**

This Python script demonstrates how to configure basic Kid Control using the MikroTik RouterOS REST API. You will need the `routeros_api` Python library (install with `pip install routeros_api`).

```python
import routeros_api
from routeros_api import exceptions as api_exceptions

ROUTER_HOST = 'your_router_ip'  # Replace with your router IP
ROUTER_USERNAME = 'api_user'      # Replace with your API username
ROUTER_PASSWORD = 'api_password'  # Replace with your API password

def configure_kid_control():
    try:
        connection = routeros_api.RouterOsClient(ROUTER_HOST, username=ROUTER_USERNAME, password=ROUTER_PASSWORD, port=8728) # Port 8728 for non-SSL API

        # --- Address List ---
        address_list_node = connection.path('/ip/firewall/address-list')
        address_list_node.add(list='kids-devices', address='192.168.88.100', comment='Kid Laptop API')
        address_list_node.add(list='kids-devices', address='192.168.88.101', comment='Kid Tablet API')
        print("Address list 'kids-devices' configured.")

        # --- Scheduler ---
        scheduler_node = connection.path('/system/scheduler')
        scheduler_node.add(name='kid-control-off-api', start_time='22:00:00', interval='1d', on_event='kid-control-disable-script-api', comment='Night Schedule API')
        scheduler_node.add(name='kid-control-on-api', start_time='07:00:00', interval='1d', on_event='kid-control-enable-script-api', comment='Morning Schedule API')
        print("Schedules 'kid-control-off-api' and 'kid-control-on-api' configured.")

        # --- Scripts ---
        script_node = connection.path('/system/script')
        script_node.add(name='kid-control-disable-script-api', source='/ip firewall filter disable numbers=[find comment="Kid Control - Block API"]')
        script_node.add(name='kid-control-enable-script-api', source='/ip firewall filter enable numbers=[find comment="Kid Control - Block API"]')
        print("Scripts 'kid-control-disable-script-script-api' and 'kid-control-enable-script-api' configured.")

        # --- Firewall Rule ---
        firewall_node = connection.path('/ip/firewall/filter')
        firewall_node.add(chain='forward', src_address_list='kids-devices', action='drop', comment='Kid Control - Block API', disabled='yes', out_interface='ether1-gateway') # Replace 'ether1-gateway'
        print("Firewall rule 'Kid Control - Block API' configured (disabled).")

        print("Kid Control configuration via API completed successfully.")

    except api_exceptions.ConnectionError:
        print("Error: Could not connect to MikroTik router. Check IP address and API service.")
    except api_exceptions.LoginError:
        print("Error: Authentication failed. Check username and password.")
    except api_exceptions.RouterOsApiError as e:
        print(f"RouterOS API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    configure_kid_control()
```

**5. Common Debugging Scenarios**

| Scenario                                      | Possible Cause                                     | Debugging Steps                                                                 |
|-----------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Kids' devices still have internet access during restricted hours.** | 1. Firewall rule not enabled by scheduler.         | 1. Check scheduler status (`/system scheduler print`).<br>2. Verify script execution logs (`/log print`).<br>3. Manually enable the firewall rule in `/ip firewall filter` and test. |
|                                               | 2. Incorrect schedule time or interval.            | 1. Double-check schedule start time and interval in `/system scheduler print`.    |
|                                               | 3. Wrong address list applied to firewall rule.      | 1. Verify `src-address-list` in firewall rule (`/ip firewall filter print`).<br>2. Check address list content (`/ip firewall address-list print`). |
| **Kids' devices blocked even during allowed hours.** | 1. Firewall rule enabled when it shouldn't be.       | 1. Check scheduler status and script execution logs.<br>2. Manually disable the rule and test. |
|                                               | 2. Conflicting firewall rules.                     | 1. Review all firewall rules in `/ip firewall filter print`.<br>2. Ensure Kid Control rules have correct order and actions. |
| **No internet access for anyone.**             | 1. Incorrect `out-interface` in firewall rule.      | 1. Verify `out-interface` is set to your WAN interface in `/ip firewall filter print`. |
|                                               | 2. Overly restrictive firewall rules.              | 1. Review all firewall rules, especially if you added whitelist rules incorrectly. |
| **API script fails to connect.**                | 1. Incorrect router IP, username, or password.     | 1. Double-check credentials in the Python script.<br>2. Test connectivity using ping or Winbox. |
|                                               | 2. API service disabled on MikroTik.               | 1. Check if API service is enabled in `/ip service print`.<br>2. Ensure firewall is not blocking API port (8728). |

**6. Version-Specific Considerations (RouterOS 6.x)**

* **Firewall Filter:** RouterOS 6.x firewall filter is robust and fully capable of implementing Kid Control.
* **Scheduler:**  The scheduler in version 6.x is reliable for time-based actions.
* **REST API:** Version 6.x supports the REST API, allowing for programmatic configuration. Ensure the `api` or `api-ssl` service is enabled in `/ip service`.
* **Resource Limitations:** For very large SOHO networks with hundreds of rules, RouterOS 6.x on older hardware might experience performance limitations. However, for typical home networks, it's generally sufficient.
* **Software Updates:** RouterOS v6 is considered legacy.  Security updates are less frequent. Consider upgrading to v7 if possible for the latest features and security patches, although v6 is still widely used and functional for this purpose.

**7. Security Hardening Measures**

* **Strong Passwords:** Use strong, unique passwords for the `admin` user and any API users. Change default passwords immediately.
* **Disable Default User:** If possible, disable the default `admin` user and create new administrative users with specific roles.
* **API Access Control:**
    * Use a dedicated API user with limited privileges only necessary for Kid Control management if possible.
    * Restrict API access to specific IP addresses or networks if applicable.
    * Consider using SSL for API communication (`api-ssl` service) for encrypted communication, although this might be more complex for basic SOHO setups.
* **Firewall Protection:** Ensure your MikroTik firewall is configured to protect itself from external threats. This is generally handled by default firewall rules, but review them to ensure they are appropriate.
* **Regular Backups:** Implement regular backups of your RouterOS configuration (see Section 10).
* **Software Updates (with caution):**  While RouterOS v6 is older, apply any critical security updates released by MikroTik for v6 if available. However, be cautious with major version upgrades in a production environment without proper testing.

**8. Performance Optimization Tips**

* **Efficient Firewall Rules:**
    * Keep your firewall rule sets as concise and specific as possible.
    * Use address lists and schedules effectively to minimize the number of rules.
    * Place more frequently matched rules higher in the rule list for faster processing.
* **Minimize Logging:**  While logging is useful for debugging, excessive logging can consume resources. Only enable logging when actively troubleshooting.
* **Hardware Considerations:** For very large SOHO networks or if you experience performance issues, consider upgrading to a more powerful MikroTik router model with more CPU and RAM. However, for typical SOHO Kid Control, performance impact is usually negligible.
* **FastTrack (Version 6.x):**  If you experience performance bottlenecks, explore using FastTrack in the firewall filter for established connections to bypass firewall processing for some traffic. However, FastTrack might bypass some firewall features, so use it cautiously and test thoroughly.  For simple Kid Control, FastTrack is usually not necessary.

**9. SOHO Environment Specifics**

**9.1. Real-World Deployment Examples**

* **Example 1: Weekday/Weekend Schedule:** Parents want to restrict internet access for kids' devices during school nights (e.g., 10 PM to 7 AM weekdays) but allow unrestricted access on weekends.
    * **Schedules:** Create two schedules: "Weekday Kid Control Off" (Mon-Fri, 10 PM - 7 AM) and "Weekend Kid Control On" (Sat-Sun, always enabled - or you can simply disable the block rule manually on weekends and re-enable on Monday).
    * **Firewall Rules:** The same firewall block rule as described in Section 3 is used, enabled/disabled by the schedules.

* **Example 2: Homework Time Exception:** Kids need internet access for homework between 4 PM and 6 PM on weekdays, even during restricted hours.
    * **Whitelist Rule:** Create an "Allow Homework" firewall rule that allows traffic to specific educational websites or services (e.g., online learning platforms) for `kids-devices` during 4 PM - 6 PM on weekdays. Place this rule *before* the main block rule.
    * **Schedules:**  Adjust the "Kid Control On" schedule to start *after* homework time (e.g., 6 PM instead of 7 AM if needed).

* **Example 3: Time Limits:**  Parents want to allow only 2 hours of internet access per day. This is more complex with basic RouterOS tools and might require external scripts or more advanced firewall configurations with connection tracking and counters, which is beyond the "Basic" complexity level of this document. For simple time limits, consider using parental control features built into operating systems or applications on the kids' devices themselves, in conjunction with RouterOS Kid Control for broader network-level restrictions.

**9.2. Scalability Considerations**

For a typical SOHO environment, this Kid Control setup is easily scalable:

* **Adding Devices:** Simply add more IP addresses or MAC addresses to the `kids-devices` address list.
* **More Schedules:** You can create more complex schedules for different days of the week or specific events.
* **More Rules:** You can add more firewall rules for whitelisting, specific application blocking, or content filtering (content filtering is more advanced and beyond "Basic" complexity).

For very large homes or small offices, consider:

* **More Powerful Router:** Upgrade to a MikroTik router with more processing power and memory if you anticipate a large number of devices and complex rules.
* **VLANs:** For larger networks, consider segmenting your network into VLANs (e.g., separate VLAN for kids' devices) for better organization and traffic control. This adds complexity but improves management.

**9.3. Monitoring Configurations**

* **Firewall Rule Counters:**  Check the counters for the "Kid Control - Block" firewall rule in `/ip firewall filter print`. This shows how many packets have been dropped by the rule, indicating Kid Control activity.
* **Logging:** Enable logging for the "Kid Control - Block" rule (as shown in Section 3). Review the logs in `/log print` or using a logging server (if configured) to see detailed records of blocked traffic, including source IPs, destination IPs, and timestamps.
* **Simple Queue Monitoring (Optional):** For bandwidth management alongside Kid Control (beyond "Basic" scope), you could use Simple Queues to monitor bandwidth usage by kids' devices.

**9.4. Disaster Recovery Steps**

* **Regular Backups:** The most crucial step is to perform regular backups of your MikroTik RouterOS configuration.
* **Backup Methods:**
    * **Manual Backup via Winbox/WebFig:**  Download the configuration file (`.backup` or `.rsc`) to your computer.
    * **Automated Backup Script (see Section 10):** Schedule a script to automatically save backups to a local drive or network share.
* **Restore Process:**
    * **Via Winbox/WebFig:** Upload the backup file and restore the configuration.
    * **CLI:** Use the `/system backup load name=backup_filename.backup` command.
* **Testing Backups:** Periodically test your backup and restore process to ensure it works correctly.
* **Documentation:** Keep a record of your Kid Control configuration and backup procedures in a safe place.

**10. Automated Backup Scripts**

This RouterOS script automates daily backups of your configuration and saves them locally on the router's disk. You can then download these backups manually or use other methods to transfer them off-router.

```routeros
# --- Automated Daily Backup Script ---
/system script
add name=daily-backup owner=admin policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,romon source="# Daily MikroTik Backup Script\r\
    :local backupName (\"backup-\" . [:system clock get date format=yyyy-MM-dd] . \"-\" . [:system clock get time format=HH-mm-ss] . \".backup\");\r\
    /system backup save name=\$backupName\r\
    :log info (\"Daily backup created: \" . \$backupName)\r\
    "

# --- Schedule the Backup Script ---
/system scheduler
add name=daily-backup-scheduler interval=1d on-event=daily-backup start-time=03:00:00 policy=ftp,reboot,read,write,policy,test,winbox,password,sensitive,romon start-date=nov/01/2023 comment="Daily Backup Scheduler"
```

**Explanation:**

* **`/system script add name=daily-backup ...`**: Creates a script named `daily-backup`.
    * `:local backupName ...`: Generates a unique backup filename using the current date and time.
    * `/system backup save name=\$backupName`: Saves the backup with the generated filename.
    * `:log info ...`: Logs a message indicating the backup was created.
* **`/system scheduler add name=daily-backup-scheduler ...`**: Schedules the `daily-backup` script to run daily at 3:00 AM.

**To improve this script further (beyond basic complexity):**

* **Backup to Network Share:** Modify the script to save backups to a network share (e.g., SMB/CIFS) using `/file print` and `/file copy`.
* **Backup Rotation:** Implement backup rotation to keep only a certain number of recent backups and delete older ones to save disk space.
* **Email Notifications:** Add email notifications to confirm successful backups or report failures.

**11. Comparative Table: CLI vs. REST API for Kid Control**

| Feature                 | CLI (Command Line Interface)                                | REST API (Application Programming Interface)                                  |
|-------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Configuration Method** | Direct command input via terminal (SSH, Telnet, Serial).    | Programmatic configuration via HTTP requests (e.g., using Python scripts).      |
| **Learning Curve**      | Steeper initially for beginners, requires RouterOS command knowledge. | Easier for programmers, especially if familiar with HTTP and JSON.             |
| **Automation**          | Limited to RouterOS scripting (powerful but RouterOS-specific). | Highly suitable for automation, integration with other systems, and scripting in various languages. |
| **Efficiency (Human)**  | Faster for quick, one-time configurations.                 | More efficient for complex, repetitive, or large-scale configurations.         |
| **Error Handling**      | Basic error messages in CLI output.                       | More robust error handling can be implemented in scripts (e.g., Python try-except). |
| **Real-time Monitoring**| Good for real-time monitoring using commands like `/log print`, `/interface monitor-traffic`. | API can be used to fetch real-time data programmatically for monitoring and dashboards. |
| **SOHO Suitability**    | Excellent for SOHO, especially for users comfortable with command lines. | Also suitable for SOHO, especially if users want to automate or integrate with other home automation systems. |

**12. Conclusion**

This document has provided a comprehensive guide to setting up Kid Control on a MikroTik RouterOS (version 6.x) in a SOHO environment. By utilizing firewall rules, schedules, and optional whitelisting, parents can effectively manage internet access for their children's devices. Both CLI and REST API examples have been provided, catering to different technical preferences and automation needs. Remember to implement security hardening measures and regular backups to ensure a secure and reliable Kid Control setup. For advanced features or larger networks, further customization and more complex configurations may be necessary. Always refer to the official MikroTik RouterOS documentation for the most up-to-date information and advanced features.

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