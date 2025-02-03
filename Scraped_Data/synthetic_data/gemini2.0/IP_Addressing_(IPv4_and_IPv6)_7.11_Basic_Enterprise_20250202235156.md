Okay, let's dive into a comprehensive exploration of IP Addressing on MikroTik RouterOS 7.11, tailored for an enterprise environment. This document will be extensive, covering a broad spectrum of RouterOS features, focusing on IP addressing, and branching into related areas to provide a holistic view.

# MikroTik RouterOS: Enterprise IP Addressing & Networking

This document outlines an enterprise-level configuration for IP addressing on MikroTik RouterOS 7.11, covering IPv4 and IPv6. It provides detailed steps, CLI commands, and explanations of related RouterOS features.

## 1. Comprehensive Configuration Scenario and Requirements

**Scenario:** A mid-sized enterprise needs to deploy a MikroTik router as a core network device. The network requires:

*   **Public IP:**  A static IPv4 address (e.g., 203.0.113.2/24) and a static IPv6 prefix (e.g., 2001:db8::/48). This will be used for internet connectivity.
*   **Internal LAN:**  Multiple VLANs with dedicated IPv4 subnets and IPv6 subnets.
    *   VLAN 10 (Management): 10.10.10.0/24 (IPv4) & 2001:db8:10::/64 (IPv6)
    *   VLAN 20 (Users): 10.20.20.0/24 (IPv4) & 2001:db8:20::/64 (IPv6)
    *   VLAN 30 (Servers): 10.30.30.0/24 (IPv4) & 2001:db8:30::/64 (IPv6)
*   **DHCP Server:** Each VLAN requires its own DHCPv4 and DHCPv6 servers.
*   **Firewall:** Basic firewall rules to protect the internal networks.
*   **Basic Routing:**  Routing between internal VLANs and out to the internet.
*   **Basic QoS:**  A basic priority queue to ensure network-critical traffic is prioritized.

**MikroTik Requirements:**

*   RouterOS 7.11 (or a 6.x version)
*   A router with VLAN-capable interfaces.
*   Basic understanding of MikroTik CLI/Winbox
*   Optional: Public IPv6 for tests.

## 2. Step-by-Step MikroTik Implementation

This section shows steps using the CLI for the most detailed example. We will also note Winbox steps where they add value.

### 2.1. Interface Configuration

**CLI:**

```routeros
/interface ethernet
set [find name=ether1] comment="WAN Uplink"
set [find name=ether2] comment="LAN Trunk"
/interface vlan
add interface=ether2 name=vlan10 vlan-id=10 comment="Management VLAN"
add interface=ether2 name=vlan20 vlan-id=20 comment="Users VLAN"
add interface=ether2 name=vlan30 vlan-id=30 comment="Servers VLAN"
```

**Explanation:**

*   `interface ethernet`: Navigates to Ethernet interface settings.
*   `set [find name=ether1] comment="WAN Uplink"`: Sets a descriptive comment for the WAN interface.
*   `interface vlan`: Navigates to VLAN interface settings.
*   `add interface=ether2 name=vlan10 vlan-id=10 comment="Management VLAN"`: Creates VLAN interfaces on ether2 with specified VLAN IDs and comments.

**Winbox:**

1. Navigate to `Interfaces`.
2. Select `ether1`, in the right panel, give a comment like "WAN Uplink"
3. Select `ether2`, in the right panel, give a comment like "LAN Trunk"
4. Click on the + to add a new interface, select VLAN.
5. Give the interface a name (e.g. vlan10), then assign the interface `ether2`, assign vlan ID of 10 and a comment (e.g. "Management VLAN")
6. Repeat step 4 & 5 for vlan20 & vlan30 with vlan ID's 20 and 30 respectively.

### 2.2. IP Addressing

**CLI:**

