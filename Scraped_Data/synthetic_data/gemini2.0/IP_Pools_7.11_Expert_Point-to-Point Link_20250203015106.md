Okay, let's delve into a comprehensive technical documentation for IP Pools in MikroTik RouterOS 7.11, tailored for an expert user.

## MikroTik RouterOS: IP Pools - Expert Level Configuration for Point-to-Point Links

This documentation focuses on a point-to-point link, using a /24 subnet, configured on interface `ether-55`, with emphasis on core MikroTik concepts and commands. We will cover IP Pools in depth, touching upon relevant topics as specified.

### 1. Configuration Scenario and MikroTik Requirements

**Scenario:** We are setting up a point-to-point link between two MikroTik routers (or a router and a client device). One router will act as the "server" and allocate IP addresses from a designated pool using DHCP server, while the other device could either request the IP automatically or set statically on the specific interface. For this documentation, we will focus primarily on the server side configuration of the IP Pool, DHCP server and network interface.

**Specific Requirements:**

*   **Subnet:** 245.159.167.0/24
*   **Interface Name:** ether-55
*   **Configuration Level:** Expert
*   **Network Scale:** Point-to-Point Link
*   **RouterOS Version:** 7.11 (Targeted, but most concepts applicable to 6.48, 7.x)

### 2. Step-by-Step MikroTik Implementation

We'll perform these steps using the CLI for precision and automation, although corresponding Winbox actions are discussed.

**Steps:**

1.  **Define the IP Pool:** This will be the range of IP addresses we'll allocate.
2.  **Configure the IP address:** Set static IP on the server's `ether-55` interface.
3.  **Configure DHCP Server:** Enable and configure DHCP server on the `ether-55` interface.
4.  **Verify:** Use ping, torch, and other diagnostic tools.

### 3. Complete MikroTik CLI Configuration Commands

Here are the CLI commands with detailed explanations.

```mikrotik
# 1. Define the IP Pool
/ip pool
add name=point-to-point-pool ranges=245.159.167.100-245.159.167.200

# Explanation:
# /ip pool - Navigates to the IP Pool configuration section.
# add - Creates a new IP Pool.
# name=point-to-point-pool - Sets the name of the pool. This name is used in DHCP server configuration.
# ranges=245.159.167.100-245.159.167.200 - Specifies the IP address range that will be included in this pool.

# 2. Configure the IP address on the interface
/ip address
add address=245.159.167.1/24 interface=ether-55 network=245.159.167.0

# Explanation:
# /ip address - Navigates to the IP Address configuration section.
# add - Creates a new IP address configuration.
# address=245.159.167.1/24 - Assigns the IP address 245.159.167.1 with a /24 subnet mask to the interface. This IP will serve as the gateway for clients.
# interface=ether-55 - Specifies that this IP address will be assigned to the interface named ether-55.
# network=245.159.167.0 - Defines the network this address belongs to. It's not strictly necessary but good practice.

# 3. Configure DHCP Server
/ip dhcp-server
add address-pool=point-to-point-pool disabled=no interface=ether-55 lease-time=1d name=point-to-point-dhcp
/ip dhcp-server network
add address=245.159.167.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=245.159.167.1

# Explanation:
# /ip dhcp-server - Navigates to the DHCP Server configuration section.
# add - Creates a new DHCP server configuration.
# address-pool=point-to-point-pool - Associates this DHCP server with the previously defined IP pool.
# disabled=no - Enables the DHCP server.
# interface=ether-55 - Specifies that the DHCP server will listen on the specified interface.
# lease-time=1d - Sets the lease time for IP addresses allocated via DHCP, in this case, 1 day.
# name=point-to-point-dhcp - Assigns a name for the DHCP server
# /ip dhcp-server network - Navigates to DHCP server network configuration.
# add - Creates a new DHCP server network configuration.
# address=245.159.167.0/24 - Defines the network the DHCP server is serving.
# dns-server=8.8.8.8,8.8.4.4 - Configures DNS servers for DHCP clients. Google DNS in this case.
# gateway=245.159.167.1 - Sets the gateway for DHCP clients.

```

