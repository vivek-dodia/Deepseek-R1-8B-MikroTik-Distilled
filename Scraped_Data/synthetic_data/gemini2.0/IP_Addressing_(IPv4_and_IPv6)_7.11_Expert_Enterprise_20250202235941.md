Okay, let's delve into a comprehensive exploration of IP Addressing and related features on MikroTik RouterOS 7.11, tailored for an enterprise environment. This document will cover the requested topics with an expert-level approach.

# MikroTik RouterOS: Enterprise IP Addressing & Networking

## 1. Comprehensive Configuration Scenario & Requirements

**Scenario:** We have a medium-sized enterprise network with multiple VLANs, requiring both IPv4 and IPv6 connectivity. The main goals are:

*   **VLAN Segmentation:** Separate networks for users (VLAN 10), servers (VLAN 20), and management (VLAN 30).
*   **IPv4 Address Management:** Utilize DHCP for user VLAN and static IPs for servers and management.
*   **IPv6 Deployment:** Enable IPv6 for future-proofing, utilizing SLAAC for user VLAN and static IPs for servers and management.
*   **Inter-VLAN Routing:** Allow routing between VLANs while enforcing firewall rules.
*   **Internet Connectivity:** Provide NAT for IPv4 and IPv6 for internal users.
*   **Remote Management:** Secure remote access using SSH and Winbox.
*   **Monitoring:** Log relevant events and network performance data.
*   **High Availability:** Implement VRRP for redundancy.

**MikroTik Requirements:**

*   RouterOS version 7.11 or higher.
*   A MikroTik device with VLAN-capable interfaces (e.g., CRS series).
*   Separate physical or virtual interfaces for the internet connection.
*   Logical interfaces using VLAN tagging on an interface
*   Capable of L3 Hardware Offloading for optimal performance.

## 2. Step-by-Step MikroTik Implementation (CLI & Winbox)

### 2.1.  Basic Setup

*   **Initial Connect:** Use Winbox or SSH to connect to the router using the initial IP (usually 192.168.88.1 if using the factory default).
*   **Set Router Identity:** Change the hostname using either of the methods below:

    *   **CLI:**

        ```
        /system identity set name=Enterprise-Router
        ```

    *   **Winbox:** *System > Identity*
*   **Secure Access:** Change the default password and disable unnecessary services.

    *   **CLI:**

        ```
        /user set admin password="NewSecurePassword"
        /ip service disable telnet
        ```

    *   **Winbox:** *System > Users* and *IP > Services*

### 2.2 Interface Configuration

*   **Ethernet Interfaces:** Identify your physical interfaces connected to the external network and internal network, in the below example we will assume that ether1 will connect to your internet and ether2 will connect to your switch.
    *  **CLI**
        ```
        /interface ethernet set ether1 name=internet
        /interface ethernet set ether2 name=internal
        ```
        *   **Winbox:** *Interface > Interface List*, rename the interfaces accordingly.
*   **VLAN Interfaces:** Create VLAN interfaces.

    *   **CLI:**
        ```
        /interface vlan add name=vlan10 vlan-id=10 interface=internal
        /interface vlan add name=vlan20 vlan-id=20 interface=internal
        /interface vlan add name=vlan30 vlan-id=30 interface=internal
        ```

    *   **Winbox:** *Interface > VLAN*, create new VLAN interfaces with the `interface` field pointing to your designated interface.
*   **Bridge:** Create a bridge, and add the VLANs to the bridge.

    *   **CLI:**
        ```
        /interface bridge add name=bridge1
        /interface bridge port add bridge=bridge1 interface=vlan10
        /interface bridge port add bridge=bridge1 interface=vlan20
        /interface bridge port add bridge=bridge1 interface=vlan30
        ```
    *   **Winbox:** *Interface > Bridge*, create a new bridge, then under the ports tab add your VLAN interfaces.

### 2.3 IP Addressing (IPv4)

*   **IP Addresses:** Assign IPv4 addresses to VLAN interfaces.

    *   **CLI:**
        ```
        /ip address add address=192.168.10.1/24 interface=vlan10
        /ip address add address=192.168.20.1/24 interface=vlan20
        /ip address add address=192.168.30.1/24 interface=vlan30
        /ip address add address=192.168.0.1/24 interface=internet
        ```
    *   **Winbox:** *IP > Addresses*, add new IP addresses on the corresponding interfaces.

