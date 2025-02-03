Okay, let's dive deep into MikroTik RouterOS, focusing on IP Addressing and encompassing all the requested topics. This will be a comprehensive guide designed for an enterprise-level deployment. We'll be using RouterOS 7.12 as our base.

**Note:** This is a *very* extensive document. I have structured it logically and will break it down into digestible chunks. We will cover the core concepts in depth, and touch on the more peripheral features.

## 1. Comprehensive Configuration Scenario & MikroTik Requirements

**Scenario:**

Imagine a medium-sized enterprise with the following requirements:

*   **Dual Internet Uplinks:** Two separate ISP connections, one IPv4 and one IPv6.
*   **Internal Network Segmentation:** Multiple VLANs for different departments (e.g., IT, Finance, HR, Guest).
*   **Guest Wi-Fi Network:** A separate wireless network with controlled access.
*   **VPN Access:** Secure remote access for employees.
*   **Centralized Authentication:** Use of a RADIUS server for user authentication.
*   **Robust Firewall:** Comprehensive protection against external threats.
*   **QoS:** Prioritize critical application traffic.
*   **Monitoring and Logging:** Continuous monitoring of system resources and network activity.

**MikroTik Requirements:**

*   A MikroTik router capable of handling the network load (e.g., CCR, CRS series).
*   RouterOS version 7.12 or later.
*   Multiple physical interfaces for WAN and LAN connections.
*   Wireless interface (if Wi-Fi is required).

## 2. Step-by-Step MikroTik Implementation (CLI & Winbox)

**Initial Setup**

Before starting with the configuration, ensure your MikroTik device is properly connected to the network, and you can access it via Winbox or SSH.

**Step 1:  System Update**
*   **Winbox:** Navigate to *System > Packages* and Check for Updates.
*   **CLI:**
    ```routeros
    /system package update check
    /system package update download
    /system reboot
    ```

**Step 2:  Initial System Configuration**

*   **Winbox:** Navigate to *System > Identity* and set a descriptive name (e.g., "EnterpriseRouter").
*   **CLI:**
    ```routeros
    /system identity set name=EnterpriseRouter
    ```

**Step 3:  User and Access Control**
*   **Winbox:** *System > Users*, add a new administrator user, and disable default admin user, use /tool fetch if you are using default admin user
*   **CLI:**
    ```routeros
   /user add name=new_admin_user group=full password=your_password
   /user disable admin
   ```

**Step 4: Interface Configuration**

For this scenario, we'll assume these interfaces:

*   `ether1`: ISP-IPv4 (WAN)
*   `ether2`: ISP-IPv6 (WAN)
*   `ether3`: Internal LAN (Trunk)
*   `wlan1`: Guest Wi-Fi
*   `ether4`: Management port (for remote access only)

*   **Winbox:** Navigate to *Interfaces*, rename the interfaces appropriately, enable the interfaces (where required).
*   **CLI:**
    ```routeros
    /interface ethernet set ether1 name=WAN-IPv4
    /interface ethernet set ether2 name=WAN-IPv6
    /interface ethernet set ether3 name=LAN
    /interface ethernet set ether4 name=MGMT
    /interface wireless set wlan1 name=Guest-WiFi
    ```
    ```routeros
    /interface ethernet enable ether1
    /interface ethernet enable ether2
    /interface ethernet enable ether3
    /interface ethernet enable ether4
    /interface wireless enable wlan1
    ```
    

**Step 5: Bridge and VLAN Configuration**

We'll create a bridge interface for LAN and VLAN tagging.

*   **Winbox:** *Bridge* -> *Bridge* -> Add a new bridge.  *Bridge* -> *Ports* and add ether3 to this bridge
*   **CLI:**
    ```routeros
    /interface bridge add name=LAN-Bridge
    /interface bridge port add bridge=LAN-Bridge interface=LAN
    ```

Now let’s create our VLANs:

*   **Winbox:**  *Interface > VLAN*, add four VLAN interfaces with IDs 10,20,30, and 40, using LAN-bridge as interface.
*   **CLI:**
    ```routeros
    /interface vlan add interface=LAN-Bridge name=VLAN-IT vlan-id=10
    /interface vlan add interface=LAN-Bridge name=VLAN-Finance vlan-id=20
    /interface vlan add interface=LAN-Bridge name=VLAN-HR vlan-id=30
    /interface vlan add interface=LAN-Bridge name=VLAN-Guest vlan-id=40
    ```

