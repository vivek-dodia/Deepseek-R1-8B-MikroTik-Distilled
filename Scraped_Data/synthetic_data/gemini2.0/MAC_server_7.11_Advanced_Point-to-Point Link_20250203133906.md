Okay, let's dive deep into configuring a MAC server on MikroTik RouterOS 7.11, focusing on a point-to-point link scenario with the specified subnet and interface.

## Scenario Description

We are setting up a point-to-point wireless link using a MikroTik router. We need to utilize the MAC server functionality on our `wlan-95` interface, operating within the 61.45.138.0/24 subnet. The goal is to allow only specific devices, identified by their MAC addresses, to connect to this wireless interface, thus enhancing security and controlling access to the network. This configuration will be targeted at advanced users comfortable with MikroTik's command-line interface (CLI) and Winbox GUI.

## Implementation Steps

Here's a step-by-step guide to implement the MAC server configuration:

### Step 1: Ensure Interface is Configured

Before enabling the MAC server, ensure that the `wlan-95` interface is properly configured and enabled. This includes setting the wireless mode, SSID, frequency, security profile, and ensuring it is operationally up.

**Pre-Configuration (Example - adjust as needed):**

```mikrotik
/interface wireless print
```

```
Flags: X - disabled, R - running
 0  R name="wlan1" mtu=1500 mac-address=00:11:22:33:44:55 actual-mtu=1500 l2mtu=1600
      max-station-count=2007 arp=enabled interface-type=Atheros AR9300
      mode=ap-bridge ssid="MySSID" frequency=2437 band=2ghz-b/g/n
      channel-width=20/40mhz-Ce country="us" antenna-gain=0
      wps-mode=disabled guard-interval=800ns vlan-id=1 vlan-mode=no-tag
      default-forwarding=yes
```

**Configuration Step:**

If necessary, configure the `wlan-95` interface using CLI or Winbox. For example:

```mikrotik
/interface wireless set wlan1 name=wlan-95
/interface wireless set wlan-95 mode=ap-bridge ssid=MySSID frequency=5200 band=5ghz-a/n/ac country=us
/interface wireless security-profiles add name=my-security mode=dynamic-keys authentication-types=wpa2-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=yoursecurepassword
/interface wireless set wlan-95 security-profile=my-security
/interface wireless enable wlan-95
/interface wireless print
```

**Post-Configuration:**

```
Flags: X - disabled, R - running
 0  R name="wlan-95" mtu=1500 mac-address=00:11:22:33:44:55 actual-mtu=1500 l2mtu=1600
      max-station-count=2007 arp=enabled interface-type=Atheros AR9300
      mode=ap-bridge ssid="MySSID" frequency=5200 band=5ghz-a/n/ac
      channel-width=20/40mhz-Ce country="us" antenna-gain=0
      wps-mode=disabled guard-interval=800ns vlan-id=1 vlan-mode=no-tag
      default-forwarding=yes security-profile=my-security
```

### Step 2: Enable the MAC Server

Enable the MAC server on the `wlan-95` interface.

**Pre-Configuration (Before Enabling MAC Server):**
```mikrotik
/interface wireless mac-server print
```
```
Flags: X - disabled, I - invalid
```

**Configuration Step (Enabling MAC Server):**
```mikrotik
/interface wireless mac-server set enabled=yes interfaces=wlan-95
/interface wireless mac-server print
```
**Post-Configuration (After Enabling MAC Server):**

```mikrotik
Flags: X - disabled, I - invalid
  0   enabled=yes interfaces=wlan-95 mac-address=00:00:00:00:00:00
```

### Step 3: Add Allowed MAC Addresses

Add the MAC addresses of the devices allowed to connect to the `wlan-95` interface. We’ll use `66:AA:BB:CC:DD:EE` and `77:BB:CC:DD:EE:FF` as examples.

**Pre-Configuration:**
```mikrotik
/interface wireless mac-server access-list print
```
```
Flags: X - disabled
```

**Configuration Step (Add Access List entries):**

```mikrotik
/interface wireless mac-server access-list add mac-address=66:AA:BB:CC:DD:EE comment="Device 1"
/interface wireless mac-server access-list add mac-address=77:BB:CC:DD:EE:FF comment="Device 2"
/interface wireless mac-server access-list print
```
**Post-Configuration:**

```mikrotik
Flags: X - disabled
 0   mac-address=66:AA:BB:CC:DD:EE comment="Device 1"
 1   mac-address=77:BB:CC:DD:EE:FF comment="Device 2"
```

### Step 4: Configure IP Address

Assign an IP address to the `wlan-95` interface from the 61.45.138.0/24 subnet. Example: 61.45.138.1/24

**Pre-Configuration (Before Setting IP):**

```mikrotik
/ip address print
```
```
Flags: X - disabled, I - invalid, D - dynamic
```

