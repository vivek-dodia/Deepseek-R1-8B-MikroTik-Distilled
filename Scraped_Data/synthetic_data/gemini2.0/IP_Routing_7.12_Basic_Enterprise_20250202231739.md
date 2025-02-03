## IP Routing in MikroTik RouterOS 7.12

### IP Addressing (IPv4 and IPv6)

**Configuration Scenario and Requirements:**

Configure IPv4 and IPv6 address and gateway for the following port: ether1

| Parameter | Description | Default Value |
|---|---|---|
| address | IPv4 address | None |
| netmask | IPv4 subnet mask | None |
| gateway | IPv4 gateway | None |
| ipv6-address | IPv6 address | None |
| prefix-length | IPv6 prefix length | None |
| ipv6-gateway | IPv6 gateway | None |

**Step-by-Step Implementation:**

1. Connect to the router via WinBox, SSH, or the command line.
2. Navigate to **IP** > **Addresses** and click on the **+** button.
3. In the **Interface** field, select `ether1`.
4. Enter the IPv4 address and netmask in the corresponding fields.
5. Enter the IPv4 gateway in the **Gateway** field (optional).
6. Click on the **IPv6** tab and enter the IPv6 address and prefix length.
7. Enter the IPv6 gateway in the **IPv6 Gateway** field (optional).
8. Click **Apply** to save the changes.

**Complete Configuration Commands:**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
```

### IP Pools

**Configuration Scenario and Requirements:**

Create an IP pool for the following range: 192.168.1.100 - 192.168.1.150

| Parameter | Description | Default Value |
|---|---|---|
| name | Pool name | None |
| range | IP address range | None |
| address | Starting IP address | None |
| gateway | Gateway address | None |
| dns-server | DNS server address | None |
| dhcp-options | DHCP options | None |

**Step-by-Step Implementation:**

1. Navigate to **IP** > **Pool** and click on the **+** button.
2. Enter a name for the pool in the **Name** field.
3. Select the appropriate interface in the **Ranges** tab.
4. Enter the starting IP address and the number of addresses in the **Range** field.
5. Enter the gateway address in the **Gateway** field (optional).
6. Enter the DNS server address in the **DNS Server** field (optional).
7. Click **Apply** to save the changes.

**Complete Configuration Commands:**

```
/ip pool add name=pool1 ranges=192.168.1.100-192.168.1.150
```

### IP Routing

**Configuration Scenario and Requirements:**

Configure a static route to the destination network 192.168.2.0/24 with a gateway of 192.168.1.2

| Parameter | Description | Default Value |
|---|---|---|
| dst-address | Destination network address | None |
| dst-address-prefix | Destination network address prefix length | None |
| gateway | Next-hop gateway address | None |
| interface | Interface to send traffic through | None |

**Step-by-Step Implementation:**

1. Navigate to **IP** > **Routes** and click on the **+** button.
2. Enter the destination network address in the **Destination** field.
3. Enter the destination network address prefix length in the **Prefix** field.
4. Enter the gateway address in the **Gateway** field.
5. Select the appropriate interface in the **Interface** field (optional).
6. Click **Apply** to save the changes.

**Complete Configuration Commands:**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
```