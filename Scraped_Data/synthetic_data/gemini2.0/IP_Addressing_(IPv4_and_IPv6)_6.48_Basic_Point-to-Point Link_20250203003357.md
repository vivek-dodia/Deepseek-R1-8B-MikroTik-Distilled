Okay, let's dive deep into configuring IP addressing and related features on a MikroTik router, specifically targeting RouterOS v6.48, with a focus on your provided parameters and a comprehensive breakdown of related topics. This will be a long but thorough guide.

## MikroTik RouterOS Configuration: Point-to-Point Link with 190.39.90.0/24

**1. Comprehensive Configuration Scenario & MikroTik Requirements:**

We aim to configure a basic point-to-point link on a MikroTik router using the specified subnet `190.39.90.0/24` on interface `ether-49`. This setup is typical for connecting two routers or devices directly over an Ethernet cable. We'll configure IP addressing, explore related features like routing, DHCP server, and delve into troubleshooting aspects. This example assumes a *Basic* configuration level.

*   **MikroTik Requirement**: A RouterBOARD device running RouterOS v6.48 or higher (7.x compatible) with a physical Ethernet interface capable of supporting our configuration.
*   **Subnet**: `190.39.90.0/24`
*   **Interface Name**: `ether-49`

**2. Step-by-Step MikroTik Implementation (CLI & Winbox):**

**CLI Implementation:**

1.  **Connect to the MikroTik Router:** Use SSH or the MikroTik console.
2.  **Set Interface IP Address:**

    ```mikrotik
    /ip address
    add address=190.39.90.1/24 interface=ether-49
    ```

    *   This command assigns IP address `190.39.90.1` with a `/24` subnet mask to the `ether-49` interface. If this device is intended to be the server device for the p2p link, assign that IP. If this device is the receiver end of the p2p link, assign `190.39.90.2`. The important part is that they are on the same subnet.
3.  **Optional - Enable IPv6:** Add a link local address (fe80::/10).

    ```mikrotik
    /ipv6 address
    add address=fe80::1/64 interface=ether-49
    ```

4.  **Disable DHCP Client (If active):** By default, a MikroTik interface might be set to acquire an IP through DHCP client. If required, disable it.
    ```mikrotik
    /ip dhcp-client disable [find interface=ether-49]
    ```

**Winbox Implementation:**

1.  **Connect to the Router using Winbox.**
2.  **Navigate to IP > Addresses:**
3.  Click the **"+"** button.
4.  Enter the Address: `190.39.90.1/24`
5.  Select `ether-49` in the **Interface** drop-down.
6.  Click **Apply** and then **OK**.
7.  **Navigate to IP > DHCP Client** and verify it is not configured for this interface.

**3. Complete MikroTik CLI Configuration Commands:**

```mikrotik
# Set IP Address for ether-49
/ip address add address=190.39.90.1/24 interface=ether-49

# Optional: Set IPv6 Link-Local Address for ether-49
/ipv6 address add address=fe80::1/64 interface=ether-49

# Optional - disable DHCP client for ether-49
/ip dhcp-client disable [find interface=ether-49]
```

**4. Common MikroTik-Specific Pitfalls, Troubleshooting & Diagnostics:**

*   **Error: `already have such address`:** If you get this error, an address already exists on that interface, or that address is configured on another interface. Use `/ip address print` to view the configuration. Use the command `/ip address remove [number of address]` to remove the address.
*   **Error: `interface not found`**: Make sure your interface name is correct. Check with `/interface print`.
*   **Problem: No connectivity:**
    *   Check IP address settings on both devices to be sure they are in the same subnet.
    *   Use `ping 190.39.90.x` (where x is the address of the device you wish to reach) to test reachability.
    *   Verify the cable is working by attempting to connect to the internet from a known working device connected to this cable.
    *   Use `torch interface=ether-49` to monitor packets on the interface, which can help diagnose layer 2 problems.
*   **Troubleshooting command:** `ping 190.39.90.2 interface=ether-49 count=5`. This command will send five ping packets to `190.39.90.2`, using the specified interface.
*   **Troubleshooting command:** `/ip address print` Displays all configured IP Addresses.
*   **Troubleshooting command:** `/interface print` Displays all interfaces with their respective statuses.

