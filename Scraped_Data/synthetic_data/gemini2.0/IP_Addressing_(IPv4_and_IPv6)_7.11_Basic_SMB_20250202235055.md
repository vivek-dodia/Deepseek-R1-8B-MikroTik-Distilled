Okay, let's dive deep into MikroTik RouterOS, focusing on IP Addressing and a broader scope of related features. This will be comprehensive and practical, tailored for an SMB environment.

# MikroTik RouterOS Deep Dive: IP Addressing & Beyond

This document will serve as an in-depth guide to managing IP addressing (both IPv4 and IPv6), related networking concepts, and crucial features in MikroTik RouterOS. We will cover configuration, troubleshooting, security, and more, specifically for a Small to Medium Business (SMB) context using RouterOS 7.11.

## 1. Comprehensive Configuration Scenario & Requirements

**Scenario:** A small office needs to connect to the internet and have a local network. The office uses a single MikroTik router (e.g., hEX or RB4011iGS+RM). They require a standard IPv4 network and are planning to implement IPv6 in the near future. Additionally, they need internal servers accessible using specific ports and secure user access to the router.

**Specific MikroTik Requirements:**

*   **WAN Connection:** Dynamic IPv4 address assigned by the ISP via DHCP.
*   **LAN Network:** Private IPv4 network (192.168.88.0/24).
*   **IPv6:** Enable IPv6 using DHCP-PD on the WAN and assign a /64 subnet on the LAN.
*   **Internal Server:** Web server on 192.168.88.10:8080 and SSH on 192.168.88.10:22 (port forwarding).
*   **Security:** Basic firewall rules and secure router management access.
*  **Network Services:** DNS caching.
*   **User Authentication:** Usernames and password with read-only rights.

## 2. Step-by-Step MikroTik Implementation (CLI & Winbox)

This section will outline the steps involved in configuring our scenario using both the MikroTik CLI and the Winbox GUI.

### 2.1. CLI Implementation

1.  **Login:** Access your MikroTik device via SSH or through the terminal in Winbox.
2.  **Interface Configuration (WAN):**
    ```mikrotik
    /interface ethernet
    set [find name=ether1] name=WAN comment="Internet Facing Interface"
    /ip dhcp-client
    add interface=WAN disabled=no comment="ISP DHCP Client"
    ```
    **Explanation:** We rename the interface for clarity and enable DHCP client on the WAN interface.

3. **Interface Configuration (LAN):**
    ```mikrotik
    /interface ethernet
    set [find name=ether2] name=LAN comment="Internal Network"
    /ip address
    add address=192.168.88.1/24 interface=LAN comment="Internal Network Address"
    ```
   **Explanation:** We rename the LAN interface and set a static IPv4 address for the router's LAN side.

4.  **IPv6 Configuration (WAN):**
    ```mikrotik
    /ipv6 dhcp-client
    add interface=WAN request=address,prefix comment="IPv6 Client"
    ```
    **Explanation:** Enables IPv6 DHCP-PD on the WAN interface.

5.  **IPv6 Configuration (LAN):**
    ```mikrotik
    /ipv6 address
    add address=::1/64 interface=LAN comment="LAN IPv6 Interface"
    ```
    **Explanation:**  Sets a link-local IPv6 address for the LAN interface. RouterOS will also automatically generate IPv6 local addresses.

6.  **IP Address Pool:**

     ```mikrotik
    /ip pool
    add name=dhcp_pool_lan ranges=192.168.88.10-192.168.88.254 comment="LAN DHCP Pool"
    ```
    **Explanation:** Create a pool of IPv4 addresses to be assigned to LAN clients by the DHCP server.

7. **DHCP Server (IPv4):**
    ```mikrotik
    /ip dhcp-server
    add address-pool=dhcp_pool_lan interface=LAN lease-time=10m name=dhcp-lan disabled=no
    /ip dhcp-server network
    add address=192.168.88.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.88.1 comment="DHCP Server Network"
    ```
    **Explanation:** Enable and configure the DHCP server on the LAN interface. We also configure DNS servers and default gateway for DHCP clients.

8. **DHCP Server (IPv6):**

      ```mikrotik
     /ipv6 dhcp-server
     add interface=LAN name=dhcpv6-lan address-pool=default use-interface-subnet=yes preferred-lifetime=10m valid-lifetime=1d  comment="DHCPv6 Server"
    /ipv6 pool
     add name=default prefix=::/64
     ```
    **Explanation:** Enables DHCPv6 service to assign IPv6 addresses to connected devices

