Okay, let's dive deep into the world of MikroTik RouterOS, focusing on IP addressing within an SMB environment. This will be a comprehensive guide, covering a wide range of MikroTik features and concepts.

## MikroTik RouterOS IP Addressing and Networking (SMB)

### 1. Comprehensive Configuration Scenario and MikroTik Requirements

**Scenario:**

A small business (SMB) with a single internet connection needs a secure and well-configured network. We'll implement basic IPv4 and IPv6 connectivity, including internal IP addressing, NAT, and a basic firewall for security.

**Specific MikroTik Requirements:**

*   **Internet Connectivity:** One internet connection via Ethernet on `ether1`, which will receive a dynamic IPv4 address via DHCP and an IPv6 address via DHCPv6-PD.
*   **Internal Network:** A private IPv4 subnet `192.168.88.0/24` on interface `bridge1` (acting as a bridge for internal LAN).
*   **WiFi Network:** A separate WiFi network using the same IPv4 subnet as the `bridge1`.
*   **Static IPv4 Address for the router:** The router should have the IP 192.168.88.1 assigned to the `bridge1` interface.
*   **Dynamic IPv4 Address Allocation (DHCP):** An DHCP server is required for clients connected to the LAN/WiFi.
*   **IPv6 Support:** Implementation of IPv6 with prefix delegation and allocation on the LAN.
*   **Basic Security:** Implement a basic firewall and network address translation (NAT).

### 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

**CLI (Command Line Interface) Implementation:**

Here's the CLI implementation with detailed explanations:

*   **Step 1: Interface Setup**

    ```mikrotik
    /interface ethernet
    set ether1 name=WAN
    /interface bridge
    add name=bridge1
    /interface wifi
    set wlan1 mode=ap-bridge ssid=MyWiFi security-profile=default
    /interface bridge port
    add bridge=bridge1 interface=ether2
    add bridge=bridge1 interface=wlan1
    ```

    *   We rename `ether1` to `WAN` for better clarity, create a bridge called `bridge1`, setup the WiFi interface with a SSID and security profile, and add `ether2` and `wlan1` to the `bridge1`.

*   **Step 2: IPv4 Addressing**

    ```mikrotik
    /ip address
    add address=192.168.88.1/24 interface=bridge1
    /ip dhcp-client
    add interface=WAN
    ```

    *   We assign a static IP address 192.168.88.1/24 to the `bridge1` interface and configure DHCP client on `WAN` for IPv4 addressing.

*   **Step 3: DHCP Server Configuration**

    ```mikrotik
    /ip pool
    add name=dhcp_pool ranges=192.168.88.100-192.168.88.200
    /ip dhcp-server
    add address-pool=dhcp_pool interface=bridge1 name=dhcp1
    /ip dhcp-server network
    add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
    ```

    *   We create a DHCP pool with addresses from `192.168.88.100` to `192.168.88.200`, create a DHCP server on the `bridge1` interface and configure the network settings such as the DNS server and the default gateway.

*   **Step 4: IPv6 Addressing**

    ```mikrotik
    /ipv6 dhcp-client
    add interface=WAN request=address,prefix use-peer-dns=yes add-default-route=yes pool-name=ipv6_pool
    /ipv6 pool
    add name=ipv6_pool prefix-length=64
    /ipv6 address
    add address=::1 interface=bridge1 from-pool=ipv6_pool
    /ipv6 nd
    set [ find default=yes ] advertise-dns=yes
    ```

    *   We create a DHCPv6 client on the `WAN` interface to request a IPv6 address and a prefix, and use this prefix for the local network on `bridge1`. We also set the ND (Neighbor Discovery) to advertise DNS.

*  **Step 5: Basic Firewall and NAT**
    ```mikrotik
    /ip firewall nat
    add action=masquerade chain=srcnat out-interface=WAN
    /ip firewall filter
    add action=accept chain=input connection-state=established,related
    add action=accept chain=input protocol=icmp
    add action=drop chain=input in-interface=!WAN
    add action=accept chain=forward connection-state=established,related
    add action=accept chain=forward src-address=192.168.88.0/24
    add action=drop chain=forward
    ```

     *  We configure NAT for outgoing traffic by masquerading traffic that goes through the WAN interface, and basic input and forward firewall rules to improve the network's security.

