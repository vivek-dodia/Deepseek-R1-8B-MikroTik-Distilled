**1. Configuration Scenario and Requirements**

* **Goal**: Configure a MAC server on a MikroTik RouterOS 7.11 device to track and manage device MAC addresses.
* **Requirements**:
    * MikroTik RouterOS 7.11 (or later) device
    * List of MAC addresses to manage

**2. Step-by-Step Implementation**

1. Log in to the RouterOS device via WinBox or SSH.
2. Navigate to **IP > MAC Server**.
3. Click the **Add (+)** button to create a new MAC server.
4. Configure the following parameters:
    * **Server**: Choose the appropriate interface for receiving MAC address updates.
    * **Name**: Assign a descriptive name to the MAC server.
    * **Timeout**: Specify the number of seconds after which inactive MAC addresses will be removed from the server.
5. Click **Apply** to save the MAC server configuration.

**3. Complete Configuration Commands**

```
/ip mac-server add server=ether1 name=my-mac-server timeout=300
```

**4. Common Pitfalls and Solutions**

* **Incorrect server selection**: Ensure that the selected interface is receiving MAC address updates.
* **Timeout value too low**: If the timeout value is too low, MAC addresses may be removed prematurely.
* **No active MAC addresses**: Verify that devices are connected to the RouterOS device and sending MAC address updates.

**5. Verification and Testing Steps**

* Use the **/ip mac-server print** command to view the list of MAC addresses tracked by the MAC server.
* Send MAC address updates from devices and observe if they are added to the MAC server.
* Delete a MAC address from the MAC server and verify that it is removed after the timeout period.

**6. Related Features and Considerations**

* **Static MAC addresses**: Static MAC addresses can be added to the MAC server to prevent them from being removed due to inactivity.
* **MAC address learning**: The MAC server can be used in conjunction with MAC address learning on switches to track MAC addresses on the network.
* **IPv6 support**: The MAC server also supports IPv6 MAC addresses.

**7. MikroTik REST API Examples**

**Endpoint**: `/ip/mac-server`

**Request Method**: `GET`

**Example JSON Payload**:

```json
{
  "server": "ether1",
  "name": "my-mac-server",
  "timeout": 300
}
```

**Expected Response**:

```json
[
  {
    ".id": "1",
    "name": "my-mac-server",
    "server": "ether1",
    "timeout": 300
  }
]
```

**8. Comprehensive Examples and Explanations**

**a. IP Addressing (IPv4 and IPv6)**

* **Address allocation**: Use `/ip address add address=<IP address>/<prefix> interface=<interface>` to assign IP addresses to interfaces.
* **DHCP server**: Configure a DHCP server using `/ip dhcp-server add interface=<interface> address-pool=<pool name>`.
* **NAT**: Enable NAT traversal with `/ip firewall nat add chain=srcnat action=masquerade out-interface=<interface>`.

**b. IP Pools**

* **Create a pool**: Use `/ip pool add name=<pool name> ranges=<IP range>`.
* **Assign a pool**: Associate a pool with an interface using `/ip address add address=<pool name> interface=<interface>`.

**c. IP Routing**

* **Static routes**: Add static routes with `/ip route add dst-address=<destination> gateway=<gateway address>`.
* **Dynamic routing**: Enable OSPF routing with `/routing ospf add area=<area id> interface=<interface>`.
* **Policy routing**: Prioritize traffic based on rules using `/ip route add routing-mark=<mark> gateway=<gateway address>`.

**d. IP Settings**

* **Interface configuration**: Set IP settings for interfaces using `/ip address add address=<IP address>/<prefix> interface=<interface>`.
* **DNS servers**: Configure DNS servers with `/ip dns set servers=<DNS server addresses>`.
* **Default gateway**: Set the default gateway with `/ip route add gateway=<gateway address>`.

**e. MAC Server**

* **See sections 2-7 above.**

**f. RoMON**

* **Enable RoMON**: Enable the remote monitoring feature with `/system romon add enabled=yes`.
* **View RoMON data**: Retrieve RoMON data using the WinBox tool or the `/romon monitor` command.

**g. WinBox**

