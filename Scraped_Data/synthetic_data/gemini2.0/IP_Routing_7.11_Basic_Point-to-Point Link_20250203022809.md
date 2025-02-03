Okay, let's craft some comprehensive documentation for configuring IP Routing on a MikroTik router, specifically for a point-to-point link scenario on RouterOS 7.11 (and compatible with 6.48 and 7.x).

# MikroTik RouterOS: IP Routing for Point-to-Point Link (Subnet 175.198.14.0/24)

This document details the configuration of IP routing for a point-to-point link using a MikroTik router running RouterOS 7.11 (compatible with 6.48 and 7.x). We'll be configuring an interface named "vlan-34" with an IP address from the 175.198.14.0/24 subnet. This configuration will be at a **Basic** level, suitable for many SOHO and SMB scenarios. The document emphasizes practical implementation using both the CLI and Winbox, while also touching upon related concepts, security, and advanced features.

## 1. Scenario and Requirements

**Scenario:** We're establishing a simple point-to-point link between two MikroTik routers. One side will have the IP 175.198.14.1/24 and the other side 175.198.14.2/24. This configuration focuses on the configuration on one side. The interface is a VLAN named `vlan-34`. We will also configure basic IP routing.

**Requirements:**

*   RouterOS version: 7.11 (or 6.48, 7.x)
*   Interface Name: `vlan-34`
*   Subnet: 175.198.14.0/24
*   Configuration Level: Basic
*   Network Scale: Point-to-Point Link

## 2. MikroTik Implementation: Step-by-Step

### 2.1. Using CLI

We will configure the following steps via CLI

*   **Create VLAN Interface**: If vlan-34 does not exist, create it.
*   **Assign IP address**: Assign an IP to the vlan-34 interface.
*   **Enable the interface**: Ensure the interface is up and running.

   ```
   /interface vlan
   add interface=ether1 name=vlan-34 vlan-id=34
   /ip address
   add address=175.198.14.1/24 interface=vlan-34 network=175.198.14.0
   /interface enable vlan-34
   ```

   **Explanation of commands:**

    * `/interface vlan add`: Adds a new VLAN interface.
        * `interface=ether1`: Specifies the physical interface the VLAN is built on. **Note**: Adjust `ether1` to your actual interface, such as `ether2` or a wireless interface.
        * `name=vlan-34`: The name of the new VLAN interface.
        * `vlan-id=34`: Specifies the VLAN ID (Tag).
    *   `/ip address add`: Adds an IP address to an interface.
        *   `address=175.198.14.1/24`: The IP address and subnet mask.
        *   `interface=vlan-34`: The interface on which the IP address is assigned.
        * `network=175.198.14.0`: Specifies the network portion of the IP.
    * `/interface enable`: Enables a specific interface.
        * `vlan-34`: Enables the VLAN interface named `vlan-34`.

### 2.2. Using Winbox GUI

1.  **Create VLAN Interface (if needed)**:
    *   Connect to your MikroTik router with Winbox.
    *   Go to "Interfaces".
    *   Click the "+" button and select "VLAN".
    *   In the "General" tab:
        *   "Name":  `vlan-34`
        *   "VLAN ID": `34`
        *   "Interface": (Select the physical interface, e.g., `ether1`)
    *   Click "Apply" and then "OK".
2.  **Assign IP Address:**
    *   Go to "IP" -> "Addresses".
    *   Click the "+" button.
    *   In the "Address" field, enter `175.198.14.1/24`.
    *   From the "Interface" dropdown, select `vlan-34`.
    *   Click "Apply" and then "OK".
3.  **Enable Interface (If not already enabled):**
    *  Go to "Interfaces".
    *  Find `vlan-34`
    *  Make sure that the interface is checked. If not, check it.

## 3. Complete MikroTik CLI Configuration

```
/interface vlan
add interface=ether1 name=vlan-34 vlan-id=34
/ip address
add address=175.198.14.1/24 interface=vlan-34 network=175.198.14.0
/interface enable vlan-34
```

## 4. Common Pitfalls, Troubleshooting, and Diagnostics