*   **DHCP Server:** Setup DHCP server for user VLAN.

    *   **CLI:**
        ```
        /ip pool add name=dhcp_pool10 ranges=192.168.10.10-192.168.10.254
        /ip dhcp-server add address-pool=dhcp_pool10 interface=vlan10 lease-time=1d name=dhcp_server10
        /ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=8.8.8.8,8.8.4.4
        ```
    *   **Winbox:** *IP > DHCP Server*, add a DHCP server, specify pool and network.

*   **IP Pools:**
  *   IP Pools in MikroTik are used to define a range of IP addresses that can be assigned to various services such as DHCP servers and VPN connections. They provide a structured way to manage IP address allocation.
  *   **CLI:**
    ```
    /ip pool
    print
    add name=pool10 ranges=192.168.10.10-192.168.10.254 # defines the range of addresses in this pool
    remove pool10 # remove the pool if needed
    ```
  *   **Winbox:** *IP > Pool*

*   **IP Settings**

  *   These settings define how the router handles IP packet forwarding, and the way the Router itself acts as an IP host
  *   **CLI:**
    ```
    /ip settings print
    set allow-fast-path=yes # enables or disables fast path
    set max-queued-packets=256 # Sets how many packets can be queued
    ```
  *   **Winbox:** *IP > Settings*

### 2.4 IP Addressing (IPv6)

*   **IPv6 Addresses:** Assign IPv6 addresses (example: /64 for each VLAN).

    *   **CLI:**

       ```
       /ipv6 address add address=2001:db8:1000::1/64 interface=vlan10
       /ipv6 address add address=2001:db8:2000::1/64 interface=vlan20
       /ipv6 address add address=2001:db8:3000::1/64 interface=vlan30
       /ipv6 address add address=2001:db8:0:1::1/64 interface=internet
       ```
    *   **Winbox:** *IPv6 > Addresses*, add addresses with correct interface.
* **IPv6 Pools**
  *   IPv6 pools operate in the same way as IPv4 pools, except that they define ranges of IPv6 addresses, usually /64 prefixes, that the router can allocate to DHCP servers or clients.
  *   **CLI:**
    ```
    /ipv6 pool
    print
    add name=ipv6_pool10 prefix=2001:db8:1000::/64 # defines a /64 prefix for this pool
    remove ipv6_pool10 # removes the specified pool
    ```
  *   **Winbox:** *IPv6 > Pool*

*   **DHCPv6 Server:** Configure DHCPv6 for user VLAN (can use SLAAC).

    *   **CLI:** (Example with SLAAC)
        ```
        /ipv6 nd prefix add interface=vlan10  prefix=2001:db8:1000::/64  advertise=yes managed-address-flag=no other-config-flag=no
        ```
    *   **Winbox:** *IPv6 > ND* Enable IPv6 Neighbor Discovery, and create a prefix for each vlan.

### 2.5 IP Routing

*   **Static Routes (IPv4):** Add default route towards internet.
    * **CLI:**
        ```
        /ip route add dst-address=0.0.0.0/0 gateway=192.168.0.2
        ```
    * **Winbox:** *IP > Routes* Add a new route, and specify the gateway and destination address.

*   **Static Routes (IPv6):** Add default route towards internet.
     * **CLI:**
        ```
        /ipv6 route add dst-address=::/0 gateway=2001:db8:0:1::2
        ```
    * **Winbox:** *IPv6 > Routes* Add a new route, and specify the gateway and destination address.

### 2.6 Firewall and NAT

*   **NAT (IPv4):** Enable NAT for internal users.

    *   **CLI:**
        ```
        /ip firewall nat add chain=srcnat action=masquerade out-interface=internet
        ```
    *   **Winbox:** *IP > Firewall > NAT*, add masquerade rule for the internet interface.
*   **NAT (IPv6):** Enable NAT66 for internal users.

    *   **CLI:**
        ```
        /ipv6 firewall nat add chain=srcnat action=masquerade out-interface=internet
        ```
    *   **Winbox:** *IPv6 > Firewall > NAT*, add masquerade rule for the internet interface.

