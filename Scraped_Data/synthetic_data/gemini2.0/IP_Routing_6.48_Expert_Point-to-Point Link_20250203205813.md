Okay, let's dive into creating a comprehensive documentation for IP routing on MikroTik RouterOS, specifically targeting version 6.48 (with some considerations for 7.x) in a point-to-point link scenario using a /24 subnet, and focusing on the "wlan-50" interface.

## Scenario Description:

We're establishing a simple point-to-point link between two MikroTik routers using wireless. The "wlan-50" interface on our primary router will be part of the 90.130.136.0/24 network. We need to configure IP addressing and routing to allow communication within this subnet and, potentially, to other networks beyond this point-to-point link.  This configuration is targeted at an Expert level user, assuming familiarity with MikroTik basics.

## Implementation Steps:

### Step 1: Initial Interface and Address Check

**Purpose:** Before making changes, verify the current interface status and IP addressing. This baseline will allow us to confirm the changes in subsequent steps.

**Before Configuration:**
   - Connect to your MikroTik router via Winbox or SSH.
   - Check the current interface status.

**CLI Command:**

```mikrotik
/interface print
/ip address print
```

**Expected Output (Example):**

```
# /interface print
Flags: X - disabled, D - dynamic, R - running, S - slave
 #    NAME                                TYPE        MTU L2MTU MAX-L2MTU
 0  R  ether1                              ether       1500  1598     1598
 1    wlan1                               wlan        1500  1598     1598
 2    wlan-50                             wlan        1500  1598     1598

# /ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24    192.168.88.0   ether1
```

**Explanation:**
The output shows a list of interfaces and their current status, followed by configured IP addresses. Here we see our “wlan-50” interface present, and an example IPv4 address assigned to ether1. This is the current state we're starting from. We can assume that the wlan-50 interface is configured with security, connected to another device etc.

**Winbox GUI:**
*   Go to *Interfaces* and see if `wlan-50` exists in the interface list.
*   Go to *IP > Addresses* to see configured IP addresses.

**Effect of Step 1:**  None, just displaying the existing setup.

### Step 2:  Assign IP Address to wlan-50 Interface

**Purpose:** Assign an IP address within the 90.130.136.0/24 subnet to the "wlan-50" interface. We will use 90.130.136.1/24 for this example.

**CLI Command:**

```mikrotik
/ip address add address=90.130.136.1/24 interface=wlan-50
```
**Explanation:**
`address=90.130.136.1/24`: Specifies the IP address and subnet mask to be assigned.
`interface=wlan-50`:  Indicates the interface to which this IP address is assigned.

**Winbox GUI:**
*   Go to *IP > Addresses*.
*   Click the "+" button.
*   Enter `Address`: `90.130.136.1/24`
*   Select `Interface`: `wlan-50`
*   Click "Apply" and then "OK".

**After Configuration:**
Re-run ` /ip address print`.

**Expected Output:**
```
# /ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE
 0   192.168.88.1/24    192.168.88.0   ether1
 1   90.130.136.1/24  90.130.136.0   wlan-50
```
**Effect of Step 2:** The wlan-50 interface is now configured with an IP address.

### Step 3: Verify Local Connectivity

**Purpose:** Use the `ping` tool to confirm if the router can reach its own IP address on the wlan-50 interface. Also verify connectivity to the peer device on the other end of the wireless link.
We will assume that the peer on the other end of the link has the address 90.130.136.2.

**CLI Command:**

```mikrotik
/ping 90.130.136.1
/ping 90.130.136.2
```

**Expected Output (if successful):**
```
  SEQ HOST                                     SIZE TTL TIME  STATUS
    0 90.130.136.1                                 56  64  1ms
    1 90.130.136.1                                 56  64  <1ms
    2 90.130.136.1                                 56  64  <1ms
  sent=3 received=3 packet-loss=0% min-rtt=<1ms avg-rtt=<1ms max-rtt=1ms

 SEQ HOST                                     SIZE TTL TIME  STATUS
    0 90.130.136.2                                 56  64  1ms
    1 90.130.136.2                                 56  64  1ms
    2 90.130.136.2                                 56  64  1ms
  sent=3 received=3 packet-loss=0% min-rtt=1ms avg-rtt=1ms max-rtt=1ms
```
**Explanation:**
The `ping` command sends ICMP echo requests to the specified IP addresses. This confirms basic network connectivity.  If all pings fail, double check the interface settings and cabling, or check that the peer device is working correctly and connected.

**Winbox GUI:**
*   Open a new terminal window.
*   Type `/ping 90.130.136.1` or `/ping 90.130.136.2` and press Enter.

**Effect of Step 3:** Basic connectivity has been verified.

### Step 4:  IP Routing (If Necessary)

**Purpose:** In a simple point-to-point configuration where both endpoints are on the same subnet, there is normally no need to add any additional routes. If the router will handle other subnets, or provide a path to other networks, routing may need to be configured. If your router had other interfaces connected to different networks, a static route to 90.130.136.0/24 *could* be defined, but in most cases, this is not required.
For illustrative purposes, let's imagine that there's a secondary router on 192.168.10.0/24 that can be reached via 90.130.136.2. Then the following command *would* be required.

