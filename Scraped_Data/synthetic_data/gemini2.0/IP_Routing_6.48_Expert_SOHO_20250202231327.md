## IP Routing

### Configuration Scenario and Requirements

**Objective:** Configure IP routing on a MikroTik RouterOS 6.48 device.

### Step-by-Step Implementation

#### IPv4 Routing

**1. Enable IP Forwarding:**
```text
/ip firewall set forward enable=yes
```

**2. Add Default Route:**
```text
/ip route add gateway=192.168.1.1
```

#### IPv6 Routing

**1. Enable IPv6 Routing:**
```text
/ipv6 firewall set enable=yes
/ipv6 ip enable=yes
```

**2. Add Default Route:**
```text
/ipv6 route add ::/0 next-hop fe80::1
```

### Complete Configuration Commands

**IPv4:**
```text
/ip firewall set forward enable=yes
/ip route add gateway=192.168.1.1
```

**IPv6:**
```text
/ipv6 firewall set enable=yes
/ipv6 ip enable=yes
/ipv6 route add ::/0 next-hop fe80::1
```

### Common Pitfalls and Solutions

**Pitfall:** No Internet connectivity after enabling IP forwarding.

**Solution:** Ensure the default route is correctly configured and that the gateway is accessible.

### Verification and Testing Steps

**Test IPv4 Connectivity:**
```text
ping 8.8.8.8
```

**Test IPv6 Connectivity:**
```text
ping6 ipv6.google.com
```

### Related Features and Considerations

* [Static Routing](https://wiki.mikrotik.com/wiki/Manual:IP/Routing)
* [BGP Routing](https://wiki.mikrotik.com/wiki/Manual:IP/BGP)
* [OSPF Routing](https://wiki.mikrotik.com/wiki/Manual:IP/OSPF)

### MikroTik REST API Examples

**Get IPv4 Default Gateway:**
```text
GET /ip/route/print?dst-address=0.0.0.0/0
```

**Expected Response:**
```json
[
  {
    "dst-address": "0.0.0.0/0",
    "gateway": "192.168.1.1"
  }
]
```