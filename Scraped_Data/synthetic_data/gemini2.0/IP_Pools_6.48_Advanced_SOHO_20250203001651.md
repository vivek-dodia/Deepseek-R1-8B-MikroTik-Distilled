Okay, let's dive into a comprehensive exploration of IP Pools on MikroTik RouterOS, framed within your SOHO environment and advanced configuration requirements. This document will be expansive to cover everything you asked for.

## MikroTik RouterOS: Advanced IP Pool Management

### 1. Comprehensive Configuration Scenario and Specific MikroTik Requirements

**Scenario:**

We're designing a SOHO network for a small office with the following requirements:

*   **Multiple VLANs:** We'll use VLANs to segment our network: one for trusted internal devices, one for guests, and one for servers.
*   **Dynamic IP Assignment:** We'll use DHCP servers to automatically assign IP addresses to devices in each VLAN.
*   **Static IP Assignments:** We'll assign static IP addresses for servers using static leases.
*   **Multiple Address Ranges:** We'll need distinct IP address ranges for each VLAN.
*   **Future Growth:**  Our IP pool setup should be scalable for future device growth.
*   **IPv6 Support:** We'll ensure IPv6 addresses are also assigned.
*   **Secure Configuration:** We'll implement security best practices for our setup.

**MikroTik Requirements:**

*   RouterOS version 6.48 or above (compatible with 6.x and 7.x)
*   Support for VLANs
*   Support for DHCP servers
*   Support for IPv4 and IPv6 addressing
*   Ability to create and manage IP pools effectively
*   Secure and reliable network operation

### 2. Step-by-Step MikroTik Implementation using CLI/Winbox

Here's a step-by-step guide using both CLI and Winbox with detailed explanations. We'll start with the CLI and illustrate equivalent Winbox screens:

**Step 1: Network Topology Planning**

Before configuring our router, let's plan the network with address ranges:

| VLAN ID | Name           | Interface | IPv4 Address Range | IPv4 Gateway | IPv6 Address Range                                      | IPv6 Gateway |
|---------|----------------|------------|-------------------|--------------|-------------------------------------------------------|--------------|
| 10      | Internal       | ether2    | 192.168.10.0/24    | 192.168.10.1 | 2001:db8:10::/64                                    | 2001:db8:10::1 |
| 20      | Guest          | ether3    | 192.168.20.0/24    | 192.168.20.1 | 2001:db8:20::/64                                    | 2001:db8:20::1 |
| 30      | Server         | ether4    | 192.168.30.0/24    | 192.168.30.1 | 2001:db8:30::/64                                    | 2001:db8:30::1 |

**Step 2: VLAN Configuration (CLI)**

```mikrotik
/interface vlan
add interface=ether2 name=vlan10 vlan-id=10
add interface=ether3 name=vlan20 vlan-id=20
add interface=ether4 name=vlan30 vlan-id=30
```

**Winbox equivalent:**

*   Go to *Interfaces -> VLAN*
*   Add a new VLAN interface:
    *   *Name:* vlan10
    *   *VLAN ID:* 10
    *   *Interface:* ether2
    *   Click *Apply* and *OK*.
*   Repeat for `vlan20` (interface ether3, VLAN ID 20) and `vlan30` (interface ether4, VLAN ID 30).

**Step 3: IP Address Assignment to VLAN Interfaces (CLI)**

```mikrotik
/ip address
add address=192.168.10.1/24 interface=vlan10
add address=192.168.20.1/24 interface=vlan20
add address=192.168.30.1/24 interface=vlan30
add address=2001:db8:10::1/64 interface=vlan10
add address=2001:db8:20::1/64 interface=vlan20
add address=2001:db8:30::1/64 interface=vlan30
```

**Winbox equivalent:**

*   Go to *IP -> Addresses*
*   Add a new IP address:
    *   *Address:* 192.168.10.1/24
    *   *Interface:* vlan10
    *   Click *Apply* and *OK*.
*   Repeat for `192.168.20.1/24` (interface `vlan20`), `192.168.30.1/24` (interface `vlan30`), `2001:db8:10::1/64` (interface `vlan10`), `2001:db8:20::1/64` (interface `vlan20`) and `2001:db8:30::1/64` (interface `vlan30`).

**Step 4: Creating IP Pools (CLI)**

