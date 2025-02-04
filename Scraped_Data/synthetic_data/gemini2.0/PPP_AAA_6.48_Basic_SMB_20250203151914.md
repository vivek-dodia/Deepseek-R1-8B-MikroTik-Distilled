Okay, let's dive into a detailed technical document on setting up PPP AAA (Authentication, Authorization, and Accounting) in MikroTik RouterOS 6.48, specifically for the subnet 225.150.229.0/24 on interface `ether-29`. We will target a basic configuration for a SMB environment.

## Scenario Description

This scenario focuses on implementing basic PPP authentication for clients connecting to a MikroTik router through a PPP interface (e.g., PPPoE or PPTP). The goal is to use a simple local user database on the router for authenticating the clients using AAA, rather than using external radius. The interface `ether-29` is designated as the physical interface for this PPP connection. This is common in setups where you might have a dedicated port for VPN or dial-up services.

## Implementation Steps

Here's a step-by-step guide to configuring PPP AAA:

### Step 1: Ensure the `ether-29` Interface is Active

*   **Before:** Verify that the `ether-29` interface is enabled and not disabled.
*   **Action:**  We will check the existing status of ether-29 and ensure it is not disabled. If it is disabled, we will enable it.
*   **CLI Example:**
    ```mikrotik
    /interface ethernet print
    ```

    **Example output:**
    ```
    Flags: D - dynamic, X - disabled, R - running, S - slave
     #    NAME                                    MTU   MAC-ADDRESS        LAST-LINK-UP-TIME
     0  R  ether1                                 1500  00:0C:29:AB:CD:EF    6d10h12m28s
     1    ether2                                 1500  00:0C:29:AB:CD:F0
     ...
    28    ether29                                1500  00:0C:29:AB:CD:1A
    ```
    If the ether29 interface has the `X` flag (which means it is disabled), then run the following to enable it.
    ```mikrotik
     /interface ethernet enable ether29
    ```
*   **Winbox:**
    *   Navigate to *Interface* in the left menu.
    *   Find *ether29* in the interface list.
    *   Ensure the checkbox under the "Enabled" column is checked. If not, select the interface and click the 'Enabled' button at the top.
*   **Effect:** This ensures the interface is ready to be used for PPP connections.

### Step 2: Create a PPP Secret

*   **Before:**  No PPP user is present, thus no authentication is possible.
*   **Action:** Create a user (secret) that clients will use to authenticate. We'll create a user named `testuser` with the password `testpass` and assign it to the `default` service.
*   **CLI Example:**
    ```mikrotik
    /ppp secret add name=testuser password=testpass service=pppoe
    ```
*   **Winbox:**
    *   Navigate to *PPP* in the left menu.
    *   Select the *Secrets* tab.
    *   Click the "+" button.
    *   In the new window:
        *   Set "Name" to `testuser`.
        *   Set "Password" to `testpass`.
        *   Set "Service" to `pppoe`.
        *   Click "Apply" and "OK".
*   **Effect:** This creates a local user database entry. In this example the service is `pppoe`, but it could be `pptp`, or other PPP services.

### Step 3: Configure a PPP Server

*   **Before:** No PPP server is configured, clients will be unable to connect.
*   **Action:** Configure a basic PPPoE server on `ether-29`.
*   **CLI Example:**
    ```mikrotik
     /interface pppoe-server server add interface=ether29 enabled=yes service-name=pppoe-server
    ```
*   **Winbox:**
    *   Navigate to *PPP* in the left menu.
    *   Select the *PPPoE Servers* tab.
    *   Click the "+" button.
    *   In the new window:
        *   Set "Interface" to `ether29`.
        *   Check the "Enabled" checkbox.
        *   Set "Service Name" to `pppoe-server`.
        *   Click "Apply" and "OK".
*   **Effect:** This enables the PPPoE server on interface `ether-29` for the previously defined `pppoe` service and `pppoe-server` service name.

### Step 4: Set the PPP Profile

* **Before**: No profile exists for the ppp connection.
* **Action**: Set IP address for PPP profile.
* **CLI Example:**
```mikrotik
 /ppp profile add name="ppp-profile" local-address=225.150.229.1 remote-address=225.150.229.2-225.150.229.254
 ```
* **Winbox**:
   * Navigate to *PPP* in the left menu.
   * Select the *Profiles* tab.
   * Click the "+" button.
   * In the new window:
        * Set "Name" to `ppp-profile`.
        * Set "Local Address" to `225.150.229.1`.
        * Set "Remote Address" to `225.150.229.2-225.150.229.254`.
        * Click "Apply" and "OK".

* **Effect**: Creates a profile which define the IP pool when PPP users are authenticated.

### Step 5: Set PPP profile to users
* **Before**: User is not using a profile.
* **Action**: Set the `ppp-profile` to user `testuser`.
* **CLI Example:**
```mikrotik
 /ppp secret set testuser profile=ppp-profile
```
* **Winbox:**
    *   Navigate to *PPP* in the left menu.
    *   Select the *Secrets* tab.
    *   Double-click on `testuser`.
    *   In the new window:
        *   Set "Profile" to `ppp-profile`.
        *   Click "Apply" and "OK".

