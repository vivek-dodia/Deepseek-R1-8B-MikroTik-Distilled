---
generated_at: 2025-02-03T21:16:25.246491
topic: RADIUS
category: Security Services
version: 6.x
scale: SOHO
level: Basic
model: gemini-2.0-flash-thinking-exp-01-21
---

## MikroTik RouterOS RADIUS Documentation for SOHO Environments (v6.x - Basic)

**Document Version:** 1.0
**Author:** [Your Name/Alias] - MikroTik Certified Engineer
**Date:** October 26, 2023
**Target Audience:** SOHO Network Administrators, MikroTik Technicians

**1. Introduction to RADIUS in SOHO**

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network. In a SOHO (Small Office/Home Office) environment, RADIUS can be used to enhance security and manage access to network resources, especially for Wi-Fi networks or VPN access. This document focuses on basic RADIUS configuration on MikroTik RouterOS v6.x for SOHO deployments.

**2. Architecture Diagram**

```mermaid
graph LR
    A[Client Device (Laptop, Phone)] --> B(MikroTik Router);
    B --> C[RADIUS Server];
    style B fill:#f9f,stroke:#333,stroke-width:2px
    subgraph SOHO Network
        A
        B
    end
    subgraph Authentication Flow
        direction LR
        B -->|Authentication Request| C
        C -->|Authentication Response (Accept/Reject)| B
        B -->|Access Granted/Denied| A
    end
```

**Diagram Explanation:**

* **Client Device:**  Represents a user device attempting to connect to the network (e.g., via Wi-Fi).
* **MikroTik Router:** Acts as the RADIUS client (NAS - Network Access Server), forwarding authentication requests to the RADIUS server.
* **RADIUS Server:**  A server (could be on-premise or cloud-based) that stores user credentials and authentication policies. It validates user requests and sends back authorization decisions.
* **Authentication Flow:** Illustrates the basic steps of RADIUS authentication: request from the router, response from the server, and access control by the router.

**3. CLI Configuration (RouterOS v6.x)**

This section details the CLI commands to configure the MikroTik RouterOS as a RADIUS client.

```cli
/radius # Navigate to the RADIUS menu

add address=192.168.1.100 secret="your_radius_secret" \ # Add RADIUS server configuration
    protocol=udp timeout=300ms comment="My RADIUS Server" \ # UDP protocol, 300ms timeout, descriptive comment
    service=ppp,login,hotspot,wireless # Services to use RADIUS for (PPP, Login, Hotspot, Wireless)
```

**Inline Comments Explanation:**

* `/radius`: Navigates the CLI to the RADIUS configuration menu.
* `add`: Creates a new RADIUS server configuration.
    * `address=192.168.1.100`: Specifies the IP address of your RADIUS server. **Replace with your RADIUS server IP.**
    * `secret="your_radius_secret"`: Sets the shared secret key used for communication between the router and the RADIUS server. **Replace with a strong, unique secret.**  This secret MUST match the secret configured on your RADIUS server for this client.
    * `protocol=udp`: Defines the communication protocol as UDP (User Datagram Protocol), which is typical for RADIUS.
    * `timeout=300ms`: Sets the timeout for RADIUS requests to 300 milliseconds. Adjust if needed based on network latency.
    * `comment="My RADIUS Server"`: Adds a descriptive comment to easily identify this RADIUS server configuration.
    * `service=ppp,login,hotspot,wireless`: Specifies which RouterOS services should utilize this RADIUS server for authentication. Common services for SOHO include:
        * `ppp`: For PPP-based VPNs (PPPoE, PPTP, L2TP).
        * `login`: For router login authentication (Winbox, SSH, WebFig).
        * `hotspot`: For Hotspot user authentication.
        * `wireless`: For Wi-Fi access point authentication (e.g., using WPA2-Enterprise).

**Applying RADIUS to Services (Example: Wireless)**

To use the configured RADIUS server for Wi-Fi authentication, you need to configure the Wireless Security Profile.

```cli
/interface wireless security-profiles # Navigate to wireless security profiles

set [ find default=no name="your_security_profile" ] authentication-types=wpa2-psk,wpa2-eap \ # Enable WPA2-EAP (RADIUS)
    mode=dynamic-keys eap-methods=passthrough group-key-update-interval=5m \ # Dynamic keys, EAP passthrough
    supplicant-identity=MikroTik use-radius=yes radius-mac-format=username # Enable RADIUS, MAC as username

/interface wireless access-list # Optional: if using access-list for finer control
# Add rules to allow access based on RADIUS authentication if needed.
```

