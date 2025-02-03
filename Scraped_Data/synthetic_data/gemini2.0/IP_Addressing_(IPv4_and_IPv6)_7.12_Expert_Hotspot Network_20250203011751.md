Okay, let's dive into a comprehensive exploration of MikroTik RouterOS configuration with a focus on IP addressing, and incorporating the full range of your requested topics. This will be an extensive document, so get ready!

**Document Purpose:** To provide a detailed guide on configuring IP addressing (IPv4 and IPv6) and related RouterOS features for a Hotspot Network, targeting a mid- to advanced-level MikroTik administrator.

**Target RouterOS Version:** 7.12 (and also providing context for 6.48 and the v7 family)

**Configuration Level:** Expert

**Network Scale:** Hotspot Network (SOHO/SMB, with notes for scaling to larger deployments)

**Specific Configuration:**

*   Subnet: 102.245.201.0/24
*   Interface Name: ether-24

## 1. Comprehensive Configuration Scenario and MikroTik Requirements

**Scenario:** We are setting up a hotspot network in a small office or public space. Users will connect wirelessly and receive IP addresses from a specific subnet. The MikroTik router will act as the central point for internet access, DHCP server, and potentially other services. The core focus here is on IP addressing management with related features.

**MikroTik Requirements:**

*   **IP Addressing:** Configure a static IP address for the specified interface (`ether-24`) within the defined subnet, with consideration for the gateway address.
*   **DHCP Server:**  Set up a DHCP server to dynamically assign IP addresses within the same subnet to connected clients.
*   **Basic Routing:** Ensure the router knows how to route traffic between the local network and the internet.
*   **Firewall:** Implement basic firewall rules to protect the network and users.
*  **Wireless:** If the Router has wireless, we will add a basic AP configuration.
*   **Monitoring and Logging:**  Set up logging and monitoring to track network activity and troubleshoot issues.

## 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

### Step 1: Setting the IP Address on `ether-24` (CLI)

1.  **Open a Terminal:** Connect to your MikroTik router using SSH or Winbox terminal.
2.  **Add the IP Address:**

```mikrotik
/ip address
add address=102.245.201.1/24 interface=ether-24
```

   *   `address=102.245.201.1/24`: Assigns the IP address 102.245.201.1 with a /24 subnet mask. We use .1 as convention for the gateway IP, which we'll use in the DHCP setup
   *   `interface=ether-24`: Specifies the interface to which this IP address is bound.

### Step 1: Setting the IP Address on `ether-24` (Winbox)

1.  **Connect to Winbox:** Connect to your MikroTik router using Winbox.
2.  **Go to IP -> Addresses:** Navigate to IP -> Addresses in the menu.
3.  **Click the "+" button:** Click the "+" button to add a new address.
4.  **Fill the Address Information:**
    *   **Address:** `102.245.201.1/24`
    *   **Interface:** `ether-24`
5.  **Click "Apply" and then "OK"** to save the configuration.

### Step 2: Setting up the DHCP Server (CLI)

1.  **Create an IP Pool:** This defines the range of IP addresses that will be dynamically assigned.

```mikrotik
/ip pool
add name=hotspot-pool ranges=102.245.201.2-102.245.201.254
```

   *   `name=hotspot-pool`: Names the IP pool for easy reference.
   *   `ranges=102.245.201.2-102.245.201.254`: Specifies the range of addresses available. The .1 address is reserved for the router itself.

2.  **Create a DHCP Server:**

```mikrotik
/ip dhcp-server
add address-pool=hotspot-pool interface=ether-24 lease-time=1d name=hotspot-dhcp
```

    *   `address-pool=hotspot-pool`: Assigns the DHCP server to use the `hotspot-pool`.
    *   `interface=ether-24`: Specifies the interface on which the DHCP server will listen for requests.
    *   `lease-time=1d`: Specifies that DHCP leases are valid for 1 day
    *   `name=hotspot-dhcp`: Specifies the name of the DHCP server for easier managment

3.  **Configure DHCP Network settings:**

```mikrotik
/ip dhcp-server network
add address=102.245.201.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=102.245.201.1
```

    *   `address=102.245.201.0/24`: Specifies the subnet to which the DHCP server is applicable
    *   `dns-server=8.8.8.8,8.8.4.4`: Specifies Google's public DNS servers
    *   `gateway=102.245.201.1`: Sets the router's IP as the gateway for DHCP clients