```routeros
/ip address
add address=203.0.113.2/24 interface=ether1 comment="Public IP"
add address=10.10.10.1/24 interface=vlan10 comment="Management LAN"
add address=10.20.20.1/24 interface=vlan20 comment="Users LAN"
add address=10.30.30.1/24 interface=vlan30 comment="Servers LAN"
/ipv6 address
add address=2001:db8::2/48 interface=ether1 advertise=no comment="Public IPv6"
add address=2001:db8:10::1/64 interface=vlan10 advertise=no comment="Management IPv6"
add address=2001:db8:20::1/64 interface=vlan20 advertise=no comment="Users IPv6"
add address=2001:db8:30::1/64 interface=vlan30 advertise=no comment="Servers IPv6"
```

**Explanation:**

*   `ip address`: Navigates to the IPv4 address settings.
*   `add address=...`: Adds an IPv4 address to the specified interface, along with a comment.
*   `ipv6 address`: Navigates to IPv6 address settings
*   `advertise=no`: This parameter is important. On a standard router, you would want `advertise=yes` for the interfaces facing your internal networks. On your WAN, `advertise=no` is important to stop accidental IPv6 RA (Router Advertisements) being issued to other networks.

**Winbox:**
1. Navigate to `IP -> Addresses` or `IPv6 -> Addresses`
2. Click the + and add addresses per CLI instructions above.

### 2.3. IP Pools

**CLI:**

```routeros
/ip pool
add name=dhcp_pool_vlan10 ranges=10.10.10.10-10.10.10.254 comment="VLAN 10 DHCP Pool"
add name=dhcp_pool_vlan20 ranges=10.20.20.10-10.20.20.254 comment="VLAN 20 DHCP Pool"
add name=dhcp_pool_vlan30 ranges=10.30.30.10-10.30.30.254 comment="VLAN 30 DHCP Pool"

/ipv6 pool
add name=ipv6_dhcp_pool_vlan10 prefix=2001:db8:10::/64 prefix-length=64 comment="VLAN 10 IPv6 Pool"
add name=ipv6_dhcp_pool_vlan20 prefix=2001:db8:20::/64 prefix-length=64 comment="VLAN 20 IPv6 Pool"
add name=ipv6_dhcp_pool_vlan30 prefix=2001:db8:30::/64 prefix-length=64 comment="VLAN 30 IPv6 Pool"
```

**Explanation:**

*   `ip pool`: Navigates to the IPv4 pool settings.
*   `add name=... ranges=...`: Creates an IPv4 pool for DHCP with a specific range.
*   `ipv6 pool`: Navigates to the IPv6 pool settings.
*   `prefix`: the network prefix
*  `prefix-length`: the network prefix length.

**Winbox:**
1. Navigate to `IP -> Pool` or `IPv6 -> Pool`.
2. Click the + and add Pools per the CLI instructions above.

### 2.4. DHCP Servers

**CLI:**

```routeros
/ip dhcp-server
add address-pool=dhcp_pool_vlan10 interface=vlan10 lease-time=10m name=dhcp_server_vlan10 comment="VLAN 10 DHCP Server"
add address-pool=dhcp_pool_vlan20 interface=vlan20 lease-time=10m name=dhcp_server_vlan20 comment="VLAN 20 DHCP Server"
add address-pool=dhcp_pool_vlan30 interface=vlan30 lease-time=10m name=dhcp_server_vlan30 comment="VLAN 30 DHCP Server"

/ipv6 dhcp-server
add address-pool=ipv6_dhcp_pool_vlan10 interface=vlan10 name=ipv6_dhcp_server_vlan10  comment="VLAN 10 IPv6 DHCP Server"
add address-pool=ipv6_dhcp_pool_vlan20 interface=vlan20 name=ipv6_dhcp_server_vlan20  comment="VLAN 20 IPv6 DHCP Server"
add address-pool=ipv6_dhcp_pool_vlan30 interface=vlan30 name=ipv6_dhcp_server_vlan30  comment="VLAN 30 IPv6 DHCP Server"

/ip dhcp-server network
add address=10.10.10.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=10.10.10.1 comment="VLAN 10 DHCP Network"
add address=10.20.20.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=10.20.20.1 comment="VLAN 20 DHCP Network"
add address=10.30.30.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=10.30.30.1 comment="VLAN 30 DHCP Network"

/ipv6 dhcp-server network
add address=2001:db8:10::/64 dns-server=2606:4700:4700::1111,2606:4700:4700::1001 gateway=2001:db8:10::1 comment="VLAN 10 IPv6 DHCP Network"
add address=2001:db8:20::/64 dns-server=2606:4700:4700::1111,2606:4700:4700::1001 gateway=2001:db8:20::1 comment="VLAN 20 IPv6 DHCP Network"
add address=2001:db8:30::/64 dns-server=2606:4700:4700::1111,2606:4700:4700::1001 gateway=2001:db8:30::1 comment="VLAN 30 IPv6 DHCP Network"
```

