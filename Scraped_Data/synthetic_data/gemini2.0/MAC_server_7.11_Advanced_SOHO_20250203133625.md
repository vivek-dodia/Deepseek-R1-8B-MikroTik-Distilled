Okay, let's craft a comprehensive guide for setting up a MAC server on MikroTik RouterOS 7.11 (also applicable to 6.48, and 7.x) within a SOHO network using the subnet 172.183.89.0/24 and the bridge interface 'bridge-22'. This is considered an "advanced" configuration due to the less common usage of MAC server functionality.

## Scenario Description:

This scenario involves setting up a MAC server on a MikroTik router. The MAC server allows the router to act as an authoritative source for IP addresses and other parameters based on the MAC addresses of connected devices on a network. This is beneficial for scenarios where static IP assignment based on MAC address is needed, allowing consistent network behavior for certain devices or when a specific IP range is desired. We will be setting it up to work on the `bridge-22` interface within the `172.183.89.0/24` subnet.

## Implementation Steps:

Here's a step-by-step guide, explaining each step, and providing practical examples:

### Step 1: Verify or Create Bridge Interface and IP Address

*   **Purpose:**  Ensure the existence of the bridge interface (`bridge-22`) and the assignment of a suitable IP address to it.
*   **CLI Commands (Before):**

    ```mikrotik
    /interface bridge print
    /ip address print
    ```

    *Output should show if `bridge-22` and an IP within 172.183.89.0/24 exists.* If not, proceed.

*   **GUI Instructions (Winbox):**
    *   **Bridge:** Navigate to `Bridge` and see if `bridge-22` exists.
    *   **IP Address:** Navigate to `IP` -> `Addresses` and see if an IP from `172.183.89.0/24` is on `bridge-22`.
*   **Action:** If the bridge does not exist create it. if an IP does not exist, assign one.

*   **CLI Commands (After Creating Bridge, example):**
     ```mikrotik
     /interface bridge add name=bridge-22
     /ip address add address=172.183.89.1/24 interface=bridge-22
     ```
*   **GUI Instructions (Winbox, Creating Bridge, example):**
    *   Go to `Bridge`, click the `+`, add the name, click `OK`.
    *   Go to `IP` -> `Addresses`, click the `+`, add the address, select `bridge-22` and click OK.
*   **Effect:** The `bridge-22` interface is created and assigned an IP address.

### Step 2: Add Bridge Ports

*   **Purpose:** Add physical or virtual interfaces to the newly created `bridge-22`.
*   **CLI Commands (Before):**
    ```mikrotik
     /interface bridge port print
    ```
*   **GUI Instructions (Winbox):**
    *   Go to `Bridge` -> `Ports` to check existing ports.
*   **Action:** Add necessary interfaces to the bridge.
*   **CLI Commands (After, example):**
    ```mikrotik
    /interface bridge port add bridge=bridge-22 interface=ether2
    /interface bridge port add bridge=bridge-22 interface=ether3
    ```
    *This assumes `ether2` and `ether3` are the interfaces for which you wish to enable the MAC server.*
*   **GUI Instructions (Winbox, example):**
    *   Go to `Bridge` -> `Ports`, click the `+`, select `bridge-22` and the desired interface from the drop-down list, and click OK. Repeat for each interface.
*   **Effect:** `ether2` and `ether3` become part of `bridge-22`, with the ability to forward frames with MAC server control.

### Step 3: Configure the MAC Server

*   **Purpose:** Enable and configure the MAC server for the bridge interface.
*   **CLI Commands (Before):**
    ```mikrotik
    /ip mac-server print
    ```
*   **GUI Instructions (Winbox):**
    *   Go to `IP` -> `MAC Server` to check the current settings.
*   **Action:** Enable the MAC server on the `bridge-22`.
*   **CLI Commands (After):**

    ```mikrotik
    /ip mac-server add interface=bridge-22
    /ip mac-server set discover=yes
    ```