*   **Firewall Rules:** Set up basic firewall rules to control traffic flow between VLANs.
    * **CLI:**
        ```
         /ip firewall filter
        add action=accept chain=forward comment="Allow established connections" connection-state=established,related
        add action=drop chain=forward comment="Drop all other traffic"
        ```
    * **Winbox:** *IP > Firewall > Filter Rules* Create accept and drop rules.

### 2.7. Security and other functionalities

*   **SSH Access:** Enable SSH access.
    * **CLI:**
        ```
        /ip ssh set allow-none-crypto=no
        /ip ssh set port=2222
        ```
    * **Winbox:** *IP > SSH* change the port and disable insecure ciphers.

* **Winbox**
  * MikroTik's Winbox GUI provides a user friendly way to configure your routers. It connects over TCP/8291 (by default).
  *   **Winbox:** Open the Winbox program and connect using either the IP or MAC address. You must download it from the MikroTik website.
  *   **Note:**  Winbox should be secured by enabling only trusted sources in *IP> Services* and setting a strong password.

* **MAC server**
  *   This service is used by Winbox to detect routers on the network. Disabling the MAC server can increase security, but may also make Winbox discoverability difficult.
  *  **CLI:**
        ```
        /tool mac-server set enabled=no
        /tool mac-server print
        ```
  * **Winbox:** *Tool > MAC Server* Change the settings from there.

*   **ROMON:** This tool allows users to manage a network of MikroTik routers from a central location.
    *  **CLI:**
        ```
        /tool romon set enabled=yes
        /tool romon print
        ```
  * **Winbox:** *Tools > RoMON* enable the service as required.

*   **Certificates:** MikroTik uses certificates for encrypted communication. This feature is essential for securing access through SSH, IPSec, and web interfaces.
    *  **CLI:**
        ```
        /certificate print # list certificates
        /certificate add name=my_certificate common-name=my.domain.com
        /certificate set my_certificate sign=yes
        /certificate export-certificate my_certificate file=certificate.pem password="password"
        ```
  * **Winbox:** *System > Certificates*, create and export certificates as required.

* **PPP AAA**
  *   PPP (Point-to-Point Protocol) is used for dial-in connections.  Authentication, authorization, and accounting (AAA) is vital for PPP connections, especially for users that connect remotely.
  *  **CLI:**
       ```
        /ppp profile print # lists PPP profiles
       /ppp profile add name=default dns-server=192.168.10.1 use-encryption=yes
       ```
  * **Winbox:** *PPP > Profiles* Configure PPP profiles as needed.

* **RADIUS**
  *   RADIUS (Remote Authentication Dial-In User Service) is an AAA protocol that helps manage user access for PPP.  You can authenticate users through RADIUS and use more advanced features.
  *  **CLI:**
    ```
    /radius print # list current radius servers
    /radius add address=10.0.0.1 secret=test service=ppp,login,hotspot
    ```
  * **Winbox:** *RADIUS* Configure RADIUS servers as needed.

*   **User/User Groups:** MikroTik user management system allows for fine-grained access controls.
    *  **CLI:**
    ```
    /user group print
    /user group add name=full-access policy=read,write,test,password
    /user add name=test-user group=full-access password=secure-password
    ```
  * **Winbox:** *System > Users*, configure user accounts and groups as necessary.

## 3. Complete MikroTik CLI Configuration Commands

