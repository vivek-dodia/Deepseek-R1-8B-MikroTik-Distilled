Okay, let's dive into a comprehensive deep dive into IP Addressing on MikroTik RouterOS, covering IPv4 and IPv6, within the context of a SOHO network at an advanced configuration level. This is going to be quite extensive, so get comfortable!

# MikroTik RouterOS IP Addressing: A Comprehensive Guide for SOHO

This document will provide a detailed explanation of IP addressing, routing, and associated features on a MikroTik RouterOS device. We will focus on practical scenarios suitable for a SOHO environment, leveraging both IPv4 and IPv6 capabilities. This document is intended for users with an intermediate-to-advanced understanding of networking concepts and MikroTik RouterOS.

## 1. Comprehensive Configuration Scenario and Requirements

**Scenario:**

A small office/home office (SOHO) environment with the following requirements:

*   **Internet Connectivity:** A single broadband connection (DHCP or Static IPv4) and an IPv6 tunnel via a provider.
*   **Internal Network:** A single LAN segment with both IPv4 and IPv6 addressing.
*   **Guest WiFi:** A separate isolated WiFi network for guests, also with IPv4 and IPv6.
*   **VPN Access:** Remote access via VPN for users.
*   **Security:** Robust firewall rules to protect the internal network.
*   **QoS:** Basic QoS rules to prioritize VoIP traffic.
*   **Basic Monitoring:** Log access attempts and unusual traffic.

**Specific MikroTik Requirements:**

*   Utilize DHCP server for IPv4 addresses on the LAN.
*   Implement IPv6 Router Advertisements for LAN devices.
*   Use IP pools to allocate addresses.
*   Configure a firewall for both IPv4 and IPv6.
*   Utilize RoMON for remote management.
*   Establish a secure VPN connection using IPsec.
*   Use a RADIUS server for AAA (Authentication, Authorization, Accounting).

## 2. Step-by-Step MikroTik Implementation

This section provides a detailed step-by-step implementation, covering both CLI and Winbox approaches where appropriate.

### Step 1: Basic Router Configuration

1.  **Connect to the Router:** Use Winbox or SSH to connect to the MikroTik router using its default IP address or IP assigned by the DHCP server.
2.  **Change Default Password:** Immediately change the default admin password.

    ```mikrotik
    /user set admin password="your_new_password"
    ```

3.  **Set Router Identity:** Assign a unique identity to the router.

    ```mikrotik
    /system identity set name="SOHO-Router"
    ```

### Step 2: IPv4 Address Configuration

1.  **WAN Interface (DHCP):** If your internet connection is via DHCP, configure the WAN interface (typically `ether1`) to obtain an address automatically.

    ```mikrotik
    /ip dhcp-client add interface=ether1 disabled=no
    ```
    In Winbox, navigate to IP -> DHCP Client and add or edit existing DHCP Client on your WAN interface.
2.  **LAN Interface (Static):** Configure the LAN interface (e.g., `ether2`) with a static IPv4 address.

    ```mikrotik
    /ip address add address=192.168.88.1/24 interface=ether2
    ```
    In Winbox, navigate to IP -> Addresses and add a new address for your LAN interface.

3.  **DHCP Server:** Setup a DHCP server on the LAN interface.

    ```mikrotik
    /ip pool add name=dhcp_pool ranges=192.168.88.100-192.168.88.254
    /ip dhcp-server add address-pool=dhcp_pool interface=ether2 lease-time=1d name=dhcp1
    /ip dhcp-server network add address=192.168.88.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.88.1
    ```
    In Winbox, navigate to IP -> Pool to create an IP Pool, then to IP -> DHCP Server to create a server using the pool.

4.  **NAT Masquerade:** Enable NAT to allow internal devices to access the internet.

    ```mikrotik
    /ip firewall nat add chain=srcnat action=masquerade out-interface=ether1
    ```
    In Winbox, navigate to IP -> Firewall, select the NAT tab, and add the new NAT rule.

### Step 3: IPv6 Address Configuration

