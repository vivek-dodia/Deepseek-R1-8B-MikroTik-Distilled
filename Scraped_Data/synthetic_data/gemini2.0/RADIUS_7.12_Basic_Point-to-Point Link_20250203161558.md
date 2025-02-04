Okay, let's craft some comprehensive documentation for configuring RADIUS on a MikroTik router in a point-to-point scenario, focusing on a specific subnet and interface, and targeting RouterOS 7.12.

## Scenario Description:

We are configuring a MikroTik router (Router A) at one end of a point-to-point link to use a RADIUS server for authentication of PPP connections (such as PPPoE or PPTP) initiated from the other end of the link (Router B). This setup is common in scenarios where you want centralized user authentication for your network, often used by small and medium-sized businesses (SMBs) or Internet Service Providers (ISPs). We'll use the interface `ether-18` and a subnet of `248.146.171.0/24`. This example focuses on the RADIUS side of the configuration. The assumption is that Router B is already configured to send user authentication requests to Router A.

## Implementation Steps:

Here's a step-by-step guide to configure RADIUS authentication on Router A (the server):

1.  **Step 1: Verify Interface and Address Configuration**
    *   **Description**: Ensure the interface `ether-18` is enabled and configured with an IP address within the `248.146.171.0/24` subnet.
    *   **Before Configuration (Example Output):**

        ```
        /interface print
        Flags: D - dynamic ; X - disabled ; R - running; S - slave
         #    NAME     TYPE        MTU  L2MTU    MAX-L2MTU MAC-ADDRESS      
         0  R ether1   ether       1500 1598    1598      XX:XX:XX:XX:XX:XX  
         1  R ether2   ether       1500 1598    1598      XX:XX:XX:XX:XX:XX  
         2    ether-18  ether       1500 1598    1598      XX:XX:XX:XX:XX:XX  
        
        /ip address print
         Flags: X - disabled, I - invalid, D - dynamic 
         #   ADDRESS            NETWORK         INTERFACE
         0  192.168.88.1/24    192.168.88.0    ether1
        ```

    *   **CLI Command:**

        ```mikrotik
        /ip address add address=248.146.171.1/24 interface=ether-18
        ```

    *   **After Configuration (Example Output):**

        ```
        /interface print
        Flags: D - dynamic ; X - disabled ; R - running; S - slave
         #    NAME     TYPE        MTU  L2MTU    MAX-L2MTU MAC-ADDRESS      
         0  R ether1   ether       1500 1598    1598      XX:XX:XX:XX:XX:XX  
         1  R ether2   ether       1500 1598    1598      XX:XX:XX:XX:XX:XX  
         2  R ether-18  ether       1500 1598    1598      XX:XX:XX:XX:XX:XX  
        
        /ip address print
         Flags: X - disabled, I - invalid, D - dynamic 
         #   ADDRESS            NETWORK         INTERFACE
         0  192.168.88.1/24    192.168.88.0    ether1
         1  248.146.171.1/24  248.146.171.0  ether-18
        ```

    *   **Winbox GUI:**
        *   Navigate to `IP` -> `Addresses`.
        *   Click the "+" button.
        *   Enter the IP address (e.g., `248.146.171.1/24`), select the interface `ether-18`, and click `OK`.

2.  **Step 2: Add RADIUS Server Configuration**
    *   **Description**:  Configure the RADIUS server details (IP address, secret, etc.).
    *   **Before Configuration (Example Output):**

        ```
         /radius print
        ```
         Output is empty, as no radius configuration has been done.

    *   **CLI Command:**

        ```mikrotik
        /radius add address=192.168.1.10 secret=mysecret service=ppp timeout=30
        ```
        *  **Explanation**: This command adds a radius configuration.
         * `address` sets the IP address of the RADIUS server.
         *  `secret` sets the shared secret key.
         * `service` sets the service this radius configuration is used for.
         * `timeout` sets the connection timeout for the RADIUS server.
    *   **After Configuration (Example Output):**

         ```
        /radius print
        Flags: X - disabled, * - default 
         #   ADDRESS      SECRET   ACCOUNTING-PORT AUTH-PORT TIMEOUT
         0   192.168.1.10   mysecret         1813       1812    30s   
        ```
    *   **Winbox GUI:**
        *   Navigate to `RADIUS`.
        *   Click the "+" button.
        *   Enter the RADIUS server IP in the `Address` field (e.g., `192.168.1.10`).
        *   Enter the `Secret` and select the `ppp` service and adjust the timeout if needed.

