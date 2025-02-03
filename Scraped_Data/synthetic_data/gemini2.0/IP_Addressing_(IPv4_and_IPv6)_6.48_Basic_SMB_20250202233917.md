Okay, let's dive into a comprehensive guide for IP Addressing on MikroTik RouterOS, covering a wide range of features and concepts. This document is structured for an SMB environment, focusing on practical implementations using RouterOS 6.48. Though written with v6.48 in mind, these principles largely apply to v7.x as well.

## MikroTik RouterOS: IP Addressing (IPv4 and IPv6) - Comprehensive Guide

### 1. Configuration Scenario and MikroTik Requirements

**Scenario:** A small business needs a reliable network with both IPv4 and IPv6 connectivity. The network consists of a main router (MikroTik) connecting to the internet, a local area network for wired devices, and a wireless network for staff and guests. The goal is to achieve secure and efficient IPv4 and IPv6 routing with integrated services.

**MikroTik Requirements:**
*   **IPv4:**
    *   Public IP address (DHCP Client) on the WAN interface.
    *   Private IPv4 range (e.g., 192.168.88.0/24) for the LAN.
    *   DHCP server for automatic IP address assignment.
    *   NAT (Network Address Translation) for internet access.
*   **IPv6:**
    *   IPv6 address via DHCP-PD (Prefix Delegation) from the ISP.
    *   Local IPv6 range for the LAN (e.g., 2001:db8:1::/48).
    *   Router Advertisement (RA) for IPv6 address autoconfiguration.
*   **Security:**
    *   Basic firewall rules to protect the network.
    *   Secure access to the router itself.

### 2. Step-by-Step MikroTik Implementation

Here's a step-by-step guide for implementing this scenario via MikroTik CLI:

**Step 1: Interface Configuration**

*   Identify your internet interface (likely `ether1`) and LAN interface (e.g., `ether2`).
    ```
    /interface print
    ```
*   Rename interfaces for clarity.
    ```
    /interface set ether1 name=WAN
    /interface set ether2 name=LAN
    /interface set ether3 name=WLAN
    ```
*   **Wireless interface:**
    *   If your router has a wireless interface, enable it, set a mode, and an SSID
        ```
        /interface wireless set wlan1 mode=ap-bridge ssid="MyOfficeWifi" security-profile=default
        /interface wireless enable wlan1
        ```
        *   Create a security profile if needed.
            ```
            /interface wireless security-profiles add name=default mode=dynamic-keys authentication-types=wpa2-psk,wpa-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key="YourWifiPassword" wpa-pre-shared-key="YourWifiPassword"
            ```
*   **Bridge:**
    *   Create a bridge for Ethernet LAN and Wireless LAN
        ```
        /interface bridge add name=LAN_Bridge
        /interface bridge port add bridge=LAN_Bridge interface=LAN
        /interface bridge port add bridge=LAN_Bridge interface=wlan1
        ```

**Step 2: IPv4 Configuration**

*   Enable DHCP client on the WAN interface.
    ```
    /ip dhcp-client add interface=WAN disabled=no
    ```
*   Configure a static IPv4 address for the LAN interface (bridge)
    ```
    /ip address add address=192.168.88.1/24 interface=LAN_Bridge
    ```
*   Create an IPv4 address pool for the DHCP server.
    ```
    /ip pool add name=dhcp_pool ranges=192.168.88.10-192.168.88.254
    ```
*   Set up DHCP server on the LAN interface (bridge)
    ```
    /ip dhcp-server add address-pool=dhcp_pool interface=LAN_Bridge name=dhcp1
    /ip dhcp-server network add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
    ```
*   Configure NAT for internet access.
    ```
    /ip firewall nat add chain=srcnat action=masquerade out-interface=WAN
    ```

**Step 3: IPv6 Configuration**

*   Enable IPv6 on the WAN interface via DHCP client (requesting PD).
    ```
    /ipv6 dhcp-client add interface=WAN request=prefix use-peer-dns=yes add-default-route=yes pool-name=ipv6_pool
    ```
*   Set up a static IPv6 address for the LAN interface (bridge)
    ```
   /ipv6 address add address=2001:db8:1::1/64 interface=LAN_Bridge eui-64=no
    ```
