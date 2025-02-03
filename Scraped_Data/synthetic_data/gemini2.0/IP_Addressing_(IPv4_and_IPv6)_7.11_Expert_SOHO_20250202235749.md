Okay, let's dive deep into a comprehensive technical documentation for MikroTik RouterOS, focusing on IP Addressing and related features, with a strong emphasis on practical, expert-level configurations.

---

# MikroTik RouterOS Expert Guide: IP Addressing & Related Features (v7.11)

This document targets an expert-level user familiar with networking concepts and aims to provide a deep dive into MikroTik RouterOS's implementation of IP addressing, related services, and advanced features. It is written for a SOHO (Small Office/Home Office) environment but includes concepts that can scale.

## 1. Comprehensive Configuration Scenario & MikroTik Requirements

**Scenario:** A small office requires a robust and secure network using IPv4 and IPv6. This network should provide:
    - Basic Internet connectivity via a PPPoE connection.
    - Multiple internal VLANs for different departments (e.g., management, sales, guest).
    - DHCPv4 and DHCPv6 services for each VLAN.
    - Basic Firewall rules to protect the internal network.
    - IPv6 support for the future.
    - Centralized user authentication through RADIUS.
    - Basic QoS to prioritize VoIP traffic.

**MikroTik Requirements:**
    - RouterOS v7.11 (or later)
    - Router with sufficient interfaces for VLANs
    - Basic understanding of networking concepts (VLANs, routing, firewalls)

## 2. Step-by-Step MikroTik Implementation

### 2.1 Initial Setup

*   Connect to the MikroTik router using Winbox or the CLI over Ethernet.
*   Set the router's identity:

    ```mikrotik
    /system identity set name=SOHO-Router
    ```
*   Update the system package if necessary:

    ```mikrotik
    /system package update check
    /system package update install
    /system reboot
    ```

### 2.2 Interface Configuration

*   Configure the PPPoE client on the external interface (assumed to be `ether1`):

    ```mikrotik
    /interface pppoe-client
    add user="<your_pppoe_user>" password="<your_pppoe_password>" interface=ether1 name=pppoe-out1 use-peer-dns=yes add-default-route=yes
    ```
*   Create VLAN interfaces (using `ether2` as the parent):

    ```mikrotik
    /interface vlan
    add interface=ether2 name=vlan10 vlan-id=10
    add interface=ether2 name=vlan20 vlan-id=20
    add interface=ether2 name=vlan30 vlan-id=30
    ```

### 2.3 IP Addressing and IP Pools

*   Assign IPv4 addresses and create IP Pools for each VLAN.

    ```mikrotik
    /ip address
    add address=192.168.10.1/24 interface=vlan10
    add address=192.168.20.1/24 interface=vlan20
    add address=192.168.30.1/24 interface=vlan30

    /ip pool
    add name=vlan10-pool ranges=192.168.10.10-192.168.10.254
    add name=vlan20-pool ranges=192.168.20.10-192.168.20.254
    add name=vlan30-pool ranges=192.168.30.10-192.168.30.254
    ```

*   Assign IPv6 addresses and create IPv6 Pools for each VLAN.

    ```mikrotik
    /ipv6 address
    add address=2001:db8:10::1/64 interface=vlan10
    add address=2001:db8:20::1/64 interface=vlan20
    add address=2001:db8:30::1/64 interface=vlan30

    /ipv6 pool
    add name=vlan10-ipv6-pool prefix=2001:db8:10::/64 prefix-length=64
    add name=vlan20-ipv6-pool prefix=2001:db8:20::/64 prefix-length=64
    add name=vlan30-ipv6-pool prefix=2001:db8:30::/64 prefix-length=64
    ```

### 2.4 DHCPv4 & DHCPv6 Server

*   Configure DHCPv4 Server for each VLAN:

    ```mikrotik
    /ip dhcp-server
    add address-pool=vlan10-pool disabled=no interface=vlan10 name=dhcp-vlan10
    add address-pool=vlan20-pool disabled=no interface=vlan20 name=dhcp-vlan20
    add address-pool=vlan30-pool disabled=no interface=vlan30 name=dhcp-vlan30

    /ip dhcp-server network
    add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=8.8.8.8,8.8.4.4 dhcp-server=dhcp-vlan10
    add address=192.168.20.0/24 gateway=192.168.20.1 dns-server=8.8.8.8,8.8.4.4 dhcp-server=dhcp-vlan20
    add address=192.168.30.0/24 gateway=192.168.30.1 dns-server=8.8.8.8,8.8.4.4 dhcp-server=dhcp-vlan30
    ```
