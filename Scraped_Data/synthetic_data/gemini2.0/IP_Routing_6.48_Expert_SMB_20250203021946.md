Okay, let's dive into a comprehensive documentation on IP routing within a MikroTik environment, focusing on a specific subnet and interface. This will be geared towards an "Expert" level configuration for an SMB network using RouterOS 6.48 (while also considering aspects of RouterOS 7).

## Comprehensive MikroTik Configuration for IP Routing on VLAN 79

This document outlines a complete configuration for routing IP traffic on a MikroTik router, specifically focusing on the `vlan-79` interface with the `211.112.123.0/24` subnet. We will cover address assignment, routing, firewall considerations, common issues, and some advanced topics.

### 1. Configuration Scenario and Requirements

*   **Scenario:** A small to medium business (SMB) network uses VLANs for segmenting network traffic. VLAN 79 is used for a specific department or purpose, and it needs to be correctly routed through the MikroTik router.
*   **Requirements:**
    *   Assign an IP address within the `211.112.123.0/24` subnet to the `vlan-79` interface.
    *   Ensure proper routing so traffic from `vlan-79` can reach other networks (e.g., the internet, other VLANs).
    *   Configure basic firewall rules to allow traffic from this subnet.
    *   Understand how routing works in MikroTik and potential pitfalls.
    *   Consider potential future expansion with advanced routing features.

### 2. Step-by-Step MikroTik Implementation

**Using CLI (Recommended):**

*   **Step 1: VLAN Interface Creation (assuming underlying interface exists, e.g. ether2)**
    ```mikrotik
    /interface vlan
    add name=vlan-79 vlan-id=79 interface=ether2
    ```
    *   `add name=vlan-79`: Creates a new VLAN interface named "vlan-79".
    *   `vlan-id=79`: Assigns the VLAN ID 79.
    *   `interface=ether2`: Specifies the physical interface the VLAN is created on (e.g., ether2). Replace 'ether2' with the appropriate interface.
* **Step 2: Assigning an IP Address**
   ```mikrotik
   /ip address
   add address=211.112.123.1/24 interface=vlan-79
   ```
    *   `add address=211.112.123.1/24`:  Assigns the IP address `211.112.123.1` with a `/24` subnet mask to the interface.
    *   `interface=vlan-79`:  Specifies which interface to apply this address to.
*   **Step 3: Setting up Basic Routing**
    *   To ensure the router knows how to reach networks other than `211.112.123.0/24`, you'll likely need a default route.
    ```mikrotik
    /ip route
    add dst-address=0.0.0.0/0 gateway=YOUR_GATEWAY_IP
    ```
     *   `add dst-address=0.0.0.0/0`:  This defines a default route (all destinations)
     *   `gateway=YOUR_GATEWAY_IP`:  Specifies the IP address of the next hop router or gateway. Replace `YOUR_GATEWAY_IP` with your ISP or upstream router's IP address.
        * You can also set the gateway via interface if needed, eg: `gateway=ether1`

*   **Step 4: Basic Firewall Configuration**
    *   Allow traffic from VLAN 79 to other networks.
    ```mikrotik
     /ip firewall filter
     add chain=forward action=accept in-interface=vlan-79
     add chain=forward action=drop in-interface=vlan-79
     add chain=input action=accept in-interface=vlan-79
    ```
    *   These rules allow all forward traffic (traffic passing through the router) originating from `vlan-79`. The drop rule will drop any traffic if not matched by previous rules
    *   Additionally, we add a rule allowing all input (traffic destined to the router itself) originating from `vlan-79`

*   **Step 5: NAT (Network Address Translation) - If needed (usually needed for internet access)**
    *  If you'd like the subnet to have access to the internet you need a NAT rule.
        ```mikrotik
        /ip firewall nat
        add chain=srcnat action=masquerade out-interface=YOUR_OUT_INTERFACE src-address=211.112.123.0/24
        ```
        *   `chain=srcnat action=masquerade`: Configures a source NAT rule for dynamic IP address translation.
        *   `out-interface=YOUR_OUT_INTERFACE`: The interface to use for sending traffic outside. Replace `YOUR_OUT_INTERFACE` with the interface connected to the internet (e.g., ether1, pppoe-out1).
        * `src-address=211.112.123.0/24`: Only NAT traffic from this network, all other traffic will remain untranslated.