1.  **IPv6 Tunnel Interface (if needed):** Assuming you have a tunnel provider, create an IPv6 tunnel interface. This example uses a 6to4 tunnel.

    ```mikrotik
    /interface 6to4 add local-address="<your_public_ipv4>" remote-address="192.88.99.1" name="ipv6-tunnel" disabled=no
    ```
    ```mikrotik
    /ipv6 address add address="2001:db8:1234::2/64" interface=ipv6-tunnel eui-64=no
    ```
    Replace `<your_public_ipv4>` with the actual public IP of your router.
2.  **LAN Interface (IPv6):** Assign an IPv6 address to the LAN interface.

    ```mikrotik
     /ipv6 address add address="2001:db8:1234::1/64" interface=ether2 eui-64=no
    ```
3. **IPv6 Router Advertisement:**  Configure Router Advertisement to enable automatic IPv6 configuration on your network.

    ```mikrotik
    /ipv6 nd add interface=ether2  other-config-flag=yes managed-address-flag=no
    ```
    In Winbox, navigate to IPv6 -> ND and add router advertisement on the LAN interface.

### Step 4: Guest WiFi Setup

1.  **Create a Virtual WiFi Interface:** Create a new WiFi interface for guest access.

    ```mikrotik
    /interface wireless add name=guest-wifi ssid="GuestWiFi" security-profile=guest-security
    /interface wireless set guest-wifi mode=ap-bridge disabled=no band=2ghz-b/g/n channel-width=20mhz
    /interface wireless security-profiles add name=guest-security mode=dynamic-keys authentication-types=wpa2-psk  unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=guestpassword
    ```
2.  **Assign an IP Address to the Guest Interface:** Create a new bridge and add the wifi and ethernet interfaces to it.

     ```mikrotik
      /interface bridge add name=guest-bridge
      /interface bridge port add bridge=guest-bridge interface=guest-wifi
     ```

3.  **Configure an IP address for the bridge interface:** Add an IPv4 address to guest bridge, for example

    ```mikrotik
    /ip address add address=192.168.99.1/24 interface=guest-bridge
    ```
4. **Create a DHCP Server for the Guest Network:** Create a pool, server and networks

    ```mikrotik
        /ip pool add name=guest_dhcp_pool ranges=192.168.99.100-192.168.99.254
        /ip dhcp-server add address-pool=guest_dhcp_pool interface=guest-bridge lease-time=1d name=guestdhcp1
        /ip dhcp-server network add address=192.168.99.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.99.1
    ```
5. **Create an IPv6 address for the bridge:**

    ```mikrotik
        /ipv6 address add address=2001:db8:1235::1/64 interface=guest-bridge eui-64=no
    ```
6. **Add Router Advertisements for the Guest Network:**

    ```mikrotik
    /ipv6 nd add interface=guest-bridge other-config-flag=yes managed-address-flag=no
    ```
7. **Isolate the Guest Network:** Set up a firewall forward rule to prevent guest network traffic reaching the LAN network.

    ```mikrotik
     /ip firewall filter add chain=forward src-address=192.168.99.0/24  in-interface=guest-bridge dst-address=192.168.88.0/24 action=drop
     /ip firewall filter add chain=forward src-address=2001:db8:1235::/64 in-interface=guest-bridge dst-address=2001:db8:1234::/64 action=drop
    ```
### Step 5: VPN (IPsec) Setup (Simplified Example)

1.  **IPsec Proposal:**

    ```mikrotik
    /ip ipsec proposal add name=my_ipsec_proposal auth-algorithms=sha256 enc-algorithms=aes-256-cbc lifetime=1d
    ```

2.  **IPsec Policy:** This is a basic policy for one peer.

    ```mikrotik
    /ip ipsec policy add proposal=my_ipsec_proposal sa-src-address=<your_router_public_ipv4> sa-dst-address=<peer_public_ipv4> tunnel=yes  src-address=192.168.88.0/24 dst-address=10.10.10.0/24
    /ip ipsec peer add address=<peer_public_ipv4> secret="your_ipsec_secret" exchange-mode=main generate-policy=no
    ```
    Replace `<your_router_public_ipv4>`, `<peer_public_ipv4>` and `your_ipsec_secret` with the actual IP address, and shared secret values.

### Step 6: RADIUS Setup

