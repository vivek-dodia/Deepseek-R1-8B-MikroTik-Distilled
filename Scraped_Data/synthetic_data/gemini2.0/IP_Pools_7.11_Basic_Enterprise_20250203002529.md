Okay, let's dive into a comprehensive documentation focusing on IP Pools within MikroTik RouterOS 7.11, suitable for an enterprise-level network. This will cover many aspects of RouterOS, particularly related to IP Pool functionality.

## Comprehensive Documentation: IP Pools in MikroTik RouterOS 7.11 (Enterprise Level)

### 1. Configuration Scenario and MikroTik Requirements

**Scenario:** An enterprise network with multiple departments requiring separate IP address ranges for security and management purposes. We need to create three distinct IP pools for different departments:
* **Pool-HR:** For Human Resources (192.168.10.0/24)
* **Pool-Eng:** For Engineering (192.168.20.0/24)
* **Pool-Guest:** For guest wifi (10.10.10.0/24)

**MikroTik Requirements:**
* RouterOS 7.11 (or compatible 7.x/6.x)
* Knowledge of basic networking concepts
* CLI access (or Winbox)

### 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

**A. CLI Implementation:**

*   **Step 1: Access the Router via CLI:**
    *   Use SSH or the terminal in Winbox to access the router's command line interface.

*   **Step 2: Create IP Pools:**
    ```mikrotik
    /ip pool
    add name="Pool-HR" ranges="192.168.10.10-192.168.10.254"
    add name="Pool-Eng" ranges="192.168.20.10-192.168.20.254"
    add name="Pool-Guest" ranges="10.10.10.10-10.10.10.254"
    ```
* **Step 3: Verify created IP Pools:**
    ```mikrotik
    /ip pool print
    ```
**B. Winbox Implementation:**

*   **Step 1:** Launch Winbox and connect to your MikroTik Router.
*   **Step 2:** Navigate to *IP* -> *Pool* in the left sidebar.
*   **Step 3:** Click the "+" button to add a new pool.
*   **Step 4:** Configure each pool:
    *   **Name:** Pool-HR
    *   **Ranges:** 192.168.10.10-192.168.10.254
    *   Click "Apply" and "OK".
    * Repeat steps for the other pools (Pool-Eng and Pool-Guest)
*  **Step 5:** Verify created IP Pools

### 3. Complete MikroTik CLI Configuration Commands

**Creating an IP Pool:**

```mikrotik
/ip pool add \
    name="<pool_name>" \
    ranges="<ip_range_start>-<ip_range_end>" \
    next-pool="<next_pool_name>" \
    comment="<description>"
```

**Parameters:**

| Parameter    | Description                                                   | Required |
|--------------|---------------------------------------------------------------|----------|
| `name`       | Unique name for the IP pool.                                  | Yes      |
| `ranges`     | The IP address range(s) to be used in format `start-end`. Can have multiple ranges comma seperated  | Yes      |
| `next-pool`  | If the current pool is exhausted, use this pool.                | No       |
| `comment`    | Optional descriptive comment.                                 | No       |

**Example (Pool-HR):**

```mikrotik
/ip pool add name="Pool-HR" ranges="192.168.10.10-192.168.10.254" comment="IP Pool for Human Resources"
```

**Displaying IP Pools:**

```mikrotik
/ip pool print
```

**Removing an IP Pool:**

```mikrotik
/ip pool remove [find name="<pool_name>"]
```

**Example (Removing Pool-HR):**

```mikrotik
/ip pool remove [find name="Pool-HR"]
```

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

* **Overlapping IP Ranges:** Ensure IP pool ranges don't overlap with each other or existing network infrastructure.
* **Incorrect Syntax:** Verify correct syntax when entering IP ranges (e.g. `192.168.1.10-192.168.1.254` or `192.168.1.10, 192.168.1.25-192.168.1.250`)
* **Exhausted Pools:** If a pool is exhausted, new devices might not get IP addresses. Use the `next-pool` attribute to specify a fallback.
* **Misconfiguration in DHCP Server:** DHCP server using IP Pool can cause conflicts if wrong pools are assigned
* **Firewall rules:** Firewall rule can prevent IP from receiving IPs from DHCP

**Troubleshooting:**

