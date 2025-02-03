Okay, let's delve into a detailed RoMON configuration for a MikroTik point-to-point link, focusing on practical implementation, troubleshooting, and security within the context of RouterOS v6.48 and v7.x.

## Scenario Description:

We have two MikroTik routers forming a point-to-point link across the 220.87.68.0/24 subnet.  We want to utilize RoMON to remotely manage and monitor both devices, even if the IP connectivity is compromised, or during initial setup. This ensures we have a reliable management channel, separate from the main data traffic. We will create a VLAN named 'vlan-25' on both routers and enable RoMON on this interface.

**Configuration Level:** Advanced

**Network Scale:** Point-to-Point Link

**Subnet:** 220.87.68.0/24

**Interface Name:** vlan-25

## Detailed Explanation of RoMON:

RoMON (Router Management Overlay Network) is a MikroTik-specific protocol that enables Layer 2-based device discovery and management, even if IP connectivity is lost or misconfigured. It operates independently of the IP layer by using a small set of special Ethernet frames. In essence, RoMON allows you to discover and connect to neighboring MikroTik devices that are also running RoMON on the same Ethernet segments or VLANs. This is helpful for out-of-band management, especially in situations where you don't have IP reachability.

**How it Works**

*   **Discovery:** RoMON-enabled devices send out discovery packets. These packets are not routed.
*   **Connection:** When you select a device found through RoMON, your client (like WinBox) establishes a Layer 2 connection.
*   **Management:** Once connected, you can manage the remote device just as if you were directly connected via IP.

**Key Features**

*   **Out-of-Band Management:** Essential when IP connectivity is unavailable.
*   **Layer 2 Operation:** Independent of the IP configuration.
*   **Secure:** Utilizes a secret key for RoMON peer authentication.

## Implementation Steps:

Here's a step-by-step guide, assuming you are configuring Router 1 first, and then Router 2.

**Router 1:**
*(Before configuration, all interfaces on the router are in a default state.)*

1.  **Step 1: Create VLAN Interface:**

    *   **Description:** We create a VLAN interface `vlan-25` on the Ethernet interface which physically connects to the peer router.  We use `ether1` as the example interface. Replace with your physical interface accordingly.
    *   **Why:** VLANs provide logical separation.
    *   **CLI Instructions:**

        ```mikrotik
        /interface vlan
        add name=vlan-25 vlan-id=25 interface=ether1
        ```
    *   **Winbox GUI:** Go to `Interface -> + -> VLAN`. Set `Name` to `vlan-25`, `VLAN ID` to `25` and select the appropriate interface, such as `ether1`.
    *   **Effect:**  A logical VLAN interface named `vlan-25` is created on `ether1`.
        
    *  **CLI Output (after step):**
        ```
        /interface vlan print
        Flags: X - disabled, R - running
         0    name="vlan-25" mtu=1500 l2mtu=1598 mac-address=00:00:00:00:00:00 vlan-id=25 interface=ether1
         ```


2.  **Step 2: Enable RoMON on VLAN Interface:**

    *   **Description:** Now we enable RoMON specifically on the newly created `vlan-25` interface. We also set a RoMON password, which will be used to allow authentication between peers and management clients.
    *   **Why:** This step enables RoMON on the VLAN where our management traffic will travel. This will be used for managing the remote device.
    *   **CLI Instructions:**
    
        ```mikrotik
        /tool romon
        set enabled=yes interfaces=vlan-25 secret="myromonsecret"
        ```
        
    *   **Winbox GUI:**  Go to `Tools -> RoMON`. Check `Enabled`, and then select `vlan-25` under `Interfaces`. Enter the desired `Secret`.
    *   **Effect:** RoMON is activated and listening on `vlan-25`. RoMON will not operate without a secret key.

    * **CLI Output (after step):**
        ```
        /tool romon print
        enabled: yes
        interfaces: vlan-25
        secret: "myromonsecret"
        router-id: 00:00:00:00:00:00
        ```

