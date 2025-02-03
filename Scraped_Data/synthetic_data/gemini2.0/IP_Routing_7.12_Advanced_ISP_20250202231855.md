**IP Routing**

**1. Configuration scenario and requirements**

In this scenario, we will configure IP routing on a MikroTik RouterOS 7.12 device to route traffic between different subnets.

**2. Step-by-step implementation**

**Step 1: Configure IP addresses on interfaces**

Assign IP addresses to the physical interfaces connected to different subnets. For example:

```
/interface address add address=192.168.1.254/24 interface=ether1
/interface address add address=192.168.2.254/24 interface=ether2
```

**Step 2: Configure IP routing**

Enable IP routing on the device:

```
/ip routing add disabled=no
```

**Step 3: Create a default route**

Configure a default route to send traffic to a gateway for all destinations not explicitly routed:

```
/ip route add gateway=192.168.1.1
```

**3. Complete configuration commands**

The complete configuration commands for this scenario are:

```
/interface address add address=192.168.1.254/24 interface=ether1
/interface address add address=192.168.2.254/24 interface=ether2
/ip routing add disabled=no
/ip route add gateway=192.168.1.1
```

**4. Common pitfalls and solutions**

- Ensure that the IP addresses assigned to the interfaces are on different subnets.
- Make sure that the gateway specified in the default route is reachable.
- If routing is not working, check the firewall rules to ensure that they are allowing the necessary traffic.

**5. Verification and testing steps**

- Ping hosts on different subnets to verify connectivity.
- Use the `/ip route print` command to check the routing table.

**6. Related features and considerations**

- For more advanced routing scenarios, you can use static routes, policy-based routing, or routing protocols (such as OSPF, BGP, or RIP).
- You can use the `/ip firewall` commands to configure firewall rules to control access to and from the network.

**7. MikroTik REST API examples**

**Get IP routing settings:**

```
GET /rest/routing/ip/settings
```

**Example response:**

```
{
  "comment": null,
  "disabled": false,
  "disable-multipath": false,
  "disable-server-side-fastpath": false,
  "disable-source-validation": false,
  "disable-unicast-routing": false,
  "inbound-interface": null,
  "max-src-addresses": 16000,
  "max-src-addresses-per-interface": 16000,
  "max-src-addrs-per-src-address": 512,
  "preserve-src-mac": false,
  "proxy-arp": disabled
}
```

**Create a static IP route:**

```
POST /rest/routing/ip/route
{
  "comment": "My static route",
  "disabled": false,
  "dst-address": "192.168.3.0/24",
  "gateway": "192.168.2.1",
  "interface": "ether2"
}
```

**Example response:**

```
{
  "id": "4"
}
```