Okay, here's a detailed technical document for bridging and switching on a MikroTik router, specifically addressing your scenario with the subnet 224.98.130.0/24 and interface `wlan-99`, targeted for RouterOS 6.48 (but also applicable to 7.x). This configuration is designed for a basic, SOHO environment.

## Scenario Description:

This scenario involves creating a bridge interface on a MikroTik router and adding the `wlan-99` wireless interface to that bridge. This effectively makes all the clients connected to the `wlan-99` interface part of the same Layer 2 broadcast domain as the other interfaces added to the bridge. This is commonly used when you want wireless clients to have direct access to the same network as your wired clients, where they will receive IP addresses from the same DHCP server. In this specific case, any IP addressing on the bridge will be done on the 224.98.130.0/24 subnet, meaning the wireless clients will be on that network too.

## Implementation Steps:

Here's how to configure the bridging and switching:

**Before starting**: The `wlan-99` wireless interface should already be configured as a working wireless interface. This guide will assume it is already working on layer2 (not as a bridge or something else).

1. **Step 1: Create a Bridge Interface**

   * **Explanation**: We need to create a bridge interface which will act as the virtual switch to connect the interfaces together.
   * **CLI Command**:
     ```mikrotik
     /interface bridge add name=bridge-local protocol-mode=none
     ```
   * **Winbox GUI**:
       * Go to `Bridge` menu.
       * Click the `+` button.
       *  Set `Name` to `bridge-local`, `Protocol Mode` to `none`
       * Click `Apply` then `OK`.
   * **Before Command Effect**: No bridge exists.
   * **After Command Effect**: A new bridge named `bridge-local` is created and listed in the interfaces menu, and ready to have interfaces added. The bridge will not forward any packets at this moment.

2. **Step 2: Add the `wlan-99` interface to the Bridge**

   * **Explanation**: Here, we add the `wlan-99` interface to the `bridge-local` bridge. This will make all wireless traffic from `wlan-99` handled by the bridge.
   * **CLI Command**:
     ```mikrotik
     /interface bridge port add bridge=bridge-local interface=wlan-99
     ```
   * **Winbox GUI**:
        * Go to `Bridge` -> `Ports` tab.
        * Click the `+` button.
        * Set `Interface` to `wlan-99`, and `Bridge` to `bridge-local`.
        * Click `Apply` then `OK`.
   * **Before Command Effect**: `wlan-99` was not a part of any bridge.
   * **After Command Effect**: Wireless traffic from `wlan-99` will now be bridged and the interface will appear in the bridge's `Ports` tab.

3. **Step 3: Add other (Optional) interfaces to the Bridge (e.g., `ether1`)**

   * **Explanation**: You can add other interfaces to the same bridge, which allows wired devices connected to `ether1` to participate in the same local network. This is optional.
   * **CLI Command Example (For `ether1`)**:
        ```mikrotik
        /interface bridge port add bridge=bridge-local interface=ether1
        ```
   * **Winbox GUI (For `ether1`)**:
        * Go to `Bridge` -> `Ports` tab.
        * Click the `+` button.
        * Set `Interface` to `ether1`, and `Bridge` to `bridge-local`.
        * Click `Apply` then `OK`.
   * **Before Command Effect**: `ether1` was not a part of the bridge.
   * **After Command Effect**: Traffic from `ether1` is now also handled by the `bridge-local`.

4.  **Step 4: Assign an IP address to the Bridge Interface**

    * **Explanation**: Assign an IP address on the bridge will configure the IP address that the bridged interfaces will use.
    * **CLI Command:**
        ```mikrotik
        /ip address add address=224.98.130.1/24 interface=bridge-local
        ```
    * **Winbox GUI**:
        * Go to `IP` -> `Addresses` tab.
        * Click the `+` button.
        * Set `Address` to `224.98.130.1/24`, and `Interface` to `bridge-local`.
        * Click `Apply` then `OK`.
    * **Before Command Effect:** The bridge interface has no IP assigned.
    * **After Command Effect:** The `bridge-local` will now operate at the IP address specified.

