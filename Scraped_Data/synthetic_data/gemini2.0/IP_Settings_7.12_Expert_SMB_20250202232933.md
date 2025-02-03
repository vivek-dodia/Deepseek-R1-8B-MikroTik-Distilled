## IP Settings

**Configuration Level:** Expert

**Network Scale:** SMB

### Configuration Scenario and Requirements

This guide will cover advanced IP settings in MikroTik RouterOS 7.12, including IP addressing, IP pools, IP routing, and related configurations.

### Step-by-Step Implementation

**1. IP Addressing**

- IPv4: Configure IP addresses using the `/ip address` command.
  ```
  /ip address add address=192.168.1.1/24 interface=ether1
  ```
- IPv6: Configure IPv6 addresses using the `/ipv6 address` command.
  ```
  /ipv6 address add address=2001:db8::1/64 interface=ether1
  ```

**2. IP Pools**

- Create an IP pool using the `/ip pool` command.
  ```
  /ip pool add name=pool1 ranges=192.168.1.10-192.168.1.20
  ```
- Assign the IP pool to an interface using the `/ip pool lease` command.
  ```
  /ip pool lease add interface=ether1 pool=pool1
  ```

**3. IP Routing**

- Add a static route using the `/ip route` command.
  ```
  /ip route add dst-address=172.16.0.0/24 gateway=192.168.1.254
  ```
- Add a dynamic routing protocol using the `/routing` command.
  ```
  /routing bgp add name=my-bgp
  /routing bgp my-bgp add neighbor=192.168.1.254
  ```

### Complete Configuration Commands

```
## IP Addressing
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1

## IP Pools
/ip pool add name=pool1 ranges=192.168.1.10-192.168.1.20
/ip pool lease add interface=ether1 pool=pool1

## IP Routing
/ip route add dst-address=172.16.0.0/24 gateway=192.168.1.254
/routing bgp add name=my-bgp
/routing bgp my-bgp add neighbor=192.168.1.254
```

### Common Pitfalls and Solutions

- **IP Address Conflicts:** Ensure that IP addresses assigned to interfaces do not conflict with other devices on the network.
- **Invalid IP Pools:** Verify that IP pool ranges do not overlap with existing IP addresses.
- **Routing Issues:** Check that static routes or dynamic routing protocols are correctly configured and active.

### Verification and Testing Steps

- Use the `/ip address print` and `/ipv6 address print` commands to verify IP addresses.
- Use the `/ip pool print` and `/ip pool lease print` commands to check IP pool configuration and leasing.
- Use the `/routing bgp print` command to check BGP neighbor status.

### Related Features and Considerations

- **Firewall:** Configure firewall rules to restrict and control IP traffic.
- **DHCP:** Set up a DHCP server to automatically assign IP addresses to clients.
- **DNS:** Configure DNS settings to resolve domain names to IP addresses.

### MikroTik REST API Examples

**Get IP Address:**

**API Endpoint:** `/ip/address/print`
**Request Method:** GET

**Example Request:**

```
curl -X GET http://192.168.1.1/api/ip/address/print
```

**Expected Response:**

```json
[
  {
    ".id": "0",
    "address": "192.168.1.1/24",
    "disabled": false,
    "interface": "ether1"
  }
]
```

**Set IP Address:**

**API Endpoint:** `/ip/address/set`
**Request Method:** POST

**Example Request Payload:**

```json
{
  ".id": "0",
  "address": "192.168.1.2/24"
}
```

**Example Request:**

```
curl -X POST http://192.168.1.1/api/ip/address/set -d '{"id": "0", "address": "192.168.1.2/24"}'
```