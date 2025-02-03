Okay, let's craft a comprehensive guide to configuring a MAC server on MikroTik RouterOS 6.48, focusing on a SOHO network using interface `wlan-39` on the subnet `105.138.10.0/24`.

## Scenario Description:

This scenario aims to provide a way to authenticate wireless clients using their MAC addresses. While not as robust or secure as using WPA2/3-Enterprise with RADIUS, MAC address authentication can be useful in controlled environments or for testing purposes. We will use the `wlan-39` interface as the access point and configure a MAC server that allows only specific clients, identified by their MAC addresses, to connect to the network. We are only focusing on the MAC server aspects. We are not going to enable wireless on the wlan-39 interface. That is outside the scope of this documentation.

## Implementation Steps:

Here’s a detailed step-by-step guide:

**1. Step 1:  Initial System State and Interface Preparation**

   *   **Purpose:** We need a starting point for our configuration. We are assuming a clean slate.
   *   **Before Configuration:** Assume the router is at factory default, or at least without prior configurations for this scenario.  `wlan-39` exists and has a default configuration.
   *   **MikroTik CLI Example:** Verify your wireless interface (`wlan-39`) exists.
      ```mikrotik
      /interface wireless print
      ```
      
      **Output Example (before any configuration):**
         ```
        Flags: X - disabled, R - running
         0    R  name="wlan1" mtu=1500 mac-address=C8:21:5E:31:14:03 arp=enabled 
              interface-type=wlan radio-name="1403" mode=ap-bridge ssid="MikroTik" 
              frequency=2412 band=2ghz-b/g/n channel-width=20/40mhz-Ce 
              disabled-auto-frequency=no antenna-gain=0 scan-list=default 
              wireless-protocol=802.11 wps-mode=disabled
         1  X  name="wlan-39" mtu=1500 mac-address=56:AB:00:10:20:3F arp=enabled
                 interface-type=wlan  frequency=2412  band=2ghz-b/g/n disabled=yes
         ```
      
       **Note:** In this scenario the interface is called wlan-39, and is disabled. We will proceed with this configuration.
   *   **Winbox GUI:** Navigate to *Wireless* under the *Interface* menu to verify the interface `wlan-39` is present.
   *   **Effect:** Checks the existing interface list. No changes to router.

**2. Step 2:  Enable and Basic Configuration of Interface `wlan-39` (Out of scope of this document, but assumed to be a configured access point)**

   *  **Purpose:** This step will bring the `wlan-39` interface up. This is outside the scope of this document, but it is required for MAC authentication to work on a wireless network. We assume `wlan-39` has been enabled, and configured as an Access Point (AP).
   *   **Before Configuration:** `wlan-39` is assumed to be enabled and in an AP mode.
   *   **MikroTik CLI Example:**
         ```mikrotik
         /interface wireless set wlan-39 mode=ap-bridge ssid=mac-auth-test
         /interface wireless enable wlan-39
        
         ```
    * **Output Example (after configuration):**
      ```
        Flags: X - disabled, R - running
         0    R  name="wlan1" mtu=1500 mac-address=C8:21:5E:31:14:03 arp=enabled 
              interface-type=wlan radio-name="1403" mode=ap-bridge ssid="MikroTik" 
              frequency=2412 band=2ghz-b/g/n channel-width=20/40mhz-Ce 
              disabled-auto-frequency=no antenna-gain=0 scan-list=default 
              wireless-protocol=802.11 wps-mode=disabled
         1    R  name="wlan-39" mtu=1500 mac-address=56:AB:00:10:20:3F arp=enabled
                 interface-type=wlan mode=ap-bridge ssid="mac-auth-test" frequency=2412 band=2ghz-b/g/n disabled=no
       ```
      
    * **Note:** The interface *must* be enabled, and operational for a wireless connection. The specific settings are outside the scope of this document.
    * **Winbox GUI:** Navigate to *Wireless* under the *Interface* menu, select the `wlan-39` and enable it, and configure it for `ap-bridge` and a suitable ssid.
    * **Effect:** The `wlan-39` is active and is an access point.