```mikrotik
/ip pool
add name=pool-vlan10 ranges=192.168.10.10-192.168.10.254
add name=pool-vlan20 ranges=192.168.20.10-192.168.20.254
add name=pool-vlan30 ranges=192.168.30.10-192.168.30.254
add name=ipv6-pool-vlan10 ranges=2001:db8:10::10-2001:db8:10::ffff
add name=ipv6-pool-vlan20 ranges=2001:db8:20::10-2001:db8:20::ffff
add name=ipv6-pool-vlan30 ranges=2001:db8:30::10-2001:db8:30::ffff
```

**Winbox equivalent:**

*   Go to *IP -> Pool*
*   Add a new Pool:
    *   *Name:* pool-vlan10
    *   *Ranges:* 192.168.10.10-192.168.10.254
    *    Click *Apply* and *OK*.
*   Repeat for `pool-vlan20` (ranges: `192.168.20.10-192.168.20.254`), `pool-vlan30` (ranges: `192.168.30.10-192.168.30.254`), `ipv6-pool-vlan10` (ranges: `2001:db8:10::10-2001:db8:10::ffff`), `ipv6-pool-vlan20` (ranges: `2001:db8:20::10-2001:db8:20::ffff`) and `ipv6-pool-vlan30` (ranges: `2001:db8:30::10-2001:db8:30::ffff`).

**Step 5: Configuring DHCP Servers (CLI)**

```mikrotik
/ip dhcp-server
add address-pool=pool-vlan10 interface=vlan10 lease-time=10m name=dhcp-vlan10
add address-pool=pool-vlan20 interface=vlan20 lease-time=10m name=dhcp-vlan20
add address-pool=pool-vlan30 interface=vlan30 lease-time=10m name=dhcp-vlan30

/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=1.1.1.1,8.8.8.8 dhcp-server=dhcp-vlan10
add address=192.168.20.0/24 gateway=192.168.20.1 dns-server=1.1.1.1,8.8.8.8 dhcp-server=dhcp-vlan20
add address=192.168.30.0/24 gateway=192.168.30.1 dns-server=1.1.1.1,8.8.8.8 dhcp-server=dhcp-vlan30

/ipv6 dhcp-server
add address-pool=ipv6-pool-vlan10 interface=vlan10 name=dhcp6-vlan10
add address-pool=ipv6-pool-vlan20 interface=vlan20 name=dhcp6-vlan20
add address-pool=ipv6-pool-vlan30 interface=vlan30 name=dhcp6-vlan30

/ipv6 dhcp-server network
add address=2001:db8:10::/64 dns-server=2606:4700:4700::1111,2001:4860:4860::8888 dhcp-server=dhcp6-vlan10
add address=2001:db8:20::/64 dns-server=2606:4700:4700::1111,2001:4860:4860::8888 dhcp-server=dhcp6-vlan20
add address=2001:db8:30::/64 dns-server=2606:4700:4700::1111,2001:4860:4860::8888 dhcp-server=dhcp6-vlan30
```

**Winbox equivalent:**

*   Go to *IP -> DHCP Server*
*   Add a new DHCP Server:
    *   *Name:* dhcp-vlan10
    *   *Interface:* vlan10
    *   *Address Pool:* pool-vlan10
    *   *Lease Time:* 10m
    *   Click *Apply* and *OK*.
*   Repeat for `dhcp-vlan20` (interface `vlan20`, address pool `pool-vlan20`), `dhcp-vlan30` (interface `vlan30`, address pool `pool-vlan30`).
*   Go to the *Networks* Tab and add new Networks for each DHCP Server, selecting the right server from the drop-down. Add `192.168.10.0/24`, `192.168.20.0/24` and `192.168.30.0/24`, with corresponding gateways and DNS Server entries.
*   Go to *IPv6 -> DHCP Server*.
*    Add a new DHCPv6 Server:
    *   *Name:* dhcp6-vlan10
    *   *Interface:* vlan10
    *   *Address Pool:* ipv6-pool-vlan10
    *   Click *Apply* and *OK*.
*   Repeat for `dhcp6-vlan20` (interface `vlan20`, address pool `ipv6-pool-vlan20`), `dhcp6-vlan30` (interface `vlan30`, address pool `ipv6-pool-vlan30`).
*   Go to *IPv6 -> DHCP Server -> Networks* and add new networks for `2001:db8:10::/64`, `2001:db8:20::/64`, and `2001:db8:30::/64` with corresponding DNS server entries.

