Okay, let's dive deep into a comprehensive documentation for MikroTik RouterOS 7.11, focusing on advanced IP addressing and its related features, tailored for an enterprise network.  This will be a substantial document covering many facets as requested.

# MikroTik RouterOS 7.11 Advanced IP Addressing in Enterprise Environments

This document outlines best practices, configurations, and troubleshooting techniques for managing IP addresses, routing, and related services in a MikroTik RouterOS environment, specifically targeting enterprise network complexities.

## 1. Configuration Scenario and Requirements

**Scenario:** We're designing a network for a medium-sized enterprise with the following requirements:

*   Multiple VLANs for segmentation (Servers, Employees, Guests).
*   IPv4 and IPv6 addressing schemes.
*   Dynamic addressing using DHCP servers.
*   Static addressing for critical infrastructure components.
*   Robust routing between VLANs and to the Internet.
*   Firewalling and NAT to protect internal resources.
*   High availability and redundancy for critical services.
*   Remote network management using Winbox, SSH, and API.
*   Secure wireless network for employees and guests with authentication.
*   QoS to ensure reliable video conferencing.

**Specific MikroTik Requirements:**

*   Utilize VLAN trunking and tagging on specific interfaces.
*   Use DHCP pools for each VLAN.
*   Implement OSPF for dynamic routing.
*   Use a firewall policy with strong security rules.
*   Use RADIUS for employee network authentication.
*   Configure high availability using VRRP.
*   Employ proper packet tagging for QoS.

## 2. Step-by-Step MikroTik Implementation

We'll demonstrate the setup using a combination of CLI commands and Winbox examples where helpful. Note that the assumption is that a base MikroTik RouterOS instance has been setup. We will be focusing on the IP components in this example.

### **A. Basic Setup:**

**CLI**

```routeros
# Set router identity
/system identity set name="EnterpriseRouter"

# Set timezone
/system clock set time-zone-name="America/New_York"
```

### **B. Interface Configuration:**

Here we are assuming the following interfaces on the router:
- `ether1` : WAN (Internet connection)
- `ether2` : Server VLAN connection
- `ether3`: Employee VLAN connection
- `ether4` : Guest VLAN connection

**CLI:**
```routeros
# Disable default firewall rules for initial setup
/ip firewall filter remove [find comment="defconf: drop all not coming from LAN"]
/ip firewall filter remove [find comment="defconf: accept established,related, untracked"]
/ip firewall filter remove [find comment="defconf: accept from LAN"]

# Rename interfaces
/interface ethernet set ether1 name="WAN"
/interface ethernet set ether2 name="Servers"
/interface ethernet set ether3 name="Employees"
/interface ethernet set ether4 name="Guests"

#Enable interfaces
/interface enable WAN
/interface enable Servers
/interface enable Employees
/interface enable Guests
```

**Winbox:**
- Go to `Interfaces` and rename the appropriate ethernet interfaces

### C. VLAN Configuration

**CLI:**
```routeros
# Create VLANs
/interface vlan add name="vlan10_Servers" vlan-id=10 interface=Servers
/interface vlan add name="vlan20_Employees" vlan-id=20 interface=Employees
/interface vlan add name="vlan30_Guests" vlan-id=30 interface=Guests
```

**Winbox:**
- Go to `Interfaces` and create a new VLAN interface.
    - Set a `Name` such as `vlan10_Servers`
    - Set the VLAN ID as `10`
    - Set the interface to be `Servers`
    - Click `OK`
- Repeat the process for `vlan20_Employees` and `vlan30_Guests`


### D. IPv4 Address Configuration

**CLI:**

```routeros
# IPv4 Addresses on VLAN interfaces
/ip address add address=192.168.10.1/24 interface=vlan10_Servers
/ip address add address=192.168.20.1/24 interface=vlan20_Employees
/ip address add address=192.168.30.1/24 interface=vlan30_Guests
```

**Winbox:**
- Go to `IP` -> `Addresses`.
- Add each IP address on the correct interfaces.

### E. IPv6 Address Configuration

**CLI:**