**Explanation:**

*   `ip dhcp-server`: Navigates to IPv4 DHCP server settings.
*   `add address-pool=... interface=... lease-time=... name=... comment=...`: Creates a DHCP server for each VLAN, specifying the address pool, interface, lease time, and comments.
*   `ip dhcp-server network`: configures the networks that the DHCP server will hand out, DNS and default gateway.
*   `ipv6 dhcp-server` and `ipv6 dhcp-server network`: As above but for IPv6

**Winbox:**
1. Navigate to `IP -> DHCP Server` or `IPv6 -> DHCP Server`
2. Click the +, configure basic settings as per CLI instructions
3. Navigate to `IP -> DHCP Server -> Networks` or `IPv6 -> DHCP Server -> Networks`
4. Click the + and add network settings as per CLI instructions

### 2.5. IP Routing

**CLI:**

```routeros
/ip route
add dst-address=0.0.0.0/0 gateway=203.0.113.1 comment="Default Route"
/ipv6 route
add dst-address=::/0 gateway=2001:db8::1 comment="Default IPv6 Route"
```

**Explanation:**

*   `ip route`: Navigates to the IPv4 routing settings.
*   `add dst-address=0.0.0.0/0 gateway=... comment=...`: Sets the default IPv4 route to the internet.
*   `ipv6 route`: Navigates to the IPv6 routing settings.
*   `add dst-address=::/0 gateway=... comment=...`: Sets the default IPv6 route to the internet.

**Winbox:**

1.  Navigate to `IP` -> `Routes` or `IPv6` -> `Routes`.
2.  Click the `+` to add a new route. Configure the default IPv4 and IPv6 route pointing to your internet gateway.

### 2.6. IP Settings

This section covers global settings that impact IP addressing

**CLI:**

```routeros
/ip settings
set allow-fast-path=yes  max-queued-packets=2048
/ipv6 settings
set accept-router-advertisements=yes disable-dad=no
```

**Explanation:**

*  `/ip settings`: Modifies global IPv4 related settings. `allow-fast-path=yes` allows for fast-path packet processing. `max-queued-packets` defines how many packets can be queued in memory.
* `/ipv6 settings`: Modifies global IPv6 related settings. `accept-router-advertisements` allows the router to process IPv6 router advertisements. `disable-dad` disables IPv6 Duplicate Address Detection, it is recommended to leave this off.

**Winbox:**

1. Navigate to `IP` -> `Settings` or `IPv6` -> `Settings`
2. Make the desired changes.

### 2.7. Firewall

**CLI:**

```routeros
/ip firewall filter
add action=accept chain=input comment="Accept Established/Related connections" connection-state=established,related
add action=accept chain=input comment="Accept ICMP" protocol=icmp
add action=accept chain=input comment="Allow established connections" connection-state=established,related
add action=accept chain=forward comment="Allow traffic to flow within LAN" in-interface-list=LAN out-interface-list=LAN
add action=drop chain=forward comment="Drop anything that's not from the LAN" in-interface=!LAN
add action=drop chain=input comment="Drop all else"
add action=fasttrack-connection chain=forward comment="Enable fasttracking" connection-state=established,related
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1 comment="Masquerade outbound connections"
/interface list
add name=LAN
add interface=vlan10 list=LAN
add interface=vlan20 list=LAN
add interface=vlan30 list=LAN
```

