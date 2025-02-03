Okay, this is a comprehensive request, and I'm going to deliver a robust document covering the breadth of your needs, focusing on RouterOS 7.12 and a hypothetical ISP environment as the scale. Let's dive in!

# MikroTik RouterOS 7.12: Comprehensive Technical Documentation for IP Addressing and Beyond (ISP Focus)

This document is designed for an ISP environment using MikroTik RouterOS 7.12 (or a similar version). It will cover IP addressing, related topics, and other aspects of MikroTik configuration as requested. The configuration level is targeted towards 'Basic', assuming general familiarity with networking concepts.

## 1. Comprehensive Configuration Scenario & MikroTik Requirements

**Scenario:** A small ISP is setting up a new customer-facing router. This router will:

*   Receive an upstream IPv4 and IPv6 connection from the core network.
*   Provide IPv4 and IPv6 addresses to customer routers via DHCP.
*   Implement a basic firewall for security.
*   Implement IP Pools for address allocation.
*   Establish basic routing to reach internet resources.

**MikroTik Requirements:**

*   RouterOS version 7.12 or 7.x or 6.x.
*   A configured WAN interface connected to the internet.
*   A configured LAN interface for customer connections.
*   Basic security measures.
*   IP Pools and DHCP servers for IPv4 and IPv6 address allocation.

## 2. Step-by-Step MikroTik Implementation (CLI & Winbox)

**A. Initial Setup (CLI):**

1.  **Connect to the Router:** Use SSH or Serial to connect to your MikroTik router.
2.  **Set Router Identity:**

    ```mikrotik
    /system identity set name=isp-router
    ```

3.  **Disable Default Configuration:**

    ```mikrotik
    /system reset-configuration skip-backup=yes
    ```

    **Note:** This will reset your router to the default config. Be cautious.

**B. Interface Configuration (CLI/Winbox):**

1.  **Identify Interfaces:**
    *   Assume `ether1` is the WAN interface connecting to the internet and `ether2` is the LAN interface connecting to clients.
    *  In Winbox, go to `Interfaces`, click `+` to add an interface if needed and then configure it accordingly.

2. **WAN Interface Configuration (CLI):**
  * Assuming you are receiving an IP dynamically from your provider:

     ```mikrotik
      /ip dhcp-client
      add interface=ether1 disabled=no
      ```
    *   If you are receiving a static IP from your provider:
    ```mikrotik
     /ip address
     add address=YOUR_WAN_IP/YOUR_WAN_MASK interface=ether1
     /ip route add gateway=YOUR_WAN_GATEWAY
    ```
      Replace `YOUR_WAN_IP/YOUR_WAN_MASK` with your IP address and mask and replace `YOUR_WAN_GATEWAY` with your default gateway.

3.  **LAN Interface Configuration (CLI):**

    ```mikrotik
    /ip address
    add address=192.168.88.1/24 interface=ether2
    ```
    In Winbox, go to `IP` -> `Addresses`, click `+` and configure the same information.

4.  **IPv6 Interface Configuration**
  * IPv6 addressing often uses static configurations. This assumes you have been given an IPv6 prefix:

    ```mikrotik
    /ipv6 address
    add address=YOUR_IPv6_ADDRESS/PREFIX_LENGTH interface=ether1
    /ipv6 route
    add dst-address=::/0 gateway=YOUR_IPv6_GATEWAY
    /ipv6 address
    add address=2001:db8::1/64 interface=ether2
     ```
      Replace `YOUR_IPv6_ADDRESS/PREFIX_LENGTH` with the IP address and prefix and replace `YOUR_IPv6_GATEWAY` with your IPv6 default gateway.
     In Winbox, go to `IPv6` -> `Addresses` and `IPv6` -> `Routes` and add the entries.

**C. IP Pool Configuration (CLI/Winbox):**

1.  **IPv4 Pool:**

    ```mikrotik
    /ip pool
    add name=customer_ipv4_pool ranges=192.168.88.10-192.168.88.254
    ```
    In Winbox, go to `IP` -> `Pool`, click `+` and fill in the same information.