3.  **Step 3: Enable RADIUS for PPP**
    *   **Description**: Tell the MikroTik router to use the configured RADIUS server for PPP authentication. This is usually configured within a PPP profile.
    *   **Before Configuration (Example Output):**

        ```
         /ppp profile print
        ```

        This command will return the current configurations for all ppp profiles
    *   **CLI Command:**

        ```mikrotik
        /ppp profile set default use-radius=yes
        ```
        *  **Explanation**: This command enables the use of radius authentication on the 'default' ppp profile, and this change applies to all ppp servers using that profile. To apply it to other profiles, replace 'default' with the profile name.
    *   **After Configuration (Example Output):**

         ```
         /ppp profile print
        Flags: * - default 
         #    NAME                                        CHANGE-TCP-MSS USE-ENCRYPTION  ONLY-ONE  ADDRESS-LIST  RADIUS-ACCOUNTING  BRIDGE    
         0 *  default                                         yes       yes    no                                              no
         
         /ppp profile print detail
         Flags: * - default 
         0   * name="default" use-encryption=yes only-one=no change-tcp-mss=yes address-list="" use-radius=yes
        ```
    *   **Winbox GUI:**
        *   Navigate to `PPP` -> `Profiles`.
        *   Double-click on the `default` profile or the one you wish to configure.
        *   Check the `Use RADIUS` box and click `OK`.

## Complete Configuration Commands:

```mikrotik
# Set IP address on ether-18
/ip address add address=248.146.171.1/24 interface=ether-18

# Add RADIUS server
/radius add address=192.168.1.10 secret=mysecret service=ppp timeout=30

# Enable RADIUS authentication for PPP default profile
/ppp profile set default use-radius=yes

# Example of enabling radius for a specific profile named 'my-profile'
#/ppp profile set my-profile use-radius=yes
```
**Parameter Explanations:**

| Command Parameter | Description | Example Value |
|-------------------|---------------------------------|-----------------|
| `/ip address add address` | The IP address and subnet mask to add | `248.146.171.1/24` |
| `/ip address add interface` | The interface where the IP address should be assigned | `ether-18` |
| `/radius add address` | The IP address of the RADIUS server | `192.168.1.10` |
| `/radius add secret` | The shared secret key for RADIUS authentication | `mysecret` |
| `/radius add service` |  The service for which RADIUS will be used. | `ppp` |
| `/radius add timeout` |  The connection timeout for the RADIUS server. | `30s` |
| `/ppp profile set <profile name> use-radius` | Enables or disables RADIUS authentication for a specific PPP profile | `yes`/`no` |

## Common Pitfalls and Solutions:

*   **RADIUS Secret Mismatch**:
    *   **Problem**: The shared secret configured on the MikroTik must match the secret configured on the RADIUS server. Authentication will fail if this mismatch happens.
    *   **Solution**: Double-check the secret on both the MikroTik and the RADIUS server. Use the same secret in both locations and make sure to type it carefully.
*   **Firewall Issues**:
    *   **Problem**: The MikroTik’s firewall might be blocking communication with the RADIUS server, especially on UDP ports 1812 (authentication) and 1813 (accounting).
    *   **Solution**: Create firewall rules allowing the MikroTik to connect to the RADIUS server on the necessary ports.

        ```mikrotik
        /ip firewall filter
        add chain=output action=accept dst-address=192.168.1.10 protocol=udp dst-port=1812,1813
        ```

*   **RADIUS Server Unreachable**:
    *   **Problem**: The MikroTik cannot reach the RADIUS server. Check the server is online and the connection from the MikroTik router is not blocked by a firewall.
    *   **Solution**: Verify network connectivity using `ping 192.168.1.10` from the MikroTik router. Ensure that the router has a route to the RADIUS server's IP address. Check if an intermediary network is blocking traffic.
*   **Incorrect Service Set**:
    *   **Problem**: When the `service=ppp` is not set correctly, Radius authentication may fail even though there is a valid authentication.
    *   **Solution**: Verify that the `service` parameter matches the radius service type on the ppp profile configuration.
*   **CPU or Memory Overload**:
    *   **Problem**: The Radius requests can be processed using a large amount of CPU and memory. If there are too many requests, this could overload the router.
    *   **Solution**: Ensure that the router is not overloaded with other tasks and has enough resources for its normal operation.

## Verification and Testing Steps:

1.  **Ping the RADIUS Server**:
    *   **Command**: `ping 192.168.1.10` (Replace with your RADIUS server IP).
    *   **Expected Result**: Successful ping indicates basic network connectivity.
2.  **Check RADIUS Logs**:
    *   **Command**: `/system logging print topic=radius`
    *   **Expected Result**: Look for RADIUS related log messages. Authentication attempts (success or failure) are logged here.
3.  **PPP Authentication Test**:
    *   **Action**: Attempt to connect with a PPP client configured to use RADIUS authentication. This should include a valid username and password.
    *   **Expected Result**: The PPP connection should establish if the RADIUS server authenticates the credentials, and logs should indicate successful login.
4.  **Torch Tool**:
    *   **Command**: `/tool torch interface=ether-18 protocol=udp port=1812,1813`
    *   **Expected Result**: This tool will show UDP traffic on port 1812 and 1813, showing the request and response from the radius server.

## Related Features and Considerations:

*   **RADIUS Accounting**: Enable RADIUS accounting to track session usage. This logs session start/stop times, bandwidth usage, etc.

    ```mikrotik
    /radius set 0 accounting=yes
    ```