*   Configure DHCPv6 Server for each VLAN:

   ```mikrotik
    /ipv6 dhcp-server
    add address-pool=vlan10-ipv6-pool interface=vlan10 name=dhcp6-vlan10  dns-server=2001:4860:4860::8888,2001:4860:4860::8844
    add address-pool=vlan20-ipv6-pool interface=vlan20 name=dhcp6-vlan20  dns-server=2001:4860:4860::8888,2001:4860:4860::8844
    add address-pool=vlan30-ipv6-pool interface=vlan30 name=dhcp6-vlan30  dns-server=2001:4860:4860::8888,2001:4860:4860::8844

    /ipv6 dhcp-server settings set store-leases-disk=yes
    ```

### 2.5 IP Routing

*   Basic routing is automatically done when the addresses are assigned to the interfaces, PPPoE default route is automatically added.

*   IPv6 configuration for routing and router advertisement:
    ```mikrotik
    /ipv6 settings set accept-router-advertisements=yes
    /ipv6 nd add interface=vlan10 advertise-dns=yes
    /ipv6 nd add interface=vlan20 advertise-dns=yes
    /ipv6 nd add interface=vlan30 advertise-dns=yes
    ```

### 2.6 Firewall and NAT

*   Basic firewall rules to allow established/related connections and drop invalid packets, allow specific ports:

    ```mikrotik
    /ip firewall filter
    add action=accept chain=input connection-state=established,related comment="Accept established and related connections"
    add action=accept chain=input protocol=udp dst-port=53 comment="Allow DNS UDP"
    add action=accept chain=input protocol=tcp dst-port=53 comment="Allow DNS TCP"
    add action=accept chain=input protocol=icmp comment="Allow ping"
    add action=drop chain=input connection-state=invalid comment="Drop invalid connections"
    add action=accept chain=forward connection-state=established,related comment="Accept Forward established and related connections"
    add action=drop chain=forward connection-state=invalid comment="Drop Forward invalid connections"
    add action=accept chain=forward in-interface=vlan10,vlan20,vlan30 out-interface=pppoe-out1 comment="Allow LAN to WAN"
    add action=drop chain=forward comment="Drop all other forward traffic"

    /ip firewall nat
    add action=masquerade chain=srcnat out-interface=pppoe-out1 comment="Masquerade LAN to WAN"
    ```
*   Basic IPv6 firewall rules to allow established/related connections and drop invalid packets:
    ```mikrotik
    /ipv6 firewall filter
    add action=accept chain=input connection-state=established,related comment="Accept established and related connections"
    add action=accept chain=input protocol=udp dst-port=53 comment="Allow DNS UDP"
    add action=accept chain=input protocol=tcp dst-port=53 comment="Allow DNS TCP"
    add action=accept chain=input protocol=icmpv6 comment="Allow ping IPv6"
    add action=drop chain=input connection-state=invalid comment="Drop invalid connections"
    add action=accept chain=forward connection-state=established,related comment="Accept Forward established and related connections"
    add action=drop chain=forward connection-state=invalid comment="Drop Forward invalid connections"
    add action=accept chain=forward in-interface=vlan10,vlan20,vlan30 out-interface=pppoe-out1 comment="Allow LAN to WAN"
    add action=drop chain=forward comment="Drop all other forward traffic"
    ```

### 2.7 RADIUS Configuration

*  Configure RADIUS client settings:
   ```mikrotik
   /radius
   add address=<radius_server_ip> secret=<radius_secret> timeout=3s service=ppp,login,hotspot
   ```
* Configure PPP secret to use RADIUS
    ```mikrotik
     /ppp secret
      add name=<ppp_user_name> service=ppp profile=default  disabled=no
      /ppp profile set default use-radius=yes
   ```

### 2.8 Quality of Service

