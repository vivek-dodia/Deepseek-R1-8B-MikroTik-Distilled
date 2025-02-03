Okay, let's dive into a comprehensive documentation for IP Addressing on MikroTik RouterOS, targeting version 6.48 (but largely applicable to 7.x as well) at an ISP-level scale.  We'll be covering a large amount of ground, keeping it practical and relevant for a seasoned MikroTik professional.  This will be a substantial document, so buckle up!

# MikroTik RouterOS IP Addressing & Related Features - ISP Level

## 1. Comprehensive Configuration Scenario

**Scenario:**  We are setting up a MikroTik router at a point of presence (POP) for a small ISP. The router will handle:

*   **Uplink (WAN):** Connection to the upstream provider, utilizing a static IPv4 address and a delegated IPv6 prefix via DHCPv6-PD.
*   **Downlink (LAN):**  Connectivity for multiple customer subnets, both IPv4 and IPv6.
*   **Management:**  Access via a dedicated management VLAN (vlan-mgmt) and IP range.
*   **DHCP:**  Providing dynamic IP address leases on each customer subnet.
*   **Routing:**  Inter-VLAN routing and routing to the internet.
*   **Security:**  Basic firewall rules to protect the router and the network.
*   **Monitoring:** Leveraging Netwatch for connectivity testing.

**Specific MikroTik Requirements:**

*   Multiple interfaces - WAN (ether1), several LAN (ether2-ether5), and VLAN interfaces
*   Support for IPv4 and IPv6 addressing and routing.
*   DHCP server configuration for IPv4 and IPv6.
*   Secure remote management access.
*   Basic firewall rules.

## 2. Step-by-Step MikroTik Implementation

We will proceed step-by-step. Here's a breakdown:

**Step 1: Basic Interface Configuration**
*   Set names for the physical interfaces.
*   Create a bridge interface for LAN ports.
*   Create a management VLAN on a specific port.

**Step 2: IP Address Assignment**
*   Configure the WAN interface with a static IPv4 address and gateway.
*   Configure the LAN bridge with an IPv4 private range.
*   Configure IPv6 on the WAN using DHCPv6-PD.
*   Configure IPv6 address(es) on the LAN bridge.
*   Configure the management VLAN interface.

**Step 3: DHCP Server Configuration**
*   Set up IPv4 and IPv6 DHCP servers on the LAN bridge.

**Step 4: Basic Routing Configuration**
*   Configure default route for IPv4 and IPv6.
*   Configure routing between subnets.

**Step 5: Basic Firewall Configuration**
*   Implement basic firewall rules for input, forward and output chains.
*   Implement NAT for IPv4.

**Step 6: Monitoring & Diagnostics**
*   Set up netwatch for basic connectivity check.
*   Verify using ping and traceroute.

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
# --- Step 1: Basic Interface Configuration ---
/interface ethernet
set ether1 name=ether1-WAN
set ether2 name=ether2-LAN
set ether3 name=ether3-LAN
set ether4 name=ether4-LAN
set ether5 name=ether5-LAN
/interface bridge
add name=bridge-LAN
/interface bridge port
add bridge=bridge-LAN interface=ether2-LAN
add bridge=bridge-LAN interface=ether3-LAN
add bridge=bridge-LAN interface=ether4-LAN
add bridge=bridge-LAN interface=ether5-LAN
/interface vlan
add interface=ether1-WAN name=vlan-mgmt vlan-id=10

# --- Step 2: IP Address Assignment ---
/ip address
add address=203.0.113.2/24 interface=ether1-WAN
add address=192.168.1.1/24 interface=bridge-LAN
add address=172.16.10.1/24 interface=vlan-mgmt
/ipv6 address
add address=::1/64 from-pool=ipv6-pool interface=bridge-LAN #This will need to be addressed again after DHCP-PD
/ipv6 dhcp-client
add interface=ether1-WAN pool-name=ipv6-pool request=prefix
/ip route
add dst-address=0.0.0.0/0 gateway=203.0.113.1
/ipv6 route
add dst-address=::/0 gateway=:: # We will address this line after DHCP-PD assignment