*   **Multiple RADIUS Servers**: Configure multiple RADIUS servers for redundancy. The router will attempt to connect with the servers one after the other until it gets a response.

    ```mikrotik
    /radius add address=192.168.1.11 secret=mysecret service=ppp timeout=30
    ```
    Note: Use the same secret on all servers for simplicity.
*   **PPP Secrets**:  While using RADIUS, the `/ppp secrets` section should not be configured for authentication. The user authentication should be done by the Radius server only.
*   **IP Pools**: If you are using Radius, it is recommended to have the IP pool on the Radius server and not configured on the Mikrotik Router.

## MikroTik REST API Examples:

```json
#Example of how to list all radius configurations
{
  "api_endpoint": "/radius",
  "request_method": "GET",
  "expected_response": "A JSON array of radius configurations"
}
```

```json
# Example API Call to add a RADIUS server
{
  "api_endpoint": "/radius",
  "request_method": "POST",
  "json_payload": {
    "address": "192.168.1.10",
    "secret": "mysecret",
    "service": "ppp",
    "timeout": "30"
  },
  "expected_response": {
     "message":"added",
      "id":"*0"
  },
    "error_handling":{
        "code":409,
        "message":"This configuration already exists."
    }
}
```

```json
# Example API call to enable RADIUS on a PPP profile

{
  "api_endpoint": "/ppp/profile",
  "request_method": "PATCH",
  "resource_id": "*0",
  "json_payload":{
     "use-radius":"yes"
    },
  "expected_response": {
       "message":"changed"
  },
  "error_handling":{
       "code":404,
       "message":"This ppp profile does not exist."
  }
}
```

**Parameter Explanations:**

*   `api_endpoint`: The RouterOS API endpoint.
*   `request_method`: HTTP method (GET, POST, PUT, PATCH, DELETE).
*   `json_payload`: JSON object to be sent with the request.
*   `resource_id`: The ID of the resource to modify or delete. For example, the ppp profile `*0` is the default profile.
*   `expected_response`: Expected response from the API.
*   `error_handling`: Expected error information.

**Note**: Replace IP addresses and secrets with your specific values. Error handling is crucial for production environments.

## Security Best Practices:

*   **Strong RADIUS Secret**: Use a strong, complex RADIUS shared secret. Do not use default or easily guessable secrets.
*   **Firewall Rules**: Implement firewall rules to restrict access to the RADIUS ports. Only allow trusted IPs to communicate with the RADIUS server.
*   **Secure RADIUS Server**: The RADIUS server itself should be secured, with regular security updates and proper access controls.
*   **Monitor Logs**: Regularly check the system logs for any suspicious activity related to RADIUS authentication.
*   **Accounting**: Enable accounting to detect abnormal usage and potential abuse.
* **Limit Radius server access**: Restrict who can access the radius server and ensure that the machine running the radius server is fully updated.
* **Use TLS**: To secure communication, use a TLS connection where possible to protect authentication secrets from sniffing.

## Self Critique and Improvements:

*   **Error Handling:** Add better error handling and more detailed troubleshooting steps.
*   **Advanced Features:** Explore additional RADIUS features (e.g., CoA (Change of Authorization)).
*   **Scalability**: Consider more complex setups for larger networks, including load balancing between RADIUS servers.
*   **User Creation:** This setup only authenticates users using Radius. It could be made better if it included how to setup the users in Radius to fully demonstrate the configuration of the feature.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) for users connecting to a network. It allows network access devices (like our MikroTik router) to authenticate users against a central database, such as an LDAP server or SQL database.

Key Aspects of RADIUS:

*   **Authentication**: Verifies the identity of the user trying to connect.
*   **Authorization**: Determines what resources the user is allowed to access.
*   **Accounting**: Tracks the user's activity on the network (session start/stop times, bandwidth usage).
*   **Client-Server Model**: The MikroTik acts as a client, sending authentication requests to the RADIUS server, which acts as the server.

## Detailed Explanation of Trade-offs:

*   **Local vs. RADIUS Authentication**: Local authentication (using `/ppp secrets`) is simpler to set up but doesn't scale well and is harder to manage. RADIUS is more complex to configure initially, but provides a centralized authentication, authorization and accounting solution for larger networks.
*   **Multiple RADIUS Servers**: Setting up multiple RADIUS servers for redundancy provides high availability but increases the complexity of configuration and maintenance.
*   **Security vs. Convenience**: Complex secrets and restricted firewall rules are more secure, but may cause difficulties in configuration. Simpler secrets may be easier to use but create a security risk.

## Configuration for Specific RouterOS Versions:

This configuration targets MikroTik RouterOS 7.12 (and is generally valid for 6.48 and 7.x), meaning that all the above commands are applicable. If you were running a significantly older RouterOS version (e.g. v6 or older), there may be some command changes such as the placement of the use-radius command inside the ppp server itself rather than on the profiles. Make sure to refer to the specific RouterOS version documentation if you are running a version older than this.

This concludes the comprehensive documentation for RADIUS setup on a MikroTik router, with a focus on practical implementations, security, and detailed explanations.