**5. Verification and Testing Steps:**

*   **Ping Test:** `ping 190.39.90.x` from your MikroTik device to verify basic connectivity with the other end of the point-to-point link. The other end device should have a static IP on the same subnet (e.g., `190.39.90.2`).

*   **Traceroute:** `traceroute 190.39.90.x` to analyze the path and hops. This is mainly used for troubleshooting connections that have multiple devices in the route.
*   **Torch:** `torch interface=ether-49` to examine real-time network traffic. Filter for specific protocols or IP addresses.
*   **Interface Status:** `/interface print` will show the status of the interface: "running", "disabled", etc.

**6. Related MikroTik-Specific Features, Capabilities & Limitations:**

*   **IP Pools**: While we've used a static IP, IP Pools are used for dynamic IP assignment (DHCP). For our p2p example, we won't need a pool unless one of our devices is a DHCP server.

    ```mikrotik
    /ip pool add name=local-pool ranges=190.39.90.100-190.39.90.200
    ```
*   **IP Routing**: RouterOS automatically creates a connected route when an IP address is set on an interface. The IP address defines the network and how the router treats that subnet.
*  **IP Settings**: Used to enable/disable ICMP redirects and other settings. Generally left at default for simple links.
*   **MAC Server**: MAC Server is used to connect to the Router's web interface by MAC Address.

* **Bridging**: MikroTik allows you to bridge two interfaces in layer two. This can be used to allow for Layer 2 access over multiple interfaces, if needed.
* **MACVLAN:** MACVLAN is used to allow creation of multiple MAC address instances, all connected to the same interface. This is useful for virtual machines on the same VLAN.
*   **VLANs**: Multiple virtual LANs can exist on `ether-49` using VLAN tagging (802.1Q). This can be used for isolating traffic.
   ```mikrotik
   /interface vlan add name=vlan100 vlan-id=100 interface=ether-49
   /ip address add address=192.168.100.1/24 interface=vlan100
   ```
* **VXLAN**: Layer 2 tunnel over IP. Useful for connecting to L2 networks over the internet.
*   **L3 Hardware Offloading**: Certain RouterBOARDs can offload IP routing to specialized hardware for better performance.
* **MACsec**: Allows encrypted communication between two interfaces connected directly via ethernet. This can be configured in the interface setting.
*   **Quality of Service (QoS)**: Use `queue tree` and `firewall mangle` rules to prioritize traffic based on IP, port, etc. We won't cover QoS for this particular point-to-point link, but it's powerful for more complex networks. We'll cover the features in greater detail below.

*   **DHCP Server**:
    ```mikrotik
    /ip dhcp-server
    add address-pool=local-pool disabled=no interface=ether-49 lease-time=10m name=local-dhcp-server
    /ip dhcp-server network
    add address=190.39.90.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=190.39.90.1
    ```
    These commands configure a DHCP server to give IP addresses from our `local-pool` to clients connected to `ether-49`. The server hands out the DNS and gateway as well.
*   **DNS**: Use `/ip dns` to configure the router's DNS server settings. The default is to use a forwarder such as google or cloudflare.
*   **SOCKS**: The router can be configured as a SOCKS Proxy.
*   **Proxy**: The router can be configured as a Web Proxy.

* **High Availability**: MikroTik routers support HA solutions such as VRRP and Bonding.
    *   **VRRP**: VRRP is a protocol to assign a Virtual IP to multiple routers. A virtual IP will be assigned to a primary router, and will transition to a backup router if the primary router fails.
    *   **Bonding**: Bonding allows multiple interfaces to work as a single interface with aggregated bandwidth. This can be used to combine multiple interfaces in order to increase bandwidth.
* **Mobile Networking**: MikroTik routers support Mobile data capabilities with support for LTE cards and SMS via connected devices. This can be used as a primary or secondary WAN.

