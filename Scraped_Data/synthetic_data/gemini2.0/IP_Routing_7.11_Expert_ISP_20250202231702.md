## IP Routing

### Prerequisites

- RouterOS 7.11 (or higher)
- Expert configuration level
- ISP network scale

### Configuration

1. **Enable IP forwarding:**

```
/ip firewall filter add action=accept chain=forward
```

2. **Configure a static route:**

```
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.1
```

3. **Configure a default route:**

```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

4. **Configure BGP routing:**

```
/routing bgp instance add name=my-bgp-instance
/routing bgp peer add instance=my-bgp-instance remote-address=192.168.1.1
```

### Common Pitfalls and Solutions

- **IP forwarding not enabled:** Ensure that IP forwarding is enabled in the firewall.
- **Incorrect subnet mask:** Verify that the subnet mask is correct for the specified destination address.
- **Gateway not reachable:** Check if the gateway IP address is reachable and on the same network as the router.
- **BGP peer misconfiguration:** Ensure that the BGP peer configuration matches the remote router's settings.

### Verification and Testing

- **Use the `ping` command:** Test connectivity to different destinations to verify routing functionality.
- **Check the routing table:** Use `/ip route print` to view the current routing table and confirm the desired routes.
- **Monitor BGP peers:** Use `/routing bgp peer print` to check the status of BGP peers and ensure they are established.

### Related Features and Considerations

- **Policy routing:** Use `/ip route add routing-mark=` to apply specific routing rules based on packet properties.
- **Virtual routing and forwarding (VRF):** Create multiple virtual routers within a single physical router to isolate traffic.
- **Multicast routing:** Configure multicast routing protocols such as IGMP snooping and PIM to handle multicast traffic.

### MikroTik REST API Examples

**Get current IP routing table:**

```
GET /interface/ip/route
```

**Add a static route:**

```
POST /interface/ip/route
{
  "dst-address": "10.0.0.0/24",
  "gateway": "192.168.1.1"
}
```

**Delete a static route:**

```
DELETE /interface/ip/route
?dst-address=10.0.0.0/24
```

**Add a BGP peering:**

```
POST /routing/bgp/peer
{
  "instance": "my-bgp-instance",
  "remote-address": "192.168.1.1"
}
```