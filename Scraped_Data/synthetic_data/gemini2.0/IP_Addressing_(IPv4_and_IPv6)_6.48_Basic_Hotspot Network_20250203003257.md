Okay, let's craft some in-depth documentation for configuring IP addressing on a MikroTik router, specifically for the provided scenario, while touching on a wide array of RouterOS features and concepts.

## MikroTik RouterOS Configuration for Hotspot Network: IP Addressing (IPv4)

This document provides a comprehensive guide to configuring IP addressing on a MikroTik router for a Hotspot network, focusing on IPv4 within the specified subnet. We will explore both CLI and Winbox configuration, as well as various related features and troubleshooting tips.

**Context:**

*   **RouterOS Version:** 6.48 (primarily), with some notes for 7.x
*   **Configuration Level:** Basic (with some excursions into Advanced)
*   **Network Scale:** Hotspot Network (SOHO focus)
*   **Subnet:** 240.40.48.0/24
*   **Interface Name:** wlan-18

**1. Comprehensive Configuration Scenario**

The goal is to provide a reliable network for a small Hotspot, allowing devices to connect wirelessly, obtain IP addresses within the designated subnet (240.40.48.0/24), and access the internet. We will also cover essential aspects such as DHCP server configuration, firewall rules, and security considerations specific to MikroTik.

**Specific MikroTik Requirements:**

*   Assign a static IPv4 address to the `wlan-18` interface.
*   Configure a DHCP server to dynamically assign IP addresses within the specified subnet to connected clients.
*   Setup basic firewall rules for security.
*   Implement basic traffic shaping and QoS.

**2. Step-by-Step MikroTik Implementation (CLI)**

Here's how to configure IP addressing via the command-line interface (CLI):

*   **Step 1: Assign Static IP Address to Interface:**

    ```mikrotik
    /ip address
    add address=240.40.48.1/24 interface=wlan-18 comment="Hotspot Network Address"
    ```

    **Explanation:**

    *   `/ip address`: Navigates to the IP address configuration menu.
    *   `add`: Adds a new IP address entry.
    *   `address=240.40.48.1/24`: Specifies the IP address and subnet mask (CIDR notation) for the interface. The router itself will have `240.40.48.1`.
    *   `interface=wlan-18`:  Specifies that the IP address should be assigned to the `wlan-18` interface.
    *   `comment="Hotspot Network Address"`: Adds a human-readable description (optional).

*   **Step 2: Create an IP Pool for DHCP:**

    ```mikrotik
    /ip pool
    add name=hotspot-pool ranges=240.40.48.10-240.40.48.254
    ```

    **Explanation:**

    *   `/ip pool`: Navigates to the IP pool configuration menu.
    *   `add`: Adds a new IP pool entry.
    *   `name=hotspot-pool`:  Names the IP pool to `hotspot-pool`.
    *   `ranges=240.40.48.10-240.40.48.254`: Defines the range of IP addresses available for DHCP assignment. Note, we avoid the first IP and start from `.10` to avoid issues and leave IP address range for static ip addresses.

