Okay, let's dive into a comprehensive guide on IP Pools within MikroTik RouterOS, focusing on practical implementation, troubleshooting, and security best practices. This guide will cover everything from basic setup to advanced configurations, and will be structured with your specified detailed requirements.

# MikroTik IP Pools: A Comprehensive Guide for SMB Networks

This document provides a detailed explanation of IP Pools within MikroTik RouterOS 7.11 (or relevant 6.x/7.x). We will cover configuration, common issues, security, and best practices, tailored for an SMB network environment.

**1. Comprehensive Configuration Scenario and Specific MikroTik Requirements**

**Scenario:** We will configure a MikroTik router for a small business network. The router needs to provide DHCP services to two separate subnets:

*   **LAN Network (Internal):** 192.168.1.0/24 for general user devices.
*   **Guest Network (WIFI):** 192.168.2.0/24 for guest devices, isolated from the LAN.

**Specific MikroTik Requirements:**

*   **Static IP:** Router will have a static IP address on the WAN side (e.g., received from ISP)
*   **DHCP:** Dynamic IP assignment using DHCP Server will be used.
*   **IP Pools:**  We need to define IP Pools for each DHCP scope.
*   **Firewall:** To secure the network, firewall rules will isolate the guest from the LAN.

**2. Step-by-Step MikroTik Implementation using CLI or Winbox with Detailed Explanations**

**Step 1: Accessing the Router**

*   **CLI:** SSH into the router using an SSH client (e.g., PuTTY). Use your username and password
*   **Winbox:** Download and open Winbox from the MikroTik website. Connect using the router's IP or MAC address.

**Step 2: Configuring IP Pools**
*   **CLI:**
     ```mikrotik
        /ip pool
        add name=lan-pool ranges=192.168.1.10-192.168.1.254
        add name=guest-pool ranges=192.168.2.10-192.168.2.254
     ```

*   **Winbox:**
    1.  Go to `IP` -> `Pool`.
    2.  Click the `+` button to add a new pool.
        *   `Name`: `lan-pool`
        *   `Ranges`: `192.168.1.10-192.168.1.254`
    3. Click `Apply`
    4.  Click the `+` button to add another new pool.
        *   `Name`: `guest-pool`
        *   `Ranges`: `192.168.2.10-192.168.2.254`
    5. Click `Apply`

**Explanation:**
*   The `/ip pool` command allows you to manage IP address pools.
*   `add name=...`: Creates a new pool with a given name.
*   `ranges=...`: Specifies the range of IP addresses that are part of the pool.

**Step 3: Configuring IP Addresses**

*   **CLI:**
    ```mikrotik
       /ip address
       add address=192.168.1.1/24 interface=ether2
       add address=192.168.2.1/24 interface=wlan1
    ```
*   **Winbox:**
    1.  Go to `IP` -> `Addresses`.
    2.  Click the `+` button to add a new address.
        *   `Address`: `192.168.1.1/24`
        *   `Interface`: `ether2` (your lan interface)
    3. Click `Apply`
    4.  Click the `+` button to add another new address.
        *   `Address`: `192.168.2.1/24`
        *   `Interface`: `wlan1` (your wifi interface)
    5. Click `Apply`

**Explanation:**
*   The `/ip address` command sets the IP addresses on router interfaces.
*   `address=...`: Specifies the IP address and subnet mask in CIDR notation.
*   `interface=...`: Specifies the interface to apply the IP address.

**Step 4: Configuring DHCP Server**

*  **CLI:**
    ```mikrotik
    /ip dhcp-server
    add address-pool=lan-pool interface=ether2 name=lan-dhcp
    add address-pool=guest-pool interface=wlan1 name=guest-dhcp
    
    /ip dhcp-server network
    add address=192.168.1.0/24 dns-server=192.168.1.1 gateway=192.168.1.1
    add address=192.168.2.0/24 dns-server=192.168.2.1 gateway=192.168.2.1
    ```