**Using Winbox (GUI):**

*   **Step 1:**  Navigate to `Interfaces`, click the "+" button, choose "VLAN".
    *   Enter "vlan-79" for the `Name`, enter "79" for the `VLAN ID`, and select the correct interface (e.g., `ether2`) from the `Interface` dropdown menu.
*   **Step 2:**  Go to `IP` > `Addresses`, click the "+" button.
    *   Enter `211.112.123.1/24` in the `Address` field, select "vlan-79" from the `Interface` dropdown menu.
*   **Step 3:**  Go to `IP` > `Routes`, click the "+" button.
    *   Enter `0.0.0.0/0` in the `Dst. Address` field, Enter the `Gateway` to which this route will send the traffic.
*   **Step 4:**  Navigate to `IP` > `Firewall`, then click on the `Filter Rules` tab.
    *  Click the "+" to add new rules. Add rules allowing traffic originating from `vlan-79` interface as shown above in CLI command.
*   **Step 5:** Navigate to `IP` > `Firewall` and click the `NAT` tab.
    *  Click the "+" to add a NAT rule, select `srcnat` as `Chain`, `action` as `masquerade`, the source address `211.112.123.0/24` and the `out-interface` connected to the internet.

### 3. Complete MikroTik CLI Configuration Commands

```mikrotik
/interface vlan
add name=vlan-79 vlan-id=79 interface=ether2

/ip address
add address=211.112.123.1/24 interface=vlan-79

/ip route
add dst-address=0.0.0.0/0 gateway=YOUR_GATEWAY_IP

/ip firewall filter
add chain=forward action=accept in-interface=vlan-79
add chain=forward action=drop in-interface=vlan-79
add chain=input action=accept in-interface=vlan-79


/ip firewall nat
add chain=srcnat action=masquerade out-interface=YOUR_OUT_INTERFACE src-address=211.112.123.0/24
```

**Table of Parameters**
| Command Element    | Example Value       | Description                                                                                                 |
| ------------------ | ------------------- | ----------------------------------------------------------------------------------------------------------- |
| `name`             | `vlan-79`          |  Name of interface                                                                                          |
| `vlan-id`          | `79`              | VLAN identifier                                                                                            |
| `interface`        | `ether2`          |  Physical interface to which VLAN is attached                                                              |
| `address`          | `211.112.123.1/24`| IP address and subnet mask                                                                                    |
| `dst-address`      | `0.0.0.0/0`        | Destination address, `0.0.0.0/0` represents all destination                                                 |
| `gateway`          | `YOUR_GATEWAY_IP` | IP address of the next hop router                                                                            |
| `chain`            | `forward`, `input`, `srcnat`| The firewall rule chain the rule applies to. Forward for traffic that pass through the router, input for traffic destined to the router, and srcnat for natting traffic. |
| `action`           | `accept`, `drop`, `masquerade`  | Action to perform. accept will accept all traffic, drop will drop all traffic, and masquerade will perform dynamic IP address translation. |
| `in-interface`    | `vlan-79`          |  The interface on which the incoming traffic arrives                                                          |
| `out-interface`   | `YOUR_OUT_INTERFACE` | The interface on which the outgoing traffic exits                                                         |
| `src-address`      | `211.112.123.0/24` | The source network for the NAT rule.                                                                            |

### 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

*   **Pitfall 1: Incorrect Interface:** If the VLAN interface is not created on the correct physical interface, traffic will not be sent or received.
    *   **Troubleshooting:** Use `/interface print` to verify interface mappings.  Use `/interface vlan print` to verify vlan interface settings.
    *   **Error Scenario:** No traffic reaches or leaves the VLAN 79 network.
    *   **Diagnosis:**  Check interface configuration, MAC address of attached equipment, and physical cabling/connectivity.
*   **Pitfall 2: Missing or Incorrect Default Route:** Without a correct default route, the MikroTik router will not know how to send traffic destined for networks outside of its local networks.
    *   **Troubleshooting:**  Use `/ip route print` to check routes.
    *   **Error Scenario:** Devices on VLAN 79 can communicate locally but cannot reach the internet or other remote networks.
    *   **Diagnosis:** Check routing table and gateway configuration. Ensure the gateway is reachable via ping.