**Step 6: IP Address Assignment (IPv4)**

*   **Winbox:** *IP > Addresses*, add addresses for the LAN interfaces, using CIDR notations. Add DHCP server for each subnet as well.
*   **CLI:**
   ```routeros
    /ip address add address=10.10.10.1/24 interface=VLAN-IT network=10.10.10.0
    /ip address add address=10.10.20.1/24 interface=VLAN-Finance network=10.10.20.0
    /ip address add address=10.10.30.1/24 interface=VLAN-HR network=10.10.30.0
    /ip address add address=10.10.40.1/24 interface=VLAN-Guest network=10.10.40.0
    /ip address add address=192.168.88.1/24 interface=MGMT network=192.168.88.0
    /ip dhcp-server add address-pool=pool_IT interface=VLAN-IT name=dhcp_IT
    /ip dhcp-server network add address=10.10.10.0/24 dns-server=10.10.10.1 gateway=10.10.10.1
    /ip dhcp-server add address-pool=pool_Finance interface=VLAN-Finance name=dhcp_Finance
    /ip dhcp-server network add address=10.10.20.0/24 dns-server=10.10.20.1 gateway=10.10.20.1
    /ip dhcp-server add address-pool=pool_HR interface=VLAN-HR name=dhcp_HR
    /ip dhcp-server network add address=10.10.30.0/24 dns-server=10.10.30.1 gateway=10.10.30.1
    /ip dhcp-server add address-pool=pool_Guest interface=VLAN-Guest name=dhcp_Guest
    /ip dhcp-server network add address=10.10.40.0/24 dns-server=10.10.40.1 gateway=10.10.40.1
    /ip pool add name=pool_IT ranges=10.10.10.10-10.10.10.254
    /ip pool add name=pool_Finance ranges=10.10.20.10-10.10.20.254
    /ip pool add name=pool_HR ranges=10.10.30.10-10.10.30.254
    /ip pool add name=pool_Guest ranges=10.10.40.10-10.10.40.254
   ```

**Step 7: IP Address Assignment (IPv6)**

This assumes your ISP provides an IPv6 subnet.
*   **Winbox:**  *IP > Addresses*, add IPv6 address.
*   **CLI:**
    ```routeros
    /ipv6 address add address=2001:db8::1/64 interface=LAN
    ```

**Step 8: Basic Routing (IPv4)**

*   **Winbox:** *IP > Routes*, add a default route.
*   **CLI:**
   ```routeros
    /ip route add dst-address=0.0.0.0/0 gateway=your_isp_gateway
   ```

**Step 9:  Basic Routing (IPv6)**

*   **Winbox:** *IPv6 > Routes*, add default route.
*   **CLI:**
  ```routeros
    /ipv6 route add dst-address=::/0 gateway=your_isp_ipv6_gateway
   ```

**Step 10: DHCPv6 Server**
* **Winbox:** *IPv6 > DHCP Server*
* **CLI:**

```routeros
/ipv6 dhcp-server add address-pool=dhcpv6pool interface=LAN name=dhcpv6_server
/ipv6 dhcp-server network add address=2001:db8::/64 dns-server=2001:db8::1 gateway=2001:db8::1
/ipv6 pool add name=dhcpv6pool prefix=2001:db8::/64
```
**Step 11: Wireless configuration for Guest WiFi**
*  **Winbox** *Wireless > Wifi Interfaces > Click on wlan1*
*   **CLI**

```routeros
/interface wireless set wlan1 band=2ghz-b/g/n country=us disabled=no mode=ap-bridge ssid=Guest-WiFi wpa2-psk="somepassword"
/interface wireless security-profiles add authentication-types=wpa2-psk mode=dynamic-keys name=Guest_Profile supplicant-identity=Guest-WiFi
/interface wireless set Guest-WiFi security-profile=Guest_Profile
```

**Step 12: Basic Firewall Configuration**
*   **Winbox:** *Firewall*
*   **CLI**

