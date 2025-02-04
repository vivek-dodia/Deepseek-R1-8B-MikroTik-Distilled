Okay, let's craft some detailed documentation for implementing RADIUS authentication with a MikroTik router, specifically targeting RouterOS 7.12 and the provided parameters.

## Scenario Description:

This document outlines the steps to configure a MikroTik router (running RouterOS 7.12) to authenticate users via a RADIUS server. The specific focus will be on basic authentication setup, preparing the router to handle RADIUS requests from clients on the subnet 177.32.91.0/24, using interface 'ether-94'. This example targets a basic Enterprise network that requires centralized user management for network access.

## Implementation Steps:

Here's a step-by-step guide on how to configure the MikroTik router for RADIUS authentication:

### **Step 1: Initial Router Configuration and Interface Setup**

*   **Pre-Configuration Check:** Before starting, ensure your MikroTik router has a basic configuration, including a properly configured IP address on the 'ether-94' interface. For simplicity, we'll assume 'ether-94' is connected to a network segment where users will attempt to connect and be authenticated.

*   **CLI Pre-Config:**
    ```
    /interface print
    /ip address print
    ```

*   **Winbox GUI Pre-Config:** Check via `Interfaces` window and `IP -> Addresses` window. Ensure ether94 is in the correct state and there is an ip address that can be used to communicate with the RADIUS server.

* **Action:** If ether-94 doesn't have an IP address, we need to add one. For this example, we will assign `177.32.91.1/24` to the interface. Also ensure that the interface is enabled.

*   **CLI Configuration:**
    ```
    /interface enable ether-94
    /ip address add address=177.32.91.1/24 interface=ether-94
    ```

*   **Winbox GUI Configuration:**
    1.  Navigate to `Interfaces`. Ensure `ether-94` is enabled (the little "tick" box). If not enable it.
    2.  Navigate to `IP -> Addresses`
    3.  Click the `+` button to add a new address. Enter `177.32.91.1/24` as the address and choose `ether-94` as the interface. Then click `Apply`.

*   **Post-Configuration Check:**
    ```
    /interface print
    /ip address print
    ```

*   **Winbox GUI Post-Config:** Check via `Interfaces` window and `IP -> Addresses` window. Verify that the interface is enabled and has the new ip address associated with it.

### **Step 2: Adding the RADIUS Server Configuration**

*   **Pre-Configuration Check:** Before setting up RADIUS, ensure you have:
    *   The RADIUS server IP address.
    *   The RADIUS server secret.
    *   The appropriate network ports for authentication and accounting (typically 1812 and 1813, respectively).

*   **Action:** Add a new RADIUS server configuration using the appropriate IP address, secret, authentication port, and accounting port.

*   **CLI Configuration:**
    ```
    /radius add address=192.168.88.100 secret=your_radius_secret service=ppp,login timeout=5 authentication-port=1812 accounting-port=1813
    ```
    *   Replace `192.168.88.100` with your RADIUS server's actual IP address.
    *   Replace `your_radius_secret` with the shared secret you configured on your RADIUS server.

*   **Winbox GUI Configuration:**
    1.  Navigate to `RADIUS`.
    2.  Click the `+` button to add a new RADIUS server.
    3.  Fill the form fields, replacing `192.168.88.100` and `your_radius_secret` as needed. Make sure `service` is ticked with `ppp` and `login`
        *   `Address`: 192.168.88.100
        *   `Secret`: your_radius_secret
        *   `Service`: Select `ppp` and `login`.
        *   `Timeout`: 5
        *   `Authentication Port`: 1812
        *   `Accounting Port`: 1813
    4.  Click `Apply`.

*   **Post-Configuration Check:**
    ```
    /radius print
    ```

*   **Winbox GUI Post-Config:** Check the `RADIUS` window and ensure the new radius server is present and has the correct information.

### **Step 3: Configuring PPP Authentication to Use RADIUS**

*   **Pre-Configuration Check:** Ensure no other authentication methods are configured that might interfere. In this example, the router is configured with a default "ppp" profile.

*   **Action:** We will need to update the default "ppp" profile to include radius authentication.

*   **CLI Configuration:**
    ```
      /ppp profile set default use-encryption=required only-one=yes  use-radius=yes
    ```

*   **Winbox GUI Configuration:**
    1.  Navigate to `PPP -> Profiles`
    2.  Double click on `default`.
    3.  Under the `General` tab:
         *   Check `Use Radius`
         *   Select `Required` for `Use Encryption`
         *   Check `Only One`
    4.  Click `Apply`.

*   **Post-Configuration Check:**
     ```
     /ppp profile print
     ```

*   **Winbox GUI Post-Config:** Ensure that the default profile is configured to use RADIUS authentication.

