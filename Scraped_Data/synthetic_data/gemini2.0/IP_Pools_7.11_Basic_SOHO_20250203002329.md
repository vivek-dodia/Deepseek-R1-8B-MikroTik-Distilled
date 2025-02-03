Okay, let's dive deep into IP Pools on MikroTik RouterOS, covering a wide range of related features, best practices, and detailed examples. This is going to be a comprehensive document, aiming to be suitable for a seasoned MikroTik professional.

## MikroTik RouterOS IP Pools: Detailed Technical Documentation (SOHO Scenario)

This document provides an in-depth exploration of IP Pools within MikroTik RouterOS 7.11 (or 6.x/7.x compatible), suitable for a Basic configuration level in a SOHO (Small Office/Home Office) environment. We will cover the technicalities, practical implementations, and advanced concepts related to IP Pools and many related RouterOS features.

### 1. Comprehensive Configuration Scenario and Specific MikroTik Requirements

**Scenario:** We're setting up a home network with a MikroTik router. We'll allocate a dynamic IP pool for devices connected via a DHCP server on our LAN and set up a separate IP pool for a VPN server, providing a fixed IP range for VPN clients. Additionally, we will look into IPv6 allocation.

**MikroTik Requirements:**

*   RouterOS version 7.11 (or 6.x/7.x compatibility)
*   Basic understanding of networking concepts (IP addressing, subnetting).
*   Access to the MikroTik router via CLI (SSH or Terminal) or Winbox.
*   A basic wired LAN setup.
*   A configured WAN interface.

### 2. Step-by-Step MikroTik Implementation

Let's break this down into detailed steps, covering both CLI and Winbox methodologies.

#### 2.1. Creating IP Pools Using CLI

**Step 1: Define the DHCP Pool (LAN)**

*   We will assign the range `192.168.88.100` to `192.168.88.250`.
*   This pool will be named "dhcp_pool."

```mikrotik
/ip pool
add name=dhcp_pool ranges=192.168.88.100-192.168.88.250
```
**Step 2: Define the VPN Pool**
* We will assign the range `192.168.90.2` to `192.168.90.100`
* This pool will be named "vpn_pool"
```mikrotik
/ip pool
add name=vpn_pool ranges=192.168.90.2-192.168.90.100
```

**Step 3: Define the IPv6 Pool (LAN)**

* We will assign a /64 range.
* This pool will be named "ipv6_pool".
* Assuming our Router has a delegated Prefix, we will use it to construct the pool.

```mikrotik
/ipv6 pool
add name=ipv6_pool prefix=2001:db8:1::/64
```

#### 2.2. Creating IP Pools Using Winbox

1.  Open Winbox and connect to your MikroTik router.
2.  Navigate to *IP* > *Pool*.
3.  Click the "+" button to add a new pool.
4.  Enter the name ("dhcp_pool" for LAN)
5.  In the *Ranges* field, type `192.168.88.100-192.168.88.250`.
6.  Click *Apply*, and then *OK*.
7.  Repeat steps 3-6 for the *vpn_pool* using range  `192.168.90.2-192.168.90.100`.
8.  Repeat steps 3-6 for the *ipv6_pool*, navigating to *IPv6* > *Pool*, and setting the *Prefix* to `2001:db8:1::/64`.

### 3. Complete MikroTik CLI Configuration Commands

Here is a consolidated version of our CLI commands, with explanations:

```mikrotik
# Define DHCP IP Pool
/ip pool
add name=dhcp_pool ranges=192.168.88.100-192.168.88.250 comment="Pool for LAN clients"

# Define VPN IP Pool
/ip pool
add name=vpn_pool ranges=192.168.90.2-192.168.90.100 comment="Pool for VPN clients"

# Define IPv6 Pool
/ipv6 pool
add name=ipv6_pool prefix=2001:db8:1::/64 comment="Pool for IPv6 clients"
```
#### IP Pool Parameters

