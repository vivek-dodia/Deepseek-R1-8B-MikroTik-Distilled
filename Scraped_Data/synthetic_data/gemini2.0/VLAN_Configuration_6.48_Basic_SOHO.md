## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

- Configure multiple isolated networks on a single physical switch using VLANs.
- Assign VLAN IDs to network ports.
- Allow communication between VLANs as needed.

### Step-by-Step Implementation

#### Create VLANs

1. Go to **Interfaces** > **VLAN**.
2. Click **+** to create a new VLAN.
3. Enter the VLAN ID (e.g., 10) and click **Apply**.
4. Repeat for other necessary VLANs.

#### Assign VLANs to Ports

1. Go to **Interfaces** > **Switch**.
2. Click on the switch port to be configured.
3. Under **VLAN**, select the desired VLAN from the dropdown.
4. Click **Apply**.

#### Enable Inter-VLAN Routing

1. Go to **IP** > **Routes**.
2. Click **+** to create a new route.
3. Enter a **Gateway** (e.g., router's IP address).
4. Set **Dst. Address** as the VLAN IP subnet (e.g., 10.10.10.0/24).
5. Set **VLAN ID** to the corresponding VLAN ID (e.g., 10).

### Complete Configuration Commands

```
/interface vlan add vlan-id=10
/interface switch vlan-id=10 port=ether1
/ip route add gateway=192.168.1.1 dst-address=10.10.10.0/24 vlan-id=10
```

### Common Pitfalls and Solutions

| Problem | Solution |
|---|---|
| VLAN IDs not consistent | Ensure all ports assigned to a VLAN have the same VLAN ID. |
| No communication between VLANs | Verify that inter-VLAN routing is enabled. |
| Security vulnerabilities | Use strong passwords for VLAN configurations. Consider implementing firewall rules between VLANs. |

### Verification and Testing Steps

- Verify VLAN assignments by using the `/interface switch print` command.
- Test connectivity between VLANs by pinging IP addresses on different VLANs.
- Check the routing table (`/ip route print`) to ensure inter-VLAN routes are present.

### Related Features and Considerations

- Use **VLAN Trunks** to extend VLANs across multiple switches.
- Configure **VLAN Traffic Isolation** to prevent communication between specific VLANs.
- For advanced configurations, consider using **VLAN Filtering** and **VLAN Tagging**.