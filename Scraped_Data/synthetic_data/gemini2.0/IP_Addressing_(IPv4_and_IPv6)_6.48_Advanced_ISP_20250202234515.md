Okay, this is an ambitious undertaking, but let's tackle it with the depth and expertise required. This document will provide a comprehensive guide to IP addressing and related networking concepts within MikroTik RouterOS, targeted at an ISP-level deployment. Given the vast scope, we will necessarily summarize some sections, but still with enough information for a technical understanding.

**I. Introduction**

This document provides a detailed guide to IP addressing (IPv4 and IPv6) within MikroTik RouterOS, targeting an ISP-level network. It covers configuration, troubleshooting, security best practices, and advanced features relevant to MikroTik deployments. It's structured to be useful for both experienced MikroTik users and those wanting to learn more. We'll explore both CLI and GUI (Winbox) configurations, and cover topics from core concepts through to advanced features.

**II. IP Addressing (IPv4 and IPv6)**

*   **Core Concepts:**
    *   **IPv4:**  Uses a 32-bit address space, typically written in dotted decimal notation (e.g., 192.168.1.1).
    *   **IPv6:** Uses a 128-bit address space, written in hexadecimal with colons (e.g., 2001:0db8::1).
    *   **Subnetting:** Divides IP address ranges into smaller networks.
    *   **CIDR:** Classless Inter-Domain Routing, allows flexible subnet sizes.

*   **MikroTik Implementation:**

    *   **Interface Addresses:** IP addresses are assigned to network interfaces.
    *   **Address Types:** Static, DHCP Client, DHCP Server, Pool
    *   **Link-Local Addresses:** Automatic IPv6 addresses on an interface.
    *   **Global Addresses:** Typically from a pool or statically configured.
    *   **Scope:** Defines where an address is valid (e.g., link-local, global).

**III. Configuration Scenario: ISP Edge Router**

This configuration assumes a MikroTik router acting as an edge router for a small ISP, providing internet access to subscribers. Key requirements include:

*   **Public IPv4 Addresses:** Assigned to a WAN interface.
*   **Private IPv4 Addresses:** Used for internal management and subscriber access.
*   **IPv6 Support:**  Global IPv6 addresses on the WAN and private IPv6 prefix for LAN.
*   **Subscriber DHCP:**  Dynamic address assignment using DHCP servers.

**IV. Step-by-Step MikroTik Implementation**

**A. IPv4 Configuration (CLI & Winbox)**

1.  **Configure WAN Interface (ether1 - example):**

    *   **CLI:**
        ```
        /ip address
        add address=203.0.113.10/24 interface=ether1 comment="Public IPv4 WAN Address"
        ```
        *   `address`: IP address and subnet mask.
        *   `interface`:  Physical or virtual network interface.
        *   `comment`: Descriptive information.

    *   **Winbox:** Navigate to `IP` -> `Addresses`, click the `+` button, fill in the IP address, interface, and add a comment.
2. **Configure Private Network Address (ether2):**

    * **CLI**

    ```
       /ip address
       add address=192.168.100.1/24 interface=ether2 comment="Private IPv4 for Subscribers"
    ```

    * **Winbox:** Navigate to `IP` -> `Addresses`, click the `+` button, fill in the IP address, interface, and add a comment.

**B. IPv6 Configuration (CLI & Winbox)**

1.  **Configure WAN IPv6 Address (ether1 - example, using DHCPv6 client):**

    *   **CLI:**
        ```
        /ipv6 dhcp-client
        add interface=ether1 request=address,prefix comment="Request IPv6 address and prefix"
        ```
    *   **Winbox:** Navigate to `IPv6` -> `DHCP Client`, click the `+` button, select the interface, check `Request`, check `Address` and `Prefix`, and add a comment.
2. **Configure Private IPv6 Prefix (ether2 - example):**

    *   **CLI:**
        ```
         /ipv6 address
         add address=2001:db8:1::1/64 interface=ether2 comment="Private IPv6 Address"
        ```

    *   **Winbox:** Navigate to `IPv6` -> `Addresses`, click the `+` button, fill in the IPv6 address, interface, and add a comment.

**V. Complete MikroTik CLI Configuration Commands**

