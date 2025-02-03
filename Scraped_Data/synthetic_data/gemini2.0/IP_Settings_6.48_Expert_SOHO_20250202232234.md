## IP Settings

### IP Addressing (IPv4 and IPv6)

#### IPv4 Configuration

**Scenario and Requirements:**

- Assign an IPv4 address and default gateway to a specific interface.

**Implementation:**

1. Navigate to `/ip address` in the RouterOS web interface.
2. Click on the "Add" button.
3. Select the desired interface from the "Interface" dropdown.
4. Enter the IPv4 address in the "Address" field.
5. Enter the default gateway in the "Gateway" field.
6. Click on the "OK" button to save the configuration.

**Configuration Commands:**

```
/ip address add address=192.168.1.10/24 interface=ether1
/ip address set 0 gateway=192.168.1.1
```

**IPv6 Configuration:**

**Scenario and Requirements:**

- Assign an IPv6 address to a specific interface.

**Implementation:**

1. Navigate to `/ipv6 address` in the RouterOS web interface.
2. Click on the "Add" button.
3. Select the desired interface from the "Interface" dropdown.
4. Enter the IPv6 address in the "Address" field.
5. Click on the "OK" button to save the configuration.

**Configuration Commands:**

```
/ipv6 address add address=2001:db8:1::1/64 interface=ether1
```

### IP Pools

#### IP Pool Creation

**Scenario and Requirements:**

- Create an IP pool for assigning dynamic IP addresses to clients.

**Implementation:**

1. Navigate to `/ip pool` in the RouterOS web interface.
2. Click on the "Add" button.
3. Enter a name for the IP pool in the "Name" field.
4. Select the range of IP addresses that should be included in the pool in the "Ranges" field.
5. Enter the subnet mask for the pool in the "Prefix" field.
6. Click on the "OK" button to save the configuration.

**Configuration Commands:**

```
/ip pool add name=my-ip-pool ranges=192.168.1.10-192.168.1.20 prefix=24
```

### IP Routing

#### Static Route Configuration

**Scenario and Requirements:**

- Add a static route to a specific network.

**Implementation:**

1. Navigate to `/ip route` in the RouterOS web interface.
2. Click on the "Add" button.
3. Enter the destination network in the "Dst. Address" field.
4. Enter the next hop gateway in the "Gateway" field.
5. Click on the "OK" button to save the configuration.

**Configuration Commands:**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.1
```

#### Default Route Configuration

**Scenario and Requirements:**

- Configure a default route to send all traffic not matching a specific route to a specific gateway.

**Implementation:**

1. Navigate to `/ip route` in the RouterOS web interface.
2. Click on the "Add" button.
3. Enter a null destination (0.0.0.0/0) in the "Dst. Address" field.
4. Enter the next hop gateway in the "Gateway" field.
5. Click on the "OK" button to save the configuration.

**Configuration Commands:**

```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
```

### Additional Features

#### MAC Server

- Assign static IP addresses based on MAC addresses.

#### RoMON

- Remote monitoring for routers.

#### WinBox

- Graphical utility for managing RouterOS from Windows.

#### Certificates

- Manage SSL certificates for secure connections.

#### PPP AAA

- Authentication and authorization for PPP connections.

#### RADIUS

- Remote Authentication Dial-In User Service (RADIUS) support.

#### User / User Groups

- Create and manage user accounts and groups.

#### Related REST API Calls

- `/ip/address`: Manage IPv4 and IPv6 addresses.
- `/ipv6/address`: Manage IPv6 addresses.
- `/ip/pool`: Manage IP pools.
- `/ip/route`: Manage IP routing.