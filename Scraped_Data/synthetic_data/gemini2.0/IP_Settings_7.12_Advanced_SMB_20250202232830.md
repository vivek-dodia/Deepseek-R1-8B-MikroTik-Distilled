## IP Settings

### IPv4 Addressing

**Configuration Scenario:** Assign an IPv4 address and network mask to an interface.

**Step-by-Step Implementation:**

1. Navigate to **IP > Addresses** in WinBox.
2. Click **Add** to create a new IP address assignment.
3. Select the interface in the **Interface** field.
4. Enter the IPv4 address in the **Address** field.
5. Enter the network mask in the **Network** field.

**Complete Configuration Commands:**

```
/ip address
add address=192.168.1.10/24 interface=ether1
```

**Common Pitfalls and Solutions:**

* **IP address conflict:** Ensure the assigned IP address is unique within the network.
* **Invalid network mask:** Verify that the network mask is valid for the IPv4 address range.

### IPv6 Addressing

**Configuration Scenario:** Assign an IPv6 address and prefix length to an interface.

**Step-by-Step Implementation:**

1. Navigate to **IP > Addresses** in WinBox.
2. Click **Add** to create a new IP address assignment.
3. Select the interface in the **Interface** field.
4. Enter the IPv6 address in the **Address** field.
5. Enter the prefix length in the **Prefix Length** field.

**Complete Configuration Commands:**

```
/ip address
add address=fe80::1/64 interface=ether1
```

**Common Pitfalls and Solutions:**

* **Invalid IPv6 address:** Ensure the assigned IPv6 address is valid and uses the correct format.
* **Duplicate IPv6 address:** Verify that the assigned IPv6 address is unique within the network.

### IP Pools

**Configuration Scenario:** Create an IP pool to assign dynamic IP addresses to clients.

**Step-by-Step Implementation:**

1. Navigate to **IP > Pool** in WinBox.
2. Click **Add** to create a new IP pool.
3. Enter a name for the pool in the **Name** field.
4. Enter the starting IP address in the **Range Start** field.
5. Enter the ending IP address in the **Range End** field.
6. Select the interface where the pool will be used in the **Interface** field.

**Complete Configuration Commands:**

```
/ip pool
add name=my-ip-pool range=192.168.1.10-192.168.1.255 interface=ether1
```

**Common Pitfalls and Solutions:**

* **Insufficient IP addresses:** Ensure the IP pool range contains enough IP addresses for the expected number of clients.
* **Address conflict:** Make sure the IP pool does not overlap with any existing IP address assignments.

### IP Routing

**Configuration Scenario:** Configure a static route to a remote network.

**Step-by-Step Implementation:**

1. Navigate to **IP > Routes** in WinBox.
2. Click **Add** to create a new route.
3. Enter the destination network address in the **Dst. Address** field.
4. Enter the network mask in the **Dst. Mask** field.
5. Enter the gateway IP address in the **Gateway** field.

**Complete Configuration Commands:**

```
/ip route
add dst-address=192.168.2.0/24 gateway=192.168.1.1
```

**Common Pitfalls and Solutions:**

* **Routing loop:** Ensure that multiple routes to the same destination network do not exist.
* **Black hole routing:** Verify that the gateway IP address is reachable and the route is valid.

### MAC Server

**Configuration Scenario:** Enable MAC server to learn and forward traffic based on MAC addresses.

**Step-by-Step Implementation:**

1. Navigate to **IP > MAC Server** in WinBox.
2. Enable **Use MAC Server** checkbox.

**Complete Configuration Commands:**

```
/ip mac-server
set use-mac-server=yes
```

**Common Pitfalls and Solutions:**

* **Port security:** Ensure that the switch ports connected to clients do not have port security enabled, as it can interfere with MAC server learning.
* **DHCP snooping:** Disable DHCP snooping on the switch ports to prevent conflicts with MAC server learning.

### RoMON

**Configuration Scenario:** Configure RoMON to monitor the router's health and send notifications.

**Step-by-Step Implementation:**

1. Navigate to **System > RoMON** in WinBox.
2. Enable **Enable RoMON** checkbox.
3. Enter an email address in the **Syslog Notification Email Address** field.

