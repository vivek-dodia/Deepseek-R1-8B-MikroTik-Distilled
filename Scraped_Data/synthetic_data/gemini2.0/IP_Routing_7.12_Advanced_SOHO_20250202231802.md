## IP Routing

### Configuration Scenario and Requirements

* Configure a MikroTik RouterOS 7.12 router to route traffic between two subnets.
* Subnet 1: 10.0.0.0/24
* Subnet 2: 192.168.1.0/24
* The router has two Ethernet interfaces:
    * eth1 connected to Subnet 1
    * eth2 connected to Subnet 2

### Step-by-Step Implementation

1. **Configure IP Addresses**

   Assign IP addresses to the router's interfaces:
   
   ```
   /ip address add address=10.0.0.1/24 interface=eth1
   /ip address add address=192.168.1.1/24 interface=eth2
   ```

2. **Enable IPv4 Forwarding**

   Enable IP forwarding on the router:
   
   ```
   /ip firewall filter add action=accept chain=forward
   ```

3. **Create a Static Route**

   Create a static route to forward traffic from one subnet to the other:
   
   ```
   /ip route add gateway=192.168.1.1 dst-address=10.0.0.0/24
   /ip route add gateway=10.0.0.1 dst-address=192.168.1.0/24
   ```

### Complete Configuration Commands

```
/ip address add address=10.0.0.1/24 interface=eth1
/ip address add address=192.168.1.1/24 interface=eth2
/ip firewall filter add action=accept chain=forward
/ip route add gateway=192.168.1.1 dst-address=10.0.0.0/24
/ip route add gateway=10.0.0.1 dst-address=192.168.1.0/24
```

### Common Pitfalls and Solutions

* **Incorrect IP Addresses:** Ensure the IP addresses assigned to the interfaces are correct and match the subnets they are connected to.
* **Disabled Forwarding:** Verify that IPv4 forwarding is enabled in the firewall configuration.
* **Overlapping Routes:** Avoid creating overlapping static routes, as they can result in incorrect routing.

### Verification and Testing Steps

* Ping from one subnet to the other to verify connectivity.
* Check the routing table to ensure the static routes have been added correctly.

### Related Features and Considerations

* **Dynamic Routing Protocols:** For more advanced routing scenarios, consider using dynamic routing protocols such as OSPF or BGP.
* **NAT (Network Address Translation):** Implement NAT to allow traffic between devices on different subnets with incompatible IP ranges.
* **Policy Routing:** Create policies to route traffic based on specific criteria, such as IP address or protocol.

### MikroTik REST API Examples

#### **API Endpoint:** `/ip/route/add`

#### **Request Method:** POST

#### **Example JSON Payload:**

```
{
  "dst-address": "10.0.0.0/24",
  "gateway": "192.168.1.1"
}
```

#### **Expected Response:**

```
{
  "success": true,
  "message": "Static route added"
}
```