*   **GUI Instructions (Winbox):**
    *   Go to `IP` -> `MAC Server` and click the `+` to create a new instance.
    *   Select `bridge-22` from the `Interface` dropdown and ensure `discover` is enabled.
*   **Effect:** MAC server is now active on the specified bridge. The `discover` option allows the router to add MAC addresses to the `/ip mac-server hosts` list as they are seen in Ethernet frames forwarded via `bridge-22`. This step *does not* immediately assign addresses.

### Step 4: Configure Static MAC Entries (Optional, but recommended)

*   **Purpose:** Associate MAC addresses to specific IP addresses and other options.
*  **CLI Commands (Before):**
    ```mikrotik
    /ip mac-server host print
    ```
*   **GUI Instructions (Winbox):**
    *   Go to `IP` -> `MAC Server` -> `Host` to check existing hosts.
*   **Action:** Add static entries to the MAC server host list.
*   **CLI Commands (After, example):**
    ```mikrotik
    /ip mac-server host add address=172.183.89.10 mac-address=AA:BB:CC:DD:EE:01 server=bridge-22
    /ip mac-server host add address=172.183.89.11 mac-address=AA:BB:CC:DD:EE:02 server=bridge-22
    ```
     *These commands map MAC addresses `AA:BB:CC:DD:EE:01` and `AA:BB:CC:DD:EE:02` to `172.183.89.10` and `172.183.89.11`, respectively.*
*   **GUI Instructions (Winbox, example):**
    *   Go to `IP` -> `MAC Server` -> `Host`, click the `+`.
    *   Add the `MAC Address` , the `Address`, and select `bridge-22` from `Server` drop-down, click OK. Repeat for each device.
*   **Effect:** Devices with the specified MAC addresses will always get assigned the given IP address, regardless of if they try to ask for DHCP.

### Step 5: (Optional) Configure DHCP Relay (If needed)

*   **Purpose:** Enable DHCP relay if you have a central DHCP server elsewhere on the network.
*   **Note:** This step is *not* required for basic MAC server functionality, but can be used with DHCP.
*   **Action:** Add the DHCP relay setup.
*   **CLI Commands (Example):**

     ```mikrotik
    /ip dhcp-relay add interface=bridge-22 dhcp-server=172.183.89.254
    ```
    *This assumes `172.183.89.254` is a different server providing DHCP.*

*   **GUI Instructions (Winbox, example):**
    *   Go to `IP` -> `DHCP Relay`, click the `+`.
    *   Select `bridge-22` from `Interface` drop-down, and enter `172.183.89.254` as the `DHCP Server`, click OK.
*   **Effect:** Clients will now get their DHCP leases from the server located at `172.183.89.254`, however, the MAC server host entries will still override any DHCP assignments.

## Complete Configuration Commands:

```mikrotik
# Create Bridge Interface
/interface bridge add name=bridge-22

# Add IP address to the bridge interface
/ip address add address=172.183.89.1/24 interface=bridge-22

# Add Interfaces to the bridge
/interface bridge port add bridge=bridge-22 interface=ether2
/interface bridge port add bridge=bridge-22 interface=ether3

# Create MAC server instance
/ip mac-server add interface=bridge-22

#Enable device discovery
/ip mac-server set discover=yes

# Add static MAC to IP mappings
/ip mac-server host add address=172.183.89.10 mac-address=AA:BB:CC:DD:EE:01 server=bridge-22
/ip mac-server host add address=172.183.89.11 mac-address=AA:BB:CC:DD:EE:02 server=bridge-22

# (Optional) Add DHCP relay settings
#/ip dhcp-relay add interface=bridge-22 dhcp-server=172.183.89.254

```

## Common Pitfalls and Solutions:

*   **Problem:**  MAC server doesn't assign IPs.
    *   **Solution:** Verify `discover` is enabled on `/ip mac-server`, that the MAC address is correct under `/ip mac-server host`, and that the devices are connected to an interface that is part of `bridge-22`. Check the host list using `/ip mac-server host print`.
