---
generated_at: 2025-02-03T21:22:14.758575
topic: MACsec
category: Bridging & Switching
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

Okay, I will generate comprehensive MikroTik RouterOS documentation for MACsec as per your specifications. Please note that MACsec support in RouterOS 6.x might be somewhat limited compared to newer versions.  We will focus on the basic setup and address the constraints of RouterOS 6.x as much as possible.

## MikroTik RouterOS MACsec Documentation (Version 6.x, SOHO - Basic)

**Topic:** MACsec (Media Access Control Security)
**RouterOS Version:** 6.x
**Network Scale:** SOHO (Small Office/Home Office)
**Complexity Level:** Basic

**1. Architecture Diagram Requirements**

For a SOHO environment, MACsec is typically deployed to secure critical links, such as between a router and a core switch or between a router and a high-value server/NAS.  Here's a basic architecture diagram illustrating a common SOHO MACsec deployment:

```mermaid
graph LR
    subgraph SOHO Network
        R[MikroTik Router] -- MACsec Link --> S[MACsec Capable Switch];
        S --> PC1[PC];
        S --> NAS[NAS Server (Critical Data)];
        R --> Internet[Internet Connection];
    end
    style R fill:#ccf,stroke:#333,stroke-width:2px
    style S fill:#f9f,stroke:#333,stroke-width:2px
    style PC1 fill:#eee,stroke:#333,stroke-width:1px
    style NAS fill:#eee,stroke:#333,stroke-width:1px
    style Internet fill:#eee,stroke:#333,stroke-width:1px
    linkStyle 0 stroke:#007bff,stroke-width:2px,stroke-dasharray:5 5
```

**Diagram Explanation:**

* **MikroTik Router:** Your main RouterOS device, acting as the gateway for the SOHO network.
* **MACsec Capable Switch:** A switch that supports MACsec, protecting the LAN segment from unauthorized access and eavesdropping.
* **MACsec Link:** The physical Ethernet link between the router and the switch, secured using MACsec encryption.
* **PC, NAS:**  Typical devices within the SOHO network, with the NAS highlighted as a critical resource that benefits from MACsec protection on the link to the switch.
* **Internet Connection:**  Standard internet connectivity provided by the MikroTik router.

**2. CLI Configuration with Inline Comments**

We will configure MACsec on an Ethernet interface of the MikroTik router.  Assume the interface is named `ether1`. You will need to have a MACsec Key Agreement (MKA) capable peer on the other end of the link (e.g., a MACsec-capable switch or another MikroTik router).

```routeros
/interface macsec add name=macsec1 interface=ether1  # Create a new MACsec interface
set macsec1 enabled=yes  # Enable the MACsec interface
set macsec1 port-priority=0  # Set port priority (lower value = higher priority in MKA)
set macsec1 confidentiality-offset=0  # Set confidentiality offset (0 for no offset, 30 or 50 for higher security)
set macsec1 cipher-suite=gcm-aes-128  # Choose cipher suite (gcm-aes-128, gcm-aes-256) - gcm-aes-128 is common and sufficient for SOHO
set macsec1 transmit-sci=yes # Enable transmit SCI (Security Channel Identifier)
set macsec1 receive-sci=yes  # Enable receive SCI

/interface macsec keys add interface=macsec1  # Add a key for the MACsec interface
set [find interface=macsec1] key=0123456789abcdef0123456789abcdef  # Set the primary key (32 hexadecimal characters - REPLACE with a strong, randomly generated key!)
set [find interface=macsec1] key-type=cak  # Key type is Connectivity Association Key (CAK)
set [find interface=macsec1] next-key=fedcba9876543210fedcba9876543210 # Set a next key for pre-computation (optional, for key rollover - REPLACE with another strong, random key if used)
set [find interface=macsec1] next-key-type=cak # Next key type

/interface ethernet set ether1 mac-protocol=macsec1  # Assign the MACsec interface to the physical Ethernet interface
```

**Important Notes:**

