Okay, let's dive into a detailed technical document focusing on RoMON (Router Management Overlay Network) in MikroTik RouterOS 6.48 (compatible with 7.x), using a practical SOHO scenario with VLAN interface `vlan-26` on the subnet 135.21.162.0/24.

## Scenario Description:

We have a SOHO network where we want to remotely manage a MikroTik router located on VLAN 26 (135.21.162.0/24). RoMON allows us to access this router's management interface (Winbox, SSH, WebFig) even if it's behind firewalls or doesn't have a direct public IP address.  RoMON will provide a secure and reliable method for managing our router remotely, without relying on direct IP connectivity to the management interface. This is particularly useful for routers in less accessible locations.

## Implementation Steps:

Here's a step-by-step guide, explaining each action and its effect. We will assume a "main" router with direct internet access (which will act as our RoMON agent/relay) and a "remote" router on vlan-26.

### Step 1: Initial Setup on the "Remote" Router (On vlan-26 - 135.21.162.0/24)

*   **Action:** Enable RoMON and set a RoMON ID. This enables the RoMON service and establishes a basic identity for the remote router within the RoMON network.

*   **Before Configuration:** We have an existing VLAN interface `vlan-26` and the remote router is configured with a static IP address within the 135.21.162.0/24 subnet, using an unused IP.
    ```
    /interface vlan
    print
    # Flags: X - disabled, R - running
    #  0  R name="vlan-26" mtu=1500 vlan-id=26 interface=ether1 use-service-tag=no

    /ip address
    print
    # Flags: X - disabled, I - invalid, D - dynamic
    #  0    address=135.21.162.10/24 network=135.21.162.0 interface=vlan-26
    ```

*   **MikroTik CLI Configuration:**
    ```mikrotik
    /tool romon
    set enabled=yes id=remote-router
    ```
*   **Winbox GUI Configuration:**
    1. Navigate to `Tools` > `RoMON`
    2. Check the `Enabled` checkbox.
    3. Set the `ID` to `remote-router`.
    4. Click `Apply`.
*   **Explanation:**
    *   `enabled=yes`: Activates the RoMON service on the router.
    *   `id=remote-router`: Assigns a unique identifier for this router within the RoMON network. This ID is used to identify this router when viewed through the Romon client interface on the "main" router.
*  **After Configuration:**
    ```
    /tool romon
    print
    enabled: yes
    id: remote-router
    key: ""
    ```
    RoMON is now active on the remote router, but is not yet visible in the management interface since no other routers are connected via RoMON.

### Step 2: Initial Setup on the "Main" Router (The RoMON Agent/Relay)

*  **Action:** Enable RoMON and set a RoMON ID. The Main router needs to run the RoMON service as well, and it needs to have a unique ID for itself.
*   **Before Configuration:** We assume a standard router setup, and we are using the internet facing interface on this device, so there are no specific configurations for this part of the setup, prior to making these changes.
*   **MikroTik CLI Configuration:**
    ```mikrotik
    /tool romon
    set enabled=yes id=main-router
    ```
*   **Winbox GUI Configuration:**
    1. Navigate to `Tools` > `RoMON`
    2. Check the `Enabled` checkbox.
    3. Set the `ID` to `main-router`.
    4. Click `Apply`.
*   **Explanation:**
    *   `enabled=yes`: Enables the RoMON service on the "main" router.
    *   `id=main-router`: Assigns the identifier "main-router" for this router within the RoMON network.
*   **After Configuration:**
     ```
     /tool romon
     print
     enabled: yes
     id: main-router
     key: ""
    ```
    RoMON is now active on the main router, however no other routers are currently visible in the management interface, since no direct connections have been configured.

### Step 3: Establishing a Layer-2 RoMON Connection

*   **Action:** We need to connect our routers at Layer 2 so RoMON can discover and connect to the Remote Router. For testing, we will be connecting the routers physically using Ethernet, but any layer-2 transparent media would work such as VLANs, or MPLS etc. We will assume that the Main Router is connected to the same broadcast domain of VLAN 26 via an ethernet connection, using the `ether1` interface.
*   **Before Configuration:** The physical ethernet connections are completed and we know `ether1` on the "main" router is in the same layer-2 domain as `vlan-26` on the remote router.
*   **MikroTik CLI Configuration:** No direct commands required, as this is an external configuration
*   **Winbox GUI Configuration:** No direct GUI configurations required.
*   **Explanation:** RoMON will now be able to send discovery and connection request between the two routers. RoMON uses layer-2 multicast discovery over all active interfaces.
*  **After Configuration:**
     The connection is now active and can be monitored from the "main" router in the RoMON neighbors section of `tools/romon`.

