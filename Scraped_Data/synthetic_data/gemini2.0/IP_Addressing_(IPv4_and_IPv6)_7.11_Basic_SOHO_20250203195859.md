Okay, let's dive into a detailed technical documentation for configuring IP addressing on a MikroTik router, specifically focusing on the provided scenario.

## Scenario Description:

We are configuring a MikroTik router in a SOHO environment. We need to assign a static IPv4 address to the wireless interface `wlan-95` on the subnet `218.175.55.0/24`. The network will primarily use IPv4. IPv6 is not the main focus in this scenario, but basic IPv6 configuration will be included.

## Implementation Steps:

Here is a step-by-step guide to configure the interface with the specified parameters:

**Step 1:  Verify the Existing Interface and IP Configurations**

*   **Purpose:** Before making any changes, it's good to understand the current state. We'll check the current interface list and IP address configurations to ensure there are no conflicts.
*   **Before:** This initial state depends on whether this is a fresh router or one that has already been configured. In a fresh router, the `wlan-95` may not exist, or it may exist with a default configuration.
*   **CLI Command(s):**

    ```mikrotik
    /interface print
    /ip address print
    ```
*   **Expected Output (Example):**
    ```
    # Example output for /interface print
    Flags: X - disabled, D - dynamic, R - running
     0  R name="ether1" type=ether mtu=1500 mac-address=XX:XX:XX:XX:XX:XX
     1    name="wlan1" type=wlan mtu=1500 mac-address=YY:YY:YY:YY:YY:YY ...
    # Example output for /ip address print
    Flags: X - disabled, I - invalid, D - dynamic
     #   ADDRESS            NETWORK         INTERFACE
    ```
*   **Winbox Equivalent:** Navigate to *Interfaces* and *IP -> Addresses* to view the same information. The interface tab will show you the available interfaces, and the address tab will show you the IP addresses.

*   **Effect:** This step provides a baseline understanding of the current setup. We can see the existing interfaces and the assigned IP addresses before applying changes.

**Step 2:  Configure the IP Address for `wlan-95`**

