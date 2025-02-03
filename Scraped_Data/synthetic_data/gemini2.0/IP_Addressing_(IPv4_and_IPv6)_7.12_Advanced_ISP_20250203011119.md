Okay, let's dive into a comprehensive MikroTik RouterOS configuration for the specified scenario, covering a wide range of topics and diving into the details you requested.

# MikroTik RouterOS Configuration: ISP-Grade IPv4 & IPv6 Implementation

This document provides a detailed configuration example for a MikroTik router acting as a gateway for an ISP-style environment, focusing on IP addressing, routing, and related advanced features within RouterOS 7.12 (and compatible with 6.48/7.x).

**Scenario:**

We are configuring a MikroTik router to manage a single subnet for wireless clients on interface `wlan-88`. This scenario will encompass both IPv4 and IPv6 configurations and touch on various aspects of RouterOS.

**Configuration Level:** Advanced
**Network Scale:** ISP
**Subnet:** 21.12.92.0/24
**Interface Name:** wlan-88

## 1. Comprehensive Configuration Scenario and Specific MikroTik Requirements

*   **Goal:** Provide a robust and scalable network configuration for wireless clients on a dedicated interface.
*   **Specific Requirements:**
    *   Assign a static IPv4 address to the `wlan-88` interface.
    *   Configure a DHCP server to provide addresses within the 21.12.92.0/24 subnet.
    *   Enable IPv6 addressing on the same interface (using SLAAC).
    *   Implement basic firewall rules for security.
    *   Showcase advanced features like IP Pools, Connection Tracking, Queues.
    *   Demonstrate troubleshooting and monitoring techniques.
    *   Provide REST API examples for common operations.
    *   Illustrate security best practices specific to MikroTik.

## 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

### 2.1. Setting Up IPv4 Addressing (CLI)

1.  **Assign IPv4 Address to `wlan-88` Interface:**
    ```mikrotik
    /ip address add address=21.12.92.1/24 interface=wlan-88
    ```
    *   **Explanation:** This command assigns the IP address 21.12.92.1 with a subnet mask of /24 to the interface `wlan-88`. This will be the router's IP address on this subnet.

2.  **Configure a DHCP Server:**

   *  Add IP Pool for DHCP server
       ```mikrotik
         /ip pool add name=dhcp-pool ranges=21.12.92.10-21.12.92.254
       ```
   *   Create a DHCP Server Instance on `wlan-88`.
       ```mikrotik
       /ip dhcp-server add address-pool=dhcp-pool interface=wlan-88 name=dhcp-wlan-88
       ```

   *   Configure the network. This is where we define the DNS server and default route information given to clients.

        ```mikrotik
        /ip dhcp-server network add address=21.12.92.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=21.12.92.1
        ```
    *   **Explanation:**  This sets up a DHCP server to dynamically assign IP addresses from the 21.12.92.10-21.12.92.254 range to clients connecting to the `wlan-88` interface. It also configures DNS and the default gateway address.

### 2.2. Setting Up IPv6 Addressing (CLI)

1.  **Enable IPv6:**
    ```mikrotik
    /ipv6 settings set disable-ipv6=no
    ```
    *   **Explanation:**  Enables global IPv6 functionality on the router.

2.  **Assign a link-local address on `wlan-88`:** While not strictly necessary as SLAAC will take care of this, it's good practice to confirm.
   ```mikrotik
   /ipv6 address add interface=wlan-88 from-pool=local-pool
   ```

3.  **Configure IPv6 RA (Router Advertisement) for SLAAC:**
    ```mikrotik
    /ipv6 nd add interface=wlan-88 advertise-dns=yes advertise-mtu=1500 other-configuration=yes managed-address=no
    ```

    *   **Explanation:** This enables Router Advertisement (RA) on the `wlan-88` interface, allowing devices to obtain an IPv6 address through Stateless Address Autoconfiguration (SLAAC). `advertise-dns` makes sure DNS information is advertised via RA, `other-configuration` configures DHCPv6 without address information.