*   **Pitfall 3: Firewall Blocking Traffic:** If firewall rules are misconfigured, legitimate traffic may be dropped.
    *   **Troubleshooting:**  Use `/ip firewall filter print` to inspect firewall rules and `/tool torch interface=vlan-79` to view traffic in real-time.  Enable log rule on firewall and view the log if packets are getting dropped.
    *   **Error Scenario:**  Devices on VLAN 79 cannot access internet resources or other network segments, even with correct routing.
    *   **Diagnosis:** Review firewall rules carefully and ensure correct order.
*   **Pitfall 4: Missing or Incorrect NAT Rule:** Without NAT, traffic coming from a private IP to a public one (and vice-versa) will not be translated
    *   **Troubleshooting:**  Use `/ip firewall nat print` to inspect NAT rules.
    *   **Error Scenario:** Devices on VLAN 79 cannot access the internet.
    *   **Diagnosis:** Review NAT rules and ensure that the correct out-interface and source address is used.

**MikroTik Tools:**

*   **Ping:** `/ping 211.112.123.1` (from router) or `/ping 8.8.8.8` (from a client on VLAN 79). Use `ping` to test basic reachability.
*   **Traceroute:** `/traceroute 8.8.8.8` - Use to diagnose routing issues, and see the path to the destination
*   **Torch:**  `/tool torch interface=vlan-79` - Live traffic monitoring on interface, use it to see real-time traffic.
*   **Log:** `/system logging print` - Check the system log for error messages. Enable logging on firewall rules.
*   **Packet Sniffer:**  `/tool sniffer` - Captures network traffic for detailed analysis.
*   **IP Scan:** `/tool ip-scan` - Discover IP hosts on the network.
*   **Resource:** `/system resource print` - Displays CPU, memory, and disk usage.
*   **Traffic Monitor:** `/interface monitor-traffic interface=vlan-79` - Shows real-time traffic for a specific interface.

### 5. Verification and Testing Steps

1.  **IP Connectivity:** From a device on the VLAN 79 network, ping the router's interface IP (`211.112.123.1`). Then, ping an internet address (e.g., `8.8.8.8`).
2.  **Routing Verification:** From the MikroTik CLI use `/traceroute 8.8.8.8` and verify that the trace takes the expected path.
3.  **Firewall Testing:** Initiate a connection from a device on the VLAN 79 network to a public server. Then, create a firewall rule to block it and verify the failure.
4.  **NAT Verification:** Check that the source IP of traffic sent from the router on the out-interface is the router's public IP address.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Policy-Based Routing:**  MikroTik allows policy-based routing, where you can route traffic based on source IP or other criteria rather than just the destination IP. This is important for more complex configurations.
*   **VRF (Virtual Routing and Forwarding):** VRF is useful for separating routing tables and traffic flows. If a single router manages multiple tenants.
*   **OSPF, RIP, BGP:** You can use dynamic routing protocols in addition to static routes. This can be important for larger networks with multiple routers.
*   **Queue Management:** MikroTik's queue management (QoS) can be used to prioritize certain traffic over others. Important for applications that need low latency.

**Less Common Features**
*   **BGP:** Border Gateway Protocol can be used for connecting to other autonomous systems, most likely ISP's. Can be used for multi-homing.
*   **MPLS:** Multi-Protocol Label Switching can be used to create very efficient networks, mostly used for ISP's.
*   **IS-IS:** Intermediate System to Intermediate System can be used for very large networks.

**Trade-offs:**
*  **Static vs. Dynamic Routing:** Static routing is simpler to configure but can be harder to maintain in larger, more dynamic networks, while dynamic routing is harder to configure, but dynamically adjusts to network changes and is easier to maintain in larger networks.
*  **Basic vs. Advanced Firewall:** Basic firewall rules are easy to set up, but they are not as secure as advanced firewall rules, while advanced firewall rules are more secure but require more time to set up, and require a deeper understanding of firewall concepts.

### 7. MikroTik REST API Examples

