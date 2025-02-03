## VLAN Configuration in RouterOS 7.11

### Configuration Scenario and Requirements

**Scenario:** Configure VLANs on a MikroTik RouterOS 7.11 device to separate traffic and improve security.

**Requirements:**

- MikroTik RouterOS 7.11 device
- Multiple physical interfaces (e.g., Ethernet ports)
- Understanding of VLAN concepts and requirements

### Step-by-Step Implementation

**1. Create VLAN Interfaces:**

Create VLAN interfaces on the physical interfaces where VLANs will be used.

```
/interface vlan add name=vlan10 vlan-id=10 interface=ether1
/interface vlan add name=vlan20 vlan-id=20 interface=ether2
```

**2. Assign IP Addresses to VLAN Interfaces:**

Assign IP addresses to the VLAN interfaces to allow communication between devices on that VLAN.

```
/ip address add address=192.168.10.1/24 interface=vlan10
/ip address add address=192.168.20.1/24 interface=vlan20
```

**3. Configure DHCP Server for VLANs:**

Set up a DHCP server on each VLAN interface to provide IP addresses to devices connected to that VLAN.

```
/ip dhcp-server add interface=vlan10 address-pool=pool10 range=192.168.10.100-192.168.10.199
/ip dhcp-server add interface=vlan20 address-pool=pool20 range=192.168.20.100-192.168.20.199
```

**4. Configure Firewall Rules:**

Create firewall rules to allow traffic between VLANs and from VLANs to the outside world (if necessary).

```
/ip firewall mangle add chain=forward action=accept in-interface=vlan10 dst-address=192.168.20.0/24
/ip firewall mangle add chain=forward action=accept in-interface=vlan20 dst-address=192.168.10.0/24
```

### Complete Configuration Commands

```
/interface vlan add name=vlan10 vlan-id=10 interface=ether1
/interface vlan add name=vlan20 vlan-id=20 interface=ether2
/ip address add address=192.168.10.1/24 interface=vlan10
/ip address add address=192.168.20.1/24 interface=vlan20
/ip dhcp-server add interface=vlan10 address-pool=pool10 range=192.168.10.100-192.168.10.199
/ip dhcp-server add interface=vlan20 address-pool=pool20 range=192.168.20.100-192.168.20.199
/ip firewall mangle add chain=forward action=accept in-interface=vlan10 dst-address=192.168.20.0/24
/ip firewall mangle add chain=forward action=accept in-interface=vlan20 dst-address=192.168.10.0/24
```

### Common Pitfalls and Solutions

- **Incorrect VLAN ID:** Ensure that the VLAN ID specified in the `vlan-id` parameter is unique and valid.
- **Duplicated VLAN Interfaces:** Do not create multiple VLAN interfaces with the same VLAN ID on the same physical interface.
- **No IP Address Assigned:** Confirm that an IP address has been assigned to the VLAN interface and that it is within the specified subnet.
- **DHCP Server Not Active:** Ensure that the DHCP server on the VLAN interface is enabled and that it has an active address pool.
- **Firewall Rules Not Applied:** Check that the firewall rules allowing traffic between VLANs and from VLANs to the outside world have been created and are applied.

### Verification and Testing Steps

- Verify VLAN interfaces and IP addresses using `/interface vlan print` and `/ip address print`.
- Check DHCP server status with `/ip dhcp-server print`.
- Test connectivity between devices on different VLANs using ping or traceroute.
- Ensure that traffic flow between VLANs is controlled according to the firewall rules.

### Related Features and Considerations

- **Bridging VLANs:** Use the `/bridge add` command to bridge VLANs and allow traffic to pass between them without going through the router.
- **VLAN Tagging:** Enable VLAN tagging on physical interfaces to allow multiple VLANs to share the same physical link.
- **Security:** Consider implementing additional security measures, such as port security and access control lists, to protect the VLANs.
- **Scalability:** RouterOS supports up to 4094 VLANs. The number of supported VLANs depends on the hardware and software configuration.