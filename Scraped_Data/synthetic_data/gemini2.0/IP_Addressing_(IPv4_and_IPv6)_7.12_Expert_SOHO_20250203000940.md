Okay, this is a substantial request, but I'm prepared to tackle it and provide a comprehensive guide for the experienced MikroTik user. This document will cover the breadth of topics requested, emphasizing practical implementations and MikroTik-specific details.

---

# MikroTik RouterOS: Expert Guide to IP Addressing and Beyond

This document provides a comprehensive exploration of IP addressing (both IPv4 and IPv6) and related networking topics within the context of MikroTik RouterOS. It is designed for expert users working in a SOHO or similar environment and targets RouterOS 7.12 (or similar 7.x).

## 1. Comprehensive Configuration Scenario & Requirements

**Scenario:** We are setting up a home/small office network using a MikroTik router as the central gateway. This network has:
* Internet access via a dynamic IPv4 address obtained through DHCP.
* Local network with IPv4 addressing using private IP addresses (192.168.88.0/24).
* IPv6 connectivity is provided by the ISP, using a /64 prefix.
* Multiple VLANs for different devices (e.g., guest network, IoT devices).
* QoS to prioritize work traffic and limit guest network bandwidth.
* Remote access via VPN.

**MikroTik Requirements:**
* Stable and secure internet connection.
* Reliable internal network connectivity.
* Flexible network segmentation using VLANs.
* Control over bandwidth usage.
* Secure remote access.
* Centralized logging and monitoring.

## 2. Step-by-Step Implementation (CLI & Winbox)

This section provides a step-by-step guide for configuring the specified scenario, both using the CLI and Winbox. We'll focus on core IP addressing and move outward from there.

### Step 1: Basic IP Configuration

**CLI:**

```routeros
# Disable default configuration
/system reset-configuration no-defaults=yes

# Set router identity
/system identity set name=SOHO-Router

# Set timezone
/system clock set time-zone-name=America/New_York

# Configure WAN interface (assuming it's ether1 and gets DHCP address)
/ip dhcp-client add interface=ether1 disabled=no

# Configure LAN interface (ether2) with IPv4
/ip address add address=192.168.88.1/24 interface=ether2 network=192.168.88.0

# Enable IPv6 forwarding
/ipv6 settings set forwarding=yes

# Configure IPv6 DHCP client on WAN interface
/ipv6 dhcp-client add interface=ether1 request=prefix use-peer-dns=yes add-default-route=yes

# Configure a IPv6 address on the LAN interface within the assigned subnet
/ipv6 address add address=::1/64 interface=ether2 eui-64=no
```