```routeros
/ip firewall filter add action=accept chain=input comment="Allow established connections" connection-state=established,related
/ip firewall filter add action=accept chain=input comment="Allow ICMP" protocol=icmp
/ip firewall filter add action=drop chain=input comment="Drop invalid connections" connection-state=invalid
/ip firewall filter add action=accept chain=input comment="Allow Winbox" dst-port=8291 in-interface=MGMT protocol=tcp
/ip firewall filter add action=accept chain=input comment="Allow SSH" dst-port=22 in-interface=MGMT protocol=tcp
/ip firewall filter add action=drop chain=input comment="Drop all other input"
/ip firewall filter add action=accept chain=forward comment="Allow established/related forwarding" connection-state=established,related
/ip firewall filter add action=accept chain=forward comment="Allow forwarding from LAN" in-interface=LAN-Bridge
/ip firewall filter add action=drop chain=forward comment="Drop other forwarding"
/ip firewall nat add action=masquerade chain=srcnat out-interface=WAN-IPv4
/ip firewall nat add action=masquerade chain=srcnat out-interface=WAN-IPv6
```

**Explanation:**

This section covers the basic setup necessary for IPv4 and IPv6 connectivity and basic firewall rules. We've configured interfaces, set up VLANs, assigned IP addresses, configured basic DHCP servers, and set up basic firewall rules.

## 3. Complete MikroTik CLI Configuration Commands

**General Syntax:**

```
/[path] [command] [parameters]
```
   *   `/` : Root level
   *   `path`: Specifies the sub menu (e.g., `/ip/address`, `/interface/ethernet`).
   *   `command`: Specifies the action (e.g., `add`, `set`, `print`).
   *   `parameters`: Specific options (e.g., `address=`, `name=`, `interface=`).

**Examples of commands used in previous sections:**

*   `/system identity set name=MyRouter`: Set device identity.
*   `/interface ethernet set ether1 name=WAN-IPv4`: Rename ethernet interface.
*   `/ip address add address=192.168.1.1/24 interface=ether3`: Add an IP address.
*   `/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254`:  Add a default route.
*   `/interface bridge add name=LAN-Bridge`: Create a new bridge
*   `/interface vlan add interface=LAN-Bridge vlan-id=10 name=VLAN-IT`: Create a new VLAN
*   `/ip dhcp-server add address-pool=my-pool interface=VLAN-IT`: Create a new DHCP server
*   `/ip pool add name=my-pool ranges=192.168.10.10-192.168.10.200`: Create a new IP pool

**Important Parameters:**

| Parameter       | Description                                                              |
| --------------- | ------------------------------------------------------------------------ |
| `name=`         | Name of the object (interface, IP address, route).                       |
| `interface=`    | Interface the object is associated with.                                |
| `address=`      | IP address with subnet mask in CIDR format (e.g., `192.168.1.1/24`).     |
| `gateway=`      | IP address of the next hop router.                                     |
| `dst-address=`  | Destination IP address or network.                                      |
| `src-address=` | Source IP address or network.                                           |
| `vlan-id=`       | VLAN ID.                                                                  |
| `action=`       | Firewall rule action (e.g., `accept`, `drop`, `masquerade`).             |
| `chain=`        | Firewall chain (e.g., `input`, `forward`, `srcnat`).                     |
| `protocol=`      | IP Protocol (e.g., tcp, udp, icmp).                                    |
| `out-interface=` | Outgoing interface of the traffic                                     |

**Note:** MikroTik's CLI offers tab completion and context-sensitive help (`?`), making command navigation easier.
## 4. Common MikroTik-Specific Pitfalls, Troubleshooting & Diagnostics

**Pitfalls:**

1.  **Default Configurations:**  Default configurations should be changed. The default user should be disabled, and weak passwords should be avoided.
2.  **Firewall Misconfigurations:** Incorrect firewall rules can block crucial traffic. Always test rules in a lab before deploying.
3.  **Interface Mismatches:** Ensure interfaces are correctly assigned for WAN/LAN.
4.  **Incorrect NAT Settings:** Incorrect NAT configuration can lead to connection issues.
5.  **DHCP Conflicts:** Multiple DHCP servers on the same network can cause IP address conflicts.
6.  **Outdated Firmware:** Use the latest stable RouterOS version for security and functionality.
7.  **Resource Overload:** Avoid exceeding CPU/RAM usage. Check system resources regularly.
8.  **Configuration Backup**: Regularly back up your configuration.

