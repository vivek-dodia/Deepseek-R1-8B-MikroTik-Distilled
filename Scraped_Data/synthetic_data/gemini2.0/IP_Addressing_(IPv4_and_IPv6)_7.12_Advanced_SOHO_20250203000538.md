Okay, let's craft a comprehensive technical document covering IP Addressing and related aspects on MikroTik RouterOS 7.12, focusing on an Advanced SOHO configuration.

# MikroTik RouterOS: Advanced IP Addressing and Network Management for SOHO

This document outlines advanced IP addressing, networking concepts, and related features on MikroTik RouterOS 7.12, designed for a SOHO (Small Office/Home Office) environment.

## 1. Comprehensive Configuration Scenario and Specific MikroTik Requirements

**Scenario:** A SOHO network requires a secure and robust internet connection, with local network segmentation for various devices. We'll implement:

*   A main LAN with a private IPv4 address range.
*   A Guest WiFi network isolated from the main LAN using VLANs.
*   IPv6 address assignment for future-proofing.
*   DHCP servers for both IPv4 and IPv6.
*   Firewall rules to control traffic flow.
*   Quality of Service (QoS) rules to prioritize specific traffic.
*   Remote access via secure VPN connection
*   Centralized management using Winbox

**Specific MikroTik Requirements:**

*   RouterOS 7.12 (or later)
*   Multi-port Router suitable for LAN, WAN, and VLAN interfaces
*   Basic network configuration of Internet connection.

## 2. Step-by-Step MikroTik Implementation using CLI & Winbox

### 2.1 Base Configuration

*   **Reset Configuration:** Start with a fresh RouterOS configuration. In Winbox, go to "System" -> "Reset Configuration" (choose "Keep user configuration" if needed, but in a new deployment you will want to uncheck it)
*   **Set Identity:**  Give your router a hostname for easier identification.
  *   CLI: `/system identity set name=soho-router`
    *   Winbox: System -> Identity

### 2.2  Interface Setup

*   **Rename Interfaces:** Change default names to be more descriptive
  *  CLI:
  ```
     /interface ethernet set ether1 name=WAN
     /interface ethernet set ether2 name=LAN
     /interface ethernet set ether3 name=SWITCH-PORT
  ```
  *   Winbox: Interface -> Ethernet -> Right click on the interface to rename it.
* **Bridge Setup:** Create a bridge for the LAN interfaces.
    *  CLI:
   ```
    /interface bridge add name=bridge-LAN
    /interface bridge port add bridge=bridge-LAN interface=LAN
    /interface bridge port add bridge=bridge-LAN interface=SWITCH-PORT
    ```
   *   Winbox:  Bridge -> Bridge -> "+" -> name: bridge-LAN; Bridge -> Ports -> "+" -> interface = LAN, Bridge = bridge-LAN;  Bridge -> Ports -> "+" -> interface = SWITCH-PORT, Bridge = bridge-LAN.

### 2.3 IP Addressing (IPv4)

*   **Assign IPv4 to Bridge:**
    *   CLI: `/ip address add address=192.168.10.1/24 interface=bridge-LAN`
    *   Winbox: IP -> Addresses -> "+" -> Address: 192.168.10.1/24, Interface: bridge-LAN
*   **Setup DHCP Server:**
    *   CLI:
   ```
   /ip pool add name=dhcp_pool_lan ranges=192.168.10.100-192.168.10.200
   /ip dhcp-server add address-pool=dhcp_pool_lan interface=bridge-LAN name=dhcp_lan
   /ip dhcp-server network add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1
   ```
    * Winbox: IP -> Pool -> "+" -> Name: dhcp\_pool\_lan, Ranges: 192.168.10.100-192.168.10.200; IP -> DHCP Server -> "+" -> Name: dhcp\_lan, Interface: bridge-LAN, Address Pool: dhcp\_pool\_lan; IP -> DHCP Server -> Networks -> "+" -> Address: 192.168.10.0/24, DNS Server: 192.168.10.1, Gateway: 192.168.10.1.

### 2.4 IP Addressing (IPv6)

*   **Enable IPv6:**
    * CLI: `/ipv6 settings set disable-ipv6=no`
    * Winbox: IP -> IPv6 -> Settings -> uncheck "disable IPv6"