**3. Step 3: Create the MAC Server List**

   *   **Purpose:** The MAC server stores a list of allowed MAC addresses.
   *   **Before Configuration:** No MAC list exists.
   *   **MikroTik CLI Example:** We'll use the command `/interface wireless mac-server` to create the MAC server list and add entries.
         ```mikrotik
         /interface wireless mac-server add address=00:11:22:33:44:55 comment="Laptop 1"
         /interface wireless mac-server add address=AA:BB:CC:DD:EE:FF comment="Smartphone"
         /interface wireless mac-server print
         ```
   *   **Output Example (after configuration):**
         ```
        Flags: X - disabled, I - invalid
         #   ADDRESS         COMMENT  
         0   00:11:22:33:44:55  Laptop 1
         1   AA:BB:CC:DD:EE:FF  Smartphone
        ```
   *   **Winbox GUI:** Navigate to *Wireless* -> *MAC* tab and click the "+" button to add new entries.
   *   **Effect:** Creates a list of allowed MAC addresses. Only devices with these MAC addresses will be allowed access.

**4. Step 4: Enable MAC Authentication**
    *   **Purpose:**  We need to configure the access point to use the MAC server list.
    *   **Before Configuration:**  MAC authentication is disabled.
    *   **MikroTik CLI Example:** 
        ```mikrotik
        /interface wireless set wlan-39 mac-auth=mac-address
        /interface wireless print wlan-39
        ```
        
       **Output Example (after configuration):**
         ```
        Flags: X - disabled, R - running
         1  R  name="wlan-39" mtu=1500 mac-address=56:AB:00:10:20:3F arp=enabled
                 interface-type=wlan mode=ap-bridge ssid="mac-auth-test" frequency=2412 
                 band=2ghz-b/g/n disabled=no mac-auth=mac-address
       ```
    *   **Winbox GUI:** Go to *Wireless*, find the `wlan-39`, and check the `Mac Auth` option and select `mac-address`.
    *   **Effect:** Only MACs in the MAC server list can connect to the access point.

**5. Step 5: Configure DHCP Server**
    *   **Purpose:** Assuming clients require an IP address.
    *   **Before Configuration:** No DHCP Server configured.
    *   **MikroTik CLI Example:**
        ```mikrotik
         /ip pool add name=dhcp-pool-105-138-10 ranges=105.138.10.100-105.138.10.200
         /ip dhcp-server add address-pool=dhcp-pool-105-138-10 interface=wlan-39 name=dhcp-server-wlan-39
         /ip dhcp-server network add address=105.138.10.0/24 gateway=105.138.10.1 dns-server=1.1.1.1,8.8.8.8
       ```

    * **Winbox GUI:** Go to *IP* -> *DHCP Server*, add a DHCP Server by selecting wlan-39, and configure the network range.
    * **Effect:** Clients receive IP addresses in the 105.138.10.0/24 range.

## Complete Configuration Commands:

```mikrotik
# Enable the interface. This step may be different, as it is out of the scope of this document.
/interface wireless set wlan-39 mode=ap-bridge ssid=mac-auth-test
/interface wireless enable wlan-39

# Configure the MAC Server with the allowed MAC addresses
/interface wireless mac-server add address=00:11:22:33:44:55 comment="Laptop 1"
/interface wireless mac-server add address=AA:BB:CC:DD:EE:FF comment="Smartphone"

# Enable MAC Authentication on the wlan-39 interface
/interface wireless set wlan-39 mac-auth=mac-address

# Configure DHCP server for the network
/ip pool add name=dhcp-pool-105-138-10 ranges=105.138.10.100-105.138.10.200
/ip dhcp-server add address-pool=dhcp-pool-105-138-10 interface=wlan-39 name=dhcp-server-wlan-39
/ip dhcp-server network add address=105.138.10.0/24 gateway=105.138.10.1 dns-server=1.1.1.1,8.8.8.8
```

**Parameter Explanation:**

| Command                                 | Parameter           | Description                                                                                                    |
| :-------------------------------------- | :------------------ | :------------------------------------------------------------------------------------------------------------- |
| `/interface wireless set wlan-39 mode=ap-bridge ssid=mac-auth-test` | `mode`      | Set the interface mode to `ap-bridge`, which acts as a typical access point |
|                                       | `ssid`      | Set the SSID, `mac-auth-test` in this example |
| `/interface wireless enable wlan-39`                                       | `disabled`      | Set to `no`, which enables the interface |
| `/interface wireless mac-server add`    | `address`           | The MAC address of the device to allow (e.g., `00:11:22:33:44:55`)                                            |
|                                       | `comment`           | A descriptive comment for the MAC address (e.g., `Laptop 1`)                                                  |
| `/interface wireless set wlan-39 mac-auth=mac-address` | `mac-auth` | Enables mac authentication, and specifies that `mac-address` method is used |
| `/ip pool add` | `name` | The name of the IP pool |
|                | `ranges` | The range of IP address in this pool |
| `/ip dhcp-server add` | `address-pool` | The name of the address pool previously configured|
|                      | `interface` | The interface on which to enable the dhcp server|
|                      | `name` | The name of this dhcp-server instance|
| `/ip dhcp-server network add` | `address` | The network address with mask, which is used to give clients an IP address|
|                          | `gateway` | The gateway of the clients|
|                          | `dns-server` | The DNS server to use for the clients|

