---

## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addresses on a MikroTik RouterOS device
- Assign IP addresses to client devices using DHCP
- Implement IPv6 Neighbor Discovery Protocol (NDP)

### Step-by-Step Implementation

**IPv4 Configuration:**

1. **Create an IP address pool:** Go to `/ip pool` and click on the "Add (+)" button. Configure the following parameters:
    - Name: Choose a descriptive name for the pool
    - Ranges: Specify the range of IPv4 addresses to assign
    - DNS server: Set the IP address of your preferred DNS server

2. **Associate the pool with an interface:** Go to `/interface` and select the interface you want to assign an IP address to. Click on the "IP" tab and then on the "Add (+)" button. Choose the created pool from the dropdown menu.

**IPv6 Configuration:**

1. **Enable IPv6:** Go to `/ipv6 settings`. Set the "Accept RA" and "Announce RA" options to "yes".

2. **Configure IPv6 addresses:** Go to `/ipv6 address`. Click on the "Add (+)" button to add an IPv6 address to an interface. Configure the following parameters:
    - Interface: Select the interface to assign the IPv6 address to
    - Address: Specify the IPv6 address
    - Prefix length: Enter the prefix length of the subnet

**DHCP Server Configuration:**

1. **Enable DHCP server:** Go to `/ip dhcp-server`. Click on the "Add (+)" button to create a new DHCP server. Configure the following parameters:
    - Interface: Select the interface to run the DHCP server on
    - Address pool: Choose the IPv4 or IPv6 pool you created earlier
    - Lease time: Set the lease time for the assigned IP addresses

**IPv6 Neighbor Discovery Protocol (NDP)**

1. **Enable NDP:** Go to `/ipv6 neighbor`. Click on the "Add (+)" button to add an NDP entry. Configure the following parameters:
    - Address: Specify the IPv6 address of the neighbor
    - Interface: Select the interface to use for NDP
    - MAC address: Enter the MAC address of the neighbor (optional)

### Complete Configuration Commands

**IPv4:**

```
/ip pool add name=<pool-name> ranges=<start-ip>-<end-ip> dns-server=<dns-server-ip>
/interface ethernet add name=<interface-name> ip-address=<ip-address> pool=<pool-name>
```

**IPv6:**

```
/ipv6 settings set accept-ra=yes announce-ra=yes
/ipv6 address add address=<ipv6-address> prefix-length=<prefix-length> interface=<interface-name>
```

**DHCP Server:**

```
/ip dhcp-server add interface=<interface-name> address-pool=<pool-name> lease-time=<lease-time>
```

### Common Pitfalls and Solutions

- **Incorrect IP address range:** Ensure that the IP address ranges do not overlap with other networks or are not reserved for special purposes.
- **Duplicate IP addresses:** Verify that no two devices have the same IP address.
- **No DNS server assigned:** Remember to specify a valid DNS server address in the DHCP pool configuration.
- **NDP not enabled:** Check if NDP is enabled on both the router and client devices.

### Verification and Testing Steps

- **IPv4:** Use the `/ip address print` command to list assigned IPv4 addresses.
- **IPv6:** Use the `/ipv6 address print` command to list assigned IPv6 addresses.
- **DHCP:** Use the `/ip dhcp-server lease print` command to check DHCP lease information.
- **NDP:** Use the `/ipv6 neighbor print` command to verify NDP entries.

### Related Features and Considerations

- **Address Prefix Lists (APLs):** Used to filter IPv6 prefixes in routing.
- **DHCP Relay:** Forwards DHCP requests to a central DHCP server.
- **Dynamic Host Configuration Protocol for IPv6 (DHCPv6):** Similar to DHCP but for IPv6 addresses.

### MikroTik REST API Examples

**Get IPv4 Address Information:**

**Endpoint:** `/api/ip/address/print`

**Request Method:** `GET`

**Example JSON Payload:**

```json
{
  "interface": "ether1"
}
```

**Expected Response:**

```json
[
  {
    "address": "192.168.1.1/24",
    "disabled": false,
    "dynamic": false,
    "interface": "ether1",
    "mac-address": "00:00:00:00:00:01",
    "name": "ether1-eth01"
  }
]
```