*   **Check IP Pool Configuration:**
    ```mikrotik
    /ip pool print
    ```
    *   Verify the ranges and names are correct.
*   **Check DHCP Server:**
    ```mikrotik
    /ip dhcp-server print
    ```
    *   Ensure the DHCP server is using the correct IP pool for each network.

*   **Check Logs:**
    ```mikrotik
    /log print
    ```
    *   Look for any errors related to IP pools or DHCP.

*   **Verify Interface Status:**
    ```mikrotik
    /interface print
    ```
    *   Ensure interfaces are enabled and correctly configured.
* **Using Torch:**
    ```mikrotik
    /tool torch interface=<interface-name>
    ```
    * Check that DHCP traffic can be seen in the specified interface. If the server is sending offer and the client is not getting, it would mean a block of some sort is present in the path.

**Diagnostics:**
* Utilize Winbox’s logging functionality to monitor system events and pinpoint misconfigurations.
* Use the `torch` tool to analyze network traffic to identify if packets are being dropped.
* Use the `/tool traceroute` to understand network paths

### 5. Verification and Testing

*   **Ping:** After assigning IP addresses from a pool, try to ping devices within the same and different pools to check connectivity.
    ```mikrotik
    /ping <ip_address>
    ```
    * Example: `ping 192.168.10.15`
*   **Traceroute:** Use traceroute to diagnose pathing to the IP addresses
    ```mikrotik
     /tool traceroute <ip_address>
    ```
    * Example `traceroute 192.168.10.15`
*   **Monitor Interfaces:** Monitor traffic and check for any issues with interface configuration.
   *   Use `/interface monitor-traffic <interface>`

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Limitations:**
    *   IP Pools are static, meaning they do not dynamically adjust.
    *   Pools are associated with DHCP servers and/or specific configurations.
    *  RouterOS is not capable of automatically growing IP Pool sizes

*   **Features:**
    *   IP Pools can be used with DHCP, Hotspot, and other services.
    *   You can utilize several different ranges within one IP pool.
    *   The `next-pool` feature allows for seamless transitions to another IP range when a pool is exhausted.

### 7. MikroTik REST API Examples

* **Authentication**
 MikroTik API uses token-based authentication, a new session should be established before performing any command
 ```bash
 # Login
 curl -X POST -H "Content-Type: application/json" -d '{"user": "apiuser", "password": "apipassword"}' https://<router_ip>/rest/user/login
# The response will have the token: {"token": "abcdefgh"}
 ```
*   **Get All IP Pools:**
    *   **Endpoint:** `/ip/pool`
    *   **Method:** GET
    *  **Example cURL:**
       ```bash
       curl -H "Authorization: Bearer abcdefgh" https://<router_ip>/rest/ip/pool
       ```

    *  **Example JSON Response:**
        ```json
        [
          {
              "id": "*1",
              "name": "Pool-HR",
              "ranges": "192.168.10.10-192.168.10.254",
              "next-pool": "",
              "comment": "IP Pool for Human Resources",
               ".id": "*1"
          },
          {
             "id": "*2",
             "name": "Pool-Eng",
             "ranges": "192.168.20.10-192.168.20.254",
             "next-pool": "",
              "comment": null,
              ".id": "*2"
          },
          {
             "id": "*3",
             "name": "Pool-Guest",
             "ranges": "10.10.10.10-10.10.10.254",
             "next-pool": "",
              "comment": null,
               ".id": "*3"
          }
        ]
        ```
*   **Create an IP Pool:**
    *   **Endpoint:** `/ip/pool`
    *   **Method:** POST
    *  **Example cURL:**
       ```bash
       curl -X POST -H "Authorization: Bearer abcdefgh" -H "Content-Type: application/json" -d '{"name": "Pool-Dev", "ranges": "192.168.30.10-192.168.30.254", "comment": "IP Pool for Development"}' https://<router_ip>/rest/ip/pool
       ```
    *   **Example JSON Response:**
        ```json
        {
          "id": "*4",
          "name": "Pool-Dev",
          "ranges": "192.168.30.10-192.168.30.254",
          "next-pool": "",
           "comment": "IP Pool for Development",
           ".id": "*4"
        }

        ```