| Parameter     | Description                                                                                    | Example                   |
|---------------|------------------------------------------------------------------------------------------------|---------------------------|
| `name`        | The name of the IP pool.                                                                       | `dhcp_pool`, `vpn_pool`    |
| `ranges`      | The IP address range(s) for the pool (comma-separated for multiple ranges).                     | `192.168.88.100-192.168.88.250` |
| `prefix`   | The IPV6 prefix for the pool                                                                                    | `2001:db8:1::/64` |
| `comment`    | An optional comment for the pool.                                                                | `Pool for LAN clients`   |

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Overlapping IP Ranges:** Avoid using IP ranges that overlap with existing network addresses.
*   **Pool Exhaustion:** Monitor pool utilization, especially in large networks. A lack of available IPs in the pool will lead to clients being unable to obtain an IP.
*   **Incorrect Subnetting:** Ensure the subnet mask is correct for the configured IP ranges.

**Troubleshooting:**

*   **Check Pool Size:** In Winbox or CLI: `/ip pool print`. Verify the range defined is correct.
*   **DHCP Server Errors:** Check DHCP server logs: `/system logging print topics=dhcp,critical`.
*   **Use Torch:** Run `/tool torch interface=ether2` (adjust your interface) to observe DHCP traffic.
*   **IP Address Conflicts:** Identify if there are other devices that may be using an address already given to a DHCP client.
*  **Verify Prefix Delegation:** If no IPV6 addresses are being assigned, ensure your router is getting a delegated prefix from your ISP.

**Diagnostics Tools:**

*   `/tool ping`: Test reachability of IPs.
*   `/tool traceroute`: Track the path to a destination.
*   `/tool torch`: Inspect network traffic.
*   `/log print`: Check system logs for errors.
* `/interface print`: Verify interface status
*  `/ipv6 nd print`: Verify ND status and neighbors
* `/ipv6 address print`: Verify IPv6 addresses are configured

### 5. Verification and Testing Steps

**Step 1: Verify IP Pool Configuration**

*   **CLI:** `/ip pool print` and `/ipv6 pool print`
*   **Winbox:** *IP* > *Pool*, and *IPv6* > *Pool*
*   Verify the pool *names*, *ranges*, and *prefixes* match the intended configuration.

**Step 2: Test DHCP Client IP Assignment (IPv4)**

1.  Connect a client device (e.g., a laptop) to your LAN.
2.  Ensure the device is configured to obtain an IP address automatically via DHCP.
3.  Verify the client obtains an IP address within the range of the `dhcp_pool` (e.g., `192.168.88.100` - `192.168.88.250`).
4. Verify on the MikroTik: `/ip dhcp-server lease print`

**Step 3: Test DHCPv6 Client IP Assignment (IPv6)**

1. Connect a client device to your LAN.
2. Ensure the device is configured to obtain an IP address automatically via DHCPv6.
3. Verify the device obtains an IP address within the range of the `ipv6_pool` (e.g. `2001:db8:1::xxx`).
4. Verify on the MikroTik: `/ipv6 dhcp-server lease print`

**Step 4: Test VPN Connection**
1. Connect a VPN Client to your Router.
2. Verify the VPN client obtains an IP address within the range of the `vpn_pool` (e.g. `192.168.90.2` - `192.168.90.100`).
3. Verify on the MikroTik: `/ip pool print`, and see used addresses in the specified range

**Tools:**

*   `ping`: Ping devices within and outside the LAN.
*   `traceroute`: Check network paths.
*   `torch`: Monitor DHCP and other relevant traffic.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **DHCP Server Integration:** IP Pools are directly used by DHCP servers to dynamically assign IP addresses.
*   **Static DHCP Leases:** You can assign static IPs from the pool to specific MAC addresses.
*   **Pool Limits:** Each pool has limitations (which depends on the hardware) on size and IP address management efficiency.
*   **Pool Utilization:** RouterOS tracks IP addresses assigned from a pool.
*  **IPv6 Pool Usage:** IPV6 Pools are assigned to DHCPv6 servers and other IPV6 capable functions.
*  **Multiple pools:** MikroTik allows multiple pools to be defined and used within the same device.

### 7. MikroTik REST API Examples

Here are some examples of how to interact with IP Pools via the MikroTik REST API. *Note: This assumes you have the API service enabled and configured on your RouterOS device.*

**API Endpoint**: `/ip/pool`

