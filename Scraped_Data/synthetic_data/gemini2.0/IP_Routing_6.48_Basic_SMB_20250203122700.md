Okay, let's dive into creating detailed technical documentation for IP routing within MikroTik RouterOS, specifically targeting the given scenario.

## Scenario Description:

This document outlines the configuration required to enable IP routing for a subnet, `87.11.67.0/24`, on a MikroTik router, using a VLAN interface named `vlan-35`. This setup is typical for small to medium-sized businesses (SMBs) or within larger networks where VLAN segmentation is used. The goal is to ensure that devices on the `87.11.67.0/24` subnet can communicate with the rest of the network (or the Internet, depending on further configurations). This configuration focuses on the basics, using direct routing of this subnet, which will be the primary route for anything directly attached to this subnet.

## Implementation Steps:

Here's a step-by-step guide to implementing the required IP routing for `87.11.67.0/24` on interface `vlan-35`.

### Step 1: Verify Interface Existence and State

**Before:** Initially, we need to ensure the `vlan-35` interface exists and is enabled.

**Command (CLI):**
```mikrotik
/interface vlan print
```
**Expected Output (Example):**
```
Flags: X - disabled, D - dynamic, R - running, S - slave
 #    NAME                                MTU   MAC-ADDRESS       VLAN-ID INTERFACE
 0  R  vlan-10                            1500  XX:XX:XX:XX:XX:XX 10      ether1
 1  R  vlan-20                            1500  XX:XX:XX:XX:XX:XX 20      ether2
```
(You may not see `vlan-35` in this output, this is okay and shows how to create the vlan-35 interface below)

**Winbox GUI:**
Navigate to *Interface* menu. Look for `vlan-35` in the list. If it doesn't exist, or isn't enabled, you must create it using the steps below.

**Why this step:** This check ensures we're starting with the correct interfaces. We are expecting to find the required interface, or know that we need to create it.

**Action:** If the interface `vlan-35` doesn't exist, proceed to the next step. If it does exist and is disabled, re-enable the interface by unchecking the "Disabled" checkbox. Skip the next step, otherwise.

### Step 2: Create the VLAN Interface (If necessary)

**Before:** Assuming `vlan-35` doesn't exist, we create it.

**Command (CLI):**
```mikrotik
/interface vlan add name=vlan-35 vlan-id=35 interface=ether3
```
**Explanation of Parameters:**

| Parameter   | Description                                                    |
|-------------|----------------------------------------------------------------|
| `name`      | The name we will give to the interface (e.g., `vlan-35`).    |
| `vlan-id`   | The VLAN ID (e.g., `35` in this case).                        |
| `interface` | The parent ethernet interface (e.g., `ether3`). |

**Winbox GUI:**

1. Go to *Interfaces* menu
2. Click on the "+" button and then select VLAN.
3. Enter the name as "vlan-35", VLAN ID as "35", and select the parent interface as "ether3" (or whatever the correct parent is).
4. Click *Apply* and *OK*.

**After:** The `vlan-35` interface is created and should be shown in the interfaces list.

**Command (CLI) to Verify:**
```mikrotik
/interface vlan print
```

**Expected Output (Example):**
```
Flags: X - disabled, D - dynamic, R - running, S - slave
 #    NAME                                MTU   MAC-ADDRESS       VLAN-ID INTERFACE
 0  R  vlan-10                            1500  XX:XX:XX:XX:XX:XX 10      ether1
 1  R  vlan-20                            1500  XX:XX:XX:XX:XX:XX 20      ether2
 2  R  vlan-35                            1500  XX:XX:XX:XX:XX:XX 35      ether3
```
**Why this step:** This creates the logical interface representing the VLAN, ensuring that all traffic on VLAN 35 will pass over this interface.

### Step 3: Assign an IP Address to the VLAN Interface

**Before:** The `vlan-35` interface exists, but does not have an IP address assigned to it.

**Command (CLI):**
```mikrotik
/ip address add address=87.11.67.1/24 interface=vlan-35
```

**Explanation of Parameters:**

| Parameter   | Description                                                    |
|-------------|----------------------------------------------------------------|
| `address`   | The IP address and subnet mask (e.g., `87.11.67.1/24`).      |
| `interface` | The interface to which the IP will be assigned (e.g., `vlan-35`). |

**Winbox GUI:**

1. Navigate to *IP* -> *Addresses*.
2. Click the "+" button.
3. Enter the address as `87.11.67.1/24`.
4. Select the `vlan-35` interface from the dropdown.
5. Click *Apply* and *OK*.

**After:** The `vlan-35` interface has an IP address configured on the network `87.11.67.0/24`.

**Command (CLI) to Verify:**
```mikrotik
/ip address print
```

**Expected Output (Example):**
```
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24    192.168.88.0    ether1
 1   87.11.67.1/24      87.11.67.0      vlan-35
```

