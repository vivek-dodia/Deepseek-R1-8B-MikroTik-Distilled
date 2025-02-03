Okay, let's dive into a comprehensive documentation for IP Routing within a MikroTik RouterOS environment, specifically targeting version 6.48 (but also applicable to v7.x), for a SOHO network using the subnet 39.214.3.0/24 on the interface named "bridge-13". This is an advanced configuration suitable for those comfortable with RouterOS CLI and concepts.

## Scenario Description:

This configuration focuses on ensuring that the MikroTik router correctly handles routing for a local subnet (39.214.3.0/24) connected to it via a bridge interface named "bridge-13". We'll be setting up the IP address on the bridge and configuring static routing. While the example here involves a single subnet and basic routing, this setup is foundational for more complex networking scenarios. The configuration described below assumes the default MikroTik configuration, i.e no other addresses, bridges, or routes are configured.

## Implementation Steps:

### Step 1: Creating a Bridge Interface and Setting an IP Address

**Before Configuration:** The router likely has a default configuration with some interfaces configured. For the sake of this example, we will assume only a default configuration.

**Action:**

* Create a new bridge interface named `bridge-13`.
* Assign the IP address `39.214.3.1/24` to the bridge interface. We will use the '.1' address for the router to avoid any host address overlap on the local network.

**CLI Command:**

```mikrotik
/interface bridge
add name=bridge-13
/ip address
add address=39.214.3.1/24 interface=bridge-13
```

**Explanation:**

*   `/interface bridge add name=bridge-13`: This command creates a new bridge interface named "bridge-13". A bridge allows multiple Ethernet interfaces to act as a single LAN segment.
*   `/ip address add address=39.214.3.1/24 interface=bridge-13`: This command assigns the IP address `39.214.3.1/24` to the newly created bridge interface "bridge-13". This is the router's IP address on this subnet.

**Winbox GUI:**
1.  Navigate to *Bridge* in the main menu.
2.  Click on the "+" button to add a new bridge and enter "bridge-13" as the name.
3. Navigate to *IP* and then *Addresses* in the main menu.
4. Click on the "+" button to add a new IP address and enter "39.214.3.1/24", and select "bridge-13" as the interface.

**After Configuration:** The router will now have a bridge interface named `bridge-13` with the IP address `39.214.3.1/24` assigned to it. You can verify this using the `/interface print` and `/ip address print` commands in the CLI, or in Winbox in the corresponding sections.

**Effect:** Devices connected to the physical ports that are members of the bridge `bridge-13` will be in the 39.214.3.0/24 network. The MikroTik will be able to send and receive IP packets on that network.

### Step 2: Adding Physical Interfaces to the Bridge

**Before Configuration:** The `bridge-13` interface exists but has no physical ports associated with it. This means the router currently is not connected to any physical network on the bridge.

**Action:**
* Add physical Ethernet interfaces to the `bridge-13` interface. In this example, we will use `ether2` and `ether3`, but you may need to use different ones based on your setup. You can add as many ports as you need on the same bridge.

**CLI Command:**

```mikrotik
/interface bridge port
add bridge=bridge-13 interface=ether2
add bridge=bridge-13 interface=ether3
```

**Explanation:**

*   `/interface bridge port add bridge=bridge-13 interface=ether2`: This command adds the physical Ethernet interface "ether2" to the "bridge-13". Any device plugged into ether2 will be on the 39.214.3.0/24 network.
*   `/interface bridge port add bridge=bridge-13 interface=ether3`: This command adds the physical Ethernet interface "ether3" to the "bridge-13" network.

**Winbox GUI:**
1. Navigate to *Bridge* and then *Ports* in the main menu.
2. Click on the "+" button to add a new port and select the interface (e.g. "ether2") and the bridge interface `bridge-13`.
3.  Repeat step 2 for `ether3`.

**After Configuration:** The bridge `bridge-13` will now have physical ports that can connect to the local network. Devices connected to `ether2` or `ether3` can communicate with the router and each other (once their addresses are correctly configured).

**Effect:** Devices connected to interfaces `ether2` and `ether3` will now be part of the local network. The MikroTik will bridge these physical ports, so the two ports will act as if connected to a common switch.

### Step 3: Verifying Connectivity

**Before Configuration:** The bridge and its addresses are setup but connectivity is untested.

**Action:**
* Verify connectivity by pinging the router from a computer on the same local network, and the other way around.

**CLI Command (from a computer on the 39.214.3.0/24 network):**

```shell
ping 39.214.3.1
```

**CLI Command (from the Router):**

