## VLAN Configuration in RouterOS 7.11

### Configuration Scenario and Requirements

- Create multiple VLANs on a MikroTik router.
- Assign VLANs to physical ports.
- Configure inter-VLAN routing.

### Step-by-Step Implementation

**1. Create VLANs**

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
```

**2. Assign VLANs to Ports**

```
/interface ethernet set ether1 vlan=VLAN1
/interface ethernet set ether2 vlan=VLAN2
```

**3. Configure Inter-VLAN Routing**

```
/ip route add dst-address=192.168.1.0/24 gateway=192.168.1.254 vlan=VLAN1
/ip route add dst-address=192.168.2.0/24 gateway=192.168.2.254 vlan=VLAN2
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
/interface ethernet set ether1 vlan=VLAN1
/interface ethernet set ether2 vlan=VLAN2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.1.254 vlan=VLAN1
/ip route add dst-address=192.168.2.0/24 gateway=192.168.2.254 vlan=VLAN2
```

### Common Pitfalls and Solutions

- **VLAN IDs not unique:** Ensure that each VLAN has a unique VLAN ID.
- **Ports not assigned to VLANs:** Make sure that all ports involved in VLANs are properly assigned.
- **Incorrect IP routes:** Verify that the IP routes for inter-VLAN traffic are correct.

### Verification and Testing Steps

- Verify the VLAN configuration with the command: ```/interface vlan print```
- Check that ports are assigned to VLANs correctly: ```/interface ethernet print```
- Test inter-VLAN connectivity using ping or traceroute commands.

### Related Features and Considerations

- **VLAN trunking:** Use VLAN trunking to extend VLANs across multiple switches.
- **VLAN security:** Implement VLAN security measures to isolate VLANs and prevent unauthorized access.
- **VLAN management:** Use tools such as VMAN (VLAN Management) to centrally manage and monitor VLAN configurations.