**Winbox Implementation (GUI):**

These steps can be accomplished via the Winbox GUI.

*   **Interface Setup:**
    *   Navigate to `Interfaces`.
    *   Rename `ether1` to `WAN`.
    *   Add a new `bridge` interface named `bridge1`.
    *   Navigate to `Wireless` add configure a new access point.
    *   Go to `Bridge` -> `Ports` tab and add the internal interfaces (`ether2` and `wlan1`) to the `bridge1`.

*   **IPv4 Addressing:**
    *   Navigate to `IP` -> `Addresses`.
    *   Add address `192.168.88.1/24` on `bridge1`.
    *   Navigate to `IP` -> `DHCP Client` and add DHCP client on `WAN`.

*   **DHCP Server Configuration:**
    *   Navigate to `IP` -> `Pool` and add `dhcp_pool` with the IP range.
    *   Navigate to `IP` -> `DHCP Server` and add a DHCP server on `bridge1`, using the newly created pool.
    *   Navigate to `IP` -> `DHCP Server` -> `Networks` and set network parameters (address, DNS server, gateway).

*   **IPv6 Addressing:**
    *   Navigate to `IPv6` -> `DHCP Client` and add DHCPv6 client on the `WAN` interface with prefix delegation.
    *   Navigate to `IPv6` -> `Pool` and add a `ipv6_pool` for IPv6 addresses.
    *   Navigate to `IPv6` -> `Addresses` and add a local IPv6 address to the `bridge1` using the pool.
    *   Navigate to `IPv6` -> `ND` and enable `advertise-dns`.

*   **Basic Firewall and NAT:**
    *   Navigate to `IP` -> `Firewall` -> `NAT` and add a `masquerade` rule on the `WAN` interface.
    *   Navigate to `IP` -> `Firewall` -> `Filter Rules` and add the firewall rules (input and forward).

### 3. Complete MikroTik CLI Configuration Commands

Here is the consolidated MikroTik CLI configuration, including relevant parameters:

```mikrotik
# Interface Configuration
/interface ethernet
set [find default-name=ether1] name=WAN
/interface bridge
add name=bridge1
/interface wifi
set wlan1 mode=ap-bridge ssid=MyWiFi security-profile=default
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan1

# IPv4 Address Configuration
/ip address
add address=192.168.88.1/24 interface=bridge1
/ip dhcp-client
add interface=WAN

# DHCP Server Configuration
/ip pool
add name=dhcp_pool ranges=192.168.88.100-192.168.88.200
/ip dhcp-server
add name=dhcp1 address-pool=dhcp_pool interface=bridge1
/ip dhcp-server network
add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1

# IPv6 Address Configuration
/ipv6 dhcp-client
add interface=WAN request=address,prefix use-peer-dns=yes add-default-route=yes pool-name=ipv6_pool
/ipv6 pool
add name=ipv6_pool prefix-length=64
/ipv6 address
add address=::1 interface=bridge1 from-pool=ipv6_pool
/ipv6 nd
set [ find default=yes ] advertise-dns=yes

# Firewall and NAT Configuration
/ip firewall nat
add action=masquerade chain=srcnat out-interface=WAN
/ip firewall filter
add action=accept chain=input connection-state=established,related
add action=accept chain=input protocol=icmp
add action=drop chain=input in-interface=!WAN
add action=accept chain=forward connection-state=established,related
add action=accept chain=forward src-address=192.168.88.0/24
add action=drop chain=forward
```

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