**Troubleshooting:**

1.  **Connectivity Issues:** Check IP addresses, routes, and firewall rules. Use `ping` and `traceroute`.
2.  **DNS Resolution Problems:** Ensure DNS servers are correctly configured.
3.  **DHCP Issues:** Verify the DHCP server settings and client leases.
4.  **Wireless Problems:** Check SSID, security settings, and channel interference.
5. **CPU Usage** : Check `/system resource` for high CPU or memory usage
6.  **Interface Errors:** Use `/interface print stats` to see if you have errors on your interfaces
7.  **Firewall issues**: Use `/ip firewall connection print` to check firewall connections.

**Diagnostics Tools:**

*   **`ping`:** Basic connectivity test.
    ```routeros
    /ping 8.8.8.8
    ```
*   **`traceroute`:**  Path tracing.
    ```routeros
    /traceroute 8.8.8.8
    ```
*   **`torch`:** Packet sniffer.
    ```routeros
    /tool torch interface=ether1
    ```
*   **`/system resource`:** System resource usage.
    ```routeros
    /system resource print
    ```
*   **`/interface print stats`:**  Interface statistics.
    ```routeros
     /interface print stats
    ```
*   **`/ip firewall connection print`:**  Firewall connection details.
    ```routeros
    /ip firewall connection print
    ```
*   **`/log print`:** System logs for errors.
    ```routeros
     /log print
    ```
* **`/interface monitor-traffic`** Show traffic on each interface in real time
* **`/tool profile`** Shows cpu usage by different processes
**Best Practice:** Use `/system routerboard upgrade` to ensure you have the latest router firmware.

## 5. Verification and Testing Steps

**Verification Steps:**

1.  **Ping Tests:** Ping external addresses and internal devices.
    ```routeros
    /ping 8.8.8.8
    /ping 10.10.10.10
    ```
2.  **Traceroute Tests:** Check network paths.
    ```routeros
    /traceroute 8.8.8.8
    ```
3.  **DHCP Leases:** Verify devices get correct IP addresses. Use `/ip dhcp-server lease print`.
    ```routeros
    /ip dhcp-server lease print
    ```
4.  **Interface Status:** Check the status of interfaces. Use `/interface print`.
    ```routeros
    /interface print
    ```
5.  **Firewall Counters:** Verify firewall rules are working. Use `/ip firewall filter print stats`
    ```routeros
    /ip firewall filter print stats
    ```
6.  **System Resource Monitoring:** Check CPU and memory.
   ```routeros
    /system resource print
   ```

**Testing Steps:**

1.  **Web Browsing:**  Test basic internet access from internal networks.
2.  **File Transfers:** Transfer files between subnets and to the internet.
3.  **VPN Access:** Test remote access via VPN.
4.  **Wireless Connectivity:**  Connect to the guest Wi-Fi and test connectivity.
5.  **Bandwidth Test** Use `/tool bandwidth-test` to test the performance of your connection
    ```routeros
    /tool bandwidth-test address=your_remote_ip protocol=tcp
    ```

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

**Specific Features:**

*   **Scripting:**  Automate tasks with RouterOS scripting.
*   **Netinstall:** Reinstall RouterOS if needed.
*   **Cloud:**  Manage devices through the MikroTik cloud service.
*   **CAPsMAN:** Centrally manage wireless access points.
*   **User Manager:** Create user access accounts for PPP and Hotspot.
*   **Queues:** Comprehensive Quality of Service (QoS) capabilities.
*   **VRF:** Virtual Routing and Forwarding for network segmentation.
*   **BGP, OSPF, RIP:**  Support for advanced routing protocols.
*   **MPLS:** Multi-Protocol Label Switching capabilities
*   **ZeroTier, Wireguard:** Support for modern VPN technologies
*   **Container** : Ability to run Linux containers on your router
*   **Traffic Flow** : Export traffic data for monitoring purposes

**Capabilities:**

*   **Highly Configurable:** Fine-grained control over network parameters.
*   **Robust Security:** Comprehensive firewall capabilities.
*   **High Performance:**  Handles significant network loads.
*   **Cost-Effective:** Provides enterprise features at a competitive price.
*  **Extensible** : Ability to add custom packages via RouterOS Package Management

