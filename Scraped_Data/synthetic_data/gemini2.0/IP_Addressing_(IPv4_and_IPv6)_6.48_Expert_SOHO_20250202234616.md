Okay, let's dive into a comprehensive guide to IP Addressing and related features on a MikroTik router, targeting a SOHO environment with an expert configuration mindset. This documentation will cover RouterOS v6.48 (and relevant updates for v7.x), as requested.

## 1. Scenario and MikroTik Requirements

**Scenario:** We're setting up a SOHO network with the following:

*   **WAN:** Connected to an ISP providing a dynamic IPv4 address via DHCP and also supporting IPv6 via DHCPv6-PD.
*   **LAN:** A single LAN segment using the `ether2` interface.
*   **Guest Wi-Fi:** A separate virtual VLAN interface on `ether2` for guest Wi-Fi.
*   **Internal Servers:** A small group of servers accessible via static IPs.
*   **Security:** Firewall rules to protect the network.

**MikroTik Requirements:**

*   Configure DHCP client on the WAN interface.
*   Configure DHCP server for the LAN network.
*   Configure a DHCP server with VLAN for the guest network
*   Configure static IP addresses for servers.
*   Implement IPv6 addressing and routing.
*   Set up basic firewall rules.
*   Provide monitoring and troubleshooting tools.

## 2. Step-by-Step Implementation

### 2.1 Initial Setup (Using Winbox or CLI)

1.  **Connect to Router:** Connect your computer to any Ethernet port of the MikroTik router that isn't `ether1` and use Winbox or CLI to connect to the default IP. The default IP is generally `192.168.88.1`. If you cannot connect using `192.168.88.1` you can use Winbox to discover the router with the "Neighbors" tab, and connect using the routers MAC address.
2.  **Update RouterOS:** Before you make any configuration changes, ensure that your RouterOS is up-to-date.

    ```mikrotik
    /system package update check
    /system package update install
    ```
   **Notes:** RouterOS updates might require a restart of your device.

### 2.2 Interface Configuration

1.  **Rename Interfaces:** Rename interfaces for clarity.
    ```mikrotik
    /interface ethernet set ether1 name=WAN
    /interface ethernet set ether2 name=LAN
    /interface ethernet set ether3 name=LAN_Alt
    ```

2.  **Create VLAN Interface:** Create a VLAN for the Guest network on `LAN`.

    ```mikrotik
    /interface vlan add name=Guest_VLAN vlan-id=10 interface=LAN
    ```
3.  **Verify Configuration**: Using `print` ensure that the interfaces have been named and the VLAN has been created.
    ```mikrotik
    /interface print
    ```

### 2.3 IPv4 Addressing

1.  **WAN DHCP Client:** Configure the WAN interface for DHCP.

    ```mikrotik
    /ip dhcp-client add interface=WAN disabled=no
    ```
2.  **LAN IP Address:** Assign an IP address to the LAN interface.

    ```mikrotik
    /ip address add address=192.168.1.1/24 interface=LAN
    ```
3. **VLAN IP Address:** Assign an IP address to the VLAN interface.
    ```mikrotik
     /ip address add address=192.168.2.1/24 interface=Guest_VLAN
    ```

4.  **LAN DHCP Server:** Configure a DHCP server for the LAN.

    ```mikrotik
    /ip pool add name=LAN_Pool ranges=192.168.1.100-192.168.1.200
    /ip dhcp-server add name=LAN_DHCP interface=LAN address-pool=LAN_Pool lease-time=10m
    /ip dhcp-server network add address=192.168.1.0/24 gateway=192.168.1.1 dns-server=1.1.1.1,8.8.8.8
    ```
5.  **VLAN DHCP Server**: Configure a DHCP server for the Guest network.

    ```mikrotik
    /ip pool add name=Guest_Pool ranges=192.168.2.100-192.168.2.200
    /ip dhcp-server add name=Guest_DHCP interface=Guest_VLAN address-pool=Guest_Pool lease-time=10m
    /ip dhcp-server network add address=192.168.2.0/24 gateway=192.168.2.1 dns-server=1.1.1.1,8.8.8.8
    ```
6.  **Static IPs:** Add static IPs to internal servers.
     ```mikrotik
     /ip address add address=192.168.1.10/32 interface=LAN comment="Server 1"
     /ip address add address=192.168.1.11/32 interface=LAN comment="Server 2"
    ```

    **Note:**  Use `/32` when you are configuring an address for a single device or server.

