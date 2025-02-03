Okay, let's dive into a detailed configuration guide for MikroTik RouterOS, focusing on IP Pools within a SOHO environment, and expanding to cover the comprehensive list of requested topics. This will be a very extensive document due to the scope.

## MikroTik RouterOS Configuration: IP Pools and Beyond

This document provides detailed technical documentation for configuring IP Pools, and many related features on MikroTik RouterOS. We will be targeting RouterOS 7.11 (and where needed mention differences with 6.48 or v7.x), assuming an expert configuration level for a SOHO network.

### 1. Configuration Scenario and MikroTik Requirements

**Scenario:** We need to configure a MikroTik router for a small office. This router will manage network addressing for internal devices on `bridge-20`. The network uses `29.46.113.0/24` as its subnet. We'll cover a basic IP pool for DHCP, and explore more complex aspects as we progress through the topics.

**MikroTik Specific Requirements:**

*   RouterOS 7.11 (though key parts of this will apply to older version or newer versions)
*   SOHO Environment
*   Subnet: `29.46.113.0/24`
*   Interface: `bridge-20`

### 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

**Using CLI:**

1.  **Create an IP Pool:**
    ```mikrotik
    /ip pool
    add name=dhcp_pool_20 ranges=29.46.113.100-29.46.113.200
    ```
2.  **Configure DHCP Server:** We will create the DHCP server later.

**Using Winbox:**

1.  Connect to your MikroTik router via Winbox.
2.  Navigate to **IP** -> **Pool**.
3.  Click the **+** button to add a new IP Pool.
4.  Enter the following:
    *   **Name:** `dhcp_pool_20`
    *   **Ranges:** `29.46.113.100-29.46.113.200`
5.  Click **Apply** and **OK**.

### 3. Complete MikroTik CLI Configuration Commands

```mikrotik
# IP Pool
/ip pool
add name=dhcp_pool_20 ranges=29.46.113.100-29.46.113.200

# IP Addressing on bridge-20
/ip address
add address=29.46.113.1/24 interface=bridge-20

# DHCP Server Configuration
/ip dhcp-server
add address-pool=dhcp_pool_20 disabled=no interface=bridge-20 name=dhcp1

# DHCP Network
/ip dhcp-server network
add address=29.46.113.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=29.46.113.1
```

**Parameter Explanation:**

*   `/ip pool add name=dhcp_pool_20 ranges=29.46.113.100-29.46.113.200`:
    *   `name`:  The name of the IP pool (e.g. dhcp_pool_20).
    *   `ranges`: A single range or comma-separated list of IP ranges.
*   `/ip address add address=29.46.113.1/24 interface=bridge-20`:
    *   `address`: IP address with subnet mask (e.g., 29.46.113.1/24).
    *   `interface`: The interface to apply the IP to.
*   `/ip dhcp-server add address-pool=dhcp_pool_20 disabled=no interface=bridge-20 name=dhcp1`:
    *   `address-pool`:  The name of the IP pool to use for DHCP assignment.
    *   `disabled`:  `yes` to disable, `no` to enable.
    *   `interface`: Interface where the DHCP service will listen for requests.
    *   `name`: Name for the DHCP server.
*   `/ip dhcp-server network add address=29.46.113.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=29.46.113.1`:
    *   `address`: The network address and subnet mask.
    *   `dns-server`: Comma-separated list of DNS server IP addresses.
    *   `gateway`: Default gateway address for the DHCP clients.

### 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

*   **Pitfall:** Overlapping IP pools. This causes unpredictable DHCP assignments, potentially creating IP conflicts. Always make sure that IP pool ranges do not overlap with other pools.
*   **Troubleshooting DHCP Issues:**
    *   Use `/ip dhcp-server lease print` to check DHCP lease details.
    *   Use `/system logging print` to look for DHCP errors or warnings.
    *   Ensure the client is on the correct VLAN if VLANs are used.
    *   Ensure the DHCP server is enabled and attached to the correct interface.
    *   Check the client's configuration, especially if you use fixed IP addresses.