```
# System Settings
/system identity set name=Enterprise-Router
/user set admin password="NewSecurePassword"
/ip service disable telnet

# Interface Configuration
/interface ethernet set ether1 name=internet
/interface ethernet set ether2 name=internal
/interface vlan add name=vlan10 vlan-id=10 interface=internal
/interface vlan add name=vlan20 vlan-id=20 interface=internal
/interface vlan add name=vlan30 vlan-id=30 interface=internal
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=vlan10
/interface bridge port add bridge=bridge1 interface=vlan20
/interface bridge port add bridge=bridge1 interface=vlan30

# IP Addressing (IPv4)
/ip address add address=192.168.10.1/24 interface=vlan10
/ip address add address=192.168.20.1/24 interface=vlan20
/ip address add address=192.168.30.1/24 interface=vlan30
/ip address add address=192.168.0.1/24 interface=internet
/ip pool add name=dhcp_pool10 ranges=192.168.10.10-192.168.10.254
/ip dhcp-server add address-pool=dhcp_pool10 interface=vlan10 lease-time=1d name=dhcp_server10
/ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=8.8.8.8,8.8.4.4

# IP Addressing (IPv6)
/ipv6 address add address=2001:db8:1000::1/64 interface=vlan10
/ipv6 address add address=2001:db8:2000::1/64 interface=vlan20
/ipv6 address add address=2001:db8:3000::1/64 interface=vlan30
/ipv6 address add address=2001:db8:0:1::1/64 interface=internet
/ipv6 nd prefix add interface=vlan10 prefix=2001:db8:1000::/64 advertise=yes managed-address-flag=no other-config-flag=no

# IP Routing
/ip route add dst-address=0.0.0.0/0 gateway=192.168.0.2
/ipv6 route add dst-address=::/0 gateway=2001:db8:0:1::2

# Firewall and NAT
/ip firewall nat add chain=srcnat action=masquerade out-interface=internet
/ipv6 firewall nat add chain=srcnat action=masquerade out-interface=internet
/ip firewall filter add action=accept chain=forward comment="Allow established connections" connection-state=established,related
/ip firewall filter add action=drop chain=forward comment="Drop all other traffic"

# Security and other configurations
/ip ssh set allow-none-crypto=no
/ip ssh set port=2222
/tool mac-server set enabled=no
/tool romon set enabled=yes
/certificate add name=my_certificate common-name=my.domain.com
/certificate set my_certificate sign=yes
/certificate export-certificate my_certificate file=certificate.pem password="password"
/ppp profile add name=default dns-server=192.168.10.1 use-encryption=yes
/radius add address=10.0.0.1 secret=test service=ppp,login,hotspot
/user group add name=full-access policy=read,write,test,password
/user add name=test-user group=full-access password=secure-password
```

## 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

*   **Incorrect Interface:**  Ensure VLAN interfaces are correctly assigned to the correct physical interface. Use `/interface print` to verify.
*   **Firewall Issues:** Incorrect firewall rules can block traffic. Use `/ip firewall filter print` to check and `/ip firewall raw print` to diagnose connection issues.
*   **DHCP/DHCPv6 Issues:** Check DHCP leases using `/ip dhcp-server lease print` and server status using `/ip dhcp-server print` or `/ipv6 dhcp-server print`
*   **Routing Table Errors:** Use `/ip route print` or `/ipv6 route print` to check routing table.
*   **Memory issues:** Check resources with `/system resource print`. If memory is exhausted, consider reducing log levels, and check for memory leaks.
*   **CPU issues:** Check resource usage using `/system resource monitor` or via Winbox under *System > Resources*. This can help determine if the device is experiencing overloads.
*   **Packet Loss:** Use `ping` and `traceroute` to diagnose issues. Use `/tool torch` to analyse packet captures and find specific issues.
* **Traffic analysis:** Use tools like `/tool sniffer` and `/tool torch` to examine packet flow.

## 5. Verification and Testing

*   **Connectivity:** Use `ping` and `traceroute` on devices within different VLANs and toward the internet.

    *   **CLI Example:**

        ```
        ping 192.168.20.10
        ping 2001:db8:2000::10
        traceroute 8.8.8.8
        traceroute 2001:4860:4860::8888
        ```

*   **DHCP:** Check that devices connected to VLAN 10 receive IP addresses. Use `/ip dhcp-server lease print`.
* **Speed Test:** Use `tool bandwidth-test` to diagnose speed and performance.
    * **CLI:**
        ```
        /tool bandwidth-test address=192.168.10.2 protocol=tcp direction=both duration=10s
        ```

* **Torch:** This will provide real-time visibility of packet information.
    * **CLI:**
        ```
         /tool torch interface=internet
        ```

## 6. Related MikroTik Features, Capabilities, and Limitations

