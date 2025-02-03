## VLAN Configuration in RouterOS 7.12

### Configuration Scenario and Requirements

* Create multiple Layer 2 VLANs for network segmentation
* Configure inter-VLAN routing
* Implement VLAN tagging for traffic isolation

### Step-by-Step Implementation

#### 1. Create VLANs

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30
```

#### 2. Assign VLANs to Physical Interfaces

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
/interface bridge port add bridge=bridge1 interface=ether3 vlan-id=30
```

#### 3. Configure Inter-VLAN Routing

Create a virtual router to route between VLANs:

```
/routing vrf add name=vrf1
/ip route add distance=100 vrf=vrf1 dst-address=0.0.0.0/0 gateway=192.168.1.1
```

#### 4. Enable VLAN Tagging

```
/interface vlan-id ether1 tag=10
/interface vlan-id ether2 tag=20
/interface vlan-id ether3 tag=30
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10
/interface vlan add name=VLAN20 vlan-id=20
/interface vlan add name=VLAN30 vlan-id=30

/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
/interface bridge port add bridge=bridge1 interface=ether3 vlan-id=30

/routing vrf add name=vrf1
/ip route add distance=100 vrf=vrf1 dst-address=0.0.0.0/0 gateway=192.168.1.1

/interface vlan-id ether1 tag=10
/interface vlan-id ether2 tag=20
/interface vlan-id ether3 tag=30
```

### Common Pitfalls and Solutions

* **Ensure that VLAN tagging is enabled:** If VLAN tagging is not enabled, traffic will not be isolated between VLANs.
* **Verify that the router has sufficient memory:** Creating multiple VLANs can consume a significant amount of memory.
* **Use a consistent VLAN numbering scheme:** This will help with troubleshooting and management.

### Verification and Testing Steps

* **Check interfaces:** Use `/interface print` to verify that VLANs are assigned to the correct interfaces.
* **Test inter-VLAN routing:**

```
/ping 192.168.20.1 vrf=vrf1
/ping 192.168.30.1 vrf=vrf1
```

* **Check VLAN tagging:** Use a protocol analyzer to verify that traffic between VLANs is being tagged correctly.

### Related Features and Considerations

* **Security:** VLANs provide basic network segmentation, but they do not provide complete isolation. Consider using additional security measures such as firewalls and access control lists.
* **Performance:** VLANs can introduce a slight amount of overhead on the network.
* **Management:** Use the RouterOS web interface or CLI to manage VLANs.