2.  **IPv6 Pool:**

    ```mikrotik
    /ipv6 pool
    add name=customer_ipv6_pool prefix=2001:db8::/64 prefix-length=64
    ```
     In Winbox, go to `IPv6` -> `Pool`, click `+` and fill in the same information.

**D. DHCP Server Configuration (CLI/Winbox):**

1.  **IPv4 DHCP Server:**

    ```mikrotik
    /ip dhcp-server
    add address-pool=customer_ipv4_pool interface=ether2 name=dhcp_lan
    /ip dhcp-server network
    add address=192.168.88.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.88.1
    ```
    In Winbox, go to `IP` -> `DHCP Server` and then to `Networks`, and configure accordingly.

2.  **IPv6 DHCP Server (DHCPv6 Server/Router Advertisements):**

    ```mikrotik
    /ipv6 dhcp-server
    add address-pool=customer_ipv6_pool interface=ether2 name=dhcpv6_lan
    /ipv6 dhcp-server settings
    set dns-server=2001:4860:4860::8888,2001:4860:4860::8844
    /ipv6 nd
    set interface=ether2 ra-interval=30s managed-address-flag=yes other-config-flag=yes
    ```
    In Winbox go to `IPv6` -> `DHCP Server` and configure accordingly, and go to `IPv6` -> `ND` and make sure that Router Advertisements are enabled.

**E. Basic Firewall (CLI/Winbox):**
1. **Accept established and related connections:**
```mikrotik
 /ip firewall filter
 add chain=forward action=accept connection-state=established,related
```
2. **Accept input on loopback:**
```mikrotik
/ip firewall filter
add chain=input action=accept in-interface=loopback
```
3. **Block all other input to the router (prevent remote management):**
```mikrotik
/ip firewall filter
add chain=input action=drop
```
4. **Allow forward traffic to the internet**
```mikrotik
 /ip firewall filter
 add chain=forward action=accept out-interface=ether1
```
5. **Drop everything else**
```mikrotik
/ip firewall filter
add chain=forward action=drop
```
   In Winbox, go to `IP` -> `Firewall`, and configure the rules in `Filter Rules`.

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
# System Identity
/system identity set name=isp-router

# Disable Default Configuration
/system reset-configuration skip-backup=yes

# WAN Interface Configuration
/ip dhcp-client
add interface=ether1 disabled=no
# or static IP
# /ip address
# add address=YOUR_WAN_IP/YOUR_WAN_MASK interface=ether1
# /ip route add gateway=YOUR_WAN_GATEWAY

# LAN Interface Configuration
/ip address
add address=192.168.88.1/24 interface=ether2

# IPv6 Interface Configuration
/ipv6 address
add address=YOUR_IPv6_ADDRESS/PREFIX_LENGTH interface=ether1
/ipv6 route
add dst-address=::/0 gateway=YOUR_IPv6_GATEWAY
/ipv6 address
add address=2001:db8::1/64 interface=ether2

# IP Pool Configuration
/ip pool
add name=customer_ipv4_pool ranges=192.168.88.10-192.168.88.254

/ipv6 pool
add name=customer_ipv6_pool prefix=2001:db8::/64 prefix-length=64

# DHCP Server Configuration
/ip dhcp-server
add address-pool=customer_ipv4_pool interface=ether2 name=dhcp_lan
/ip dhcp-server network
add address=192.168.88.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.88.1

/ipv6 dhcp-server
add address-pool=customer_ipv6_pool interface=ether2 name=dhcpv6_lan
/ipv6 dhcp-server settings
set dns-server=2001:4860:4860::8888,2001:4860:4860::8844
/ipv6 nd
set interface=ether2 ra-interval=30s managed-address-flag=yes other-config-flag=yes

# Firewall Rules
/ip firewall filter
add chain=input action=accept in-interface=loopback
add chain=forward action=accept connection-state=established,related
add chain=forward action=accept out-interface=ether1
add chain=input action=drop
add chain=forward action=drop