9.  **NAT (Port Forwarding):**

     ```mikrotik
    /ip firewall nat
    add chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=8080 protocol=tcp dst-port=8080 in-interface=WAN comment="Web Server"
    add chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=22 protocol=tcp dst-port=22 in-interface=WAN comment="SSH"
    add action=masquerade chain=srcnat out-interface=WAN comment="NAT Outgoing Traffic"
     ```
    **Explanation:** Configures port forwarding for the web and SSH servers, and enables NAT to allow internal clients to access the internet.

10. **DNS settings:**
    ```mikrotik
    /ip dns
    set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8 cache-max-ttl=1d comment="DNS settings"
   ```
   **Explanation:** Enabled DNS cache and specified forwarder DNS servers.

11. **Firewall:**
    ```mikrotik
    /ip firewall filter
    add chain=input action=accept connection-state=established,related comment="Accept established & related connections"
    add chain=input action=drop in-interface=WAN comment="Drop Invalid connections"
    add chain=input action=accept protocol=icmp comment="Accept ICMP"
    add chain=input action=accept protocol=tcp dst-port=8291 comment="Accept Winbox access"
    add chain=input action=drop comment="Drop everything else"
    add chain=forward action=accept connection-state=established,related comment="Accept established & related connections"
    add chain=forward action=drop in-interface=WAN comment="Drop invalid forwarding"
    add chain=forward action=accept comment="Accept forwarded traffic"
     ```
     **Explanation:** A basic firewall configuration that permits established connections, ICMP, winbox access and blocks other input traffic to the router.  Also allows all forwarded traffic, this is very permissive so consider blocking some traffic between network segments.

12. **User Management:**
    ```mikrotik
    /user group
    add name=read_only policy=read
    /user
    add name=readonlyuser password=YourPassword group=read_only
    ```
    **Explanation:** Creates a user group with read-only access and a user with that permission. Remember to use secure passwords.

### 2.2. Winbox Implementation

1.  **Connect:** Open Winbox and connect to your router.
2.  **Interface Configuration:** Navigate to `Interfaces` and rename `ether1` to "WAN" and `ether2` to "LAN". Add a comment if desired.
3.  **IPv4 Address:** Go to `IP > Addresses` and add an address `192.168.88.1/24` to the "LAN" interface.
4.  **DHCP Client:** Go to `IP > DHCP Client` and add an entry with the interface set to "WAN."
5.  **IPv6 Address:** Go to `IPv6 > Addresses` and add address `::1/64` on interface `LAN`.
6.  **IPv6 DHCP Client:** Go to `IPv6 > DHCP Client` and add an entry with the interface set to "WAN". Ensure request address and prefix are selected.
7. **IP Pool:** Go to `IP > Pool` and create the pool with name `dhcp_pool_lan` and the desired range.
8.  **DHCP Server (IPv4):** Go to `IP > DHCP Server`, click add, select `LAN` interface. Navigate to `Networks` and add network with `192.168.88.0/24` and set the DNS servers.
9.  **DHCP Server (IPv6):** Go to `IPv6 > DHCP Server`, click add, select `LAN` interface. Also add an IPv6 Pool as mentioned in the CLI section.
10. **NAT:** Go to `IP > Firewall > NAT`, click add and make 3 rules, first 2 with dst-nat chain, specifying the address and port to forward, and the third rule for NAT masquerade.
11. **DNS:** Go to `IP > DNS` and set DNS servers and enable `Allow Remote Requests`.
12. **Firewall:** Go to `IP > Firewall > Filter Rules`, add required input and forward rules.
13. **User:** Go to `System > Users`, add the read-only group and then a new user with required credentials and assign them to the new group.

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
# Interface configuration (WAN)
/interface ethernet set [find name=ether1] name=WAN comment="Internet Facing Interface"
/ip dhcp-client add interface=WAN disabled=no comment="ISP DHCP Client"

# Interface configuration (LAN)
/interface ethernet set [find name=ether2] name=LAN comment="Internal Network"
/ip address add address=192.168.88.1/24 interface=LAN comment="Internal Network Address"

# IPv6 configuration (WAN)
/ipv6 dhcp-client add interface=WAN request=address,prefix comment="IPv6 Client"