*   **Incorrect Interface Selection:** Ensure you've correctly selected the interfaces for DHCP clients, server, and addresses. Verify bridge settings.
*   **DHCP Server Issues:** Check for address conflicts in the DHCP pool or DNS settings on the DHCP network configuration. Use `/ip dhcp-server lease print` to check active DHCP leases.
*   **Firewall Blockages:** Incorrect firewall rules can block essential services (DNS, DHCP). Check `/ip firewall filter print` and use `torch` on interface to see the traffic flow.
*   **IPv6 Configuration Issues:** Verify the router receives IPv6 via DHCPv6 and that the interface has a valid link-local address. Use the `/ipv6 dhcp-client print` command to see the status of the IPv6 DHCP client.
*   **DNS Issues:** Ensure the router itself can resolve names (`/tool dns lookup google.com`). Verify the DHCP server provides the correct DNS server configuration.
*   **Routing Issues:** Check the routing table (`/ip route print`) to ensure that the default route is present. Also, verify that the IPv6 routing table is correct (`/ipv6 route print`).
*   **General Troubleshooting:** Use `/system resource print` to verify system resources, `/log print` to check system logs for errors, and the `ping` and `traceroute` tools for connectivity testing.

### 5. Verification and Testing

*   **Ping Test:** Verify the router has internet connectivity by pinging `8.8.8.8` and `2001:4860:4860::8888`:

    ```mikrotik
    /ping 8.8.8.8
    /ipv6 ping 2001:4860:4860::8888
    ```
*   **Traceroute:** Test network path to the internet:

    ```mikrotik
    /tool traceroute 8.8.8.8
    /ipv6 tool traceroute 2001:4860:4860::8888
    ```
*   **DHCP Lease Check:**

    ```mikrotik
    /ip dhcp-server lease print
    ```
*   **Torch:** Analyze traffic flow on interfaces (e.g., `WAN`):

    ```mikrotik
    /tool torch interface=WAN
    ```

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **MikroTik Address Lists:** For categorizing and managing IP addresses.
*   **VRF:** Virtual Routing and Forwarding allows for routing isolation.
*   **Connection Tracking:** Used by the firewall to keep track of network connections and is essential for NAT and stateful firewalling.
*   **Queues:** For QoS configuration using PCQ and HTB algorithms.
*   **Route Filtering:** To control routing updates and policies for more complex networks.

### 7. MikroTik REST API Examples

Here's a basic example using the MikroTik REST API (assuming you have the REST API enabled on your router).

**API Endpoint:** `https://<your_router_ip>/rest/ip/address`

* **List IP Addresses (GET)**

    *   **Method:** `GET`
    *   **Example cURL command:**
        ```bash
        curl -k -u <username>:<password> -H "Content-Type: application/json" https://<your_router_ip>/rest/ip/address
        ```

        **Expected Response (JSON):**
        ```json
        [
           {
                ".id": "*1",
                "address": "192.168.88.1/24",
                "interface": "bridge1",
                "dynamic": "false"
            },
            {
                ".id": "*2",
                "address": "172.16.1.10/24",
                "interface": "WAN",
                "dynamic": "true"
            }
        ]
        ```

* **Add IP Address (POST)**

   * **Method:** `POST`
   * **Example cURL command:**

     ```bash
     curl -k -u <username>:<password> -H "Content-Type: application/json" -d '{"address": "192.168.88.2/24", "interface": "bridge1"}' https://<your_router_ip>/rest/ip/address
     ```

     **Expected Response (JSON):**
     ```json
        {
        "message": "added",
        "id": "*3"
        }
     ```

* **Update IP Address (PUT)**

    *   **Method:** `PUT`
    *   **Example cURL command:**
         ```bash
           curl -k -u <username>:<password> -H "Content-Type: application/json" -d '{"address": "192.168.88.3/24", "interface": "bridge1"}'  https://<your_router_ip>/rest/ip/address/*2
         ```
     **Expected Response (JSON):**
      ```json
         {
           "message": "changed"
         }
      ```
*   **Delete IP Address (DELETE)**

    *   **Method:** `DELETE`
    *   **Example cURL command:**
        ```bash
        curl -k -u <username>:<password> -H "Content-Type: application/json" -X DELETE https://<your_router_ip>/rest/ip/address/*3
        ```
       **Expected Response (JSON):**
        ```json
           {
            "message": "removed"
           }
        ```

*Note: Replace `<your_router_ip>`, `<username>`, and `<password>` with your MikroTik's IP address, username, and password.*

**Important Notes about API:**
* Enable the API service on the router at `/ip service` and set the proper security settings.
* The router MUST have a password set before enabling the API.
*  The ID of the resource (ex: `*2` in the example) is generated on resource creation and may change between different routers and even when creating new resources, so make sure to check that resource's ID before using the API.

