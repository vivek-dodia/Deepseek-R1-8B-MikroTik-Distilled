Okay, let's dive into creating comprehensive documentation for MikroTik RouterOS, focusing on IP addressing and related features, targeted at an ISP-level network environment. This will be a very extensive document, covering the full range of requested topics.

# MikroTik RouterOS for ISPs: Comprehensive IP Addressing and Beyond

This document provides in-depth technical guidance for configuring and managing MikroTik routers within an Internet Service Provider (ISP) setting. We will use RouterOS v7.12 (though most concepts apply to 6.x or 7.x) and assume an advanced configuration level.

## 1. Configuration Scenario and Requirements

**Scenario:**

We are building the core routing infrastructure for a small to medium-sized ISP. The network consists of:

*   **Core Router (CCR):** Manages routing between upstream providers and customer edge routers.
*   **Customer Edge Routers (CERs):** Located at the customer premises and connect to the core router.
*   **Public IPv4 Addressing:**  We use a /24 range from our upstream provider and allocate blocks to customers.
*   **Public IPv6 Addressing:** We use a /48 range from our upstream provider and allocate /64 blocks to customers.
*   **Internal Management Network:** IPv4 range for router management, isolated from customer networks.
*   **Dynamic Customer Addressing:** Customer IP assignment using DHCP for IPv4 and SLAAC/DHCPv6 for IPv6.
*   **Basic QoS:** Bandwidth limiting on customer-facing interfaces.
*   **Security:** Robust firewall rules to protect the infrastructure.
*   **VPN Access:** Allow remote access to core router for maintenance.
*   **Monitoring:** SNMP for basic infrastructure monitoring.

**MikroTik Requirements:**

*   High performance and stability of the Core Router (CCR).
*   Scalability to support a growing customer base.
*   Flexibility in IP address assignment (static/dynamic).
*   Advanced routing capabilities (OSPF/BGP).
*   Comprehensive firewall and QoS features.
*   Secure management access.
*   Detailed logging for monitoring and troubleshooting.

## 2. Step-by-Step MikroTik Implementation (CLI & Winbox)

This will provide examples using both the command-line interface (CLI) and Winbox GUI, while most configuration can be done in both, certain complex commands might be easier to implement in CLI.

### 2.1. Initial Setup (CLI)
*   **Connect via SSH:** SSH into the MikroTik device.
*   **Set the Router Identity:**
    ```
    /system identity set name=core-router
    ```
*   **Set Time Zone:**
    ```
    /system clock set time-zone-name="America/New_York"
    ```

### 2.2. Interface Configuration (CLI/Winbox)

*   **Identify Interfaces:**  Use `/interface print` in CLI or the `Interfaces` tab in Winbox to identify your interfaces.  We'll assume `ether1` is for the uplink and `ether2` onwards connect to customers.
*   **Rename Interfaces (CLI):**
    ```
    /interface ethernet set ether1 name=WAN
    /interface ethernet set ether2 name=Customer1
    /interface ethernet set ether3 name=Customer2
     ```
* **Configure Interface IP Addresses (CLI):**
    ```
    /ip address add address=203.0.113.1/24 interface=WAN
    /ip address add address=192.168.100.1/24 interface=Customer1
    /ip address add address=192.168.101.1/24 interface=Customer2
    /ipv6 address add address=2001:db8::1/64 interface=WAN
    /ipv6 address add address=2001:db8:1::1/64 interface=Customer1
    /ipv6 address add address=2001:db8:2::1/64 interface=Customer2
    ```
* **Alternative GUI Configuration:** In the Winbox go to `IP->Addresses` add an IP address using the `+` button and set `Address` and `Interface` as required.

### 2.3. IP Pools (CLI)

* **Creating IPv4 Pool:**
  ```
  /ip pool add name=customer-ipv4-pool ranges=192.168.100.10-192.168.100.254
  ```

* **Creating IPv6 Pool:**
  ```
  /ipv6 pool add name=customer-ipv6-pool prefix=2001:db8:1::/64
  ```

* **Alternative GUI Configuration:** In the Winbox go to `IP->Pools` add an IP Pool using the `+` button and set `Name` and `Ranges` as required.

### 2.4. DHCP Server Setup (CLI)

