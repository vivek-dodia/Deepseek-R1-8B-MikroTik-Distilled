## Bridge Setup in RouterOS 6.48 (Expert)

### 1. Configuration Scenario and Requirements

- Establish a bridge interface to connect multiple physical interfaces.
- Assign IP addresses and configure DHCP/NAT for the bridged network.
- Implement firewall rules to protect the network.

### 2. Step-by-Step Implementation

**Step 1: Create Bridge Interface**

```text
/interface bridge add name=my-bridge
```

**Step 2: Add Physical Interfaces to Bridge**

```text
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**Step 3: Configure IP Address and DHCP**

```text
/ip address add address=192.168.1.1/24 interface=my-bridge
/ip dhcp-server add interface=my-bridge address-pool=dhcp-pool range=192.168.1.100-192.168.1.200
```

**Step 4: Configure NAT**

```text
/ip firewall nat add chain=srcnat out-interface=my-bridge action=masquerade
```

**Step 5: Configure Firewall Rules**

```text
/ip firewall filter add chain=input in-interface=my-bridge action=accept
/ip firewall filter add chain=output out-interface=my-bridge action=accept
```

### 3. Complete Configuration Commands

```text
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/ip address add address=192.168.1.1/24 interface=my-bridge
/ip dhcp-server add interface=my-bridge address-pool=dhcp-pool range=192.168.1.100-192.168.1.200
/ip firewall nat add chain=srcnat out-interface=my-bridge action=masquerade
/ip firewall filter add chain=input in-interface=my-bridge action=accept
/ip firewall filter add chain=output out-interface=my-bridge action=accept
```

### 4. Common Pitfalls and Solutions

- **Incorrect Interface Assignment:** Ensure that the correct physical interfaces are assigned to the bridge.
- **IP Address Conflict:** Verify that the IP address assigned to the bridge is not already in use on another interface.
- **DHCP Server Misconfiguration:** Confirm that the DHCP server has a valid address pool and is enabled on the bridge interface.
- **Firewall Rule Issues:** Ensure that the firewall rules allow traffic in and out of the bridge interface as intended.

### 5. Verification and Testing Steps

- **Connectivity Test:** Ping and access devices connected to the bridged network.
- **DHCP Lease Verification:** Confirm that devices are receiving IP addresses from the DHCP server.
- **Network Access:** Test internet connectivity and access to external resources.

### 6. Related Features and Considerations

- **VLANs:** Bridges can be used to segment networks into VLANs using bridge ports with specific VLAN ID assignments.
- **Trunking:** Bridges can be configured for trunking, allowing multiple VLANs to be carried over a single physical interface.
- **Security:** Implement additional security measures such as VLAN segregation, access control lists (ACLs), and intrusion detection/prevention systems (IDS/IPS) to enhance network security.