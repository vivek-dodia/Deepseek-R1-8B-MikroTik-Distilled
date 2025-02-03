**Bridge Setup in RouterOS 6.x/7.x**

## Configuration Scenario and Requirements

- Create a bridge interface to connect multiple physical ports into a single logical network segment.
- Configure spanning tree, VLANs, and MAC filtering.
- Secure the bridge and prevent unauthorized access.

## Step-by-Step Implementation

**1. Create Bridge Interface**

```
/interface bridge add name=my-bridge
```

**2. Add Ports to Bridge**

```
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**3. Enable Spanning Tree Protocol**

```
/interface bridge set my-bridge stp=yes
```

**4. Configure VLANs**

* Add and tag VLAN interfaces on the bridge.
* Configure the bridge to accept VLAN-tagged traffic.

```
/interface vlan add name=vlan10 vlan-id=10
/interface bridge port set my-bridge-port1 vlan-mode=tag vlan-id=10
/interface bridge port set my-bridge-port2 vlan-mode=tag vlan-id=10
/interface bridge set my-bridge vlan-filtering=yes
```

**5. Enable MAC Filtering**

```
/interface bridge mac-filter add bridge=my-bridge mac-address=00:00:00:00:00:01
```

**6. Secure the Bridge**

* Disable bridge protocol discovery to prevent unauthorized access.
* Set a bridge password to require authentication for management operations.

```
/interface bridge set my-bridge protocol-mode=disabled
/interface bridge set my-bridge password=my-secure-password
```

## Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/interface bridge set my-bridge stp=yes
/interface vlan add name=vlan10 vlan-id=10
/interface bridge port set my-bridge-port1 vlan-mode=tag vlan-id=10
/interface bridge port set my-bridge-port2 vlan-mode=tag vlan-id=10
/interface bridge set my-bridge vlan-filtering=yes
/interface bridge mac-filter add bridge=my-bridge mac-address=00:00:00:00:00:01
/interface bridge set my-bridge protocol-mode=disabled
/interface bridge set my-bridge password=my-secure-password
```

## Common Pitfalls and Solutions

* **Incorrect port configuration:** Ensure the ports added to the bridge are physically connected and configured in the correct VLAN mode.
* **STP configuration:** Verify that the spanning tree settings are appropriate for the network topology to avoid loops.
* **MAC filtering errors:** Check the MAC addresses being filtered and ensure they are valid.

## Verification and Testing Steps

* Use the "/interface bridge print" command to verify the bridge configuration.
* Check the "/interface bridge port print" command to confirm the ports added to the bridge.
* Ping between hosts on different VLANs to test connectivity.
* Run the "/interface bridge mac-filter print" command to view configured MAC filters.

## Related Features and Considerations

* **Port Isolation:** Enable port isolation to prevent communication between devices connected to the same bridge.
* **VLAN Trunking:** Configure VLAN trunking to pass multiple VLANs over a single physical link.
* **Security:** Implement additional security measures such as firewall rules and intrusion detection systems.

## MikroTik REST API Examples

**Endpoint:** `/interface/bridge`

**Request Method:** GET

**Example Request:**

```
curl -X GET -H "Authorization: Basic admin:admin" http://192.168.88.1/rest/interface/bridge
```

**Expected Response:**

```json
[
  {
    "name": "my-bridge",
    "ports": [
      "ether1",
      "ether2"
    ],
    "stp": "enabled",
    "vlan-filtering": "enabled",
    "password": "my-secure-password"
  }
]
```