### 2.4 IPv6 Addressing

1.  **IPv6 DHCP Client:** Enable IPv6 DHCP client on the WAN.

    ```mikrotik
    /ipv6 dhcp-client add interface=WAN request=address,prefix
    ```
2.  **LAN IPv6 Address:** Assign IPv6 prefix to the LAN interface.

    ```mikrotik
    /ipv6 address add interface=LAN address=::1/64 from-pool=DHCPv6_Pool
    ```
3. **VLAN IPv6 Address:** Assign IPv6 prefix to the Guest_VLAN interface.

    ```mikrotik
     /ipv6 address add interface=Guest_VLAN address=::1/64 from-pool=DHCPv6_Pool
    ```
4. **IPv6 Pool**: Define IPv6 Pool.
   ```mikrotik
    /ipv6 pool add name=DHCPv6_Pool prefix=::/64
   ```
    **Note:** In RouterOS v7.x, DHCPv6 client prefix delegation is automatic on interfaces, which simplifies configuration. In RouterOS 6.x, you need to configure IP6 pools with the desired prefix. This configuration is an example for v7.x, as v6.x has a slightly different mechanism to achieve the same result.

### 2.5 IP Routing

1.  **Default Route:** A default route to the internet should be automatically added by the DHCP client. Verify that a default route is present.

    ```mikrotik
    /ip route print
    ```

    **Note**:  If no default route is present, you may need to add a manual route if the route is not provided by your ISP:
    ```mikrotik
     /ip route add gateway=[ISP Gateway IP]
    ```
2. **IPv6 Default Route:** A default IPv6 route is automatically handled by the `ipv6 dhcp-client`. However, verify that the route is present.
   ```mikrotik
   /ipv6 route print
   ```
    **Note:** Check the IPv6 routes; they usually are auto-added from `dhcp-client`

### 2.6 IP Settings

1.  **IP DNS Settings:** Configure DNS servers.

    ```mikrotik
    /ip dns set servers=1.1.1.1,8.8.8.8 allow-remote-requests=yes
    ```
2.  **Disable Fasttrack**: Fasttrack can cause issues with some applications. If you are troubleshooting any issues, disabling this is a good place to start.
   ```mikrotik
   /ip firewall filter set fasttrack-connection=no
    ```

    **Note:** In production environments, you may want to reenable fasttrack.

### 2.7 MAC Server

The MAC server is enabled by default and can help with accessing the router using Winbox via it's MAC address. This is especially useful if you do not know the routers IP address, but have physical access to the local network.

### 2.8 RoMON

RoMON allows for monitoring of a network of routers.

1. **Enable RoMON:** To enable RoMON you will need to specify an interface
    ```mikrotik
    /tool romon set enabled=yes interfaces=LAN,WAN
    ```
   **Note:** It is a best practice to disable RoMON on the WAN interface for security reasons.
2. **View neighbors:**
    ```mikrotik
    /tool romon print
    ```
   **Note:** RoMON will only show other devices on a RoMON enabled network.

### 2.9 Winbox

Winbox is a GUI tool for managing MikroTik devices.

*   Ensure Winbox is downloaded from the MikroTik website.
*   Use the "Neighbors" tab to find MikroTik devices on the local network, which should automatically populate.
*   Use your username and password to log in to the router.
*   Winbox is usually on port 8291.

### 2.10 Certificates

Certificates are necessary for secured communication such as HTTPS and IPSec.

1.  **Generate a self-signed certificate:**

    ```mikrotik
    /certificate add name=self_signed common-name=router.local key-usage=tls-server,tls-client,digital-signature
    /certificate sign self_signed
    ```
   **Note:** A self-signed certificate is not recommended in a production environment.
2.  **Import existing certificates:**
    * Use Winbox to navigate to `/System/Certificates`.
    * Use the import button at the top of the screen to import a certificate file.

### 2.11 PPP AAA

PPP AAA is used for authentication of PPP users. This is not used in a typical SOHO environment, however it is good to know.

1.  **Create a user profile:**

    ```mikrotik
    /ppp profile add name=default-profile use-encryption=yes only-one=yes
    ```
2. **Create a PPP secret:**

    ```mikrotik
    /ppp secret add name=test-user password=test-password profile=default-profile service=pppoe
    ```

### 2.12 RADIUS

