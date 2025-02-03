## Bridge Setup in RouterOS 7.12

### Configuration Scenario and Requirements

- Create a bridged network between multiple Ethernet interfaces.
- Allow seamless data transfer between devices connected to the bridge.
- Implement this configuration in an SMB (Small to Medium Business) setting.

### Step-by-Step Implementation

**1. Create the Bridge Interface:**

- Navigate to: `/interface bridge`
- Click on the "+" button
- Enter a name for the bridge (e.g., "Bridge1")
- Click "Create"

**2. Add Interfaces to the Bridge:**

- Select the bridge interface created in Step 1
- In the "Ports" tab, click on the "+" button
- Select the physical Ethernet interfaces to add to the bridge
- Click "Add"

**3. Configure IP Address (Optional):**

- If necessary, assign an IP address to the bridge interface for management purposes.
- Select the bridge interface
- In the "Address" tab, enter the desired IP address, subnet mask, and gateway (if required)

**4. Enable Bridge Protocol Filtering (Optional):**

- Bridge Protocol Filtering (BPF) prevents unwanted traffic from entering the bridge.
- Select the bridge interface
- In the "BPF" tab, enable "Use BPF for incoming traffic" and "Use BPF for outgoing traffic"

**5. Configure Spanning Tree Protocol (Optional):**

- Spanning Tree Protocol (STP) prevents loops in the bridged network.
- Select the bridge interface
- In the "Spanning Tree" tab, choose the desired STP mode (e.g., "STP") and settings

### Complete Configuration Commands

```
/interface bridge add name=Bridge1
/interface bridge port add bridge=Bridge1 interface=ether1
/interface bridge port add bridge=Bridge1 interface=ether2
/ip address add address=192.168.1.1/24 interface=Bridge1
/interface bridge set bridge=Bridge1 bpf-in=yes bpf-out=yes
/interface bridge set bridge=Bridge1 spanning-tree-protocol=stp
```

### Common Pitfalls and Solutions

- **Duplicate IP Addresses:** Ensure that all devices connected to the bridge have unique IP addresses.
- **STP Loops:** Configure STP to prevent loops in the network topology.
- **BPF Misconfiguration:** Ensure that BPF filters are configured correctly to allow desired traffic and block unwanted traffic.

### Verification and Testing Steps

- **Connectivity Test:** Verify that devices connected to the bridge can communicate with each other.
- **IP Address Check:** Confirm that the bridge interface has the correct IP address and is accessible.
- **BPF Test:** Use a packet capture tool to ensure that BPF filters are working as intended.
- **STP Check:** Use a network monitoring tool to verify that STP is functioning properly.

### Related Features and Considerations

- **VLANs:** Bridges can be used to create separate VLANs for different types of traffic.
- **Hotspot:** Bridges can be used to create wireless hotspots with isolated user access.
- **Load Balancing:** Bridges can be used to distribute traffic across multiple WAN links for load balancing.