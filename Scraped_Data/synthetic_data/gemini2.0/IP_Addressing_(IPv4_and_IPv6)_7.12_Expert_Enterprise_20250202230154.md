**IP Addressing (IPv4 and IPv6)**

**1. Configuration Scenario and Requirements**

- Configure IPv4 and IPv6 addressing on a RouterOS device.
- Enable DHCP server for IPv4 and IPv6.
- Configure static IP addresses for specific devices.
- Implement IPv6 privacy extensions.

**2. Step-by-Step Implementation**

**2.1 IP Addressing**

a. Configure IPv4 address on the router's interface:
```
/ip address add address=<IPv4_address> interface=<interface>
```

b. Configure IPv6 address on the router's interface:
```
/ipv6 address add address=<IPv6_address> interface=<interface>
```

**2.2 DHCP Server**

a. Enable IPv4 DHCP server:
```
/ip dhcp-server enable
```

b. Configure IPv4 DHCP pool:
```
/ip pool add name=<pool_name> ranges=<IP_range1>,<IP_range2>,...
```

c. Enable IPv6 DHCP server:
```
/ipv6 dhcp-server enable
```

d. Configure IPv6 DHCP pool:
```
/ipv6 pool add name=<pool_name> prefixes=<prefix1>/<length>,<prefix2>/<length>,...
```

**2.3 Static IP Addresses**

Assign static IPv4 address to a device:
```
/ip address add address=<IPv4_address> interface=<interface> disabled=no
```

Assign static IPv6 address to a device:
```
/ipv6 address add address=<IPv6_address> interface=<interface> disabled=no
```

**2.4 IPv6 Privacy Extensions**

Enable privacy extensions:
```
/ipv6 address add address=<IPv6_address> interface=<interface> privacy=strong
```

**3. Complete Configuration Commands**

Refer to Step 2 for complete configuration commands.

**4. Common Pitfalls and Solutions**

- Check if the correct interface is selected for IP addressing.
- Ensure proper subnet masking and prefix lengths are used.
- Verify that the DHCP pools and ranges are configured correctly.
- Check if privacy extensions are supported on the client devices.
- In case of IPv6 addressing issues, use the "ipv6 address find" command to identify potential conflicts.

**5. Verification and Testing Steps**

- Use "/ip address print" and "/ipv6 address print" commands to verify IP addresses.
- Test DHCP server functionality by connecting devices to the network.
- Verify that static IP addresses are assigned correctly.
- Perform IPv6 privacy extension tests using tools like "radvdump" or "tcpdump".

**6. Related Features and Considerations**

- DHCP relay for forwarding DHCP requests to multiple servers.
- IPv6 Neighbor Discovery Protocol (NDP) for automatic address assignment.
- Router Advertisements (RAs) to configure IPv6 clients.
- Firewall rules to control IP traffic based on address.

**7. MikroTik REST API Examples**

**7.1 Get IP Address**

**Endpoint:** "/ip/address/get"
**Request Method:** GET
**Example JSON Payload:**
```
{
  ".proplist": "address,interface"
}
```
**Expected Response:**
```
[
  {
    ".id": ".id.52F690DB8C34E437",
    "address": "192.168.1.1",
    "interface": "LAN"
  }
]
```

**7.2 Add IPv6 Static IP Address**

**Endpoint:** "/ipv6/address/add"
**Request Method:** POST
**Example JSON Payload:**
```
{
  "address": "2001:db8::1/64",
  "interface": "WAN"
}
```

**8. IP Pools**

**8.1 IP Pool Types**

RouterOS supports the following IP pool types:
- DHCPv4
- DHCPv6
- Static
- RADIUS

**8.2 DHCP Pool Configuration**

**8.2.1 DHCP Server:**
- Enable server: "/ip dhcp-server enable"
- Configure pool: "/ip pool add name=<pool_name> ranges=<range1>,<range2>,..."

**8.2.2 DHCPv6 Server:**
- Enable server: "/ipv6 dhcp-server enable"
- Configure pool: "/ipv6 pool add name=<pool_name> prefixes=<prefix1>/<length>,<prefix2>/<length>,..."

**8.3 Static Pool Configuration**

Create static IP pool:
```
/ip pool add name=<pool_name> type=static addresses=<ip1>,<ip2>,...
```

**8.4 RADIUS Pool Configuration**

- Enable RADIUS authentication: "/ip dhcp-server set use-radius=yes"
- Configure RADIUS server: "/radius add server=<radius_server> secret=<radius_secret>"
- Create RADIUS pool: "/ip pool add name=<pool_name> type=radius radius-server=<radius_server>"

**8.5 Common Pitfalls and Solutions**

- Ensure valid IP ranges and prefixes are used.
- Check RADIUS server settings and connectivity.
- Verify that the DHCP server is active and listening on the correct interface.

**9. IP Routing**

**9.1 Routing Protocols**

RouterOS supports various routing protocols, including:
- OSPF
- RIP
- BGP
- EIGRP
- Static

**9.2 Static Routes**

Add static route:
```
/ip route add dst-address=<destination> gateway=<gateway>
```

**9.3 BGP Configuration**

- Enable BGP: "/routing bgp enable"
- Configure AS and router ID: "/routing bgp router-id=<router_id> as=<as>"
- Add neighbors: "/routing bgp peer add address=<neighbor_address>"

**10. IP Settings**

**10.1 Firewall**

Enable firewall: "/ip firewall enable"
Add firewall rule:
```
/ip firewall filter add action=accept chain=forward src-address=<source_ip> dst-address=<destination_ip>
```

**10.2 NAT**

Enable NAT: "/ip firewall nat enable"
Add NAT rule:
```
/ip firewall nat add action=masquerade chain=srcnat out-interface=<interface>
```

**10.3 Proxy**

Configure proxy settings:
```
/ip proxy set port=<proxy_port> enable=yes
/proxy set address=<proxy_address>
```

**10.4 Common Pitfalls and Solutions**

- Incorrect firewall rules can block traffic.
- NAT rules should match the traffic direction.
- Proxy settings need to be adjusted based on the proxy server's capabilities.