**Explanation:**

*   `ip firewall filter`: Navigates to firewall filter rule settings.
*   `add action=accept chain=input comment=...`: Defines rules to accept established/related connections and ICMP on the input chain.
*  `add action=accept chain=forward comment=...`: Defines rules to allow traffic to flow within the LAN.
*   `add action=drop chain=input comment=...`: Defines a rule to drop any other input traffic.
*   `add action=fasttrack-connection chain=forward comment=...`: Enables fasttrack for speed increases.
*   `ip firewall nat`: Navigates to NAT rule settings.
*   `add action=masquerade chain=srcnat out-interface=ether1 comment=...`: Creates a masquerade NAT rule for outbound traffic from the internal network to the internet.
*  `interface list`: defines an interface list for easier firewall configuration.

**Winbox:**
1. Navigate to `IP -> Firewall`. Add rules per CLI instructions, also add to nat and interface list

### 2.8. Quality of Service

**CLI:**

```routeros
/queue type
add kind=pfifo name=queue_type_priority
/queue simple
add max-limit=5M/5M name="Queue for VoIP" queue=queue_type_priority target-addresses=10.10.10.0/24
```

**Explanation:**

*   `queue type`: Navigates to queue type settings.
*   `add kind=... name=...`: Defines a new queue type.
*   `queue simple`: Navigates to simple queue settings.
*   `add max-limit=... name=... target=...`: Creates a simple queue to rate limit/prioritize traffic, here we're showing an example of prioritizing traffic to 10.10.10.0/24 with a custom queue type and rate limiting of 5Mbit up and down.

**Winbox:**
1.  Navigate to `Queues` and `Queue Types`. Add queues and types per the CLI instructions above.

## 3. Complete MikroTik CLI Configuration

