## Bridge Setup in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

- Create a bridge interface to connect multiple physical interfaces and form a Layer 2 broadcast domain.
- Assign IP addresses to the bridge interface for management and connectivity.
- Configure firewall rules to protect the bridged network from external threats.

### Step-by-Step Implementation

**1. Create Bridge Interface**

- Navigate to `Interfaces > Bridge` in the RouterOS web interface.
- Click on the `+` button to create a new bridge.
- Enter a name for the bridge (e.g., "Corporate-Bridge") and leave the other settings as default.

**2. Add Physical Interfaces**

- Select the physical interfaces that need to be bridged.
- In the `Bridge ports` section, click on the `+` button and select the desired interfaces from the drop-down list.

**3. Assign IP Address**

- Assign an IP address to the bridge interface for management and connectivity.
- Navigate to `IP > Addresses` and click on the `+` button.
- Select the bridge interface from the `Interface` drop-down list.
- Enter the desired IP address, subnet mask, and default gateway.

**4. Configure Firewall Rules**

- Create firewall rules to protect the bridged network.
- Navigate to `IP > Firewall > Filter Rules` and click on the `+` button.
- Create a rule to block inbound traffic from external sources to the bridge interface.

```
- Chain: input
- Action: drop
- Interface list: Corporate-Bridge
- Direction: in
```

**5. Enable Bridge Forwarding**

- Ensure that bridging is enabled on the bridge interface.
- Navigate to `Interfaces > Bridge` and select the bridge interface.
- In the `General` tab, verify that the `Forwarding` checkbox is enabled.

### Complete Configuration Commands

```
/interface bridge add name=Corporate-Bridge
/interface bridge port add bridge=Corporate-Bridge interface=ether1
/interface bridge port add bridge=Corporate-Bridge interface=ether2
/ip address add address=192.168.1.1/24 interface=Corporate-Bridge
/ip firewall filter add action=drop in-interface-list=Corporate-Bridge direction=in
/interface bridge set Corporate-Bridge forward=enable
```

### Common Pitfalls and Solutions

**Pitfall:** Loopback traffic on the bridge interface.

**Solution:** Ensure that the bridge interface is not included in any firewall rules that allow loopback traffic.

**Pitfall:** Incorrectly assigned IP addresses.

**Solution:** Verify that the IP address assigned to the bridge interface does not conflict with any other IP addresses on the network.

### Verification and Testing Steps

- Verify that the bridge interface is created and active.
- Check that the physical interfaces are successfully bridged and can communicate with each other.
- Test the firewall rules by attempting to access the bridged network from an external source.

### Related Features and Considerations

- **VLAN Trunking:** Can be used in conjunction with bridges to create multiple logical networks on a single physical interface.
- **Bridge Filtering:** Allows filtering of traffic based on MAC addresses to improve network security.
- **STP (Spanning Tree Protocol):** Prevents bridge loops and ensures network stability.