### Step 2: Setting up the DHCP Server (Winbox)

1.  **Go to IP -> Pool:** Navigate to IP -> Pool in the menu.
2.  **Click the "+" button:** Click the "+" button to add a new pool.
3.  **Fill the Pool Information:**
    *   **Name:** `hotspot-pool`
    *   **Ranges:** `102.245.201.2-102.245.201.254`
4.  **Click "Apply" and then "OK"** to save the configuration.
5.  **Go to IP -> DHCP Server:** Navigate to IP -> DHCP Server in the menu.
6.  **Click the "+" button:** Click the "+" button to add a new DHCP Server.
7.  **Fill the Server Information:**
    *   **Name:** `hotspot-dhcp`
    *   **Interface:** `ether-24`
    *   **Address Pool:** `hotspot-pool`
    *   **Lease Time:** `1d`
8.  **Click "Apply" and then "OK"** to save the configuration.
9. **Go to IP -> DHCP Server -> Networks**
10. **Click the "+" button:** Click the "+" button to add a new DHCP network
11. **Fill the Network Information:**
    *   **Address:** `102.245.201.0/24`
    *   **Gateway:** `102.245.201.1`
    *   **DNS Servers:** `8.8.8.8,8.8.4.4`
12. **Click "Apply" and then "OK"** to save the configuration.

### Step 3: Basic Routing (CLI)

1.  **Add a Default Route:** This is a temporary configuration for demonstration, usually provided by your ISP. In a Hotspot Network, you would use a dynamic routing protocol or a default route. If there's a gateway, it should be included. Let's assume a Gateway Address of 192.168.1.1 (this address is example). If you don't have a gateway or are using a different IP, please use the correct one for your needs.

```mikrotik
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.1.1
```

   *   `dst-address=0.0.0.0/0`: Represents any destination address (default route).
   *   `gateway=192.168.1.1`: Specifies the gateway to use for traffic destined outside the local network. This address will vary based on your connection.

### Step 3: Basic Routing (Winbox)

1.  **Go to IP -> Routes:** Navigate to IP -> Routes in the menu.
2.  **Click the "+" button:** Click the "+" button to add a new route.
3.  **Fill the Route Information:**
    *   **Dst. Address:** `0.0.0.0/0`
    *   **Gateway:** `192.168.1.1`
4.  **Click "Apply" and then "OK"** to save the configuration.

### Step 4: Basic Firewall (CLI)
*  **Add NAT Rule:** NAT will be required to access the internet when using a private IP.
```mikrotik
/ip firewall nat
add chain=srcnat action=masquerade out-interface=<YOUR_WAN_INTERFACE>
```
Replace `<YOUR_WAN_INTERFACE>` with your actual WAN interface name (e.g., ether1, pppoe-out1).

   *   `chain=srcnat`: Specifies source NAT (Network Address Translation).
    *   `action=masquerade`: Changes the source IP to the router's IP.
    *   `out-interface=<YOUR_WAN_INTERFACE>`: NATs packets from the local subnet when they go through a specific interface

### Step 4: Basic Firewall (Winbox)
1.  **Go to IP -> Firewall -> NAT:** Navigate to IP -> Firewall -> NAT
2.  **Click the "+" button:** Click the "+" button to add a new NAT rule
3.  **Go to Tab "General":**
    *   **Chain:** `srcnat`
4.  **Go to Tab "Action":**
    *   **Action:** `masquerade`
5.   **Go to Tab "Out. Interface:**
    *  **Out. Interface:** `<YOUR_WAN_INTERFACE>`
6. **Click "Apply" and then "OK"** to save the configuration.

### Step 5: Basic Wireless (CLI)
*  **Enable Interface:**
```mikrotik
/interface wireless
enable wlan1
```
*   **Set Configuration**
```mikrotik
/interface wireless
set wlan1 mode=ap-bridge ssid=hotspot-wifi band=2ghz-b/g/n channel-width=20mhz frequency=2437 country=us security-profile=default
```
   *   `mode=ap-bridge`: Access Point bridge mode.
    *   `ssid=hotspot-wifi`: Wireless SSID.
    *   `band=2ghz-b/g/n`: 2.4GHz band.
    *    `channel-width=20mhz`: 20 Mhz channel width.
    *   `frequency=2437`: Channel.
    *   `country=us`: Select Country.
    *   `security-profile=default`: Default Profile - Requires a Security Profile setup.