### 2.3. Firewall Configuration (CLI)

1.  **Basic Firewall Rules:**
    ```mikrotik
    /ip firewall filter
    add chain=input action=accept comment="Allow established and related connections" connection-state=established,related
    add chain=input action=drop comment="Drop all other input connections" in-interface-list=!LAN
    add chain=forward action=accept comment="Allow established and related connections" connection-state=established,related
    add chain=forward action=drop comment="Drop all other forward connections" connection-state=new connection-nat-state=!dstnat in-interface=wlan-88
    ```
    *   **Explanation:** These rules ensure that only legitimate traffic is allowed through the router. Only established/related is allowed, all else is dropped. Additionally, new connections on wlan-88 must either be DNAT connections or be dropped.
    *   **Note:** You should tailor the rules to your specific needs.

### 2.4. Winbox Configuration (Partial)

*   **IP Addresses:** Navigate to `IP > Addresses`. Click `+`, set the address and interface, and press `OK`.
*   **DHCP Server:** Navigate to `IP > DHCP Server`. Click `+`, select the interface, and press `OK`. Then, in `Networks`, click `+` to add network info.
*   **IPv6:** Navigate to `IPv6` > `Settings`. Make sure IPv6 is not disabled. Navigate to `IPv6` > `Addresses`, click `+` and set interface and pool, then press `OK`. Navigate to `IPv6` > `ND`, click `+` and set the interface, check the "Advertise DNS" checkbox, and press `OK`.
*   **Firewall:** Navigate to `IP > Firewall` and add filter rules as needed.

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
/ip address
add address=21.12.92.1/24 interface=wlan-88

/ip pool
add name=dhcp-pool ranges=21.12.92.10-21.12.92.254

/ip dhcp-server
add address-pool=dhcp-pool interface=wlan-88 name=dhcp-wlan-88

/ip dhcp-server network
add address=21.12.92.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=21.12.92.1

/ipv6 settings
set disable-ipv6=no

/ipv6 address
add interface=wlan-88 from-pool=local-pool

/ipv6 nd
add interface=wlan-88 advertise-dns=yes advertise-mtu=1500 other-configuration=yes managed-address=no

/ip firewall filter
add chain=input action=accept comment="Allow established and related connections" connection-state=established,related
add chain=input action=drop comment="Drop all other input connections" in-interface-list=!LAN
add chain=forward action=accept comment="Allow established and related connections" connection-state=established,related
add chain=forward action=drop comment="Drop all other forward connections" connection-state=new connection-nat-state=!dstnat in-interface=wlan-88
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

*   **Pitfalls:**
    *   **Incorrect Interface Selection:** Ensure the correct interface (`wlan-88` in this case) is targeted in all commands.
    *   **DHCP Server Conflict:** Ensure the DHCP range doesn't conflict with static addresses.
    *   **Firewall Misconfiguration:**  Too restrictive rules can block legitimate traffic. Be careful of incorrect chain placement.
    *   **IPv6 DNS:** Double check for proper IPv6 DNS resolution, particularly when working with SLAAC and DHCPv6
    *   **Incorrect MTU:** Ensure correct MTU value is configured for the interfaces and IPv6 MTU configurations.
*   **Troubleshooting:**
    *   **Ping Test:** `ping 21.12.92.1` from a connected client to test connectivity and confirm the assigned IP. `ping6 -I wlan-88 <IPv6 Gateway Address>` to test IPv6 connectivity.
    *   **Torch Tool:** `/tool torch interface=wlan-88` to analyze live traffic on the interface.
    *   **Log:** Check `/system logging print` for any errors or warnings.
    *   **DHCP Leases:** Check active leases in `/ip dhcp-server lease print`.
    *   **IPv6 Neighbors:** Check `/ipv6 nd print` to verify IPv6 neighbor discovery is functioning correctly.