*   **Bridging & Switching:** MikroTik bridges act as layer 2 devices, making the router act as a switch, and allows the implementation of VLANs on physical interfaces.
*   **L3 Hardware Offloading:**  Improves packet forwarding performance by leveraging switch chip hardware acceleration when working with bridges. Requires careful configuration.
*   **MACsec:** MikroTik supports MACsec (Media Access Control Security) for secure communication over Ethernet links. However, it is not generally recommended to use this for general network traffic.
*   **Quality of Service:** MikroTik provides advanced QoS features like HTB and PCQ for traffic shaping and prioritisation. You can do this via `/queue simple add ...`
*   **Switch Chip Features:** MikroTik devices with a switch chip, like CRS series, support features like hardware VLAN filtering and port mirroring.
*   **VLAN:** MikroTik implements VLANs using the 802.1q standard, allowing multiple logical networks over a single physical link.
*   **VXLAN:** MikroTik supports VXLAN (Virtual Extensible LAN) for creating overlay networks.
*   **Connection Tracking:** MikroTik maintains a connection tracking table, enabling stateful firewall rules and NAT functionalities.
*   **Packet Flow:** Understanding packet flow (input, forward, output chains) is critical for firewall configuration. Refer to the MikroTik documentation.
*   **Queues:** Queues allow bandwidth limiting and QoS rules using HTB or PCQ, which is vital to prioritise traffic.
*   **Kid Control:** Basic rules can be used for restricting access to certain resources, generally through a firewall.
*   **UPnP/NAT-PMP:** These rules allow port forwarding through the router to internal clients, usually to bypass a firewall or port forward.
*   **DHCP:** MikroTik supports both IPv4 and IPv6 DHCP servers and clients. `/ip dhcp-server print`, `/ipv6 dhcp-server print`
*   **DNS:** Local DNS caching and forwarding via `/ip dns set allow-remote-requests=yes`. DNS services are provided through `/ip dns`.
*   **SOCKS/Proxy:** Provides basic HTTP/HTTPS proxy capabilities via `/ip proxy`.
*   **Load Balancing:** Achieved using bonding and routing with equal-cost multi-path (ECMP).
*   **Bonding:** Combines multiple Ethernet interfaces for increased bandwidth or redundancy. See `/interface bonding print`.
*   **VRRP:** Provides router redundancy by using virtual IP addresses. Configure this through `/interface vrrp add ...`
*   **MPLS:** MikroTik supports MPLS for building complex carrier-grade networks. Implement through `/mpls print` and related tools.
*   **OSPF/RIP/BGP:** Supports various routing protocols for dynamic routing. Configure using the relevant submenus under `/routing`.
*   **Policy Routing:** Route packets based on source addresses or specific conditions via `/ip route rule add ...`
*   **VRF:** Supports Virtual Routing and Forwarding, allowing for the creation of multiple routing tables. Configure using `/routing vrf add ...`
*   **System Utilities:** MikroTik includes a variety of utilities for monitoring, such as: `graphing`, `health`, `log`, `netwatch`, `packet sniffer`, `profiler`, `resource`, `snmp`, `torch`, `traceroute`, `traffic flow`, `watchdog`.
*   **VPNs:** Supports a wide range of VPN technologies including IPsec, L2TP, OpenVPN, WireGuard.
*   **Wireless:** MikroTik devices have built in WiFi support, and CAPsMAN is available for centralised wireless network management.
*   **Internet of Things:** Supports some IOT interfaces via: `Bluetooth`, `GPIO`, `Lora`, `MQTT`.
*   **Hardware:** MikroTik offers a wide variety of devices with different processors, memory, and interface capabilities.
*   **Diagnostics, monitoring and troubleshooting:** All commands under section 5.0
*  **Extended features:** MikroTik routers provide features like containers for customisable features.

## 7. MikroTik REST API Examples

**Note:** The MikroTik API uses a REST-like interface accessible over HTTPS. It requires authentication and understanding of the RouterOS object model. It's recommended to use the secure API over HTTPS

### 7.1.  Example: Retrieving IP Addresses

*   **API Endpoint:** `/ip/address`
*   **Request Method:** `GET`
*   **Example using `curl`:**

    ```bash
    curl -k -u admin:YourSecurePassword \
    -H "Content-Type: application/json" \
    https://YourRouterIP/rest/ip/address
    ```