### Step 4: Monitoring RoMON Peers on the "Main" Router

*   **Action:** Check the RoMON neighbors on the "Main" Router to see the connection to the "Remote" Router.

*   **Before Configuration:** The connection is active, and the devices are connected at layer 2.

*   **MikroTik CLI Configuration:**
    ```mikrotik
    /tool romon neighbours print
    ```

*   **Winbox GUI Configuration:**
    1.  Navigate to `Tools` > `RoMON` > `Neighbours` tab.
*  **Explanation**
    The `Neighbours` tab, or `neighbours print` command in the CLI, shows the connected RoMON devices.
*   **After Configuration:** (Example Output)
    ```
    /tool romon neighbours print
    Columns: ID, MAC-ADDRESS, DISTANCE, INTERFACE, VERSION
    #   ID              MAC-ADDRESS        DISTANCE  INTERFACE   VERSION
    0   remote-router  C8:4A:98:XX:XX:XX          1   ether1     6.48
    ```
  We can see that the "remote-router" is discovered and accessible through RoMON, with an interface name that is used as part of the connection. In this case, it's 'ether1'. This interface needs to be connected to the same broadcast domain as 'vlan-26' on the remote router.

### Step 5: Connecting to the "Remote" Router using RoMON

*   **Action:** Connect to the "Remote" Router using the RoMON discovery feature.

*   **Before Configuration:** We have a successful RoMON neighbor discovery.

*  **MikroTik CLI Configuration:** No direct CLI command is needed for the connection, instead, we access the remote router via mac-address in a Winbox session.

*   **Winbox GUI Configuration:**
    1. Open Winbox.
    2. In the "Connect To" field, enter the MAC address of the `remote-router` (from the RoMON neighbor output). Make sure the 'Connect To RoMON' checkbox is checked.
    3. Enter the username and password for the `remote-router`.
    4. Click `Connect`.

*  **Explanation**
  Winbox can make connections to discovered RoMON neighbors directly through their MAC address via RoMON. This allows for managing devices behind firewalls or without public IPs, as long as the devices have a valid layer-2 connection.

*  **After Configuration**
  We now have an active Winbox session with the remote router on VLAN 26, using the layer-2 connection established by the RoMON network.

## Complete Configuration Commands:

Here's the complete set of commands for both the "remote" and "main" routers.

**"Remote Router" (on 135.21.162.0/24):**

```mikrotik
/tool romon
set enabled=yes id=remote-router
/interface vlan
add name=vlan-26 vlan-id=26 interface=ether1
/ip address
add address=135.21.162.10/24 interface=vlan-26
```

**"Main Router":**

```mikrotik
/tool romon
set enabled=yes id=main-router
```

## Common Pitfalls and Solutions:

*   **RoMON is not discovering neighbors:**
    *   **Problem:** Layer-2 connectivity is not working between interfaces (firewalls, misconfigured VLANs or port configuration).
    *   **Solution:** Verify physical connections, VLAN configurations and interface settings. Use the `/interface ethernet monitor ether1` command, or it's Winbox equivalent, to check the connection for ethernet issues, or `/interface vlan monitor vlan-26`, for VLAN issues.
*   **Incorrect RoMON ID:**
    *   **Problem:** RoMON IDs must be unique. If routers have the same ID, they may fail to connect properly.
    *   **Solution:** Verify and change IDs using `/tool romon set id=unique-id`.
*  **RoMON interface not in the broadcast domain:**
    *  **Problem:**  RoMON will try and establish links on all active interfaces. If the remote router's interface is on a VLAN, the main router must have an interface on the same broadcast domain to discover it.
    *  **Solution:** Ensure that both devices are connected at layer-2. This may require additional interface configuration, VLAN configuration or bridging between interfaces.
*   **RoMON connection is unstable:**
    *   **Problem:**  The Layer-2 connection between RoMON devices might be unstable.
    *   **Solution:** Monitor your Layer-2 infrastructure, check for spanning-tree loops, and packet loss/corruption. Use the monitor tool to test interfaces and physical layer health.

## Verification and Testing Steps:

1.  **Verify RoMON Neighbors on "Main Router":**
    *   Execute `/tool romon neighbours print` on the "Main Router" and confirm that "remote-router" is listed and shows the correct interface, MAC Address and distance.