# IPv6 configuration (LAN)
/ipv6 address add address=::1/64 interface=LAN comment="LAN IPv6 Interface"

# IP Pool
/ip pool add name=dhcp_pool_lan ranges=192.168.88.10-192.168.88.254 comment="LAN DHCP Pool"

# DHCP Server (IPv4)
/ip dhcp-server add address-pool=dhcp_pool_lan interface=LAN lease-time=10m name=dhcp-lan disabled=no
/ip dhcp-server network add address=192.168.88.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.88.1 comment="DHCP Server Network"

#DHCP Server (IPv6)
/ipv6 dhcp-server add interface=LAN name=dhcpv6-lan address-pool=default use-interface-subnet=yes preferred-lifetime=10m valid-lifetime=1d  comment="DHCPv6 Server"
/ipv6 pool add name=default prefix=::/64

# NAT (Port Forwarding)
/ip firewall nat add chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=8080 protocol=tcp dst-port=8080 in-interface=WAN comment="Web Server"
/ip firewall nat add chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=22 protocol=tcp dst-port=22 in-interface=WAN comment="SSH"
/ip firewall nat add action=masquerade chain=srcnat out-interface=WAN comment="NAT Outgoing Traffic"

# DNS Settings
/ip dns set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8 cache-max-ttl=1d comment="DNS settings"

# Firewall
/ip firewall filter add chain=input action=accept connection-state=established,related comment="Accept established & related connections"
/ip firewall filter add chain=input action=drop in-interface=WAN comment="Drop Invalid connections"
/ip firewall filter add chain=input action=accept protocol=icmp comment="Accept ICMP"
/ip firewall filter add chain=input action=accept protocol=tcp dst-port=8291 comment="Accept Winbox access"
/ip firewall filter add chain=input action=drop comment="Drop everything else"
/ip firewall filter add chain=forward action=accept connection-state=established,related comment="Accept established & related connections"
/ip firewall filter add chain=forward action=drop in-interface=WAN comment="Drop invalid forwarding"
/ip firewall filter add chain=forward action=accept comment="Accept forwarded traffic"

# User Management
/user group add name=read_only policy=read
/user add name=readonlyuser password=YourPassword group=read_only
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, & Diagnostics

### Common Pitfalls

*   **Firewall Rule Order:**  The order of firewall rules is critical; rules are processed sequentially.
*   **NAT Issues:** Incorrect NAT settings can block internet access or port forwarding.
*   **DHCP Conflicts:** Conflicting DHCP ranges or static IPs may cause network issues.
*   **Interface Configuration:** Ensure the correct interface is selected for each configuration (WAN/LAN).
*   **IPv6 Conflicts:**  Improper IPv6 setup, particularly when using DHCP-PD, can result in clients failing to acquire IPv6 addresses.
*   **Incorrect MTU:** A misconfigured MTU can cause connectivity problems especially with PPPoE or VPN tunnels.

### Troubleshooting & Diagnostics

*   **`ping`:** Test reachability to other devices or the internet.
*   **`traceroute`:** Identify the network path taken by packets to find where issues occur.
*   **`torch`:** Packet capturing tool to see real-time network traffic. This is great for finding out specific packets or protocols that are not working.
*   **`/log print`:** Review router logs for errors or warnings.
*   **`/system resource monitor`:** Check CPU and memory usage, which can indicate performance bottlenecks.
*   **`/interface print stats`:** View interface statistics to monitor traffic.
*    **`/tool bandwidth-test`**: Measure the bandwidth.
*    **`/tool profile`**: Identify CPU or memory intensive processes
*    **Winbox > Tools > Packet Sniffer**:  Graphical interface for packet capturing.
*  **Winbox > Tools > Torch**: Graphical interface for real-time traffic analysis.
* **Winbox > System > Health**: Monitor hardware health parameters.

**Example Troubleshooting:**

* **Problem:** No internet access on LAN client
    * **Action:** Use `ping` to check if you can reach an external IP, and if not, verify `nat` is configured correctly and the WAN is receiving an IP.
 *   **Problem:** Website not accessible via port forwarding
    * **Action:** use `torch` to verify if the traffic is reaching the port on the WAN interface, and if it is reaching the LAN server. Check the `dst-nat` configuration.

## 5. Verification & Testing