**Example 1: Get IP Pool List (GET)**

*   **Endpoint:** `/ip/pool`
*   **Method:** GET
*   **Request Payload:** None
*   **Example Response:**

```json
[
  {
    "name": "dhcp_pool",
    "ranges": "192.168.88.100-192.168.88.250",
    "comment": "Pool for LAN clients",
    ".id": "*1"
  },
  {
    "name": "vpn_pool",
    "ranges": "192.168.90.2-192.168.90.100",
     "comment": "Pool for VPN clients",
    ".id": "*2"
  }
]
```

**Example 2: Create IP Pool (POST)**

*   **Endpoint:** `/ip/pool`
*   **Method:** POST
*   **Request Payload (JSON):**

```json
{
  "name": "test_pool",
  "ranges": "10.0.0.10-10.0.0.20",
  "comment": "Created via API"
}
```

*   **Expected Response:** (200 OK) with the new pool object.

```json
{
    "name": "test_pool",
    "ranges": "10.0.0.10-10.0.0.20",
    "comment": "Created via API",
    ".id": "*3"
}
```

**Example 3: Update IP Pool (PUT)**

*   **Endpoint:** `/ip/pool/*1` (replace `*1` with the ID of the pool to update)
*   **Method:** PUT
*   **Request Payload (JSON):**

```json
{
    "comment": "Updated comment through API",
     "ranges": "192.168.88.100-192.168.88.254"
}
```
*   **Expected Response:** (200 OK) with the updated pool object.

```json
{
  "name": "dhcp_pool",
    "ranges": "192.168.88.100-192.168.88.254",
    "comment": "Updated comment through API",
    ".id": "*1"
  }
```

**Example 4: Delete IP Pool (DELETE)**

*   **Endpoint:** `/ip/pool/*3` (replace `*3` with the ID of the pool to delete)
*   **Method:** DELETE
*   **Request Payload:** None
*   **Expected Response:** (200 OK)

**API Endpoint**: `/ipv6/pool`

**Example 5: Get IPv6 Pool List (GET)**

*   **Endpoint:** `/ipv6/pool`
*   **Method:** GET
*   **Request Payload:** None
*   **Example Response:**
```json
[
    {
        "name": "ipv6_pool",
        "prefix": "2001:db8:1::/64",
        "comment": "Pool for IPv6 clients",
        ".id": "*1"
    }
]
```

**Example 6: Create IPv6 Pool (POST)**
*   **Endpoint:** `/ipv6/pool`
*   **Method:** POST
*   **Request Payload (JSON):**

```json
{
  "name": "test_ipv6_pool",
  "prefix": "2001:db8:2::/64",
  "comment": "Created via API"
}
```

*   **Expected Response:** (200 OK) with the new pool object.
```json
{
    "name": "test_ipv6_pool",
        "prefix": "2001:db8:2::/64",
        "comment": "Created via API",
         ".id": "*2"
    }
```

### 8. In-Depth Explanations of Core Concepts (MikroTik Specific)

**Bridging and Switching:**

*   **Bridging:** In MikroTik, a bridge combines multiple interfaces into a single broadcast domain. It's often used to allow devices connected to different physical ports or interfaces to communicate as if they are on the same network.
*   **Switching:** MikroTik routers with switch chips handle switching operations in hardware for increased performance.  VLANs can be used within a bridge.

**Routing:**

*   **IP Routing Table:** The MikroTik router uses a routing table to make decisions on how to send IP packets to different destinations. This table is updated by static routes, dynamically from routing protocols, and through direct interface connection information.
*   **Policy Routing:**  RouterOS allows policy-based routing, which enables you to route traffic based on criteria other than the destination IP address, like source IP, ports, and protocols. This provides fine-grained control over traffic flow.
*   **Virtual Routing and Forwarding - VRF:** VRFs allow for multiple independent routing tables within a router, enabling separation of routing domains. Useful for isolating customer networks or providing different levels of access to different resources.

**Firewall:**

