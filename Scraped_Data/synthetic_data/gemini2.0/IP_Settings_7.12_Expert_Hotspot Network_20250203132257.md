Okay, let's dive into a detailed expert-level configuration for IP settings on a MikroTik RouterOS device, specifically targeting a VLAN interface within a Hotspot network, focusing on practical, real-world implementation.

## Scenario Description:

We are configuring a MikroTik router, running RouterOS 7.12, to provide network connectivity for a Hotspot network.  The specific focus is on the `vlan-90` interface. This interface is associated with VLAN 90 on the router and will use the IP subnet `99.236.13.0/24`.  We aim for a robust, well-documented setup suitable for a service provider-level deployment.

**Target:** RouterOS 7.12 (compatible with 6.48, and later 7.x versions)
**Configuration Level:** Expert
**Network Scale:** Hotspot Network (SOHO, SMB, Enterprise, ISP, Hotspot Network, Point-to-Point Link)
**Subnet:** 99.236.13.0/24
**Interface Name:** vlan-90

## Implementation Steps:

Here’s a detailed step-by-step guide, with explanations and commands:

### 1. **Step 1: Create the VLAN Interface**

**Goal:** Before we can assign an IP address, we need to create the VLAN interface.
**Why:** The VLAN interface creates a logical division within a physical interface to provide VLAN tagging and routing.

**Before Configuration:**  Let's assume you have a physical interface, for example, `ether1` (this interface should be chosen based on your physical network topology).

**CLI Command:**
```mikrotik
/interface vlan
add name=vlan-90 vlan-id=90 interface=ether1
```
**Explanation:**
* `/interface vlan add`:  Creates a new VLAN interface.
* `name=vlan-90`:  Assigns the name 'vlan-90' to the interface.
* `vlan-id=90`: Sets the VLAN tag ID to 90.
* `interface=ether1`: Specifies the physical interface on which this VLAN will operate (replace `ether1` with the correct physical interface).

**Winbox GUI Equivalent:**
1. Go to *Interface*.
2. Click the "+" button, and select *VLAN*.
3. Enter: *Name*: `vlan-90`, *VLAN ID*: 90, *Interface*: `ether1`
4. Click *OK*.

**After Configuration:** A new interface `vlan-90` will appear in `/interface print` (CLI) or the Interface list in Winbox, but will initially be in a non-active state.

### 2. **Step 2: Assign the IP Address**

**Goal:** Set the IP address on the `vlan-90` interface.
**Why:**  This is required for the interface to participate in IP networking.

**Before Configuration:** `vlan-90` interface exists, but has no IP address assigned.

**CLI Command:**
```mikrotik
/ip address
add address=99.236.13.1/24 interface=vlan-90
```
**Explanation:**
* `/ip address add`: Adds a new IP address configuration.
* `address=99.236.13.1/24`: Specifies the IP address and subnet mask for the interface.
* `interface=vlan-90`: Specifies which interface the IP address will be assigned to.

**Winbox GUI Equivalent:**
1. Go to *IP* > *Addresses*.
2. Click the "+" button.
3. Enter: *Address*: `99.236.13.1/24`, *Interface*: `vlan-90`.
4. Click *OK*.

**After Configuration:** The `vlan-90` interface now has the IP address `99.236.13.1/24` assigned to it and will become active once the physical interface on which it's created has been enabled (enabled by default).

### 3. **Step 3: Enable the Interface**

**Goal:** Activate the `vlan-90` interface.
**Why:**  A newly created interface is not active by default. This step ensures that it can participate in network communication.

**Before Configuration:**  The interface `vlan-90` is up and has an IP Address, but if the underlying physical interface was not active, `vlan-90` would not be active.

**CLI Command**
This is done as a sanity check, as usually physical interfaces are enabled by default:
```mikrotik
/interface enable ether1
```

**Winbox GUI Equivalent**
1. Go to *Interface*
2. Locate the `ether1` (or the physical interface used for the vlan)
3. Select the interface and make sure that the Enabled column has a checkmark

**After Configuration:** The interface `vlan-90` is now active and can pass traffic according to its IP configuration, assuming the physical interface is active.

