## VLAN Configuration in RouterOS 6.48 (ISP)

### Configuration Scenario and Requirements

- Configure VLANs to segment a network for different departments or services.
- Set up inter-VLAN routing for communication between VLANs.
- Provide Internet access to all VLANs through a single uplink.

### Step-by-Step Implementation

**1. Create VLANs**

**Command:**
```
/interface vlan add name=VLAN1 vid=1
```

* Replace `VLAN1` and `1` with your desired VLAN name and ID.

**2. Assign Interfaces to VLANs**

**Command:**
```
/interface bridge port add bridge=VLAN1 interface=ether1-bridge
```

* Replace `VLAN1` with the VLAN name.
* Replace `ether1-bridge` with the physical interface assigned to the VLAN.

**3. Enable Inter-VLAN Routing**

**Command:**
```
/ip routing add dst-address=0.0.0.0/0 gateway=192.168.1.1
```

* Replace `192.168.1.1` with your router's IP address.

**4. Configure Default Gateway for VLANs**

**Command:**
```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 interface=VLAN1
```

* Replace `VLAN1` with the VLAN name.

**5. Allow DHCP on VLANs**

**Command:**
```
/ip dhcp-server network add address=192.168.1.0/24 interface=VLAN1 dhcp-options=option1,option2
```

* Replace `VLAN1` with the VLAN name.
* Set `address` to the desired IP range for the VLAN.
* Replace `option1` and `option2` with any additional DHCP options.

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vid=1
/interface bridge port add bridge=VLAN1 interface=ether1-bridge
/ip routing add dst-address=0.0.0.0/0 gateway=192.168.1.1
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 interface=VLAN1
/ip dhcp-server network add address=192.168.1.0/24 interface=VLAN1 dhcp-options=option1,option2
```

### Common Pitfalls and Solutions

- **VLANs not communicating:** Ensure that inter-VLAN routing is enabled and that the gateway IP is correct.
- **Devices not receiving IP addresses:** Check that DHCP is enabled on the VLANs and that the devices are connected to the correct VLAN.
- **Internet access issues:** Verify that the default gateway is set correctly for each VLAN.

### Verification and Testing Steps

- Ping between devices in different VLANs to test inter-VLAN communication.
- Verify that devices on each VLAN can access the Internet.
- Check DHCP leases to ensure that devices are receiving IP addresses from the correct VLAN.

### Related Features and Considerations

- Advanced VLAN features: QinQ, MAC-based VLAN assignment
- Layer 3 VLANs for inter-VLAN routing
- Security considerations: VLANs do not provide complete isolation; consider firewall rules for further protection.