```routeros
# Enable IPv6
/ipv6 settings set disable-ipv6=no

# Set IPv6 addresses
/ipv6 address add address=2001:db8:10::1/64 interface=vlan10_Servers
/ipv6 address add address=2001:db8:20::1/64 interface=vlan20_Employees
/ipv6 address add address=2001:db8:30::1/64 interface=vlan30_Guests
```

**Winbox:**
- Go to `IPv6` -> `Addresses`.
- Add each IPv6 address on the correct interfaces.

### F. DHCP Server Configuration

**CLI:**

```routeros
# Create DHCP Server for each VLAN
/ip dhcp-server add address-pool=pool10 interface=vlan10_Servers name="dhcp-server10"
/ip dhcp-server add address-pool=pool20 interface=vlan20_Employees name="dhcp-server20"
/ip dhcp-server add address-pool=pool30 interface=vlan30_Guests name="dhcp-server30"


# Configure DHCP address pools
/ip pool add name=pool10 ranges=192.168.10.10-192.168.10.254
/ip pool add name=pool20 ranges=192.168.20.10-192.168.20.254
/ip pool add name=pool30 ranges=192.168.30.10-192.168.30.254

# DHCP Network
/ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=1.1.1.1,1.0.0.1
/ip dhcp-server network add address=192.168.20.0/24 gateway=192.168.20.1 dns-server=1.1.1.1,1.0.0.1
/ip dhcp-server network add address=192.168.30.0/24 gateway=192.168.30.1 dns-server=1.1.1.1,1.0.0.1
```

**Winbox:**
- Go to `IP` -> `Pool`, add the necessary pools as listed above
- Go to `IP` -> `DHCP Server` and add three DHCP servers with the following settings:
    - `Name`: `dhcp-server10`
    - `Interface`: `vlan10_Servers`
    - `Address Pool`: `pool10`
    - Set `Lease Time` as desired.
- Go to `IP` -> `DHCP Server` -> `Networks` and add the corresponding networks.

### G. IPv6 DHCP Server Configuration

**CLI**

```routeros
/ipv6 dhcp-server add name="dhcpv6-servers" interface=vlan10_Servers
/ipv6 dhcp-server add name="dhcpv6-employees" interface=vlan20_Employees
/ipv6 dhcp-server add name="dhcpv6-guests" interface=vlan30_Guests

/ipv6 pool add name="ipv6pool10" prefix=2001:db8:10::/64
/ipv6 pool add name="ipv6pool20" prefix=2001:db8:20::/64
/ipv6 pool add name="ipv6pool30" prefix=2001:db8:30::/64

/ipv6 dhcp-server server set dhcpv6-servers address-pool=ipv6pool10
/ipv6 dhcp-server server set dhcpv6-employees address-pool=ipv6pool20
/ipv6 dhcp-server server set dhcpv6-guests address-pool=ipv6pool30
```

**Winbox**
- Go to `IPv6` -> `Pool` and add the IPv6 Pools as outlined in the above commands
- Go to `IPv6` -> `DHCP Server` and add three DHCP servers with the following settings:
    - `Name`: `dhcpv6-servers`
    - `Interface`: `vlan10_Servers`
    - `Address Pool`: `ipv6pool10`
    - Set `Lease Time` as desired.
- Repeat the process for `dhcpv6-employees` and `dhcpv6-guests`


### H. IP Routing (OSPF) Configuration

**CLI:**
```routeros
# Enable OSPF
/routing ospf instance add name="ospf-instance" router-id=10.10.10.1

# Add OSPF networks
/routing ospf network add network=192.168.10.0/24 area=backbone
/routing ospf network add network=192.168.20.0/24 area=backbone
/routing ospf network add network=192.168.30.0/24 area=backbone

# Add OSPFv6 instance
/routing ospfv3 instance add name="ospfv3-instance" router-id=10.10.10.1

# Add OSPFv6 networks
/routing ospfv3 network add network=2001:db8:10::/64 area=backbone
/routing ospfv3 network add network=2001:db8:20::/64 area=backbone
/routing ospfv3 network add network=2001:db8:30::/64 area=backbone
```
**Winbox**
- Go to `Routing` -> `OSPF` -> `Instances` and create an instance called `ospf-instance`
- Go to `Routing` -> `OSPF` -> `Networks` and add the three networks
- Go to `Routing` -> `OSPFv3` -> `Instances` and create an instance called `ospfv3-instance`
- Go to `Routing` -> `OSPFv3` -> `Networks` and add the three networks