*   **Error Scenario:**
    *   **Scenario:** A client cannot obtain an IP address.
        1.  **Check:**  Verify DHCP is enabled for the correct interface, the pool has available leases, and the firewall isn't blocking DHCP traffic.
        2.  **Action:** Check logs, ping the gateway from the client, check that a default route to the internet is configured and working correctly.

## 5. Verification and Testing Steps

1.  **Client Connection:** Connect a wireless client to the network.
2.  **IP Address Check:** Verify the client obtains an IP address in the 21.12.92.0/24 range. Verify the IPv6 address is automatically configured.
3.  **Ping Router:** Ping the router's address (21.12.92.1) and its IPv6 link-local address from the client.
4.  **Internet Access:** Check that the client can access the internet.
5.  **Traceroute:** Run `traceroute 8.8.8.8` (and `traceroute6 2001:4860:4860::8888`) from the client to verify routing.
6.  **Torch Analysis:** Use `torch` to observe traffic patterns on the `wlan-88` interface.
7.  **Lease Check:** Use `/ip dhcp-server lease print` to confirm DHCP leases are being issued.
8.  **IPv6 Neighbor:** Use `/ipv6 nd print` to check that IPv6 ND is working as intended.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **IP Pools:** Allows for more complex address assignment, with ranges, exclusions, and options for DHCP Server.
*   **Connection Tracking:** Critical for the firewall, tracks state of TCP/UDP connections, allowing more efficient rules.
*   **Queue Management:** Allows prioritization of traffic for Quality of Service (QoS).
*   **Firewall:** Highly granular firewall, can filter based on various criteria (IP, ports, MAC, etc.).
*   **Limitations:**
    *   Hardware limitations can affect performance when dealing with very large traffic loads. Ensure correct hardware selection for your use case.
    *   Overly complex configurations can be hard to maintain and troubleshoot. Keep them simple and well-documented.
*   **Less Common Feature Scenarios:**
    *   **MAC Binding:** Associate specific IP addresses with MAC addresses to provide static leases.
    *   **Hotspot:** Use MikroTik's Hotspot feature for user management and access control.
    *   **VLANs:** Create VLANs on the wireless interface to segment the network for better control, requires tagging on the wlan interface and connected switches.

## 7. MikroTik REST API Examples

*   **Get Interface Configuration:**
    *   **API Endpoint:** `https://<router-ip>/rest/interface`
    *   **Request Method:** `GET`
    *   **Example Response:** (JSON, abbreviated)
        ```json
        [
          {
            "name": "wlan-88",
            "type": "wlan",
            "mtu": 1500,
            "disabled": false,
            "mac-address": "XX:XX:XX:XX:XX:XX",
            "actual-mtu": 1500
          }
        ]
        ```
*  **Get Addresses:**
    *  **API Endpoint:** `https://<router-ip>/rest/ip/address`
    *  **Request Method:** `GET`
    *  **Example Response:** (JSON, abbreviated)
        ```json
            [
                {
                    "address": "21.12.92.1/24",
                    "interface": "wlan-88",
                     "network": "21.12.92.0",
                    "disabled": false,
                    "dynamic": false,
                    "invalid": false,
                    "actual-interface": "wlan-88",
                    "id": "*1"
                }
            ]
        ```
*   **Add a new address:**
   *   **API Endpoint:** `https://<router-ip>/rest/ip/address`
   *   **Request Method:** `POST`
   *   **Example Request JSON Payload:**
        ```json
         {
           "address": "21.12.92.2/24",
           "interface": "wlan-88"
         }
        ```
   *   **Expected Response**
       * Success: Status code 201 with the new object created
       * Error: Status code 4xx or 5xx indicating issue.

*   **Add a new dhcp-server**
   *   **API Endpoint:** `https://<router-ip>/rest/ip/dhcp-server`
   *   **Request Method:** `POST`
   *   **Example Request JSON Payload:**
        ```json
         {
            "name": "dhcp-wlan-88-v2",
            "interface": "wlan-88",
            "address-pool": "dhcp-pool"
         }
        ```
   *   **Expected Response**
       * Success: Status code 201 with the new object created
       * Error: Status code 4xx or 5xx indicating issue.

