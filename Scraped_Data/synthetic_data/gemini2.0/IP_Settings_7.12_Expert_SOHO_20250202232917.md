**IP Settings**

## Configuration Scenario and Requirements

**Objective:** Configure IP settings on a MikroTik RouterOS device for optimal network connectivity and functionality.

## Step-by-Step Implementation

**Step 1: IP Addressing (IPv4)**

```
/ip address
add address=192.168.1.1/24 interface=ether1
```

**Explanation:** This command creates an IPv4 address on the `ether1` interface and assigns the network mask `/24`.

**Step 2: IP Addressing (IPv6)**

```
/ip address
add address=2001:db8::1/64 interface=ether1
```

**Explanation:** This command creates an IPv6 address on the `ether1` interface and assigns the prefix length `/64`.

**Step 3: IP Pool**

```
/ip pool
add name=my-pool ranges=192.168.1.10-192.168.1.254 interface=ether1
```

**Explanation:** This command creates an IP address pool named `my-pool` with a range of addresses from `192.168.1.10` to `192.168.1.254` that can be assigned to clients on the `ether1` interface.

**Step 4: IP Routing**

```
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.1.1
```

**Explanation:** This command creates a default route that forwards all traffic not explicitly routed to the gateway with the IP address `192.168.1.1`.

**Step 5: DNS**

```
/ip dns
set servers=8.8.8.8,8.8.4.4
```

**Explanation:** This command specifies the DNS servers to use for resolving domain names.

## Complete Configuration Commands

```
/ip address
add address=192.168.1.1/24 interface=ether1
/ip address
add address=2001:db8::1/64 interface=ether1
/ip pool
add name=my-pool ranges=192.168.1.10-192.168.1.254 interface=ether1
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.1.1
/ip dns
set servers=8.8.8.8,8.8.4.4
```

## Common Pitfalls and Solutions

- **Incorrect IP address or subnet mask:** Ensure the IP address and subnet mask are valid for the network.
- **Gateway mismatch:** Verify that the gateway specified in the IP routing command is reachable.
- **DNS server unavailability:** Check that the DNS servers are accessible and responsive.

## Verification and Testing Steps

- Test IP connectivity by pinging an external IP address.
- Run a traceroute to a remote host to verify routing.
- Use the `/ip dns print` command to check DNS settings.

## Related Features and Considerations

- **Address Scopes:** Use address scopes to assign different IP address ranges based on specific criteria.
- **DHCP Server:** Set up a DHCP server to automatically assign IP addresses to clients.
- **Firewall Rules:** Create firewall rules to control access to and from specific IP addresses or ranges.

## MikroTik REST API Examples

**Get IP Addresses**

**API Endpoint:** `/ip/address/print`
**Request Method:** GET
**Example JSON Payload:**

```json
{}
```

**Expected Response:**

```json
[
  {
    ".id": "1",
    "address": "192.168.1.1/24",
    "interface": "ether1"
  },
  {
    ".id": "2",
    "address": "2001:db8::1/64",
    "interface": "ether1"
  }
]
```

**Add IP Address**

**API Endpoint:** `/ip/address/add`
**Request Method:** POST
**Example JSON Payload:**

```json
{
  "address": "192.168.2.1/24",
  "interface": "ether2"
}
```

**Expected Response:**

```json
{
  ".id": "3"
}
```