*   **Request IPv6 Prefix (If ISP Supports):**
    *   This depends on your ISP's configuration. Let's assume we get a `/64` prefix via DHCPv6-PD (Prefix Delegation) on the WAN.
  * CLI:
  ```
  /ipv6 dhcp-client add interface=WAN request=prefix add-default-route=yes
  /ipv6 address add interface=bridge-LAN from-pool=prefix-pool advertise=yes
  ```
   *   Winbox: IP -> DHCP Client -> "+" -> Interface: WAN, Request: Prefix, uncheck "Use Peer DNS", check "Add default Route"; IP -> IPv6 -> Addresses -> "+" -> Interface: bridge-LAN, Address: Select "From Pool", Check Advertise.
  * Note: The Prefix pool will automatically be generated after the DHCP6 client obtains a prefix. Check by using the command `/ipv6 pool print`
*   **Setup IPv6 DHCP Server (DHCPv6 Server):**
  * CLI:
    ```
   /ipv6 dhcp-server add interface=bridge-LAN name=dhcp_ipv6_lan address-pool=prefix-pool
   /ipv6 dhcp-server settings set managed-address=yes other-config=yes
   ```
  * Winbox: IP -> DHCPv6 Server -> "+" -> Name: dhcp\_ipv6\_lan, Interface: bridge-LAN, Pool: prefix\_pool; IP -> DHCPv6 Server -> Settings -> Check "Managed Address Config", Check "Other Config".

### 2.5 VLAN Setup (Guest WiFi)

*   **Create VLAN Interface:**
    * CLI:
   ```
   /interface vlan add name=vlan-guest-wifi vlan-id=10 interface=bridge-LAN
   ```
  *  Winbox: Interface -> VLAN -> "+" -> Name: vlan-guest-wifi, VLAN ID: 10, Interface: bridge-LAN
*   **Assign IPv4 to VLAN Interface:**
  *  CLI: `/ip address add address=192.168.20.1/24 interface=vlan-guest-wifi`
  * Winbox: IP -> Addresses -> "+" -> Address: 192.168.20.1/24, Interface: vlan-guest-wifi
* **DHCP Server for Guest WiFi:**
 *   CLI:
 ```
   /ip pool add name=dhcp_pool_guest_wifi ranges=192.168.20.100-192.168.20.200
   /ip dhcp-server add address-pool=dhcp_pool_guest_wifi interface=vlan-guest-wifi name=dhcp_guest_wifi
   /ip dhcp-server network add address=192.168.20.0/24 dns-server=192.168.20.1 gateway=192.168.20.1
```
 * Winbox: IP -> Pool -> "+" -> Name: dhcp\_pool\_guest\_wifi, Ranges: 192.168.20.100-192.168.20.200; IP -> DHCP Server -> "+" -> Name: dhcp\_guest\_wifi, Interface: vlan-guest-wifi, Address Pool: dhcp\_pool\_guest\_wifi; IP -> DHCP Server -> Networks -> "+" -> Address: 192.168.20.0/24, DNS Server: 192.168.20.1, Gateway: 192.168.20.1.

* **Wireless Setup for Guest WiFi:**
    * Create a new security profile for the guest wifi using WPA2 or WPA3.
    * Create a new WiFi interface under the Wireless tab that uses the created security profile, and the SSID you would like.
    * Bridge this new wifi interface with the vlan-guest-wifi interface.
   *  CLI:
  ```
   /interface wireless security-profiles add authentication-types=wpa2-psk,wpa2-eap,wpa3-psk,wpa3-eap mode=dynamic-keys name=guest_security_profile supplicant-identity=MikroTik wpa2-pre-shared-key=guest_password wpa3-pre-shared-key=guest_password
  /interface wireless wifi add disabled=no mode=ap-bridge security-profile=guest_security_profile ssid=guest_wifi_ssid band=2ghz-g/n/ax channel-width=20/40mhz-Ce tx-power=default
  /interface bridge port add bridge=bridge-LAN interface=wlan1
  ```
  * Winbox: Wireless -> Security Profiles -> "+" -> Name: guest\_security\_profile; Mode: dynamic-keys, Authentication Types: wpa2-psk,wpa3-psk, WPA2 Pre-Shared Key: guest\_password, WPA3 Pre-Shared Key: guest\_password; Wireless -> WiFi Interfaces -> "+" -> Name: wlan1,  Mode: AP Bridge, SSID: guest\_wifi\_ssid, Band: 2ghz-g/n/ax, Channel Width: 20/40MHz-Ce,  Security Profile: guest\_security\_profile; Bridge -> Ports -> "+" -> interface = wlan1, Bridge = bridge-LAN