### 4.1. Pitfalls

*   **Incorrect VLAN ID:**  Ensure the VLAN ID (34 in this case) matches on both ends of the link. Mismatched VLAN IDs mean that the devices are not on the same broadcast domain.
*   **Incorrect Subnet Mask**: Make sure the subnet mask (/24) is consistent on all devices in the network.
*   **Interface Mismatch**:  Verify that the interface name (`ether1` in the CLI example) is correct.
*   **IP Address Overlap:** Check that IP addresses in the subnet are unique and avoid conflicts.

### 4.2. Troubleshooting

1.  **Interface Status:**
    *   Check if the interface is enabled `/interface print`. Look for `vlan-34`, the `enabled` column should be `yes`
    *   Ensure that the interface is running. Check using `/interface monitor vlan-34`.
2.  **IP Address Configuration:**
    *   Verify that the IP address is assigned to the correct interface using `/ip address print`.
3.  **Connectivity Issues:**
    *   Use `ping` to test basic IP connectivity. For example, `ping 175.198.14.2` from Router A, and `ping 175.198.14.1` from Router B.
    *   Use `traceroute` to examine the path between two routers, for example `traceroute 175.198.14.2`.

### 4.3. Error Scenarios

*   **Error: "invalid value for argument address"**: This typically occurs when the IP address is not in the correct format or overlaps another existing IP address.

    ```
    [admin@MikroTik] > /ip address add address=175.198.14.1 interface=vlan-34
    invalid value for argument address: 175.198.14.1
    ```

*   **Error: "already have such address"**: When the IP address being added already exist in the router.

    ```
    [admin@MikroTik] > /ip address add address=175.198.14.1/24 interface=vlan-34
    already have such address
    ```

*   **Error: "invalid value for argument interface"**: This appears when a non-existent interface is referenced.

    ```
    [admin@MikroTik] > /ip address add address=175.198.14.1/24 interface=invalid-interface
    invalid value for argument interface: invalid-interface
    ```

### 4.4. Diagnostics Using Built-in Tools

*   **Ping:** Tests basic network connectivity between IP addresses.

    ```
    /ping 175.198.14.2
    ```
*   **Traceroute:** Shows the path packets take to reach a destination IP address.

    ```
    /traceroute 175.198.14.2
    ```
*   **Torch:** Real-time packet monitoring for specific interfaces.

    ```
    /tool torch interface=vlan-34
    ```
*   **Log:** The log files record system events and can assist in troubleshooting. Access via `/log print`.

## 5. Verification and Testing

### 5.1. CLI Verification

*   **Verify Interface Status:**

    ```
    /interface print where name=vlan-34
    ```

    Check for the interface `enabled` status.
*   **Verify IP Address Assignment:**

    ```
    /ip address print where interface=vlan-34
    ```

    Check for assigned IP `175.198.14.1/24`.
*   **Ping Test:**

    ```
    /ping 175.198.14.2
    ```

    This should be successful if the other end is configured correctly.

### 5.2. Winbox Verification

*   **Interface:** Go to "Interfaces" and check the status of `vlan-34`.
*   **IP Address:** Go to "IP" -> "Addresses" and verify the entry for `175.198.14.1/24` on interface `vlan-34`.
*   **Ping:** Open the "Tools" menu, go to "Ping", enter `175.198.14.2`, and click "Start."

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

### 6.1. Less Common Features

*   **Virtual Routing and Forwarding (VRF):** For complex scenarios, you can create VRFs to separate routing tables. This requires a deep understanding of routing and can be considered an expert configuration.

*   **Policy-Based Routing (PBR):**  Allows routing decisions to be based on more than just the destination IP, like source IP, ports or protocols. This is advanced configuration suitable for specific cases.

*   **L3 Hardware Offloading:** MikroTik devices with switch chips can often offload certain L3 operations to the hardware, improving performance. (Configuration is mostly automatic, but must be on supported hardware).

### 6.2. Limitations

