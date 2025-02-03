## Bridge Setup in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

In this configuration scenario, we want to create a bridge that connects two physical interfaces on a MikroTik router. The bridge will allow packets to pass between the two interfaces, creating a simple network segment.

### Step-by-Step Implementation

**1. Identify Interfaces:**
- Determine the names of the two physical interfaces you want to bridge. For example, `ether1` and `ether2`.

**2. Create Bridge:**
- Go to the Bridge menu in Winbox or issue the following command:
```
/interface bridge add name=mybridge
```
Replace `mybridge` with a suitable name for your bridge.

**3. Add Interfaces to Bridge:**
- Add the two physical interfaces to the bridge by going to the Ports tab in the bridge's configuration and dragging and dropping the interfaces onto the bridge name.
- Alternatively, use the following command:
```
/interface bridge port add bridge=mybridge interface=ether1
/interface bridge port add bridge=mybridge interface=ether2
```

**4. Enable Bridge:**
- Click the Enable checkbox in the bridge's configuration or run the command:
```
/interface bridge set mybridge enabled=yes
```

### Complete Configuration Commands

```
/interface bridge add name=mybridge
/interface bridge port add bridge=mybridge interface=ether1
/interface bridge port add bridge=mybridge interface=ether2
/interface bridge set mybridge enabled=yes
```

### Common Pitfalls and Solutions

- **Interfaces not in the same VLAN:** Ensure that the interfaces you are bridging are in the same VLAN.
- **Traffic not passing:** Check if the interfaces have correct IP addresses and are up and running. Verify the bridge forwarding.
- **Loopback Traffic:** If the bridge is not forwarding traffic, check for any loopback interfaces or other misconfigurations that may be causing loops.

### Verification and Testing Steps

- **Ping from one interface to another:** Test connectivity between the two interfaces by pinging from one to the other.
- **Check ARP Table:** Ensure that the bridge is updating the ARP table correctly. Use the command `/ip arp print` to check.
- **Check Traffic:** Monitor network traffic using tools like Wireshark or the RouterOS Traffic Flow tool to verify that packets are flowing through the bridge.

### Related Features and Considerations

- **VLANs:** You can configure VLANs on the bridge to create isolated network segments within the bridge.
- **Firewall Rules:** Apply firewall rules to the bridge to control traffic flow and enhance security.
- **Bridge Forwarding:** Configure bridge forwarding options to optimize packet forwarding within the bridge.

### MikroTik REST API Examples

**Create Bridge:**

**API Endpoint:** `/interface/bridge`

**Request Method:** POST

**JSON Payload:**
```json
{
  "name": "mybridge"
}
```

**Example Response:**

```json
{
  "return": {
    "name": "mybridge"
  }
}
```

**Add Interface to Bridge:**

**API Endpoint:** `/interface/bridge/port`

**Request Method:** POST

**JSON Payload:**
```json
{
  "bridge": "mybridge",
  "interface": "ether1"
}
```

**Example Response:**

```json
{
  "return": {
    "bridge": "mybridge",
    "interface": "ether1"
  }
}
```