**Winbox Equivalent:**

*   **IP Pool:** Navigate to "IP" -> "Pool" and add a new entry.
*   **IP Address:** Navigate to "IP" -> "Addresses" and add a new entry.
*   **DHCP Server:** Navigate to "IP" -> "DHCP Server," add a new DHCP server, then navigate to the "Networks" tab and create a network entry.

### 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Pool Range Conflicts:** The IP pool must be within the subnet configured on the interface.
*   **Interface Mismatch:** DHCP server and interface configurations must match.
*   **Firewall Rules:** Default MikroTik firewall rules can block DHCP or ICMP; be mindful of those.
*   **Lease Time:** A very short lease time might lead to constant re-assignments.
*   **Address-conflict:** An address in use that is also within the pool will create issues.

**Troubleshooting:**

*   **DHCP Server Logs:** `system log print topics=dhcp` to diagnose DHCP issues.
*   **Packet Sniffer:** `/tool sniffer` or `torch` tool on `ether-55` to observe DHCP packets.
*   **Address Conflicts:** Monitor address conflicts in the DHCP leases.
*   **Interface Status:** Check that the interface is enabled and has proper link. `interface print`

**Example Error Scenario:**

If the IP address on `ether-55` is *not* within the same subnet mask as the DHCP network, the client won't get DHCP and may not even communicate, example:

```mikrotik
/ip address
add address=10.0.0.1/24 interface=ether-55
/ip dhcp-server network
add address=245.159.167.0/24 gateway=245.159.167.1 dns-server=8.8.8.8,8.8.4.4
```
In the above scenario, the IP on the `ether-55` interface will not be in the same network.

```
[admin@MikroTik] > /ip dhcp-server network print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS          GATEWAY         DNS-SERVER                   DOMAIN
 0   245.159.167.0/24   245.159.167.1 8.8.8.8,8.8.4.4
[admin@MikroTik] > /ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0  10.0.0.1/24        10.0.0.0        ether-55
```
The client would not be able to receive an IP. This is an extremely common issue.

### 5. Verification and Testing

**Verification Commands:**

*   **Ping:** `ping 245.159.167.1` from a client or any other IP in the same subnet to check connectivity. `ping 245.159.167.100` from the server to ping a specific IP in the pool.
*   **DHCP Leases:** `/ip dhcp-server lease print` to view issued IP addresses and client MAC addresses.
*   **Interface Status:** `interface print` to verify the status of `ether-55`.
*   **Torch:** `/tool torch interface=ether-55` to view real-time traffic on the interface.
*   **Traceroute:** `traceroute 8.8.8.8` from the client to verify if it can reach external hosts.

**Testing Steps:**

1.  Connect a client device to `ether-55`.
2.  Ensure the client is configured to use DHCP.
3.  Check the client's IP address.
4.  Ping the server IP address (245.159.167.1).
5.  Ping external addresses to test routing.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **IP Pool Usage:** IP pools are not only used by DHCP server but also for IPsec, and other features requiring IP address assignment.
*   **Multiple Pools:** MikroTik allows the creation of multiple IP pools for different purposes (VLANs, clients, etc.).
*   **Static DHCP Leases:** You can assign static IP addresses from the pool based on the client's MAC address. `/ip dhcp-server lease add address=245.159.167.150 mac-address=00:01:02:03:04:05 server=point-to-point-dhcp`
*   **Pool Ordering:** When multiple pools exist, MikroTik allocates IP addresses based on the order they are defined.
*   **Lease-Time:** The lease-time configuration influences how often clients request and renew the DHCP lease.
*   **Limitations:** DHCP Server in RouterOS cannot provide options beyond what it is programmed to provide. For instance, it cannot push a specific gateway for each MAC-address or client.
*   **RADIUS:** DHCP can be integrated with RADIUS server for centralized authentication/accounting.

**Less Common Features:**