```
# IPv4
/ip address
add address=203.0.113.10/24 interface=ether1 comment="Public IPv4 WAN Address"
add address=192.168.100.1/24 interface=ether2 comment="Private IPv4 for Subscribers"

# IPv6
/ipv6 dhcp-client
add interface=ether1 request=address,prefix comment="Request IPv6 address and prefix"
/ipv6 address
add address=2001:db8:1::1/64 interface=ether2 comment="Private IPv6 Address"
```

**VI. Common MikroTik Pitfalls, Troubleshooting & Diagnostics**

*   **Address Conflicts:** Ensure no IP address overlaps. Use `/ip address print` to check current address assignments.
*   **Interface Status:** Use `/interface print` to check the status of interfaces (up/down).
*   **Routing Issues:**  Use `/ip route print` to examine the routing table.
*   **Firewall Issues:** Check `/ip firewall filter print` for blocking rules.
*   **Reachability Issues:** Use `ping`, `traceroute` and `torch`.
*   **Log Errors:** Examine the log using `/system logging print` and `system log print follow-lines=10` to view real-time log output.

**VII. Verification and Testing**

*   **Ping:** Use `ping 8.8.8.8` from the router to test basic connectivity.
*   **Traceroute:** Use `traceroute 8.8.8.8` to check routing paths.
*   **Torch:** Use `/tool torch interface=ether1` to monitor network traffic and find the source of the traffic.
*   **Interface Monitoring:** Use `/interface monitor ether1` to monitor link status and traffic statistics.

**VIII. Related MikroTik Features, Capabilities, and Limitations**

*   **IP Pools:** Dynamically assign IP addresses using IP Pools.
*   **Routing:** Route packets based on destination IP. (See IP Routing section below)
*   **Firewall:** Secure the router by filtering traffic. (See Firewall Section below)
*   **DHCP Server:** Provide IP addresses to clients. (See IP Services Section below)
*   **DHCP Client:**  Automatically get IP address information from an upstream DHCP Server.
*   **NAT:** Translate private addresses to public addresses (and vice versa). (See Firewall Section Below)
*   **Limitations:** Router performance depends on the specific MikroTik model and hardware.

**IX. MikroTik REST API Examples**

*  **Endpoint:** `/ip/address`
*  **Method:** `GET`
*  **Example:** (Requires MikroTik API enabled and authentication)
   *   **Request (Using cURL):**

        ```bash
        curl -k -u "api_user:api_password" https://192.168.100.1/rest/ip/address
        ```
    *  **Response (JSON - Example):**

        ```json
        [
          {
              ".id": "*1",
              "address": "203.0.113.10/24",
              "interface": "ether1",
              "comment": "Public IPv4 WAN Address",
              "dynamic": "false",
              "disabled": "false"
          },
          {
              ".id": "*2",
              "address": "192.168.100.1/24",
              "interface": "ether2",
              "comment": "Private IPv4 for Subscribers",
              "dynamic": "false",
              "disabled": "false"
           }
        ]
        ```

* **Example: Adding a new IP address (using POST)**
    *   **Endpoint:** `/ip/address`
    *   **Method:** `POST`
    *   **Request (Using cURL):**

        ```bash
        curl -k -u "api_user:api_password" -H "Content-Type: application/json" -d '{"address": "192.168.100.2/24", "interface": "ether2", "comment": "Test API Address"}' https://192.168.100.1/rest/ip/address
        ```
     * **Response (JSON - Example):**

        ```json
        {
          "message": "added",
          "id": "*3"
         }
        ```
* **Example: Deleting an IP Address (using DELETE)**

    * **Endpoint:** `/ip/address/ *3` (Note the ID comes from the previous example)
    * **Method:** `DELETE`
    * **Request (Using cURL):**

        ```bash
        curl -k -u "api_user:api_password" -X DELETE https://192.168.100.1/rest/ip/address/*3
        ```
    * **Response (JSON - Example):**

        ```json
           {
              "message": "removed",
              "id": "*3"
          }
        ```

**Note:**
* The API will need to be enabled with user configuration for access.
* Replace the IP, user and password with your configuration.
* The `*` character is how RouterOS identifies an entry, you'll need to get the correct ID.

**X. Core Concepts: In-Depth**

