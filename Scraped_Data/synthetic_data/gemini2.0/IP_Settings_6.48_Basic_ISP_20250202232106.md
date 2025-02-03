**IP Settings**

**Configuration Scenario and Requirements**

This documentation covers IP settings in MikroTik RouterOS 6.48 for ISP networks. It focuses on basic configuration, addressing, routing, and related features to provide reliable and scalable IP services to end-users.

**Step-by-Step Implementation**

**1. IP Addressing**

* Assign an IP address to each network interface using the `/ip address` command:

```
/ip address add address=192.168.1.1/24 interface=ether1
```

* Configure multiple IP addresses on an interface using `/ip address add additional-address`:

```
/ip address add additional-address=192.168.2.1/24 interface=ether1
```

* Enable or disable IP forwarding to route traffic between interfaces:

```
/ip firewall filter add action=accept chain=forward
```

**2. IP Pools**

* Create an IP pool to assign dynamic IP addresses:

```
/ip pool add name=pool-dhcp range=192.168.1.20-192.168.1.200
```

* Set the pool as the DHCP server:

```
/ip dhcp-server add address-pool=pool-dhcp interface=ether1
```

**3. IP Routing**

* Set a default gateway for outgoing traffic:

```
/ip route add gateway=192.168.1.254
```

* Add static routes for specific destinations:

```
/ip route add distance=1 gateway=192.168.2.1 dst-address=192.168.2.0/24
```

* Enable dynamic routing protocols (e.g., OSPF, BGP) to exchange routing information with neighboring devices.

**4. IP Settings**

* Configure IP settings such as MTU size, MSS clamping, and TCP keepalive:

```
/ip settings set mtu=1500 mss=1452 tcp-keepalive=yes
```

* Enable or disable ICMP redirects to inform hosts of better routes:

```
/ip settings set icmp-redirect=yes
```

**Common Pitfalls and Solutions**

* **IP address conflicts:** Ensure that all IP addresses on the network are unique.
* **Incorrect subnet mask:** Make sure the subnet mask is appropriate for the network size.
* **Disabled IP forwarding:** Verify that IP forwarding is enabled to allow traffic to be routed.
* **Misconfigured DHCP server:** Check that the DHCP server is correctly configured and that the pool is assigned to the desired interface.

**Verification and Testing Steps**

* Test IP connectivity using `ping` and `traceroute`.
* Check IP addresses and routing tables to verify correctness.
* Configure a DHCP client on a host device to obtain an IP address from the pool.
* Use packet sniffers to monitor network traffic and identify any issues.

**Related Features and Considerations**

* **DNS:** Configure DNS settings to provide name resolution for hosts.
* **Firewall:** Implement firewall rules to filter traffic and protect the network.
* **QoS:** Configure Quality of Service (QoS) rules to prioritize traffic based on application or protocol.

**MikroTik REST API Examples**

**Get IP Address for an Interface**

* **Endpoint:** `/ip/address/print`
* **Request Method:** `GET`
* **Example Payload:** N/A
* **Expected Response:**

```json
[
  {
    ".id": "1",
    "address": "192.168.1.1/24",
    "anycast": false,
    "comment": null,
    "disabled": false,
    "dhcp": false,
    "dynamic": false,
    "interface": "ether1",
    "ipv6": false,
    "network": "192.168.1.0",
    "prefix-length": 24
  }
]
```

**Add an IP Pool**

* **Endpoint:** `/ip/pool`
* **Request Method:** `POST`
* **Example Payload:**

```json
{
  "name": "pool1",
  "ranges": [
    {
      "start": "10.0.0.10",
      "end": "10.0.0.20"
    }
  ]
}
```

* **Expected Response:**

```json
{
  ".id": "1",
  "comment": null,
  "disabled": false,
  "name": "pool1",
  "ranges": [
    {
      "end": "10.0.0.20",
      "start": "10.0.0.10"
    }
  ]
}
```