**Configuration Step (Assign IP address):**
```mikrotik
/ip address add address=61.45.138.1/24 interface=wlan-95
/ip address print
```
**Post-Configuration (After Setting IP):**
```mikrotik
Flags: X - disabled, I - invalid, D - dynamic
 0   address=61.45.138.1/24 network=61.45.138.0 interface=wlan-95 actual-interface=wlan-95
```

### Step 5: (Optional) Disable Default Forwarding

For a point-to-point link, it may be prudent to disable default forwarding to limit traffic between connected interfaces.

**Pre-Configuration (Before disabling Forwarding):**

```mikrotik
/interface wireless print
```
```
Flags: X - disabled, R - running
 0  R name="wlan-95" mtu=1500 mac-address=00:11:22:33:44:55 actual-mtu=1500 l2mtu=1600
      max-station-count=2007 arp=enabled interface-type=Atheros AR9300
      mode=ap-bridge ssid="MySSID" frequency=5200 band=5ghz-a/n/ac
      channel-width=20/40mhz-Ce country="us" antenna-gain=0
      wps-mode=disabled guard-interval=800ns vlan-id=1 vlan-mode=no-tag
      default-forwarding=yes security-profile=my-security
```
**Configuration Step:**
```mikrotik
/interface wireless set wlan-95 default-forwarding=no
/interface wireless print
```

**Post-Configuration:**

```mikrotik
Flags: X - disabled, R - running
 0  R name="wlan-95" mtu=1500 mac-address=00:11:22:33:44:55 actual-mtu=1500 l2mtu=1600
      max-station-count=2007 arp=enabled interface-type=Atheros AR9300
      mode=ap-bridge ssid="MySSID" frequency=5200 band=5ghz-a/n/ac
      channel-width=20/40mhz-Ce country="us" antenna-gain=0
      wps-mode=disabled guard-interval=800ns vlan-id=1 vlan-mode=no-tag
      default-forwarding=no security-profile=my-security
```
## Complete Configuration Commands

Here are the complete CLI commands to implement the setup:

```mikrotik
# Configure Wireless interface (Adjust to match your needs)
/interface wireless set wlan1 name=wlan-95
/interface wireless set wlan-95 mode=ap-bridge ssid=MySSID frequency=5200 band=5ghz-a/n/ac country=us
/interface wireless security-profiles add name=my-security mode=dynamic-keys authentication-types=wpa2-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=yoursecurepassword
/interface wireless set wlan-95 security-profile=my-security
/interface wireless enable wlan-95

# Enable MAC Server
/interface wireless mac-server set enabled=yes interfaces=wlan-95

# Add allowed MAC addresses (Adjust to match your needs)
/interface wireless mac-server access-list add mac-address=66:AA:BB:CC:DD:EE comment="Device 1"
/interface wireless mac-server access-list add mac-address=77:BB:CC:DD:EE:FF comment="Device 2"

# Assign IP Address
/ip address add address=61.45.138.1/24 interface=wlan-95

# (Optional) Disable default forwarding
/interface wireless set wlan-95 default-forwarding=no
```

## Common Pitfalls and Solutions

*   **Incorrect MAC Addresses:** Double-check the MAC addresses entered in the access list. A single typo can prevent devices from connecting.
    *   **Solution:** Verify MAC addresses using `ipconfig /all` (Windows), `ifconfig` (Linux/macOS), or the device's interface settings.
*   **MAC Server Not Enabled:** Ensure the MAC server is enabled for the specific interface.
    *   **Solution:**  Check `/interface wireless mac-server print` to verify `enabled=yes` and that the correct `interfaces` are specified.
*   **Wireless Settings Mismatch:** Ensure wireless settings on the client device match the router configuration (SSID, security profile, key).
    *   **Solution:** Verify the client's Wi-Fi settings.
*   **No IP address assigned to interface:** Ensure that there is an IP address bound to the interface
    *   **Solution:** Use `/ip address print`, and verify that the interface has an IP address

## Verification and Testing Steps

1.  **Device Connection:** Attempt to connect a device with a MAC address *not* in the access list. The device should *fail* to connect.
2.  **Authorized Device Connection:** Connect a device with a MAC address *in* the access list.  The device should successfully connect.
3.  **Ping Test:**  After a successful connection, ping the router's IP address (`61.45.138.1`) from the connected client.
    *   **Example (From Client):** `ping 61.45.138.1`
4.  **Torch:** Use the MikroTik `torch` tool on the router to view network traffic on the `wlan-95` interface.
    *   **Example (On MikroTik Router):** `/tool torch interface=wlan-95`
5.  **Monitoring:** use the `/interface wireless registration-table print` to check connected client information and Signal Strength, and other metrics.

## Related Features and Considerations