* **Effect**: The PPP user will be using the specified profile, thus IP addresses will be assigned from the specified range.

## Complete Configuration Commands

Here's the complete set of MikroTik CLI commands:

```mikrotik
/interface ethernet enable ether29
/ppp secret add name=testuser password=testpass service=pppoe
/interface pppoe-server server add interface=ether29 enabled=yes service-name=pppoe-server
/ppp profile add name="ppp-profile" local-address=225.150.229.1 remote-address=225.150.229.2-225.150.229.254
/ppp secret set testuser profile=ppp-profile
```

**Parameter Explanations:**

| Command                  | Parameter         | Description                                                                            |
|--------------------------|-------------------|----------------------------------------------------------------------------------------|
| `/interface ethernet enable` | `ether29`    | The name of interface to enable.
| `/ppp secret add`       | `name`          | Username for PPP authentication                                                        |
|                          | `password`      | Password for PPP authentication                                                        |
|                          | `service`         | The service that uses this secret. Examples: `pppoe`, `pptp`.   |
| `/interface pppoe-server server add` | `interface`       | The interface to run the PPPoE server on                                                  |
|                          | `enabled`         |  Enable or disable the server (`yes` or `no`)                                                               |
|                          | `service-name`| The name of service which will appear in client, in this case `pppoe-server`.
| `/ppp profile add`       | `name`          | The name of PPP profile.
|                          | `local-address`      | The local address of ppp connection.
|                          | `remote-address`         | The range of addresses to be assigned to remote clients.  |
| `/ppp secret set`       | `name`          | The name of the user to modify.
|                          | `profile`      | The profile to be assigned to this user.   |

## Common Pitfalls and Solutions

*   **Authentication Failures:**
    *   **Problem:** Clients cannot connect with "Invalid Username/Password" error.
    *   **Solution:** Double-check the username and password on both the client and the router. Verify the `service` is correctly configured in the `/ppp secret` config.
*   **Interface Not Active:**
    *   **Problem:** Clients cannot connect, server does not respond.
    *   **Solution:** Ensure the `ether-29` interface is enabled. Look for the 'R' or 'r' flag in the `/interface ethernet print` output.
*   **IP Address Conflicts:**
    *   **Problem:** Clients connected via PPP cannot access the internet or have IP conflicts.
    *   **Solution:** Ensure the `local-address` and `remote-address` ranges do not conflict with other IP subnets in your network.
*  **Service Mismatch**:
    * **Problem**: Client connection fails because client service does not match with user's `service`.
    * **Solution**: Ensure that the server's service is the same as the `service` defined in `/ppp secret`. Also, client must use this service name in their connection configuration. For example in the example above, user `testuser` is using `pppoe` service, thus the server must have an `pppoe-server` service enabled.

## Verification and Testing Steps

1.  **Client Connection:** Attempt to connect using a PPP client (e.g., Windows VPN client, macOS Network connection, etc.) using the `testuser` and `testpass` credentials, using `pppoe-server` as the service name. Ensure that the client is set to the correct interface (ether-29 in this case).
2.  **Interface Status:**
    *   **CLI:** Use `/interface pppoe-server server print` to view the server status. Look for a new active interface related to the authenticated client.
    *   **Winbox:** Navigate to *PPP* -> *Active Connections* to view the connected clients and their assigned IP.
3.  **Ping Test:** After connecting, ping the router's IP (in this case `225.150.229.1`) from the client to verify reachability.
    ```bash
    ping 225.150.229.1
    ```
4.  **Torch:** Use MikroTik's torch tool to monitor traffic on interface ether-29 during connection:
    ```mikrotik
    /tool torch interface=ether29
    ```
    This will show the ongoing packet flow.

## Related Features and Considerations

*   **RADIUS:** For larger environments, use a RADIUS server for authentication, authorization, and accounting. This would involve configuring the `/ppp aaa` settings to point to your RADIUS server.
*   **VPNs (PPTP, L2TP, SSTP, OpenVPN):** This setup can be extended to configure other VPN types. Each VPN type has slightly different configurations but similar underlying principles.
*  **Firewall Rules:**  Implement appropriate firewall rules to control traffic to and from the PPP client subnet for security.
*  **QoS**: Set up QoS (Quality of Service) rules to prioritize certain types of traffic for optimal performance for PPP connections.

## MikroTik REST API Examples (if applicable)

MikroTik RouterOS does not support REST API for all operations. However, some specific functions can be performed via the API. In the context of AAA, here is how to create and modify a PPP secret using the API:

*   **API Endpoint:**  `/ppp/secret`
*   **Request Method:** POST (for creating), PUT (for modifying)

**Example: Creating a PPP Secret (POST request)**

*   **Endpoint:** `https://<router_ip>/rest/ppp/secret`
*   **Method:** POST
*   **JSON Payload:**
    ```json
    {
        "name": "apiuser",
        "password": "apipassword",
        "service": "pppoe"
    }
    ```

