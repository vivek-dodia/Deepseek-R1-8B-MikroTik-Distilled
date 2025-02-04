Okay, let's dive into a detailed configuration for RADIUS authentication on a MikroTik RouterOS device, focusing on the specifics you've outlined.

## Scenario Description:

This scenario addresses the need to authenticate users connecting to a MikroTik router via the `bridge-82` interface using a RADIUS server. This configuration is suitable for an ISP environment or any network where centralized user authentication is required for access control. We will be using the IP subnet 226.17.206.0/24 on `bridge-82`. While this is a basic setup, it forms the foundation for more complex configurations involving various user authentication methods such as Hotspot or PPP. The goal is to ensure only users authenticated by the RADIUS server can gain access to the network on `bridge-82`.

## Implementation Steps:

Here’s a step-by-step guide with explanations, MikroTik CLI examples, and before/after configurations:

### Step 1: Configure the Bridge Interface

First, ensure your bridge interface (`bridge-82`) exists and has the appropriate IP configuration. We'll create the bridge if it doesn't exist.

**Before Configuration:**

```
/interface bridge print
Flags: X - disabled, R - running
 #    NAME               MTU  MAC-ADDRESS       ADMIN-MAC        
```
*Assume the bridge interface does not exist*

**CLI Instructions:**

```
/interface bridge
add name=bridge-82
/interface bridge port
add bridge=bridge-82 interface=ether1 #replace ether1 with the correct interface
/ip address
add address=226.17.206.1/24 interface=bridge-82
```

**Explanation:**

*   `/interface bridge add name=bridge-82`:  Creates a new bridge interface named `bridge-82`.
*   `/interface bridge port add bridge=bridge-82 interface=ether1`: Adds `ether1` to the `bridge-82`. This should be replaced with your actual interface connected to your users.
*   `/ip address add address=226.17.206.1/24 interface=bridge-82`: Assigns the IP address 226.17.206.1/24 to the bridge interface, setting the network.

**After Configuration:**

```
/interface bridge print
Flags: X - disabled, R - running
 #    NAME               MTU  MAC-ADDRESS       ADMIN-MAC        
 0  R bridge-82          1500 xx:xx:xx:xx:xx:xx xx:xx:xx:xx:xx:xx

/interface bridge port print
Flags: X - disabled, I - inactive, D - dynamic
 #    INTERFACE     BRIDGE          HW        PRIORITY PATH-COST  INTERNAL-PRIORITY   
 0  ether1          bridge-82       yes        0        10          0

/ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE                      
 0  226.17.206.1/24    226.17.206.0   bridge-82
```

### Step 2: Configure RADIUS Client Settings

Next, add the RADIUS server settings.

**Before Configuration:**

```
/radius print
Flags: X - disabled, I - invalid
```

**CLI Instructions:**

```
/radius
add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=3
add address=192.168.88.10 secret="your_radius_secret" service=hotspot timeout=3
```

**Explanation:**

*   `/radius add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=3`: Adds the RADIUS server with IP 192.168.88.10 (replace with the correct server IP) using a shared secret "your_radius_secret", and set to authenticate using the ppp service. The timeout is set to 3 seconds.
*    `/radius add address=192.168.88.10 secret="your_radius_secret" service=hotspot timeout=3`: Adds the RADIUS server with IP 192.168.88.10 (replace with the correct server IP) using a shared secret "your_radius_secret", and set to authenticate using the hotspot service. The timeout is set to 3 seconds.

**After Configuration:**

```
/radius print
Flags: X - disabled, I - invalid
 #   ADDRESS         SECRET           SERVICE TIMEOUT
 0   192.168.88.10   your_radius_secr ppp    3
 1   192.168.88.10   your_radius_secr hotspot    3
```

### Step 3: Configure Firewall Rules (Optional, but Highly Recommended)

To secure the router, add firewall rules that allow only necessary RADIUS traffic. This step can be optional, but it is HIGHLY recommended.

**Before Configuration:**

```
/ip firewall filter print
Flags: X - disabled, I - invalid, D - dynamic
```

**CLI Instructions:**

```
/ip firewall filter
add chain=input protocol=udp dst-port=1812 src-address=192.168.88.10 action=accept comment="Allow RADIUS authentication"
add chain=input action=drop comment="Drop all other input traffic"
```

**Explanation:**