*   **MPLS (Multi-Protocol Label Switching)**:  A protocol to use labels to direct traffic.
    * **LDP (Label Distribution Protocol)**: Used to manage labels in MPLS networks.
    * **VPLS (Virtual Private LAN Service)**: Provides a virtual Ethernet network between different locations. This can be used for L2 connectivity over the internet.

*   **Network Management**
    *   **ARP**: The router maintains a table of IP address to MAC address mapping.
    *   **Cloud**: MikroTik offers a cloud service, allowing easy access to devices behind a NAT.
    *   **Openflow**: The router can be configured as a Openflow switch.

*   **Routing**
    *   **OSPF (Open Shortest Path First)**: Interior Gateway Protocol. Used for distributing routing information in complex networks.
    *   **RIP (Routing Information Protocol)**: An older, and simpler routing protocol. Not recommended over OSPF, which is better for large networks.
    *   **BGP (Border Gateway Protocol)**: Used to route traffic between networks (Typically with multiple ISPs). A powerful and complex protocol.
    *   **Policy Based Routing**: A powerful way to route traffic based on various conditions.
    * **VRF (Virtual Routing and Forwarding)**: Creates multiple routing tables, and separates traffic by route.
    *   **Route Selection and Filters**: Allows for fine control of routing, to ensure traffic routes the way the admin wants.
*   **System Information and Utilities**
    *   **Clock**: Used to set system time.
    *   **Scheduler**: Used to execute commands at specified intervals.
    *   **Services**: Allows the router to support telnet, SSH, api, and other services.
    * **NTP**: Allows the router to set system time by communicating with an NTP Server.
    * **Precision Time Protocol (PTP)**: Can be configured on the Router to synchronize the time with a primary device.
*   **VPN**:
    *   **IPsec**: IPsec is an encryption protocol. Can be used to create site to site and remote access VPNs.
    *   **L2TP**: Creates L2 tunnel over IP. Useful for remote access VPNs.
    *   **OpenVPN**: A mature open source VPN protocol. Can be used for remote access VPNs.
    *  **PPPoE**: Used for connection with ISPs that use the PPPoE protocol for connection.
    *   **WireGuard**: Modern VPN protocol, generally with higher performance than the alternatives.
    * **SSTP**: Secure Socket Tunneling Protocol, useful in situations where standard VPN protocols are blocked or filtered.

*   **Wired Connections:**
    *   **Ethernet**: The router supports many standards, including 10/100/1000 speeds, and 10/25/40/100GB fiber.
*   **Wireless**
    *   **WiFi**: The Router supports common 2.4/5ghz WiFi. The Router can also support 60 ghz and 6 ghz WiFi as well.
    *  **CAPsMAN**: Central AP management, designed to manage many access points in a wireless environment.
    *  **HWMPplus mesh**: Allows creating a meshed WiFi network.
* **Internet of Things**
    *   **Bluetooth**: Available on certain MikroTik devices.
    *   **GPIO**: Used to send and receive messages to digital input and output pins.
    *   **Lora**: Allows creation of a long range LoRa network.
    *   **MQTT**:  A popular protocol for IoT devices.

* **Hardware**
    * **Disks**: MikroTik supports external USB storage.
    * **Grounding**: MikroTik devices should be properly grounded.
    * **Peripherals**: The router supports serial, USB, and other peripherals.
    * **Ports**: MikroTik device have specific speed and functionality for each port.
    *   **RouterBOARD**: Refers to the line of hardware products from MikroTik.

