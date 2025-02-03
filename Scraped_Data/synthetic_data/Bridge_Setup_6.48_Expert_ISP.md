## Bridge Setup in RouterOS 6.48 (ISP)

### Scenario and Requirements

In an ISP network, we need to set up a bridge to connect multiple customer Ethernet segments to a single upstream provider link.

* Requirements:
    * Multiple Ethernet interfaces on the router
    * Upstream provider connection on a separate interface
    * DHCP server for IP address assignment to customers

### Step-by-Step Implementation

#### 1. Create Bridge Interface

```
/interface bridge add name=ISP-Bridge
```

#### 2. Add Ports to Bridge

```
/interface bridge port add bridge=ISP-Bridge port=ether1
/interface bridge port add bridge=ISP-Bridge port=ether2
/interface bridge port add bridge=ISP-Bridge port=ether3
```

**Note:** Replace `ether1`, `ether2`, and `ether3` with the actual Ethernet interface names.

#### 3. Assign IP Address to Bridge

```
/ip address add address=10.0.0.1/24 interface=ISP-Bridge
```

#### 4. Enable DHCP Server

```
/ip dhcp-server add interface=ISP-Bridge lease-time=3600s address-pool=ISP-Pool name=ISP-DHCP
```

#### 5. Create Address Pool

```
/ip pool add name=ISP-Pool ranges=10.0.0.5-10.0.0.254
```

### Complete Configuration Commands

```
/interface bridge add name=ISP-Bridge
/interface bridge port add bridge=ISP-Bridge port=ether1
/interface bridge port add bridge=ISP-Bridge port=ether2
/interface bridge port add bridge=ISP-Bridge port=ether3
/ip address add address=10.0.0.1/24 interface=ISP-Bridge
/ip dhcp-server add interface=ISP-Bridge lease-time=3600s address-pool=ISP-Pool name=ISP-DHCP
/ip pool add name=ISP-Pool ranges=10.0.0.5-10.0.0.254
```

### Common Pitfalls and Solutions

* **Duplicate MAC Address:** Ensure that the router's MAC address is not already in use by another device on the network. If it is, you may need to change the router's MAC address.
* **Invalid IP Address:** Verify that the IP address assigned to the bridge is not in use by another device on the network.
* **DHCP Server Not Running:** Ensure that the DHCP server is enabled and properly configured.

### Verification and Testing Steps

* Check that the customer devices can obtain IP addresses via DHCP.
* Test connectivity between customer devices on different Ethernet segments.
* Ping the upstream provider gateway from the bridge interface.

### Related Features and Considerations

* **VLAN Bridging:** You can create VLANs on the bridge interface to segment customer traffic further.
* **Port Isolation:** Enable port isolation on the bridge to prevent customers from communicating with each other directly.
* **Firewall Rules:** Apply firewall rules to the bridge interface to control traffic to and from the customer segments.