3.  **Step 3: (Optional) Configure IP Address on VLAN interface**

    *   **Description:** Though RoMON does not require an IP address, it is useful for testing your physical setup with regular networking tools. Set an IP address on the VLAN interface so you can test connectivity.
    *   **Why:** An IP is used for testing. The IP layer is not used by RoMON.
    *   **CLI Instructions:**

        ```mikrotik
        /ip address
        add address=220.87.68.1/24 interface=vlan-25
        ```
    *   **Winbox GUI:**  Go to `IP -> Addresses`. Click `+`. Set `Address` to `220.87.68.1/24` and `Interface` to `vlan-25`.

    *   **Effect:**  Router 1 now has IP address on vlan-25.
   
    * **CLI Output (after step):**
        ```
         /ip address print
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   220.87.68.1/24     220.87.68.0      vlan-25
        ```

**Router 2:**
*(Before configuration, all interfaces on the router are in a default state.)*

1.  **Step 4: Create VLAN Interface (Router 2):**

    *   **Description:** Just like on Router 1, we create a VLAN interface with matching settings.
    *   **Why:** Both routers need a matching VLAN to exchange RoMON packets.
    *   **CLI Instructions:**
        ```mikrotik
        /interface vlan
        add name=vlan-25 vlan-id=25 interface=ether1
        ```

    *   **Winbox GUI:**  Go to `Interface -> + -> VLAN`. Set `Name` to `vlan-25`, `VLAN ID` to `25` and select the appropriate interface, such as `ether1`.

    *   **Effect:**  A logical VLAN interface named `vlan-25` is created on `ether1` on Router 2.

     *  **CLI Output (after step):**
        ```
        /interface vlan print
        Flags: X - disabled, R - running
         0    name="vlan-25" mtu=1500 l2mtu=1598 mac-address=00:00:00:00:00:00 vlan-id=25 interface=ether1
         ```

2.  **Step 5: Enable RoMON on VLAN Interface (Router 2):**

    *   **Description:** We also enable RoMON on the `vlan-25` interface and use the *same* secret key as Router 1.
    *   **Why:** RoMON peers must share the same secret for authentication.
    *   **CLI Instructions:**
        ```mikrotik
        /tool romon
        set enabled=yes interfaces=vlan-25 secret="myromonsecret"
        ```
    *   **Winbox GUI:** Go to `Tools -> RoMON`. Check `Enabled`, and then select `vlan-25` under `Interfaces`. Enter the *same* `Secret` you used on Router 1, "myromonsecret".

    *   **Effect:** RoMON is active on Router 2.

    * **CLI Output (after step):**
        ```
        /tool romon print
        enabled: yes
        interfaces: vlan-25
        secret: "myromonsecret"
        router-id: 00:00:00:00:00:00
        ```

3.  **Step 6: (Optional) Configure IP Address on VLAN Interface (Router 2)**

    *   **Description:** Just like Router 1, we set an IP on the VLAN for testing the link
    *   **Why:** An IP is used for testing. The IP layer is not used by RoMON.
    *   **CLI Instructions:**
    
         ```mikrotik
          /ip address
          add address=220.87.68.2/24 interface=vlan-25
         ```

    *   **Winbox GUI:**  Go to `IP -> Addresses`. Click `+`. Set `Address` to `220.87.68.2/24` and `Interface` to `vlan-25`.
    
    *   **Effect:** Router 2 now has an IP on VLAN 25.

    * **CLI Output (after step):**
        ```
         /ip address print
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   220.87.68.2/24     220.87.68.0      vlan-25
        ```

## Complete Configuration Commands:

**Router 1:**

```mikrotik
/interface vlan
add name=vlan-25 vlan-id=25 interface=ether1

/tool romon
set enabled=yes interfaces=vlan-25 secret="myromonsecret"

/ip address
add address=220.87.68.1/24 interface=vlan-25
```