## Complete Configuration Commands:
```mikrotik
/interface vlan
add name=vlan-90 vlan-id=90 interface=ether1

/ip address
add address=99.236.13.1/24 interface=vlan-90

/interface enable ether1
```
**Parameter Explanation:**
| Command         | Parameter           | Description                                                                         |
|-----------------|---------------------|------------------------------------------------------------------------------------|
| `/interface vlan add` | `name` |  The name of the VLAN interface (e.g., `vlan-90`).                     |
| `/interface vlan add` | `vlan-id`        |  The VLAN tag ID (e.g., `90`).                                                  |
| `/interface vlan add` | `interface`      |  The physical interface this VLAN is associated with (e.g., `ether1`).             |
| `/ip address add`   | `address`         |  The IP address and subnet mask to assign to the interface (e.g., `99.236.13.1/24`).|
| `/ip address add`   | `interface`       |  The interface to assign the IP address to (e.g., `vlan-90`).                    |
| `/interface enable`   | `name`         | The physical interface to enable. Usually this is `ether1` or the interface in which the vlan was created (e.g., `ether1`)                   |

## Common Pitfalls and Solutions:

*   **Incorrect VLAN ID:** If the VLAN ID on the MikroTik doesn't match the VLAN ID on your switch, no traffic will pass through.
    *   **Solution:** Double-check the VLAN ID configuration on both devices.
*   **Incorrect Physical Interface:** You need to use the correct physical interface on which to create the VLAN, otherwise you won't be able to tag traffic.
    *   **Solution:** Verify that the VLAN is attached to the correct physical interface in the `/interface vlan` configuration.
*   **Subnet Mask Issues:** Incorrect subnet mask can cause routing problems.
    *   **Solution:** Ensure the subnet mask (/24 in this case) matches the intended network size.
*   **Firewall Rules:** Firewall rules might be blocking traffic on the interface.
    *   **Solution:**  Check the `/ip firewall filter` rules, ensuring that traffic for the `vlan-90` interface is not blocked unnecessarily.
*  **Underlying interface is down** If the underlying interface, in this case `ether1`, is disabled, the VLAN `vlan-90` will also be down.
    * **Solution** Ensure that the underlying physical interface `ether1` is enabled.
*  **Incorrect gateway is set in client devices** If client devices do not have the correct gateway set, their traffic will not reach the MikroTik router
    * **Solution** Ensure that the client devices use `99.236.13.1` as the gateway to reach the router.

## Verification and Testing Steps:
1.  **Ping Test:**  Ping the IP address assigned to the VLAN interface from the router itself.

    ```mikrotik
    /ping 99.236.13.1
    ```
    Expected Result: Should have a 100% success rate if the IP address has been set correctly and the interface is up.
2.  **Ping from another device** Try to ping `99.236.13.1` from a different computer connected to the vlan.
    *   Expected Result: Success.

3.  **Interface Status Check:** Check the status of the interface.
    ```mikrotik
    /interface print
    ```
     Expected result: The status of `vlan-90` should be `running`.

4.  **IP Address Print:** Check the IP addresses assigned to interfaces.
    ```mikrotik
    /ip address print
    ```
    Expected Result:  The `99.236.13.1/24` IP address should be listed with the associated `vlan-90` interface.

5.  **Torch Tool:** Use the `torch` tool to analyze traffic on the interface.

    ```mikrotik
    /tool torch interface=vlan-90
    ```
    Expected Result:  You should see the traffic going over the `vlan-90` interface (e.g., ping requests).

## Related Features and Considerations:

*   **DHCP Server:** You would likely want to set up a DHCP server on `vlan-90` to assign IP addresses automatically to devices in the subnet.
*   **Firewall Rules:** Implement firewall rules to control what traffic can pass in/out of the `vlan-90` interface.
*   **NAT (Network Address Translation):** If the `vlan-90` network needs access to the internet through another interface, set up source NAT.
*   **Routing:** Depending on the network layout you may need to add specific routing rules.
*   **Hotspot Server:** Integrate `vlan-90` with MikroTik’s Hotspot functionality for user authentication and management.
*   **VRF (Virtual Routing and Forwarding):** If you have a complex network setup, VRF could isolate routes for specific VLANs.
*   **QoS:**  Implement Quality of Service (QoS) to prioritize traffic and control bandwidth on the `vlan-90` interface.

**Impact in real world:** This configuration is fundamental for network segmentation, allowing traffic isolation using VLANs. For example, you can keep your "guest" network isolated from your "internal" network, without having to use different hardware or routers.

## MikroTik REST API Examples:

Let's show an example on how to create the VLAN interface using the Mikrotik API:

**API Endpoint:** `/interface/vlan`

**Request Method:** `POST`

**Example JSON Payload:**
```json
{
    "name": "vlan-90",
    "vlan-id": 90,
    "interface": "ether1"
}
```
**Explanation of parameters in JSON Payload:**
| Parameter   | Description                                                                  |
|------------|------------------------------------------------------------------------------|
| `name`     | Name of the new VLAN interface.                                               |
| `vlan-id`  | VLAN tag to use.                                                            |
| `interface` | The physical interface the VLAN will be assigned to.                      |