5. **Step 5: Configure DHCP Server**

   * **Explanation**: If you want the clients on this network to receive IP addresses automatically, set up a DHCP server for the network, on the bridge interface.
   * **CLI Command:**
      ```mikrotik
      /ip dhcp-server add address-pool=dhcp_pool_local disabled=no interface=bridge-local lease-time=10m name=dhcp_local
      /ip pool add name=dhcp_pool_local ranges=224.98.130.2-224.98.130.254
      /ip dhcp-server network add address=224.98.130.0/24 gateway=224.98.130.1 dns-server=8.8.8.8,1.1.1.1
      ```
   * **Winbox GUI**:
       * Go to `IP` -> `DHCP Server` -> `DHCP` tab, click the `+` button.
       *  Set `Name` to `dhcp_local`, `Interface` to `bridge-local`. Make sure `disabled` is not checked. Click `Apply`, then switch to `Networks` tab.
       * Go to `IP` -> `Pool`, click `+` button, set the `Name` to `dhcp_pool_local` and `Ranges` to `224.98.130.2-224.98.130.254`, then click `Apply` then `OK`.
       * Go back to `IP` -> `DHCP Server` -> `Networks` tab, click the `+` button.
       * Set the `Address` to `224.98.130.0/24`, `Gateway` to `224.98.130.1`, `DNS Server` to `8.8.8.8,1.1.1.1`. Click `Apply` then `OK`.
    * **Before Command Effect:** No DHCP server is running.
    * **After Command Effect:** A DHCP server is running for the bridge interface and clients can get an IP automatically.

## Complete Configuration Commands:

```mikrotik
/interface bridge
add name=bridge-local protocol-mode=none
/interface bridge port
add bridge=bridge-local interface=wlan-99
add bridge=bridge-local interface=ether1  # Optional - add other interfaces as needed
/ip address
add address=224.98.130.1/24 interface=bridge-local
/ip dhcp-server
add address-pool=dhcp_pool_local disabled=no interface=bridge-local lease-time=10m name=dhcp_local
/ip pool
add name=dhcp_pool_local ranges=224.98.130.2-224.98.130.254
/ip dhcp-server network
add address=224.98.130.0/24 gateway=224.98.130.1 dns-server=8.8.8.8,1.1.1.1
```

**Parameter Explanation Table:**

| Command      | Parameter          | Description                                                                              |
|--------------|--------------------|------------------------------------------------------------------------------------------|
| `/interface bridge add` | `name`             | The name of the bridge interface.                                                               |
|              | `protocol-mode`   | Bridge protocol settings, `none` turns it off for basic bridging, could also be `stp`, `rstp` or `mstp`.              |
| `/interface bridge port add` | `bridge`    | The bridge interface name to which the port should be added.                    |
|              | `interface`        | The specific interface to add to the bridge.                                                  |
| `/ip address add` | `address`          | The IP address and subnet mask to assign to the bridge interface.                          |
|              | `interface`          | The interface for the IP to be assigned. In this case the bridge.                       |
| `/ip dhcp-server add`    |  `address-pool`     |  Name of IP pool to be used for leases|
|           |  `disabled`           |   If the dhcp server is enabled or not. `no` to enable.                                                               |
|           | `interface`       |  The bridge interface the dhcp server will be used on.                                                              |
|           | `lease-time`   |   The dhcp lease time, in this case is 10m (10 minutes)                                                                |
|           |  `name`            |  The name of the dhcp server.                                                               |
| `/ip pool add`    | `name`         | The pool name for dhcp ip address leases.                                                          |
|           |  `ranges`        |   The pool of ip address to give out.                                                               |
| `/ip dhcp-server network add`    | `address`  | The network address of the subnet.                                                     |
|           | `gateway`         |   The default gateway for the subnet.                                                              |
|           |  `dns-server`        |   The DNS servers to pass on to clients.                                                              |

## Common Pitfalls and Solutions:

*   **Wireless Connectivity Issues**: If clients can't connect to the Wi-Fi or get IP addresses:
    *   **Problem**: Ensure your wireless security profile is correctly configured on the `wlan-99` interface.
    *   **Solution**: Double-check the `Security Profile` of your wireless interface.
*   **No DHCP Leases**: If clients don't get an IP address:
    *   **Problem**: The DHCP server might be misconfigured, or no DHCP is running.
    *   **Solution**: Check if the DHCP server is enabled (`/ip dhcp-server print`). Verify the `address-pool`, `network`, and `interface` configuration is correct.
*   **Routing Issues**: If devices on the bridge can’t reach the internet or local network:
    *   **Problem**: The bridge IP might be misconfigured, the DHCP config is incorrect, or the default gateway is missing in the DHCP configuration.
    *   **Solution**: Verify the IP address of the bridge (e.g. `224.98.130.1/24`), check the dhcp networks config and verify the gateway and dns is set correctly for DHCP.