* **`key` and `next-key`:**  **Replace the example keys (`0123456789abcdef0123456789abcdef` and `fedcba9876543210fedcba9876543210`) with strong, randomly generated 32-character hexadecimal keys.** These keys must be **identical** on both MACsec peers.
* **`cipher-suite`:**  `gcm-aes-128` provides a good balance of security and performance for most SOHO environments. `gcm-aes-256` is more secure but may have a slight performance impact.
* **`confidentiality-offset`:**  Offsets of 30 or 50 can increase security against certain attacks but might affect performance slightly. `0` is typically sufficient for basic SOHO security.
* **`transmit-sci` and `receive-sci`:** SCI is generally required for MACsec to function correctly in modern networks.
* **Key Management:**  This example uses pre-shared keys. For larger deployments or higher security needs, consider more advanced key management solutions if supported by your hardware and RouterOS version.

**3. REST API Implementation (Python code)**

Since RouterOS 6.x REST API capabilities might be limited, we'll use a Python library (like `routeros_api`) to interact with the RouterOS API.  We'll perform the same MACsec configuration as in the CLI example.

```python
import routeros_api
from routeros_api import exceptions

ROUTER_HOST = 'your_router_ip'  # Replace with your Router IP
ROUTER_USER = 'api_user'       # Replace with your API username
ROUTER_PASSWORD = 'api_password' # Replace with your API password
MACSEC_INTERFACE_NAME = 'ether1' # Physical Ethernet interface for MACsec

# Generate strong, random keys (replace these with your own secure key generation)
PRIMARY_KEY = '0123456789abcdef0123456789abcdef' # REPLACE with your strong key
NEXT_KEY = 'fedcba9876543210fedcba9876543210'    # REPLACE with your strong key (if using next-key)

try:
    api_client = routeros_api.RouterOsApiPool(ROUTER_HOST, username=ROUTER_USER, password=ROUTER_PASSWORD, plaintext_login=True)
    api = api_client.get_api()

    # Create MACsec interface
    macsec_interface = api.get_resource('/interface/macsec')
    macsec_interface.add(name='macsec1', interface=MACSEC_INTERFACE_NAME)
    print(f"MACsec interface 'macsec1' created on {MACSEC_INTERFACE_NAME}")

    # Configure MACsec interface
    macsec_interface.set(
        id='macsec1', # Use ID to ensure we are setting the correct interface
        enabled='yes',
        port_priority='0',
        confidentiality_offset='0',
        cipher_suite='gcm-aes-128',
        transmit_sci='yes',
        receive_sci='yes'
    )
    print(f"MACsec interface 'macsec1' configured.")

    # Add MACsec key
    macsec_keys = api.get_resource('/interface/macsec/keys')
    macsec_keys.add(interface='macsec1')
    print("MACsec key entry added.")

    # Set MACsec key values
    keys_list = macsec_keys.get(search={'interface': 'macsec1'}) # Get the ID of the newly added key
    if keys_list:
        key_id = keys_list[0]['id']
        macsec_keys.set(
            id=key_id,
            key=PRIMARY_KEY,
            key_type='cak',
            next_key=NEXT_KEY, # Optional - if using next key
            next_key_type='cak' # Optional - if using next key
        )
        print("MACsec keys configured.")
    else:
        print("Error: Could not retrieve MACsec key ID.")

    # Assign MACsec to physical interface
    ethernet_interface = api.get_resource('/interface/ethernet')
    ethernet_interface.set(id=MACSEC_INTERFACE_NAME, mac_protocol='macsec1')
    print(f"MACsec 'macsec1' assigned to Ethernet interface '{MACSEC_INTERFACE_NAME}'.")


except exceptions.RouterOsApiError as e:
    print(f"RouterOS API Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'api_client' in locals() and api_client.connected:
        api_client.close()
```

**Error Handling:**

The Python code includes basic error handling using `try...except` blocks to catch `RouterOsApiError` (for RouterOS API specific issues) and general exceptions. In a production script, you would want more robust error handling and logging.