* **Installation**: Download and install WinBox from mikrotik.com/download.
* **Connection**: Establish a connection to the RouterOS device using the IP address or hostname.
* **Usage**: Navigate through the RouterOS menus and configure settings using a graphical interface.

**h. Certificates**

* **Generate a certificate**: Use `/certificate add common-name=<certificate name>` to generate a self-signed certificate.
* **Import a certificate**: Import an existing certificate using `/certificate import file-name=<certificate file path>`.

**i. PPP AAA**

* **Configure AAA**: Set up AAA settings for PPP with `/ppp aaa set user=<user name> password=<password> service=<service name>`.
* **Create a profile**: Create a PPP profile with `/ppp profile add name=<profile name> remote-address=<remote address> local-address=<local address>`.

**j. RADIUS**

* **Configure RADIUS**: Set up RADIUS authentication with `/radius add server=<server address> secret=<secret>`.
* **Create a RADIUS profile**: Create a RADIUS profile with `/radius profile add name=<profile name> server=<server address>`.

**k. User / User Groups**

* **Create a user**: Use `/user add name=<user name> group=<group name> password=<password>`.
* **Create a group**: Create a user group with `/user group add name=<group name>`.

**l. Bridging and Switching**

* **Create a bridge**: Create a bridge interface with `/bridge add name=<bridge name>`.
* **Add ports to a bridge**: Assign ports to a bridge with `/interface bridge port add bridge=<bridge name> interface=<interface name>`.
* **Enable spanning tree**: Enable spanning tree on a bridge with `/bridge port set bridge=<bridge name> interface=<interface name> spanning-tree=yes`.

**m. MACVLAN**

* **Create a MACVLAN interface**: Create a MACVLAN interface with `/interface macvlan add name=<macvlan name> parent=<parent interface>`.
* **Assign an address**: Assign an IP address to the MACVLAN interface with `/ip address add address=<IP address>/<prefix> interface=<macvlan name>`.

**n. L3 Hardware Offloading**

* **Configure offloading**: Enable offloading on an interface with `/interface ethernet set name=<interface name> hardware-offloading=all`.
* **Verify offloading**: Use `/interface ethernet monitor-traffic` to check if offloading is working.

**o. MACsec**

* **Enable MACsec**: Enable MACsec on an interface with `/interface macsec add name=<interface name> mode=encrypt`.
* **Configure keys**: Set up MACsec keys with `/macsec key add id=<key id> key=<key>`.

**p. Quality of Service**

* **Create a queue**: Create a queue with `/queue type=simple name=<queue name> parent=<parent queue>`.
* **Configure traffic shaping**: Limit traffic on a queue with `/queue simple set name=<queue name> max-limit=<limit>`
* **Assign queues to interfaces**: Assign queues to interfaces with `/interface ethernet set name=<interface name> queue=<queue name>`.

**q. Switch Chip Features**

* **Configure VLANs**: Create VLANs on switches with `/vlan add name=<vlan name> interface=<interface name> tagged=yes`.
* **Configure ports**: Set port settings on switches with `/interface switch port set interface=<interface name> name=<port name>`.

**r. VLAN**

* **Create a VLAN**: Create a VLAN with `/vlan add name=<vlan name> interface=<interface name> tagged=yes`.
* **Assign ports to a VLAN**: Assign ports to a VLAN with `/interface bridge port add bridge=<vlan name> interface=<interface name> vlan-id=<vlan id>`.

**s. VXLAN**

* **Create a VXLAN interface**: Create a VXLAN interface with `/interface vxlan add name=<vxlan name> local-address=<local address> remote-address=<remote address>`.
* **Assign an address**: Assign an IP address to the VXLAN interface with `/ip address add address=<IP address>/<prefix> interface=<vxlan name>`.

**t. Firewall and Quality of Service**

* **Filter traffic**: Create firewall rules with `/ip firewall add chain=input action=drop`.
* **Rate limit connections**: Limit the number of connections with `/queue type=codel name=<queue name> parent=<parent queue>`.
* **Prioritize traffic**: Mark traffic for prioritization with `/queue type=mark name=<queue name> parent=<parent queue> target=<mark>`.

**u. IP Services (DHCP, DNS, SOCKS, Proxy)**

* **Configure DHCP**: Set up a DHCP server