Okay, let's dive into a detailed configuration and explanation of a MAC server setup on a MikroTik router running RouterOS 7.11, focusing on the subnet 112.58.138.0/24 on interface `vlan-60`. This is a less common feature, so we'll pay close attention to the details.

## Scenario Description:

We are setting up a MAC server on a MikroTik router. This MAC server will provide IP addresses to devices connecting to the network via DHCP based on their MAC addresses. This is useful for static IP assignments based on devices, even when DHCP is in use. Instead of using the DHCP reservations, we will create MAC server rules for specific MACs on our network. The `vlan-60` interface, which is associated with the 112.58.138.0/24 subnet, will be our focus.

## Implementation Steps:

Here's a step-by-step guide to configure the MAC server. We will be using both CLI and Winbox for this example.

### 1. **Step 1**: Ensure Basic Network Configuration is in Place

*   **Explanation**: Before configuring the MAC server, ensure that basic network functionality is established. This includes a defined interface (in this case, `vlan-60`), a configured IP address range for the interface, and a DHCP server.

*   **Pre-Configuration Check (CLI):**
    ```mikrotik
    /interface print
    /ip address print
    /ip dhcp-server print
    ```

    **Pre-Configuration Check (Winbox):**
    *Navigate to `Interface` to verify the existence of `vlan-60`.*
    *Navigate to `IP -> Addresses` to ensure the interface has an IP address*
    *Navigate to `IP -> DHCP Server` to make sure a DHCP server is set up on interface*

*   **Example Pre-Configuration Output (CLI):**

    ```
    /interface print
    Flags: D - dynamic; X - disabled; R - running; S - slave
     #    NAME                                TYPE      MTU  L2MTU MAX-L2MTU
     0  R ether1                              ether     1500 1596  9190
     1  R vlan-60                             vlan      1500 1596  9190
    ```
    ```
    /ip address print
    Flags: X - disabled, I - invalid, D - dynamic
    #   ADDRESS            NETWORK         INTERFACE
    0   192.168.88.1/24    192.168.88.0    ether1
    1   112.58.138.1/24   112.58.138.0    vlan-60
    ```
    ```
    /ip dhcp-server print
    Flags: X - disabled, I - invalid
     #   NAME                     INTERFACE   RELAY        ADDRESS-POOL LEASE-TIME ADD-ARP
    0   dhcp-vlan60       vlan-60      0.0.0.0    dhcp_pool1           3d yes
    ```

*   **Action**: No changes are needed here, assuming this setup is already configured.

### 2. **Step 2**: Enable the MAC Server

*   **Explanation**: We now need to enable the MAC server itself. This server will listen for DHCP requests and determine IP addresses based on MAC rules.

*   **Pre-Configuration Check (CLI):**
    ```mikrotik
    /ip mac-server print
    ```

*   **Pre-Configuration Check (Winbox):**
    *Navigate to `IP -> MAC Server`.*

*   **Example Pre-Configuration Output (CLI):**
    ```
    /ip mac-server print
    Flags: X - disabled, I - invalid
    ```
    *Note: there are no mac-servers configured yet*

*   **Configuration (CLI):**
    ```mikrotik
    /ip mac-server add interface=vlan-60 disabled=no
    ```

    *`interface=vlan-60`*: Specifies the interface to listen for MAC server requests on.
    *`disabled=no`*: Enables the MAC server on the interface.

*   **Configuration (Winbox):**
    *Navigate to `IP -> MAC Server`, click the `+` icon.*
    *Select `vlan-60` under the `Interface` dropdown.*
    *Uncheck the `Disabled` box.*
    *Click `OK` to add the MAC server entry.*

*   **Post-Configuration Check (CLI):**
    ```mikrotik
    /ip mac-server print
    ```

*   **Post-Configuration Check (Winbox):**
    *Verify a MAC server entry now exists under `IP -> MAC Server` with the interface as `vlan-60`.*

*   **Example Post-Configuration Output (CLI):**
    ```
    /ip mac-server print
    Flags: X - disabled, I - invalid, D - dynamic
     #   INTERFACE   DISABLED
     0  vlan-60       no
    ```

*   **Effect**: This enables the MAC server on the `vlan-60` interface.

### 3. **Step 3**: Configure MAC Address Rules

*   **Explanation**: Now we'll configure rules based on MAC addresses. These rules will specify the IP address to be assigned for a specific MAC address.

*   **Pre-Configuration Check (CLI):**
    ```mikrotik
    /ip mac-server mac-address print
    ```

*   **Pre-Configuration Check (Winbox):**
    *Navigate to `IP -> MAC Server -> MAC Addresses`.*

*   **Example Pre-Configuration Output (CLI):**
    ```
    /ip mac-server mac-address print
    Flags: X - disabled, I - invalid
    ```
    *Note: there are no mac-addresses configured yet*