* Basic queue to prioritize VOIP
    ```mikrotik
        /queue simple
        add max-limit=2M/2M name=VOIP queue=pcq-upload-default/pcq-download-default target=192.168.0.0/16 dst-port=5060,5061,10000-20000
    ```

### 2.9 Other Settings

* Basic WinBox config for safe access:

   ```mikrotik
     /tool mac-server set allowed-interface-list=none
     /tool mac-server mac-winbox set allowed-interface-list=none
     /ip service set api disabled=yes
     /ip service set ssh address=192.168.0.0/16
   ```

* Set NTP Client
   ```mikrotik
        /system ntp client set enabled=yes server-address=2.pool.ntp.org
   ```

## 3. Complete MikroTik CLI Configuration Commands

This section provides a consolidated list of the CLI commands used in the previous steps with detailed parameter explanations.

### 3.1 System Identity

*   `/system identity set name=<name>`
    *   `name`:  The name of the router (string).

### 3.2 System Package

*   `/system package update check`
    *   Checks for available updates

*   `/system package update install`
    * Installs any available updates
* `/system reboot`
    * Reboots the router

### 3.3 Interface PPPoE Client

*   `/interface pppoe-client add user=<user> password=<password> interface=<interface> name=<name> use-peer-dns=<yes|no> add-default-route=<yes|no>`
    *   `user`: The PPPoE username (string).
    *   `password`: The PPPoE password (string).
    *   `interface`: The physical interface (e.g., `ether1`).
    *   `name`: The name of the PPPoE client interface (string).
    *  `use-peer-dns`:  If set to yes it will use the DNS from the PPPoE server.
     *   `add-default-route`:  If set to yes, it will add a default route when the connection is established.

### 3.4 Interface VLAN

*   `/interface vlan add interface=<interface> name=<name> vlan-id=<vlan-id>`
    *   `interface`: The parent physical interface.
    *   `name`: The name of the VLAN interface (string).
    *   `vlan-id`: The VLAN ID (integer 1-4094).

### 3.5 IP Address

*   `/ip address add address=<ip/cidr> interface=<interface>`
    *   `address`: The IPv4 address and subnet mask in CIDR format.
    *   `interface`: The interface to assign the address.
*    `/ipv6 address add address=<ipv6/cidr> interface=<interface>`
     * `address`: The IPv6 address and subnet mask in CIDR format.
     *   `interface`: The interface to assign the address.

### 3.6 IP Pool

*   `/ip pool add name=<name> ranges=<range-start>-<range-end>`
    *   `name`: The name of the IP pool (string).
    *   `ranges`: The IPv4 address range (e.g., `192.168.10.10-192.168.10.254`).
*   `/ipv6 pool add name=<name> prefix=<prefix> prefix-length=<length>`
     *   `name`: The name of the IPv6 pool (string).
     *   `prefix`: The IPv6 prefix (e.g., `2001:db8:10::/64`).
     *   `prefix-length`: The prefix length (e.g., `64`).

### 3.7 IP DHCP Server

*   `/ip dhcp-server add name=<name> interface=<interface> address-pool=<pool>`
    *   `name`: The name of the DHCP server (string).
    *   `interface`: The interface to listen for DHCP requests.
    *   `address-pool`: The IP pool to use for leases.
* `/ip dhcp-server network add address=<network/cidr> gateway=<gateway> dns-server=<dns1>,<dns2> dhcp-server=<dhcp-name>`
     *   `address`: The network address range in CIDR format.
     *   `gateway`: The gateway address of the network.
     *   `dns-server`: The DNS server addresses separated by commas.
     * `dhcp-server`: The DHCP server name.

*   `/ipv6 dhcp-server add name=<name> interface=<interface> address-pool=<pool> dns-server=<dns1>,<dns2>`
    *   `name`: The name of the DHCPv6 server (string).
    *   `interface`: The interface to listen for DHCPv6 requests.
    *   `address-pool`: The IPv6 pool to use for leases.
    *   `dns-server`: The DNS server addresses separated by commas.
* `/ipv6 dhcp-server settings set store-leases-disk=<yes|no>`
    * `store-leases-disk`: If set to yes, it will store the leases on disk

