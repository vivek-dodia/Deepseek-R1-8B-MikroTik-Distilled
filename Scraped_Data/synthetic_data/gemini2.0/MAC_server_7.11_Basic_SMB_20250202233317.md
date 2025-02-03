**Configuration Scenario and Requirements**

The MAC server feature in MikroTik RouterOS allows administrators to manage and control network access based on MAC addresses. This is useful for restricting access to specific devices or limiting the number of devices connected to the network.

**Step-by-Step Implementation**

1. **Enable MAC Server:** Navigate to **IP** > **MAC Server** and click the **+** button.

2. **Configure MAC Server Settings:** Enter a name for the MAC server and select the interface to which it will be applied.

3. **Add MAC Address:** Click the **+** button under the **Allowed MAC Addresses** section. Enter the MAC address of the device you want to allow access to. You can also add multiple MAC addresses by clicking the **Add Other** button.

4. **Set Default Action:** Choose the default action for the MAC server. Options include:

   - **Accept:** Allow all connections.
   - **Deny:** Block all connections.
   - **Reject:** Send a rejection message to the client.

5. **Save Configuration:** Click **Apply** to save the MAC server configuration.

**Complete Configuration Commands**

```
/ip mac-server add name=[MAC Server Name] interface=[Interface]
/ip mac-server set [MAC Server Name] allow-mac-address=[Allowed MAC Address]
/ip mac-server set [MAC Server Name] default-action=[Default Action]
```

**Common Pitfalls and Solutions**

- **MAC Address Not Added:** Ensure that you have entered the correct MAC address and that the interface selected is connected to the network.
- **Default Action Not Set:** Choose a default action to avoid unexpected behavior.
- **Incorrect Interface:** The MAC server must be applied to the correct interface on which devices are connecting.

**Verification and Testing Steps**

1. Connect a device with an allowed MAC address to the network.
2. Verify that the device can access the network.
3. Connect a device with an unauthorized MAC address to the network.
4. Check the MAC server logs to see if the connection was blocked.

**Related Features and Considerations**

- **IP Binding:** Use IP binding to restrict access based on both MAC address and IP address.
- **DHCP Server:** The MAC server can be used in conjunction with the DHCP server to lease IP addresses to authorized devices.
- **Firewall:** The MAC server can be used to create firewall rules based on MAC addresses.

**MikroTik REST API Examples**

**Endpoint:** `/ip/mac-server`

**Request Method:** `GET`

**Example JSON Payload:**

```
{
  "interface": "bridge-local"
}
```

**Expected Response:**

```
[
  {
    "name": "default",
    "interface": "bridge-local",
    "default-action": "accept",
    "allowed-mac-address": []
  }
]
```

**Additional Information**

- IP Addressing
   - IPv4: Uses 32-bit addresses, supports static IP address assignment and DHCP.
   - IPv6: Uses 128-bit addresses, supports static IP address assignment and DHCPv6.
- IP Pools: Allow for assigning IP addresses from a dedicated range.
- IP Routing: Determines how packets are forwarded between interfaces.
- IP Settings: Configure global IP parameters, such as TCP/IP stack settings.
- RoMON: Remote monitoring and management tool.
- WinBox: Windows-based GUI for managing RouterOS devices.
- Certificates: Manage SSL/TLS certificates for secure communication.
- PPP AAA: Authentication, authorization, and accounting for PPP connections.
- RADIUS: Centralized authentication and authorization server.
- User / User Groups: Create and manage user accounts and groups for access control.
- Bridging and Switching: Create and manage logical and physical bridges and switches.
- MACVLAN: Assign multiple MAC addresses to a single physical interface.
- L3 Hardware Offloading: Offload routing and switching tasks to the router's hardware.
- MACsec: Secure MAC addresses to protect against spoofing and other attacks.
- Quality of Service: Prioritize network traffic and ensure performance for critical applications.
- Switch Chip Features: Manage advanced features of MikroTik switch chips, such as VLANs and port mirroring.
- VLAN: Create and manage virtual LANs to segment the network.
- VXLAN: Tunnel Ethernet frames over IP networks.
- Firewall and Quality of Service (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP): Comprehensive firewall and QoS features for network security and performance.
- IP Services (DHCP, DNS, SOCKS, Proxy): Provide essential IP services for network functionality.
- High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples): Ensure network uptime and redundancy.
- Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application): Support for mobile networking and connectivity.
- Multi Protocol Label Switching - MPLS (Including: MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference): Comprehensive MPLS protocol implementation.
- Network Management (Including: ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow): Manage network devices and services.
- Routing (Including: Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS): Implement and manage routing protocols.
- System Information and Utilities (Including: Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP): Manage system settings and perform various tasks.
- Virtual Private Networks (Including: 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier): Create and manage VPN connections.
- Wired Connections (Including: Ethernet, MikroTik wired interface compatibility, PWR Line): Configure and manage wired network connections.
- Wireless (Including: WiFi, Wireless Interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, Spectral scan): Configure and manage wireless networks.
 - Internet of Things (Including: Bluetooth, GPIO, Lora, MQTT): Support for IoT devices and applications.
 - Hardware (Including: Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features): Manage hardware devices and settings.
 - Diagnostics, monitoring and troubleshooting (Including: Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats and monitor-traffic, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 general guidance, Torch, Traceroute, Traffic Flow, Traffic Generator, Watchdog): Monitor and troubleshoot network issues.
 - Extended features (Including: Container, DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, IP packing): Utilize additional features to enhance network functionality.