*   **Step 3: Configure the DHCP Server:**

    ```mikrotik
    /ip dhcp-server
    add address-pool=hotspot-pool interface=wlan-18 lease-time=10m name=hotspot-dhcp
    /ip dhcp-server network
    add address=240.40.48.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=240.40.48.1
    ```

    **Explanation:**

    *   `/ip dhcp-server`: Navigates to the DHCP server configuration menu.
    *   `add address-pool=hotspot-pool interface=wlan-18 lease-time=10m name=hotspot-dhcp`:
        *   Creates a DHCP server.
        *   `address-pool=hotspot-pool`: Specifies the pool of IP addresses to use for allocation (created in step 2).
        *   `interface=wlan-18`: Assigns the DHCP server to the `wlan-18` interface.
        *   `lease-time=10m`: Sets the lease duration to 10 minutes, can be increased as needed (`h` for hours, `d` for days).
        *   `name=hotspot-dhcp`: Names the DHCP server instance.
    *   `/ip dhcp-server network`: Navigates to the DHCP network settings.
        * `add address=240.40.48.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=240.40.48.1`:
        *   `address=240.40.48.0/24`:  Specifies the network the dhcp server services.
        *   `dns-server=8.8.8.8,8.8.4.4`: Sets the DNS servers handed to clients (Google DNS).
        *   `gateway=240.40.48.1`: Sets the default gateway (router's address).

*   **Step 4: Enable basic NAT:**

    ```mikrotik
      /ip firewall nat
      add chain=srcnat action=masquerade out-interface=pppoe-out1
    ```
    **Explanation:**
    * `/ip firewall nat` : Navigates to the NAT configuration menu.
    * `add chain=srcnat action=masquerade out-interface=pppoe-out1` : Adds a rule that will masquerade traffic leaving the router through interface `pppoe-out1`. Usually it is the WAN internet access interface.

**3. Complete MikroTik CLI Configuration Commands**

Here's the complete CLI configuration:

```mikrotik
/ip address
add address=240.40.48.1/24 interface=wlan-18 comment="Hotspot Network Address"
/ip pool
add name=hotspot-pool ranges=240.40.48.10-240.40.48.254
/ip dhcp-server
add address-pool=hotspot-pool interface=wlan-18 lease-time=10m name=hotspot-dhcp
/ip dhcp-server network
add address=240.40.48.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=240.40.48.1
/ip firewall nat
add chain=srcnat action=masquerade out-interface=pppoe-out1
```

**4. Common Pitfalls, Troubleshooting, and Diagnostics**

*   **Error:** DHCP clients not getting IP addresses.
    *   **Cause:** Incorrect IP address configuration on the `wlan-18` interface, wrong DHCP pool settings, or a firewall blocking DHCP.
    *   **Troubleshooting:**
        *   Use `/ip address print` to check IP address assignment on `wlan-18`.
        *   Use `/ip dhcp-server print` and `/ip pool print` to verify DHCP server and IP pool settings.
        *   Use `/ip firewall filter print` to check for blocking rules.
        *   Check the logs `/system logging print` for DHCP errors.
*   **Error:** Clients cannot connect to the internet.
    *   **Cause:**  Missing NAT rules, incorrect default route, or DNS issues.
    *   **Troubleshooting:**
        *   Ensure there is a masquerade NAT rule `/ip firewall nat print`.
        *   Use `/ip route print` to verify the default route.
        *   Verify DNS server settings in `/ip dhcp-server network print`
*   **Error:** Interface `wlan-18` not active, or not listed.
    *   **Cause:** Interface disabled, hardware issue, or incorrect configuration.
    *   **Troubleshooting:**
        *   Use `/interface print` to verify interface status. Enable if needed: `/interface enable wlan-18`
        *   Check hardware logs for issues.

**5. Verification and Testing**

*   **Ping:** From a client connected to the Hotspot, ping the router's IP: `ping 240.40.48.1`.
*   **Traceroute:**  Use `traceroute 8.8.8.8` to test path to external network
*   **Torch:** Use `tool torch interface=wlan-18` on the router to monitor traffic.
*   **DHCP Leases:** View connected clients and allocated IP addresses: `/ip dhcp-server lease print`.

**6. Related MikroTik Features, Capabilities, and Limitations**

*   **IP Pools:** Allows granular IP range management, useful in larger networks with multiple DHCP scopes.
*   **DHCP Options:** Customize DHCP server to provide additional information to clients (e.g., NTP server).
    ```mikrotik
    /ip dhcp-server option
    add code=42 name=ntp-server value=192.168.88.1 # example setting the ntp to the router
    /ip dhcp-server network
    set 0 dhcp-option=ntp-server # Setting ntp-server to first network, can use the network number from print
    ```
*   **Static Leases:** Assign specific IP addresses to specific MAC addresses via DHCP:
    ```mikrotik
    /ip dhcp-server lease
    add address=240.40.48.100 mac-address=AA:BB:CC:DD:EE:FF server=hotspot-dhcp
    ```
*   **Limitations:**  Maximum DHCP leases depend on the RouterBoard model and available RAM. Be aware, that RouterOS has limit on addresses pool and DHCP addresses.

**7. MikroTik REST API Examples**

*   **API Endpoint:**  `/ip/address`
*   **Request Method:** POST (to add an address)
*   **Example JSON Payload:**

    ```json
    {
      "address": "240.40.48.2/24",
      "interface": "wlan-18",
       "comment" : "Second IP for hotspot"
    }
    ```
*   **Expected Response (successful):**

    ```json
    {
      "message": "added",
      "id": "*1"  // Example ID
    }
    ```

*  **API Endpoint:** `/ip/dhcp-server/network`
*  **Request Method:** POST (to add a dhcp-network)
*   **Example JSON Payload:**
    ```json
    {
      "address" : "240.40.49.0/24",
       "dns-server" : "8.8.8.8,8.8.4.4",
       "gateway" : "240.40.49.1"
    }
    ```
*   **Expected Response (successful):**
    ```json
     {
       "message": "added",
       "id": "*1" // Example ID
     }
    ```
    **Note:** The MikroTik API requires authentication using token. Also, some endpoints require specific permission to be accessed.

**8. In-depth Explanations of Core Concepts**

*   **Bridging:** The concept of grouping multiple interfaces into a single logical interface. Not directly used in this example, but crucial when combining wired and wireless interfaces or working with VLANs.
*   **Routing:** In this setup, routing is simple, clients use the router as a gateway (240.40.48.1) to reach other networks. For more complex routing scenarios you can use `IP Route` rules to specify route to reach the internet using the router IP.
*   **Firewall:** Implemented with the `/ip firewall` submenu. The example uses basic `masquerade` NAT. However, it can be extended with rules to control what traffic is allowed into and out of the network.
*   **DHCP:** The Dynamic Host Configuration Protocol. Allows the router to automatically assign IP address, DNS, Gateway and other necessary configuration for clients connecting to the network.

**9. Security Best Practices**

*   **Strong Router Password:** Always set a strong password for your router's admin user.
*   **Disable Unnecessary Services:** Turn off services you don't need (e.g., API, telnet). `/ip service disable api`
*   **Firewall Rules:** Implement robust firewall rules to block unwanted traffic.
*   **Regular Updates:** Keep RouterOS updated to patch vulnerabilities.
*   **HTTPS for Winbox/Webfig**: Secure access to RouterOS with certificates. See topic below.

**10. Detailed Explanations and Configuration Examples (Selected Topics)**

**Note: Some examples may be a bit complex for this example, but important for the MikroTik ecosystem.**

*   **IP Addressing (IPv4 and IPv6):**
    *   **IPv4:** As demonstrated above, we assign static addresses, create pools, and configure DHCP.
    *   **IPv6:** Similar configuration to IPv4, but requires more advanced knowledge of IPv6 networking (Prefix delegation etc.). We can assign addresses manually using the `/ipv6 address` configuration menu, and use the `/ipv6 dhcp-server` for IP assignation.
*   **IP Pools:**
    *   Used by the DHCP server to allocate addresses dynamically. Can be used also in other features like Hotspot and Address-Lists for Firewall Rules.
*   **IP Routing:**
    *   Used to specify the routes the router will use to send packets to destinations. Can be `static` or `dynamic` using routing protocols like OSPF or BGP. `/ip route` menu.
*   **IP Settings:**
    *   Configures global IP settings like the source address for connection tracking. Use `/ip settings` to configure global parameters.
*   **MAC Server:**
    *   Used by the `/tool mac-server` to provide access to the router using the MAC address. Often used for RouterBoard recovery using `Netinstall`.
*   **RoMON:**
    *   Router Management Overlay Network, allows management of routers through a dedicated network. Use `/tool romon` configuration menu.
*   **WinBox:**
    *   MikroTik's GUI configuration tool. Provides the same functionality as the CLI with visual representation.
*   **Certificates:**
    *   Used to secure access to Webfig, API and services. Generate certificates on `/certificate` menu, you can use Let's encrypt integration to generate free and valid certificates.
*   **PPP AAA:**
    *   Authentication, Authorization, and Accounting for PPP connections, often used for PPPoE/L2TP. `/ppp aaa` to configure.
*   **RADIUS:**
    *   Remote Authentication Dial-In User Service, used for centralized authentication, can be used with Hotspot, PPP. `/radius` config menu.
*   **User / User groups:**
    *   Used to control access to the router. You can create user groups and assign specific access permissions using `/user group`, `/user` menus.
*   **Bridging and Switching:**
    *   Used to connect different network segments. Can be configured in `/interface bridge` menu.
*   **MACVLAN:**
    *   Creates multiple virtual network interfaces sharing the same MAC address. Often used in containerization. `/interface macvlan` menu.
*   **L3 Hardware Offloading:**
    *   Offloads routing and switching tasks to the switch chip to improve performance. Can be configured on `/interface ethernet` (only on supported hardware).
*   **MACsec:**
    *   Link-layer security protocol that provides hop-by-hop encryption. Used for secure communication in Ethernet connections `/interface ethernet security`.
*   **Quality of Service (QoS):**
    *   Prioritizes traffic and limits bandwidth, ensuring crucial traffic isn't impacted by less important traffic. Implemented in the `/queue` menu.
*   **Switch Chip Features:**
    *   MikroTik routers often have switch chips with advanced features like VLAN tagging, port mirroring. `/interface ethernet switch` menu.
*   **VLAN:**
    *   Virtual LANs, allows creation of multiple logical networks on the same physical infrastructure. Used in `/interface vlan` and bridge configuration.
*   **VXLAN:**
    *   Virtual Extensible LAN, used for Layer 2 tunneling over Layer 3 networks. Used in `/interface vxlan`.
*   **Firewall and QoS (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP):**
    *   See section 8 explanation. All configurations are done on `/ip firewall` and `/queue` menus.
*   **IP Services (DHCP, DNS, SOCKS, Proxy):**
    *   `/ip dhcp-server`, `/ip dns`, `/ip socks`, `/ip proxy`. Configures all mentioned services to support the network needs.
*   **High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples):**
    *   Used for network resilience, configurations varies based on the type of HA solution. `/interface bonding` and `/interface vrrp` menus.