*   Configure Router Advertisement (RA) for the LAN interface (bridge).
     ```
        /ipv6 nd add interface=LAN_Bridge advertise-dns=yes managed-address-flag=yes other-config-flag=yes
    ```

**Step 4: Firewall Configuration (Basic)**

*   Basic firewall rules.
    ```
    /ip firewall filter add chain=input connection-state=established,related action=accept comment="Accept Established and Related Connections"
    /ip firewall filter add chain=input protocol=icmp action=accept comment="Accept ICMP"
    /ip firewall filter add chain=input in-interface=!WAN action=accept comment="Accept input from LAN"
    /ip firewall filter add chain=input action=drop comment="Drop all other input"
    /ip firewall filter add chain=forward connection-state=established,related action=accept comment="Accept Established and Related Connections"
     /ip firewall filter add chain=forward action=drop comment="Drop all other forward"
    ```

**Step 5: Security Best Practices**

*   Change the default admin password
*   Disable unwanted services.
*   Limit Winbox access to trusted IP addresses.
    ```
    /ip service set winbox address=192.168.88.0/24
    ```
*   Use a secure password for wireless access.
*   Enable MAC address filtering for wireless access if required.

**Step 6: System Settings**

*   Set system time
    ```
    /system clock set time=09:00:00 date=jan/01/2024 time-zone-name="America/Los_Angeles"
    ```
*   Set system identity
    ```
    /system identity set name=MikroTikRouter
    ```
*   Enable NTP client for time sync
    ```
    /system ntp client set enabled=yes primary-ntp=time.google.com
    ```

### 3. Complete MikroTik CLI Configuration Commands

Here's a breakdown of the primary commands used in the implementation:

| Command                      | Parameter              | Description                                                        |
| ---------------------------- | ---------------------- | ------------------------------------------------------------------ |
| `/interface set`            | `name`, `disabled`    | Modifies interface settings (e.g., name, enable/disable).        |
| `/ip dhcp-client add`        | `interface`, `disabled` | Adds a DHCP client for dynamic IP address on an interface.       |
| `/ip address add`           | `address`, `interface` | Assigns a static IP address to an interface.                    |
| `/ip pool add`              | `name`, `ranges`       | Creates an IP pool for DHCP server address allocation.            |
| `/ip dhcp-server add`       | `address-pool`, `interface`, `name` | Creates a DHCP server on the specified interface.           |
| `/ip dhcp-server network add`| `address`, `dns-server`, `gateway`  | Defines DHCP server network settings.                       |
| `/ip firewall nat add`        | `chain`, `action`, `out-interface` | Creates a NAT rule for masquerading traffic.            |
| `/ipv6 dhcp-client add`      | `interface`,`request`,`use-peer-dns`,`add-default-route`, `pool-name`| Enables IPv6 DHCP client |
| `/ipv6 address add`         | `address`,`interface`,`eui-64`| Sets IPv6 address on an interface |
| `/ipv6 nd add` | `interface`,`advertise-dns`,`managed-address-flag`, `other-config-flag`| Enables IPv6 Router Advertisement |
| `/ip firewall filter add`   | `chain`, `action`, `protocol`, `connection-state`,`in-interface` | Creates a firewall filter rule to control traffic.            |
| `/ip service set` | `winbox` `address` | Limit access to winbox |
| `/system clock set` | `time`, `date`, `time-zone-name` | set system time |
| `/system identity set` | `name` | Set device identity |
| `/system ntp client set` | `enabled`, `primary-ntp` | Set NTP server |
|`/interface bridge add` | `name` | Creates a new bridge |
|`/interface bridge port add`| `bridge`, `interface` | Add interface to a bridge |
|`/interface wireless set` | `wlan1`, `mode`,`ssid`,`security-profile` | set wireless interface |
| `/interface wireless security-profiles add` | `name`, `mode`, `authentication-types`, `unicast-ciphers`, `group-ciphers`, `wpa2-pre-shared-key`, `wpa-pre-shared-key` | set wireless security profile |

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

*   **DHCP Issues:** Ensure the DHCP server is enabled on the correct interface, IP pool ranges are valid, and lease times are appropriate.
    *   Use `/ip dhcp-server lease print` to check DHCP leases.
