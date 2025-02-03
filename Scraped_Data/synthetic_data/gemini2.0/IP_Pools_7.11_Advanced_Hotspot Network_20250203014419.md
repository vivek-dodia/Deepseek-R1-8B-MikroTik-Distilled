Okay, let's dive deep into configuring IP Pools on a MikroTik RouterOS 7.11 device for a hotspot network scenario using a /24 subnet, alongside detailed explanations of related RouterOS features. This will be an extensive guide.

## 1. Comprehensive Configuration Scenario and MikroTik Requirements

**Scenario:** We are setting up a hotspot network using a MikroTik router. Clients will connect to this hotspot and receive IP addresses from a specific pool. The network will utilize the subnet `104.235.235.0/24`, and clients will be bridged onto `bridge-5`. The IP pool will serve DHCP for this bridge interface.

**MikroTik Requirements:**

*   MikroTik RouterOS version 7.11 (or 7.x compatible).
*   A configured `bridge-5` interface (we'll assume this exists, but we will include bridging configuration).
*   Basic network configuration (we'll focus on IP pools).
*   Understanding of subnetting and IP addressing.
*   Client devices that will connect to the hotspot.

## 2. Step-by-Step MikroTik Implementation

### Using Winbox:

1.  **Open Winbox** and connect to your MikroTik router.
2.  **Create the IP Pool:**
    *   Go to *IP > Pool*.
    *   Click the "+" button to add a new IP Pool.
    *   In the "Name" field, enter `hotspot-pool`.
    *   In the "Ranges" field, enter `104.235.235.2-104.235.235.254` (or adjust the range as needed).
    *   Click "Apply" and "OK".
3.  **Create the IP Address:**
    *   Go to *IP > Addresses*.
    *   Click the "+" button to add a new IP address.
    *   In the "Address" field, enter `104.235.235.1/24`.
    *   In the "Interface" dropdown, select `bridge-5`.
    *   Click "Apply" and "OK".
4.  **Configure DHCP Server:**
     * Go to *IP > DHCP Server*.
     * Click on the "+" button.
     * In the "Name" field, enter `hotspot-dhcp-server`.
     * In the "Interface" dropdown, select `bridge-5`.
     * Click "Apply" and then go to the "Network" tab.
     * Click the "+" button, in the "Address" field, enter `104.235.235.0/24`, in "Gateway" field enter `104.235.235.1`, "DNS Server" enter `8.8.8.8,8.8.4.4`, "Domain" enter `hotspot.local`, "Lease time" enter `1d`.
     * Click "Apply" and "OK".
     * Now on the DHCP server tab, click the DHCP server you created and select "Leases" to check currently assigned IP's.

### Using CLI:

```mikrotik
# Create the IP Pool
/ip pool add name=hotspot-pool ranges=104.235.235.2-104.235.235.254

# Create the IP Address on bridge-5
/ip address add address=104.235.235.1/24 interface=bridge-5

# Create the DHCP Server
/ip dhcp-server add name=hotspot-dhcp-server interface=bridge-5 address-pool=hotspot-pool

# Configure DHCP Server Network
/ip dhcp-server network add address=104.235.235.0/24 gateway=104.235.235.1 dns-server=8.8.8.8,8.8.4.4 domain=hotspot.local lease-time=1d

# Enable the dhcp server
/ip dhcp-server enable hotspot-dhcp-server

# Optional - add bridge
/interface bridge add name=bridge-5
/interface bridge port add bridge=bridge-5 interface=ether2
/interface bridge port add bridge=bridge-5 interface=wlan1
```

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
# Create the IP Pool:
/ip pool add name=hotspot-pool ranges=104.235.235.2-104.235.235.254

# Explanation:
#   name:  The name of the IP pool (hotspot-pool).
#   ranges: The range of IP addresses this pool will distribute (104.235.235.2 to 104.235.235.254).

# Add an IP address to an interface:
/ip address add address=104.235.235.1/24 interface=bridge-5

# Explanation:
#   address: The IP address and subnet mask to be assigned to the interface (104.235.235.1/24).
#   interface: The interface to which the IP address will be assigned (bridge-5).

# Add a DHCP Server:
/ip dhcp-server add name=hotspot-dhcp-server interface=bridge-5 address-pool=hotspot-pool

# Explanation:
#   name: The name of the DHCP server (hotspot-dhcp-server).
#   interface: The interface on which the DHCP server will listen for requests (bridge-5).
#   address-pool: The IP pool from which the DHCP server will assign IP addresses (hotspot-pool).

# Add a DHCP Network:
/ip dhcp-server network add address=104.235.235.0/24 gateway=104.235.235.1 dns-server=8.8.8.8,8.8.4.4 domain=hotspot.local lease-time=1d

# Explanation:
#    address: The subnet of this network (104.235.235.0/24).
#    gateway: The IP address of the gateway for this network (104.235.235.1).
#    dns-server: DNS server(s) for DHCP clients (8.8.8.8, 8.8.4.4)
#    domain: Domain for dhcp client (hotspot.local)
#    lease-time:  DHCP lease time (1d).

# Enable dhcp server
/ip dhcp-server enable hotspot-dhcp-server

# Add a bridge (optional)
/interface bridge add name=bridge-5
/interface bridge port add bridge=bridge-5 interface=ether2
/interface bridge port add bridge=bridge-5 interface=wlan1

# Explanation
# The first command adds a bridge interface, the following two commands add physical interfaces to the bridge.
```

## 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

*   **Issue:** Clients not getting IP addresses.
    *   **Troubleshooting:**
        *   Verify that the bridge interface `bridge-5` is active.
        *   Check the DHCP Server is enabled `/ip dhcp-server print`.
        *   Verify that the DHCP Server is enabled `/ip dhcp-server enable hotspot-dhcp-server`.
        *   Check the `address` range is within the pool.
        *   Verify that the DHCP network is correct.
        *   Use `torch interface=bridge-5` to see if DHCP requests are reaching the router and if it is responding.
        *   Check the `/ip dhcp-server lease print` command if any leases have been issued.
        *   Check if the interfaces are in the bridge.
        *   Check the firewall for any blocking rules
        *   Review logs using `/system logging print` and `/system logging action print` commands for any errors.
    *   **Error Scenario:** DHCP server logs show "no more addresses to give." This means your pool is exhausted or that clients are holding their leases without disconnecting.

*   **Issue:** IP address conflicts.
    *   **Troubleshooting:** Ensure that no other devices on your network have manually configured IP addresses within the DHCP pool.
    *   **Error Scenario:** DHCP clients are unable to connect to the network because of address conflict, often with a message such as "duplicate IP detected".

*   **Issue:** DNS resolution problems.
    *   **Troubleshooting:**  Make sure that the `dns-server` settings in the DHCP network are correct and accessible.
    *   **Error Scenario:** Clients get an IP address but can't reach websites because of missing DNS configuration.

**Diagnostic Tools:**

*   **`ping`:** To check basic connectivity. Example: `ping 104.235.235.1` (ping the gateway).
*   **`traceroute`:** To see the path taken by packets. Example: `traceroute 8.8.8.8`.
*   **`torch`:** Real-time traffic analyzer. Example: `torch interface=bridge-5`.
*   **`/log print`:** Check router logs for errors or warnings. Example: `/log print where topics~"dhcp"`.

## 5. Verification and Testing Steps

1.  **Connect Client Devices:** Connect several clients (laptops, phones) to the `bridge-5` interface (or the interfaces bridged to it).
2.  **Check IP Assignments:** On the clients, check that they have obtained IP addresses within the `104.235.235.0/24` subnet (104.235.235.2 to 104.235.235.254).
3.  **Ping the Gateway:** Verify that clients can ping the gateway IP address (`104.235.235.1`).
4.  **Access Internet:** If applicable, verify that clients can reach the internet and resolve domain names (e.g., `ping google.com`).
5.  **Check DHCP Leases:** Use `/ip dhcp-server lease print` to see assigned leases and ensure no address conflicts occur.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Address Lists:** You can use IP pools in conjunction with address lists for firewall rules or QoS.  For example, create an address list named `hotspot-clients` and configure it to match the DHCP server's leases.
```mikrotik
/ip firewall address-list add address=104.235.235.0/24 list=hotspot-clients
```
*   **Multiple IP Pools:** RouterOS allows multiple pools to be configured for different subnets or interfaces. This enables flexible address allocation in larger networks.
*   **Lease Binding:** You can bind IP addresses to specific MAC addresses to give clients the same IP address every time.
*   **Rate Limiting:** Use RouterOS's queue features to control the bandwidth allocated to clients based on their IP addresses or DHCP leases.
*   **Limitations:** Very large pools (e.g., /16) might become unwieldy to manage, especially in very dynamic network scenarios.
*   **Less Common Features:**
    * **DHCP options:** You can configure DHCP options to distribute more specific information to clients (e.g., NTP servers, custom DNS servers).
    * **DHCP Server Scripting:**  You can use the `on-event` scripting feature of the DHCP Server to run custom scripts on lease acquisition and expiration.

## 7. MikroTik REST API Examples

**API Endpoint:** `/ip/pool`

**Get all IP pools:**

*   **Method:** `GET`
*   **Endpoint:** `/ip/pool`
*   **Example `curl` command:**
    ```bash
    curl -k -u admin:your_password -H "Content-Type: application/json" https://192.168.88.1/rest/ip/pool
    ```
* **Example JSON Response:**
    ```json
    [
        {
          ".id": "*2",
          "name": "hotspot-pool",
          "ranges": "104.235.235.2-104.235.235.254"
        }
    ]
    ```

**Create a new IP pool:**

*   **Method:** `POST`
*   **Endpoint:** `/ip/pool`
*   **JSON Payload:**
    ```json
    {
      "name": "test-pool",
      "ranges": "192.168.200.2-192.168.200.254"
    }
    ```
*   **Example `curl` command:**
    ```bash
    curl -k -u admin:your_password -X POST -H "Content-Type: application/json" -d '{"name": "test-pool","ranges":"192.168.200.2-192.168.200.254"}' https://192.168.88.1/rest/ip/pool
    ```
*   **Expected Response (201 Created):**
    ```json
    {
     ".id":"*3",
     "name":"test-pool",
     "ranges":"192.168.200.2-192.168.200.254"
    }
    ```

**Get single IP Pool by ID:**

*   **Method:** `GET`
*   **Endpoint:** `/ip/pool/*2` (example getting pool with id *2)
*   **Example `curl` command:**
    ```bash
    curl -k -u admin:your_password -H "Content-Type: application/json" https://192.168.88.1/rest/ip/pool/*2
    ```

**Delete an IP pool:**

*   **Method:** `DELETE`
*   **Endpoint:** `/ip/pool/*3` (example getting pool with id *3)
*   **Example `curl` command:**
    ```bash
    curl -k -u admin:your_password -X DELETE -H "Content-Type: application/json" https://192.168.88.1/rest/ip/pool/*3
    ```
*   **Expected Response (204 No Content):**

## 8. In-Depth Explanations of Core Concepts

*   **Bridging:** Bridging is a Layer 2 mechanism that combines multiple interfaces into a single logical interface. This allows devices on different interfaces to communicate as if they are on the same network segment.
   * `bridge-5` in our case, connects all clients together logically on the same subnet. We are using a bridge in this case to allow wireless devices connected on `wlan1` and wired devices connected on `ether2` to obtain IP addresses from our IP Pool.

*   **Routing:** While not explicitly configured in this pool setup (we’re in the same subnet, so no routing needed),  routing is used to direct network traffic between different subnets.  When packets leave the `bridge-5` subnet, the router's IP address on `bridge-5` is used as the default gateway for the clients, so the router can route traffic to other networks and to the internet.

*   **Firewall:**  The firewall is crucial for security. It can be used to filter traffic based on IP addresses, ports, protocols, and more. Using IP Pools (and especially Address Lists) makes it easy to create rules that apply to all the devices using a certain IP pool.  For example, you can create a firewall rule that blocks all internet traffic from the `hotspot-pool` if necessary (very bad idea for a Hotspot, but possible).

*   **IP Addressing:** IP addresses are used to identify devices on a network. A subnet mask defines which part of an IP address refers to the network and which part refers to the host. Our example uses a /24, which means the first three octets are the network, and the last octet is the host.

*   **IP Pools:** IP pools are a set of IP addresses that the router can dynamically assign to network devices using DHCP. DHCP assigns an IP address to clients, a subnet mask, the gateway for traffic to exit the subnet, the DNS servers for name resolution, a domain and a lease time for the IP address before it must be renewed.

## 9. Security Best Practices

*   **Strong Passwords:** Ensure that the MikroTik router has a strong administrator password.
*   **Disable Default Services:**  Disable any services that are not necessary, such as Telnet and SSH, unless required.
*   **Firewall Rules:** Implement firewall rules to block unnecessary incoming traffic to the router and the network.
*   **Regular Updates:** Keep your MikroTik RouterOS software updated.
*   **Access Control:** Limit access to the router to specific IP addresses or networks (e.g., use `winbox-mac-address` or `allow-address` properties in `/ip service`).
*   **HTTPS for API:** Always use HTTPS for the RouterOS API.
*   **RADIUS:** For advanced hotspot security and user control, utilize RADIUS for authentication and authorization (will be covered later)

## 10. Detailed Explanations and Configuration Examples for RouterOS Topics

(This is a large section, so let's start with detailed explanations of some key topics, and we'll build on this in future iterations)

### IP Addressing (IPv4 and IPv6)
*   **IPv4:** IPv4 addresses are 32-bit numbers, generally represented in dot-decimal notation (e.g., 192.168.1.1). They are used to uniquely identify a device on a network.
    *   **Configuration:**  `ip address add address=192.168.1.1/24 interface=ether1` sets a static IPv4 address on `ether1`.
    *   **Private vs Public:** Private IPs (e.g., `192.168.0.0/16`, `10.0.0.0/8`) are used in local networks, while Public IPs are used on the internet.
    *   **Subnetting:** Dividing a network into smaller subnets using subnet masks (/24, /16, etc).
*   **IPv6:** IPv6 addresses are 128-bit addresses, represented in hexadecimal notation (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
    *   **Configuration:** `ipv6 address add address=2001:db8::1/64 interface=ether1` sets a static IPv6 address on `ether1`.
    *   **Stateless Address Autoconfiguration (SLAAC):** IPv6 devices can automatically configure their addresses using router advertisements.
    *   **Privacy Extensions:**  Temporary addresses that change frequently to improve privacy (not enabled by default on RouterOS).

### IP Pools
*   **Concept:** A range of IP addresses used for dynamic assignment, usually by a DHCP server.
*   **Configuration:**
    *   `ip pool add name=my-pool ranges=192.168.2.10-192.168.2.200` creates an IPv4 pool.
    *   `ip pool add name=ipv6-pool ranges=2001:db8:100::100-2001:db8:100::200` creates an IPv6 pool.
*   **Use cases:** DHCP servers, PPP servers (for IP allocation to PPP clients), address lists for filtering traffic.
*   **Management:** Can be managed via command line or Winbox GUI.

### IP Routing
*   **Concept:** The process of selecting a path for network traffic to reach its destination.
*   **Static Routing:** Manual configuration of routing paths, like setting a default gateway.
    *   `ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1` is a default route to the internet.
*   **Dynamic Routing:** Using protocols such as OSPF, RIP, or BGP to learn routing information dynamically.
    *   OSPF is used in enterprise environments for its rapid convergence and cost-based routing.
    *   BGP is used for inter-domain routing on the Internet (e.g., between ISPs).
*   **Policy Routing:** Routing based on different criteria beyond destination IP address (e.g., source IP, packet size, or even an application).
*   **Virtual Routing and Forwarding (VRF):** Allows you to create independent routing tables on the same router to separate networks.

### IP Settings
*   **Concept:** Global settings that influence how IP works on the router.
*   **IP Forwarding:** `ip settings set ip-forward=yes` enables IP forwarding (needed to act as a router).
*   **Allow Fast Path:** `ip settings set allow-fast-path=yes` enables faster packet processing for some specific scenarios, bypassing more resource-intensive processing steps.
*   **ICMP Settings:** Control how the router handles ICMP messages (ping, etc.)
*   **Source Validation:**  `ip settings set rp-filter=loose` helps prevent spoofed IP addresses but might break some applications
    * `rp-filter=strict`: The source address must match the network interface the packet arrived on.

### MAC Server
*   **Concept:** A service that allows clients to access the router using MAC addresses in order to set the router's IP address. Primarily used for initial router configuration or when a router does not have a static address.
*   **Configuration:**
    *   `tool mac-server set enabled=yes` enables the MAC server
    *   `tool mac-server set allowed-interface=all` allows access via all interfaces.

### RoMON
*   **Concept:** Router Management Overlay Network. A MikroTik-specific technology for out-of-band management. It creates a logical network over Layer 2 for router discovery and management without relying on IP addresses.
*   **Configuration:**
    *   `romon set enabled=yes` Enables RoMON on the router.
    *   `romon set secret=my-secret` sets a shared secret for RoMON.
*   **Use case:** Useful for managing remote routers in situations where the IP network is down or inaccessible.
*   **Limitations:** RoMON is limited to MikroTik devices and may not be as flexible or widely supported as other remote access methods.

### WinBox
*   **Concept:** A proprietary GUI application used to manage MikroTik routers.
*   **Use:** Provides a user-friendly way to configure and monitor router settings, including interfaces, firewall rules, and IP settings.
*   **Limitations:** Available for Windows only (officially). There are some unofficial cross-platform solutions.

### Certificates
*   **Concept:** Digital certificates used to establish secure connections over HTTPS, TLS, and other protocols.
*   **Configuration:**
    *   RouterOS can generate self-signed certificates or import certificates from a trusted CA.
    *   `certificate add name=my-cert common-name="router.local"` creates a self-signed certificate.
*   **Use:** Essential for securing the router's web interface, API, and VPN connections.
*   **Security:** Ensure that private keys are protected and not exposed. Use strong passwords for any protected keys.

### PPP AAA
*   **Concept:** Point-to-Point Protocol Authentication, Authorization, and Accounting. Used for managing PPP connections.
*   **Authentication:** Methods like PAP, CHAP, and MS-CHAPv2 for verifying user credentials.
*   **Authorization:**  Determine what resources the authenticated user can access.
*   **Accounting:**  Keep track of connection time, data usage, and other metrics.
*   **Use:** Essential for VPNs (PPTP, L2TP, PPPoE) and hotspots.

### RADIUS
*   **Concept:** Remote Authentication Dial-In User Service. A centralized authentication system, widely used in ISP and enterprise networks.
*   **Configuration:**
    *   `radius add address=192.168.5.1 secret=mysecret` sets up a RADIUS client on the MikroTik device.
*   **Use:** For authenticating and authorizing users for wireless, VPN, and other network services.
*   **Advantages:**  Centralized user management, better control and audit capabilities.

### User / User groups
*   **Concept:** User management is critical for controlling access to your router and network resources.
*   **Local Users:** Can be managed on the router directly. `user add name=myuser password=mypassword group=read`.
*   **User Groups:** Used to assign different levels of permission. `group add name=readonly policy=read` creates a read only group.
*   **Limitations:**  Local users may not scale well for large networks.  RADIUS is often preferred for larger deployments.

### Bridging and Switching
* **Concept:** Bridging connects multiple network interfaces as if they were one large network. Switching refers to packet forwarding within a bridge interface using Layer 2 addressing (MAC addresses).
* **Configuration:**
  ```mikrotik
  /interface bridge add name=bridge1
  /interface bridge port add bridge=bridge1 interface=ether1
  /interface bridge port add bridge=bridge1 interface=ether2
  ```
  This creates a bridge named `bridge1` which includes ethernet interfaces `ether1` and `ether2`.
* **Use Cases:**
    * Connect multiple subnets as one.
    * Connecting multiple interfaces to the same DHCP server or hotspot.
    * Layer-2 VLAN management and passing.
* **Spanning Tree Protocol (STP):** RouterOS implements STP and Rapid STP (RSTP) to prevent loops.
* **Hardware Offloading:** Some RouterBoard hardware can do L2 bridging and switching faster through hardware offloading.

### MACVLAN
* **Concept:** A virtual interface that uses a parent ethernet interface's physical MAC address. This allows multiple devices to operate on a single physical network interface, appearing as if they have separate MAC addresses.
* **Configuration:**
  ```mikrotik
    /interface macvlan add interface=ether1 mac-address=02:00:00:00:00:01 name=macvlan1
    /interface macvlan add interface=ether1 mac-address=02:00:00:00:00:02 name=macvlan2
  ```
  This creates two MACVLAN interfaces `macvlan1` and `macvlan2` on parent interface `ether1`.
* **Use Cases:**
    * Virtualization and Containerization: Each virtual machine or container can get its own MAC address and IP address on a physical interface.
    * Testing and network labs.
    * Network address management.
* **Limitations:**
    * Limited hardware support for offloading
    * More overhead than plain interfaces.

### L3 Hardware Offloading
* **Concept:** L3 hardware offloading allows specific hardware to do routing or other layer 3 operations instead of the CPU.
* **Benefits:**
    * Reduced CPU load.
    * Increased Throughput.
    * Better Performance.
* **Configuration:**
  ```mikrotik
  /ip firewall set use-ip-firewall=yes
  ```
  This would enable usage of fasttrack, for example.
* **Limitations:**
    * May not support all features.
    * Only available on specific MikroTik hardware.
    * Requires specific firewall settings to take advantage of L3 hardware offloading.

### MACsec
* **Concept:** Media Access Control Security.  MACsec provides hop-by-hop security for ethernet links by encrypting traffic at the data link layer.
* **Configuration:**
  ```mikrotik
  /interface macsec add name=macsec1  interface=ether1 key=12345678901234567890123456789012
  /interface macsec set macsec1 enabled=yes
  ```
  Creates a macsec interface on `ether1`.
* **Use Cases:**
    * Securing sensitive data transmissions between routers.
    * Protecting communications at the link level within an enterprise network.
    * Encrypting communications between Point-to-Point links.
* **Limitations:**
    * Requires specific hardware support.
    * Adds overhead due to encryption processing.

### Quality of Service
* **Concept:**  Mechanisms to prioritize different types of network traffic. This helps to ensure that important traffic (e.g., VoIP or video streaming) is not impacted by other less critical traffic.
* **Queues:** RouterOS uses queues to shape traffic.
  ```mikrotik
    /queue type add name=voip_queue kind=pcq pcq-rate=1M
    /queue tree add queue=voip_queue max-limit=2M parent=global interface=bridge1
  ```
This would create a `pcq` queue for VoIP and limit the traffic to 2 Mbps
* **Use Cases:**
  * Prioritizing voice traffic for better call quality.
  * Limiting bandwidth consumption of file transfers.
  * Ensuring critical application data is handled promptly.
* **Firewall integration:** QoS can be implemented using firewall rules (Mangle) to mark packets based on criteria, then Queues to prioritize or limit traffic.

### Switch Chip Features
* **Concept:** Many MikroTik routers use dedicated switch chips to handle bridging, switching, and VLAN operations at a hardware level, providing increased performance and reduced CPU load.
* **VLAN Support:** Supports VLAN tagging on physical interfaces, allowing for segregating traffic.
* **Port Mirroring:** Allows you to copy traffic from one port to another for analysis.
* **Link Aggregation:** Can bond multiple interfaces together for increased bandwidth and redundancy (LAG).
* **Limitations:** Features and capabilities depend on the specific switch chip used in your device, and some features may have limitations.
* **Hardware Offloading:** The switch chip can offload processing for bridging, VLAN, etc., reducing CPU usage.

### VLAN
* **Concept:** Virtual LANs logically divide a physical network into multiple separate broadcast domains. This helps to improve security, isolate traffic, and reduce broadcast domains.
* **Configuration:**
  ```mikrotik
  /interface vlan add name=vlan10 interface=bridge1 vlan-id=10
  /interface vlan add name=vlan20 interface=bridge1 vlan-id=20
  ```
  This creates two VLAN interfaces on the bridge interface `bridge1`.
* **Use Cases:**
  * Separating different departments within an office.
  * Isolating guest traffic from the main network.
  * Creating separate broadcast domains in larger networks.
* **VLAN tagging:** RouterOS uses 802.1q standard for VLAN tagging.
* **Trunks:** Use trunk links to carry multiple VLANs on a single link.

### VXLAN
* **Concept:** Virtual eXtensible LAN is a tunneling protocol used for extending Layer-2 networks over Layer-3 infrastructure. VXLAN encapsulates Layer-2 traffic in UDP packets using MAC-in-UDP encapsulation.
* **Configuration:**
  ```mikrotik
  /interface vxlan add name=vxlan10 vni=1000 interface=ether1 remote-address=192.168.1.2
  ```
This will create a vxlan interface to `192.168.1.2` using `vni=1000`.
* **Use Cases:**
  * Extending networks across different physical locations (e.g., datacenters).
  * Connecting virtual machines in different networks.
  * Creating isolated Layer-2 segments over an existing Layer-3 network.
* **Limitations:**
    * Adds overhead because of encapsulation
    * Requires a properly configured IP network for underlying transport.

### Firewall and Quality of Service
    *   **Connection Tracking:** Used to keep track of network connections to allow return traffic based on state. (`ip firewall connection`)
        *   The connection tracking allows to match "state" in firewall rules.
    *   **Firewall:** Used to control traffic based on IP addresses, ports, protocols, etc. (`ip firewall filter`, `ip firewall nat`, `ip firewall mangle`)
        *   Filter: Match on layer 3 and layer 4, can ACCEPT, DROP or REJECT packets.
        *   NAT: Network Address Translation, is used to change the IP addresses and ports of packets.
        *   Mangle: Can manipulate IP packet headers, used for QoS, routing, policy based routing etc.
    *   **Packet Flow in RouterOS:** Follows a specific processing chain (input->forward->output).
    *   **Queues:** Used to implement Quality of Service (QoS) by prioritizing or shaping traffic.
    *   **Firewall and QoS Case Studies:** Implementing firewall rules for blocking traffic, NAT rules for internet access, and QoS for prioritizing traffic.
    *   **Kid Control:** Time based access control using a firewall (`time` parameter in firewall rule)
    *   **UPnP:** Universal Plug and Play is a network protocol that allows for devices on a network to discover each other.
    *   **NAT-PMP:** NAT Port Mapping Protocol, allows automatic port forwarding.

### IP Services
    *   **DHCP:** Dynamic Host Configuration Protocol, used for dynamically assigning IP addresses, subnet masks, and other network settings to clients.
    *   **DNS:** Domain Name System, used to translate human-readable domain names into IP addresses.
    *   **SOCKS:** Socket Secure proxy, can be used as a generic proxy, useful for applications that require socks support.
    *   **Proxy:** A web proxy that can cache web pages and filter requests.

### High Availability Solutions
    *   **Load Balancing:** Distributing network traffic across multiple servers or links to improve performance and redundancy.
    *   **Bonding:** Combines multiple physical network interfaces into one logical link to increase bandwidth and provide failover.
    *   **Bonding Examples:** Combining Ethernet interfaces or wireless interfaces, depending on what's available on the router.
    *   **HA Case Studies:** Building highly available solutions using bonding and VRRP in real-world scenarios.
    *   **Multi-chassis Link Aggregation Group (MLAG):** Extends link aggregation across multiple physical switches.
    *   **VRRP:** Virtual Router Redundancy Protocol, enables multiple routers to share a single virtual IP address.
    *   **VRRP Configuration Examples:** Setting up VRRP with multiple routers for high availability.

### Mobile Networking
    *   **GPS:** Using the router's GPS capabilities for positioning and time synchronization.
    *   **LTE:** Connecting to mobile networks via LTE modems.
    *   **PPP:** Point-to-Point Protocol is the basis of most cellular connections.
    *   **SMS:** Sending and receiving SMS messages via the cellular interface, for example for network notifications.
    *   **Dual SIM Application:** Using multiple SIM cards for redundancy or different providers.

### Multi Protocol Label Switching - MPLS
    *   **MPLS Overview:** A protocol used for forwarding packets based on labels rather than IP addresses.
    *   **MPLS MTU:** Configuration of Maximum Transmission Unit for MPLS.
    *   **Forwarding and Label Bindings:** How MPLS packets are forwarded using the labels.
    *   **EXP bit and MPLS Queuing:** Using the EXP bit for traffic prioritization within MPLS.
    *   **LDP:** Label Distribution Protocol is used for the dynamic exchange of labels in an MPLS network.
    *   **VPLS:** Virtual Private LAN Service used to extend Layer 2 networks over a wide area using MPLS.
    *   **Traffic Eng:** Traffic Engineering provides control over the routes traffic takes.
    *   **MPLS Reference:** Reference to the standards and RFCs of MPLS.

### Network Management
    *   **ARP:** Address Resolution Protocol, used to map IP addresses to MAC addresses.
    *   **Cloud:** RouterOS cloud service for remote