*   **Winbox:**
    1.  Go to `IP` -> `DHCP Server`.
    2.  Click the `+` button to add a new DHCP server.
        *   `Name`: `lan-dhcp`
        *  `Interface`: `ether2`
        *   `Address Pool`: `lan-pool`
    3.  Click `Apply`
     4.  Click the `+` button to add a new DHCP server.
        *   `Name`: `guest-dhcp`
        *  `Interface`: `wlan1`
        *   `Address Pool`: `guest-pool`
    5. Click `Apply`
    6. Go to the `Networks` Tab and click the `+` button to add the lan network
        * `Address`: `192.168.1.0/24`
        * `Gateway`: `192.168.1.1`
        * `DNS Servers`: `192.168.1.1`
    7. Click `Apply`
     8.  Click the `+` button to add a new network for the guest network.
        * `Address`: `192.168.2.0/24`
        * `Gateway`: `192.168.2.1`
        * `DNS Servers`: `192.168.2.1`
   9. Click `Apply`

**Explanation:**

*   The `/ip dhcp-server` command sets up DHCP server instances.
*   `address-pool=...`: Associates a DHCP server with an IP pool.
*   `interface=...`: Specifies the interface the server is active on.
*   The `/ip dhcp-server network` adds network configurations for dhcp clients.

**3. Complete MikroTik CLI Configuration Commands with Relevant Parameters**

Here is a complete CLI configuration for your reference

```mikrotik
# IP Pools
/ip pool
add name=lan-pool ranges=192.168.1.10-192.168.1.254
add name=guest-pool ranges=192.168.2.10-192.168.2.254

# IP Addresses
/ip address
add address=192.168.1.1/24 interface=ether2
add address=192.168.2.1/24 interface=wlan1

# DHCP Server
/ip dhcp-server
add address-pool=lan-pool interface=ether2 name=lan-dhcp
add address-pool=guest-pool interface=wlan1 name=guest-dhcp
/ip dhcp-server network
add address=192.168.1.0/24 dns-server=192.168.1.1 gateway=192.168.1.1
add address=192.168.2.0/24 dns-server=192.168.2.1 gateway=192.168.2.1
```

**Relevant Parameters (Examples):**

| Command          | Parameter     | Description                                                         | Example                               |
|------------------|---------------|---------------------------------------------------------------------|---------------------------------------|
| `/ip pool add`   | `name`        | Unique name for the IP pool.                                        | `name=lan-pool`                       |
|                  | `ranges`      | Range(s) of IP addresses (can have multiple comma-separated ranges). | `ranges=192.168.1.10-192.168.1.254` |
| `/ip address add` | `address`     | IP address and subnet mask.                                         | `address=192.168.1.1/24`              |
|                  | `interface`   | Interface to apply the IP address to.                               | `interface=ether2`                    |
| `/ip dhcp-server add`| `name` | Name of the DHCP Server | `name=lan-dhcp` |
|  | `address-pool` | The IP Pool used by the DHCP server | `address-pool=lan-pool` |
|                  | `interface`   | The interface where DHCP will listen.                                 | `interface=ether2`                    |
| `/ip dhcp-server network add` | `address` | The network range to serve DHCP clients in | `address=192.168.1.0/24`|
|    | `gateway` | The gateway address to hand out to clients | `gateway=192.168.1.1` |
|    | `dns-server` | The dns server to hand out to clients | `dns-server=192.168.1.1` |

**4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics Using Built-in Tools**

**Pitfalls:**

*   **Incorrect IP Ranges:** Ensure pool ranges don’t overlap with router IPs or other existing devices.
*   **Interface Mismatch:** Double-check DHCP server interfaces.
*   **Firewall Issues:** Blocking DHCP packets from guest network (if required) or not allowing the DNS server.
*   **Pool Exhaustion:**  Ensure pools are large enough to support the number of clients, especially for guests.
*   **DHCP Network Configuration:** Forgetting to configure the DHCP networks will result in clients not receiving a valid network configuration.

**Troubleshooting:**