*   **Spanning Tree Conflicts**: In more advanced setups, using STP/RSTP could cause issues.
    *   **Problem**:  STP can loop ports.
    *   **Solution**:  If using spanning tree protocols, make sure all bridge interfaces use the same setting, and all the ports are correctly configured for root and priority. For basic bridges it's better to use `protocol-mode=none`.
*   **High CPU/Memory Usage**:
    *   **Problem**: Too many bridge ports and broadcast traffic can cause high resource usage.
    *   **Solution**: Monitor your router's resource usage in `/system resource print`. If usage is too high, filter broadcast traffic or use VLANs for a more advanced setup. You may need a stronger router if the CPU is too high.
*   **Security Issues**:
    *   **Problem**: The bridge could make a "flat" network, where all connected devices are on the same network and reachable from each other.
    *   **Solution**: Be aware that devices on this bridge can reach each other, and make sure to have a proper security configuration such as firewall, or VLANS if necessary.

## Verification and Testing Steps:

1.  **Ping Test:**
    *   From a computer connected to the `wlan-99` Wi-Fi, ping the bridge IP:
        ```bash
        ping 224.98.130.1
        ```
    *   If you get a response, the bridging is configured correctly.
    *   If you do not get a response, check your IP address on your computer and if you can ping the router from any interface (wired or wireless). If this fails, you may have to reconfigure your wireless security, the bridge, or your firewall.

2.  **IP Configuration:**
    *   Verify your device gets an IP address from the correct range (224.98.130.2-224.98.130.254). This means the DHCP configuration is ok.

3. **Traceroute**:
   * Do a traceroute to an external website, to verify if your route is working fine.
     ```bash
        traceroute google.com
     ```

4.  **MikroTik Torch**:
    *   Run `/tool torch interface=bridge-local` on the MikroTik router and observe traffic patterns. This is useful if you want to diagnose network congestion.

5.  **Check Bridge Table**:
    *   On the Mikrotik router run `/interface bridge host print`. You should see devices on your wireless and wired interfaces. If you do not see any, try to check if your computer is getting an ip address correctly.

## Related Features and Considerations:

*   **VLANs:** For a more complex setup, consider using VLANs to isolate different types of traffic on the same physical bridge.
*   **Firewall Rules:** Properly configured firewall rules are essential to secure this bridged network. Make sure you block inter-VLAN routing if required, or any traffic you don't want to be routed.
*   **Multiple Bridges:** You can create multiple bridges for different subnets, each on a different network, to isolate traffic from each other.
*   **Spanning Tree Protocol (STP/RSTP):** For looped network topologies, use STP/RSTP to prevent network loops.
*   **Wireless Advanced Settings:** Consider configuring wireless advanced features such as client isolation, or disabling unnecessary features for security.
*   **IP Addressing Scheme:** Always plan your addressing scheme for future expansion and manageability.
*   **MAC Address Table Size**: RouterOS has a limited MAC address table for Layer 2 switching. If your network has many devices, the bridge's MAC address table may run out of space. This can cause issues with the network. Monitor your bridge mac address usage with the command: `/interface bridge host print`.

## MikroTik REST API Examples:

This feature does not translate well to the REST API. The API allows you to manage bridges, and bridge ports, but not in one step. Therefore it can be difficult to set up a fully functional bridge using REST, compared to the CLI.

**Example 1: Create a Bridge Interface (Simplified)**

*   **Endpoint:** `/interface/bridge`
*   **Method:** `POST`
*   **Request Payload (JSON):**

    ```json
    {
        "name": "bridge-local",
        "protocol-mode": "none"
    }
    ```
*   **Expected Response (201 Created):**

    ```json
    {
        "id": "*12"
        "name": "bridge-local",
        "protocol-mode": "none",
        // ... other fields
     }
    ```
* **Error Handling:** If you try to create a bridge that already exists, or an incorrect parameter is sent, an error code can be expected in the response. Make sure to handle these in your script/program.
* **Explanation:**
    *  `name`: sets the bridge name.
    *  `protocol-mode`: sets the spanning tree protocol of the bridge.

**Example 2: Add an Interface to a Bridge**
*   **Endpoint:** `/interface/bridge/port`
*   **Method:** `POST`
*   **Request Payload (JSON):**
    ```json
    {
        "bridge": "bridge-local",
        "interface": "wlan-99"
    }
    ```
*   **Expected Response (201 Created):**
    ```json
    {
        "bridge": "bridge-local",
        "interface": "wlan-99",
         // ... other fields
     }
    ```
