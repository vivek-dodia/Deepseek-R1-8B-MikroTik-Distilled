**IP Routing**

**Configuration Scenario and Requirements**

* Configure IP routing on a MikroTik RouterOS 7.11 device to allow traffic flow between subnets.

**Step-by-Step Implementation**

1. **Configure IP Addresses:** Assign IP addresses to the router interfaces connecting to each subnet.

   ```
   /ip address add address=192.168.10.1/24 interface=ether1
   /ip address add address=192.168.20.1/24 interface=ether2
   ```

2. **Create a Bridge:** Create a bridge to connect the interfaces.

   ```
   /interface bridge add name=br0 add-ports=ether1 ether2
   ```

3. **Enable IP Routing:** Enable IP forwarding on the bridge.

   ```
   /ip firewall filter add action=accept chain=forward
   ```

4. **Add Static Routes:** If necessary, add static routes to the routing table to direct traffic to specific destinations.

   ```
   /ip route add dst-address=192.168.30.0/24 gateway=192.168.10.2
   ```

**Complete Configuration Commands**

```
/ip address add address=192.168.10.1/24 interface=ether1
/ip address add address=192.168.20.1/24 interface=ether2
/interface bridge add name=br0 add-ports=ether1 ether2
/ip firewall filter add action=accept chain=forward
/ip route add dst-address=192.168.30.0/24 gateway=192.168.10.2
```

**Common Pitfalls and Solutions**

* Ensure IP addresses are correctly assigned and subnet masks are appropriate.
* Verify that the bridge is active and forwarding traffic.
* Check that the static routes are correct and pointing to the desired gateways.

**Verification and Testing Steps**

* Ping devices on different subnets.
* Use the "/routing ping" command to trace the route.
* Monitor traffic flow using tools like Wireshark.

**Related Features and Considerations**

* Dynamic routing protocols (e.g., OSPF, RIP, BGP) can be used to automatically update routes.
* Firewall rules can be configured to control traffic flow.
* Quality of Service (QoS) settings can prioritize specific traffic types.

**MikroTik REST API Examples**

**Add IP Address:**

```
API Endpoint: /ip/address/add
Request Method: POST
Example JSON Payload:
```json
{
  "interface": "ether1",
  "address": "192.168.10.1/24"
}
```
**Enable IP Forwarding:**

```
API Endpoint: /ip/firewall/filter/add
Request Method: POST
Example JSON Payload:
```json
{
  "action": "accept",
  "chain": "forward"
}
```
**Expected Response:**

```json
{
  "id": "1"
}
```