1.  **Add RADIUS Server:**
    ```mikrotik
    /radius add address=<radius_server_ip> secret=<radius_shared_secret> timeout=30s accounting-port=1813
    ```
    Replace `<radius_server_ip>` and `<radius_shared_secret>` with the correct server IP and shared secret.

2.  **Configure PPP AAA:**
    ```mikrotik
    /ppp profile set <your_profile> use-radius=yes
    ```
    Replace `<your_profile>` with the ppp profile used for your VPN setup.

### Step 7: RoMON Setup

1.  **Enable RoMON:**

    ```mikrotik
    /romon set enabled=yes
    ```

2.  **Set a RoMON Password:**

    ```mikrotik
    /romon set password="your_romon_password"
    ```

### Step 8: Firewall and Quality of Service

*   **Basic Firewall (IPv4):**
    ```mikrotik
    /ip firewall filter add chain=input connection-state=established,related action=accept
    /ip firewall filter add chain=input protocol=icmp action=accept
    /ip firewall filter add chain=input in-interface=ether1 action=drop
    /ip firewall filter add chain=forward connection-state=established,related action=accept
    /ip firewall filter add chain=forward in-interface=ether1 action=drop
     /ip firewall filter add chain=input action=drop
    ```
*   **Basic Firewall (IPv6):**
    ```mikrotik
     /ipv6 firewall filter add chain=input connection-state=established,related action=accept
     /ipv6 firewall filter add chain=input protocol=icmpv6 action=accept
     /ipv6 firewall filter add chain=input in-interface=ether1 action=drop
     /ipv6 firewall filter add chain=forward connection-state=established,related action=accept
     /ipv6 firewall filter add chain=forward in-interface=ether1 action=drop
    /ipv6 firewall filter add chain=input action=drop
    ```

*   **QoS:** Create simple queue types.
    ```mikrotik
        /queue type add kind=pcq name=pcq-download pcq-classifier=dst-address
        /queue type add kind=pcq name=pcq-upload pcq-classifier=src-address
    ```

### 9. Full CLI Configuration

Here's the full CLI configuration based on the steps above.

```mikrotik
/system identity set name="SOHO-Router"
/user set admin password="your_new_password"

/interface wireless security-profiles add name=guest-security mode=dynamic-keys authentication-types=wpa2-psk  unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=guestpassword
/interface wireless add name=guest-wifi ssid="GuestWiFi" security-profile=guest-security
/interface wireless set guest-wifi mode=ap-bridge disabled=no band=2ghz-b/g/n channel-width=20mhz

/interface bridge add name=guest-bridge
/interface bridge port add bridge=guest-bridge interface=guest-wifi

/ip address add address=192.168.88.1/24 interface=ether2
/ip address add address=192.168.99.1/24 interface=guest-bridge

/ip dhcp-client add interface=ether1 disabled=no
/ip pool add name=dhcp_pool ranges=192.168.88.100-192.168.88.254
/ip dhcp-server add address-pool=dhcp_pool interface=ether2 lease-time=1d name=dhcp1
/ip dhcp-server network add address=192.168.88.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.88.1

/ip pool add name=guest_dhcp_pool ranges=192.168.99.100-192.168.99.254
/ip dhcp-server add address-pool=guest_dhcp_pool interface=guest-bridge lease-time=1d name=guestdhcp1
/ip dhcp-server network add address=192.168.99.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.99.1

/ip firewall nat add chain=srcnat action=masquerade out-interface=ether1
/ip firewall filter add chain=input connection-state=established,related action=accept
/ip firewall filter add chain=input protocol=icmp action=accept
/ip firewall filter add chain=input in-interface=ether1 action=drop
/ip firewall filter add chain=forward connection-state=established,related action=accept
/ip firewall filter add chain=forward in-interface=ether1 action=drop
/ip firewall filter add chain=forward src-address=192.168.99.0/24  in-interface=guest-bridge dst-address=192.168.88.0/24 action=drop
/ip firewall filter add chain=input action=drop

/interface 6to4 add local-address="<your_public_ipv4>" remote-address="192.88.99.1" name="ipv6-tunnel" disabled=no
/ipv6 address add address="2001:db8:1234::2/64" interface=ipv6-tunnel eui-64=no
/ipv6 address add address="2001:db8:1234::1/64" interface=ether2 eui-64=no
/ipv6 address add address="2001:db8:1235::1/64" interface=guest-bridge eui-64=no
/ipv6 nd add interface=ether2  other-config-flag=yes managed-address-flag=no
/ipv6 nd add interface=guest-bridge other-config-flag=yes managed-address-flag=no
/ipv6 firewall filter add chain=input connection-state=established,related action=accept
/ipv6 firewall filter add chain=input protocol=icmpv6 action=accept
/ipv6 firewall filter add chain=input in-interface=ether1 action=drop
/ipv6 firewall filter add chain=forward connection-state=established,related action=accept
/ipv6 firewall filter add chain=forward in-interface=ether1 action=drop
/ipv6 firewall filter add chain=forward src-address=2001:db8:1235::/64 in-interface=guest-bridge dst-address=2001:db8:1234::/64 action=drop
/ipv6 firewall filter add chain=input action=drop

/ip ipsec proposal add name=my_ipsec_proposal auth-algorithms=sha256 enc-algorithms=aes-256-cbc lifetime=1d
/ip ipsec policy add proposal=my_ipsec_proposal sa-src-address=<your_router_public_ipv4> sa-dst-address=<peer_public_ipv4> tunnel=yes  src-address=192.168.88.0/24 dst-address=10.10.10.0/24
/ip ipsec peer add address=<peer_public_ipv4> secret="your_ipsec_secret" exchange-mode=main generate-policy=no

/radius add address=<radius_server_ip> secret=<radius_shared_secret> timeout=30s accounting-port=1813
/ppp profile set <your_profile> use-radius=yes

/romon set enabled=yes
/romon set password="your_romon_password"

/queue type add kind=pcq name=pcq-download pcq-classifier=dst-address
/queue type add kind=pcq name=pcq-upload pcq-classifier=src-address
```

