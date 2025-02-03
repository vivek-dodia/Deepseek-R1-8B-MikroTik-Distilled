## Bridge Setup in RouterOS 7.11 (Expert)

### Configuration Scenario and Requirements

- Establish a bridge interface to connect multiple physical ports and create a single logical network.
- Assign a static IP address and subnet mask to the bridge interface.
- Configure firewall rules to restrict access to the bridge network.

### Step-by-Step Implementation

**1. Create a Bridge Interface**

```
/interface bridge add name=my-bridge
```

**2. Add Ports to the Bridge**

```
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**3. Assign IP Address to the Bridge**

```
/ip address add address=192.168.1.1/24 interface=my-bridge
```

**4. Configure Firewall Rules**

```
/ip firewall filter add chain=input action=accept src-address-list=allowed-ips
/ip firewall filter add chain=forward action=drop
/ip firewall filter add chain=output action=accept
```

**5. Create Address List for Allowed IPs**

```
/ip firewall address-list add address=192.168.1.0/24 name=allowed-ips
```

### Common Pitfalls and Solutions

- **Ensure ports are in the correct mode:** Verify that the ports added to the bridge are configured in bridge mode using `/interface ethernet switch port set <port-name> switch-mode=bridge`.
- **Avoid IP address conflicts:** Check that the IP address assigned to the bridge does not conflict with other interfaces on the router or network.
- **Firewall rules not configured properly:** Ensure that the firewall rules are applied to the correct chain and that the allowed address list is created correctly.

### Verification and Testing Steps

- Ping the bridge interface from another device on the network to verify connectivity.
- Use `ip neighbor print` to check if IP addresses are being assigned correctly.
- Test firewall rules by attempting to access the bridge network from a restricted IP address.

### Related Features and Considerations

- **VLANs:** Bridges can be used to segment traffic on different VLANs.
- **Port Security:** Configuring port security on bridge ports can enhance network security by restricting MAC addresses allowed to access the network.
- **STP (Spanning Tree Protocol):** Bridges can be configured to participate in STP to prevent network loops.