1.  **Check Logs:** Use the `/system logging print` command to inspect system logs for DHCP errors.
2.  **DHCP Leases:** View DHCP leases using `/ip dhcp-server lease print` to confirm clients receive IPs.
3.  **Torch:** Use `/tool torch interface=ether2` or `/tool torch interface=wlan1` to monitor DHCP traffic.
4.  **Ping:** Use `/ping 192.168.1.1` to check reachability.
5.  **Interface Status:** Verify interface is enabled and connected (`/interface print`).
6.  **Packet Sniffer:** Use `/tool sniffer` to capture DHCP packets if all else fails.

**Diagnostics:**

*   **`ping`:** Verify basic connectivity
*   **`traceroute`:** Trace the network path
*   **`torch`:** Real-time packet capture
*   **`packet sniffer`:** Captures packets for detailed analysis
*   **`log print`:** Accesses all logs

**5. Verification and Testing Steps Using MikroTik Tools**

**Verification:**

1.  **Connect Devices:** Connect devices to both the LAN and Guest networks.
2.  **IP Address Check:** Confirm devices received IP addresses from the correct pools. (check the DHCP leases in `/ip dhcp-server lease print`)
3.  **Connectivity Test:** Ping a device on the LAN from the router, and vice-versa, same for the Guest network.
4.  **Internet Access:** Check internet connectivity on both networks.
5.  **Firewall Test:** Ensure devices on the guest network cannot access the LAN network (if firewall isolation rules are in place).

**Testing Tools:**

*   **`/ping <IP_address>`:** Checks IP reachability
*   **`/tool torch interface=<interface>`:** Captures live traffic
*   **`/ip dhcp-server lease print`:** View DHCP lease information.

**6. Related MikroTik-Specific Features, Capabilities, and Limitations**

**Features:**

*   **Multiple IP Pools:** Create pools for various network segments.
*   **Custom DHCP Options:** Configure specific DHCP options (e.g., DNS servers, NTP servers).
*   **Static DHCP Leases:** Assign fixed IP addresses to specific MAC addresses.
*   **DHCP Lease Time:** Control how long DHCP leases remain valid.
*   **DDNS (Dynamic DNS):** Allows the router to update a hostname with its changing IP address.

**Capabilities:**

*   **High Throughput:** MikroTik routers support high DHCP throughput.
*   **Flexible Configuration:** Very configurable to meet various needs.
*   **Advanced QoS:** Prioritize DHCP traffic with QoS.

**Limitations:**

*   **Hardware Dependent:** Maximum DHCP performance is tied to hardware capabilities.
*   **Complex Configuration:** Can be complex if not approached methodically.

**7. MikroTik REST API Examples (if applicable)**

Here are examples of how to manage IP Pools using the MikroTik REST API:

*Note: Ensure your MikroTik has API access enabled by configuring `/ip service api`. If using https, ensure your certificate is trusted.*

**Example 1: Get list of IP Pools (GET)**

*   **API Endpoint:** `/ip/pool`
*   **Request Method:** GET
*   **Expected Response (JSON Example):**
    ```json
    [
      {
        "name": "lan-pool",
        "ranges": "192.168.1.10-192.168.1.254",
        ".id": "*12"
      },
      {
        "name": "guest-pool",
        "ranges": "192.168.2.10-192.168.2.254",
         ".id": "*13"
      }
    ]
    ```

**Example 2: Create a new IP Pool (POST)**

*   **API Endpoint:** `/ip/pool`
*   **Request Method:** POST
*   **Example JSON Payload:**
    ```json
    {
      "name": "test-pool",
      "ranges": "10.0.0.10-10.0.0.200"
    }
    ```
*   **Expected Response (JSON Example):**
    ```json
    {
       "message": "added",
        ".id": "*14"
    }
    ```

**Example 3: Update IP Pool (PUT)**

*   **API Endpoint:** `/ip/pool/*12`  (*12 is the id you will see in the first example*)
*   **Request Method:** PUT
*   **Example JSON Payload:**
    ```json
     {
        "ranges": "192.168.1.50-192.168.1.200"
     }
    ```
*   **Expected Response (JSON Example):**
    ```json
    {
       "message": "changed"
    }
    ```

**Example 4: Delete IP Pool (DELETE)**

*   **API Endpoint:** `/ip/pool/*14`
*   **Request Method:** DELETE
*   **Expected Response (JSON Example):**
    ```json
    {
    	"message": "removed"
    }
    ```

