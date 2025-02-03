## Bridge Setup in RouterOS 7.11

**Configuration Level:** Advanced

**Network Scale:** Enterprise

### Configuration Scenario and Requirements

* Create a bridge interface to connect multiple physical interfaces.
* Assign IP addresses to the bridge interface.
* Enable DHCP server on the bridge interface.
* Configure firewall rules to allow traffic between the bridged interfaces.

### Step-by-Step Implementation

**1. Create Bridge Interface**

```
/interface bridge add name=bridge-name
```

**2. Add Physical Interfaces to Bridge**

```
/interface bridge port add interface=ether1-bridge bridge=bridge-name
/interface bridge port add interface=ether2-bridge bridge=bridge-name
```

**3. Assign IP Address to Bridge**

```
/ip address add address=10.10.10.1/24 interface=bridge-name
```

**4. Enable DHCP Server**

```
/ip dhcp-server add interface=bridge-name address-pool=dhcp-pool
/ip dhcp-pool add name=dhcp-pool ranges=10.10.10.101-10.10.10.254
```

**5. Configure Firewall Rules**

```
/ip firewall filter add in-interface=ether1-bridge out-interface=ether2-bridge action=accept
/ip firewall filter add in-interface=ether2-bridge out-interface=ether1-bridge action=accept
```

### Complete Configuration Commands

```
/interface bridge add name=bridge-name
/interface bridge port add interface=ether1-bridge bridge=bridge-name
/interface bridge port add interface=ether2-bridge bridge=bridge-name
/ip address add address=10.10.10.1/24 interface=bridge-name
/ip dhcp-server add interface=bridge-name address-pool=dhcp-pool
/ip dhcp-pool add name=dhcp-pool ranges=10.10.10.101-10.10.10.254
/ip firewall filter add in-interface=ether1-bridge out-interface=ether2-bridge action=accept
/ip firewall filter add in-interface=ether2-bridge out-interface=ether1-bridge action=accept
```

### Common Pitfalls and Solutions

* **Ensure that all physical interfaces added to the bridge are configured correctly.** Otherwise, traffic may not flow properly.
* **Avoid assigning the same IP address to multiple bridge interfaces.** This can lead to IP address conflicts and network issues.
* **Use strong firewall rules to protect the bridged network.** Avoid allowing unnecessary traffic between the bridged interfaces.

### Verification and Testing Steps

* Check the bridge interface configuration using `/interface bridge print`.
* Assign IP addresses to devices connected to the bridged interfaces.
* Verify DHCP operation by observing IP address assignments on the connected devices.
* Test connectivity between the bridged interfaces by pinging or using other communication tools.

### Related Features and Considerations

* **VLANs:** VLANs can be configured on the bridge interface to further segment the network.
* **Bonding:** Multiple physical interfaces can be bonded together to increase bandwidth and redundancy.
* **Security:** Secure communication between the bridged interfaces by using secure protocols (e.g., SSH, VPN) and implementing appropriate firewall rules.