**Expected Response (Success):**
```json
{
    ".id": "*E1337" // unique id of the created interface
}
```

**Error Response Example:**
```json
{
  "message": "already have such item",
  "error": true
}
```

This error response indicates that there is already a VLAN interface with the specified name, or using the specified parameters.

To add the IP address to the interface the following request can be used:

**API Endpoint:** `/ip/address`

**Request Method:** `POST`

**Example JSON Payload:**
```json
{
    "address": "99.236.13.1/24",
    "interface": "vlan-90"
}
```
**Explanation of parameters in JSON Payload:**
| Parameter   | Description                                                                  |
|------------|------------------------------------------------------------------------------|
| `address`     | The IP address and subnet to assign to the interface, in CIDR format.                                               |
| `interface`  | The interface where the IP address should be set.                                                          |

**Expected Response (Success):**
```json
{
    ".id": "*E1338" // unique id of the created address
}
```

**Error Response Example:**
```json
{
  "message": "invalid value for argument address: not an IP address",
  "error": true
}
```

This error response indicates that the given IP address is incorrect or not in CIDR format.

**Important Notes:**
*   Remember to handle potential errors returned from the API calls.
*   You'll need to properly set up authentication headers when making the requests to the MikroTik API.

## Security Best Practices

*   **Firewall rules:** Only allow traffic needed for the intended functionality of the Hotspot Network.
*  **Limit access to the router:** Don't expose the management interface to the public internet. Restrict access via firewall rules or a specific subnet.
*   **Regular updates:** Keep the router's RouterOS version updated with the latest security patches.
*   **Strong passwords:** Use strong, unique passwords for all router accounts.
*   **Disable unnecessary services:** Only enable necessary services like SSH or API. Disable Telnet if enabled.
*   **Audit logging:** Configure logging to identify potential security breaches.
*  **Use HTTPS for API** Always use the HTTPS protocol for API access to keep authentication data secure.
*  **Enable MAC Address Authentication** Implement MAC Address Authentication to improve the security when assigning ip addresses to devices.

## Self Critique and Improvements

This configuration is well-structured and covers the basic IP address assignment for a VLAN interface. However, here are some areas that could be improved or further modified:

*   **DHCP Server Configuration:** Adding details on DHCP server configuration would be valuable since this is a common requirement in a real-world Hotspot setup.
*   **Firewall Rule Examples:**  Include specific firewall rule examples to protect the network.
*   **QoS Configuration:**  Provide basic QoS examples to manage the traffic on `vlan-90`.
*   **Real-World Application:** Showing a more practical setup such as a guest network configuration, would enhance the overall implementation.
*   **More REST API Examples:** Add more examples such as retrieving interfaces or assigned IP addresses using the API.

## Detailed Explanations of Topic

**IP Settings:** In MikroTik RouterOS, IP settings control how the router handles network addresses. This involves configuration of IP addresses, subnet masks, routing tables, and interfaces. IP addressing is a core part of any network, and in MikroTik, this is handled via the `/ip address` menu. Proper IP configuration enables communication between devices in the network, as well as with external networks such as the Internet. VLAN interfaces, such as the `vlan-90` in this scenario, are logical entities that use IP configurations to allow devices within that VLAN to communicate with each other.

## Detailed Explanation of Trade-offs

When assigning an IP address to an interface, trade-offs to consider:
*   **Static vs DHCP:** Using a static IP address (like in this example) provides more control and predictability, while DHCP provides address assignment automation. The trade-off is between manageability and automation.
*   **Subnet Size:** The `/24` subnet mask in this example allows for 254 usable addresses. Smaller subnets limit the number of devices on the network, and larger subnets can introduce broadcast traffic issues. The trade-off is between scalability and efficiency.
*   **Security Considerations:** Exposing the management interface to public or untrusted subnets is a risk and can be mitigated by proper access control lists or by firewall rules on the interface. The trade-off is between convenience and security.
*  **VLAN Usage**: Using VLANs creates a network isolation at Layer 2 which can be useful to isolate specific networks but makes configuration more complex when compared to having all devices in the same network.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS 7.12, 6.48, and other 7.x versions, since there aren't any specific commands in this configuration that are version-specific. Be sure to consult the official RouterOS documentation for any version changes.

This documentation provides a comprehensive guide for setting up IP settings on a VLAN interface within a Hotspot environment in MikroTik RouterOS, addressing configuration, verification, and best practices.