### 8. In-Depth Explanations of Core Concepts

*   **Bridging:**  MikroTik bridges allow you to combine different interfaces into a single broadcast domain, functioning like a switch. This makes it easier to manage multiple LAN segments. The bridge can be assigned an IP address, allowing the router to act as a default gateway.
*   **Routing:** MikroTik supports static routes, dynamic routing protocols (OSPF, BGP, RIP), and policy-based routing. The routing table determines the next hop for packets.
*   **Firewall:**  MikroTik's stateful firewall uses connection tracking to decide whether packets should pass through based on their connection state, making filtering much safer and efficient. It also offers various features like NAT, Mangle, Raw rules, and more.

### 9. Security Best Practices

*   **Change Default Credentials:** Update the default `admin` password immediately.
*   **Disable Unnecessary Services:** Disable services like telnet and SSH unless absolutely necessary.
*   **Strong Passwords:** Use strong, unique passwords for user accounts and the web interface.
*   **Firewall Configuration:** Implement strict firewall rules and only allow necessary access.
*   **Regular RouterOS Updates:** Keep the MikroTik device updated with the latest software for security patches.
*   **Use VPN:** Consider using VPN for remote access rather than exposing management interfaces directly to the internet.
*   **IP Services Access Control:** Manage access to services such as `Winbox`, `SSH` and `API`. Use the `/ip service` command to restrict access to only trusted IP addresses.
*  **Enable RPKI:** For BGP networks, enable RPKI to prevent route hijacking.
* **Disable default services**: Disable services that are not needed, specially the default `www` service in the `IP services` section.

### 10. Detailed Explanations and Configuration Examples for Specified Topics

Let's delve into the required topics with explanations and examples, which we will be providing progressively as it is a lot of content.

#### IP Addressing (IPv4 and IPv6)

*   **IPv4:**  The most common addressing protocol, represented in dotted decimal notation (e.g., `192.168.88.1`). Each device on the network needs a unique IPv4 address for communication.
*   **IPv6:**  The successor to IPv4, designed to address the exhaustion of IPv4 addresses. IPv6 addresses are represented in hexadecimal notation (e.g., `2001:db8::1`).
    *   **Configuration:** Use `/ip address` for IPv4 and `/ipv6 address` for IPv6.
    *   **Prefix Delegation:** With IPv6, a range of addresses are assigned to the network, for this, the option `request=prefix` must be set on the dhcp client.

    **Example:**
    ```mikrotik
    /ip address
    add address=192.168.1.10/24 interface=bridge1
    /ipv6 address
    add address=2001:db8::1/64 interface=bridge1
    ```

#### IP Pools

*   **Definition:** Used by DHCP servers and other services to allocate IP addresses from a defined range.
*   **Creation:** Use `/ip pool` to create named IP pools.
    *   The `ranges` parameter specifies the address range.

    **Example:**
    ```mikrotik
    /ip pool
    add name=lan_pool ranges=192.168.88.100-192.168.88.200
    /ipv6 pool
    add name=ipv6_lan_pool prefix-length=64
    ```
*   **Usage:**  The pools are used in DHCP servers and IPv6 addresses configuration

    **Example:**
    ```mikrotik
    /ip dhcp-server
    add name=dhcp1 address-pool=lan_pool interface=bridge1
     /ipv6 address
    add address=::1 interface=bridge1 from-pool=ipv6_lan_pool
    ```

#### IP Routing

*   **Static Routes:** Explicit routes are configured manually, good for small, static networks.
*   **Dynamic Routing:** Use routing protocols (OSPF, BGP, RIP) to learn routes dynamically.
*   **Routing Table:**  Use `/ip route print` and `/ipv6 route print` to inspect the routing tables.
* **Policy based routing:** Implement more advanced routing solutions, routing packages based on different parameters such as the source address, protocol and other firewall marks.

    **Example:**
    ```mikrotik
    /ip route
    add dst-address=0.0.0.0/0 gateway=192.168.1.1
    ```
    **Example (Policy based routing):**
    ```mikrotik
    /ip route
    add dst-address=0.0.0.0/0 gateway=192.168.1.1 routing-mark=internet-access
    /ip firewall mangle
    add chain=prerouting action=mark-routing new-routing-mark=internet-access in-interface=ether1
    ```