*   **Example curl command**
    ```bash
    curl -k -u "apiuser:apipassword" -H "Content-Type: application/json" -X POST -d '{"name":"apiuser","password":"apipassword","service":"pppoe"}' https://<router_ip>/rest/ppp/secret
    ```
    (You would need to create API user beforehand)

*   **Expected Response (201 Created):**

    ```json
    {
    	".id": "*1",
    	"name": "apiuser",
    	"password": "apipassword",
    	"service": "pppoe",
        "profile": "default",
        "comment": ""
    }
    ```

*   **Error Handling:** If you receive an error, check the response for error messages.
* **Example: Modify a PPP Secret (PUT request)**

*   **Endpoint:** `https://<router_ip>/rest/ppp/secret/*1` (assuming the ID is `*1` obtained from previous operation)
*   **Method:** PUT
*   **JSON Payload:**
    ```json
        {
        "password": "newapipassword",
        "profile": "ppp-profile"
        }
    ```
*  **Example curl command**
```bash
    curl -k -u "apiuser:apipassword" -H "Content-Type: application/json" -X PUT -d '{"password":"newapipassword","profile": "ppp-profile"}' https://<router_ip>/rest/ppp/secret/*1
```
*   **Expected Response (200 OK):**

    ```json
    {
    	".id": "*1",
    	"name": "apiuser",
    	"password": "newapipassword",
    	"service": "pppoe",
        "profile": "ppp-profile",
        "comment": ""
    }
    ```
*   **Error Handling:** If you receive an error, check the response for error messages.
    For example, 400 Bad Request error would indicate that JSON is not well-formed. 404 Not Found indicates that no object with the provided id was found.

**Notes:**
*    The router must be configured to allow API access. This involves enabling the "api" or "api-ssl" service in `/ip service` .
*    The "apiuser" user must have sufficient permissions to make changes to PPP secrets.

## Security Best Practices

*   **Strong Passwords:** Use strong, unique passwords for PPP users. Do not use the example password provided in this documentation (`testpass`).
*   **Encryption:** Enable encryption for PPP connections (MPPE for PPTP) to protect sensitive data. For PPPoE, the PPPoE protocol itself does not have any encryption, so if your connection goes through an unsafe network, consider setting up an IPsec tunnel within the pppoe.
*   **Firewall:** Implement strict firewall rules to only allow necessary traffic on the `ether-29` interface and the PPP interface.
*   **Rate Limiting:** Use `ppp profile` rate limiting to limit the bandwidth of each user for the PPP service.
*   **Keep RouterOS Updated:** Always use the latest stable version of RouterOS to ensure security patches are applied.

## Self Critique and Improvements

*   **Limited AAA Functionality**: This basic setup uses the built-in user database which is not scalable. Moving to RADIUS would offer more advanced features such as centralized user management, and support for different authentication methods.
*   **Hardcoded IP Addresses:** The example provided hardcoded ip addresses, which is fine for basic setups. This should be migrated to dhcp/ip-pool for dynamic IP assignments.
*   **Limited Security:** Basic configurations provide minimal security. Adding encryption for PPP connections is highly recommended.
*   **Missing QoS:** The example provided lacks traffic shaping and prioritization.
*  **No Logging:** This example provides no specific logging instructions. This should be implemented when the PPP interface is used in production environment.

## Detailed Explanations of Topic

**AAA (Authentication, Authorization, Accounting)**

*   **Authentication:** Verifying the identity of a user or device (e.g., username/password).
*   **Authorization:** Determining what a user or device is allowed to access or do.
*   **Accounting:** Tracking user activity and resource usage.

In the context of PPP, AAA is used to:

1.  **Authenticate:** Verify the credentials of the client trying to connect.
2.  **Authorize:** Grant the client access to the network resources based on their identity.
3.  **Account:** Keep track of the client's session information (e.g., connection time, data usage).

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS:**
    *   **Local:** Simple to configure for small networks. Lacks scalability and advanced features like per-user accounting, and centralized user management. Suitable for basic setups.
    *   **RADIUS:** More complex to set up but offers greater flexibility, scalability, and better security. Suitable for larger environments where advanced authentication/authorization methods are needed.
*   **Encryption:**
    *   **No Encryption:** Faster, but highly insecure. Data transmitted is in cleartext.
    *   **Encryption:** Significantly more secure (if configured correctly). Adds overhead for the encryption/decryption process.
*  **Static IP Assignment**: Static ip addresses are easier to setup and maintain for small scale setups, but for large scale setups with dynamic ip pools, they do not scale.
* **Service Name**: In PPPoE connections the service name is optional, however, it is recommended to define a `service-name` for each server to easily identify the server and its usage in client settings.

## Configuration for Specific RouterOS Versions

This configuration is valid for RouterOS 6.48 and newer. There are no major changes needed for most of the common PPP AAA configurations between 6.x and 7.x RouterOS versions. However, the API is significantly different in RouterOS 7.x, it is recommended to research the new REST api if working with version 7.

I hope this detailed technical document is helpful and provides a comprehensive guide to setting up PPP AAA in your MikroTik RouterOS environment!
