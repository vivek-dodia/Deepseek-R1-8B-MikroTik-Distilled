## IP Settings

### Configuration Scenario and Requirements

This section provides information on configuring IP addressing, including IPv4 and IPv6, and related IP settings.

### Step-by-Step Implementation

#### IP Addressing

1. Address an interface with an IPv4 address:
   ```
   /ip address add address=192.168.1.1/24 interface=ether1
   ```

2. Assign an IPv6 address using EUI-64 (link-local):
   ```
   /ip address add address=fe80::1 interface=ether1
   ```

#### IP Pools

1. Create an IPv4 pool:
   ```
   /ip pool add name=my-pool ranges=192.168.1.10-192.168.1.20
   ```

2. Lease an IP address from the pool to an interface:
   ```
   /ip address add pool=my-pool interface=ether2
   ```

#### IP Routing

1. Enable IP forwarding:
   ```
   /ip firewall add action=accept chain=forward
   ```

2. Add a static route:
   ```
   /ip route add dst-address=192.168.2.0/24 gateway=192.168.1.254
   ```

3. Configure OSPFv2 routing:
   ```
   /routing ospf set enabled=yes
   /routing ospf interface add interface=ether1 cost=1
   ```

### Complete Configuration Commands

**IP Addressing**
| Parameter | Description |
|---|---|
| address | IP address and network prefix |
| interface | Interface name |

**IP Pools**
| Parameter | Description |
|---|---|
| name | Pool name |
| ranges | IP address ranges within the pool |

**IP Routing**
| Parameter | Description |
|---|---|
| dst-address | Destination network address |
| gateway | Gateway IP address |
| cost | OSPF interface cost |

### Common Pitfalls and Solutions

- **Incorrect IP addressing:** Ensure the IP address and network mask are valid and compatible with the network configuration.
- **Duplicated IP addresses:** Check for any duplicate IP addresses on the network, as this can lead to connectivity issues.
- **Incorrect routing configuration:** Verify that static routes and routing protocols are configured correctly to ensure proper routing.

### Verification and Testing Steps

- Use the command `/ip address print` to verify IP addresses assigned to interfaces.
- Test connectivity to different IP addresses to ensure proper routing.
- Use the command `/ip route print` to check routing table entries.

### Related Features and Considerations

- **NAT:** Network Address Translation (NAT) can be used to translate private IP addresses to public IP addresses.
- **DHCP:** Dynamic Host Configuration Protocol (DHCP) can be used to automatically assign IP addresses to devices.
- **Firewall:** The built-in firewall can be configured to control incoming and outgoing traffic.

### MikroTik REST API Examples

**Get IP Address**
```
GET /ip/address/print
```
**Response:**
```
[
  {
    ".id": "~1",
    "address": "192.168.1.1/24",
    "disabled": false,
    "interface": "ether1"
  },
  {
    ".id": "~2",
    "address": "fe80::1",
    "disabled": false,
    "interface": "ether2"
  }
]
```

**Add IP Pool**
```
POST /ip/pool/add
{
  "name": "my-pool",
  "ranges": [
    "192.168.1.10-192.168.1.20"
  ]
}
```
**Response:**
```
{
  ".id": "~1",
  "name": "my-pool",
  "ranges": [
    "192.168.1.10-192.168.1.20"
  ]
}
```