**Inline Comments Explanation:**

* `/interface wireless security-profiles`: Navigates to the wireless security profiles menu.
* `set [ find default=no name="your_security_profile" ]`:  Selects the specific wireless security profile you want to modify. **Replace `"your_security_profile"` with the name of your profile.**  `default=no` ensures you are not modifying the default profile.
    * `authentication-types=wpa2-psk,wpa2-eap`: Enables both WPA2-PSK (for fallback or other SSIDs) and WPA2-EAP (RADIUS authentication).
    * `mode=dynamic-keys`: Uses dynamic keys for enhanced security.
    * `eap-methods=passthrough`: Allows the RADIUS server to determine the EAP method.
    * `group-key-update-interval=5m`:  Sets the interval for group key updates.
    * `supplicant-identity=MikroTik`:  Sets a supplicant identity (optional).
    * `use-radius=yes`: **Crucially enables RADIUS authentication for this security profile.**
    * `radius-mac-format=username`:  Sends the client's MAC address as the username to the RADIUS server (common in SOHO for simple MAC-based authentication or logging). You can configure other formats if your RADIUS server expects different usernames.

**4. REST API Implementation (Python - `routeros_api`)**

This Python script uses the `routeros_api` library to configure RADIUS settings via the MikroTik API.

```python
import routeros_api
import routeros_api.exceptions

# RouterOS connection details
HOST = 'your_router_ip' # Replace with your RouterOS IP
USERNAME = 'your_username' # Replace with your RouterOS username
PASSWORD = 'your_password' # Replace with your RouterOS password
RADIUS_SERVER_IP = '192.168.1.100' # Replace with your RADIUS server IP
RADIUS_SECRET = 'your_radius_secret' # Replace with your RADIUS secret
WIRELESS_PROFILE_NAME = 'your_security_profile' # Replace with your wireless security profile name

try:
    # Connect to RouterOS API
    api = routeros_api.RouterOsApiPool(HOST, username=USERNAME, password=PASSWORD, port=8728).get_api()

    # Get RADIUS resource
    radius_resource = api.get_resource('/radius')

    # Add RADIUS server configuration
    radius_resource.add(
        address=RADIUS_SERVER_IP,
        secret=RADIUS_SECRET,
        protocol='udp',
        timeout='300ms',
        comment='My RADIUS Server (API)',
        service='ppp,login,hotspot,wireless'
    )
    print("RADIUS server configuration added successfully.")

    # Get Wireless Security Profiles resource
    wireless_profiles_resource = api.get_resource('/interface/wireless/security-profiles')

    # Find the target wireless security profile
    profile = wireless_profiles_resource.get(name=WIRELESS_PROFILE_NAME)
    if profile:
        profile_id = profile[0]['.id'] # Get the internal ID of the profile

        # Update Wireless Security Profile for RADIUS
        wireless_profiles_resource.set(
            id=profile_id,
            authentication_types='wpa2-psk,wpa2-eap',
            mode='dynamic-keys',
            eap_methods='passthrough',
            group_key_update_interval='5m',
            supplicant_identity='MikroTik',
            use_radius='yes',
            radius_mac_format='username'
        )
        print(f"Wireless Security Profile '{WIRELESS_PROFILE_NAME}' updated for RADIUS.")
    else:
        print(f"Wireless Security Profile '{WIRELESS_PROFILE_NAME}' not found.")


except routeros_api.exceptions.RouterOsApiError as e:
    print(f"RouterOS API Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'api' in locals() and api:
        api.close() # Close the API connection
```

**Python Code Explanation:**