* **IPv4 DHCP Server:**
    ```
    /ip dhcp-server add name=dhcp-customer1 address-pool=customer-ipv4-pool interface=Customer1 \
    lease-time=1h authoritative=yes
    /ip dhcp-server network add address=192.168.100.0/24 gateway=192.168.100.1 dns-server=8.8.8.8,8.8.4.4
    ```
*   **IPv6 DHCP Server:**
     ```
     /ipv6 dhcp-server add name=dhcpv6-customer1 interface=Customer1 address-pool=customer-ipv6-pool
     /ipv6 dhcp-server network add address=2001:db8:1::/64 dns-server=2001:4860:4860::8888,2001:4860:4860::8844
     ```
* **Alternative GUI Configuration:** In the Winbox go to `IP->DHCP Server` add a DHCP Server using the `+` button and set as required.

### 2.5. Basic Routing (CLI)

* **Add a Default IPv4 Route:**
    ```
    /ip route add dst-address=0.0.0.0/0 gateway=203.0.113.2
    ```
* **Add a Default IPv6 Route:**
    ```
    /ipv6 route add dst-address=::/0 gateway=2001:db8::2
    ```
* **Alternative GUI Configuration:** In the Winbox go to `IP->Routes` add a Route using the `+` button and set as required.

### 2.6. Firewall (CLI)

* **Basic IPv4 Input Filter:**
  ```
  /ip firewall filter add chain=input connection-state=established,related action=accept
  /ip firewall filter add chain=input protocol=icmp action=accept
  /ip firewall filter add chain=input in-interface=WAN action=drop
  ```
* **Basic IPv6 Input Filter:**
    ```
    /ipv6 firewall filter add chain=input connection-state=established,related action=accept
    /ipv6 firewall filter add chain=input protocol=icmpv6 action=accept
    /ipv6 firewall filter add chain=input in-interface=WAN action=drop
    ```
*   **NAT masquerade (IPv4):**
    ```
    /ip firewall nat add chain=srcnat out-interface=WAN action=masquerade
    ```
* **Alternative GUI Configuration:** In the Winbox go to `IP->Firewall` add a new rule using the `+` button and set as required, make sure to navigate between filter and NAT rules.

### 2.7.  QoS - Simple Queue (CLI)
*   **Create a queue for customer1:**
    ```
    /queue simple add name=customer1 target=192.168.100.0/24 max-limit=10M/10M
    ```
*  **Alternative GUI Configuration:** In the Winbox go to `Queues->Simple Queues`, add a queue rule using the `+` button and set as required.

### 2.8. Remote Management (CLI)

*   **Allow management access from specific IP:**
    ```
     /ip service set ssh address=192.168.0.0/24
     ```
*   **Alternative GUI Configuration:** In the Winbox go to `IP->Services`, you can modify ports or allowed addresses for each service

## 3. Complete MikroTik CLI Configuration

```
# System settings
/system identity set name=core-router
/system clock set time-zone-name="America/New_York"

# Interface settings
/interface ethernet set ether1 name=WAN
/interface ethernet set ether2 name=Customer1
/interface ethernet set ether3 name=Customer2

# IP Address
/ip address add address=203.0.113.1/24 interface=WAN
/ip address add address=192.168.100.1/24 interface=Customer1
/ip address add address=192.168.101.1/24 interface=Customer2
/ipv6 address add address=2001:db8::1/64 interface=WAN
/ipv6 address add address=2001:db8:1::1/64 interface=Customer1
/ipv6 address add address=2001:db8:2::1/64 interface=Customer2

# IP Pools
/ip pool add name=customer-ipv4-pool ranges=192.168.100.10-192.168.100.254
/ipv6 pool add name=customer-ipv6-pool prefix=2001:db8:1::/64

# DHCP Server
/ip dhcp-server add name=dhcp-customer1 address-pool=customer-ipv4-pool interface=Customer1 lease-time=1h authoritative=yes
/ip dhcp-server network add address=192.168.100.0/24 gateway=192.168.100.1 dns-server=8.8.8.8,8.8.4.4
/ipv6 dhcp-server add name=dhcpv6-customer1 interface=Customer1 address-pool=customer-ipv6-pool
/ipv6 dhcp-server network add address=2001:db8:1::/64 dns-server=2001:4860:4860::8888,2001:4860:4860::8844

# Routing
/ip route add dst-address=0.0.0.0/0 gateway=203.0.113.2
/ipv6 route add dst-address=::/0 gateway=2001:db8::2

# Firewall
/ip firewall filter add chain=input connection-state=established,related action=accept
/ip firewall filter add chain=input protocol=icmp action=accept
/ip firewall filter add chain=input in-interface=WAN action=drop
/ipv6 firewall filter add chain=input connection-state=established,related action=accept
/ipv6 firewall filter add chain=input protocol=icmpv6 action=accept
/ipv6 firewall filter add chain=input in-interface=WAN action=drop

/ip firewall nat add chain=srcnat out-interface=WAN action=masquerade

# QoS
/queue simple add name=customer1 target=192.168.100.0/24 max-limit=10M/10M

# Remote Management
/ip service set ssh address=192.168.0.0/24
```