#### IP Settings

*   **General Settings:** Configure essential parameters such as the TCP/IP stack and connection tracking settings.

    **Example:**
    ```mikrotik
    /ip settings
    set tcp-syncookies=yes
    ```

#### MAC Server

*   **Functionality:** Provides MAC address-based services such as Wake on LAN, MAC address learning, etc.
    *   The MAC server provides information about devices connected to the interfaces.
*   **Configuration:** Use `/tool mac-server` to enable the mac server and configure its behaviour.

    **Example:**
    ```mikrotik
    /tool mac-server
    set enabled=yes interfaces=all
    /tool mac-server print
    ```

#### RoMON

*   **MikroTik specific tool**
*   **Functionality:** MikroTik's Remote Monitoring tool, used for discovery, and access for remote Mikrotik devices.
*   **Configuration:** Use `/tool romon` to configure romon on interfaces and the service configuration
    *   It can be configured by an interface or all of them, it will be available through Layer2.
    *   Can be configured on the same port as other services like SSH.

    **Example:**
    ```mikrotik
    /tool romon
    set enabled=yes interfaces=all
    /tool romon print
    ```
#### WinBox

*   **Mikrotik Specific Tool**
*   **Functionality:** Graphical user interface for managing MikroTik routers. It is the most commonly used tool to configure the devices, and it can be configured through the `/ip service` command.
    *   Offers a simpler way to manage the MikroTik RouterOS than the CLI.
*   **Access Control:** It's recommend to restrict the access using the `address` parameter at `/ip service print`

    **Example:**
    ```mikrotik
     /ip service
     set winbox disabled=no address=192.168.88.0/24
    ```

#### Certificates

*   **Functionality:** Required for secure communication such as HTTPS and VPN.
*   **Generation:** Can be self-signed or obtained from a Certificate Authority.
    *  The most common way is to generate them locally on the device.
*   **Configuration:** Use `/certificate` commands to manage certificates.
    * Can be managed both through the command line and the GUI.

    **Example (generate a self-signed cert):**
    ```mikrotik
    /certificate
    add name=my-cert common-name=router.local generate-key=yes key-usage=tls-server
    ```

#### PPP AAA

*   **Functionality:** PPP Authentication, Authorization, and Accounting (AAA) allows you to manage user access to a network.
*   **Configuration:** Used in conjunction with PPP profiles (e.g., PPPoE) and the RADIUS Server to enable AAA.
     *   Can be configured in the `ppp` section.
     *   It must be coupled with a radius server if RADIUS AAA is desired.
   **Example (use local authentication):**
     ```mikrotik
     /ppp profile
     add name=my-ppp-profile use-encryption=yes
    /ppp secret
    add name=my-user password=my-password profile=my-ppp-profile service=pppoe
     ```
#### RADIUS

*   **Functionality:** Remote Authentication Dial-In User Service provides a centralized way to manage user authentication.
*   **Configuration:** Configure RADIUS clients and servers in the `/radius` and `/ppp aaa` sections.
    *   Used mainly with VPNs and access points.

    **Example (Add RADIUS server):**
    ```mikrotik
    /radius
    add address=192.168.100.1 secret=mysecret
    /ppp aaa
    set use-radius=yes accounting=yes
    ```

#### User / User groups

*   **Functionality:** User Management is managed by the `/user` command, where users can be created or modified, together with the permissions groups that these users belong to using the `/user group` commands.
*   **Configuration:**  Users can be local to the device, or can be authenticated through a RADIUS server.

    **Example:**
    ```mikrotik
    /user group
    add name=readonly policy=read
     /user
    add name=readonly-user password=my-password group=readonly
    ```

#### Bridging and Switching

*   **Functionality:** Creating layer-2 networks for LAN segments.
*   **Configuration:** `/interface bridge` is used for bridge creation, and `/interface bridge port` for assigning ports to the bridge.
*   **Spanning Tree Protocol (STP):** Prevents loops in network topologies (configurable in bridge settings).

    **Example (Bridge creation):**
    ```mikrotik
    /interface bridge
    add name=lan_bridge
    /interface bridge port
    add bridge=lan_bridge interface=ether2
    add bridge=lan_bridge interface=ether3
    ```