# --- Step 3: DHCP Server Configuration ---
/ip dhcp-server
add address-pool=dhcp-pool disabled=no interface=bridge-LAN lease-time=1d name=dhcp-server-lan
/ip dhcp-server network
add address=192.168.1.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.1.1
/ipv6 dhcp-server
add address-pool=ipv6-pool disabled=no interface=bridge-LAN lease-time=1d name=dhcp-server6-lan
/ipv6 dhcp-server server
set [ find name=dhcp-server6-lan ] address-pool=ipv6-pool

# --- Step 4: Basic Routing Configuration ---
# (Default IPv4 route set in Step 2)
# (IPv6 default route will be set after prefix is received)

# --- Step 5: Basic Firewall Configuration ---
/ip firewall filter
add action=accept chain=input comment="Allow established connections" connection-state=established,related
add action=accept chain=input comment="Allow ICMP" protocol=icmp
add action=accept chain=input comment="Allow SSH from LAN" dst-port=22 in-interface=bridge-LAN protocol=tcp
add action=accept chain=input comment="Allow WinBox from LAN" dst-port=8291 in-interface=bridge-LAN protocol=tcp
add action=drop chain=input comment="Drop all other input"
add action=accept chain=forward comment="Allow established connections" connection-state=established,related
add action=accept chain=forward comment="Allow forward" in-interface=bridge-LAN
add action=drop chain=forward comment="Drop other forwards"
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1-WAN
/ip firewall raw
add action=notrack chain=prerouting dst-address=192.168.1.0/24
add action=notrack chain=prerouting in-interface=bridge-LAN

