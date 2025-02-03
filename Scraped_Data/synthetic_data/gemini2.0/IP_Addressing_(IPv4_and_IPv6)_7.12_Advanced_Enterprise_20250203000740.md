Okay, let's dive into creating comprehensive documentation for MikroTik RouterOS IP addressing and related features, tailored for an enterprise-level network on RouterOS 7.12.

# MikroTik RouterOS: Enterprise IP Addressing and Advanced Networking

This document provides a deep dive into IP addressing, routing, and related advanced features within MikroTik RouterOS, specifically targeted for enterprise environments using RouterOS 7.12. We will explore IPv4 and IPv6 configurations, implement security best practices, and leverage a variety of MikroTik-specific tools.

## 1. Comprehensive Configuration Scenario

**Scenario:** An enterprise network with multiple departments requires separate VLANs for security and management purposes. The router acts as a core routing and firewall device with public IPv4 and IPv6 addressing. This example will focus on the following aspects:

*   **Internet Connection:** One public IPv4 address and a delegated IPv6 prefix from the ISP.
*   **Internal Networks:**
    *   VLAN 10:  Corporate Network (192.168.10.0/24 IPv4, 2001:db8:10::/64 IPv6)
    *   VLAN 20:  Guest Network (192.168.20.0/24 IPv4, 2001:db8:20::/64 IPv6)
    *   VLAN 30:  Management Network (192.168.30.0/24 IPv4, 2001:db8:30::/64 IPv6)
*   **Routing:** Dynamic routing using OSPF for internal networks, static routing for default gateway.
*   **Firewall:**  Basic filtering and NAT for IPv4 traffic.
*   **Security:** Secure remote access using SSH and strong passwords.

**MikroTik Requirements:**

*   RouterOS 7.12 or later (compatible with 6.x as noted)
*   Multi-interface RouterBOARD (e.g. CCR series).
*   Basic networking knowledge

## 2. Step-by-Step Implementation

Here’s a step-by-step implementation using CLI commands with explanations, and guidance on how to perform the equivalent using Winbox.

### Step 1: Interface Configuration

*   **Interface Identification:**  Assume `ether1` is the WAN interface, and `ether2` connects to the internal switch.
*   **VLAN Setup:** Configure VLANs on `ether2`.

**CLI:**

```routeros
# Add VLAN interfaces
/interface vlan
add name=vlan10 vlan-id=10 interface=ether2
add name=vlan20 vlan-id=20 interface=ether2
add name=vlan30 vlan-id=30 interface=ether2

# Set Interface Names (Optional but helpful)
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN-Trunk
```

**Winbox:**

1.  Navigate to `Interfaces`
2.  Click the `+` and choose `VLAN`
3.  Enter a `Name`, `VLAN ID` and `Interface`
4.  Repeat for each VLAN
5. Select `Ethernet` Tab, double-click `ether1` and change the name to `WAN`.
6. Repeat for `ether2`, naming it `LAN-Trunk`.

### Step 2: IP Addressing

*   **WAN IP:** Assume `203.0.113.10/24` is the public IPv4 address and `2001:db8:1::/48` is the delegated IPv6 prefix. We'll assign `2001:db8:1::1/64` to the WAN interface.
*   **VLAN IPs:**  Assign IP addresses to each VLAN interface.

**CLI:**

```routeros
/ip address
add address=203.0.113.10/24 interface=WAN
add address=192.168.10.1/24 interface=vlan10
add address=192.168.20.1/24 interface=vlan20
add address=192.168.30.1/24 interface=vlan30
add address=2001:db8:1::1/64 interface=WAN
add address=2001:db8:10::1/64 interface=vlan10
add address=2001:db8:20::1/64 interface=vlan20
add address=2001:db8:30::1/64 interface=vlan30
```

**Winbox:**

1.  Navigate to `IP` > `Addresses`
2.  Click the `+` button.
3.  Enter the `Address` (e.g., `203.0.113.10/24`), select the `Interface` (e.g., `WAN`).
4.  Repeat for all IPs, both IPv4 and IPv6.