1.  **Internet Access:**
    *   Use a LAN client to access a website and perform a speed test.
    *   Use `ping 8.8.8.8` or `ping google.com` from the MikroTik terminal.
2.  **Local Network:**
    *   Ping between different devices in the local network.
3.  **Port Forwarding:**
    *   From a client outside the LAN, try to access the web server and SSH using the public IP.
4.  **IPv6:**
    *   Check the client has an IPv6 address.
    *   From the client, try to reach `ipv6.google.com`.
    *   From the router, use `ping ipv6.google.com`.

## 6. Related MikroTik-Specific Features, Capabilities, & Limitations

*   **Bridging:** Connect network segments logically to have one broadcast domain (Layer 2).
*   **Routing:** Dynamically route packets based on destination using static routes, OSPF, RIP, BGP.
*   **Firewall:** Powerful stateful packet filtering for securing the network.
*   **Quality of Service (QoS):** Traffic shaping and prioritization.
*   **VPN:** Secure connections to remote networks using IPsec, WireGuard, L2TP, etc.
*   **DHCP Server:** Dynamic IPv4 and IPv6 address assignment with lease management.
*   **DNS Server:** Caching DNS resolver, which allows to speed up common lookups, also useful for custom DNS records.
*   **Scripting:** Automate RouterOS tasks using scripts.
*   **CAPsMAN:** Centralized management of multiple wireless access points.
*  **Netwatch**: Monitoring tool that helps detecting outages based on ping or specific http/https checks.
*  **Limitations:**
    *   Hardware resources limitations (CPU, RAM, storage) based on model.
    *   Software license restrictions on certain features.
    *   Some advanced feature such as VXLAN or MACsec may have hardware limitations, depending on switch chip features.
    *   Specific features or implementations can vary between different RouterOS versions.
    *   Configuration complexity on more complex scenarios.

## 7. MikroTik REST API Examples

For this example, we will focus on fetching basic RouterOS system information.

**API Endpoint:** `/system/resource`

**Request Method:** GET

**Example Request (using curl):**

```bash
curl -k -u "apiuser:apipassword" -H "Content-Type: application/json" https://<router_ip>/rest/system/resource
```

**Note:** `apiuser` and `apipassword` should be replaced with a user with API access. The `-k` flag skips certificate verification. Ensure you have the api user enabled.

**Example Response (JSON Payload):**

```json
{
    ".id": "*0",
    "uptime": "5h1m58s",
    "version": "7.11",
    "build-time": "2023-04-20 13:55:58",
    "free-memory": "967MiB",
    "total-memory": "1272MiB",
    "cpu": "ARMv7",
    "cpu-frequency": "880MHz",
    "cpu-load": "3%",
    "free-hdd-space": "109MiB",
    "total-hdd-space": "128MiB",
    "write-sect-since-reboot": "1818",
    "architecture-name": "arm",
    "board-name": "RB4011iGS+RM",
    "platform": "RouterOS"
}
```

**Example API Call to disable/enable an interface:**

**API Endpoint:** `/interface/ethernet`

**Request Method:** PUT

**Example JSON Payload (to disable ether3 interface):**

```json
{
    ".id":"*2",
    "disabled":"true"
}

```

**Explanation:** The `.id` field identifies the interface you wish to modify (you can discover ids using a GET method) and the field `disabled` has a boolean value, use true or false to toggle the interface status.

**API Response (Successful):**
```
{
    "message": "updated"
}
```

**Example API Call to add a new firewall rule:**

**API Endpoint:** `/ip/firewall/filter`

**Request Method:** POST

**Example JSON Payload (to allow traffic to port 80):**

```json
{
    "chain": "forward",
    "action": "accept",
    "protocol": "tcp",
    "dst-port": "80",
    "comment":"Allow port 80"
}
```

**Explanation:** Creates a new forward rule in the firewall to allow traffic to port 80.

**API Response (Successful):**
```
{
    "message": "added",
    "ret": {
        ".id": "*4"
     }
}
```

**Note:** To interact with the MikroTik REST API, you need to configure an API user with the appropriate rights.

## 8. In-Depth Explanations of Core Concepts (MikroTik Implementation)

