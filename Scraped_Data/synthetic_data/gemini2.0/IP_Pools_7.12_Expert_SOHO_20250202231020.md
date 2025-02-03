## IP Pools

### Introduction

IP pools are used to dynamically assign IP addresses to clients on a network. They are typically used in conjunction with DHCP (Dynamic Host Configuration Protocol). RouterOS supports both IPv4 and IPv6 IP pools.

### Configuration

**1. Create an IP Pool**

```
/ip pool add name=pool1 ranges=192.168.1.10-192.168.1.20 comment="Office LAN"
```

**Parameters:**

- name: Name of the IP pool
- ranges: Range of IP addresses to be assigned
- comment: Optional comment to describe the pool

**2. Assign IP Pool to an Interface**

```
/interface add dhcp-server name=dhcp-server1 address=192.168.1.1 interface=ether1 pool=pool1 lease-time=8h
```

**Parameters:**

- name: Name of the DHCP server
- address: IP address of the DHCP server
- interface: Interface to which the DHCP server will be assigned
- pool: Name of the IP pool to be used by the DHCP server
- lease-time: Lease time for IP addresses assigned by the DHCP server

### Verification

**1. Check IP Pool**

```
/ip pool print
```

**2. Check DHCP Server**

```
/interface dhcp-server print
```

### Common Pitfalls and Solutions

- **Duplicate IP addresses:** Ensure that the IP address range specified in the IP pool does not overlap with any existing IP addresses on the network.
- **Incorrect lease time:** Set the lease time appropriately to prevent IP address conflicts.
- **Firewall rules:** Ensure that firewall rules are configured to allow DHCP traffic.

### Related Features

- DHCP
- Static IP addresses
- NAT (Network Address Translation)

### MikroTik REST API

**Endpoint:** /ip/pool

**Method:** GET

**Example JSON Payload:**

```json
{
  "action": "getall"
}
```

**Expected Response:**

```json
[
  {
    ".id": "1",
    "name": "pool1",
    "ranges": "192.168.1.10-192.168.1.20",
    "comment": "Office LAN"
  }
]
```