*   **NAT Not Working:** Verify the `out-interface` parameter is correct and the firewall rules are allowing outbound traffic.
    *   Use `/ip firewall nat print` to see the NAT rules.
*   **IPv6 Connectivity Issues:** Check if the DHCPv6 client is getting a prefix and Router Advertisements (RA) are enabled on LAN.
    *   Use `/ipv6 dhcp-client print` and `/ipv6 nd print` for diagnostic information.
*   **Firewall Rule Order:** Firewall rules are processed in order. Ensure the rules allow for necessary traffic before dropping others.
    *   Use `/ip firewall filter print` to check the rules.
*   **Misconfigured Bridge:** Ensure that all interfaces you intend to bridge are part of a single bridge, and there are no conflicts between interface IP addresses and the bridge's IP address.
    * Use `/interface bridge print` and `/interface bridge port print` to check the bridge configuration

*   **Troubleshooting Tools:**
    *   **Ping:** `ping <IP_address>` - Check basic network connectivity.
    *   **Traceroute:** `traceroute <IP_address>` - Trace the route to a destination.
    *   **Torch:** `/tool torch interface=WAN` - Monitor real-time traffic flow.
    *   **Packet Sniffer:** `/tool sniffer quick interface=WAN` - Capture packets for in-depth analysis.
    *   **Log:** `/system logging print` - View logs for any system issues

### 5. Verification and Testing Steps

*   **Ping Tests:** From a device on the LAN, ping both an external IPv4 address (e.g., 8.8.8.8) and an IPv6 address (e.g., 2001:4860:4860::8888).
*   **Web Browsing:** Try browsing websites to check both IPv4 and IPv6 connectivity.
*   **DHCP Assignment:** Check if the LAN devices are getting IP addresses from the DHCP server using `/ip dhcp-server lease print` on the MikroTik.
*   **IPv6 Address Autoconfiguration:** Verify if your LAN devices get a IPv6 address using SLAAC (Stateless Address Autoconfiguration).
*   **Traffic Monitor:** Use Torch on interfaces to verify if traffic flows to the right interfaces.
*   **Firewall Monitoring:** Monitor the firewall counters to ensure your rules work as expected.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Address Lists:** Group IP addresses for firewall rules and QoS (Quality of Service).
*   **Layer 7 Protocols:** Apply firewall rules based on application protocols (HTTP, DNS).
*   **Queues:** Configure QoS for bandwidth management.
*   **VLANs:** Segment the network into isolated subnets.
*   **VPN:** Configure IPsec, WireGuard, or other VPN protocols for secure remote access.
*   **Scripting:** Automate tasks with RouterOS scripting.
*   **Limitations:** Some low-end MikroTik devices have limited hardware capabilities affecting routing performance with complex firewall rules or QoS policies.
*   **Features:**
    *   **L3 Hardware Offloading:** The ability to use the hardware on the MikroTik device to perform routing functions. This can greatly improve performance.
    *   **Switch Chip Features:** A MikroTik with a switch chip has capabilities similar to a managed switch. You can set up vlans directly on the switch chip using `/interface ethernet switch`.
    *   **MACVLAN** A virtual interface based on an existing interface which allows multiple MAC address to be used on one single interface.
    *   **MACsec:** MAC security which allows the encryptions of traffic on the link layer
*   **Note:** RouterOS version updates can introduce new features and behaviors that could require configuration changes. Always refer to the changelog.

### 7. MikroTik REST API Examples

These examples focus on basic IP address operations via MikroTik's REST API:

*   **API Endpoint:** `/ip/address`
*   **Authentication:** RouterOS API authentication is not shown here and is assumed to be pre-configured.

*   **Example 1: List all IP addresses**

    *   **Method:** `GET`
    *   **Request URL:** `https://<router-ip>/rest/ip/address`
    *   **Expected JSON Response:**
        ```json
        [
          {
            "address": "192.168.88.1/24",
            "interface": "LAN_Bridge",
            "id": "*1",
            "network": "192.168.88.0",
             "dynamic": false,
             "disabled": false,
            "actual-interface": "LAN_Bridge"

          }
           ,
          {
            "address": "192.168.1.1/24",
            "interface": "WAN",
            "id": "*2",
             "network": "192.168.1.0",
            "dynamic": true,
            "disabled": false,
            "actual-interface": "WAN"

          }
        ]
        ```