### Step 3: IP Pools

Create IP pools for DHCP server on each VLAN.

**CLI:**

```routeros
/ip pool
add name=vlan10-pool ranges=192.168.10.100-192.168.10.254
add name=vlan20-pool ranges=192.168.20.100-192.168.20.254
add name=vlan30-pool ranges=192.168.30.100-192.168.30.254

add name=vlan10-pool6 ranges=2001:db8:10::100-2001:db8:10::fffe
add name=vlan20-pool6 ranges=2001:db8:20::100-2001:db8:20::fffe
add name=vlan30-pool6 ranges=2001:db8:30::100-2001:db8:30::fffe

```

**Winbox:**

1.  Navigate to `IP` > `Pools`
2.  Click the `+` button
3.  Enter the `Name`, and range in the `Ranges` field.
4. Repeat for all pools.

### Step 4: DHCP Server Configuration

Set up DHCP servers on each VLAN interface for both IPv4 and IPv6

**CLI:**
```routeros
/ip dhcp-server
add name=dhcp-vlan10 interface=vlan10 address-pool=vlan10-pool
add name=dhcp-vlan20 interface=vlan20 address-pool=vlan20-pool
add name=dhcp-vlan30 interface=vlan30 address-pool=vlan30-pool

/ipv6 dhcp-server
add name=dhcp6-vlan10 interface=vlan10 address-pool=vlan10-pool6
add name=dhcp6-vlan20 interface=vlan20 address-pool=vlan20-pool6
add name=dhcp6-vlan30 interface=vlan30 address-pool=vlan30-pool6
```

**Winbox:**

1.  Navigate to `IP` > `DHCP Server`
2.  Click the `+` button.
3.  Enter the `Name`, select the `Interface`, and choose the corresponding `Address Pool`.
4. Repeat for each DHCP server (both IPv4 and IPv6).

### Step 5: IP Routing

*   **Default Route:** Set the default route to the ISP's gateway (Assume `203.0.113.1` for IPv4 and `2001:db8:1::2` for IPv6).
*   **OSPF:**  Configure OSPF for dynamic routing within the internal network.

**CLI:**

```routeros
/ip route
add dst-address=0.0.0.0/0 gateway=203.0.113.1
/ipv6 route
add dst-address=::/0 gateway=2001:db8:1::2

/routing ospf instance
add name=ospf-instance redistribute-connected=yes

/routing ospf area
add instance=ospf-instance area-id=0.0.0.0

/routing ospf interface
add interface=vlan10 area=0.0.0.0 instance=ospf-instance
add interface=vlan20 area=0.0.0.0 instance=ospf-instance
add interface=vlan30 area=0.0.0.0 instance=ospf-instance
```

**Winbox:**

1.  Navigate to `IP` > `Routes`.
2.  Click the `+` button.
3.  Enter `0.0.0.0/0` as `Dst. Address`, and the ISP gateway address (`203.0.113.1`) as the `Gateway`.
4.  Repeat for IPv6, setting `::/0` for the destination and `2001:db8:1::2` for the gateway.
5. Navigate to `Routing` > `OSPF`
6. Click on the `Instances` tab and add a new instance, setting the `name` and selecting `yes` for `Redistribute connected`
7. Click on the `Areas` tab and add a new area, using `0.0.0.0` for the `area id` and the instance name defined before.
8. Click on the `Interface` tab and add new entries for each of the internal network interfaces and choosing the `area` and `instance`.

### Step 6: Firewall and NAT

*   **Basic NAT:**  Configure NAT for IPv4 outbound traffic.
*   **Basic Firewall:**  Allow established/related connections, drop invalid connections and some basic forwarding rules.

**CLI:**

```routeros
/ip firewall nat
add chain=srcnat action=masquerade out-interface=WAN
/ip firewall filter
add chain=input connection-state=established,related action=accept
add chain=input connection-state=invalid action=drop
add chain=forward connection-state=established,related action=accept
add chain=forward connection-state=invalid action=drop
add chain=input protocol=icmp action=accept
add chain=input protocol=tcp dst-port=22 action=accept
add chain=forward src-address=192.168.10.0/24 dst-address=192.168.20.0/24 action=drop

```