**Assumptions:**
*   The MikroTik router has the API service enabled
*   The user has the correct permissions to perform the requests
*   The port for the API is the default port 8728

**Get VLAN Interface details:**

*   **API Endpoint:** `/interface/vlan`
*   **Request Method:** `GET`
*   **Example cURL command:**
    ```bash
    curl -k -u admin:YOUR_ADMIN_PASSWORD https://YOUR_MIKROTIK_IP:8729/interface/vlan
    ```
*   **Expected Response (Example JSON):**
    ```json
    [
        {
            ".id": "*1",
            "name": "vlan-79",
            "mtu": "1500",
            "actual-mtu": "1500",
            "vlan-id": "79",
            "interface": "ether2",
            "disabled": "false"
        }
        {
         ".id": "*2",
            "name": "vlan-80",
            "mtu": "1500",
            "actual-mtu": "1500",
            "vlan-id": "80",
            "interface": "ether2",
            "disabled": "false"
        }
    ]
    ```

**Add IP Address to the interface:**

*   **API Endpoint:** `/ip/address`
*   **Request Method:** `POST`
*  **Example cURL command:**
    ```bash
    curl -k -u admin:YOUR_ADMIN_PASSWORD -H "Content-Type: application/json" -X POST  -d '{"address":"211.112.123.1/24", "interface":"vlan-79"}' https://YOUR_MIKROTIK_IP:8729/ip/address
    ```
*   **Example JSON payload:**
    ```json
    {
        "address": "211.112.123.1/24",
        "interface": "vlan-79"
    }
    ```
*   **Expected Response (Example JSON):**
    ```json
    {
        "message": "added",
        ".id": "*1"
    }
    ```
*   **Note:** Always replace `YOUR_ADMIN_PASSWORD`, `YOUR_MIKROTIK_IP`, and other placeholders with actual values. The API port is 8729 when SSL is enabled. The API documentation can be found on the router itself or online on the MikroTik wiki.

**Add a default route:**

*   **API Endpoint:** `/ip/route`
*   **Request Method:** `POST`
*   **Example cURL command:**
    ```bash
    curl -k -u admin:YOUR_ADMIN_PASSWORD -H "Content-Type: application/json" -X POST -d '{"dst-address":"0.0.0.0/0", "gateway":"YOUR_GATEWAY_IP"}' https://YOUR_MIKROTIK_IP:8729/ip/route
    ```
*   **Example JSON payload:**
    ```json
    {
        "dst-address": "0.0.0.0/0",
        "gateway": "YOUR_GATEWAY_IP"
    }
    ```
*   **Expected Response (Example JSON):**
    ```json
    {
        "message": "added",
        ".id": "*1"
    }
    ```
*   **Note:** Always replace `YOUR_ADMIN_PASSWORD`, `YOUR_MIKROTIK_IP`, and `YOUR_GATEWAY_IP` with actual values.

### 8. In-Depth Explanation of Core Concepts

*   **IP Addressing:** Every device on a network requires an IP address. MikroTik assigns IPv4 (and IPv6) addresses to interfaces. The subnet mask determines the range of addresses within a network.
*   **IP Pools:** IP pools can be used to provide IP addresses to devices dynamically. These are primarily used with DHCP server, or PPP connections.
*   **Routing:** The process of forwarding network traffic from one network to another.  MikroTik uses routing tables to determine the best path for traffic.  Default routes send any unmatched traffic to a particular destination, while static routes are a route to a specific destination IP.
*   **Bridging:** Allows network segments to act as one.  All traffic passes through the same bridge.  Important to know the difference between routing and bridging.
*   **Firewall:** Controls network traffic based on rules.  Rules can accept, drop, or modify traffic based on source/destination IPs, ports, protocols, etc. The packet flow goes through the input, forward, and output chains sequentially.
*   **NAT (Network Address Translation):** Allows devices with private IP addresses to communicate on the internet. Source NAT translates the source IP of packets, while destination NAT translates the destination IP of packets.

### 9. Security Best Practices Specific to MikroTik Routers