### **Step 4: (Optional) Configure Hotspot or Other Services**
   This step will depend on the desired use case. For example, if you wish to use RADIUS for Hotspot, please consult the other official MikroTik documentation.

## Complete Configuration Commands:

```
# Enable Interface
/interface enable ether-94

# Add IP Address to interface
/ip address add address=177.32.91.1/24 interface=ether-94

# Add RADIUS server
/radius add address=192.168.88.100 secret=your_radius_secret service=ppp,login timeout=5 authentication-port=1812 accounting-port=1813

# Enable radius authentication for default PPP profile
/ppp profile set default use-encryption=required only-one=yes use-radius=yes
```

*   **`/interface enable ether-94`**: Enables the specified interface.
    *  `ether-94`: the name of the interface to enable.
*   **`/ip address add address=177.32.91.1/24 interface=ether-94`**: Assigns the IP address `177.32.91.1/24` to interface `ether-94`.
    *   `address`: The IP address and subnet mask in CIDR notation.
    *   `interface`: The interface to assign the IP address to.
*   **`/radius add address=192.168.88.100 secret=your_radius_secret service=ppp,login timeout=5 authentication-port=1812 accounting-port=1813`**: Adds a new RADIUS server.
    *   `address`: The IP address of the RADIUS server.
    *   `secret`: The shared secret used to authenticate with the RADIUS server.
    *   `service`: Specifies the services that will use the RADIUS server (`ppp` and `login`).
    *   `timeout`: The timeout (in seconds) for a response from the RADIUS server.
    *   `authentication-port`: The port number used for authentication requests (usually 1812).
    *   `accounting-port`: The port number used for accounting requests (usually 1813).
*   **`/ppp profile set default use-encryption=required only-one=yes use-radius=yes`**: Modifies the default PPP profile to enable RADIUS authentication.
    *   `use-encryption`: `required` means that connections will use encryption.
    *   `only-one`: `yes` means that only one connection can be active for the user.
    *   `use-radius`: `yes` enables RADIUS authentication.

## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Secret:** Ensure the secret configured on the MikroTik matches exactly the secret configured on your RADIUS server. Use the `/radius print` CLI command or the `RADIUS` window in Winbox to double-check.
*   **RADIUS Server Unreachable:** Verify that the MikroTik router can reach the RADIUS server on ports 1812 and 1813. Use the `ping` command or the `/tool/traceroute` to diagnose network connectivity issues.
*   **Firewall Blocking RADIUS Traffic:** If a firewall is configured on the MikroTik router, ensure rules are in place to allow traffic on ports 1812 and 1813 destined for the RADIUS server. Check `/ip firewall filter print` or the `IP -> Firewall` window in Winbox.
*   **RADIUS Server Configuration:** Incorrect configurations on the RADIUS server are also a very common cause of failure. Review RADIUS logs on the RADIUS server for more detailed error messages if the MikroTik log does not provide enough information.
*   **Authentication Issues:** Check MikroTik logs `System -> Log` for RADIUS-related error messages (e.g., incorrect username/password, RADIUS timeout). On the RADIUS server, ensure proper user and policy configuration.
*   **Resource Issues:** Check `/system resource print` in CLI or `System -> Resources` in winbox for high CPU or memory usage. If this is the case, you need to re-evaluate the needs of the device.
*   **Timeout:** Ensure that the timeout is sufficient for the RADIUS server to respond. The default value is 5 seconds, consider increasing it in case of high network latency.

## Verification and Testing Steps:

1.  **Connectivity Test:** Ping the RADIUS server from the MikroTik using `/ping <radius-server-ip>`.
2.  **RADIUS Logs:** Monitor the MikroTik's logs (`/system logging action`) for RADIUS-related events.
3.  **PPP Client Connection:** Attempt to connect using a PPP client and monitor the logs on both the MikroTik and the RADIUS server for successful authentication.
4.  **RADIUS Accounting:** If accounting is configured, verify that accounting packets are being sent to the RADIUS server by checking the radius logs.
5.  **Torch:** If necessary, use the torch `/tool torch interface=ether-94 protocol=udp port=1812,1813` to capture packets and verify that the communication to the RADIUS is established.
6.  **PPP Client status:** Check `/ppp active print` in CLI or `PPP -> Active connections` in winbox.

## Related Features and Considerations:

*   **Hotspot Configuration:** RADIUS can be used to authenticate users in a Hotspot setup.
*   **User Manager:** MikroTik's User Manager package offers a web interface for managing RADIUS users and policies. This package can be installed directly in the router.
*   **Dynamic VLANs:** RADIUS can be used to dynamically assign VLANs based on the user.
*   **Accounting:** RADIUS accounting provides detailed logs of user activity that can be used for billing and monitoring.

## MikroTik REST API Examples (if applicable):