### 3.8 IP Routing
*  `/ipv6 settings set accept-router-advertisements=<yes|no>`
   *  `accept-router-advertisements`: If set to yes it will accept router advertisements.
* `/ipv6 nd add interface=<interface> advertise-dns=<yes|no>`
   * `interface`: The interface that should send router advertisements.
   * `advertise-dns`: If set to yes it will send the DNS servers in router advertisements.

### 3.9 IP Firewall

*   `/ip firewall filter add action=<action> chain=<chain> ...`
    *   `action`:  `accept`, `drop`, `reject`.
    *   `chain`:  `input`, `forward`, `output`.
    *   Other parameters: `connection-state`, `protocol`, `dst-port`, etc.
* `/ipv6 firewall filter add action=<action> chain=<chain> ...`
    *   `action`:  `accept`, `drop`, `reject`.
    *   `chain`:  `input`, `forward`, `output`.
    *   Other parameters: `connection-state`, `protocol`, `dst-port`, etc.

*   `/ip firewall nat add action=masquerade chain=srcnat out-interface=<interface>`
    *   `action`:  `masquerade`, `src-nat`, `dst-nat`.
    *   `chain`:  `srcnat`, `dstnat`.
    *   `out-interface`: The interface to perform NAT on.

### 3.10 RADIUS

*  `/radius add address=<address> secret=<secret> timeout=<timeout> service=<service>`
   * `address`: RADIUS server IP address.
   * `secret`: shared secret with the RADIUS server.
   * `timeout`: Timeout before assuming the radius server is not reachable.
   * `service`: Type of authentication to use radius server for `ppp,login,hotspot`.
* `/ppp profile set default use-radius=<yes|no>`
   * `use-radius`: use RADIUS for authentication.
* `/ppp secret add name=<user>  service=ppp profile=default  disabled=no `
   *  `name`:  The ppp username that will use radius for authentication
    * `service`: Type of authentication to use for secret `ppp`.
    *  `profile`: Which profile to use for user settings.
    *  `disabled`: Enable/disable this user.

### 3.11 Quality of Service
* `/queue simple add max-limit=<upload>/<download> name=<name> target=<ip/cidr> dst-port=<port> queue=<queue>`
    * `max-limit`: Max limit to apply for this queue.
    * `name`: queue name.
    * `target`: IP address for traffic to be matched.
    * `dst-port`: Destination port to match.
    * `queue`: queue to use for this rule.

### 3.12  Winbox and other settings
* `/tool mac-server set allowed-interface-list=<list>`
    * `allowed-interface-list`: Allowed interfaces to connect to via MAC address `none`, `all`
* `/tool mac-server mac-winbox set allowed-interface-list=<list>`
    * `allowed-interface-list`: Allowed interfaces to connect to via MAC address using Winbox.
* `/ip service set api disabled=<yes|no>`
   * `disabled`: Enable/Disable API access.
* `/ip service set ssh address=<ip/cidr>`
    * `address`: IP address that is allowed to connect to via ssh.
* `/system ntp client set enabled=<yes|no> server-address=<address>`
    * `enabled`: Enable NTP client.
    * `server-address`: NTP server address.

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting & Diagnostics

### Pitfalls:

*   **Default Configuration Overload:**  MikroTik routers often come with a complex default configuration. Best practice is to clear the configuration.
*   **Firewall Misconfiguration:**  Incorrect firewall rules are the most common cause of connectivity issues. Use connection tracking effectively and keep rules specific.
*   **VLAN Tagging Issues:** Ensure VLAN IDs match on switches and the router. Check if the correct interface is configured as a trunk port.
*   **DHCP Server Configuration:** DHCP server misconfiguration can cause address conflicts. Ensure the correct pools are assigned to interfaces.
*   **IPv6 Issues:**  IPv6 can be more complex to configure correctly. Ensure correct router advertisements and addressing.
*   **Resource Usage:** High CPU load can be caused by complex firewall rules, QoS, or routing protocols.

### Troubleshooting:

*   **Connectivity Problems:**
    *   Use `ping` to check basic connectivity to different network locations.
    *   Use `traceroute` to see the path a packet takes.
    *   Check firewall rules using `/ip firewall filter print`.
    *   Check IP addresses assigned with `/ip address print`.
    *   Check for any routing issues with `/ip route print`.
