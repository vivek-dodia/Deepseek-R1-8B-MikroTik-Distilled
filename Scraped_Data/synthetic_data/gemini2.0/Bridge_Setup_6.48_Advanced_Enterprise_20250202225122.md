## Bridge Setup in RouterOS 6.48

### Configuration Scenario and Requirements

**Objective:** Configure a bridge to connect multiple network segments.

**Requirements:**

- RouterOS 6.48 (or later) router
- Multiple network interfaces

### Step-by-Step Implementation

#### 1. Create the Bridge

```
/interface bridge add name=my-bridge
```

#### 2. Add Interfaces to the Bridge

Bridge each required interface to the newly created bridge:

```
/interface ethernet set ether1 master=my-bridge
/interface ethernet set ether2 master=my-bridge
```

#### 3. Configure IP Address for the Bridge (Optional)

If the bridge requires a direct IP address, assign it on the bridge interface:

```
/interface bridge set my-bridge address=10.10.10.1/24
```

### Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface ethernet set ether1 master=my-bridge
/interface ethernet set ether2 master=my-bridge
/interface bridge set my-bridge address=10.10.10.1/24
```

### Common Pitfalls and Solutions

- **Bridge interface not operational:** Ensure all member interfaces are up and connected to the same physical network.
- **No connectivity between bridged interfaces:** Check for packet forwarding rule blocks or firewall rules.
- **IP address conflict on the bridge:** If the bridge is assigned an IP address, verify that no other interface on the network is using the same address.

### Verification and Testing Steps

- Check the interface status to confirm the bridge is active:

```
/interface bridge print
```

- Ping devices on the bridged interfaces to verify connectivity.

### Related Features and Considerations

- **STP (Spanning Tree Protocol):** Use STP to prevent bridge loops and ensure network stability.
- **VLANs (Virtual LANs):** Implement VLANs on the bridge to segment the network further.
- **Firewall:** Implement firewall rules on the bridge interface to control traffic flow.

### MikroTik REST API Examples

**Create Bridge:**

**Endpoint:** `/interface/bridge`

**Method:** POST

**JSON Payload:**

```json
{
  "name": "my-bridge"
}
```

**Response:**

```json
{
  "id": 1
}
```

**Add Interface to Bridge:**

**Endpoint:** `/interface/ethernet/<interface-name>`

**Method:** PUT

**JSON Payload:**

```json
{
  "master-port": "my-bridge"
}
```

**Response:**

```json
{
  "id": 1
}
```