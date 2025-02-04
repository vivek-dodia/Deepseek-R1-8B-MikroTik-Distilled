Okay, let's craft some detailed expert-level documentation for a point-to-point link setup on a MikroTik router using RouterOS 7.11, focusing specifically on the configuration of a wireless interface named `wlan-11` within a 10.95.198.0/24 subnet and with a heavy emphasis on WinBox usage.

## Scenario Description:

This scenario describes configuring a MikroTik router as one end of a point-to-point wireless link. The specific objective is to configure the wireless interface `wlan-11` with the proper IP address within the 10.95.198.0/24 subnet, ensuring network connectivity and accessibility. This setup would typically be used to bridge two physical locations wirelessly, creating a single network segment. This configuration does *not* include routing between networks, and assumes that the wireless bridge will be transparent at L2. This is common in situations where a single network needs to be extended between buildings.

## Implementation Steps:

Here's a step-by-step guide with explanations, CLI/WinBox instructions, before/after state, and expected effects:

**Step 1: Initial System State Check**

*   **Explanation:** Before making any changes, it's crucial to check the current interface configuration. This helps identify existing settings and avoid potential conflicts.
*   **WinBox:** In WinBox, navigate to "Interfaces" and locate the interface named `wlan-11`. Note its current state (enabled/disabled, IP, MAC address).
*   **CLI (before):**
    ```mikrotik
    /interface print where name="wlan-11"
    ```
    **Expected Output (example):**
    ```
    Flags: X - disabled, R - running
    0  R  name="wlan-11" type=wlan mac-address=XX:XX:XX:XX:XX:XX mtu=1500 l2mtu=1600
         keepalive-frames=disabled disabled=no
    ```
*   **Effect:** Allows you to understand the current configuration. You can see if the interface is enabled and its MAC address.

**Step 2: Enable and Configure the Wireless Interface**

*   **Explanation:**  First, enable the interface if it is disabled. Then, ensure the wireless mode and frequencies are set up for the point-to-point link using appropriate frequency and band settings. It is assumed that these values are already known. This may require radio tuning on either side of the link.
*   **WinBox:** Navigate to "Interfaces" > "wlan-11". Ensure the "Enabled" checkbox is ticked. Then click on the "Wireless" tab. Set the "Mode" to `bridge` if not already set. In the "Frequency" box, set the correct frequency based on your area and regulatory compliance. In the "Band" box set the required band. Finally, set the SSID. For a point-to-point link it is also highly recommended to set the wireless security under the "Wireless" tab, and select an appropriate protocol.

*   **CLI (before):** See the output of Step 1
*  **CLI (during):**
    ```mikrotik
    /interface wireless set wlan-11 disabled=no mode=bridge band=5ghz frequency=5180 ssid=my-point-to-point-ssid security-profile=my-security-profile
    ```
    **Explanation:**
    * `disabled=no`: Enables the interface.
    * `mode=bridge`: Sets the interface to bridge mode for point to point links, allowing layer-2 connectivity
    * `band=5ghz`: Sets the wireless band (example). Choose an appropriate band
    * `frequency=5180`: Sets the wireless frequency (example). Choose the correct frequency according to your regulation and area.
    * `ssid=my-point-to-point-ssid`: Sets the SSID name (example, change to your SSID).
	* `security-profile=my-security-profile`: Sets the wireless security profile (example, change to your security profile. Ensure the other side of the link has an identical security profile)

*   **CLI (after):**
    ```mikrotik
    /interface wireless print where name="wlan-11"
    ```
    **Expected Output (example):**
    ```
    Flags: X - disabled, R - running
    0  R  name="wlan-11" mtu=1500 l2mtu=1600 mac-address=XX:XX:XX:XX:XX:XX
         arp=enabled  band=5ghz channel-width=20/40/80mhz-XXXX ssid="my-point-to-point-ssid"
         frequency=5180 mode=bridge disabled=no
         security-profile=my-security-profile
    ```
*   **Effect:** The wireless interface is now enabled, and ready to be configured with an IP address.

**Step 3: Configure IP Address on `wlan-11`**

*   **Explanation:**  Assign an IP address to the `wlan-11` interface from the 10.95.198.0/24 subnet, ensuring the correct netmask.
*   **WinBox:** Navigate to "IP" > "Addresses". Click on the "+" button. Enter the address `10.95.198.1/24` and choose `wlan-11` as the interface. Press "Apply" then "OK". Note that on the other side of the point-to-point link, you *cannot* use the same address. This is a common mistake that causes routing failures. Typically, the next available address would be used, e.g. 10.95.198.2/24.
*   **CLI (before):**
    ```mikrotik
    /ip address print
    ```
    **Expected Output (example):**
    ```
    #   ADDRESS            NETWORK         INTERFACE
    ```
*   **CLI (during):**
    ```mikrotik
    /ip address add address=10.95.198.1/24 interface=wlan-11
    ```
    **Explanation:**
    *   `address=10.95.198.1/24`: Sets the IP address to 10.95.198.1 with a /24 netmask.
    *   `interface=wlan-11`: Assigns this IP address to the `wlan-11` interface.