RADIUS (Remote Authentication Dial-In User Service) is used for centralized authentication.

1. **Add a RADIUS server:**

    ```mikrotik
    /radius add address=192.168.1.2 secret=radius-secret service=ppp
    ```

    **Note:** The `secret` must match the secret configured on the RADIUS server.

2. **Verify RADIUS is working:**
    * Use `/tool radius test` command to test the connection.

### 2.13 User / User groups

RouterOS users and groups are used to control access to the device.

1.  **Add a user:**

    ```mikrotik
    /user add name=admin password=strongpassword group=full
    ```
   **Note:** The `group` options are `read`, `write`, `test`, `full`.
2. **Add a group:**
   ```mikrotik
    /user group add name=limited policy=read,test
    ```

### 2.14 Bridging and Switching

Bridging combines multiple interfaces into one network. Switching allows traffic to be forwarded based on MAC addresses.

1. **Create a bridge:**

    ```mikrotik
    /interface bridge add name=LAN_Bridge
    ```

2.  **Add Interfaces to Bridge:**

    ```mikrotik
    /interface bridge port add bridge=LAN_Bridge interface=LAN
    /interface bridge port add bridge=LAN_Bridge interface=LAN_Alt
    ```

    **Note:** If bridging multiple interfaces, ensure that the IP address is assigned to the bridge interface, rather than the individual physical interfaces.

### 2.15 MACVLAN

MACVLAN allows creating multiple virtual interfaces with different MAC addresses on the same physical interface.

1.  **Create a MACVLAN:**
    ```mikrotik
    /interface macvlan add interface=LAN mac-address=02:03:04:05:06:07 name=MACVLAN_1
    /interface macvlan add interface=LAN mac-address=02:03:04:05:06:08 name=MACVLAN_2
    ```
2. Assign IP addresses:
    ```mikrotik
    /ip address add interface=MACVLAN_1 address=192.168.3.1/24
    /ip address add interface=MACVLAN_2 address=192.168.4.1/24
   ```

### 2.16 L3 Hardware Offloading

L3 Hardware Offloading can improve router performance by offloading routing to the switch chip.
   * Verify if L3 Hardware Offloading is supported on your device using `/system resource print`.

### 2.17 MACsec

MACsec is a layer-2 encryption protocol. This is not used in a typical SOHO environment.

### 2.18 Quality of Service

QoS allows you to prioritize certain types of traffic. This is covered under the Firewall section.

### 2.19 Switch Chip Features

Switch chips on MikroTik routers can have various functionalities, such as VLAN tagging and rate limiting.  This is mostly configured on the `/interface ethernet switch` menu.

### 2.20 VLAN

We have already implemented VLAN's with `Guest_VLAN`.

### 2.21 VXLAN

VXLAN provides network virtualization capabilities. This is not used in a typical SOHO environment, but is useful for more advanced configuration scenarios.

### 2.22 Firewall and Quality of Service

1.  **Basic Firewall Rules:**

    ```mikrotik
    /ip firewall filter add chain=input connection-state=established,related action=accept comment="Allow established and related connections"
    /ip firewall filter add chain=input protocol=icmp action=accept comment="Allow ICMP"
    /ip firewall filter add chain=input in-interface=WAN action=drop comment="Drop invalid connections from WAN"
    /ip firewall filter add chain=forward connection-state=established,related action=accept comment="Allow established and related forward"
    /ip firewall filter add chain=forward in-interface=WAN action=drop comment="Drop invalid forward connections from WAN"
    /ip firewall nat add chain=srcnat out-interface=WAN action=masquerade comment="Masquerade outgoing traffic"
    ```

    **Notes:**
    *  These are basic rules. You can add more rules to allow specific traffic to specific devices.
    *  `Masquerade` does Network Address Translation (NAT).
2.  **Connection Tracking:** RouterOS maintains connection tracking for the firewall. You can view the connection tracking table using:
    ```mikrotik
    /ip firewall connection print
    ```
3.  **Packet Flow:**
    *   Ingress: Packet arrives at an interface.
    *   Firewall: Packet is processed by input, forward, and output chains.
    *   Routing: Router decides where to send the packet.
    *   Egress: Packet leaves the router through an interface.
4.  **Queues:**
     *  Simple Queues: Used for simple bandwidth control.
    ```mikrotik
    /queue simple add name=download target=LAN max-limit=10M/20M
    ```
    *  Queue Tree: More advanced queuing with more granular control.