**Why this step:** This assigns an IP address to the VLAN interface, allowing the router to communicate on the `87.11.67.0/24` subnet and acts as the gateway for this subnet.

### Step 4: (Optional, but Recommended) Configure a DNS Server for this Subnet

This is optional, but highly recommended. If you are going to configure a DHCP server, it is best practice to also configure a DNS server, so devices on this subnet know where to go to resolve names.

**Before:** There may or may not be any DNS server configuration.

**Command (CLI):**
```mikrotik
/ip dns set servers=8.8.8.8,1.1.1.1 allow-remote-requests=yes
```

**Explanation of Parameters:**

| Parameter             | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `servers`             | A comma-separated list of DNS servers (e.g., `8.8.8.8,1.1.1.1`).|
| `allow-remote-requests`| Enable remote DNS requests so devices behind the router can resolve DNS names. |

**Winbox GUI:**

1.  Go to *IP* -> *DNS*.
2.  Enter the DNS server addresses in the *Servers* field (e.g., `8.8.8.8,1.1.1.1`).
3.  Check the `Allow Remote Requests` box.
4.  Click *Apply* and *OK*.

**After:** DNS Server settings are configured.

**Command (CLI) to Verify:**
```mikrotik
/ip dns print
```

**Expected Output (Example):**
```
          servers: 8.8.8.8,1.1.1.1
   dynamic-servers:
allow-remote-requests: yes
      max-udp-packet: 4096
            query-server-timeout: 2s
           query-total-timeout: 10s
           cache-max-age: 1d
       cache-size: 2048KiB
```

**Why this step:**  This ensures devices on the subnet have the DNS service needed to find resources on the internet.

### Step 5 (Optional, but Recommended): Configure a DHCP Server for the VLAN

This configuration step configures a DHCP server for the subnet.

**Before:** There may or may not be any DHCP server configuration.

**Command (CLI):**
```mikrotik
/ip dhcp-server add address-pool=dhcp_pool_vlan_35 disabled=no interface=vlan-35 name=dhcp-vlan-35
/ip dhcp-server network add address=87.11.67.0/24 dns-server=8.8.8.8,1.1.1.1 gateway=87.11.67.1
/ip pool add name=dhcp_pool_vlan_35 ranges=87.11.67.100-87.11.67.200
```

**Explanation of Parameters:**

*   `/ip dhcp-server add`:
    *   `address-pool`: The name of the IP pool to use for lease assignments.
    *   `disabled`: Whether the DHCP server is disabled or not.
    *   `interface`: The interface the DHCP server will operate on.
    *   `name`: The name you are assigning to this DHCP server.