**Router 2:**
```mikrotik
/interface vlan
add name=vlan-25 vlan-id=25 interface=ether1

/tool romon
set enabled=yes interfaces=vlan-25 secret="myromonsecret"

/ip address
add address=220.87.68.2/24 interface=vlan-25
```

## Common Pitfalls and Solutions:

*   **Secret Mismatch:**
    *   **Problem:** If the `secret` is different on each router, RoMON will not work.
    *   **Solution:** Ensure the secret is identical on both routers. Double check for leading or trailing spaces.
*   **Incorrect VLAN ID:**
    *   **Problem:** If the `vlan-id` is different on each router or different from the VLAN configured on the switch, RoMON packets will not reach each device.
    *   **Solution:** Ensure that the VLAN ID is the same on both routers and matching on any intermediate switches
*   **Interface Issues:**
    *   **Problem:** The interface on which you enable the VLAN may not be correctly configured. For example, it might be disabled.
    *   **Solution:** Verify the interface is up, is not an bridge port, and has physical connectivity (e.g., the cable is connected).
*   **RoMON not enabled**
    *   **Problem:**  RoMON is not enabled.
    *   **Solution:** Use the following command:
        ```mikrotik
        /tool romon
        set enabled=yes
        ```
* **Firewall Interference**
   *   **Problem:** If a firewall is set up incorrectly, this can interfere with connectivity, particularly the optional IP on the interface.
   *   **Solution:** If using a firewall ensure that communication on the interface is permitted.
*   **Resource Issues:**
    *   **Problem:** RoMON uses very few resources. However, if you are experiencing very high CPU or memory usage, other issues should be investigated first.
    *   **Solution:** Use `/system resource print` to verify the status of the router.

## Verification and Testing Steps:

1.  **IP Connectivity Test (optional):**
    *   Use `ping 220.87.68.2` on Router 1, and `ping 220.87.68.1` on Router 2.  If this works then the Layer 3 is working as expected. If it does *not* work, this can help narrow down the problem to be physical and/or VLAN connectivity related.
2.  **RoMON Discovery:**
    *   **Winbox:** In Winbox, click "Neighbors" (you may have to disable IP neighbors by going to `IP` -> `Neighbors` and unchecking `Enable`).  With RoMON correctly configured, you should see the remote router appear in the list, with a `RoMON` type. You should be able to connect to it using its MAC address.
    *  **CLI** In the CLI, type `/tool romon print neighbors`. This command will list the RoMON neighbors. It should show the other device.
3.  **RoMON Connection:**
    *   **Winbox:** Select the RoMON neighbor and connect with its RoMON MAC address. If the link is established then the remote router's login window will appear. Log in.
    *   **CLI:** There is no direct CLI method to connect via RoMON to a device. This is primarily a Winbox and API tool.
4.  **Torch:**
    *   **Description:**  Use torch to verify RoMON packets are being sent and received on your desired interface.
    *   **CLI Instructions:**
        ```mikrotik
        /tool torch interface=vlan-25 protocol=romon
        ```
    *   **Winbox GUI:** Go to `Tools` -> `Torch` and set the interface to `vlan-25` with protocol `romon`.

## Related Features and Considerations:

*   **Multiple RoMON interfaces:**  You can enable RoMON on multiple interfaces for more flexible reachability.
*   **Link Aggregation:** RoMON can also function through bonded interfaces.
*  **RoMON on wireless links:** RoMON is able to be used over wireless links with a few caveats. Ensure proper VLAN configurations.
*  **RoMON and Router ID:**  Each RoMON enabled interface generates a Router ID which uniquely identifies the device and interface, by its MAC address. This can aid with device identification on busy networks.

## MikroTik REST API Examples:

Here's how you could enable RoMON using the API.

**Enable RoMON with Secret:**
* **Endpoint:** `/tool/romon`
* **Method:** PUT