*   **Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application):**
    *   If your router has mobile capabilities, configure `/interface lte` and use related features. `/system gps` menu for GPS configuration.
*   **Multi Protocol Label Switching - MPLS (Including: MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference):**
    *   A data forwarding technique used in large and service provider networks. `/mpls` configuration menu.
*   **Network Management (Including: ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow):**
    *   Centralized network management with tools like ARP inspection `/ip arp`, `/cloud` config, DHCP, DNS, SOCKS, and Proxy, and OpenFlow for software-defined networking.
*   **Routing (Including: Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS):**
    *   Multiple routing protocols for dynamic network routing. `/routing` config menu.
*   **System Information and Utilities (Including: Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP):**
    *   Tools for system operation. `/system` menu.
*   **Virtual Private Networks (Including: 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier):**
    *   Multiple tunneling options for secure network connectivity. `/interface` config menus for the corresponding protocols.
*   **Wired Connections (Including: Ethernet, MikroTik wired interface compatibility, PWR Line):**
    *   Configuration of the wired interfaces, check compatibility with RouterBoard on `/interface ethernet` menu.
*   **Wireless (Including: WiFi, Wireless Interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, Spectral scan):**
    *   Wireless network configuration, use `/interface wireless` and `/capsman` for centralized management.
*   **Internet of Things (Including: Bluetooth, GPIO, Lora, MQTT):**
    *   Additional configuration options for specialized devices, you can check the device compatibility and documentation to find the correct commands.
*   **Hardware (Including: Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features):**
    *  Hardware information, usually no configuration, check the documentation for each of the parameters.
*   **Diagnostics, monitoring and troubleshooting (Including: Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats and monitor-traffic, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 general guidance, Torch, Traceroute, Traffic Flow, Traffic Generator, Watchdog):**
    *   Essential tools for troubleshooting and monitoring of the device.
*  **Extended features (Including: Container, DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, IP packing):**
    *  Specialized features for advanced tasks. Check the compatibility of the feature with your RouterBoard.

This detailed explanation, with examples, should cover your requirements. Please ask if you have further questions or need more specific configurations. Remember to adjust configurations as needed for your specific hardware and network setup.