## 4. Common Pitfalls and Troubleshooting

*   **Incorrect Interface Selection:** Ensure that interface names (e.g., `ether1`, `ether2`, `wlan1`) are correct. Use `/interface print` to verify.
*   **NAT Misconfiguration:** Check if the `out-interface` in NAT rule points to your actual WAN interface. Incorrect NAT can result in internet connectivity issues.
*   **Firewall Conflicts:** Double-check filter rules, order matters. Use `/ip firewall filter print` and `/ipv6 firewall filter print` to review the configured rules and the counters to understand which rules are hit.
*   **IP Conflict:** Make sure IP addresses do not overlap across different interfaces.
*   **DHCP Issues:** Check `/ip dhcp-server lease print` for active leases, or examine logs using `/log print`. Use the command `/ip dhcp-server print` to check the configuration parameters of dhcp server.
*   **IPv6 Connectivity:** Always verify your IPv6 connectivity using `ping` and `traceroute`. Ensure your tunnel interface is functional.
*   **RoMON Connectivity:** Make sure the remote device is on the same broadcast domain to the RoMON master. You can use `/tool romon print` to view the configured settings.
*   **VPN Issues:** Check IPsec logs using `/log print topic=ipsec` for errors. Check the IPsec policies and peer settings.
*   **RADIUS Issues:** Use `/ppp secret print detail` to check the RADIUS settings. Use logs to check for RADIUS errors.

## 5. Verification and Testing Steps

*   **Ping Test:**
    *   From the router: `ping 8.8.8.8` (IPv4), `ping 2001:4860:4860::8888` (IPv6)
    *   From a LAN client: Verify connectivity to the router, the internet, and other devices on the network.
*   **Traceroute:**
    *   From the router: `traceroute 8.8.8.8` (IPv4), `traceroute 2001:4860:4860::8888` (IPv6)
    *   From a LAN client:  Verify the route taken to the internet.
*   **Torch:** Use `torch` on the WAN interface to monitor packets and their source/destination details for troubleshooting purposes: `/tool torch interface=ether1`
*   **IP Scan:**  Use `/tool ip-scan interface=ether2` to scan the LAN for available IP address.
*   **DHCP:** Ensure clients receive IP addresses correctly.
*   **RoMON:** Connect using Winbox via RoMON to confirm connection.

