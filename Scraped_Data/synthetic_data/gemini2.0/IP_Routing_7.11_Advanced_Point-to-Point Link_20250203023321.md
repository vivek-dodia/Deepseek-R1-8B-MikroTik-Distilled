Okay, let's dive into a comprehensive guide for configuring IP Routing on a MikroTik RouterOS 7.11 (or 6.48 and 7.x) device for a point-to-point link using a specific subnet and bridge interface. This documentation will cover all the aspects you've requested, including core concepts, security, and practical examples.

## 1. Configuration Scenario and Specific MikroTik Requirements

**Scenario:** We're setting up a point-to-point link, such as between two buildings or offices. We'll use a MikroTik router on each end to establish IP connectivity and allow devices on either side of the bridge to communicate with each other. The key requirement is to route traffic using a dedicated subnet across this link.

**Specific MikroTik Requirements:**

*   **RouterOS Version:** 7.11 (or 6.48, 7.x)
*   **Configuration Level:** Advanced
*   **Network Scale:** Point-to-Point Link
*   **Subnet:** 48.107.119.0/24
*   **Interface Name:** `bridge-46` (This is our dedicated bridge interface)

## 2. Step-by-Step MikroTik Implementation

Here’s the step-by-step implementation using both the CLI and Winbox, with detailed explanations.

### 2.1. CLI Implementation

