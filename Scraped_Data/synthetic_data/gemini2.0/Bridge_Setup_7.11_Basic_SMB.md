## Bridge Setup in RouterOS 7.11

### Configuration Scenario and Requirements

* Connect multiple Ethernet interfaces into a single logical bridge.
* Allow traffic to flow between the bridged interfaces.

### Step-by-Step Implementation

**1. Enable Bridging:**

* Navigate to `/interface bridge` in the RouterOS configuration menu.
* Click the `+` button to create a new bridge.

**2. Add Interfaces to Bridge:**

* Select the bridge you created in step 1.
* Drag and drop the required Ethernet interfaces onto the bridge interface.

**3. Enable Bridging:**

* Make sure the `enabled` parameter is set to `yes` for the bridge.

**4. Save and Apply:**

* Click `Apply` to save and apply the configuration.

### Complete Configuration Commands

```
/interface bridge add
/interface bridge set name=MY_BRIDGE
/interface bridge port add interface=ETH1
/interface bridge port add interface=ETH2
/interface bridge set enabled=yes
```

### Common Pitfalls and Solutions

* **Duplicated MAC Addresses:** Ensure that all interfaces added to the bridge have unique MAC addresses. Otherwise, traffic may not flow correctly.
* **Misconfigured Interfaces:** Double-check that all bridged interfaces are configured with appropriate IP addresses and VLAN settings.
* **Firewall Rules:** If necessary, create firewall rules to allow traffic between the bridge interfaces.

### Verification and Testing Steps

* Check the bridge interface status by running the command:
```
/interface bridge print detail
```

* Ping between devices connected to the bridged interfaces to verify connectivity.

### Related Features and Considerations

* **MAC Filtering:** You can optionally configure MAC filtering to restrict access to the bridge from specific devices.
* **VLAN Tagging:** If necessary, you can configure VLAN tagging on the bridged interfaces to segregate traffic.
* **STP:** Spanning Tree Protocol (STP) can be enabled on the bridge to prevent network loops.
* **Security:** Consider implementing security best practices, such as firewall rules and intrusion detection systems.