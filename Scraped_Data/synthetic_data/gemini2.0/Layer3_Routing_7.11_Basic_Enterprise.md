**Layer 3 Routing in MikroTik RouterOS 7.11**

### Configuration Scenario and Requirements

**Objective:** Establish Layer 3 routing between multiple subnets.

* Multiple subnets connected via MikroTik routers
* Routers running RouterOS 7.11 or higher
* Basic understanding of IP routing and subnetting

### Step-by-Step Implementation

**1. Define Static Routes**

- Navigate to **IP -> Routes** in RouterOS GUI
- Click on **Add New** and configure the following parameters:

| Parameter | Description |
|---|---|
| Destination | Subnet address of the destination network |
| Gateway | IP address of the gateway for the destination |
| Type | Static |

**2. Create Firewall Rules for Routing**

- Allow traffic to pass through the router for the configured routes:
- Navigate to **IP -> Firewall -> Filter Rules**
- Click on **Add New** and configure the following parameters:

| Parameter | Description |
|---|---|
| Chain | input |
| Destination Address | Destination subnet address |
| Protocol | all |
| Action | accept |

**3. Configure Interface Forwarding**

- Ensure that the interfaces connected to the different subnets are enabled for forwarding:
- Navigate to **Interfaces** in RouterOS GUI
- Select the interface and click on **Settings**
- Enable **Forwarding** (Make sure it's not set to "disabled")

### Complete Configuration Commands

**Router 1**

```
/ip route add dst-address=10.0.0.0/24 gateway=172.16.0.2
/ip firewall filter add chain=input dst-address=10.0.0.0/24 action=accept
/interface ether1 set forwarding=enable
```

**Router 2**

```
/ip route add dst-address=192.168.0.0/24 gateway=172.16.0.1
/ip firewall filter add chain=input dst-address=192.168.0.0/24 action=accept
/interface ether2 set forwarding=enable
```

### Common Pitfalls and Solutions

* **Incorrect Gateway Address:** Verify that the gateway address specified for the static route is correct.
* **Firewall Blocking Traffic:** Ensure that the firewall rule permits traffic for the configured routes.
* **Disabled Forwarding:** Confirm that the interfaces involved in routing have forwarding enabled.

### Verification and Testing Steps

* **Ping:** Test connectivity between devices on different subnets by pinging their IP addresses.
* **Traceroute:** Use the traceroute command to verify the routing path between devices.
* **Network Monitoring:** Monitor the router's status to check for any routing errors or performance issues.

### Related Features and Considerations

* **OSPF and BGP Routing:** For more advanced Layer 3 routing scenarios, consider using dynamic routing protocols such as OSPF or BGP.
* **Policy Routing:** Implement policy-based routing to prioritize traffic or control access based on source/destination addresses.
* **IPsec VPNs:** Use IPsec VPNs to create secure tunnels for interconnecting remote subnets over the internet.

**Note:**
The provided configuration example is for illustrative purposes only. Adjust the IP addresses, subnets, and gateway addresses to match your specific network requirements.