## 6. MikroTik-Specific Features, Capabilities and Limitations

*   **IP Pools:** Efficiently manage IP address allocation. The IP pool configuration allows you to specify the range of IPv4 addresses that will be assigned to hosts dynamically.
*   **Bridging:** MikroTik supports bridging to combine multiple interfaces into a single LAN.
*   **Routing:** Supports various static, dynamic (OSPF, RIP, BGP) routing protocols.
*   **Firewall:** Powerful filtering and NAT engine for robust security.
*   **QoS:**  Advanced queue management and shaping functionalities.
*   **RoMON:**  Allows remote management of multiple MikroTik devices.
*   **API:** A comprehensive REST API for configuration and monitoring.
*   **Limitations:** Specific hardware limitations depend on the router model (CPU, memory, interface count).

## 7. MikroTik REST API Examples

**Example 1: Get a list of all IP addresses**

*   **Endpoint:** `/ip/address`
*   **Method:** `GET`
*   **Request:** Empty
*   **Example with CURL:**
    ```bash
    curl -k -u admin:<your_password> https://<router_ip>/rest/ip/address
    ```

*   **Response (Example):**

```json
[
    {
        ".id": "*1",
        "address": "192.168.88.1/24",
        "interface": "ether2",
        "network": "192.168.88.0",
        "dynamic": "false",
        "actual-interface": "ether2"
    },
    {
       ".id": "*2",
       "address": "192.168.99.1/24",
       "interface": "guest-bridge",
       "network": "192.168.99.0",
       "dynamic": "false",
       "actual-interface": "guest-bridge"
   },
    {
        ".id": "*3",
        "address": "2001:db8:1234::1/64",
        "interface": "ether2",
        "network": "2001:db8:1234::",
        "dynamic": "false",
        "actual-interface": "ether2"
    },
    {
        ".id": "*4",
        "address": "2001:db8:1235::1/64",
        "interface": "guest-bridge",
        "network": "2001:db8:1235::",
        "dynamic": "false",
        "actual-interface": "guest-bridge"
    }
]

```

**Example 2: Add a new IP address**

*   **Endpoint:** `/ip/address`
*   **Method:** `POST`
*   **Request (JSON Payload):**

```json
{
  "address": "192.168.90.1/24",
  "interface": "ether3"
}
```
*  **Example with CURL**

    ```bash
    curl -k -u admin:<your_password> -X POST -H "Content-Type: application/json" -d '{"address": "192.168.90.1/24","interface": "ether3"}'  https://<router_ip>/rest/ip/address
    ```

*   **Response (Example):**

```json
{
    ".id": "*5",
    "address": "192.168.90.1/24",
    "interface": "ether3",
    "network": "192.168.90.0",
    "dynamic": "false",
    "actual-interface": "ether3"
}
```

**Note:** Ensure you replace `<router_ip>` with your router's IP address and `<your_password>` with the actual admin password.

## 8. In-Depth Explanations

*   **Bridging:** Allows multiple interfaces to act as a single broadcast domain. Packets received on one port are forwarded to all other ports on the same bridge (depending on the destination MAC address)
*   **Routing:** Determines the path of network traffic based on IP addresses. Static routes are manually configured, while dynamic routes are learned using routing protocols.
*   **Firewall:**  Acts as a barrier between your network and untrusted networks. It analyzes traffic based on configured rules (source/destination IP, ports, protocols). RouterOS filters are stateful, which means that established and related connections are tracked automatically.
*   **Connection Tracking:** RouterOS keeps track of active connections, which speeds up the filtering process.
*   **Packet Flow:** Packets arrive at an interface, go through ingress filters, the routing decision, egress filters and exit an interface.
*  **Quality of Service (QoS):**  Allows for prioritization of certain types of traffic based on bandwidth allocation. Queue management in MikroTik allows setting different priorities to different types of packets, shaping the traffic rate, limiting the rate.
* **IP Services:**
 * **DHCP:** MikroTik acts as a DHCP server to assign IP addresses to devices on the network.
  * **DNS:** Configured DNS settings specify name resolution servers used. The router can act as a local cache DNS server or redirect requests to external servers.