*   **Bridging:** In MikroTik, bridges create a single Layer 2 broadcast domain by linking multiple interfaces. They are useful for combining multiple interfaces into a single LAN.
*   **Routing:** RouterOS uses a routing table and various routing protocols (static, OSPF, RIP, BGP) to determine the path for packets. It evaluates the routes and calculates the best way to route traffic.
*   **Firewall:** MikroTik's stateful firewall filters packets based on rules, connection state, and more. It's a core component for security.
*   **NAT (Network Address Translation):**  RouterOS uses NAT to translate private IP addresses to public ones, enabling access to the internet. Masquerading is used for this purpose.
*  **IP Address Pools:**  Ranges of IP addresses that can be used for assigning dynamically by the DHCP server.
*  **IP Settings:** General IP configuration options such as ARP, and disabled IPv4 or IPv6.

## 9. Security Best Practices (MikroTik)

*   **Secure Passwords:** Use strong, unique passwords for all user accounts.
*   **Disable Default User:** Disable the default admin user or change its password.
*   **Firewall Rules:** Implement robust firewall rules to block unauthorized access.
*   **Secure Services:** Limit the exposed services (e.g., disable unnecessary services).
*   **Winbox Access:** Restrict Winbox access only from trusted IPs or enable two-factor authentication
*   **Regular Updates:** Keep RouterOS updated to patch security vulnerabilities.
*   **Monitor Logs:** Regularly review logs for suspicious activity.
*   **VPN for Remote Access:** Use VPN instead of exposing router management to the internet.
*   **Certificates:** Use strong TLS certificates for secure connections.
*   **API Access:** Protect the REST API by using separate user accounts and disabling it unless necessary.

## 10. Detailed Explanations & Configuration Examples (Additional MikroTik Topics)

### IP Addressing (IPv4 and IPv6)
* We have already covered IPv4 and IPv6 addresses extensively. MikroTik's addresses are defined in `/ip address` for IPv4, and `/ipv6 address` for IPv6. Address allocation via DHCP is handled through `DHCP Client` and `DHCP Server`, and their IPv6 counterparts `/ipv6 dhcp-client` and `/ipv6 dhcp-server`

### IP Pools
* MikroTik IP pools are managed using `/ip pool`. Pools are used by DHCP to allocate IP addresses dynamically.  You can define ranges and name the pools. Pools can be created for both IPv4 and IPv6 using `/ipv6 pool`

### IP Routing
* MikroTik's routing configuration is handled by `/ip route` for IPv4 and `/ipv6 route` for IPv6. Static and dynamic routing is available.
    * **Static routing**: `/ip route add dst-address=10.0.0.0/24 gateway=192.168.88.2`
    * **Dynamic routing (OSPF)**: The configuration is under `/routing ospf`.

### IP Settings
*  General IP Settings are located in `/ip settings`. Here, you can manage ARP (enabled by default), disabled IPv4 or IPv6, disable ICMP redirect and other settings.

### MAC server
* The MAC Server is used to allow connections from Winbox via MAC address.
* `/tool mac-server set allowed-interfaces=all enabled=yes`.

### RoMON
* RoMON (Router Management Overlay Network) allows to manage multiple MikroTik devices from a central console, even if they're not IP reachable.
* `/tool romon set enabled=yes` and use `/tool romon monitor` to monitor devices in the RoMON network.

### WinBox
* Winbox is a GUI application to manage MikroTik devices. It connects via MAC address or IP address over port `8291`.
* The default settings allow access from any IP, you can restrict IPs in `/ip service` and by adding a firewall rule allowing access to port `8291` from specific IP.

### Certificates
* MikroTik supports certificates for secure connections. Certificates can be configured under `System > Certificates`.
* Certificates can be used for IPsec, HTTPS and other secure services.

### PPP AAA
* MikroTik supports PPP (Point-to-Point Protocol) authentication and authorization, you can enable authentication based on CHAP and PAP protocols in `PPP > Profiles > Use Authentication`
* The authentication can be done on local users or using external RADIUS services.

### RADIUS
* RouterOS can act as a RADIUS client to allow access via external servers. RADIUS servers are added under `PPP > Secrets > Use RADIUS`. The RADIUS server configuration is located in `PPP > Secrets > Use RADIUS`

### User / User groups
* User groups are managed in `/user group` with policies for the user rights.
    * `add name=read_only policy=read`.
* User accounts are managed in `/user`, where you specify the username, password and the user group.
    * `add name=test password=test group=read_only`

### Bridging and Switching
* MikroTik bridges are under `interface > bridge` and combine different ports to work as a single Layer 2 interface.
    * `/interface bridge add name=bridge_lan`.