*   **Note:** Replace `<router-ip>` with the actual IP address or hostname of your MikroTik router. You will also need to ensure the API service is enabled, and login with proper authentication.

## 8. In-Depth Explanations of Core Concepts

*   **Bridging:** MikroTik supports bridging to connect multiple interfaces as one logical segment, but is not used here.
*   **Routing:** In this scenario, all devices route to the MikroTik router, which does the routing to other networks.
*   **Firewall:**
    *   **Chain:** Defines the direction of traffic: input (to the router), output (from the router), and forward (through the router).
    *   **Rules:** Define the action (accept, drop, reject) based on criteria.
    *   **Connection Tracking:**  Keeps track of connections' state. It is vital for security rules, as it is important to allow already established connections, while new connection attempts may need additional verification.
*   **IP Pools:** Allows for more controlled IP address management, and the DHCP server uses these pools to assign IPs.
*   **IPv6 Implementation:** MikroTik fully supports IPv6 including SLAAC and DHCPv6 for address assignment and can route between IPv4 and IPv6, as long as both are configured correctly.
*   **DHCP Server:** Dynamically assigns IPs to clients, simplifying IP management.

## 9. Security Best Practices Specific to MikroTik

*   **Strong Passwords:** Set complex passwords for all router users.
*   **Disable Unnecessary Services:** Disable services you're not using (e.g., telnet, API if not used).
*   **Firewall Hardening:** Implement comprehensive firewall rules, especially for input chain.
*   **Regular Software Updates:** Keep RouterOS updated to patch vulnerabilities.
*   **Limit API Access:** Secure the API by only allowing access from specific IP addresses.
*   **User Management:** Create specific users with limited privileges, avoid using admin for everything.
*   **Address lists:** Create address lists to simplify firewall rules, and for ease of management.
*   **Interface Lists:** Use interface lists to group similar interfaces together.
*  **SSH Key Authentication:** Disable password authentication for SSH connections. Configure SSH keys.
*  **VPN Access:** If remote access is required, use a secure VPN protocol such as Wireguard or IPSec.

## 10. Detailed Explanations and Configuration Examples for Advanced Topics

### IP Addressing (IPv4 and IPv6)

*   **IPv4:**  Addresses are 32-bit. Used extensively throughout networking, despite the shortage of addresses.
*   **IPv6:**  Addresses are 128-bit, offering much more address space, intended to replace IPv4.
*   **Addressing Concepts:** Subnetting (using netmasks to define network boundaries), CIDR notation, Classful vs Classless addressing (not much applicable today), public vs private addressing.
*   **Example:**
    ```mikrotik
     /ip address add address=192.168.1.1/24 interface=ether1
     /ipv6 address add interface=ether1 address=2001:db8::1/64
    ```

### IP Pools

*   **Concept:** Ranges of IP addresses used for various purposes, such as DHCP assignment.
*   **Example:**
    ```mikrotik
    /ip pool add name=my-pool ranges=192.168.10.100-192.168.10.200
    ```
*  **DHCP Server and Pools:** Pools are primarily for the DHCP server. The server will lease IPs from these pools.

### IP Routing

*   **Concept:**  How the router decides where to send traffic to reach its destination network.
*   **Static Routes:**  Manually configured routes.
    ```mikrotik
    /ip route add dst-address=10.10.10.0/24 gateway=192.168.1.2
    ```
*   **Dynamic Routing Protocols:**  (OSPF, BGP, RIP) automatically learn and adapt routes. This is very useful in larger networks where manual maintenance of routes is not feasible.

### IP Settings

*   **Concept:** Global settings, usually pertaining to ICMP, ARP, and fast-path configuration.
*   **Example:**
   ```mikrotik
   /ip settings set allow-fast-path=yes
    ```