## 4. Common MikroTik Pitfalls, Troubleshooting, and Diagnostics

**Pitfalls:**

*   **Firewall Misconfiguration:** Incorrect filter rules, especially the order of rules, can block necessary traffic.
*   **NAT Issues:** Double NAT can cause problems with certain applications.  Use `masquerade` correctly.
*   **Incorrect IP Addressing:** Conflicts between IPs, incorrect subnet masks, or mismatched addresses will lead to connectivity issues.
*   **Resource Constraints:**  Overloading the router with too many connections or complex QoS rules can lead to performance degradation.
*   **Insecure Defaults:** Default usernames and passwords, enabled services, and lack of firmware updates create security risks.
*   **Incorrect interface assignment:** The router needs to know which ports to work as WAN and LAN.

**Troubleshooting:**

*   **`/ping`:** Use the ping tool in the CLI to check basic connectivity to other devices.
*   **`/traceroute`:** Check path to a specific destination (including IPv6) to identify routing issues.
*   **`/interface monitor-traffic`:** Monitor interface traffic for bandwidth usage and congestion.
*   **`/tool torch`:** Capture and analyze network packets to diagnose problems.
*   **`/log print`:** Examine the RouterOS system log for errors and warnings.
*   **`/ip firewall connection print`**:  Check firewall connection tracking.
*   **`/system resource monitor`**: Check the CPU and Memory usage of the device
*   **Winbox:** Use the graphs available in Winbox to monitor CPU, Memory and interface traffic in real time.

**Diagnostics:**

*   **`/system health print`:** Check the overall health of the router (temperature, voltage).
*   **`/system resource print`:** View resource usage (CPU, memory, disk).
*   **`/interface ethernet monitor`**: Monitor link status, speed, and errors.
*   **Use the `Tools` menu** in Winbox for `Ping`, `Traceroute` and `Torch`.
*   **Use `Logs` menu** to examine logs.

**Error Handling:**

*   **Check Logs:** RouterOS provides detailed logs. Regularly check `/log print` for warnings or errors that might indicate a configuration issue or a problem.
*   **Rollback Configuration:** If you make a mistake, use `/system configuration rollback` to revert to the previous working configuration. Always take configuration backups.

## 5. Verification and Testing

*   **Ping test:**
    * **CLI** `ping <ip_address>`. For instance: `ping 8.8.8.8`
    * **Winbox** Go to `Tools->Ping` and execute the test.
*   **Traceroute test:**
    * **CLI** `traceroute <ip_address>`. For instance: `traceroute 8.8.8.8`
    * **Winbox** Go to `Tools->Traceroute` and execute the test.
*   **DHCP test:** Connect a client to an interface and see if it obtains an IPv4/IPv6 address successfully.
*   **Bandwidth test:** Use the bandwidth test tool `/tool bandwidth-test` to measure the link speed.
    * **CLI** `tool bandwidth-test address=192.168.100.1 user=<user> password=<pass> direction=both protocol=tcp`
    * **Winbox** Go to `Tools->Bandwidth Test` and execute the test.
*   **Firewall test:** Test if a firewall rule is working. Use `torch` to test.
*   **QoS test:** Check if the set bandwidth limits are being applied correctly.

## 6. Related MikroTik Features, Capabilities, and Limitations