```routeros
# Interfaces
/interface ethernet
set [find name=ether1] comment="WAN Uplink"
set [find name=ether2] comment="LAN Trunk"
/interface vlan
add interface=ether2 name=vlan10 vlan-id=10 comment="Management VLAN"
add interface=ether2 name=vlan20 vlan-id=20 comment="Users VLAN"
add interface=ether2 name=vlan30 vlan-id=30 comment="Servers VLAN"

# IP Addresses
/ip address
add address=203.0.113.2/24 interface=ether1 comment="Public IP"
add address=10.10.10.1/24 interface=vlan10 comment="Management LAN"
add address=10.20.20.1/24 interface=vlan20 comment="Users LAN"
add address=10.30.30.1/24 interface=vlan30 comment="Servers LAN"
/ipv6 address
add address=2001:db8::2/48 interface=ether1 advertise=no comment="Public IPv6"
add address=2001:db8:10::1/64 interface=vlan10 advertise=no comment="Management IPv6"
add address=2001:db8:20::1/64 interface=vlan20 advertise=no comment="Users IPv6"
add address=2001:db8:30::1/64 interface=vlan30 advertise=no comment="Servers IPv6"


# IP Pools
/ip pool
add name=dhcp_pool_vlan10 ranges=10.10.10.10-10.10.10.254 comment="VLAN 10 DHCP Pool"
add name=dhcp_pool_vlan20 ranges=10.20.20.10-10.20.20.254 comment="VLAN 20 DHCP Pool"
add name=dhcp_pool_vlan30 ranges=10.30.30.10-10.30.30.254 comment="VLAN 30 DHCP Pool"

/ipv6 pool
add name=ipv6_dhcp_pool_vlan10 prefix=2001:db8:10::/64 prefix-length=64 comment="VLAN 10 IPv6 Pool"
add name=ipv6_dhcp_pool_vlan20 prefix=2001:db8:20::/64 prefix-length=64 comment="VLAN 20 IPv6 Pool"
add name=ipv6_dhcp_pool_vlan30 prefix=2001:db8:30::/64 prefix-length=64 comment="VLAN 30 IPv6 Pool"


# DHCP Servers
/ip dhcp-server
add address-pool=dhcp_pool_vlan10 interface=vlan10 lease-time=10m name=dhcp_server_vlan10 comment="VLAN 10 DHCP Server"
add address-pool=dhcp_pool_vlan20 interface=vlan20 lease-time=10m name=dhcp_server_vlan20 comment="VLAN 20 DHCP Server"
add address-pool=dhcp_pool_vlan30 interface=vlan30 lease-time=10m name=dhcp_server_vlan30 comment="VLAN 30 DHCP Server"

/ipv6 dhcp-server
add address-pool=ipv6_dhcp_pool_vlan10 interface=vlan10 name=ipv6_dhcp_server_vlan10  comment="VLAN 10 IPv6 DHCP Server"
add address-pool=ipv6_dhcp_pool_vlan20 interface=vlan20 name=ipv6_dhcp_server_vlan20  comment="VLAN 20 IPv6 DHCP Server"
add address-pool=ipv6_dhcp_pool_vlan30 interface=vlan30 name=ipv6_dhcp_server_vlan30  comment="VLAN 30 IPv6 DHCP Server"


/ip dhcp-server network
add address=10.10.10.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=10.10.10.1 comment="VLAN 10 DHCP Network"
add address=10.20.20.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=10.20.20.1 comment="VLAN 20 DHCP Network"
add address=10.30.30.0/24 dns-server=1.1.1.1,8.8.8.8 gateway=10.30.30.1 comment="VLAN 30 DHCP Network"

/ipv6 dhcp-server network
add address=2001:db8:10::/64 dns-server=2606:4700:4700::1111,2606:4700:4700::1001 gateway=2001:db8:10::1 comment="VLAN 10 IPv6 DHCP Network"
add address=2001:db8:20::/64 dns-server=2606:4700:4700::1111,2606:4700:4700::1001 gateway=2001:db8:20::1 comment="VLAN 20 IPv6 DHCP Network"
add address=2001:db8:30::/64 dns-server=2606:4700:4700::1111,2606:4700:4700::1001 gateway=2001:db8:30::1 comment="VLAN 30 IPv6 DHCP Network"


# IP Routing
/ip route
add dst-address=0.0.0.0/0 gateway=203.0.113.1 comment="Default Route"
/ipv6 route
add dst-address=::/0 gateway=2001:db8::1 comment="Default IPv6 Route"

# IP Settings
/ip settings
set allow-fast-path=yes  max-queued-packets=2048
/ipv6 settings
set accept-router-advertisements=yes disable-dad=no

# Firewall
/ip firewall filter
add action=accept chain=input comment="Accept Established/Related connections" connection-state=established,related
add action=accept chain=input comment="Accept ICMP" protocol=icmp
add action=accept chain=input comment="Allow established connections" connection-state=established,related
add action=accept chain=forward comment="Allow traffic to flow within LAN" in-interface-list=LAN out-interface-list=LAN
add action=drop chain=forward comment="Drop anything that's not from the LAN" in-interface=!LAN
add action=drop chain=input comment="Drop all else"
add action=fasttrack-connection chain=forward comment="Enable fasttracking" connection-state=established,related
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1 comment="Masquerade outbound connections"
/interface list
add name=LAN
add interface=vlan10 list=LAN
add interface=vlan20 list=LAN
add interface=vlan30 list=LAN

#Quality of Service
/queue type
add kind=pfifo name=queue_type_priority
/queue simple
add max-limit=5M/5M name="Queue for VoIP" queue=queue_type_priority target-addresses=10.10.10.0/24
```

## 4. Common Pitfalls, Troubleshooting, and Diagnostics

### 4.1. Common Pitfalls:

*   **Incorrect VLAN IDs:** Double-check VLAN tagging on switches and the MikroTik.
*   **DHCP Server Issues:** Incorrect IP pools, overlapping ranges, and missing gateway/DNS configurations can cause DHCP failures. Check the lease table.
*   **Firewall Misconfigurations:**  Blocking essential traffic by incorrectly placing or ordering rules. Start with very open rules and restrict them slowly.
*   **Routing Conflicts:**  Multiple default routes, routing protocol misconfigurations, resulting in unpredictable traffic flow.
*   **IPv6 DAD:** On IPv6 you might need to turn off IPv6 DAD (Duplicate Address Detection) for interfaces.