*   `/ip dhcp-server network add`:
    *   `address`: The network address this DHCP service serves.
    *   `dns-server`: The dns server to tell clients to use (set to Google public and Cloudflare's dns)
    *   `gateway`: The gateway address for the clients.
*   `/ip pool add`:
    *   `name`: The name of the IP address pool.
    *   `ranges`: The IP range that will be leased to clients.

**Winbox GUI:**

1.  Go to *IP* -> *Pool*.
2.  Click the "+" button, and add a pool with Name: dhcp_pool_vlan_35, Ranges: `87.11.67.100-87.11.67.200`
3.  Go to *IP* -> *DHCP Server*
4.  Click the "+" button, select Interface `vlan-35`, name `dhcp-vlan-35` and select `dhcp_pool_vlan_35` for the address-pool.
5. Go to *IP* -> *DHCP Server* -> *Networks* tab.
6. Click the "+" button, add `87.11.67.0/24` to the *Address* field, add `8.8.8.8,1.1.1.1` to *DNS Servers* field, and add `87.11.67.1` to *Gateway* field.

**After:** The DHCP Server is ready and will now give out IPs on this subnet for clients.

**Command (CLI) to Verify:**
```mikrotik
/ip dhcp-server print
/ip dhcp-server network print
/ip pool print
```

**Expected Output (Example):**
```
Flags: X - disabled, I - invalid
 #   NAME         INTERFACE    LEASE-TIME ADDRESS-POOL    DISABLED
 0   dhcp-vlan-35 vlan-35      10m        dhcp_pool_vlan_35 no
```
```
Flags: X - disabled
 #   ADDRESS         GATEWAY       DNS-SERVER
 0   87.11.67.0/24   87.11.67.1   8.8.8.8,1.1.1.1
```
```
Flags: X - disabled, I - invalid, D - dynamic
 #   NAME              RANGES
 0   dhcp_pool_vlan_35 87.11.67.100-87.11.67.200
```

**Why this step:** This ensures devices on the subnet automatically receive an IP address and other networking settings, making network administration easier.

## Complete Configuration Commands:

Here are all the CLI commands compiled to create the described setup.
```mikrotik
/interface vlan
add name=vlan-35 vlan-id=35 interface=ether3
/ip address
add address=87.11.67.1/24 interface=vlan-35
/ip dns
set servers=8.8.8.8,1.1.1.1 allow-remote-requests=yes
/ip dhcp-server
add address-pool=dhcp_pool_vlan_35 disabled=no interface=vlan-35 name=dhcp-vlan-35
/ip dhcp-server network
add address=87.11.67.0/24 dns-server=8.8.8.8,1.1.1.1 gateway=87.11.67.1
/ip pool
add name=dhcp_pool_vlan_35 ranges=87.11.67.100-87.11.67.200
```

## Common Pitfalls and Solutions:

*   **VLAN Tagging Issues:**  If devices on the VLAN cannot communicate, double-check that the switch port connected to the MikroTik is correctly configured for VLAN tagging (`Trunk`). Make sure the VLAN ID is correct, and the parent ethernet port exists.
*   **Incorrect IP Configuration:** Mismatched subnets or incorrect IP assignments can cause routing issues. Verify subnet masks and IP addresses. Use `/ip address print` to verify the address configuration.
*   **Firewall Rules:** Default MikroTik firewall rules can sometimes block traffic. Ensure necessary forward rules are in place, specifically if forwarding to other subnets is required. Review `/ip firewall filter print`.
*  **DNS Server Settings:** If DNS is configured incorrectly, devices will have issues resolving names. Verify DNS server settings are correct. use `/ip dns print`.
*   **DHCP Server Issues:** Check if there are conflicts in address pools or if the server is disabled. Check the configuration using `/ip dhcp-server print`, `/ip dhcp-server network print`, and `/ip pool print`.
*   **Resource Issues:** If the router is experiencing high CPU or memory usage, this configuration might not be the cause. But it is best practice to be mindful of resource usage. Tools like `/tool profile` and `/system resource monitor` can provide insights.

## Verification and Testing Steps:

1.  **Ping Test:**  From a device on the `87.11.67.0/24` network, ping the VLAN interface IP (`87.11.67.1`). If this fails, there's likely an issue with the local IP configuration or the vlan. Use the command line `/ping 87.11.67.1`.
2.  **Ping Outside IP:** From a device on the `87.11.67.0/24` network, ping an external IP address like `8.8.8.8`. If this fails, then check the gateway and the connection to the internet (if applicable). Use the command line `/ping 8.8.8.8`.
3.  **Traceroute:** Use traceroute to examine the path to an external IP. This can help identify routing loops or intermediate network issues. use the command line `/tool traceroute 8.8.8.8`.
4.  **DHCP lease check:** Verify that DHCP leases are issued on the `vlan-35` network. Use the command line `/ip dhcp-server lease print`.
5.  **MikroTik Torch:** Use torch to monitor packets on the `vlan-35` interface during testing to analyze traffic flow. Use `/tool torch interface=vlan-35`.

## Related Features and Considerations:

*   **Advanced Routing Protocols:** For more complex setups (e.g., larger networks with redundant links), consider using dynamic routing protocols like OSPF or BGP.
*   **Firewall Rules:** Be sure to implement firewall rules to filter the traffic as required. This includes setting default rules, forward rules, and connection tracking.
*   **QoS (Quality of Service):** Implement QoS if bandwidth is constrained. This will allow prioritization of traffic.

## MikroTik REST API Examples (if applicable):
**Note**: RouterOS API access must be configured.
For basic API configuration access, you need to install the *api* package if not installed by default.

### Get Interface list
API Endpoint: `https://<router-ip>/rest/interface/vlan`
Method: `GET`
Request Body: none
Example `curl` Command:
```bash
curl -k -u <user>:<password> https://<router-ip>/rest/interface/vlan
```
Expected Response (JSON):
```json
[
    {
        "name": "vlan-10",
        "vlan-id": "10",
        "interface": "ether1",
         "mtu": "1500",
         "mac-address": "XX:XX:XX:XX:XX:XX",
        ".id": "*0"
    },
    {
        "name": "vlan-20",
        "vlan-id": "20",
        "interface": "ether2",
         "mtu": "1500",
         "mac-address": "XX:XX:XX:XX:XX:XX",
        ".id": "*1"
    }
]
```

### Add a VLAN Interface
API Endpoint: `https://<router-ip>/rest/interface/vlan`
Method: `POST`
Request Body (JSON):
```json
{
    "name": "vlan-35",
    "vlan-id": "35",
    "interface": "ether3"
}
```
Example `curl` Command:
```bash
curl -k -u <user>:<password> -H "Content-Type: application/json" -X POST -d '{"name": "vlan-35", "vlan-id": "35", "interface": "ether3"}' https://<router-ip>/rest/interface/vlan
```
Expected Response (JSON):
```json
{ ".id":"*2" }
```
### Add an IP address
API Endpoint: `https://<router-ip>/rest/ip/address`
Method: `POST`
Request Body (JSON):
```json
{
    "address":"87.11.67.1/24",
    "interface":"vlan-35"
}
```
Example `curl` Command:
```bash
curl -k -u <user>:<password> -H "Content-Type: application/json" -X POST -d '{"address":"87.11.67.1/24", "interface":"vlan-35"}' https://<router-ip>/rest/ip/address
```
Expected Response (JSON):
```json
{ ".id":"*2" }
```
### Update the DNS server configuration
API Endpoint: `https://<router-ip>/rest/ip/dns`
Method: `PATCH`
Request Body (JSON):
```json
{
  "servers":"8.8.8.8,1.1.1.1",
  "allow-remote-requests":"yes"
}
```
Example `curl` Command:
```bash
curl -k -u <user>:<password> -H "Content-Type: application/json" -X PATCH -d '{"servers":"8.8.8.8,1.1.1.1","allow-remote-requests":"yes"}' https://<router-ip>/rest/ip/dns
```
Expected Response (JSON):
```json
{ ".id":"*0" }
```
**Note**:
Error handling should be implemented in a production environment. The API returns errors in JSON format. For example a malformed JSON input would yield: `{"message":"Expected value: object, found: string","type":"invalid-value","param":null,"code":17}`.

## Security Best Practices:

*   **API Security:**  Enable API over HTTPS and use strong passwords or API tokens. Restrict API access to trusted networks.
*   **Firewall:** Limit access to the router itself via a strong firewall. Disable unused services on the router that expose it to attacks.
*   **RouterOS Updates:** Keep the RouterOS firmware updated. Enable auto-updates or manually update when recommended by MikroTik.
*   **VLAN Security:** If you are creating multiple VLANs, ensure proper firewall rules between the VLANs to protect the different networks.
*   **DHCP Security:** Ensure that the DHCP server is only on the interfaces that it should be serving addresses on. Limit leases as needed. Use static leases for devices that should have static IP addresses.
*   **DNS Security:** Ensure that the only DNS server allowed is ones that you can trust.

## Self Critique and Improvements

This configuration provides basic IP routing but could be enhanced.

*   **Routing Protocols:** For complex network topologies, implementing OSPF or BGP would improve routing efficiency.
*   **NAT and Firewall:**  This configuration does not provide NAT for the `87.11.67.0/24` subnet. This would be essential for internet access.
*   **Security Policies**: Advanced firewall rules could be added to limit traffic, like blocking specific protocols or ports to specific networks.
*   **Monitoring:** Additional monitoring is needed to alert when this service is not working correctly. This includes logging important events, and monitoring resource usage.

## Detailed Explanation of Topic

**IP Routing:** The fundamental concept of IP routing is to determine the best path for network traffic to travel from a source to a destination. When a device sends a packet, a router must decide which interface to forward it to based on its destination IP address. In MikroTik, this is done using routing tables. Each entry in the table consists of a network prefix (IP address and subnet mask), a gateway (next-hop address) and an interface (where to send the packets). The router compares the destination IP of the packet with each entry in the table. If there is a match, the router sends the packet to the defined gateway using the interface associated with that route.

When we configure `87.11.67.1/24` on the vlan-35 interface, we are informing the router that, for all traffic destined to the network `87.11.67.0/24`, that the `vlan-35` interface should be used, and anything on that network can be reached directly, since it is a directly attached network. If there are no other routes that contain the destination IP address, this will be the route that will be used for all traffic destined for this subnet.

## Detailed Explanation of Trade-offs

When it comes to IP routing, there are many choices to be made, for example:

*   **Static vs Dynamic Routing:**
    *   **Static Routing:** Simpler to configure, ideal for smaller networks where routes rarely change. But it is not scalable and doesn't recover from route failures automatically.
    *   **Dynamic Routing (e.g., OSPF, BGP):** Automatically adjusts routes based on network changes. Ideal for larger, more complex networks. Requires more configuration, and can be more difficult to troubleshoot, but scales much more effectively.
*   **Directly Connected Subnet:** Adding a subnet and directly attaching it to an interface will always take precedence over all other routes, unless an exact match to a subnet that is not directly connected exists.

## Configuration for Specific RouterOS Versions:

The commands in this document are compatible with RouterOS v6.48 and RouterOS v7.x. All the commands that are used have remained relatively consistent, and the general principle is still the same. However, some of the underlying implementation may be different in newer versions. When it comes to API, if you have a modern version, the newer api format is recommended.

This documentation provides a solid starting point for implementing IP routing on MikroTik. Please ensure you understand the full impact of each command before implementing it on a live system. Always test changes in a lab environment first.