# --- Step 6: Monitoring & Diagnostics ---
/tool netwatch
add comment="Check google" host=8.8.8.8 interval=1m timeout=1s
```

**Explanation of Important Parameters:**

| Parameter              | Description                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------------|
| `name`                   | Descriptive name for an interface.                                                                                  |
| `interface`              | The physical interface the configuration applies to.                                                              |
| `bridge`                 | Bridge interface name for the port.                                                                                     |
| `vlan-id`                | VLAN tag.                                                                                                       |
| `address`                | IP address and subnet mask (e.g., 192.168.1.1/24).                                                                  |
| `gateway`                | IP address of the next-hop router.                                                                                  |
| `pool-name`              | DHCP pool name.                                                                                                     |
| `request`                | Specifies the type of IPv6 address request. Prefix is required for DHCPv6-PD.                              |
| `lease-time`             | DHCP lease time (e.g., 1d for 1 day).                                                                           |
| `dns-server`             | DNS server addresses for clients.                                                                                 |
| `action`                 | Firewall action (accept, drop, etc.).                                                                            |
| `chain`                  | Firewall chain (input, forward, output, etc.).                                                                     |
| `connection-state`       | Firewall state (established, related).                                                                             |
| `protocol`               | IP protocol (icmp, tcp, etc.).                                                                                    |
| `dst-port`               | Destination port number.                                                                                           |
| `in-interface`           | Input interface.                                                                                                   |
| `out-interface`          | Output interface.                                                                                                  |
| `host`                   | Host to monitor for netwatch.                                                                                    |
| `interval`               | Check interval for netwatch.                                                                                    |
| `timeout`              | Timeout for netwatch.                                                                                    |

**Note:** The IPv6 route and IPv6 address were added as a generic example.  After DHCPv6-PD assigns a prefix to the WAN interface, you must modify the IPv6 address and the default route to use this information. This is covered in troubleshooting below.

## 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Firewall Misconfiguration:** A common mistake is having a firewall rule that blocks legitimate traffic.
*   **Incorrect VLAN Settings:** Ensure VLAN IDs match on both ends.
*   **DHCP Issues:**  Ensure DHCP server is properly configured and IP address pools are defined correctly.
*   **Routing Problems:** Ensure all routes are properly set, especially for VLANs.
*   **IPv6-PD Prefix Issues:** Getting a delegated prefix from the upstream provider may be an issue and needs proper checking.
*   **Resource Issues:**  Overloading router with too many rules, etc.
*   **Firmware Issues:** Outdated RouterOS versions can cause unexpected issues.

**Troubleshooting:**

*   **Connectivity Issues:** Use `ping` to test basic connectivity. If ping fails, use `traceroute` to identify the hop where the connection breaks.
*   **Firewall Issues:**  Use `/tool torch` to see the flow of traffic and identify if packets are being dropped due to firewall rules. `/log print` to see firewall logs.
*   **DHCP Issues:**  Check DHCP leases under `/ip dhcp-server lease print` to identify issues.
*   **Routing Issues:** Check routing table using `/ip route print`. Use `/tool sniffer` or `/tool traffic-generator` for more advanced testing.
*   **IPv6 Issues:**  Use `ping6` and `traceroute6`. Check DHCPv6 client leases.

   **IPv6 DHCP-PD Troubleshooting:**
   1.  **Initial Check:** Verify the DHCPv6-Client status on `/ipv6 dhcp-client print`. Look for a "status" of "bound" and an assigned `prefix`. If `status` is blank or "searching," check your ISP connection and DHCP settings. Also verify if the "delegated prefix" field contains a valid IPv6 block of addresses.
   2.  **Prefix Adjustment:** If a prefix is obtained, we must adjust the address on the LAN bridge. For instance, if your delegated prefix is `2001:db8:100::/48` and you want the `/64` subnet on the LAN, use the following command, replacing the `::1/64` with something like `2001:db8:100::1/64`. The IP address will use the first few digits of the delegated prefix, the bridge interface will use the remaining digits of the delegated prefix.
      ```mikrotik
      /ipv6 address set [find interface=bridge-LAN] address=2001:db8:100::1/64
      ```
   3. **Default Gateway Update:**  After the DHCPv6 client acquires a prefix, we need to update our default gateway. Since the gateway will come from the upstream router on the provider network, it is impossible to know.  A generic route will be set using the interface, and the router will use a link-local address for the gateway.
        ```mikrotik
        /ipv6 route set [find dst-address=::/0 ] gateway=:: interface=ether1-WAN
        ```
    4.  **Dynamic Update Script:** For robust operation, use a script to dynamically update your IPv6 address based on the prefix. This would involve checking the DHCPv6 client for the obtained prefix, calculating the appropriate address for your network(s), and then updating the interface address. Such a script is more advanced but ensures continuous operation even when prefixes change. There are many examples of these on the MikroTik forums.

**Diagnostics:**

*   **`/system resource print`**: Monitor CPU, RAM, and disk usage.
*   **`/interface monitor-traffic`**:  Monitor the traffic on specific interfaces for issues.
*   **`/log print`**:  Check system logs for errors and warnings.
*  **`/tool profile`**: Profile the router's useage of various resources, often handy when debugging problems.
* **`/interface ethernet monitor`**: Monitor link stats such as link speed, packets dropped, and errors.

## 5. Verification and Testing

**Verification:**

*   **Ping:**  Ping devices on the LAN and internet to verify connectivity:

    ```mikrotik
    /ping 8.8.8.8
    /ping 192.168.1.20
    /ping6 2001:4860:4860::8888
    ```
*   **Traceroute:** Trace the path to a destination to identify routing problems:

    ```mikrotik
    /traceroute 8.8.8.8
    /traceroute6 2001:4860:4860::8888
    ```
*   **DHCP Leases:** Check DHCP leases to ensure IP addresses are being assigned correctly:

    ```mikrotik
    /ip dhcp-server lease print
    /ipv6 dhcp-server lease print
    ```

**Testing:**

*   **Traffic Analysis with Torch:**  Use `torch` to examine the traffic flow and identify issues:
    ```mikrotik
    /tool torch interface=ether1-WAN
    ```
*   **Bandwidth Testing:** Use `/tool bandwidth-test` to test bandwidth and throughput:
    ```mikrotik
    /tool bandwidth-test address=192.168.1.20 protocol=tcp direction=both
    ```
*   **Netwatch Monitoring:** Verify that Netwatch is working as configured using `/tool netwatch print` to show status.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

**IP Addressing:**

*   **Address Pools:**  `/ip pool` – Create IP address pools for DHCP servers or other uses.
*   **Static Addresses:** Manual assignment of IPs on interfaces.
*   **Virtual Addresses:** Assigning secondary IPs to interfaces.

**IP Routing:**

*   **Static Routes:**  Manually configured routing paths.
*   **Dynamic Routing:**  Support for protocols like OSPF, RIP, BGP.
*   **Policy Routing:** Route based on attributes like source IP, protocol, etc.

**Firewall:**

*   **Stateful Firewall:** Track connection states to allow only return traffic.
*   **NAT:** Network Address Translation for IPv4.
*   **Mangle:** Modify packet headers for advanced firewall rules and QoS.

**DHCP:**

*   **DHCP Servers:**  Dynamic address assignment to client devices.
*   **DHCP Relay:** Relay DHCP requests to other DHCP servers.
*   **DHCPv6 Client/Server:** Full support for DHCPv6.

**Security:**

*   **Access Control Lists (ACLs):** Control access to the router's management interface.
*   **Secure Passwords:** Best practice - use strong, unique passwords.
*   **SSH Access:**  Disable Telnet, and use SSH instead.
*   **HTTPS/TLS for Web Interface:** Enforce HTTPS and use self-signed certificates.
*   **Firewall rules:** Limit the exposure of services and allow specific communication only.

**Capabilities:**

*   Highly flexible and customizable.
*   Wide range of features in a single router.
*   Cost-effective and high performance.

**Limitations:**

*   Can be complex to configure for new users.
*   Steep learning curve, especially with advanced features.
*   Limited hardware resources on some router models (CPU, RAM).

## 7. MikroTik REST API Examples

Here's a practical example showing how to use the MikroTik REST API to retrieve the IP address list:

**API Endpoint:**  `/ip/address`

**Request Method:** GET

**Example Command (Using `curl`):**

```bash
curl -k -X GET -H "Content-Type: application/json" \
     -u 'api_user:api_password' \
     "https://your_router_ip/rest/ip/address"