* **Diagnostics**
    *   **Bandwidth Test**: Allows testing of throughput between two devices.
    *   **Detect Internet**: Tests connection to the internet.
    *   **Dynamic DNS**: Allows the router to be accessed via a hostname even if the IP address is dynamic.
    *   **Interface stats and monitor-traffic**: Allows monitoring of the performance and bandwidth usage of an interface.
    *   **IP Scan**: Allows network discovery for all devices on a subnet.
    *   **Log**: Used to view logged messages, for the purposes of debugging.
    *   **Netwatch**: Allows monitoring of hosts, and triggers an action based on host status.
    *   **Packet Sniffer**: Used to capture network packets.
    *   **Ping**: Test if a host is reachable.
    *   **Profiler**: Helps identify CPU utilization, useful when troubleshooting performance issues.
    *   **Resource**: Shows general system resources such as cpu load, memory usage, and uptime.
    *   **SNMP**: Simple network management protocol, useful to allow third party management programs.
    *  **Speed Test**: Tests the connection speed with an external speed testing server.
    *   **Torch**: Displays real-time network packets on an interface. Useful for troubleshooting.
    *   **Traceroute**: Used to trace the network route a packet takes to reach its destination.
    *   **Traffic Flow**: Allows you to view the traffic flow from a specific ip address or subnet.
    *  **Traffic Generator**: A tool to generate traffic to test your network.
* **Extended Features**
    *   **Container**: The router can run containers.
    *   **DLNA Media server**: The router can act as a media server on the network.
    *   **SMB**: The router can be set up as a network file share.

**7. MikroTik REST API Examples:**

The MikroTik API allows remote configuration and management. Here are examples related to IP addresses:

*   **API Endpoint:** `/ip/address`

*   **Get all IP Addresses:**
    *   **Request Method:** `GET`
    *   **Example curl request:**

        ```bash
        curl -k -u 'username:password' https://<router_ip>/rest/ip/address
        ```
    *   **Expected Response (JSON):**
        ```json
        [
            {
            "id": "*1",
            "address": "190.39.90.1/24",
            "interface": "ether-49",
            "network": "190.39.90.0",
            "actual-interface": "ether-49",
            "disabled": "false",
            "dynamic": "false",
            "invalid": "false"
        },
        {
            "id": "*2",
            "address": "192.168.88.1/24",
            "interface": "bridge1",
            "network": "192.168.88.0",
            "actual-interface": "bridge1",
            "disabled": "false",
            "dynamic": "false",
            "invalid": "false"
        }
        ]
        ```
* **Add a new address (POST):**
  *   **Request Method:** `POST`
  *   **Request JSON Payload:**

        ```json
        {
          "address": "190.39.90.2/24",
          "interface": "ether-49"
        }
        ```
  * **Example curl Request:**
        ```bash
        curl -k -u 'username:password' -H "Content-Type: application/json" -X POST -d '{"address": "190.39.90.2/24", "interface": "ether-49"}' https://<router_ip>/rest/ip/address
        ```
   *   **Expected Response (JSON):**

        ```json
            {
            "id": "*3"
            }
        ```
* **Remove an IP address (DELETE):**

    * **Request Method:** `DELETE`
    * **Example curl request:**

        ```bash
         curl -k -u 'username:password' -X DELETE https://<router_ip>/rest/ip/address/*3
        ```
    * **Expected Response (JSON):**
        ```json
        {
            "status": "ok"
        }
       ```

**8. In-depth Explanations of Core Concepts:**