*   **Bridging:** Combine multiple interfaces to act as a single network segment (Layer 2 forwarding).
*   **Routing:**  Advanced routing protocols like OSPF, BGP for complex topologies and multiple uplinks.
*   **Firewall:**  Connection-tracking, source and destination NAT, filtering based on addresses, ports, protocols, etc.
*   **Quality of Service:**  Control network bandwidth and prioritize traffic.
*   **IP Services:** Includes DHCP, DNS, SOCKS, and proxy servers, all built into RouterOS.
*   **VPN:** Wide array of VPN technologies, including IPsec, L2TP, PPTP, SSTP, OpenVPN, WireGuard.
*   **Mobile Networking:** Support for 3G/4G/LTE connections, useful for backup uplinks.
*   **MPLS:** Provides traffic engineering and QoS capabilities for carrier-grade networks.
*   **Network Management:** SNMP, Cloud access, Netflow, and more.
*   **System Utilities:** Scheduler, email notifications, fetch, time sync, etc.
* **Limitations:**
    * **Hardware**: Limited Hardware resources on lower tier devices may struggle with more demanding configurations.
    * **Single point of failure**: If used in a single configuration, the router represents a single point of failure for the network.
    * **Memory and CPU limitations:** Overly complex or large configurations may suffer from memory and CPU limits.
    * **Complexity:** Mikrotik can be complex for new users and may have a steep learning curve.

## 7. MikroTik REST API Examples

**Authentication:**  For simplicity, we'll use basic authentication. It is recommended to use a more secure authentication in production environments.

**API Endpoint:** `https://<your_router_ip>/rest/`

**7.1 Get Interface List**
*   **Request Method:** `GET`
*   **Endpoint:** `/rest/interface`
*   **Request Headers:** `Authorization: Basic <base64-encoded username:password>`
*   **Example `curl` command:**
    ```bash
    curl -X GET -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" https://192.168.88.1/rest/interface
    ```
*   **Example Response (JSON):**
    ```json
    [
      {
        "id": "*1",
        "name": "ether1",
        "type": "ether",
        "mtu": 1500,
        "actual-mtu": 1500,
         "link-downs": 0,
         "link-downs-since-reset": 0
      },
       {
        "id": "*2",
        "name": "ether2",
        "type": "ether",
        "mtu": 1500,
        "actual-mtu": 1500,
         "link-downs": 0,
         "link-downs-since-reset": 0
      }
    ]
    ```

**7.2 Get IP Address List**
*   **Request Method:** `GET`
*   **Endpoint:** `/rest/ip/address`
*   **Request Headers:** `Authorization: Basic <base64-encoded username:password>`
*   **Example `curl` command:**
    ```bash
     curl -X GET -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" https://192.168.88.1/rest/ip/address
    ```
*   **Example Response (JSON):**
    ```json
     [
        {
          "id": "*1",
          "address": "192.168.88.1/24",
          "network": "192.168.88.0",
          "interface": "ether1"
       }
     ]
    ```

**7.3 Add IP Address**

*   **Request Method:** `POST`
*   **Endpoint:** `/rest/ip/address`
*   **Request Headers:**
    *   `Authorization: Basic <base64-encoded username:password>`
    *   `Content-Type: application/json`
*   **Example JSON Payload:**
    ```json
    {
        "address": "192.168.88.2/24",
        "interface": "ether2"
    }
    ```
*   **Example `curl` command:**
    ```bash
    curl -X POST -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" -H "Content-Type: application/json" -d '{"address": "192.168.88.2/24", "interface": "ether2"}' https://192.168.88.1/rest/ip/address
    ```
*   **Example Response (JSON):**
    ```json
    {"id":"*2"}
    ```

**7.4 Update IP address**
*   **Request Method:** `PATCH`
*   **Endpoint:** `/rest/ip/address/<id>` (replace `<id>` with id from a previous GET operation)
*   **Request Headers:**
    *   `Authorization: Basic <base64-encoded username:password>`
    *   `Content-Type: application/json`
* **Example JSON Payload:**
    ```json
    {
      "address": "192.168.88.3/24"
    }
    ```
*   **Example `curl` command:**
    ```bash
    curl -X PATCH -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" -H "Content-Type: application/json" -d '{"address": "192.168.88.3/24"}' https://192.168.88.1/rest/ip/address/*2
    ```