*   **Hardware Limitations**: Some features, like L3 Hardware Offloading, are dependent on the specific hardware of the MikroTik router. Low-end devices may have limited feature support.
*   **Performance**: RouterOS can handle significant loads, but there are limits. Overloading CPUs can impact performance.

## 7. MikroTik REST API Examples

### 7.1. List IP Addresses on an Interface

**Endpoint:** `/ip/address`

**Method:** `GET`

**Example cURL Request:**

```bash
curl -k -u "admin:<your_password>" -H "Content-Type: application/json" https://<your_router_ip>/rest/ip/address?interface=vlan-34
```

**Expected Response (JSON):**

```json
[
  {
    ".id": "*3",
    "address": "175.198.14.1/24",
    "interface": "vlan-34",
    "network": "175.198.14.0",
    "disabled": false,
    "actual-interface": "vlan-34"
  }
]
```

### 7.2 Add New IP Address on an Interface

**Endpoint:** `/ip/address`

**Method:** `POST`

**Example cURL Request:**
```bash
curl -k -u "admin:<your_password>" -H "Content-Type: application/json" -X POST -d '{"address": "175.198.14.254/24", "interface": "vlan-34"}' https://<your_router_ip>/rest/ip/address
```

**Expected Response (JSON):**
```json
{
  ".id": "*4"
}
```

**Note**: You will need to replace `<your_password>` and `<your_router_ip>` with the actual password of the user and IP of your MikroTik router.

## 8. In-Depth Explanations of Core Concepts

### 8.1. IP Addressing

*   **IPv4 Address Structure:** IPv4 addresses are 32-bit numerical labels assigned to devices. The address `175.198.14.1` represents a specific device within the subnet `175.198.14.0/24`.
*   **Subnet Masks:** The `/24` part of `175.198.14.1/24` specifies the subnet mask. A /24 network mask means the first 24 bits are the network address, and the remaining 8 bits are used for host addresses, providing 254 usable host addresses in the 175.198.14.0/24 subnet. The subnet mask determines which part of the IP is the network and which is the host.
*   **Network Address:** The `175.198.14.0` network address identifies a specific network.
*   **Broadcast Address:** The broadcast address is typically the last IP address in the subnet. For 175.198.14.0/24, this would be 175.198.14.255.

### 8.2. IP Routing

*   **Purpose:**  IP routing is the process of selecting paths for network traffic. The goal is to move network packets from a source to its intended destination.
*   **Routing Table:** MikroTik routers maintain a routing table that dictates how IP packets are forwarded. Each entry maps a network destination to a route to reach that destination (a next hop IP).
*   **Static vs. Dynamic Routing:** In this basic example, we are only implicitly using a "connected" route when we assign the IP address to the interface. For more complex networks, you can configure static routes or use dynamic routing protocols like OSPF or BGP.

### 8.3. Bridging and Switching

*   **Bridging:** Allows Ethernet frames to be forwarded based on MAC addresses within a common broadcast domain. Bridges are layer-2 devices, that do not handle routing or IPs. In our case, we are configuring IP addresses, therefore, we are not using bridging.
*   **Switching:** Refers to the internal process of a hardware switch chip that forwards frames based on MAC addresses (Layer 2). MikroTik routers with integrated switch chips can offload switching functions to dedicated hardware.
*   **Relationship with Routing:** When routing, the traffic will be moved between different broadcast domains. We are using routing when assigning an IP address to the vlan interface.

### 8.4 VLAN

* **VLAN Tagging:** A VLAN Tag (802.1Q Tag) is an Ethernet Header extension used to mark a frame belonging to a specific VLAN.
* **Logical Network Separation:** VLANs create logical separation in a physical network, meaning devices in one VLAN cannot communicate directly with those on a different VLAN, unless they go through a router.
* **VLAN ID**: Unique identifier assigned to the VLAN.

## 9. Security Best Practices

### 9.1. Router Access

*   **Strong Passwords:** Use strong, unique passwords for the `admin` account.
*   **Disable Default Accounts:** If possible, disable the default `admin` account and create a new administrator account with a unique username.
*   **Secure Access Protocols:** Enable secure access protocols like HTTPS, and SSH. Disable Telnet.
*   **Firewall Access Control:** Implement firewall rules to restrict access to the router from unauthorized IP addresses or networks.