#### MACVLAN

*   **Functionality:** Allows creating multiple logical interfaces on a single physical interface, each with a unique MAC address. Used mainly for containers and virtual machines.
*   **Configuration:** Use the `/interface macvlan` command to create a macvlan interface from a parent one, then these interfaces can be assigned different IP addresses.

    **Example:**
     ```mikrotik
     /interface macvlan
     add name=macvlan1 mac-address=02:4D:E5:55:4F:46 master-interface=ether2
      /ip address
      add address=192.168.89.1/24 interface=macvlan1
    ```

#### L3 Hardware Offloading

*   **Functionality:** Offloads routing and NAT processing to the switch chip's hardware for improved performance.
*   **Configuration:** Can be enabled in the `/interface ethernet` settings, if the hardware supports it.
    * Not all devices support this feature, refer to the device manual for this.
    * In some devices this feature can be enabled globally using the `/interface settings`

     **Example:**
     ```mikrotik
     /interface ethernet
     set ether1 l3-hw-offloading=yes
    ```

#### MACsec

*   **Functionality:** Layer-2 encryption protocol, providing point-to-point encryption.
    *   Usually used with fiber connections.
*   **Configuration:** Configure it in the `/interface ethernet` settings. It can use pre-shared keys or X.509 certificates.

   **Example:**
   ```mikrotik
  /interface ethernet
  set ether1 macsec-enabled=yes macsec-key=000102030405060708090a0b0c0d0e0f
  ```

#### Quality of Service

*   **Functionality:** Traffic prioritization based on packet characteristics.
*   **Configuration:** `/queue tree` and `/queue type` used to set up traffic prioritization and limiting.
*   **PCQ and HTB:** Common queueing algorithms.

     **Example (Basic Queue):**
    ```mikrotik
    /queue tree
    add name=download parent=global-in max-limit=50M
    add name=upload parent=global-out max-limit=20M
    ```

#### Switch Chip Features

*   **Functionality:** The RouterOS has access to the switch chip features to do VLAN and L2 features on the switch chip for faster processing.
*   **Configuration:** Configured through the `/interface ethernet switch` menu, with the specific parameters for each model.
 *  **VLAN Tagging**: VLAN tagging can also be configured through the switch chip feature.

   **Example:**
    ```mikrotik
      /interface ethernet switch vlan
       add ports=ether2-ether5 vlan-id=10 vlan-header=add-if-missing
       add ports=ether2-ether5 vlan-id=20 vlan-header=add-if-missing
   ```

#### VLAN

*   **Functionality:** Layer 2 virtual networks, used for traffic segregation.
*   **Configuration:** `/interface vlan` is used to create VLAN interfaces, and are associated to physical or bridge interfaces.
*   **VLAN IDs:** Must match on the devices that should communicate with each other through VLAN.

    **Example:**
    ```mikrotik
    /interface vlan
    add name=vlan10 vlan-id=10 interface=bridge1
    /ip address
    add address=192.168.10.1/24 interface=vlan10
    ```

#### VXLAN

*   **Functionality:** Layer 2 tunnels using Layer 3 for interconnections between networks.
    * It acts as a VLAN between different networks without the need for direct connectivity.
*   **Configuration:** Configured through the `/interface vxlan` menu.

   **Example:**
    ```mikrotik
    /interface vxlan
    add name=vxlan1 vxlan-id=1000 mac-address=02:00:00:00:00:01 remote-address=192.168.100.2
    ```

#### Firewall and Quality of Service (QoS)

*   **Connection Tracking:** The firewall tracks stateful connections.
    * It helps the router to understand if the connection is already established.
    * `/ip firewall connection print` shows the currently established connections.
*   **Firewall Filter:** Rules for packet filtering (allow, drop, etc.).
    *  `/ip firewall filter` configure filtering rules.
    * The rules are processed from top to bottom, the first match is the rule that takes effect.