*   `add chain=input protocol=udp dst-port=1812 src-address=192.168.88.10 action=accept comment="Allow RADIUS authentication"`: Allows UDP traffic on port 1812 (RADIUS authentication port) originating from the RADIUS server.
*   `add chain=input action=drop comment="Drop all other input traffic"`: This is very important for security, it drops any traffic that is not specifically allowed. Note that adding this before adding other necessary rules (such as allowing SSH or Winbox access) will result in you locking yourself out of the router if you are using an external ip address. Always add a rule to allow your management access before adding this rule.

**After Configuration:**

```
/ip firewall filter print
Flags: X - disabled, I - invalid, D - dynamic
 0  chain=input action=accept protocol=udp src-address=192.168.88.10 dst-port=1812 comment="Allow RADIUS authentication"
 1  chain=input action=drop comment="Drop all other input traffic"
```

### Step 4: Configure Hotspot or PPP for RADIUS Authentication

Now, configure a method to use RADIUS authentication for your users. This example uses a Hotspot server for authentication.

**Before Configuration:**

```
/ip hotspot print
Flags: X - disabled, I - invalid
```

**CLI Instructions:**

```
/ip hotspot
add name=hotspot1 interface=bridge-82 profile=default
/ip hotspot profile
set default use-radius=yes
```

**Explanation:**

*   `/ip hotspot add name=hotspot1 interface=bridge-82 profile=default`: Creates a hotspot server on the `bridge-82` interface using the default profile.
*   `/ip hotspot profile set default use-radius=yes`: Configures the default hotspot profile to use RADIUS authentication.

**After Configuration:**

```
/ip hotspot print
Flags: X - disabled, I - invalid
 #   NAME     INTERFACE   PROFILE     ADDRESS-POOL
 0  hotspot1 bridge-82   default     none

/ip hotspot profile print
Flags: X - disabled, * - default
 0  * default name="default" hotspot-address=0.0.0.0/0 dns-name="" html-directory="hotspot" http-proxy=0.0.0.0:0
       radius-address=0.0.0.0/0 radius-port=1812 radius-accounting=no
       mac-cookie-timeout=0s idle-timeout=none keepalive-timeout=none
       rate-limit="" use-radius=yes login-by=cookie,http-chap,http-pap,https
```

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to implement the setup, with parameter explanations:

```
/interface bridge
add name=bridge-82
/interface bridge port
add bridge=bridge-82 interface=ether1
/ip address
add address=226.17.206.1/24 interface=bridge-82
/radius
add address=192.168.88.10 secret="your_radius_secret" service=ppp timeout=3
add address=192.168.88.10 secret="your_radius_secret" service=hotspot timeout=3
/ip firewall filter
add chain=input protocol=udp dst-port=1812 src-address=192.168.88.10 action=accept comment="Allow RADIUS authentication"
add chain=input action=drop comment="Drop all other input traffic"
/ip hotspot
add name=hotspot1 interface=bridge-82 profile=default
/ip hotspot profile
set default use-radius=yes
```

**Parameter Explanations:**

| Command        | Parameter     | Explanation                                                                      |
| -------------- | ------------- | -------------------------------------------------------------------------------- |
| `/interface bridge add` | name | Name of the bridge interface (e.g., `bridge-82`).                             |
| `/interface bridge port add` | bridge |  Bridge interface name to add the port to.    |
| `/interface bridge port add` | interface | Interface to add to the bridge. |
| `/ip address add`    | address       | IP address and subnet mask for the interface (e.g., `226.17.206.1/24`).         |
| `/ip address add`    | interface       | Interface the IP address should be assigned to.                              |
| `/radius add`      | address      | IP address of the RADIUS server.                                                 |
| `/radius add`      | secret       | Shared secret for communication with the RADIUS server.                           |
| `/radius add`      | service      | Service type that uses RADIUS (e.g., `ppp`, `hotspot`).                                    |
| `/radius add`      | timeout       | How long (in seconds) the router waits for a response from the RADIUS server before giving up.                       |
| `/ip firewall filter add`  | chain        | Firewall chain (`input`, `forward`, `output`).                              |
| `/ip firewall filter add`  | protocol     | IP protocol (`udp`, `tcp`, etc.).                                   |
| `/ip firewall filter add`  | dst-port     | Destination port number.                                                    |
| `/ip firewall filter add`  | src-address  | Source IP address or subnet.                                                  |
| `/ip firewall filter add`  | action       | Action to take (e.g., `accept`, `drop`).                                    |
| `/ip firewall filter add`  | comment       | Description of rule                                    |
| `/ip hotspot add`       | name         | Name for the Hotspot server.                                                |
| `/ip hotspot add`       | interface    | Interface the Hotspot server will operate on.                            |
| `/ip hotspot add`       | profile      | Hotspot profile to use (e.g., `default`).                               |
| `/ip hotspot profile set` | use-radius   | Enables/disables RADIUS authentication for the Hotspot profile.        |