**Winbox:**

1.  Navigate to `IP` > `Firewall` > `NAT`
2.  Click the `+` button. Select `srcnat` for `Chain`, `masquerade` for `Action`, and the `WAN` interface in `Out. Interface`
3. Navigate to `IP` > `Firewall` > `Filter Rules`
4.  Click the `+` button, and add the filters shown above, modifying the needed parameters.
### Step 7: Security Configurations

*  **Enable SSH Server**
*  **Change Default Admin Password**
*  **Disable Telnet Service**

**CLI:**

```routeros
/ip service set telnet disabled=yes
/user set admin password="your_strong_password"
```

**Winbox:**

1.  Navigate to `IP` > `Services`
2.  Double click the `telnet` service and check the `disabled` check box.
3. Navigate to `System` > `Users`
4.  Double click on the `admin` user and change the `Password`.

## 3. Complete MikroTik CLI Configuration

Here's a consolidated configuration block that can be pasted into your MikroTik terminal (CLI):

```routeros
/interface vlan
add name=vlan10 vlan-id=10 interface=ether2
add name=vlan20 vlan-id=20 interface=ether2
add name=vlan30 vlan-id=30 interface=ether2
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN-Trunk

/ip address
add address=203.0.113.10/24 interface=WAN
add address=192.168.10.1/24 interface=vlan10
add address=192.168.20.1/24 interface=vlan20
add address=192.168.30.1/24 interface=vlan30
add address=2001:db8:1::1/64 interface=WAN
add address=2001:db8:10::1/64 interface=vlan10
add address=2001:db8:20::1/64 interface=vlan20
add address=2001:db8:30::1/64 interface=vlan30

/ip pool
add name=vlan10-pool ranges=192.168.10.100-192.168.10.254
add name=vlan20-pool ranges=192.168.20.100-192.168.20.254
add name=vlan30-pool ranges=192.168.30.100-192.168.30.254
add name=vlan10-pool6 ranges=2001:db8:10::100-2001:db8:10::fffe
add name=vlan20-pool6 ranges=2001:db8:20::100-2001:db8:20::fffe
add name=vlan30-pool6 ranges=2001:db8:30::100-2001:db8:30::fffe

/ip dhcp-server
add name=dhcp-vlan10 interface=vlan10 address-pool=vlan10-pool
add name=dhcp-vlan20 interface=vlan20 address-pool=vlan20-pool
add name=dhcp-vlan30 interface=vlan30 address-pool=vlan30-pool
/ipv6 dhcp-server
add name=dhcp6-vlan10 interface=vlan10 address-pool=vlan10-pool6
add name=dhcp6-vlan20 interface=vlan20 address-pool=vlan20-pool6
add name=dhcp6-vlan30 interface=vlan30 address-pool=vlan30-pool6

/ip route
add dst-address=0.0.0.0/0 gateway=203.0.113.1
/ipv6 route
add dst-address=::/0 gateway=2001:db8:1::2

/routing ospf instance
add name=ospf-instance redistribute-connected=yes
/routing ospf area
add instance=ospf-instance area-id=0.0.0.0
/routing ospf interface
add interface=vlan10 area=0.0.0.0 instance=ospf-instance
add interface=vlan20 area=0.0.0.0 instance=ospf-instance
add interface=vlan30 area=0.0.0.0 instance=ospf-instance

/ip firewall nat
add chain=srcnat action=masquerade out-interface=WAN
/ip firewall filter
add chain=input connection-state=established,related action=accept
add chain=input connection-state=invalid action=drop
add chain=forward connection-state=established,related action=accept
add chain=forward connection-state=invalid action=drop
add chain=input protocol=icmp action=accept
add chain=input protocol=tcp dst-port=22 action=accept
add chain=forward src-address=192.168.10.0/24 dst-address=192.168.20.0/24 action=drop

/ip service set telnet disabled=yes
/user set admin password="your_strong_password"
```