**4. Common Debugging Scenarios**

* **No MACsec Link Established:**
    * **Key Mismatch:** The most common issue. Ensure the pre-shared keys are **identical** on both MACsec peers. Double-check for typos and correct key type (CAK).
    * **Cipher Suite Mismatch:** Verify that both peers are configured with the same `cipher-suite`.
    * **SCI Mismatch:** Ensure both `transmit-sci` and `receive-sci` are enabled or disabled consistently on both sides.
    * **MKA Failure:** Check RouterOS logs (`/log print`) for MACsec or MKA related errors. Increase logging verbosity if needed (`/system logging add topics=macsec,mka action=memory`).
    * **Physical Link Issues:** Rule out basic Ethernet connectivity problems (cable, port issues).

* **Performance Issues:**
    * **CPU Overload:** MACsec encryption/decryption is CPU-intensive. Monitor CPU usage on the MikroTik router (`/system resource print`). If CPU is consistently high, consider:
        * Using a less CPU-intensive cipher suite (if security requirements allow).
        * Offloading MACsec processing to hardware if your MikroTik model supports it (check RouterOS documentation for hardware offload capabilities, which might be limited in RouterOS 6.x).
        * Upgrading to a more powerful MikroTik router.
    * **Incorrect MTU:** MACsec adds overhead. Ensure that the MTU (Maximum Transmission Unit) is properly configured to account for MACsec headers.  Consider using path MTU discovery or manually reducing the MTU on the MACsec interface and physical interface.

* **Intermittent Link Issues:**
    * **Key Rollover Problems:** If using `next-key`, ensure the key rollover process is correctly configured and synchronized on both peers. Incorrect key rollover can lead to temporary link disruptions.
    * **MKA Session Instability:**  Check logs for MKA session flaps or renegotiations.  This could indicate underlying network issues or configuration problems.

**Debugging Commands:**

* **`/interface macsec print`**:  Shows the MACsec interface configuration.
* **`/interface macsec keys print`**:  Displays configured MACsec keys (keys themselves are masked in output for security, but you can see key IDs, types, etc.).
* **`/interface macsec mka print`**:  Provides status information about the MKA session. Look at `state`, `negotiated-cipher-suite`, `negotiated-confidentiality-offset`, etc.
* **`/interface macsec statistics print`**:  Shows MACsec statistics (packets encrypted, decrypted, errors, etc.). Useful for performance monitoring and troubleshooting.
* **`/log print topics=macsec,mka`**:  Filter logs specifically for MACsec and MKA messages.

**5. Version-Specific Considerations (RouterOS 6.x)**

* **Feature Set:**  MACsec support in RouterOS 6.x might be more basic compared to later versions (RouterOS 7+).  Advanced features like hardware offload, more cipher suite options, or sophisticated key management might be limited or unavailable.
* **Stability:**  Ensure you are running the latest stable release of RouterOS 6.x to benefit from bug fixes and improvements related to MACsec.
* **Documentation:**  Refer to the MikroTik RouterOS 6.x documentation specifically for MACsec, as newer documentation might describe features not available in version 6.x.
* **Hardware Compatibility:**  MACsec is generally hardware-dependent. Verify that the Ethernet interfaces on your MikroTik router and the peer device (switch, etc.) are indeed MACsec-capable. Not all Ethernet ports support MACsec. Check the specifications of your MikroTik hardware.

**6. Security Hardening Measures**

