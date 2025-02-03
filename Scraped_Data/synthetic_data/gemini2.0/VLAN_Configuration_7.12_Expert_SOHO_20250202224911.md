## **VLAN Configuration on MikroTik RouterOS 7.12**

### **Scenario and Requirements**

* Create multiple VLANs to segment the network and isolate traffic.
* Configure interfaces to be members of specific VLANs.
* Allow communication between VLANs through a router interface.

### **Step-by-Step Implementation**

**1. Create VLANs**

```
/interface vlan add name=VLAN1 id=10
/interface vlan add name=VLAN2 id=20
```

**2. Assign Interfaces to VLANs**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
```

**3. Enable Inter-VLAN Routing**

```
/ip routing add dst-address=10.0.10.0/24 gateway=10.0.0.1
/ip routing add dst-address=10.0.20.0/24 gateway=10.0.0.1
```

**4. Configure Router Interface for Inter-VLAN Communication**

```
/interface bridge add name=bridge2
/interface bridge port add bridge=bridge2 interface=ether3
/ip address add address=10.0.0.1/24 interface=bridge2
```

### **Complete Configuration Commands**

```
/interface vlan add name=VLAN1 id=10
/interface vlan add name=VLAN2 id=20
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=10
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=20
/ip routing add dst-address=10.0.10.0/24 gateway=10.0.0.1
/ip routing add dst-address=10.0.20.0/24 gateway=10.0.0.1
/interface bridge add name=bridge2
/interface bridge port add bridge=bridge2 interface=ether3
/ip address add address=10.0.0.1/24 interface=bridge2
```

### **Common Pitfalls and Solutions**

* **Incorrect VLAN ID:** Ensure that the VLAN ID specified in the configuration matches the ID assigned to the VLAN in the switch.
* **Multiple Default Gateways:** Avoid creating multiple default gateways on the same interface, as this can lead to routing issues.
* **VLAN Hopping:** Implement VLAN hopping prevention mechanisms to prevent unauthorized devices from accessing other VLANs.

### **Verification and Testing Steps**

* **Ping between VLANs:** Test connectivity between devices on different VLANs to verify if inter-VLAN communication is established.
* **VLAN Membership:** Check the VLAN membership of interfaces using `/interface bridge port print` to ensure correct configuration.
* **Route Table:** Verify that the route table contains entries for the inter-VLAN subnets.

### **Related Features and Considerations**

* **Port Isolation:** Enable port isolation on VLAN-member ports to prevent communication between devices on the same VLAN.
* **DHCP Server:** Configure DHCP servers on each VLAN to provide IP addressing for devices connected to that VLAN.
* **Security**: Implement security measures such as firewall rules and ACLs to restrict access to VLANs and protect network resources.

### **MikroTik REST API Example**

**API Endpoint:** `/interface/vlan`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "name": "VLAN1",
  "id": 10
}
```

**Expected Response:**

```
{
  "interface": "vlan10"
}
```