*   **Example 2: Add an IP address**

    *   **Method:** `POST`
    *   **Request URL:** `https://<router-ip>/rest/ip/address`
    *   **Request JSON Payload:**
        ```json
        {
          "address": "192.168.89.1/24",
          "interface": "LAN_Bridge"
        }
        ```
    *   **Expected JSON Response (Success):**
        ```json
        {
            "message": "added",
             "id": "*3"

        }
        ```
*   **Example 3: Delete an IP address**

    *   **Method:** `DELETE`
    *   **Request URL:** `https://<router-ip>/rest/ip/address/*3`
    *   **Expected JSON Response:**
    ```json
        {
            "message": "removed"
        }
        ```

### 8. In-Depth Explanations of Core Concepts

*   **Bridging:** Combines multiple interfaces into a single broadcast domain, similar to a network switch.
*   **Routing:** Determines the path traffic takes based on destination IP addresses.
*   **Firewall:** Filters and controls network traffic based on rules.
*   **NAT:** Translates private IP addresses to a public IP address for internet access.
*   **DHCP:** Automatically assigns IP addresses to network devices.
*   **Router Advertisement (RA):** Enables automatic IPv6 address configuration on local devices.
*   **IP Pools:** Manages and allocates IP addresses for DHCP services.
*   **MAC Address Filtering:** A security feature that limits wireless access based on the device's MAC address.
*   **Connection tracking:** The router keeps track of all connections, which is crucial for firewall rules to work as expected.

### 9. Security Best Practices

*   **Strong Passwords:** Use strong, unique passwords for the router.
*   **Disable Unneeded Services:** Disable services like telnet or SSH if not needed.
*   **Limit Winbox Access:** Restrict Winbox access to trusted IP addresses only.
*   **Firewall Rules:** Implement strong firewall rules to protect your network.
*   **Regular Updates:** Keep the RouterOS firmware updated for security patches.
*   **Secure Wireless:** Use strong Wi-Fi passwords (WPA2 or WPA3)
*   **MAC address filtering:** Enable MAC address filtering on the Wireless interface if needed.
*   **Limit API access:** Restrict the IP address allowed to connect to the API
*  **Use Certificates:** Use trusted certificates to encrypt connections to the router when using https or other secure services
*  **Regular Backups:** Regular backup configuration files and store them in a safe place.
*  **VPNs:** Use a VPN to manage your router. If you need to remotely access your router, make sure you use a VPN to protect your connection.

### 10. Detailed Explanations and Configurations of MikroTik Topics

**Here are further explanations and configuration examples for the specified MikroTik topics:**

#### **IP Pools**

IP Pools are used to manage a range of IP addresses that are allocated to different services, primarily DHCP servers. They allow for easy management of IP address space.

*   **Configuration:**
    ```
    /ip pool add name=dhcp-pool ranges=192.168.10.10-192.168.10.200
    /ip pool add name=static-pool ranges=192.168.10.10
    ```
*  **Use Case:** In the examples above, `dhcp-pool` will be used by a DHCP server and `static-pool` will be used to assign a single IP address to a static lease.

#### **IP Routing**

IP routing determines the path traffic will take to reach its destination. MikroTik supports static routes, dynamic routing protocols, and policy-based routing.

*   **Configuration:**
    * **Static route:**
        ```
        /ip route add dst-address=10.10.10.0/24 gateway=192.168.1.2
        ```
    * **OSPF**
      *   Add an OSPF instance:
          ```
          /routing ospf instance add name=ospf1 router-id=192.168.88.1
          ```
     *   Add OSPF networks:
          ```
           /routing ospf network add network=192.168.88.0/24 area=backbone
          ```

*   **Explanation:** A static route is configured for traffic destined to `10.10.10.0/24` to go through `192.168.1.2`. The OSPF configurations enable the router to participate in the OSPF routing protocol.
*   **Note:** Route selection is based on several factors. You should always verify that the routes are what you expect them to be using the command `/ip route print`.

#### **IP Settings**

IP settings includes RouterOS configuration related to the handling of ICMP, TCP and other IP protocols.

*   **Configuration:**
    ```
    /ip settings set allow-fast-path=yes tcp-syncookies=yes tcp-fin-timeout=10s tcp-keepalive-timeout=1h tcp-max-segment-size=1460
    ```