*   **Update an IP Pool:**
    *   **Endpoint:** `/ip/pool/<id>`
    *   **Method:** PUT
    *   **Example cURL:**
          ```bash
           curl -X PUT -H "Authorization: Bearer abcdefgh" -H "Content-Type: application/json" -d '{"comment": "Updated comment for the pool"}' https://<router_ip>/rest/ip/pool/*1
           ```
    *   **Example JSON Response:**
        ```json
        {
          "id": "*1",
          "name": "Pool-HR",
          "ranges": "192.168.10.10-192.168.10.254",
          "next-pool": "",
          "comment": "Updated comment for the pool",
           ".id": "*1"
        }
        ```

* **Delete an IP Pool**
    * **Endpoint:** `/ip/pool/<id>`
    * **Method:** DELETE
    * **Example cURL:**
    ```bash
    curl -X DELETE -H "Authorization: Bearer abcdefgh" https://<router_ip>/rest/ip/pool/*4
    ```
    *  **Example JSON Response:**
    ```json
     {"message": "removed"}
    ```

### 8. In-Depth Explanations of Core Concepts (MikroTik Implementation)

*   **Bridging:** MikroTik bridges group different network interfaces, to allow devices connected to those interfaces to be in the same network. MikroTik bridges operate at layer 2. VLAN tags can be used on bridge interfaces for segmentation, allowing for multiple networks on same physical link.
*   **Routing:** MikroTik uses IP routing to move packets between networks. Each interface should belong to an IP network, that is used to determine to which interface a packet should be forwarded. MikroTik can have multiple routing tables for different scenarios.
*   **Firewall:** MikroTik's firewall provides robust filtering and NAT capabilities. Uses `chain` as entry points for the rules. Firewall rules are processed sequentially, meaning rule order is extremely important.
    *   **NAT (Network Address Translation):** Used for modifying source or destination address of a packet, usually used for connecting private network behind a public interface.
    *   **Connection Tracking:** MikroTik uses connection tracking to track network flows. This is used to implement stateful firewall rules.
    *   **Packet Flow:** Packet enters a MikroTik device through an interface and then is sent to the firewall, then the routing table, and after that the interface again.
*   **DHCP Server:** MikroTik DHCP servers provide addresses to clients in a specified network using IP Pools. DHCP servers can handle multiple networks.
*  **VLAN**: VLANs are used to segment a network at the Layer 2 level. VLANs use VLAN tags to distinguish traffic belonging to different networks, and they can be used in conjunction with bridges and interfaces to allow different networks in the same physical connection.
*  **VXLAN**: VXLAN is a tunneling protocol, used to extend layer 2 segments over layer 3. It allows for creating virtual networks that span multiple locations.
*   **QoS:** Quality of Service in MikroTik allows for shaping and prioritizing network traffic. Queues, mangle and traffic policies are used in conjunction to limit traffic.

### 9. Security Best Practices Specific to MikroTik Routers

*   **Change Default Password:** Always change the default admin password immediately.
*   **Disable Unnecessary Services:** Disable services that are not needed (e.g., telnet, api-ssl if not needed).
    ```mikrotik
    /ip service disable telnet
    /ip service disable api-ssl
    ```
*   **Implement Firewall Rules:** Set up a robust firewall to block unwanted connections, and allow only necessary connections.
*   **Secure Winbox Access:** Restrict access to Winbox from specific IP addresses.
    ```mikrotik
    /ip service set winbox address=192.168.1.0/24
    ```
*   **Regularly Update RouterOS:** Keep RouterOS and firmware updated with the latest versions.
*   **Use Strong Authentication:** Employ strong authentication for all services, if possible use SSH key-based authentication for API and SSH.
*   **Disable Neighbor Discovery:** Neighbor Discovery is used to discover MikroTik devices in same networks, if not needed it should be disabled.
*  **Use HTTPS for API:** Use HTTPS and certificates to encrypt traffic, as well as API authentication to ensure security.
*  **Regularly check logs:** To check for unusual activity, and be aware of system changes.

### 10. Detailed Explanations and Configuration Examples

#### IP Addressing (IPv4 and IPv6)

*   **IPv4:**
    *   Configuration example:
    ```mikrotik
     /ip address
    add address=192.168.1.1/24 interface=ether1
    ```
    *   IP addressing uses subnet masks to define the network portion of the IP.

