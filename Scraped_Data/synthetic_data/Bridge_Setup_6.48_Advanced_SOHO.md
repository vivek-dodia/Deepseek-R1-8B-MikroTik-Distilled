## Bridge Setup in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

* Create a bridge between two or more physical interfaces.
* Allow devices connected to the bridged ports to communicate with each other.
* Assign IP addresses to the bridge interface for management and connectivity.

### Step-by-Step Implementation

**1. Create the Bridge**

```
/interface bridge add name=my-bridge
```

**2. Add Physical Interfaces to the Bridge**

```
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**3. Configure IP Address for the Bridge**

```
/ip address add address=192.168.1.1/24 interface=my-bridge
```

**4. Enable DHCP Server on the Bridge**

```
/ip dhcp-server add interface=my-bridge address-pool=my-pool range=192.168.1.100-192.168.1.254
```

### Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/ip address add address=192.168.1.1/24 interface=my-bridge
/ip dhcp-server add interface=my-bridge address-pool=my-pool range=192.168.1.100-192.168.1.254
```

### Common Pitfalls and Solutions

* **Interfaces Not Being Added to the Bridge:** Ensure the specified interfaces are enabled and available before adding them to the bridge.
* **IP Address Conflict:** Avoid assigning IP addresses that are already in use on the network.
* **No DHCP Leases:** Verify that the DHCP server is enabled and the address pool is configured correctly.

### Verification and Testing Steps

* Check the bridge status: `/interface bridge print`
* Verify IP address and connectivity: `/ip address print`
* Test DHCP lease assignment: Connect a device to the bridge and run `ipconfig` (or similar command) to check for an assigned IP address.

### Related Features and Considerations

* **VLANs:** Bridges can be used to segment traffic into virtual LANs (VLANs) using VLAN tags.
* **STP (Spanning Tree Protocol):** Enable STP to prevent bridging loops and ensure network stability.
* **Security:** Consider using firewall rules to restrict access to and from the bridged network.