*   **Wireless Security Profile:** The MAC server operates in conjunction with the security profile, so make sure your wireless security is setup correctly (WPA2/WPA3, etc).
*   **Wireless Access List:** The MAC Server Access list should only be used if you are wanting to block devices.
*   **Firewall:** Use MikroTik firewall rules to enhance security (e.g., limiting access to specific ports or services) after the MAC authentication.
*   **DHCP:** If using DHCP, configure it on the interface after setting up the IP address
*   **Bandwidth Limiting:** Configure QoS rules if necessary, using the MAC addresses to restrict each device.
*  **Hotspot Integration**: Use the MAC server for hotspot environments, for instance, in conjunction with user management tools.

## MikroTik REST API Examples (if applicable)

Since we are configuring core RouterOS functionality, direct REST API manipulation may be less common. However, it is helpful to show how to add an entry to the MAC server access list.

**Example REST API request:**
*   **Endpoint**: `/interface/wireless/mac-server/access-list`
*   **Method:** POST
*   **Payload:** (JSON)
```json
{
    "mac-address": "88:CC:DD:EE:FF:00",
    "comment": "Device 3 via API"
}
```
**Expected Response**
A successful response will usually be an empty array, which is an acknowledgement of the completed request. For instance:
```json
[]
```

**Example CLI Equivalent:**
```mikrotik
/interface wireless mac-server access-list add mac-address=88:CC:DD:EE:FF:00 comment="Device 3 via API"
```

**Error Handling**
If for instance, the `mac-address` value is not a valid mac address, the api will return something like:
```json
{
    "message": "invalid mac address",
    "code": "invalid-value"
}
```
**Note:** Before using the API, make sure you have enabled and configured API access on your MikroTik router (under `/ip service`).

## Security Best Practices

*   **Limit API Access:** Restrict access to the MikroTik API using firewall rules.
*   **Strong Passwords:** Use strong, unique passwords for all access methods.
*   **Regularly Audit:** Review access lists and configurations regularly for potential security vulnerabilities.
*   **Keep RouterOS Updated:** Apply the latest updates to address security concerns and performance issues.
*   **Disable Unnecessary Services:** Disable any services not required for your setup (e.g., SNMP, FTP).
*   **Firewall Rules**: Ensure there are firewall rules to restrict access to the router from external networks, if the wireless interface is not part of an internal, secure network.

## Self Critique and Improvements

This configuration is generally sound for the stated scenario, but here are some possible improvements:

*   **Automation:** Implement scripts to add/remove MAC addresses via a management interface, for easier administrative overhead.
*   **Centralized Management:** Consider using MikroTik's CAPsMAN feature for managing multiple APs (if you have a larger network).
*   **Integration with AAA Servers:** Integrate with RADIUS for more robust access control and logging.
*   **Logging:** Enable adequate logging to track connections, disconnections and possible security breaches.
*   **Monitor CPU usage**: When adding a lot of entries to the access list, or when the server needs to process a lot of requests, observe the CPU usage to make sure there is not a bottleneck.

## Detailed Explanations of Topic

A MAC server in MikroTik RouterOS allows the device to only permit connections from devices with MAC addresses listed in its access list, for specific interfaces. It's a method of providing basic network access control at the data link layer (layer 2). MAC addresses are unique hardware identifiers for each network interface. A MAC Server, on the other hand, uses a list of accepted MAC addresses, and denies connection to any device that is not part of it. By utilizing the MAC server, you are adding an extra layer of security to prevent unauthorized devices from connecting. This is mostly used in wireless networks, but can also be used on other interface types like ethernet or VLANs.

## Detailed Explanation of Trade-offs

*   **MAC Filtering vs. WPA2/WPA3:** MAC filtering alone isn't a substitute for strong wireless encryption. It is simple to spoof MAC addresses, so it is best to use both methods. While MAC filtering can help with access control, it's not a strong security method against determined attackers.
*   **Dynamic vs. Static MAC List:** A static MAC list requires manual updates each time a device needs to join. A dynamic list, which requires integration with a separate server like RADIUS, can help alleviate this burden, but with higher overhead.
*   **Centralized vs. Local Configuration:** For small networks, configuring access lists manually on each device is acceptable. But for larger environments, using CAPsMAN or a centralized management system would be much more beneficial.
*   **Overhead and Performance:** The access list lookup increases with the number of allowed MAC addresses. Too many entries might slightly impact performance, especially on lower-end devices. Monitor CPU and memory usage if you have a very large access list.

## Configuration for Specific RouterOS Versions:

The commands used in this documentation apply to RouterOS 7.11, as well as RouterOS 6.48 and other 7.x versions. There may be some slight differences in the output, but the underlying concepts and commands remain largely the same. Always refer to MikroTik's official documentation for specific version differences and updates.

This detailed explanation provides a solid foundation for configuring the MAC server on MikroTik, including a practical real-world example, security best practices, and explanations of relevant features. Always tailor the configuration to your specific needs and perform thorough testing before deploying it in a production environment.