*   **Bridging:** Connects multiple interfaces at layer 2 to make them part of the same LAN segment.  MikroTik uses `/interface bridge`.
*   **Routing:** Directs traffic between different networks at layer 3. MikroTik uses `/ip route`. (See IP Routing Section below)
*   **Firewall:** Controls network traffic based on rules to secure the network. MikroTik uses `/ip firewall`. (See Firewall and QoS section below)
*  **IP Pools**: Dynamic ranges of IP Addresses to allocate via DHCP. MikroTik uses `/ip pool`. (See IP Pools Section below)

**XI. Security Best Practices for MikroTik**

*   **Strong Passwords:** Use strong, unique passwords for all accounts.
*   **Disable Unnecessary Services:** Disable services you don't use (e.g., `api`, `www-ssl`). Use `/ip service print` to show running services and `/ip service disable api` to disable the API.
*   **Firewall Rules:** Implement strict firewall rules, specifically filtering input and forward chains.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version.
*   **Remote Access:** Limit remote access to specific IP addresses.
*   **Change Default Ports:**  Change default ports for services like Winbox. Use `/ip service set winbox port=8291` to change the winbox port from the default 8291.
*   **User Groups:** Use different groups for different access levels. Use `/user group print` and `/user group add` to view and add groups.
*   **API Security:** Disable the API if not needed, or at a minimum ensure proper user security.

**XII. Detailed Explanations & Configuration Examples**

**A. IP Pools**

*   **Concept:**  Ranges of IP addresses used for dynamic allocation (e.g., DHCP).
*   **Configuration (CLI):**

    ```
    /ip pool
    add name=dhcp-pool ranges=192.168.100.2-192.168.100.254
    ```

    *   `name`: Pool name.
    *   `ranges`:  IP address range.

* **Configuration (Winbox):** Navigate to `IP` -> `Pool`, click the `+` button, fill in the pool name and the range of addresses.

**B. IP Routing**

*   **Concept:** Directs network traffic based on destination IP addresses.
*   **Configuration (CLI):**

    ```
    /ip route
    add dst-address=0.0.0.0/0 gateway=203.0.113.1  comment="Default Route to Internet"
    ```
    *   `dst-address`: Destination IP address or network.
    *   `gateway`: Next-hop router.

*   **Winbox:**  Navigate to `IP` -> `Routes`, click the `+` button, fill in the `Dst. Address`, and `Gateway`.

**C. IP Settings**

*   **Concept:** Basic router settings that influence IP and general network operation.
*   **Configuration (CLI):**

    ```
    /ip settings
    set tcp-syncookies=yes  forwarding=yes  allow-fast-path=yes
    ```

     *   `tcp-syncookies`: Enables syncookie protection against SYN flood attacks.
     *   `forwarding`: Enables IP forwarding between interfaces.
     *   `allow-fast-path`: Enables fast path processing.

*   **Winbox:** Navigate to `IP` -> `Settings`, make desired adjustments.

**D. MAC server**

* **Concept:** MikroTik RouterOS has a MAC-based server that allows to manage ARP and Neighbor Discovery for some interfaces.
* **Configuration (CLI)**
```
/interface ethernet
set ether1 mac-address=00:11:22:33:44:55
/interface print
```
   *   `mac-address`: Sets the MAC address of the interface.

* **Winbox:** Navigate to `Interfaces`, click on the interface you want to configure, go to the `General` tab and modify the `MAC address` property.

**E. RoMON**

* **Concept:** MikroTik's proprietary network discovery protocol that allows to build a logical topology for management purpose.
* **Configuration (CLI):**
```
/tool romon
set enabled=yes
add interface=ether1
```
 * `enabled`: Sets whether RoMON is enabled or disabled.
 * `interface`: Configures the RoMON interface.

* **Winbox:** Navigate to `Tools` -> `RoMON`.

**F. WinBox**

* **Concept:** Windows-based GUI configuration tool for MikroTik.
* **Functionality:** Configures almost all router features with a graphical interface.
* **Best Practice:** Secure access through the proper firewall rules and strong authentication.

**G. Certificates**

* **Concept:** Used for secure HTTPS, VPNs, and other secure services.
* **Configuration (CLI):**
   ```
   /certificate
   add name=my-certificate common-name=my-router key-usage=digital-signature,key-encipherment,data-encipherment generate-key
   ```
    *   `name`: Certificate name.
    *   `common-name`: Certificate identifier.
    *   `key-usage`: Specifies how the certificate can be used.
    *   `generate-key`: Generates a self-signed certificate.

