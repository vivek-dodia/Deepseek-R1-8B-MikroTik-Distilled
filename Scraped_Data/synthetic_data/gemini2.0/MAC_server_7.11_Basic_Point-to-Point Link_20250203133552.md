Okay, let's dive into creating a comprehensive documentation for a MikroTik MAC Server setup within the context you've provided.

## Scenario Description:

This scenario focuses on configuring a MikroTik router to act as a MAC server on a specific VLAN interface. The MAC server will respond to MAC address-based requests, typically used for initial network access or device identification. The network is a point-to-point link using VLAN 73 with subnet 176.252.253.0/24. This setup is suitable for a range of environments, from SOHO to small business networks, or even as part of a larger ISP infrastructure.

## Implementation Steps:

Here's a step-by-step guide to configuring the MAC server on your MikroTik router:

### **Step 1: Ensure VLAN Interface is Configured**

*   **Before:** Verify that your `vlan-73` interface exists, has the correct ID (73) and is active. If it does not exist, create it. We're assuming it's already created and correctly tagged/untagged on the appropriate physical interface.
*   **Why:** The MAC server needs to listen on a specific interface.
*   **CLI Example (Check existing configuration):**
    ```mikrotik
    /interface vlan print
    ```
    **Output Example (assuming it's configured):**
    ```
    Flags: X - disabled, R - running
     #    NAME       MTU   MAC-ADDRESS      VLAN-ID INTERFACE
     0  R vlan-73     1500  00:11:22:33:44:55   73     ether1
    ```
*   **CLI Example (Create VLAN interface, if it does not exist):**
    ```mikrotik
    /interface vlan add name=vlan-73 vlan-id=73 interface=ether1
    ```
*   **Winbox GUI:**
    1.  Go to `Interfaces` -> `VLAN` tab.
    2.  If the `vlan-73` interface exists, ensure the VLAN ID (73) is correct and that it is bound to the correct physical interface. If not, create it by pressing the "+" button.
    3.  Set the Name to `vlan-73`, VLAN ID to `73` and set the Interface to the appropriate physical interface.
    4.  Click `Apply`.

### **Step 2: Configure the IP Address on the VLAN interface.**

*   **Before:** The interface does not have an IP address in the target subnet.
*   **Why:** For the MAC Server to function it needs to be able to communicate on the network.
*  **CLI Example (Configuration):**
    ```mikrotik
    /ip address add address=176.252.253.1/24 interface=vlan-73
    ```
    **Output (verify IP):**
    ```mikrotik
    /ip address print
    ```
    ```
    Flags: X - disabled, I - invalid, D - dynamic
     #   ADDRESS            NETWORK         INTERFACE
     0   176.252.253.1/24   176.252.253.0   vlan-73
    ```
*   **Winbox GUI:**
    1.  Go to `IP` -> `Addresses`.
    2.  Add a new address: Set the Address to `176.252.253.1/24`, select the Interface `vlan-73`.
    3.  Click `Apply`.

### **Step 3: Enable and Configure the MAC Server**

*   **Before:** The MAC server is disabled.
*   **Why:**  The MAC server needs to be explicitly enabled and configured to be active on your interface.
*   **CLI Example (Enable and configure):**
    ```mikrotik
    /tool mac-server set enabled=yes interface=vlan-73
    ```
*   **CLI Example (Verify Configuration):**
    ```mikrotik
    /tool mac-server print
    ```
    **Output:**
    ```
    enabled: yes
    interfaces: vlan-73
    allowed-address-list:
    ```
*   **Winbox GUI:**
    1.  Go to `Tools` -> `MAC Server`.
    2.  Check the `Enabled` checkbox.
    3.  Under the `Interfaces` section, select `vlan-73`.
    4.  Click `Apply`.

### **Step 4: Configure Allowed MAC Addresses (Optional)**

*   **Before:** No MAC address filtering is in place.
*   **Why:** Limiting which MAC addresses the server will respond to can provide an added layer of security or control.
*   **CLI Example (Allow specific MAC addresses):**
    ```mikrotik
    /tool mac-server set allowed-address-list=00:AA:BB:CC:DD:EE,00:11:22:33:44:55
    ```
*  **CLI Example (Verify Configuration):**
   ```mikrotik
   /tool mac-server print
   ```
   **Output:**
   ```
    enabled: yes
    interfaces: vlan-73
    allowed-address-list: 00:AA:BB:CC:DD:EE,00:11:22:33:44:55
   ```
*   **Winbox GUI:**
    1.  In the `MAC Server` window, locate the `Allowed Address List` text box.
    2.  Enter the comma separated MAC address list you want to allow.
    3.  Click `Apply`.

## Complete Configuration Commands:

Here's the complete set of commands to implement the described setup:

```mikrotik
/interface vlan
add name=vlan-73 vlan-id=73 interface=ether1 #adjust interface as needed

/ip address
add address=176.252.253.1/24 interface=vlan-73

/tool mac-server
set enabled=yes interface=vlan-73 allowed-address-list=00:AA:BB:CC:DD:EE,00:11:22:33:44:55 #optional address list
```

**Parameters Explanation Table:**

| Command Parameter              | Purpose                                                                      | Values                                      |
|--------------------------------|------------------------------------------------------------------------------|---------------------------------------------|
| `interface vlan add name`     | Name of the new VLAN interface.                                              | String, e.g., `vlan-73`                       |
| `interface vlan add vlan-id`   | VLAN Tag ID                                                                | Number, e.g., `73`                          |
| `interface vlan add interface`| Physical interface VLAN is created on                                       | Existing interface name, e.g. `ether1`       |
| `ip address add address`      | IPv4 address with CIDR mask.                                                 | IP/Mask format, e.g., `176.252.253.1/24`      |
| `ip address add interface`    | Interface the IP address will be assigned to.                                | Existing interface name, e.g., `vlan-73`     |
| `tool mac-server set enabled` | Enables/disables the MAC server functionality.                               | `yes` or `no`                               |
| `tool mac-server set interface`| Interface(s) the server will listen on.                                       | Comma-separated list, e.g., `vlan-73`         |
| `tool mac-server set allowed-address-list`| Comma separated list of MAC Addresses that the server will respond to. | Comma separated MAC addresses, e.g `00:AA:BB:CC:DD:EE,00:11:22:33:44:55` |

**Notes:**
*   Replace `ether1` with the interface that carries your VLAN tag.
*   If the address list is not set, all MAC address requests will be responded to.

## Common Pitfalls and Solutions:

*   **Problem:** MAC Server not responding.
    *   **Solution:**
        *   Verify `enabled` flag is set to `yes`.
        *   Double-check the interface in `tool mac-server` matches the VLAN interface in `/interface vlan`.
        *   Make sure the device sending MAC requests is actually using that interface.
        *   Check if a firewall is blocking MAC server traffic. (MAC servers send replies on Layer 2)
        *   If an allowed list is enabled, ensure the MAC is on that list, or remove the list for basic testing.
*   **Problem:** Incorrect VLAN ID or interface.
    *   **Solution:** Use `/interface vlan print` to verify ID and interface. Adjust as necessary.
*   **Problem:** Firewall Rules Blocking ARP Requests/Responses
    *   **Solution:** Although most ARP traffic is done before the firewall, certain configurations may cause interference.
        *  Review and adjust firewall rules if required. ARP is a Layer 2 protocol, but some configurations may cause this traffic to be routed.
*   **Problem:** Resource issues if too many concurrent requests.
    *   **Solution:** Monitor CPU and memory via `/system resource print`. If this is a problem, use `allowed-address-list` to reduce the scope of MAC Server activity, or upgrade hardware.

## Verification and Testing Steps:

1.  **Use Torch on the Interface:**
    ```mikrotik
    /tool torch interface=vlan-73 duration=1m
    ```
    * Look for traffic that indicates the MAC server is being requested, you will see packets with the destination MAC being the broadcast address, and the source address being the device that is looking for the MAC Server.
    * You will see the MikroTik responding with packets that have the destination MAC being the MAC address of the requesting device.
    * Look for ARP requests (if they are ARP requests) to the server address `176.252.253.1`.
2.  **Check the MAC Server List:**
    ```mikrotik
     /tool mac-server print
    ```
    * Ensure the configuration is as expected.
3. **Use a test device.**
    * Set the IP configuration on the test device to the same subnet, and try to ping the MikroTik.

## Related Features and Considerations:

*   **DHCP Server:** The MAC Server is often used in conjunction with a DHCP server, typically to assign IP addresses to newly connected devices after the initial access has been granted.
*   **RADIUS/Authentication:** For more advanced scenarios, consider integration with a RADIUS server for authentication of MAC addresses and for other purposes.
*   **VLAN Trunking:** The configuration can be extended to multiple VLANs by creating additional `vlan-7x` interfaces and adding them to the mac server.
*   **Bridge Interfaces:** The VLAN interfaces can be assigned to a bridge, or the physical interfaces can be assigned to a bridge, and the VLAN tags configured on the bridge.
*   **MAC-Telnet:** MikroTik uses a MAC-Telnet server, which uses the MAC Server to be able to connect to the device before the IP address is configured.

## MikroTik REST API Examples:

Here are some examples using the MikroTik REST API. You will need to first configure the API access on your router. These can be run from a tool such as curl, postman or any similar API tool.

**Example: Enable MAC Server and Set Interface:**

*   **Endpoint:** `/tool/mac-server`
*   **Method:** `PATCH`
*   **Request JSON Payload:**
    ```json
    {
      "enabled": true,
      "interfaces": "vlan-73"
    }
    ```
*   **Expected Response:** `200 OK`, The response body will include the updated MAC Server settings.

**Example: View Current MAC Server Settings**

*   **Endpoint:** `/tool/mac-server`
*   **Method:** `GET`
*   **Expected Response:**
    ```json
     {
      ".id": "*",
      "enabled": true,
      "interfaces": "vlan-73",
      "allowed-address-list": ""
    }
    ```

**Error Handling Example:**

If an error arises, such as providing the wrong interface, the HTTP response code will be other than `200`, and include an error message in the body. Check the returned error message for debugging purposes.

## Security Best Practices:

*   **`allowed-address-list`:**  Limit allowed MAC addresses if possible for stronger security, to prevent rogue devices from misusing the MAC server or gaining unauthorized access.
*   **Monitor Logs:** Check logs frequently (`/log print`) for any suspicious activity.
*   **Password Security:** Ensure a strong password is used to access the router, even if using physical access.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version for security patches.
*   **Firewall:** Be sure that the firewall is correctly configured to prevent external access to the MAC Server. MAC Servers are typically used on a Layer-2 basis, so no IP access should be required.
* **MAC server does not offer any access to the router or network directly:** It can be seen as a "bootstrap" configuration tool, not an end-user or server access mechanism.

## Self Critique and Improvements:

*   **Improvement:** While this covers a basic setup, advanced configurations could include integrating with RADIUS for authentication and authorization. This would provide more control over the devices that are granted access.
*   **Improvement:** Adding logging to keep track of requests would provide greater observability.
*   **Improvement:** The MAC Server can be used for other purposes, such as setting up multiple networks where the IP addressing or VLAN tagging differs on a per device basis. This can greatly increase the complexity of the network, but is possible.
*   **Improvement:** Consider the scalability of the network, the `allowed-address-list` can grow very large in a busy network, which can be inefficient. Using Radius or similar authentication would be a good improvement.
*   **Tradeoff:** Using a `allowed-address-list` increases security, but adds to the maintenance required for adding new devices.

## Detailed Explanations of Topic

The MAC server is a MikroTik feature that listens for specific MAC address requests and responds on Layer 2, without necessarily needing an IP address already configured on the target device. This is useful when you want to configure devices which do not have the IP address, or the network addressing or configuration is not yet known. For example, during device deployment, initial setup, or when using protocols such as MAC-Telnet to remotely access a router that does not have the IP address configured. It differs from other methods of access and control as it works at the MAC address level, on the Layer 2 of the network. This means it is not reliant on IP addressing or routing rules.

## Detailed Explanation of Trade-offs

Here are some trade-offs to consider when using the MAC Server:

*   **Security vs. Convenience:**
    *   Using an `allowed-address-list` makes the network more secure but more difficult to manage, as you have to manually add devices as they appear.
    *   Disabling `allowed-address-list` makes it easy to add new devices, but it does not guarantee any level of security, as anyone can send MAC Address requests and the MAC Server will respond.
*   **Layer 2 vs Layer 3:** The MAC server operates on Layer 2, and does not require IP addressing, so devices will need another method to gain access to the network once the initial connection is done using the MAC Server.
*   **Scalability:** In a large network, MAC servers may suffer from performance issues if they are required to maintain an extremely long list, if too many concurrent requests arrive, or when trying to handle a high volume of MAC address requests. Using RADIUS or a similar authentication server would greatly increase the scalability of a network using this method of access.
*   **Complexity:** Although the configuration is simple, a network which relies heavily on MAC Servers and access may increase the complexity of the network design and management.

## Configuration for Specific RouterOS Versions:

The commands in this documentation are valid for RouterOS 7.11 (and 6.48 and other 7.x versions), but there are no significant differences in MAC Server configuration across RouterOS versions 6.x and 7.x. If you are on a very old version, make sure you are running an updated and supported RouterOS version for best compatibility and security.

Let me know if you have other aspects you'd like to explore or any adjustments you need.
