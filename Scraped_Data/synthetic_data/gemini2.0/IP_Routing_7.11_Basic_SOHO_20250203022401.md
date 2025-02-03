Okay, let's craft comprehensive documentation for IP routing within the specified MikroTik RouterOS environment, focusing on a SOHO setup using the bridge interface.

## MikroTik RouterOS Configuration: IP Routing for 160.113.147.0/24 on bridge-52

This document provides a detailed guide to configuring IP routing on a MikroTik RouterOS device for the subnet 160.113.147.0/24 using the bridge interface named `bridge-52`. We'll cover basic IP configuration, address assignment, and routing, along with related topics, troubleshooting and security best practices relevant to MikroTik devices.

### 1. Configuration Scenario & Requirements

**Scenario:** We are setting up a small home or office network where devices within the 160.113.147.0/24 subnet will connect through a bridge interface called `bridge-52`. The MikroTik router will act as the gateway for this network, providing routing to other networks (e.g., the internet).

**Specific Requirements:**

*   **Subnet:** 160.113.147.0/24
*   **Interface:**  `bridge-52` (Bridge Interface).
*   **Router IP:** Assign a static IP address within the subnet to the bridge interface to act as the gateway for the local network.
*   **Routing:** The MikroTik router will route traffic between the `bridge-52` network and other networks.

### 2. Step-by-Step Implementation

This section provides steps to implement the IP routing configuration using both CLI commands and Winbox graphical user interface.

**2.1 Implementation using MikroTik CLI:**

*   **Step 1: Create Bridge Interface (if not already created)**
    *If you already have a bridge named `bridge-52`, you can skip this step.*
    ```mikrotik
    /interface bridge
    add name=bridge-52
    ```
     *   **Explanation:** This command creates a bridge interface with the name `bridge-52`.

*   **Step 2: Add Interface(s) to Bridge**
    ```mikrotik
    /interface bridge port
    add bridge=bridge-52 interface=ether2 # Replace with your desired interface(s).
    add bridge=bridge-52 interface=ether3 # Add more ports as needed.
    ```
    *   **Explanation:** This adds `ether2` and `ether3` (or desired ports) to the `bridge-52` interface.  These ports will now act as a single bridged network.
    *   **Note:** You can add more or fewer ports depending on your network hardware configuration.
*   **Step 3: Assign IP Address to the Bridge Interface**
    ```mikrotik
    /ip address
    add address=160.113.147.1/24 interface=bridge-52
    ```
    *   **Explanation:** This assigns the IP address 160.113.147.1/24 to the `bridge-52` interface. This IP address becomes the gateway for clients connected to this network.

*   **Step 4: (Optional) Set a Default Route**
    ```mikrotik
    /ip route
    add dst-address=0.0.0.0/0 gateway=192.168.88.1 # Replace 192.168.88.1 with your ISP gateway
    ```
     *   **Explanation:** This adds a default route that sends all traffic destined for networks outside of your local subnet to the gateway address provided. Ensure your gateway IP address is correct.
    *   **Note:** This step is only needed if you want to allow routing to internet or other networks.
* **Step 5: (Optional) NAT (Network Address Translation)**
  ```mikrotik
     /ip firewall nat
      add chain=srcnat action=masquerade out-interface=<your_wan_interface>  # Replace <your_wan_interface> with the interface connected to the internet.
  ```
     *   **Explanation:** This configures NAT, which allows devices on the internal network to access the internet by translating their private IP addresses to the router's public IP address.
     *   **Note:** Replace `<your_wan_interface>` with your public-facing interface (e.g., `ether1` or `pppoe-out1`).

**2.2 Implementation using Winbox GUI:**

*   **Step 1: Create Bridge Interface:**
    1. Connect to your MikroTik router using Winbox.
    2.  Navigate to `Interface` -> `Bridge`.
    3. Click the `+` (Add) button.
    4. Enter `bridge-52` as the name.
    5. Click `Apply` and `OK`.
*   **Step 2: Add Interfaces to the Bridge:**
    1. Go to `Interface` -> `Bridge` -> `Ports` tab.
    2. Click the `+` (Add) button.
    3. Select your desired interface from `Interface` dropdown (e.g., `ether2`).
    4. Choose `bridge-52` from `Bridge` dropdown.
    5. Click `Apply` and `OK`.
    6. Repeat for all ports you want to add to the bridge.
