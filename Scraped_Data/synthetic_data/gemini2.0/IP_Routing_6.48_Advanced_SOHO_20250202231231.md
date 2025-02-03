**IP Routing**

## Configuration Scenario and Requirements

Configure IP routing for a SOHO network with the following requirements:

- A public IPv4 address on the WAN interface
- A private IPv4 subnet for the LAN network
- Enable DHCP for automatic IP address assignment on the LAN

## Step-by-Step Implementation

**1. Configure WAN Interface**

```
/interface add name=wan type=ethernet address=00:00:00:00:00:00
/ip address add address=X.X.X.X/24 interface=wan
```

Replace `00:00:00:00:00:00` with the WAN interface's MAC address and `X.X.X.X` with the public IPv4 address.

**2. Create LAN Bridge and Interface**

```
/interface bridge add name=br-lan
/interface add name=lan type=bridge bridge=br-lan
```

**3. Configure LAN Interface**

```
/ip address add address=192.168.1.1/24 interface=lan
```
> **Note:** Replace `192.168.1.1` with the desired LAN IP address.

**4. Enable DHCP Server**

```
/ip dhcp-server add interface=lan address-pool=lan-pool lease-time=1h
/ip pool add name=lan-pool ranges=192.168.1.2-192.168.1.254
```

**5. Enable IP Forwarding**

```
/ip routing set enabled=yes
```

## Complete Configuration Commands

```
/interface add name=wan type=ethernet address=00:00:00:00:00:00
/ip address add address=X.X.X.X/24 interface=wan
/interface bridge add name=br-lan
/interface add name=lan type=bridge bridge=br-lan
/ip address add address=192.168.1.1/24 interface=lan
/ip dhcp-server add interface=lan address-pool=lan-pool lease-time=1h
/ip pool add name=lan-pool ranges=192.168.1.2-192.168.1.254
/ip routing set enabled=yes
```

## Common Pitfalls and Solutions

- **Network connectivity issues:** Verify MAC addresses, IP addresses, and physical connections.
- **No DHCP assignments:** Check DHCP server configuration, including the address pool and lease time.
- **IP address conflicts:** Use `ip scan` command to detect duplicate addresses.

## Verification and Testing Steps

- Ping the WAN interface to verify internet connectivity.
- Check DHCP lease information using `ip dhcp-server lease print` to ensure devices are receiving addresses.
- Traceroute to an external website to verify IP routing.

## Related Features and Considerations

- **Policy Routing:** Advanced IP routing options for controlling traffic based on specific criteria.
- **NAT and Firewall:** Implement NAT rules and firewall configurations for secure network access.
- **IPsec:** Use IPsec VPN to encrypt and protect traffic between remote networks.
- **Load Balancing:** Balance WAN traffic across multiple interfaces for increased performance.

## MikroTik REST API Examples

**List IP Addresses on WAN Interface**

**API Endpoint:** `/routing/ip/address`

**Request Method:** `GET`

**Expected Response:**

```
[
  {
    "address": "X.X.X.X/24",
    "interface": "wan"
  }
]
```

**Create LAN IP Address**

**API Endpoint:** `/routing/ip/address`

**Request Method:** `POST`

**Example JSON Payload:**

```
{
  "address": "192.168.1.1/24",
  "interface": "lan"
}
```