*   **Connection Tracking:** The MikroTik firewall tracks network connections and allows rules to apply based on connection state.
*   **Packet Flow:** Incoming packets on a MikroTik first pass the input chain, then forward chain for routed traffic, and output for traffic from the router itself.
*   **NAT:** Network Address Translation is often used to translate a private LAN IP to a public IP.
*   **Queues:** Quality of Service on a MikroTik is primarily managed through queues.  This allows you to control the amount of bandwidth specific traffic flows may consume.

### 9. Security Best Practices (MikroTik Specific)

*   **Strong Passwords:** Ensure a strong admin password is set.
*   **Disable Unnecessary Services:** Disable services like telnet, www, and API if not required.
*   **Restrict Winbox/SSH Access:**  Only allow connections to Winbox and SSH from trusted IP addresses.
*   **Firewall Rules:** Set up proper firewall rules to block incoming and outgoing traffic that you do not want.
*   **Regular Updates:** Update your RouterOS firmware and RouterBoard firmware frequently.
*  **Use of certificates:** Ensure that services like Winbox and API only allow secure connections.
*   **Avoid Default Usernames and Passwords:** Do not use default user names like "admin"

### 10. Detailed Explanations and Configuration Examples

#### IP Addressing (IPv4 and IPv6)

*   **IPv4:** Uses 32-bit addresses, typically represented in dotted decimal notation (e.g., 192.168.88.1).
    ```mikrotik
    /ip address
    add address=192.168.88.1/24 interface=ether2
    ```
*   **IPv6:** Uses 128-bit addresses, represented in hexadecimal notation (e.g., 2001:db8::1).
    ```mikrotik
    /ipv6 address
    add address=2001:db8::1/64 interface=ether2
    ```

#### IP Routing
*   **Static Route:** Manual entry of how to reach a certain network.
    ```mikrotik
     /ip route
     add dst-address=10.10.10.0/24 gateway=192.168.88.2
    ```
* **OSPF Routing:** Dynamic routing protcol that can learn and share routes among routers.
    ```mikrotik
    /routing ospf instance
    add name=ospf1 router-id=192.168.88.1
    /routing ospf area
    add instance=ospf1 name=backbone area-id=0.0.0.0
    /routing ospf interface
    add interface=ether2 network-type=point-to-point cost=1 instance=ospf1 area=backbone
    ```

#### IP Settings

*   **Disabled:**  Will not respond to ARP or IP traffic.
* **ARP:** How to resolve IP Addresses to MAC addresses
    ```mikrotik
    /ip settings
    set arp-timeout=15s
    ```
#### MAC server

*  **MAC Server:** Used to access the MikroTik without IP address if it is on the same layer 2 network.
  ```mikrotik
  /tool mac-server
    set enabled=yes allowed-interface-list=lan
  ```
#### RoMON

* **RoMON:** Remote Monitoring allows for accessing the router via a layer 2 address, great for out of band management.
    ```mikrotik
    /tool romon
      set enabled=yes secret="password"
    /tool romon port
      add interface=ether2
    ```

#### WinBox

*  **WinBox:** The GUI to manage the Router, allows for secure access to the device.
    ```mikrotik
    /tool user
    add name=admin password=StrongPassword group=full
    /ip service
      set winbox address=192.168.88.0/24
    ```

#### Certificates

*   **Certificates:** Used to encrypt network services such as Winbox or the API
    ```mikrotik
   /certificate
    add name="my-cert" common-name=MyRouter.com subject-alt-name="DNS:MyRouter.com,IP:192.168.88.1"
    sign my-cert ca=no
    /ip service
      set api certificate=my-cert
    ```

#### PPP AAA

*   **PPP AAA:** PPP Authentication, Authorization, and Accounting
    ```mikrotik
    /ppp profile
        add name="my-profile" local-address=192.168.88.1 remote-address=vpn_pool use-encryption=yes dns-server=8.8.8.8
    /interface l2tp-server
        add user=user password=password profile=my-profile
    ```

#### RADIUS

*   **RADIUS:** Remote Authentication Dial-In User Service, used for centralized authentication.
    ```mikrotik
    /radius
      add address=192.168.88.2 secret=secret timeout=30s authentication=yes accounting=yes
    /ppp profile
        set my-profile use-radius=yes
    ```

#### User / User groups