*   **DHCP Options:** Using DHCP options for more advanced configurations (e.g., custom DNS servers, boot server).  This can be set under the `/ip dhcp-server network` section. `/ip dhcp-server network set 0 dhcp-option=43:"010400000000"` for Vendor-Specific Information.
*   **MAC-Address Filtering:** DHCP can be configured to only provide IP's to known MAC's.
*   **Client Scripts:** MikroTik can execute scripts upon DHCP lease assignments, and can make use of variables such as client mac-address, client IP, server-address, etc.

### 7. MikroTik REST API Examples

**Important:** MikroTik's REST API has not reached full parity with CLI/Winbox in every aspect.  However, essential tasks can be done using the API. You should enable and use HTTPS for security.

**Enable HTTPS:**
```mikrotik
/ip service enable api-ssl
```

**Base URL (replace with your router IP):**
`https://<router-ip>/rest/`

**API Example 1: Get IP Pool details**

*   **Endpoint:** `/ip/pool`
*   **Method:** `GET`
*   **Request Body:** (None)
*   **Example curl command:**
```bash
curl -k -u admin:password https://<router-ip>/rest/ip/pool
```
*   **Expected Response (JSON):**
```json
[
    {
        ".id": "*1",
        "name": "point-to-point-pool",
        "ranges": "245.159.167.100-245.159.167.200"
    }
]
```