```mikrotik
/ping 39.214.3.X
```

(Replace 'X' with the IP address of a device connected to the bridge).

**Explanation:**
*   `ping 39.214.3.1`: This command sends ICMP echo request packets to the router's IP address on the subnet. If successful, you will see reply packets.
*   `/ping 39.214.3.X`: This will ping the IP address on the local network (where X is a device's address).

**After Configuration:** Successful pings from devices on the `39.214.3.0/24` subnet will confirm basic connectivity within the local network and with the router.

**Effect:** If connectivity is verified, you know the bridge and addressing is working as expected.

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to achieve the setup:

```mikrotik
/interface bridge
add name=bridge-13
/ip address
add address=39.214.3.1/24 interface=bridge-13
/interface bridge port
add bridge=bridge-13 interface=ether2
add bridge=bridge-13 interface=ether3
```

**Parameter Explanations:**

| Command | Parameter        | Description                                                  |
| :------ | :--------------- | :----------------------------------------------------------- |
| `/interface bridge add`    | `name`             | The name of the bridge interface (e.g., `bridge-13`).   |
| `/ip address add`     | `address`      | The IP address and subnet mask in CIDR notation (e.g., `39.214.3.1/24`). |
|       | `interface`      | The interface to apply this IP address to (e.g., `bridge-13`). |
| `/interface bridge port add` | `bridge` | The bridge to add this port to.  |
|       | `interface`      | The physical interface to add to the bridge. |

## Common Pitfalls and Solutions:

1.  **Incorrect Subnet Mask:**
    *   **Problem:** Incorrect subnet mask (e.g., using `/16` instead of `/24`) can cause devices to not be able to communicate with the router and each other.
    *   **Solution:** Double-check the subnet mask and ensure it matches the intended network design. In this case, it should be `/24`. Check using `/ip address print`.
2.  **Interface Not Added to Bridge:**
    *   **Problem:** Forgetting to add physical interfaces to the bridge means that even though the IP address is set up on the bridge, physical ports are not associated, so devices can't communicate.
    *   **Solution:** Use `/interface bridge port print` to verify that your physical interfaces have been correctly added to the bridge.
3. **Firewall Issues:**
   * **Problem:** Default firewalls or misconfigured rules can block communication on the network.
    *   **Solution:** Ensure the MikroTik firewall is configured to allow traffic between devices on this network if firewalls are enabled.
4.  **Duplicate IP Addresses:**
    *   **Problem:** If another device has the same IP address as the router, conflicts will occur.
    *   **Solution:** Ensure the assigned router IP is unique and not used by any other device on the subnet.
5.  **Wrong Physical Port:**
   * **Problem:** Accidentally plugging devices into other, unconnected, ports.
   * **Solution:** Ensure all required devices are plugged into the ports that are members of the bridge (check using `/interface bridge port print`).
6.  **High CPU Usage:**
    *   **Problem:** Basic routing and bridging will not usually use too much CPU, but if many interfaces or packets are used, the router CPU could increase its usage.
    *   **Solution:** Check the CPU using `/system resource print`. Reduce the number of concurrent connections, or upgrade the router if hardware is not enough to handle the load.

## Verification and Testing Steps:

1.  **Ping from a connected device to router:** Use the command `ping 39.214.3.1` on a device connected to ether2 or ether3. You should receive replies from the router.
2.  **Ping from router to a connected device:** Use the command `/ping 39.214.3.X` (where X is the IP of a connected device). You should receive replies.
3.  **Traceroute:** If possible, perform a traceroute from a connected device to another device on the network or to an external address. The route should show that packets are being forwarded via the router.
4.  **Torch:** Use MikroTik's `/tool torch` to monitor live traffic on the `bridge-13` interface to check if packets are being sent and received. The packets should belong to the expected network, with a correct source and destination IP addresses.
5.  **Interface Status:** Check interface status using `/interface print` to ensure the bridge and interfaces are active and do not show any errors.
6.  **IP Address Print:** Check the IP address assigned to the bridge with `/ip address print`.

## Related Features and Considerations:

1.  **VLANs:** For more complex networks, you can use VLANs within the bridge to separate different logical networks.
2.  **DHCP Server:**  Setting up a DHCP server on the bridge interface will automatically assign IP addresses to devices on the subnet, removing the need for manual IP configuration on client devices.
3.  **Firewall Rules:** Implementing firewall rules is essential for securing the network. Allow traffic from specific sources and ports.
4.  **Traffic Shaping:** You can apply traffic shaping rules to manage the amount of bandwidth used by different users and services within the network. This can prevent one device from using all available bandwidth.
5.  **Bonding/Teaming:** You can add more ports on the bridge by aggregating several physical interfaces (e.g., `ether2` and `ether3` can be bonded using a bonding interface and then added to the bridge).
6.  **Routing Protocols:** In more complex networks, you might want to use routing protocols such as OSPF or BGP, which can coexist with static routing.
7.  **Static Routing:** While this example is for a local subnet, you can also use static routes to reach other networks. The route should use the router's gateway address.
8. **Monitoring:**  It's recommended to configure SNMP or other monitoring protocols to track network health, interface statistics and CPU usage.

## MikroTik REST API Examples (if applicable):

While the basic bridge and IP configuration can be done using the API, it can be cumbersome to do so because the API does not reflect changes dynamically (i.e, one command may need to be performed before another command is executed). Here are examples of how to create a new bridge, add an IP address, and add interfaces:

**Example 1: Create a New Bridge Interface**

*   **API Endpoint:** `/interface/bridge`
*   **Request Method:** POST
*   **JSON Payload:**

```json
{
  "name": "bridge-13"
}
```

*   **Expected Response (200 OK):**
    ```json
   {
      "id": "*0",
       ".id":"*0",
       "name":"bridge-13",
       "mtu":"1500",
       "actual-mtu":"1500",
        "l2mtu":"1598",
        "arp":"enabled",
        "disabled":"false",
       "running":"false"
    }
    ```
  * **Error handling:** If a bridge with the same name already exists, the API will return a `400 Bad Request` status code with error details.

**Example 2: Add an IP Address to the Bridge**

*   **API Endpoint:** `/ip/address`
*   **Request Method:** POST
*   **JSON Payload:**

```json
{
  "address": "39.214.3.1/24",
  "interface": "bridge-13"
}
```
*   **Expected Response (200 OK):**
    ```json
    {
        "id": "*1",
        ".id": "*1",
        "address": "39.214.3.1/24",
        "network": "39.214.3.0",
        "interface": "bridge-13",
        "actual-interface": "bridge-13",
        "dynamic": "false",
        "invalid": "false"
    }
    ```
  * **Error handling:** If the interface or network address is invalid, or a duplicate address exists, the API will return a `400 Bad Request` status code with error details.

**Example 3: Add Physical Ports to the Bridge**

*   **API Endpoint:** `/interface/bridge/port`
*   **Request Method:** POST
*   **JSON Payload for adding ether2 and ether3**

```json
[
  {
  "bridge": "bridge-13",
  "interface": "ether2"
  },
   {
  "bridge": "bridge-13",
  "interface": "ether3"
  }
]
```
*   **Expected Response (200 OK):**
    ```json
[
  {
    "id": "*2",
    ".id": "*2",
     "bridge": "bridge-13",
    "interface": "ether2",
    "priority": "0x80",
    "path-cost": "10",
     "external-fdb": "false",
    "horizon": "none",
    "edge": "auto",
    "auto-isolate": "no",
    "point-to-point": "no"
   },
{
    "id": "*3",
     ".id": "*3",
    "bridge": "bridge-13",
    "interface": "ether3",
    "priority": "0x80",
     "path-cost": "10",
   "external-fdb": "false",
   "horizon": "none",
    "edge": "auto",
   "auto-isolate": "no",
    "point-to-point": "no"
  }
]
    ```
  * **Error handling:** If an interface is invalid or does not exist, the API will return a `400 Bad Request` status code with error details.

**Note:** The MikroTik REST API can be used to perform almost any action you can perform with the CLI or Winbox. However, careful planning and sequencing of API calls is essential for proper operation.

## Security Best Practices

1.  **Disable Unused Services:**  Disable any unused services on the router to reduce the attack surface. Services such as telnet or ftp can pose a security risk.
2.  **Strong Passwords:** Use a strong, unique password for all user accounts on the router.
3.  **Firewall:** Implement a robust firewall configuration. Only allow necessary ports from trusted IP addresses. Deny all other incoming and outgoing traffic.
4.  **Secure Access:** Only allow router access from known IP addresses. Enable secure protocols like HTTPS for web access, and SSH for CLI access. Disable the HTTP service for remote management.
5.  **Regular Updates:** Always keep the RouterOS software updated to the latest stable version. This ensures you have the most recent security patches and bug fixes.
6.  **Monitor Logs:** Regularly review system logs for any suspicious activity.
7.  **Limit User Access:** Create specific users with only necessary permissions, and don't use the admin user for day-to-day management.
8.  **Bridge Filtering:** You can configure bridge filtering to control what types of traffic are allowed to pass through the bridge. This can add another layer of security, but can also be hard to manage correctly.
9.  **Wireless:** If you are using WiFi on the MikroTik, ensure the wireless network is secure, using the latest encryption protocol (WPA3 if available) and a strong password.
10. **Do not use default usernames or ports:** Change the default usernames and remote access ports (e.g. ssh port to something other than 22, API to something other than 8728).

## Self Critique and Improvements

This configuration is a solid foundation for a basic SOHO setup. However, here's where it could be improved:

1.  **DHCP Server:** Adding a DHCP server on the bridge would make it easier to manage client IP addresses. It would also prevent the need for manually configuring IP addresses on each device.
2.  **More Advanced Firewall:** The current setup does not include any firewall rules. An implementation with address lists, different chain and port rules will increase network security.
3.  **Traffic Shaping:** Implementing basic QoS for bandwidth management could prioritize certain applications or users. This would help with network congestion and ensure that important applications have the required bandwidth.
4.  **Logging:** Adding more advanced logging and monitoring would assist in identifying problems faster.
5.  **Remote Logging:** Implementing a remote syslog server allows to keep logs even if the router is compromised.

## Detailed Explanation of Topic: IP Routing

IP routing is the process of selecting paths for network traffic to travel across one or more networks. It determines the direction that packets take from their source to their destination. In essence, routers make the decision of which way to forward each incoming IP packet. This is done using routing tables that map destinations to gateways that the router should forward the packet to. This table usually contains several elements:

*   **Destination Network:** The network (or IP address) the packet is trying to reach.
*   **Gateway:** The IP address of the next hop router or next device that can take the packet one step closer to its final destination. This can also be the same interface the packet is received from, in the case of directly connected networks.
*   **Interface:** The interface (e.g., `ether2`, `bridge-13`) used to reach the network or gateway.
*   **Route Preference:** A number that indicates the desirability of this route. In case multiple routes to the same destination exist, the router will choose the route with the lowest preference.
*   **Distance:** The hop count to reach a certain network or IP address.

Routers use this information to make decisions about where to forward packets. The most specific route (longest prefix match) is chosen in case multiple routes for the same destination are available. Routes can be static (configured manually) or dynamic (learned through routing protocols).

## Detailed Explanation of Trade-offs:

When configuring IP routing, there are trade-offs to consider:

1.  **Static vs Dynamic Routing:**
    *   **Static Routing:** Simple to implement for small networks, less resource intensive, but requires manual configuration for each route. If a path fails, there is no fallback in case the link goes down.
    *   **Dynamic Routing:** Automatically learns routes, adapts to network changes, scalable for large networks, but more complex to set up, and uses more router resources.
2.  **Bridge vs Routed Interfaces:**
    *   **Bridge:** Multiple ports act as a single network (like a switch), easier to set up, less CPU intensive for simple networks. All devices in the bridge are part of the same network and broadcast domain.
    *   **Routed Interfaces:** Each interface is a separate network, offers more control, and increases security (can implement specific firewall rules between each network), but more complex to configure, and requires IP addresses on each interface.
3.  **Firewall Performance:**
    *  **Complex Firewall Rules:** The more complex the firewall rules (with more lists, and complex matching) the higher the load on the router CPU to process all packets. This can result in higher latency.
    *  **Simple Firewall Rules:** Using fewer and simpler rules will result in a faster throughput and less latency but could expose the network to security risks.
4.  **Network Segmentation:**
    *   **Single Broadcast Domain (Bridge):** Easier configuration, but may cause performance and security issues in larger networks. One broadcast will reach all devices on the same bridge, making troubleshooting more difficult.
    *   **Multiple Broadcast Domains (Routed Interfaces/VLANs):** Increased security and less broadcast traffic, but more complex configuration.
5. **Router CPU Usage:**
   * **More Complex Configuration:** The more complex a configuration (for instance with more complex firewalls, multiple bridges or VLANs, or advanced routing) the more CPU will be required to process the data.
   * **Simpler Configuration:** If not enough CPU is used by the router, latency can be very high, and the router could be unresponsive. If a simpler configuration is implemented, the CPU will perform better but the functionality will be limited.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 6.48. Most, if not all of these commands, are fully compatible with RouterOS v7.x. There may be slight differences in output, but the syntax and functionality is the same. If a very specific version is being used, you should check the Mikrotik documentation before implementing the configuration in a production environment.

By following these instructions, you should have a good understanding of how to configure basic IP routing on a MikroTik device. If you need help on specific parts of this document, please ask!