*   **Step 3: Assign IP Address:**
    1. Go to `IP` -> `Addresses`.
    2. Click the `+` (Add) button.
    3. In `Address` enter: `160.113.147.1/24`.
    4. Select `bridge-52` from `Interface` dropdown.
    5. Click `Apply` and `OK`.
*   **Step 4: (Optional) Set Default Route:**
    1. Go to `IP` -> `Routes`.
    2. Click the `+` (Add) button.
    3. In `Dst. Address` enter: `0.0.0.0/0`.
    4. In `Gateway` enter your ISP's gateway address (e.g., 192.168.88.1).
    5. Click `Apply` and `OK`.
*   **Step 5: (Optional) NAT Configuration:**
    1. Go to `IP` -> `Firewall` -> `NAT`.
    2. Click the `+` (Add) button.
    3. In `Chain`, select `srcnat`.
    4. In `Action`, select `masquerade`.
    5. In `Out. Interface`, select your WAN interface (e.g., ether1 or pppoe-out1).
    6. Click `Apply` and `OK`.

### 3. Complete MikroTik CLI Configuration Commands

Here are the complete CLI commands that can be copied and pasted into a MikroTik terminal.

```mikrotik
/interface bridge
add name=bridge-52

/interface bridge port
add bridge=bridge-52 interface=ether2
add bridge=bridge-52 interface=ether3

/ip address
add address=160.113.147.1/24 interface=bridge-52

/ip route
add dst-address=0.0.0.0/0 gateway=192.168.88.1 # Replace with your ISP gateway

/ip firewall nat
add chain=srcnat action=masquerade out-interface=<your_wan_interface>  # Replace with your WAN interface
```

### 4. Common MikroTik Pitfalls, Troubleshooting & Diagnostics

**Pitfalls:**

*   **IP Conflict:** Ensure no other device on the network uses the same IP address as assigned to the bridge interface.
*   **Bridge Misconfiguration:** Devices may fail to connect if bridge ports are not configured correctly.
*   **Firewall Rules:** Ensure firewall rules don't block necessary traffic.
*   **Incorrect Gateway:** Incorrect default gateway will prevent internet access.
*   **NAT issue:**  If NAT is not configured correctly, devices behind the MikroTik router won't be able to access the internet.

**Troubleshooting:**

*   **Connectivity Check:**  Use `ping` from the MikroTik and from devices on the network:
    ```mikrotik
    /ping 160.113.147.1  # Ping the bridge interface from the router itself
    /ping 160.113.147.2 # Ping a device from the network
    ```

*   **Route Verification:** Check routing tables using:
    ```mikrotik
    /ip route print
    ```
   *   This will show the defined routes. Ensure a default route exists for internet access.
*   **Interface Status:**  Check the status of the bridge interface and associated ports using:
   ```mikrotik
   /interface print
   /interface bridge port print
   ```
    * Make sure the interfaces are in running state and there are no errors.
*   **Firewall Check:** If the traffic is blocked, check `IP` -> `Firewall` -> `Filter Rules` and disable temporary to test.

*   **Torch Utility:** Use `torch` for real-time traffic analysis. For example, to see traffic on the bridge interface:
    ```mikrotik
    /tool torch interface=bridge-52
    ```

*   **Error Scenario Example:**

    If a device on the `160.113.147.0/24` network cannot reach the internet, the error might look like:
        *   `Ping` to 8.8.8.8 (Google DNS) will fail with "request timed out".
        *   `traceroute` to 8.8.8.8 will show a single hop to the gateway address.
        *   **Troubleshooting Steps:**
            *   Confirm the default route and NAT configurations.
            *   Check firewall rules if blocking traffic.
            *   Verify gateway is correct and responsive.
            *   Ensure the WAN interface is correctly configured and active.

### 5. Verification and Testing

*   **Ping Test:** From a device connected to the `bridge-52` network:
    *   Ping the router's IP address (160.113.147.1).
    *   Ping an external IP address (e.g., 8.8.8.8).
*   **Traceroute Test:** From a device connected to the `bridge-52` network:
    *   `traceroute` to an external IP (e.g., 8.8.8.8) to verify path of the network traffic.