* Ports can be added as bridge ports
     * `/interface bridge port add interface=ether3 bridge=bridge_lan`.

### MACVLAN
* MACVLAN allows multiple virtual interfaces on a single physical interface sharing its mac address.
     * `/interface macvlan add interface=ether2 name=macvlan1 mac-address=02:00:00:00:00:01`.

### L3 Hardware Offloading
* Hardware offloading can improve throughput by leveraging the switch chip capabilities. Offloading configurations depends on the device and specific hardware chip.
*  Can be enabled in `/interface/ethernet`, `hw-offload=yes`.
* Enable `hw-offload-ipsec`, `hw-offload-vlan`, `hw-offload-bridge` if supported.

### MACsec
* MACsec provides security at the Data Link Layer using encryption and authentication between nodes on the same local area network. Configuration is done under `/interface macsec`.
    * `/interface macsec add interface=ether2 key=00112233445566778899aabbccddeeff name=macsec-ether2`

### Quality of Service
* QoS (Quality of Service) in RouterOS is managed with queues.
* `/queue simple` is the default queue system for simple shaping. Use `add name=queue_name target=192.168.88.0/24 max-limit=5M`.
* Use `/queue tree` for advanced shaping.

### Switch Chip Features
* Switch chip features can be configured on supported devices. The configurations depends on the specific hardware and manufacturer.
* Configurations are available under `/interface/ethernet/switch` or `/interface/vlan-table` (if supported by the switch chip)

### VLAN
* VLAN (Virtual LAN) is implemented using VLAN tags to create logical segmentation on the Layer 2 network.
*  `interface vlan add name=vlan100 vlan-id=100 interface=bridge_lan`.

### VXLAN
* VXLAN (Virtual Extensible LAN) is a tunneling protocol for extending Layer 2 domains across Layer 3 networks.
 * `interface vxlan add name=vxlan1 vni=1000 interface=ether1 remote-address=10.0.0.2`.

### Firewall and Quality of Service

#### Connection tracking
* RouterOS keeps track of connections to filter them in the firewall and to improve performance. Connection tracking settings are located in `/ip settings`.

#### Firewall
* The firewall rules are configured in `/ip firewall filter` for filtering, `/ip firewall nat` for NAT and port forwarding and `/ip firewall mangle` for packet marking and traffic manipulation.
*  **Firewall Rules:**
    *   `add chain=forward action=drop in-interface=WAN comment="Drop Invalid forwarding"`.
    *   `add chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=80 protocol=tcp dst-port=80 in-interface=WAN`.
    *   `add chain=srcnat action=masquerade out-interface=WAN`.
    *   `add chain=input action=accept protocol=icmp`.

#### Packet Flow in RouterOS
* Packets are first processed by the Input chain, then Forward and if needed, by the Output chain.
* The packet first reaches the `/interface`, and depending on it's destination, it will hit Input, Forward or Output chains.
* If the packet's destination is not the router itself, it will go to the forwarding chain, being processed in the order rules are defined.

#### Queues
*  Queues are managed using `/queue simple` or `/queue tree`.
   * `add name=queue_name target=192.168.88.0/24 max-limit=5M`.

#### Firewall and QoS Case Studies
* Examples of use cases:
    * Block P2P traffic by filtering layer 7 protocols.
    * Prioritize VoIP traffic with QoS and packet marking.
    * Implement rate limiting per IP address.

#### Kid Control
*  Firewall and scheduling can be used for restricting access based on schedules and specific clients.
*  Use the `/ip firewall filter add` command to restrict specific IPs based on time and destination.

#### UPnP
* Universal Plug and Play (UPnP) can enable automatic port forwarding.
* Configuration are located in `/ip upnp set enabled=yes` and `/ip upnp interfaces`.

#### NAT-PMP
* NAT Port Mapping Protocol (NAT-PMP) is similar to UPnP but simpler, same usage as UPnP.

### IP Services

#### DHCP
* DHCP client and server configuration is handled by `/ip dhcp-client` and `/ip dhcp-server` for IPv4 and `/ipv6 dhcp-client` and `/ipv6 dhcp-server` for IPv6.
    * `/ip dhcp-server add interface=LAN address-pool=dhcp_pool`
    * `/ip dhcp-client add interface=WAN`
* Lease management is configured under `/ip dhcp-server lease`.