*   **Explanation:** This configuration enables faster TCP processing with fast-path option, enables TCP SYN cookies to prevent SYN flood attacks, sets TCP timeout values, and set the TCP maximum segment size
*  **Note:** These settings should be changed only if required. The default values are usually optimal.

#### **MAC Server**

MikroTik MAC server provides the ability to connect to the router using WinBox at the MAC layer, without using an IP address.

*   **Configuration:**
    ```
    /tool mac-server set allowed-interfaces=all enabled=yes
    /tool mac-server mac-winbox set allowed-interfaces=all enabled=yes
    ```
*  **Explanation:** This command allows the router to be connected to through Winbox at the MAC layer. This is usefull when no IP addresses have been assigned yet.
*   **Note:** This should be limited to specific interfaces for security reasons. In general, you should use IP layer access to Winbox unless there is a real need to use MAC layer connections.

#### **RoMON**

RoMON (Router Management Overlay Network) is a MikroTik protocol that allows you to manage multiple MikroTik devices from one central point, simplifying administration of larger networks

*   **Configuration:**
    ```
    /tool romon set enabled=yes  id="romon-main"
    /tool romon port add interface=LAN_Bridge
    ```
*  **Explanation:** This will enable RoMon and allow connection through the LAN interface
*  **Note:** This functionality requires the romon password to be set up using the command `/tool romon set secret="romonpass"`

#### **WinBox**

Winbox is a GUI application provided by MikroTik that can connect to a RouterOS device through a LAN connection using a mac or IP address.

*   **Configuration:**
    ```
    /ip service set winbox address=192.168.88.0/24
    /ip service set winbox disabled=no
    ```
*  **Explanation:** This allows connection through Winbox using an IP from 192.168.88.0/24.
*   **Note:** Restrict the allowed IPs to increase security.

#### **Certificates**

Certificates are used for encryption and identification, commonly used with HTTPS access, VPN and other secure services.

*   **Configuration:**
    ```
     /certificate import file-name=my-cert.pem passphrase="password"
     /certificate import file-name=my-key.pem passphrase="password"
     /certificate print
     /ip service set www-ssl certificate=my-cert
     ```

*   **Explanation:** Imports certificate and private keys. `www-ssl` uses the certificate `my-cert`.
*   **Note:** Certificates are created outside of MikroTik and then imported.

#### **PPP AAA**

PPP AAA (Point-to-Point Protocol Authentication, Authorization, and Accounting) is a set of protocols used in PPP connections to ensure secure access.

*   **Configuration:**
    ```
    /ppp profile add name=myprofile local-address=10.10.10.1 remote-address=10.10.10.2
    /ppp secret add name=testuser password=testpass profile=myprofile service=pppoe
    ```
*   **Explanation:** A PPPoE profile is created and a PPP secret user is set.
*   **Note:** Additional parameters are needed depending on the security you are trying to achieve. This also depends on your service provider.

#### **RADIUS**

RADIUS (Remote Authentication Dial-In User Service) is a protocol used for centralized authentication, authorization, and accounting of users.

*   **Configuration:**
    ```
    /radius add address=10.10.10.5 secret=mysecret
    /ppp secret add name=testuser password=testpass profile=myprofile service=pppoe use-radius=yes
    ```
*   **Explanation:** Configures RADIUS server at IP address `10.10.10.5`. The user `testuser` will now use radius for authentication instead of the local secret list.
*   **Note:** RADIUS server needs to be configured first. You will need to configure your user information in the RADIUS server.

#### **User / User Groups**

RouterOS has the capability to define users and groups which have different levels of access.

*   **Configuration:**
    ```
    /user group add name=admin group=full
    /user add name=myadmin password=securepassword group=admin
     ```
*  **Explanation:** Creates an admin group and creates a user `myadmin` that belongs to it. This admin group has full access to the device.
*   **Note:** You can create more groups with more restrictive rights. You should always create a user with less rights than `full` for your day to day work.

#### **Bridging and Switching**

Bridging connects multiple interfaces together, while switching can offload some of the forwarding to hardware, improving performance

