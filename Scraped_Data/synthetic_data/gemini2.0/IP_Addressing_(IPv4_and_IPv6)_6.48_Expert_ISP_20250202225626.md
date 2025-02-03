## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addressing on a RouterOS device.
- Establish default routes for IPv4 and IPv6 traffic.

### Step-by-Step Implementation

#### IPv4 Addressing
1. Navigate to **IP** > **Addresses** in WinBox.
2. Click **"+"** to create a new IPv4 address.
3. Select the appropriate **Interface** and enter the **IPv4 Address**.
4. Set the **Network** mask and **Gateway** as required.

**Example:**

```
/ip address add address=192.168.1.1/24 gateway=192.168.1.254 interface=ether1
```

#### IPv6 Addressing
1. Navigate to **IP** > **Addresses** in WinBox.
2. Click **"+"** to create a new IPv6 address.
3. Select the appropriate **Interface**.
4. Enter the **IPv6 Address** (e.g., `2a01:4f8:c0a8:8345::1/64`).
5. Set the **Gateway** IP address if necessary.

**Example:**

```
/ip address add address=2a01:4f8:c0a8:8345::1/64 interface=ether1
```

#### Default Routes

#### IPv4 Default Route
1. Navigate to **IP** > **Routes** in WinBox.
2. Click **"+"** to create a new IPv4 route.
3. Set the **Destination Network** (e.g., `0.0.0.0/0`).
4. Enter the **Gateway** IP address.

**Example:**

```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

#### IPv6 Default Route
1. Navigate to **IPv6** > **Routes** in WinBox.
2. Click **"+"** to create a new IPv6 route.
3. Set the **Destination Network** (e.g., `::/0`).
4. Enter the **Gateway** IP address.

**Example:**

```
/ipv6 route add dst-address=::/0 gateway=2a01:4f8:c0a8:8345::1
```

### Complete Configuration Commands

#### IPv4 Addressing
- Add IPv4 address: `/ip address add address=<address> interface=<interface> network=<mask>`
- Remove IPv4 address: `/ip address remove address=<address> interface=<interface>`

#### IPv6 Addressing
- Add IPv6 address: `/ip address add address=<address> interface=<interface>`
- Remove IPv6 address: `/ip address remove address=<address> interface=<interface>`

#### Default Routes
- IPv4: `/ip route add dst-address=<network> gateway=<gateway>`
- IPv6: `/ipv6 route add dst-address=<network> gateway=<gateway>`

### Common Pitfalls and Solutions

- Ensure the network mask matches the subnet of the IPv4 address.
- Verify that the IPv6 address is correctly formatted.
- Check if the gateway is reachable and has a valid IP address.
- Resolve address collision issues by using different IP addresses.

### Verification and Testing Steps

- Ping the configured IPv4 and IPv6 addresses to verify connectivity.
- Use the `traceroute` command to trace the path to a remote host.
- Check the IP addresses and routes using the `/ip address print` and `/ip route print` commands.
- Use the `/ip verify address` and `/ip verify route` commands to validate the configurations.

### Related Features and Considerations

- Use IP Pools to assign IP addresses dynamically.
- Implement IP Routing to forward traffic between different networks.
- Configure IP Settings to modify global IP parameters.

### MikroTik REST API Examples

#### List IPv4 Addresses
```
GET /ip/address
```

#### Add IPv4 Address
```
POST /ip/address
{
  "address": "192.168.1.100/24",
  "interface": "ether1"
}
```

#### Remove IPv4 Address
```
DELETE /ip/address/1
```
where `1` is the ID of the IPv4 address to be removed.

#### List IPv6 Addresses
```
GET /ipv6/address
```

#### Add IPv6 Address
```
POST /ipv6/address
{
  "address": "2a01:4f8:c0a8:8345::100/64",
  "interface": "ether1"
}
```

#### Remove IPv6 Address
```
DELETE /ipv6/address/1
```
where `1` is the ID of the IPv6 address to be removed.