**IP Pools**

**1. Configuration Scenario and Requirements**

An IP pool is a range of IP addresses that can be assigned to devices on a network. This is a common technique used by ISPs to manage their customers' IP addresses.

**2. Step-by-step Implementation**

**2.1. Create the IP Pool**

Log into the MikroTik router using WinBox or the command line interface (CLI).
Navigate to **IP** > **Pool**.
Click the **Plus** button to create a new pool.
Enter a **Name** for the pool (e.g., ISP-Customers).
Enter the **IP Range** that you want to use for the pool (e.g., 192.168.1.0/24).
Set the **Network** to the subnet that will be using the IP pool (e.g., 192.168.1.0/24).
Click **OK** to save the pool.

**2.2. Add Gateway**

If you want to use the MikroTik router as the default gateway for the pool, you need to add the router's IP address as the gateway. Navigate to **IP** > **Routes**.
Click the **Plus** button to create a new route.
Enter the **Gateway** for the pool (e.g., 192.168.1.1).
Enter the **Network** to the subnet that will be using the IP pool (e.g., 192.168.1.0/24).
Click **OK** to save the route.

**2.3. Assign the IP Pool to Interface**

If you want to assign the IP pool to a specific interface, do the following:
Navigate to **IP** > **Address**.
Click the **Plus** button to create a new IP address.
Select the **Interface** that you want to assign the IP pool to (e.g., ether1).
Enter the **IP Address** of the subnet that will be using the IP pool (e.g., 192.168.1.1).
Enter the **Network** to the subnet that will be using the IP pool (e.g., 192.168.1.0/24).
Click **OK** to save the address.

**3. Complete Configuration Commands**

```
/ip pool
add name=ISP-Customers ranges=192.168.1.0/24
/ip address
add interface=ether1 address=192.168.1.1/24
/ip route
add dst-address=192.168.1.0/24 gateway=192.168.1.1
```

**4. Common Pitfalls and Solutions**

* Ensure that the IP range you specify does not overlap with any existing IP addresses on your network.
* If you are using the MikroTik router as the default gateway, make sure that the router's IP address is added as the gateway for the pool.
* If you are assigning the IP pool to a specific interface, make sure that the interface is enabled and configured with the correct IP address and network settings.

**5. Verification and Testing Steps**

* To verify that the IP pool is configured correctly, you can use the following command:

```
/ip pool
print
```

* To test the IP pool, you can assign an IP address from the pool to a device on your network.

**6. Related Features and Considerations**

* You can use multiple IP pools to manage different subnets on your network.
* You can use the MikroTik router's DHCP server to automatically assign IP addresses from the pool to devices on your network.
* You can use the MikroTik router's firewall to restrict access to the IP pool to specific devices or networks.

**7. MikroTik REST API Examples**

**Endpoint:** `/api/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "name": "ISP-Customers",
  "ranges": [
    "192.168.1.0/24"
  ],
  "network": "192.168.1.0/24"
}
```

**Expected Response:**

```json
{
  "id": "1",
  "name": "ISP-Customers",
  "ranges": [
    "192.168.1.0/24"
  ],
  "network": "192.168.1.0/24"
}
```

**8. Additional Examples and Explanations**

Refer to the following links for additional examples and explanations of the topics mentioned in the special instructions:

* [IP Addressing (IPv4 and IPv6)](https://wiki.mikrotik.com/wiki/Manual:IP/IPv4)
* [IP Pools](https://wiki.mikrotik.com/wiki/Manual:IP/Pool)
* [IP Routing](https://wiki.mikrotik.com/wiki/Manual:IP/Route)
* [IP Settings](https://wiki.mikrotik.com/wiki/Manual:IP)
* [MAC server](https://wiki.mikrotik.com/wiki/Manual:MAC_server)
* [RoMON](https://wiki.mikrotik.com/wiki/Manual:RoMON)
* [WinBox](https://wiki.mikrotik.com/wiki/Manual:Winbox)
* [Certificates](https://wiki.mikrotik.com/wiki/Manual:Certificate)
* [PPP AAA](https://wiki.mikrotik.com/wiki/Manual:PPP/AAA)
* [RADIUS](https://wiki.mikrotik.com/wiki/Manual:RADIUS)
* [User / User groups](https://wiki.mikrotik.com/wiki/Manual:User_Manager)
* [Bridging and Switching](https://wiki.mikrotik.com/wiki/Manual:Switch)
* [MACVLAN](https://wiki.mikrotik.com/wiki/Manual:MACVLAN)
* [L3 Hardware Offloading](https://wiki.mikrotik.com/wiki/Manual:L3HW)
* [MACsec](https://wiki.mikrotik.com/wiki/Manual:MACsec)
* [Quality of Service](https://wiki.mikrotik.com/wiki/Manual:QoS)
* [Switch Chip Features](https://wiki.mikrotik.com/wiki/Manual:Switch_Features)
* [VLAN](https://wiki.mikrotik.com/wiki/Manual:VLAN)
* [VXLAN](https://wiki.mikrotik.com/wiki/Manual:VXLAN)
* [Firewall and Quality of Service (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP)](https://wiki.mikrotik.com/wiki/Manual:Firewall)
* [IP Services (DHCP, DNS, SOCKS, Proxy)](https://wiki.mikrotik.com/wiki/Manual:IP/Services)
* [High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples)](https://wiki.mikrotik.com/wiki/Manual:High_Availability)
* [Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application)](https://wiki.mikrotik.com/wiki/Manual:Mobile)
* [Multi Protocol Label Switching - MPLS (Including: MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference)](https://wiki.mikrotik.com/wiki/Manual:MPLS)
* [Network Management (Including: ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow)](https://wiki.mikrotik.com/wiki/Manual:IP/Services)
* [Routing (Including: Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS)](https://wiki.mikrotik.com/wiki/Manual:Routing)
* [System Information and Utilities (Including: Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP)](https://wiki.mikrotik.com/wiki/Manual:System)
* [Virtual Private Networks (Including: 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier)](https://wiki.mikrotik.com/wiki/Manual:VPN)
* [Wired Connections (Including: Ethernet, MikroTik wired interface compatibility, PWR Line)](https://wiki.mikrotik.com/wiki/Manual:Interface/Ethernet)
* [Wireless (Including: WiFi, Wireless Interface, W60G,