### 9.2. Specific Features

*   **Disable Unnecessary Services:** Disable unused IP services like Telnet or FTP.
*   **API Access:** Restrict API access to specific IP addresses.
*   **Keep RouterOS Updated:** Regularly update your RouterOS to the latest stable version to protect against known vulnerabilities.

## 10.  Detailed Explanations and Configuration Examples for MikroTik Topics

### 10.1. IP Addressing (IPv4 and IPv6)

*   **IPv4:** (Covered in depth above).
*   **IPv6:** RouterOS supports both IPv4 and IPv6. IPv6 addresses are 128-bit. Basic IPv6 config example:
    ```
    /ipv6 address add address=2001:db8::1/64 interface=vlan-34
    ```
    *   `address=2001:db8::1/64`: An IPv6 address and prefix length.
    *   `interface=vlan-34`: The interface to assign the address to.

### 10.2. IP Pools

*   **Purpose:** Used to manage IP address ranges for dynamic address allocation (e.g., DHCP).
*   **Configuration Example:**
    ```
    /ip pool add name=test_pool ranges=192.168.10.10-192.168.10.100
    ```
    *   `name=test_pool`: Name of the pool
    *   `ranges=192.168.10.10-192.168.10.100`: The IP range to use in the pool.

### 10.3. IP Routing

*   **Static Routing:** Manually define routes.
    ```
    /ip route add dst-address=192.168.20.0/24 gateway=175.198.14.2
    ```
    *   `dst-address=192.168.20.0/24`: Target network.
    *   `gateway=175.198.14.2`: Next-hop IP.
*  **Dynamic Routing**: Use protocols like OSPF, BGP, or RIP to learn routes dynamically. Configuration is complex and out of scope for this basic guide.

### 10.4. IP Settings

*   **Global IP Settings:** Used for general network configuration.
   ```
    /ip settings print
   ```
   * The command can be used to print the current settings.
   ```
   /ip settings set allow-fast-path=yes
   ```
  * Enables fast path processing.
   ```
    /ip settings set disable-ipv6=yes
   ```
   * Disables IPv6 processing.

### 10.5. MAC Server

*   **Purpose:** For remote management of MikroTik devices. Configured under `/tool mac-server`.
    ```
    /tool mac-server print
    ```
    * Displays the current mac server configuration.
    ```
    /tool mac-server set allowed-interface=all enabled=yes
    ```
    * Allow all interfaces to use mac server.

### 10.6. RoMON

*   **Purpose:** MikroTik's proprietary management protocol for managing networks. Configured under `/tool romon`.
*   **Example**:
    ```
   /tool romon set enabled=yes
   /tool romon print
   ```
   * Enable and print current RoMON configuration.

### 10.7. WinBox

*   **GUI Interface:** MikroTik's primary graphical interface for configuration and monitoring.
*   **Secure Connection:** Use secure connections with HTTPS.

### 10.8. Certificates

*   **Purpose:** Used for secure connections (HTTPS, VPNs). Configured under `/certificate`.
    ```
    /certificate print
    ```
    * List current certificates.
    ```
    /certificate generate-self-signed name=test-cert common-name=test
    ```
    * Generate a self-signed certificate.

### 10.9. PPP AAA

*   **Purpose:** Authentication, Authorization, and Accounting for PPP connections. Configured under `/ppp aaa`.
*   **RADIUS Client**: Configure radius to authenticate with users.
    ```
    /ppp aaa set use-radius=yes
    /radius add address=192.168.1.10 secret=test_secret service=ppp timeout=20s
    ```

### 10.10. RADIUS

*   **Purpose:** Centralized Authentication for users.
*   **RADIUS Configuration:**
    ```
    /radius add address=192.168.1.10 secret=test_secret service=login timeout=20s
    ```
    *   `address=192.168.1.10`: RADIUS server IP.
    *   `secret=test_secret`: RADIUS shared secret.
    *   `service=login`: Service for authentication.
    *   `timeout=20s`: Timeout for connection to the RADIUS server.