```

**Example Response (JSON):**

```json
[
  {
    "id": "*0",
    "address": "192.168.1.1/24",
    "interface": "bridge-LAN",
    "network": "192.168.1.0",
    "actual-interface": "bridge-LAN",
    "dynamic": "false",
    "invalid": "false"
  },
   {
    "id": "*1",
    "address": "203.0.113.2/24",
    "interface": "ether1-WAN",
    "network": "203.0.113.0",
    "actual-interface": "ether1-WAN",
    "dynamic": "false",
    "invalid": "false"
  }
]
```

**Example - add an address:**
**API Endpoint:** `/ip/address`

**Request Method:** POST

**Example Command (Using `curl`):**

```bash
curl -k -X POST -H "Content-Type: application/json" \
     -u 'api_user:api_password' \
     -d '{"address": "192.168.2.1/24", "interface": "bridge-LAN"}' \
     "https://your_router_ip/rest/ip/address"
```

**Example Response (JSON):**

```json
{
   "message": "added",
   "id": "*10"
}
```

**API Notes:**

*   Replace `your_router_ip`, `api_user`, and `api_password` with your actual MikroTik router's IP, API username, and password.
*   Enable the API on the router in `/ip service print` - make sure it is active.
*   The API user needs to be created in `/user` with permissions.
*   Use the `-k` flag to ignore certificate errors if you are using a self-signed certificate.
*   Explore the MikroTik API documentation (`https://your_router_ip/rest/docs` or refer to the MikroTik official website) for more API endpoints and capabilities.

## 8. In-Depth Explanations of Core Concepts

**Bridging:**
   *  MikroTik bridging combines multiple physical interfaces into a single logical layer 2 interface. This allows for seamless traffic forwarding between ports without needing routing on the same network.
   *  Bridging is useful for creating a LAN with multiple wired ports that all exist in the same broadcast domain.
   *  Bridging is managed using `/interface bridge` and `/interface bridge port` commands.
   *  You can add multiple interfaces to one or more bridges and manage them all independently.
**Routing:**

   *  MikroTik routing directs traffic between different networks, using IP addresses and routing tables.
   *  Static routing manually sets routes to specific networks, while dynamic routing (OSPF, RIP, BGP) automatically learns paths to networks.
   *  Routing is the core mechanism that enables communication between networks with different IP subnets.
   *  Routing is configured using `/ip route`, `/ipv6 route`, and potentially routing protocols configurations.
