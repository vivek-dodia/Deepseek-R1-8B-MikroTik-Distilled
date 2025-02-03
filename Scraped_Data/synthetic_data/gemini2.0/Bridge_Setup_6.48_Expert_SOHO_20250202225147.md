## Bridge Setup in RouterOS 6.48

### Configuration Scenario and Requirements

- Create a bridge to connect two physical interfaces.
- Configure the bridge with an IP address and gateway.
- Allow traffic to pass between the two interfaces.

### Step-by-Step Implementation

1. **Create the bridge:**
```
/interface bridge add name=br0
```

2. **Add interfaces to the bridge:**
```
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
```

3. **Configure the bridge IP address and gateway:**
```
/ip address add address=192.168.1.1/24 interface=br0
/ip route add gateway=192.168.1.254
```

4. **Allow traffic between the interfaces:**
```
/ip firewall filter add action=accept chain=input in-interface=ether1 out-interface=ether2
/ip firewall filter add action=accept chain=input in-interface=ether2 out-interface=ether1
```

### Complete Configuration Commands

```
/interface bridge add name=br0
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
/ip address add address=192.168.1.1/24 interface=br0
/ip route add gateway=192.168.1.254
/ip firewall filter add action=accept chain=input in-interface=ether1 out-interface=ether2
/ip firewall filter add action=accept chain=input in-interface=ether2 out-interface=ether1
```

### Common Pitfalls and Solutions

- **Interfaces not added to the bridge:** Ensure that the interfaces you want to connect are added to the bridge using the `/interface bridge port add` command.
- **Incorrect bridge IP address or gateway:** Check the IP address and gateway configured on the bridge. They should be in the same subnet as the devices you want to connect.
- **Firewall rules blocking traffic:** Verify that the firewall rules allow traffic between the interfaces. Ensure that the chain, in-interface, and out-interface parameters are configured correctly.

### Verification and Testing Steps

- **Test connectivity:** Ping the IP address of a device on the other interface.
- **Check firewall rules:** Run the `/ip firewall filter print` command to verify that the rules are in place and configured correctly.
- **Monitor traffic:** Use the `/interface monitor` command to monitor traffic passing through the bridge.

### Related Features and Considerations

- **Bonding:** Bridges can be bonded to create a single logical interface with increased bandwidth and redundancy.
- **VLANs:** VLANs can be used to segment traffic on the bridge into separate networks.
- **Security:** Configure firewall rules on the bridge to restrict access and protect the network.

### MikroTik REST API Examples

**Fetch bridge information:**

Endpoint: `/interface/bridge`

Request Method: GET

Example JSON Payload:

```json
{
  ".proplist": "name,interfaces"
}
```

Expected Response:

```json
[
  {
    "name": "br0",
    "interfaces": [
      "ether1",
      "ether2"
    ]
  }
]
```

**Add an interface to a bridge:**

Endpoint: `/interface/bridge/port`

Request Method: POST

Example JSON Payload:

```json
{
  "bridge": "br0",
  "interface": "ether3"
}
```

Expected Response:

```json
{
  "bridge": "br0",
  "interface": "ether3"
}
```