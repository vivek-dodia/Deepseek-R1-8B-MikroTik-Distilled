## IP Routing

### Configuration Scenario and Requirements

* Configure IP routing on a MikroTik RouterOS 7.11 device to establish connectivity between different subnets within an enterprise network.

### Step-by-Step Implementation

**1. IP Addressing:**

* Assign IP addresses to each subnet interface.

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2
```

**2. IP Routing:**

* Enable IP forwarding on the router.

```
/ip routing
set disabled=no
```

* Add static routes to the routing table.

```
/ip route
add dst-address=192.168.2.0/24 gateway=192.168.1.1
add dst-address=192.168.1.0/24 gateway=192.168.2.1
```

**3. MAC Server:**

* Add MAC addresses to the MAC server to manage and assign IP addresses based on MAC addresses.

```
/ip neighbor
add mac-address=00:11:22:33:44:55 interface=ether1
/ip dhcp-server
lease add mac-address=00:11:22:33:44:55 address=192.168.1.2
```

### Complete Configuration Commands

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2

/ip routing
set disabled=no

/ip route
add dst-address=192.168.2.0/24 gateway=192.168.1.1
add dst-address=192.168.1.0/24 gateway=192.168.2.1

/ip neighbor
add mac-address=00:11:22:33:44:55 interface=ether1

/ip dhcp-server
lease add mac-address=00:11:22:33:44:55 address=192.168.1.2
```

### Common Pitfalls and Solutions

* **Name resolution:** Ensure DNS is properly configured or add host records to the MikroTik device.
* **Interface configuration:** Verify that the interfaces are in the correct state (up) and configured with the correct IP addresses.
* **Firewall rules:** Check if there are any firewall rules blocking traffic.

### Verification and Testing Steps

* Ping between devices on different subnets.
* Use tools like `traceroute` to verify the path taken by packets.
* Monitor the routing table and interface statistics to ensure traffic is flowing as expected.

### Related Features and Considerations

* **Routing Protocols:** Utilize routing protocols such as OSPF or BGP to automate routing configuration and exchange routing information with other routers.
* **DHCP Relay:** Configure DHCP relay to allow devices to obtain IP addresses from a centralized DHCP server.
* **Load Balancing:** Implement load balancing to distribute traffic across multiple internet connections.

### MikroTik REST API Examples

**Get IP Address Configuration:**

```
ENDPOINT: /api/ip/address
REQUEST METHOD: GET
EXPECTED RESPONSE:
```
```json
{
  "address": "192.168.1.1",
  "interface": "ether1",
  "broadcast": "192.168.1.255",
  "network": "192.168.1.0",
  "netmask": "255.255.255.0",
  "gateway": null
}
```

**Add Static Route:**

```
ENDPOINT: /api/ip/route
REQUEST METHOD: POST
REQUEST BODY:
```
```json
{
  "dst-address": "192.168.2.0/24",
  "gateway": "192.168.1.1"
}
```
```
EXPECTED RESPONSE:
```
```json
{
  "comment": null,
  "distance": 1,
  "dst-address": "192.168.2.0/24",
  "gateway": "192.168.1.1",
  "id": 10
}
```

**Add MAC Address to MAC Server:**

```
ENDPOINT: /api/ip/neighbor
REQUEST METHOD: POST
REQUEST BODY:
```
```json
{
  "mac-address": "00:11:22:33:44:55",
  "interface": "ether1",
  "comment": "My MAC Address"
}
```
```
EXPECTED RESPONSE:
```
```json
{
  "address": null,
  "comment": "My MAC Address",
  "interface": "ether1",
  "last-seen": null,
  "mac-address": "00:11:22:33:44:55",
  "timeout": 300
}
```