* **Import Libraries:** Imports `routeros_api` and `routeros_api.exceptions` for API interaction and error handling.
* **Configuration Variables:**  Defines variables for RouterOS IP, credentials, RADIUS server details, and wireless profile name. **Replace placeholders with your actual values.**
* **`try...except...finally` Block:** Encloses the API operations for error handling and resource cleanup.
* **API Connection:** Establishes a connection to the RouterOS API using `routeros_api.RouterOsApiPool`.
* **RADIUS Resource:** Gets the RADIUS resource object using `api.get_resource('/radius')`.
* **`radius_resource.add(...)`:** Adds the RADIUS server configuration similar to the CLI example.
* **Wireless Profiles Resource:** Gets the wireless security profiles resource.
* **Find Profile:** Retrieves the specific wireless security profile by name using `wireless_profiles_resource.get(name=WIRELESS_PROFILE_NAME)`.
* **`wireless_profiles_resource.set(...)`:** Updates the wireless security profile with RADIUS settings.
* **Error Handling:** `routeros_api.exceptions.RouterOsApiError` catches RouterOS specific API errors. The generic `Exception` catches other potential Python errors.
* **API Close:** `api.close()` ensures the API connection is closed in the `finally` block, even if errors occur.

**5. Common Debugging Scenarios**

* **Authentication Failures:**
    * **Check RADIUS Server Logs:** The primary place to troubleshoot is the RADIUS server logs. These logs will provide details about authentication requests, username/password checks, and reasons for failure.
    * **Verify Shared Secret:** Ensure the `secret` configured on the MikroTik router **exactly matches** the secret configured for this client on the RADIUS server. Case sensitivity matters.
    * **Network Connectivity:** Confirm that the MikroTik router can reach the RADIUS server on UDP port 1812 or 1813 (authentication/accounting ports, respectively, though accounting is not configured here). Use `ping 192.168.1.100` from the MikroTik CLI. Check firewall rules if any.
    * **Service Mismatch:** Double-check that the `service` parameter in the `/radius add` command includes the services you are using RADIUS for (e.g., `wireless`, `hotspot`).
    * **Username/Password Issues:** Verify the username and password are correct in the RADIUS server's user database.
    * **RADIUS Server Configuration:** Ensure the RADIUS server is correctly configured to accept authentication requests from the MikroTik router's IP address and is listening on the correct ports.

* **No RADIUS Requests Sent:**
    * **`use-radius=yes`:** Double-check that `use-radius=yes` is enabled in the relevant service configuration (e.g., wireless security profile).
    * **Service Type:** Verify that the service type configured on the MikroTik (e.g., `wireless`, `hotspot`) is actually configured to use RADIUS.
    * **Firewall on Router:** Check if any firewall rules on the MikroTik itself are blocking outbound UDP traffic to the RADIUS server.
    * **Interface Configuration:** Ensure the interface used for the service (e.g., wireless interface) is correctly configured and enabled.

* **Debugging Commands on MikroTik:**
    * **`/radius print`:** Displays the configured RADIUS servers and their status.
    * **`/system logging action add name=radius_log target=memory memory-lines=1000`**: Creates a logging action to store RADIUS logs in memory.
    * **`/system logging add topics=radius action=radius_log`**: Enables logging for RADIUS topics using the created action.
    * **`/log print where topics~"radius"`**: Displays the RADIUS logs from memory.  Look for error messages or clues about authentication issues.

**6. Version-Specific Considerations (RouterOS v6.x)**

* **Feature Stability:** RADIUS functionality in RouterOS v6.x is generally stable and mature.
* **API Compatibility:** The `routeros_api` library is compatible with RouterOS v6.x API.
* **Security Updates:** Ensure your RouterOS v6.x is updated to the latest stable version within the 6.x branch to benefit from security patches. However, consider migrating to a newer RouterOS version (v7) for the latest features and long-term support, if feasible.
* **RADIUS Accounting:** While this document focuses on basic authentication, RouterOS v6.x also supports RADIUS accounting. If you need to track user session duration and data usage, you would need to configure accounting settings in the `/radius` menu and on your RADIUS server.

**7. Security Hardening Measures**

* **Strong Shared Secret:** Use a strong, randomly generated shared secret for RADIUS communication. Avoid weak or easily guessable secrets.
* **Secret Management:** Securely store and manage the RADIUS shared secret. Do not expose it in scripts or configuration files in plain text unnecessarily.
* **Firewall Filtering:** If possible, restrict access to the RADIUS server to only the MikroTik router's IP address. Implement firewall rules on the RADIUS server and potentially on the MikroTik router itself to limit access to RADIUS ports (1812, 1813).
* **Regular Secret Rotation:** Periodically change the RADIUS shared secret as part of good security practice. Update both the MikroTik and RADIUS server configurations accordingly.
* **Monitor RADIUS Logs:** Regularly review RADIUS server and MikroTik RADIUS logs for any suspicious activity or authentication failures that might indicate security breaches or misconfigurations.
* **Consider RADIUS Accounting:** While not directly for authentication security, RADIUS accounting can help detect anomalies in usage patterns and potentially identify compromised accounts.
* **RouterOS Security:** Harden the MikroTik router itself by:
    * Changing default admin password.
    * Disabling unused services.
    * Implementing a strong firewall (as documented in other examples).
    * Keeping RouterOS updated.
    * Limiting access to management interfaces (Winbox, SSH, WebFig) to trusted networks.