### I. Basic Firewall Configuration (for this example only, real world should be more complex)

**CLI:**
```routeros
# Enable Forwarding
/ip settings set allow-fast-path=yes

# Enable NAT
/ip firewall nat add chain=srcnat action=masquerade out-interface=WAN

# Block Invalid Connections
/ip firewall filter add chain=input action=drop connection-state=invalid
/ip firewall filter add chain=forward action=drop connection-state=invalid

# Allow DNS
/ip firewall filter add chain=input action=accept protocol=udp port=53
/ip firewall filter add chain=input action=accept protocol=tcp port=53

# Allow HTTP and HTTPS
/ip firewall filter add chain=input action=accept protocol=tcp port=80
/ip firewall filter add chain=input action=accept protocol=tcp port=443

# Allow ICMP Ping
/ip firewall filter add chain=input action=accept protocol=icmp

# Default Drop all other traffic
/ip firewall filter add chain=input action=drop

# Allow forward traffic from the VLANs
/ip firewall filter add chain=forward action=accept in-interface-list=LAN


# Drop All Forward traffic by default
/ip firewall filter add chain=forward action=drop
```

**Winbox:**
- Go to `IP` -> `Firewall` -> `NAT` and create the NAT rule
- Go to `IP` -> `Firewall` -> `Filter Rules` and create the above rules


## 3. MikroTik CLI Configuration Commands

### Interface Commands

**VLAN Creation:**

```routeros
/interface vlan add name=<vlan_name> vlan-id=<vlan_id> interface=<parent_interface>
```

*   `name`: VLAN interface name
*   `vlan-id`: VLAN tag number (1-4094)
*   `interface`: Physical interface for VLAN
*   `mtu`: Maximum Transmission Unit. Default 1500.

**IP Address Configuration:**

```routeros
/ip address add address=<ip_address/prefix> interface=<interface_name>
```

*   `address`: IP address and network prefix in CIDR notation. E.g. `192.168.1.1/24`
*   `interface`: Name of the interface.
*   `network`: If not stated it will be computed from address.

**DHCP Server Configuration:**

```routeros
/ip dhcp-server add name=<dhcp_server_name> interface=<interface_name> address-pool=<address_pool_name>
/ip dhcp-server network add address=<network_address/prefix> gateway=<gateway_ip> dns-server=<dns_ip1>,<dns_ip2>
/ip pool add name=<pool_name> ranges=<ip_range_start>-<ip_range_end>
```

*   `name`: DHCP server name.
*   `interface`: Interface to provide DHCP on.
*   `address-pool`: Name of IP pool.
*   `address`: The IP address range for the pool. E.g. `192.168.1.0/24`
*   `gateway`: Default gateway for DHCP clients.
*   `dns-server`: DNS servers to provide to DHCP clients.
*   `ranges`: IP address range for pool.

**OSPF Configuration:**

```routeros
/routing ospf instance add name=<instance_name> router-id=<router_id_ip>
/routing ospf network add network=<network_address/prefix> area=<area_name>
/routing ospfv3 instance add name=<instance_name> router-id=<router_id_ip>
/routing ospfv3 network add network=<network_address/prefix> area=<area_name>
```

*   `name`: OSPF instance name.
*   `router-id`: Router ID (must be an IP). E.g. `10.10.10.1`
*   `network`: The network range to add. E.g. `192.168.1.0/24`
*   `area`: OSPF area. Usually "backbone".

**Firewall Rules:**
```routeros
/ip firewall filter add chain=<chain_name> action=<action> <matching_parameters>
/ip firewall nat add chain=<chain_name> action=<action> <matching_parameters>
```
* `chain`: The firewall chain to add a rule to `input`, `forward`, or `srcnat`, `dstnat`
* `action`: The firewall action `accept`, `drop`, or `masquerade`
* `matching_parameters`: Parameters for matching a specific connection, such as `protocol`, `src-address`, `dst-address`, etc.

## 4. Common Pitfalls, Troubleshooting, and Diagnostics