**Step 6: Static Lease Assignment for Servers (CLI)**

```mikrotik
/ip dhcp-server lease
add address=192.168.30.10 mac-address=00:11:22:33:44:55 server=dhcp-vlan30
add address=192.168.30.11 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-vlan30
```

**Winbox equivalent:**

*   Go to *IP -> DHCP Server -> Leases*
*   Click the blue plus to add a new static lease
    *   *Address:* 192.168.30.10
    *   *MAC Address:* `00:11:22:33:44:55`
    *   *Server:* dhcp-vlan30
    *   Click *Apply* and *OK*.
*   Repeat for `192.168.30.11` with MAC `AA:BB:CC:DD:EE:FF`.

### 3. Complete MikroTik CLI Configuration Commands

The complete CLI configuration is as follows:

```mikrotik
/interface vlan
add interface=ether2 name=vlan10 vlan-id=10
add interface=ether3 name=vlan20 vlan-id=20
add interface=ether4 name=vlan30 vlan-id=30

/ip address
add address=192.168.10.1/24 interface=vlan10
add address=192.168.20.1/24 interface=vlan20
add address=192.168.30.1/24 interface=vlan30
add address=2001:db8:10::1/64 interface=vlan10
add address=2001:db8:20::1/64 interface=vlan20
add address=2001:db8:30::1/64 interface=vlan30

/ip pool
add name=pool-vlan10 ranges=192.168.10.10-192.168.10.254
add name=pool-vlan20 ranges=192.168.20.10-192.168.20.254
add name=pool-vlan30 ranges=192.168.30.10-192.168.30.254
add name=ipv6-pool-vlan10 ranges=2001:db8:10::10-2001:db8:10::ffff
add name=ipv6-pool-vlan20 ranges=2001:db8:20::10-2001:db8:20::ffff
add name=ipv6-pool-vlan30 ranges=2001:db8:30::10-2001:db8:30::ffff

/ip dhcp-server
add address-pool=pool-vlan10 interface=vlan10 lease-time=10m name=dhcp-vlan10
add address-pool=pool-vlan20 interface=vlan20 lease-time=10m name=dhcp-vlan20
add address-pool=pool-vlan30 interface=vlan30 lease-time=10m name=dhcp-vlan30

/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=1.1.1.1,8.8.8.8 dhcp-server=dhcp-vlan10
add address=192.168.20.0/24 gateway=192.168.20.1 dns-server=1.1.1.1,8.8.8.8 dhcp-server=dhcp-vlan20
add address=192.168.30.0/24 gateway=192.168.30.1 dns-server=1.1.1.1,8.8.8.8 dhcp-server=dhcp-vlan30

/ip dhcp-server lease
add address=192.168.30.10 mac-address=00:11:22:33:44:55 server=dhcp-vlan30
add address=192.168.30.11 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-vlan30

/ipv6 dhcp-server
add address-pool=ipv6-pool-vlan10 interface=vlan10 name=dhcp6-vlan10
add address-pool=ipv6-pool-vlan20 interface=vlan20 name=dhcp6-vlan20
add address-pool=ipv6-pool-vlan30 interface=vlan30 name=dhcp6-vlan30

/ipv6 dhcp-server network
add address=2001:db8:10::/64 dns-server=2606:4700:4700::1111,2001:4860:4860::8888 dhcp-server=dhcp6-vlan10
add address=2001:db8:20::/64 dns-server=2606:4700:4700::1111,2001:4860:4860::8888 dhcp-server=dhcp6-vlan20
add address=2001:db8:30::/64 dns-server=2606:4700:4700::1111,2001:4860:4860::8888 dhcp-server=dhcp6-vlan30
```

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Incorrect Interface Binding:** DHCP servers not bound to the correct VLAN interfaces.
*   **IP Overlap:** IP address ranges for different networks overlapping.
*   **Firewall Blocking DHCP:** The firewall might be blocking DHCP requests.
*   **Incorrect Pool Ranges:** DHCP pools not matching the network address ranges.
*   **Misconfigured DNS:** Clients not receiving correct DNS server settings from DHCP.
*   **Incorrect Gateway:** DHCP not sending the correct gateway address.