## 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

*   **Incorrect Interface Configuration:** Double-check VLAN IDs, interface assignments.
*   **Firewall Blocking:** Use `torch` or `/tool/packet-sniffer` to analyze traffic flow. Verify firewall rules if communication fails.
*   **Routing Issues:** Check routing table (`/ip route print`). Ensure OSPF is configured correctly. Use `/routing ospf neighbor print` to verify OSPF adjacencies.
*   **DHCP problems:** Ensure the correct IP pools are configured and that you do not have overlapping IP addresses.
*   **Connectivity:** Use `ping` and `traceroute` to diagnose connectivity problems.

**Example CLI Troubleshooting Commands:**

```routeros
/tool torch interface=WAN
/tool packet-sniffer
/ip route print
/routing ospf neighbor print
/ping 8.8.8.8
/traceroute 8.8.8.8
/log print
```

## 5. Verification and Testing

1.  **Ping Test:**  Verify connectivity from client devices on each VLAN to the router's gateway addresses and external IPs.
2.  **Traceroute:** Trace routes to verify path selection through the router.
3.  **DHCP Lease:** Check that DHCP clients are obtaining leases correctly. Use `/ip dhcp-server lease print`.
4.  **Firewall Checks:** Use `/ip firewall filter print` and `connection tracking` to verify firewall operation.

## 6. Related MikroTik-Specific Features

*   **Bridging:**  If you needed to pass VLANs untagged to the connected switch, we could use a bridge instead of just VLAN interfaces.
*   **L3 Hardware Offloading:** Some RouterBOARDs can hardware-offload routing for better performance (check `/interface ethernet print detail` for offloading support).
*   **MACVLAN:** Create virtual interfaces with unique MAC addresses on the same ethernet interface.
*   **Switch Chip Features**: MikroTik routers with dedicated switch chips offer more advanced VLAN switching options that are not available on interfaces using the CPU only.
*   **RoMON:** Router Management Overlay Network (RoMON) provides out-of-band management, especially useful in larger deployments and also in troubleshooting scenarios.
*   **WinBox:** MikroTik's GUI for easy configuration and management.
*   **Certificates:** Implement TLS for HTTPS access to the web interface.

## 7. MikroTik REST API Examples

**API Endpoint**: `/ip/address`

**Request Method**: `POST` to create, `PUT` to update, `DELETE` to remove

**Example API Call to Add an IP Address:**

```json
{
   "method": "POST",
   "endpoint": "/ip/address",
   "data": {
      "address": "192.168.100.1/24",
      "interface": "vlan10"
   }
}
```

**Expected Response (Successful):**

```json
{
  "id": "*1",
  "address": "192.168.100.1/24",
   "interface": "vlan10",
   "dynamic": false,
   "invalid": false
}
```

**Example API Call to Delete an IP Address:**

```json
{
    "method": "DELETE",
   "endpoint": "/ip/address",
   "id": "*1"
}
```

**Expected Response (Successful):**

```json
{
"message": "removed"
}
```
**Note**: Use HTTP basic authentication to authenticate with the MikroTik API. The username and password should correspond to a MikroTik user with the necessary API permissions.

## 8. In-Depth Core Concepts: MikroTik Implementation

*   **Bridging:** MikroTik bridges behave similarly to a traditional switch, connecting different interfaces on the same Layer 2 network.
*   **Routing:** MikroTik handles IP routing using its integrated routing table. Dynamic routing protocols (OSPF, BGP) and static routes can be configured. RouterOS has powerful policy routing capabilities that allow you to specify routes depending on the traffic source and destination.
*   **Firewall:** The stateful firewall provides granular control over traffic flow by inspecting network packets. It is based on chains (input, output, forward), where rules are evaluated in order.
*   **Connection Tracking:** MikroTik uses connection tracking to maintain state for TCP, UDP and other connection types. This helps optimize firewall performance and is used by NAT and other RouterOS services.

## 9. Security Best Practices