*   **Incorrect VLAN tagging:** Double-check VLAN assignments on interfaces and switches. Use `/interface vlan print detail` to see VLAN configuration.
*   **DHCP server misconfiguration:**  Verify address pool ranges, interface assignments, and network settings. Use `/ip dhcp-server lease print` to check connected leases.
*   **Routing issues:** Use `/routing ospf neighbor print` (or IPv6 version) to check OSPF neighbor status.  Use `/ip route print` (or `/ipv6 route print`) to view routing table. Use `traceroute` to see the network hops.
*   **Firewall blocking:**  Use `/ip firewall filter print` to review rules. Check `/ip firewall connection print` for active connections to confirm blocked traffic.
*   **Performance bottlenecks:** Use `/tool profile` to identify CPU/memory hogs. Use `/interface monitor-traffic interface=<interface_name>` to watch interface traffic.
*   **Connectivity Issues:** Use `ping <address>` and `traceroute <address>` to check connectivity. Use `/tool torch interface=<interface_name>` to see network traffic in detail.
*   **Incorrect MTU settings:** Check MTU on all interfaces involved and match them appropriately. Inconsistencies in MTU settings can lead to fragmentation and performance issues.


## 5. Verification and Testing

*   **Ping:** Use `ping <destination_address>` from the router's CLI to check reachability. From clients, ping gateway and other resources.
*   **Traceroute:** Use `traceroute <destination_address>` to view network path hops. Check if route is correct.
*   **Torch:** `/tool torch interface=<interface>` to capture and analyze traffic on a specific interface. Filter on protocols, addresses, etc.
*   **Bandwidth Test:**  Use `/tool bandwidth-test` to test the speeds between the router and another device.
*   **Monitor traffic:** `/interface monitor-traffic <interface>` to check the bandwidth usage on an interface

## 6. MikroTik-Specific Features, Capabilities, and Limitations

*   **Bridging:** RouterOS bridging is used for combining multiple interfaces as a single broadcast domain, also used for wireless AP. Limited by single CPU core processing.
*   **Switching:** RouterOS has switch chip functionalities. L3 offloading allows hardware-based forwarding.
*   **Firewall and QoS:** Layer-7 filtering, mangle rules, and powerful queueing. Limited only by router's resources.
*   **VPN:** Wide variety of VPN options. IPsec performance is dependent on hardware acceleration.
*   **Routing:** Static, OSPF, RIP, BGP, VRF. Supports complex routing policies.
*   **Security:** Strong firewall, user management, password policies. Requires careful configuration to avoid lockouts.
*   **Limitations:** Performance depends on the RouterBOARD model and CPU type. CPU offloading features will improve performance.

## 7. MikroTik REST API Examples

**API Endpoint:** `/ip/address`

**Request Method:** `GET`

**Request Example (get all addresses):**

```bash
curl -k -u admin:<password> -H "Content-Type: application/json" https://<router_ip>/rest/ip/address
```

**Expected Response:**

```json
[
    {
        ".id": "*1",
        "address": "192.168.88.1/24",
        "interface": "ether1",
        "network": "192.168.88.0",
        "actual-interface": "ether1"
    },
    {
        ".id": "*2",
        "address": "10.0.0.1/24",
        "interface": "vlan10",
        "network": "10.0.0.0",
        "actual-interface": "vlan10"
    }
]
```

**API Endpoint:** `/ip/address`

**Request Method:** `POST`

**Request Example (create address):**

```bash
curl -k -u admin:<password> -H "Content-Type: application/json" -d '{
  "address": "192.168.1.10/24",
  "interface": "ether2"
}' https://<router_ip>/rest/ip/address
```

**Expected Response:**
```json
{
    "message": "added",
    "id": "*3"
}
```

**API Endpoint:** `/ip/dhcp-server`

**Request Method:** `GET`

**Request Example (get all DHCP servers):**

```bash
curl -k -u admin:<password> -H "Content-Type: application/json" https://<router_ip>/rest/ip/dhcp-server
```

**Expected Response:**