*   **Expected Response (JSON):**

    ```json
    [
        {
            ".id": "*0",
            "address": "192.168.10.1/24",
            "interface": "vlan10",
            "actual-interface": "vlan10",
            "dynamic": "false",
            "invalid": "false",
            "disabled": "false"
        },
        {
            ".id": "*1",
            "address": "192.168.20.1/24",
            "interface": "vlan20",
             "actual-interface": "vlan20",
            "dynamic": "false",
            "invalid": "false",
             "disabled": "false"
        }
     ]
    ```

### 7.2 Example: Adding a Firewall Rule

*   **API Endpoint:** `/ip/firewall/filter`
*   **Request Method:** `POST`
*   **Example Request (JSON):**

    ```json
     {
        "chain": "forward",
        "action": "accept",
        "connection-state": "established,related",
        "comment": "Allow established/related connections"
    }
    ```

*   **Example `curl` Command:**

    ```bash
    curl -k -u admin:YourSecurePassword \
      -H "Content-Type: application/json" \
      -X POST -d @request.json \
      https://YourRouterIP/rest/ip/firewall/filter
    ```
    *Where `request.json` contains the above JSON payload.*

*   **Expected Response (JSON):**

    ```json
    {
         ".id": "*1"
     }
    ```

### 7.3. Example: Update a Firewall Rule
*   **API Endpoint:** `/ip/firewall/filter/<id>`
*   **Request Method:** `PUT`
* **Example Request (JSON)**
    ```json
        {
        "comment": "Updated allow established connections"
    }
    ```
*   **Example `curl` Command:**

    ```bash
    curl -k -u admin:YourSecurePassword \
      -H "Content-Type: application/json" \
      -X PUT -d @request.json \
      https://YourRouterIP/rest/ip/firewall/filter/*1
    ```
    *Where `request.json` contains the above JSON payload. Replace *1 with the id of the rule you want to modify*

*   **Expected Response (JSON):**
    ```json
     {
         ".id": "*1",
          "comment": "Updated allow established connections"
     }
    ```

### 7.4 Example: Delete a Firewall Rule

*   **API Endpoint:** `/ip/firewall/filter/<id>`
*   **Request Method:** `DELETE`

* **Example `curl` Command:**

    ```bash
    curl -k -u admin:YourSecurePassword \
      -H "Content-Type: application/json" \
      -X DELETE \
      https://YourRouterIP/rest/ip/firewall/filter/*1
    ```
 *  **Expected Response:**  204 No Content (on success)

**Note:** The REST API requires you to enable it using `/ip service set api-ssl enabled=yes`

## 8. In-Depth Explanations of Core Concepts

*   **Bridging:** A bridge is a layer 2 networking device that forwards packets based on their MAC addresses. MikroTik bridges act as a logical switch, allowing multiple interfaces to function as a single broadcast domain. This allows VLANs to be implemented logically.
*   **Routing:** Routing is the process of forwarding packets between networks based on their destination IP address. MikroTik uses routing tables to determine the best path for packets, supporting both static and dynamic routing protocols.
*   **Firewall:** MikroTik's firewall is a stateful firewall, which means that it tracks the state of connections. It processes packets in chains (input, forward, output) and uses filters and NAT rules to control traffic flow.

## 9. Security Best Practices

*   **Strong Passwords:** Use strong and unique passwords for all user accounts and protect secrets.
*   **Disable Unnecessary Services:** Disable services like Telnet, API, Winbox via default ports.
*   **Firewall Rules:** Implement robust firewall rules. Block any traffic from untrusted sources.
*   **Secure Remote Access:** Use SSH instead of Telnet, and secure Winbox access (disable unnecessary access).
*   **Regular Updates:** Keep RouterOS up-to-date to patch security vulnerabilities.
*   **Certificate Management:** Use valid certificates for secure services like HTTPS, VPN, and API.
*   **Regular Backups:** Backup the router configuration regularly.
*   **Monitor Logs:** Enable logging for security-related events and actively monitor.
*   **Limit Admin Access:** Don't use admin account unless necessary, use separate accounts with appropriate permissions.

## 10.  Detailed Explanations and Configuration Examples

Covered in previous sections.

This document provides an extensive overview of IP addressing and other features within MikroTik RouterOS, designed for an enterprise-level environment. The information is detailed with the best practices to use these features, all from a CLI or Winbox perspective. Feel free to ask if you need clarification on any specific aspect!