*   **Winbox:** Navigate to `System` -> `Certificates`.

**H. PPP AAA (Authentication, Authorization, Accounting)**

* **Concept:** Enables control of user authentication and access for PPP based connections.
* **Configuration (CLI):**
```
/ppp profile add name=pppoe-profile use-encryption=yes
/ppp secret add name=john password=password profile=pppoe-profile service=pppoe
```
* `name`: PPP profile or secret name.
* `use-encryption`: sets if the connection is encrypted.
* `password`:  Password of the secret account.
* `profile`: The used profile.
* `service`: Specifies the used service.

* **Winbox:** Navigate to `PPP` -> `Profiles`, `PPP` -> `Secrets`

**I. RADIUS**

* **Concept:** Centralized Authentication, Authorization, and Accounting server.
* **Configuration (CLI):**
```
/radius
add address=192.168.10.1 secret=secret123 service=ppp,login
```
 * `address`: IP Address of the RADIUS server.
 * `secret`: shared secret.
 * `service`: the service that will use the radius.

* **Winbox:** Navigate to `Radius`.

**J. User / User groups**

* **Concept:** Different user accounts with different privileges.
* **Configuration (CLI):**
```
/user add name=testuser group=read password=password
/user group add name=limited policy=read,test
```

* `name`: Username or user group name.
* `group`: assign the user to a group.
* `password`: the user password.
* `policy`: the policy assigned to the group

* **Winbox:** Navigate to `System` -> `Users` or `System` -> `User Groups`.

**K. Bridging and Switching**

*   **Concept:**  Bridges connect interfaces to create a single Layer 2 broadcast domain. Switching happens within the same broadcast domain.
*   **Configuration (CLI):**

    ```
    /interface bridge
    add name=bridge1 protocol-mode=rstp
    /interface bridge port
    add bridge=bridge1 interface=ether2
    add bridge=bridge1 interface=ether3
    ```
    *   `name`: Bridge name.
    *   `protocol-mode`: Spanning tree protocol.
    *   `interface`: Interface to add to bridge.

* **Winbox:** Navigate to `Bridge`.

**L. MACVLAN**

*   **Concept:**  Virtual interfaces with unique MAC addresses, allowing multiple devices to share a physical interface.
*   **Configuration (CLI):**
    ```
      /interface macvlan
      add interface=ether2 mac-address=00:00:00:00:00:01  name=macvlan1
    ```
   * `interface`: physical interface.
   * `mac-address`: mac address of the new interface.
   * `name`:  new interface name

*  **Winbox:** Navigate to `Interfaces` -> add new interface type `MACVLAN`

**M. L3 Hardware Offloading**

* **Concept:** Offloads L3 processing to hardware to improve forwarding performance.
* **Configuration (CLI):**
```
  /interface ethernet
  set ether1 l3-hw-offloading=yes
```
* `l3-hw-offloading`: Enables or disables the hardware offloading.

* **Winbox:** Navigate to `Interfaces`, edit the ethernet interface in question and enable the hardware offloading option.

**N. MACsec**

* **Concept:** Provides L2 security by adding encryption and integrity validation.
* **Configuration (CLI):**
```
/interface macsec add name=macsec1 interface=ether2 primary-key=0123456789ABCDEF
```
* `name`: name of the new macsec interface.
* `interface`: The interface you want to create a macsec on.
* `primary-key`: The primary key for the encryption

* **Winbox:** Navigate to `Interfaces`, add a new interface of type `MACsec`

**O. Quality of Service (QoS)**

* **Concept:** Controls bandwidth usage based on rules.
* **Configuration (CLI):**

    ```
    /queue simple
    add max-limit=10M/10M name=queue1 target=192.168.100.0/24
    ```
    *   `max-limit`:  Maximum bandwidth.
    *   `name`: Queue name.
    *   `target`: Source or destination network.

*  **Winbox:** Navigate to `Queues`.

**P. Switch Chip Features**

*   **Concept:** Many MikroTik devices use dedicated switch chips.
*   **Functionality:** Layer 2 hardware offloading, VLAN tagging/untagging.
*   **Configuration:**  Managed via `/interface ethernet switch` (specific to each device model).

**Q. VLAN**