**Troubleshooting:**

*   **Check Interface Status:** Ensure interfaces are enabled and operational using `/interface print`.
*   **Verify IP Addresses:** Confirm interface IP addresses with `/ip address print`.
*   **DHCP Server Status:** Check the DHCP server status with `/ip dhcp-server print` and `/ip dhcp-server lease print`.
*   **DHCP Lease Log:** Monitor DHCP lease assignments in `/log print topics=dhcp`.
*   **Firewall Rules:** Use `/ip firewall filter print` to examine firewall rules.
*   **Connectivity Tests:** Use `ping` and `traceroute` from the router and connected clients.
*   **Packet Sniffer (Torch):** Use `/tool torch` to capture DHCP packets for diagnosis.

**Example: Using Torch to debug DHCP:**
```mikrotik
/tool torch interface=vlan10 protocol=udp port=67
```
This command will display UDP traffic on port 67, which is typically the source port for DHCP responses, allowing you to investigate where or why these responses are not reaching clients.  If you see requests but not responses, that can help to narrow the cause.

### 5. Verification and Testing Steps

*   **Interface Status:**
    *   Check if all created VLAN interfaces are up and running:
        ```mikrotik
        /interface print
        ```
*   **IP Address Confirmation:**
    *   Ensure IP addresses and ranges are correctly set up:
        ```mikrotik
        /ip address print
        ```
*   **DHCP Server Verification:**
    *   Confirm the DHCP servers are running and serving leases:
        ```mikrotik
        /ip dhcp-server print
        /ip dhcp-server lease print
        ```
    * Check DHCPv6 Server as well with
        ```mikrotik
        /ipv6 dhcp-server print
        /ipv6 dhcp-server lease print
        ```
*   **Client IP Address Testing:**
    *   Connect a client device to each VLAN and check if it receives a correct IP address via DHCP and IPv6 addresses
*   **Ping Test:**
    *   Test connectivity from a client in each VLAN to the router's IP on that VLAN:
        ```mikrotik
        ping 192.168.10.1
        ping 192.168.20.1
        ping 192.168.30.1
        ping 2001:db8:10::1
        ping 2001:db8:20::1
        ping 2001:db8:30::1
         ```
*   **Traceroute Test:**
    *   Check routing path from a client to the internet:

    ```mikrotik
        traceroute 8.8.8.8
        traceroute 2001:4860:4860::8888
    ```
*   **DNS Resolution:**
    *   Verify that clients can resolve domain names using the configured DNS servers. (nslookup, dig, etc).
*   **Check Logging:** Check router logs with `/log print` to identify any warnings or errors during DHCP assignment or IP allocation.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **IP Pools:**
    *   Can be dynamically assigned to DHCP servers.
    *   Support multiple address ranges.
    *   Used for PPPoE secret addressing.
*   **DHCP Server:**
    *   Supports dynamic and static lease assignments.
    *   Option for DHCP server network configurations.
    *   DHCP relay capability.
    *   PXE Boot options.
*   **VLANs:**
    *   Support for 802.1q VLAN tagging.
    *   VLAN interfaces can be configured on any physical interface.
    *   Trunking and access ports.
*   **Firewall:**
    *   Stateful packet inspection.
    *   NAT/masquerading for internet access.
    *   Advanced filtering rules based on IP addresses, ports, and protocols.
* **IPv6:**
    * IPv6 Support in almost every routerOS component
    * IPv6 DHCP Server, client and routing support

**Limitations:**

*   Maximum address ranges per pool.
*   Hardware limitations in IP address assignments (CPU/RAM dependent).

### 7. MikroTik REST API Examples

Here are examples of how you might interact with MikroTik's API using its proprietary `/rest/` endpoint to manage IP pools. Note: The MikroTik REST API is not a full featured API, and access to specific parts of it are limited. It has some usability considerations that have to be taken in to account.

**Prerequisites:**

*   Enable the REST API service under `IP->Services`.
*   Create a dedicated user with `api` permission.
*   Authentication: Basic authentication required.

**Example 1: Fetching IP Pools**

**Endpoint:** `/rest/ip/pool`
**Method:** `GET`
**No Payload**

**Example Request (using curl):**

