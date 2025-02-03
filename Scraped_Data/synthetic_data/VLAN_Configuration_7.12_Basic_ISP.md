## VLAN Configuration in MikroTik RouterOS 7.12 for ISPs

### Configuration Scenario and Requirements

- Create multiple VLANs on a MikroTik router to segment and isolate traffic for different customer premises.
- AssignVLAN interfaces to customer-facing ports.
- Implement DHCP and static IP address assignment on each VLAN.

### Step-by-Step Implementation

**1. Create VLANs**

- Navigate to **Interfaces** > **VLAN**
- Click on the **+** button
- Enter the following parameters:
    - **Name:** Name of the VLAN
    - **VID:** VLAN ID (e.g., 10)
- Click **OK**

**2. Assign VLAN Interfaces to Ports**

- Navigate to **Interfaces** > **Ether**
- Select the desired port
- Click on the **VLAN** tab
- Select the created VLAN from the dropdown
- Click **OK**

**3. Configure DHCP**

- Navigate to **IP** > **DHCP Server**
- Click on the **+** button
- Enter the following parameters:
    - **Name:** Name of the DHCP server
    - **Interface:** VLAN interface (e.g., VLAN10)
    - **Address Pool:** Range of IP addresses to be assigned
- Click **OK**

**4. Configure Static IP Address Assignments**

- Navigate to **IP** > **Addresses**
- Click on the **+** button
- Enter the following parameters:
    - **Interface:** VLAN interface (e.g., VLAN10)
    - **Address:** Specific IP address to be assigned
- Click **OK**

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vid=10
/interface vlan add name=VLAN20 vid=20

/interface ethernet set ether2 vlan=VLAN10
/interface ethernet set ether3 vlan=VLAN20

/ip dhcp-server add name=DHCP10 interface=VLAN10 address-pool=10.10.10.0/24
/ip dhcp-server add name=DHCP20 interface=VLAN20 address-pool=10.20.20.0/24

/ip address add address=10.10.10.1/24 interface=VLAN10
/ip address add address=10.20.20.1/24 interface=VLAN20
```

### Common Pitfalls and Solutions

- **VLANs not working:** Ensure that the ports are assigned to the correct VLANs and that the VLANs are created on the router.
- **DHCP not assigning IP addresses:** Check if the DHCP server is enabled and that the address pool is configured correctly.
- **Static IP addresses not assigned:** Verify that the static IP addresses are configured on the correct VLAN interface.

### Verification and Testing Steps

- Use the command `/ip neighbor print detail` to check if clients are obtaining IP addresses from the DHCP server.
- Ping devices on different VLANs to ensure connectivity.

### Related Features and Considerations

- **Security:** Implement access control lists (ACLs) to restrict traffic between different VLANs.
- **Trunking:** Use a trunk port to connect multiple VLANs to a single switch port.
- **VLAN membership:** Use the `/interface vlan membership print` command to view the VLANs assigned to each interface.