*   **Concept:** Virtual LANs logically segment a network.
*   **Configuration (CLI):**

    ```
    /interface vlan
    add interface=ether2 name=vlan10 vlan-id=10
    ```
    *   `interface`: Parent interface.
    *   `name`: VLAN interface name.
    *   `vlan-id`: VLAN identifier.

* **Winbox:** Navigate to `Interfaces`, add a new interface of type `VLAN`

**R. VXLAN**

*   **Concept:**  Virtual extensible LANs, allowing Layer 2 extensions across Layer 3 networks.
*   **Configuration (CLI):**
   ```
    /interface vxlan
    add name=vxlan1 vni=1000 interface=ether1 remote-address=203.0.113.15
    ```
   * `name`: VXLAN Interface Name
   * `vni`: VXLAN Network Identifier.
   * `interface`:  Physical interface of the tunnel.
   * `remote-address`: IP Address of the remote end.

*   **Winbox:** Navigate to `Interfaces`, add a new interface of type `VXLAN`.

**S. Firewall and Quality of Service (Detailed)**

   * **Connection Tracking:** MikroTik uses connection tracking to maintain information about active network connections.  Allows for stateful firewall rules.
   * **Firewall:**
      *   **Concepts:** Filter network traffic, perform NAT, and control access.  Consists of filter rules, NAT rules, and mangle rules.
      *   **Configuration (CLI):**
          ```
          /ip firewall filter
          add chain=forward action=drop src-address=192.168.100.0/24 dst-address=10.0.0.0/8
          ```
          *   `chain`: `input`, `output`, `forward`.
          *   `action`: `accept`, `drop`, `reject`.
          *   `src-address`, `dst-address`: Source or destination IP address.

      *  **Winbox:** Navigate to `Firewall`.

    *   **Packet Flow in RouterOS:** Packets enter at the `input` chain, are routed based on destination, then pass through `forward` chain, and exit at `output` chain.
    *   **Queues:** Queues can be used to limit bandwidth, prioritize certain traffic types, and create advanced traffic shaping.
        *  **Configuration (CLI):**
            ```
            /queue tree
            add name="queue_up" parent="global-out" queue=default limit-at=5M max-limit=10M
            /queue tree add name=queue_down parent=global-in queue=default limit-at=5M max-limit=10M
            /queue tree add name=queue-http parent=queue_down queue=pcq-download packet-mark=http
            ```
              *   `name`: Queue name.
              *   `parent`:  Parent queue.
              *   `queue`: Queues type.
              *   `packet-mark`: Traffic marking based on other rules.

        * **Winbox:** Navigate to `Queues`.
    *   **Firewall and QoS Case Studies:**  Complex setups where firewall marking is used to prioritize certain traffic types.
    *   **Kid Control:** Can be used to implement blocking by IP or time.
    *  **UPnP/NAT-PMP:** Allows to dynamically create NAT entries (usually for gaming). Not recommended for security purposes.

**T. IP Services**

    *   **DHCP Server:**  Automatically assigns IP addresses to clients.
         *  **Configuration (CLI):**
            ```
            /ip dhcp-server
            add address-pool=dhcp-pool interface=ether2 lease-time=10m name=dhcp1
            /ip dhcp-server network
            add address=192.168.100.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.100.1
            ```
                *  `address-pool`: The IP pool used for the leases.
                *  `interface`: Interface the DHCP server will be active.
                *  `lease-time`: How long is the DHCP lease.
                *  `dns-server`: The dns server that clients will use.
                *  `gateway`: The gateway for the clients.

        * **Winbox:** Navigate to `IP` -> `DHCP Server`.
    *   **DNS:** Provides name resolution.
        * **Configuration (CLI):**
            ```
             /ip dns set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
            ```
                 *  `allow-remote-requests`: Allows queries from external networks.
                 *  `servers`: List of DNS servers to use.

        * **Winbox:** Navigate to `IP` -> `DNS`
    *   **SOCKS:** Proxy server for TCP connections
         *   **Configuration (CLI):**
            ```
            /ip socks set enabled=yes max-connections=10
           ```
                  *  `enabled`: Enables or disables the service
                  * `max-connections`: Max concurrent connections.
         * **Winbox:** Navigate to `IP` -> `Socks`
    *   **Proxy:** HTTP proxy server for web traffic.
        *   **Configuration (CLI):**
            ```
            /ip proxy
            set enabled=yes port=3128
           ```
              *  `enabled`: Enables or disables the service.
              * `port`: The listening port.
        * **Winbox:** Navigate to `IP` -> `Web Proxy`.