* **Example Response (JSON):**
   ```json
    {"message":"updated"}
   ```

**7.5 Delete IP Address**
*   **Request Method:** `DELETE`
*   **Endpoint:** `/rest/ip/address/<id>` (replace `<id>` with id from a previous GET operation)
*   **Request Headers:** `Authorization: Basic <base64-encoded username:password>`
*   **Example `curl` command:**
    ```bash
    curl -X DELETE -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" https://192.168.88.1/rest/ip/address/*2
    ```
* **Example Response (JSON):**
    ```json
     {"message":"removed"}
    ```

**Note:** Always enable HTTPS for API access and restrict API access using firewall rules.

## 8. Core Concepts (MikroTik Implementation)

*   **Bridging:** MikroTik bridges use software forwarding to combine network interfaces into a single broadcast domain. Can optionally include a VLAN tag.
*   **Routing:** The core routing engine allows static routes, dynamic routing protocols like OSPF and BGP, policy-based routing, and VRF (Virtual Routing and Forwarding).
*   **Firewall:**  The firewall is based on connection tracking.  Rules are evaluated from top to bottom; the first matching rule takes action.
*   **IP Pools:** IP Pools are used to create blocks of IP addresses that are assigned to interfaces and clients.
*   **DHCP Server:**  Provides IP address assignment based on pool ranges, lease times, DNS servers. Can handle IPv4 and IPv6 addresses.
*   **Queue Management:** Hierarchical queuing is supported; simple queues and queue trees allow you to shape bandwidth.
*   **L3 Hardware Offloading:** Allows routers with supported hardware to perform routing and firewall tasks using the CPU.

## 9. Security Best Practices

*   **Change default username and passwords.**
*   **Disable unnecessary services (telnet, ftp).**
*   **Use strong passwords.**
*   **Implement a robust firewall configuration.**
*   **Regularly update RouterOS software.**
*   **Disable remote Winbox access on the WAN.**
*   **Configure a secure VPN for remote access.**
*   **Implement port knocking or rate limiting for management ports.**
*   **Use HTTPS for API access.**
*   **Filter management access to a limited list of IP addresses.**
*   **Implement IPS/IDS with fail2ban script.**
*   **Disable `ip/neighbour discovery` on WAN interfaces.**
*   **Enable RouterOS firewall for internal traffic between interfaces.**
*   **Filter access to all services using `/ip/services`.**
*   **Use IPsec or WireGuard to secure traffic if a VPN tunnel is required.**
*   **Avoid using the admin username, create a user with administrative privileges for day-to-day operations and keep the admin account for emergencies.**
*   **Back up regularly the router configuration.**

## 10. Detailed Explanations and Configuration Examples

### 10.1. IP Addressing (IPv4 and IPv6)

**IPv4:**

*   **Manual IP Address Configuration:**
    ```
    /ip address add address=<ip_address>/<cidr> interface=<interface_name>
    ```
*   **DHCP Client:** Obtain an address dynamically from a DHCP server.
    ```
    /ip dhcp-client add interface=<interface_name> disabled=no
    ```

**IPv6:**

*   **Manual IPv6 Address Configuration:**
    ```
    /ipv6 address add address=<ipv6_address>/<cidr> interface=<interface_name>
    ```
*   **SLAAC (Stateless Address Autoconfiguration):** The interface automatically configures a unique address based on its MAC address and the announced network prefix from the router.

*   **DHCPv6 Client:**
    ```
    /ipv6 dhcp-client add interface=<interface_name> request=address,prefix disabled=no
    ```

### 10.2 IP Pools
* **Static Pool**
   * **Definition**: a manually defined range of IP addresses
   * **Use Cases**: assign IP addresses to devices, define IP addresses for a specific network
   * **CLI Configuration**:
    ```
    /ip pool add name=static-ipv4-pool ranges=192.168.10.10-192.168.10.20
   ```
* **DHCP Pool**
   * **Definition**: an IP pool that will be assigned to DHCP server
   * **Use Cases**: Automatically give IP addresses to DHCP clients
   * **CLI Configuration**:
    ```
     /ip pool add name=dhcp-ipv4-pool ranges=192.168.100.10-192.168.100.254
    ```
