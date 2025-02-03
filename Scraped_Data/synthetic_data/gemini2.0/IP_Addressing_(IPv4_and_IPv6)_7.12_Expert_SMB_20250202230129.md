### IP Addressing (IPv4 and IPv6)

#### Configuration Scenario and Requirements

Configure IP addresses and related settings for IPv4 and IPv6 networks on a MikroTik RouterOS 7.12 router.

#### Step-by-Step Implementation

**IPv4**

1. Create an IP address pool for dynamic IP assignment:

```
/ip pool add name=pool1 ranges=192.168.1.0/24
```

2. Assign the IP pool to an interface:

```
/interface ip address add address=192.168.1.1/24 interface=ether1 pool=pool1
```

**IPv6**

1. Configure IPv6 address ranges on interfaces:

```
/ipv6 address add address=2001:db8::1/64 interface=ether1
/ipv6 address add address=2002:db8::1/64 interface=ether2
```

2. Enable Router Advertisement (RA) to announce IPv6 addresses:

```
/ipv6 nd ra set enabled=yes interface=ether1
/ipv6 nd ra set enabled=yes interface=ether2
```

#### Complete Configuration Commands

**IPv4:**

```
/ip pool add name=pool1 ranges=192.168.1.0/24
/interface ip address add address=192.168.1.1/24 interface=ether1 pool=pool1
```

**IPv6:**

```
/ipv6 address add address=2001:db8::1/64 interface=ether1
/ipv6 address add address=2002:db8::1/64 interface=ether2
/ipv6 nd ra set enabled=yes interface=ether1
/ipv6 nd ra set enabled=yes interface=ether2
```

#### Common Pitfalls and Solutions

* **IP Address Conflict:** Ensure that each device has a unique IP address. Use the `/ip address print` command to check for conflicts.
* **Subnet Mismatch:** The IP address and subnet mask must match. Verify using the `/ip address print` command.
* **Gateway Issues:** Ensure that the default gateway is accessible and routes traffic correctly.

#### Verification and Testing Steps

* **IPv4:** Ping an external IP address to verify connectivity. Use the `/ip address print` command to check the IP configuration.
* **IPv6:** Use the `/ipv6 address print` command to verify IPv6 addresses. Ping an IPv6 address to test connectivity.

#### Related Features and Considerations

* **DHCP:** Use DHCP to automatically assign IP addresses to devices.
* **Static IP Addresses:** Manually configure specific IP addresses for devices that require fixed addresses.
* **IP Aliasing:** Assign multiple IP addresses to a single interface.

#### REST API Examples

**IPv4:**

**Endpoint:** `/ip/pool`
**Method:** POST

**Request:**

```json
{
  "name": "pool1",
  "ranges": ["192.168.1.0/24"]
}
```

**Response:**

```json
{
  "id": "1"
}
```

**IPv6:**

**Endpoint:** `/ipv6/address`
**Method:** POST

**Request:**

```json
{
  "address": "2001:db8::1/64",
  "interface": "ether1"
}
```

**Response:**

```json
{
  "id": "1"
}
```