### 10.11. User / User groups

*   **Users:** Can be configured under `/user`.
    ```
    /user print
    ```
     * Prints current configured users.
    ```
    /user add name=test_user password=test password-never-expires=yes group=read
    ```
    * Adds new user with the specified parameters.
*   **User Groups**: Configured under `/user group`.
    ```
    /user group print
    ```
    * Prints configured user groups.

### 10.12. Bridging and Switching

*   **Bridging**: (Explained above).

*   **Switching:**
    *   **Switch Chip Configuration:** MikroTik switches use a dedicated switch chip for fast layer-2 operations. Configuration under `/interface ethernet switch`.
     ```
        /interface ethernet switch print
     ```
     * Prints current switch configuration.

### 10.13. MACVLAN

*   **Purpose:** Creates multiple virtual network interfaces on a single physical interface, each with a unique MAC address.
*  **Example**:
    ```
    /interface macvlan add interface=ether1 mac-address=00:11:22:33:44:55 name=macvlan1
    ```
    *   `interface=ether1`: Specifies the physical interface.
    *   `mac-address=00:11:22:33:44:55`: Specific MAC address for the macvlan.
    *   `name=macvlan1`: The name of the new interface.

### 10.14. L3 Hardware Offloading

*   **Purpose:** To offload L3 operation to switch hardware.
*   **Configuration:** Mostly automatic if the hardware supports it. Can be checked using `/interface ethernet print`.
  ```
    /interface ethernet print
  ```
    * Check the `l3-hw-offload` flag.

### 10.15. MACsec

*   **Purpose:**  A security standard that provides secure communication at the data link (layer 2) level between two network nodes. Configured under `/interface ethernet macsec`.
    ```
     /interface ethernet macsec print
    ```
    * Prints current MACsec configuration.

### 10.16. Quality of Service (QoS)

*   **Purpose:** Manages network traffic priority using queues. Configured using `/queue`.
*   **Example:**
    ```
   /queue simple add name=queue-low target=vlan-34 max-limit=1M
    ```
   * Add a queue to limit bandwidth on vlan-34

### 10.17. Switch Chip Features

*   **VLAN Filtering:** Configurable in `/interface ethernet switch vlan`.
    ```
     /interface ethernet switch vlan print
    ```
    * Prints the vlan configuration on the switch.

### 10.18. VLAN

*   **VLAN Tagging:** (Covered in main example).

### 10.19. VXLAN

*   **Purpose:** Network virtualization protocol for overlay networks. Configured using `/interface vxlan`.
    ```
     /interface vxlan print
    ```
    * Prints current VXLAN interfaces.

### 10.20. Firewall and Quality of Service

*   **Connection Tracking**: Core to the operation of MikroTik's firewall.
    * Configuration: `/ip firewall connection`.
*   **Firewall:** Filters traffic based on configurable rules.
    * Configuration: `/ip firewall filter` for forwarding rules, `/ip firewall nat` for NAT rules.
   ```
        /ip firewall filter print
        /ip firewall nat print
   ```
   * Prints current rules.
    ```
        /ip firewall filter add chain=input action=accept comment="Allow Established" connection-state=established,related
    ```
    * Add a firewall rule to allow established and related traffic to the input chain.
*   **Packet Flow in RouterOS:** Understanding the packet flow is critical to writing correct firewall rules. Input chain is used for traffic to the router, forward is used for traffic passing through, and output chain is used for traffic leaving the router.
*   **Queues:** Manage bandwidth for specific traffic. (Covered above).
*   **Kid Control, UPnP, NAT-PMP:** Specific features with unique use cases, configured in respective submenus of the firewall.

### 10.21. IP Services

*   **DHCP Server:** Configures a DHCP server to assign IP addresses.
    * Configured under `/ip dhcp-server`.
*   **DNS Server:** Configures a DNS server to resolve domain names.
    * Configured under `/ip dns`.