*   **IPv6:**
    *   Configuration example:
      ```mikrotik
    /ipv6 address
     add address=2001:db8::1/64 interface=ether1
    ```
    *   IPv6 uses 128 bit address and is usually represented by hexadecimal.

#### IP Settings
*   **IP settings** define general parameters for IP addressing and behavior.
     *   Configuration example:
      ```mikrotik
      /ip settings set allow-fast-path=yes
      /ip settings set tcp-syncookies=yes
       ```

#### MAC server

*   **MAC server** allows for the configuration of MAC addresses that can access the router via MAC address, rather than IP address.
   *   Configuration example:
       ```mikrotik
        /tool mac-server print
        /tool mac-server set enabled=yes interfaces=all
      ```

#### RoMON
*   **RoMON** allows for remote monitoring of other RouterOS devices via MAC address, used for advanced management.
   *   Configuration example:
       ```mikrotik
        /tool romon print
        /tool romon set enabled=yes
      ```

#### WinBox
*  **WinBox** is a GUI tool for MikroTik management. It allows access to all device configurations in a graphical format.
   *  Configuration example:
      *  To enable Winbox:
      ```mikrotik
       /ip service set winbox disabled=no
       ```
#### Certificates
*  **Certificates** are used for encrypting traffic using protocols like SSL/TLS, needed for secure access to the device.
  *  Configuration example:
   * To generate certificate:
   ```mikrotik
   /certificate
   add name=routerCA common-name=myCA key-usage=key-cert-sign,crl-sign
    /certificate sign routerCA ca=yes
   add name=routerCert common-name=router.example.com key-usage=tls-server
    /certificate sign routerCert ca=routerCA
   ```

#### PPP AAA
*   **PPP AAA** provides authentication, authorization, and accounting functions for PPP connections (e.g. PPPoE, L2TP).
    *  Configuration example:
     ```mikrotik
     /ppp profile
     add name=ppp-profile local-address=192.168.1.10 remote-address=Pool-HR use-encryption=yes
     ```
#### RADIUS
*  **RADIUS** is a network protocol that allows centralized authentication and authorization, usually used in conjunction with PPP AAA.
    *   Configuration example:
     ```mikrotik
     /radius
     add address=192.168.2.1 secret="mysecret" service=ppp,login
     ```

#### User / User groups
*   **User / User groups** allows the creation and management of users on the RouterOS device.
    *  Configuration example:
    ```mikrotik
     /user group
      add name="admin-group" policy=admin
     /user
      add name="adminuser" group="admin-group" password="mypassword"
    ```
#### Bridging and Switching
*   **Bridging and Switching:** Used for connecting multiple network interfaces and allowing them to operate at Layer 2.
    *   Configuration example:
       ```mikrotik
        /interface bridge
         add name=bridge1
        /interface bridge port
         add bridge=bridge1 interface=ether1
         add bridge=bridge1 interface=ether2
        ```

#### MACVLAN
*   **MACVLAN** creates virtual network interfaces based on the physical interfaces, each with it's own MAC address.
   *   Configuration example:
      ```mikrotik
       /interface macvlan
        add mac-address=00:00:00:00:00:01 interface=ether1 name=macvlan1
       /ip address add address=192.168.2.1/24 interface=macvlan1
      ```

#### L3 Hardware Offloading
*   **L3 Hardware Offloading** uses dedicated hardware for routing of packets, used for devices with specific chipsets, for improved performance.
   *    Configuration example:
        ```mikrotik
        /interface ethernet set ether1 l3-hw-offloading=yes
        ```
#### MACsec
*   **MACsec** uses MAC layer encryption to provide point to point security at Layer 2.
   *   Configuration example:
        ```mikrotik
        /interface macsec add name=macsec1 interface=ether1 key="00112233445566778899aabbccddeeff"  cipher=aes-128-gcm
        ```

#### Quality of Service
*   **Quality of Service:** Configures rules to prioritize and limit certain types of traffic.
    *   Configuration example:
       ```mikrotik
        /queue tree
        add name="downstream" parent=global-in max-limit=10M
        add name="upstream" parent=global-out max-limit=5M
       /queue simple
       add target=192.168.1.0/24 max-limit=1M/2M name=user-traffic
       ```