*   **Packet Flow:**  Packets go through input, forward, and output chains.
*   **Queues:** Used for QoS (rate limiting, traffic prioritization).
*   **Case Studies:** Block specific protocols, or implement parental controls.
*   **Kid Control:** Using a parental control based on scheduling and web filtering
*   **UPnP:**  Universal Plug and Play, which allows applications to open ports through the firewall, but is a security risk.
*   **NAT-PMP:**  Network Address Translation Port Mapping Protocol, same functionality as UPnP.

    **Example (Firewall Filter):**
    ```mikrotik
    /ip firewall filter
    add chain=input action=accept protocol=icmp
    add chain=input action=drop in-interface=!WAN
     /ip firewall nat
      add chain=srcnat action=masquerade out-interface=WAN
    ```
    **Example (Parental Controls):**
     ```mikrotik
    /ip firewall filter
    add chain=forward action=drop src-address=192.168.88.100 time=18h-22h,sat,sun
    ```

#### IP Services (DHCP, DNS, SOCKS, Proxy)

*   **DHCP:** `/ip dhcp-server`, provides dynamic IP addresses to clients.
    * It can be configured to provide different services such as DNS and gateway information.
*   **DNS:** `/ip dns`, DNS client and cache for name resolution.
    *   Configure the DNS server for the router.
    *  It can use static entries, or can be configured to be a caching DNS server.
*   **SOCKS Proxy:** `/ip socks`, create a SOCKS proxy for application-level traffic redirection.
*   **HTTP Proxy:** `/ip proxy`, create an HTTP proxy for HTTP traffic redirection.

    **Example (DHCP):**
    ```mikrotik
    /ip dhcp-server
    add address-pool=lan_pool interface=bridge1
    /ip dhcp-server network
    add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1
    ```

    **Example (DNS):**
        ```mikrotik
        /ip dns
        set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
        ```

#### High Availability Solutions (HA)

*   **Load Balancing:** Distributes traffic across multiple links (e.g., ECMP).
*   **Bonding:** Combines multiple interfaces for increased bandwidth or redundancy.
    *  Supported modes: Active-backup, balance-rr, balance-xor, balance-alb.
*   **VRRP:** Virtual Router Redundancy Protocol for failover between routers.
    * When the master router fails, a secondary takes over, making sure the network remains stable.
*   **Multi-chassis Link Aggregation Group (MC-LAG):** More complex version of bonding between different devices.

    **Example (Bonding):**
        ```mikrotik
        /interface bonding
        add mode=balance-alb name=bond1 slaves=ether1,ether2
        ```

    **Example (VRRP):**
        ```mikrotik
        /interface vrrp
        add interface=ether1 vrid=1 priority=100
        ```

#### Mobile Networking

*   **GPS:** For location services.
*   **LTE:** Integrated LTE modules.
*   **PPP:** Point-to-Point Protocol for cellular connections.
    * Used when connecting through modems and cellphones.
*   **SMS:** Send and receive SMS.
    *  It is often used to check the device status through SMS.
*   **Dual SIM:** Manage multiple SIM cards (if supported by the device).

    **Example (LTE Configuration):**
        ```mikrotik
        /interface lte
        set apn=internet
        ```

#### Multi Protocol Label Switching - MPLS

*   **MPLS Overview:** Multiprotocol Label Switching, used for efficient traffic forwarding.
*   **MPLS MTU:** Maximum Transmission Unit for MPLS packets.
*   **Forwarding and Label Bindings:** Used to decide which traffic to forward through MPLS.
*   **EXP bit and MPLS Queuing:** Used for QoS within the MPLS network.
*   **LDP:** Label Distribution Protocol for distributing labels.
*   **VPLS:** Virtual Private LAN Service.
*   **Traffic Eng:** MPLS Traffic Engineering for optimizing path selection.

   **Example (Simple MPLS Configuration):**
    ```mikrotik
    /mpls interface
    add interface=ether1
    /mpls ldp
    set enabled=yes transport-address=192.168.100.1
    ```

#### Network Management

*   **ARP:** Address Resolution Protocol for mapping IP to MAC addresses.
    *  The router needs the correct ARP table to know where to send packets.
    * `/ip arp` to configure the ARP table.
*   **Cloud:**  MikroTik's cloud services for remote management.
*