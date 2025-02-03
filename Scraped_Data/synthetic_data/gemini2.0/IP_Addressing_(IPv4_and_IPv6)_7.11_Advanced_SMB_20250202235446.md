Okay, buckle up! This is going to be a deep dive into MikroTik RouterOS. This document aims to be a comprehensive guide for an advanced user, covering a vast array of topics. Let's get started.

## MikroTik RouterOS Deep Dive: Advanced IP Addressing and Beyond

This documentation will guide you through advanced IP addressing, routing, security, and other critical aspects of MikroTik RouterOS. We'll be focusing on a practical scenario for an SMB network with a RouterOS version 7.11 or higher.

**1. Comprehensive Configuration Scenario**

Imagine an SMB network with the following requirements:

*   **Connectivity:** A primary internet connection via a dynamic IPv4 address (DHCP client) and a backup fiber connection with a static IPv4 address.
*   **Internal Network:** Multiple VLANs for departments (Sales, Tech, Guest).
*   **IPv6 Support:** Future-proofing the network with IPv6 addressing.
*   **VPN Access:** Remote access via IPsec.
*   **Centralized DNS:** Local caching DNS server.
*   **Guest Network:** Limited access via a guest VLAN with firewall restrictions and rate limiting.
*   **Secure Management:** SSH access only from trusted IPs.
*   **Dynamic DNS:** Allow internal services to be accessible via DDNS.
*   **Network Monitoring:** Comprehensive logging and resource monitoring

**2. Step-by-Step MikroTik Implementation (CLI & Winbox)**

We will cover both CLI and Winbox methods. In this example, we assume you have a clean MikroTik setup.

### Step 1: Basic Interface Configuration

*   **CLI:**

    ```mikrotik
    /interface ethernet
    set [find default-name=ether1] name=WAN-Primary
    set [find default-name=ether2] name=WAN-Backup
    set [find default-name=ether3] name=LAN-Master
    set [find default-name=ether4] name=Port4
    set [find default-name=ether5] name=Port5
    ```
*   **Winbox:** Go to *Interfaces*, double-click on *ether1*, change the name to `WAN-Primary` etc.
*   **Explanation:** Renames physical interfaces for clarity. This is crucial for complex configurations.

### Step 2: IPv4 Addressing

*   **CLI:**

    ```mikrotik
    /ip address
    add address=192.168.10.2/24 interface=LAN-Master comment="LAN"
    add address=192.168.20.1/24 interface=LAN-Master vlan-id=20 comment="VLAN Sales"
    add address=192.168.30.1/24 interface=LAN-Master vlan-id=30 comment="VLAN Tech"
    add address=192.168.40.1/24 interface=LAN-Master vlan-id=40 comment="VLAN Guest"
    /ip dhcp-client
    add interface=WAN-Primary disabled=no
    /ip address
    add address=203.0.113.2/24 interface=WAN-Backup comment="Static IP Backup"
    ```