* **Strong Pre-Shared Keys:**  **Crucially, use strong, randomly generated 32-character hexadecimal keys for MACsec.**  Avoid weak or easily guessable keys. Use a cryptographically secure random number generator to create keys.
* **Secure Key Storage:**  Store the MACsec keys securely. Avoid storing them in plain text in scripts or configuration files if possible.  Consider using a password manager or secure vault for key management.
* **Access Control:**  Restrict access to the MikroTik router's configuration. Use strong passwords for administrative users and consider implementing role-based access control (if available in RouterOS 6.x - check documentation). Limit API access to only authorized users and systems.
* **Regular Key Rotation (Optional):**  While not strictly necessary in a typical SOHO environment, for higher security, consider periodically rotating the MACsec keys. This requires a well-planned key rollover process (using `next-key` mechanism if implemented correctly on both peers).
* **Monitor for Anomalies:**  Regularly monitor MACsec statistics and logs for any unusual activity or errors that might indicate a security issue or misconfiguration.

**7. Performance Optimization Tips**

* **Cipher Suite Selection:**  `gcm-aes-128` is generally a good choice for performance and security in SOHO environments.  `gcm-aes-256` offers higher security but may have a slight performance overhead.  Test both and choose based on your specific needs and hardware capabilities.
* **Confidentiality Offset:**  Using a confidentiality offset (`30` or `50`) increases security but can slightly impact performance. If performance is critical, use `0` unless required by security policy.
* **MTU Optimization:**  Correct MTU configuration is crucial for MACsec performance. Ensure that the MTU is set appropriately to avoid fragmentation due to MACsec overhead. Path MTU discovery or manual MTU reduction might be needed.
* **Hardware Offload (If Available):**  Check if your MikroTik router model and RouterOS 6.x version support MACsec hardware offload. Hardware offload can significantly improve performance by offloading encryption/decryption tasks from the CPU to dedicated hardware. Consult MikroTik documentation for your specific hardware.
* **Minimize CPU Load:**  Avoid running other CPU-intensive processes on the MikroTik router if MACsec performance is critical. Dedicate sufficient CPU resources to MACsec processing.

**SOHO Environment Specific Requirements:**

**Real-World Deployment Examples:**

* **Securing NAS Link:** Protect the link between the MikroTik router and a NAS (Network Attached Storage) device containing sensitive data. This prevents eavesdropping or tampering on the network link.
* **Protecting Critical Workstation:** Secure the connection between the router and a workstation used for sensitive tasks (e.g., home office workstation handling financial data, remote access to corporate resources).
* **Securing Core Switch Link:**  Protect the uplink between the MikroTik router and a core switch in a small office, securing the entire LAN segment connected to that switch.

**Scalability Considerations:**

* **Limited Scalability in SOHO:** MACsec in a SOHO environment is typically deployed on a small number of critical links. Scalability is not usually a primary concern in this context.
* **Hardware Limits:**  Scalability is mainly limited by the processing capabilities of the MikroTik router and the number of MACsec-capable interfaces available. RouterOS 6.x on SOHO-grade hardware might have limitations on the number of concurrent MACsec sessions it can handle effectively.
* **Key Management:**  Pre-shared keys are simple for SOHO but do not scale well for larger networks. For larger deployments, more advanced key management (like 802.1X based key distribution, if supported in later RouterOS versions and hardware) would be needed.

**Monitoring Configurations:**

* **Real-time Monitoring (CLI):** Use commands like `/interface macsec mka print` and `/interface macsec statistics print` in the CLI to monitor the MACsec link status and performance in real-time.
* **Logging:** Configure RouterOS logging to capture MACsec and MKA events. Set up remote logging (e.g., to a syslog server) for centralized monitoring and analysis.
* **SNMP (Simple Network Management Protocol):** If your monitoring system supports SNMP, configure SNMP on the MikroTik router to collect MACsec related MIBs (if available in RouterOS 6.x - check MIB documentation). This allows for integration with network monitoring dashboards.
* **API-based Monitoring (Scripting):** Use the RouterOS API (as shown in the Python example) to periodically query MACsec status, statistics, and MKA information.  Write scripts to parse this data and generate alerts or reports if issues are detected.

**Disaster Recovery Steps:**