**U. High Availability Solutions**

    *   **Load Balancing:**  Distributes traffic across multiple links.
        *   **Configuration (CLI):**  Uses policy based routing to direct different kinds of traffic based on weight or other properties.
    *   **Bonding:** Combines multiple links into one.
        *   **Configuration (CLI):**
        ```
        /interface bonding
        add mode=balance-alb name=bond1 slaves=ether1,ether2
        ```
            *   `mode`: Bonding mode.
            *   `slaves`: List of the interfaces used in the bonding interface.

    *   **Bonding Examples:**  Different bonding modes for different use cases (active-backup, load balancing).
    *   **HA Case Studies:** Different implementation scenarios depending on the requirement.
    *   **Multi-chassis Link Aggregation Group (MLAG):** Requires special compatible switches.
    *   **VRRP:** Virtual Router Redundancy Protocol - provides router redundancy using an IP address.
        *  **Configuration (CLI):**
            ```
            /interface vrrp add interface=ether2 name=vrrp1 vrid=1 priority=100 virtual-address=192.168.100.254/24
           ```
                * `interface`: The interface used for the VRRP instance.
                * `vrid`: The VRRP Id.
                * `priority`: The election priority.
                * `virtual-address`: The shared virtual address.

    *   **VRRP Configuration Examples:**  Different scenarios depending on network topology.

**V. Mobile Networking**

    *   **GPS:** Access GPS data (e.g. position, time).
    *   **LTE:** Configure cellular connections.
        *  **Configuration (CLI):**
            ```
            /interface lte apn add apn=internet interface=lte1 use-peer-dns=yes
            ```
                * `apn`: the provider's APN
                * `interface`: LTE interface name.
                * `use-peer-dns`:  Use the DNS from the provider.
    *   **PPP:**  Connect using PPP over cellular or other connections.
    *   **SMS:** Send and receive SMS messages.
        *   **Configuration (CLI):**
            ```
            /tool sms send phone-number=1234567890 message="Hello World!"
            ```
        *  **Winbox:** Navigate to `Tools` -> `SMS`.
    *  **Dual SIM Application:**  Allows the use of two SIM cards in the same device.

**W. Multi Protocol Label Switching - MPLS**

    *   **MPLS Overview:**   Provides a layer 2.5 switching method
    *   **MPLS MTU:** MTU value for MPLS packets.
    *   **Forwarding and Label Bindings:** How MPLS labels are used to forward packets.
    *   **EXP bit and MPLS Queuing:**  EXP is used for QoS.
    *   **LDP:** Label Distribution Protocol for dynamic label distribution.
        *   **Configuration (CLI):**
           ```
           /mpls ldp
           set enabled=yes transport-address=192.168.100.1
            /mpls ldp interface add interface=ether2
            ```
            * `enabled`: Enables or disables LDP on the router.
            * `transport-address`: The transport address for LDP.
    *   **VPLS:** Virtual Private LAN Service for L2 VPN over MPLS.
        *   **Configuration (CLI):**
        ```
         /interface vpls add vpls-id=1234 interface=ether2 remote-peer=203.0.113.10
       ```
                *   `vpls-id`: The VPLS ID.
                *   `interface`: The interface that will connect to the VPLS.
                * `remote-peer`: The IP address of the peer VPLS device.
    *   **Traffic Engineering:** How MPLS can be used for traffic control.
    *   **MPLS Reference:** Specific commands and implementations.

**X. Network Management**

    *   **ARP:** Address Resolution Protocol, used to resolve IP addresses to MAC addresses.
    *   **Cloud:** MikroTik cloud functionality.
    *   **DHCP:** See IP Services section.
    *   **DNS:** See IP Services section.
    *   **SOCKS:** See IP Services section.
    *   **Proxy:** See IP Services section.
    *   **Openflow:**  Software defined networking.