*   **IP Addressing (IPv4 and IPv6)**:
    *   IPv4 addresses are 32-bit addresses, typically written as four decimal numbers separated by periods (e.g., `192.168.1.1`). They're used to uniquely identify devices on a network.
    *   IPv6 addresses are 128-bit addresses, often written as eight groups of four hexadecimal digits separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`). The primary purpose is to solve the IPv4 exhaustion issue, but offers many other benefits as well.
    *   Subnet masks (like `/24`) determine the network portion and host portion of an IP address. `/24` means the first 24 bits are the network ID.

*   **IP Pools**:  A range of IPs used for dynamic assignment via DHCP.

*   **IP Routing**: The router uses the destination IP of incoming packets, and determines the output interface and next-hop IP based on routing table entries. A directly connected network creates a route entry in the routing table.

*   **Bridging**: Transparent Layer 2 forwarding. It's like a switch, and it allows traffic on multiple interfaces to be in the same layer 2 domain, and on the same subnet.

*   **Firewall**: A configurable set of rules to filter traffic. MikroTik's firewall is extremely powerful. We will discuss the firewall more in section 10.
*   **Routing Protocol**: In the routeros environment, the router must know the routing path for all subnets on the network. When manually configured, this involves static routing. Routing protocols will allow the router to automatically configure the best routes for networks.

**9. Security Best Practices:**

*   **Strong Passwords:** Always use a strong, unique password for the admin user.
*   **Disable Unnecessary Services:** Disable any services you are not using, such as telnet and API.
*   **Firewall Rules:** Filter inbound traffic using firewall rules.
*   **Regular Updates:** Keep your RouterOS version up to date.
*   **MAC Access Lists:** Use `/interface ethernet mac-access-list` to restrict access to the ethernet interfaces.
*   **SSH Port Modification:** Change the default SSH port.
*   **API User Permissions:** Limit the permissions of API users.
*   **HTTPS for Web UI:** Use HTTPS for web access, and enforce strong TLS settings in `/ip service ssl`.
*   **ROMON Password**: Set a strong ROMON Password to prevent unauthorized access to your router.
* **Certificates**: When a client device is used for external management of the router, a certificate should be used to prevent man-in-the-middle attacks. The same is true for TLS enabled services.

**10. Detailed Explanations and Configuration Examples for MikroTik Topics**

Let's dive into the detailed configurations and explanations for the rest of the listed topics.

**- IP Addressing (IPv4 and IPv6)**: As discussed earlier, we've configured a static IPv4 address. Let's add a global IPv6 address.

    ```mikrotik
    /ipv6 address add address=2001:db8::1/64 interface=ether-49
    ```
    *   This adds a global IPv6 address to our interface. Note that you would need to use a specific IP address as provided by your ISP or network administrator.

**- IP Pools:** We briefly touched on this. IP Pools are crucial for DHCP. Let's create a simple pool:

    ```mikrotik
    /ip pool
    add name=dhcp_pool ranges=190.39.90.100-190.39.90.200
    ```
    *   This creates a pool named `dhcp_pool` with addresses from `.100` to `.200` in the `/24` subnet.

**- IP Routing:**

    *   **Static Routes**: We can add a static route using the command:
        ```mikrotik
        /ip route add dst-address=10.0.0.0/24 gateway=192.168.1.1
        ```
        This command tells the router to route packets destined for `10.0.0.0/24` to the next-hop of `192.168.1.1`. In this specific example, the gateway must exist within the routing table.
    *   **Dynamic Routes:** For dynamic routing, protocols like OSPF or BGP are used, which are more complex. We'll cover OSPF as an example here:
        ```mikrotik
        /routing ospf instance add name=ospf1 router-id=192.168.10.1
        /routing ospf network add network=190.39.90.0/24 area=backbone
        /routing ospf interface add interface=ether-49
        ```
        This configures a basic OSPF instance with a router ID, adds the network, and sets up OSPF on the specified interface.

**- IP Settings:**  These settings control global IP behaviour, typically left at default values:

    ```mikrotik
    /ip settings
    set allow-fast-path=yes icmp-rate-limit=10000 log-martians=no
    ```

**- MAC Server**: This is used to connect to webfig by MAC address.

    ```mikrotik
    /tool mac-server set allowed-interfaces=all enabled=yes
    /tool mac-server print
    ```

**- RoMON:** RoMON (Router Management Overlay Network) allows managing MikroTik routers through a separate, more private network. Let's configure RoMON:

    ```mikrotik
    /tool romon set enabled=yes interface=ether1
    /tool romon set id=router1
    /tool romon set password=your_secure_password
    ```

**- WinBox:**

    *   Winbox is the Windows GUI that allows for the configuration of your router. It connects through the MAC Address of the router by default. It is an essential tool for many administrators.
    * It can also connect via IP if the Router allows.

**- Certificates:** Certificates are necessary for secure services like HTTPS, VPNs, etc. Here is how to generate a self signed certificate.
    ```mikrotik
    /certificate
    add name=my_cert common-name=190.39.90.1 subject-alt-name="DNS:190.39.90.1, IP:190.39.90.1"
    /certificate sign my_cert
    /ip service set www certificate=my_cert
    ```

**- PPP AAA:** PPP AAA (Authentication, Authorization, Accounting) is used for PPP connections such as PPPoE. It provides a framework for controlling which users are allowed to connect, what they are authorized to access, and logging information about usage.
    *   We won't create a full AAA setup, but we will create a simple user for demonstration purposes.

    ```mikrotik
        /ppp secret
        add name=test_user password=your_secure_password service=any profile=default
    ```
   This command adds the user `test_user` with `your_secure_password`. This user can be used to log in through a VPN.

**- RADIUS:** RADIUS is used to centralize authentication for a large number of users. We can add a radius server using the command below:
    ```mikrotik
    /radius add address=192.168.1.1 secret=radius_secret service=ppp timeout=3000
    ```
*   `address` Specifies the address of the radius server
*   `secret` is the secret that the server uses to authenticate with the radius server
*   `service` tells what service will use this radius config
*   `timeout` is a timeout in milliseconds.

**- User / User groups:**
    ```mikrotik
    /user group add name=admin-group policy=read,write,test,reboot,password
    /user add group=admin-group name=admin_user password=your_secure_password
    ```
    This creates a new group `admin-group` with all of the important policies, and creates a user that belongs to that group.

**- Bridging and Switching**: Let's create a bridge to include our interface.
   ```mikrotik
    /interface bridge add name=bridge1
    /interface bridge port add bridge=bridge1 interface=ether-49
    ```
    This creates a bridge, and adds our `ether-49` interface to the bridge. The device will now forward packets between ports.

**- MACVLAN:** Let's create a MACVLAN interface on `ether-49`.
    ```mikrotik
    /interface macvlan add name=macvlan1 interface=ether-49 mac-address=02:44:44:44:44:01
    /ip address add address=192.168.1.2/24 interface=macvlan1
    ```

**- L3 Hardware Offloading**: This is generally enabled by default, and can be verified under `/system routerboard settings`. Hardware offloading improves performance by offloading packet processing to specialized hardware.

**- MACsec**: MACsec provides encryption for L2 traffic.
    ```mikrotik
        /interface ethernet set ether-49 mac-sec-profile=default
        /interface macsec profile add name=default cipher-suite=gcm-aes-128 secret=a1a2a3a4a5a6a7a8a1a2a3a4a5a6a7a8
        /interface ethernet set ether-49 mac-sec-enable=yes
    ```
   This commands enables MACsec for the interface with the specified profile, and adds a new profile.

**- Quality of Service (QoS):**

    *   **Mangle:** Let's prioritize traffic from the `190.39.90.0/24` subnet:

        ```mikrotik
        /ip firewall mangle
        add chain=forward src-address=190.39.90.0/24 action=mark-packet new-packet-mark=local_priority passthrough=yes
        ```
        This rule marks all packets with `local_priority` coming from that subnet.

    *   **Queue Tree:** Now we use the mark to prioritize:

        ```mikrotik
        /queue tree
        add name=local_priority_queue parent=global-out packet-mark=local_priority priority=1
        add name=default_queue parent=global-out priority=8
        ```

    *   **Connection Tracking:** MikroTik's firewall uses connection tracking. A good practice is to add an input rule that accepts established connections, and invalid connections dropped.
      ```mikrotik
      /ip firewall filter
      add chain=input connection-state=established action=accept
      add chain=input connection-state=invalid action=drop
      ```

**- Switch Chip Features:**  Certain RouterBOARDs have switch chips with VLAN tagging capabilities. VLAN IDs can be configured under `/interface ethernet switch vlan`. These settings are specific to the features of the switch chip on your device. The exact implementation is hardware dependent.
**- VLAN:** We briefly covered VLAN in section 6. Here is how to add a tagged VLAN interface to `ether-49`
    ```mikrotik
    /interface vlan add name=vlan100 vlan-id=100 interface=ether-49
    /ip address add address=192.168.100.1/24 interface=vlan100
    ```

**- VXLAN**: To create a VXLAN tunnel, we must configure a virtual interface.
```mikrotik
/interface vxlan add name=vxlan1 vni=100 remote-address=192.168.1.2 interface=ether-49
/ip address add address=172.16.1.1/24 interface=vxlan1
```
This creates a tunnel to `192.168.1.2`, on vni 100 using the specified interface. A destination must also be added. A virtual subnet is assigned on this interface.

**- Firewall and Quality of Service (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP):**
    *   **Firewall Rules:**
        *   **Input Chain**: Used to filter traffic destined for the router itself.

            ```mikrotik
             /ip firewall filter
             add chain=input action=drop in-interface=ether-49 src-address=0.0.0.0/8
             add chain=input action=drop in-interface=ether-49 src-address=127.0.0.0/8
             add chain=input action=drop in-interface=ether-49 src-address=172.16.0.0/12
             add chain=input action=drop in-interface=ether-49 src-address=192.168.0.0/16
             add chain=input protocol=tcp dst-port=22 action=accept comment="Allow SSH from our network" src-address=190.39.90.0/24
             add chain=input action=drop protocol=tcp dst-port=22 comment="Drop SSH from other sources"
             add chain=input action=accept protocol=icmp comment="Allow ping from our network" src-address=190.39.90.0/24
             add chain=input action=drop protocol=icmp comment="Drop ping from other sources"
             add chain=input action=accept comment="Accept established connections" connection-state=established
             add chain=input action=drop comment="Drop all invalid connections" connection-state=invalid
            ```
           This configuration drops private subnets to prevent spoofing, accepts SSH connections from our network, and also blocks them from other sources, allows ping from our network, and blocks ping from other sources, accepts established connections, and drops invalid packets.
        *   **Forward Chain:** Used to filter traffic passing through the router:
           ```mikrotik
            /ip firewall filter
            add chain=forward action=accept comment="Allow Forward for our subnet" src-address=190.39.90.0/24 dst-address=190.39.90.0/24
           add chain=forward action=drop comment="Drop other subnets"
           ```
           This configuration accepts packets for our subnet, and drops traffic for other subnets.
        *   **Connection Tracking:** The firewall uses connection tracking and connection states (`established`, `invalid`, etc.)

    *   **Packet Flow:**
        1.  Incoming packets reach the interface.
        2.  The firewall's input chain processes them.
        3.  Packets are routed.
        4.  The firewall's forward chain processes transit packets.
        5.  Packets exit through an interface.

    *   **Queues (PCQ):** Per-Connection Queueing.

        ```mikrotik
        /queue type add name=pcq-download kind=pcq pcq-classifier=dst-address pcq-rate=20M
        /queue type add name=pcq-upload kind=pcq pcq-classifier=src-address pcq-rate=10M
        /queue simple add max-limit=20M/10M name=pcq-queue queue=pcq-download/pcq-upload target=190.39.90.0/24
        ```
        This configuration creates a PCQ, and sets a download/upload rate limit of 20/10Mbps for the specified subnet.

    *   **Firewall and QoS Case Studies:** Real-world examples are heavily dependent on specific requirements. Examples can range from prioritization of VoIP traffic, to throttling file sharing.
    *   **Kid Control:** Can be done by filtering by destination URLs and times. An example would be to drop any connection destined to "facebook.com" between the hours of 9 PM and 7 AM.
        ```mikrotik
        /ip firewall filter add chain=forward dst-address=www.facebook.com out-time=21:00:00-07:00:00 action=drop comment="Block facebook at night"
        ```
    *   **UPnP:** Universal Plug and Play is a protocol to enable automatic port forwarding by the client application. This is not recommended due to security risks, but is supported on the router.
    * **NAT-PMP:** A NAT protocol alternative to UPnP.

**- IP Services (DHCP, DNS, SOCKS, Proxy)**:

    *   **DHCP:** We configured a basic DHCP server earlier. Additional options like static DHCP leases can be configured as well.
        ```mikrotik
        /ip dhcp-server lease add address=190.39.90.150 mac-address=00:11:22:33:44:55 server=local-dhcp-server
        ```
        This ensures that the device with the specified MAC address always gets IP `190.39.90.150`.

    *   **DNS:**
       ```mikrotik
        /ip dns set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
        ```
       This command configures the router to use google's DNS