*   **Router Resource Monitor:** Check the router's CPU and memory usage while testing:
   ```mikrotik
   /system resource print
   ```
    *   This ensures that router isn't overloaded.
*   **Interface Statistics:** Check the interface stats for traffic:
    ```mikrotik
    /interface monitor bridge-52 once
    ```

### 6. Related MikroTik-Specific Features, Capabilities, & Limitations

*   **Bridging:** MikroTik bridges work at Layer 2, allowing multiple interfaces to act as a single segment.  They are essential for creating local networks with multiple physical ports.
*   **Routing:** MikroTik supports static and dynamic routing. Static routing is used in this case.
*   **Firewall:** The firewall allows for complex rules to control traffic flow, including NAT and QoS.
*   **L3 Hardware Offloading:** Some MikroTik devices support Layer 3 hardware offloading, which can greatly improve routing performance. (Not applicable here as we're using a bridge, but crucial in routed scenarios.)
*   **VLAN:** While not part of this scenario, MikroTik bridges can also support VLANs for network segmentation.
*   **Limitations:**
    *   MikroTik devices have varying hardware limitations depending on the model (CPU, memory, interfaces).
    *   Complex configurations can impact performance, particularly on less powerful devices.
*   **Less Common Scenario:**
   *   **VLAN Tagging on Bridge Ports:** You can configure the bridge to support VLANs, effectively tagging packets with a VLAN ID as they traverse the bridge. This adds segmentation within the bridge network but would require changes to the above configuration.

### 7. MikroTik REST API Examples (Basic)

Here are basic examples for some of the CLI commands:

*   **Getting Interface Information:**

    *   **API Endpoint:** `/interface`
    *   **Request Method:** GET
    *   **Example Request (via `curl`):**
        ```bash
        curl -k -u 'admin:<your_password>' 'https://<router_ip>/rest/interface'
        ```

        *   **Expected Response (Example JSON):**
            ```json
            [
                {
                    ".id": "*1",
                    "name": "ether1",
                    "type": "ether",
                    "mtu": "1500",
                    "actual-mtu": "1500",
                    "l2mtu": "1598",
                    "mac-address": "XX:XX:XX:XX:XX:XX",
                    "disabled": "false",
                    "running": "true"
                   },
                   {
                        ".id": "*2",
                        "name": "bridge-52",
                        "type": "bridge",
                        "mtu": "1500",
                        "actual-mtu": "1500",
                        "l2mtu": "1598",
                        "mac-address": "YY:YY:YY:YY:YY:YY",
                        "disabled": "false",
                        "running": "true"
                   }
             ]
           ```

*   **Getting IP Addresses:**

    *   **API Endpoint:** `/ip/address`
    *   **Request Method:** GET
    *   **Example Request (via `curl`):**
        ```bash
        curl -k -u 'admin:<your_password>' 'https://<router_ip>/rest/ip/address'
        ```
     *   **Expected Response (Example JSON):**
            ```json
            [
                 {
                   ".id": "*2",
                    "address": "160.113.147.1/24",
                    "interface": "bridge-52",
                    "actual-interface": "bridge-52",
                    "network": "160.113.147.0",
                    "disabled": "false",
                    "dynamic": "false",
                    "invalid": "false"
                 }
            ]
            ```
*   **Adding IP address:**
   *   **API Endpoint:** `/ip/address`
   *   **Request Method:** POST
    *   **Example Request (via `curl`):**
          ```bash
          curl -k -u 'admin:<your_password>' -H "Content-Type: application/json" -X POST -d '{"address": "160.113.147.2/24", "interface": "bridge-52"}' 'https://<router_ip>/rest/ip/address'
          ```
    *   **Expected Response (Example JSON):**
        ```json
          {
              ".id": "*3",
               "address": "160.113.147.2/24",
                "interface": "bridge-52",
                "actual-interface": "bridge-52",
                "network": "160.113.147.0",
               "disabled": "false",
                "dynamic": "false",
                "invalid": "false"
            }
        ```
        * **Note:** Replace `<router_ip>` with the router's IP address or host name and `<your_password>` with the administrator password. These are just basic examples, the MikroTik API offers much more.

### 8. In-Depth Explanation of Core Concepts

*   **IP Addressing:** IP addresses are fundamental for communication. IPv4 addresses (like 160.113.147.1/24) are 32-bit values, often represented in dotted-decimal notation. The `/24` represents the subnet mask, which defines how many addresses are in the subnet.
    *   **Why this address?** The IP `160.113.147.1` is the router's interface address and acts as the default gateway for the devices in the `160.113.147.0/24` network.
*   **Bridging:** Bridging at Layer 2 combines multiple Ethernet interfaces to act as one. All traffic coming into a port on the bridge goes to every other port on the bridge.
    *   **Why bridge?**  It provides a simple way to extend a single network without needing IP routing between each port.
*   **IP Routing:**  Routing occurs at Layer 3 (IP Layer). Routing decisions determine the path a packet takes to reach its destination. In this basic setup, static routing allows the router to direct traffic to other networks.
   *  **Why Static Routing:** In this case we have defined a default route, which indicates all traffic destined for outside our local network (160.113.147.0/24) should be routed to our ISP default gateway.
*   **Firewall & NAT:** Firewall rules control traffic flow in and out of the router. Network Address Translation (NAT) maps private IP addresses to a single public IP address, enabling devices on private networks to access the internet.
   *  **Why NAT:** In this case, NAT allows devices in our 160.113.147.0/24 subnet to access internet using the public IP address assigned to the WAN interface of the router.

### 9. Security Best Practices

*   **Strong Passwords:** Use strong, unique passwords for your MikroTik administrator account.
*   **Disable Default User:** Disable the default admin user or change its username.
*   **Access Control:** Limit Winbox and SSH access to specific IP addresses.
*   **Firewall Rules:** Implement robust firewall rules to block unwanted traffic.
*   **Regular Updates:**  Keep RouterOS and firmware updated to the latest version to address security vulnerabilities.
*   **Disable Unnecessary Services:** Disable any services not needed.
*   **Less Common Features:**
    *   **ROMON Security:**  If using RoMON (MikroTik's remote monitoring protocol), ensure its encryption is enabled and access is tightly controlled. RoMON is powerful, but a breach would allow remote control over all attached MikroTik devices.
    *   **API Security:** Use HTTPS for API access and restrict API access only to authorized IPs.
*   **Best Practice Example:**
    ```mikrotik
    # Limit winbox access to specific IPs
    /ip service set winbox address=192.168.1.0/24
    # Disable default admin
    /user set admin disabled=yes
    # Create a new admin user
    /user add name=secureadmin group=full password=securepassword
    # Limit ssh to specific IPs
    /ip service set ssh address=192.168.1.0/24
    # Enable HTTPS for API access
    /ip service set api-ssl certificate=my_certificate
    ```

### 10. Detailed Explanations and Configuration Examples for MikroTik Topics

Due to the extensive scope of each of these topics, this section provides a high-level overview and configuration examples.

#### **IP Addressing (IPv4 and IPv6)**

*   **IPv4:** We covered IPv4 configuration above using static address assignment.
*   **IPv6:**
    ```mikrotik
    # Enable IPv6
    /ipv6 settings set disabled=no
    # Request IPv6 address through DHCP client on WAN
    /ipv6 dhcp-client add interface=ether1 add-default-route=yes request=address,prefix
    # Add IPv6 address to the bridge (ULAs)
    /ipv6 address add address=fd00::1/64 interface=bridge-52
    ```

#### **IP Pools**

*   Used for dynamic address assignments (e.g., for DHCP).
    ```mikrotik
    /ip pool add name=lan-pool ranges=160.113.147.10-160.113.147.254
    ```

#### **IP Routing**

*   We covered static routing above. Dynamic protocols (OSPF, RIP, BGP) are used for complex network environments.
*   **Policy-Based Routing:** Lets you direct traffic based on more criteria than just destination.

#### **IP Settings**

*   General settings, such as disabling ICMP redirects.
    ```mikrotik
    /ip settings set icmp-redirects=no
    ```

#### **MAC server**

*   Allows MAC addresses to be used for identification and access control. This is rarely used in typical SOHO scenarios but is useful in more complex scenarios involving RADIUS servers and captive portals.
  ```mikrotik
   /mac-server
   set enabled=yes
  ```

#### **RoMON**

*   MikroTik's remote monitoring tool that allowes to monitor MikroTik devices from a centralized location.
     ```mikrotik
     /romon set enabled=yes
     /romon port add interface=ether1
     ```
#### **WinBox**

*  MikroTik's GUI management tool. Enable/Disable using:
  ```mikrotik
  /ip service set winbox disabled=no
  ```

#### **Certificates**

*   Used for HTTPS access, VPNs (IPsec, OpenVPN), and other secure protocols.
    ```mikrotik
    # Generate self-signed certificate
    /certificate add name=my_certificate common-name=router.local
    ```

#### **PPP AAA**

*   Authentication, Authorization, and Accounting for PPP connections.
    ```mikrotik
    /ppp aaa set use-radius=yes
    ```

#### **RADIUS**

*   Centralized authentication server used for user management (useful in larger networks).
  ```mikrotik
   /radius add address=10.0.0.1 secret=radius_secret service=ppp
  ```

#### **User / User groups**

*   Manage access to the router.
  ```mikrotik
   /user group add name=readonly policy=read
   /user add name=viewer group=readonly password=viewerpass
  ```

#### **Bridging and Switching**

*   We've already covered basic bridging, including interface ports and VLANs.
    *  **Layer 2 Switching** Bridge acts as layer 2 switch.
*   **Spanning Tree:** Used for loop prevention
     ```mikrotik
     /interface bridge set bridge-52 protocol-mode=rstp
     ```
#### **MACVLAN**

*   Creates virtual interfaces from a single physical interface, each with its own MAC address. Not often used in SOHO environments, but used for more complex virtualization scenarios.
   ```mikrotik
   /interface macvlan add interface=ether1 mac-address=02:XX:XX:XX:XX:XX name=macvlan1
   ```

#### **L3 Hardware Offloading**

*   Offloads Layer 3 routing processing to the hardware, significantly improving throughput, mostly when using routed interfaces.
     ```mikrotik
     /interface ethernet set ether1 l3-hw-offloading=yes
     ```

#### **MACsec**

*   Layer 2 security protocol that encrypts ethernet traffic, used in critical infrastructure to provide data integrity. Requires dedicated hardware support.
    ```mikrotik
   /interface macsec set ether1 key=secret-key profile=macsec-profile
    ```

#### **Quality of Service**

*   Traffic prioritization using queues and shaping.

    ```mikrotik
    /queue tree add name=download parent=global max-limit=10M
    /queue tree add name=upload parent=global max-limit=5M
    /queue simple add queue=download target=192.168.1.0/24
    /queue simple add queue=upload target=192.168.1.0/24
    ```

#### **Switch Chip Features**

*   Specific features offered by switch chips on some MikroTik hardware. Used for hardware VLAN support and traffic management within the switch.
   *   **Port Isolation** You can isolate certain ports at the hardware level.
    ```mikrotik
    /interface ethernet switch port set ether2 mirror-target=ether3
    ```

#### **VLAN**

*   Network segmentation within a physical network.
    ```mikrotik
    /interface vlan add name=vlan100 vlan-id=100 interface=bridge-52
    /ip address add address=192.168.100.1/24 interface=vlan100
    ```

#### **VXLAN**

*   Layer 2 overlay network that extends LANs over IP networks, used to extend networks across sites.
     ```mikrotik
      /interface vxlan add name=vxlan1 vni=1000 interface=ether1 remote-address=10.0.0.2
     ```

#### **Firewall and Quality of Service**

*   **Connection tracking** : Keeps track of established connections for better firewall decisions.
*   **Firewall** : Rules to control traffic, NAT, etc.
    ```mikrotik
   /ip firewall filter add chain=forward action=drop src-address=10.0.0.0/24
   ```

*   **Packet Flow in RouterOS**: The way packets travel through the router's system, including connection tracking, nat and routing.
*   **Queues:** Traffic shaping and prioritization.
*   **QoS Case Studies:** See examples above for Quality of Service.
*   **Kid Control:**  Time-based access control to limit internet usage for children.
*   **UPnP:** Automatic port mapping using UPnP for devices to easily expose services behind the NAT.
   ```mikrotik
    /ip upnp set enabled=yes
   ```
*   **NAT-PMP:** Similar to UPnP using the NAT-PMP protocol.

#### **IP Services (DHCP, DNS, SOCKS, Proxy)**

*   **DHCP Server:** For dynamic IP address assignment.
    ```mikrotik
    /ip dhcp-server add name=lan-dhcp interface=bridge-52 address-pool=lan-pool
    /ip dhcp-server network add address=160.113.147.0/24 gateway=160.113.147.1 dns-server=8.8.8.8
    ```
*   **DNS Server:** For DNS resolution.
    ```mikrotik
    /ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
    ```
*   **SOCKS Proxy:** Allows client connections via SOCKS proxy to access remote networks.
*   **Proxy:** Provides a caching proxy server for web browsing.

#### **High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples)**

*   **Load Balancing:** Using multiple WAN connections for balancing traffic (not covered here).
*   **Bonding:** Aggregates multiple Ethernet links for increased bandwidth and redundancy, including many options.
  ```mikrotik
   /interface bonding add name=bond1 mode=802.3ad slaves=ether2,ether3
  ```
*   **VRRP:** Provides redundancy for IP addresses, making sure a second router takes over in case a primary fails.
  ```mikrotik
   /interface vrrp add interface=ether1 vrid=1 address=10.0.0.1/24 priority=100
  ```
*   **HA Case Studies** Complex solutions requiring dedicated configurations.
*   **Multi-chassis Link Aggregation Group**  Requires specific hardware configurations.

#### **Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application)**

*   **LTE Interface:** Used for connecting to mobile networks.
*   **GPS:**  Provides location information.
*   **PPP:** Includes PPPoE, PPTP, and L2TP connections.
*   **SMS:** Used for sending and receiving text messages using mobile interface.
*   **Dual SIM Application:** Used on routers that have dual SIM capabilities.

#### **Multi Protocol Label Switching - MPLS**

*   Complex protocol to expedite routing based on labels.
*   **MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference** Advanced topics that are beyond the scope of a basic SOHO setup.

#### **Network Management**

*   **ARP:** Address Resolution Protocol for mapping IP to MAC addresses.
*  **Cloud:** MikroTik cloud management features.
*   **DHCP, DNS, SOCKS, Proxy:** See above.
*  **Openflow** Software defined networking.

#### **Routing**

*   **Routing Protocol Overview:**  Static vs. Dynamic routing.
*   **Moving from ROSv6 to v7 with examples:** Changes in routing between ROS version 6 and 7.
*   **Routing Protocol Multi-core Support:** Support for multicore processors for better routing performance.
*   **Policy Routing:** Route traffic based on specific criteria.
*   **Virtual Routing and Forwarding - VRF:** Allows multiple routing tables to exist within a single router.
*   **OSPF, RIP, BGP:** Dynamic routing protocols for automated routing decisions.
*   **RPKI:** Routing Public Key Infrastructure for route validation and security.
*   **Route Selection and Filters:** Rules to determine optimal path and filter routes.
*   **Multicast:** Routing for sending packets to many destinations simultaneously.
*   **Routing Debugging Tools:** Tools like `traceroute` and `routing monitor`.
*   **Routing Reference:** Comprehensive documentation of routing configuration.
*   **BFD:** Bi-directional forwarding detection, for faster link failure detection
*   **IS-IS:** Another link state routing protocol used mainly in large enterprise environments.

#### **System Information and Utilities**

*   **Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP.**
    *   **Clock:** Set system time and timezone.
    ```mikrotik
     /system clock set time-zone-name=Europe/London
    ```
    *   **Device-mode:** Sets device to router, switch, etc mode.
    *   **E-mail:** Configure email settings for sending notifications.
    *   **Fetch:** Used for downloading files.
    *   **Files:** View and manage files.
    *   **Identity:** Set device name
       ```mikrotik
       /system identity set name=myrouter
      ```
    *   **Interface Lists:** Logical group of interfaces.
    *   **Neighbor discovery:** Used to find other devices in the network.
    *  **Note** Add notes to configuration for documentation.
    *   **NTP:** Network Time Protocol to synchronize time.
    ```mikrotik
     /system ntp client set enabled=yes primary-ntp=0.pool.ntp.org secondary-ntp=1.pool.ntp.org
    ```
    *   **Partitions:** Manage storage partitions.
    *  **Precision Time Protocol:** Used to provide high-precision time synchronization.
    *   **Scheduler:** Schedule events or tasks.
      ```mikrotik
      /system scheduler add name=test interval=1m start-time=now on-event="/log info message=\"scheduler test\""
    ```
    *   **Services:** Manage enabled services.
    *  **TFTP** Trivial File Transfer Protocol client and server.

#### **Virtual Private Networks (VPNs)**

*   **6to4:** IPv6 transition mechanism.
*   **EoIP:** Ethernet over IP tunneling.
*   **GRE:** Generic Routing Encapsulation tunneling.
*   **IPIP:** IP in IP tunneling.
*   **IPsec:** Secure IP tunneling protocol.
   ```mikrotik
      /ip ipsec proposal add name=my_proposal auth-algorithms=sha256 enc-algorithms=aes-256-cbc
   ```
*   **L2TP:** Layer 2 Tunneling Protocol.
    ```mikrotik
    /interface l2tp-server server set enabled=yes default-profile=default
    ```
*   **OpenVPN:** Open-source VPN protocol.
*   **PPPoE:** Point-to-Point Protocol over Ethernet.
   ```mikrotik
      /interface pppoe-client add user=myuser password=mypassword interface=ether1
    ```
*   **PPTP:** Point-to-Point Tunneling Protocol (less secure, use only when needed).
*  **SSTP:** Secure Socket Tunneling Protocol, used to create VPN over SSL.
*   **WireGuard:** Modern VPN protocol known for its speed and security.
  ```mikrotik
      /interface wireguard add name=wireguard1
      /interface wireguard peers add allowed-address=10.0.0.2/32 interface=wireguard1
  ```
*   **ZeroTier:** Software defined networking.

#### **Wired Connections**

*   **Ethernet:** Standard Ethernet configuration.
*   **MikroTik wired interface compatibility:** Check hardware compatibility and MTU settings.
*   **PWR Line:**  Power over Ethernet capabilities for certain MikroTik devices.

#### **Wireless**

*   **WiFi:** Wireless interfaces (2.4 GHz, 5 GHz).
*   **Wireless Interface:** Basic configuration of wireless interfaces.
*   **W60G:** 60GHz Wireless standard.
*   **CAPsMAN:** Centralized Access Point Management.
*   **HWMPplus mesh:** Wireless Mesh technology.
*  **Nv2:** Proprietary wireless protocol of MikroTik.
*   **Interworking Profiles:** Allows to manage different wireless standards and protocols.
*   **Wireless Case Studies:** Examples for different wireless configurations.
*   **Spectral scan:** To analyze RF interference.
    ```mikrotik
    /interface wireless spectral-history wlan1
    ```

#### **Internet of Things (IoT)**

*   **Bluetooth, GPIO, Lora, MQTT:** Used for different IoT solutions
    *   **GPIO** General-purpose input/output pins, used to control devices or receive signals.
    *   **Lora:** Low range, low power network protocol for IoT sensors.
    *   **MQTT:** Lightweight communication protocol used for sending messages to IoT devices.

#### **Hardware**

*   **Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features.**
    *   **Disks:** View disk status, health and capacity.
    *   **Grounding:** Proper grounding for protection against electrical surges.
    *   **LCD Touchscreen** Functionality for MikroTik devices with LCD screen.
    *   **LEDs** How to configure the LEDs on the device for visual status.
    *   **MTU** Maximum Transmission Unit settings and its importance in networking.
    *   **Peripherals:**  How to connect and manage external devices.
    *   **PoE-Out:** Power over Ethernet port functionality for other connected devices.
    *   **Ports:** Different ports used on MikroTik router.
    *   **Product Naming:** Naming convention used for naming MikroTik devices.
    *   **RouterBOARD:** General overview of MikroTik hardware devices.
    *   **USB Features:** Configuration and usage of USB ports for storage and other peripheral connectivity.

#### **Diagnostics, Monitoring and Troubleshooting**

*   **Bandwidth Test:** To test throughput between devices.
    ```mikrotik
     /tool bandwidth-test address=10.0.0.2 protocol=udp
    