**Winbox:**
1. System -> Reset Configuration -> Check "No Default Configuration" -> Reset.
2. System -> Identity -> Set "Name" to "SOHO-Router".
3. System -> Clock -> set timezone.
4. IP -> DHCP Client -> Add -> Interface "ether1" (make sure it has "Use Peer DNS" ticked and is enabled.
5. IP -> Addresses -> Add -> Address: `192.168.88.1/24`, Interface: `ether2`.
6. IPv6 -> Settings -> Tick "Forwarding".
7. IPv6 -> DHCP Client -> Add -> Interface `ether1`, set "Request" to "Prefix" and tick "Add Default Route".
8. IPv6 -> Addresses -> Add -> Address: `::1/64`, Interface: `ether2`.

**Explanation:**
* `/system reset-configuration`: This command clears any existing configuration
* `/system identity`: Sets the name of the router for easier identification.
* `/ip dhcp-client`: Sets the WAN interface to obtain an IP address from a DHCP server.
* `/ip address`: Configures a static IPv4 address on the LAN interface.
* `/ipv6 settings set forwarding=yes` enables IPv6 forwarding, which is needed for routing IPv6 traffic.
* `/ipv6 dhcp-client` enables the router to receive an IPv6 address and a prefix from the ISP using DHCPv6.
* `/ipv6 address`: Configures an IPv6 address on the LAN interface.

### Step 2: Creating an IP Pool

**CLI:**

```routeros
/ip pool add name=lan-pool ranges=192.168.88.10-192.168.88.254
```

**Winbox:**
1. IP -> Pool -> Add -> Name `lan-pool`, Ranges `192.168.88.10-192.168.88.254`

**Explanation:**
* `/ip pool`: Defines an IP address pool to be used by a DHCP server.

### Step 3: Setting up DHCP Server

**CLI:**

```routeros
/ip dhcp-server add address-pool=lan-pool interface=ether2 lease-time=1d name=lan-dhcp disabled=no
/ip dhcp-server network add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1
```

**Winbox:**
1. IP -> DHCP Server -> Add -> Interface `ether2`, Name `lan-dhcp`, Lease Time `1d`, Address Pool: `lan-pool`.
2. IP -> DHCP Server -> Network -> Add -> Address `192.168.88.0/24`, Gateway `192.168.88.1`, DNS Servers: `192.168.88.1`

**Explanation:**
* `/ip dhcp-server`: Configures the DHCP server to assign IP addresses to devices on the LAN network.
* `/ip dhcp-server network`: Defines the network properties for the DHCP server.

### Step 4: Basic Firewall Configuration

**CLI:**

```routeros
/ip firewall filter
add chain=input action=accept connection-state=established,related comment="Accept Established and Related"
add chain=input action=accept protocol=icmp comment="Allow ICMP"
add chain=input action=drop in-interface-list=WAN comment="Drop all other inputs from WAN"
add chain=forward action=accept connection-state=established,related comment="Accept established forward"
add chain=forward action=drop connection-state=invalid comment="Drop invalid forward"
add chain=forward action=accept src-address=192.168.88.0/24 comment="Allow LAN Forward"
add chain=forward action=drop comment="Drop all other forward"

/ip firewall nat add chain=srcnat action=masquerade out-interface=ether1 comment="Masquerade traffic on WAN"

/ipv6 firewall filter
add chain=input action=accept connection-state=established,related comment="Accept established IPv6 connections"
add chain=input action=accept protocol=icmpv6 comment="Allow ICMPv6"
add chain=input action=drop in-interface-list=WAN comment="Drop other IPv6 inputs from WAN"
add chain=forward action=accept connection-state=established,related comment="Accept established IPv6 forward"
add chain=forward action=drop connection-state=invalid comment="Drop invalid IPv6 forward"
add chain=forward action=accept src-address=::/64 comment="Allow LAN IPv6 Forward"
add chain=forward action=drop comment="Drop all other IPv6 forward"

/ipv6 firewall nat add chain=srcnat out-interface=ether1 action=masquerade comment="Masquerade IPv6 traffic on WAN"

/interface list add name=WAN
/interface list member add interface=ether1 list=WAN
```

**Winbox:**
1. IP -> Firewall -> Filter Rules -> Add a new rule for each line in the CLI version.
2. IP -> Firewall -> NAT -> Add a rule for masquerading.
3. IPv6 -> Firewall -> Filter Rules -> Add a new rule for each line in the CLI version.
4. IPv6 -> Firewall -> NAT -> Add a rule for masquerading.
5. Interface -> Lists -> Add `WAN` List.
6. Interface -> Lists -> Member -> Add `ether1` to `WAN` List.

**Explanation:**
* `/ip firewall filter`: Defines firewall rules for IPv4 traffic, allowing established and related connections and ICMP, and dropping other inputs and forwarded traffic from outside.
* `/ip firewall nat`: Configures NAT for the network, allowing private addresses to access the internet.
* `/ipv6 firewall filter`: Defines firewall rules for IPv6 traffic, similarly to IPv4.
* `/ipv6 firewall nat`: Configures NAT6 for IPv6, although it's not always needed and may not apply to your situation, we include for completeness.
* `/interface list`: Defines a list to be used in firewall rules.

### Step 5: Verifying the Setup

Use `ping` from the router terminal:
```routeros
/ping 8.8.8.8
/ipv6 ping 2001:4860:4860::8888
```

Use `traceroute` to check internet path:
```routeros
/tool traceroute 8.8.8.8
/ipv6 tool traceroute 2001:4860:4860::8888
```
On a client on the LAN, check IP address is within the DHCP range, and test internet connectivity.

## 3. Complete CLI Configuration Commands

Here's a breakdown of common commands used, with parameters.

### IP Address Configuration

```routeros
/ip address
  add address=<ip_address/prefix> interface=<interface_name> \
    network=<network_address> disabled=[yes|no] comment=<comment>
  remove <id>
  set <id> disabled=[yes|no] address=<ip_address/prefix> interface=<interface_name> \
    network=<network_address> comment=<comment>
  print
```

| Parameter       | Description                                               |
|-----------------|-----------------------------------------------------------|
| `address`       | The IP address and prefix length. (e.g., 192.168.1.100/24)   |
| `interface`     | The network interface the address is assigned to. (e.g., ether2)|
| `network`        | The network address for the subnet.  (e.g., 192.168.1.0)       |
| `disabled`      | Enable or disable the address.                           |
| `comment`       | A descriptive note for the address.                       |
| `remove <id>` | Removes the address with the specified id. |
| `set <id>` | Modifies an existing address, using the given id.|

### IP Pools

```routeros
/ip pool
  add name=<pool_name> ranges=<start_ip>-<end_ip> comment=<comment>
  remove <id>
  set <id> ranges=<start_ip>-<end_ip> comment=<comment> name=<pool_name>
  print
```

| Parameter    | Description                                       |
|--------------|---------------------------------------------------|
| `name`       | The name of the IP pool.                             |
| `ranges`     | The range of IP addresses in the pool. (e.g., 192.168.1.10-192.168.1.20) |
| `comment`   | A descriptive note for the pool.                 |
| `remove <id>`| Removes the pool with the specified id.           |
| `set <id>` | Modifies an existing pool, using the given id.   |

### IP DHCP Server

```routeros
/ip dhcp-server
  add address-pool=<pool_name> interface=<interface_name> lease-time=<lease_time> \
    name=<server_name> disabled=[yes|no] comment=<comment>
  remove <id>
  set <id> disabled=[yes|no] address-pool=<pool_name> interface=<interface_name> \
    lease-time=<lease_time> comment=<comment> name=<server_name>
  print

/ip dhcp-server network
  add address=<network_address/prefix> gateway=<gateway_ip> \
    dns-server=<dns_server_ip1,dns_server_ip2,...> comment=<comment>
  remove <id>
  set <id> address=<network_address/prefix> gateway=<gateway_ip> \
    dns-server=<dns_server_ip1,dns_server_ip2,...> comment=<comment>
  print
```

| Parameter       | Description                                              |
|-----------------|----------------------------------------------------------|
| `address-pool`  | The name of the IP pool to use for DHCP.                      |
| `interface`     | The network interface to listen on for DHCP requests.      |
| `lease-time`   | How long an IP address is leased to a client (e.g. 1d, 12h).|
| `name`          | The name of the DHCP server instance.                     |
| `disabled`      | Enable or disable the server.                            |
| `comment`      | A descriptive note for the server.                     |
| `network`       | The network address and prefix length to use with this server|
| `gateway`       | The router's IP for the given network. |
| `dns-server`   | A list of DNS servers to give to clients, or comma separated. |
| `remove <id>` | Removes the dhcp server or network with specified id. |
| `set <id>` | Modifies an existing dhcp server or network, using the given id. |

### IPv6 Address Configuration

```routeros
/ipv6 address
  add address=<ipv6_address/prefix> interface=<interface_name> eui-64=[yes|no] disabled=[yes|no] comment=<comment>
  remove <id>
  set <id> disabled=[yes|no] address=<ipv6_address/prefix> interface=<interface_name> eui-64=[yes|no] comment=<comment>
  print
```
| Parameter       | Description                                               |
|-----------------|-----------------------------------------------------------|
| `address`       | The IPv6 address and prefix length. (e.g., 2001::1/64)   |
| `interface`     | The network interface the address is assigned to. (e.g., ether2)|
| `eui-64` | When set to "yes", will form the host address part from the interfaces MAC address.        |
| `disabled`      | Enable or disable the address.                           |
| `comment`       | A descriptive note for the address.                       |
| `remove <id>` | Removes the address with the specified id. |
| `set <id>` | Modifies an existing address, using the given id.|

### IPv6 DHCP Client
```routeros
/ipv6 dhcp-client
 add interface=<interface_name> request=[address|prefix] use-peer-dns=[yes|no] add-default-route=[yes|no] disabled=[yes|no] comment=<comment>
 remove <id>
 set <id> disabled=[yes|no] request=[address|prefix] use-peer-dns=[yes|no] add-default-route=[yes|no] comment=<comment>
 print
```
| Parameter       | Description                                               |
|-----------------|-----------------------------------------------------------|
| `interface`     | The network interface the DHCP client is assigned to. (e.g., ether1)|
| `request` | Whether to request only an address, or also a prefix.        |
| `use-peer-dns`      | Whether to use the DNS advertised by the DHCP server.                           |
| `add-default-route`       | Whether to add the gateway advertised by the DHCP server.                       |
| `disabled`      | Enable or disable the client.                           |
| `comment`       | A descriptive note for the client.                       |
| `remove <id>` | Removes the client with the specified id. |
| `set <id>` | Modifies an existing client, using the given id.|

### Firewall Filter Rules

```routeros
/ip firewall filter
  add chain=<chain_name> action=[accept|drop|reject] protocol=[tcp|udp|icmp] \
    src-address=<ip_address/prefix> dst-address=<ip_address/prefix> \
    in-interface-list=<list_name> out-interface-list=<list_name> \
    connection-state=[established|related|invalid|new] comment=<comment>

  remove <id>
  set <id> disabled=[yes|no] chain=<chain_name> action=[accept|drop|reject] protocol=[tcp|udp|icmp] \
    src-address=<ip_address/prefix> dst-address=<ip_address/prefix> \
    in-interface-list=<list_name> out-interface-list=<list_name> \
    connection-state=[established|related|invalid|new] comment=<comment>
    print
```

| Parameter           | Description                                               |
|---------------------|-----------------------------------------------------------|
| `chain`            | The firewall chain to apply to (e.g., input, forward, output). |
| `action`           | The action to take for matched packets.     |
| `protocol`         | The IP protocol (e.g., tcp, udp, icmp).                  |
| `src-address`      | The source IP address or range (optional).           |
| `dst-address`      | The destination IP address or range (optional).        |
| `in-interface-list`| Match the input interface, to the specified list. |
| `out-interface-list` | Match the output interface to the specified list.  |
|`connection-state` | The connection state to match |
| `comment`           | A descriptive note for the rule.                       |
| `remove <id>` | Removes the filter with the specified id. |
| `set <id>` | Modifies an existing filter, using the given id. |

### Firewall NAT Rules

```routeros
/ip firewall nat
 add chain=<chain_name> action=[masquerade|src-nat|dst-nat] \
 out-interface=<interface_name> src-address=<ip_address/prefix> dst-address=<ip_address/prefix> to-address=<ip_address>
 comment=<comment>
 remove <id>
 set <id> disabled=[yes|no] chain=<chain_name> action=[masquerade|src-nat|dst-nat] \
 out-interface=<interface_name> src-address=<ip_address/prefix> dst-address=<ip_address/prefix> to-address=<ip_address>
 comment=<comment>
 print
```
| Parameter | Description |
|--|--|
| `chain`  | The chain to which the rule is applied (srcnat/dstnat)|
| `action` | Which action to take when the rule is matched (masquerade, src-nat, dst-nat)|
| `out-interface` | The output interface to be matched|
| `src-address` | The source address to be matched|
| `dst-address` | The destination address to be matched|
|`to-address` | When performing a source or destination NAT, this is the new IP to send to|
|`comment` | A descriptive comment for the rule|
| `remove <id>` | Removes the NAT rule with the specified id. |
| `set <id>` | Modifies an existing NAT rule, using the given id. |

## 4. Common Pitfalls, Troubleshooting, and Diagnostics

* **Incorrect Interface:** Double-check that IP addresses and DHCP servers are assigned to the correct interfaces. Winbox can help visualize the network interfaces, and `/interface print` in CLI can help you determine if the interface has the correct status.
* **Firewall Blocking:** Firewall rules that are too restrictive can block essential services. Use the `torch` tool under `/tool torch` to see which rules are being applied to a given traffic flow, if you are suspicious of your firewall rules.
* **DHCP Issues:** If clients don't receive IP addresses, check that the DHCP server is enabled, running on the correct interface, and with valid IP pool ranges configured. Use the `/ip dhcp-server leases print` to view the current leases provided by the server.
* **DNS Problems:** If the DHCP server does not have DNS servers configured, clients may be unable to resolve hostnames. If using the router as the DNS server, ensure the `/ip dns` setting is configured correctly.
* **IPv6 Prefix Issues:** Ensure that your IPv6 DHCP client is correctly configured to request a prefix. If the prefix changes, it could cause issues if you have manually configured addresses on the network, as the prefix and address will no longer be correct for the local IPv6 network. You may need to remove your addresses and re-add them, or consider using SLAAC for your network instead of manual addressing.
* **NAT Problems:** Incorrect NAT rules will prevent local machines from accessing the internet. Use the `/ip firewall nat print` command to review all NAT rules, and ensure you are masquerading traffic from your local network that is going out the correct public interface.
* **Routing Issues:** When having multiple routers or gateways, if machines are unable to communicate with each other, check the routing tables using `/ip route print` to verify that traffic is taking the correct path.
* **Resource Exhaustion:** During periods of heavy traffic or under attack, a MikroTik can experience resource exhaustion, manifesting as slow performance, dropped packets, and frequent reboots. Use `/system resource print` to monitor the resource usage of your router.

**Diagnostics Tools:**
* `/ping`: Test connectivity to IP addresses and hostnames.
* `/traceroute`: Trace the network path of a packet.
* `/tool torch`: Real-time packet sniffing tool.
* `/log print`: View system logs for errors and warnings.
* `/interface ethernet monitor <interface_name>`: Monitor specific interface statistics.

## 5. Verification and Testing

1.  **Basic Connectivity:**
    *   `ping` from the router to 8.8.8.8 (IPv4) and `ipv6 ping 2001:4860:4860::8888` (IPv6)
    *   `ping` from a LAN client to the router's LAN IP.
    *   `ping` from a LAN client to 8.8.8.8 and `ipv6 ping 2001:4860:4860::8888`
2.  **DHCP Functionality:**
    *   Ensure that a client connected to the LAN interface is obtaining an IP address within the configured range.
    *   Verify that the correct gateway and DNS servers are being assigned.
3. **Firewall Effectiveness**
	* Try to ping a machine on the LAN from the internet, it should be dropped.
	* Ensure that the internet is available from your LAN clients.
4. **NAT Effectiveness**
	* Use a site like whatsmyip.org to verify that your internet traffic is using your routers IP address.
5.  **Traceroute:**
    *   Run traceroute from a client to 8.8.8.8 and `ipv6 tool traceroute 2001:4860:4860::8888`, observe the hops.
6.  **Torch:**
    *   Use torch to monitor traffic on the WAN interface to identify if a specific client is causing a lot of traffic.

## 6. Related MikroTik Features, Capabilities, and Limitations

*   **IP Address Assignment Modes:** DHCP, Static, PPPoE, etc. MikroTik supports various methods for assigning IP addresses.
*   **IP Aliasing:** Multiple IP addresses on a single interface.
*   **Virtual Interfaces:** VLANs, EoIP, IPIP, Wireguard, etc.
*   **Policy-Based Routing:** Route traffic based on source or destination IP, protocol, and other factors.
*   **Connection Tracking:** The firewall relies on connection tracking, which needs to be taken into account when using the firewall with complex setups, such as source or destination NAT, where you may need to perform certain configurations in the raw chain.
*   **Layer 7 Firewall Rules:** Inspecting packet data up to the application layer.
*  **Routing Protocols:** Supports BGP, OSPF, RIP, and other dynamic routing protocols.
*   **IPv6 Capabilities:** Full IPv6 support, including DHCPv6, SLAAC, routing protocols and more.
*   **Resource Limits:** Some MikroTik models have limitations in memory, CPU, and interface speeds, which may become a bottleneck in demanding setups. The resource usage should be considered when creating complex setups, and the appropriate model selected to handle the resource usage requirements of the network.

## 7. MikroTik REST API Examples

MikroTik provides a REST API for managing the router. Here are some examples using HTTP requests. You may require setting up a user with API permissions, and have HTTPS enabled on your router. These also require the `tool fetch` command, or another external application capable of making an HTTP request.

**Note:** These API calls require a user with full API permissions. Replace `192.168.88.1` with the router's IP.

### Get IP Addresses

```routeros
/tool fetch url="https://192.168.88.1/rest/ip/address" user=api_user password=api_password http-header-field="Content-Type: application/json"
:put $[/tool fetch get body]
```

**Expected JSON response:**
```json
[
  {
    ".id": "*0",
    "address": "192.168.88.1/24",
    "interface": "ether2",
    "network": "192.168.88.0",
    "disabled": false,
    "dynamic": false
  },
 {
    ".id": "*1",
    "address": "10.0.1.120/32",
    "interface": "ether1",
    "network": "10.0.1.120",
    "disabled": false,
    "dynamic": true
  }
]
```

### Add a new Address

```routeros
/tool fetch url="https://192.168.88.1/rest/ip/address" user=api_user password=api_password \
    http-method=post http-header-field="Content-Type: application/json" \
     http-data='{"address": "192.168.88.200/24", "interface": "ether2"}'
:put $[/tool fetch get body]
```

**Expected JSON response:**

```json
{ ".id": "*1", "address": "192.168.88.200/24", "interface": "ether2", "dynamic": false }
```

### Update Address
```routeros
/tool fetch url="https://192.168.88.1/rest/ip/address/*0" user=api_user password=api_password \
    http-method=patch http-header-field="Content-Type: application/json" \
     http-data='{"address": "192.168.88.5/24"}'
:put $[/tool fetch get body]
```

**Expected JSON response:**
```json
{ ".id": "*0", "address": "192.168.88.5/24", "interface": "ether2", "dynamic": false }
```

### Delete Address

```routeros
/tool fetch url="https://192.168.88.1/rest/ip/address/*1" user=api_user password=api_password http-method=delete
:put $[/tool fetch get body]
```

**Expected response (empty string on successful deletion):**
```
""
```

## 8. Core Concepts & MikroTik Implementation

*   **Bridging:** Combines multiple interfaces into a single logical interface (a switch). In RouterOS, bridge interfaces can have IPs assigned to them, and operate at Layer 2. VLANs can be added to a bridge, in either a trunked or access config.
*   **Routing:** Packet forwarding between networks using IP addresses. MikroTik's routing engine is highly flexible, supporting static routes, dynamic routing, policy routing, and VRFs, and is extremely configurable, including route filtering and multi-path routing using BFD.
*   **Firewall:** Packet filtering based on source/destination IP, ports, protocols, and connection state. RouterOS firewall can filter Layer 3 & 4 data. Layer 7 filters can inspect higher level data, such as http headers.
* **Quality of Service:** Using queues to prioritize traffic. RouterOS has a variety of queue options, such as simple queues, queue trees, PCQ, and HTB, offering a comprehensive suite of tools for implementing QoS on your network.
* **Connection Tracking:** The RouterOS firewall maintains a stateful connection tracking table, which is used to determine if a packet is a part of a new, existing, or invalid connection. The connection tracker should be taken into account when creating firewall rules.

## 9. Security Best Practices

*   **Change Default Credentials:** Change the default admin password immediately.
*   **Disable Unused Services:** Disable unnecessary services like SSH, Telnet, and API access on all interfaces except those you need to administer the device.
*   **Firewall:** Create a comprehensive firewall to limit access to the router and network from outside.
*   **HTTPS for API:** Use HTTPS for accessing the API.
*   **VPN for Remote Access:** Use a VPN (IPsec, WireGuard) for remote access to the router.
*   **Regular Updates:** Update RouterOS regularly to patch vulnerabilities.
*   **Access Control:** Use a separate user for API access, giving only the permissions required for API access to that user.
*   **Limit Winbox Access:** Restrict Winbox access to specific IP addresses, and consider not exposing the port to the internet.
*   **Strong Passwords:** Use strong, unique passwords for all users.
*   **Review Logs:** Regularly review system logs for any suspicious activity.
*   **Limit Exposure:** Restrict access to services on the router (such as winbox, api access, or ssh) to only the interfaces you need to access them from.

## 10. Detailed Explanations and Configurations

This section contains a detailed explanation of each of the requested topics, including configurations, and examples.

### IP Addressing (IPv4 and IPv6)

* **IPv4:**
    * Uses a 32-bit address, commonly represented in dotted decimal form (e.g., 192.168.1.1).
    * Divided into private (RFC1918) and public address ranges.
    * Subnetting uses CIDR notation (e.g., /24 represents 255.255.255.0).
    * Configuration in MikroTik is done using the `/ip address` command, which can be configured on any interface, such as physical interfaces, VLAN interfaces, bridge interfaces and virtual interfaces.
* **IPv6:**
    * Uses a 128-bit address, typically written in hexadecimal notation (e.g., 2001:0db8::1).
    * The IPv6 address is typically divided into two parts, the network prefix and the interface ID.
    * Supports various addressing types, including global unicast, link-local, and multicast.
    * Configured in MikroTik using the `/ipv6 address` command, which also can be configured on a variety of interfaces.
    * Automatic address configuration via SLAAC is also supported on RouterOS, as well as DHCPv6.
*   **Configuration Examples:**
    *   Static IPv4 address: `/ip address add address=192.168.1.100/24 interface=ether2`
    *   Static IPv6 address: `/ipv6 address add address=2001:0db8::1/64 interface=ether2`
    *  DHCPv4: `/ip dhcp-client add interface=ether1`
    *  DHCPv6: `/ipv6 dhcp-client add interface=ether1 request=prefix`

### IP Pools

*   **Purpose:** A range of IP addresses, used by DHCP servers, or for other tasks, like setting up static mapping.
*   **Creation:** Defined using the `/ip pool` command.
*   **Usage:** IP pools are assigned to DHCP servers, but may also be assigned to other features such as static mappings, and IPsec policy assignment.
*  **Example:** `/ip pool add name=my-pool ranges=192.168.10.10-192.168.10.100`

### IP Routing

*   **Static Routes:** Manually defined routes, such as those you would configure for a site-to-site VPN, or for routing traffic to a VLAN.
    *   Command: `/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2`
*   **Dynamic Routing:** Using protocols like OSPF, RIP, and BGP, to learn routes automatically.
    *  OSPF:
        1.  `/routing ospf instance add name=my-ospf`
        2. `/routing ospf interface add interface=ether2 instance=my-ospf`
        3. `/routing ospf network add network=192.168.1.0/24 instance=my-ospf`
*   **Policy-Based Routing (PBR):** Route traffic based on criteria other than the destination IP, such as the source address, or routing mark.
    *   Command:
        1. `/ip route rule add src-address=192.168.10.0/24 action=lookup-only-in-table table=vlan10`
        2. `/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.2 table=vlan10`
*   **VRF (Virtual Routing and Forwarding):** Allows multiple independent routing tables on the same router.
    *   Command:
        1.  `/routing vrf add name=vrf1`
        2.  `/ip address add interface=ether2 vrf=vrf1 address=10.10.10.1/24`
        3.  `/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.2 vrf=vrf1`
*   **Routing Table:**
    *   View the routing table: `/ip route print`
    *   Routing table also supports IPv6: `/ipv6 route print`
*   **Route Filters:**
    * Routes can be filtered in the routing table. You may use filter chains for more complicated routing configurations. This allows you to dynamically modify and filter routes, as they are being learned or imported into the routing table. This is very useful when you are learning routes from multiple routers using dynamic routing protocols such as BGP or OSPF.
*   **Route Selection:** The process of selecting a best route, based on the AD value of the various routes being learned. The lower the AD value, the better. If two routes have the same AD value, then the route with the lowest metric will be the best route. If both routes have the same metric, the route with the lower IP will be selected.
*   **Multi-path Routing:** Supports multiple routes to the same destination, and can perform load balancing between the available routes, depending on the routing protocol being used.

### IP Settings

*   **General Settings:**
    *   `forwarding`: Enable