**8. In-depth Explanations of Core Concepts, Focusing on MikroTik's Implementation**

*   **Bridging and Switching:** MikroTik bridges combine multiple network segments into one, while switching forwards traffic based on MAC addresses. We are using layer 3 routing here as the interfaces are not bridged and we have an IP address on each interface.
*   **Routing:** MikroTik's routing engine determines the best path for packets, usually with a primary goal of directing traffic toward the internet. We are using direct routes here based on our local subnets.
*   **Firewall:**  MikroTik's firewall is a powerful stateful firewall used to filter, NAT, and manage traffic. We will implement isolation rules to control traffic between networks.

**9. Security Best Practices Specific to MikroTik Routers**

1.  **Strong Passwords:** Use strong, unique passwords.
2.  **Disable Unnecessary Services:** Turn off unneeded services (e.g., telnet, ftp).
3.  **Firewall Rules:** Use a restrictive firewall, allow only required ports.
4.  **Regular Updates:** Keep RouterOS updated with the latest security patches.
5.  **Secure Remote Access:** Disable or restrict remote API access. Use strong authentication (certificates) for API access if required.
6.  **Access Control:** Restrict access to RouterOS management.
7.  **Limit DHCP Lease Time:** Use shorter DHCP leases to enhance security.
8. **Router API:** Restrict API access to known IPs only. Ensure HTTPS is used for API access

**10. Detailed Explanations and Configuration Examples for the Following MikroTik Topics:**

(Detailed information will be provided in the sections below)

*   **IP Addressing (IPv4 and IPv6)**
    * IPv4 addressing is the use of the common 32 bit addressing that is used by most devices today. We have covered examples in this document above.
    * IPv6 addressing is a 128-bit IP address system that is slowly replacing IPv4.
    ```mikrotik
     /ipv6 address
     add address=2001:db8::1/64 interface=ether2
     ```
     To setup DHCPv6, we need to add an address pool and server configuration as follows:
      ```mikrotik
     /ipv6 pool
     add name=ipv6-pool prefix=2001:db8::/64
     /ipv6 dhcp-server
     add address-pool=ipv6-pool interface=ether2 name=ipv6-dhcp
     /ipv6 dhcp-server network
     add address=2001:db8::/64 dns-server=2001:4860:4860::8888,2001:4860:4860::8844
    ```
*   **IP Pools:** See above comprehensive explanations.
*   **IP Routing:** (Covered above. Static routes and dynamic routes via routing protocols such as OSPF and BGP)
*   **IP Settings:** (Global IP settings: ARP, ICMP settings, etc.)
    ```mikrotik
      /ip settings
      set allow-fast-path=yes
    ```
*   **MAC server:** (Used for MAC telnet/Winbox connections. Not recommended for production.)
   ```mikrotik
   /tool mac-server
   set enabled=yes
   ```
*   **RoMON:** (MikroTik proprietary remote management protocol.)
    ```mikrotik
    /tool romon
    set enabled=yes
    ```
*   **WinBox:** (Graphical management utility for MikroTik RouterOS.)
    * Winbox can be connected via IP address or MAC address. Ensure it is secured via password and potentially by a secure source IP address.

*   **Certificates:** (Used for secure communication over TLS/SSL)
    * Generate a certificate using `/certificate add name=my-certificate common-name=my-router-name`
*   **PPP AAA:** (Authentication, Authorization, and Accounting for PPP)
     * The use of a radius server is highly recommended for PPP users.
     ```mikrotik
     /ppp profile add name=my-ppp-profile use-encryption=yes
     /ppp secret add name=test-user profile=my-ppp-profile password=password service=pppoe
     /interface ppp-server server set enabled=yes
     ```
*   **RADIUS:** (Centralized authentication and authorization server.)
    ```mikrotik
      /radius add address=192.168.1.100 secret=secret service=ppp timeout=30
    ```
*   **User / User groups:** (Manage RouterOS users and permissions)
    ```mikrotik
    /user add name=test-user password=password group=full
    ```
