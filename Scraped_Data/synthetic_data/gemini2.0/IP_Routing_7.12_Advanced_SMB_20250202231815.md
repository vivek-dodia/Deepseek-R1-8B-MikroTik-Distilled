## IP Routing

**1. Configuration Scenario and Requirements**

- Configure IP routing on a MikroTik RouterOS device to route traffic between multiple subnets.
- Use static routes and a default gateway.

**2. Step-by-Step Implementation**

**2.1 IP Addressing**

Assign IP addresses to the interfaces on the device:

```console
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
```

**2.2 Static Routes**

Add static routes to direct traffic to specific subnets:

```console
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
/ip route add dst-address=172.16.0.0/24 gateway=192.168.2.2
```

**2.3 Default Gateway**

Set the default gateway to route traffic to a gateway device:

```console
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.2
```

**3. Complete Configuration Commands**

```console
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
/ip route add dst-address=172.16.0.0/24 gateway=192.168.2.2
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.2
```

**4. Common Pitfalls and Solutions**

- **Incorrect IP addresses:** Ensure that the IP addresses assigned to interfaces and static routes are correct.
- **Conflicting routes:** Avoid adding multiple routes to the same destination with different gateways.
- **Gateway not reachable:** Verify that the gateway device is reachable and has the appropriate routes configured.

**5. Verification and Testing Steps**

- Ping the destination subnets to confirm that traffic is routed correctly.
- Use the "/ip route print" command to display the current routing table and verify the routes.

## Related Features and Considerations

- Use RIP or OSPF routing protocols for dynamic routing.
- Enable packet forwarding to allow traffic to pass through the device.
- Consider using firewall rules to restrict or filter traffic based on IP addresses and ports.

## MikroTik REST API Examples

**Create a static route:**

**Endpoint:** `/routing/ip/route`

**Request Method:** POST

**JSON Payload:**

```json
{
  "dst-address": "10.0.0.0/24",
  "gateway": "192.168.1.2"
}
```

**Expected Response:**

```json
{
  "id": "1"
}
```

**Get all IP routes:**

**Endpoint:** `/routing/ip/route`

**Request Method:** GET

**Expected Response:**

```json
[
  {
    "id": "1",
    "dst-address": "10.0.0.0/24",
    "gateway": "192.168.1.2"
  }
]
```

**Note:** Refer to the MikroTik REST API documentation for more advanced IP routing operations.