### 4.2. Troubleshooting using MikroTik Tools:

*   **Ping & Traceroute:**  Test basic IP connectivity between devices.
    ```routeros
    /ping address=10.20.20.5
    /traceroute address=8.8.8.8
    /ipv6 ping address=2001:db8:20::5
    /ipv6 traceroute address=2001:4860:4860::8888
    ```
*   **Torch:** Capture and analyze live traffic to diagnose issues at the interface level.
    ```routeros
    /tool torch interface=vlan20
    ```
    This will show a live view of all traffic passing over vlan20. You can filter on specific addresses or protocols.
*   **Packet Sniffer:** Capture packets for offline analysis.
    ```routeros
    /tool packet-sniffer
    set file-name=capture1 interface=vlan20 duration=60
    start
    ```
*   **Log:** Check system logs for errors and warnings, especially DHCP and firewall logs.
    ```routeros
     /log print where topics~"dhcp|firewall"
    ```
*   **Resource Monitor:**  Monitor CPU, memory, and interface utilization.
    ```routeros
    /system resource monitor
    ```
*   **Interface Monitor:** Monitor interface up-time, packets, errors
     ```routeros
     /interface monitor ether1
     ```
### 4.3. Error Handling:

*   If a command doesn't work, check for typos and syntax errors.
*   Use Winbox for simpler tasks or to verify CLI commands.
*   Use the RouterOS logs to check for any reported errors.

## 5. Verification and Testing Steps

*   **Basic Connectivity:**  Ping devices on different VLANs and to the internet.
*   **DHCP:** Check that devices receive IP addresses from the correct DHCP server.
*   **Internet Access:** Verify internet connectivity from all VLANs.
*   **Firewall:** Test connectivity through open firewall rules and test by adding restrictive rules.
*   **QoS:** Verify QoS configuration by monitoring queue usage while generating traffic.
*   **IPv6:** Ping and Traceroute IPv6 devices and destinations.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Bridging:** MikroTik supports bridging to create a switched network. While not used directly in this example, it's critical for combining multiple interfaces as a layer-2 network
*  **Switching:** MikroTik devices with switch-chips can perform wire-speed layer-2 switching operations, often in addition to routing.
*  **MACVLAN:** MikroTik supports MACVLAN to configure multiple virtual interfaces on a single physical interface.
*   **L3 Hardware Offloading:** Some MikroTik devices support hardware offloading for layer-3 operations, improving performance.
*   **MACsec:** For enhanced security on your LAN, you can configure MACsec on MikroTik switches and routers.
*   **VLAN:** MikroTik supports VLAN tagging, trunking, and access ports on Ethernet interfaces.
*  **VXLAN:** MikroTik supports layer 2 VXLAN tunnels.
*   **NAT:** Supports various NAT types, including masquerade, src-nat, dst-nat.
*   **Connection Tracking:** Provides stateful tracking of connections for use with the firewall.
*  **Packet Flow in RouterOS:** It is vital to understand the order packets are processed in RouterOS (Input->Forward->Output) when writing firewall rules.
*  **Queues:** RouterOS supports simple queues, pcq queues, queue trees, etc. to handle traffic shaping and QoS.
*  **Kid Control:** RouterOS supports content filtering, schedules, and more for child safety.
*  **UPnP:** RouterOS supports Universal Plug and Play for automatic port forwarding, but it is not recommended for security reasons.
*  **NAT-PMP:** NAT Port Mapping Protocol is also supported on MikroTik.
*  **IP Services:** MikroTik devices can provide DHCP, DNS, SOCKS, and Proxy servers.
*  **High Availability:** Options include VRRP, Bonding, or Multi-chassis Link Aggregation Group.
*   **Mobile Networking:** MikroTik supports USB and M.2 based LTE modems, GPS, and SMS functions.
*   **MPLS:** Multi-Protocol Label Switching is supported for advanced networking.
*  **Network Management:** Includes ARP, cloud interface, DHCP, DNS, SOCKS, and Proxy configurations.
*   **Routing Protocols:** Supports OSPF, RIP, BGP, and policy-based routing.
*   **System Tools:** Includes clock, email, fetch, files, identity, interface lists, neighbor discovery, NTP, partitions, and scheduler
*  **VPNs:** Supports various VPN protocols like IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, Wireguard.
*  **Wired and Wireless:** Supports many wired ethernet connections, 802.11 wireless, CAPSMAN, Nv2
*  **IoT:** Includes Bluetooth, GPIO, Lora, and MQTT capabilities for IOT purposes.
* **Hardware:** Wide array of supported hardware features (disks, LEDs, MTU, peripherals, PoE, ports, USB features, etc.)
*   **Diagnostics:** Includes tools for bandwidth testing, dynamic DNS, graphing, health monitoring, log management, netwatch, packet sniffing, ping, profiling, resource monitoring, SNMP, speed testing, S-RJ10 general guidance, torch, traceroute, traffic flow, and traffic generation.
*  **Extended Features:** Includes support for containers, DLNA Media server, ROSE-storage, SMB, UPS monitoring, Wake on LAN, and IP packing.