**Limitations:**

*   **Steep Learning Curve:** RouterOS is powerful but can be complex.
*   **Hardware Limitations:** Performance depends on the chosen RouterBOARD model.
*   **Complex Configurations:** Advanced configurations can be challenging to manage.
*   **Resource Constraints:** Entry level routers have limited resources.
*   **Limited Software Support:** RouterOS has its own operating system and software environment which can limit the availability of some software.
*   **Limited Package Support** - only some packages are available for download to routers.

## 7. MikroTik REST API Examples (Applicable)

RouterOS has a REST API that lets you manage it remotely.

**General API Endpoint:**
   `https://[router_ip]/rest/`

**API Authentication:**

Use basic HTTP authentication (username and password).

**Example 1: Get list of interfaces**

*   **Endpoint:**  `https://[router_ip]/rest/interface`
*   **Method:** `GET`
*   **Request (using curl):**
    ```bash
    curl -u admin:password https://[router_ip]/rest/interface -k
    ```
*   **Expected Response (JSON):**
    ```json
    [
        {
            "id": "*0",
            "name": "ether1",
            "type": "ethernet",
            "mtu": "1500",
            "mac-address": "xx:xx:xx:xx:xx:xx"
            ...
        },
         {
            "id": "*1",
            "name": "ether2",
            "type": "ethernet",
            "mtu": "1500",
            "mac-address": "xx:xx:xx:xx:xx:xx"
            ...
        }
    ]
    ```

**Example 2: Create an IP Address**

*   **Endpoint:**  `https://[router_ip]/rest/ip/address`
*   **Method:** `POST`
*   **Request (using curl) with JSON payload:**
    ```bash
    curl -u admin:password -X POST -H "Content-Type: application/json" -d '{"address":"192.168.5.5/24", "interface":"ether3"}'  https://[router_ip]/rest/ip/address -k
    ```
*   **Expected Response (JSON):**
    ```json
    {
        "id": "*F",
        "address": "192.168.5.5/24",
        "interface": "ether3",
        "network": "192.168.5.0"
       ...
    }
    ```

**Example 3: Update System Identity**

*   **Endpoint:** `https://[router_ip]/rest/system/identity`
*   **Method:** `PUT`
*   **Request (using curl) with JSON payload:**
    ```bash
    curl -u admin:password -X PUT -H "Content-Type: application/json" -d '{"name":"UpdatedRouterName"}' https://[router_ip]/rest/system/identity/*0  -k
    ```

*   **Expected Response (JSON):**
    ```json
        {
            "id": "*0",
            "name": "UpdatedRouterName"
        }
    ```

**Note:** You can use any tool to send HTTP requests, like `curl`, `Postman`, or scripting languages. The API is not very efficient for bulk data.

## 8. In-Depth Explanations of Core Concepts

**Bridging:**
    * Allows multiple interfaces to act as a single layer 2 network, which can include both Ethernet and wireless interfaces
    * Bridging allows all devices connected to different ports to belong to the same subnet.
    * Filtering and queuing can occur on the bridge.

**Routing:**
    * Allows packets to travel between different networks
    * RouterOS supports both static routes and dynamic routing protocols (OSPF, BGP, RIP).
    * Routes are used to determine the best path for packets.

**Firewall:**
    * Protects your network against external threats.
    * Firewall can work at different layers of the network stack.
    * RouterOS supports different types of firewalls including NAT, filter, mangle.
    * Firewall can also perform deep packet inspection for more advanced features.
    * Firewall rules are applied in order of their configuration

## 9. Security Best Practices

1.  **Strong Passwords:**  Use strong, unique passwords for all user accounts.
2.  **Disable Default User:**  Disable the default admin user.
3.  **Access Control:**  Restrict access to management interfaces.
4.  **Firewall Rules:** Implement strict firewall rules to block unauthorized access.
5.  **Service Hardening:** Disable unnecessary services and ports.
6.  **Regular Updates:**  Keep RouterOS updated with the latest patches.
7.  **VPN for Remote Access:** Use secure VPN connections for remote management.
8.  **Backups:** Regularly back up the RouterOS configuration.
9.  **Use HTTPS:** Use HTTPS and not HTTP to access the router
10. **Use WinBox in safe mode** : Avoid making unwanted changes