#### Switch Chip Features
*  **Switch Chip Features:** On router devices with switch chips, the switch can be used to do hardware switching, greatly improving local area network performance.
     *   Configuration example:
        ```mikrotik
          /interface ethernet switch port
           print
        /interface ethernet switch port set  ether2 switch=switch1 vlan-header=add-if-missing
        ```
#### VLAN
*   **VLANs:** Used to logically separate network segments on a single physical link.
    *   Configuration example:
        ```mikrotik
        /interface vlan
          add name=vlan10 vlan-id=10 interface=ether1
         /ip address
           add address=192.168.10.1/24 interface=vlan10
         ```
#### VXLAN
*   **VXLAN:** Allows for creating Layer 2 networks on top of layer 3 by using tunnel encapsulation.
    *   Configuration example:
        ```mikrotik
         /interface vxlan
         add name=vxlan1 vxlan-id=1000 interface=ether1 remote-address=192.168.2.2
        ```

#### Firewall and Quality of Service

*   **Connection Tracking:** Tracks TCP/UDP sessions, used for stateful filtering.

*   **Firewall:** Rules for filtering, NAT, and mangling packets.
    ```mikrotik
    /ip firewall filter
    add chain=forward action=accept connection-state=established,related
    add chain=forward action=drop in-interface-list=WAN
    ```

*   **Packet Flow in RouterOS:** Packet enters through interface -> Firewall -> Routing Table ->Interface again

*  **Queues:** Configures traffic shaping and limiting.

* **Firewall and QoS Case Studies:**
   *  **Basic firewall:**
     *  Drop all incoming on WAN
       ```mikrotik
       /ip firewall filter add action=drop chain=input in-interface-list=WAN
      ```
    * Allow only local access
     ```mikrotik
       /ip firewall filter add action=accept chain=input in-interface-list=LAN
     ```

*  **Kid Control:** Using firewall rules and queues to limit traffic for certain devices.

*  **UPnP (Universal Plug and Play):** Allows automatic port forwarding for local devices.
  ```mikrotik
    /ip upnp set enabled=yes
  ```

*  **NAT-PMP (NAT Port Mapping Protocol):** Alternative port mapping method, if needed.
  ```mikrotik
   /ip upnp set nat-pmp-enabled=yes
  ```

#### IP Services (DHCP, DNS, SOCKS, Proxy)
*  **DHCP Server:** Automatically assigns IP addresses to clients.
    ```mikrotik
    /ip dhcp-server
    add address-pool=Pool-HR interface=ether2 name=dhcp1
    /ip dhcp-server network
     add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=1.1.1.1
    ```

*   **DNS:** Configures local DNS server for queries.
    ```mikrotik
    /ip dns
    set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8
   ```
*   **SOCKS:** SOCKS proxy service on the router.
    ```mikrotik
     /ip socks
      set enabled=yes address=0.0.0.0 port=1080
    ```

*   **Proxy:** Web proxy service on the router.
    ```mikrotik
    /ip proxy set enabled=yes src-address=0.0.0.0 port=8080
   ```

#### High Availability Solutions

*   **Load Balancing:** Distribute traffic among multiple links for redundancy.
*   **Bonding:** Combines multiple interfaces into a single logical link.
    *   Configuration example:
     ```mikrotik
     /interface bonding add mode=802.3ad name=bonding1 interfaces=ether1,ether2
      /ip address add address=192.168.3.1/24 interface=bonding1
     ```
*   **Bonding Examples:** Active backup, load balancing, IEEE 802.3ad.
*   **HA Case Studies:** Scenarios with load balancing and redundancy.
*   **Multi-chassis Link Aggregation Group:** Bonding interfaces from different devices (requires compatible hardware).

*   **VRRP:** Virtual Router Redundancy Protocol.
    *   Configuration example:
       ```mikrotik
      /interface vrrp add interface=ether1 priority=100 vrid=10 name=vrrp1 virtual-address=192.168.1.100
      /ip address add address=192.168.1.1/24 interface=ether1
      ```
*   **VRRP Configuration Examples:** Using VRRP for failover.

#### Mobile Networking

*   **GPS:** Configures GPS for location tracking.
    ```mikrotik
   /system gps
    set enabled=yes
    ```