*  **Set Security Profile**
```mikrotik
/interface wireless security-profiles
set [ find default=yes ] mode=dynamic-keys authentication-types=wpa2-psk,wpa3-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=<YOUR_WPA2_PASSWORD> wpa3-pre-shared-key=<YOUR_WPA3_PASSWORD>
```
    * `mode=dynamic-keys`: Dynamic keys
    * `authentication-types=wpa2-psk,wpa3-psk` Supported Protocols
    * `unicast-ciphers=aes-ccm`: Unicast Cipher
    * `group-ciphers=aes-ccm`: Group Cipher
    * `wpa2-pre-shared-key=<YOUR_WPA2_PASSWORD>` WPA2 Password
    * `wpa3-pre-shared-key=<YOUR_WPA3_PASSWORD>` WPA3 Password

### Step 5: Basic Wireless (Winbox)

1. **Go to Wireless:** Navigate to Wireless
2. **Enable Interface:** Click on interface "wlan1" and check the check box `Enabled`.
3. **Go to Wireless Interfaces:** Click on interface "wlan1"
4. **Go to "Wireless" tab:**
    *   **Mode:** `ap bridge`
    *   **SSID:** `hotspot-wifi`
    *   **Band:** `2ghz-b/g/n`
    *   **Channel Width:** `20mhz`
    *   **Frequency:** `2437`
    *   **Country:** `us`
5.  **Go to "Security Profiles" tab:** Click the button "Security Profiles".
6.  **Select "default" profile:** Select "default" profile.
    *    **Mode:** `dynamic keys`
    *    **Authentication Types:** `wpa2-psk`, `wpa3-psk`
    *    **Unicast Ciphers:** `aes-ccm`
    *    **Group Ciphers:** `aes-ccm`
    *    **WPA2 Pre-Shared Key:** `<YOUR_WPA2_PASSWORD>`
    *    **WPA3 Pre-Shared Key:** `<YOUR_WPA3_PASSWORD>`
7.  **Click "Apply" and then "OK"** to save the configuration.

## 3. Complete MikroTik CLI Configuration Commands

Here is the combined CLI configuration:

```mikrotik
/ip address
add address=102.245.201.1/24 interface=ether-24

/ip pool
add name=hotspot-pool ranges=102.245.201.2-102.245.201.254

/ip dhcp-server
add address-pool=hotspot-pool interface=ether-24 lease-time=1d name=hotspot-dhcp

/ip dhcp-server network
add address=102.245.201.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=102.245.201.1

/ip route
add dst-address=0.0.0.0/0 gateway=192.168.1.1

/ip firewall nat
add chain=srcnat action=masquerade out-interface=<YOUR_WAN_INTERFACE>

/interface wireless
enable wlan1

/interface wireless
set wlan1 mode=ap-bridge ssid=hotspot-wifi band=2ghz-b/g/n channel-width=20mhz frequency=2437 country=us security-profile=default

/interface wireless security-profiles
set [ find default=yes ] mode=dynamic-keys authentication-types=wpa2-psk,wpa3-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=<YOUR_WPA2_PASSWORD> wpa3-pre-shared-key=<YOUR_WPA3_PASSWORD>
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

### Pitfalls:

*   **Incorrect Interface:**  Double-check the interface name (`ether-24`) is correct. Errors result if the interface doesn't exist or is misconfigured.
*   **DHCP Conflicts:** Ensure no other DHCP servers are running on the same network segment.
*   **Routing Errors:**  Misconfigured default routes will prevent traffic from reaching the internet.  If you don't have a default gateway, try to traceroute to a common IP, such as Google's DNS server.
*   **Firewall Issues:** Overly restrictive firewall rules can block legitimate traffic, e.g., blocking DNS resolution.
*   **Incorrect Subnet:** Setting up the router with an incorrect subnet mask can lead to network communication issues.
*   **NAT Issues:** Without proper NAT, devices in your local network can't access the internet
*   **Wireless Issues:**  Incorrect country, channel, and security settings might cause connectivity problems. Also, incompatible security profiles.

### Troubleshooting:

1.  **`ping`:** Use the `ping` command to test basic connectivity:

    ```mikrotik
    /ping 102.245.201.1
    /ping 8.8.8.8
    ```

    *   If you cannot ping 102.245.201.1 there's something wrong with the router's local interface.
    *   If you cannot ping 8.8.8.8 and 102.245.201.1 is working, there is a routing or internet connectivity issue.

2.  **`traceroute`:** Use `traceroute` to trace the route packets are taking.

    ```mikrotik
    /tool traceroute 8.8.8.8
    ```

    This will help identify points of failure, showing the path the packets are taking towards the internet

3.  **`torch`:** Use `torch` to monitor live traffic on interfaces:

    ```mikrotik
    /tool torch interface=ether-24
    ```

    This will show all the incoming and outgoing traffic on the specified interface. You can select protocols and ports to refine your results.

4.  **`log`:** Review the system log to look for errors.

    ```mikrotik
    /system logging print
    ```

    Also, log using the specific log option:
    ```mikrotik
    /system logging action print
    ```

5. **Monitor Interface:** Review stats for the interface to check for errors.

    ```mikrotik
    /interface monitor ether-24
    ```
6. **Check DHCP Leases:** Ensure that devices are being properly leased IP addresses

    ```mikrotik
    /ip dhcp-server lease print
    ```
7. **Check Wireless Connections:** Ensure that devices are being properly connected to your wireless interface.
    ```mikrotik
    /interface wireless registration-table print
    ```

### Error Scenarios

1. **No IP Address on the Interface:** If the IP address is not assigned to the interface, all devices in the network will not be able to communicate. The log will show ARP issues and no responses from DHCP requests.
2. **Incorrect Gateway:** Incorrect gateway configuration can lead to issues when trying to access internet resources. Trace will show the traffic trying to reach the specified gateway, but never arriving at its destination.
3. **DHCP Server Not Enabled:** When a DHCP server is not enabled, clients will fail to get a private IP address and they will not be able to communicate.
4. **Wireless Security Mismatch:** If clients are failing to connect and authentication fails, there could be a security protocol/password issue.
5. **NAT Rule missing** If there are no NAT rules on the firewall, devices will not be able to reach the internet. The log will show packets hitting the firewall and not getting to their destination.

## 5. Verification and Testing Steps

1.  **Connect a Client:** Connect a device (laptop, phone) to `ether-24` (or to the Wireless Network).
2.  **Check IP Address:** Verify that the client receives an IP address within the `102.245.201.0/24` subnet. Check this on the client itself.
3.  **Ping the Router:**  Ping the router's IP (`102.245.201.1`) from the client.
4.  **Ping an External IP:** Ping an external IP address (e.g., 8.8.8.8) from the client.
5.  **Test Internet Access:** Browse the internet.
6.  **Monitor MikroTik:** Use the MikroTik's tools (`ping`, `traceroute`, `torch`) as explained above to verify proper operation of the network.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

### IP Addressing (IPv4 and IPv6)

*   **IPv4:**
    *   Static IP Addresses:  Directly assigned to an interface.
    *   DHCP Client: Allows the router to obtain an address from a DHCP server, typically from an ISP.
    *   DHCP Server:  Dynamically assigns IP addresses to clients.
    *   IP Pools: Manage and control address ranges for DHCP, Hotspot, etc.

*   **IPv6:**
    *   Static IPv6 Addresses: similar to IPv4, but uses IPv6 address format.
    *   DHCPv6 Client/Server: Similar to IPv4, but operates over IPv6
    *   Router Advertisement (RA): Sends Router Advertisements, to announce the IPv6 prefix.
    *   SLAAC: Stateless Address Auto Configuration - Allows hosts to automatically configure an IPv6 address.
    *   6to4/6in4 tunnels: Mechanisms to transit IPv6 packets over an IPv4 network.

### IP Pools

*   Used primarily for DHCP, PPPoE, and Hotspot assignments.
*   Can be subdivided and assigned to specific services.
*   Support for IP address ranges.

### IP Routing

*   Static Routes: Manually configured routes.
*   Dynamic Routing Protocols: OSPF, RIP, BGP.
*   Policy-Based Routing: Route based on source/destination criteria.
*   VRF: Virtual Routing and Forwarding for network segmentation.

### IP Settings

*   Includes various global settings (e.g., ARP).
*   `/ip settings`: Shows general IP settings
*   `/ip settings set allow-fast-path=yes`: Can enable fast-path optimization for better performance
*  `arp`: Specifies how ARP is managed on the interface
    * `arp=enabled`: ARP is enabled.
    * `arp=reply-only`: Router will not generate ARP requests, only respond to them.
    * `arp=disabled`: ARP is disabled on this interface.
    * `arp=proxy-arp`: Allows the router to act as a proxy and respond to ARP requests on behalf of other devices.

### MAC Server

*   Allows configuring the router as an ARP Proxy, or a server for MAC discovery.
*   Useful for scenarios with layer 2 connectivity or when you need to control and identify MAC addresses in the network.

### RoMON

*   Router Management Overlay Network.
*   Used to manage MikroTik routers remotely, even when they're not directly reachable via IP.
*   Requires enabling RoMON on the routers and connecting through a RoMON agent on a reachable router.
*   Useful for complicated network topologies.
*   Can allow access even if an error occurs during configuration, avoiding the need to physically access the router.
```mikrotik
/tool romon set enabled=yes id=my-romon-id
/tool romon port add interface=ether1
```
### WinBox

*   Graphical user interface for managing MikroTik devices.
*   Allows configuration using a more friendly approach.
*   Supports drag-and-drop configuration.
*   May be less powerful for some more advanced configurations that are available on the CLI.
*   Offers a good interface for beginners and administrators that prefer a graphical approach.

### Certificates

*   Used for secure connections, such as HTTPS for management, and VPN connections.
*   RouterOS can act as a Certificate Authority (CA) or generate and import certificates.
*   Used in conjuction with IPSEC, OpenVPN, and secure Web interfaces
*   Certificate Management is under `/system certificate`.
```mikrotik
/system certificate
print
```

### PPP AAA

*   Authentication, Authorization, and Accounting for PPP (Point-to-Point Protocol).
*   Used in conjunction with PPPoE, PPTP, L2TP tunnels.
*   Provides centralized user management.
*   Typically requires a RADIUS server.

### RADIUS

*   Remote Authentication Dial-In User Service.
*   A centralized authentication server used for user authentication in a PPP environment, or for hotspot management.
*   Typically runs on a separate server.

### User/User Groups

*   Used for RouterOS administration access.
*   Can be used to manage permissions and access control.
*   Good security practice to have different users and access levels.
*   RouterOS Users are managed in `/user`.

```mikrotik
/user print
```
```mikrotik
/user group print
```

### Bridging and Switching

*   Bridging allows joining multiple interfaces together at layer 2, effectively making them part of the same network segment.
*   Switching is a hardware-level bridge feature that can be optimized to increase performance, especially when routing is not required.
*   Allows network segments to share the same IP address range and broadcast domain.
*   Used for LAN setup, Wireless bridging, and some types of VPN connections.
```mikrotik
/interface bridge
print
```
### MACVLAN

*   A way to assign multiple logical MAC addresses to a single physical interface.
*   Each MAC VLAN can have its own IP configuration.
*   Usefull when a single interface requires multiple logical connections.
```mikrotik
/interface macvlan print
```

### L3 Hardware Offloading

*   Certain MikroTik devices can offload layer-3 processing to hardware, increasing performance.
*   Not available on all devices.
*   Improves packet forwarding speeds significantly.
*  `ip firewall layer7-protocol print` - Shows current offload settings

### MACsec

*   Media Access Control Security.
*   Provides layer 2 link encryption between devices.
*   Improves security for critical connections, especially in large networks.
*   Requires additional hardware support.

### Quality of Service (QoS)

*   Used to prioritize or limit specific types of traffic.
*   Implemented using queues and firewall rules.
*   Helps to ensure that critical traffic is not affected by other bandwidth-intensive applications.
```mikrotik
/queue simple
print
```

### Switch Chip Features

*   Access to the specific switch chip's settings and features.
*   Allows advanced configurations such as VLANs, rate limiting, and port mirroring.
*   Requires detailed knowledge of the switch chip's architecture and capabilities.

### VLAN

*   Virtual Local Area Networks.
*   Allows to logically segment the network into smaller broadcast domains.
*   Requires configuration both on the switch/router level and the end device level.
*   Useful for separating different departments or types of traffic, providing greater security.
```mikrotik
/interface vlan
print
```

### VXLAN

*   Virtual eXtensible Local Area Network.
*   Allows creation of Layer 2 networks across Layer 3 boundaries.
*   Supports network virtualization.
*  Useful for modern virtual environments where Layer 2 networks must be expanded.
```mikrotik
/interface vxlan print
```

### Firewall and Quality of Service (QoS)

#### Connection Tracking
 *   RouterOS automatically tracks connections to determine if the packet is part of an established connection.
 *   Stateful Firewall operation is based on connection tracking.

#### Firewall
*   Based on Chain, Rules, Actions
*   Filter rules control which traffic will be accepted/rejected
*   NAT rules control how source/dest IPs/ports will be modified.
```mikrotik
/ip firewall filter print
/ip firewall nat print
```

#### Packet Flow in RouterOS
*   RouterOS processes packets following a specific path:
   *   `Incoming Interface --> Prerouting Filter --> Routing Decision --> Postrouting Filter --> Outgoing Interface`

#### Queues
*   Used for QoS, prioritize traffic or set limits to specific flows
*  Can be set using Queue Types and Queue Trees.
*   Can be used for download/upload shaping, bandwidth limits and priority management.
```mikrotik
/queue type print
/queue tree print
```
#### Firewall and QoS Case Studies
*   Limit Bandwidth for specific users using Firewall + Simple Queues
*   Prioritize VOIP traffic using Firewall + Queue Trees
*   Implement traffic shaping

#### Kid Control
*   Firewall rules that are configured to restrict access to specific services based on source addresses and schedules.
*   Allows parents to control the time and resources their children can access.
*   Requires planning and careful implementation.

#### UPnP
*   Universal Plug and Play.
*   Allows devices within the network to automatically open ports on the firewall.
*   Can be a security risk, but is a very useful feature for user experience.
*   NAT-PMP is an alternative to UPnP.
*  Settings can be managed under `/ip upnp`.
*  Settings can be managed under `/ip upnp set enabled=yes allow-disable-external-interface=yes`.

#### NAT-PMP
*   NAT Port Mapping Protocol.
*   Alternative to UPnP.
*   Used for the same purpose.
*   Settings can be managed under `/ip nat-pmp`.
*  Settings can be managed under `/ip nat-pmp set enabled=yes allow-disable-external-interface=yes`.

### IP Services (DHCP, DNS, SOCKS, Proxy)

*   **DHCP:** Explained above.
*   **DNS:**
    *   DNS Cache: Improves DNS resolution performance.
    *   DNS Server: Allows the router to provide DNS services to local clients.
    *   Can be set using `/ip dns set servers=8.8.8.8,8.8.4.4`.
*   **SOCKS:** SOCKS Proxy server (can proxy HTTP/HTTPS/SOCKS traffic).
*   **Proxy:** HTTP Proxy.
    *   Can be transparent (the proxy works automatically without client configuration).
    *   Used for HTTP content filtering, caching, access control, etc.

### High Availability Solutions

#### Load Balancing
*   Distribute traffic accross different uplinks or connections.
*   Can be based on a variety of algorithms like Round Robin, Failover, etc.
*   Can be used to increase internet throughput, or provide redundancy for mission-critical applications.
```mikrotik
/ip firewall mangle print
```
#### Bonding
*   Links different physical interfaces together in order to increase bandwidth or provide redundancy.
*   Can be used with different modes like Balance-RR, Active-Backup, 802.3ad, etc
*   Requires additional care during configuration.
```mikrotik
/interface bonding print
```

#### Bonding Examples
*   Using bonding to increase bandwidth.
*   Using bonding for redundancy (in Active-Backup mode)

#### HA Case Studies
*   Setup of a High Availability firewall using VRRP
*   Setup of a Load Balancing environment
*   Network Failover configuration

#### Multi-chassis Link Aggregation Group (MLAG)
*   Allows different devices to act like they were bonded
*  Creates a more robust solution in larger networks
* Requires complex configuration

#### VRRP
*   Virtual Router Redundancy Protocol.
*   Allows multiple routers to share a virtual IP and improve network availability.
*   If the main router fails, the backup takes over without service interruptions.
```mikrotik
/interface vrrp
print
```

#### VRRP Configuration Examples
*   Setup of multiple VRRP routers and priority levels.
*   Configuring failover for high availability.
*  Implementation with and without preemption.

### Mobile Networking

#### GPS
*   Used for tracking RouterOS devices location.
*   Configuration and reading of GPS data.
*   `tools gps` command.
*  Can be used for location-based applications.

#### LTE
*   Configure and manage LTE interfaces (3G, 4G, 5G)
*   Settings are located on `/interface lte`
*  Can be used for Wireless Internet Connections

#### PPP
*   Point to Point Protocol is used on the dial-up interfaces
*   Used for modem configuration and dial-up connections
*  Settings are under `/interface ppp`

#### SMS
*   Can send and receive SMS messages using LTE interfaces
*   Used for configuration and network monitoring

#### Dual SIM Application
*   Configuration of Dual SIM devices
*   Can be used to switch between SIM card providers
*  Can use Failover or Load Balancing modes.

### Multi Protocol Label Switching (MPLS)

#### MPLS Overview
*   A mechanism used to speed up packet routing based on labels instead of IP addresses.
*   Used in ISP networks.
*  Complex Configuration

#### MPLS MTU
*   Used for configuration of the maximum MTU size for MPLS
*   Can be different from regular MTU

#### Forwarding and Label Bindings
*   RouterOS creates label mappings based on the destination IP addresses
*   Label Binding can be configured and controlled

#### EXP Bit and MPLS Queuing
*   The experimental bit can be used for QoS in MPLS networks
*   Can be used for setting priority between MPLS packets
*  Requires proper planning for implementation

#### LDP
*   Label Distribution Protocol, used for management of MPLS label distribution.
*   Must be configured in all devices.
*   Different LDP protocols and implementations may cause interoperability issues.

#### VPLS
*   Virtual Private LAN Service
*   Allows layer 2 VPN functionality using MPLS

#### Traffic Eng
*   Used to configure traffic engineering on the MPLS network
*   Used to control paths to guarantee the quality of service
* Complex Configuration.

#### MPLS Reference
*   Different MPLS configurations and examples, based on your network topology.
*  Different reference topologies must be understood.

### Network Management

#### ARP
*   Address Resolution Protocol
*   Used to resolve IP addresses to MAC addresses.
*   Can be managed on a per interface level.

#### Cloud
*   MikroTik's Cloud Management Solution
*   Allows management of MikroTik devices through a cloud interface
*  Requires a RouterOS license.

#### DHCP
*   Covered previously.

#### DNS
*   Covered previously.

#### SOCKS
*   Covered previously.

#### Proxy
*   Covered previously.

#### Openflow
*   Protocol used for Software Defined Networking (SDN)
*   Allows the Router to be configured externally using Openflow.
*   Not commonly used in standard setups.
*   Requires Openflow controller to operate.

### Routing

#### Routing Protocol Overview
*  Different Routing Protocols allow the routers to discover routes to other networks.
*  Static Routes, OSPF, RIP, BGP, are examples of routing protocols.

#### Moving from ROSv6 to v7 with examples
*   Significant changes in ROSv7, especially for routing.
*   Requires careful migration planning and testing.
*   Some routing protocols had significant modifications.

#### Routing Protocol Multi-core Support
*   Modern RouterOS devices can leverage multi-core CPU processing
*   This increases throughput and overall routing performance.

#### Policy Routing
*  Policy Based routing allows specific traffic flows to take different paths.
*  Requires configuration of Mangle rules and specific route tables.

#### Virtual Routing and Forwarding - VRF
*   Virtual Routing and Forwarding allows virtual routers to run in the same device.
*  Allows multiple routing domains and network segmentation.

#### OSPF
*   Open Shortest Path First.
*   A common routing protocol for enterprise networks.
*   Requires area and network configuration.

#### RIP
*   Routing Information Protocol
*   A simpler routing protocol, easier to understand and configure.
*   Used in smaller networks.

#### BGP
*   Border Gateway Protocol.
*   The routing protocol for the internet.
*   Used for inter-domain routing.
*   Complex configuration.
*  Requires ASN number.

#### RPKI
*   Resource Public Key Infrastructure.
*   Used to validate BGP routes and improve security.
*  Must be properly setup with certificates and configuration.

#### Route Selection and Filters
*   Used to prioritize routing paths.
*   BGP filters, OSPF cost, and other metrics will affect the route selection.

#### Multicast
*   Used for one-to-many communication
*  Used for streaming applications.
*  Specific configuration is needed.

#### Routing Debugging Tools
*   `traceroute`
*   `ping`
*   `torch`
*   Routing logs and