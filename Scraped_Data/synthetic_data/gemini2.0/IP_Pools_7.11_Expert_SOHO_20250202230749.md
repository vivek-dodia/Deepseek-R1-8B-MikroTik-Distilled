## IP Pools

### Configuration Scenario and Requirements

This scenario demonstrates the configuration of IP pools on a MikroTik RouterOS device to dynamically assign IP addresses to clients.

### Step-by-Step Implementation

1. Connect to the RouterOS device using WinBox or SSH.
2. Navigate to **IP > Pools**.
3. Click the **(+)** button to create a new IP pool.
4. Enter the following parameters:
   - Name: Specify a descriptive name for the pool, such as "Office-Pool".
   - Ranges: Define the range of IP addresses to be assigned by the pool, e.g., "10.0.0.101-10.0.0.200".
   - Gateway: Enter the default gateway IP address for the clients assigned from this pool.
5. Click **Apply** to save the configuration.

### Complete Configuration Commands

```
/ip pool add name=Office-Pool ranges=10.0.0.101-10.0.0.200 gateway=10.0.0.1
```

### Common Pitfalls and Solutions

- **Ensure that the IP range does not overlap with any existing IP address assignments.** Verify the available IP addresses on the network before configuring a new pool.
- **Disable DHCP on any other interfaces that may conflict with the IP pool.** This prevents duplicate IP address assignments and ensures clients receive addresses from the intended pool.

### Verification and Testing Steps

- Assign the IP pool to a DHCP server interface.
- Connect a client device and obtain an IP address from the pool.
- Verify that the assigned IP address is within the specified range and has the correct gateway.

### Related Features and Considerations

- **DHCP Server:** IP pools are used in conjunction with DHCP servers to dynamically assign IP addresses to clients.
- **Address Reservation:** The IP pool can be configured with static IP reservations for specific devices.
- **MAC Binding:** Clients can be bound to specific IP addresses based on their MAC addresses.

### MikroTik REST API Examples

#### Endpoint: `/ip/pool`

#### Method: POST

#### Request Payload:

```json
{
  "name": "Office-Pool",
  "ranges": ["10.0.0.101-10.0.0.200"],
  "gateway": "10.0.0.1"
}
```

#### Expected Response:

```json
{
  "id": "0"
}
```

## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

This scenario demonstrates the configuration of IPv4 and IPv6 addresses on a MikroTik RouterOS device.

### Step-by-Step Implementation

**IPv4:**

1. Navigate to **IP > Addresses**.
2. Click the **(+)** button to create a new IPv4 address.
3. Enter the following parameters:
   - Address: Specify the IP address, e.g., "10.0.0.1".
   - Interface: Select the interface on which the IP address will be assigned.
   - Network: Enter the network subnet mask, e.g., "24".

**IPv6:**

1. Navigate to **IP > Addresses**.
2. Click the **(+)** button and select "Add IPv6 Address".
3. Enter the following parameters:
   - Address: Specify the IPv6 address, e.g., "2001:db8::1".
   - Prefix: Enter the IPv6 prefix length, e.g., "64".
   - Interface: Select the interface on which the IPv6 address will be assigned.

### Complete Configuration Commands

**IPv4:**

```
/ip address add address=10.0.0.1 interface=ether1 network=24
```

**IPv6:**

```
/ipv6 address add address=2001:db8::1 prefix=64 interface=ether1
```

### Common Pitfalls and Solutions

- **Ensure that the IP addresses are within the valid ranges for the assigned interfaces.**
- **Avoid conflicting IP addresses:** Verify that the assigned IP addresses do not conflict with any other devices on the network.
- **Consider using DHCP for dynamic IP address assignment:** This simplifies IP address management and reduces the risk of IP conflicts.

### Verification and Testing Steps

- Ping the IP addresses from another device on the network.
- Use the "/ip address print" or "/ipv6 address print" commands to view the configured IP addresses.

### Related Features and Considerations