*   **Strong Passwords:** Use strong, unique passwords for administrative accounts.
*   **Disable Unnecessary Services:** Disable services like telnet, API, and www-ssl (web interface) if you don't need them or restrict access to certain networks.
*   **Firewall:**  Use the firewall to restrict access to the MikroTik router itself, for example to only allow access from the management network. Block all access by default.  Carefully design filter and NAT rules.
*   **Regular Updates:** Keep RouterOS updated to patch security vulnerabilities.
*   **Secure Access to Winbox:** Only allow access to Winbox from trusted networks.
*   **VPN for Remote Access:** Use VPN for remote access to the MikroTik router instead of exposing the Web or Winbox directly to the internet.
*   **RoMON Security:** If using RoMON, secure it appropriately as it can provide full access to the device and other routers on the RoMON network.
*   **HTTPS:** Use HTTPS for accessing the router's web interface.
* **Input chain:** Lock down access to the router with filter rules. Only allow specific IP's or networks to connect to the router.
* **Output Chain:** Usually less restrictive than the input chain, but it can be secured based on specific scenarios.
* **L3 Hardware Offloading**: If supported by the router hardware, enable L3 hardware offloading. This will reduce the CPU load.
* **MACsec**: Use MACsec to encrypt ethernet traffic. MACsec is only available on some MikroTik devices, and needs to be enabled on both ends to work correctly.

### 10. Detailed Explanations and Configuration Examples for various MikroTik topics

#### IP Addressing (IPv4 and IPv6)
MikroTik supports IPv4 and IPv6 addressing.

*   **IPv4:** Uses 32-bit addresses, normally represented in dotted-decimal notation. e.g 192.168.1.1/24
*   **IPv6:** Uses 128-bit addresses, normally represented in hexadecimal notation. e.g 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64

```mikrotik
/ip address
add address=192.168.1.1/24 interface=ether1  # IPv4 address
add address=2001:db8::1/64 interface=ether1  # IPv6 address
```
*  **`add address`**: adds an IP address to the system
*  **`address`**: The ip address and subnet mask
*  **`interface`**: The interface to which the IP address will be assigned.

#### IP Pools
IP pools are used for dynamic address allocation, usually in conjunction with DHCP servers.

```mikrotik
/ip pool
add name=my-pool ranges=192.168.1.100-192.168.1.200
```
*   **`add name`**: Adds a new IP Pool with the given name.
*  **`ranges`**: The range of IP addresses for the pool.

#### IP Routing
Routes direct traffic to the correct networks, the default route is used for any traffic that does not match other entries in the routing table.

```mikrotik
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.1.254
add dst-address=10.0.0.0/24 gateway=192.168.1.10
```
*   **`add dst-address`**: Adds a route for the specified destination network.
*   **`gateway`**: The next-hop IP for this route.

#### IP Settings
Contains global IP settings, like router ID's for routing protocols.

```mikrotik
/ip settings
set router-id=10.10.10.1
```
*   **`set router-id`**: Sets the router ID, used by routing protocols.

#### MAC server
Allows remote access to the router using it's MAC address. This can be used with Winbox, for example.

```mikrotik
/tool mac-server
set allowed-interface-list=all enabled=yes
```
*   **`set allowed-interface-list`**: The list of interfaces that the service will listen to.
*   **`enabled`**:  Whether the service is enabled or not.

#### RoMON
Remote Monitoring is a MikroTik protocol that can be used to manage multiple routers, and access them even if they have misconfigured IP addresses.

```mikrotik
/tool romon
set enabled=yes id=myromonkey  secret=mysecret
```
*   **`set enabled`**: Enables the RoMON service.
*   **`id`**: Sets the RoMON ID.
*   **`secret`**: Sets the RoMON encryption secret.

#### WinBox
Winbox is the MikroTik GUI tool. Make sure it's secure as described in the section Security Best Practices.

#### Certificates
MikroTik can use certificates for various services, such as HTTPS, or IPsec.

```mikrotik
/certificate
import file=mycert.pem password=mypempassword
```
*  **`import file`**: Imports the certificate file.
*  **`password`**: The password for the certificate.

#### PPP AAA
PPP authentication, authorization, and accounting. Used with pppoe, pptp, l2tp etc.