* **High Availability Solutions:**
  * **VRRP:** Virtual Router Redundancy Protocol (VRRP) allows multiple routers to share the same virtual IP address. If the master router fails, the backup router takes over.
*   **Mobile Networking:**
  *   **LTE:** MikroTik supports LTE connections to provide internet access when a wired network is not available.

## 9. Security Best Practices

*   **Change Default Password:**  This should always be the first step.
*   **Disable Unnecessary Services:** Only enable necessary services like SSH, Winbox and RoMON.
*   **Use Strong Passwords:**  Avoid simple, predictable passwords.
*   **Firewall Rules:** Carefully configure firewall rules to block unauthorized access to your network.
*   **Regular Updates:** Keep the RouterOS software updated for the latest security patches.
*   **Secure Access:** Limit Winbox and SSH access to specific IP addresses if possible.
*   **Disable Default User:**  Disable or rename default users.
*  **MAC Access List:** Use mac access list for controlling the access to your wireless networks.
* **Certificates:** Use secure connections with certificates in order to protect from Man In The Middle attacks.
*  **IPsec:** Use secure key exchange and strong encryption for your VPN setup.
*   **RADIUS:** Use strong secrets and network separation for the RADIUS server.
* **Log Analysis:** Regularly analyze log files looking for suspicious access attempts.

## 10. Detailed Explanations and Configurations

This is the most detailed section, further expanding on the components listed in the topic.

### IP Addressing

**IPv4:**

*   Uses 32-bit addresses.
*   Written in dotted decimal notation (e.g., 192.168.1.1).
*   Subnet masks define network ranges (e.g., 255.255.255.0 or /24).
*   Private address ranges for internal networks (e.g., 192.168.0.0/16, 10.0.0.0/8).
*   Public addresses assigned to devices on the internet.

**IPv6:**

*   Uses 128-bit addresses.
*   Written in hexadecimal notation (e.g., 2001:db8::1).
*   Can have multiple addresses (link-local, global unicast, etc).
*   Supports autoconfiguration.
*   Largely eliminates need for NAT.
*   Router Advertisements (RA) are sent by the router to communicate to the hosts on the network and provide addressing details.

**Configuration:**

*   **Add IPv4 address:** `/ip address add address=<ip_address>/<subnet_mask> interface=<interface_name>`
*   **Add IPv6 address:** `/ipv6 address add address=<ipv6_address>/<prefix> interface=<interface_name> eui-64=no`
*    *   `address`:  The address you are assigning
    *   `interface`:  The interface to which you are assigning the address
    *   `eui-64=no`: Specifies that the interface id is to be assigned by the user (not taken from the MAC address)
    *   `prefix`: Specifies the mask size. For example /24 for ipv4 or /64 for IPv6 addresses.

### IP Pools

*   Defines ranges of IP addresses to be allocated dynamically (typically by DHCP servers).
*   Allows management of IP address resources in an organized manner.
*   IP pools can be defined for both IPv4 and IPv6 addresses.
*   Can create IP pools for different subnets or scopes, for example, LAN and Guest network.

**Configuration:**

*   **Add IP pool:** `/ip pool add name=<pool_name> ranges=<range_start>-<range_end>`
*   Use `/ip pool print` command to check existing pools.

### IP Routing

*   Determines the path network packets will take.
*   Static routes are manually added with a destination and a gateway.
*   Dynamic routing protocols like OSPF, RIP, and BGP allow automatic route learning.
*   Supports policy-based routing for advanced traffic control.
*   The route selection process involves selecting the most specific route for the destination of the packet.

**Configuration:**

*   **Add static route:** `/ip route add dst-address=<destination_network>/<subnet_mask> gateway=<gateway_address>`
*   **View routes:** `/ip route print`

### IP Settings

*   Global network settings in RouterOS.
*   Configuration options like allow-fast-path, ip-forwarding, icmp-rate-limit.
*   Impacts how the router handles IP traffic.
*   Use `/ip settings print` to see the current settings.
*  Modify using `/ip settings set <parameter> = <value>`.