## Common Pitfalls and Solutions:

*   **Incorrect RADIUS Secret:** Ensure the RADIUS secret on the MikroTik matches the RADIUS server.
    *   **Solution:** Double-check the secret on both devices and verify the encryption algorithm is compatible (e.g., MD5).
*   **Firewall Blocking RADIUS:** Firewall rules on the MikroTik or RADIUS server might block the traffic.
    *   **Solution:** Use `torch` or `/tool sniffer` to identify where packets are dropped and adjust firewall rules accordingly.
*   **RADIUS Server Not Responding:** The RADIUS server may be down or unreachable.
    *   **Solution:** Use ping or traceroute to check connectivity to the RADIUS server, or check the server logs for issues.
*   **Incorrect Service Type:**  If the wrong service is used in RADIUS client, the authentication may fail.
    *   **Solution**: Verify that the service in the RADIUS client on the MikroTik (ppp, hotspot, etc) matches the client configuration on the RADIUS server.
*   **Incorrect DNS Configuration:**  If the dns configuration is not correct, users may not be able to reach the login page.
     *   **Solution**: Check DNS configuration on both the server and the users machines.

**Security Issues:**
*   **Using default hotspot configuration:** Leaving the default configuration might be a security issue, change the default login page, and create a custom profile.
*   **Exposing RADIUS to public IP Addresses**: If your RADIUS server can be reached publicly, it might be a vulnerability. Make sure to only expose this on private networks.

**Resource Issues:**
*   Too many users trying to authenticate at once may use all router cpu and ram resources.
    *  **Solution:** If this is happening, consider using a more powerful router, or configure rate limits for the user access.

## Verification and Testing Steps:

1.  **Check Router Reachability:**  Confirm that users on the 226.17.206.0/24 subnet can reach the router's IP address (226.17.206.1). Use `ping 226.17.206.1` on a client in the same subnet.
2.  **Monitor Hotspot Log:** Use `/log print where topics~"hotspot"` to check if users are redirected to the hotspot login page. This will help diagnose any issues related to user connections and authentication attempts.
3.  **Monitor RADIUS Logs:** Check the RADIUS server logs for successful or failed authentication attempts.
4.  **Use Torch:** Employ `/tool torch interface=bridge-82` to check if the RADIUS traffic is reaching the router.
5.  **Use `/tool sniffer`:** Use the sniffer to capture packets, and check the RADIUS traffic.
6. **Attempt to Login:** Try to login to the hotspot using a valid user on the RADIUS server.
7. **Check RADIUS server logs:** If authentication fails, check the RADIUS server logs for details.

## Related Features and Considerations:

*   **Accounting:** Enable RADIUS accounting to track user sessions and data usage. Set `radius-accounting=yes` in the `/ip hotspot profile` settings.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy.
*   **Dynamic User Profiles:** Implement dynamic VLAN assignment or QoS based on user attributes received from the RADIUS server.
*  **VLANs:** Use VLANs to segregate traffic for different user groups.
*  **Guest Networks:** Create specific Hotspot configurations for guest networks.

**Real-world Impact:**

This setup enables centralized authentication for users connecting to the `bridge-82` interface. This is useful for managing user access in a controlled environment, such as an ISP or a large office building. When a user is authenticated by RADIUS, the router will allow them internet access, following the other rules that are in place. This also allows the operator to track user logins, accounting, and other important information.

## MikroTik REST API Examples (if applicable):

This example shows how to get the radius configuration using the MikroTik REST API:

**Endpoint:** `/radius`

**Method:** `GET`

**Request:**
No request body needed.

**Example cURL command:**
```bash
curl -k -u "api_user:api_password" https://your_router_ip/rest/radius
```

**Expected Response (JSON):**