**Firewall:**
   *  MikroTik firewall controls network access and protects the router and network from malicious traffic.
   *  Firewall works using configurable rules that inspect the packet headers and payload and apply actions.
   *  Stateful firewalling keeps track of connections, allowing only return traffic to established connections.
   *  NAT translates private IP addresses to public ones.
   *  Firewall is controlled using `/ip firewall filter`, `/ip firewall nat`, and `/ip firewall mangle`.

## 9. Security Best Practices

*   **Change Default Credentials:** Change the default username and password immediately.
*   **Disable Unnecessary Services:** Disable services like Telnet, API, and FTP if not needed.
*   **Strong Passwords:** Use strong, unique passwords for the router.
*   **SSH Access:**  Disable Telnet and use SSH instead for remote access.
*   **HTTPS/TLS:** Enforce HTTPS for web access, and use self-signed certificates.
*   **Firewall Rules:**
    *   Implement input chain rules to restrict access to the router itself.
    *   Implement forward chain rules to control traffic flow.
    *   Use allow-by-default policies when possible, and blacklist unwanted IPs and protocols.
*   **Regular Updates:** Keep RouterOS updated to the latest version to address security vulnerabilities.
*   **Use of VLANs**: Using VLANs to isolate different portions of your network.
*   **Avoid Public Management Ports:** Do not expose winbox and SSH to the internet - use VPNs or dedicated management network.

## 10. Detailed Explanations and Configuration Examples for Specific MikroTik Topics

This is a very comprehensive topic, so we will provide an overview and CLI examples to serve as a starting point for each component. This will allow a full implementation, but will require reading the RouterOS documentation to fully understand the capabilities.

**IP Addressing (IPv4 and IPv6)**
   - Covered in detail above in the main example, but this includes `/ip address` and `/ipv6 address` for assigning IPs to interfaces.
   - Example of assigning a static IPv4 address:
     ```mikrotik
     /ip address add address=192.168.100.1/24 interface=ether2-LAN
     ```
   - Example of assigning a static IPv6 address:
    ```mikrotik
      /ipv6 address add address=2001:db8:100::1/64 interface=bridge-LAN
    ```

**IP Pools**
   - Used to define ranges of addresses for DHCP servers or other services.
   - Example of adding an IPv4 address pool:
    ```mikrotik
    /ip pool add name=dhcp-pool ranges=192.168.100.100-192.168.100.200
    ```
  - Example of adding an IPv6 address pool:
    ```mikrotik
    /ipv6 pool add name=ipv6-pool prefix=2001:db8:100::/48 prefix-length=64
    ```
**IP Routing**
   - See the example above using `/ip route` and `/ipv6 route`. This manages how packets get delivered.
   - Example of adding a default IPv4 route:
      ```mikrotik
      /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
      ```
  - Example of adding a default IPv6 route:
      ```mikrotik
      /ipv6 route add dst-address=::/0 gateway=:: interface=ether1-WAN
      ```
**IP Settings**
   - Settings for the global IP stack settings, including IPv4 and IPv6 features.
   - Example of enabling IPv6 routing:
      ```mikrotik
      /ipv6 settings set forward=yes
      ```
**MAC server**
  - Allows mapping from IP address to the underlying MAC address.
   - Enabled by default.  No specific use case in our scenario.
  - Example of viewing MAC server entries:
    ```mikrotik
     /ip arp print
    ```
**RoMON**
  - MikroTik's Router Management over Network.  A proprietary protocol for managing devices.
  - Out of scope for our basic scenario.
  - Example of configuring RoMON on an interface.
   ```mikrotik
    /tool romon set enabled=yes interfaces=ether1-WAN,bridge-LAN
   ```
**WinBox**
  - MikroTik's primary GUI tool for router management.
  - Accessable via HTTPS or the winbox application.
  - Out of scope for our basic scenario.
**Certificates**
  - Manages certificate used in RouterOS, particularly for HTTPS, IPsec, VPNs etc.
  - Out of scope for our basic scenario.
  - Example of generating a self signed certificate:
    ```mikrotik
      /certificate add name=selfsigned-certificate common-name=your-domain.com
      /certificate sign selfsigned-certificate
     ```
**PPP AAA**
  - PPP (Point to Point Protocol) uses AAA (Authentication, Authorization and Accounting).
  - Used for connecting to PPP links, such as PPPoE.
   - Out of scope for our basic scenario.
