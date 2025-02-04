---
generated_at: 2025-02-03T15:18:16.520633
topic: OSPF
category: Routing
version: 6.x
scale: SOHO
level: Advanced
subnet: 172.18.144.160/27
scenario: VPN Tunnel Issues
environment: Campus Network
affected_users: 285
duration: 13 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF in a SOHO campus network with VPN tunnel issues. Let's start by breaking down each section as specified.

First, the initial problem report. The users can't access resources over the VPN, and OSPF isn't advertising routes. Symptoms include failed VPN tunnels, OSPF neighbors not establishing, and high latency. Maybe some packet loss too. 285 users affected over 13 hours. Got it.

Next, the environment description. The network is a campus setup with two buildings connected via a VPN. The subnet is 172.18.144.160/27. Need to create a Mermaid diagram. Let me sketch the topology: two routers (R1 and R2) connected through a VPN. Each has a LAN subnet. R1 is in Building A, R2 in Building B. The VPN uses IPsec. OSPF is supposed to share routes between them. Mermaid code would show R1 and R2 connected via IPsec tunnel, each connected to their respective LANs.

Initial assessment steps. Start with checking OSPF neighbors and status. Use commands like /routing ospf neighbor print. Then check VPN tunnel status with /interface ipsec policy print. Verify OSPF interfaces and network configuration. Maybe look at routes with /ip route print. Also, check logs for errors: /log print.

Detailed debugging process. First, confirm OSPF neighbors. If they're not up, check OSPF configuration. Verify area IDs, network statements, hello intervals. Then check VPN: are the policies correct? Are there any drops in IPsec traffic? Use /interface ipsec active-peers print and /interface ipsec statistics print. Maybe test connectivity over the tunnel with ping. Check firewall rules to ensure OSPF (protocol 89) and IPsec (UDP 500, 4500) are allowed. Look for MTU issues. Maybe OSPF packets are fragmented because of the tunnel's MTU, causing drops. Use ping with DF flag to test.

Key findings. Suppose the MTU mismatch is the issue. The VPN tunnel has a lower MTU, and OSPF packets are too large, getting fragmented but the DF flag is set, so they're dropped. Hence, OSPF adjacencies can't form. Root cause is MTU settings on the tunnel interfaces not accounting for IPsec overhead.

Solution: Adjust MTU on OSPF interfaces to 1400 to prevent fragmentation. Update the OSPF network configuration with the correct MTU. Maybe set the IPsec policies to correct MTU as well.

Verification: After changing MTU, check OSPF neighbors come up. Verify routes are exchanged. Test VPN connectivity and user access.

Prevention measures: Document MTU requirements for VPN tunnels, implement monitoring for OSPF and IPsec, adjust interface MTUs during setup.

Related commands: Include the OSPF neighbor print, IPsec policies, MTU settings, firewall checks.

Common pitfalls: Forgetting MTU with VPNs, mismatched OSPF areas, firewall blocking protocols.

Wait, also need to include before and after configurations. Before: OSPF interface with MTU 1500. After: MTU 1400. Also check if IPsec policies had the correct proposal with proper encryption settings that might affect packet size.

Log examples: Maybe logs showing OSPF packets timed out, or IPsec drops. CLI outputs from commands like /routing ospf neighbor print showing no neighbors, or /interface ipsec active-peers showing no active peers.

Hmm, need to structure each section with the right commands and examples. Make sure the CLI commands are in code blocks, comments explain complex ones. Also, ensure the Mermaid diagram is correctly formatted.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF VPN Tunnel Issues

## 1. Initial Problem Report and Symptoms
**Report**: Users in a SOHO campus network (172.18.144.160/27) report inability to access resources over the VPN tunnel.  
**Symptoms**:  
- VPN tunnel between two MikroTik routers (R1 and R2) fails intermittently.  
- OSPF neighbors not establishing.  
- High latency (200ms+) and packet loss (15-20%) on the tunnel.  
- 285 users affected for 13 hours.

---

## 2. Environment Description and Network Topology
**Network Type**: Campus network with two buildings connected via IPsec VPN.  
**Subnet**: `172.18.144.160/27` (split into `/30` for VPN and `/28` for LANs).  

```mermaid
graph TD
  R1[RouterOS 6.x (R1)] -->|IPsec Tunnel| R2[RouterOS 6.x (R2)]
  R1 --> LAN1[172.18.144.160/28]
  R2 --> LAN2[172.18.144.176/28]
```

---

## 3. Initial Assessment Steps
1. **Check OSPF neighbor status**:  
   ```bash
   /routing ospf neighbor print
   # Output: No neighbors listed
   ```
2. **Verify VPN tunnel status**:  
   ```bash
   /interface ipsec policy print
   # Output: Phase2 status=established, but packets=0
   ```
3. **Check OSPF network configuration**:  
   ```bash
   /routing ospf network print
   # Output: network=172.18.144.160/27 area=backbone
   ```

---

## 4. Detailed Debugging Process
### Step 1: Confirm OSPF Adjacency Requirements
```bash
/routing ospf interface print
# Output: 
#   interface=ether1 mtu=1500
#   interface=ipsec-tunnel1 mtu=1500 (incorrect for IPsec overhead)
```

### Step 2: Check IPsec Tunnel Health
```bash
/interface ipsec active-peers print
# Output: No active peers during downtime

/interface ipsec statistics print
# Output: 
#   encrypted-bytes=0
#   decrypted-bytes=0
```

### Step 3: Test Path MTU
```bash
/ping 172.18.144.177 size=1472 do-not-fragment=yes
# Output: Packet needs to be fragmented but DF set
```

### Step 4: Firewall Rules Check
```bash
/ip firewall filter print
# Output: No rules allowing OSPF (protocol 89) or IPsec (UDP 500/4500)
```

---

## 5. Key Findings and Root Cause Analysis
**Root Cause**:  
- **MTU Mismatch**: OSPF packets (1500 MTU) exceeded IPsec tunnel MTU (1420 after ESP overhead), causing fragmentation drops.  
- **Firewall Misconfiguration**: Blocked OSPF (89) and IPsec (500/4500) traffic.  

---

## 6. Solution Implementation Steps
1. **Adjust MTU on OSPF interfaces**:  
   ```bash
   /interface ethernet set ether1 mtu=1400
   /interface ipsec set ipsec-tunnel1 mtu=1400
   ```
2. **Update Firewall Rules**:  
   ```bash
   /ip firewall filter add chain=input protocol=89 action=accept
   /ip firewall filter add chain=input protocol=udp dst-port=500,4500 action=accept
   ```

---

## 7. Verification Process
1. **Confirm OSPF Neighbors**:  
   ```bash
   /routing ospf neighbor print
   # Output: state="Full" address=172.18.144.177
   ```
2. **Test VPN Throughput**:  
   ```bash
   /ping 172.18.144.177 size=1400 do-not-fragment=yes
   # Output: 0% packet loss
   ```

---

## 8. Prevention Measures
- Document MTU requirements for VPN tunnels.  
- Implement OSPF/IPsec monitoring scripts.  
- Validate firewall rules during network changes.  

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Check OSPF adjacency |
| `/interface ipsec active-peers print` | Verify IPsec tunnel status |
| `/ip firewall filter print` | Review firewall rules |

---

## 10. Common Pitfalls to Avoid
- Ignoring MTU adjustments for IPsec tunnels.  
- Forgetting to allow OSPF (protocol 89) in firewalls.  
- Using mismatched OSPF area IDs or authentication.  
```