5. **Firewall and QoS Case Studies**
    * **Port forwarding**: To forward TCP/UDP ports for a particular device:
    ```mikrotik
    /ip firewall nat add chain=dstnat protocol=tcp dst-port=8080 action=dst-nat to-addresses=192.168.1.10 to-ports=8080 comment="Forward TCP 8080 to server"
    ```
    * **QoS**: To limit the bandwidth for torrents, you can use layer-7 protocols and mangle rules:
       ```mikrotik
        /ip firewall layer7-protocol add name=torrent regexp="^.+(bt|bit|torr).+"
        /ip firewall mangle add chain=forward layer7-protocol=torrent action=mark-packet new-packet-mark=torrent-packet
        /queue simple add name=torrent-queue target=torrent-packet max-limit=1M
       ```
6. **Kid Control**: Kid control can be implemented via time rules using the `/ip firewall filter` functionality. This rule drops traffic at a specific time.
7. **UPnP**: UPnP should not be enabled unless it is needed to avoid exposing unintended ports. This is done in the `/ip upnp` functionality.
8. **NAT-PMP**: Similar to UPnP, NAT-PMP should be enabled only if needed. This is done in the `/ip nat-pmp` functionality.

### 2.23 IP Services

1.  **DHCP:** DHCP was already covered in IP Addressing.
2.  **DNS:** DNS was covered in IP Settings.
3.  **SOCKS:**
     * The socks proxy can be configured via the `/ip socks` functionality.
4. **Proxy**:
     * The proxy server can be configured via the `/ip proxy` functionality.

### 2.24 High Availability Solutions

1.  **Load Balancing:**  Load balancing requires multiple WAN connections and can be implemented using `policy routing`. This is a more advanced topic and is beyond the scope of this document.
2.  **Bonding:**  Bonding combines multiple physical interfaces into one logical interface to provide increased bandwidth. This is not generally recommended for a SOHO environment.
3. **Bonding Examples**
    * To create a bonding interface with the `balance-rr` mode:
    ```mikrotik
    /interface bonding add name=bond1 mode=balance-rr slaves=ether3,ether4
    ```
4. **HA Case Studies**
    * High availability using VRRP (Virtual Router Redundancy Protocol) is common in enterprise environments. This is beyond the scope of the SOHO scenario.
5.  **Multi-chassis Link Aggregation Group (MLAG):**  MLAG provides redundancy by using separate switches. This is not generally applicable for a SOHO environment.
6.  **VRRP:**
    * Create a virtual interface with a priority:
    ```mikrotik
    /interface vrrp add interface=LAN name=vrrp1 priority=200 vrid=1 virtual-address=192.168.1.254/24
    ```
7. **VRRP Configuration Examples**
    * To test VRRP add a second router with a lower priority such as 100, and the address 192.168.1.254 on the virtual address. If the first router goes offline, the second router will take over the virtual IP.

### 2.25 Mobile Networking

1.  **GPS:** MikroTik devices can utilize GPS modules to synchronize time.
2.  **LTE:**  MikroTik devices with LTE functionality allow for cellular internet connectivity.
3.  **PPP:** PPP is used for dial-up connections.
4.  **SMS:**  Some LTE devices can send and receive SMS messages.
5.  **Dual SIM Application:** Some MikroTik devices allow for dual sim functionality.

### 2.26 Multi Protocol Label Switching - MPLS

1.  **MPLS Overview:** MPLS uses labels to route traffic, and is more commonly used in large enterprise and ISP networks.
2.  **MPLS MTU:** MPLS requires an MTU that is sufficient for the MPLS packet.
3.  **Forwarding and Label Bindings:** These define how MPLS labels are added and removed.
4.  **EXP bit and MPLS Queuing:** The EXP bit is used for QoS in MPLS networks.
5.  **LDP:** Label Distribution Protocol is used to create label bindings.
6.  **VPLS:** Virtual Private LAN Service creates a layer-2 multipoint service.
7.  **Traffic Eng:** MPLS traffic engineering allows for more intelligent routing.
8.  **MPLS Reference** The `/mpls` configuration menu provides all of the MPLS functionality.

### 2.27 Network Management