While basic RADIUS configuration cannot be done directly with the REST API, you can retrieve configuration values, and manipulate them with API calls.

**Example: Get RADIUS Configuration**

*   **API Endpoint:** `/radius`
*   **Request Method:** `GET`
*   **Example `curl` command:**

    ```bash
    curl -k -u admin:your_router_password 'https://192.168.88.1/rest/radius'
    ```
*   **Expected Response (JSON):**

    ```json
    [
        {
          "id": "*1",
          "address": "192.168.88.100",
          "secret": "your_radius_secret",
          "service": "ppp,login",
          "timeout": "5",
          "authentication-port": "1812",
          "accounting-port": "1813",
          "disabled": "false"
        }
    ]
    ```

**Example: Update RADIUS Configuration**

*   **API Endpoint:** `/radius/*1` (Replace `*1` with the ID of the RADIUS server you want to update.)
*   **Request Method:** `PATCH`
*   **Example JSON Payload:**

    ```json
    {
        "timeout": "10"
    }
    ```
*   **Example `curl` command:**

    ```bash
    curl -k -u admin:your_router_password -H "Content-Type: application/json" -d '{"timeout": "10"}' 'https://192.168.88.1/rest/radius/*1' -X PATCH
    ```
*   **Expected Response:** (200 OK) or error message.
*   **Error Handling:** If the `id` does not exist, the API will return a 404. Invalid values (e.g., a non-numeric timeout) can cause 400 Bad Request errors. These can be handled in a client application with error checking.

**Important notes:**
*   Always use https when communicating with the api.
*   Use `-k` for self-signed certificates.

## Security Best Practices

*   **Secure RADIUS Secret:** The RADIUS secret should be complex and known only to the MikroTik router and the RADIUS server.
*   **Restrict Access:** Limit access to the MikroTik router to trusted users and networks. The REST API and winbox interface, for example should not be publicly accessible.
*   **Enable Logging:** Properly configure logging to capture and monitor authentication events and potential attacks.
*   **Regular Updates:** Keep your MikroTik router's RouterOS version updated to ensure the latest security patches.
*   **Rate Limiting:** Consider using rate-limiting features on the router to prevent denial-of-service attacks against the authentication process.

## Self Critique and Improvements:

This configuration is a basic setup for RADIUS authentication and provides the bare minimum. Here are some potential improvements:

*   **More Detailed Logging:** Configure more detailed logging for debugging and auditing purposes.
*   **Multiple RADIUS Servers:** Add failover RADIUS servers for redundancy.
*   **Dynamic VLAN Assignment:** Implement dynamic VLAN assignment based on user authentication.
*   **More Advanced Authentication:** Explore more advanced authentication protocols such as EAP.
*   **Central User Management:** Integrate the MikroTik router with centralized user management systems.
*   **More granular access-control rules:** Use the radius response for more granular control in the network.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to a network. In our scenario, the MikroTik router acts as a Network Access Server (NAS) and communicates with the RADIUS server to authenticate user connection attempts.

*   **Authentication:** Verifies the user's identity. This typically involves sending the user's credentials (username and password) to the RADIUS server, which then checks them against its database.
*   **Authorization:** Determines what resources the user is allowed to access. This is usually done after successful authentication and the RADIUS server returns parameters that are used to define access rights.
*   **Accounting:** Keeps track of user sessions and resource usage. This allows administrators to monitor network usage and generate reports or usage-based charges.

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:** Local authentication is simpler to configure but lacks centralized management and scalability. RADIUS authentication provides centralized control, better scalability, and enhanced security.
*   **PAP vs. CHAP Authentication:** PAP (Password Authentication Protocol) is simpler but transmits passwords in clear text making it insecure. CHAP (Challenge-Handshake Authentication Protocol) is more secure, because it transmits hashed passwords and it's widely supported. Consider other stronger authentication protocols if needed.
*   **Single vs. Multiple RADIUS Servers:** A single RADIUS server is easier to configure but represents a single point of failure. Multiple RADIUS servers provide redundancy and fault tolerance.
*   **Timeout:** A low timeout value can lead to connection failures if the network is slow. A high timeout value can delay error detection and can impact user experience. It is important to configure a timeout that is appropriate for the network and the RADIUS infrastructure.
*   **Accounting** Accounting is valuable for monitoring and reporting, but also increases the network and server load. Carefully plan the needed use case and resources.
*   **Encryption:** While PPP encryption is a good method to protect communication, other options like IPsec can be considered for more robust end to end encryption, for some specific use cases.

## Configuration for Specific RouterOS Versions:

This documentation targets RouterOS 7.12, but it's also compatible with 6.48 and other 7.x versions. Please consult the official MikroTik documentation for specific version differences or feature variations if needed.

Let me know if you would like any more specific configurations, or extra features to be added to this example!