*   **Configuration (CLI):**
    ```mikrotik
    /ip mac-server mac-address add mac-address=00:11:22:33:44:55 address=112.58.138.10
    /ip mac-server mac-address add mac-address=AA:BB:CC:DD:EE:FF address=112.58.138.20
    ```

    *`mac-address=00:11:22:33:44:55`*: Specifies the MAC address to match. Replace with an actual MAC address in your network.
    *`address=112.58.138.10`*: Specifies the IP address to assign to the given MAC.
    *Repeat this command for each MAC address and associated IP.*

*   **Configuration (Winbox):**
    *Navigate to `IP -> MAC Server -> MAC Addresses`, click the `+` icon.*
    *Enter the MAC address and corresponding IP address and click `OK`.*
    *Repeat for each MAC and IP combination.*

*   **Post-Configuration Check (CLI):**
    ```mikrotik
    /ip mac-server mac-address print
    ```

*   **Post-Configuration Check (Winbox):**
    *Verify that each MAC address entry exists under `IP -> MAC Server -> MAC Addresses`.*

*   **Example Post-Configuration Output (CLI):**

    ```
    /ip mac-server mac-address print
    Flags: X - disabled, I - invalid
     #   MAC-ADDRESS       ADDRESS
     0   00:11:22:33:44:55  112.58.138.10
     1   AA:BB:CC:DD:EE:FF  112.58.138.20
    ```

*   **Effect**: This configures static IP assignment based on MAC addresses. DHCP requests from these MAC addresses will now receive the configured IPs.

## Complete Configuration Commands:

```mikrotik
/ip mac-server
add interface=vlan-60 disabled=no

/ip mac-server mac-address
add mac-address=00:11:22:33:44:55 address=112.58.138.10
add mac-address=AA:BB:CC:DD:EE:FF address=112.58.138.20
```

## Common Pitfalls and Solutions:

1.  **DHCP Server Conflict:**
    *   **Problem:** If a DHCP reservation is set up for the same IP address as the MAC server entry, there could be conflicts.
    *   **Solution:** Avoid duplicate IP addresses. If you need to use specific IP addresses, prefer using the mac server over DHCP reservations or do not use any DHCP reservation for the MACs configured in the mac server.
2.  **Incorrect Interface:**
    *   **Problem:** The MAC server is not enabled on the correct interface.
    *   **Solution:** Double-check that the MAC server is bound to the `vlan-60` interface.
3.  **Incorrect MAC Address:**
    *   **Problem:** Typing a MAC address incorrectly can result in devices not receiving the correct IP address.
    *   **Solution:** Always copy and paste MAC addresses or use the MikroTik tools to discover devices and their MACs.
4.  **Misconfigured Address**:
    *   **Problem:** Typing an incorrect IP Address on the `address` param will cause the DHCP to provide the incorrect IP for that MAC.
    *   **Solution:** Always verify the configured IP Addresses to make sure they match your network design.

## Verification and Testing Steps:

1.  **Device Connection:** Connect a device with a MAC address that you've configured in the MAC server to the `vlan-60` network.
2.  **IP Address Verification:** Check the connected device's IP address. It should be the address you assigned in the MAC server. You can do this on the device itself, or via the MikroTik router.
3.  **MikroTik Lease Monitoring:**
    *   Use the command:
    ```mikrotik
        /ip dhcp-server lease print where mac-address=00:11:22:33:44:55
    ```
    *   Check that the client has the correct IP.

4.  **Torch (traffic analysis tool):** Use `/tool torch interface=vlan-60` to observe DHCP requests and responses on the `vlan-60` interface. Verify the correct MAC addresses are involved in the DHCP process.
5.  **Packet Capture:** Use `/tool packet-sniffer` to capture DHCP requests.

## Related Features and Considerations:

1.  **DHCP Options:** The MAC server does not impact DHCP options, use DHCP server settings for these if needed.
2.  **Address Pool Management:** Ensure that the MAC server's IP assignments are within your DHCP address pool, but outside any dynamic range, to avoid collisions.
3.  **MAC Address Discovery:** Tools like the MikroTik `neighbor discovery` or `torch` can be helpful in finding MAC addresses of network devices.
4.  **Security:** Be cautious with MAC address assignment. MAC addresses are not a strong form of security, and they can be spoofed, but this can be a first line of defense in your network. MAC addresses should also be kept private to avoid tracking.
5. **Monitoring:** `/ip mac-server monitor [id]` can be used to track mac server performance.

## MikroTik REST API Examples:

```bash
# Example: Get the list of configured MAC servers
curl -k -u admin:YOUR_PASSWORD -H 'Content-Type: application/json' https://YOUR_ROUTER_IP/rest/ip/mac-server

# Example: Add a MAC server on vlan-60
curl -k -u admin:YOUR_PASSWORD -H 'Content-Type: application/json' -X POST -d '{"interface": "vlan-60", "disabled": false}' https://YOUR_ROUTER_IP/rest/ip/mac-server

# Example: Get the list of MAC address entries
curl -k -u admin:YOUR_PASSWORD -H 'Content-Type: application/json' https://YOUR_ROUTER_IP/rest/ip/mac-server/mac-address

# Example: Add a mac-address with specific address
curl -k -u admin:YOUR_PASSWORD -H 'Content-Type: application/json' -X POST -d '{"mac-address": "00:11:22:33:44:55", "address": "112.58.138.10"}' https://YOUR_ROUTER_IP/rest/ip/mac-server/mac-address
```