1.  **ARP:** ARP is used to resolve IP addresses to MAC addresses. You can view the ARP table via `/ip arp print`.
2.  **Cloud:** The MikroTik cloud functionality allows for accessing the router via the internet.  This is not recommended for security reasons.
3.  **DHCP:** DHCP was covered in IP Addressing.
4.  **DNS:** DNS was covered in IP Settings.
5.  **SOCKS:** SOCKS was covered in IP Services.
6.  **Proxy:** Proxy was covered in IP Services.
7. **Openflow** Openflow is used to configure software defined networking (SDN), but is beyond the scope of a SOHO environment.

### 2.28 Routing

1.  **Routing Protocol Overview:** RouterOS supports many routing protocols like OSPF, RIP, and BGP.
2.  **Moving from ROSv6 to v7 with examples:** Moving from ROSv6 to v7 involves new package management, and configuration paradigms.  The following will be updated for use with v7.
3.  **Routing Protocol Multi-core Support:** RouterOS has improved multi-core support for routing protocols.
4.  **Policy Routing:** Allows for routing packets based on different criteria (e.g. source address). This is useful for load balancing and traffic steering.
5. **Virtual Routing and Forwarding - VRF:** Allows for different routing tables for different network segments. This is more common in enterprise environments.
6.  **OSPF:** Open Shortest Path First is an interior gateway protocol. This is not typically used in SOHO environments.
7.  **RIP:** Routing Information Protocol is a distance vector protocol. This is not recommended for new networks.
8.  **BGP:** Border Gateway Protocol is used to connect autonomous systems on the internet. This is not common for a SOHO environment.
9. **RPKI** RPKI is used to secure BGP by validating routes.
10. **Route Selection and Filters:** RouterOS uses filters to select routes. These can be configured using `prefix-lists` and filters.
11. **Multicast**: Multicast allows for sending a single packet to a group of destination hosts, and is generally used for video streaming.
12. **Routing Debugging Tools** The `/routing` menu provides many options for monitoring and debugging routing issues.
13. **Routing Reference** The RouterOS documentation is very useful for learning more about routing.
14. **BFD** Bidirectional Forwarding Detection is a low overhead protocol used to detect network failure.
15. **IS-IS** Intermediate System to Intermediate System is a routing protocol that can be used as an alternative to OSPF.

### 2.29 System Information and Utilities

1.  **Clock:** You can set the time via the `/system clock` functionality.
2.  **Device-mode:** MikroTik devices can operate in a different device-mode. This is usually set automatically, but can be changed if needed via the `/system device-mode` functionality.
3.  **E-mail:** You can configure email notifications for specific events via the `/tool e-mail` functionality.
4.  **Fetch:** The fetch tool allows for downloading files from a remote server via the `/tool fetch` functionality.
5.  **Files:** The files tool provides a way to interact with the file system.
6.  **Identity:** The identity of the device can be changed via the `/system identity` functionality.
7.  **Interface Lists:** Lists of interfaces can be used for grouping similar interfaces via the `/interface list` functionality.
8. **Neighbor discovery**: Can be used to find neighbors on the network, and should be enabled for features like RoMON.
9.  **Note:** Allows for adding comments to configurations via the `/system note` functionality.
10. **NTP:** Network time protocol can be used to ensure that devices have the correct time via the `/system ntp client` functionality.
11. **Partitions** This menu displays information about the partitions on the device.
12. **Precision Time Protocol** The `/system ptp` functionality allows for high precision time synchronization.
13. **Scheduler** The scheduler allows for running tasks at a specific time via the `/system scheduler` functionality.
14. **Services** Services are configurable on the `/ip service` functionality.
15. **TFTP:** Trivial File Transfer Protocol is used for transferring files to and from the device, using the `/tool tftp-server` functionality.

### 2.30 Virtual Private Networks

1.  **6to4:** Provides IPv6 connectivity over an IPv4 network.
2.  **EoIP:** Ethernet over IP provides a layer-2 tunnel over IP.
3.  **GRE:** Generic Routing Encapsulation provides a tunnel over IP.
4. **IPIP:** IP in IP encapsulation.
5.  **IPsec:** IP security provides encryption and authentication for IP traffic. This is one of the most common VPN protocols.
6.  **L2TP:** Layer 2 Tunneling Protocol provides a layer-2 tunnel over IP.
7.  **OpenVPN:** OpenVPN is a popular open-source VPN solution.
8. **PPPoE**: Point to point over ethernet.
9. **PPTP**: Point to point tunneling protocol.
10. **SSTP**: Secure Socket Tunneling Protocol uses https to tunnel traffic.
11. **WireGuard:** WireGuard is a modern VPN protocol that is fast and secure.
12. **ZeroTier**: ZeroTier provides a software defined networking solution, similar to a VPN.