*   **User:** Users on the Router for different access purposes.
    ```mikrotik
    /user
        add name=readonly group=read password=password
    ```
*   **User Groups:** Defines the access rights given to a user.
    ```mikrotik
    /user group
        add name=readonly policy=readonly
    ```

#### Bridging and Switching

*   **Bridge:** Combines multiple interfaces into a single Layer 2 broadcast domain.
     ```mikrotik
     /interface bridge
       add name=bridge1 protocol-mode=rstp
     /interface bridge port
       add bridge=bridge1 interface=ether2
       add bridge=bridge1 interface=ether3
     /ip address
      add interface=bridge1 address=192.168.88.1/24
      ```
* **Switching:** Hardware level switching of ports on the Router.
    ```mikrotik
    /interface ethernet switch vlan
      add vlan-id=10 ports=ether2-master,ether3,ether4,ether5
      add vlan-id=20 ports=ether2-master,ether6,ether7
    /interface ethernet switch port
      set ether2-master vlan-mode=secure vlan-header=add-if-missing
      set ether3 vlan-mode=secure vlan-header=add-if-missing
      set ether4 vlan-mode=secure vlan-header=add-if-missing
      set ether5 vlan-mode=secure vlan-header=add-if-missing
      set ether6 vlan-mode=secure vlan-header=add-if-missing
      set ether7 vlan-mode=secure vlan-header=add-if-missing
    /ip address
      add address=192.168.88.1/24 interface=ether2-master
    /interface vlan
      add vlan-id=10 interface=ether2-master name=vlan10
      add vlan-id=20 interface=ether2-master name=vlan20
    /ip address
      add address=192.168.89.1/24 interface=vlan10
      add address=192.168.90.1/24 interface=vlan20
    ```

#### MACVLAN

*   **MACVLAN:** Virtual interfaces on top of the existing physical interface, allows you to assign multiple MAC and IP addresses to a single physical interface
     ```mikrotik
      /interface macvlan
        add interface=ether2 mode=vepa mac-address=00:00:00:00:00:01 name=macvlan1
        add interface=ether2 mode=vepa mac-address=00:00:00:00:00:02 name=macvlan2
    /ip address
      add address=192.168.88.2/24 interface=macvlan1
      add address=192.168.88.3/24 interface=macvlan2
    ```

#### L3 Hardware Offloading

*  **L3 Hardware Offloading:** Allows hardware to perform routing tasks on the device. This allows for faster performance.
    ```mikrotik
    /interface ethernet
        set ether2 l3-hw-offloading=yes
    ```

#### MACsec
*  **MACsec:** MAC layer security for encrypting traffic on a wire
    ```mikrotik
    /interface ethernet macsec
        add interface=ether2 key=key_value name=macsec1
    ```

#### Quality of Service

*   **Queues:** RouterOS uses queues to define the speed or throughput of traffic.
    ```mikrotik
    /queue simple
      add name=download-limit target=ether2 max-limit=10M/10M
    ```

#### Switch Chip Features

*   **Switch Chip Features:** These are advanced options for managing the router's built in switch chip.
    ```mikrotik
    /interface ethernet switch port
      set ether2-master vlan-mode=secure vlan-header=add-if-missing
    ```

#### VLAN

*   **VLAN:** Virtual LAN allows for traffic segmentation within a switch.
    ```mikrotik
    /interface vlan
        add name=vlan10 interface=ether2 vlan-id=10
    ```

#### VXLAN

*   **VXLAN:** Virtual eXtensible LAN for tunneling traffic across a network.
    ```mikrotik
    /interface vxlan
       add name=vxlan1 interface=ether2 vni=1000 remote-address=10.10.10.20
    ```

#### Firewall and Quality of Service

*   **Connection Tracking:** Allows for stateful firewall policies.
*   **Firewall Rules:** Rules to filter and manipulate traffic.
    ```mikrotik
    /ip firewall filter
       add chain=forward action=drop in-interface=ether2
    ```
*   **Packet Flow in RouterOS:** Defines the order of operation on the RouterOS
*  **Queues:** RouterOS defines queues for managing Quality of Service.
    ```mikrotik
      /queue simple
        add name=download-limit target=ether2 max-limit=10M/10M
    ```