```bash
curl -u apiuser:password -X GET http://<router-ip>/rest/ip/pool
```

**Example Response (JSON):**

```json
[
    {
        ".id": "*1",
        "name": "pool-vlan10",
        "ranges": "192.168.10.10-192.168.10.254"
    },
    {
        ".id": "*2",
        "name": "pool-vlan20",
        "ranges": "192.168.20.10-192.168.20.254"
    },
    {
        ".id": "*3",
        "name": "pool-vlan30",
        "ranges": "192.168.30.10-192.168.30.254"
    },
  {
        ".id": "*4",
        "name": "ipv6-pool-vlan10",
        "ranges": "2001:db8:10::10-2001:db8:10::ffff"
    },
  {
        ".id": "*5",
        "name": "ipv6-pool-vlan20",
        "ranges": "2001:db8:20::10-2001:db8:20::ffff"
    },
{
        ".id": "*6",
        "name": "ipv6-pool-vlan30",
        "ranges": "2001:db8:30::10-2001:db8:30::ffff"
    }
]
```

**Example 2: Adding an IP Pool**

**Endpoint:** `/rest/ip/pool`
**Method:** `POST`
**Payload:** (JSON)

```json
{
    "name": "pool-vlan40",
    "ranges": "192.168.40.10-192.168.40.254"
}
```

**Example Request (using curl):**

```bash
curl -u apiuser:password -H "Content-Type: application/json" -X POST -d '{"name":"pool-vlan40","ranges":"192.168.40.10-192.168.40.254"}' http://<router-ip>/rest/ip/pool
```

**Example Response (JSON):**

```json
{
    "message": "added",
    ".id": "*7"
}
```

**Example 3: Deleting an IP Pool**

**Endpoint:** `/rest/ip/pool/*1` (replace *1 with the ID of the pool)
**Method:** `DELETE`

**Example Request (using curl):**

```bash
curl -u apiuser:password -X DELETE http://<router-ip>/rest/ip/pool/*1
```

**Example Response (JSON):**

```json
{
    "message": "removed"
}
```

**Note:** The REST API can be very brittle and requires significant error handling in your code. It is highly dependent on routerOS versions.

### 8. In-depth Explanations of Core Concepts

*   **Bridging and Switching:**
    *   Bridging combines multiple network segments into a single logical network. We are not using bridging here, as each interface is separated via VLANs.
    *   Switching forwards network frames within a network segment. Our VLAN setup uses the switch to isolate the traffic between VLANs.
*   **Routing:**
    *   Routing determines the path that network traffic takes to reach its destination. Our router acts as a gateway for each subnet, and will route between them internally.
*   **Firewall:**
    *   The firewall controls network traffic based on rules, enabling or denying it to provide security. We will add the basics of this later.
*  **IP Addressing (IPv4 and IPv6)**
    * IP Addressing refers to the way that devices on a network have an identity. IPv4 uses 32 bits, and is currently in very short supply. IPv6 uses 128 bits to provide significantly more IP addresses.
    * IPv4 addresses use a dotted decimal format with 4 octets (0-255). An IP address will be accompanied by a netmask (such as /24, or 255.255.255.0) which determines what portion of the address defines the network ID.
    * IPv6 addresses have a different layout based on hexidecimal digits, using : separators and the /64 netmask.
    * RouterOS provides dual-stack (IPv4 and IPv6) functionality throughout the whole operating system.

### 9. Security Best Practices Specific to MikroTik Routers

*   **Strong Passwords:** Use strong, unique passwords for the router.
*   **Disable Unnecessary Services:** Disable services like API access or unused ports.
*   **Firewall Rules:** Configure a robust firewall to allow only necessary traffic.
*   **Regular Updates:** Update RouterOS to the latest stable version to fix security vulnerabilities.
*   **Secure Winbox:** Only allow access from trusted IP addresses.
*   **SSH Security:** Disable password login, use SSH keys.
*   **VPN for Remote Access:** Use a VPN for remote access instead of direct web/API access.
*   **Rate Limiting:** Implement rate limiting for specific ports.
*   **Limit Remote Access IPs:** Limit the IPs that are able to connect to services like SSH and API.