*   **Purpose:** Assign a static IPv4 address to the `wlan-95` interface. If `wlan-95` does not exist, we will need to create and configure it.
*   **Before:**
    *   The output from **Step 1** will show that no IPv4 address is assigned to wlan-95 (or that the interface doesn't exist).
*   **CLI Command(s):**

    ```mikrotik
    #Create the interface if it does not exist
    /interface wireless add name=wlan-95 disabled=no mode=ap-bridge ssid=mikrotik-ap \
    band=2ghz-b/g/n channel-width=20mhz frequency=2412 security-profile=default

    /ip address add address=218.175.55.1/24 interface=wlan-95
    ```
    *   **Note:** This step assumes the wlan interface was not previously defined. If `wlan-95` already exists, skip the `interface wireless add` command.
    *   **Important:** If you don't set the default security profile, it will be disabled by default.
*   **Winbox Equivalent:**
    *   *Interfaces* (if the interface does not exist): press the **+** button and select Wireless interface. Add the above configuration.
    *   *IP -> Addresses*: Click the "+" button, enter `218.175.55.1/24` in the "Address" field, and select "wlan-95" in the "Interface" drop-down menu.
*   **Effect:** The `wlan-95` interface will be assigned the IP address `218.175.55.1/24`. This allows devices on the network to communicate with the router's IP address. The wireless interface is created and enabled.

*   **After:**
    *   `/interface print` now shows a wireless interface that is enabled named `wlan-95`
    *   `/ip address print` shows an IP address on the `wlan-95` interface, with a network of `218.175.55.0/24`

**Step 3 (Optional): Configure IPv6 Address**

*   **Purpose:**  Add a link-local IPv6 address to `wlan-95` for basic IPv6 connectivity. This is an optional step.
*   **Before:** No IPv6 address is configured for `wlan-95`.
*   **CLI Command(s):**

    ```mikrotik
    /ipv6 address add interface=wlan-95 address=fe80::1/64
    ```
    *   **Note:** Link-local addresses (starting with `fe80::`) are automatically assigned by interfaces, so this step can be omitted if you just want to use the auto-configured one.
*   **Winbox Equivalent:** Navigate to *IPv6 -> Addresses*, Click on "+" button and in the "Address" field, enter `fe80::1/64`. Select the interface drop-down to `wlan-95`.
*   **Effect:** The `wlan-95` interface now has a link-local IPv6 address, which will be used for network discovery.
*  **After:**
     *   `/ipv6 address print` will show the link-local address on the interface `wlan-95`

## Complete Configuration Commands:

Here's a complete set of MikroTik CLI commands to implement the setup:

```mikrotik
/interface wireless add name=wlan-95 disabled=no mode=ap-bridge ssid=mikrotik-ap \
band=2ghz-b/g/n channel-width=20mhz frequency=2412 security-profile=default

/ip address add address=218.175.55.1/24 interface=wlan-95
/ipv6 address add interface=wlan-95 address=fe80::1/64
```

**Parameter Explanations:**

| Command                                   | Parameter         | Description                                                                                                 | Example Value            |
| :---------------------------------------- | :---------------- | :---------------------------------------------------------------------------------------------------------- | :----------------------- |
| `/interface wireless add`                | `name`            | The name of the wireless interface.                                                                         | `wlan-95`                |
| `/interface wireless add`                | `disabled`        | Enable or disable interface.                                                                            | `no`                     |
| `/interface wireless add`                | `mode`        | The mode of the wireless interface.                                                                        | `ap-bridge`                 |
| `/interface wireless add`                | `ssid`        | The SSID name for the wireless network.                                                                        | `mikrotik-ap`                 |
| `/interface wireless add`                | `band`        | The band used for wireless.                                                                        | `2ghz-b/g/n`                 |
| `/interface wireless add`                | `channel-width`        | The width of the radio channel                                                                        | `20mhz`                |
| `/interface wireless add`                | `frequency`        | The frequency of the radio channel                                                                        | `2412`                |
| `/interface wireless add`                | `security-profile`        | The security profile for the wireless network                                                                         | `default`                |
| `/ip address add`                         | `address`         | The IP address and subnet mask.                                                                           | `218.175.55.1/24`          |
| `/ip address add`                         | `interface`       | The interface to assign the IP address to.                                                                | `wlan-95`                |
| `/ipv6 address add`                       | `interface`       | The interface to assign the IPv6 address to.                                                                | `wlan-95`                |
| `/ipv6 address add`                       | `address`         | The IPv6 address. In this case a link-local address.                                                        | `fe80::1/64`             |

## Common Pitfalls and Solutions:

*   **Interface `wlan-95` Already Exists:** If an interface with that name already exists, the script might throw an error. Use `/interface print` to check for existing interfaces and rename or remove the old interface before running the script.
*   **Incorrect Subnet Mask:** If the subnet mask is wrong (e.g., `/32` instead of `/24`), devices on the network will not be able to communicate properly. Always double-check the subnet mask.
*   **Conflicting IP Addresses:** If the chosen IP address is already assigned to another device on the network, there will be a conflict.  Ensure the IP address is unique.
*   **Wireless Interface not enabled:** Ensure that the wireless interface is enabled before assigning the IP address. Use the command `/interface wireless enable wlan-95` to enable the wireless interface if necessary.
*   **Wireless Interface Security Settings**: If the `security-profile` is not defined, or not configured, devices will be unable to connect to the wireless network. You may use `/interface wireless security-profiles print` and `/interface wireless security-profiles add` to modify the security settings.
*   **Firewall Rules:** If your firewall is enabled, there may be a firewall ruleset that prevents traffic on this interface, or between different interfaces. Ensure that your firewall is configured correctly, for example, you may need to allow input on the `wlan-95` interface.
*   **High CPU/Memory Usage:** This basic configuration should not normally cause any high CPU or memory usage, but a large number of connected wireless devices, or more complex configurations (like a hotspot setup) might cause performance issues. The tools `/system resource monitor` and `/tool profile` can help troubleshoot such issues.

## Verification and Testing Steps:

1.  **Check IP Address Assignment:** Use `/ip address print` to verify that the IP address is assigned to `wlan-95`.
2.  **Ping the Interface IP:** From another device connected to the `wlan-95` network, ping the router's IP address (`218.175.55.1`).

    ```bash
    ping 218.175.55.1
    ```
    Successful pings indicate that basic IP connectivity is working.
3.  **Check IPv6 Address:** Verify the IPv6 address assignment using `/ipv6 address print`
4.  **Ping the IPv6 Interface IP:** From another device connected to the `wlan-95` network, ping the router's IPv6 link-local address (`fe80::1`). The equivalent ping command would be `ping6 fe80::1%<wlan-95-interface>`.
5.  **Check Interface Status:** Use `/interface print` to ensure `wlan-95` is enabled and running.
6.  **Check wireless clients:** From the web interface or winbox, check the status of the wireless clients that connected to the wireless network

## Related Features and Considerations:

*   **DHCP Server:** To automatically assign IP addresses to connected devices, configure a DHCP server on `wlan-95`.
*   **Firewall Rules:** Secure the network by setting up appropriate firewall rules for `wlan-95`.
*   **VLANs:** Consider using VLANs for network segmentation if you have more complex requirements.
*   **Wireless Security:** Configure WPA2 or WPA3 security for the `wlan-95` wireless interface using security profiles.
*  **Routing:** If traffic needs to be routed to other networks, routing rules must be configured
*   **IPv6 DHCPv6 Server:** If you plan on using IPv6 on your network, add a DHCPv6 server on this interface, and configure IPv6 routing and firewall rules.

## MikroTik REST API Examples:

Here's how to add the same IP address configuration using the MikroTik REST API. Note that using the API requires the REST interface to be enabled in the router first. You can do this by using `/ip service enable api` and `/ip service enable api-ssl`.

**1. Creating Wireless Interface**
   *   **API Endpoint**: `https://<router-ip>/rest/interface/wireless`
   *   **Request Method**: `POST`
   *   **Example JSON Payload**:
      ```json
       {
            "name": "wlan-95",
            "disabled": false,
            "mode": "ap-bridge",
            "ssid": "mikrotik-ap",
            "band": "2ghz-b/g/n",
            "channel-width": "20mhz",
            "frequency": 2412,
            "security-profile":"default"
        }
      ```
   *   **Expected Response (201 Created):**
       ```json
       {
          "id": "*5",
          "name": "wlan-95",
          "type": "wlan",
          ...
        }
       ```
    *   **Error Handling:**
        *   A 400 (Bad Request) response will occur if the request data does not conform to the required structure or if a parameter is invalid.
        *   A 409 (Conflict) response will occur if an interface with that name already exists.

**2. Adding IP Address**

*   **API Endpoint:** `https://<router-ip>/rest/ip/address`
*   **Request Method:** `POST`
*   **Example JSON Payload:**

    ```json
    {
        "address": "218.175.55.1/24",
        "interface": "wlan-95"
    }
    ```

*   **Expected Response (201 Created):**

    ```json
    {
      "id": "*3",
      "address": "218.175.55.1/24",
      "network": "218.175.55.0/24",
      "interface": "wlan-95",
      ...
    }
    ```
*    **Error Handling:**
        *   A 400 (Bad Request) response will occur if the request data does not conform to the required structure or if a parameter is invalid.
        *   A 409 (Conflict) response will occur if an IP address already exists on that interface.

**3. Adding IPv6 Address**

*   **API Endpoint:** `https://<router-ip>/rest/ipv6/address`
*   **Request Method:** `POST`
*   **Example JSON Payload:**

    ```json
    {
      "address": "fe80::1/64",
      "interface": "wlan-95"
    }
    ```

*   **Expected Response (201 Created):**

    ```json
    {
        "id": "*7",
        "address": "fe80::1/64",
        "interface": "wlan-95",
        ...
    }
    ```

    *    **Error Handling:**
        *   A 400 (Bad Request) response will occur if the request data does not conform to the required structure or if a parameter is invalid.
        *   A 409 (Conflict) response will occur if an IP address already exists on that interface.

**Note:** To execute these API calls, you'll need to use a tool like `curl`, `Postman` or `Insomnia` and provide appropriate authentication headers (e.g., username and password). You can use the `Basic` auth method to authenticate to the router.

## Security Best Practices:

*   **Strong Wireless Security:** Always use WPA2 or WPA3 with a strong password. Configure a security profile and assign it to the interface.
*   **Firewall:** Configure a proper firewall on the router to prevent unwanted access to the network.  Limit the services accessible from the WAN interface.
*   **RouterOS Updates:** Keep RouterOS updated to the latest stable version for security patches.
*   **Secure Access:** Limit access to the RouterOS configuration interface (e.g., only allow access from known IP addresses). Use a secure password and consider changing the default username.
*   **Disable Unused Services:** Disable services like Telnet and the default API endpoint that are not needed.
* **Secure API Usage:**  Always use TLS when accessing the REST API by using `https://` and ensure the router has a valid certificate. Do not use default passwords.
* **Monitor for Unauthorised Changes:** Periodically review the router's configuration for unauthorised changes.

## Self Critique and Improvements:

This configuration is suitable for a basic SOHO setup.

*   **Improvements:**
    *   **Dynamic IP Address Assignment:** Implement a DHCP server for the `wlan-95` network to automatically assign IP addresses to clients, if needed.
    *   **Advanced Wireless:** Configure advanced wireless settings such as channel selection, power levels and advanced security settings.
    *   **Firewall Rules:** Add detailed firewall rules to secure the router, and the internal network.
    *   **IPv6 Support:**  Implement a full IPv6 stack by creating a DHCPv6-PD server for this interface.
    *   **Monitoring:** Configure SNMP for monitoring the router, CPU and memory usage, and the overall interface utilisation.
    *   **Logging:** Configure the log settings to record relevant information for troubleshooting purposes.

## Detailed Explanations of Topic:

**IP Addressing (IPv4 and IPv6):**

*   **IPv4:** Uses a 32-bit address represented in dotted decimal notation (e.g., `218.175.55.1`). The subnet mask (`/24` in our example) defines the network portion of the IP address, allowing the router to determine which addresses are on its local network.
*   **IPv6:** Uses a 128-bit address, represented in hexadecimal format (e.g., `fe80::1`). IPv6 provides a much larger address space and is intended to be the successor to IPv4.
*   **Link-Local Addresses:**  IPv6 addresses starting with `fe80::` are link-local addresses, used for communication within the local network segment. They are not routable on the internet.
*   **Subnetting:** Subnetting divides larger networks into smaller, more manageable segments. This enhances efficiency and control. The `/24` notation is the prefix length which corresponds to the number of bits used to represent the network, in this case 24 bits, leaving 8 bits for hosts on the network.

## Detailed Explanation of Trade-offs:

*   **Static vs. Dynamic IP:**
    *   **Static IP:** Easier for server devices with consistent addressing, but requires manual configuration. It is also easier to manage and provides a predictable address.
    *   **Dynamic IP (DHCP):**  Simple to configure on clients, but their IP addresses may change. Suitable for devices that don't require static IPs like laptops and phones.
*   **IPv4 vs. IPv6:**
    *   **IPv4:** Well-established, but address space is limited. NAT (Network Address Translation) is needed to allow multiple devices behind a single public IPv4 address.
    *   **IPv6:** Vast address space eliminates the need for NAT and simplifies network configuration, but it has slower adoption.
*   **Subnet Mask Length:**
    *   **Smaller Subnets:** With a more specific prefix (e.g., `/28`), fewer IP addresses will be available, but that can improve security by segmenting networks.
    *   **Larger Subnets:**  With a shorter prefix (e.g., `/24` which is commonly used in SOHO networks), more IP addresses are available but can increase broadcasting traffic.
*   **Manual vs. API Configuration:**
    *   **Manual:** Good for one-off configurations via the CLI or Winbox, but might not be efficient for larger deployments.
    *   **API:** Offers the benefits of automation, ideal for managing multiple MikroTik devices, or for a network environment where many configurations have to be done.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 7.11, and is also compatible with RouterOS versions 6.48 and any other version in the 7.x branch.  The core commands for IP address assignment, wireless configuration, and IPv6 addressing haven't had breaking changes, therefore any router using those versions of RouterOS should be compatible with this setup.

If you are using RouterOS version 6 or lower, be aware that the REST API was not available in those versions, and that you will have to use the `/ip service` section to enable the `api`, `api-ssl` or `www` interface.

This comprehensive documentation should provide you with a strong starting point for configuring IP addressing on your MikroTik router. Let me know if you have any further questions.