*   **Error Scenarios:**
    *   `Error: Pool is exhausted`: The DHCP server can't allocate any new IP addresses because there are none left in the pool, increase the pool range.
    *   `Error: Duplicate IP Address`: A device is already assigned the IP address. Check DHCP leases and static IPs.
    *   `DHCP server does not start`: Make sure the interface is up and the server is configured correctly.
*   **Diagnostics using Built-in tools:**
    *   `/ping <IP Address>`: To check basic connectivity.
    *   `/traceroute <IP Address>`: To trace the path a packet takes.
    *   `/tool torch interface=bridge-20`: To examine network traffic in real-time.
    *   `/ip dhcp-server lease print`: To view active DHCP leases

### 5. Verification and Testing Steps

1.  **Client IP Test:** Connect a device to the network and check if it gets an IP address from the configured pool using the `ipconfig` command in Windows or `ifconfig` on Linux and macOS.
2.  **Ping Test:** Ping the MikroTik router’s IP address (`29.46.113.1`) from a client and another IP address in the configured subnet from the router.
3.  **Torch Test:** Run `/tool torch interface=bridge-20` to see DHCP traffic during the IP assignment.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **IP Pools:** Can be used for many services, not just DHCP (e.g. for Hotspot, PPPoE). Pools can be named arbitrarily to identify them based on use case.
*   **Multiple DHCP Servers:** You can create several DHCP servers for different interfaces/VLANs.
*   **DHCP Option:** Options such as NTP, domain name, and custom options can be added for DHCP clients.
*   **Static DHCP Leases:** Specify IP addresses for certain MAC addresses, ensuring specific devices always get the same IP.
*   **Limitations:** Number of addresses in the pool. If the pool is too small, your router will run out of IPs to assign to your devices. There are limits on the number of IPs per pool depending on the device. You should refer to the documentation for your device.

### 7. MikroTik REST API Examples

Here are example REST API calls for managing IP pools. We'll assume you have enabled the API service:

**API Endpoint:** `/ip/pool`

**1. Get IP Pools:**
*   **Method:** `GET`
*   **Example (cURL):**
```bash
curl -u <user>:<password> -k -H "Content-Type: application/json" "https://<router-ip>/rest/ip/pool"
```
*   **Example Response:**
```json
[
  {
    ".id": "*1",
    "name": "dhcp_pool_20",
    "ranges": "29.46.113.100-29.46.113.200"
  }
]
```

**2. Create a New IP Pool:**
*   **Method:** `POST`
*   **Example (cURL):**
```bash
curl -u <user>:<password> -k -H "Content-Type: application/json" -d '{"name":"test_pool", "ranges":"192.168.10.10-192.168.10.20"}' "https://<router-ip>/rest/ip/pool"
```
*   **Example Response:**
```json
{
    ".id": "*2"
}
```
**3. Delete an existing IP Pool:**
*   **Method:** `DELETE`
*   **Example (cURL):**
```bash
curl -u <user>:<password> -k -H "Content-Type: application/json" -X DELETE "https://<router-ip>/rest/ip/pool/*2"
```
*   **Example Response:**
```json
{
    "message": "removed"
}
```
**NOTE:** Replace `<user>`, `<password>`, and `<router-ip>` with your actual credentials and router IP. These commands are intended to be illustrative.
**Note:** The REST API documentation for MikroTik is not always very verbose. It is often best to explore the API using the `print` functionality of the REST API. For example you could send a GET to `/ip` and `/ip/address`.

### 8. In-depth Explanations of Core Concepts

*   **IP Addressing (IPv4):** The foundation of network communication.  IP addresses are used to identify devices on a network. In our example we used CIDR notation (`/24` indicates a subnet mask of `255.255.255.0`).
*   **IP Pools:**  These are pre-defined ranges of IP addresses managed by RouterOS, typically used in conjunction with DHCP.
*   **IP Routing:**  The process of forwarding data packets across networks. MikroTik uses routing tables to determine where to send packets based on destination IP addresses.
*   **IP Settings:** Various settings such as IP forwarding, ICMP handling, and other parameters related to the IP layer.
*   **Bridging:** Creates a Layer 2 network, combining multiple interfaces into one logical interface, allowing all bridged interfaces to be on the same network (subnet) - in our case, `bridge-20`.
*   **Firewall:** Inspects network traffic, blocking or allowing packets based on predefined rules.
*   **DHCP:** Automatically assigns IP addresses to clients on a network.