- **IP Routing:** IP addresses are used for routing network traffic between devices.
- **DNS:** DNS servers can be configured to resolve IP addresses to domain names.
- **DHCP:** DHCP servers can be used to automatically assign IP addresses to clients.

### MikroTik REST API Examples

#### Endpoint: `/ip/address`

#### Method: POST

#### Request Payload (IPv4):

```json
{
  "address": "10.0.0.1",
  "interface": "ether1",
  "network": "24"
}
```

#### Request Payload (IPv6):

```json
{
  "address": "2001:db8::1",
  "prefix": "64",
  "interface": "ether1"
}
```

#### Expected Response:

```json
{
  "id": "0"
}
```

## IP Routing

### Configuration Scenario and Requirements

This scenario demonstrates the configuration of IP routing on a MikroTik RouterOS device to forward packets between different networks.

### Step-by-Step Implementation

1. Navigate to **IP > Routes**.
2. Click the **(+)** button to create a new static route.
3. Enter the following parameters:
   - Destination: Specify the destination network or IP address to be routed, e.g., "192.168.2.0/24".
   - Gateway: Enter the IP address of the gateway or next hop device for the route.
   - Distance: Set the administrative distance for the route.
4. Click **Apply** to save the configuration.

### Complete Configuration Commands

```
/ip route add dst-address=192.168.2.0/24 gateway=10.0.0.2 distance=2
```

### Common Pitfalls and Solutions

- **Ensure that the destination network is reachable:** Verify that the destination network is reachable from the router through the specified gateway.
- **Avoid creating routing loops:** Configure routes carefully to prevent creating routing loops that can lead to network instability.
- **Configure default routes:** If necessary, configure a default route to handle traffic to destinations not explicitly defined in the routing table.

### Verification and Testing Steps

- Ping destinations to verify that they are reachable.
- Use the "/ip route print" command to view the configured routing table.

### Related Features and Considerations

- **IP Addressing:** IP addresses and subnets are used to identify and route traffic between networks.
- **IP Forwarding:** IP forwarding must be enabled to allow the router to forward packets between interfaces.
- **Firewall:** Firewalls can be configured to control and filter traffic based on IP addresses and ports.

### MikroTik REST API Examples

#### Endpoint: `/ip/route`

#### Method: POST

#### Request Payload:

```json
{
  "dst-address": "192.168.2.0/24",
  "gateway": "10.0.0.2",
  "distance": 2
}
```

#### Expected Response:

```json
{
  "id": "0"
}
```

## IP Settings

### Configuration Scenario and Requirements

This scenario demonstrates the configuration of advanced IP settings on a MikroTik RouterOS device to control various aspects of IP networking.

### Step-by-Step Implementation

1. Navigate to **IP > Settings**.
2. Configure the following parameters as required:
   - **IP Firewall:** Enable or disable the built-in firewall.
   - **IP Checksum:** Configure checksum offloading for improved performance.
   - **IP No Fast Path:** Disable fast path acceleration for increased security and stability.
   - **IP MTU:** Set the maximum transmission unit (MTU) size for all interfaces.
   - **IP Proxy ARP Auto-Reply:** Configure the router to automatically respond to ARP requests for other devices on the network.
3. Click **Apply** to save the configuration.

### Complete Configuration Commands

```
/ip settings set ip-firewall=enabled ip-checksum=hardware ip-no-fastpath=no ip-mtu=1500 ip-proxy-arp-auto-reply=enabled
```

### Common Pitfalls and Solutions

- **Be cautious when disabling IP firewall:** Disabling the firewall may expose the device to security risks.
- **Ensure that IP checksum offloading is supported:** Not all hardware may support checksum offloading.
- **Consider the impact of changing the MTU size:** Reducing the MTU size may improve reliability but reduce bandwidth.

### Verification and Testing Steps

- Verify firewall status using the "/ip firewall print" command.
- Checksum offloading can be tested by sending packets with different checksum configurations.
- Ping devices to test MTU size and network connectivity.

### Related Features and Considerations

- **IP Routing:** IP settings can influence routing behavior and performance.
-