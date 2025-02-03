**IP Settings**

**1. Configuration Scenario and Requirements**

- Configure IP settings, including IPv4 and IPv6 addresses, on a MikroTik RouterOS 7.12 device.
- Assign IP addresses to specific interfaces.
- Enable DHCP server on one interface.
- Allow access to the router's web interface only from specific IP addresses.
- Configure MAC server to track MAC addresses of connected devices.

**2. Step-by-Step Implementation**

**Configure IPv4 Address:**

```
/ip address add address=192.168.1.1/24 interface=ether1
```

**Configure IPv6 Address:**

```
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

**Assign IP Address to Interface:**

```
/interface ip address add address=172.16.2.10/24 interface=ether2
```

**Enable DHCP Server:**

```
/ip dhcp-server add address-pool=dhcp-pool1 interface=ether3
```

**Restrict Web Interface Access:**

```
/ip firewall filter
add action=deny dst-address=192.168.1.0/24 chain=input
```

**Configure MAC Server:**

```
/ip mac-server server=mac-server1 interface=ether4
```

**3. Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1
/interface ip address add address=172.16.2.10/24 interface=ether2
/ip dhcp-server add address-pool=dhcp-pool1 interface=ether3
/ip firewall filter
add action=deny dst-address=192.168.1.0/24 chain=input
/ip mac-server server=mac-server1 interface=ether4
```

**4. Common Pitfalls and Solutions**

- **DHCP Server Not Assigning Addresses:** Ensure that the DHCP server is enabled on the correct interface and that the address pool has a sufficient number of available IP addresses.
- **Web Interface Not Accessible:** Check that the IP address used to access the web interface matches one of the allowed IP addresses in the firewall rule.
- **MAC Server Not Tracking MAC Addresses:** Verify that the MAC server is running and that the interface specified is the one connected to the devices you want to track.

**5. Verification and Testing Steps**

- Ping the IP addresses assigned to the router to verify connectivity.
- Use a DHCP client to obtain an IP address from the DHCP server.
- Attempt to access the web interface from allowed and denied IP addresses to test the firewall rule.
- Monitor the MAC server logs to see if MAC addresses are being tracked.

**6. Related Features and Considerations**

- Consider using static IP addresses for critical devices to ensure they always have the same IP address.
- Limit the number of IP addresses allowed in the DHCP pool to prevent IP conflicts.
- Regularly check the MAC server logs to identify unauthorized devices on the network.

**7. MikroTik REST API Examples**

**Get IP Addresses:**

**Endpoint:** `/ip/address/print`

**Request Method:** GET

**Example JSON Payload:**

```
{
}
```

**Expected Response:**

```
[
  {
    "disabled": false,
    "interface": "ether1",
    "address": "192.168.1.1/32",
    "network": "192.168.1.0/24"
  },
  {
    "disabled": false,
    "interface": "ether2",
    "address": "172.16.2.10/32",
    "network": "172.16.2.0/24"
  }
]
```

**Add IPv6 Address:**

**Endpoint:** `/ipv6/address/add`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "address": "2001:db8::1/64",
  "interface": "ether1"
}
```

**Expected Response:**

```
{
  "address": "2001:db8::1/64",
  "interface": "ether1",
  "id": 1
}
```