**CLI Command:**
```mikrotik
 /ip route add dst-address=192.168.10.0/24 gateway=90.130.136.2
```

**Explanation:**
`dst-address=192.168.10.0/24` : The destination network or host address.
`gateway=90.130.136.2`: The IP address of the next hop router that can reach the destination.

**Winbox GUI:**
*   Go to *IP > Routes*.
*   Click the "+" button.
*   Enter `Dst. Address`: `192.168.10.0/24`.
*   Enter `Gateway`: `90.130.136.2`.
*   Click "Apply" and then "OK".

**After Configuration:**
Run `/ip route print`

**Expected Output (Example):**

```
# /ip route print
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, P - prohibit
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0  AC  0.0.0.0/0                      192.168.88.1       1
 1  DC  192.168.88.0/24          192.168.88.1   ether1          0
 2  DC  90.130.136.0/24           90.130.136.1   wlan-50     0
 3  AS 192.168.10.0/24       90.130.136.2    1

```
**Effect of Step 4:** Routes to the 90.130.136.0/24 and 192.168.10.0/24 networks have been configured.

## Complete Configuration Commands:

```mikrotik
/interface print
/ip address print
/ip address add address=90.130.136.1/24 interface=wlan-50
/ping 90.130.136.1
/ping 90.130.136.2
/ip route print
/ip route add dst-address=192.168.10.0/24 gateway=90.130.136.2
/ip route print
```

## Common Pitfalls and Solutions:

*   **Incorrect IP address or subnet mask:** Verify the IP address and subnet mask are correct using `/ip address print`. If the IP address or subnet mask is incorrect, remove the IP address entry with `/ip address remove <number>`, and add the new one.
*   **Firewall blocking ICMP:** Ensure that firewall rules aren't blocking ping requests using `/ip firewall filter print`. If so add an allow rule with: `/ip firewall filter add chain=input protocol=icmp action=accept`.
*   **Wireless link issues:** If pings are failing, check the wireless interface configuration, signal strength, and authentication settings. Using the `/interface wireless registration-table print` will allow you to see connected clients.
*   **Routing loops:** If you create complex routing setups, always verify routes, or use a dynamic routing protocol. Check routes with `/ip route print`. Avoid recursive routes (where the next hop is within the destination network).
*   **MTU Issues:** Mismatched MTU settings on the interfaces, especially when using VPNs can cause connection issues. Check interface MTU and try to match MTUs in the path.  Use the `/interface print` command to see the current MTU settings.
*   **High CPU/Memory:** Complex firewall rules, routing protocols, and numerous connections can cause high resource usage. Monitor using `/system resource print`. Consider using hardware acceleration or simplifying the configuration to resolve the issue.

## Verification and Testing Steps:

1.  **Ping the interface IP:**  Use `/ping 90.130.136.1` to confirm the router can reach its IP on `wlan-50`.
2.  **Ping the peer device:** Use `/ping 90.130.136.2` to confirm connectivity to the far end.
3.  **Traceroute:** Use `/tool traceroute 90.130.136.2` to view the path the packets are taking to reach their destination and if there are any hops in between (for troubleshooting).
4.  **Check the routing table:** Verify that the routing table shows the correct routes with `/ip route print`.
5.  **Test application connectivity:** If a specific application is failing, test communication at the application level to ensure it can reach the other end.

## Related Features and Considerations:

*   **OSPF/BGP:** If more complex networks are present beyond the point-to-point link, explore dynamic routing protocols like OSPF or BGP.
*   **VLANs:** If the wlan-50 interface must be partitioned into multiple networks, explore VLAN tagging and configuration.
*   **VPNs:** If the wireless link is not secure, you should explore using a VPN over this link.
*   **Firewall:** Ensure that proper firewall rules are configured to protect against malicious traffic.
*   **QoS (Quality of Service):** If latency or bandwidth issues are present, QoS rules can be added to improve performance of the link.
*   **DHCP Server/Client:** If you need dynamic addressing, consider a DHCP server on this link, or a DHCP client if there is one provided by the peer.
*   **Bridge Mode:** If transparent bridging is required, this configuration must be changed from routing to bridging.

## MikroTik REST API Examples (if applicable):

This scenario is not complex enough to require extensive use of the REST API. The most relevant examples are for creating an IP address and route, and these can be accessed via the `/ip/address` and `/ip/route` endpoints. The `/interface/wireless` endpoint can be used to further configure the wlan-50 interface, as well.

Example to add an IP address:

```
API Endpoint: /ip/address
Method: POST
JSON Payload:
{
   "address":"90.130.136.1/24",
   "interface":"wlan-50"
}
Expected Response (Success):
{
    ".id": "*1",
    "address": "90.130.136.1/24",
    "interface": "wlan-50",
    "dynamic": false,
    "disabled": false,
    "invalid": false
}
```

