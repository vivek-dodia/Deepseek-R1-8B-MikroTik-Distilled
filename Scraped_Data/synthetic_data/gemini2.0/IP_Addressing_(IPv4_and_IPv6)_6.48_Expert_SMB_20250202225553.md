**IP Addressing (IPv4 and IPv6)**

**Configuration Scenario and Requirements**

* Configure IPv4 and IPv6 addresses on router interfaces
* Assign IP addresses from IP pools
* Enable IP routing and forwarding
* Configure MAC server for MAC address-to-IP address binding
* Monitor network traffic using RoMON

**Step-by-Step Implementation**

**IPv4 and IPv6 Address Configuration**

1. Access the RouterOS console (WinBox, WebFig, or CLI)
2. Navigate to **IP > Addresses**
3. Add IPv4 address: ```command
/ip address add address=192.168.1.1/24 interface=ether1
```
4. Add IPv6 address: ```command
/ipv6 address add address=2001:db8:85a3::8a2e:370:7334 interface=ether1
```

**IP Pools**

1. Navigate to **IP > Pool**
2. Create an IPv4 pool: ```command
/ip pool add name=office-pool range=192.168.1.2-192.168.1.254
```
3. Create an IPv6 pool: ```command
/ipv6 pool add name=office-pool-v6 range=2001:db8:85a3::8a2e:370:7335-2001:db8:85a3::8a2e:370:7434
```

**IP Routing and Forwarding**

1. Enable IP forwarding: ```command
/ip routing add dst-address=0.0.0.0/0 gateway=192.168.1.254
```
2. Add static route for IPv6: ```command
/ipv6 route add dst-address=2001:db8:85a3::/48 gateway=2001:db8:85a3::1
```

**MAC Server**

1. Enable MAC server: ```command
/mac-server enable
```
2. Bind MAC address to IPv4 address: ```command
/mac-server set address=00:11:22:33:44:55 mac-address=00:11:22:33:44:55
```
3. Bind MAC address to IPv6 address: ```command
/ipv6 mac-server set address=2001:db8:85a3::8a2e:370:7334 mac-address=00:11:22:33:44:55
```

**RoMON Monitoring**

1. Open RoMON: ```command
/tool romon
```
2. Monitor IP traffic: ```command
/tool romon interface=ether1
```

**Complete Configuration Commands**

```bash
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8:85a3::8a2e:370:7334 interface=ether1
/ip pool add name=office-pool range=192.168.1.2-192.168.1.254
/ipv6 pool add name=office-pool-v6 range=2001:db8:85a3::8a2e:370:7335-2001:db8:85a3::8a2e:370:7434
/ip routing add dst-address=0.0.0.0/0 gateway=192.168.1.254
/ipv6 route add dst-address=2001:db8:85a3::/48 gateway=2001:db8:85a3::1
/mac-server enable
/mac-server set address=00:11:22:33:44:55 mac-address=00:11:22:33:44:55
/ipv6 mac-server set address=2001:db8:85a3::8a2e:370:7334 mac-address=00:11:22:33:44:55
```

**Common Pitfalls and Solutions**

* **Incorrect subnet mask:** Ensure the subnet mask is correctly configured for the IPv4 and IPv6 addresses.
* **IP address conflict:** Avoid using the same IP address on multiple interfaces or assigning it from an overlapping IP pool.
* **Default gateway not set:** Configure a default gateway for IP routing.
* **MAC address not bound:** Bind the MAC address of the device to the IP address using the MAC server.
* **RoMON not working:** Check the interface name and ensure RoMON is enabled.

**Verification and Testing Steps**

* Use ```command
ping
``` to verify IP address connectivity.
* Check the routing table using ```command
ip route print
```
* Monitor traffic using RoMON (```command
/tool romon
```).
* Test MAC address binding using ```command
arp
```.

**Related Features and Considerations**

* DHCP for automatic IP address assignment
* DNS for name resolution
* NAT for network address translation
* Firewall for access control

**MikroTik REST API Examples**

**Add IPv4 Address**

```bash
API Endpoint: /ip/address
Request Method: POST
Example JSON Payload:
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
Expected Response:
{
  "id": 1
}
```

**Add IPv6 Address**

```bash
API Endpoint: /ipv6/address
Request Method: POST
Example JSON Payload:
{
  "address": "2001:db8:85a3::8a2e:370:7334",
  "interface": "ether1"
}
Expected Response:
{
  "id": 1
}
```

**Add IP Pool**

```bash
API Endpoint: /ip/pool
Request Method: POST
Example JSON Payload:
{
  "name": "office-pool",
  "ranges": [
    {
      "from": "192.168.1.2",
      "to": "192.168.1.254"
    }
  ]
}
Expected Response:
{
  "id": 1
}
```

**Enable MAC Server**

```bash
API Endpoint: /mac-server
Request Method: PUT
Example JSON Payload:
{
  "enabled": true
}
Expected Response:
{}
```