### MAC Server

*  **Concept:**  Used for remote MAC address access/configuration.
*  **Use Cases:**  Mainly used for MAC-based management or configuration tools.

### RoMON (Router Management Overlay Network)

*   **Concept:** MikroTik's proprietary tool for managing a network of routers.
*   **Features:**  Centralized management, remote access, device discovery.
*   **Considerations:**  Needs RoMON configuration on each router, less common than other central management tools.

### WinBox

*   **Concept:**  GUI tool to manage MikroTik routers.
*   **Features:**  User-friendly interface, visual configuration, real-time monitoring.
*   **Limitations:** Some advanced configurations may only be done via CLI.

### Certificates

*   **Concept:** Used to secure communication, such as web interfaces and VPNs.
*   **Features:** Self-signed or CA-signed certificates, certificate management.
*   **Security:** Use strong keys and keep certificates up-to-date.

### PPP AAA

*   **Concept:**  Authentication, Authorization, and Accounting for Point-to-Point Protocol connections.
*   **Features:**  User authentication, session management, accounting records.
*   **Considerations:** Commonly used for PPPoE or PPTP services.

### RADIUS

*   **Concept:**  Centralized authentication server.
*   **Features:**  Centralized user management, authorization, and accounting.
*   **Use Cases:**  Used in conjunction with PPP AAA, Hotspot, or other services requiring authentication.

### User / User Groups

*   **Concept:**  Manage users and groups for router access.
*   **Features:**  User levels, password management, group-based permissions.
*   **Security:** Use strong passwords, limit user privileges.

### Bridging and Switching

*   **Concept:**  Combine interfaces into a single logical segment.
*   **Features:**  Forwarding traffic between interfaces, VLAN tagging/untagging.
*   **Limitations:** Can introduce latency compared to routed traffic.
*   **MAC Address Learning:** When a device sends traffic, the switch notes its MAC address and maps it to a physical interface. This enables the switch to forward only necessary traffic, and not every single packet to all ports.
*   **Spanning Tree:** MikroTik offers STP/RSTP/MSTP for loop prevention, and correct port state management.
*   **Example:**
    ```mikrotik
    /interface bridge add name=my-bridge
    /interface bridge port add bridge=my-bridge interface=ether1
    /interface bridge port add bridge=my-bridge interface=ether2
    ```

### MACVLAN

*   **Concept:** Create multiple logical interfaces based on a single physical interface.
*   **Features:** Assign multiple MAC addresses, create separate networks on the same physical interface.
*   **Use Cases:** Useful for containerization and other applications that require logical separation of ports.

### L3 Hardware Offloading

*   **Concept:**  Offload routing and switching tasks from the CPU to specialized hardware.
*   **Benefits:** Increased throughput and reduced CPU usage.
*   **Considerations:** Not all hardware supports L3 offloading, some features might be unavailable when enabled.

### MACsec

*   **Concept:** Layer 2 encryption using MAC addresses.
*   **Features:** Link encryption, and integrity protection.
*   **Security:** Provides strong link-layer security.
*   **Use Cases:** Mainly used in sensitive links or locations where layer-2 attacks are possible.

### Quality of Service (QoS)

*   **Concept:** Prioritize certain traffic types over others.
*   **Features:** Queues, shaping, bandwidth control.
*   **Use Cases:**  Improve quality of service for critical applications, such as VoIP, or lower priority of P2P downloads.
*   **Queues:** The primary tool for QoS on MikroTik routers.
   *   **Simple Queues:** Easy to configure, but limited functionality.
   *   **Queue Tree:** Can create hierarchical queues, providing much more control over traffic.
*   **Example (Simple Queue):**
    ```mikrotik
    /queue simple add name=voip-queue target=192.168.1.0/24 max-limit=500k/500k
    ```
