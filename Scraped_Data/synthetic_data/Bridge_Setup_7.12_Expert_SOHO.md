## Bridge Setup in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

- Create a bridge interface to connect multiple physical interfaces.
- Configure the bridge to forward traffic between the connected interfaces.
- Assign IP addresses to the bridge interface for management purposes.

### Step-by-Step Implementation

**1. Create the Bridge Interface**

```
/interface bridge add name=my-bridge
```

**2. Add Physical Interfaces to the Bridge**

```
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**3. Enable Bridging**

```
/interface bridge settings set bridge=my-bridge forwarding=yes
```

**4. Assign IP Addresses to the Bridge**

```
/ip address add address=192.168.1.1/24 interface=my-bridge
```

**5. Configure DHCP Server (Optional)**

To provide IP addresses to devices connected to the bridge, you can configure a DHCP server:

```
/ip dhcp-server add interface=my-bridge address-pool=my-pool lease-time=86400
/ip dhcp-pool add name=my-pool ranges=192.168.1.10-192.168.1.254
```

### Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/interface bridge settings set bridge=my-bridge forwarding=yes
/ip address add address=192.168.1.1/24 interface=my-bridge
/ip dhcp-server add interface=my-bridge address-pool=my-pool lease-time=86400
/ip dhcp-pool add name=my-pool ranges=192.168.1.10-192.168.1.254
```

### Common Pitfalls and Solutions

- **Looping and Redundancy:** Ensure that there are no direct or indirect physical connections between the ports assigned to the bridge, as this can create a loop and cause network issues.
- **VLAN Conflicts:** If the interfaces being bridged belong to different VLANs, ensure that the bridge is configured to pass all VLANs by setting `vlan-filtering=no` in `/interface bridge settings`.
- **IP Conflict:** If multiple IP addresses are assigned to the bridge interface, remove the duplicate IP addresses using `/ip address remove address=<IP address> interface=my-bridge`.

### Verification and Testing Steps

- Verify the bridge interface is created and running:

```
/interface bridge print
```

- Check that the ports are added to the bridge:

```
/interface bridge port print where bridge=my-bridge
```

- Test connectivity between devices connected to the bridge:

```
ping <destination IP address>
```

### Related Features and Considerations

- **VLAN Bridging:** RouterOS supports bridging between VLANs, allowing you to create isolated networks on the same physical network.
- **Security:** Consider applying firewall rules and access policies to the bridge interface to protect against unauthorized access.
- **Bonding:** You can combine multiple physical interfaces into a single logical interface using bonding, increasing bandwidth and redundancy.