```mikrotik
/ppp profile
add name=my-ppp-profile local-address=192.168.2.1 remote-address=my-pool
```
*  **`add name`**: Creates a PPP profile with the given name.
*   **`local-address`**: The IP assigned to the router on a pppoe session.
*   **`remote-address`**: The IP address or pool assigned to the client on a pppoe session.

#### RADIUS
Remote authentication, authorization, and accounting for centralized user management. Can be used in conjuction with PPP AAA

```mikrotik
/radius
add address=192.168.1.100 secret=myradiussecret service=ppp
```
*   **`add address`**: Sets the IP address for the radius server
*   **`secret`**: Sets the radius secret.
*   **`service`**: The service type that radius will be used for.

#### User / User groups
Users and groups can be used to manage access to the router.

```mikrotik
/user group
add name=my-group policy=read,write,test,password
/user
add name=myuser group=my-group password=mypassword
```
*  **`add name`**: Creates a user group or a new user with the given name.
*  **`group`**: Sets the user group of the user.
*  **`policy`**: Sets the permissions of the user group.
*  **`password`**: The password for the user.

#### Bridging and Switching
MikroTik routers support bridging and switching, in some cases using hardware offloading.

```mikrotik
/interface bridge
add name=my-bridge
/interface bridge port
add bridge=my-bridge interface=ether1
add bridge=my-bridge interface=ether2
```
*   **`add name`**: Creates a bridge interface with the given name.
*   **`bridge`**: Sets the bridge interface for the port.
*   **`interface`**: The interfaces to add to the bridge.

#### MACVLAN
Create virtual interfaces with different MAC addresses on a physical interface.

```mikrotik
/interface macvlan
add interface=ether1 mac-address=02:00:00:00:00:01 name=macvlan-1
```
*   **`add interface`**: The physical interface for the MACVLAN
*  **`mac-address`**: The mac address for the virtual interface.
*  **`name`**: The name for the virtual interface.

#### L3 Hardware Offloading
If supported by your hardware you should enable L3 hardware offloading to improve performance.

```mikrotik
/interface ethernet
set ether1 l3-hw-offloading=yes
```
*   **`set l3-hw-offloading`**: Enables or disables L3 Hardware offloading.

#### MACsec
MACsec can be used to encrypt Ethernet traffic, but is not supported on all Mikrotik hardware.

```mikrotik
/interface ethernet macsec
add  interface=ether1 encrypt=yes
```
*   **`add interface`**: The interface to add MACsec to.
*  **`encrypt`**: Specifies if encryption is enabled.

#### Quality of Service
Quality of Service (QoS) allows prioritization of traffic based on different criteria.

```mikrotik
/queue simple
add name=myqueue target=192.168.1.0/24 max-limit=10M
```
*   **`add name`**: Creates a new queue with the given name.
*   **`target`**: The target network or address for the queue.
*   **`max-limit`**: The maximum bandwidth limit for the queue.

#### Switch Chip Features
Certain MikroTik routers come with specialized switch chips with additional features. These features can be accessed using the `/interface ethernet switch` menu in CLI. The features depend on the router and the switch chip.

#### VLAN
Virtual LAN's for network segmentation. See examples above.

#### VXLAN
VXLAN creates a virtual network on top of the existing network, useful for extending Layer 2 domains.

```mikrotik
/interface vxlan
add name=vxlan1 vni=1000 interface=ether1 remote-address=192.168.1.2
```
*   **`add name`**: Create a new vxlan interface with the given name.
*   **`vni`**: The vni id.
*  **`interface`**: The physical interface for the tunnel
*  **`remote-address`**: The destination for the tunnel.

#### Firewall and Quality of Service
MikroTik's firewall is very flexible and can be used for a large amount of use cases, together with QoS, you have a lot of control on the traffic.

##### Connection Tracking
Connection tracking keeps track of the state of network connections, which is used in the firewall to manage stateful rules. Connection tracking is enabled by default.

##### Firewall
MikroTik's firewall is a very powerful tool for managing network traffic. See examples above.

##### Packet Flow in RouterOS
The packet goes through the input, forward, and output chains. You should have an understanding of what traffic goes through which chain.

##### Queues
Queues are used to manage the bandwidth, or set priorities for different traffic.