### 2.31 Wired Connections

1.  **Ethernet:** Ethernet settings can be configured in the `/interface ethernet` functionality.
2.  **MikroTik wired interface compatibility:** Check the RouterOS documentation for wired interface compatibility for your device.
3.  **PWR Line:** PWR line is the ethernet interface that is used for power over ethernet.

### 2.32 Wireless

1.  **WiFi:** WiFi is configured via the `/interface wireless` functionality.
2.  **Wireless Interface:** This menu contains information about the wireless interface.
3.  **W60G:** This is for 60 ghz wireless connections.
4.  **CAPsMAN:** CAPsMAN provides centralized management for wireless networks.
5.  **HWMPplus mesh:** Allows for wireless mesh functionality, using the `/interface w60g` functionality.
6.  **Nv2:** Nv2 is a proprietary wireless protocol developed by MikroTik.
7.  **Interworking Profiles:** Interworking Profiles allow for integration between WiFi networks and other networks, using the `/interface wireless` functionality.
8. **Wireless Case Studies** Advanced configuration of wireless settings.
9.  **Spectral scan:** This provides an interface to analyze the radio frequency spectrum via the `/interface wireless spectral-history` functionality.

### 2.33 Internet of Things

1. **Bluetooth:** This functionality allows for the use of Bluetooth devices.
2. **GPIO:** This is generally used for more specialized use cases.
3. **Lora:** This is for use of Long Range low powered networks.
4. **MQTT:** This is for Message Queuing Telemetry Transport.

### 2.34 Hardware

1. **Disks:** This menu displays information about the connected disks.
2. **Grounding:** MikroTik devices should be properly grounded to avoid damage due to electrical surges.
3. **LCD Touchscreen:** Some MikroTik devices have a built in LCD screen.
4. **LEDs:** This menu is used to control the LEDs on the device.
5. **MTU in RouterOS:** Maximum Transmission Unit determines the size of a single packet. This is typically 1500 for ethernet.
6. **Peripherals:** This menu is used to view connected peripheral devices.
7. **PoE-Out:** Power over Ethernet can be used to power other devices.
8. **Ports:** This menu shows information about the device's ports.
9. **Product Naming:** Refer to the MikroTik website for information on product naming.
10. **RouterBOARD:** This refers to the hardware platform from MikroTik.
11. **USB Features:** This menu shows information about connected USB devices.

### 2.35 Diagnostics, Monitoring and Troubleshooting

1.  **Bandwidth Test:** `/tool bandwidth-test` is used to measure bandwidth between two devices.
2.  **Detect Internet:** `/tool detect-internet` will attempt to detect if the device has an internet connection.
3.  **Dynamic DNS:** `/ip cloud` is used for dynamic DNS.
4.  **Graphing:** RouterOS can graph resource usage, using the `/tool graphing` functionality.
5.  **Health:** The `/system health` menu provides information about device health.
6.  **Interface stats and monitor-traffic:** The `/interface monitor` functionality allows for viewing traffic on a particular interface.
7.  **IP Scan:** The `/ip scan` functionality allows for scanning for devices on a network.
8.  **Log:** The system logs can be viewed using the `/system log print` command.
9.  **Netwatch:** The `/tool netwatch` functionality allows for monitoring of devices on the network.
10. **Packet Sniffer:** The `/tool sniffer` functionality allows for capturing network packets.
11. **Ping:** The ping tool allows for testing connectivity using the `/ping` command.
12. **Profiler:** The profiler is a tool for CPU performance analysis using the `/tool profiler` functionality.
13. **Resource:** This is used to view device resources using the `/system resource print` functionality.
14. **SNMP:** The Simple Network Management Protocol can be used for remote monitoring.
15. **Speed Test:** The speed test functionality can be found under the `/tool bandwidth-test` menu.
16. **S-RJ10 general guidance:** This applies to the s-rj10 10gbps sfp+ ethernet ports.
17. **Torch:** Torch can be used to monitor the traffic passing through a particular interface or firewall rule. The `/tool torch` tool will display a live view of the current traffic.
18. **Traceroute:**  The traceroute utility can be used to determine the network path to a particular destination using the `/traceroute` command.
19. **Traffic Flow:** The `/ip traffic-flow` menu allows for exporting network traffic information.
20. **Traffic Generator:** The `/tool traffic-generator` functionality allows for generating test traffic.
21. **Watchdog:** The `/system watchdog` functionality can be used to automatically reboot the device if it stops responding.

