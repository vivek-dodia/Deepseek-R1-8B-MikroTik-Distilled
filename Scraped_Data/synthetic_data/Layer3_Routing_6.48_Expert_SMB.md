## Layer3 Routing in RouterOS 6.48

### Configuration Scenario and Requirements

This guide demonstrates how to configure a MikroTik RouterOS 6.48 device as a Layer3 router, allowing it to perform inter-VLAN routing and provide internet access to multiple VLANs.

* RouterOS version: 6.48 (6.x or 7.x compatible)
* Multiple VLANs configured on the switch ports
* An internet gateway (or upstream router) with a LAN interface
* Static IP address assignment for each VLAN

### Step-by-Step Implementation

**1. Configure VLANs**

Create and configure VLANs on the switch ports where devices will reside. This can be done through the switch configuration interface or via RouterOS CLI:

```
/interface vlan add name=VLAN1 vlan-id=1 interface=ether1

/interface vlan add name=VLAN2 vlan-id=2 interface=ether2
```

**2. Create Bridge Interfaces**

Create bridge interfaces for each VLAN, which will act as the Layer2 switch:

```
/interface bridge add name=Bridge1 vlan1=VLAN1
/interface bridge add name=Bridge2 vlan1=VLAN2
```

**3. Configure IP Addresses**

Assign static IP addresses to each bridge interface:

```
/ip address add address=192.168.1.1/24 interface=Bridge1
/ip address add address=192.168.2.1/24 interface=Bridge2
```

**4. Enable IP Forwarding**

Enable IP forwarding on the router to allow traffic to be routed between VLANs:

```
/ip firewall filter add action=accept chain=forward
```

**5. Configure Gateway**

Set the default gateway for each bridge interface to the internet gateway's LAN IP:

```
/ip route add gateway=192.168.0.1 dst-address=0.0.0.0/0
```

**6. Configure NAT**

Enable source NAT for traffic from the VLANs to access the internet:

```
/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1-gateway
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=1 interface=ether1
/interface vlan add name=VLAN2 vlan-id=2 interface=ether2
/interface bridge add name=Bridge1 vlan1=VLAN1
/interface bridge add name=Bridge2 vlan1=VLAN2
/ip address add address=192.168.1.1/24 interface=Bridge1
/ip address add address=192.168.2.1/24 interface=Bridge2
/ip firewall filter add action=accept chain=forward
/ip route add gateway=192.168.0.1 dst-address=0.0.0.0/0
/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1-gateway
```

### Common Pitfalls and Solutions

* **No internet access:** Ensure that the gateway is configured correctly and that the NAT rules are applied.
* **VLANs cannot communicate:** Verify that the VLANs are correctly configured and that the bridge interfaces are enabled.
* **Traffic is not routed between VLANs:** Check if IP forwarding is enabled and if there are any firewall rules blocking traffic.

### Verification and Testing Steps

* Ping between different VLANs to verify Layer3 connectivity.
* Access the internet from devices connected to each VLAN.
* Run traceroutes to verify the routing path.

### Related Features and Considerations

* **VLAN Trunking:** Configure VLAN trunking to allow multiple VLANs to pass over a single physical link.
* **Firewall Rules:** Implement firewall rules to control traffic flow and enhance network security.
* **Policy Routing:** Create custom routing rules based on source IP, destination IP, or other criteria.