**RADIUS**
  - Allows for remote user authentication, authorization, and accounting.
   - Out of scope for our basic scenario.
  - Example of configuring RADIUS server:
     ```mikrotik
      /radius add address=10.0.0.10 secret=test-secret timeout=20
     ```

**User / User groups**
  - Manages users and groups on the RouterOS for access to winbox and API.
  - See section "Security best practices" for additional information.
  - Example of adding a user with api rights.
    ```mikrotik
     /user add name=api_user password=secret group=full
     ```
**Bridging and Switching**
   - Bridging covered above in core concepts.
  - Switching is mostly managed by the underlying hardware, providing wire speed forwarding of traffic.
  - Example of modifying bridge settings:
  ```mikrotik
  /interface bridge set bridge-LAN stp=yes
  ```
**MACVLAN**
  - Allows the creation of multiple virtual interfaces on top of a single interface.  Requires specific hardware.
  - Out of scope for our basic scenario.
  - Example of adding a MACVLAN interface:
     ```mikrotik
     /interface macvlan add interface=ether2-LAN mac-address=02:44:66:88:aa:cc name=macvlan1
    ```

**L3 Hardware Offloading**
  - Leverages hardware processing to improve router performance.
  - Example of enabling L3 Hardware Offloading on a bridge:
  ```mikrotik
  /interface bridge set bridge-LAN l3-hw-offloading=yes
  ```
**MACsec**
  - MACsec is an IEEE standard for data confidentiality and integrity.
  - Out of scope for our basic scenario.

**Quality of Service**
   - QoS controls and manages network traffic, prioritizing certain traffic types or limiting bandwidth.
   - See below for further explanation.

**Switch Chip Features**
   - Advanced hardware features of a specific hardware switch.
   - Requires specific hardware for configuration.
   - Out of scope for our basic scenario.

**VLAN**
  - Allows segmentation of a network into smaller broadcast domains.
  - Covered above in the main example, using `/interface vlan`.
  - Example of creating a VLAN interface:
     ```mikrotik
     /interface vlan add interface=ether2-LAN name=vlan10 vlan-id=10
     ```

**VXLAN**
  - Virtual eXtensible LAN allows for layer 2 connectivity over layer 3 networks.
  - Out of scope for our basic scenario.
  - Example of setting up a VXLAN tunnel:
      ```mikrotik
      /interface vxlan add name=vxlan1 vni=1000 interface=ether2-LAN remote-address=10.0.0.2
      ```

**Firewall and Quality of Service**
   - Includes connection tracking, various firewall rules, packet flow, queues, case studies, kid control, UPnP, and NAT-PMP.

   **Connection Tracking**
        -  Keeps track of connections for stateful firewalling.
        - Enabled by default and essential for the operation of the firewall.
   **Firewall**
        - Covered above and uses `/ip firewall filter`, `/ip firewall nat`, and `/ip firewall mangle`.
        - Example of allowing SSH from the LAN (as seen above).
   **Packet Flow in RouterOS**
        - Determines where packets go.  First through the hardware, then through the firewall and routing.
        - Requires advanced knowledge of the architecture.
        - Example of viewing the packet flow via the torch:
         ```mikrotik
          /tool torch interface=ether2-LAN
         ```
   **Queues**
        - Configurable QoS, to limit/prioritize bandwidth.
       - Example of setting up a simple queue on an interface:
       ```mikrotik
       /queue simple add max-limit=10M name=download target=ether2-LAN
       ```
   **Firewall and QoS Case Studies**
        - Examples of how to use firewall and QoS in real world networks.
        - Out of scope for this document.
   **Kid Control**
        -  Limits access based on various factors, including websites and time.
        - Example of adding a kid control rule:
         ```mikrotik
         /ip firewall layer7-protocol add name=youtube regexp="^.+(youtube.com).*\$"
         /ip firewall filter add chain=forward layer7-protocol=youtube time=00:00:00-16:00:00 action=drop
        ```
   **UPnP**
        - Allows network devices to discover each other and initiate connections.
        - Example of enabling UPnP:
         ```mikrotik
         /ip upnp set enabled=yes
         ```
   **NAT-PMP**
        - Provides NAT traversal on IPv4 networks.
        -  Example of enabling NAT-PMP:
          ```mikrotik
          /ip upnp set nat-pmp-enabled=yes
        ```

