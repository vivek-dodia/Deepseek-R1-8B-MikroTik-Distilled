Okay, let's dive deep into MikroTik RouterOS, focusing on IP Addressing for a SOHO environment, as requested. This documentation will be comprehensive and will cover all the specified areas. We'll use RouterOS 6.48 as our base, but many concepts will apply to version 7.x as well.

# MikroTik RouterOS IP Addressing & Beyond: SOHO Implementation

## 1. Comprehensive Configuration Scenario and Requirements

Our SOHO scenario involves a typical home network with the following requirements:

*   **WAN Connection:** A single internet connection via DHCP.
*   **LAN Network:** A private network using the 192.168.88.0/24 subnet.
*   **Wireless Access:** A Wi-Fi network using the same subnet as the LAN.
*   **Basic Security:** Basic firewall configuration to protect the internal network.
*   **IPv6 Support:** To prepare for the future, basic IPv6 configuration, if the ISP provides it.

**MikroTik Specific Requirements:**

*   RouterOS v6.48+
*   Using Winbox or CLI for configuration.
*   Emphasis on command-line implementation with GUI explanation.
*   Practical, easily verifiable configuration.
*   Best practices implementation.

## 2. Step-by-Step MikroTik Implementation (CLI/Winbox)

Here is a step-by-step guide on how to implement the above scenario using CLI commands. I will also note the equivalent actions in Winbox when applicable.

### Step 1: Basic System Setup

*   **CLI:**
    ```mikrotik
    /system identity set name="SOHO-Router"
    /system clock set time-zone-name=America/New_York #or your timezone
    ```
*   **Winbox:**
    *   Navigate to *System > Identity* to set the Router name.
    *   Navigate to *System > Clock* to set timezone.

### Step 2: Interface Configuration

*   **WAN Interface (assuming `ether1` is the WAN):**
    ```mikrotik
    /interface ethernet set ether1 name=WAN
    ```
    *   **Winbox:**
        *   Navigate to *Interfaces*, double click `ether1`, rename it to `WAN`.
*   **LAN Interface (assuming `ether2` is the LAN):**
    ```mikrotik
    /interface ethernet set ether2 name=LAN
    ```
    *   **Winbox:**
        *   Navigate to *Interfaces*, double click `ether2`, rename it to `LAN`.
*   **Wireless Interface (assuming `wlan1` is the wireless interface):**
    ```mikrotik
    /interface wireless set wlan1 mode=ap-bridge ssid=MySOHO-WiFi band=2ghz-b/g/n security-profile=default
    /interface wireless set wlan1 disabled=no
    ```
   *  **Winbox:**
        *   Navigate to *Wireless*, double click `wlan1`.
        *   Set *Mode* to *ap-bridge*, set *SSID* to `MySOHO-WiFi`, *Band* to *2ghz-b/g/n*.
        *   Go to the *Wireless > Security Profiles* tab, double click the *default* profile and change to the security profile and pre-shared key you need.
        *   Enable `wlan1` in the *Interfaces* menu.

### Step 3: IP Addressing (IPv4)

*   **Assign a static IP to LAN interface (192.168.88.1/24):**
    ```mikrotik
    /ip address add address=192.168.88.1/24 interface=LAN
    ```
    *   **Winbox:**
        *   Navigate to *IP > Addresses*, click the plus sign (+).
        *   Add Address, interface and apply.

*   **Enable DHCP Server for the LAN interface:**
    ```mikrotik
    /ip dhcp-server add address-pool=default disabled=no interface=LAN name=dhcp-lan
    /ip dhcp-server network add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
    ```
   *  **Winbox:**
        * Navigate to *IP > DHCP Server*, click the plus sign (+).
        * Select `LAN` in the interface dropdown, name your DHCP server,  apply.
        * Go to the *Networks* tab, click the plus sign (+)
        * Enter your network `192.168.88.0/24`, `192.168.88.1` for the gateway and DNS, apply.
*   **DHCP Client Configuration (for WAN if applicable):**
    ```mikrotik
    /ip dhcp-client add interface=WAN disabled=no
    ```
    *   **Winbox:**
        *   Navigate to *IP > DHCP Client*, click the plus sign (+).
        *   Select the `WAN` interface, and enable.

### Step 4: NAT and Basic Firewall