2.  **Connect to the "Remote Router" using Winbox:**
    *   Use Winbox to connect via MAC address, ensuring the "Connect To RoMON" checkbox is selected.

## Related Features and Considerations:

*   **RoMON Key:** You can add a key for additional security using `/tool romon set key=your_secret_key`. This prevents unauthorized access to RoMON networks.
    * **Trade-off:** Adding a key increases security, but all Routers on the RoMON network must use the same key.
*   **RoMON Over VPN:** RoMON can also function over VPN tunnels if layer-2 transparency is maintained, for devices across routed networks.
*   **RoMON Over MPLS:** RoMON is a layer-2 discovery protocol, and as such, can function over MPLS circuits, to remote networks without the use of a VPN.

## MikroTik REST API Examples (if applicable):

While direct API access to establish RoMON connections is not available, you can use the API to get RoMON neighbor information and check the status:

**Retrieve RoMON Neighbors:**

*   **API Endpoint:** `/tool/romon/neighbour`
*   **Request Method:** GET
*   **Example Request (using curl):**

    ```bash
    curl -k -u "api_user:api_password" -H "Content-Type: application/json" \
        https://your_main_router_ip/rest/tool/romon/neighbour
    ```

*   **Example Response:**

    ```json
    [
      {
        "id": "remote-router",
        "mac-address": "C8:4A:98:XX:XX:XX",
        "distance": "1",
        "interface": "ether1",
        "version": "6.48"
      }
    ]
    ```

**Set RoMON Key:**

*   **API Endpoint:** `/tool/romon`
*   **Request Method:** PUT
*   **Example Request (using curl):**

    ```bash
    curl -k -u "api_user:api_password" -H "Content-Type: application/json" \
        -X PUT -d '{"key": "your_secret_key"}' \
        https://your_main_router_ip/rest/tool/romon
    ```
*   **Explanation:** This will set the key parameter of the global `/tool/romon` configuration, which will be used for authentication.
*   **Example Response:**

    ```json
        {
        "enabled": true,
        "id": "main-router",
        "key": "your_secret_key"
    }
    ```
*   **Error Handling:**
   *   API calls can return HTTP status codes indicating success or failure. 200 for success, 401 for unauthorized access and 400 or 500 for internal errors.

## Security Best Practices:

*   **RoMON Key:**  Always set a strong RoMON key.
*   **Access Control:**  Use user access control to restrict who can access RoMON-enabled routers via the API.
*   **Secure API Access:** Use HTTPS for API access, as well as secure credentials, never expose your Router API to the internet.

## Self Critique and Improvements:

*   **Complexity:**  This setup is relatively simple but can become complex with larger networks and multiple RoMON agents, requiring careful planning for routing.
*   **Scalability:** While RoMON can support large networks, it is primarily a layer-2 protocol, and might not be the best choice for connecting via the internet directly.
*   **Improvement:** This documentation could be improved by providing more detailed information about troubleshooting tools (such as torch and packet sniffing), for more in-depth diagnostics.
*   **Automation:** We could improve this configuration by providing API examples to automate the RoMON setup on larger networks.

## Detailed Explanations of Topic:

**RoMON (Router Management Overlay Network):** RoMON is a MikroTik proprietary layer-2 management protocol. It allows Winbox, WebFig, and SSH connections to a router to be tunneled over layer-2 networks. This is useful when a router doesn't have a direct IP connection, is behind NAT, or is behind a firewall. RoMON uses a low-overhead protocol that sends discovery and management requests on all active interfaces that are able to receive broadcasts. The RoMON agent routers can then be used to connect to the remote devices over their layer-2 connection.

## Detailed Explanation of Trade-offs:

*   **RoMON vs. Direct IP:** Direct IP connectivity requires public IPs, port forwarding, and potentially firewall configuration. RoMON does not need this as long as there is a path between Routers at layer-2.
*   **RoMON vs. VPN:** VPNs provide layer-3 connectivity, while RoMON is layer-2, however VPNs often require more complex setup and resource consumption. VPNs are more secure than RoMON if using a secure protocol, but RoMON is simpler for quick connections in situations where layer-2 connectivity can be provided.
*   **RoMON Security:** RoMON by itself is a low-overhead protocol, and does not provide the levels of security of a VPN. It's recommended to implement a RoMON Key to increase security.

## Configuration for Specific RouterOS Versions:

The configuration in this document is applicable for RouterOS 6.48, as well as newer 7.x versions. The RoMON commands and functionalities remain largely the same between versions. The output format, command options, or available parameters in the CLI could change between versions.
