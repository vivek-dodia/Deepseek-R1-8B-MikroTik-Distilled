Okay, let's dive deep into configuring IP Pools on a MikroTik RouterOS device, focusing on the provided context and extending it to cover all the required areas. This document aims for expert-level understanding.

## IP Pools Configuration for 84.171.203.0/24 on interface ether-89

This document details setting up and understanding IP Pools on a MikroTik router using the specified subnet (84.171.203.0/24) and interface (`ether-89`). We will cover the practical implications of this configuration and explore additional RouterOS features.

### 1. Comprehensive Configuration Scenario and MikroTik Requirements

**Scenario:**

We need to configure a MikroTik router to manage IP addresses within the 84.171.203.0/24 subnet. This IP pool will be used for various purposes, such as assigning addresses to clients via DHCP, creating static mapping of addresses, for virtual network interfaces, or for network-wide routing purposes. The router will use `ether-89` as its primary interface for these addresses. The setup will focus on using an IP pool, a cornerstone of IP management on MikroTik.

**MikroTik Requirements:**

*   **RouterOS Version:** 7.11 (also valid for 6.48 and 7.x versions).
*   **Interface:** `ether-89` will be the designated interface.
*   **Subnet:** 84.171.203.0/24 is the target network.
*   **IP Pool:**  We will configure a pool from this subnet to allocate IP addresses dynamically or statically.
*   **DHCP Server:** We will set up a DHCP server using the pool for a practical example of address assignment (optional but beneficial for demonstration).
*   **Firewall Rules:** We will implement firewall rules to allow or restrict traffic within this subnet.

### 2. Step-by-Step MikroTik Implementation

#### Using Winbox:

1.  **Connect to Your Router:** Open Winbox, connect to your MikroTik router using MAC address or IP.
2.  **Create IP Pool:**
    *   Go to "IP" > "Pool".
    *   Click the "+" button.
    *   Set `Name` (e.g., "pool-84.171.203.0").
    *   Set `Ranges` to `84.171.203.10-84.171.203.254`.
    *   Click Apply and OK.