*   **Firewall and QoS Case Studies:** Allows for different real world implementations of Firewall and QoS
*  **Kid Control:** Rules to limit a child's access to the network.
*   **UPnP:** Allows applications to auto create firewall rules.
   ```mikrotik
     /ip upnp set enabled=yes
    ```
*  **NAT-PMP:** Similar to UPnP but utilizes a different protocol.

#### IP Services

*   **DHCP:** Allows for automatic IP configuration of hosts.
    ```mikrotik
    /ip dhcp-server
      add name=dhcp1 address-pool=dhcp_pool interface=ether2
    /ip dhcp-server network
      add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=8.8.8.8
    ```
*   **DNS:** Allows for name resolution.
    ```mikrotik
    /ip dns
        set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
    ```
*   **SOCKS:** Allows for a SOCKS proxy.
    ```mikrotik
     /ip socks set enabled=yes
    ```
*   **Proxy:** Allows for a web proxy service
    ```mikrotik
    /ip proxy set enabled=yes
    ```

#### High Availability Solutions

*  **Load Balancing:** Distributing traffic among multiple links
    ```mikrotik
      /ip route
        add dst-address=0.0.0.0/0 gateway=192.168.88.2 check-gateway=ping distance=1
        add dst-address=0.0.0.0/0 gateway=192.168.88.3 check-gateway=ping distance=2
    ```
*   **Bonding:** Combines multiple Ethernet ports into a single link.
    ```mikrotik
      /interface bonding
        add name=bond1 mode=802.3ad slaves=ether2,ether3
    ```
*   **Bonding Examples:** Using different bonding modes.
*   **HA Case Studies:** Examples on how to configure HA solutions.
*   **Multi-chassis Link Aggregation Group:**  Similar to bonding but can be spread among multiple physical devices.
*   **VRRP:** Virtual Router Redundancy Protocol, allows for multiple routers to appear as one.
    ```mikrotik
      /interface vrrp
        add interface=ether2 name=vrrp1 vrid=1 priority=100 virtual-address=192.168.88.254
      /interface vrrp
        add interface=ether2 name=vrrp2 vrid=1 priority=90 virtual-address=192.168.88.254
    ```
*   **VRRP Configuration Examples:** Examples on how to configure VRRP

#### Mobile Networking

*   **GPS:** Global Positioning System.
*   **LTE:** Long Term Evolution mobile network connectivity
    ```mikrotik
    /interface lte
      set apn=internet
      set interface=lte1
    /ip route
      add dst-address=0.0.0.0/0 gateway=lte1
    ```
*   **PPP:** Point to Point Protocol
*   **SMS:** Short Message Service
*   **Dual SIM Application:** Using a router that has two SIM slots.

#### Multi Protocol Label Switching - MPLS

*   **MPLS Overview:** Allows for creating labels and forwarding on Layer 2.5.
*   **MPLS MTU:** The Maximum Transfer Unit of an MPLS network
*   **Forwarding and Label Bindings:** How labels are associated with routes.
*   **EXP bit and MPLS Queuing:** Using the EXP bit for Quality of Service on an MPLS Network.
*   **LDP:** Label Distribution Protocol, how to distribute labels between MPLS routers.
*   **VPLS:** Virtual Private LAN Service using MPLS.
*  **Traffic Eng:** Traffic Engineering on an MPLS Network.
*   **MPLS Reference:** Further reading about MPLS on MikroTik.

#### Network Management

*   **ARP:** Address Resolution Protocol.
*   **Cloud:** Allows for remote management via the MikroTik Cloud.
    ```mikrotik
    /system cloud
        set enabled=yes
    ```
*  **DHCP:** See DHCP setup above
*   **DNS:** See DNS setup above
*  **SOCKS:** See SOCKS setup above
*   **Proxy:** See Proxy setup above
* **Openflow:** Allows for using the router as an openflow switch.
    ```mikrotik
    /interface openflow
       add controller-address=192.168.88.2 controller-port=6653 name=openflow1
    ```

