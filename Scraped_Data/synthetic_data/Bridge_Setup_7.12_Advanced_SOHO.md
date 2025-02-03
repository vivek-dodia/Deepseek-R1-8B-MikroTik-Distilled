## Bridge Setup in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

- Create a bridge interface to connect multiple Ethernet interfaces and allow communication between devices on those interfaces.
- Configure MAC address filtering to restrict access to the bridge.
- Set up IP addressing for the bridge interface.

### Step-by-Step Implementation

**1. Create Bridge Interface**

- Go to **Interfaces** -> **Wireless** -> **Bridge**
- Click **Add** to create a new bridge interface.
- Enter a **Name** for the bridge, e.g., "br0".
- Select the **Master** interface, which will act as the primary interface for the bridge.
- Click **Apply**.

**2. Add Interfaces to Bridge**

- Select the **Bridge** tab.
- Click **+** to add interfaces to the bridge.
- Select the **Member** interfaces from the list.
- Click **OK**.

**3. Configure MAC Address Filtering**

- Go to **IP** -> **Firewall** -> **MAC Filter**
- Click **Add** to create a new MAC filter rule.
- In the **Chain** field, select **bridge-local**.
- In the **Action** field, select **accept**.
- In the **Src. Address** field, enter the MAC address to allow.
- Click **Apply**.

**4. Set Up IP Addressing**

- Go to **IP** -> **Addresses**
- Click **Add** to assign an IP address to the bridge interface.
- Enter the **Address** and **/Prefix** in CIDR notation.
- Select the **Interface** as the bridge name, e.g., "br0".
- Click **Apply**.

### Complete Configuration Commands

```
/interface bridge add name=br0
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
/ip firewall mac-filter add chain=bridge-local action=accept src-address=00:11:22:33:44:55
/ip address add address=192.168.1.1/24 interface=br0
```

### Common Pitfalls and Solutions

- **Bridge Master Interface:** Ensure the selected master interface is connected and active.
- **MAC Filter:** Check the MAC addresses allowed on the bridge to prevent unauthorized access.
- **Loopback:** Avoid connecting a bridge port to itself, as this can create a loop and network instability.

### Verification and Testing Steps

- Check the bridge interface status by going to **Interfaces** -> **Bridge**.
- Test connectivity between devices on the bridged interfaces using ping or traceroute.
- Verify IP connectivity by testing the bridge IP address.

### Related Features and Considerations

- **Bridge VLANs:** Create virtual LANs within a bridge to isolate traffic between different groups of devices.
- **Port Isolation:** Prevent direct communication between devices connected to different ports on the bridge.
- **Security:** Implement proper firewall rules and MAC address filtering to protect the bridged network from unauthorized access.