## 10. Detailed Explanations and Configuration Examples

Now, we'll delve deeper into each of the specified MikroTik topics, providing detailed explanations and configuration examples. We'll build upon the core configuration already described.

### IP Addressing (IPv4 and IPv6)

*   **IPv4 Addressing:**
    *   Use CIDR notation (e.g., `192.168.1.1/24`).
    *   Private address ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
    *   Assign IP addresses to interfaces.
    ```routeros
        /ip address add address=192.168.1.1/24 interface=ether3
    ```
*   **IPv6 Addressing:**
    *   Use CIDR notation (e.g., `2001:db8::1/64`).
    *   Assign IPv6 addresses to interfaces.
    ```routeros
        /ipv6 address add address=2001:db8::1/64 interface=ether3
    ```
    * RouterOS supports multiple types of IPv6 addressing: SLAAC, DHCPv6, and static addressing
    * Router advertisements can be enabled for your interfaces
    ```routeros
        /ipv6 nd add interface=ether3 advertise=yes
    ```

### IP Pools

*   **Definition:** Ranges of IP addresses used by DHCP servers.
*   **Configuration:**
    ```routeros
        /ip pool add name=pool-lan ranges=192.168.1.100-192.168.1.200
        /ip pool add name=pool-ipv6 prefix=2001:db8::/64 prefix-length=64
    ```
    * Pools can be assigned for DHCPv4 or DHCPv6

### IP Routing

*   **Static Routes:** Manual routes for destination networks.
    ```routeros
        /ip route add dst-address=172.16.0.0/24 gateway=192.168.1.254
        /ipv6 route add dst-address=2001:db8:2::/64 gateway=2001:db8::2
    ```
*   **Dynamic Routing:**
    *   **OSPF (Open Shortest Path First):** Link-state routing protocol.
    ```routeros
        /routing ospf instance add name=ospf-lan router-id=192.168.1.1
        /routing ospf area add area-id=0.0.0.0 instance=ospf-lan
        /routing ospf interface add interface=ether3 area=0.0.0.0
    ```
    *   **BGP (Border Gateway Protocol):** Path vector routing protocol used in ISP networks.
    ```routeros
       /routing bgp instance add name=bgp-as65000 router-id=192.168.1.1 as=65000
        /routing bgp peer add name=peer-isp instance=bgp-as65000 remote-address=192.0.2.2 remote-as=65001
    ```
    *   **RIP (Routing Information Protocol):** Distance-vector routing protocol.
     ```routeros
         /routing rip interface add interface=ether3
    ```

### IP Settings

*   **General IP settings:** Allows you to set common settings for IP routing
    *  `ip/settings`: Enables / disables IPv4 forwarding, sets ICMP settings, allows setting broadcast addresses.

### MAC server

*   **Definition:** Enables MAC address based access
*  **Configuration:**
 ```routeros
     /tool mac-server set allowed-interface=ether1,ether2,ether3 enabled=yes
     /tool mac-server mac-winbox set allowed-interface=ether1,ether2,ether3 enabled=yes
 ```

### RoMON

*   **Definition:** MikroTik's Router Management Overlay Network. Allows you to remotely connect to devices without any IP address.
*  **Configuration**

    ```routeros
    /tool romon set enabled=yes port=17000
    /tool romon port add interface=ether1
    ```

### WinBox

*   **Definition:** MikroTik's Windows-based GUI management tool.
*   **Access:**  Use IP address or MAC address for connections, WinBox can also connect via RoMON.
*  **Tips:**
     *   Use "Safe Mode" when making changes
     *   Use secure passwords
     *   Use `/system password` to change your password
     *   Use `/tool fetch` to connect to your device
### Certificates
*   **Definition:** Used for secure communication over SSL/TLS
*   **Importing a Certificate**
     * You can import your certificate in WinBox under  `System > Certificates`
     * You can create a self-signed certificate by executing this code
```routeros
      /certificate add name=mycertificate common-name=my_router_hostname key-usage=digital-signature,key-encipherment,tls-server key-size=2048
```

### PPP AAA
*  **Definition:** Uses authentication, authorization, and accounting for PPP connections.
*   **Configuration:** Uses `/ppp aaa` to configure parameters for user accounts. You can use local authentication or RADIUS