**IP Services (DHCP, DNS, SOCKS, Proxy)**
   - Services include DHCP server, DNS server, SOCKS proxy, and web proxy.
   - DHCP detailed above.

   **DNS**
     - Example of enabling the DNS server:
      ```mikrotik
       /ip dns set allow-remote-requests=yes
       /ip dns set servers=8.8.8.8,8.8.4.4
      ```
   **SOCKS Proxy**
     - Proxy for use with applications.
      - Example of enabling SOCKS proxy:
        ```mikrotik
        /ip socks set enabled=yes
        ```
   **Proxy**
     - HTTP Proxy for web traffic.
      - Example of setting up web proxy:
        ```mikrotik
         /ip proxy set enabled=yes
         /ip proxy access add dst-address=192.168.1.0/24
        ```

**High Availability Solutions**
   - Include load balancing, bonding, case studies, multi-chassis LAG, VRRP.

   **Load Balancing**
        - Provides for routing traffic over multiple links.
        - Example of load balancing using multiple gateways:
         ```mikrotik
          /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 check-gateway=ping
          /ip route add dst-address=0.0.0.0/0 gateway=192.168.2.1 check-gateway=ping
         ```
  **Bonding**
      - Multiple links used as a single logical connection.
     - Example of creating a bonding interface:
     ```mikrotik
     /interface bonding add mode=802.3ad name=bond1 slaves=ether2-LAN,ether3-LAN
     ```
    **Bonding Examples**
        - Real world configuration examples.  Out of scope for this document.
    **HA Case Studies**
         - How to implement highly available networks with Mikrotik devices.
        - Out of scope for this document.
   **Multi-chassis Link Aggregation Group**
        -  Advanced feature combining bonding across multiple routers.
        - Out of scope for our basic scenario.
   **VRRP**
        - The Virtual Router Redundancy Protocol, for high availability routing.
       - Example of setting up VRRP:
         ```mikrotik
         /interface vrrp add interface=ether2-LAN name=vrrp1 priority=100 vrid=1 virtual-address=192.168.1.254/24
         ```
    **VRRP Configuration Examples**
        -  Real world configurations.  Out of scope for this document.

**Mobile Networking**
   - Includes GPS, LTE, PPP, SMS, and Dual SIM application.
    - Out of scope for our basic scenario.

**Multi Protocol Label Switching - MPLS**
    - Wide range of MPLS features, generally used by ISPs.
    - Out of scope for our basic scenario.

**Network Management**
    - Includes ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow.
    - Out of scope for our basic scenario, as many are covered above.

**Routing**
   - Includes Routing protocols overview, moving from v6 to v7, multi-core support, policy routing, VRF, OSPF, RIP, BGP, RPKI, Route Selection/Filters, Multicast, debugging, and BFD/IS-IS.
  - Covered above.

**System Information and Utilities**
    - Includes Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, and TFTP.
      - Example of setting the system identity:
       ```mikrotik
       /system identity set name=your-router-name
       ```
**Virtual Private Networks**
    - Include 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, and ZeroTier.
      - Example of enabling wireguard:
        ```mikrotik
         /interface wireguard add name=wg1 listen-port=51820 mtu=1420
         ```
**Wired Connections**
    - Includes Ethernet, MikroTik wired interface compatibility, and PWR Line.
   - Covered above using `/interface ethernet`

**Wireless**
    - Includes WiFi, Wireless interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, and Spectral scan.
   - Out of scope for our basic scenario.

**Internet of Things**
    - Includes Bluetooth, GPIO, Lora, and MQTT.
   - Out of scope for our basic scenario.

**Hardware**
   -  Includes Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, and USB Features.
   - Out of scope for our basic scenario.

**Diagnostics, Monitoring and Troubleshooting**
    - Includes Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 guidance, Torch, Traceroute, Traffic Flow, and Watchdog.
    - Some of these have been covered above.

   - Example of enabling the watchdog:
      ```mikrotik
       /system watchdog set enabled=yes
       ```
**Extended Features**
    - Includes Container, DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, and IP packing.
   - Out of scope for our basic scenario.

This completes the comprehensive documentation.