**Complete Configuration Commands:**

```
/system romon
set enabled=yes syslog-notification-email-address=admin@example.com
```

**Common Pitfalls and Solutions:**

* **Email setup:** Ensure that the email server is configured and accessible by the router.
* **Network connectivity:** Verify that the router has network connectivity to send RoMON notifications.

### WinBox

**Configuration Scenario:** Configure WinBox to connect to the router remotely.

**Step-by-Step Implementation:**

1. Launch WinBox and click **File > Connect**.
2. Enter the IP address or hostname of the router in the **Address** field.
3. Enter the username and password for accessing the router.
4. Click **Connect** to establish the connection.

**Complete Configuration Commands:**

```
(Not applicable for WinBox configuration)
```

**Common Pitfalls and Solutions:**

* **Firewall rule:** Ensure that the router's firewall allows access to WinBox from the remote client.
* **User permissions:** Verify that the user has sufficient permissions to access the router via WinBox.

### Certificates

**Configuration Scenario:** Import a certificate for use in SSL/TLS connections.

**Step-by-Step Implementation:**

1. Navigate to **System > Certificates** in WinBox.
2. Click **Import**.
3. Browse to the certificate file and click **Open**.
4. Enter a name for the certificate in the **Certificate Name** field.

**Complete Configuration Commands:**

```
/certificate
import file-name=my-certificate.crt
```

**Common Pitfalls and Solutions:**

* **Certificate format:** Ensure that the certificate is in the correct format (e.g., PEM or DER).
* **Certificate validity:** Verify that the certificate is valid and not expired.

### PPP AAA

**Configuration Scenario:** Configure PPP AAA to authenticate and authorize users connecting via PPP.

**Step-by-Step Implementation:**

1. Navigate to **PPP > AAA** in WinBox.
2. Enable **Use AAA** checkbox.
3. Select a secret method in the **Secret Hashes** dropdown.
4. Enter the secret in the **Secret** field.

**Complete Configuration Commands:**

```
/ppp aaa
set use-aaa=yes secret-hashes=pap2 secret=my-secret
```

**Common Pitfalls and Solutions:**

* **Secret security:** Ensure that the PPP secret is secure and not shared publicly.
* **PPP profile:** Verify that the PPP profile used by clients is configured to use the AAA service.

### RADIUS

**Configuration Scenario:** Configure RADIUS to authenticate and authorize users connecting via RADIUS.

**Step-by-Step Implementation:**

1. Navigate to **System > RADIUS** in WinBox.
2. Enable **Use RADIUS** checkbox.
3. Enter the RADIUS server IP address in the **Address** field.
4. Enter the RADIUS server port in the **Port** field.
5. Enter the RADIUS shared secret in the **Secret** field.

**Complete Configuration Commands:**

```
/system radius
set use-radius=yes address=192.168.1.10 port=1812 secret=my-secret
```

**Common Pitfalls and Solutions:**

* **RADIUS server availability:** Ensure that the RADIUS server is accessible by the router.
* **RADIUS profile:** Verify that the RADIUS profile used by clients is configured to use the correct RADIUS server settings.

### User / User Groups

**Configuration Scenario:** Create a user and add them to a user group.

**Step-by-Step Implementation:**

1. Navigate to **System > Users** in WinBox.
2. Click **Add** to create a new user.
3. Enter a username in the **Name** field.
4. Enter a password in the **Password** field.
5. Navigate to **System > User Groups** in WinBox.
6. Click **Add** to create a new user group.
7. Enter a name for the group in the **Name** field.
8. Add the user to the group by clicking **Add** in the **Members** tab.

**Complete Configuration Commands:**

```
/user
add name=my-user password=my-password
/user group
add name=my-user-group members=my-user
```

**Common Pitfalls and Solutions:**

* **Password security:** Ensure that the user's password is secure and not shared publicly.
* **User permissions:** Verify that the user group has the appropriate permissions to access the router's functionality.

### Bridging and Switching

**Configuration Scenario:** Configure a bridge to connect multiple interfaces into a single logical network.

**Step-by-Step Implementation:**

1. Navigate