* **Configuration Backup:**  Regularly back up the MikroTik router's configuration, including the MACsec settings. Use RouterOS backup functionality (`/system backup save`) or export the configuration to a file (`/export file=config.rsc`). Store backups securely and offsite.
* **Configuration Restoration:** In case of configuration loss or corruption, restore the backup configuration using `/system backup load` or import the configuration file using `/import file=config.rsc`. Test the restoration process periodically.
* **Key Management Documentation:**  Keep a secure record of the MACsec pre-shared keys used.  In case of key loss, you will need to reconfigure MACsec with the original keys or generate new keys and update both peers.
* **Fallback Plan:**  In case of a MACsec failure that cannot be quickly resolved, have a fallback plan. This might involve temporarily disabling MACsec on the affected link (if security impact is acceptable) to restore connectivity while troubleshooting the MACsec issue.

**Automated Backup Scripts (RouterOS Scripting):**

Here's a basic example of a RouterOS script to automate configuration backup:

```routeros
:local backupFileName ("macsec_config_backup_" . [:system clock get date format=yyyy-MM-dd] . "_" . [:system clock get time format=HH-mm-ss])
/system backup save name=$backupFileName
:log info ("MACsec Configuration Backup Created: " . $backupFileName)

# Optional: Download backup via FTP (replace with your FTP server details)
#:local ftpServer "your_ftp_server_ip"
#:local ftpUser "ftp_username"
#:local ftpPassword "ftp_password"
#:delay 5s  # Wait for backup file creation
#/tool fetch url="ftp://$ftpUser:$ftpPassword@$ftpServer/$backupFileName.backup" mode=ftp upload=yes src-path=$backupFileName.backup
#:log info ("MACsec Configuration Backup Uploaded to FTP Server: " . $ftpServer)

# Optional: Cleanup old backups (keep last 7 backups for example)
#:local backupCount [/file find name~"macsec_config_backup_.*\.backup" count-only]
#:if ($backupCount > 7) do={
#  :local oldestBackup [/file find name~"macsec_config_backup_.*\.backup" order-by=creation-time first]
#  /file remove $oldestBackup
#  :log info ("Oldest Backup Removed.")
#}
```

**Explanation:**

* **`backupFileName`**:  Generates a filename for the backup using the current date and time.
* **`/system backup save name=$backupFileName`**:  Creates a backup file with the generated name.
* **`:log info (...)`**:  Logs messages to the RouterOS log for monitoring backup status.
* **Optional FTP Upload (commented out):**  Shows how to upload the backup to an FTP server for offsite storage. You need to uncomment and configure FTP server details.
* **Optional Backup Cleanup (commented out):** Demonstrates how to remove old backup files to prevent disk space exhaustion.  Adjust the `backupCount` value as needed.

**Schedule the Script:**

Use the RouterOS scheduler (`/system scheduler`) to run this script automatically at regular intervals (e.g., daily or weekly).

**Comparative Table for Different Approaches:**

| Feature/Aspect        | Pre-Shared Keys (PSK) | Certificate-Based Authentication (Not in Basic 6.x) |
|------------------------|-----------------------|---------------------------------------------------|
| **Key Management**     | Manual, Simple        | More complex, Scalable, Automated                |
| **Security**           | Good for SOHO        | Higher Security, Stronger Authentication          |
| **Scalability**        | Limited               | Better Scalability                               |
| **Complexity**         | Low                   | Higher                                           |
| **Configuration**      | Easier                | More involved                                     |
| **RouterOS 6.x Support** | Yes (Basic)           | Limited or No (Basic 6.x)                         |
| **SOHO Suitability**   | Excellent             | Overkill for most SOHO scenarios                  |

**Conclusion:**

This document provides a comprehensive guide to setting up basic MACsec in a SOHO environment using MikroTik RouterOS 6.x. While RouterOS 6.x might have limitations compared to newer versions, MACsec can still significantly enhance the security of critical network links in a SOHO setup. By following these instructions, understanding the debugging steps, and implementing the security hardening measures, you can effectively deploy and manage MACsec in your SOHO network. Remember to always consult the official MikroTik documentation for the most up-to-date information and best practices.

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