### 9. Security Best Practices Specific to MikroTik Routers

*   **Strong Passwords:** Use strong, unique passwords for all user accounts.
*   **Service Security:** Only enable required services (like the API). Disable unused ones.
*   **Firewall Rules:** Implement strict firewall rules to allow only necessary traffic to your router and network.
*   **RouterOS Updates:** Keep RouterOS updated with the latest stable version to patch security vulnerabilities.
*   **Remote Access:** If remote access is necessary, use secure protocols (e.g., SSH, HTTPS).
*   **Winbox Access:** Restrict Winbox access to specific IP addresses.
*   **API Access:**  Secure the API by setting user passwords and restricting access to specific IP addresses.
*   **MAC Server** The MAC server allows remote access to the device via MAC address. Be careful of this service as it does not provide any sort of encryption. This can make the router vulnerable. It is best not to use the MAC Server functionality unless required, and even then, best practice would be to turn the feature off immediately after using it.
*   **RoMON** The RoMON feature allows remote configuration, and discovery of devices. Be very careful with RoMON if you enable it. If the router is compromised, RoMON may give access to additional network equipment. Make sure to always limit the network/ports RoMON can access. This is the same best practice as above. Only enable it if you need it and turn it off after usage.
*   **Certificates** - Use signed certs wherever possible for encrypted services, self-signed certs can lead to man in the middle attack if clients are not validating certificates properly.
*   **AAA** -  Make sure you have proper accounting for all remote access. You want to be able to track which user, is logging in and out. You can achieve this by setting up a AAA server like RADIUS.
*   **User/User Groups** Make sure to create groups for administration and give each admin their own user and password. If more than one person has the same password you are not auditing correctly.
*   **L3 Hardware Offloading** Make sure to understand the rules and limitations of hardware offloading. This can create a security hole as the hardware is doing the processing, and may skip firewall rules etc.
*   **MACsec** Should be used if possible for Layer 2 security.
*   **QoS** Understand how the QoS is applied on the device and how to prevent abuse by miscreants.
*   **Switch Chip Features** Understand the switch features of the device, and how to configure them safely.
*   **VLAN** VLANs should be used wherever possible. This is the best way to create network isolation.
*   **VXLAN** Should be used when you need Layer 2 access over Layer 3
*   **Firewall** Review your firewall rules to make sure only desired traffic is being allowed.
*   **IP Services** Review all running services to make sure they are needed. Disable all non essential services.
*   **HA Solutions** Make sure you secure all HA solutions as a compromised HA solution will give access to the entire network.
*   **MPLS** If MPLS is used. Make sure the routers are secure and configured properly.
*   **Network Management** Be careful about exposing management services to outside networks.
*   **Routing** Review routing protocols and routes carefully as any compromise on routing can lead to a compromise of the network.
*   **VPN** Understand all the VPN protocols and use the most secure one that applies. For example wireguard is generally more secure and easier to configure.
*   **Wired Connections** Check all wired connection for physical security.
*   **Wireless** Secure all wireless networks with strong passwords and encryption.
*   **IoT** Isolate all IOT devices on their own VLANS.
*   **Hardware** Physically secure the router.
*   **Diagnostics** Limit and control who can run diagnostics on the network.
*   **Extended Features** Review the security of all extended features, such as docker containers and smb.

### 10. Detailed Explanations and Configuration Examples for MikroTik Topics

Now, let's delve into the specifics of each topic:

**IP Addressing (IPv4 and IPv6)**

*   **IPv4:** We’ve already covered the basics. Remember that you must use subnet masks with IPv4.
    ```mikrotik
    /ip address add address=192.168.1.1/24 interface=ether1 comment="Example IPv4 Address"
    ```
*   **IPv6:** You must have an ISP which provides IPv6. Typically it would be either via DHCPv6 or manual IPv6.
    *   **Example of a DHCPv6 request:**
        ```mikrotik
          /ipv6 dhcp-client
          add interface=ether1 request=address,prefix use-peer-dns=yes
        ```
    *  **Example of a manual IPv6 address:**
        ```mikrotik
        /ipv6 address add address=2001:db8::1/64 interface=ether1
        ```