Example to add a static route:
```
API Endpoint: /ip/route
Method: POST
JSON Payload:
{
 "dst-address": "192.168.10.0/24",
  "gateway": "90.130.136.2"
}

Expected Response (Success):
{
    ".id": "*1",
     "dst-address": "192.168.10.0/24",
    "gateway": "90.130.136.2",
    "distance": 1,
    "disabled": false,
    "type":"unicast",
    "routing-mark":"",
    "pref-src":"",
    "check-gateway":"no"
}
```

**Error Handling:**
* If there is an error adding an IP address (such as trying to add a duplicate), then the response will return an error, and include an error message describing the issue.  For example, trying to add a duplicate will return a `status=error` and include the message "already have such address on interface".
* Error codes vary based on the type of error and API endpoint. Error handling logic in your client application should inspect these fields.
* A good approach is to always first call `/ip/address` using the GET method, then check if an IP address exists before calling POST.

## Security Best Practices

*   **Secure the wireless interface:** Use strong encryption (WPA2 or WPA3) and a complex passphrase for the wireless interface. Restrict access via mac addresses using the `access-list` or `connect-list` in the wireless security settings.
*   **Firewall Rules:** Only allow necessary incoming traffic to the router. Deny any connections which you do not require.
*   **RouterOS Version:** Keep RouterOS updated to the latest stable version to avoid potential security vulnerabilities.
*   **Strong Passwords:** Use strong passwords for admin and other router users. Change the default username and password.
*   **Disable unused services:** Disable any unused services (e.g., unused API interfaces).
*   **SSH Access:** If SSH access is not required then disable the service, or restrict access using firewall rules. Consider using a non-standard port for SSH.
*  **API Access:** If the API is not required, ensure that the service is disabled using `/ip service disable api`. Ensure only trusted networks/hosts are permitted access to the API interface by configuring `allowed-from` settings.

## Self Critique and Improvements

This configuration is a straightforward, but comprehensive starting point for a point-to-point IP routing scenario on MikroTik.
Here are some areas for potential improvements:
*   **Dynamic Routing:** If more than two routers are in the network, using OSPF is preferable to static routes.
*   **VPN:** If security is a concern, implement a VPN tunnel to encrypt the traffic sent between the two routers.
*   **Monitoring:** Add monitoring tools like the `torch` tool, or other monitoring software to the routers to monitor resource usage and the state of the wireless links.
*   **Scripts:** Automate configuration with scripts if needed to deploy the configurations. This is especially useful when rolling out changes to several devices at once.
*   **Netwatch/SNMP:** Add active monitoring to ensure the connection status of the point-to-point link using `/tool netwatch`, and integrate SNMP logging for larger networks.

## Detailed Explanations of Topic

**IP Routing** is the fundamental process that allows data to travel between networks. In a simple point-to-point network, such as our case, the routing is mostly implicit. When an IP address is assigned to the `wlan-50` interface, a *connected route* is automatically created in the routing table. The router knows that the IP addresses of the 90.130.136.0/24 subnet are on the `wlan-50` interface. When a device on the other end of the wireless link sends a packet to the router, it is addressed to the router’s IP address or a device within the 90.130.136.0/24 network, the router inspects the destination address and forwards it according to its routing table. In the described configuration we have a connected route for the wlan-50 interface, and a static route for 192.168.10.0/24 via 90.130.136.2. When multiple routes are available the router will choose the route with the lowest distance, or the best route, depending on the type of routing protocol in use. The default distance for connected routes is 0. The router maintains a routing table which is a list of networks and their next hops.

## Detailed Explanation of Trade-offs

*   **Static Routing vs. Dynamic Routing:** Static routing (like the 192.168.10.0/24 route) is simple to implement, but it requires manual configuration. This is fine in simple, static setups. However, if the network is more dynamic, or has more than two routers, static routing becomes cumbersome and error-prone. Dynamic routing protocols like OSPF or BGP automatically adapt to network changes (e.g., a link going down). OSPF is usually used in intra-domain routing, while BGP is often used for inter-domain routing. If you only need basic connectivity with a single peer, static routing can be suitable, if the requirements grow then you should switch to a dynamic routing protocol. If you do use a dynamic routing protocol you must ensure that the router resources are sufficient to handle the load required for the routing protocol.

*   **Manual IP Addressing vs DHCP:** Manually assigning IP addresses can be okay in small networks where the number of devices are small and static. For larger networks, DHCP allows dynamic IP address assignments which reduces the work for administrators. For simple point-to-point links, it is often the case that only two IP addresses are required, and they can be assigned statically. When DHCP is required it is important to ensure the DHCP server is correctly configured, and that the DHCP client is configured to use the DHCP provided address.

## Configuration for Specific RouterOS Versions:

This documentation is targeting RouterOS 6.48 and is also applicable to version 7.x, but the `ipv6` commands and more advanced `route filter` features which can exist in RouterOS 7.x have not been included. While many commands are similar in 6.x and 7.x, always check the MikroTik documentation for differences and syntax changes for complex configurations.

This has been a comprehensive breakdown of setting up IP routing on a MikroTik router for a point-to-point link using the specified parameters. It includes detailed steps, troubleshooting guidance, security considerations, and alternative setups. Please verify that your RouterOS version is at least 6.48 before using the provided commands.