*   **Configuration:**
    ```
    /interface bridge add name=my-bridge
    /interface bridge port add bridge=my-bridge interface=ether2
    /interface bridge port add bridge=my-bridge interface=ether3
    /interface ethernet switch vlan add vlan-id=10 ports=ether2,ether3
    ```
*  **Explanation:** Creates a bridge called `my-bridge` and adds the interfaces `ether2` and `ether3` to it. Creates a vlan id 10 on the switch chip.
*   **Note:** A bridge is a software-based function. Using the switch chip functions provides higher throughput.

#### **MACVLAN**

MACVLAN allows creation of multiple virtual interfaces on a single physical interface, each with its own MAC address, enabling multiple IP addresses per physical interface.

*   **Configuration:**
    ```
    /interface macvlan add name=macvlan1 interface=ether2 mac-address=02:00:00:00:00:01
    /interface macvlan add name=macvlan2 interface=ether2 mac-address=02:00:00:00:00:02
    /ip address add interface=macvlan1 address=192.168.10.1/24
    /ip address add interface=macvlan2 address=192.168.20.1/24
    ```
*  **Explanation:** This configuration creates two `macvlan` interfaces based on `ether2` with different MAC addresses, each with a different IP address range.
*   **Note:** MACVLAN is primarily used to virtualize network interfaces on a server.

#### **L3 Hardware Offloading**

L3 Hardware Offloading allows certain routing processes to be performed directly on the hardware, bypassing the CPU and improving throughput.

*   **Configuration:**
    ```
    /interface ethernet set ether2 l3-hw-offloading=yes
    /interface ethernet set ether3 l3-hw-offloading=yes
    ```
*   **Explanation:** Enables the L3 hardware offloading on interfaces `ether2` and `ether3`.
*   **Note:** Not all hardware supports L3 Hardware Offloading. Check your device's documentation.

#### **MACsec**

MACsec (Media Access Control Security) provides link layer encryption, enhancing security between devices.

*   **Configuration:**
   ```
   /interface ethernet macsec add name=macsec1 interface=ether2 cipher-suite=gcm-aes-128 key="0123456789abcdef0123456789abcdef" port=2
   /interface ethernet set ether2 macsec=macsec1
   ```
*   **Explanation:**  Creates a macsec policy on interface ether2 using gcm-aes-128 encryption
*   **Note:** Both sides of the link needs to have MACsec configured with identical keys. Requires specific hardware that supports MACsec.

#### **Quality of Service**

QoS ensures that important traffic gets the bandwidth it needs.

*   **Configuration:**
    ```
    /queue simple add name="video" target=192.168.88.0/24 max-limit=2M/5M priority=1/1
    /queue simple add name="normal" target=192.168.88.0/24 max-limit=5M/10M priority=8/8
    ```
*   **Explanation:** The `video` queue has a higher priority than the `normal` queue.
*  **Note:** You can use many different methods to classify traffic that needs QoS. You can classify based on IP address, port, protocol, etc.

#### **Switch Chip Features**

Switch chip features allow for VLANs, port mirroring, and other functionalities to be managed within the hardware of a MikroTik device that has a switch chip.

*   **Configuration:**
    ```
    /interface ethernet switch vlan add vlan-id=10 ports=ether2,ether3
    /interface ethernet switch port set ether2 vlan-mode=secure
    /interface ethernet switch port set ether3 vlan-mode=secure
    ```
*   **Explanation:** Creates a VLAN id of 10 on interfaces ether2 and ether3.
*   **Note:** Switch chip configurations are only applicable if your MikroTik device has a switch chip.

#### **VLAN**

VLANs (Virtual Local Area Networks) logically separate network traffic within a shared infrastructure.

*   **Configuration:**
    ```
    /interface vlan add name=vlan10 vlan-id=10 interface=LAN_Bridge
    /ip address add address=192.168.10.1/24 interface=vlan10
     /interface vlan add name=vlan20 vlan-id=20 interface=LAN_Bridge
    /ip address add address=192.168.20.1/24 interface=vlan20
    ```
*   **Explanation:** Creates VLANs with IDs 10 and 20 on `LAN_Bridge`.
*   **Note:** VLANs should be properly configured on the switches to transport VLAN traffic.

#### **VXLAN**

VXLAN (Virtual Extensible LAN) is a network virtualization technology that extends Layer 2 networks over Layer 3.