**IP Pools**

*   As discussed earlier, IP pools are fundamental to DHCP. You can create many IP pools for different interfaces.
    ```mikrotik
    /ip pool
    add name=pool_vlan10 ranges=10.10.10.100-10.10.10.200
    add name=pool_vlan20 ranges=10.20.20.100-10.20.20.200
    ```

**IP Routing**

*   **Static Routes:**  Manually define routes to specific networks.
    ```mikrotik
    /ip route
    add dst-address=10.0.0.0/24 gateway=192.168.1.254
    ```
*   **Dynamic Routing:**  Use routing protocols like OSPF, RIP, or BGP.
  *   **OSPF example**
        ```mikrotik
        /routing ospf instance
        add name=ospf1 router-id=10.10.10.1

        /routing ospf area
        add instance=ospf1 name=backbone-area
        
        /routing ospf network
        add area=backbone-area network=10.10.10.0/24
        add area=backbone-area network=10.20.20.0/24

        ```

**IP Settings**

*   Adjust settings like forwarding, ICMP handling, etc.
    ```mikrotik
    /ip settings set allow-fast-path=yes ip-forward=yes
    ```

**MAC Server**

*   Allows you to manage or view a device by MAC address.  This is unencrypted, and should be avoided if possible.
    ```mikrotik
    /tool mac-server
    set allowed-interface=ether1 enabled=no
    ```

**RoMON**

*   A remote monitoring system (usually used in a lab) to discover and manage other devices. Be careful to turn off when not needed.
    ```mikrotik
    /tool romon
    set enabled=no
    ```

**WinBox**

*  Winbox is the proprietary MikroTik GUI. It is a common tool used to manage Mikrotik routers. It has all functionality.
    * Make sure to always use the latest Winbox version.

**Certificates**

*   Used for encryption with HTTPS, IPsec, etc.
    ```mikrotik
    /certificate import file-name=my_cert.pem password="your_password"
    ```

**PPP AAA**

*   Authentication, Authorization, and Accounting for PPP connections. Usually used with RADIUS
    ```mikrotik
    /ppp aaa set use-radius=yes accounting=yes interim-update=60s
    ```
**RADIUS**

*   Centralized authentication for PPP, Hotspot, etc.
    ```mikrotik
    /radius
    add address=192.168.2.10 secret="radius_secret" service=ppp timeout=10
    ```

**User / User groups**

*   Create individual users and group them for permissions.
    ```mikrotik
    /user
    add name="admin_user" password="strongpassword" group=full
    /user group add name="vpn_user"
    /user add name="vpn1" password="strongvpnpassword" group=vpn_user
    ```

**Bridging and Switching**

*   Connect interfaces into a bridge.
    ```mikrotik
    /interface bridge
    add name=bridge-lan
    /interface bridge port
    add bridge=bridge-lan interface=ether1
    add bridge=bridge-lan interface=ether2
    ```

**MACVLAN**

* Creates virtual interfaces on top of physical interfaces using MAC address for segmentation.
    ```mikrotik
      /interface macvlan
        add interface=ether1 mac-address=02:02:02:02:02:02 name=macvlan1
        add interface=ether1 mac-address=03:03:03:03:03:03 name=macvlan2
    ```

**L3 Hardware Offloading**

* Offloads processing from the CPU to specialized hardware. Has limitations and can break firewall and other rules. Consult Mikrotik manual to see what features are supported on the specific device.
```mikrotik
 /interface ethernet set ether1 l3-hw-offloading=yes
```

**MACsec**

*   Layer 2 security based on encryption.
    ```mikrotik
    /interface macsec
    add name=macsec1 interface=ether1 mode=static cipher-suite=gcm-aes-256 key=00112233445566778899AABBCCDDEEFF00
    ```

**Quality of Service**

*   Prioritize traffic based on type, source, or destination.
    ```mikrotik
     /queue type add name="video_queue" kind=pcq pcq-rate=2M pcq-classifier=dst-address,dst-port
     /queue simple add target=192.168.1.0/24 name="Video_Queue" max-limit=1M queue=video_queue
    ```

**Switch Chip Features**