### 2.6 Firewall Setup

*   **NAT for Internet access:**
    * CLI:
  ```
   /ip firewall nat add chain=srcnat action=masquerade out-interface=WAN
  ```
   *   Winbox: IP -> Firewall -> NAT -> "+" -> Chain: srcnat, Action: masquerade, Out. Interface: WAN
*   **Forwarding Rules:** Ensure the guest network is isolated from the main network, but can access internet. Add a forward rule that accepts connections from vlan-guest-wifi to the WAN and blocks any connections to bridge-LAN.
  * CLI:
  ```
    /ip firewall filter add chain=forward action=accept in-interface=vlan-guest-wifi out-interface=WAN
    /ip firewall filter add chain=forward action=drop in-interface=vlan-guest-wifi out-interface=bridge-LAN
    /ip firewall filter add chain=forward action=accept connection-state=established,related
    /ip firewall filter add chain=forward action=drop
  ```
   *  Winbox: IP -> Firewall -> Filter Rules -> "+" -> Chain: Forward, In Interface: vlan-guest-wifi, Out Interface: WAN, Action: Accept; IP -> Firewall -> Filter Rules -> "+" -> Chain: Forward, In Interface: vlan-guest-wifi, Out Interface: bridge-LAN, Action: Drop, IP -> Firewall -> Filter Rules -> "+" -> Chain: Forward, connection-state: established,related, Action: Accept; IP -> Firewall -> Filter Rules -> "+" -> Chain: Forward, Action: Drop

### 2.7 Remote Access Setup (Wireguard VPN)
  * **Add an Interface:**
    * CLI:
    ```
      /interface wireguard add listen-port=13231 name=wg1
    ```
    * Winbox: Interfaces -> "+" -> WireGuard -> Name: wg1, Listen Port: 13231
  * **Add IP Addresses:**
    * CLI:
    ```
    /ip address add address=10.10.10.1/24 interface=wg1
    ```
    * Winbox: IP -> Addresses -> "+" -> Address: 10.10.10.1/24, Interface: wg1
  * **Add a peer:**
    * CLI:
   ```
    /interface wireguard peers add interface=wg1 allowed-address=10.10.10.2/32 public-key="[Your WireGuard Public Key]" persistent-keepalive=25
   ```
    * Winbox: Interfaces -> WireGuard -> Peers -> "+" -> Interface: wg1, Allowed Addresses: 10.10.10.2/32, Public Key: "[Your WireGuard Public Key]", Persistent Keepalive: 25
  * **Add firewall rule:**
    * CLI:
   ```
    /ip firewall nat add chain=srcnat action=masquerade out-interface=bridge-LAN
   ```
    * Winbox: IP -> Firewall -> NAT -> "+" -> Chain: srcnat, Action: masquerade, Out. Interface: bridge-LAN

### 2.8 Winbox Setup
  * Download and install Winbox from the MikroTik website.
  * Use the "Neighbors" tab to find the newly configured router.
  * Login using the default username and password if this is a new configuration.
  * Change the default password for security purposes.

## 3. Complete MikroTik CLI Configuration Commands