**8. Performance Optimization Tips**

* **RADIUS Server Proximity:** Place the RADIUS server as close to the MikroTik router as possible in the network to minimize latency and improve authentication speed. A local RADIUS server on the same LAN is ideal for SOHO.
* **UDP Protocol:** UDP is generally faster than TCP for RADIUS due to its connectionless nature and lower overhead. Stick with UDP unless you have specific reasons to use TCP.
* **Timeout Value:** Adjust the `timeout` parameter in `/radius add` appropriately. A too-short timeout can lead to unnecessary retransmissions, while a too-long timeout can cause delays in authentication failures. 300ms is a reasonable starting point for a local network.
* **Minimize RADIUS Attributes:** Only request and send necessary RADIUS attributes to reduce the size of RADIUS packets and processing overhead. In basic SOHO scenarios, you likely only need username and password authentication attributes.
* **RouterOS Resource Monitoring:** Monitor the CPU and memory usage of your MikroTik router. If RADIUS processing is causing high load, consider upgrading to a more powerful MikroTik model or optimizing other router configurations.

**9. SOHO Specific Requirements**

**9.1. Real-World Deployment Examples**

* **Example 1: Secure Wi-Fi for Home Office:**
    * **Scenario:** A home office with multiple family members and guests using Wi-Fi. The user wants to control and monitor Wi-Fi access using RADIUS.
    * **Implementation:** Use a RADIUS server (e.g., FreeRADIUS on a Raspberry Pi or a cloud-based RADIUS service). Configure the MikroTik router's Wi-Fi security profile to use WPA2-EAP and point it to the RADIUS server. Create user accounts on the RADIUS server for each family member and guest (if needed).
    * **Benefits:** Centralized user management, potentially MAC address-based authentication for ease of use in a home environment, basic logging of Wi-Fi access.

* **Example 2: VPN Access Control for Small Business:**
    * **Scenario:** A small business with remote employees needing VPN access to the office network. The business wants to use RADIUS for VPN user authentication.
    * **Implementation:** Set up a VPN server on the MikroTik router (e.g., L2TP/IPsec). Configure the VPN server to use RADIUS for authentication. Point the RADIUS client configuration on the MikroTik to an on-premise or cloud-based RADIUS server. Create VPN user accounts on the RADIUS server for employees.
    * **Benefits:** Secure VPN access with centralized user management, stronger password policies enforced by RADIUS, logging of VPN connections.

**9.2. Scalability Considerations (SOHO)**

* **Limited Scale:** SOHO environments typically have a relatively small number of users and devices. Basic RADIUS setups on RouterOS v6.x are generally sufficient for this scale.
* **RADIUS Server Capacity:** The scalability bottleneck is more likely to be the RADIUS server itself, especially if using a low-resource server like a Raspberry Pi.  Consider the expected number of concurrent authentication requests.
* **RouterOS Performance:** For a small number of RADIUS users, MikroTik SOHO routers have sufficient processing power. If you anticipate a significant increase in users or services using RADIUS, you might need to consider a more powerful RouterOS device.
* **Cloud RADIUS for Scalability:** For future growth or if you anticipate needing to handle a larger number of users, consider using a cloud-based RADIUS service. These services are designed to be highly scalable and reliable.

**9.3. Monitoring Configurations**

* **RouterOS Logging (as shown in Debugging section):** Enable RADIUS logging on the MikroTik to monitor authentication attempts and errors. Regularly check these logs.
* **RADIUS Server Monitoring:** Implement monitoring on your RADIUS server itself. Most RADIUS server software provides logging and monitoring capabilities. Monitor server CPU, memory, disk space, and RADIUS service status.
* **Simple Network Management Protocol (SNMP):** RouterOS supports SNMP. You can use SNMP to monitor the overall health and performance of the MikroTik router, including resource usage that might be affected by RADIUS processing. Configure an SNMP server to collect data from the MikroTik.
* **System Health Monitoring in RouterOS:** Use RouterOS's built-in `/system health print` to check CPU load and memory usage. If you suspect RADIUS is causing performance issues, monitor these parameters.