*   Advanced features in the switch chip on RouterBOARD devices (VLANs, port mirroring, etc). Requires access to the `switch` menu.
    ```mikrotik
       /switch vlan
       add vlan-id=20 ports=ether2,ether3
    ```
**VLAN**

*   Virtual LANs for network segmentation.
    ```mikrotik
    /interface vlan
    add name=vlan10 interface=bridge-lan vlan-id=10
    add name=vlan20 interface=bridge-lan vlan-id=20
    ```
**VXLAN**

*   Layer 2 overlay network over Layer 3.
    ```mikrotik
      /interface vxlan
      add name=vxlan1 vni=1000 interface=ether1 remote-address=10.10.10.2
    ```

**Firewall and Quality of Service**

*   **Connection Tracking:** Stateful inspection.
*   **Firewall:** Filters packets based on rules.
    ```mikrotik
    /ip firewall filter
    add chain=input protocol=tcp dst-port=22 action=accept comment="Allow SSH access"
    add chain=input action=drop comment="Drop all other"
    ```
*   **Packet Flow:** RouterOS packet processing order.
*   **Queues:** Manages bandwidth usage.
*   **Firewall and QoS Case Studies:** Implementing specific policies to manage traffic.
*   **Kid Control:** Example implementation, using a user group.
*   **UPnP:** Example implementation to allow devices to configure their own port forwards.
*   **NAT-PMP:** Alternative port mapping for some applications.

**IP Services (DHCP, DNS, SOCKS, Proxy)**

*   **DHCP Server:** As detailed earlier.
*   **DNS Server:** Caching and forwarding DNS server.
   ```mikrotik
     /ip dns
     set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8
   ```
*   **SOCKS Proxy:** Enable and configure SOCKS server to route traffic.
    ```mikrotik
    /ip socks set enabled=yes port=1080
    ```
*   **Web Proxy:** Enable and configure a web proxy to cache web traffic.
  ```mikrotik
   /ip proxy set enabled=yes cache-administrator=admin@example.com
  ```

**High Availability Solutions**

*   **Load Balancing:** Using multiple WAN links.
*   **Bonding:** Aggregating multiple interfaces into one logical interface for speed and redundancy.
    ```mikrotik
    /interface bonding add name=bond1 mode=802.3ad slaves=ether1,ether2
    ```
*   **HA Case Studies:** Examples of HA deployments.
*   **Multi-chassis Link Aggregation Group:** Combining links between switches.
*   **VRRP:** Router redundancy protocol.
    ```mikrotik
    /interface vrrp add interface=ether1 vrid=1 priority=200 password=password
    ```
*   **VRRP Configuration Examples:** Setting up VRRP between two routers.

**Mobile Networking**

*   **GPS:** Using a GPS module with the MikroTik router.
*   **LTE:** Configuring LTE interfaces and mobile networking.
    ```mikrotik
    /interface lte
     set 0 apn=your_apn user=your_user password=your_password
    ```
*   **PPP:** Configuring PPP connections.
*   **SMS:** Using SMS for notifications and remote management.
*   **Dual SIM Application:** Using dual SIM cards for redundancy or load balancing.

**Multi Protocol Label Switching - MPLS**

*   **MPLS Overview:** Basics of MPLS technology.
*   **MPLS MTU:** MTU considerations for MPLS.
*   **Forwarding and Label Bindings:** How MPLS labels are used.
*   **EXP bit and MPLS Queuing:** Prioritizing MPLS traffic.
*   **LDP:** Label Distribution Protocol.
*   **VPLS:** Virtual Private LAN Service.
*   **Traffic Eng:** Traffic engineering using MPLS.
*   **MPLS Reference:** Links to further reading.

**Network Management**

*   **ARP:** Address Resolution Protocol.
    ```mikrotik
      /ip arp add interface=ether1 address=10.10.10.1 mac-address=00:11:22:33:44:55
    ```
*   **Cloud:** Connecting to MikroTik's Cloud services.
*   **DHCP:** As detailed before.
*   **DNS:** As detailed before.
*   **SOCKS and Proxy:** As detailed before.
*   **OpenFlow:** Using OpenFlow for programmable networking.

**Routing**

