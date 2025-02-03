## IP Settings in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

**Goal:** Configure IP settings, including IPv4 and IPv6 addressing, IP pools, IP routing, RoMON, WinBox, and RADIUS authentication.

**Requirements:**

- MikroTik RouterOS 7.11 or later
- Basic understanding of networking concepts

### Step-by-Step Implementation

**1. IPv4 and IPv6 Addressing**

**Commands:**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
```

**2. IP Pools**

**Commands:**

```
/ip pool add name=pool1 ranges=192.168.1.100-192.168.1.150
/ip pool add name=pool2 ranges=2001:db8::100-2001:db8::150
```

**3. IP Routing**

**Commands:**

```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
/ip route add dst-address=::/0 gateway=2001:db8::254
```

**4. RoMON**

**Commands:**

```
/system romon set server=192.168.1.10 username=admin password=mypassword
```

**5. WinBox**

**Commands:**

```
/ip service set winbox port=8291
```

**6. RADIUS Authentication**

**Commands:**

```
/radius add server=server1 address=192.168.1.100 secret=mysecret
/user add name=user1 group=group1 password=mypassword auth-type=radius
```

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
/ip pool add name=pool1 ranges=192.168.1.100-192.168.1.150
/ip pool add name=pool2 ranges=2001:db8::100-2001:db8::150
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
/ip route add dst-address=::/0 gateway=2001:db8::254
/system romon set server=192.168.1.10 username=admin password=mypassword
/ip service set winbox port=8291
/radius add server=server1 address=192.168.1.100 secret=mysecret
/user add name=user1 group=group1 password=mypassword auth-type=radius
```

### Common Pitfalls and Solutions

**Pitfall:** Incorrect IP address or subnet mask

**Solution:** Verify the IP address and subnet mask are correct for the network.

**Pitfall:** IP conflict with other devices

**Solution:** Check for duplicate IP addresses on the network using tools like `ip neighbor` or `ping`.

**Pitfall:** RoMON server unreachable

**Solution:** Ensure the RoMON server is accessible and the correct server address and credentials are configured.

### Verification and Testing Steps

1. Verify IP addressing by running `ip address print`
2. Check IP pool configuration with `ip pool print`
3. Test IP routing by pinging external hosts
4. Test RoMON by connecting to the router via RoMON console
5. Test WinBox connection by accessing the router's web interface
6. Check RADIUS authentication by attempting to login with a RADIUS user

### Related Features and Considerations

- DHCP for IP address assignment
- DNS for hostname resolution
- Firewall for network security
- QoS for traffic prioritization

### MikroTik REST API Examples

**Get IP Address:**

**Endpoint:** `/ip/address/print`

**Request Method:** GET

**Example Request:**

```json
{
  ".proplist": "list"
}
```

**Expected Response:**

```json
[
  {
    ".id": ".1",
    "address": "192.168.1.1/24",
    "interface": "ether1"
  },
  {
    ".id": ".2",
    "address": "2001:db8::1/64",
    "interface": "ether1"
  }
]
```

**Add IP Pool:**

**Endpoint:** `/ip/pool/add`

**Request Method:** POST

**Example Request Body:**

```json
{
  "name": "pool1",
  "ranges": ["192.168.1.100-192.168.1.150"]
}
```