*   **Strong Passwords:**  Use strong, unique passwords for all user accounts.
*   **Disable Unused Services:** Disable unnecessary services like Telnet.
*   **Firewall Rules:** Implement a strict firewall rule set to limit access.
*   **HTTPS Access:**  Use HTTPS for accessing the router's web interface and disable HTTP.
*   **Secure Remote Access:** Use SSH instead of Telnet and consider IP address restrictions.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version.
*   **Access Control:** Restrict management access to specific IP addresses or networks.

## 10. Detailed Explanations and Configuration Examples

This section will expand on all the topics listed in the "Requirements" section.

### IP Addressing (IPv4 and IPv6)

*   **IPv4:** Uses 32-bit addresses. Example: `192.168.1.1/24` (where /24 is the network mask). The main limitation of IPv4 is the number of available addresses, which is why we are moving towards IPv6.
*   **IPv6:** Uses 128-bit addresses. Example: `2001:db8::1/64`. It offers a larger address space and improved routing. IPv6 is also usually paired with auto-configuration options (SLAAC) for ease of deployment.
    * **Subnetting**: In MikroTik, IPv4 and IPv6 addressing configuration are similar. In IPv4, subnet masks are expressed in CIDR notation (e.g., /24), while in IPv6, the prefix length (e.g., /64) indicates the network size. A smaller subnet (like /28) will offer fewer host addresses than a larger subnet (like /24).

   **Configuration Examples:**

   ```routeros
   # IPv4
    /ip address add address=192.168.10.1/24 interface=vlan10
   # IPv6
   /ipv6 address add address=2001:db8:10::1/64 interface=vlan10
   ```

   **Notes:**
    * IPv4 addresses are configured under `/ip address`.
    * IPv6 addresses are configured under `/ipv6 address`.
    * The `address` parameter is used to define the IP address and network mask.
    * The `interface` parameter specifies which interface the IP address should be assigned to.

### IP Pools

*   **Purpose**: IP pools define ranges of IP addresses used by services like DHCP servers.
*   **Configuration Examples**:

   ```routeros
   /ip pool add name=pool1 ranges=192.168.1.100-192.168.1.200
   /ipv6 pool add name=pool1-6 ranges=2001:db8:1::100-2001:db8:1::200
   ```

  **Notes**:
    * IPv4 pools are configured under `/ip pool` and IPv6 pools under `/ipv6 pool`.
    * The `ranges` parameter defines the start and end of the IP address range.

### IP Routing

*   **Static Routing:** Manually configured routes to specific networks or gateways.
*   **Dynamic Routing (OSPF, BGP, RIP):** Allows routers to automatically learn and adjust routes as needed.
*   **Policy-Based Routing:** Route traffic based on more granular criteria, such as source/destination IP and other connection details.
   **Configuration Examples**:
   ```routeros
   # Static route to 10.10.10.0/24 via 192.168.1.2
   /ip route add dst-address=10.10.10.0/24 gateway=192.168.1.2
   # OSPF configuration
   /routing ospf instance add name=ospf-inst redistribute-connected=yes
   /routing ospf area add instance=ospf-inst area-id=0.0.0.0
   /routing ospf interface add interface=vlan10 area=0.0.0.0 instance=ospf-inst
   ```

   **Notes:**
    * Static routes are configured under `/ip route`.
    * Dynamic routing configurations will vary by routing protocol (OSPF, BGP, RIP).
    * Policy-based routing is set using firewall mangle rules.

### IP Settings

*   **General settings:**  Parameters like IP forwarding, ICMP settings.
    **Configuration Example**:

    ```routeros
    /ip settings set allow-fast-path=yes tcp-syncookie=yes
    ```

**Notes**:
    * Settings are modified under `/ip settings`

### MAC server

* **Purpose**: Used for remotely managing RouterOS devices at layer 2
* **Configuration Example**:
   ```routeros
    /tool mac-server set enabled=yes allowed-interface=all
   ```
**Notes**:
    *  Enabled to manage the router at layer 2 via Winbox (useful when router has no IP address).
    *  `allowed-interface` dictates which interface can be used for layer 2 access.