### RADIUS

*   **Definition:** Centralized authentication server.
*   **Configuration:**
    ```routeros
        /radius add address=192.168.2.1 secret=radiussecret timeout=30
        /ppp secret set use-radius=yes
    ```

### User / User Groups

*   **Users:** System and VPN user accounts.
    ```routeros
        /user add name=john group=read,write password=user_password
        /user group add name=admin policy=write,read,test,password
        /user set john group=admin
    ```
*   **User Groups:** Permissions management.
    ```routeros
        /user group add name=admin policy=write,read,test,password
    ```

### Bridging and Switching

*   **Bridge:** Allows multiple interfaces to function as one.
    ```routeros
        /interface bridge add name=mybridge
        /interface bridge port add bridge=mybridge interface=ether2
        /interface bridge port add bridge=mybridge interface=ether3
    ```
* **Switching**
    * MikroTik routers are often equipped with a switch chip
    * The switch chip can perform hardware based L2 operations
    * Switch chip features can be configured with the `/interface ethernet switch` menu

### MACVLAN

*   **Definition:**  Create multiple MAC addresses on a single physical interface.
*   **Configuration:**
    ```routeros
        /interface macvlan add interface=ether3 mac-address=02:00:00:00:00:01 name=macvlan1
        /interface macvlan add interface=ether3 mac-address=02:00:00:00:00:02 name=macvlan2
    ```
### L3 Hardware Offloading

*   **Definition:** Offload L3 functions from CPU to the switch chip.
* **Configuration**:
    * L3 hardware offloading can be enabled via the interface settings by adding the `l3-hw-offload=yes` parameter to your bridge

### MACsec

*   **Definition:** Layer 2 link encryption security protocol
*   **Configuration:**
     ```routeros
      /interface macsec add name=macsec1 interface=ether1 key=macseckey
     ```
### Quality of Service

*   **Queues:** Implement QoS to manage bandwidth usage.
    ```routeros
        /queue tree add name=upload-queue max-limit=10M
        /queue tree add name=download-queue max-limit=50M
        /queue tree add parent=upload-queue queue=default
        /queue tree add parent=download-queue queue=default
    ```
*  **Simple Queues:** Limit individual connections
    ```routeros
        /queue simple add name=user-limit target-addresses=192.168.1.10 max-limit=2M/2M
    ```

### Switch Chip Features

*   **VLANs on Switch Chip:** Use switch chip for VLAN tagging.
*   **Port Isolation:** Isolate ports for better security.
* **Configuration:**
    * Access switch chip features with `/interface ethernet switch`
    * Use `/interface ethernet switch vlan print` to view VLAN configuration
    * Use `/interface ethernet switch port print` to view port settings

### VLAN

*   **Definition:**  Virtual LANs for network segmentation.
*   **Configuration:**
    ```routeros
        /interface vlan add interface=ether3 vlan-id=10 name=vlan-it
        /interface vlan add interface=ether3 vlan-id=20 name=vlan-finance
    ```
*   **VLAN Trunking:** Trunk multiple VLANs on a single interface.
    ```routeros
       /interface bridge vlan add bridge=mybridge tagged=ether3 vlan-ids=10,20
    ```

### VXLAN

*   **Definition:** Layer 2 overlay network technology.
*   **Configuration:**
    ```routeros
        /interface vxlan add name=vxlan1 vni=1000 remote-address=10.0.0.2 interface=ether3
    ```

### Firewall and Quality of Service

*   **Connection Tracking:**  Track connections for stateful filtering.
*   **Firewall Filter Rules:** Define rules for network traffic (input, forward, output).
    ```routeros
        /ip firewall filter add chain=input action=accept protocol=tcp dst-port=80
        /ip firewall filter add chain=forward action=drop src-address=192.168.1.0/24 dst-address=10.0.0.0/24
        /ip firewall filter add chain=input action=drop
    ```
*  **NAT:** Network Address Translation
    ```routeros
        /ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
    ```
*   **Packet Flow in RouterOS:** Understand how packets are processed.
*   **Queues:** Implement QoS to manage bandwidth usage.
* **Firewall and QoS Case Studies:** Implementation of