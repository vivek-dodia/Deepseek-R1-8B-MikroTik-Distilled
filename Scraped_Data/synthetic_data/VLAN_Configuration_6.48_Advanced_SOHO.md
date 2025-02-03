## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

- Create multiple VLANs for network segmentation
- Assign VLAN IDs to physical ports
- Configure inter-VLAN routing

### Step-by-Step Implementation

**1. Create VLANs**

- Navigate to **IP** > **VLAN**
- Click on the **+** button to create a new VLAN
- **Name:** VLAN1
- **VLAN ID:** 10

- Repeat steps to create additional VLANs (e.g., VLAN2 with VLAN ID 20).

**2. Assign Ports to VLANs**

- Navigate to **Interfaces** > **All**
- Select the desired physical port (e.g., ether1)
- Click on the **VLAN** tab
- **Untagged VLAN:** VLAN1 (10)

- Repeat steps to assign other physical ports to different VLANs.

**3. Configure Inter-VLAN Routing**

- Navigate to **IP** > **Routes**
- Click on the **+** button to create a new route
- **Destination:** 0.0.0.0/0
- **Gateway:** IP address of the router on the VLAN (e.g., 192.168.10.1 for VLAN1)
- **Interface:** VLAN interface (e.g., vlan10)

- Repeat steps to create additional routes for other VLANs.

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=10
/interface vlan add name=VLAN2 vlan-id=20
/interface ethernet vlan add interface=ether1 vlan=vlan10 untagged=yes
/interface ethernet vlan add interface=ether2 vlan=vlan20 untagged=yes
/ip route add gateway=192.168.10.1 interface=vlan10 dst-address=0.0.0.0/0
/ip route add gateway=192.168.20.1 interface=vlan20 dst-address=0.0.0.0/0
```

### Common Pitfalls and Solutions

- **Incorrect VLAN ID:** Ensure that the VLAN IDs used do not conflict with existing network configurations.
- **Mismatched Port Assignments:** Verify that physical ports are assigned to the correct VLANs.
- **No Inter-VLAN Routing:** Ensure that static routes are configured to allow traffic between VLANs.

### Verification and Testing Steps

- Use the `/interface vlan print` command to verify the created VLANs.
- Use the `/interface ethernet vlan print` command to check port assignments.
- Use the `/ip route print` command to confirm that inter-VLAN routes are present.
- Test connectivity between VLANs using ping or traceroute.

### Related Features and Considerations

- **VLAN Trunking:** Use trunking to transport multiple VLANs over a single physical link.
- **Security:** Implement VLANs with appropriate security measures such as firewalls and access control lists.
- **Management VLAN:** Create a dedicated VLAN for management purposes to enhance security and control.