### RoMON

* **Purpose**: RoMON provides out-of-band management, especially useful in larger deployments and also in troubleshooting scenarios.
* **Configuration Example**:
   ```routeros
  /tool romon set enabled=yes id=default secret="romon_secret"
  /tool romon port add interface=ether1
   ```
**Notes**:
    * `enabled` enables or disables RoMON functionality.
    * `id` defines the RoMON identifier.
    * `secret` adds an extra layer of security to the RoMON connection.
    * `interface` defines the interface which allows RoMON connections.

### WinBox

* **Purpose**: MikroTik's GUI for easy configuration and management.
* **Functionality**:  Allows configuring almost all aspects of RouterOS.
* **Notes**: Winbox is a very powerful management tool, but not all functions are fully available. Some specific settings or troubleshooting actions must be done using the CLI.

### Certificates

*   **Purpose:** Enable secure HTTPS access to the RouterOS web interface, and other services which use TLS.
*  **Configuration Example**:
   ```routeros
    /certificate import file-name=cert.pem
    /ip service set www-ssl certificate=cert
    ```
**Notes**:
    * `file-name` must match the certificate in your router's file system.
    * Use the `www-ssl` service to apply the certificate to web access.

### PPP AAA

*   **Purpose**: Provides authentication, authorization, and accounting for PPP connections (PPPoE, PPTP, L2TP).
*   **Configuration Example**:
   ```routeros
   /ppp aaa set use-radius=yes
   ```
**Notes**:
    * Uses `radius` server or the `local` database as authentication backend.
    * It is very important to configure `ppp secret` records for local authentication.

### RADIUS

*   **Purpose**: Provides centralized authentication for various services.
*   **Configuration Example**:

   ```routeros
   /radius add address=192.168.1.10 secret="radius_secret" service=ppp,dhcp
   ```
**Notes**:
    * `address` should point to the RADIUS server.
    * `secret` should match the one configured on the RADIUS server.
    * `service` indicates which services use this RADIUS server.

### User / User groups

*   **Purpose:** Create users with different access levels to manage the RouterOS.
*   **Configuration Example**:

   ```routeros
    /user group add name=full_access policy=ftp,read,write,test,password,web,winbox,api,romon
    /user add name=john group=full_access password="secure_password"
    ```
**Notes**:
    * `/user group` defines a group with specific permissions.
    * `/user add` creates the new user with specified permissions.

### Bridging and Switching

*   **Bridging**: Connects multiple interfaces at Layer 2 allowing devices in the bridge to communicate directly with each other.
*   **Switching**:  Handles traffic forwarding based on MAC addresses at the hardware level.
*   **Configuration Examples**:

   ```routeros
   /interface bridge add name=bridge1
   /interface bridge port add bridge=bridge1 interface=ether2
   /interface bridge port add bridge=bridge1 interface=ether3
   ```
**Notes**:
    * Interfaces can be part of a bridge or a hardware switch, not both.

### MACVLAN

*   **Purpose**: Create multiple virtual interfaces with different MAC addresses from the same physical interface.
*   **Configuration Example**:
   ```routeros
    /interface macvlan add interface=ether2 mac-address=02:00:00:00:00:01 name=macvlan1
    /interface macvlan add interface=ether2 mac-address=02:00:00:00:00:02 name=macvlan2
    ```
**Notes**:
    * Allows multiple devices to have different MAC addresses, even using the same physical interface.

### L3 Hardware Offloading

*   **Purpose**: Accelerate routing performance using hardware offload on some RouterBOARD chipsets.
*   **Verification**:  Check `/interface ethernet print detail` to see if the interface supports offloading.
*   **Configuration**: Automatic when supported, no manual config needed.

**Notes**:
    * Not all RouterBOARDs support L3 hardware offloading.

### MACsec

*   **Purpose**: Provides layer 2 security to all traffic over the ethernet link.
*   **Configuration Example**:
    ```routeros
    /interface macsec add name=macsec1 interface=ether2 key=0123456789ABCDEF0123456789ABCDEF
    ```