*   **DHCP Problems:**
    *   Use `/ip dhcp-server lease print` to see currently allocated leases.
    *  Use `/ipv6 dhcp-server lease print` to see currently allocated leases.
    *   Check if IP pools are correctly configured and assigned to interfaces.
    *   Use `torch` to capture DHCP traffic.
*   **VLAN Issues:**
    *   Use `/interface vlan print` to check VLAN configuration.
    *   Check for link status on the trunk port.
    *  Check tagged/untagged state on the bridge.
*   **General Performance:**
    *   Use `/system resource print` to check CPU and memory usage.
    *   Use `/tool profile` to see which services are using the most resources.
    *  Use `/tool monitor traffic` to capture traffic statistics
*   **Log analysis**
   * Use `/log print` to view logs

### Diagnostics using MikroTik Built-in Tools:

*   **`ping`:** Basic connectivity test to hosts.
    ```mikrotik
    /ping 8.8.8.8
    /ping 2001:4860:4860::8888
    ```
*   **`traceroute`:** Shows the path packets take.
    ```mikrotik
    /traceroute 8.8.8.8
    /traceroute 2001:4860:4860::8888
    ```
*   **`torch`:** Real-time packet analyzer. Excellent for debugging traffic.
    ```mikrotik
    /tool torch interface=ether1
    ```
*   **`/system resource print`:**  Displays CPU, memory, and other system resources.
    ```mikrotik
    /system resource print
    ```
*   **`/ip firewall connection print`:**  Shows current firewall connections and their status.
    ```mikrotik
    /ip firewall connection print
    ```
*   **`/interface monitor-traffic`:**  Monitors real time interface traffic.
    ```mikrotik
    /interface monitor-traffic ether1
    ```
*   **`/log print`:** Shows system logs
    ```mikrotik
    /log print
    ```

## 5. Verification and Testing Steps

*   **Basic Internet Connectivity:**
    *   Check if devices can connect to the internet.
    *   Ping external addresses using IPv4 and IPv6.
*   **DHCP Lease Checks:**
    *   Verify that devices receive IP addresses via DHCP (IPv4 and IPv6).
    *   Check IP leases using `/ip dhcp-server lease print`.
    *   Check IP leases using `/ipv6 dhcp-server lease print`.
*   **VLAN Traffic:**
    *   Verify that devices connected to each VLAN can only communicate with other devices on the same VLAN (if no routing between VLANs is configured in the firewall).
    *   Use `ping` between devices in the same VLAN.
*   **Firewall Rules:**
    *   Check connectivity to allowed ports and addresses.
    *   Test denied access to disallowed resources.
*   **RADIUS Authentication:**
   * Connect via PPP to the router and check the logs to confirm RADIUS was used.
*   **Quality of Service**
   * Test VOIP quality.
   * Download files and make calls and test how the router is shaping the traffic.

## 6. Related MikroTik-Specific Features, Capabilities, & Limitations

