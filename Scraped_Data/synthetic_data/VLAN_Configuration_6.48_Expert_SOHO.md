## VLAN Configuration in MikroTik RouterOS

### Configuration Scenario and Requirements

- Create multiple VLANs on a single physical interface
- Assign IP addresses and configure routing between VLANs

### Step-by-Step Implementation

#### Creating VLANs

```
/interface vlan add name=vlan10 interface=ether1 vlan-id=10
/interface vlan add name=vlan20 interface=ether1 vlan-id=20
/interface vlan add name=vlan30 interface=ether1 vlan-id=30
```

#### Assigning IP Addresses

```
/ip address add address=192.168.10.1/24 interface=vlan10
/ip address add address=192.168.20.1/24 interface=vlan20
/ip address add address=192.168.30.1/24 interface=vlan30
```

#### Configuring Routing

```
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.254 interface=vlan10
/ip route add dst-address=192.168.30.0/24 gateway=192.168.10.254 interface=vlan10
/ip route add dst-address=192.168.10.0/24 gateway=192.168.20.254 interface=vlan20
/ip route add dst-address=192.168.30.0/24 gateway=192.168.20.254 interface=vlan20
/ip route add dst-address=192.168.10.0/24 gateway=192.168.30.254 interface=vlan30
/ip route add dst-address=192.168.20.0/24 gateway=192.168.30.254 interface=vlan30
```

### Complete Configuration Commands

```
/interface vlan add name=vlan10 interface=ether1 vlan-id=10
/interface vlan add name=vlan20 interface=ether1 vlan-id=20
/interface vlan add name=vlan30 interface=ether1 vlan-id=30

/ip address add address=192.168.10.1/24 interface=vlan10
/ip address add address=192.168.20.1/24 interface=vlan20
/ip address add address=192.168.30.1/24 interface=vlan30

/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.254 interface=vlan10
/ip route add dst-address=192.168.30.0/24 gateway=192.168.10.254 interface=vlan10
/ip route add dst-address=192.168.10.0/24 gateway=192.168.20.254 interface=vlan20
/ip route add dst-address=192.168.30.0/24 gateway=192.168.20.254 interface=vlan20
/ip route add dst-address=192.168.10.0/24 gateway=192.168.30.254 interface=vlan30
/ip route add dst-address=192.168.20.0/24 gateway=192.168.30.254 interface=vlan30
```

### Common Pitfalls and Solutions

- **Incorrect VLAN ID:** Ensure that the VLAN IDs assigned to each interface are unique.
- **Routing Misconfiguration:** Verify that the IP routes are configured correctly for each VLAN.
- **VLAN Tags:** If using tagged VLANs, ensure that the switch is configured to pass the appropriate VLAN tags.

### Verification and Testing Steps

1. Check the VLAN interfaces using `/interface vlan print`.
2. Verify IP addresses using `/ip address print`.
3. Test connectivity between VLANs using `ping`.

### Related Features and Considerations

- **VLAN Filtering:** Use `/interface vlan filter` to restrict traffic between VLANs.
- **VLAN Trunks:** Connect multiple switches using a trunk port to allow VLAN traffic to pass between them.
- **Security:** VLANs can enhance network security by isolating different types of traffic.