* **Example (Queue Tree)**
    ```mikrotik
    /queue tree add name="parent queue" parent=global
    /queue tree add name="child queue" parent="parent queue" max-limit=2M
    /queue tree add name="voip queue" parent="child queue" packet-mark=voip-packets max-limit=500k
    /mangle add chain=forward action=mark-packet new-packet-mark=voip-packets dst-port=5060
    ```

### Switch Chip Features

*   **Concept:**  Features supported by the switch chip on the router.
*   **Features:** VLAN support, port mirroring, rate limiting, etc.
*   **Considerations:** These vary from device to device, so check the hardware capabilities for your router.
*   **Switching VLANs:** Using switch chip features to handle VLANS, rather than the router CPU will result in improved performance.

### VLAN

*   **Concept:**  Divide a physical network into multiple logical networks.
*   **Features:**  Tagged and untagged VLANs, VLAN trunking.
*   **Use Cases:** Network segmentation, security, manage access control for different networks.
*   **Example:**
    ```mikrotik
    /interface vlan add name=vlan10 vlan-id=10 interface=ether1
    /interface vlan add name=vlan20 vlan-id=20 interface=ether1
    ```

### VXLAN

*   **Concept:** Layer 2 tunneling over an IP network.
*   **Features:** Layer 2 extension across different networks.
*   **Use Cases:** Virtualized environments, connecting networks across WAN links.
*   **Example:**
    ```mikrotik
    /interface vxlan add name=vxlan10 vni=1000 interface=ether1
    ```

### Firewall and Quality of Service

*   **Connection Tracking:** Track the state of each connection.
*   **Firewall:** Layer 3 and 4 firewall to filter traffic.
*   **Packet Flow:** `Input` (traffic that goes to the router), `Output` (traffic initiated by the router) and `Forward` (traffic going through the router).
*   **Queues:**  (see above).
*   **Firewall and QoS Case Studies:** Prioritizing VoIP, dropping P2P traffic, etc.
*   **Kid Control:** Limit access time of devices using time-based firewall rules or scheduler.
*   **UPnP/NAT-PMP:** Automatically configure port forwards for connected devices. Use caution when enabling this feature.

### IP Services (DHCP, DNS, SOCKS, Proxy)

*   **DHCP:** Dynamically assigning IP addresses to devices.
    *   **DHCP Relay:** Forwards DHCP requests to a different server.
*   **DNS:** Domain Name resolution.
    *   **DNS Cache:** Store resolved names for faster access, reducing latency.
    *   **DNS Server:**  Configures a local DNS server, and allows static DNS entries.
*   **SOCKS Proxy:** An intermediary between client and the target server. Can be used to access resources that are only available from certain IPs.
*   **Web Proxy:** An intermediary that can filter and cache web traffic. Very useful when you want to do detailed web traffic monitoring or filtering.

### High Availability Solutions

*   **Load Balancing:** Distribute traffic across multiple links or servers.
*   **Bonding:** Combine multiple links into a single logical link.
    *   **Example:**
         ```mikrotik
        /interface bonding add name=bond1 mode=802.3ad slaves=ether1,ether2
        ```
*  **HA Case Studies:** Combine multiple devices for fail-over protection and increased availability.
*   **Multi-Chassis Link Aggregation Group (MLAG):** Combine links from multiple switches.
*   **VRRP (Virtual Router Redundancy Protocol):**  Provide backup routing using virtual IP addresses.

### Mobile Networking

*   **GPS:** Capture GPS coordinates.
*   **LTE:** Connect to mobile networks using LTE modems, and control LTE device parameters (APN, band selection).
*   **PPP:** Used for dial-up connections (typically with older mobile technologies) and PPP over Ethernet (PPPoE).
*   **SMS:** Send and receive SMS messages (useful for remote diagnostics and triggers).
*   **Dual SIM Application:** Configure and prioritize usage of two different SIM cards.

### Multi Protocol Label Switching - MPLS