### 2.36 Extended features

1. **Container:** RouterOS can now run docker containers. This is an advanced feature, and requires a device with sufficient resources.
2. **DLNA Media server:** This function is used to setup a media server via the `/dlna` menu.
3. **ROSE-storage:** This functionality can be used to setup a storage server.
4. **SMB:** This function is used for setting up a server message block using the `/smb` menu.
5. **UPS:** This functionality is used for setting up an Uninterruptible Power Supply using the `/ups` menu.
6. **Wake on LAN:** This allows for remotely turning on a computer.
7. **IP packing:** IP packing allows you to define IP addresses using variable data length.

## 3. Complete CLI Configuration

Here's a consolidated view of the CLI commands used:

```mikrotik
# Initial Setup
/system package update check
/system package update install

# Interface Configuration
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN
/interface ethernet set ether3 name=LAN_Alt
/interface vlan add name=Guest_VLAN vlan-id=10 interface=LAN

# IPv4 Addressing
/ip dhcp-client add interface=WAN disabled=no
/ip address add address=192.168.1.1/24 interface=LAN
/ip address add address=192.168.2.1/24 interface=Guest_VLAN
/ip pool add name=LAN_Pool ranges=192.168.1.100-192.168.1.200
/ip dhcp-server add name=LAN_DHCP interface=LAN address-pool=LAN_Pool lease-time=10m
/ip dhcp-server network add address=192.168.1.0/24 gateway=192.168.1.1 dns-server=1.1.1.1,8.8.8.8
/ip pool add name=Guest_Pool ranges=192.168.2.100-192.168.2.200
/ip dhcp-server add name=Guest_DHCP interface=Guest_VLAN address-pool=Guest_Pool lease-time=10m
/ip dhcp-server network add address=192.168.2.0/24 gateway=192.168.2.1 dns-server=1.1.1.1,8.8.8.8
/ip address add address=192.168.1.10/32 interface=LAN comment="Server 1"
/ip address add address=192.168.1.11/32 interface=LAN comment="Server 2"

# IPv6 Addressing
/ipv6 dhcp-client add interface=WAN request=address,prefix
/ipv6 pool add name=DHCPv6_Pool prefix=::/64
/ipv6 address add interface=LAN address=::1/64 from-pool=DHCPv6_Pool
/ipv6 address add interface=Guest_VLAN address=::1/64 from-pool=DHCPv6_Pool


# IP DNS Settings
/ip dns set servers=1.1.1.1,8.8.8.8 allow-remote-requests=yes

# IP Settings
/ip firewall filter set fasttrack-connection=no

# RoMON
/tool romon set enabled=yes interfaces=LAN

# Certificates
/certificate add name=self_signed common-name=router.local key-usage=tls-server,tls-client,digital-signature
/certificate sign self_signed

# PPP AAA
/ppp profile add name=default-profile use-encryption=yes only-one=yes
/ppp secret add name=test-user password=test-password profile=default-profile service=pppoe

# RADIUS
/radius add address=192.168.1.2 secret=radius-secret service=ppp

# User
/user add name=admin password=strongpassword group=full
/user group add name=limited policy=read,test

# Bridging
/interface bridge add name=LAN_Bridge
/interface bridge port add bridge=LAN_Bridge interface=LAN
/interface bridge port add bridge=LAN_Bridge interface=LAN_Alt

# MACVLAN
/interface macvlan add interface=LAN mac-address=02:03:04:05:06:07 name=MACVLAN_1
/interface macvlan add interface=LAN mac-address=02:03:04:05:06:08 name=MACVLAN_2
/ip address add interface=MACVLAN_1 address=192.168.3.1/24
/ip address add interface=MACVLAN_2 address=192.168.4.1/24

# Firewall Rules
/ip firewall filter add chain=input connection-state=established,related action=accept comment="Allow established and related connections"
/ip firewall filter add chain=input protocol=icmp action=accept comment="Allow ICMP"
/ip firewall filter add chain=input in-interface=WAN