**Y. Routing**

    *   **Routing Protocol Overview:** Different types of routing protocols (static, dynamic).
    *   **Moving from ROSv6 to v7 with examples:** Routing protocol implementation changes.
    *   **Routing Protocol Multi-core Support:** How multi-core processors are used to improve routing performance.
    *   **Policy Routing:** Direct traffic based on criteria other than destination IP address.
    *   **Virtual Routing and Forwarding - VRF:**  Allows multiple routing instances.
        *   **Configuration (CLI):**
           ```
           /routing vrf add name=customer1
           /ip route add dst-address=10.0.0.0/8 vrf=customer1 gateway=192.168.200.1
           ```
                  *   `name`: VRF instance name.
                  *   `dst-address`: Destination network.
                  *   `vrf`: Which VRF to use.
                  *   `gateway`: Next-hop router.
    *   **OSPF:** Open Shortest Path First, a link-state routing protocol.
         *   **Configuration (CLI):**
           ```
           /routing ospf instance set default-instance router-id=1.1.1.1
           /routing ospf area add area-id=0.0.0.0
           /routing ospf interface add interface=ether2 area=0.0.0.0
           ```

                *   `router-id`:  Router identifier.
                *   `area-id`: OSPF area ID.
                *  `interface`: Interfaces to enable on OSPF.
    *   **RIP:** Routing Information Protocol, a distance-vector routing protocol.
         *   **Configuration (CLI):**
         ```
          /routing rip instance set default-instance redistribute-connected=yes
          /routing rip interface add interface=ether2
          ```
                  *  `redistribute-connected`: Announces connected routes via RIP.
                  * `interface`: The interface that will run RIP.

    *   **BGP:** Border Gateway Protocol, an exterior gateway protocol.
         *   **Configuration (CLI):**
            ```
            /routing bgp instance set default-instance router-id=1.1.1.1 as=65000
            /routing bgp peer add remote-address=10.0.0.2 remote-as=65001 update-source=ether2
           ```
            *   `router-id`: BGP Router identifier.
            *   `as`: Autonomous system number.
            *   `remote-address`: IP Address of the BGP peer.
            *   `remote-as`: Remote BGP system number.
            * `update-source`: Local IP Address used for the BGP session.

    *   **RPKI:** Route Public Key Infrastructure, used for secure BGP routing.
    *   **Route Selection and Filters:** Configure how routes are selected.
    *   **Multicast:** Send traffic to multiple receivers.
    *   **Routing Debugging Tools:** Tools like `/routing debug`
    *   **Routing Reference:** Specific commands and implementations.
    *   **BFD:** Bidirectional Forwarding Detection, used to quickly detect failures.
       *   **Configuration (CLI):**
           ```
           /routing bfd interface add interface=ether2 min-rx-interval=500 min-tx-interval=500
           ```
                  *  `interface`: interface to enable BFD on.
                  *  `min-rx-interval`: Minimum receive interval.
                  * `min-tx-interval`: Minimum transmit interval.
    *   **IS-IS:** Intermediate System to Intermediate System routing protocol.

**Z. System Information and Utilities**

    *   **Clock:**  Set system time.
        * **Configuration (CLI):**
            ```
            /system clock set time="10:00:00" date=2024-02-10
           ```
                 *   `time`: Set the time of day.
                 *   `date`: Set the date.
     *  **Winbox:** Navigate to `System` -> `Clock`
    *   **Device-mode:** Determine the working mode for specific routerboard products.
    *   **E-mail:** Configure email sending and email server for system notifications.
    *   **Fetch:** Download files via HTTP/HTTPS
    *   **Files:** View and manage files on the router.
        * **Configuration (CLI):**
            ```
            /file print
           ```
                *   shows all the files in the device.
    *   **Identity:** Set a router name.
         *   **Configuration (CLI):**
            ```
            /system identity set name=myrouter
           ```
                 *   `name`: Router hostname.
     *  **Winbox:** Navigate to `System` -> `Identity`.
    *   **Interface Lists:** Group multiple interfaces together for better handling.
    *   **Neighbor discovery:** Discover neighboring MikroTik devices on the same network
    *   **Note:** Add comments to the configuration.
    *   **NTP:** Network Time Protocol, used for time synchronization.
         *  **Configuration (CLI):**
             ```
             /system ntp client set enabled=yes primary-ntp=1.1.1.1
            ```
                    *  `enabled`: enables the NTP client.
                    *  `primary-ntp`: The address of the time server.