**Configuration:**

*   `/ip settings set allow-fast-path=no`
*   `fast path` is an option for hardware offloading of routed packets.

### MAC Server

*   Provides information about hosts on the network using MAC addresses.
*   Used for debugging and MAC address monitoring.
*   Displays MAC, IP, and interface information.
*   Accessible using tools like Winbox or CLI.

**Configuration:**

*   `/tool mac-server print` to check status
*   `/tool mac-server set enabled=yes` to enable it

### RoMON (Router Management Overlay Network)

*   Allows managing multiple MikroTik routers using a single interface.
*   Creates an overlay network using a unique RoMON ID.
*   Devices communicate over Layer 2 and can be accessed regardless of IP configurations.
*   Provides an alternative management method when IP access is unavailable.
*   Can be password protected.

**Configuration:**

*   `/romon set enabled=yes interface=<interface>`
*   `/romon set password=<password>`
*   `Use /tool romon print` to view current settings.

### WinBox

*   The GUI configuration tool for MikroTik RouterOS.
*   Provides a graphical interface to manage router settings.
*   Supports drag-and-drop configurations and live monitoring.
*   Connects over TCP, can be done via IP address or RoMON.
*   All CLI configurations can be performed via Winbox interface using corresponding menus.

**Configuration:**

*   Connect via IP or RoMON, or directly using MAC Address
*   Navigate via menus for each section, to implement all CLI commands described above.

### Certificates

*   Used for secure communication (HTTPS, IPsec).
*   Can use self-signed or CA-signed certificates.
*   Import or generate certificates within RouterOS.
*  Used for secure connections using services like Winbox, HTTPS API access.

**Configuration:**

*   `/certificate print`
*   `/certificate import file=<certificate_file>`
*   `/certificate generate-self-signed name=<certificate_name>`

### PPP AAA

*   AAA (Authentication, Authorization, Accounting) services for Point-to-Point Protocol connections.
*   Can be linked to an external RADIUS server for user management.
*   Controls user access for VPN connections (PPTP, L2TP, PPPoE).
*   Can be configured in PPP profiles.

**Configuration:**

*   `/ppp profile set use-radius=yes <profile_name>`
*   `/ppp secret set service=<service_name> profile=<profile_name>`

### RADIUS (Remote Authentication Dial-In User Service)

*   A centralized authentication and authorization system.
*   Used to manage user credentials and access policies.
*   Radius client is configured on MikroTik, and connects to the server to validate credentials.
*   Supports various protocols and services (PPP, Hotspot).

**Configuration:**

*   `/radius add address=<radius_ip> secret=<radius_secret>`
*   `port`, `accounting-port`, `timeout` etc. can be specified.

### User / User Groups

*   Manage user accounts on the MikroTik router.
*   Users can be assigned to groups with specific access privileges.
*   Use to control administrative access and permissions.
*   Create a separate administrative user from the default `admin` user for security.

**Configuration:**

*   `/user add name=<user_name> password=<user_password> group=full`
*   `/user print`
*   `/user group print`
*   `/user disable <user_name>`
*   `/user enable <user_name>`

### Bridging and Switching

*   Combines multiple interfaces into a single Layer 2 broadcast domain.
*   Supports Ethernet, WiFi, VLAN interfaces.
*   Allows devices on different interfaces to communicate on the same subnet.
*   Bridge settings such as `fast-forward` and `hw` can optimize performance.

**Configuration:**

*   `/interface bridge add name=<bridge_name>`
*   `/interface bridge port add bridge=<bridge_name> interface=<interface_name>`
*   Use `/interface bridge print` to check existing configuration

### MACVLAN

*   Creates multiple virtual interfaces on a single physical interface using different MAC addresses.
*   Each virtual interface has its own IP address and settings.
*   Useful for creating multiple isolated networks on a single interface.

**Configuration:**

*   `/interface macvlan add mac-address=<mac_address> interface=<interface_name> name=<macvlan_name>`
*   assign IP addresses to macvlan interfaces.

### L3 Hardware Offloading

*   Speeds up L3 routing by processing it in hardware rather than CPU.
*   Enables higher