```json
[
    {
        ".id": "*1",
        "name": "dhcp-server1",
        "interface": "vlan10",
        "address-pool": "pool1"
    },
   {
        ".id": "*2",
        "name": "dhcp-server2",
        "interface": "vlan20",
        "address-pool": "pool2"
   }
]
```


**API Endpoint:** `/ip/firewall/filter`

**Request Method:** `GET`

**Request Example (get firewall rules):**

```bash
curl -k -u admin:<password> -H "Content-Type: application/json" https://<router_ip>/rest/ip/firewall/filter
```
**Expected Response:**

```json
[
  {
    ".id": "*0",
    "chain": "forward",
    "action": "accept",
    "in-interface-list": "LAN",
    "disabled": "false"
  },
 {
    ".id": "*1",
    "chain": "forward",
    "action": "drop",
    "disabled": "false"
 }
]
```

## 8. In-depth Explanations of Core Concepts

*   **Bridging:** Combines multiple interfaces into a single layer-2 network segment. Requires bridging firewall rules to secure.
*   **Routing:** Process of forwarding packets between different networks based on routing protocols or static routes. Critical for connectivity between VLANs and external networks.
*   **Firewall:** Inspects and filters network traffic based on configured rules. Essential for protecting your network from unauthorized access.
*   **NAT:** Translates private IP addresses to public IP addresses. Allows devices behind a router to access the Internet.

## 9. Security Best Practices

*   **Strong Passwords:** Use complex and unique passwords for all MikroTik router accounts.
*   **Secure Services:** Disable unnecessary services (e.g., Telnet, FTP, www).
*   **Firewall:** Configure strong firewall rules to limit access to the router. Create a whitelist of allowed IP addresses for remote access.
*   **Regular Updates:** Keep RouterOS software up to date to protect against vulnerabilities.
*   **Access Control:** Use user groups and permissions to limit access to certain configuration features.
*   **SSH/API Keys:** Utilize SSH key-based authentication for secure remote access.
*   **Monitor Logs:** Regularly review the system logs for suspicious activity.
*   **HTTPS access:** Enforce HTTPS access for Winbox and webfig access.
*   **Backup:** Create regular configuration backups. Use `export file=backup` to create a backup file.

## 10. Detailed Explanation and Configuration Examples for MikroTik Topics

(Due to the length of this document, not all topics can be covered in exhaustive detail, but I will provide a summary with configuration details)

### **IP Addressing (IPv4 and IPv6):**

*   **IPv4:**  32-bit addresses. Example: `192.168.1.1/24`.
*   **IPv6:** 128-bit addresses. Example: `2001:db8::1/64`.
*   MikroTik allows assigning static or dynamic IP addresses to interfaces and using IP pools.