## 7. MikroTik REST API Examples

This section shows REST API examples, using MikroTik's `/rest` API. You must enable the API and HTTPS server, before attempting any calls.

### 7.1. Get Interface List

**API Endpoint:** `/interface/ethernet`

**Request Method:** `GET`

**Example Curl Command:**

```bash
curl -k -u admin:<your-password> https://<your-router-ip>/rest/interface/ethernet
```

**Expected Response:**

```json
[
    {
        "name": "ether1",
        "mac-address": "AA:BB:CC:DD:EE:FF",
        "mtu": 1500,
        "actual-mtu": 1500,
        "l2mtu": 1598,
        "speed": 1000000000,
        "full-duplex": true,
        "running": true,
        "disabled": false,
        "last-link-down-time": "1970-01-01T00:00:00+0000",
        "comment": "WAN Uplink",
         ".id": "*1"
    },
    {
        "name": "ether2",
        "mac-address": "AA:BB:CC:DD:EE:00",
        "mtu": 1500,
        "actual-mtu": 1500,
        "l2mtu": 1598,
        "speed": 1000000000,
        "full-duplex": true,
        "running": true,
        "disabled": false,
         "last-link-down-time": "1970-01-01T00:00:00+0000",
         "comment": "LAN Trunk",
        ".id": "*2"
    }
]

```
### 7.2. Add New VLAN Interface

**API Endpoint:** `/interface/vlan`

**Request Method:** `POST`

**Example Curl Command:**

```bash
curl -k -u admin:<your-password> -H "Content-Type: application/json" -X POST  -d '{ "interface": "*2", "name":"vlan40", "vlan-id":"40", "comment":"VLAN 40" }' https://<your-router-ip>/rest/interface/vlan
```

**Expected Response (Success):**

```json
{
    "message":"added",
    "id": "*21"
}
```

### 7.3. Get IP Addresses

**API Endpoint:** `/ip/address`

**Request Method:** `GET`

**Example Curl Command:**

```bash
curl -k -u admin:<your-password> https://<your-router-ip>/rest/ip/address
```

**Expected Response:**

```json
[
    {
        "address": "203.0.113.2/24",
        "interface": "ether1",
        "actual-interface": "ether1",
        "network": "203.0.113.0",
        "broadcast": "203.0.113.255",
        "disabled": false,
        "dynamic": false,
        "comment": "Public IP",
        ".id": "*3"
    },
        {
        "address": "10.10.10.1/24",
        "interface": "vlan10",
        "actual-interface": "vlan10",
        "network": "10.10.10.0",
        "broadcast": "10.10.1