```json
[
  {
    ".id": "*0",
    "address": "192.168.88.10",
    "secret": "your_radius_secret",
    "service": "ppp",
    "timeout": "3",
    "accounting": "no"
  },
  {
    ".id": "*1",
    "address": "192.168.88.10",
    "secret": "your_radius_secret",
    "service": "hotspot",
    "timeout": "3",
     "accounting": "no"
   }

]
```

**API Parameter Descriptions**

| Parameter      | Type  | Description                                                        |
| -------------- | ----- | ------------------------------------------------------------------ |
| `address`      | String| IP address of the RADIUS server.                                 |
| `secret`       | String| Shared secret for communication with the RADIUS server.               |
| `service`      | String| Service type (e.g., `ppp`, `hotspot`).                             |
| `timeout`      | Integer| Timeout in seconds for RADIUS responses.  |
|`accounting` | String  | "yes" or "no" to enable accounting. |

**Error Handling:**
*   A status code of 200 means a successful call.
*   Error status codes (4xx, 5xx) will be returned with an error message in json format.

## Security Best Practices

*   **Strong RADIUS Secret:** Use a strong, randomly generated RADIUS secret. Avoid simple or default secrets.
*   **Restrict Access to RADIUS Server:** Ensure the RADIUS server is only accessible from trusted networks. Do not expose the radius server to the public internet.
*   **Monitor Logs:** Regularly monitor both the MikroTik and RADIUS server logs for unusual activity.
*   **Limit Services:** Do not use more services than you need on the router. Disable unnecessary services.
*   **Use a Management VLAN:** Ensure that management access to the router is on a different VLAN or interface, that is not exposed to the users.

## Self Critique and Improvements

**Critique:**

*   **Basic Setup:** This is a very basic setup, a more complex setup should consider features like dynamic VLANs, QoS, per-user bandwidth limits.
*   **Firewall Complexity:** The firewall rules are basic. Real-world setups should have more complex filter rules and connection tracking for proper security.
*   **Lack of Logging:** Log levels should be customized to capture important security-related information, and the logs should be sent to a central logging server.

**Improvements:**

*   **Dynamic User Management:** Configure user groups and use RADIUS to dynamically apply these groups.
*   **Advanced Firewall Rules:** Add more firewall rules to protect the router and the network further.
*   **Traffic Shaping:** Add traffic shaping and Quality of service (QoS) rules to manage and limit bandwidth usage per user.
*   **Automated Configuration:** Use configuration management tools for easier deployments of many routers.
*   **Central Logging System:** Route all logs to a central location for easier auditing and analysis.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service)**

RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users attempting to access network resources. It’s widely used for managing user access in various network environments.

*   **Authentication:** Verifies user credentials (username and password).
*   **Authorization:** Determines what resources a user can access.
*   **Accounting:** Tracks user session information, such as start time, end time, data usage, etc.

RADIUS operates on a client-server model. The RADIUS client (e.g., MikroTik router) sends authentication requests to the RADIUS server. The server verifies the credentials and responds with acceptance or rejection. RADIUS uses UDP as its transport protocol, and the most common ports are 1812 for authentication, and 1813 for accounting. It should be noted that there is also a TCP implementation, but it is less common.

## Detailed Explanation of Trade-offs

**Different RADIUS settings:**

*   **Timeout:** A short timeout will mean the user may have problems authenticating with the server. If the timeout is too high, it will increase the time that users must wait when there is a RADIUS authentication failure.
*   **Service Type:** Choosing the correct service type is important, as this is the configuration that the RADIUS server will be expecting. If using the wrong service type, authentication will fail.
*   **Firewall Rules**:  A very restrictive firewall will greatly increase the security of the router, but it may be difficult to diagnose if it is not configured correctly, and may cause the router to stop working.
*   **Accounting**:  If accounting is enabled, then session information can be tracked, such as session start time, end time, data usage, but this can put a higher load on the RADIUS server, and the MikroTik router.

## Configuration for Specific RouterOS Versions:

The provided configuration is compatible with RouterOS versions 6.48 and 7.x. There are no specific commands that differ between these two versions that would impact this setup. However, you should keep an eye out for changes in newer versions of RouterOS. For example, new commands and functionalities are always being added.

This comprehensive documentation should give you a solid foundation for implementing RADIUS authentication on your MikroTik router. Remember to test thoroughly and monitor your setup after deployment.