**Example Firewall Rule for limiting winbox:**
```mikrotik
/ip firewall filter
add chain=input protocol=tcp dst-port=8291 src-address-list=trusted-ips action=accept comment="Allow Winbox from Trusted IPs"
add chain=input protocol=tcp dst-port=8291 action=drop comment="Drop Winbox from other IPs"
```

**Example of adding a trusted address list:**

```mikrotik
/ip firewall address-list
add address=192.168.1.0/24 list=trusted-ips
add address=10.10.10.1 list=trusted-ips
```

### 10. Detailed Explanations and Configuration Examples for all Requested Topics

**Note:** It is impossible to cover all of these topics in deep detail due to the very large nature of MikroTik.  I will provide a summary and some relevant examples to the current configuration we have done, while leaving some topics as an overview.

####   - IP Addressing (IPv4 and IPv6)

*   Already covered in configuration steps 2 and 3.
*   RouterOS is fully dual stack and supports both.

####   - IP Pools

*   Covered in configuration step 4.
*   Used to provide a dynamic pool of addresses to a DHCP Server, or to be used in other components.

####   - IP Routing

*   Covered in a basic sense through the gateway addresses we added to DHCP.
*   RouterOS supports a wide range of routing protocols, as covered later.
*   The router will automatically route between subnets that it is directly connected to.

####   - IP Settings

*   Under `/ip settings`, many low level settings can be adjusted.
*   Most commonly used is the `disable-arp`, but generally you don't need to adjust this.
*  `allow-fast-path`, `disable-fasttrack` and `fasttrack-remove-on-disable` options can be useful, but should be used with care.
*  Setting can be modified to fine tune the IP stack.

####   - MAC Server
*   Provides a way to connect to a device using MAC address rather than IP.
*   Accessible via winbox, or command line in `/tool mac-server`
*   Generally not required for normal operations.

####   - RoMON
*   Provides a way to discover and manage MikroTik devices using a proprietary protocol.
*   Useful for very large networks, not required in SOHO.
*   Can be configured in `/tool romon`.

####   - WinBox
*   Mikrotik's GUI management tool.
*   Provides all of the functionality of CLI in a graphical interface.
*   Most of our steps have included both CLI and Winbox instruction.
*   Accessed over port 8291 and can be secured using firewall rules.

####   - Certificates
*   Used to secure connections such as HTTPS and VPNs.
*   Can be used to create your own Root CA or use certificates from a provider.
*   Accessible in `/certificate`.
*  Generally not required for basic SOHO configuration.
*   Can be used for CAPsMAN

####   - PPP AAA

*   AAA (Authentication, Authorization, Accounting) is typically used in dial-up (PPP) setups.
*   Often used with VPN protocols.
*   Is done via Radius or local databases.
*   Not typically required in a basic setup.

####   - RADIUS
*   RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized authentication and authorization.
*   Used for AAA on PPP, VPNs, and WiFi networks
*   Managed via `/radius` and can be used alongside the AAA component.

####   - User / User groups
*   RouterOS can have multiple users.
*   Users are assigned to groups which control access levels.
*   Users and groups can be managed via `/user`.
*   Good practice to assign users to groups with limited access rather than giving them full admin rights, but in a SOHO environment, often you only need one admin user.

####   - Bridging and Switching
*   Already covered to some extent.
*   Bridge mode joins interfaces together to appear on the same network segment.
*   Switching does not assign an IP, but directs traffic at layer 2.
*   This example is using switching through VLANs.

####   - MACVLAN
*   MACVLAN creates virtual interfaces on top of a parent interface, each with its own MAC address.
*   Useful for very specific use cases such as containerization.
*   Configured in `/interface macvlan`.
*   Not typically required in normal SOHO setup.

####   - L3 Hardware Offloading
*   Some MikroTik hardware has support for L3 (Layer 3) hardware offloading.
*   Offloading takes IP processing off the CPU onto a dedicated chip.
*   Can greatly improve routing performance.
*   Automatically enabled when supported.
*  Can be checked with `/interface ethernet print` and looking for `l3-hw-offload`

####   - MACsec
*   MACsec (Media Access Control Security) provides secure communication at the data link layer (Layer 2).
*   Requires hardware support, which not all MikroTik devices provide.
*   Can be configured in `/interface ethernet macsec`.
*   Typically not required in a basic SOHO environment.

####   - Quality of Service
*   QoS (Quality