*   **Basic NAT (Masquerading):**
    ```mikrotik
    /ip firewall nat add chain=srcnat action=masquerade out-interface=WAN
    ```
   *  **Winbox:**
        *   Navigate to *IP > Firewall*, go to the *NAT* tab, click the plus sign (+).
        *   Set *Chain* to *srcnat*, *Out. Interface* to *WAN*, *Action* to *masquerade*.
*   **Basic Firewall:**
     ```mikrotik
      /ip firewall filter add chain=forward action=drop connection-state=invalid log=yes comment="Drop Invalid Connections"
      /ip firewall filter add chain=forward action=accept connection-state=established,related log=yes comment="Accept Established, Related"
      /ip firewall filter add chain=forward action=drop in-interface=WAN log=yes comment="Drop new connection in WAN"
      /ip firewall filter add chain=input action=accept in-interface=LAN log=yes comment="Accept all input from LAN"
      /ip firewall filter add chain=input action=drop connection-state=invalid log=yes comment="Drop Invalid connections to router"
      /ip firewall filter add chain=input action=accept connection-state=established,related log=yes comment="Accept Established, Related connections to router"
      /ip firewall filter add chain=input action=drop in-interface=WAN log=yes comment="Drop all new connections from WAN to router"
    ```
   *  **Winbox:**
        *   Navigate to *IP > Firewall*, go to the *Filter Rules* tab, click the plus sign (+) multiple times, setting each of the filter rules accordingly.

### Step 5: IPv6 Basic Configuration (If applicable)

*   **Enable IPv6 package**
        ```mikrotik
         /system package enable ipv6
         ```
         *  **Winbox:**
             *  Navigate to *System > Packages*, enable the *ipv6* package and reboot.

*   **DHCPv6 Client Configuration**
    ```mikrotik
     /ipv6 dhcp-client add interface=WAN request=address,prefix
    ```
 *   **Winbox:**
      *Navigate to *IPv6 > DHCP Client*, click the plus sign (+) and select your *WAN* interface, apply.
*   **Assign IPv6 Address to LAN**
     ```mikrotik
        /ipv6 address add address=::1/64 interface=LAN
     ```
 *   **Winbox:**
      *Navigate to *IPv6 > Addresses*, click the plus sign (+), set address to *::1/64* and interface to *LAN*.

*  **Advertise prefixes for DHCPv6 in LAN**
    ```mikrotik
      /ipv6 nd add interface=LAN other-configuration=yes managed-address-configuration=no
    ```
 *   **Winbox:**
      *Navigate to *IPv6 > ND*, click the plus sign (+), select your `LAN` interface, check *other-configuration*, apply.

### Step 6: DNS Server Setup

*   **Configure DNS:**
    ```mikrotik
    /ip dns set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
    ```
    *   **Winbox:**
        *   Navigate to *IP > DNS* and enable *Allow Remote Requests*, add `8.8.8.8` and `8.8.4.4` to *Servers*.

## 3. Complete MikroTik CLI Configuration Commands

Here's a consolidated view of all the CLI commands:

```mikrotik
/system identity set name="SOHO-Router"
/system clock set time-zone-name=America/New_York

/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN

/interface wireless set wlan1 mode=ap-bridge ssid=MySOHO-WiFi band=2ghz-b/g/n security-profile=default
/interface wireless set wlan1 disabled=no

/ip address add address=192.168.88.1/24 interface=LAN
/ip dhcp-server add address-pool=default disabled=no interface=LAN name=dhcp-lan
/ip dhcp-server network add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
/ip dhcp-client add interface=WAN disabled=no

/ip firewall nat add chain=srcnat action=masquerade out-interface=WAN

/ip firewall filter add chain=forward action=drop connection-state=invalid log=yes comment="Drop Invalid Connections"
/ip firewall filter add chain=forward action=accept connection-state=established,related log=yes comment="Accept Established, Related"
/ip firewall filter add chain=forward action=drop in-interface=WAN log=yes comment="Drop new connection in WAN"
/ip firewall filter add chain=input action=accept in-interface=LAN log=yes comment="Accept all input from LAN"
/ip firewall filter add chain=input action=drop connection-state=invalid log=yes comment="Drop Invalid connections to router"
/ip firewall filter add chain=input action=accept connection-state=established,related log=yes comment="Accept Established, Related connections to router"
/ip firewall filter add chain=input action=drop in-interface=WAN log=yes comment="Drop all new connections from WAN to router"

/system package enable ipv6
/ipv6 dhcp-client add interface=WAN request=address,prefix
/ipv6 address add address=::1/64 interface=LAN
/ipv6 nd add interface=LAN other-configuration=yes managed-address-configuration=no

/ip dns set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, Diagnostics

### Pitfalls
* **Firewall Misconfiguration**: Incorrect firewall rules are the most common issue. Double check your filter rules order.
* **DHCP Server Errors**: Ensure the DHCP server is assigned to the correct interface and the address pool does not conflict.
* **NAT Issues**: If internet access isn't working, make sure masquerading is enabled and the out-interface is correctly set to your WAN interface.
* **IPv6 Misconfiguration**: Make sure your provider provides you with IPv6 and you are using the right addressing.
* **Winbox Errors:** Using the same interface on winbox as you are configuring can cause loss of connection. Use MAC address when this happens.

### Troubleshooting
* **Ping:** The `ping` utility is used to test network connectivity. You can use the following commands:
    ```mikrotik
    /ping 8.8.8.8
    /ping 192.168.88.1
    ```
* **Traceroute:** The `traceroute` command helps you trace the path of your network traffic.
    ```mikrotik
    /traceroute 8.8.8.8
    ```
* **Torch:** The `torch` tool can monitor live traffic on an interface:
    ```mikrotik
    /tool torch interface=WAN duration=10s
    ```
*   **Log:** The RouterOS system log can be a valuable source of information for troubleshooting. Review the log frequently when debugging:
    ```mikrotik
     /system logging print
    ```
* **Interface Status:** Check interface status:
    ```mikrotik
    /interface print
    ```
    *   **Winbox:**
        *   Navigate to *Interfaces* and check for `R` (running) flags and see if errors are incrementing.
*   **DHCP Leases:** check assigned IP addresses
    ```mikrotik
    /ip dhcp-server lease print
    ```
    *  **Winbox:**
         * Navigate to *IP > DHCP Server > Leases*

### Diagnostics

*   **Resource Monitor:** Use the resource monitor to check CPU, memory, and disk usage:
    ```mikrotik
    /system resource print
    ```
    *   **Winbox:**
        *   Navigate to *System > Resources*.

## 5. Verification and Testing Steps

*   **Connectivity Test:**
    *   From a device on the LAN (connected by Ethernet or Wi-Fi), ping the router's LAN IP (192.168.88.1)
        ```bash
        ping 192.168.88.1
        ```
    *   Try pinging an external IP address (e.g., 8.8.8.8).
        ```bash
        ping 8.8.8.8
        ```
    *   Browse a webpage to confirm internet access.
*   **DHCP Test:**
    *  Check that a device gets an IP address automatically by the MikroTik DHCP Server.
    * Check the leases table with the command
    ```mikrotik
    /ip dhcp-server lease print
    ```
*   **Firewall Test:**
    *   Connect to the WAN interface from another network to see that you cannot connect to the router.
    *  Make sure that you can connect to the router from your LAN interface.
*   **IPv6 Test:**
    *   From your device in the LAN try to access IPv6 only websites like [test-ipv6.com](http://test-ipv6.com)
    *   Run the command `ipconfig /all` on windows or `ip a` on linux and check that you have a proper IPv6 address in your LAN interface.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

### IP Addressing
*   **Static and Dynamic Addressing:** Supports both static IP addresses and dynamic addressing via DHCP.
*   **Multiple Subnets:** RouterOS can manage multiple subnets on different interfaces.
*   **VRF:** Virtual Routing and Forwarding, enables the creation of separate routing domains on the same router.
*   **Multiple IPs on an Interface:** RouterOS can handle multiple IP addresses on the same interface.
*   **IPv6 Support:** Full IPv6 support, including address assignment, routing, and firewalling.
*  **Limitations:** While the RouterOS allows for a great number of interfaces and IP addresses it is limited to the underlying hardware capabilities.

### IP Pools
*   **Address Pools:** Used for managing dynamic address allocation, specifically DHCP.
    ```mikrotik
    /ip pool add name=dhcp_pool ranges=192.168.88.100-192.168.88.200
    ```
    *   **Winbox:**
        * Navigate to *IP > Pool*, and add the pool.

### IP Routing
*   **Static Routing:** Manually define routes to specific networks:
    ```mikrotik
    /ip route add dst-address=10.0.0.0/24 gateway=192.168.88.2
    ```
    *  **Winbox:**
        *  Navigate to *IP > Routes*, and add the static route.
*   **Dynamic Routing:** Supports various routing protocols such as OSPF, RIP, and BGP.
    * We will be exploring these protocols later in this document.
*   **Policy Based Routing:** Routes traffic based on policies, not just destination IP.
*  **Limitations:** RouterOS requires specific configurations to use all routing features and the underlying hardware may have specific throughput limitations.

### IP Settings
*   **Global Settings:** Includes options like TCP MSS, ARP settings, and other IP related configuration:
    ```mikrotik
    /ip settings set tcp-syn-cookies=yes
    ```
    *  **Winbox:**
        *  Navigate to *IP > Settings*, and enable the required feature.

### MAC server
*  **MAC Server:** Used for low level network access for devices that do not have a usable IP address. It allows you to connect to devices without IP addresses in an easy way.
    ```mikrotik
      /tool mac-server set allowed-interface-list=all
      /tool mac-server mac-winbox set allowed-interface-list=all
    ```
    *  **Winbox:**
      *Navigate to *Tools > Mac Server* and *Tools > Mac Server > Mac Winbox* and set `Allowed Interface List` to *all* or specific interfaces.

### RoMON
* **RoMON:** Router Management Overlay Network - allows you to manage MikroTik devices even if they are not on the same network by using MAC addresses.
*   RoMON is enabled globally, set the ID, and set the enabled interface list.
    ```mikrotik
     /tool romon set enabled=yes id=myromon
     /tool romon interface add interface=ether1
    ```
    *   **Winbox:**
        *   Navigate to *Tools > RoMON*, set the `Enabled` parameter, set your id and under the *Interfaces* tab select your interfaces that will be part of the RoMON network.

### WinBox
*   **GUI Interface:** The primary GUI tool to manage your RouterOS devices.
*   **Remote Access:** Connect remotely to RouterOS using Winbox via IP address or MAC address.
*   **Direct access:** Connect to the router from the LAN by accessing its IP in your browser or via the official WinBox application.
* **Limitations:** The winbox can stop working if you are making configurations to its own interface in the router, also it requires a working IP address for access.

### Certificates
*   **Certificate Management:** RouterOS can create and manage SSL certificates for secure connections (HTTPS, VPNs).
    *   Import existing certificates.
    *   Generate certificate signing requests.
*  **Limitations:** Requires some knowledge of PKI to configure the certificates properly.

### PPP AAA
* **PPP AAA:** Used to authenticate PPP connections using local or external databases.
*   **Authentication, Authorization and Accounting (AAA)**
    ```mikrotik
    /ppp profile add name="ppp-profile" use-encryption=yes
    ```
 *  **Winbox:**
     * Navigate to *PPP > Profiles*, and add a new profile for PPP authentication.

### RADIUS
*   **RADIUS Client:** Supports RADIUS for centralized user authentication.
    ```mikrotik
    /radius add address=192.168.100.1 secret=your_secret
    ```
    *   **Winbox:**
        *   Navigate to *RADIUS*, and add the Radius server address and secret.
*   **Use Case:** used in VPN authentication and wireless authentication.

### User / User Groups
*   **User Management:** Create and manage users with different permissions.
    ```mikrotik
    /user add name=admin_user password=securepassword group=full
    ```
    *   **Winbox:**
        *   Navigate to *System > Users*, add new user with full access.
*   **User Groups:** Allows grouping users for permissions management.
    *   `full`, `read`, `write` are built-in groups that provide different level of access to the router.
*  **Limitations:** Always use a strong password for the router, avoid generic user names.

### Bridging and Switching
*   **Bridging:** Combine multiple interfaces into a single layer 2 network.
    ```mikrotik
    /interface bridge add name=bridge-lan
    /interface bridge port add bridge=bridge-lan interface=LAN
    /interface bridge port add bridge=bridge-lan interface=wlan1
    ```
     *  **Winbox:**
         * Navigate to *Bridge*, add a new bridge.
         * Navigate to the *Ports* tab, add all the interfaces you need to the bridge.
*   **Switching:** MikroTik devices with switch chips provide hardware-based switching for faster throughput.
    *    RouterOS allows VLAN configurations and offloading.
* **Limitations:** not all MikroTik devices have a switch chip and if you do not use L3 hardware offload you are limited by your CPU throughput.

### MACVLAN
* **MACVLAN:** Create virtual interfaces with separate MAC addresses on a single physical interface.
    ```mikrotik
    /interface macvlan add interface=ether2 mac-address=02:00:00:00:00:01 name=macvlan-1
    ```
    *   **Winbox:**
        *   Navigate to *Interfaces* then *plus (+)* and select *MACVLAN*, select the interface and MAC address.
*  **Use Case:** Virtualized environments and network segmentation.
* **Limitations:** only a limited number of MACVLAN interfaces are allowed.

### L3 Hardware Offloading
*   **Hardware Offloading:**  Offload routing, switching, firewall and other tasks to the switch chip on your hardware for increased performance:
    ```mikrotik
    /interface ethernet set ether2 l3-hw-offloading=yes
    ```
     *  **Winbox:**
         * Navigate to *Interfaces*, double click on your *ether2* interface, on the *General* tab enable the `L3 Hardware Offloading` option.
*   **Benefits:** Reduced CPU usage, increased throughput.
*  **Limitations:** Not all interfaces support hardware offloading, certain features are not available when using hardware offloading.

### MACsec
*   **MACsec:**  MAC Layer Security, provides encryption on the link level for secure communication between devices in a LAN.
    ```mikrotik
        /interface macsec set enabled=yes
        /interface macsec add interface=ether1 cipher-suite=aes-128-gcm-16
    ```
  *  **Winbox:**
        * Navigate to *Interfaces*, double click on your *ether1* interface, on the *MACsec* tab set *Enabled* to `Yes` and choose the correct *Cipher Suite* .
        * Add the *MACsec* interface using *plus (+)* and select the new *MACsec* interface.
* **Limitations:** Requires that both ends of the link support MACsec, complex to implement and troubleshoot.

### Quality of Service
*   **QoS:** Control bandwidth allocation for different traffic types:
    *   **Queues:** Configure queues for rate limiting and prioritizing traffic:
    ```mikrotik
    /queue simple add target=192.168.88.0/24 max-limit=10M/10M name=lan_queue
    ```
        *  **Winbox:**
            * Navigate to *Queues > Simple Queues* and add a new queue with the target network and max-limit values.
    *   **Firewall Marking:** Mark packets using firewall rules for queueing purposes:
    ```mikrotik
    /ip firewall mangle add chain=prerouting action=mark-packet in-interface=ether1 new-packet-mark=mark-wan
    ```
        *  **Winbox:**
            *Navigate to *IP > Firewall > Mangle*, and add the mark rule.
    *   **Use Case:** Prioritize VoIP traffic over other data, limit bandwidth for specific users.
*   **Limitations:** QoS on MikroTik can be difficult to configure, complex queue trees are required for proper functionality.

### Switch Chip Features
*   **VLAN Support:**  Hardware-based VLAN support using the built-in switch chip
    *   **Tagging/Untagging:** Configure VLAN tagging and untagging on specific ports.
     ```mikrotik
       /interface vlan add interface=ether2 vlan-id=10 name=vlan10
    ```
        *  **Winbox:**
             * Navigate to *Interfaces*, *plus (+)* and select *VLAN*, select your interface and VLAN ID.
    *   **Port Isolation:** Isolate ports within the switch for security.
* **Limitations:** not all MikroTik hardware has a switch chip and can be used as a switch, these features may depend on the switch chip features and driver capabilities.

### VLAN
*   **Virtual LANs:** Create logical networks within a physical network.
    *   **Tagged/Untagged VLANs:** Support for both tagged and untagged VLAN traffic.
        ```mikrotik
        /interface vlan add interface=ether2 vlan-id=10 name=vlan10
        /ip address add address=192.168.10.1/24 interface=vlan10
        ```
            *  **Winbox:**
                 * Navigate to *Interfaces*, *plus (+)* and select *VLAN*, select your interface and VLAN ID.
                 * Navigate to *IP > Addresses*, add the address to the VLAN interface.
*   **Trunking:** Configure trunk ports to pass multiple VLANs.
*   **Use Case:** Network segmentation, improving security and manageability.
*   **Limitations:** Can add significant complexity to the network if not configured properly.

### VXLAN
*   **Virtual Extensible LANs:** Create overlay networks across existing network infrastructure.
    ```mikrotik
      /interface vxlan add name=vxlan1 vni=100 remote-address=192.168.1.1 interface=ether1
      /interface bridge add name=bridge-vxlan
      /interface bridge port add bridge=bridge-vxlan interface=vxlan1
    ```
      *   **Winbox:**
          *   Navigate to *Interfaces*, click the plus sign (+) and add a *VXLAN* interface, setting the VNI, remote address, and the underlying interface.
          *   Navigate to *Bridge*, click the plus sign (+), add a new bridge.
          *   Navigate to *Bridge > Ports*, click the plus sign (+) and add the *VXLAN* interface to the bridge.
*   **Use Case:** Extending layer 2 networks over layer 3 networks.
*  **Limitations:** VXLAN configurations are complex and resource intensive on the CPU and Memory.

### Firewall and Quality of Service (Detailed)

#### Connection Tracking
* **Connection Tracking:** RouterOS keeps track of connections which helps when defining firewall rules.
    *   Stateful firewall: Tracks connection states such as `established`, `related`, `invalid`.
    ```mikrotik
      /ip firewall connection print
    ```
* **Limitations:** Connection tracking consumes resources on the CPU and memory, it may limit the overall throughput on the router.

#### Firewall
*   **Filter Rules:** Block or allow traffic based on source/destination IPs, ports, and protocols.
*   **NAT Rules:** Translate private IP addresses to public IPs (masquerade) or vice versa.
*   **Mangle Rules:** Modify packets for QoS, routing decisions, and other purposes.
    *   `chain=prerouting`: Executes before routing decisions.
    *   `chain=forward`: Executes on transit traffic.
    *   `chain=input`: Executes on traffic destined to the router.
    *   `chain=output`: Executes on traffic originated from the router.
*   **Use Case:** Protect your network, enable access to services from the outside, prioritize traffic.
*   **Limitations:** Complex firewall rules can be challenging to troubleshoot.

#### Packet Flow in RouterOS
*  The packet flow is roughly divided into the following processes:
    *   **Prerouting:** First stop for all incoming traffic.
    *   **Input:** Traffic destined for the router itself.
    *   **Forward:** Traffic that is routed through the router
    *   **Output:** Traffic originating from the router.
    *   **Postrouting:** Last stop before exiting the router.
*   All of the different rules of `Firewall, Mangle and NAT` are executed at different stages of the packet flow.
*  **Limitations:** The knowledge of the packet flow is needed when designing a full network with a complex firewall.

#### Queues
*   **Simple Queues:** Basic rate limiting for individual IPs or subnets.
*   **Queue Tree:** Complex hierarchies for detailed traffic prioritization, bandwidth allocation and limiting.
    *   `parent`: Defines the parent queue for hierarchical configurations.
    *   `max-limit`: Maximum bandwidth for the queue.
    *   `burst-limit`: Bandwidth limit for short traffic bursts.
    *   `priority`: Priority of traffic.
* **Limitations:** Queue tree configurations are complex and resource intensive.

#### Firewall and QoS Case Studies
* **Limiting Bandwidth for Guest Network:**
    * Use `queue simple` to set a maximum upload and download for your Guest WiFi network
*   **Prioritizing VoIP Traffic:**
    * Use `mangle` to mark VoIP packets with a `packet-mark`.
    *   Use `queue tree` to prioritize packets marked as VoIP by assigning a higher `priority` to the queue.
*  **Case Study:** Setting up QoS to ensure that video conference have a higher priority than normal browsing traffic.
    * Use `mangle` to mark all video conference traffic (based on port)
    * Use `queue tree` to give high priority to the marked packets.

#### Kid Control
*   **Time-Based Firewall Rules:** Allow or block internet access based on time or day.
    ```mikrotik
      /ip firewall filter add chain=forward action=drop in-interface=LAN dst-port=80,443 time=0s-17h,sun-sat log=yes comment="Block internet for kids"
      /ip firewall filter add chain=forward action=accept in-interface=LAN dst-port=80,443 time=17h-0s,sun-sat log=yes comment="Allow internet for kids"
    ```
 *   **Winbox:**
        *  Navigate to *IP > Firewall > Filter Rules*, and add the rules, setting the time in the advanced tab.
*   **Use Case:** Limiting the amount of time that devices can access the internet.
*   **Limitations:** The configuration can become difficult to manage if there are multiple devices and time restrictions.

#### UPnP
*   **Universal Plug and Play (UPnP):** Automatically create firewall rules for services behind the router.
    ```mikrotik
    /ip upnp set enabled=yes
    ```
    *  **Winbox:**
        *  Navigate to *IP > UPnP*, enable the *Enabled* checkbox.
*   **Use Case:** Allows automatic port forwarding by devices.
*   **Security Risk:** May pose security risks as the router will automatically open ports for different devices, this should be used with caution.

#### NAT-PMP
*  **NAT Port Mapping Protocol (NAT-PMP):** Similar to UPnP, but specific for Apple devices.
  ```mikrotik
    /ip natpmp set enabled=yes
  ```
    *  **Winbox:**
          *  Navigate to *IP > NAT-PMP* and enable the *Enabled* checkbox.
*   **Use Case:** Allows Apple devices to automatically map external ports to internal services.
*   **Security Risk:** Similar to UPnP, NAT-PMP can be used to open unnecessary ports, and should be used with caution.

### IP Services

#### DHCP
*   **DHCP Server:** Provides automatic IP address assignment to clients.
*   **Lease Management:** Displays and manages DHCP leases.
*   **Static Leases:** Assign specific IP addresses to clients based on their MAC addresses.
    ```mikrotik
    /ip dhcp-server lease add address=192.168.88.100 mac-address=AA:BB:CC:DD:EE:FF server=dhcp-lan
    ```
  *  **Winbox:**
        *   Navigate to *IP > DHCP Server > Leases*, and add the static IP for the MAC address.
*   **Use Case:** Automatically configure devices connected to the network.
*  **Limitations:** The DHCP server should be configured to avoid IP conflicts and provide proper lease times.

#### DNS
*   **DNS Server:** Caches DNS queries to speed up browsing and provide local name resolution.
    *   **Static DNS entries:** Add local domain names to resolve to specific IP addresses.
    ```mikrotik
     /ip dns static add address=192.168.88.1 name=myrouter.lan
    ```
    *  **Winbox:**
        * Navigate to *IP > DNS > Static*, and add the static address entry.
*   **DNS Forwarding:** Forwards queries to external DNS servers.
*   **Use Case:** Provide proper DNS resolution for clients in your network.
*  **Limitations:** Local DNS server can be used for caching but does not provide advanced functionality.

#### SOCKS
*   **SOCKS Proxy:** Allows client to access internet through the Router.
    ```mikrotik
      /ip socks set enabled=yes port=1080
    ```
    *  **Winbox:**
       * Navigate to *IP > SOCKS*, enable the SOCKS Proxy and change the default port.
*   **Use Case:** Secure access to external services via proxy.
*  **Limitations:** Security implications should be carefully considered since it can become a vulnerable point in the network.

#### Proxy
*   **Web Proxy:** Caches web content to improve browsing speeds and security.
    ```mikrotik
      /ip proxy set enabled=yes port=8080
    ```
   *  **Winbox:**
         *  Navigate to *IP > Proxy*, enable the web proxy.
*  **Use Case:** Improve network performance, content filtering, logging access.
*  **Limitations:** Can use high CPU and memory for caching, should be configured carefully.

### High Availability Solutions

#### Load Balancing
*   **Multiple WAN Connections:** Route traffic over multiple internet connections.
    *   **Per-connection Load Balancing:** Load balance on a per connection basis, it can load balance new connections to the different links.
        ```mikrotik
        /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 check-gateway=ping distance=1
        /ip route add dst-address=0.0.0.0/0 gateway=192.168.2.1 check-gateway=ping distance=2
       ```
*   **Use Case:** Increase bandwidth and redundancy.
*   **Limitations:** Routing protocols are required for advanced configurations and better failure detection.

#### Bonding
*   **Interface Bonding (Link Aggregation):** Combine multiple physical interfaces into a single logical interface for increased bandwidth and redundancy.
    ```mikrotik
    /interface bonding add name=bond1 mode=802.3ad slaves=ether1,ether2 transmit-hash-policy=layer-2
    ```
    *   **Winbox:**
       * Navigate to *Interfaces*, click on the *plus (+)* sign, select *Bonding*, select your interfaces and bonding protocol.
*   **Use Case:**  Increase bandwidth and redundancy for wired connections.
*  **Limitations:** Requires that your switch supports the bonding protocol.

#### Bonding Examples
*   **802.3ad (LACP):** The most common bonding protocol, requires negotiation between the two end devices.
*   **Balance-RR (Round Robin):** Distribute traffic evenly between all the links.
*   **Active-Backup:** One link is used for traffic, others are in