*   **CLI (after):**
    ```mikrotik
     /ip address print
    ```
    **Expected Output (example):**
    ```
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS            NETWORK         INTERFACE
    0   10.95.198.1/24      10.95.198.0     wlan-11
    ```
*   **Effect:** The `wlan-11` interface now has a valid IP address within the designated subnet.

**Step 4: Check Wireless Connection Status (optional, but very recommended)**

*   **Explanation:** Verify the wireless connection with the paired device on the other end of the point-to-point link. If the connection is not working, then IP connectivity will not work. Check the scan list.
*   **WinBox:** In "Wireless" tab for the wlan-11 interface, you will see under the "Status" area, the current state. You should see a "connected to AP", which specifies the other side of the link.
*   **CLI (during):**
    ```mikrotik
    /interface wireless registration-table print
    ```
    **Expected Output (example, if connected):**
    ```
    #  INTERFACE    MAC-ADDRESS       AP-MAC          SIGNAL    TX-RATE     RX-RATE    Uptime
    0  wlan-11      XX:XX:XX:XX:XX:XX  YY:YY:YY:YY:YY:YY  -56dBm   433.3Mbps    433.3Mbps  00:05:01
    ```
*   **Effect:** You can see if the connection is made, the signal strength and other connection metrics.

## Complete Configuration Commands:

```mikrotik
# Enable the wlan-11 Interface, and set the wireless parameters (change as needed)
/interface wireless set wlan-11 disabled=no mode=bridge band=5ghz frequency=5180 ssid=my-point-to-point-ssid security-profile=my-security-profile

# Assign an IP address to the wlan-11 interface
/ip address add address=10.95.198.1/24 interface=wlan-11
```

## Common Pitfalls and Solutions:

*   **Wireless Connection Issues:**
    *   **Problem:** Unable to connect or intermittent connections.
    *   **Solution:** Verify the frequency, band, and SSID match on both devices. Ensure the security settings (password, encryption) are identical. Check the signal strength and potential interference from other devices using the same radio bands. You can use `/interface wireless scan` to detect other networks.
*   **IP Address Conflicts:**
    *   **Problem:** IP address is already in use, creating routing conflicts.
    *   **Solution:** Ensure no other devices or interfaces use the same IP address.
*   **Interface Disabled:**
    *   **Problem:** The wireless interface is not enabled, or has been accidently disabled.
    *   **Solution:**  Double-check that `disabled=no` on the `wlan-11` interface. Check to see if the interface is accidentally administratively disabled.
*   **Security Mismatches:**
    *   **Problem:** Wireless connection fails due to wrong security settings or keys.
    *   **Solution:** Ensure both devices are using the same security profile, encryption protocol, and password.
*  **MTU Mismatch**
   * **Problem:** Packet fragmentation and throughput loss.
   * **Solution:** Check if both sides of the link have the same MTU configured.

## Verification and Testing Steps:

1.  **Ping Test:** Ping the IP address of the other end of the point-to-point link on the other router.
    ```mikrotik
    /ping 10.95.198.2
    ```
    *   **Expected Output:**  Successful pings with minimal latency.
2.  **Traceroute:** Use traceroute to verify the network path.
    ```mikrotik
    /tool traceroute 10.95.198.2
    ```
    *   **Expected Output:** Shows one hop to the other side of the bridge.
3.  **Wireless Status:** Use `/interface wireless registration-table print` to check connection details as noted above.
4.  **Torch Tool:** Use `/tool torch interface=wlan-11` to view live traffic on the interface and diagnose potential issues.

## Related Features and Considerations:

*   **Wireless Security:** Always set up strong wireless security using WPA2 or WPA3 encryption and a complex password.
*   **Bandwidth Management:** Implement QoS rules to control and prioritize traffic.
*   **Monitoring:** Use The Dude or similar tools to monitor the network link's performance.
*   **NTP Client:** Ensure the router time is synchronized with an NTP server.
*  **Link Layer Discovery (LLDP):** Enable LLDP to easily identify connected devices, or troubleshoot any mis-configurations.
* **Wireless Naming Convention**: It may be better to create a specific naming convention (like "wlan-ptp") to clearly denote the purpose of the wireless interface.

## MikroTik REST API Examples:

Here's an example of setting the interface's IP via the MikroTik REST API. Note that you will need to setup REST API access before this will work.
```bash
# Example setting IP Address for wlan-11 using API
# API Endpoint: /ip/address
# HTTP method : POST
curl -k -u user:password -H "Content-Type: application/json" -X POST \
-d '{
      "address": "10.95.198.1/24",
      "interface": "wlan-11"
    }' \
https://<your-mikrotik-ip>/rest/ip/address
```

```json
# Expected Successful Response (200 OK)
{
    "message": "added",
    "id": "*1"  # ID of the created rule, unique to your device.
}
```