*   **Problem:**  Devices get wrong IPs.
    *   **Solution:** Ensure no DHCP server is running in the same network or that DHCP relay is correctly configured to avoid conflict. Check for duplicate entries in `/ip mac-server host`. Remove the host entries, and then add them again.
*   **Problem:** High CPU usage due to many mac server hosts.
    *   **Solution:** Limit the number of static MAC entries or move the static mapping to the actual DHCP server (if used).
*    **Problem:** MAC server interfering with other devices.
    *    **Solution:** Review bridge configurations in `/interface bridge port` to make sure only the necessary devices are affected by the MAC server configuration.

## Verification and Testing Steps:

1.  **Connect a device:** Connect a device with MAC address `AA:BB:CC:DD:EE:01` to either `ether2` or `ether3`.
2.  **Check IP:** The device should get IP address `172.183.89.10`.
3.  **Ping:** Try pinging `172.183.89.10` from the MikroTik router or another device on the same network: `/ping 172.183.89.10`.
4.  **Check MAC Server Host list:** On the MikroTik router, use `/ip mac-server host print` to see if the device's MAC is listed correctly.
5.  **Torch:** Use `/tool torch interface=bridge-22` to monitor network traffic and ensure that traffic is passing and IP addresses are assigned.
6.  **Logging**: Use `/system logging action print` and `/system logging print` to monitor any related actions that may be logged.

## Related Features and Considerations:

*   **DHCP Server:** Instead of using static entries, you can set up a DHCP server on the same bridge interface, and the MAC server will take precedence if you have host entries configured.
*   **VLANs:** You can add multiple VLANs to the same bridge interface, giving you the ability to set up complex networking using VLAN IDs.
*   **Firewall:** Consider using firewall rules to further control the traffic within the `172.183.89.0/24` subnet.
*   **Address Lists:**  Use address lists in conjunction with MAC server configurations for more advanced traffic control or other rule-based behavior.

## MikroTik REST API Examples (if applicable):

While there is no specific direct API call to "MAC Server", you would need to use `interface/bridge`, `ip/mac-server`, and `ip/mac-server/host` for full control. Below are examples for the most relevant actions:

*   **Create a MAC Server instance:**

    ```
    Endpoint: /ip/mac-server
    Method: POST
    Payload (JSON):
    {
        "interface": "bridge-22"
    }
    Expected Response: (Success): HTTP 201 Created, includes id of the new instance.
    ```

    *   **Error Handling:**  If the interface does not exist, the API would return `HTTP 400 Bad Request` and a JSON error message.

*   **Set MAC Server discovery to true:**

    ```
    Endpoint: /ip/mac-server/0
    Method: PATCH
    Payload (JSON):
    {
         "discover": true
    }
    Expected Response: HTTP 200 OK
    ```
*   **Add a MAC Server host entry:**

    ```
     Endpoint: /ip/mac-server/host
     Method: POST
     Payload (JSON):
     {
        "address": "172.183.89.10",
         "mac-address": "AA:BB:CC:DD:EE:01",
        "server": "bridge-22"
    }
    Expected Response: (Success): HTTP 201 Created, includes id of the new entry.
    ```
*   **Delete a MAC Server host entry:**
    ```
     Endpoint: /ip/mac-server/host/0
     Method: DELETE
     Expected Response: (Success): HTTP 204 No Content
    ```
    *  **Error Handling:** If the resource was not found, an `HTTP 404 Not Found` would be returned.

*   **Example API Request for all IP MAC Server Hosts:**
    ```
    Endpoint: /ip/mac-server/host
    Method: GET
    Expected Response: (Success): HTTP 200 OK, a list of all configured hosts in JSON.
    ```
    * **Response Example:**
    ```json
    [
        {
            ".id":"*0",
            "address":"172.183.89.10",
            "mac-address":"AA:BB:CC:DD:EE:01",
             "server":"bridge-22"
         }
    ]
    ```