#### Routing
*   **Routing Protocol Overview:** Introduces dynamic routing protocols.
*   **Moving from ROSv6 to v7 with examples:** Moving the configurations from the older RouterOS to the new RouterOS.
*   **Routing Protocol Multi-core Support:** Support for multiple cores to perform routing.
*   **Policy Routing:**  See Policy Routing Setup above.
*   **Virtual Routing and Forwarding - VRF:** See VRF setup above.
*   **OSPF:** See OSPF setup above.
*   **RIP:** Routing Information Protocol, older routing protocol.
*   **BGP:** Border Gateway Protocol, used in ISP environments to advertise routes across different domains.
* **RPKI:** Resource Public Key Infrastructure.
*   **Route Selection and Filters:** How routes are chosen and how they are filtered
*   **Multicast:** Sending the same traffic to multiple locations at the same time.
*   **Routing Debugging Tools:** Debugging tools for route troubleshooting.
*   **Routing Reference:** Further reading for routing on MikroTik.
*   **BFD:** Bidirectional Forwarding Detection, for faster link failure detection.
    ```mikrotik
    /routing bfd
      add name=bfd1 local-address=192.168.88.1 remote-address=192.168.88.2
    ```
*   **IS-IS:** Intermediate System to Intermediate System, a link state routing protocol used in enterprise and ISP environments.

#### System Information and Utilities

*   **Clock:**  Set the time and date.
    ```mikrotik
    /system clock
        set time=12:00:00 date=dec/25/2023
    ```
*  **Device-mode:** Option to put the device into read-only mode or change the type of device it reports as
*   **E-mail:** Configure sending emails from the router.
    ```mikrotik
    /tool e-mail
       set server=mail.server.com port=587 start-tls=yes user=user@domain.com password=password from=user@domain.com
    ```
*   **Fetch:** Download files from a remote location.
    ```mikrotik
    /tool fetch address=example.com dst-path=test.txt
    ```
*   **Files:** Manage the file system on the Router.
*   **Identity:** Set the hostname of the router.
    ```mikrotik
    /system identity
      set name=MyRouter
    ```
*   **Interface Lists:** Create lists of interfaces that can be used for rules and policies.
    ```mikrotik
    /interface list
      add name=lan
    /interface list member
      add list=lan interface=ether2
      add list=lan interface=bridge1
    ```
*   **Neighbor discovery:** Used to find MikroTik routers on the same layer 2 network.
    ```mikrotik
      /ip neighbor discovery set discover-interfaces=ether2
    ```
*   **Note:** Adds a simple note to the system.
    ```mikrotik
    /system note
        add comment="This router is on the main network"
    ```
*   **NTP:** Network Time Protocol for time synchronization.
     ```mikrotik
      /system ntp client set enabled=yes primary-ntp=time.google.com
     ```
*   **Partitions:** Used for managing the physical storage of the device.
*   **Precision Time Protocol:** Used to sync the time on an industrial network or network that has timing implications.
*   **Scheduler:** For scheduling tasks at certain times or intervals.
    ```mikrotik
    /system scheduler
      add name=daily-backup start-time=12:00:00 interval=1d on-event="/system backup save name=daily-backup"
    ```
*   **Services:** Control which services are active on the router.
*   **TFTP:** Trivial File Transfer Protocol

#### Virtual Private Networks

*   **6to4:** IPv6 transition protocol.
    ```mikrotik
    /interface 6to4
       add name=6to4-tunnel mtu=1280 disabled=no
    ```
*   **EoIP:** Ethernet over IP tunneling.
    ```mikrotik
    /interface eoip
      add name=eoip-tunnel remote-address=10.10.10.10 tunnel-id=100
    ```
*   **GRE:** Generic Routing Encapsulation tunneling.
    ```mikrotik
    /interface gre
      add name=gre-tunnel remote-address=10.10.10.10
    ```
*   **IPIP:** IP in IP tunneling.
    ```mikrotik
    /interface ipip
      add name=ipip-tunnel remote-address=10.10.10.10
    ```
*   **IPsec:** IP security for encrypting traffic.
   ```mikrotik
    /ip ipsec proposal
      add auth-algorithms=sha256 enc-algorithms=aes-256-cbc name=proposal1