```routeros
/ip address add address=192.168.1.1/24 interface=ether1 comment="Main Router IP"
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

### **IP Pools:**

*   Ranges of IP addresses that can be used for DHCP.
*   MikroTik manages IP Pools through `/ip pool`

```routeros
/ip pool add name=pool1 ranges=192.168.1.10-192.168.1.254
/ip pool print
```

### **IP Routing:**

*   Forwarding of packets using static routes or dynamic protocols.
*   MikroTik's IP Routing settings are under `/ip route`.
*   Supports OSPF, RIP, BGP, and VRF

```routeros
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.254
/routing ospf instance add name="ospf-main" router-id=10.10.10.1
```

### **IP Settings:**

*   General network settings
*   Mainly used for enabling and disabling certain features like fast-path and connection tracking

```routeros
/ip settings set allow-fast-path=yes
/ip settings print
```

### **MAC server:**

*   Used for managing MAC addresses and related actions.
*   Can be used for DHCP control, VLAN assignments, and MAC filtering

```routeros
/mac-server print
```

### **RoMON:**

*   MikroTik's Router Management Overlay Network
*   Allows managing other MikroTik routers that are in the RoMON network
*   Uses `/tool romon`
```routeros
/tool romon set enabled=yes password=romon_password
```

### **Winbox:**

*   Graphical configuration tool. Allows remote and local router management.
*   MikroTik's primary GUI

### **Certificates:**

*   Used for encrypted access via HTTPS, SSL VPNs.
*   Stored in the `/certificate` menu
*   Used for secure connections and authentication

```routeros
/certificate print
```

### **PPP AAA:**

*   Authentication, Authorization, and Accounting for PPP connections
*   Used for creating PPP profiles and authenticating PPP users

```routeros
/ppp profile print
/ppp secret print
```

### **RADIUS:**

*   Centralized authentication server for PPP and wireless.
*   Configured in `/radius` menu
*   Integrates with external servers for authentication

```routeros
/radius add address=192.168.1.200 secret=radius_secret
/radius print
```

### **User / User Groups:**

*   User management and access control for the router.
*   Users are stored in the `/user` menu
*   User groups can be made in `/user group`

```routeros
/user add name=testuser password=testpass group=read
/user group print
```

### **Bridging and Switching:**

*   Bridging combines multiple interfaces into a single layer-2 network.
*   Switching utilizes dedicated chips for hardware based forwarding.
*   Configured under `/interface bridge`

```routeros
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=ether2
```

### **MACVLAN:**

*   Virtual interfaces on a single physical interface, each with its own MAC.
*   Configured in `/interface macvlan`

```routeros
/interface macvlan add interface=ether1 mac-address=00:00:00:00:00:01
```

### **L3 Hardware Offloading:**

*   Offloads layer-3 processing to dedicated switch chip on supported devices
*   Allows for hardware based layer 3 packet forwarding
*   Settings can be configured on the bridge interface
```routeros
/interface bridge set l3-hw-offload=yes
```


### **MACsec:**

*   MAC Layer security for ethernet connections
*   Encrypts packets on the wire using encryption keys
*   Configured in the `/interface macsec` menu.
```routeros
/interface macsec add name=macsec1 parent-interface=ether2  cipher-suite=aes-gcm-128  key-type=pre-shared-key
/interface macsec key add key=0102030405060708090a0b0c0d0e0f10
```

### **Quality of Service (QoS):**

*   Prioritizes traffic based on defined rules.
*   Implemented using `/queue`
*   Allows prioritization of high importance traffic

```routeros
/queue simple add name=qos-voip target=192.168.1.0/24 max-limit=2M/2M priority=1
```

### **Switch Chip Features:**

*   Specific features available on switch chips on certain MikroTik devices.
*   Includes port-based features, such as port mirroring, VLAN settings, etc.
*   Configurations are specific to the particular switch chip and device

### **VLAN:**

*   Virtual LAN segmentation.
*   Configured using `/interface vlan`

```routeros
/interface vlan add name=vlan10 vlan-id=10 interface=ether2
```

### **VXLAN:**

*   Virtual eXtensible LAN.
*   Layer 2 overlay networking protocol.
*   Can be used to connect geographically dispersed LANs using an L3 network underlay.
*   Configured using `/interface vxlan`

```routeros
/interface vxlan add name="vxlan1" vni=1000 remote-address=10.0.0.200 interface=ether1
```

### **Firewall and QoS:**

*   **Connection tracking:**  Keeps track of network connections.
*   **Firewall:** Filters packets based on rules.
*   **Packet Flow in RouterOS:** Order of rule processing in chains (input, forward, output).
*   **Queues:** Used for QoS and traffic shaping.
*   **Case studies:** Different use cases for firewalls and QoS.
*   **Kid Control:**  Time-based access rules for kids.
*   **UPnP and NAT-PMP:**  Port forwarding solutions for applications.

```routeros
/ip firewall filter add chain=input action=drop connection-state=invalid
/ip firewall nat add chain=srcnat action=masquerade out-interface=ether1
/queue simple add name=voip target=192.168.1.0/24 max-limit=1M/1M priority=1
```

### **IP Services (DHCP, DNS, SOCKS, Proxy):**

*   **DHCP:** Dynamic IP address allocation.
*   **DNS:** DNS server and client configuration.
*   **SOCKS:** Proxy server for SOCKS protocol.
*   **Proxy:** Web proxy features

```routeros
/ip dhcp-server add address-pool=pool1 interface=ether2
/ip dns set servers=8.8.8.8,8.8.4.4
/ip socks set enabled=yes
/ip proxy set enabled=yes
```

### **High Availability Solutions:**

*   **Load Balancing:**  Distributing traffic across multiple links.
*   **Bonding:** Combining multiple interfaces into a single logical interface.
*   **HA Case Studies:** Examples of HA configurations.
*   **Multi-chassis Link Aggregation Group (MLAG):** Combining multiple links between two chassis.
*   **VRRP:** Virtual Router Redundancy Protocol.
*   **VRRP Configuration Examples:** Examples of configuring VRRP

```routeros
/interface bonding add name=bond1 mode=802.3ad slaves=ether1,ether2
/routing vrrp add interface=bond1 vrid=1 priority=100
```

### **Mobile Networking:**

*   **GPS:** GPS support for location.
*   **LTE:** 4G/LTE support for mobile internet.
*   **PPP:** Point-to-Point Protocol for dial-up and VPNs.
*   **SMS:** SMS functionality.
*   **Dual SIM Application:**  Using two SIM cards.

```routeros
/interface lte set lte1 apn=internet
/ppp secret add name=user1 password=password profile=default
```

### **Multi Protocol Label Switching - MPLS:**

*   **MPLS Overview:**  Label switching for faster routing.
*   **MPLS MTU:**  Setting MTU for MPLS.
*   **Forwarding and Label Bindings:** How labels are used in routing.
*   **EXP bit and MPLS Queuing:**  QoS using EXP bit.
*   **LDP:**  Label Distribution Protocol.
*   **VPLS:** Virtual Private LAN Service.
*   **Traffic Engineering:**  Optimizing traffic flow.

```routeros
/mpls interface add interface=ether2
/mpls ldp set enabled=yes
```

### **Network Management:**

*   **ARP:** Address Resolution Protocol.
*   **Cloud:**  MikroTik's cloud service for management.
*   **DHCP, DNS, SOCKS, Proxy** (mentioned above)
*   **Openflow:**  SDN protocol for network control

```routeros
/ip arp print
/system cloud set enabled=yes
```

### **Routing:**

*   **Routing Protocol Overview:** Overview of routing protocols.
*   **Moving from ROSv6 to v7:** Considerations when upgrading.
*   **Multi-core Support:** Utilization of multi-core CPUs for routing.
*   **Policy Routing:** Advanced route selection.
*   **VRF:** Virtual Routing and Forwarding.
*   **OSPF, RIP, BGP:**  Dynamic routing protocols.
*  **RPKI:** Route Origin Validation
*   **Route Selection and Filters:** Controlling route selection.
*   **Multicast:** Configuring multicast.
*   **Routing Debugging Tools:** Tools for troubleshooting routing.
*   **BFD:** Bidirectional Forwarding Detection.
*  **IS-IS:** Intermediate System to Intermediate System Protocol

```routeros
/routing ospf instance add name=ospf1 router-id=10.0.0.1
/routing bgp instance add name=bgp1 as=65000 router-id=10.0.0.1
```

### **System Information and Utilities:**

*   **Clock:** System time and timezone settings.
*   **Device-mode:**  Router operating mode.
*   **E-mail:** Email configuration for alerts.
*   **Fetch:**  File transfer utility.
*   **Files:** File management.
*   **Identity:** Set router hostname.
*   **Interface Lists:** Create custom interface groups
*   **Neighbor discovery:**  Discovers other network devices
*  **Note:** Ability to add system notes
*   **NTP:** Network Time Protocol.
*   **Partitions:** Managing storage partitions
*   **Precision Time Protocol:** (PTP) Provides accurate time synchronization
*   **Scheduler:** Schedule events.
*   **Services:** Enabled RouterOS services.
*   **TFTP:**  Trivial File Transfer Protocol.

```routeros
/system clock set time-zone-name=America/New_York
/system identity set name=MyRouter
/system scheduler add name=daily-backup on-event="/export file=backup"
```

### **Virtual Private Networks:**

*   **6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier:** VPN configuration examples.
* Wide variety of VPN options available

```routeros
/interface wireguard add name=wg1 listen-port=51820
/interface wireguard peers add allowed-address=10.0.0.2/32 endpoint=10.0.0.100:51820  public-key=abc
/ip ipsec peer add address=10.0.0.100/32 enc-algorithm=aes-256
/ip ipsec policy add src-address=1