**9.4. Disaster Recovery Steps**

* **Configuration Backup:** Regularly back up your MikroTik RouterOS configuration. This is crucial for any disaster recovery scenario. Use the automated backup scripts described below.
* **RADIUS Server Backup:** Back up the configuration and user database of your RADIUS server. The backup method will depend on the RADIUS server software you are using (e.g., database backups for FreeRADIUS).
* **Redundancy (Optional for SOHO):** For higher availability, consider setting up a redundant RADIUS server. RouterOS supports configuring multiple RADIUS servers. If the primary server fails, the router will attempt to use the secondary server.
* **Document Recovery Procedures:**  Document the steps to restore your MikroTik configuration and RADIUS server configuration. Test these recovery procedures periodically.
* **Emergency Access:** Ensure you have a backup method to access the MikroTik router in case RADIUS authentication fails or the RADIUS server is unavailable (e.g., a local admin account on the RouterOS that bypasses RADIUS).

**9.5. Automated Backup Scripts (RouterOS Scripting)**

This is a basic example of a RouterOS script to automate configuration backups and email them.

```routeros
:local backupFile ("/backup/router-backup-" . [:system date format="%Y-%M-%D"] . ".backup")
/system backup save name=$backupFile
/tool e-mail send to="your_email@example.com" \ # Replace with your email address
    subject="MikroTik Configuration Backup" \
    body="Router configuration backup attached." \
    file=$backupFile
:log info "Configuration backup created and emailed."
```

**Script Explanation:**

* **`:local backupFile ...`:** Creates a variable `backupFile` with the backup filename. It includes the date in the filename for versioning.
* **/system backup save name=$backupFile:** Saves a RouterOS configuration backup to the specified file.
* **/tool e-mail send ...:** Sends an email with the backup file attached. **Replace `"your_email@example.com"` with your actual email address.** You need to configure email settings under `/tool e-mail` in RouterOS for this to work.
* **`:log info ...`:** Logs a message to the RouterOS log indicating that the backup was created and emailed.

**Scheduling the Script:**

Use RouterOS `/system scheduler` to run this script automatically (e.g., daily).

```cli
/system scheduler
add name="Daily Backup" interval=1d start-time=01:00:00 on-event="/path/to/your/backup_script.rsc" # Replace with the actual script file path
```

**Comparative Table for Different RADIUS Approaches in SOHO**

| Feature             | Local RADIUS Server (e.g., FreeRADIUS on Raspberry Pi) | Cloud-Based RADIUS Service | MikroTik User Manager (Built-in RADIUS Lite) |
|----------------------|-------------------------------------------------------|-----------------------------|-------------------------------------------------|
| **Complexity**       | Medium (setup, maintenance)                            | Low (subscription-based)    | Low (integrated into RouterOS)                |
| **Scalability**       | Limited by server hardware                            | High (cloud infrastructure) | Very Limited (basic features)                  |
| **Cost**             | Hardware cost (Raspberry Pi), software is often free  | Subscription fees           | Included in RouterOS                             |
| **Control**           | Full control over server and data                    | Less control, relies on provider | Limited feature set, RouterOS dependent          |
| **Features**          | Rich feature set (depending on RADIUS server software) | Varies by provider, often rich | Basic RADIUS features, limited customization   |
| **Reliability**      | Depends on server setup and maintenance              | High (provider responsibility) | Depends on RouterOS stability                 |
| **SOHO Suitability** | Good for tech-savvy users wanting more control       | Excellent for ease of use and scalability | Good for very basic RADIUS needs within MikroTik |

**10. Conclusion**

RADIUS provides a valuable mechanism for centralized authentication in SOHO environments using MikroTik RouterOS. This document has outlined the basic configuration steps, debugging techniques, security considerations, and SOHO-specific aspects of RADIUS deployment. By implementing these guidelines, SOHO network administrators can enhance the security and manageability of their networks. Remember to adapt these configurations to your specific needs and always prioritize security best practices.

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