* **Example JSON Payload:**
```json
{
 "enabled": true,
 "interfaces": "vlan-25",
 "secret": "myromonsecret"
}
```

* **Expected Response (200 OK):**

```json
{
    ".id": "*57",
    "enabled": "true",
    "interfaces": "vlan-25",
    "secret": "myromonsecret",
    "router-id": "00:00:00:00:00:00"
}
```
**Error Handling:**
If there is a error in the API call, the system will return a 4XX error. Check that the body of the message is in the correct format, and that all parameters are valid. The format for the body response will be specific to the REST API implementation, but will usually include an error message.

**Get RoMON Status:**
* **Endpoint:** `/tool/romon`
* **Method:** GET

* **Expected Response (200 OK):**
```json
[
    {
        ".id": "*57",
        "enabled": "true",
        "interfaces": "vlan-25",
        "secret": "myromonsecret",
        "router-id": "00:00:00:00:00:00"
    }
]
```
**Error Handling:**
If there is a error in the API call, the system will return a 4XX error. Check that the body of the message is in the correct format, and that all parameters are valid. The format for the body response will be specific to the REST API implementation, but will usually include an error message.

**Important Note on API:** The `.` symbol is used when an id is provided.

## Security Best Practices

*   **Strong RoMON Secret:** Always use a strong, randomly generated secret for RoMON. Change this secret regularly.
*   **Limited RoMON Interfaces:** Only enable RoMON on interfaces needed for management.
*   **Isolate VLANs:** Segregate RoMON traffic into its own VLAN.
*   **Monitor RoMON traffic:** Keep an eye on any unexpected RoMON activity.

## Self Critique and Improvements

*   **Complexity:** The current setup is very basic and addresses a very specific use case of a Point-to-Point Link. There is an assumption here that no additional switches exist between the two MikroTik routers, as no information was provided. The configuration of a switch could be included, showing how to configure the correct VLAN tagging and how this impacts RoMON operations.
*   **Dynamic VLAN assignment:** VLANs were statically assigned, it would be valuable to see an example of how this would work with dynamic VLAN assignment on an ethernet switch.
*  **Alternative configuration:**  Instead of using VLANs, we could demonstrate RoMON usage on regular ethernet ports. This may be more appropriate for testing.
*   **Alternative protocols:**  It might be helpful to contrast RoMON with other remote management protocols, like SSH, and show the relative benefits of both approaches.
*   **Advanced Monitoring:**  We could include more advanced RoMON monitoring, using scripts or third-party software to keep better track of device health, and report on any errors.

## Detailed Explanation of Trade-offs:

*   **Layer 2 vs. Layer 3 management:** RoMON is Layer 2 and more reliable in situations where IP configuration is problematic. SSH, which is Layer 3, relies on a functional IP config.
*   **VLANs vs. no VLANs:** Using VLANs creates segregation, but adds complexity, particularly on a larger network with multiple switches. RoMON over regular ethernet simplifies the setup but can create management conflicts on larger networks.
*   **Security vs. Convenience:**  A strong password provides good security, but is more difficult to manage. Using a simple default password makes the system far more convenient, at the cost of a huge security vulnerability. It is generally best practice to use a complex and randomly generated password.

## Configuration for Specific RouterOS Versions:

This configuration works on both RouterOS v6.48 and v7.x. No commands used are specific to one version or another.
All commands used in the script above are compatible with MikroTik RouterOS v6.48 and v7.x.  The functionality of RoMON has not changed significantly between these versions. However the command output may vary slightly.
For example, in v7.x the `tool romon` interface will have additional options, such as `rx-bytes`, `tx-bytes` and `last-seen`. These values are useful for debugging.

This detailed documentation provides a practical, secure, and reliable method to implement RoMON for a MikroTik point-to-point link scenario. It covers configuration, troubleshooting, API access, and security best practices, all geared towards a real-world MikroTik environment.