* **Dynamic Pool**
   * **Definition**: an IP pool that will be created dynamically
   * **Use Cases**: automatically assign IP addresses using PPP/IPsec, etc.
   * **CLI Configuration**: You don't need to create dynamic pools as they will be created automatically when a client obtains a dynamic IP

### 10.3 IP Routing

*   **Static Routes:** Manually configured routes.
    ```
    /ip route add dst-address=<dest_address>/<cidr> gateway=<gateway_ip>
    ```
*   **Dynamic Routing Protocols:**
    *   **OSPF:**
        ```
        /routing ospf instance add name=default router-id=<router_id>
        /routing ospf network add network=<network_address>/<cidr> area=backbone
        ```
    *   **BGP:**
        ```
        /routing bgp instance add name=default as=<your_asn> router-id=<router_id>
        /routing bgp peer add name=upstream remote-address=<peer_ip> remote-as=<peer_asn>
        ```
*   **Policy Based Routing:** Routing based on source address, ports, etc.

    ```
    /ip route rule add src-address=<source_address>/<cidr> action=lookup-only-in-table table=<routing_table>
    /ip route add dst-address=<dest_address>/<cidr> gateway=<gateway_ip> routing-mark=<routing_table>
    ```
* **VRF:**
   * **Definition:** Virtual Routing and Forwarding allow the creation of multiple routing tables within the same router. Each VRF has its own interfaces, routing tables and rules.
   * **Use Cases:** Network isolation within the same router
   * **CLI Configuration**:
    ```
    /routing vrf add name=vrf-customer1 routing-mark=vrf-customer1
    /interface ethernet set ether2 vrf=vrf-customer1
    /ip address add address=10.0.0.1/24 interface=ether2 vrf=vrf-customer1
    /ip route add dst-address=0.0.0.0/0 gateway=10.0.0.2 routing-mark=vrf-customer1
    ```
*   **Route Filtering:**  Use `/routing filter` to control which routes are accepted or advertised.

### 10.4 IP Settings

*   **IP Forwarding:** Enable/disable packet forwarding.
    ```
    /ip settings set ip-forward=yes
    ```
*   **ARP Timeout:** Configure the ARP table timeout.
    ```
    /ip settings set arp-timeout=5m
    ```
*   **ICMP Redirects:** Control ICMP redirect generation.
    ```
    /ip settings set send-redirects=yes
    ```
*   **IP Source Validation:** Control IP source address validation.
    ```
    /ip settings set source-validation=yes
    ```
### 10.5 MAC server

* **Definition:** The MAC server is a service within RouterOS that allows you to discover and manage network devices through their MAC addresses.
* **Use Cases:** Useful to implement specific configurations or rules based on MAC addresses. It is also possible to remotely configure the devices using the MAC address if needed.
* **CLI Configuration:**
 ```
 /tool mac-server set allowed-interface=all
 /tool mac-server print
 ```

### 10.6 RoMON
* **Definition:** Router Management Overlay Network. A proprietary management protocol that allows to discover and manage RouterOS devices in a mesh topology.
* **Use Cases:** Remotely manage large deployments of MikroTik devices.
* **CLI Configuration:**
 ```
 /tool romon set enabled=yes
 /tool romon print
 ```

### 10.7 WinBox

* **Definition:** A GUI tool for managing MikroTik RouterOS devices.
* **Use Cases:** Manage devices using a graphical interface, monitor traffic, create or modify configurations
* **CLI Configuration:** Winbox does not have a CLI equivalent. Is necessary to install and use the graphical interface on your PC.

### 10.8 Certificates
* **Definition:** Use X.509 certificates to secure RouterOS services using TLS/SSL.
* **Use Cases:** HTTPS for Web server, API access, VPN connections and other RouterOS services.
* **CLI Configuration:**
```
/certificate import file=certificate.pem passphrase=<pass>
/certificate print
```

### 10.9 PPP AAA
* **Definition:** Authentication, Authorization, and Accounting protocols used by PPP, DHCP, VPN and other RouterOS services.
* **Use Cases:** Control user access to the RouterOS services.
* **CLI Configuration:**
```
/ppp profile add name=default-ppp dns-server=8.8.8.8,8.8.4.4 use-encryption=yes
/ppp secret add name=user1 password=password profile=default-ppp local-address=192.168.1.1 remote-address=192.168.1.2 disabled=no
```