**Notes**:
    * The `key` field specifies the security association key for MACsec
    * Must be supported by the hardware interface.

### Quality of Service (QoS)

* **Purpose**: Prioritize certain types of traffic over others, usually based on source, destination or protocol.
* **Configuration Example**:
  ```routeros
   /queue tree add name=queue1 parent=global-total max-limit=100M
  /queue tree add name=queue1-prio1 parent=queue1 queue=default priority=1
   /queue tree add name=queue1-prio2 parent=queue1 queue=default priority=2
   /ip firewall mangle add chain=forward dst-port=443 action=mark-packet new-packet-mark=prio1
   /queue simple add max-limit=50M packet-mark=prio1 target=192.168.0.0/24 queue=queue1-prio1
  /queue simple add max-limit=25M packet-mark=prio2 target=192.168.1.0/24 queue=queue1-prio2
   ```
**Notes**:
    * QoS is a very complex topic. This example shows how to use queue trees and simple queues to manage bandwidth.
    * This uses a firewall rule to mark packets and those are the packets targeted by the queues.
    * Mangle rules mark packets, while queues define how much bandwidth will be used by each type of marked packet.

### Switch Chip Features

*   **Purpose**: Use advanced capabilities of hardware switch chips on specific RouterBOARD models for advanced layer 2 capabilities.
*   **Configuration Example**:

    ```routeros
    /interface ethernet switch vlan add vlan-id=10 ports=ether2,ether3
    ```

**Notes**:
    * Available on specific RouterBOARD models with switch chips.
    * Check the product documentation for specific features.

### VLAN

*   **Purpose**: Create virtual LANs to isolate and segment networks on the same physical infrastructure.
*   **Configuration Example**:
   ```routeros
    /interface vlan add name=vlan10 vlan-id=10 interface=ether2
    /interface vlan add name=vlan20 vlan-id=20 interface=ether2
   ```
**Notes**:
    * VLANs use tags (802.1q) on top of Ethernet links to separate different broadcast domains.

### VXLAN

*   **Purpose**: A tunneling protocol that encapsulate Layer 2 traffic over an IP network. Used for layer 2 extensions across Layer 3 networks.
*   **Configuration Example**:

   ```routeros
   /interface vxlan add name=vxlan1 vni=1000  remote-address=192.168.1.10 interface=ether1
   ```

**Notes**:
    * Requires both endpoints to have a VXLAN interface configured.
    * `VNI` is used to separate different layer 2 network extensions.

### Firewall and Quality of Service (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP)

*   **Connection Tracking**: Maintains state for connections allowing stateful firewall rules.
    *   This is a core part of MikroTik firewall functionality.
*   **Firewall**: Filter traffic, perform NAT and more.

  **Configuration Example**:
   ```routeros
     # Forward traffic to a service port
     /ip firewall nat add chain=dstnat dst-port=80 protocol=tcp action=dst-nat to-addresses=192.168.1.10 to-ports=80
     # Block traffic from certain source
     /ip firewall filter add chain=forward src-address=192.168.2.0/24 action=drop
    ```
**Notes**:
    *  Multiple chains are available (`input`, `output` and `forward`).
    *  Packets are processed according to rules configured on each chain, on order.
*   **Packet Flow in RouterOS**: The packet flows from interface, to firewall, through queues and finally to it's destination.
*   **Queues**: Manage traffic bandwidth, create priorities, and shape the traffic.
*   **Firewall and QoS Case Studies**: Use-case based firewall configurations and quality of service rules for example to prioritizes VoIP traffic or limit torrent traffic.
*  **Kid Control**: Uses Layer 7 firewall rules or time based rules to manage internet access for kids.
*  **UPnP**: Allow internal services to be published to the Internet automatically.
    * Enabled by default, but can be configured in `/ip upnp`.
*  **NAT-PMP**: An alternative to UPnP to publish internal services to the Internet.
    * Configured via `/ip nat-pmp`

###