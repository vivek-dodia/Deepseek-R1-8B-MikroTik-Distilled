**IP Settings**

**1. Configuration Scenario and Requirements**

This section will cover advanced IP settings in MikroTik RouterOS, including IP addressing, IP pools, IP routing, MAC server, and RoMON.

**2. Step-by-Step Implementation**

**IP Addressing**

* Assign an IPv4 address to an interface:

```
/ip address add address=192.168.1.1/24 interface=ether1
```

* Assign an IPv6 address to an interface:

```
/ipv6 address add address=2001:db8:1:1::1/64 interface=ether1
```

**IP Pools**

* Create an IP pool:

```
/ip pool add name=my-pool range=192.168.1.10-192.168.1.20
```

* Assign an IP address from a pool to an interface:

```
/ip address add interface=ether1 pool=my-pool
```

**IP Routing**

* Add a static route:

```
/ip route add destination=192.168.2.0/24 gateway=192.168.1.2
```

* Enable dynamic routing:

```
/ip route add distance=100 routing-mark=ospf protocol=ospf
```

**MAC Server**

* Enable MAC server:

```
/mac-server enable
```

* Add a static MAC-IP binding:

```
/mac-server add mac-address=00:11:22:33:44:55 ip-address=192.168.1.10
```

**RoMON**

* Enable RoMON:

```
/romon enable
```

* Set RoMON password:

```
/romon password set=my-password
```

**3. Complete Configuration Commands**

Refer to the following tables for the complete command syntax and parameters used in the above scenarios:

| Command | Parameters |
|---|---|
| /ip address add | address, interface |
| /ipv6 address add | address, interface |
| /ip pool add | name, range |
| /ip address add | interface, pool |
| /ip route add | destination, gateway, routing-mark, protocol |
| /mac-server enable | no parameters |
| /mac-server add | mac-address, ip-address |
| /romon enable | no parameters |
| /romon password set | password |

**4. Common Pitfalls and Solutions**

* **IP address conflict:** Ensure that the IP addresses assigned to interfaces and IP pools do not conflict.
* **Wrong subnet mask:** Use the appropriate subnet mask when assigning IP addresses.
* **Invalid IP pool range:** The IP pool range should be within the subnet assigned to the interface.
* **MAC-IP binding not working:** Verify that the MAC server is enabled and that the MAC-IP binding is correctly configured.
* **RoMON password not set:** Set a RoMON password to prevent unauthorized access.

**5. Verification and Testing Steps**

* Ping the assigned IP addresses to verify connectivity.
* Use "ip addr" and "ip -6 addr" commands to check IP addresses on interfaces.
* Check the "IP -> Pool" tab in the WebFig to verify IP pools.
* Test static routes using "tracert" or "traceroute" commands.
* Use the "ping mac-address" command to test MAC-IP bindings.
* Access the device via RoMON using the configured password

**6. Related Features and Considerations**

* DHCP server: For automatic IP address assignment.
* DNS server: For name resolution.
* Firewall: To control access to IP resources.
* NAT: To translate IP addresses and port numbers.
* QoS: To prioritize network traffic.

**7. MikroTik REST API Examples**

**Create an IP address:**

**API Endpoint:** `/api/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
```

**Expected Response:**

```
{
  "id": "1"
}
```

**Create an IP pool:**

**API Endpoint:** `/api/ip/pool/add`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "name": "my-pool",
  "range": "192.168.1.10-192.168.1.20"
}
```

**Expected Response:**

```
{
  "id": "1"
}
```

**Add a static route:**

**API Endpoint:** `/api/ip/route/add`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "destination": "192.168.2.0/24",
  "gateway": "192.168.1.2"
}
```

**Expected Response:**

```
{
  "id": "1"
}
```