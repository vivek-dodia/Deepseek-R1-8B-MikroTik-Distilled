## Bridge Setup in RouterOS 7.11 (Expert)

### Configuration Scenario and Requirements

* **Goal:** Create a bridge interface to connect multiple physical interfaces and allow traffic to flow between them.
* **Prerequisites:**
    * RouterOS devices with compatible physical interfaces
    * RouterOS 7.11 (6.46 or later)
    * Basic networking knowledge

### Step-by-Step Implementation

1. **Identify Physical Interfaces:** Identify the physical interfaces that will be bridged.
2. **Create Bridge Interface:**
   - Navigate to **Bridge > Bridges** menu.
   - Click **Plus ( + )** button to create a new bridge.
3. **Configure Bridge Properties:**
   - **Name:** Specify a descriptive name for the bridge.
   - **Interfaces:** Select the physical interfaces to include in the bridge.
4. **Bridge Settings:**
   - **Protocol:** Choose the bridging protocol (Spanning Tree Protocol).
5. **Apply Configuration:** Click **Apply** to save the changes.

### Complete Configuration Commands

```
/interface bridge add name=bridge-name
/interface bridge port add bridge=bridge-name interface=interface-name
/interface bridge settings set bridge=bridge-name stp-enable=yes
/system reboot
```

### Common Pitfalls and Solutions

* **Incorrect Interface Selection:** Ensure that the selected physical interfaces are compatible with bridging.
* **STP Configuration:** If STP is enabled, ensure that the devices in the bridged network have unique MAC addresses.
* **VLAN Tagging:** If VLAN tagging is being used, ensure that the bridge interface is configured for the appropriate VLANs.

### Verification and Testing Steps

1. **Bridge Status:** Check the bridge status in the **Bridge > Bridges** menu.
2. **Connectivity Test:** Connect devices to the bridged interfaces and verify traffic flows successfully.
3. **STP Convergence:** If STP is enabled, observe the STP convergence process using the **STP > Status** menu.

### Related Features and Considerations

* **VLAN Support:** Bridges can support VLANs to isolate traffic between different network segments.
* **Security:** Consider firewall rules to protect the bridged network from external threats.
* **STP Enhancements:** Rapid Spanning Tree Protocol (RSTP) or Multiple Spanning Tree Protocol (MSTP) can be used for faster STP convergence.