## Common Pitfalls and Solutions:

*   **Problem:** Device fails to connect.
    *   **Solution:** Double-check the MAC address in the MAC server list against the device's MAC address. Typos are a common issue. Make sure the MAC address in the client is the correct MAC address.
    *   **Troubleshooting:** Check `/interface wireless registration-table` to see if the device attempts to connect. The column `mac-address` in that table provides the actual MAC address the device is trying to use. If the client appears on the list, but no IP is assigned, then your dhcp-server, or pool is not working.
*   **Problem:**  Clients connect and disconnect intermittently.
    *   **Solution:** Check for overlapping channel usage.
    *   **Troubleshooting:** Use the wireless scan tool `/interface wireless scan` to see if other access points are using the same channel. Change the channel on your access point to a less congested one.
*   **Problem:** High CPU utilization.
    *   **Solution:** Review other services running on the router. Consider if you are using other intensive features. If this occurs only with a high number of connected clients, then the router may be undersized. Consider upgrading to a more powerful router.
    *   **Troubleshooting:**  Use the `/system resource print` command to monitor CPU and memory usage.
*   **Problem:** DHCP lease not assigned.
    *   **Solution:**  Verify DHCP server configuration, address pool and network.
    *   **Troubleshooting:**  Check `/ip dhcp-server lease print` to examine active DHCP leases and check for conflicts or errors. Verify the DHCP pool is configured correctly for the subnet.
*   **Security Issue:** MAC address spoofing is possible, so this method should *not* be used as a robust security solution.
    *   **Mitigation:** Use WPA2/3-Enterprise with RADIUS for more secure authentication.
    *   **Note:** MAC address filtering is a weak form of security and is easily bypassed.

## Verification and Testing Steps:

1.  **Connect a device with a permitted MAC:**
    *   Connect a wireless client (with a MAC address in the mac-server list) to the `wlan-39` SSID.
    *   The client should be able to connect, and it should obtain an IP address from the configured DHCP server.
2.  **Check DHCP Leases:**
    *   On the MikroTik, use the following command:
        ```mikrotik
        /ip dhcp-server lease print
        ```
        You should see an entry for the connected client.
3.  **Ping:**
    *   From the connected client, ping the router's IP address on the network (typically the gateway of your network: `105.138.10.1`).
    *   From the MikroTik router, ping the client IP address.
4.  **Connect a device with a non-permitted MAC:**
    *   Try connecting a wireless client with a MAC not in the MAC server list. It should *not* be able to connect to the wireless network. Or it may connect to the access point, but not receive an IP address.
5.  **Registration table:**
    *   Check the current registration table on the router:
          ```mikrotik
          /interface wireless registration-table print
          ```
      *   Look for the `mac-address` column, and verify that the allowed MAC address is associated with the connection.

## Related Features and Considerations:

*   **Wireless Security:** As noted, MAC filtering is very limited, and it is recommended to use WPA2/3-PSK or WPA2/3-Enterprise.
*   **RADIUS:** For more robust access control, consider using a RADIUS server with WPA2/3-Enterprise.
*   **User Manager:**  MikroTik's User Manager can be used for creating accounts, limiting bandwidth usage and more. It can be used as an advanced version of the MAC server functionality.
*   **Hotspot:** The hotspot feature offers far more control for captive portals and user-based authentication for Wi-Fi access.
*   **Real-world impact:** This simple setup can be used for a small office to prevent casual connections to a WiFi network, or to set up a test network. However, due to security implications, it is not recommended for sensitive deployments.

## MikroTik REST API Examples (if applicable):

