## Bridge Setup in RouterOS 7.11 for ISPs

### Configuration Scenario and Requirements

- Create a bridge to connect multiple Ethernet interfaces into a single layer 2 network.
- Assign IP address and gateway to the bridge interface.
- Enable MAC learning and forwarding on the bridge.
- Allow traffic from specific MAC addresses.
- Configure DHCP server on the bridge interface.

### Step-by-Step Implementation

#### 1. Create Bridge Interface

```
/interface bridge add name=ISP-Bridge
```

#### 2. Add Ports to Bridge

```
/interface bridge port add bridge=ISP-Bridge interface=ether1
/interface bridge port add bridge=ISP-Bridge interface=ether2
```

#### 3. Assign IP Address and Gateway

```
/ip address add address=10.0.0.1/24 interface=ISP-Bridge
/ip route add gateway=10.0.0.254 interface=ISP-Bridge
```

#### 4. Enable MAC Learning and Forwarding

```
/bridge set ISP-Bridge ageing-time=0 mac-learning=yes
```

#### 5. Allow MAC Addresses

```
/bridge host add address=00:00:de:ad:be:ef interface=ISP-Bridge
```

#### 6. Configure DHCP Server

```
/ip dhcp-server add interface=ISP-Bridge name=ISP-DHCP range=10.0.0.100-10.0.0.200 lease-time=24h
```

### Complete Configuration Commands

```
/interface bridge add name=ISP-Bridge
/interface bridge port add bridge=ISP-Bridge interface=ether1
/interface bridge port add bridge=ISP-Bridge interface=ether2
/ip address add address=10.0.0.1/24 interface=ISP-Bridge
/ip route add gateway=10.0.0.254 interface=ISP-Bridge
/bridge set ISP-Bridge ageing-time=0 mac-learning=yes
/bridge host add address=00:00:de:ad:be:ef interface=ISP-Bridge
/ip dhcp-server add interface=ISP-Bridge name=ISP-DHCP range=10.0.0.100-10.0.0.200 lease-time=24h
```

### Common Pitfalls and Solutions

- **MAC address not recognized:** Ensure that MAC learning is enabled on the bridge.
- **IP address conflict:** Verify that the IP address assigned to the bridge is not already in use on the network.
- **DHCP server not responding:** Check if the DHCP server is running and configured correctly.

### Verification and Testing Steps

- **Ping** from devices connected to the bridge to verify connectivity.
- **Check MAC address table** on the bridge to ensure that devices are being learned and forwarded.
- **Test DHCP** by requesting an IP address from the DHCP server.

### Related Features and Considerations

- **VLANs:** Bridges can be configured to separate traffic into different VLANs.
- **Port Isolation:** Bridges can be configured to isolate traffic between different ports, preventing communication within the bridge.
- **Security:** Use firewalls and access control rules to restrict traffic on the bridge interface.