3.  **Configure IP Address on Interface:**
    *   Go to "IP" > "Addresses".
    *   Click "+".
    *   Set the `Address` to `84.171.203.1/24` (or any other IP within the /24 range that you want as the router's address on the subnet).
    *   Set the `Interface` to `ether-89`.
    *   Click Apply and OK.
4.  **Set up DHCP Server (Optional):**
    *   Go to "IP" > "DHCP Server".
    *   Click "DHCP Setup".
    *   Choose `ether-89` as the interface, and click "Next".
    *   Ensure `84.171.203.1/24` as network address click "Next".
    *   Ensure `84.171.203.1` as gateway, click "Next".
    *   Select created pool `pool-84.171.203.0` as address pool, click "Next".
    *   Set DNS Servers to `8.8.8.8`, `8.8.4.4`, click "Next".
    *   Set a lease time and click "Next" and "OK" if all config looks good.
5.  **Firewall Rules (Basic):**
    *   Go to "IP" > "Firewall".
    *   Configure firewall rules as needed, such as allowing or denying specific traffic for testing purposes.
        *   Example: to allow connections from outside to your devices, set a rule for src-address 84.171.203.0/24 with action accept.
        *   Example: to allow connections from your devices to the world, set a rule for dst-address 0.0.0.0/0 with action accept.

#### Using CLI:

```routeros
/ip pool
add name="pool-84.171.203.0" ranges="84.171.203.10-84.171.203.254"

/ip address
add address=84.171.203.1/24 interface=ether-89

/ip dhcp-server
add address-pool=pool-84.171.203.0 disabled=no interface=ether-89 lease-time=10m name=dhcp-84.171.203
/ip dhcp-server network
add address=84.171.203.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=84.171.203.1

/ip firewall filter
add action=accept chain=forward src-address=84.171.203.0/24
add action=accept chain=forward dst-address=0.0.0.0/0
```

### 3. Complete MikroTik CLI Configuration Commands

**IP Pool Configuration:**

```routeros
/ip pool
add name="pool-84.171.203.0" ranges="84.171.203.10-84.171.203.254"
print # to view the pool and ensure it was created successfully
```

*   `name`: Specifies the unique name for the IP pool.
*   `ranges`: Defines the range of IP addresses included in the pool. Can be one or more ranges, separated by commas (e.g., "192.168.1.10-192.168.1.50,192.168.1.100-192.168.1.150").
*   `print` :  prints a list of all the configured IP pools. This is a good method for reviewing configurations in the CLI.

**Interface Configuration:**

```routeros
/ip address
add address=84.171.203.1/24 interface=ether-89
print # to view the address and ensure it was created successfully
```

*   `address`: Sets the IP address and subnet mask for the interface.
*   `interface`: Specifies the interface to which the IP address is assigned.
*   `print` :  prints a list of all the configured IP addresses, including those assigned to interfaces.

**DHCP Server Configuration (Optional):**

```routeros
/ip dhcp-server
add address-pool=pool-84.171.203.0 disabled=no interface=ether-89 lease-time=10m name=dhcp-84.171.203
print # to verify that the server was added
/ip dhcp-server network
add address=84.171.203.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=84.171.203.1
print # to verify that the network was configured
```

*   `address-pool`:  Specifies the pool to use to assign IP addresses.
*   `disabled`:  Sets if the DHCP server is active or disabled.
*   `interface`: Select the interface that will have the DHCP server.
*   `lease-time`: Sets the lease time for assigned IP addresses.
*   `name`:  Specifies the unique name for the DHCP server.
*   `address`: Specifies the network address associated with the server.
*   `dns-server`: Specifies the DNS server addresses given to the client.
*   `gateway`: Specifies the router IP address given to the client.

**Firewall Rules:**

```routeros
/ip firewall filter
add action=accept chain=forward src-address=84.171.203.0/24
add action=accept chain=forward dst-address=0.0.0.0/0
print # to verify that the rules were added
```

*   `action`: Specifies the action to be performed (accept, drop, reject).
*   `chain`: Defines the firewall chain the rule will be applied to.
*   `src-address`: Source IP address that will trigger this rule.
*    `dst-address`: Destination IP address that will trigger this rule.
*   `print` :  prints a list of all firewall rules, along with other information such as chain name and action performed.

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Overlapping IP Ranges:** Ensure that the IP ranges in your pools and DHCP servers do not overlap. This is a common source of issues that lead to unpredictable behavior.
*   **Incorrect Interface:** Assigning the IP address to the wrong interface.
*   **DHCP Server Not Enabled:** Forgetting to enable the DHCP server or correctly configuring the network settings.
*   **Firewall Blocking:** Overly restrictive firewall rules might block traffic to/from devices within the subnet.
*   **MTU Issues:** Mismatched MTU settings between clients and the router can cause packet fragmentation problems which can lead to the network being unusable.

**Troubleshooting:**

*   **Check Logs:** Use `/system logging print` to check logs for any errors related to IP pools, DHCP, or firewall.
*   **Interface Status:** Check if `ether-89` is up (`/interface ethernet print`).
*   **DHCP Leases:** Use `/ip dhcp-server lease print` to see assigned IP addresses. If there are no leases, there might be a problem with the DHCP server or the client device.
*   **Ping Test:** Use `/ping 84.171.203.1` from your MikroTik router to test if the router is up and reachable.  Also, try pinging the client devices within the subnet to confirm their connectivity.
*   **Torch:** Use the `/tool torch interface=ether-89` to monitor the traffic on the interface and look for any errors or anomalies.
*    **Packet Sniffer**: You can use `/tool packet-sniffer start file-name=capture` to capture network traffic from an interface and analyze the data.

**Error Scenarios:**

*   **Error:** "Error: could not add address, network overlaps with existing networks."
    *   **Cause:** An IP address within the pool overlaps with another IP address on the router or the DHCP Server configuration does not match the network settings.
    *   **Solution:** Remove overlapping addresses or adjust the network settings.
*   **Error:** "DHCP server did not respond" on a client.
    *   **Cause:**  Firewall rules are blocking DHCP traffic or DHCP Server is not enabled correctly.
    *   **Solution:**  Check `/ip dhcp-server print`, and firewall rules for blocks. Verify the network is set up correctly. Use torch to monitor the DHCP discovery and offer packets.

### 5. Verification and Testing Steps

*   **Ping:** Ping devices within the subnet from the router (`/ping 84.171.203.x`).
*   **Traceroute:** Use traceroute to identify the path from the router to the internet or to any destination on the subnet (`/traceroute 84.171.203.x`).
*   **Torch:** Monitor traffic on `ether-89` (`/tool torch interface=ether-89`) for correct traffic flow.
*   **DHCP Client:** Connect a device to the `ether-89` network and verify it gets an IP address from the pool.
*   **Packet Sniffer:** Use `/tool packet-sniffer start file-name=capture interface=ether-89` to capture network traffic on `ether-89`. Analyze the capture with a tool like Wireshark.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **IP Pool Usage:** IP Pools are used not only for DHCP but also for hotspot, virtual private network (VPN) server configurations, and static mappings. For example, if you are creating a Point-to-Point VPN, you'd use an IP Pool for the virtual interfaces involved in the connection.

*   **Hotspot:** MikroTik Hotspot uses IP Pools for IP address assignment to hotspot clients. You can manage user groups and their respective address pools.

*   **Virtual Routing and Forwarding (VRF):** VRFs can utilize IP Pools for defining routing instances. Multiple routing tables can coexist on the same router for multiple clients. You'd assign a different IP Pool to each VRF instance so the different networks do not collide.

*   **Limitations:**
    *   **Pool Size:** A single pool cannot span multiple subnets or non-contiguous IP address ranges. Multiple pools will have to be created for this.
    *   **Address Conflicts:** While RouterOS helps with avoiding IP collisions, manual configuration errors are possible.
    *   **Dynamic Address Assignment:** Dynamic IP assignment can lead to short periods when a device is waiting for a lease. In very busy environments with frequent connections and disconnections, this can become a concern.

**Scenario using less common feature: VRF:**

```routeros
/routing vrf
add name=vrf-84.171.203.0
/ip address
add address=84.171.203.1/24 interface=ether-89 vrf=vrf-84.171.203.0
/ip pool
add name=pool-vrf-84.171.203.0 ranges="84.171.203.10-84.171.203.254"
/ip dhcp-server
add address-pool=pool-vrf-84.171.203.0 disabled=no interface=ether-89 lease-time=10m name=dhcp-vrf-84.171.203 vrf=vrf-84.171.203.0
/ip dhcp-server network
add address=84.171.203.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=84.171.203.1 vrf=vrf-84.171.203.0
```

This sets up a VRF named `vrf-84.171.203.0`. It is configured with its own IP address, IP Pool, and DHCP Server within the VRF context.

### 7. MikroTik REST API Examples

MikroTik RouterOS has a built in REST API. These are some example usages of this API to manage an IP pool. To use these API calls, you need to enable the API service. Navigate to `/ip services` and enable `api` and `api-ssl`.

**Example: Create an IP Pool**

*   **Endpoint:** `https://<your_router_ip>/rest/ip/pool`
*   **Method:** `POST`
*   **JSON Payload:**

    ```json
    {
      "name": "pool-rest-test",
      "ranges": "192.168.1.20-192.168.1.50"
    }
    ```

*   **Expected Response (201 Created):**

    ```json
    {
      ".id": "*2",
      "name": "pool-rest-test",
      "ranges": "192.168.1.20-192.168.1.50"
    }
    ```

**Example: Get IP Pool**

*   **Endpoint:** `https://<your_router_ip>/rest/ip/pool/<pool_id>`
*   **Method:** `GET`
*   **JSON Payload:** None

*   **Expected Response (200 OK):**

    ```json
    {
      ".id": "*2",
      "name": "pool-rest-test",
      "ranges": "192.168.1.20-192.168.1.50"
    }
    ```

**Example: Update IP Pool**

*   **Endpoint:** `https://<your_router_ip>/rest/ip/pool/<pool_id>`
*   **Method:** `PATCH`
*   **JSON Payload:**

    ```json
    {
      "ranges": "192.168.1.60-192.168.1.100"
    }
    ```

*   **Expected Response (200 OK):**

    ```json
    {
       ".id": "*2",
       "name": "pool-rest-test",
       "ranges": "192.168.1.60-192.168.1.100"
    }
    ```

**Example: Delete IP Pool**

*   **Endpoint:** `https://<your_router_ip>/rest/ip/pool/<pool_id>`
*   **Method:** `DELETE`
*   **JSON Payload:** None
*   **Expected Response (204 No Content):** Empty response

**Note:**
Replace `<your_router_ip>` with the IP address of your MikroTik router and `<pool_id>` with the ID of the pool you wish to interact with (e.g., `*1`, `*2`). You can get the pool id by listing all the IP pools with a GET request to `/rest/ip/pool`.

### 8. In-Depth Explanations of Core Concepts

*   **IP Addressing:**  IPv4 addresses are 32-bit numbers that are used to identify devices on a network. In the example, 84.171.203.0/24 denotes the network address with the subnet mask, which indicates that the first 24 bits represent the network, and the last 8 bits are available for host addresses.
*   **IP Pools:** IP Pools are a logical grouping of IP addresses available for allocation. This grouping of addresses will have some restrictions such as a restriction on which subnets or contiguous IP ranges that can be combined. This enables better management of IP address allocations across a network.
*   **IP Routing:** IP Routing is the process of forwarding packets from one network to another.  A router determines the best path to send the packet based on routing tables. In our example, the MikroTik router will use its routing table to determine how to send packets to other subnets.
*   **IP Settings:** This includes setting up IP addresses for interfaces, configuring DHCP servers, and setting up IP Pools. IP Settings configuration is key to getting the router functioning as intended.
*   **Bridging:** A bridge is a networking device that connects multiple network segments, forming a single logical network. The router forwards packets based on MAC addresses. In a MikroTik, you can bridge multiple interfaces together so the same subnet can be extended over multiple physical interfaces. The router learns which MAC addresses are associated with each port and then forwards the traffic accordingly.
*   **Firewall:** The firewall controls which traffic can pass through the router based on defined rules.  It inspects incoming and outgoing traffic for patterns that match defined rules, and it can filter traffic based on several different criteria. This is a critical component to ensuring the network's security.

### 9. Security Best Practices Specific to MikroTik Routers

*   **Change Default Credentials:** Always change the default admin password.
*   **Disable Unused Services:** Disable unnecessary services (e.g., Telnet, API if not needed). Use `/ip services print` to list active services and `/ip services disable <service name>` to disable any unused services.
*   **Firewall Rules:** Create specific firewall rules to allow only necessary traffic. Always implement a default-drop rule at the end of your firewall configuration to prevent all traffic not explicitly allowed.
*   **Secure API Access:** If using the REST API, use SSL (`api-ssl`) and restrict access using IP address restrictions.
*   **Keep RouterOS Updated:** Regularly update RouterOS to patch security vulnerabilities. You can do so by navigating to `/system package update` in CLI or under `System -> Packages` in Winbox. Check `check-for-updates`, install any updates if any and reboot the router if necessary.
*   **Remote Access:** Restrict remote access to specific trusted IPs. Use `/ip firewall filter` to set rules to only allow access from your designated remote location.
*   **Strong Passwords:** Use strong, unique passwords for all accounts.

### 10. Detailed Explanations and Configuration Examples for Other MikroTik Topics

This section covers various RouterOS topics with specific examples:

**IP Addressing (IPv4 and IPv6):**

*   **IPv4:**  We've primarily focused on IPv4 in our example, but MikroTik also supports IPv6. You can configure both at the same time.

```routeros
/ipv6 address add address=2001:db8::1/64 interface=ether-89
```
This configures an IPv6 address `2001:db8::1/64` to the `ether-89` interface.

*   **IPv6:** You need to enable IPv6 routing and consider using DHCPv6 or IPv6 autoconfiguration if devices are connected directly to the interface. IPv6 uses autoconfiguration, meaning devices will be assigned an IP without needing a DHCPv6 server, so long as a Router Advertisement message is being transmitted.
```routeros
/ipv6 settings set disable-ipv6=no
/ipv6 nd set interface=ether-89 advertise-dns=yes advertise-managed-flag=no
```
This configures IPv6 and advertises the IPv6 Router Address to the devices connected to the network.

**MAC Server:**

*   Used to remotely manage Mikrotik devices via MAC Addresses (neighbor discovery).

```routeros
/tool mac-server set allowed-interface-list=all enabled=yes
/tool mac-server mac-winbox set allowed-interface-list=all enabled=yes
```
These commands allow MAC server to be used to connect to the router. `allowed-interface-list=all` is often used when you need access from any interface. A specific list can be specified with interface names separated by commas.

**RoMON:**

*   MikroTik proprietary protocol used for remote management of multiple MikroTik devices in the same network. You can manage one MikroTik through another.
```routeros
/tool romon set enabled=yes id=router1 romon-port=ether-89
```
This will enable RoMON on `ether-89` with ID of `router1`.

**WinBox:**

*   The graphical user interface for RouterOS. It is used in conjunction with the CLI to manage your router.
    *   You can download WinBox for your operating system here: [https://mt.lv/winbox](https://mt.lv/winbox)

**Certificates:**

*   Used for secure communication (HTTPS, VPN, etc).  You can create self-signed certificates or import from a certificate authority.

```routeros
/certificate generate-self-signed name=selfsigned-cert common-name="router1.local" subject-alt-name=router1.local
/certificate print
```
This generates a self signed certificate. This certificate can be exported and installed on devices for secure connectivity.

**PPP AAA:**

*   PPP (Point-to-Point Protocol) Authentication, Authorization, and Accounting. You can use local user database or remote RADIUS servers for user validation.

```routeros
/ppp secret add name=user1 password=password1 service=ppp profile=default
```
This will create a new PPP account with name user1, password password1. This can be used for PPPoE, PPTP, etc.

**RADIUS:**

*   Remote Authentication Dial-In User Service. Used for central user authentication.

```routeros
/radius add address=192.168.1.10 secret=radius_secret timeout=3
```
This configures a RADIUS server at 192.168.1.10, with shared secret `radius_secret`. This server will be used when a user tries to connect and the router needs to validate the connection.

**User / User groups:**

*   Used to manage user permissions and access.

```routeros
/user group add name=admin policy=read,write,test,password,reboot,policy,ftp,web,winbox,api,romon
/user add name=admin group=admin password=admin
```
This will create a user group with full permissions and a user with full administrator rights.

**Bridging and Switching:**

```routeros
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=ether-89
/interface bridge port add bridge=bridge1 interface=ether-90
```
This will create a bridge and then add two interfaces to it. Now the devices on these interfaces are on the same network.

**MACVLAN:**
*  Used to create virtual interfaces with different MAC addresses on the same physical interface. Useful in environments where several virtual interfaces are necessary, but physical interfaces are limited.

```routeros
/interface macvlan add name=macvlan-89-1 master-interface=ether-89 mac-address=02:02:02:02:02:01
/interface macvlan add name=macvlan-89-2 master-interface=ether-89 mac-address=02:02:02:02:02:02
```
This will create 2 virtual interfaces with different MAC addresses based on `ether-89`.

**L3 Hardware Offloading:**

*  Hardware acceleration of L3 (IP) functions on the router for increased performance.
  This is an important feature if your router is under high load.

```routeros
/interface ethernet set ether-89 l3-hw-offloading=yes
```
This enables Layer 3 Hardware offloading on the interface `ether-89`.

**MACsec:**

*  Layer 2 security protocol to secure Ethernet links.

```routeros
/interface macsec add name=macsec-89 parent-interface=ether-89 key=0102030405060708090a0b0c0d0e0f10
/interface macsec print
```
This creates a MACsec interface associated with `ether-89` with a key for secure communication. You will need to configure both sides of the link to use MACsec.

**Quality of Service:**

*   Used to prioritize network traffic.

```routeros
/queue type add name=priority-queue kind=pcq pcq-rate=1M
/queue simple add name=priority-q target=84.171.203.0/24 queue=priority-queue
```
This will create a simple queue that prioritizes traffic from the network `84.171.203.0/24`.
You can monitor the queue statistics using the `/queue simple monitor <queue_name>` command.

**Switch Chip Features:**

*   Configuration options available on routers that contain a switch chip.

```routeros
/interface ethernet switch vlan print
```
This command prints switch configuration of all the ports. If your device has a switch chip, you can configure VLANs, rate limiting, mirroring and other low-level features. This is usually different from the router capabilities.

**VLAN:**

*   Virtual LANs. Logically separate the network using tags.

```routeros
/interface vlan add name=vlan10 interface=ether-89 vlan-id=10
/ip address add address=192.168.10.1/24 interface=vlan10
```
This creates a VLAN with ID `10` on `ether-89` and assigns it an IP address. Devices on VLAN 10 will be separated from devices not using a VLAN tag on the interface.

**VXLAN:**

*   Layer 2 overlay network protocol over a Layer 3 network.

```routeros
/interface vxlan add name=vxlan10 vni=100 remote-address=192.168.1.10 interface=ether-89
/interface bridge port add bridge=bridge1 interface=vxlan10
```
This adds a VXLAN tunnel to a remote IP address that can be used as part of a bridge to connect different networks together. You will have to configure both routers to use VXLAN with the same VNI.

**Firewall and Quality of Service:**

*   **Connection tracking**: Tracks all connections, which can be helpful for troubleshooting
    *   `/ip firewall connection print` shows all current connections.
*   **Firewall**: Used for filtering traffic based on source, destination and various other criteria. Example shown above.
*   **Packet Flow in RouterOS**: You can see the general packet flow from the MikroTik manual.
*  **Queues**: Used for QoS. See example above.
*   **Firewall and QoS Case Studies**: A specific example of QoS is to prioritize VoIP traffic and low-latency communication.
*   **Kid Control**: Allows restricting network access based on time and IP address for children's devices.
*   **UPnP**: Allows automatic port forwarding. This is not recommended for production systems for security reasons.
    *   `/ip upnp set enabled=yes`
*   **NAT-PMP**: Allows for automatic port forwarding, similar to UPnP. This is not recommended for production systems for security reasons.
    *   `/ip upnp set allow-natpmp=yes`

**IP Services (DHCP, DNS, SOCKS, Proxy):**

*   **DHCP:** Dynamic Host Configuration Protocol for automatic IP address assignment. Example shown above.
*   **DNS:** Domain Name System for resolving domain names to IP addresses.
    *   `/ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes`
*   **SOCKS:** SOCKS proxy service.
    *   `/ip socks set enabled=yes`
*   **Proxy:** HTTP Proxy Service.
    *   `/ip proxy set enabled=yes`

**High Availability Solutions:**

*   **Load Balancing:** Distribute traffic across multiple paths.
    *   You can use PCC (Per Connection Classifier) and ECMP (Equal-Cost Multi-Path) for basic load balancing.
*   **Bonding:** Combine multiple interfaces to act as one.
    *   `/interface bonding add name=bond1 mode=802.3ad slaves=ether-89,ether-90`
*   **Bonding Examples**: Different modes such as active-backup, load-balancing, etc. are available.
*   **HA Case Studies**: High Availability can be configured by using CARP or VRRP protocols.
*   **Multi-chassis Link Aggregation Group (MLAG)**: Not natively supported in MikroTik RouterOS. It requires a special setup of network switches for it to function.
*   **VRRP:** Virtual Router Redundancy Protocol.
    *   `/interface vrrp add name=vrrp1 interface=ether-89 vrid=1 priority=100`
    *    `/interface vrrp add name=vrrp1 interface=ether-89 vrid=1 priority=90`
     This would set up two devices in a VRRP environment.
*   **VRRP Configuration Examples**:  You'll need multiple MikroTik devices. Each will have a unique priority and an identical VRID for proper operation.

**Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application)**

*   **GPS:** MikroTik device can use GPS to get location data.
*   **LTE:** You can connect to a mobile network using a compatible modem.
*   **PPP:** Protocol for point to point links (PPPoE, PPTP, etc)
*   **SMS:** Some MikroTik models can send/receive SMS messages.
    *   `/system sms print`
*   **Dual SIM Application:** Configure load balancing, failover, etc. between different cellular providers.

**Multi Protocol Label Switching - MPLS**

*   **MPLS Overview:** Provides a way to forward traffic with labels for faster routing.
*   **MPLS MTU:** Special considerations for MTU on MPLS networks.
*   **Forwarding and Label Bindings:** MPLS uses labels to determine routing paths
*   **EXP bit and MPLS Queuing:** The EXP bits are used for quality of service.
*   **LDP:** Label Distribution Protocol to manage label mappings.
    *    `/mpls ldp set enabled=yes`
*   **VPLS:** Virtual Private LAN Service, creating Layer 2 connections over an MPLS network.
*   **Traffic Eng:** Manipulate MPLS traffic paths to control network traffic.
*   **MPLS Reference**: The MikroTik manual will help in understanding the MPLS features in RouterOS.

**Network Management (Including: ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow)**
*   **ARP:** Address Resolution Protocol.
    *   `/ip arp print` displays the ARP table.
*   **Cloud:** Used for MikroTik cloud configuration
    *    `/system cloud print`
*   **DHCP:** Shown above
*   **DNS:** Shown above
*   **SOCKS:** Shown above
*   **Proxy:** Shown above
*   **Openflow:** A network protocol that allows network devices to be remotely controlled. Not often used in home or SMB environments.

**Routing (Including: Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS)**

*   **Routing Protocol Overview**: RouterOS supports several routing protocols.
*   **Moving from ROSv6 to v7 with examples**: There are slight changes between ROS v6 and v7. Usually it is recommended to review documentation and test configurations before deploying an updated system.
*   **Routing Protocol Multi-core Support**: RouterOS can use multiple cores for higher processing in routing.
*   **Policy Routing**: Allows you to change the route the router will use based on specific conditions.
*   **Virtual Routing and Forwarding - VRF**: Shown in the example above.
*   **OSPF**: Open Shortest Path First Routing.
    *   `/routing ospf instance add name=ospf1 router-id=192.168.1.10`
*   **RIP**: Routing Information Protocol.
    *   `/routing rip set enabled=yes`
*   **BGP**: Border Gateway Protocol.
    *   `/routing bgp instance add name=bgp1 router-id=192.168.1.10`
*   **RPKI**: Route Origin Validation.
*   **Route Selection and Filters**: Use filters for better control of routing.
*   **Multicast**: IP Multicast used for distributing video traffic in particular
*   **Routing Debugging Tools**: Use `/tool torch` and `/routing debug` commands for troubleshooting.
*   **Routing Reference**: The MikroTik manual has more information about the routing features in RouterOS.
*   **BFD**: Bidirectional Forwarding Detection.
    *    `/routing bfd set enabled=yes`
*   **IS-IS**: Intermediate System to Intermediate System Routing protocol.

**System Information and Utilities**

*   **Clock**: To keep accurate time.
    *   `/system clock print`
    *   `/system clock set time=12