```bash
# Example enabling wireless interface using API
# API Endpoint: /interface/wireless
# HTTP method : PUT
curl -k -u user:password -H "Content-Type: application/json" -X PUT \
-d '{
      ".id": "*0", # The id number of the wlan-11 interface. Check the "Interfaces" section in WinBox. This can change if you add/remove devices.
       "disabled": false
    }' \
https://<your-mikrotik-ip>/rest/interface/wireless
```

```json
# Expected Successful Response (200 OK)
{
  "message": "updated"
}
```

**Parameter Descriptions:**
*   `address` - String: The IP address with the subnet mask in CIDR notation.
*   `interface` - String: The name of the interface to apply the address.
*   `.id` - String: The unique ID of the interface to be modified. The first time you configure the interface, it will be "*0". You can use WinBox to determine the id number of any interface by looking at the interface configuration page.
*  `disabled` - Boolean: Whether to disable the wireless interface, `true` or `false`.
*   **Error Handling:** A failure will return an error message in the response body with an error code. Example: `{"error": "not found"}`. You should validate the response status code and the JSON response for errors.

## Security Best Practices

*   **Secure Wireless:** Use strong WPA2/WPA3 with a strong key.
*   **Disable Unnecessary Services:** Turn off unused features such as API access and unsecure protocols.
*   **Change Default Credentials:** Do not use default usernames and passwords.
*   **Firewall Rules:** Apply firewall rules to restrict access to the router and to protect against malicious attacks.
*   **RouterOS Updates:**  Always keep your RouterOS updated to the latest version to mitigate security risks.
*  **Disable Discovery Protocols:** Disable unecessary broadcast and discovery protocols. These include `cdp`, `lldp`, and `mndp`. These protocols are often used for network management, however can be exploited by malicious actors.

## Self Critique and Improvements

*   **Dynamic IP Assignment:** The current configuration uses static IP assignment. DHCP could be added if DHCP server access is needed over the wireless link. DHCP servers can also be used to dynamically provide IP addresses, when static addresses are not needed.
*   **Omitted Routing**: This configuration omits L3 routing. If routing is needed, a routing table must be configured.
*   **Advanced Wireless:** The wireless settings could be further optimized with specific channel selections, band configurations and other wireless features specific to MikroTik.
*   **Backup Configuration:** The configuration does not include a backup process. Regularly backup the configuration via the `system backup` command.

## Detailed Explanations of Topic

**WinBox** is the most common method of managing MikroTik routers, and is designed as a user-friendly graphical interface. It allows for full configuration of RouterOS. It connects using MikroTik's proprietary protocol and is available for Windows, Mac, Linux and Web (via webfig). It provides access to virtually all RouterOS features, and shows a real-time representation of the router's internal state. The WinBox program was designed to give full access to a RouterOS device without requiring CLI access. This makes it easier to get started with RouterOS devices for new users. While the GUI interface of WinBox may appear basic, it is a very powerful tool for device management.

## Detailed Explanation of Trade-offs

*   **Static IP vs Dynamic IP:** Static IP addresses offer predictable access and simplifies the setup of point to point links, but require manual configuration and can be more challenging to manage. Dynamic IP via DHCP simplifies configuration (particularly if there are many devices), but can be less predictable, and is more difficult to diagnose. Static IP configuration is better for this use case since it can be more easily diagnosed and managed.
* **Bridge Mode vs. Router Mode**: This configuration uses `bridge` mode, which passes L2 traffic between the two sides of the wireless link. This is often ideal for point-to-point links as it makes one large L2 network. When routing is needed between networks the `router` mode needs to be used. When routing between networks, you will likely need to configure additional network elements such as firewalls and NAT.
*   **Wireless Band:** 2.4 GHz is more readily available, but has higher interference and less bandwidth. 5 GHz is less susceptible to interference and has more bandwidth available, but has more limited range. The correct choice of frequency is dependent on the situation, and may be dependent on regulatory restrictions in the country where you are using the equipment.
*   **Security Protocol:** WEP is insecure and should not be used. WPA2 is the minimum security requirement for a secure link. WPA3 is the most secure protocol but will also provide the lowest throughput because of its increased overhead.
*   **Frequency Selection:** Selecting non-overlapping channels helps mitigate interference, increasing stability and bandwidth for the link. Using wireless scan tools to select the frequency with the lowest interference.
*   **MTU Size:** Setting too high of a MTU can lead to dropped fragmented packets. Setting it too low can lead to unnecessary overhead. For this configuration, using the default MTU is recommended unless you need to specify the MTU based on other parts of your network.
*   **Wireless Transmit Power:** Setting a high transmit power can lead to interference if the signal is too strong, leading to connectivity issues. Using lower transmit powers where possible can improve stability.

## Configuration for Specific RouterOS Versions:
This documentation and configuration is designed specifically for RouterOS 7.11 (or RouterOS 6.48 or 7.x). Some of the commands or features may be unavailable or behave differently in older RouterOS versions. Any of the listed CLI commands or API calls will be functional on version 7.11.

This concludes the detailed documentation for configuring a MikroTik point-to-point wireless link using WinBox, a 10.95.198.0/24 subnet, and the `wlan-11` interface. Remember to adjust values, especially IP addresses and security settings, to match your network environment.