*  **SOCKS/Proxy**: Configured under `/ip socks` and `/ip proxy`.

### 10.22. High Availability Solutions

*   **Load Balancing:** Distributes traffic across multiple links. Can be configured using Equal-Cost Multi-Path routing (ECMP) or more advanced methods.
    ```
    /ip route add dst-address=0.0.0.0/0 gateway=175.198.14.2 distance=1
    /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 distance=2
    ```
    * Adds two gateways for load balancing, using distance for preference.
*   **Bonding:** Combines multiple physical links into one virtual link for redundancy and load balancing. Configured under `/interface bonding`.
*   **VRRP**: Creates a virtual router with one active at a time. Configured under `/interface vrrp`.

### 10.23. Mobile Networking

*   **GPS:** Allows for GPS data to be collected. Configured under `/system gps`.
*   **LTE:** Allows for connection via LTE network. Configured under `/interface lte`.
*  **PPP, SMS**: Configured under respective menu items under `/interface`.

### 10.24. MPLS

* **MPLS Overview**: MPLS is a routing method to direct packets via labels instead of network addresses.
*  **Configuration**: Requires complex understanding and specific topology to properly be configured. Configured under `/mpls`.

### 10.25. Network Management

*   **ARP:** Address Resolution Protocol, used to resolve IP addresses to MAC addresses. `/ip arp`.
*   **Cloud, DHCP, DNS, SOCKS, Proxy**: (Explained above).
*   **Openflow**: Network protocol that allows configuration of the network, via Openflow controllers. Configured under `/openflow`.

### 10.26. Routing

* **Routing Protocol Overview:** (Explained above).
* **OSPF, RIP, BGP**: Common routing protocols, for routing traffic between networks. Configured under `/routing ospf`, `/routing rip`, `/routing bgp`.
* **Policy Routing, VRF**:  (Explained above).
* **Route Selection and Filters**: Used to control route selection and which routes to accept/reject.

### 10.27. System Information and Utilities

*   **Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP**:  Various tools and services available in RouterOS, to configure the device, and monitor system, that are out of the scope of this explanation.
*   **Services**: Allows control of the services running on the router. Configured under `/ip services`.

### 10.28. Virtual Private Networks (VPNs)

*   **6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier**: All common VPN protocols used in RouterOS for establishing secure encrypted connections, configured under `/interface` and/or `/ip/ipsec` and specific submenu for each protocol.

### 10.29. Wired Connections

*   **Ethernet**: The basic interface for most wired connections.
*   **MikroTik wired interface compatibility, PWR Line**: Check for specific models and compatibility in vendor's documentation.
*   **MTU**: Configured under `/interface ethernet`. Should be configured in order to match the underlying layer 2 network.

### 10.30. Wireless

*   **WiFi, Wireless Interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, Spectral scan**: Various options and tools for configuring wireless connections and monitoring network health.

### 10.31. Internet of Things

*   **Bluetooth, GPIO, Lora, MQTT**:  Specific IoT features are available for compatible hardware.

### 10.32. Hardware

*   **Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features**: Information specific to the device hardware. MTU should be configured according to the underlying layer 2 network.

### 10.33. Diagnostics, monitoring and troubleshooting

*   **Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats and monitor-traffic, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 general guidance, Torch, Traceroute, Traffic Flow, Traffic Generator, Watchdog:** Various tools that can be used to troubleshoot and monitor the health and operation of the router.
    * (Covered above).

### 10.34. Extended features

* **Container**: Docker containers can be run on RouterOS if supported. Configured under `/container`.
*   **DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, IP packing**: Additional features that expand the functionality of MikroTik devices.

## Conclusion

This document has provided an in-depth look at configuring basic IP routing for a point-to-point link on a MikroTik router, with a strong emphasis on practical implementation using CLI and Winbox. We've also covered related concepts, security best practices, and many of RouterOS's features, along with troubleshooting and diagnostic tools. This should provide a comprehensive guide for anyone looking to understand basic IP configuration on MikroTik routers. Remember to tailor the configurations to your specific network needs, and always test thoroughly before deploying to a live environment.