*   **LTE:** Configures LTE/4G/5G interfaces.
   ```mikrotik
   /interface lte add name=lte1 apn=internet
   ```

*   **PPP:** Configures dial-up connections.
    ```mikrotik
     /interface ppp-client add name=ppp1 user="username" password="password" interface=lte1
    ```
*   **SMS:** Allows sending and receiving SMS messages (on devices that support).
*   **Dual SIM Application:** Configuration for dual sim routers.

#### Multi Protocol Label Switching - MPLS
*   **MPLS Overview:** Provides packet forwarding based on labels rather than IP addresses.
*   **MPLS MTU:** Maximum Transmission Unit for MPLS frames.
*   **Forwarding and Label Bindings:** How labels are distributed and mapped to routes.
*   **EXP bit and MPLS Queuing:** Quality of Service using MPLS labels.
*   **LDP:** Label Distribution Protocol, used for allocating labels.
*   **VPLS:** Virtual Private LAN Service, for bridging layer 2 over MPLS networks.
*   **Traffic Eng:** Traffic Engineering used for path control and traffic distribution.
*   **MPLS Reference:** Detailed reference information for MPLS.

#### Network Management
*  **ARP:** Address Resolution Protocol.
    ```mikrotik
    /ip arp print
    /ip arp add address=192.168.1.10 mac-address=00:00:00:00:00:01 interface=ether1
    ```
*   **Cloud:** Connects the router to MikroTik cloud for management and backup.
    ```mikrotik
    /system cloud set enabled=yes
    ```
*   **DHCP:** Provides IP addressing to network clients.

*   **DNS:** DNS server settings.
    ```mikrotik
    /ip dns set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8
    ```
* **SOCKS:** For SOCKS proxy service.

* **Proxy:** For web proxy service.

*   **Openflow:** Configures Openflow settings for software-defined networking.

#### Routing
*   **Routing Protocol Overview:** Overview of protocols like OSPF, RIP, and BGP.
*   **Moving from ROSv6 to v7 with examples:**
    *    Main changes are regarding routing tables and routing protocols, make sure that they are set correctly when changing versions.
*   **Routing Protocol Multi-core Support:** RouterOS v7 uses multi-core processor for routing, for increased performance.
*   **Policy Routing:** Allows routing based on specific criteria, like source address or other attributes.

*   **Virtual Routing and Forwarding - VRF:** Allows creating different routing tables for the same router.
     ```mikrotik
     /routing vrf add name=vrf1 route-distinguisher=100:1
     /ip address add address=10.10.10.1/24 interface=ether2 routing-mark=vrf1
     /routing rule add dst-address=10.10.10.0/24 table=vrf1
     ```
*   **OSPF:** Open Shortest Path First routing protocol.

*   **RIP:** Routing Information Protocol.

*   **BGP:** Border Gateway Protocol.

*  **RPKI:** Resource Public Key Infrastructure, for securing BGP routes.

*   **Route Selection and Filters:** Modifying routes based on attributes.

*   **Multicast:** For multicast routing.

*   **Routing Debugging Tools:** Tools for monitoring and debugging routes.

*   **Routing Reference:** Details about routing settings.
* **BFD:** Bidirectional Forwarding Detection, used to detect connection loss.

*   **IS-IS:** Intermediate System to Intermediate System routing protocol.

#### System Information and Utilities

*   **Clock:** System time settings.
    ```mikrotik
    /system clock set time=12:00:00 date=jan/01/2024
    ```
*   **Device-mode:** Set device mode to router, bridge or other.
*   **E-mail:** Configure email notification on certain events.
*   **Fetch:** Download files using http or ftp.
    ```mikrotik
    /tool fetch url="http://example.com/file.txt"
    ```
*   **Files:** Manage device files.
    ```mikrotik
    /file print
    ```
*  **Identity:** Set Router identity.
    ```mikrotik
   /system identity set name=router1
    ```
*   **Interface Lists:** Lists used for grouping interfaces.

*   **Neighbor discovery:** Discovers neighboring devices.
*   **Note:** Add notes for documentation purposes.
*   **NTP:** Configure Network Time Protocol.
  ```mikrotik
   /system ntp client set enabled=yes primary-ntp=time1.google.com secondary-ntp=time2.google.com
  ```