*   **Routing Protocol Overview:** Introduction to routing protocols.
*   **Moving from ROSv6 to v7 with examples:** Migration guidance for routing configs.
*   **Routing Protocol Multi-core Support:** Using multi-core CPUs for faster routing.
*   **Policy Routing:** Routing based on criteria other than just destination.
    ```mikrotik
     /ip route rule add src-address=10.10.10.0/24 action=lookup-only-in-table table=ISP1
     /ip route add dst-address=0.0.0.0/0 gateway=192.168.100.1 routing-mark=ISP1
    ```
*   **VRF:** Virtual Routing and Forwarding.
    ```mikrotik
      /routing vrf add name=VRF1 interfaces=ether1 route-distinguisher=10:1
    ```
*   **OSPF, RIP, BGP:** Detailed configurations for each protocol.
*   **RPKI:** Resource Public Key Infrastructure for BGP security.
*   **Route Selection and Filters:** How routes are chosen and filtered.
*   **Multicast:** Sending traffic to multiple destinations.
*   **Routing Debugging Tools:** Using tools to diagnose routing problems.
*   **Routing Reference:** Links to detailed documentation.
*  **BFD** Bidirectional Forwarding Detection. To quickly detect if a link has gone down.
    ```mikrotik
      /routing bfd add interface=ether1 min-rx-interval=50ms min-tx-interval=50ms
    ```
* **IS-IS** Interior Gateway Protocol.
    ```mikrotik
        /routing isis instance add name=isis1 system-id=11.2222.3333.4444

        /routing isis interface
        add instance=isis1 interface=ether1
    ```

**System Information and Utilities**

*   **Clock:** Setting system time and date.
*   **Device-mode:** Routerboard configuration.
*   **E-mail:** Sending email notifications from the router.
    ```mikrotik
    /tool e-mail set address=email@example.com port=587 user=sender@example.com password="password" ssl=yes
    ```
*   **Fetch:** Downloading files over HTTP/HTTPS.
*   **Files:** Managing files on the router.
*   **Identity:** Setting the router's name.
    ```mikrotik
    /system identity set name="myrouter"
    ```
*   **Interface Lists:** Grouping interfaces.
    ```mikrotik
    /interface list add name="WAN"
    /interface list member add list=WAN interface=ether1
    ```
*   **Neighbor discovery:** Finding other network devices.
*   **Note:** Adding textual notes to router configurations.
*   **NTP:** Network Time Protocol.
    ```mikrotik
      /system ntp client set enabled=yes primary-ntp=pool.ntp.org
    ```
*   **Partitions:** Managing disk partitions on the router.
*   **Precision Time Protocol:** For precise clock synchronization.
*   **Scheduler:** Automating tasks.
    ```mikrotik
      /system scheduler add name=reset-stats on-event="/interface ethernet monitor ether1 once do={/interface ethernet reset-counters ether1}" start-time=10:00:00 interval=1d
    ```
*   **Services:** Enabling/disabling services.
    ```mikrotik
    /ip service set www disabled=yes
    ```
*   **TFTP:** Simple file transfer protocol.

**Virtual Private Networks**

*   **6to4:** IPv6 transition mechanism.
*   **EoIP:** Ethernet over IP tunneling.
    ```mikrotik
      /interface eoip add name=eoip1 tunnel-id=1 remote-address=192.168.10.1
    ```
*   **GRE:** Generic Routing Encapsulation tunneling.
    ```mikrotik
        /interface gre add name=gre1 local-address=192.168.10.1 remote-address=192.168.10.2
    ```
*   **IPIP:** IP over IP tunneling.
    ```mikrotik
        /interface ipip add name=ipip1 local-address=192.168.10.1 remote-address=192.168.10.2
    ```
*   **IPsec:** Securing network traffic using IPsec.
    ```mikrotik
        /ip ipsec peer add address=192.168.10.2 secret="your_secret"
        /ip ipsec proposal add name="myproposal" auth-algorithms=sha256 enc-algorithms=aes-256-cbc lifetime=8h
        /ip ipsec policy add peer=192.168.10.2  proposal=myproposal
    ```
*   **L2TP:** Layer 2 Tunneling Protocol.
*   **OpenVPN:** Open Source VPN protocol.
    ```mikrotik
        /interface ovpn-server server set enabled=yes
    ```