*   **Configuration:**
    ```
     /interface vxlan add name=vxlan1 vni=1000 interface=LAN_Bridge remote-address=10.10.10.2
     /ip address add address=10.10.10.1/24 interface=vxlan1
    ```
*   **Explanation:** Creates a VXLAN tunnel with a specific VNI over the LAN interface.
*   **Note:** The remote side needs to have a similar setup with the addresses switched.

#### **Firewall and Quality of Service**

*   **Connection Tracking:**
    *   MikroTik's firewall keeps track of connections through the connection tracker. This functionality allows you to use the `connection-state=established,related` parameters in firewall rules to only allow traffic that has been initiated from your network to pass through.
*   **Firewall:**
    *   Basic firewall rule:
        ```
        /ip firewall filter add chain=input protocol=tcp dst-port=80 action=accept comment="Allow HTTP"
        /ip firewall filter add chain=input action=drop comment="Drop all other input"
        ```
*  **Packet Flow in RouterOS:**
    * Incoming packets enter the router at an interface. They are then routed through the firewall and routing engines. Finally, they are forwarded out the correct interface.
*   **Queues:**
     *   Simple queue:
        ```
        /queue simple add target=192.168.88.0/24 max-limit=10M/10M name=normal-queue
        ```
*  **Firewall and QoS Case Studies:**
    *   **Prioritizing Voice Traffic:** You could create a QoS policy that prioritizes traffic from voice IP addresses to allow for high quality calls.
*   **Kid Control:** Use firewall rules to block access to specific websites and domains at specific times.
*   **UPnP (Universal Plug and Play):**  Allows devices to automatically configure port forwarding for specific applications.
*   **NAT-PMP:** (NAT Port Mapping Protocol) is a protocol that can be used to allow for automatic port forwarding.

#### **IP Services**

*   **DHCP:**
    *    Already configured above. `/ip dhcp-server`, `/ip dhcp-server network`, and `/ip pool` are used for DHCP configuration.
*  **DNS:**
     *   Set DNS servers.
          ```
          /ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
          ```
*  **SOCKS:**
    *   Create a SOCKS proxy:
         ```
         /ip socks set enabled=yes address=192.168.88.1 port=8080
         ```
*   **Proxy:**
    *   Create a simple web proxy:
         ```
         /ip proxy set enabled=yes src-address=192.168.88.1 port=3128
         ```
*   **Note:** The DHCP server was configured before in the basic section.

#### **High Availability Solutions**

*   **Load Balancing:**
    *   Use multiple WAN links and configure policy routing to distribute traffic evenly across links.
*  **Bonding:**
    *   Combine multiple ethernet interfaces to create one virtual interface with more throughput.
        ```
        /interface bonding add mode=802.3ad slaves=ether2,ether3 name=bond1
        ```
*  **Bonding Examples:**
    *   Configure Link Aggregation to increase the bandwidth between your router and switch by using `mode=802.3ad` bonding.
*   **HA Case Studies:**
    *   VRRP: Use VRRP to allow seamless failover from the master router to the backup router.
*   **Multi-chassis Link Aggregation Group (MLAG):**
    *   Combine ports from multiple switches to create a logical single link for increased bandwidth and redundancy.
*  **VRRP (Virtual Router Redundancy Protocol):**
    *   Configuration:
       ```
        /interface vrrp add interface=LAN_Bridge vrid=10 priority=200 address=192.168.88.254/24 name=vrrp1
       ```
*  **VRRP Configuration Examples:**
    * Set up multiple routers with identical VRRP configurations to allow seamless failover if the primary router goes down.
 *   **Note:** For more complex setups, you would configure OSPF or BGP for routing between the routers.

#### **Mobile Networking**

*  **GPS:**
     *   View information:
          ```
           /system gps monitor
          ```
    *  **Note:** Only applicable to devices that have GPS.
*   **LTE:**
    *   Configure LTE interface:
        ```
        /interface lte set lte1 apn=myapn user=user password=password
        /interface lte enable lte1
        ```
*  **PPP:**
    *  Configure a PPP client interface:
        ```
         /interface ppp-client add interface=lte1 connect-timeout=60 name=ppp1 user=user password=password
         ```
*   **SMS:**
      *   Send an SMS:
           ```
           /tool sms send phone