While the MikroTik API is powerful, there are no dedicated endpoints for specific "MAC server" lists or settings. You'd typically manage MAC auth within the wireless interface settings and the access lists through existing API endpoints. Here are examples of how you would use the API.

**Enable MAC Authentication:**

```bash
curl -k -u admin:your_admin_password -H "Content-Type: application/json" -X PUT "https://192.168.88.1/rest/interface/wireless/wlan-39" -d '{"mac-auth":"mac-address"}'
```

**Response (successful):**

```json
{
   ".id": "*1",
   "mac-auth": "mac-address"
}
```

**Explanation:**

*   `curl -k -u admin:your_admin_password`: Basic authentication. Change `admin` and `your_admin_password`. Replace `192.168.88.1` with your routers IP address.
*   `-H "Content-Type: application/json"`: Sets the content type.
*   `-X PUT`:  Indicates that this is an update operation.
*   `"https://192.168.88.1/rest/interface/wireless/wlan-39"`:  API endpoint for `wlan-39`.
*   `-d '{"mac-auth":"mac-address"}'`:  The JSON payload, setting the MAC auth mode to `mac-address`.

**Adding an Allowed MAC Address (through general access lists):**
*   This operation is not directly available as a "MAC server" operation. You would typically manage MAC access through other methods, such as firewall rules or queues. This is outside the scope of this document.

**Error Handling:**

*   A common error would be a `401 Unauthorized` if authentication fails.
*   `400 Bad Request` if the JSON payload is malformed.
*   `500 Internal Server Error` if there are issues on the MikroTik side.
*   Check the router logs for specific error messages.

**Note:**  API calls may be different based on RouterOS version. Always consult the MikroTik API documentation for the correct endpoint and parameters.

## Security Best Practices

*   **MAC Address Filtering is Not Secure:**  MAC addresses are easily spoofed. This should be treated as a basic hurdle and not security.
*   **Use WPA2/3 Encryption:** Always use WPA2 or WPA3 for wireless security.
*   **Strong Router Password:** Protect your router's admin account with a strong password and consider disabling the default admin user.
*   **Regular Software Updates:** Keep your RouterOS up to date for the latest bug and security fixes.
*   **Disable unnecessary services:** Disable any unused services to minimize the attack surface.

## Self Critique and Improvements

*   **Limited Security:** MAC address authentication alone is insufficient for securing a network.
*   **Scalability:** Manually adding many MAC addresses can be tedious. Consider more complex solutions.
*   **Automation:** Can be improved with API scripting for mass device addition and network management.
*   **Error Handling:** The example lacks error checking and reporting.

**Improvements:**
*   **RADIUS for Authentication:** Add integration with RADIUS for real security.
*   **Scripted MAC Addition:** Develop scripts to automate MAC address management.
*   **Monitoring:** Set up alerting on the router for abnormal behavior.

## Detailed Explanations of Topic

MAC server functionality allows the administrator to create a list of MAC addresses that are allowed to connect to a wireless access point. This means that only devices with a MAC address specified in the list will be able to associate with the AP. This process is similar to a simple access control list based on MAC addresses. The MAC address is the hardware address of the client's wireless card.

It provides basic protection against casual unauthorized access attempts, however it can not be considered a strong security measure. Since MAC addresses are easily spoofed, a device can copy the MAC address of an authorized device and gain access to the wireless network.

## Detailed Explanation of Trade-offs

**Trade-offs using MAC-address authentication:**

*   **Complexity:** Easy to setup
*   **Security:** It's a weak form of security.
*   **Administration:** Simple to manage, especially for a small number of devices, but it may become tedious for large networks.
*   **Cost:** No additional costs. Built in functionality.

**Alternatives:**

*   **WPA2/3-PSK:** Easy to configure but shared password, not per-user.
*   **WPA2/3-Enterprise:** More complex to configure with a RADIUS server, but offers better security. This allows per-user credentials.
*   **Hotspot:** Provides a captive portal, useful for public networks, but more complex to setup.

**When to Use MAC-Server Authentication:**
* Testing environments
* Small, isolated networks where convenience is the primary concern.
* Low-security applications.

## Configuration for Specific RouterOS Versions:

The configurations provided are valid for RouterOS version 6.48 and later versions, as mentioned in the question requirements. There are no significant changes related to the `mac-server` configuration that are specific to RouterOS version.

This detailed guide should give you a solid foundation for implementing MAC server functionality in your MikroTik environment. Please ask if you have any further questions or requests.