*   **Partitions:** Disk partition management.
*   **Precision Time Protocol:** Configure Precision Time Protocol.
*   **Scheduler:** Configure scheduled jobs.
    ```mikrotik
    /system scheduler add name=myscript on-event="/system script run myscript" start-time=00:00 interval=1d
    ```
*   **Services:** Services running on the router.

*   **TFTP:** Trivial File Transfer Protocol, used for server access.

#### Virtual Private Networks

*   **6to4:** IPv6 transition technology.
*   **EoIP:** Ethernet over IP tunneling protocol.
   ```mikrotik
   /interface eoip add name=eoip1 remote-address=192.168.2.2 tunnel-id=100 interface=ether1
   ```
*   **GRE:** Generic Routing Encapsulation tunneling protocol.
    ```mikrotik
   /interface gre add name=gre1 remote-address=192.168.2.2 local-address=192.168.1.1
   ```
*   **IPIP:** IP over IP tunneling protocol.
  ```mikrotik
  /interface ipip add name=ipip1 local-address=192.168.1.1 remote-address=192.168.2.2
  ```
*   **IPsec:** IP security, provides encrypted connection.
  ```mikrotik
  /ip ipsec proposal
   add name=proposal1 auth-algorithms=sha256 enc-algorithms=aes-256-cbc lifetime=1h
  /ip ipsec policy
  add proposal=proposal1  src-address=192.168.1.0/24 dst-address=192.168.2.0/24 tunnel=yes
  /ip ipsec peer add address=192.168.2.2 secret=mypassword
  ```
*   **L2TP:** Layer 2 Tunneling Protocol.
    ```mikrotik
  /interface l2tp-server server set enabled=yes use-ipsec=yes
  /ppp secret add name=l2tpuser password=mypassword service=l2tp
  /ip ipsec proposal
  add auth-algorithms=sha256 enc-algorithms=aes-256-cbc lifetime=1h name=myproposal
  /ip ipsec policy
  add proposal=myproposal src-address=0.0.0.0/0 dst-address=0.0.0.0/0 tunnel=yes
    ```
*  **OpenVPN:** OpenVPN tunneling protocol.

*   **PPPoE:** Point-to-Point Protocol over Ethernet.

*   **PPTP:** Point-to-Point Tunneling Protocol.

*   **SSTP:** Secure Socket Tunneling Protocol.

*  **WireGuard:** WireGuard tunneling protocol.

*  **ZeroTier:** ZeroTier tunneling protocol.

#### Wired Connections

*  **Ethernet:** Ethernet settings for interfaces.
    ```mikrotik
    /interface ethernet print
    /interface ethernet set ether1 speed=100M full-duplex=yes
   ```
*   **MikroTik wired interface compatibility:** Overview of compatibility with different interfaces.

*   **PWR Line:** Router power over ethernet.

#### Wireless

*   **WiFi:** Configure wireless interface.
  ```mikrotik
    /interface wifi
     set wlan1 band=2ghz-b/g/n mode=ap-bridge ssid=MyWiFi frequency=2437
   /interface wireless security-profiles add name=profile1 mode=dynamic-keys authentication-types=wpa2-psk,wpa3-psk
   /interface wifi set wlan1 security-profile=profile1
   /interface wireless set wlan1 security-profile=profile1
  ```
*   **Wireless Interface:** Configuration of wireless interfaces.

*   **W60G:** Wireless 60 GHz technology.
*   **CAPsMAN:** Centralized AP management.
    ```mikrotik
      /capsman manager set enabled=yes
    ```
*  **HWMPplus mesh:** Ad-hoc wireless mesh network.
*   **Nv2:** MikroTik proprietary wireless protocol.

*   **Interworking Profiles:** For connecting to other networks.
*   **Wireless Case Studies:** Examples with wireless configurations.

*   **Spectral scan:** For analysing the radio spectrum.

#### Internet of Things

*  **Bluetooth:** Bluetooth settings and integration.
*  **GPIO:** General Purpose Input/Output interface settings.
*  **Lora:** Lora configurations for long-range IoT.
*  **MQTT:** Message Queueing Telemetry Transport.

#### Hardware

*  **Disks:** Disk storage configurations.
    ```mikrotik