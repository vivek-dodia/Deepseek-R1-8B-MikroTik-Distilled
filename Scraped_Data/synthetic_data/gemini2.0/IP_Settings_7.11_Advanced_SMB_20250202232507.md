## IP Settings

### IP Addressing (IPv4 and IPv6)

IPv4 and IPv6 addresses are assigned to interfaces to enable communication on the network. IPv4 addresses are 32-bit addresses, while IPv6 addresses are 128-bit addresses.

**Configuration Steps:**

1. Go to **IP > Addresses**.
2. Click the **+** button to add a new address.
3. Select the **Interface** to assign the address to.
4. Enter the **Address**.
5. Click **OK**.

**Example:**

```
/ip address add address=192.168.1.10/24 interface=ether1
```

### IP Pools

IP pools are used to dynamically assign IP addresses to devices on a network. This is useful for scenarios where devices frequently join and leave the network, such as in a DHCP environment.

**Configuration Steps:**

1. Go to **IP > Pool**.
2. Click the **+** button to add a new pool.
3. Enter a **Name** for the pool.
4. Select the **Ranges** to include in the pool.
5. Click **OK**.

**Example:**

```
/ip pool add name=dhcp-pool ranges=192.168.1.10-192.168.1.254
```

### IP Routing

IP routing is used to determine the path that IP packets take through a network. Routers use routing tables to determine which interface to forward packets to based on their destination address.

**Configuration Steps:**

1. Go to **IP > Routes**.
2. Click the **+** button to add a new route.
3. Enter the **Destination** network to be routed.
4. Select the **Interface** to use for routing.
5. Enter the **Gateway** IP address.
6. Click **OK**.

**Example:**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.1 interface=ether2
```

### MAC Server

A MAC server is used to associate MAC addresses with IP addresses. This is useful for managing network access and security.

**Configuration Steps:**

1. Go to **IP > MAC Server**.
2. Click the **+** button to add a new MAC address.
3. Enter the **MAC Address** and **IP Address** of the device to be associated.
4. Click **OK**.

**Example:**

```
/ip mac-server add mac-address=00:11:22:33:44:55 ip-address=192.168.1.10
```

### Common Pitfalls and Solutions

**Pitfall 1:** Invalid IP address or subnet mask
**Solution:** Ensure that the IP address and subnet mask are valid and match the network configuration.

**Pitfall 2:** Incorrect routing configuration
**Solution:** Verify that the routing table has the correct destination networks, gateways, and interfaces.

**Pitfall 3:** MAC address conflicts
**Solution:** Ensure that each MAC address is unique and associated with only one IP address.

### Verification and Testing Steps

1. Use the **ping** command to test connectivity to different IP addresses on the network.
2. Use the **traceroute** command to trace the path taken by packets through the network.
3. Use the **ip address print** command to verify that IP addresses are assigned to interfaces correctly.
4. Use the **ip route print** command to verify that the routing table is configured correctly.

### Related Features and Considerations

- DHCP Server
- DNS Server
- Firewall
- Traffic Shaping

### MikroTik REST API Examples

**ENDPOINT:** /ip/address

**METHOD:** GET

**Example JSON Response:**

```json
[
  {
    "address": "192.168.1.10/24",
    "interface": "ether1",
    "dynamic": false
  }
]
```

**ENDPOINT:** /ip/address

**METHOD:** POST

**Example JSON Request Body:**

```json
{
  "address": "192.168.1.11/24",
  "interface": "ether1"
}
```