*   **MPLS Overview:** Route packets using labels instead of IP addresses.
*   **MPLS MTU:** Set Maximum Transmission Unit for MPLS traffic.
*   **Forwarding and Label Bindings:** How labels are assigned and packets are forwarded.
*   **EXP bit and MPLS Queuing:** How to prioritize MPLS traffic.
*   **LDP (Label Distribution Protocol):**  Used to exchange labels between MPLS routers.
*   **VPLS (Virtual Private LAN Service):**  Connect multiple LANs over an MPLS network, acting like one giant LAN segment.
*   **Traffic Eng (Traffic Engineering):** Control the path of MPLS traffic.
*   **MPLS Reference:**  MPLS specifications and best practices.

### Network Management

*   **ARP:** Resolves IP addresses to MAC addresses.
*   **Cloud:** Manage devices via MikroTik's cloud platform.
*   **DHCP:** See above.
*   **DNS:** See above.
*   **SOCKS Proxy:** See above.
*   **Web Proxy:** See above.
*   **Openflow:** For software defined networks using the OpenFlow protocol.

### Routing

*   **Routing Protocol Overview:** OSPF, RIP, BGP, RPKI.
*   **Moving from ROSv6 to v7:** Configuration and feature differences between major versions of RouterOS.
*   **Routing Protocol Multi-core Support:** How routing protocols take advantage of multi-core CPUs for enhanced performance.
*   **Policy Routing:** Routing based on multiple criteria (source/destination IP, interface, etc).
*   **Virtual Routing and Forwarding (VRF):**  Create multiple virtual routing tables on the same router.
*  **OSPF:** A link-state routing protocol used mainly in large internal networks.
*  **RIP:** Distance vector routing protocol. Commonly found in older networks.
*  **BGP:** A path vector routing protocol used to interconnect Autonomous Systems on the internet.
*  **RPKI:** Resource Public Key Infrastructure to validate BGP routes.
*   **Route Selection and Filters:** Manipulating routes and preventing routing loops.
*   **Multicast:** Sending traffic to multiple destinations.
*  **Routing Debugging Tools:** Tools to diagnose routing problems (logging, traffic analysis, `traceroute`, `ping`).
*  **Routing Reference:** MikroTik documentation for routing protocols.
*   **BFD (Bidirectional Forwarding Detection):** Used to detect link failures between devices rapidly.
*   **IS-IS (Intermediate System to Intermediate System):** Another link-state routing protocol, commonly used in large internal networks, and by ISPs.

### System Information and Utilities

*   **Clock:** Configure time and timezones.
*   **Device-mode:** Different operating modes that MikroTik routers support.
*   **E-mail:** Configure the router to send emails, for alerts and notifications.
*   **Fetch:** Download files over HTTP/HTTPS or FTP.
*   **Files:** Manage files on the router storage.
*   **Identity:** Set the router's name.
*   **Interface Lists:** (See above).
*   **Neighbor Discovery:** Detect other MikroTik routers on the network.
*   **Note:** Leave a system message, so the user knows the purpose and settings when logging in.
*   **NTP:** Network Time Protocol.
*   **Partitions:** Manage partitions on the router storage.
*   **Precision Time Protocol:** High accuracy time synchronization.
*   **Scheduler:** Run commands at specific times or intervals.
*   **Services:** Configure different services running on the router (API, telnet, SSH, winbox).
*   **TFTP:** Trivial File Transfer Protocol.

### Virtual Private Networks (VPN)

*   **6to4:**  An IPv6 transition mechanism.
*   **EoIP (Ethernet over IP):** Tunnel layer 2 traffic.
*   **GRE (Generic Routing Encapsulation):** Used to encapsulate various network layer protocols.
*   **IPIP (IP in IP):** Tunnel IPv4 packets in an IPv4 header.
*   **IPsec:** A robust VPN protocol for secure, encrypted connections.
*   **L2TP (Layer 2 Tunneling Protocol):**  Used for remote access.
*   **OpenVPN:** A powerful, open-source VPN protocol.
*   **PPPoE:** Common protocol for connecting to ISPs, primarily using ADSL.
*   **PPTP:** Older and less secure VPN protocol.
*   **SSTP (Secure Socket Tunneling Protocol):** VPN protocol used mainly on Microsoft platforms.
*   **WireGuard:** Modern, and secure VPN protocol.
*   **ZeroTier:** A software defined networking platform for connecting various devices across networks.