*   **Bridging and Switching:** MikroTik routers can act as both Layer 2 (bridging) and Layer 3 (routing) devices.  Multiple interfaces can be combined into a bridge for Layer 2 forwarding or a switch chip can be configured with VLAN capabilities.
*   **MAC Server:** Allows management of the router using its MAC address. Can be restricted to specific interfaces for security.
*   **RoMON:** MikroTik's Router Management Overlay Network. A proprietary protocol for managing MikroTik devices in a network.
*   **WinBox:**  MikroTik's GUI management tool. It allows you to configure the router via the GUI. Can be restricted to specific IP addresses.
*   **Certificates:** RouterOS allows the usage of certificates for secure communication with services like HTTPS or VPN connections.
*   **PPP AAA (Authentication, Authorization, Accounting):** Used to authenticate users for PPP connections.
*   **RADIUS:** A standard protocol for centralized user authentication.
*   **User / User groups:**  You can define user accounts and assign them to groups with limited privileges.
*   **MACVLAN:** Allows the creation of multiple virtual interfaces on a single physical interface with unique MAC addresses.
*   **L3 Hardware Offloading:** Certain MikroTik devices support hardware offloading of Layer 3 routing to reduce CPU utilization.
*   **MACsec:**  Layer 2 security protocol for encrypting Ethernet links.
*   **Quality of Service (QoS):** Allows control of the bandwidth used by different types of traffic (e.g. prioritising VoIP traffic).
*   **Switch Chip Features:**  MikroTik switch chips have hardware VLAN, port isolation, and other features.
*   **VLAN (Virtual LANs):** Provides logical separation of networks.
*   **VXLAN:** Virtual Extensible LAN, a Layer 2 overlay network protocol.
*   **Connection Tracking:** Keeps track of active connections, crucial for proper firewall functionality.
*   **NAT (Network Address Translation):** Maps internal IP addresses to a public IP address for internet access.
*  **Firewall and QoS Case Studies:** Complex examples to build out larger networks.
*  **Kid Control:** Set up rules for kid's computer usage.
*  **UPnP, NAT-PMP:** Enable easy port forwarding for internal devices.
*   **IP Services (DHCP, DNS, SOCKS, Proxy):**  MikroTik devices can act as various network services.
*   **High Availability Solutions (Load Balancing, Bonding, VRRP):** Implement features for high-availability and redundancy.
*  **Mobile Networking (GPS, LTE, PPP, SMS):** Enables connectivity with cellular providers.
*   **Multi-Protocol Label Switching (MPLS):**  A high-performance traffic-forwarding mechanism.
*   **Network Management (ARP, Cloud, DHCP, DNS, SOCKS, Proxy):**  Tools to manage network settings.
*   **Routing (OSPF, RIP, BGP, RPKI, VRF):**  Implement various routing protocols for complex network topologies.
*   **System Information and Utilities:**  Tools to get information about the system.
*   **Virtual Private Networks (IPsec, L2TP, WireGuard, etc.):** Establish VPN tunnels for secure communication.
*   **Wired Connections:** Support for Ethernet interfaces and other interfaces.
*   **Wireless (WiFi, CAPsMAN, Mesh):** Allows the configuration of Wireless Networks.
*   **Internet of Things (Bluetooth, GPIO, Lora, MQTT):**  Support for IoT protocols.
*   **Hardware (Disks, LEDs, Ports, USB):**  Configuration of the hardware.
*   **Diagnostics, Monitoring, and Troubleshooting:** Built-in tools for diagnostics.
*   **Extended Features (Containers, DLNA, SMB):** Various additional features.
*   **Limitations:**
    *   Resource limits based on router hardware.
    *   Complexity can lead to misconfiguration if not done properly.
    *   Performance impacts with high firewall rules and complicated QoS setups.

## 7. MikroTik REST API Examples (Where Applicable)

MikroTik API can be accessed over `https` and basic authentication is used.

**Note:** API is disabled by default on most devices, ensure it is enabled using `/ip service set api disabled=no`

**API Endpoint:** `https://<router_ip>/rest/`

**Authentication:** Basic Authentication - provide your MikroTik user credentials.

**Example 1: Get List of Interfaces**

*   **API Endpoint:** `https://<router_ip>/rest/interface`
*   **Method:** `GET`
*   **Request (curl):**
    ```bash
    curl -k -u <username>:<password> https://<router_ip>/rest/interface
    ```
*   **Expected Response (JSON):**
    ```json
     [
      {
        "id": "*1",
        "name": "ether1",
        "type": "ether",
        "mtu": "1500",
        "actual-mtu": "1500",
        "mac-address": "XX:XX:XX:XX:XX:XX",
        "rx-rate": "0",
        "tx-rate": "0",
        "last-link-down-time": "00:00:00",
        "last-link-up-time": "00:00:00",
        "link-downs": "0",
        "running": "true",
        "enabled": "true",
        "disabled": "false"
      },
      {
        "id": "*2",
        "name": "ether2",
        "type": "ether",
        "mtu": "1500",
        "actual-mtu": "1500",
        "mac-address": "XX:XX:XX:XX:XX:XX",
        "rx-rate": "0",
        "tx-rate": "0",
        "last-link-down-time": "00:00:00",
        "last-link-up-time": "00:00:00",
        "link-downs": "0",
        "running": "true",
        "enabled": "true",
        "disabled": "false"
      }
     ]
    ```

