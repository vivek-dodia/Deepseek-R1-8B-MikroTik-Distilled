## Bridge Setup in RouterOS 7.12

### Configuration Scenario and Requirements

* Create a bridge as the primary interface for multiple physical ports.
* Assign IP addresses to the bridge interface and configure DHCP for connected clients.

### Step-by-Step Implementation

#### 1. Create the Bridge

```
/interface bridge add name=br0
```

#### 2. Add Ports to the Bridge

```
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
```

#### 3. Assign an IP Address to the Bridge

```
/ip address add address=192.168.1.1/24 interface=br0
```

#### 4. Enable DHCP Server on the Bridge

```
/ip dhcp-server enable server=dhcp-server interface=br0 subnet=192.168.1.0/24 lease-time=default
```

### Complete Configuration Commands

```
/interface bridge add name=br0
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
/ip address add address=192.168.1.1/24 interface=br0
/ip dhcp-server enable server=dhcp-server interface=br0 subnet=192.168.1.0/24 lease-time=default
```

### Common Pitfalls and Solutions

* **Ports not added correctly to the bridge:** Check if the ports are physically connected and if the correct interface names are used.
* **IP address not assigned:** Ensure that the bridge interface is correctly created and has an IP address.
* **DHCP server not started:** Verify that the DHCP server is enabled and has the correct interface and subnet settings.

### Verification and Testing Steps

* **Ping the bridge IP address:** From another device connected to the bridge, ping the bridge's IP address to test connectivity.
* **Connect a client to the bridge:** Assign an IP address to a client connected to one of the bridge ports and verify internet connectivity.
* **Run a DHCP lease check:** Use the `/ip dhcp-server lease print` command to confirm that DHCP leases are being issued correctly.

### Related Features and Considerations

* **VLANs:** Bridges can be used to segment VLANs within a network.
* **Multi-WAN failover:** Bridges can be used to create load-balancing and failover configurations for multiple WAN connections.
* **Security:** Ensure that the bridge is configured with appropriate firewall rules and security measures, such as MAC filtering.

**Note:** The provided configuration commands are for RouterOS 7.12. For other RouterOS versions, refer to the official documentation.