##### Firewall and QoS Case Studies
You should create your own case studies to learn how to use them in different scenarios.

##### Kid Control
MikroTik's firewall can be used for simple parental controls by creating filter rules with time constraints.

##### UPnP
Universal Plug and Play is a feature that allows devices to configure the firewall and NAT rules automatically. This is usually disabled in a secure environment.

##### NAT-PMP
Network Address Translation Port Mapping Protocol is similar to UPnP, but it is considered more secure. This is usually disabled in a secure environment.

#### IP Services (DHCP, DNS, SOCKS, Proxy)
IP services such as DHCP, DNS, SOCKS, and Proxy services.

##### DHCP
Dynamic Host Configuration Protocol, used for dynamically assigning IP addresses.

```mikrotik
/ip dhcp-server
add address-pool=my-pool interface=ether1 lease-time=1h name=mydhcpserver
/ip dhcp-server network
add address=192.168.1.0/24 dns-server=192.168.1.1 gateway=192.168.1.1
```
*   **`add address-pool`**: The IP pool to assign IP addresses from.
*   **`interface`**: The interface the DHCP server will listen to.
*   **`lease-time`**: How long an address will be leased.
*   **`dns-server`**: The dns server to give to the clients.
*   **`gateway`**: The default gateway for the clients.

##### DNS
The Domain Name System, used to resolve names to IP addresses.

```mikrotik
/ip dns
set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
```
*   **`set servers`**: The dns servers to use.
*   **`allow-remote-requests`**: If other hosts can use this router for DNS.

##### SOCKS
SOCKS can be used to proxy traffic.

```mikrotik
/ip socks
set enabled=yes
```
*  **`set enabled`**: Enables the SOCKS proxy server.

##### Proxy
MikroTik also supports web proxies.

```mikrotik
/ip proxy
set enabled=yes
```
*  **`set enabled`**: Enables the web proxy server.

#### High Availability Solutions
MikroTik supports various high availability solutions, such as load balancing, bonding, and VRRP.

##### Load Balancing
Traffic can be distributed across multiple paths.

##### Bonding
Multiple physical interfaces are used as one single interface, providing redundancy and more bandwidth.

```mikrotik
/interface bonding
add name=mybond mode=802.3ad slaves=ether1,ether2
```
*   **`add name`**: Creates a new bonding interface.
*   **`mode`**:  The bonding mode.
*   **`slaves`**: The list of physical interfaces that will be part of the bond.

##### Bonding Examples
You should create your own examples to learn how bonding is used in different scenarios.

##### HA Case Studies
You should create your own case studies to learn how to use HA features in different scenarios.

##### Multi-chassis Link Aggregation Group
Mikrotik does not support MC-LAG in the traditional sense. Bonding should be used instead.

##### VRRP
Virtual Router Redundancy Protocol is used to provide redundancy on the network layer.

```mikrotik
/interface vrrp
add name=vrrp1 interface=ether1 vrid=10 priority=100 address=192.168.1.1/24
```
*   **`add name`**: Creates a new VRRP interface.
*   **`interface`**: The physical interface.
*   **`vrid`**: The VRRP identifier.
*   **`priority`**: The VRRP priority.
*   **`address`**: The virtual IP address.

##### VRRP Configuration Examples
You should create your own VRRP examples to learn how to use VRRP in different scenarios.

#### Mobile Networking
MikroTik routers support mobile networking, including GPS, LTE, PPP, SMS, and Dual SIM applications.

##### GPS
MikroTik routers that support GPS can use this for location services.

##### LTE
MikroTik routers with an LTE interface can use this for connectivity.

##### PPP
PPP is used in conjunction with LTE, or other dialup connections.

##### SMS
MikroTik devices with an LTE modem can be used for sending and receiving text messages.

##### Dual SIM Application
Some devices support two sim cards for redundancy and load balancing.

#### Multi Protocol Label Switching - MPLS
MPLS is used to create fast and efficient networks by labeling packets. Usually used by ISP's

##### MPLS Overview
MPLS is a label switching technology.

##### MPLS MTU
MTU is important for MPLS tunnels.

##### Forwarding and Label Bindings
How MPLS labels are bound and forwarded.

##### EXP bit and MPLS Queuing
How EXP