*   **API Endpoint**: `/rest/ip/mac-server` and `/rest/ip/mac-server/mac-address`
*   **Request Method**: `GET`, `POST`
*   **JSON Payload**:
    *   `interface`: (String) Name of the interface.
    *   `disabled`: (Boolean) Whether the MAC server is disabled.
    *   `mac-address`: (String) MAC Address of the client device.
    *   `address`: (String) IP Address to assign to that MAC.
*   **Expected Response**: JSON data showing the current configuration, or the result of adding/modifying entries.
*   **Error Handling**: The API will return appropriate HTTP status codes and error messages if there are problems with the request (e.g., missing parameters, authentication issues).

## Security Best Practices

1.  **Password Management:** Ensure your MikroTik router has a strong and complex password.
2.  **Access Control:** Restrict access to the router's management interface using firewall rules and access lists. Do not expose your admin ports to the internet.
3.  **MAC Address Filtering:** Do not rely solely on MAC address filtering for network security, as it is easily bypassed. MAC Address filtering should be combined with other security methods such as strong passwords, firewall rules, and access lists.
4.  **Regular Updates:** Keep the RouterOS updated to patch any security vulnerabilities.

## Self Critique and Improvements

*   **Improvement**: Dynamic MAC Address Assignment
    *   Current Setup: We have a static, one-to-one mapping of MAC addresses to IP addresses.
    *   Improved Setup: If possible, a system which can allocate IP addresses dynamically within a certain range, per MAC address can be beneficial, but is not supported by RouterOS directly. Such functionality can be achieved via API and external scripts.

*   **Improvement**: Centralized MAC Management
    *   Current Setup: The MAC address and IP assignments are local to the router.
    *   Improved Setup: Consider a centralized system where MAC assignments are managed, which can provide better control and logging, but is out of scope for RouterOS capabilities.

## Detailed Explanations of Topic

*   **MAC Server Functionality**: The MikroTik MAC server acts as a custom DHCP server, but it bases its IP assignment solely on the MAC address of the connecting device. It acts *before* the default DHCP process, which means that these IP addresses will be assigned as soon as the request is sent. It checks against the configured MAC address rules and uses the corresponding IP address. If a MAC address is not found, the DHCP process continues to allocate a dynamic address.
*   **Use Cases**: Ideal for assigning static IPs to specific network devices that need consistent addresses, while maintaining the convenience of DHCP. This can be particularly useful in environments with managed switches where the network admin wants to provide fixed addresses to various devices, without having to set static IPs on the client device itself.
*   **Relation to DHCP**: The MAC server operates in tandem with the standard DHCP server. It intercepts DHCP requests and assigns IP addresses before the regular DHCP server has a chance to act. If a MAC address is not listed in the MAC server rules, the standard DHCP process will allocate an IP address from the pool.

## Detailed Explanation of Trade-offs

*   **Trade-off: DHCP Reservations vs MAC Server Rules**

    *   **DHCP Reservations**:
        *   **Pros**: Easier for beginners to understand, can be accessed easily via Winbox or the CLI.
        *   **Cons**: DHCP Reservations are assigned at a different step from the MAC address check, meaning that the client will usually receive a random address before a DHCP lease with the reservation is given.
    *   **MAC Server Rules**:
        *   **Pros**: Faster IP address assignment and more reliable when a large number of reservations need to be setup. Provides a static IP as the first DHCP request, which is also useful for client devices to immediately use the IP address assigned.
        *   **Cons**: More advanced feature, harder to troubleshoot and is only a manual implementation via CLI or Winbox, so no central management or tools to easily monitor MAC registrations.

*   **Trade-off: Manual vs Dynamic MAC Management**
    *   **Manual**:
        *   **Pros**: Complete control over assigned IP Addresses.
        *   **Cons**: Increased administrative overhead.
    *   **Dynamic**:
        *   **Pros**: Automation, can scale to many devices.
        *   **Cons**: Requires scripting and external systems, which makes setup more complex and requires deeper knowledge in both scripting and networking.

## Configuration for Specific RouterOS Versions:

*   The configuration described above works for RouterOS 7.11. The same configuration works for RouterOS versions 6.48 and above as well, but might use older menu structures or syntax.
*   If using older versions of RouterOS (e.g. v6.x), the command `/ip mac-server` might use different sub-commands, syntax, or parameter names. You will need to check the corresponding manuals.

This documentation provides a detailed overview of how to set up a MAC server on a MikroTik router, offering step-by-step instructions, configurations, troubleshooting, and security considerations. The provided examples are testable and applicable in real-world scenarios.