* **Error Handling:** If the bridge or the interface doesn't exist, or an incorrect parameter is sent, an error code can be expected in the response. Make sure to handle these in your script/program.
*   **Explanation:**
    * `bridge`: The name of the bridge interface the port will be added to.
    * `interface`: The name of the interface you want to add to the bridge.

**Example 3: Get bridge information**

*   **Endpoint:** `/interface/bridge`
*   **Method:** `GET`
*   **Request Payload:** None
* **Expected Response (200 OK):**

    ```json
     [
         {
             "id": "*12",
             "name": "bridge-local",
             "protocol-mode": "none",
             // ... other fields
         }
    ]

    ```

**Note:** Ensure you are authenticated with the MikroTik API to perform the above calls.

## Security Best Practices

*   **Wireless Security:**  Use strong WPA2/WPA3 encryption with a complex passphrase for your wireless network.
*   **Firewall:**  Implement a strong firewall to control traffic between the bridge, other interfaces, and external networks. This will improve your overall network security.
*   **Management Access:** Restrict access to the router management interface. Do not let external addresses have access to it, and make sure to limit the allowed ip addresses with access to it.
*   **RouterOS Updates:**  Keep your RouterOS updated to the latest stable version for security patches. RouterOS updates can fix security bugs and implement important security updates, so updating is very important.
*  **Client isolation**: Use client isolation to prevent wireless clients from connecting to each other, which can be a security issue in the case of malicious devices.
* **Wireless security profiles**: Always configure proper security profiles, to prevent unauthorized access to your wireless network.
* **Default credentials**: Never use the default login name and password, always set up your own.
* **Bridge security**: Set up your bridge as secure as possible, if needed you can limit mac addresses allowed on the bridge.

## Self Critique and Improvements

*   **Basic Setup:** This is a basic bridging configuration. It would be beneficial to expand upon more complex setups like VLANs, bonding or port security.
*   **Error Handling:** Error handling in the CLI commands is very basic. It can be improved with better error handling for more complex situations.
*   **Automation:** For more complex setups, consider using scripts or automation for repetitive tasks.
*   **Monitoring**: Setup monitoring tools to monitor bridge usage, traffic patterns and error messages.
*   **Security**: For more sensitive environments, implementing additional firewall rules or more security features is recommended.

## Detailed Explanations of Topic

**Bridging and Switching**:

*   **Bridging:** Creates a single broadcast domain, merging two or more networks at Layer 2 of the OSI model. The bridge functions as a network switch, learning MAC addresses and forwarding frames accordingly. In MikroTik, this is done using a virtual bridge interface.
*   **Switching**: Refers to the hardware-level forwarding of frames based on their destination MAC address. Bridges operate on the concept of switching, learning mac addresses dynamically and routing packets on layer 2.
* **Layer 2:** This operation is on the layer 2 of the OSI model, which handles the routing of traffic through mac addresses.
*   **Broadcast Domain:** A bridge creates a shared broadcast domain. All devices on the bridge receive broadcasts and layer 2 multicast traffic, regardless of what port the traffic is coming from. This has security implications and should be considered.

## Detailed Explanation of Trade-offs

*   **Bridge vs. Router:** Bridging makes multiple networks one single network at Layer 2. Routing, on the other hand, keeps each network separate by using Layer 3 (IP addresses). Routing provides more security and manageability. Bridges allow multiple interfaces to act as a single logical interface, which can simplify routing and administration, and reduce processing on the router.
*   **Flat Network:** A bridge will create a flat network, which means all devices on the bridge are directly reachable by each other, and potentially vulnerable if there is a malicious device.
*   **STP/RSTP:** While essential for loop prevention, STP/RSTP can add overhead and complexity. Use only when necessary. If you have a single bridge with no loops, it's safe to disable it and run `protocol-mode=none`, which also makes bridging faster.
*   **CPU and Memory:** Bridging increases traffic on the router, which can consume CPU and memory. Monitor resources and optimize configurations.
*   **Security:** Bridging can add security risks, as mentioned previously. Firewall configurations and client isolation can be used to avoid this.

## Configuration for Specific RouterOS Versions:

This configuration is for both RouterOS 6.48 and 7.x, using the same command syntax. There are few differences in syntax between these versions for basic bridging, which is why this configuration works for both.

This complete documentation should provide a solid foundation for understanding and configuring bridging and switching on a MikroTik RouterOS device. Feel free to ask if you need more clarification or additional examples!
