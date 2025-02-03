## VLAN Configuration in RouterOS 6.48 for ISP Networks

### Configuration Scenario and Requirements

* Configure multiple VLANs on a MikroTik router in an ISP network.
* VLANs should be used to isolate and segment traffic for different customers or services.
* The router should be able to route traffic between VLANs and to the WAN interface.

### Step-by-Step Implementation

**Step 1: Create VLANs**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
```

**Step 2: Assign VLANs to Physical Ports**

```
/interface ethernet switch port add bridge=bridge1 vlan=VLAN10
/interface ethernet switch port add bridge=bridge1 vlan=VLAN20
```

**Step 3: Configure DHCP Server for Each VLAN**

```
/ip dhcp-server add address-pool=VLAN10-pool range=10.10.10.0/24 interface=VLAN10
/ip dhcp-server add address-pool=VLAN20-pool range=10.20.20.0/24 interface=VLAN20
```

**Step 4: Configure Default Gateway for Each VLAN**

```
/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade
/ip route add gateway=10.10.10.1/24 interface=VLAN10
/ip route add gateway=10.20.20.1/24 interface=VLAN20
```

**Step 5: Configure Inter-VLAN Routing**

```
/ip firewall filter add chain=forward action=accept src-address=VLAN10 dst-address=VLAN20
/ip firewall filter add chain=forward action=accept src-address=VLAN20 dst-address=VLAN10
```

### Complete Configuration Commands

**VLAN Configuration**

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
```

**VLAN Port Configuration**

```
/interface ethernet switch port add bridge=bridge1 vlan=VLAN10
/interface ethernet switch port add bridge=bridge1 vlan=VLAN20
```

**DHCP Server Configuration**

```
/ip dhcp-server add address-pool=VLAN10-pool range=10.10.10.0/24 interface=VLAN10
/ip dhcp-server add address-pool=VLAN20-pool range=10.20.20.0/24 interface=VLAN20
```

**Default Gateway Configuration**

```
/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade
/ip route add gateway=10.10.10.1/24 interface=VLAN10
/ip route add gateway=10.20.20.1/24 interface=VLAN20
```

**Inter-VLAN Routing Configuration**

```
/ip firewall filter add chain=forward action=accept src-address=VLAN10 dst-address=VLAN20
/ip firewall filter add chain=forward action=accept src-address=VLAN20 dst-address=VLAN10
```

### Common Pitfalls and Solutions

* **VLAN IDs:** Ensure that VLAN IDs do not overlap with any other VLANs in the network.
* **Port Assignment:** Verify that the correct ports are assigned to each VLAN.
* **DHCP Server Configuration:** Ensure that the DHCP server pools and ranges are correct and do not overlap.
* **Default Gateway Configuration:** Ensure that the default gateway IP addresses match the VLAN subnets.

### Verification and Testing Steps

* Check the VLAN configuration with `/interface vlan print`.
* Verify VLAN port assignments with `/interface ethernet switch port print`.
* Test DHCP connectivity by connecting a client to each VLAN and obtaining an IP address.
* Ping between different VLANs to verify inter-VLAN routing.

### Related Features and Considerations

* **VLAN Tagging:** Configure VLAN tagging (802.1Q) to allow traffic to be tagged and untagged on specific ports.
* **QOS:** Implement Quality of Service (QOS) for each VLAN to prioritize traffic.
* **Security:** Use firewall rules and ACLs to restrict access between VLANs and to the WAN interface.