*   **PPPoE:** Point-to-Point Protocol over Ethernet.
    ```mikrotik
      /interface pppoe-client add user=username password=password interface=ether1
    ```
*   **PPTP:** Point-to-Point Tunneling Protocol (insecure, generally avoided)
*   **SSTP:** Secure Socket Tunneling Protocol.
*   **WireGuard:**  Modern, secure VPN protocol.
     ```mikrotik
        /interface wireguard add name=wireguard1 listen-port=51820 private-key="<private_key>"
        /interface wireguard peers add interface=wireguard1 allowed-address="10.10.10.0/24"  endpoint=192.168.10.2:51820  public-key="<public_key>"
        /ip address add address=10.10.10.1/24 interface=wireguard1
    ```
*   **ZeroTier:** Mesh networking solution.

**Wired Connections**

*   **Ethernet:** Basic Ethernet interface configuration.
*   **MikroTik wired interface compatibility:** Checking hardware compatibility for different interfaces.
*   **PWR Line:** Power Line Communications

**Wireless**

*   **WiFi:** Configuring basic wireless networks.
    ```mikrotik
    /interface wifi set 0 mode=ap-bridge ssid=my_wifi_ssid band=2ghz-b/g/n security-profile=default
    ```
*   **Wireless Interface:** General wireless settings.
*   **W60G:** 60 GHz wireless.
*   **CAPsMAN:** Centralized wireless management system.
*   **HWMPplus mesh:** Wireless mesh networking.
*   **Nv2:** Proprietary wireless protocol.
*   **Interworking Profiles:** Settings for seamless roaming between networks.
*   **Wireless Case Studies:** Examples of complex wireless deployments.
*   **Spectral scan** Can be used to diagnose interference on the wireless spectrum.

**Internet of Things**

*   **Bluetooth:** Using Bluetooth interface.
*   **GPIO:** General Purpose Input/Output
*   **Lora:** Low-power, wide-area wireless technology.
*   **MQTT:** Message Queuing Telemetry Transport.

**Hardware**

*   **Disks:** Managing disks for storage.
*   **Grounding:** Proper grounding of your RouterBOARD.
*   **LCD Touchscreen:** Using LCD touchscreens on RouterBOARDs.
*   **LEDs:** Setting the functionality of LEDs.
*   **MTU in RouterOS:** Maximum Transmission Unit settings.
*   **Peripherals:** Connecting USB and other peripherals.
*   **PoE-Out:** Using Power over Ethernet output.
*   **Ports:** Available ports on the RouterBOARD.
*   **Product Naming:** Understanding MikroTik product naming conventions.
*   **RouterBOARD:** Specific RouterBOARD models and features.
*   **USB Features:** Using USB storage and peripherals.

**Diagnostics, monitoring and troubleshooting**

*   **Bandwidth Test:** Testing network bandwidth.
    ```mikrotik
    /tool bandwidth-test address=192.168.10.2
    ```
*   **Detect Internet:** Tool to identify Internet connectivity.
*   **Dynamic DNS:** Updating Dynamic DNS records.
    ```mikrotik
        /ip ddns add interface=ether1 service=no-ip domain=yourdomain.ddns.net username=username password=password
    ```
*   **Graphing:**  Using graphing for network monitoring.
*   **Health:** System health monitoring.
*   **Interface stats and monitor-traffic:** Viewing traffic statistics.
    ```mikrotik
    /interface monitor-traffic ether1
    ```
*   **IP Scan:** Scanning for IPs on the network.
    ```mikrotik
        /tool ip-scan interface=ether1
    ```
*   **Log:** Viewing system logs.
*   **Netwatch:**  Monitoring network hosts.
     ```mikrotik
        /tool netwatch add host=8.8.8.8 interval=10s up-script="/log info message=\"8.8.8.8 is up\"" down-script="/log info message=\"8.8.8.8 is down\""
    ```
*   **Packet Sniffer:** Capturing network packets for analysis.
*   **Ping:** Testing network reachability.
*   **Profiler:** Analyzing system resource usage.
*   **Resource:** Checking system resource information.
*   **SNMP:** Simple Network Management Protocol.
    ```mikrotik
    /snmp set enabled=yes
    