```
# System Setup
/system identity set name=soho-router

# Interface Setup
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=LAN
/interface ethernet set ether3 name=SWITCH-PORT
/interface bridge add name=bridge-LAN
/interface bridge port add bridge=bridge-LAN interface=LAN
/interface bridge port add bridge=bridge-LAN interface=SWITCH-PORT


# IPv4 Address & DHCP
/ip address add address=192.168.10.1/24 interface=bridge-LAN
/ip pool add name=dhcp_pool_lan ranges=192.168.10.100-192.168.10.200
/ip dhcp-server add address-pool=dhcp_pool_lan interface=bridge-LAN name=dhcp_lan
/ip dhcp-server network add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1

# IPv6 Setup
/ipv6 settings set disable-ipv6=no
/ipv6 dhcp-client add interface=WAN request=prefix add-default-route=yes
/ipv6 address add interface=bridge-LAN from-pool=prefix-pool advertise=yes
/ipv6 dhcp-server add interface=bridge-LAN name=dhcp_ipv6_lan address-pool=prefix-pool
/ipv6 dhcp-server settings set managed-address=yes other-config=yes


# VLAN Setup
/interface vlan add name=vlan-guest-wifi vlan-id=10 interface=bridge-LAN
/ip address add address=192.168.20.1/24 interface=vlan-guest-wifi
/ip pool add name=dhcp_pool_guest_wifi ranges=192.168.20.100-192.168.20.200
/ip dhcp-server add address-pool=dhcp_pool_guest_wifi interface=vlan-guest-wifi name=dhcp_guest_wifi
/ip dhcp-server network add address=192.168.20.0/24 dns-server=192.168.20.1 gateway=192.168.20.1


#Wireless Setup
/interface wireless security-profiles add authentication-types=wpa2-psk,wpa2-eap,wpa3-psk,wpa3-eap mode=dynamic-keys name=guest_security_profile supplicant-identity=MikroTik wpa2-pre-shared-key=guest_password wpa3-pre-shared-key=guest_password
/interface wireless wifi add disabled=no mode=ap-bridge security-profile=guest_security_profile ssid=guest_wifi_ssid band=2ghz-g/n/ax channel-width=20/40mhz-Ce tx-power=default
/interface bridge port add bridge=bridge-LAN interface=wlan1

# Firewall Setup
/ip firewall nat add chain=srcnat action=masquerade out-interface=WAN
/ip firewall filter add chain=forward action=accept in-interface=vlan-guest-wifi out-interface=WAN
/ip firewall filter add chain=forward action=drop in-interface=vlan-guest-wifi out-interface=bridge-LAN
/ip firewall filter add chain=forward action=accept connection-state=established,related
/ip firewall filter add chain=forward action=drop

# Wireguard VPN Setup
/interface wireguard add listen-port=13231 name=wg1
/ip address add address=10.10.10.1/24 interface=wg1
/interface wireguard peers add interface=wg1 allowed-address=10.10.10.2/32 public-key="[Your WireGuard Public Key]" persistent-keepalive=25
/ip firewall nat add chain=srcnat action=masquerade out-interface=bridge-LAN
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

*   **Incorrect Interface Selection:** Double-check interface names in commands.
*   **Firewall Rule Order:** Rules are processed sequentially; ensure correct order. Use `/ip firewall filter print` and `/ip firewall nat print` to check rule ordering.
*   **DHCP Server Conflicts:** Ensure no other DHCP server is active on the same network. Use `/ip dhcp-server print` and `/ip dhcp-client print` to diagnose DHCP problems.
*   **Missing or Incorrect Routes:** If traffic isn't routing correctly, use `/ip route print` to check routing tables, and add a default route manually using `/ip route add dst-address=0.0.0.0/0 gateway=<gateway-ip>`.
*  **Incorrect MTU settings:**  Sometimes incorrect MTU settings can lead to connection issues.
*   **IPv6 Issues:** Check if your ISP supports IPv6 and if the DHCPv6-PD is functioning correctly. If the DHCPv6 Client is not obtaining a prefix make sure that the client interface is set to the correct interface. Use `/ipv6 dhcp-client print` to check the current status.
*   **Winbox Errors:** Check for Winbox version compatibility with RouterOS.
*   **Log Review:** Utilize `/system logging print` to view logs, which can help identify issues.
*  **Certificate issues:** Incorrect certificates for VPNs or other services can cause issues with connections.
* **DNS Issues:** Incorrect DNS settings can cause issues resolving hostnames. Ensure that the correct DNS server is configured in your DHCP Network settings. Use `/ip dns print` to view current DNS settings and try to use `/tool dns-query name=<website address>` to debug DNS issues.

**Diagnostics Tools:**

*   `ping <ip-address>`: Test basic connectivity.
*   `traceroute <ip-address>`: Trace the path of network packets.
*   `torch <interface>`: Monitor real-time traffic on an interface.
*   `/tool bandwidth-test <ip-address> user=<username> password=<password>`: Check network speed.
*   `/system resource print`:  View resource usage.

## 5. Verification and Testing Steps

*   **IPv4 connectivity:** Connect a device to the LAN and verify it gets an IP via DHCP and internet access.
*   **IPv6 connectivity:** Ensure devices on the LAN also receive IPv6 addresses and can access IPv6 resources.
*   **Guest WiFi Network:** Connect a device to the guest WiFi and verify isolation from the LAN, but internet access.
*   **VPN Testing:**  Test the WireGuard VPN connection using a client.
*   **Ping:** Use `ping` from the router to various internal and external addresses to verify connectivity.
*   **Traceroute:** Use `traceroute` to diagnose routing issues if connections fail.
* **Torch:** Monitor traffic using torch to diagnose firewall issues if connections are being dropped.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

**MikroTik Strengths:**

*   **Feature Rich:**  Extensive routing, firewall, VPN, and QoS capabilities.
*   **Customizable:** Highly configurable using the CLI and Winbox.
*   **Performance:** Hardware acceleration and efficient packet processing.
*   **Cost-effective:** Good performance for price.
*   **Regular Updates:** Constant updates and bug fixes.
*   **Multiple Management Interfaces**: Supports management using CLI, Winbox, API, and web interface

**Limitations:**

*   **Complexity:** Steep learning curve for beginners.
*   **Configuration Errors:**  Can be easily misconfigured if not careful.
*   **Hardware limitations:** Lower models can have limitations in the amount of features, connections, and traffic that they can handle.

## 7. MikroTik REST API Examples

### 7.1 Get Interface List
*   **Endpoint:** `/interface/`
*   **Method:** `GET`
*   **Example Request (using curl):**
    ```bash
    curl -u admin:yourpassword -k -H "Content-Type: application/json" "https://<your-router-ip>/rest/interface"
    ```
*  **Example Response:**
```json
[
  {
    ".id": "*1",
    "name": "WAN",
    "type": "ether",
    "mtu": "1500",
    "mac-address": "4C:5E:0C:00:00:00",
    "enabled": true,
    "running": true
  },
  {
    ".id": "*2",
    "name": "LAN",
    "type": "ether",
    "mtu": "1500",
    "mac-address": "4C:5E:0C:00:00:01",
    "enabled": true,
    "running": false
  }
]
```

### 7.2 Add a new IP Address
*   **Endpoint:** `/ip/address`
*   **Method:** `POST`
*   **Example Request (using curl):**
    ```bash
    curl -u admin:yourpassword -k -H "Content-Type: application/json" -X POST -d '{ "address": "192.168.5.5/24", "interface": "bridge-LAN" }'  "https://<your-router-ip>/rest/ip/address"
    ```
* **Example Response:**
```json
{
    "message": "added",
     ".id": "*23"
}
```

### 7.3 Get DHCP Server list
*   **Endpoint:** `/ip/dhcp-server`
*   **Method:** `GET`
*   **Example Request (using curl):**
    ```bash
    curl -u admin:yourpassword -k -H "Content-Type: application/json" "https://<your-router-ip>/rest/ip/dhcp-server"
    ```
*  **Example Response:**
```json
 [
    {
        ".id": "*0",
        "interface": "bridge-LAN",
        "name": "dhcp_lan",
        "address-pool": "dhcp_pool_lan",
        "lease-time": "10m",
        "disabled": false
    },
    {
        ".id": "*1",
        "interface": "vlan-guest-wifi",
        "name": "dhcp_guest_wifi",
        "address-pool": "dhcp_pool_guest_wifi",
        "lease-time": "10m",
        "disabled": false
    }
]
```
**Note:** The API utilizes the router's HTTPS interface, and the "-k" flag disables SSL certificate verification. Replace `<your-router-ip>` and `yourpassword` appropriately.

## 8. In-Depth Explanations of Core Concepts

*   **Bridging:** Combining interfaces as a single Layer 2 domain, allowing devices on different interfaces to communicate as if they are on the same segment. This is how we allow devices on the LAN and SWITCH-PORT to communicate.
*   **Routing:**  Forwarding IP packets between different networks. MikroTik uses a combination of static and dynamic routing (OSPF, BGP, RIP). We used static routes and DHCP server assignment in this configuration.
*   **Firewall:** Controlling network traffic using rules based on source, destination, and other parameters. Important for network security. We use NAT to allow multiple devices to access internet using the routers public IP and used forward rules to control traffic between VLANs.
*   **VLANs:**  Creating logically separated networks on the same physical infrastructure. This allows us to separate our guest network from our LAN.
*   **NAT (Network Address Translation):** Translating private IP addresses to public addresses, allowing internal devices to access the internet. This is required for devices with private IP addresses to be able to access the internet.

## 9. Security Best Practices Specific to MikroTik Routers

*   **Change Default Password:** Immediately change the default username and password.
*   **Disable Unnecessary Services:** Disable unneeded IP services like telnet.
*   **Enable Firewall:** Implement a strong firewall with default deny rules.
*   **Limit Access:** Restrict access to management interfaces using a firewall.
*   **Use Strong Passwords:** Implement strong passwords for all users and services.
*   **Keep RouterOS Updated:** Regularly update RouterOS to patch vulnerabilities.
*  **Use secure VPNs:** For remote access, always utilize a secure VPN like IPSec or WireGuard. Avoid using weaker protocols like PPTP.
*  **Limit guest access:** Limit guest access to the local network by using forward rules in the firewall, and restrict them to only internet access.
*  **Use secure wireless encryption:** WPA3 is better than WPA2, use the most secure encryption method for all wireless networks.

## 10. Detailed Explanations and Configuration Examples for Additional MikroTik Topics

### IP Pools

*   **Purpose:**  A defined set of IP addresses used for DHCP assignment.
*   **Configuration:**
    ```
    /ip pool add name=dhcp_pool_lan ranges=192.168.10.100-192.168.10.200
    /ip pool print
    ```
*   **Explanation:** `name` is the pool identifier, and `ranges` is the IP range.
    * Use `/ip pool print` to view currently configured pools.
    * Pools can be viewed and created in Winbox under IP -> Pools.

### IP Routing

*   **Purpose:** Defines how the router forwards packets.
*   **Configuration:**
   ```
    /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1  #Static default route (change 192.168.1.1 to your gateway's IP)
    /ip route print
    ```
*   **Explanation:** `dst-address` is the destination network, and `gateway` is the router's next hop.
    *  Use `/ip route print` to view currently configured routes.
    * Routes can be viewed and created in Winbox under IP -> Routes.

### IP Settings

*   **Purpose:** Global IP settings for router behavior.
*   **Configuration:**
    ```
    /ip settings set allow-fast-path=yes
    /ip settings print
    ```
*   **Explanation:** `allow-fast-path` is one of the many parameters that can be set to improve performance on supported platforms.
   *Use `/ip settings print` to view current settings.
  *Settings can be viewed and modified in Winbox under IP -> Settings.

### MAC server

*   **Purpose:** Allows MAC address based access control to the router.
*   **Configuration:**
    ```
    /tool mac-server set allowed-interface-list=all
    /tool mac-server print
    ```
*   **Explanation:**  `allowed-interface-list` specifies which interfaces should be used by MAC address based access. You can also define mac server users using `tool mac-server user`.
*   Use `/tool mac-server print` to view current settings.
*  Settings can be viewed and modified in Winbox under Tool -> MAC Server

### RoMON

*   **Purpose:**  MikroTik's proprietary management tool for multiple MikroTik devices.
*   **Configuration:**
    ```
    /tool romon set enabled=yes
    /tool romon print
    ```
*   **Explanation:** RoMON needs to be enabled on each router before using it, and is not necessary for basic configurations.
   *Use `/tool romon print` to view current settings.
  *Settings can be viewed and modified in Winbox under Tool -> RoMON

### WinBox

*   **Purpose:** MikroTik's GUI management tool.
*   **Configuration:**
    * No specific CLI configuration, but it is recommended to change the default Winbox username and password.
*   **Explanation:** Winbox is a primary tool for MikroTik routers that provides a user friendly GUI for configuration and management. It can be installed on various operating systems and is downloadable from the MikroTik website.

### Certificates

*   **Purpose:**  Used for secure services such as HTTPS, VPNs, and CAPsMAN.
*   **Configuration:**  Create a new certificate by first generating a certificate signing request.
    ```
    /certificate generate-csr common-name=my.router.com key-size=2048 output-file=my-router.csr
    ```
    Then, sign this certificate using your trusted certificate authority, or the built in CA. Finally, import the signed certificate.
    ```
     /certificate import file=my-router.crt
    ```
*   **Explanation:**  The router can be used as a CA or a certificate request can be sent to an external CA to manage security on the router.
*   Use `/certificate print` to view current settings.
*   Settings can be viewed and modified in Winbox under System -> Certificates

### PPP AAA

*   **Purpose:** Authentication, Authorization, and Accounting for PPP connections.
*   **Configuration:**
    ```
    /ppp aaa set use-radius=yes interim-update=30s
    /ppp aaa print
    ```
*  **Explanation:** PPP AAA configures the router to use a RADIUS server for authentication for PPP connections.
*   Use `/ppp aaa print` to view current settings.
*   Settings can be viewed and modified in Winbox under PPP -> AAA

### RADIUS

*   **Purpose:** Centralized authentication server for network devices.
*   **Configuration:**
    ```
    /radius add address=192.168.1.10 secret="mysecret" service=ppp,login timeout=30
    /radius print
    ```
*   **Explanation:**  This example adds a RADIUS server with address 192.168.1.10, shared secret `mysecret`, for `ppp` and login service authentication, with a timeout of 30 seconds.
*   Use `/radius print` to view currently configured RADIUS servers.
*   Settings can be viewed and modified in Winbox under RADIUS.

### User / User Groups

*   **Purpose:**  Manage router access with specific permissions.
*   **Configuration:**
    ```
    /user group add name=admin policy=read,write,test,password
    /user add name=admin group=admin password="securepassword"
    /user print
    ```
*   **Explanation:** Creates a new user group with admin policies, and a new user named `admin` within the admin group.
* Use `/user print` to view existing users and groups.
* Users and groups can be viewed and modified in Winbox under System -> Users.

### Bridging and Switching

*   **Purpose:** Create Layer 2 connectivity by combining multiple network interfaces.
*   **Configuration:**
  ```
    /interface bridge add name=bridge-LAN
    /interface bridge port add bridge=bridge-LAN interface=LAN
    /interface bridge port add bridge=bridge-LAN interface=SWITCH-PORT
  ```
*   **Explanation:** The example creates a bridge named bridge-LAN and adds the LAN and SWITCH-PORT interfaces to it.
*  Use `/interface bridge print` to view currently configured bridges.
*  Bridges can be viewed and modified in Winbox under Bridge -> Bridges.

### MACVLAN

*   **Purpose:**  Allows multiple MAC addresses on a single physical interface.
*   **Configuration:**
  ```
    /interface macvlan add interface=bridge-LAN mac-address=02:00:00:00:00:01 name=macvlan-1
    /interface macvlan print
  ```
*   **Explanation:** The example creates a MACVLAN interface using the bridge-LAN interface and manually sets the MAC address.
*   Use `/interface macvlan print` to view existing MACVLAN interfaces.
*   MACVLAN interfaces can be viewed and modified in Winbox under Interface -> MACVLAN.

### L3 Hardware Offloading

*   **Purpose:**  Hardware acceleration to improve forwarding performance.
*   **Configuration:**
    ```
     /interface ethernet set ether1 l3-hw-offloading=yes
    ```
*   **Explanation:** When supported by your hardware you can enable L3 hardware offloading to improve forwarding performance.
 *   Use `/interface ethernet print` to view current interface settings.
*    Settings can be viewed and modified in Winbox under Interface -> Ethernet.
    * Check `/system resource print` and look at `hw-offloading` for the status of your devices hardware offloading.

### MACsec

*   **Purpose:** Security for layer-2 connections by securing the MAC layer.
*   **Configuration:**
  ```
     /interface macsec add name=macsec1 interface=LAN secret="mysecretkey"
     /interface macsec print
  ```
*  **Explanation:** The example creates a MACsec interface called `macsec1` using the LAN interface, and sets the security key for the connection.
 *   Use `/interface macsec print` to view existing MACsec settings.
 *   Settings can be viewed and modified in Winbox under Interface -> MACsec.

### Quality of Service

*   **Purpose:** Control bandwidth usage and prioritize important traffic.
*   **Configuration:**
  ```
   /queue simple add target=192.168.10.0/24 max-limit=10M/10M name=LAN_QOS
   /queue simple add target=192.168.20.0/24 max-limit=5M/5M name=guest_QOS
   /queue simple print
  ```
*   **Explanation:** Example creating a simple queue to limit the LAN to 10 Mbps and the guest WiFi to 5 Mbps.
*    Use `/queue simple print` to view currently configured queues.
*  Queues can be viewed and modified in Winbox under Queues.

### Switch Chip Features

*   **Purpose:** Access and configure features of the switch chip integrated into the router.
*   **Configuration:**
  ```
  /interface ethernet switch print
  ```
*   **Explanation:** This command will display the current switch settings. Depending on the device, different parameters will be available.
*   Use `/interface ethernet switch print` to view current settings.
*  Settings can be viewed and modified in Winbox under Interfaces -> Ethernet -> Switch Tab

### VLAN

*   **