*   **Winbox:** *IP > Addresses*, add addresses for each interface and create `VLAN interfaces* using *Interfaces*, and *IP>DHCP client* configure the primary WAN Interface.
*   **Explanation:** Assigns static IPv4 addresses to the LAN interface and creates VLANs for subnets. The DHCP client is configured on `WAN-Primary`. We've added a static IP to our backup interface `WAN-Backup` as well.
    *   **VLAN Setup**: You create a vlan interface under `Interfaces` then set the interface, `vlan ID` etc.
    *  **IP address assignment to VLAN**: You assign the IP address in the same way you would to a regular interface, but specify the `interface` you created with your VLAN.

### Step 3: IPv6 Addressing

*   **CLI:**

    ```mikrotik
    /ipv6 address
    add address=2001:db8:1::1/64 interface=LAN-Master comment="IPv6 LAN"
    add address=2001:db8:1:20::1/64 interface=LAN-Master vlan-id=20 comment="IPv6 VLAN Sales"
    add address=2001:db8:1:30::1/64 interface=LAN-Master vlan-id=30 comment="IPv6 VLAN Tech"
    add address=2001:db8:1:40::1/64 interface=LAN-Master vlan-id=40 comment="IPv6 VLAN Guest"

     /ipv6 dhcp-client
    add interface=WAN-Primary request=address,prefix
    ```
*   **Winbox:** *IPv6 > Addresses*, add IPv6 addresses as above. *IPv6>DHCP Client* to configure DHCP-Client for IPv6 on the WAN-Primary interface.
*   **Explanation:** Configures IPv6 addresses for all interfaces. IPv6 DHCP client is enabled for auto configuration of address and prefixes.

### Step 4: IP Pools

*   **CLI:**

    ```mikrotik
    /ip pool
    add name=dhcp_pool_lan ranges=192.168.10.100-192.168.10.200
    add name=dhcp_pool_sales ranges=192.168.20.100-192.168.20.200
    add name=dhcp_pool_tech ranges=192.168.30.100-192.168.30.200
    add name=dhcp_pool_guest ranges=192.168.40.100-192.168.40.200
    ```
*   **Winbox:** *IP > Pool*, create the pool with appropriate names and ranges
*   **Explanation:** Creates IP address pools for DHCP servers on each VLAN.

### Step 5: IP DHCP Server

*   **CLI:**

    ```mikrotik
    /ip dhcp-server
    add address-pool=dhcp_pool_lan interface=LAN-Master name=dhcp_lan
    add address-pool=dhcp_pool_sales interface=LAN-Master vlan-id=20 name=dhcp_sales
    add address-pool=dhcp_pool_tech interface=LAN-Master vlan-id=30 name=dhcp_tech
    add address-pool=dhcp_pool_guest interface=LAN-Master vlan-id=40 name=dhcp_guest
    /ip dhcp-server network
    add address=192.168.10.0/24 dns-server=192.168.10.2 gateway=192.168.10.2
    add address=192.168.20.0/24 dns-server=192.168.20.1 gateway=192.168.20.1
    add address=192.168.30.0/24 dns-server=192.168.30.1 gateway=192.168.30.1
    add address=192.168.40.0/24 dns-server=192.168.40.1 gateway=192.168.40.1
    ```

*   **Winbox:** *IP > DHCP Server*, Add DHCP server with the appropriate `interface`, `address-pool` and name. In the same area select *Networks* add the appropriate settings for `address`, `gateway` and `dns-server`
*   **Explanation:** Sets up DHCP servers for each LAN interface.

### Step 6: IP Routing

*   **CLI:**

    ```mikrotik
    /ip route
    add dst-address=0.0.0.0/0 gateway=WAN-Primary check-gateway=ping distance=1 comment="Primary WAN Route"
    add dst-address=0.0.0.0/0 gateway=203.0.113.1 check-gateway=ping distance=2 comment="Backup WAN Route"
    /ipv6 route
     add dst-address=::/0 gateway=WAN-Primary check-gateway=ping distance=1 comment="Primary IPv6 WAN Route"
     add dst-address=::/0 gateway=fe80::1 distance=2 comment="Backup IPv6 Gateway route"
    ```
*   **Winbox:** *IP > Routes*. Add a default route via your Primary WAN with a distance of 1. Add a backup route via your secondary connection with a distance of 2.
*   **Explanation:** Configures default routes for internet access using the Primary WAN connection as first choice, and uses distance to make the backup connection secondary. IPv6 gateway is configured in the same way.

### Step 7: Firewall Configuration
*   **CLI**
    ```mikrotik
    /ip firewall filter
    add chain=input action=accept comment="Allow established and related connections" connection-state=established,related
    add chain=input action=accept comment="Allow loopback" src-address=127.0.0.1
    add chain=input action=accept protocol=icmp comment="Allow ICMP"
    add chain=input action=drop comment="Drop everything else"

    add chain=forward action=accept comment="Allow established and related connections" connection-state=established,related
    add chain=forward action=accept comment="Allow traffic within LAN" src-address=192.168.0.0/16 dst-address=192.168.0.0/16
    add chain=forward action=drop comment="Drop all else"
    
    /ip firewall nat
    add chain=srcnat action=masquerade out-interface=WAN-Primary comment="Masquerade primary WAN"
    add chain=srcnat action=masquerade out-interface=WAN-Backup comment="Masquerade backup WAN"
    
    ```
*   **Winbox:**  *IP > Firewall* Set up basic filter rules to accept established and related connections, allow loopback, allow icmp and drop the rest. Set up NAT rules to masquerade connections out the primary and secondary WAN interfaces.
*   **Explanation:** This sets up a basic firewall allowing internal networks access to the internet while protecting the router.

### Step 8: IP Services
*   **CLI**
    ```mikrotik
    /ip dns
    set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8
    /ip dns cache
    enable=yes
    /ip service
    set www address=192.168.10.0/24
    set ssh address=192.168.10.0/24
    ```
*   **Winbox:** *IP > DNS* - configure external DNS servers and allow remote requests, *IP>Services* - specify the networks that can access the Winbox and SSH
*   **Explanation:** Configures the DNS server on the MikroTik with public DNS forwarders and enables the caching.  Limits access to HTTP and SSH to the LAN network

### Step 9: RoMON
* **CLI:**
    ```mikrotik
    /tool romon
    set enabled=yes secret="your_secure_romon_secret"
    ```
* **Winbox:** *Tools > RoMON*. Enable RoMON, and set a secret. You may need to add allowed addresses if you only want RoMON to be accessible from specific IPs.
* **Explanation:** This enables Remote Monitoring, which is useful for centralized management of MikroTik routers.

### Step 10: WinBox
*   **Winbox:** Winbox is the primary method for GUI based configuration of MikroTik routers. Its used in many of the previous steps. Its an official tool that can be downloaded from the MikroTik website.
*   **Explanation:** The Winbox application provides a GUI based alternative to the CLI.  All the steps performed in the CLI can also be performed using Winbox.

### Step 11: Certificates
* **CLI:**
  ```mikrotik
  /certificate
  import file="your_certificate.crt" passphrase="your_certificate_passphrase"
  import file="your_key.key" passphrase="your_key_passphrase"
  ```
*   **Winbox:** *System > Certificates* Import the certificate and key files.
* **Explanation**:  Certificates are required for things like IPSec VPN connections.  This CLI example imports the certificate and key files using a secure password.

### Step 12: PPP AAA
*   **CLI:**
  ```mikrotik
  /ppp aaa
   set use-radius=yes interim-update=30
   /ppp profile
   set [find name=default] use-encryption=yes
  ```
*   **Winbox:** *PPP > AAA* and *PPP > Profiles*. Enable use of RADIUS and enable encryption in the default ppp profile.
*   **Explanation:** This is required for authentication of users via a radius server.

### Step 13: RADIUS
* **CLI:**
  ```mikrotik
  /radius
  add address=192.168.10.10 secret="your_radius_secret" timeout=30 authentication-port=1812 accounting-port=1813
  ```
* **Winbox:** *RADIUS* and add your radius server settings.
* **Explanation:** Add your radius server to enable authentication and accounting features.

### Step 14: Users / User Groups
*   **CLI:**
  ```mikrotik
   /user group
   add name="admin_group" policy="read,write,test,password,reboot,policy,ftp,web,local,winbox,api,romon,telnet,ssh,sniff,sensitive"
   /user add name="admin" group="admin_group" password="your_secure_password"
  ```
*   **Winbox:** *System > Users* and *System > User Groups*
*   **Explanation:** Create User groups, and users to be able to log into your MikroTik device using a secure password.

### Step 15: Bridging and Switching

* **CLI:**

    ```mikrotik
     /interface bridge
     add name=bridge_lan
     /interface bridge port
     add bridge=bridge_lan interface=LAN-Master
     add bridge=bridge_lan interface=Port4
     add bridge=bridge_lan interface=Port5
    /ip address
    set [find interface="LAN-Master"] interface=bridge_lan
    ```
*   **Winbox:** *Interfaces > Bridge* add a new bridge and name it *bridge_lan*. then *Interfaces > Bridge > Ports* add your physical interfaces to the bridge. finally, *IP > Addresses* set the interface of `LAN-Master` to the `bridge_lan` interface you just created.
* **Explanation:** This example shows how to add multiple physical ports to a single bridge interface, in this example adding `LAN-Master, Port4, and Port5` to `bridge_lan` interface.  The IP address is now assigned to the `bridge_lan` interface rather than the physical `LAN-Master` interface. This enables the physical ports to be part of the same network segment.

### Step 16: MACVLAN
*   **CLI:**
    ```mikrotik
     /interface macvlan
     add mac-address=02:00:00:00:00:01 interface=ether1 comment="MACVLAN 1"
     add mac-address=02:00:00:00:00:02 interface=ether1 comment="MACVLAN 2"
    ```
*   **Winbox:** *Interfaces > MACVLAN* Create MACVLAN interfaces with the desired MAC address and assigned interface.
*   **Explanation:** Creates multiple virtual interfaces on top of a single interface that each have a different MAC address, useful for containerisation and testing scenarios.

### Step 17: L3 Hardware Offloading

*   **CLI:**

    ```mikrotik
    /interface ethernet
    set [find name=LAN-Master] l3-hw-offloading=yes
    ```
*   **Winbox:** *Interfaces*, then double click the ethernet interface, select `l3 Hardware Offloading`
*   **Explanation:**  Enables L3 hardware offloading on the selected ethernet interface. This can drastically improve packet processing speed. *Note: hardware offloading is not supported on all MikroTik routers and will be displayed as an available option only on those devices that support it.*

### Step 18: MACsec
*  **CLI:**

   ```mikrotik
   /interface ethernet macsec
    add interface=ether2 key="Your-secret-key" comment="MACsec config"
    ```

*  **Winbox:** *Interface > MACsec*, then create a new entry, select the `interface` and add a `key`.
*  **Explanation:** Enables MACsec on an Ethernet interface, providing link-layer encryption and authentication.

### Step 19: Quality of Service
* **CLI:**
  ```mikrotik
   /queue tree
   add name="upload_limit_guest" parent=WAN-Primary queue=default max-limit=5M
   add name="download_limit_guest" parent=WAN-Primary queue=default max-limit=10M
   /queue simple
   add name="guest-queue" target=192.168.40.0/24 max-limit=10M/10M queue=upload_limit_guest/download_limit_guest
    ```

*  **Winbox:** *Queues > Queue Trees* and *Queues > Simple Queues*. Create the upload and download limits in *Queue Trees* then the simple queue that applies to a specific subnet (in this case the `guest` network) using your queue trees to define the limits.
*  **Explanation:** Limits the bandwidth available on the `guest` network using QoS.

### Step 20: Switch Chip Features
*   **CLI:**

    ```mikrotik
     /interface ethernet switch vlan
     add switch=switch1 vlan-id=20 ports=ether3,ether4
     add switch=switch1 vlan-id=30 ports=ether3,ether5
    ```
*  **Winbox:** *Interfaces > Ethernet* double click the interface and see what options are available for hardware switch chip features. *Interfaces > Switch > VLAN* for creating switch chip VLANs.
* **Explanation:** This allows you to configure VLAN functionality within the hardware of the switch chip, if available on your device. This configuration moves processing of VLANs to the hardware. *Note:  not all devices have a hardware switch chip.*

### Step 21: VLAN

*   **CLI:**

    ```mikrotik
     /interface vlan
     add interface=LAN-Master name=vlan-sales vlan-id=20
     add interface=LAN-Master name=vlan-tech vlan-id=30
     add interface=LAN-Master name=vlan-guest vlan-id=40
    ```
*   **Winbox:** *Interfaces > VLAN* create your VLAN interfaces by specifying the parent interface and vlan-id.
*   **Explanation:**  This shows how to create VLANs on top of the `LAN-Master` interface, with the VLAN IDs of 20, 30, and 40, these are used in the prior sections.

### Step 22: VXLAN
*   **CLI:**
   ```mikrotik
  /interface vxlan
   add name=vxlan1 vni=1000 interface=ether1 remote-address=10.10.10.2
   ```
*   **Winbox:** *Interface > VXLAN*. Create a new VXLAN interface with the `VNI`, `interface` and `remote-address`.
*  **Explanation:** This shows how to create a VXLAN interface with a `vni`, and remote address. This is used to tunnel data over an existing network.

### Step 23: Firewall and Quality of Service
(Refer to steps 7 and 19 for some basic configurations and explanations, more details and case studies below)

*   **Connection Tracking:** RouterOS automatically tracks connections and stores this data in a connection table. This allows the router to efficiently manage traffic and match return traffic to established connections.  You can view the connection table in *IP > Firewall > Connections*.
*   **Firewall:** The firewall in RouterOS operates on a chain based system. Packets enter the router and are processed in a pre-defined order in the forward, input and output chains.  Each chain contains rules. The rules will either accept, drop, or perform another action on the packet.  Rules can be matched by IP address, interface, protocol, and much more.
*   **Packet Flow in RouterOS:** Packets will flow through the router using the following process:
    *   **Physical Interface:** Packet enters or leaves the router on a physical interface.
    *   **Bridge and VLAN processing:** Packets will be processed by bridge or VLAN interfaces if they exist.
    *   **Firewall:** Packets are processed by the firewall rules.
    *   **Routing:** Packets are routed based on their destination address
    *   **Queues:** Packets are queued based on the defined rules
    *   **Physical Interface:** Packet leaves the router on a physical interface.
*   **Queues:** RouterOS offers both simple queues and queue trees for managing bandwidth. Simple queues are suitable for a per client or per subnet setup, and queue trees can provide more complex multi-tiered queuing setups.
*   **Firewall and QoS Case Studies:**
    *   **Traffic Prioritization:** Prioritize VoIP packets over less important traffic using queues with priority settings.
    *   **Rate Limiting:** Limit bandwidth for less important traffic.
    *   **Blocking Malicious IPs:** Block known malicious IP ranges using firewall filter rules.
*   **Kid Control:** Utilize time based firewall rules to control internet access for specific devices.
*   **UPnP:**  The Universal Plug and Play protocol, RouterOS supports UPnP which allows for automatic forwarding of ports. This can be useful in some situations, but poses a security risk if improperly configured.
*   **NAT-PMP:** NAT-PMP (NAT Port Mapping Protocol) can also automatically map ports, much like UPnP. This can be useful when UPNP is not supported on the client, or you do not wish to expose all port forwarding capabilities.

### Step 24: IP Services

*   **DHCP:**
    *   We covered basic DHCP config already in Step 5.
    *   RouterOS supports static leases, and multiple DHCP servers per interface.
*   **DNS:**
    *   The DNS server acts as a caching forwarder, forwarding DNS queries to configured external servers.
    *   The DNS server can provide local hostname records that do not exist on the public internet.
*   **SOCKS:**
    *   RouterOS can be configured as a SOCKS proxy, useful for redirecting traffic over alternative routes or for tunneling connections.
*   **Proxy:**
    *   RouterOS supports both HTTP and HTTPS proxies, this can be used to cache internet content and increase download speeds for commonly visited content.

### Step 25: High Availability Solutions

*   **Load Balancing:**
    *   RouterOS supports several load balancing approaches, including ECMP (Equal Cost Multi Path), and PCC (Per Connection Classifier). ECMP can be used for load balancing across multiple internet connections. PCC load balances using connection information.
*   **Bonding:**
    *   RouterOS supports bonding, which combines multiple interfaces to appear as a single interface to increase speed, bandwidth and provide link redundancy. Bonding can be done in a few different modes (802.3ad, balance-rr etc.)
*   **Bonding Examples:**
    *   **802.3ad** - Requires compatible switch at the other end, provides LACP link aggregation
    *   **Balance-rr** - Round robin load balancing across multiple interfaces.
*   **HA Case Studies:**
    *   **Dual ISP Failover:** Configure two internet links, with the backup link automatically taking over if the primary link fails.
    *   **Dual Router HA:** Utilize VRRP to create a hot standby router that will take over in case of hardware failure.
*   **Multi-Chassis Link Aggregation Group (MLAG)** - Allows aggregation of links across two separate switches.
*   **VRRP:** (Virtual Router Redundancy Protocol): Provides router redundancy so a backup router can seamlessly take over should a primary router fail.
*   **VRRP Configuration Examples:**
    *   Two routers with same VRRP settings. One router is the master, and one router is the backup.
    *   If the Master router goes down, the Backup router will take over the IP address.

### Step 26: Mobile Networking
*   **GPS:**
    * RouterOS has a built-in GPS client that can provide time and location data.
*   **LTE:**
    *   RouterOS supports LTE modems via USB, and in some cases built-in modules. RouterOS can be configured to auto connect to the LTE network.
*   **PPP:**
    *   PPP is used for several connection types (PPPoE, PPTP etc.) using authentication to connect to a remote network.
*   **SMS:**
    *   RouterOS can send and receive SMS messages via LTE modems.
*   **Dual SIM Application:**
    * RouterOS can be configured to use multiple SIM cards for failover and redundancy.

### Step 27: Multi Protocol Label Switching - MPLS
*   **MPLS Overview:** MPLS creates a label switched path, which speeds up packet forwarding by pre-defining the path that packets take.
*   **MPLS MTU:** The MTU setting for MPLS interfaces is very important to ensure consistent routing of packets.
*  **Forwarding and Label Bindings:** MPLS involves the creation of a forwarding table that maps IP addresses to MPLS labels.
* **EXP bit and MPLS Queuing:** The EXP bit can be used to apply QoS rules to different types of MPLS traffic.
*   **LDP:** (Label Distribution Protocol): Used to dynamically exchange labels between routers in a MPLS network.
*   **VPLS:** (Virtual Private LAN Service): Extends the layer 2 network across an MPLS network.
*   **Traffic Eng:** Traffic engineering can be used to manage the traffic path through a MPLS network.
*   **MPLS Reference:** For a more detailed overview and use case of MPLS see the MikroTik documentation.

### Step 28: Network Management

*   **ARP:**  RouterOS has a built in ARP table that stores MAC to IP address mappings. The ARP table can be viewed using the command `ip arp print`.
*   **Cloud:** The MikroTik cloud feature allows for remote access to your router. Use with caution as its a security risk to enable access if you are not sure what you are doing.
*   **DHCP:** DHCP has been covered previously, including DHCP leases and server setup.
*   **DNS:**  DNS configuration for forwarding and local records has been discussed previously
*   **SOCKS:** Configuration and usage of SOCKS proxy has also been previously discussed.
*  **Proxy:** HTTP and HTTPS proxy configuration has also been discussed previously.
*   **OpenFlow:** RouterOS can use the OpenFlow protocol, which allows network devices to be centrally managed and programmed.

### Step 29: Routing

*   **Routing Protocol Overview:**
   *   RouterOS supports several routing protocols (OSPF, RIP, BGP) as well as static routing.
*   **Moving from ROSv6 to v7 with examples:**
  *  ROSv7 uses a different syntax for routing protocol configuration compared to v6. Its important to use the correct syntax. Check the MikroTik documentation for details.
*   **Routing Protocol Multi-core Support:**
   * ROSv7 supports multicore routing and should take advantage of the additional processing power if available.
*  **Policy Routing:** Routing decisions can be made based on policy, for example routing specific traffic through a secondary interface, or based on source address.
*   **Virtual Routing and Forwarding - VRF:** This allows for multiple routing tables to be used, isolating different networks and providing separation.
*   **OSPF:** (Open Shortest Path First): Link state routing protocol, suitable for medium and large networks.
    *   RouterOS supports OSPFv2 and OSPFv3
*   **RIP:** (Routing Information Protocol): Distance vector routing protocol, suitable for small networks.
*   **BGP:** (Border Gateway Protocol): Path vector protocol, used for routing between Autonomous systems.
*   **RPKI:** (Resource Public Key Infrastructure): Used to validate routes and prevent BGP hijacking.
*   **Route Selection and Filters:**  Routing decisions can be controlled with route filters and policies.
*   **Multicast:**  RouterOS supports multicast routing using PIM (Protocol Independent Multicast)
*   **Routing Debugging Tools:**  Use the ping and traceroute tools to diagnose routing problems, and routing logging to debug complex issues.
*   **Routing Reference:** Consult the official RouterOS documentation for in-depth explanations of the available routing features.
*   **BFD:** (Bidirectional Forwarding Detection): Used to rapidly detect failures in paths and speed up failover times.
*   **IS-IS:** (Intermediate System to Intermediate System): A link state routing protocol similar to OSPF.

### Step 30: System Information and Utilities

*   **Clock:** The system clock is used for logging and scheduling.
*   **Device-mode:** This is used for device configurations like CAPsMAN, or simple router mode.
*   **E-mail:** RouterOS can send emails for alerts and monitoring.
*   **Fetch:** The fetch tool is used to download files from the internet.
*   **Files:** Used for managing the files that exist on the router, such as script files or backups.
*   **Identity:** Set the routers identity hostname.
*   **Interface Lists:** Create interface lists for easier configuration of firewall rules and other configuration options.
*   **Neighbor discovery:** RouterOS will discover other routers on the network automatically using protocols like LLDP.
*   **Note:** Use the note to document your configurations.
*   **NTP:** Use NTP to synchronise time with public time servers.
*   **Partitions:** RouterOS allows for multiple partitions, you may need to use it if the `/` disk is full and you want to use additional space on your storage drive.
*   **Precision Time Protocol:** PTP is used to provide more accurate timing for things like financial transactions, or real-time audio and video.
*   **Scheduler:** Schedule routine tasks to be completed automatically by the router.
*   **Services:** Set which interfaces can access management interfaces like web, winbox, ssh etc.
*   **TFTP:** (Trivial File Transfer Protocol) Used for transferring files such as router upgrades and backups.

### Step 31: Virtual Private Networks

*   **6to4:** A tunnelling method that encapsulates IPv6 packets inside IPv4.
*   **EoIP:** (Ethernet over IP): Used to create layer 2 tunnels across a network.
*   **GRE:** (Generic Routing Encapsulation): Used to encapsulate network layer protocols over a virtual network.
*   **IPIP:**  (IP in IP): Used to encapsulate IP packets inside other IP packets.
*   **IPsec:**  (IP Security): A suite of protocols used for securing IP communications over a network, used in VPNs.
*   **L2TP:** (Layer 2 Tunnelling Protocol): Another tunnelling protocol, commonly used in VPN setups.
*   **OpenVPN:** A very popular opensource VPN protocol.
*  **PPPoE:** (Point to Point Protocol over Ethernet): Used by some internet service providers for authentication.
*   **PPTP:** (Point to Point Tunnelling Protocol): An older VPN protocol.
*   **SSTP:** (Secure Socket Tunnelling Protocol): Uses HTTPS to create a secure tunnel.
*   **WireGuard:**  A modern VPN protocol focusing on speed and simplicity.
*  **ZeroTier:** A virtual networking tool, useful for creating overlay networks for connecting devices.

### Step 32: Wired Connections

*  **Ethernet:**  Standard wired interface, usually copper or fibre connection.
*   **MikroTik wired interface compatibility:** Some MikroTik devices support different interfaces such as SFP and SFP+. Check your devices documentation for compatibility.
*   **PWR Line:** Allows power and data to be transmitted over the same line.

### Step 33: Wireless
*   **WiFi:**  Standard wireless technology (802.11a/b/g/n/ac/ax). RouterOS is a full featured wireless AP.
*   **Wireless Interface:** RouterOS supports configuring both AP mode and Station mode.
*   **W60G:** 60Ghz Wireless technology used for short range high bandwidth connections.
*   **CAPsMAN:** (Centralized Access Point System MANager) Allows for centralized management of multiple wireless access points.
*   **HWMPplus mesh:** Used to create a mesh network using proprietary routing protocols.
*   **Nv2:**  Proprietary wireless protocol used by MikroTik.
*   **Interworking Profiles:** Used to integrate with external Wi-Fi networks for roaming and authentication.
*   **Wireless Case Studies:**
   *   Configure a wireless bridge.
   *   Configure a wireless hotspot with captive portal.

### Step 34: Internet of Things

*   **Bluetooth:** Bluetooth is supported on some MikroTik devices to allow for local device connections.
*   **GPIO:** (General Purpose Input Output): Use GPIO to monitor and interact with physical systems.
*   **Lora:** Long Range low power wireless technology.
*   **MQTT:** (Message Queuing Telemetry Transport): Used for passing messages between devices.

### Step 35: Hardware

*   **Disks:** MikroTik devices use flash storage or hard drives for firmware, logs and other files.
*   **Grounding:**  Make sure your MikroTik device is properly grounded, especially if using outdoors.
*   **LCD Touchscreen:** Some MikroTik devices have LCD screens used for configuration and monitoring.
*   **LEDs:** Some MikroTik devices have LEDs that can be used to visualise network status.
*   **MTU in RouterOS:**  The MTU (Maximum Transmission Unit) setting is important to ensure consistent network communication.
*   **Peripherals:** USB ports can be used for extra storage, or LTE modems.
*   **PoE-Out:**  Power over ethernet output to power other devices.
*   **Ports:** MikroTik devices have a variety of ports including ethernet, SFP, USB etc.
*   **Product Naming:** Mikrotik product names are used to identify the hardware specifications, this is useful for knowing which devices support which features.
*   **RouterBOARD:**  The RouterBOARD refers to a collection of hardware devices and products by MikroTik.
*   **USB Features:**  USB can be used for storage, LTE modems, and other features.

### Step 36: Diagnostics, Monitoring and Troubleshooting

*   **Bandwidth Test:**  Use the bandwidth test to measure network throughput.
*   **Detect Internet:** Use to test connectivity to the internet.
*   **Dynamic DNS:**  Use a dynamic DNS service to allow access to your router with a consistent hostname.
*   **Graphing:** Use graphing to visualise resource usage on your router.
*   **Health:** Monitor the health of the router, including CPU usage, RAM usage and other important settings.
*   **Interface stats and monitor-traffic:**  View the stats of interfaces to see what traffic is passing through.
*   **IP Scan:** Scan for IP addresses on the network.
*   **Log:** Log events on the router, useful for diagnosing problems and troubleshooting issues.
*   **Netwatch:** Monitor the state of IP addresses and trigger actions on state change.
*   **Packet Sniffer:** Capture network traffic for diagnosing network issues.
*   **Ping:** Test connectivity to a destination host.