**API Example 2: Create a new IP Pool (Note: You'd typically use POST method)**

*   **Endpoint:** `/ip/pool`
*   **Method:** `POST`
*   **Request Body:**
```json
{
  "name": "test-pool",
  "ranges": "192.168.200.100-192.168.200.200"
}
```
*   **Example curl command:**
```bash
curl -k -u admin:password -H "Content-Type: application/json" -X POST -d '{"name": "test-pool", "ranges": "192.168.200.100-192.168.200.200"}' https://<router-ip>/rest/ip/pool
```
*   **Expected Response (JSON):**
```json
  {
    ".id": "*2"
  }
```

**API Example 3: Get DHCP Server details**

*   **Endpoint:** `/ip/dhcp-server`
*   **Method:** `GET`
*   **Request Body:** (None)
*  **Example curl command:**
```bash
curl -k -u admin:password https://<router-ip>/rest/ip/dhcp-server
```
* **Expected Response (JSON):**
```json
[
    {
        ".id": "*0",
        "name": "point-to-point-dhcp",
        "interface": "ether-55",
        "address-pool": "point-to-point-pool",
        "lease-time": "1d",
        "authoritative": "yes",
        "disabled": "no",
        "add-arp": "yes"
    }
]
```

**API Example 4: Update DHCP server settings**
*   **Endpoint:** `/ip/dhcp-server/*0`
*   **Method:** `PUT`
*   **Request Body:**
```json
{
  "lease-time": "2d"
}
```
*   **Example curl command:**
```bash
curl -k -u admin:password -H "Content-Type: application/json" -X PUT -d '{"lease-time": "2d"}' https://<router-ip>/rest/ip/dhcp-server/*0
```
*   **Expected Response (JSON):**
```json
{
    "lease-time": "2d"
}
```

**Notes:**

*   Replace `<router-ip>` with your router's actual IP address.
*   Use a proper client to send the request and handle the response.
*   Always enable HTTPS for API access for security and provide the appropriate credentials.
*  `.id` value will vary based on the current configuration. Always verify before executing PUT operations.

### 8. In-Depth Explanations of Core Concepts

*   **IP Addressing:** The foundation of network communication. We use IPv4 here, with a subnet of /24, allowing up to 254 hosts. Each IP within a subnet must have its unique network and host components.
*   **IP Pools:** A logical group of IP addresses managed by MikroTik. It doesn't have a physical representation, but represents a range that can be allocated by features such as DHCP. The pool name is used as a reference in other configuration elements (like DHCP).
*   **IP Routing:** Not directly in play here (in the client scenario), because we're focusing on a single point-to-point link, but each MikroTik router has an IP routing table that dictates how traffic is forwarded. DHCP clients have a default gateway set.
*  **IP Settings:** The settings that are defined under `/ip settings` can be useful for advanced network configurations and specific scenarios such as disabling packet fragmentation.

### 9. Security Best Practices

*   **Strong Passwords:** Use a strong, complex password for the MikroTik router.
*   **Disable Unused Services:** Turn off services that are not in use, such as `api`, `www`, `telnet` and `ftp`.
*   **HTTPS for API Access:** Always use HTTPS with API enabled for secure communication.
*   **Firewall Rules:** Configure firewall rules to protect your router from outside access. Use input chains to control management interfaces and forward chains to control traffic flow. `ip firewall filter add chain=input in-interface=ether-55 protocol=tcp dst-port=8291 action=accept comment="Allow Winbox Access"`. `ip firewall filter add chain=input in-interface=ether-55 protocol=tcp dst-port=80 action=drop comment="Drop WWW Access"`.
*   **Limit Access:** Restrict access to Winbox, SSH, and other services using firewall rules based on source IP addresses.
*   **Regular Updates:** Keep RouterOS updated to address known vulnerabilities. `/system package update check-for-updates`.

### 10. Detailed Explanations and Configuration Examples for Specified Topics

This is the bulk of the document and we will go over each topic individually, explaining and providing detailed examples.

#### IP Addressing (IPv4 and IPv6)
*   **IPv4:** Uses 32-bit addresses represented in dot-decimal notation (e.g., 192.168.1.1). Subnet masks define network size (e.g., /24 means 255.255.255.0).
    *   **Example:** `/ip address add address=192.168.10.1/24 interface=ether1` adds an IPv4 address to ether1.
*   **IPv6:** Uses 128-bit addresses, typically represented in colon-hexadecimal notation (e.g., 2001:0db8::1). Has similar subnet concepts, but use prefix lengths (e.g., /64).
    *   **Example:** `/ipv6 address add address=2001:db8::1/64 interface=ether1` adds an IPv6 address to ether1.
    *   **Example of setting a static IPv6 address (must be linked to an IPv6 prefix):**
```mikrotik
        /ipv6 address
        add address=2001:db8:1::1/64 interface=ether-55
```
    *   **Example of setting up an IPv6 DHCP Client on interface ether-55:**
```mikrotik
       /ipv6 dhcp-client
       add interface=ether-55 request=address,prefix use-peer-dns=yes add-default-route=yes
```
    *   **Example of setting up an IPv6 DHCP Server on interface ether-55:**
```mikrotik
       /ipv6 pool
       add name=ipv6-pool prefix=2001:db8:1::/64
       /ipv6 dhcp-server
       add interface=ether-55 address-pool=ipv6-pool name=ipv6-dhcp
       /ipv6 dhcp-server network
       add address=2001:db8:1::/64
```

#### IP Pools
*   As previously discussed, IP Pools are logical containers for IP addresses. Pools are typically used to allocate IP addresses automatically using DHCP or for the allocation in IPsec and other VPN features.
    *   **Example:** `/ip pool add name=my-pool ranges=192.168.1.10-192.168.1.254` creates a pool named 'my-pool'.
    *   **Example of IP Pool used in DHCP server:** `/ip dhcp-server add name=my-dhcp interface=ether2 address-pool=my-pool`.
    *  **Example of multiple IP Pool Ranges:** `/ip pool add name=my-pool ranges=192.168.1.10-192.168.1.20,192.168.1.50-192.168.1.70`
    *   **Example of IPv6 pool:** `/ipv6 pool add name=my-ipv6-pool prefix=2001:db8:1::/64`

#### IP Routing
*   MikroTik uses a routing table to determine the best path for IP packets to reach their destination. Routes can be static or dynamically learned through routing protocols such as OSPF, BGP or RIP.
    *   **Example Static Route:** `/ip route add dst-address=10.0.0.0/24 gateway=192.168.2.1` creates a static route for the 10.0.0.0/24 network.
    *   **Example of removing a static route:** `/ip route remove [find dst-address=10.0.0.0/24]`.
   * **Example using policy based routing:**
```mikrotik
/ip route rule
add dst-address=192.168.1.0/24 action=lookup-only-in-table table=table1
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.2.1 routing-mark=table1
/ip route
add dst-address=0.0.0.0/0 gateway=192.168.3.1
```
This example will use 192.168.2.1 to reach anything in the 192.168.1.0/24 network and 192.168.3.1 for everything else.

#### IP Settings
*   Global IP settings control various parameters, like IP forwarding, TCP settings and more.
    *  **Example:** `/ip settings set ip-forward=yes tcp-syncookies=yes max-queued-tcp-connections=2500`
    *  **Example of disabling source routing:** `/ip settings set allow-source-routing=no`
    *  **Example of disabling ICMP redirect:** `/ip settings set send-redirects=no`

#### MAC Server
*   The MAC server allows access to the router via MAC address. This can be used to bypass network or IP configurations and connect directly to the router's MAC interface. Use caution enabling this feature.
    *   **Example:** `/tool mac-server set allowed-interfaces=ether1 enabled=yes` allows MAC-level access via interface ether1.
    *   **Example of setting the username and password for the MAC Server:**
```mikrotik
        /tool mac-server
        set allowed-interfaces=ether1 enabled=yes
        /tool mac-server mac-winbox
        add disabled=no users=macuser
        /user add name=macuser group=full password=macpassword
```
   *  **Example of disabling the MAC server:** `/tool mac-server set enabled=no`

#### RoMON
*   RoMON (Router Management Overlay Network) is used to manage MikroTik routers across different networks. It allows you to discover and connect to devices through their MAC addresses. Not enabled by default.
    *   **Example:** `/tool romon set enabled=yes` enables RoMON.
    *   **Example of setting a custom RoMON ID:** `/tool romon set enabled=yes id=myromonid`
   *  **Example of adding a RoMON Secret password:** `/tool romon set enabled=yes secret=mysecret`. Be careful with RoMON as a weak password can expose the routers in your network. It is recommended to use a randomly generated password.
   *  **Example of disabling RoMON:** `/tool romon set enabled=no`

#### WinBox
*   Winbox is a GUI utility to manage MikroTik devices. Uses tcp port 8291.
    *  **Example of changing WinBox port:** `/ip service set winbox port=8292`
    *  **Example of disabling WinBox:** `/ip service set winbox disabled=yes`
    *   **Example of limiting the WinBox access:**
```mikrotik
      /ip firewall filter
      add chain=input in-interface=ether1 protocol=tcp dst-port=8291 action=accept comment="Allow Winbox from known subnet" src-address=192.168.1.0/24
      add chain=input in-interface=ether1 protocol=tcp dst-port=8291 action=drop comment="Drop other Winbox connections"
```

#### Certificates
*   Certificates are used for secure communication (HTTPS, IPsec, etc.). RouterOS supports importing and generating certificates.
    *   **Example Import Certificate:** `/certificate import file-name=mycert.pem passphrase=mypassword`
    *   **Example of generating a self-signed certificate:** `/certificate add name=my-self-signed common-name=router.local key-usage=digital-signature,key-encipherment,tls-server`
   *  **Example of exporting a certificate:** `/certificate export certificate=my-self-signed file-name=my-self-signed.crt`
   * **Example of enabling HTTPS and choosing a certificate:**
```mikrotik
     /ip service set api-ssl certificate=my-self-signed
```

#### PPP AAA
*   PPP (Point-to-Point Protocol) AAA (Authentication, Authorization, Accounting) allows you to control and manage dial-in connections. Used for PPPoE, PPTP and L2TP.
    *   **Example Local User Setup:** `/ppp secret add name=myuser password=mypassword service=pppoe`
    *   **Example of setting up a PPPoE server:**
```mikrotik
      /interface pppoe-server server
      add interface=ether1 service-name=mypppoe enabled=yes
```
   *  **Example of setting up a PPPoE Client:**
```mikrotik
       /interface pppoe-client
       add user=myuser password=mypassword interface=ether1 add-default-route=yes
```
   *   **Example of disabling PPP AAA for all interfaces:** `/ppp secret set * disabled=yes`

#### RADIUS
*   RADIUS (Remote Authentication Dial-In User Service) allows centralized authentication, authorization and accounting. Commonly used for WiFi access or PPPoE services.
    *   **Example Add RADIUS server:** `/radius add address=192.168.1.1 secret=myradiussecret`
    *  **Example using RADIUS with PPP AAA:**
```mikrotik
       /ppp profile set default use-radius=yes
```
   *  **Example using RADIUS with DHCP:**
```mikrotik
    /ip dhcp-server set 0 use-radius=yes
```
    * **Example of setting up a RADIUS server on a remote host:**
```mikrotik
   /radius
    add address=192.168.10.1 secret=mysecret service=ppp timeout=10
```

#### User / User groups
*   RouterOS uses users and groups to control access and permissions. Groups allow you to set multiple user permissions at once.
    *   **Example Create User:** `/user add name=testuser password=mypassword group=read`
    *   **Example Create Group:** `/user group add name=superadmin policy=write,read,test,password`
     * **Example of setting a specific user password:** `/user set testuser password=newpass`
     *  **Example of removing a specific user:** `/user remove testuser`
     *  **Example of setting a specific user group:** `/user set testuser group=write`

#### Bridging and Switching
*   Bridging allows you to combine multiple network interfaces together acting like a switch, making the router behave like a Layer 2 device. Switching is the basic functionality for forwarding frames based on MAC addresses within a bridge or on a router with built-in switch chip.
    *   **Example Bridge Creation:** `/interface bridge add name=mybridge`
    *   **Example Adding Interfaces to Bridge:** `/interface bridge port add bridge=mybridge interface=ether1` `/interface bridge port add bridge=mybridge interface=ether2`
    *   **Example setting up the Spanning Tree Protocol (STP) on a bridge:** `/interface bridge set mybridge stp=yes`
    *   **Example of using the bridge to forward only untagged traffic and dropping all tagged traffic:**
```mikrotik
       /interface bridge port
       add bridge=mybridge interface=ether1 pvid=1 frame-types=admit-only-untagged
       add bridge=mybridge interface=ether2 pvid=1 frame-types=admit-only-untagged
```
   * **Example using a bridge to manage VLANs:**
```mikrotik
    /interface bridge
    add name=bridge1
    /interface bridge port
    add bridge=bridge1 interface=ether1
    add bridge=bridge1 interface=ether2 pvid=10 frame-types=admit-only-vlan-tagged
    /interface bridge vlan
    add bridge=bridge1 tagged=ether1 vlan-ids=10
```
    *   **Example of setting up hardware offloading on a bridge:** `/interface bridge set mybridge use-ip-firewall=no use-ip-firewall-for-vlan=no use-ip-firewall-for-raw=no`

#### MACVLAN
*  MACVLAN creates virtual interfaces on a physical interface, using different MAC address. Allows multiple MAC addresses on the same interface.
     *   **Example creation of a MACVLAN interface:** `/interface macvlan add interface=ether1 mac-address=02:02:02:02:02:02`
     * **Example setting a IP on a MACVLAN interface:** `/ip address add address=192.168.1.2/24 interface=macvlan1`.
    *  **Example of using a MACVLAN with DHCP:**
```mikrotik
       /ip dhcp-server
       add address-pool=my-pool disabled=no interface=macvlan1 lease-time=1d name=macvlan-dhcp
```

#### L3 Hardware Offloading
*   Offloads Layer 3 forwarding to the switch chip. Allows for increased performance for routing capabilities.
    *   **Example enabling hardware offloading:** `/interface ethernet set ether1 l3-hw-offloading=yes`
    *   **Example disabling hardware offloading:** `/interface ethernet set ether1 l3-hw-offloading=no`
   *   **Example of displaying the status of L3 HW offloading:** `interface ethernet print` and observe the `l3-hw-offloading` value.

#### MACsec
*   MACsec provides encryption on the Layer 2 level, it can be used to secure traffic between two MikroTik devices.
    *   **Example enable MACsec profile:**
```mikrotik
     /interface macsec profile
     add name=myprofile cipher-suite=gcm-aes-256-gmac-xpn confidentiality-offset=30 sa-key=0123456789abcdef0123456789abcdef
     /interface macsec
     add interface=ether1 profile=myprofile enabled=yes
```
   *   **Example of disabling MACsec on an interface:** `/interface macsec set 0 enabled=no`
   * **Example of adding a second interface to MACsec:**
```mikrotik
     /interface macsec add interface=ether2 profile=myprofile enabled=yes
```

#### Quality of Service
*   QoS controls the priority of network traffic. MikroTik provides many ways to implement QoS, from Simple Queues to complex HTB queues.
    *   **Example Simple Queue:** `/queue simple add target=192.168.1.0/24 max-limit=1M/1M name=myqueue` limits all the traffic in this subnet to 1 Mbit up/down.
    *   **Example setting up a queue tree to prioritize specific traffic:**
```mikrotik
       /queue tree
       add name="parent" parent=global-out max-limit=10M
       add name="priority" parent="parent" packet-mark="voice-mark" queue=default-small
       add name="default" parent="parent" queue=default
       /ip firewall mangle
       add chain=prerouting action=mark-packet new-packet-mark=voice-mark protocol=udp src-port=5060
```
   * **Example of setting up a queue with burst:**
```mikrotik
    /queue simple
    add name=queue1 target=192.168.1.10/32 max-limit=5M/5M burst-limit=10M/10M burst-threshold=7M/7M burst-time=30s
```
   * **Example of using PCQ:**
```mikrotik
    /queue type
    add name=pcq-download kind=pcq pcq-rate=5M pcq-classifier=dst-address
    /queue type
    add name=pcq-upload kind=pcq pcq-rate=2M pcq-classifier=src-address
    /queue simple
    add name=users target=192.168.1.0/24 queue=pcq-download/pcq-upload
```

#### Switch Chip Features
*   If your RouterBOARD has an embedded switch chip, you can configure VLANs, port mirroring, etc. at hardware level.
    *   **Example VLAN Creation on Switch Chip:** `/interface ethernet switch vlan add vlan-id=10 ports=ether1,ether2`
    *   **Example Setting the default VLAN id on a switch port:** `/interface ethernet switch port set ether1 default-vlan-id=10`
   *  **Example of setting up a port as trunk:** `/interface ethernet switch port set ether1 vlan-mode=secure vlan-header=add-if-missing`
   *  **Example of disabling hardware switching on a specific port:** `/interface ethernet switch port set ether1 switch-disabled=yes`

#### VLAN
*   VLANs (Virtual LANs) segment a physical network into smaller broadcast domains. VLANs are identified by a VLAN ID (802.1Q tag).
    *   **Example Create VLAN Interface:** `/interface vlan add name=vlan10 vlan-id=10 interface=ether1`
    *   **Example Adding a IP address on a VLAN interface:** `/ip address add address=192.168.10.1/24 interface=vlan10`.
   *  **Example of using VLAN's with bridge:**
```mikrotik
    /interface bridge
    add name=bridge1
    /interface bridge port
    add bridge=bridge1 interface=ether1 pvid=1
    add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged pvid=10
    /interface vlan
    add name=vlan10 vlan-id=10 interface=bridge1
```
   *   **Example of setting up a VLAN on a bridge with an untagged interface:**
```mikrotik
        /interface bridge
        add name=bridge1
        /interface bridge port
        add bridge=bridge1 interface=ether1 pvid=1
        add bridge=bridge1 interface=ether2 pvid=10 frame-types=admit-only-vlan-tagged
        /interface bridge vlan
        add bridge=bridge1 tagged=ether