#### DNS
* MikroTik DNS server can cache frequently used queries to speed up name resolutions. DNS settings are under `/ip dns`.
    * `/ip dns set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8`.

#### SOCKS
* RouterOS can act as a SOCKS proxy server. The configuration is in `/ip socks`.
    * `/ip socks set enabled=yes`

#### Proxy
* RouterOS can act as a HTTP proxy. The configurations is under `/ip proxy`
   * `/ip proxy set enabled=yes`

### High Availability Solutions

#### Load Balancing
* Load balancing can be achieved using multiple WAN interfaces by using ECMP (Equal-Cost Multi-Path) routing.
* Configure routes with same distance to different gateways.
  *  `/ip route add gateway=10.0.0.1 distance=1`
  * `/ip route add gateway=10.0.1.1 distance=1`
* Also can be configured using PCC (Per Connection Classifier).

#### Bonding
* Bonding allows to use multiple Ethernet links as one single logical interface, increasing bandwidth or adding redundancy.
* Configurations under `interface > bonding`.
   * `/interface bonding add name=bond1 mode=802.3ad slaves=ether2,ether3`

#### Bonding Examples
*   **Active-backup**: Redundancy mode; only one link is active at any time.
*   **802.3ad (LACP)**: Dynamic mode, load sharing and link aggregation.
*   **Balance-rr**: Round-robin distribution of packets.
*   **Balance-xor**: Traffic distribution based on source and destination MAC addresses

#### HA Case Studies
* Examples of use cases:
    * Using VRRP for failover between two routers.
    * Using link bonding to aggregate connections to the core switch.
    * Using VRRP with multiple WAN connections.

#### Multi-chassis Link Aggregation Group
* Not a native MikroTik feature, but can be supported using specific configurations for switch-to-switch interconnectivity.

#### VRRP
* Virtual Router Redundancy Protocol (VRRP) is used to have a virtual IP address, and provides failover using a backup router if primary fails.
* VRRP configurations under `/interface vrrp`.
    * `/interface vrrp add interface=LAN vrid=1 address=192.168.88.2/24 priority=100`

#### VRRP Configuration Examples
*   **Simple failover**: VRRP config to take over the role as the master router when the primary router fails.
*   **Load sharing**: Using VRRP with multiple gateways to share the load.

### Mobile Networking

#### GPS
* MikroTik routers with GPS modules can provide location information using `/system gps`.
   * `/system gps monitor` to view the GPS status.

#### LTE
* LTE interface configuration is done under `interface > lte`.
    * `/interface lte set apn=your_apn user=your_user password=your_password`

#### PPP
* PPP configuration is done in `PPP` configuration tab, specifying the authentication mode. PPP can be used by dial-up connections or VPN.
    * `/ppp secret add name=user1 password=password1 service=pppoe`

#### SMS
* MikroTik LTE devices can send and receive SMS messages using the `/tool sms` utility.
  * `/tool sms send phone-number=5551234567 message="Hello"`

#### Dual SIM Application
* Dual SIM cards can be configured for redundancy or to balance between different providers using `/interface lte set sim-slot=1,2`.

### Multi Protocol Label Switching - MPLS

#### MPLS Overview
* MPLS is a routing method that can increase performance by labeling packets, it is used by ISPs.
* Configurations are located under the `/mpls` and `/mpls ldp` sections.

#### MPLS MTU
* MPLS requires enough MTU, which is specified under `/mpls`.
  * `/mpls set mtu=1508`.

#### Forwarding and Label Bindings
* MPLS uses labels to forward traffic, labels are assigned using different methods.

#### EXP bit and MPLS Queuing
* EXP bits can be used to prioritize MPLS traffic.
* QoS for MPLS traffic can be done with queues.

#### LDP
* Label Distribution Protocol (LDP) is used to establish label mappings between routers.
* `/mpls ldp set enabled=yes`.

#### VPLS
* Virtual Private LAN Service (VPLS) is a Layer 2 VPN over an MPLS network.
* `/mpls vpls add name=vpls1 vni=1000 remote-id=10.0.0.2`.

#### Traffic Eng
* MPLS Traffic Engineering is used to optimize the network usage based on QoS and bandwidth requirements.

#### MPLS Reference
* Check documentation for a complete reference of MPLS commands.

### Network Management

#### ARP
* Address Resolution Protocol (ARP) is used to map IP to MAC addresses.
*