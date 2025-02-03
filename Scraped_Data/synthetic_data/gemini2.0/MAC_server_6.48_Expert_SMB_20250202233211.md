## MAC Server

**1. Configuration Scenario and Requirements**

The MAC server feature in RouterOS allows you to manage MAC addresses on your network. You can use it to:

- Assign static IP addresses to devices based on their MAC addresses.
- Control access to your network by allowing or denying access to specific MAC addresses.
- Track and monitor which devices are connected to your network.

**2. Step-by-Step Implementation**

To configure the MAC server, follow these steps:

1. Open WinBox and connect to your MikroTik router.
2. Go to the **IP** menu and select **MAC Server**.
3. Click the **Add** button.
4. In the **MAC Address** field, enter the MAC address of the device you want to manage.
5. In the **IP Address** field, enter the IP address you want to assign to the device.
6. Click the **OK** button.

**3. Complete Configuration Commands**

The following commands can be used to configure the MAC server:

- `/ip mac-server add address=XX:XX:XX:XX:XX:XX interface=ether1 static-arp=yes` - Adds a new MAC server entry with the specified MAC address, interface, and static ARP setting.
- `/ip mac-server remove address=XX:XX:XX:XX:XX:XX` - Removes the MAC server entry with the specified MAC address.
- `/ip mac-server print` - Displays the list of all MAC server entries.

**4. Common Pitfalls and Solutions**

- Make sure that the MAC address you enter is correct. If you enter an incorrect MAC address, the device will not be able to connect to the network.
- Make sure that the IP address you assign to the device is not already in use by another device on the network. If you assign a duplicate IP address, the device will not be able to connect to the network.
- If you are using static ARP, make sure that the MAC address and IP address are correct. If you enter an incorrect MAC address or IP address, the device will not be able to connect to the network.

**5. Verification and Testing Steps**

To verify that the MAC server is working properly, you can:

- Ping the device to see if it responds.
- Check the MAC server table to see if the device's MAC address is listed.
- Use the WinBox MAC Ping tool to test MAC connectivity.

**6. Related Features and Considerations**

The MAC server feature is related to the following features:

- **IP Addressing** - The MAC server uses IP addresses to assign to devices.
- **IP Routing** - The MAC server can be used to control access to your network by allowing or denying access to specific MAC addresses.
- **Firewall** - The MAC server can be used to create firewall rules that allow or deny traffic based on MAC addresses.

**7. MikroTik REST API Examples**

The following REST API examples can be used to manage the MAC server:

- **Add a MAC server entry:**

   ```
   POST /api/ip/mac-server
   {
       "mac-address": "XX:XX:XX:XX:XX:XX",
       "interface": "ether1",
       "static-arp": true
   }
   ```

- **Remove a MAC server entry:**

   ```
   DELETE /api/ip/mac-server/XX:XX:XX:XX:XX:XX
   ```

- **Get all MAC server entries:**

   ```
   GET /api/ip/mac-server
   ```

**8. Other Relevant Topics**

**IP Addressing (IPv4 and IPv6)**

IP addressing is the process of assigning unique identifiers to devices on a network. IPv4 is the most common type of IP address, but IPv6 is becoming more popular.

**IP Pools**

IP pools are groups of IP addresses that are assigned to devices on a network. You can use IP pools to manage the assignment of IP addresses and to ensure that all devices on your network have a unique IP address.

**IP Routing**

IP routing is the process of forwarding packets from one network to another. Routers use routing tables to determine the best path for packets to take.

**IP Settings**

IP settings are the configuration options that are used to configure IP addresses, IP pools, and IP routing on a router.

**RoMON**

RoMON is a monitoring tool that can be used to monitor the performance of your router. RoMON can be used to collect data on a variety of metrics, including CPU usage, memory usage, and traffic statistics.

**WinBox**

WinBox is a graphical user interface (GUI) that can be used to configure MikroTik routers. WinBox provides a variety of tools and features that make it easy to manage your router.

**Certificates**

Certificates are used to secure communications between devices. Certificates can be used to authenticate devices, encrypt traffic, and protect data from eavesdropping.

**PPP AAA**

PPP AAA is a protocol that is used to authenticate and authorize users who are connecting to a network over a PPP connection. PPP AAA can be used to control access to your network and to track user activity.

**RADIUS**

RADIUS is a server that is used to authenticate and authorize users who are connecting to a network. RADIUS can be used to control access to your network and to track user activity.

**User / User groups**

Users and user groups are used to control access to your network. You can create users and user groups to assign different permissions to different users.

**Bridging and Switching**

Bridging and switching are two techniques that are used to connect devices on a network. Bridging is used to connect devices on the same LAN, while switching is used to connect devices on different LANs.

**MACVLAN**

MACVLAN is a technology that allows you to create virtual LANs (VLANs) on a single physical network. MACVLAN can be used to isolate traffic between different VLANs and to improve network security.

**L3 Hardware Offloading**

L3 hardware offloading is a feature that can be used to improve the performance of your router. L3 hardware offloading allows the router to offload some of its processing tasks to a dedicated hardware chip.

**MACsec**

MACsec is a protocol that is used to encrypt traffic between devices on a network. MACsec can be used to protect data from eavesdropping and to improve network security.