### Wired Connections

*   **Ethernet:** Standard wired interface, commonly used with routers.
*   **MikroTik wired interface compatibility:** Hardware limitations for certain MikroTik devices.
*   **PWR Line:** MikroTik's proprietary way to deliver power and data over a standard two-wire cable.

### Wireless

*   **WiFi:** Various Wi-Fi settings, and configuration options.
*   **Wireless Interface:** Configurations for wireless cards in router.
*   **W60G:** High speed, short range 60 GHz Wireless.
*   **CAPsMAN:** Manage multiple APs from a single device.
*   **HWMPplus mesh:** MikroTik's proprietary mesh protocol.
*   **Nv2:** MikroTik proprietary protocol used for Point to Point connections.
*   **Interworking Profiles:** Allow devices to connect based on pre-defined profiles, mostly applicable in larger networks.
*   **Wireless Case Studies:** Implementations of wireless networks.
*   **Spectral scan:** Scan for wireless interference on the spectrum.

### Internet of Things (IoT)

*  **Bluetooth:** Connecting to Bluetooth devices.
*  **GPIO (General Purpose Input/Output):** Control external hardware with the router.
*  **Lora:** Wide area, low power, low bandwidth wireless communication protocol.
*  **MQTT:**  Message Queuing Telemetry Transport - a standard protocol used for IoT communications.

### Hardware

*   **Disks:** Manage local storage for logs or files.
*   **Grounding:** Importance of proper grounding in order to protect against electrical damage.
*   **LCD Touchscreen:** If your device has an LCD, how to configure the screen.
*   **LEDs:** How to use LED indicators to monitor devices.
*   **MTU in RouterOS:** How to configure the Maximum Transmission Unit (MTU), to avoid packet fragmentation.
*   **Peripherals:** Compatibility of connected USB peripherals (e.g., 3G/4G modems).
*   **PoE-Out:** Power other devices via ethernet.
*   **Ports:** Management of physical ports.
*   **Product Naming:** MikroTik's device naming scheme.
*   **RouterBOARD:** Hardware platform overview.
*   **USB Features:** How to utilize USB ports on routers.

### Diagnostics, monitoring and troubleshooting

*   **Bandwidth Test:** Measure throughput of connections.
*   **Detect Internet:** Checks if the router can reach the internet.
*   **Dynamic DNS:** Update dynamic DNS entries, whenever IP address is changed.
*   **Graphing:** Visualize performance and bandwidth over time.
*   **Health:** Monitor system health (CPU, memory, etc).
*   **Interface stats and monitor-traffic:** Detailed traffic statistics on interfaces, and visualization of live traffic.
*   **IP Scan:** Discover devices on the network.
*   **Log:** Centralized router logs for troubleshooting.
*   **Netwatch:** Monitor the state of network connections, and take actions based on state.
*   **Packet Sniffer:** Capture network traffic for detailed inspection.
*   **Ping:** Standard ICMP ping tool for connectivity tests.
*   **Profiler:** Analyze performance of individual processes.
*   **Resource:** System resource utilization.
*  **SNMP (Simple Network Management Protocol):** Remote management and monitoring.
*   **Speed Test:** Testing the connection speed to the router.
*   **S-RJ10 general guidance:** Guidance on using S-RJ10 ports on routers.
*   **Torch:** Live traffic monitoring.
*  **Traceroute:** Trace path to a destination.
*   **Traffic Flow:** Monitor network traffic flow in real time.
*   **Traffic Generator:** Generate traffic for testing.
*   **Watchdog:** Automatically reboot the router in case of a system failure or lockup.

### Extended Features

*   **Container:**  