```

## 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Incorrect Interface Selection:** Ensure you choose the correct interfaces for WAN and LAN.
*   **Conflicting IP Addresses:** Avoid overlapping IP ranges.
*   **Firewall Rules:** Incorrect rules can block essential traffic.
*   **Forgotten DHCP Settings:** DNS, gateway, and network settings must be correct.
*   **IPv6 Configuration:** Proper prefix delegation, and IPv6 addressing and routing are critical.
* **Unreachable default gateway**: In case you use static IP addressing, incorrect configuration of the default gateway prevents the router from accessing internet resources.

**Troubleshooting:**

*   **Check Interfaces:** Use `/interface print` to verify status.
*   **Ping:** Use `/ping` to check connectivity to gateways and other IPs.
*   **Traceroute:** Use `/tool traceroute` to trace paths to destinations.
*   **Torch:** Use `/tool torch` to view live packet captures.
*   **DHCP Leases:** Use `/ip dhcp-server lease print` to view issued DHCP addresses.
*   **Firewall logs**: Enable firewall logs and check them for any blocked connections.
*  **Route print**: Use `/ip route print` and `/ipv6 route print` to verify the routing table.
*   **Logs:** Use `/system logging print` to view system logs and identify potential problems.
*   **Connection Tracking:** Use `/ip firewall connection print` to observe active connections.

**Diagnostics:**

*   `/system resource print` : To check CPU, memory, and storage usage.
*   `/interface monitor-traffic` : Monitor real-time interface traffic.
*  `/tool profile`: To identify performance bottlenecks within the router.

## 5. Verification and Testing Steps (MikroTik Tools)

1.  **Connectivity Check:**
    *   Ping the WAN gateway using `/ping <WAN_GATEWAY_IP>`.
    *   Ping an external IP (e.g., `8.8.8.8`) using `/ping 8.8.8.8`.
     *   Ping an IPv6 external IP (e.g., `2001:4860:4860::8888`).
    *   Traceroute to an external IP (`/tool traceroute 8.8.8.8`).
    *   From a connected client, check if you are receiving IP addresses via DHCP.
    *  Test internet access from a client.
2.  **DHCP Server Check:**
    *  Check lease information on the router by running `/ip dhcp-server lease print`.
    *  Verify that client machines are receiving DHCP leases in their network settings.
3.  **Firewall Check:**
    *  Use torch to capture traffic and verify if firewall rules are working as expected.
    * Check firewall statistics using `/ip firewall connection print`.
4.  **IPv6 Check**
   * Verify that client machines are receiving IPv6 addresses using Router Advertisements or DHCPv6.
   * Ping an IPv6 external IP (e.g., `2001:4860:4860::8888`) from a client.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

**Features:**

*   **RouterOS:** Highly flexible, feature-rich OS.
*   **Firewall:** Statefull firewall for complex traffic management.
*   **QoS:** Advanced queues for traffic prioritization.
*   **Routing:** Support for static and dynamic routing protocols (OSPF, BGP, etc).
*   **VPN:** Comprehensive VPN capabilities (IPsec, L2TP, OpenVPN, Wireguard).
*   **Scripting:** Allows automation via scripting language.
*   **Winbox:** User-friendly GUI for configuration.
*  **REST API:** Access to the router from external applications.

**Capabilities:**

*   Handles large numbers of connections.
*   Complex routing and filtering.
*   Multiple VPN tunnels.
*   Traffic shaping.

**Limitations:**

*  Some hardware may have performance limitations.
*  Advanced features require technical expertise.
*  Certain features may have license constraints.

## 7. MikroTik REST API Examples

**A. Retrieve Interface List (GET)**

*   **Endpoint:** `/interface`
*   **Method:** `GET`
*   **Request (via curl):**

    ```bash
    curl -k -u admin:<password> https://<router_ip>/rest/interface
    ```

*   **Expected Response (JSON):**

    ```json
    [
        {
            "id": "*0",
            "name": "ether1",
            "type": "ether",
            "mtu": "1500",
            "actual-mtu": "1500",
            "mac-address": "C8:2A:14:XX:XX:XX",
             "enabled": true,
             "running": true
        },
        {
            "id": "*1",
            "name": "ether2",
            "type": "ether",
            "mtu": "1500",
            "actual-mtu": "1500",
            "mac-address": "C8:2A:14:YY:YY:YY",
            "enabled": true,
            "running": true
        }
    ]
    ```

**B. Update Interface Configuration (POST)**

*   **Endpoint:** `/interface/ether1` (Note: Use the full path, like `ether1` instead of the ID)
*   **Method:** `POST`
*   **Request (via curl):**

    ```bash
    curl -k -u admin:<password> -H "Content-Type: application/json" -X POST -d '{"disabled": true}' https://<router_ip>/rest/interface/ether1
    ```

*   **Example JSON Payload:**

    ```json
    {"disabled": true}
    ```

*   **Expected Response (JSON):**

    ```json
        {
            "id": "*0",
             "name": "ether1",
             "type": "ether",
            "mtu": "1500",
            "actual-mtu": "1500",
            "mac-address": "C8:2A:14:XX:XX:XX",
            "enabled": false,
            "running": false
        }
    ```

**C. Add IP Address (POST)**
*   **Endpoint:** `/ip/address`
*   **Method:** `POST`
*   **Request (via curl):**
 ```bash
 curl -k -u admin:<password> -H "Content-Type: application/json" -X POST -d '{"address": "192.168.90.1/24", "interface":"ether2"}' https://<router_ip>/rest/ip/address
 ```
*   **Example JSON Payload:**
    ```json
      {"address": "192.168.90.1/24", "interface":"ether2"}
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "id": "*5",
        "address": "192.168.90.1/24",
        "interface": "ether2",
         "network":"192.168.90.0"
    }
    ```

## 8. In-Depth Explanations of Core Concepts (MikroTik Focus)

*   **Bridging:** Combines multiple interfaces into one logical interface, operating at Layer 2. In MikroTik, you create a `bridge` interface and add physical or virtual interfaces as bridge ports. Traffic within a bridge is switched based on MAC addresses.
*   **Routing:**  Directs traffic between networks based on IP addresses. MikroTik has a powerful routing engine supporting static routes and dynamic protocols like OSPF, RIP, and BGP.
*   **Firewall:** Statefull packet filter which keeps track of connections and their state. In MikroTik, firewall rules are arranged in chains and processed top-down, acting as gatekeepers for traffic.
*   **IP Addressing:** MikroTik supports both IPv4 and IPv6. Addresses are assigned to interfaces, and routing decisions are based on source and destination IPs. MikroTik also provides IP pools for dynamic address allocation.
*   **DHCP:** MikroTik acts as DHCP server for client address allocation, and also a DHCP client to receive IPs.
* **Connection tracking:** RouterOS maintains a table of ongoing connections and utilizes it for stateful firewall inspection.
* **Packet Flow:** Packets traverse through various stages in RouterOS, including input, output, and forward chains based on the packet's direction, and are processed by the firewall and routing.

## 9. Security Best Practices

*   **Change Default Password:** The default admin password must be changed upon setup.
*   **Disable Unnecessary Services:** Disable unused services.
*   **Firewall Rules:** Implement a proper firewall with both input and forward rules.
*   **Strong Passwords:**  Use strong and unique passwords for all user accounts.
*   **Limit Access:** Limit access to the router management interfaces.
*   **Regular Updates:** Keep RouterOS updated with the latest security patches.
*   **SSH Key-Based Authentication:**  Use SSH keys for secure access.
*   **Disable Telnet:**  Use SSH instead.
*  **VPN for Remote Access**: Use secure VPN protocols for remote management, instead of exposing services publicly.
* **Monitor Logs:** Regularly monitor and analyze the system logs for suspicious activity.
* **Implement Rate Limiting:** Implement rate limiting to protect the router from DDoS attacks.

## 10. Detailed Explanations and Configuration Examples

This section expands on the requested topics:

### IP Addressing (IPv4 and IPv6)

*   **IPv4:** 32-bit addresses, traditionally used.  Configured using `/ip address`.  Includes `address`, `interface`, and `network` properties.
*   **IPv6:** 128-bit addresses, uses colon-hexadecimal notation.  Configured using `/ipv6 address`.  Includes `address`, `interface`, and `prefix-length` properties.

### IP Pools

*   **IPv4 Pools:** Define ranges of IPv4 addresses for DHCP distribution. Use `/ip pool`. Parameters include `name` and `ranges`
*   **IPv6 Pools:** Define prefixes of IPv6 addresses. Use `/ipv6 pool`. Parameters include `name`, `prefix` and `prefix-length`.

### IP Routing

*   **Static Routing:** Explicitly defined routes to specific destinations. Use `/ip route`. Can be implemented using `/ipv6 route`.
*   **Dynamic Routing:** Uses protocols (OSPF, BGP, RIP) to learn routes. MikroTik implements most of the common routing protocols. Use `/routing ospf`, `/routing bgp` and `/routing rip` respectively.
*   **Policy Based Routing:** Routes traffic differently based on source, destination, or other parameters using `routing policy-based-routing`.
*   **VRF (Virtual Routing and Forwarding):** Allows multiple routing tables on the same router `/routing vrf`.

### IP Settings

*   Global IP settings on `/ip settings`.
*   Contains flags for fast-track, connection tracking, TCP settings, ICMP settings, and other parameters.
*  Can be used to tweak the global networking behavior of the router.

### MAC server

*   Allows management and configuration of the router using MAC address.
*   Accessible via winbox or by using MikroTik discovery tools.
*   Can be enabled using `/tool mac-server`.

### RoMON

*   MikroTik's proprietary remote management tool for RouterBoards.
*   Allows access to management interfaces even when IP connectivity is lost.
*   Can be configured using `/tool romon`.

### WinBox

*   Graphical user interface for MikroTik configuration.
*   Connects via IP or MAC addresses.
*   Supports drag-and-drop, and easy configuration of most RouterOS features.
*   Available for Windows, Linux, and macOS.
*   Can be downloaded from the MikroTik website.

### Certificates

*   Used for secure communication (HTTPS, VPNs, etc.).
*   Can generate self-signed certificates or import certificates from a CA (Certificate Authority).
*  Managed under `/certificate`.

### PPP AAA

*   AAA (Authentication, Authorization, and Accounting) for PPP connections.
*   Used for secure authentication of PPP clients.
*   Can use local user database or external servers (RADIUS).
*  Managed under `/ppp aaa`.

### RADIUS

*   Used for centralized authentication.
*   Allows MikroTik to authenticate users via a RADIUS server.
*   Can be used for PPP, hotspot, and other services.
*  Configured under `/radius`.

### User / User groups

*   Manages user accounts for access to the router.
*   Users can be part of a group.
*   Permissions can be set on user or group level.
*   Can be configured using `/user` and `/user group`.

### Bridging and Switching

*   **Bridging:**  Combines multiple interfaces into one Layer 2 network.
*   **Switching:** Hardware-accelerated forwarding of packets on the same broadcast domain.
*   `/interface bridge` is the primary command for bridging.

### MACVLAN

*   Creates virtual network interfaces associated with a physical interface on the MAC layer.
*   Used to provide multiple MAC addresses on the same physical interface.
*  Managed using `/interface macvlan`.

### L3 Hardware Offloading

*   Offloads routing to specialized hardware for increased throughput.
*  Enabled per interface under `/interface ethernet`.

### MACsec

*   Provides data encryption on the MAC layer.
*   Secures traffic between directly connected switches.
*  Managed under `/interface macsec`.

### Quality of Service

*   Traffic shaping and prioritizing for bandwidth management.
*   Implemented using queues, PCQ, HTB, and other features under `/queue`.

### Switch Chip Features

*   Provides access to hardware switch chip features.
*   VLAN filtering, port mirroring, and other functions.
*   Can be configured via `/interface ethernet switch`.

### VLAN

*   Segment the network into different Layer 2 broadcast domains.
*   Uses VLAN IDs.
*   Can be used in bridges or switch chips using `/interface vlan`.

### VXLAN

*   Layer 2 network overlay using UDP tunnels.
*   Used for extending Layer 2 networks across Layer 3.
*  Configured under `/interface vxlan`.

### Firewall and Quality of Service

* **Connection Tracking**: Tracks network connections and its state, used by the stateful firewall.
* **Firewall**: Implements packet filtering based on various criteria such as IP, port, connection state, etc. Implemented using `/ip firewall filter`.
* **Packet Flow in RouterOS**: Describes how packets move through the system, from interface input to output with multiple hooks (prerouting, input, forward, output, postrouting).
* **Queues**: Used to manage bandwidth and prioritize traffic using various techniques, such as simple queues, queue tree, PCQ etc.
* **Firewall and QoS Case Studies**: Applying firewall and QoS in real-world scenarios, such as limiting torrent traffic.
* **Kid Control**: Simple way to control and limit internet access for specific devices, based on MAC addresses. Can be implemented using simple queues, parent queue, and time ranges.
* **UPnP**: Universal Plug and Play to allow clients to request port forwards from the router automatically. Controlled via `/ip upnp`.
* **NAT-PMP**: NAT Port Mapping Protocol, an alternative to UPnP. Controlled via `/ip natpmp`.

### IP Services (DHCP, DNS, SOCKS, Proxy)

*   **DHCP:**  Dynamic Host Configuration Protocol for IP assignment, use `/ip dhcp-server`.
*   **DNS:** Domain Name System server for hostname resolution, use `/ip dns`.
*   **SOCKS:**  SOCKS proxy server, use `/ip socks`.
*   **Proxy:** HTTP proxy server, use `/ip proxy`.

### High Availability Solutions

*   **Load Balancing**: Distributes network traffic across multiple paths or links. Can be implemented using Policy Routing, ECMP, and other techniques.
*   **Bonding**: Aggregates multiple interfaces into a single logical link for increased bandwidth or redundancy. Can be configured under `/interface bonding`.
*   **Bonding Examples**: Example bonding configurations such as 802.3ad, active-backup, etc.
*   **HA Case Studies**: Applying high availability solutions in real-world scenarios, such as redundant internet connections, etc.
*  **Multi-chassis Link Aggregation Group**: Bonding multiple links from different switches to a single device.
*   **VRRP**: Virtual Router Redundancy Protocol that provides redundancy for gateway address. Can be implemented using `/interface vrrp`.
*   **VRRP Configuration Examples**: Example VRRP setups.

### Mobile Networking

*   **GPS:**  Provides location data using GPS receiver, under `/system gps`.
*   **LTE:**  4G/LTE mobile connectivity using integrated modems under `/interface lte`.
*  **PPP**: Point-to-Point Protocol for point-to-point connections over serial or wireless interfaces. Configured using `/ppp`.
*   **SMS:** Sending and receiving SMS messages over LTE connections. Configured under `/tool sms`.
*   **Dual SIM Application**: Using dual SIM LTE modules.

### Multi Protocol Label Switching - MPLS

*   **MPLS Overview**: Layer 2.5 protocol for traffic engineering and fast packet forwarding.
*  **MPLS MTU**: Configuring MPLS MTU settings.
*   **Forwarding and Label Bindings**: Mechanism for labels and forwarding paths.
*   **EXP bit and MPLS Queuing**: Using the EXP bits for traffic prioritisation.
*   **LDP**: Label Distribution Protocol for dynamic label distribution. Configured using `/mpls ldp`.
*  **VPLS**: Virtual Private LAN service, allows transparent LAN connection between different locations, configured using `/mpls vpls`.
*  **Traffic Eng**:  Traffic engineering with MPLS for bandwidth optimisation, configured under `/mpls traffic-eng`.
*  **MPLS Reference**: Documentation and materials.

### Network Management

*   **ARP:** Address Resolution Protocol for mapping IP addresses to MAC addresses under `/ip arp`.
*   **Cloud:** MikroTik Cloud service for managing devices remotely using `/cloud`.
*   **DHCP:** Dynamic Host Configuration Protocol, configured under `/ip dhcp-server`.
*   **DNS:** Domain Name System, configured using `/ip dns`.
*   **SOCKS:** SOCKS proxy server, under `/ip socks`.
*   **Proxy:** HTTP proxy server, under `/ip proxy`.
* **Openflow**: Software-defined networking protocol that allows remote management of network flow. Can be configured under `/interface openflow`.

### Routing

*   **Routing Protocol Overview**: Introduction to static and dynamic routing protocols.
* **Moving from ROSv6 to v7 with examples**: Guidelines and examples to make the transition from ROSv6 to ROSv7, including significant differences.
*   **Routing Protocol Multi-core Support**: Using multiple CPU cores for improved routing performance.
*  **Policy Routing**:  Routing packets based on source and other parameters. Can be configured using `/routing policy-based-routing`.
*  **Virtual Routing and Forwarding - VRF**: Provides separation of routing tables, can be configured using `/routing vrf`.
* **OSPF**: Open Shortest Path First routing protocol, can be configured using `/routing ospf`.
* **RIP**: Routing Information Protocol, can be configured under `/routing rip`.
* **BGP**: Border Gateway Protocol used for routing between different autonomous systems, configured under `/routing bgp`.
*   **RPKI:**  Resource Public Key Infrastructure for validating route origins, can be configured under `/routing bgp rpkivalidator`.
*   **Route Selection and Filters**: Controlling routes using filtering mechanisms.
*  **Multicast**: Sending a single message to a group of recipients. Configured using `/routing multicast`.
*  **Routing Debugging Tools**: Tools for diagnosing and debugging routing issues.
* **Routing Reference**: Official documentation and materials about routing.
*  **BFD**: Bidirectional Forwarding Detection for quick failure detection in routing adjacencies, using `/routing bfd`.
* **IS-IS**: Intermediate System to Intermediate System routing protocol. Configured under `/routing isis`.

### System Information and Utilities

*   **Clock:** Setting time and timezone using `/system clock`.
*   **Device-mode:**  Switching between router and device mode. `/system device-mode`.
*   **E-mail:** Configuring SMTP settings for email notifications under `/system email`.
*   **Fetch:** Retrieving files over HTTP and HTTPS under `/tool fetch`.
*   **Files:** Managing router files under `/file`.
*   **Identity:**  Setting router name under `/system identity`.
*   **Interface Lists:** Organizing interfaces into lists for easier management under `/interface list`.
*  **Neighbor Discovery**: Detecting nearby devices using MikroTik Discovery Protocol, under `/ip neighbor`.
* **Note**: Adding custom notes to the router settings, under `/system note`.
*   **NTP:** Network Time Protocol client for time synchronization under `/system ntp client`.
*   **Partitions:** Managing router storage partitions under `/system partition`.
*   **Precision Time Protocol**: High precision time synchronization protocol using `/system ptp`.
*  **Scheduler**:  Scheduling tasks to be executed at certain times or intervals, under `/system scheduler`.
*   **Services:** Enabling and disabling various services under `/ip service`.
* **TFTP**: Trivial File Transfer Protocol server for transferring files, under `/ip tftp`.

### Virtual Private Networks

*   **6to4:** IPv6 transition protocol, under `/ipv6 6to4`.
*   **EoIP:** Ethernet over IP tunneling, under `/interface eoip`.
*   **GRE:** Generic Routing Encapsulation, under `/interface gre`.
*   **IPIP:** IP-in-IP tunneling, under `/interface ipip`.
*   **IPsec:** Secure VPN protocol, under `/ip ipsec`.
*   **L2TP:** Layer 2 Tunneling Protocol, under `/interface l2tp-server`.
*   **OpenVPN:** Open source VPN protocol, under `/interface openvpn-server`.
*   **PPPoE:** Point-to-Point Protocol over Ethernet, under `/interface pppoe-server`.
*   **PPTP:** Point-to-Point Tunneling Protocol, under `/interface pptp-server`.
*   **SSTP:** Secure Socket Tunneling Protocol, under `/interface sstp-server`.
*   **WireGuard:** Modern VPN protocol, under `/interface wireguard`.
*   **ZeroTier**: Software defined network service, under `/interface zerotier`.

### Wired Connections

*   **Ethernet:** Configuring wired ethernet interfaces using `/interface ethernet`.
*  **MikroTik wired interface compatibility**: Documentation about which SFP and RJ45 interfaces are compatible with each RouterBoard.
*   **PWR Line:** Ethernet over power lines, using `/interface pwrline`.

### Wireless

*   **WiFi:** Configuring WiFi interfaces under `/interface wireless`.
*   **Wireless Interface:** Managing wireless settings.
*   **W60G:**  60GHz wireless interfaces under `/interface w60g`.
*   **CAPsMAN:**  Centralized Access Point System Manager for managing WiFi networks centrally, using `/capsman`.
*   **HWMPplus mesh**: Hardware mesh protocol for ad-hoc wireless networks, configured using `/interface wireless mesh`.
* **Nv2**: MikroTik proprietary wireless protocol, using `/interface wireless n-v2`.
*   **Interworking Profiles:**  Advanced wireless configuration.
*  **Wireless Case Studies**: Practical examples about using wireless solutions.
*   **Spectral scan**: Analyzing WiFi spectrum with `/interface wireless spectral-scan`.

### Internet of Things

*   **Bluetooth:**  Configuring Bluetooth interfaces under `/interface bluetooth`.
*   **GPIO:** General Purpose Input Output interface. Under `/system gpio`.
*  **Lora**: Low-Power, Wide-Area Network (LoRaWAN) interface for IoT applications, under `/interface lora`.
*  **MQTT**: Lightweight messaging protocol for IoT devices, under `/tool mqtt`.

### Hardware

*   **Disks:**  Managing router disks and storage, under `/disk`.
*   **Grounding:** Grounding the router for electrical protection.
*   **LCD Touchscreen**: Setting up the LCD interface, using `/system lcd`.
*   **LEDs:** Controlling the router's LEDs, under `/system led`.
*  **MTU in RouterOS**: Information and guidance about configuring MTU in MikroTik.
*   **Peripherals:**  Managing attached peripherals (USB, serial).
*   **PoE-Out:** Configuring PoE out functionality on a port. Under `/interface ethernet poe`.
*   **Ports:** Physical interfaces on the router.
*   **Product Naming:** Decoding MikroTik product names.
*   **RouterBOARD:** MikroTik hardware platform.
*   **USB Features:** Using the router's USB ports.

### Diagnostics, monitoring and troubleshooting

* **Bandwidth Test**: Testing network throughput between two points using `/tool bandwidth-test`.
* **Detect Internet**: Simple way to check if the router is connected to the internet using `/tool detect-internet`.
* **Dynamic DNS**: Configuring DDNS clients to keep domain name updated with dynamic IP addresses, under `/ip ddns`.
* **Graphing**: Creating graphical representations of various parameters using `/tool graphing`.
*   **Health:**  Monitoring the router's health and status under `/system health`.
*   **Interface stats and monitor-traffic:** Monitoring interface traffic using `/interface monitor-traffic` or checking interface stats using `/interface print stats`.
*   **IP Scan:** Scanning for devices in the network using `/tool ip-scan`.
*   **Log:**  Analyzing system logs, under `/system logging`.
*   **Netwatch:**  Monitoring hosts and executing actions on status changes. Under `/tool netwatch`.
*   **Packet Sniffer:** Capturing network packets using `/tool sniffer`.
*   **Ping:** Testing network reachability using `/ping`.
*   **Profiler:**  Identifying performance bottlenecks using `/tool profile`.
*   **Resource:** Monitoring resource usage using `/system resource print`.
*   **SNMP:**  Simple Network Management Protocol. Can be configured using `/snmp`.
*  **Speed Test**: Testing internet speed using `/tool speedtest`.
*   **S-RJ10 general guidance:** Guidance for using