## Security Best Practices

*   **Limit Access:** Only allow network administrators to access the MAC server configuration to prevent accidental or malicious configuration changes.
*   **MAC Spoofing:** Be aware of MAC spoofing attacks. The MAC server provides IP addresses based on MAC and is vulnerable to MAC address forgery, especially in an insecure environment.
*   **Use with DHCP:** When used in conjunction with DHCP, ensure the DHCP server is correctly secured. For instance if using DHCP relay, make sure the DHCP server in another subnet is properly protected.
*   **Firewall:**  Use MikroTik's firewall to restrict traffic based on IP and MAC addresses.
*   **Logging:** Enable logging for MAC server related events to monitor any unusual activity.

## Self Critique and Improvements

This configuration is functional and provides a good start for a basic MAC server configuration, but the following improvements could be made:

*   **Dynamic Host Handling:**  It only handles pre-configured MAC addresses. Implementing an automated way to deal with new devices on the network could improve the setup, though there isn't an automated MAC server functionality in MikroTik.
*   **Detailed Error Handling:** Provide better error handling for various possible issues in the configuration.
*  **Scalability:** The current configuration can be difficult to manage if there are many different host entries. Consider other options if this scales to be too large.
*   **Real-world Example:** A more in-depth explanation of use cases, specific scenarios where this would be a great solution would benefit the documentation.

## Detailed Explanations of Topic

A MAC server in MikroTik RouterOS provides the ability to make IP address assignments based on the source MAC address of a received Ethernet frame. It functions by monitoring traffic on specified interfaces (usually bridge interfaces) and when a matching MAC address appears in the `/ip mac-server hosts` list, the device is given the corresponding IP. This is often used to assign static IPs to specific devices regardless of DHCP, or for controlling access based on MAC. The combination of `/ip mac-server`, `/ip mac-server host` provides a system that does not involve DHCP but works by inspecting Ethernet frames.

## Detailed Explanation of Trade-offs

*   **MAC Server vs. DHCP:**
    *   **MAC Server:** Provides consistent IP assignment based on MAC address without any dynamic lease, useful for devices that don't need DHCP or for forcing a specific IP address. Less dynamic, better for static setups.
    *   **DHCP:**  Assigns IP addresses dynamically based on lease times, more flexible for general use. DHCP also has address reservations based on MAC addresses, which can replace the MAC server's functions.
*   **Static vs. Dynamic MAC Server Entries:**
    *   **Static:** Ensures that the same device always gets the same IP, simplifies configuration, but requires manual entries.
    *   **Dynamic (via discover):** The router keeps a running list of discovered MAC addresses.  This is simpler but less secure, as any MAC may get an address if discovered.
*   **Using with DHCP Relay vs. DHCP Server**
    *   **DHCP Relay:** Pushes all DHCP requests to a central server, and uses the MAC server as a means of controlling which clients get what address.
    *   **DHCP Server:** Router serves as the DHCP server. This may cause conflicts if not correctly set up.
*   **Security:**
    *   **MAC Server Alone:** Easy to spoof due to the fact that it does not authenticate the device, only checks source MAC address.
    *   **MAC Server with DHCP:** More secure, as the DHCP Server assigns leases and the MAC server enforces a rule.

## Configuration for Specific RouterOS Versions:

This configuration is valid for RouterOS versions 6.48 and all versions in the 7.x series. The CLI commands are consistent across these versions. The Winbox GUI navigation may differ slightly between version 6.x and 7.x, but the overall functionality is identical. No special version-specific considerations are needed, unless the end-user is using a very old version (5.x or earlier), then upgrades are required.

This detailed document should provide a comprehensive and practical understanding of how to configure a MAC server on your MikroTik RouterOS device within a SOHO network. Let me know if you need clarification on anything or have another topic to explore!