*   **Bridging and Switching:** (Explained above. Combine multiple interfaces and bridge traffic.)
    ```mikrotik
       /interface bridge add name=lan-bridge
       /interface bridge port add bridge=lan-bridge interface=ether2
       /interface bridge port add bridge=lan-bridge interface=ether3
       /ip address add address=192.168.1.1/24 interface=lan-bridge
    ```
*   **MACVLAN:** (Virtual interfaces based on a single physical interface.)
  ```mikrotik
    /interface macvlan add interface=ether2 mac-address=02:02:03:04:05:06 name=macvlan1
    /ip address add address=192.168.2.1/24 interface=macvlan1
  ```
*   **L3 Hardware Offloading:** (Hardware acceleration for routing.)
     * Enabled by default on many routers, ensure the `allow-fast-path` is set to yes
*   **MACsec:** (IEEE standard for link-layer security.)
    ```mikrotik
    /interface macsec add name=macsec1 interface=ether2 cipher-suite=GCM-AES-256-128 primary-key=secret-key-hex
    ```
*   **Quality of Service:** (Prioritize specific traffic types.)
    ```mikrotik
    /queue simple add max-limit=10M/10M name=queue1 target=192.168.1.0/24
    ```
*   **Switch Chip Features:** (Hardware capabilities of the router's switch chip.)
    * Specific to the router model, typically exposed as switch settings.
*   **VLAN:** (Virtual LANs for segmenting the network.)
    ```mikrotik
       /interface vlan add interface=ether2 name=vlan10 vlan-id=10
       /ip address add address=192.168.3.1/24 interface=vlan10
    ```
*   **VXLAN:** (Layer 2 overlay network tunneling protocol.)
    ```mikrotik
       /interface vxlan add name=vxlan1 vni=100 remote-address=192.168.10.1 interface=ether2
    ```
*   **Firewall and Quality of Service:** (Detailed explanation provided above)
    *   **Connection tracking:** Keeps a record of each connection that passes through the router.
    *   **Firewall:** Filters and manages network traffic.
    *   **Packet Flow:** Order in which packets pass through the system.
    *   **Queues:** Controls bandwidth usage
    *  **Kid Control:** Can be configured through user groups and simple queues
    * **UPnP:** Used for port forwarding, can be a security risk.
    * **NAT-PMP:** (Another form of port forwarding)
*   **IP Services (DHCP, DNS, SOCKS, Proxy):**
    *   **DHCP:** (Dynamic IP address assignment, covered above)
    *   **DNS:** (Domain Name System resolver)
    ```mikrotik
    /ip dns set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8
    ```
    *   **SOCKS:** (Proxy service)
    ```mikrotik
    /ip socks set enabled=yes
    ```
    *   **Proxy:** (HTTP/HTTPS proxy)
    ```mikrotik
    /ip proxy set enabled=yes
    ```
*   **High Availability Solutions:**
    *   **Load Balancing:** Distribute network traffic across multiple links/devices.
    *   **Bonding:** Combines multiple physical interfaces into a single logical link.
    ```mikrotik
      /interface bonding add mode=802.3ad name=bond1 slaves=ether2,ether3
      /ip address add address=192.168.1.1/24 interface=bond1
    ```
    *   **Bonding Examples:** (Covered above)
    *   **HA Case Studies:** (Redundancy and failover designs)
    *   **Multi-chassis Link Aggregation Group:** (LAG spanning multiple devices)
    *   **VRRP:** (Virtual Router Redundancy Protocol for router failover.)
    ```mikrotik
      /interface vrrp add interface=ether2 priority=100 vrid=1 v3-protocol=yes
      /ip address add address=192.168.1.1/24 interface=vrrp1
      /interface vrrp add interface=ether2 priority=90 vrid=1 v3-protocol=yes
      /ip address add address=192.168.1.1/24 interface=vrrp2
    ```
    *   **VRRP Configuration Examples:** (Covered above)
*  **Mobile Networking:**
    * **GPS:** (Can obtain geographic coordinates)
    * **LTE:** (For cellular connectivity, requires an LTE modem or device)
    *   **PPP:** (Point-to-Point protocol for cellular connections)
    * **SMS:** (To send and receive SMS messages)
    * **Dual SIM:** (For cellular connection redundancy)
*   **Multi Protocol Label Switching - MPLS:**
    *   **MPLS Overview:** (A tunneling protocol for improving performance in networks).
    *   **MPLS MTU:** (Maximum Transmittable Unit).
    *   **Forwarding and Label Bindings:** (How packets are forwarded).
    *   **EXP bit and MPLS Queuing:** (How QoS is applied)
    *   **LDP:** (Label Distribution Protocol for label exchange).
    *   **VPLS:** (Virtual Private LAN Service)
    *   **Traffic Eng:** (Traffic optimization).
    *   **MPLS Reference:** (Mikrotik documentation)
*   **Network Management:**
    *   **ARP:** (Address Resolution Protocol)
    ```mikrotik
       /ip arp print
    ```
    *   **Cloud:** (Dynamic DNS and management service)
    *   **DHCP:** (Dynamic Host Configuration Protocol)
    *  **DNS:** (Domain Name System)
    *  **SOCKS:** (Proxy service)
    *  **Proxy:** (HTTP/HTTPS proxy)
    * **Openflow:** (Network protocol to control network devices).
*   **Routing:**
    *   **Routing Protocol Overview:** (Static and dynamic routing protocols)
    *   **Moving from ROSv6 to v7 with examples:** (Routing changes from ROSv6 to ROSv7)
    *   **Routing Protocol Multi-core Support:** (How routes scale)
    *  **Policy Routing:** (Route traffic using complex policies)
    *   **Virtual Routing and Forwarding - VRF:** (Allows multiple routing instances)
    ```mikrotik
      /routing vrf add name=vpn-vrf
      /ip address add address=192.168.10.1/24 interface=ether2 vrf=vpn-vrf
    ```
    *   **OSPF:** (Open Shortest Path First, Interior Gateway Protocol)
    ```mikrotik
     /routing ospf instance add name=ospf1 router-id=1.1.1.1
     /routing ospf area add instance=ospf1 area-id=0.0.0.0
     /routing ospf network add area=0.0.0.0 network=192.168.1.0/24
    ```
    *   **RIP:** (Routing Information Protocol, distance-vector)
     ```mikrotik
      /routing rip instance add name=rip1
      /routing rip interface add interface=ether2 rip-in=yes rip-out=yes
    ```
    *   **BGP:** (Border Gateway Protocol, Exterior Gateway Protocol)
    ```mikrotik
    /routing bgp instance add as=65001 name=bgp1 router-id=1.1.1.1
    /routing bgp peer add instance=bgp1 remote-address=192.168.1.100 remote-as=65002
    ```
    *   **RPKI:** (Resource Public Key Infrastructure, for BGP)
    *   **Route Selection and Filters:** (How routes are chosen and filtered).
    *   **Multicast:** (Sending data to multiple recipients)
    *   **Routing Debugging Tools:** (Troubleshooting commands for routing)
    *   **Routing Reference:** (Official MikroTik documentation)
    *   **BFD:** (Bidirectional Forwarding Detection, failure detection)
     ```mikrotik
      /routing bfd add remote-address=192.168.1.100 interface=ether2
    ```
    *   **IS-IS:** (Intermediate System to Intermediate System, link-state protocol)
*   **System Information and Utilities:**
    *   **Clock:** (Time and date settings)
     ```mikrotik
      /system clock set time=10:00:00 date=jan/01/2024
    ```
    *   **Device-mode:** (Mode of operation of the router)
    *   **E-mail:** (Notification service)
     ```mikrotik
      /system e-mail set address=smtp.gmail.com from="your-email@gmail.com" password="app-password" port=587 start-tls=yes user="your-email@gmail.com"
     ```
    *   **Fetch:** (Downloads files over HTTP, HTTPS or FTP)
    ```mikrotik
    /tool fetch url=https://www.google.com/ output-file=google.html
    ```
    *   **Files:** (File system management)
    *   **Identity:** (Set hostname)
     ```mikrotik
      /system identity set name=my-router
    ```
    *   **Interface Lists:** (Group interfaces for easy filtering)
      ```mikrotik
       /interface list add name=lan
       /interface list member add interface=ether2 list=lan
      ```
    *   **Neighbor discovery:** (Discovers other MikroTik devices on the network)
    *   **Note:** (Add notes for documentation)
    *   **NTP:** (Network Time Protocol client)
     ```mikrotik
      /system ntp client set enabled=yes server-primary=time.google.com server-secondary=pool.ntp.org
    ```
    *   **Partitions:** (Disk partition management)
    *   **Precision Time Protocol:** (More accurate time synchronization protocol)
    *   **Scheduler:** (Execute commands at scheduled times)
    ```mikrotik
     /system scheduler add name=reboot on-event="/system reboot" start-time=00:00:00 interval=1d
    ```
    *   **Services:** (Enable/Disable services)
    *   **TFTP:** (Trivial File Transfer Protocol)
*   **Virtual Private Networks:**
    *   **6to4:** (Transition technology for IPv6)
    *   **EoIP:** (Ethernet over IP tunneling)
    ```mikrotik
    /interface eoip add local-address=192.168.1.1 remote-address=192.168.1.100 tunnel-id=10
    ```
    *   **GRE:** (Generic Routing Encapsulation tunneling)
     ```mikrotik
    /interface gre add local-address=192.168.1.1 remote-address=192.168.1.100
    ```
    *   **IPIP:** (IP in IP tunneling)
     ```mikrotik
      /interface ipip add local-address=192.168.1.1 remote-address=192.168.1.100
    ```
    *   **IPsec:** (Security protocol suite for VPNs)
    ```mikrotik
      /ip ipsec proposal add auth-algorithms=sha256 enc-algorithms=aes-256-cbc name=my-proposal
      /ip ipsec peer add address=192.168.1.100/32 exchange-mode=main my-id=address profile=default
      /ip ipsec identity add peer=192.168.1.100 secret="secret"
      /ip ipsec policy add peer=192.168.1.100 proposal=my-proposal sa-src-address=192.168.1.1 sa-dst-address=192.168.1.100
    ```
    *   **L2TP:** (Layer 2 Tunneling Protocol for VPNs)
     ```mikrotik
       /interface l2tp-server server set enabled=yes
    ```
    *   **OpenVPN:** (Open-source VPN protocol)
    *   **PPPoE:** (Point-to-Point Protocol over Ethernet for dial-up connections)
    ```mikrotik
       /interface pppoe-client add interface=ether1 user=username password=password
    ```
    *   **PPTP:** (Point-to-Point Tunneling Protocol for VPNs)
    *   **SSTP:** (Secure Socket Tunneling Protocol for VPNs)
    *   **WireGuard:** (Modern VPN protocol)
     ```mikrotik
      /interface wireguard add listen-port=13231 name=wg1 private-key="your-key"
      /interface wireguard peers add allowed-address=192.168.1.100/32 endpoint=192.168.1.100:13231 interface=wg1 persistent-keepalive=20 public-key="other-key"
    ```
    *  **ZeroTier:** (Hybrid cloud/on-premise network solution).
*   **Wired Connections:**
    *   **Ethernet:** (Standard wired network connection)
    *  **MikroTik wired interface compatibility:** (Compatibility of different interfaces).
    *  **PWR Line:** (Power-line networking)
*   **Wireless:**
    *   **WiFi:** (Wireless connectivity)
    *  **Wireless Interface:** (Configuration of wireless interfaces).
    *  **W60G:** (60GHz Wireless)
    *   **CAPsMAN:** (Centralized AP management).
    *   **HWMPplus mesh:** (MikroTik's proprietary mesh routing protocol)
    *   **Nv2:** (MikroTik's proprietary wireless protocol)
    *   **Interworking Profiles:** (Roaming configuration).
    *   **Wireless Case Studies:** (Example configurations).
*   **Internet of Things:**
    *   **Bluetooth:** (Short range wireless communication protocol).
    *   **GPIO:** (General Purpose Input Output, custom hardware usage)
    *   **Lora:** (Long Range Wide Area Network communication protocol