### 10.10 RADIUS
* **Definition:** Centralized authentication server
* **Use Cases:** Use RADIUS to control user authentication for PPP, VPN, Wireless and other RouterOS services.
* **CLI Configuration:**
```
/radius add address=192.168.1.1 secret=secret timeout=30s
/ppp profile set use-radius=yes
```
### 10.11 User / User groups
* **Definition:** User accounts to login to the router via SSH, Winbox, or API.
* **Use Cases:** Assign permissions to different users to manage the device.
* **CLI Configuration:**
```
/user add name=user1 password=password group=full
/user group add name=test_group
/user group set test_group policy=read
```
### 10.12 Bridging and Switching

*   **Creating a Bridge:**
    ```
    /interface bridge add name=bridge1
    /interface bridge port add bridge=bridge1 interface=ether2
    /interface bridge port add bridge=bridge1 interface=ether3
    ```
*   **Spanning Tree Protocol (STP):**  Protect against loops in the network.
    ```
    /interface bridge set bridge1 stp=yes
    ```
*   **Switching:** Hardware-level forwarding between ports in the same bridge.
    *   **VLAN Tagging:** Tag traffic entering or exiting a bridge port.
        ```
        /interface bridge vlan add bridge=bridge1 vlan-ids=10,20
        /interface bridge port add bridge=bridge1 interface=ether2 pvid=10
        /interface bridge port add bridge=bridge1 interface=ether3 pvid=20
        ```
     *   **MSTP:** Create multiple STP domains.
        ```
        /interface bridge set bridge1 protocol-mode=mstp
        ```

### 10.13 MACVLAN
* **Definition:** A virtual interface created within an existing Ethernet interface. Each virtual interface will have a unique MAC address.
* **Use Cases:** Create multiple network segments using a single interface.
* **CLI Configuration:**
```
/interface macvlan add name=macvlan1 interface=ether2 mac-address=<MAC Address>
```

### 10.14 L3 Hardware Offloading
* **Definition:** Enables to perform L3 functionalities (like routing, firewall and others) in the router's hardware instead of relying on the CPU.
* **Use Cases:** Improve network performance in high traffic environments.
* **CLI Configuration:**
```
/interface ethernet set ether2 l3-hw-offloading=yes
```
### 10.15 MACsec
* **Definition:** A Layer 2 security protocol that encrypts communications at the link layer.
* **Use Cases:** Provide confidentiality and integrity to communication on the wired interfaces.
* **CLI Configuration:**
```
/interface macsec add name=macsec1 interface=ether2 pre-shared-key=secureKey
/interface ethernet set ether2 macsec=macsec1
```

### 10.16 Quality of Service

*   **Simple Queues:**  Basic bandwidth limiting.
    ```
    /queue simple add name=customer1 target=<ip_address>/<cidr> max-limit=10M/10M
    ```
*   **Queue Trees:**  More advanced QoS with traffic classification.
    ```
    /queue tree add name=upload parent=global-out max-limit=10M
    /queue tree add name=download parent=global-in max-limit=10M
    /queue type add name=htb kind=pcq pcq-classifier=dst-address
    /queue tree add name=customer1-upload parent=upload queue=htb
    /queue tree add name=customer1-download parent=download queue=htb
    /ip firewall mangle add chain=forward src-address=<ip_address>/<cidr> action=mark-packet new-packet-mark=customer1-upload
    /ip firewall mangle add chain=forward dst-address=<ip_address>/<cidr> action=mark-packet new-packet-mark=customer1-download
    /queue tree add parent=customer1-upload packet-mark=customer1-upload queue=htb
    /queue tree add parent=customer1-download packet-mark=customer1-download queue=htb
    ```

*   **Traffic Classification (Mangle):** Identify packets for specific QoS rules.
    ```
        /ip firewall mangle add chain=forward src-address=<ip_address>/<cidr> action=mark-packet new-packet-mark=customer1-traffic
    ```

### 10.17 Switch Chip Features
* **Definition:** MikroTik routers use specialized switch chips which include different functionalities that improve the