**Step 1: Create the Bridge Interface (if it doesn't exist)**

```mikrotik
/interface bridge
add name=bridge-46
```

*   **Explanation:** This creates a new bridge interface named `bridge-46`. Bridge interfaces allow multiple physical or virtual interfaces to act as a single network segment, in this case, to facilitate the point-to-point link.

**Step 2: Add Interfaces to the Bridge**
    * This step will vary based on what interface is used to make the point to point link. It could be a physical ethernet or wireless interface.
    * For this example we will use eth2
```mikrotik
/interface bridge port
add bridge=bridge-46 interface=eth2
```

**Step 3: Assign an IP Address to the Bridge Interface**

```mikrotik
/ip address
add address=48.107.119.1/24 interface=bridge-46
```

*   **Explanation:** This command assigns the IP address `48.107.119.1` with a `/24` subnet mask to the bridge interface `bridge-46`. This address will serve as the gateway for other devices on this network. On the other end of the point-to-point link a different address in this subnet will need to be used. For example 48.107.119.2/24

**Step 4: Ensure IP Forwarding is Enabled**
   * Most often IP forwarding is enabled by default but in some instances it can be disabled, to be sure we will verify it and enable it if it is not.
```mikrotik
/ip settings
set forwarding=yes
```

*   **Explanation:** This command ensures that the router allows traffic to be forwarded between interfaces.

**Step 5: (Optional) Add an IP Route (If needed for accessing this subnet from a different network.)**
    * This step is not always necessary and depends on the requirements of the router. For a point to point link, it may not be needed. If a router does not know how to reach this subnet, a route will need to be added.
    * We will assume that the gateway to this router is 192.168.88.1
```mikrotik
/ip route
add dst-address=48.107.119.0/24 gateway=192.168.88.1
```

### 2.2. Winbox Implementation

1.  **Connect to your Router:** Open Winbox and connect to your MikroTik router.
2.  **Create the Bridge Interface:** Go to `Interfaces` -> `Bridge` tab. Click the `+` button, enter `bridge-46` in the "Name" field, and click `Apply` then `OK`.
3.  **Add interfaces to the Bridge Interface:** Go to `Interfaces` -> `Bridge` -> `Ports` tab. Click the `+` button, select `bridge-46` from the "Bridge" drop-down and the interface (e.g., `eth2`) from the "Interface" drop-down, and click `Apply` then `OK`.
4.  **Assign IP Address:** Go to `IP` -> `Addresses`. Click the `+` button. In the `Address` field, enter `48.107.119.1/24`. In the `Interface` drop-down, select `bridge-46`. Click `Apply` then `OK`.
5. **Ensure IP Forwarding is enabled:** Go to `IP` -> `Settings`. Check the box next to "Forwarding" and click `Apply` then `OK`.
6. **(Optional) Add an IP Route:** Go to `IP` -> `Routes`. Click the `+` button. In the "Dst. Address" field, enter `48.107.119.0/24`. In the "Gateway" field, enter `192.168.88.1` (or the correct gateway). Click `Apply` then `OK`.

## 3. Complete MikroTik CLI Configuration Commands

Here are the complete commands from the above steps in a single block:

```mikrotik
/interface bridge
add name=bridge-46

/interface bridge port
add bridge=bridge-46 interface=eth2

/ip address
add address=48.107.119.1/24 interface=bridge-46

/ip settings
set forwarding=yes

/ip route
add dst-address=48.107.119.0/24 gateway=192.168.88.1
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

### Common Pitfalls:

*   **Incorrect Subnet Mask:** Using a wrong subnet mask (e.g., /16 instead of /24) can cause IP address conflicts and routing issues.
*   **Interface Not Assigned to Bridge:** Forgetting to add the physical interfaces to the bridge will mean traffic cannot pass through the bridge.
*   **IP Forwarding Disabled:** If forwarding is not enabled, the router won't route traffic between interfaces.
*   **Firewall Blocking Traffic:** If a firewall rule is configured to block traffic on this bridge it will prevent the connection from working.
*   **Incorrect Gateway:** If a route needs to be added and the gateway is incorrect, this will lead to routing issues.
*   **MTU issues**: Mismatch of MTU between interfaces can cause connection issues. This will likely only cause an issue if a virtual tunnel is used such as a vlan or vpn.

### Troubleshooting:

1.  **Ping:** Use `ping 48.107.119.2` (or the IP address on the other end of your link) to verify basic connectivity.
    ```mikrotik
    /ping 48.107.119.2
    ```

    *   **Error Scenario:** If you receive "Host unreachable" or timeout errors, check IP addresses, bridge configuration, interfaces, and basic connectivity.

2.  **Traceroute:** Use `traceroute 48.107.119.2` to trace the path traffic is taking.
    ```mikrotik
    /tool traceroute 48.107.119.2
    ```

    *   **Error Scenario:** If the trace stops at the first hop (your router), you might have routing problems or firewall blocking it.
3.  **Torch:** Use `torch interface=bridge-46` to see real-time traffic.
    ```mikrotik
    /tool torch interface=bridge-46
    ```

    *   **Error Scenario:** If you don't see any traffic, check interface configuration, cable connections, or firewall.
4.  **Log:** Check system logs under `/system log` for any errors related to interfaces, IP addresses, or routing.
    ```mikrotik
    /system log print
    ```

    *   **Error Scenario:** Look for messages like "interface down", "address conflict", or "no route to host."
5. **Interface status:** In `Interface` window in Winbox, it is possible to see if an interface is enabled or not, the current status and if it is running. A red 'X' would indicate that the interface is not enabled.
6. **Interface Counters:** The `Interface` window in Winbox also displays traffic data. Using this it can be verified if packets are being sent and recieved on the link. This can help diagnose if there is a physical issue with the connection.

## 5. Verification and Testing Steps

1.  **Ping Test:** Ping the IP address of the device on the other end of the point-to-point link from the Mikrotik, and from any device on the local network attached to the bridge interface to verify network reachability.
2.  **Interface traffic:** Verify the interface counters in Winbox to see if data is moving across the interface.
3.  **Traceroute Test:** Use traceroute to confirm that the packets are going through the configured path and not bypassing the network.
4.  **Firewall Rule Verification:** Verify that a firewall rule is not blocking the traffic.
5.  **Connectivity Tests:** If connected to a larger network, test access to other network resources to ensure proper routing.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Bridging:** MikroTik's bridge functionality is powerful but has limitations like spanning-tree issues if not properly configured.
*   **Routing Protocols:** For more complex routing scenarios, MikroTik supports protocols like OSPF, BGP, and RIP.
*   **VRF (Virtual Routing and Forwarding):** VRF allows multiple routing tables on the same device. This could be useful if multiple independent networks are connected to the router.
*   **Policy-Based Routing (PBR):** PBR allows for more advanced routing decisions based on packet properties.

### Example using less common features:

* **MACVLAN** : MACVLAN allows multiple MAC addresses on a single interface. This is useful for hosting virtual machines on a single physical interface.
* **VLAN**: VLAN tags can be assigned to the bridge interface and allow more logical network segregation.

## 7. MikroTik REST API Examples

MikroTik API examples using MikroTik specific calls.
These examples assume that the API is enabled on the router and that you have authentication details. For demonstration, basic HTTP authentication is used. In production systems, use more secure authentication methods. The IP of the router used is 192.168.88.1

**Note:** MikroTik REST API calls require an API user to be created in the Mikrotik and that the API service is enabled. This will vary based on the network setup of the router and are not covered in this documentation.

### 7.1. Get Interface Bridge Configuration
*   **API Endpoint:** `https://192.168.88.1/rest/interface/bridge`
*   **Request Method:** `GET`
*   **Example CURL Command:**
```bash
curl -k -u apiuser:apipassword https://192.168.88.1/rest/interface/bridge
```
    *   **Expected Response (Example JSON):**
```json
[
  {
    ".id": "*1",
    "name": "bridge-46",
    "mtu": "1500",
    "actual-mtu": "1500",
    "l2mtu": "1598",
    "arp": "enabled",
    "max-message-size": "10240",
    "mac-address": "00:00:5E:00:53:01",
    "fast-forward": "yes",
    "allow-fast-path": "yes",
    "protocol-mode": "none",
    "priority": "32768",
    "multicast-router": "disabled",
    "igmp-snooping": "yes",
    "auto-isolate": "no",
    "vlan-filtering": "no"
  }
]
```

### 7.2. Create Interface Bridge
*   **API Endpoint:** `https://192.168.88.1/rest/interface/bridge`
*   **Request Method:** `POST`
*   **Example CURL Command:**
```bash
curl -k -u apiuser:apipassword -H "Content-Type: application/json" -X POST -d '{"name":"bridge-50"}' https://192.168.88.1/rest/interface/bridge
```

    *   **Example JSON payload:**
```json
    {"name":"bridge-50"}
```

    *   **Expected Response (Example JSON):**
```json
    {
    ".id":"*5"
    }
```

### 7.3. Delete Interface Bridge
*   **API Endpoint:** `https://192.168.88.1/rest/interface/bridge/*5`
*   **Request Method:** `DELETE`
*   **Example CURL Command:**
```bash
curl -k -u apiuser:apipassword -X DELETE https://192.168.88.1/rest/interface/bridge/*5
```

   *   **Expected Response (Empty Body with 204 status code):**
```
Empty Body and 204 Status Code
```

### 7.4. Add IP Address to interface

*   **API Endpoint:** `https://192.168.88.1/rest/ip/address`
*   **Request Method:** `POST`
*   **Example CURL Command:**
```bash
curl -k -u apiuser:apipassword -H "Content-Type: application/json" -X POST -d '{"address":"48.107.119.2/24", "interface": "bridge-46"}' https://192.168.88.1/rest/ip/address
```

   *   **Example JSON payload:**
```json
    {"address":"48.107.119.2/24", "interface": "bridge-46"}
```
   *   **Expected Response (Example JSON):**
```json
    {
    ".id":"*10"
    }
```

### 7.5. Delete IP Address from interface

*   **API Endpoint:** `https://192.168.88.1/rest/ip/address/*10`
*   **Request Method:** `DELETE`
*   **Example CURL Command:**
```bash
curl -k -u apiuser:apipassword -X DELETE https://192.168.88.1/rest/ip/address/*10
```

   *   **Expected Response (Empty Body with 204 status code):**
```
Empty Body and 204 Status Code
```
## 8. In-Depth Explanation of Core Concepts

*   **Bridging:** In MikroTik, a bridge is like a virtual switch. It allows multiple interfaces to act as a single Layer 2 network. All interfaces connected to a bridge are in the same broadcast domain. It does not inherently perform IP routing.
*   **Routing:** Routing is the process of determining the best path for a packet to travel from one network to another. MikroTik uses its routing table, which consists of static routes set by the user as well as dynamic routes learned from routing protocols, to make these decisions.
*   **Firewall:** MikroTik's firewall operates on Layers 3 and 4 of the OSI model. It examines traffic based on source and destination IP addresses, port numbers, protocols and other criteria. Firewall rules are applied to a traffic flow on a per interface basis.
*   **IP Addressing:** MikroTik supports both IPv4 and IPv6 addressing. Each interface has an assigned IP address and subnet. The subnet mask determines the network size and number of valid hosts.

## 9. Security Best Practices

*   **Strong Passwords:** Use strong, unique passwords for the router's user accounts.
*   **Restrict Access:** Limit access to the router's management interfaces using source IP filtering in the firewall.
*   **Disable Unused Services:** Disable unused services like the API or telnet.
*   **Update RouterOS:** Keep the RouterOS software updated to the latest version to patch security vulnerabilities.
*   **Firewall Rules:** Implement a strict firewall policy, allowing only necessary traffic.
*   **Secure API Access:** For API access, use HTTPS and secure authentication. Consider using certificate-based authentication.
*   **RoMON** RoMON allows layer 2 management of routers. This should be disabled if not needed because it is a security concern as it allows access without logging in.

## 10. Detailed Explanations and Configuration Examples

### 10.1. IP Addressing (IPv4 and IPv6)

*   **IPv4:**
    *   **Example:** `48.107.119.1/24`
    *   **Explanation:** Assigns IPv4 address `48.107.119.1` and a `/24` (255.255.255.0) subnet mask.
*   **IPv6:**
    *   **Example:** `2001:db8::1/64`
    *   **Explanation:** Assigns an IPv6 address and a `/64` prefix.
    *   **Configuration:**
```mikrotik
    /ipv6 address
    add address=2001:db8::1/64 interface=bridge-46
```

### 10.2. IP Pools

*   **Explanation:** IP pools are used for dynamic IP address assignment, particularly with DHCP.
*   **Example:**
```mikrotik
    /ip pool
    add name=dhcp-pool ranges=48.107.119.100-48.107.119.200
```
    *   **Explanation:** Creates a pool named `dhcp-pool` with address ranges `48.107.119.100-48.107.119.200`.

### 10.3. IP Routing

*   **Explanation:** Configures routes that determine where packets should be sent.
*   **Example:**
```mikrotik
    /ip route
    add dst-address=192.168.0.0/24 gateway=192.168.88.1
```
    *   **Explanation:** Adds a static route for network `192.168.0.0/24` via gateway `192.168.88.1`.

### 10.4. IP Settings

*   **Explanation:** Contains general IP settings, such as enabling or disabling IP forwarding.
*   **Example:**
```mikrotik
    /ip settings
    set forwarding=yes
```
    *   **Explanation:** Enables IP forwarding.

### 10.5. MAC Server

*   **Explanation:** Allows discovering MAC addresses on the network. Primarily used for management and troubleshooting.
*   **Configuration:**
```mikrotik
    /tool mac-server
    set allowed-interface-list=all
```
    *   **Explanation:** Enables the MAC server on all interfaces. Security warning, this should be enabled carefully and for specific interfaces if needed.

### 10.6. RoMON

*   **Explanation:** MikroTik's remote management protocol. Use carefully as it can be a security risk if used inappropriately.
*   **Configuration:**
```mikrotik
    /tool romon
    set enabled=yes
```
    *   **Explanation:** Enables RoMON. This should be disabled unless needed.

### 10.7. WinBox

*   **Explanation:** MikroTik's GUI configuration utility. Can be used to do all the tasks described in this documentation.
*   **Use:** Download from mikrotik website. Connect via mac address or IP.

### 10.8. Certificates

*   **Explanation:** Used for encrypted services like web interface and VPNs.
*   **Configuration:** Requires creation of the certificate and is beyond the scope of this document.

### 10.9. PPP AAA

*   **Explanation:** Authentication, authorization, and accounting for PPP connections.
*   **Configuration:** Uses RADIUS server to authenticate PPP users. Beyond the scope of this document.

### 10.10. RADIUS

*   **Explanation:** Centralized authentication server often used with PPP, wireless, and hotspot services.
*   **Configuration:**
```mikrotik
    /radius
    add address=192.168.88.2 secret=radiussecret service=ppp,login,hotspot
```
    *   **Explanation:** Configures RADIUS server at `192.168.88.2` with shared secret `radiussecret` for PPP, login, and hotspot services.

### 10.11. User / User Groups

*   **Explanation:** Manages router access and permissions.
*   **Configuration:**
```mikrotik
    /user group add name=admin policy=read,write,test,password
    /user add name=admin group=admin password=myadminpass
```
    *   **Explanation:** Creates a user group `admin` with full permissions and user `admin` with password `myadminpass`.

### 10.12. Bridging and Switching

*   **Explanation:** Layer 2 networking, connecting interfaces on the same broadcast domain.
*   **Configuration:**
```mikrotik
    /interface bridge
    add name=bridge-1
    /interface bridge port
    add bridge=bridge-1 interface=ether1
    add bridge=bridge-1 interface=ether2
```
    *   **Explanation:** Creates a bridge interface `bridge-1` and adds `ether1` and `ether2` to it.

### 10.13. MACVLAN

*   **Explanation:** Allows multiple MAC addresses on a single interface. Useful for virtualized environments.
*   **Configuration:**
```mikrotik
    /interface macvlan
    add interface=ether2 mac-address=00:00:5E:00:00:01 name=macvlan-1
    add interface=ether2 mac-address=00:00:5E:00:00:02 name=macvlan-2
```
   *   **Explanation:** Adds macvlan interfaces macvlan-1 and macvlan-2 on interface ether2 with specific MAC addresses.

### 10.14. L3 Hardware Offloading

*   **Explanation:** Offloads L3 processing to the switch chip to improve performance. Can be enabled if your hardware supports it.
*  **Configuration:**
```mikrotik
  /interface ethernet
  set ether1 l3-hw-offloading=yes
```
    *  **Explanation:** Enables hardware offloading on interface ether1. This is only supported on some MikroTik devices.

### 10.15. MACsec

*   **Explanation:** Layer 2 encryption. Useful for securing wired networks. Configuration is not covered in this documentation.
*   **Use:** Not commonly used and will add complexity to the network.

### 10.16. Quality of Service

*   **Explanation:** Manages bandwidth allocation and prioritization.
*   **Configuration:** Requires configuring mangle rules, queue trees and is not covered in this documentation.

### 10.17. Switch Chip Features

*   **Explanation:** Allows configuring switch chip specific features such as VLAN tagging.
*   **Configuration:** Depends on the MikroTik hardware used. Configured from `switch` in Winbox or `/interface ethernet switch` on the command line.

### 10.18. VLAN

*   **Explanation:** Creates isolated logical networks on the same physical network.
*   **Configuration:**
```mikrotik
   /interface vlan
   add interface=bridge-46 name=vlan-100 vlan-id=100
```
    *   **Explanation:** Adds a vlan interface tagged with ID 100 to bridge-46.

### 10.19. VXLAN

*   **Explanation:** Layer 2 over Layer 3 tunneling protocol. Useful for network virtualization. Configuration is not covered in this documentation.
*   **Use:** Not commonly used.

### 10.20. Firewall and Quality of Service

*   **Explanation:** Controls network access and bandwidth usage.
*   **Configuration:**
    *   **Connection Tracking:** Keep track of connections for easier firewall management.
    *   **Firewall:** `ip firewall filter` to control traffic, `nat` to translate addresses.
    *   **Packet Flow in RouterOS:** Incoming packets are processed, routed, and may be dropped or forwarded according to configurations.
    *   **Queues:** `queue tree` to prioritize different types of traffic.
    *   **Firewall and QoS Case Studies:** Can use layer7 protocols and mangle to mark different types of traffic.
    *   **Kid Control:** Can be achieved via parental control DNS, time based firewall rules and url filtering.
    *   **UPnP:** Can be enabled for ease of use, but not recommended in secure environments.
    *   **NAT-PMP:** Alternative to UPnP

### 10.21. IP Services (DHCP, DNS, SOCKS, Proxy)

*   **DHCP Server:** Assigns IP addresses to clients.
```mikrotik
        /ip dhcp-server
        add address-pool=dhcp-pool interface=bridge-46 name=dhcp1
        /ip dhcp-server network
        add address=48.107.119.0/24 dns-server=8.8.8.8 gateway=48.107.119.1
```

*   **DNS Server:** Provides name resolution.
```mikrotik
    /ip dns
    set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
```

*   **SOCKS Proxy:** Allows secure connections. Configuration not covered in this documentation.
*   **Proxy:** Allows caching for faster web browsing. Configuration not covered in this documentation.

### 10.22. High Availability Solutions

*   **Load Balancing:** Spreads traffic over multiple links. Requires configuration of routing.
*   **Bonding:** Creates a single logical interface from multiple physical links.
```mikrotik
        /interface bonding
        add mode=802.3ad name=bond1 slaves=ether1,ether2
```
*   **Bonding Examples:**
    * **802.3ad** A standard link aggregation protocol. Requires that the switch and the router are setup to use this protocol.
*   **HA Case Studies:** VRRP can be used for HA.
*   **Multi-chassis Link Aggregation Group:** Aggregates ports from multiple routers.
*   **VRRP (Virtual Router Redundancy Protocol):** Creates redundant gateways.
```mikrotik
        /interface vrrp
        add interface=bridge-46 name=vrrp1 priority=100 vrid=1
        /ip address
        add address=48.107.119.2/24 interface=vrrp1
```
*   **VRRP Configuration Examples:**  A priority of 100 indicates that this router will be the master, while a router with a lower priority is a backup.

### 10.23. Mobile Networking

*   **GPS:** For location-based services.
*   **LTE:** For cellular internet access.
*   **PPP:** Point to Point Protocol. Often used in conjunction with cellular connections.
*   **SMS:** Short Messaging Service.
*   **Dual SIM Application:** Connect to multiple carriers for failover or load balancing.

### 10.24. Multi Protocol Label Switching - MPLS

*   **MPLS Overview:** A technology for speeding up traffic forwarding.
*   **MPLS MTU:** MTU configurations for MPLS.
*   **Forwarding and Label Bindings:** How labels are assigned and traffic is forwarded.
*   **EXP bit and MPLS Queuing:** MPLS uses EXP bits for QoS.
*   **LDP:** Label Distribution Protocol.
*   **VPLS:** Virtual Private LAN Service.
*   **Traffic Eng:** MPLS traffic engineering.
*   **MPLS Reference:** Links to more documentation. Not covered in this document.

### 10.25. Network Management

*   **ARP:** Address Resolution Protocol.
*   **Cloud:** MikroTik cloud services for management.
*   **DHCP:** Server/Client configurations.
*   **DNS:** Configuration of DNS services.
*   **SOCKS:** Server configurations.
*   **Proxy:** Server configurations.
*   **Openflow:** SDN protocol.

### 10.26. Routing

*   **Routing Protocol Overview:** Types of routing protocols and their use cases.
*   **Moving from ROSv6 to v7 with examples:** Changes in routing in v7.
*   **Routing Protocol Multi-core Support:** Use of multi-core processors to improve routing.
*   **Policy Routing:** Routing based on certain packet properties.
*   **Virtual Routing and Forwarding - VRF:** Allows multiple routing tables.
*   **OSPF:** Open Shortest Path First routing protocol.
```mikrotik
        /routing ospf instance
        add disabled=no name=ospf-1 router-id=48.107.119.1
        /routing ospf network
        add area=backbone network=48.107.119.0/24
```
*   **RIP:** Routing Information Protocol.
*   **BGP:** Border Gateway Protocol.
*   **RPKI:** Route Public Key Infrastructure.
*   **Route Selection and Filters:** How routes are selected and filtered.
*   **Multicast:** Routing of multicast traffic.
*   **Routing Debugging Tools:** Tools for troubleshooting routing.
*   **Routing Reference:** Links to more documentation.
*   **BFD:** Bidirectional Forwarding Detection.
*   **IS-IS:** Intermediate System to Intermediate System.

### 10.27. System Information and Utilities

*   **Clock:** System clock settings.
*   **Device-mode:** Router mode or switch mode.
*   **E-mail:** Router can send email messages.
*   **Fetch:** Downloads resources from the internet.
*   **Files:** Router file system.
*   **Identity:** Sets the router name.
*   **Interface Lists:** Allows grouping interfaces.
*   **Neighbor discovery:** Tools to discover other devices on the network.
*   **Note:** Allows user to add notes to the router configurations.
*   **NTP:** Network Time Protocol.
*   **Partitions:** Disk management.
*   **Precision Time Protocol:** PTP for time synchronization.
*   **Scheduler:** Automate tasks.
*   **Services:** Enables/Disables services on the router.
*   **TFTP:** Trivial File Transfer Protocol server.

### 10.28. Virtual Private Networks

*   **6to4:** IPv6 transition protocol.
*   **EoIP:** Ethernet over IP Tunneling.
*   **GRE:** Generic Routing Encapsulation.
*   **IPIP:** IP in IP Tunneling.
*   **IPsec:** IP Security VPN protocol.
*   **L2TP:** Layer 2 Tunneling Protocol.
*   **OpenVPN:** Open source VPN software.
*   **PPPoE:** Point to Point Protocol over Ethernet.
*   **PPTP:** Point to Point Tunneling Protocol.
*   **SSTP:** Secure Socket Tunneling Protocol.
*   **WireGuard:** Modern VPN protocol.
```mikrotik
        /interface wireguard
        add listen-port=51820 name=wg1
        /interface wireguard peers
        add allowed-address=48.107.119.2/32 endpoint-address=192.168.88.2 endpoint-port=51820 interface=wg1 persistent-keepalive=25 public-key="publickey"
        /ip address
        add address=48.107.119.1/24 interface=wg1
```
*   **ZeroTier:** Allows creation of virtual LANs.

### 10.29. Wired Connections

*   **Ethernet:** Wired connections and configuration.
*   **MikroTik wired interface compatibility:** Overview of which devices support certain Ethernet standards.
*   **PWR Line:** Power Line Communication technology.

### 10.30. Wireless

*   **WiFi:** Wireless interface and settings.
*   **Wireless Interface:** Configuration of wireless interfaces.
*   **W60G:** 60 GHz wireless technology.
*   **CAPsMAN:** Centralized wireless configuration manager.
*   **HWMPplus mesh:** Wireless mesh networking.
*   **Nv2:** Proprietary MikroTik wireless protocol.
*   **Interworking Profiles:** Wireless roaming standards.
*   **Wireless Case Studies:** Examples of complex wireless configurations.
*   **Spectral scan:** Tools to analyze the wireless spectrum.

### 10.31. Internet of Things

*   **Bluetooth:** Bluetooth support.
*   **GPIO:** General purpose input/output ports.
*   **Lora:** Long Range radio communication.
*   **MQTT:** Message Queuing Telemetry Transport for IoT.

### 10.32. Hardware

*   **Disks:** Storage on the router.
*   **Grounding:** Importance of grounding MikroTik equipment.
*   **LCD Touchscreen:** Configuration for LCD displays.
*   **LEDs:** Control LED behavior.
*   **MTU in RouterOS:** Maximum transmission unit.
*   **Peripherals:** USB devices.
*   **PoE-Out:** Power over Ethernet output.
*   **Ports:** Physical ports on the router.
*   **Product Naming:** MikroTik product naming convention.
*   **RouterBOARD:** MikroTik hardware platform.
*   **USB Features:** USB port functionality.

### 10.33. Diagnostics, monitoring and troubleshooting

*   **Bandwidth Test:** Tests the throughput of a connection.
```mikrotik
    /tool bandwidth-test address=48.107.119.2 user=test password=test
```
*   **Detect Internet:** Checks if the router has internet connectivity.
*   **Dynamic DNS:** Allows the router to update DNS records with dynamic IPs.
*   **Graphing:** Router resource graphs.
*   **Health:** Monitor device hardware status.
*   **Interface stats and monitor-traffic:** Displays real-time traffic on interfaces.
*   **IP Scan:** Scans the network for devices.
*   **Log:** Router logs.
*   **Netwatch:** Monitors network resources.
*   **Packet Sniffer:** Captures network packets for analysis.
*   **Ping:** Tests network connectivity.
*   **Profiler:** Displays router resource usage.
*   **Resource:** System resource information.
*   **SNMP:** Simple Network Management Protocol.
*   **Speed Test:** Test the internet speed.
*   **S-RJ10 general guidance:** Guidance on using S-RJ10 interfaces.
*   **Torch:** Real-time traffic analysis tool.
*   **Traceroute:** Tracks the route of packets across networks.
*   **Traffic Flow:** Traffic flow analysis.
*   **Traffic Generator:** Generates synthetic traffic.
*   **Watchdog:** Automatically reboots the router.

### 10.34