**Example 2: Create a New VLAN Interface**

*   **API Endpoint:** `https://<router_ip>/rest/interface/vlan`
*   **Method:** `POST`
*   **Request (curl):**
    ```bash
    curl -k -u <username>:<password> -H "Content-Type: application/json" -X POST -d '{"interface": "ether2", "name": "vlan40", "vlan-id": 40}' https://<router_ip>/rest/interface/vlan
    ```
*   **Request Payload (JSON):**

    ```json
    {
        "interface": "ether2",
        "name": "vlan40",
        "vlan-id": 40
    }
    ```

*   **Expected Response (JSON):**
    ```json
    {
      "id": "*3"
    }
    ```
   `*3` is the generated id of the new vlan.

**Example 3: Get a specific IP address**

*  **API Endpoint:** `https://<router_ip>/rest/ip/address/<id>`
* **Method:** `GET`
* **Request (curl):**
    ```bash
     curl -k -u <username>:<password> https://<router_ip>/rest/ip/address/*1
   ```
*  **Expected Response (JSON):**
  ```json
 {
    "id": "*1",
    "address": "192.168.10.1/24",
    "interface": "vlan10",
    "actual-interface": "vlan10",
    "invalid": "false",
    "dynamic": "false"
  }
 ```

## 8. In-Depth Explanations of Core Concepts

*   **Bridging:**  MikroTik bridges combine multiple Ethernet interfaces into a single logical Layer 2 segment. This enables multiple devices to connect to a single interface and all act on the same subnet.
*   **Routing:**  MikroTik devices are primarily routers. They can route traffic between different subnets by reading the destination IP and forwarding the traffic to the correct interface via routing protocols.
*   **Firewall:**  A critical security component. Connection tracking is important for stateful firewalls. In RouterOS the rules are processed in order so it is important to order the rules properly. The firewall blocks by default all the traffic that is not configured.
*   **Connection Tracking:**  The firewall keeps track of connection states. The main purpose is to allow established and related traffic automatically and drop other traffic. This allows the admin to only allow the specific traffic that needs to go in and out of the router.
*   **NAT:** Allows internal devices to access the internet using the router's public IP. Important for privacy and to avoid public IP exhaustion. It is common to use masquerading for source nat.

## 9. Security Best Practices Specific to MikroTik Routers

*   **Change Default Credentials:** Change the default admin password. Create a new user with admin privileges and disable the default admin account.
*   **Restrict Access:**  Limit access to Winbox, SSH, and other services using IP address restrictions.
    ```mikrotik
        /ip service set ssh address=192.168.0.0/24
    ```
*   **Disable Unused Services:**  Disable services like `api` if not needed.
    ```mikrotik
       /ip service set api disabled=yes
    ```
*   **Secure MAC-Server:** Configure the MAC server to only be enabled on the specific ports when debugging or setting up the router.
    ```mikrotik
       /tool mac-server set allowed-interface-list=none
       /tool mac-server mac-winbox set allowed-interface-list=none
    ```
*   **Firewall Rules:**  Use a restrictive firewall policy.  Drop all traffic that is not required.
    ```mikrotik
        /ip firewall filter add action=drop chain=input comment="Drop all other input traffic"
    ```
*   **Keep RouterOS Updated:** Patch your RouterOS with the latest version.
    ```mikrotik
       /system package update check
       /system package update install
       /system reboot
    ```
*   **Secure Remote Access:** Use VPNs (IPSec, WireGuard) for secure remote access instead of opening up management ports to the internet.
*   **Monitor Logs Regularly:** Check logs for suspicious activity.
    ```mikrotik
       /log print
    ```
*  **Implement RADIUS for Centralized Authentication:** Centralize authentication for all users using RADIUS server.
*  **Use HTTPS for API Access:** Ensure you are using HTTPS when accessing the API and use a secure password.

## 10. Detailed Explanation and Configuration for Each Topic

All the topics have already been covered in the previous sections in a practical format, providing configuration examples, troubleshooting and security information.

---

This document provides a highly detailed and expert-level view of IP addressing and related topics in MikroTik RouterOS.  It offers practical examples, troubleshooting, and