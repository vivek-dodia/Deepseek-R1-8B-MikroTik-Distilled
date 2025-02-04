---
generated_at: 2025-02-03T16:26:21.895692
topic: RIP
category: Routing
version: 6.x
scale: SMB
level: Expert
subnet: 172.23.1.16/28
scenario: OSPF Adjacency Problems
environment: Edge Location
affected_users: 367
duration: 6 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario based on the user's specifications. Let me break down the requirements step by step. 

First, the topic is RIP, but the scenario is about OSPF adjacency problems. Wait, that's a bit confusing. The user might have made a typo, but I should follow the given details. The RouterOS version is 6.x, which is important because command syntax and features can vary between versions. The network scale is SMB (Small/Medium Business), so the setup isn't too large. The subnet given is 172.23.1.16/28, which is a small subnet with 14 usable IPs. The environment is an edge location, which might mean it's connecting to a larger network or the internet. The affected users are 367, which is a lot for an SMB, maybe a branch office. The duration is 6 hours, indicating a significant outage.

The user wants sections from 1 to 10, including specific elements like problem report, network topology in Mermaid, CLI commands, logs, etc. Let me start structuring each part.

1. **Initial Problem Report and Symptoms**: Need to describe what users are experiencing—connectivity issues, maybe between two routers. Symptoms like OSPF adjacency not forming, routes missing. Timeframe of 6 hours.

2. **Environment Description and Network Topology**: Need to create a Mermaid diagram. Since it's an edge location, maybe two routers connected, one as edge router (R1) with public IP, another internal (R2) connected via a switch. Subnet 172.23.1.16/28 between them. Possibly a third device (FW) for firewall.

3. **Initial Assessment Steps**: Check OSPF status, interfaces, logs. Use commands like `/routing ospf neighbor print`, check interface configurations, IP addresses, MTU settings.

4. **Detailed Debugging Process**: Check OSPF configuration with `/routing ospf instance print`, look for network announcements. Verify area IDs, hello intervals, dead timers. MTU mismatch is a common issue. Use `ping` with do-not-fragment to test MTU. Check authentication settings if any.

5. **Key Findings and Root Cause Analysis**: Suppose the MTU on one interface is lower than the other, causing OSPF adjacency failures. OSPF requires MTU to match. Maybe R2's interface has MTU 1400, while R1 uses 1500.

6. **Solution Implementation Steps**: Adjust MTU on R2's interface to 1500. Use commands like `/interface ethernet set ether2 mtu=1500`. Then reset OSPF process or reboot the router.

7. **Verification Process**: Check OSPF neighbors again, confirm state is Full. Check routing table for OSPF routes. Test connectivity between subnets.

8. **Prevention Measures**: Standardize MTU settings across devices, enable OSPF logging, document network configurations, regular audits.

9. **Related Commands Reference**: List commands used for OSPF, interface checks, logs, etc.

10. **Common Pitfalls**: MTU mismatches, area ID mismatches, authentication errors, network statements misconfiguration.

I need to ensure that CLI commands are in code blocks, include comments, and show before/after configurations where relevant. Also, include example log outputs, like OSPF state changes or authentication failures.

Wait, the user mentioned the topic is RIP but the scenario is OSPF. Maybe it's a mistake. Should I proceed with OSPF as per the scenario? The user might have intended OSPF but wrote RIP in the topic. Since the scenario specifies OSPF Adjacency Problems, I'll focus on OSPF.

Let me make sure all sections are covered. For the network topology in Mermaid, use a simple diagram with R1 connected to R2 and a firewall. Interfaces and IP addresses should be specified.

In the debugging process, checking OSPF neighbor states. If the state is ExStart or Init, that indicates a problem. MTU mismatch would cause neighbors to not form adjacency. Also, area IDs must match, and networks must be properly advertised.

Including log examples: maybe logs showing that OSPF packets are being dropped due to size exceeding MTU. Or neighbor transitions stuck in ExStart.

Root cause analysis: MTU mismatch. On RouterOS, the interface MTU includes the Ethernet header, so if one interface is set to 1500 and the other to 1400, OSPF packets (which are 1500 bytes) would be fragmented, but OSPF doesn't allow fragmentation, leading to adjacency failures.

Solution: Adjust MTU on the misconfigured interface. Then verify.

Prevention measures: Ensure consistent MTU across all OSPF interfaces, use automated config management, etc.

Common pitfalls: Forgetting that MTU includes L2 headers, leading to effective MTU being lower than expected. Also, OSPF network statements not covering the interface's IP, causing neighbors not to communicate.

I think that covers all sections. Now, structure each part with markdown, code blocks for CLI commands, mermaid diagram, and so on.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF Adjacency (v6.x)

## 1. Initial Problem Report and Symptoms
**Report**: Edge location users (367) unable to access central resources for 6 hours.  
**Symptoms**:
- OSPF neighbors stuck in "ExStart/Exchange" state
- Missing routes in routing table (`172.23.1.16/28` not propagating)
- Intermittent packet loss between edge and core networks
- High CPU on edge router during initial failure

## 2. Environment Description
**Network Topology** (Mermaid):
```mermaid
graph TD
    R1[Edge Router (R1)<br>172.23.1.17/28] -->|OSPF Area 0| SW1
    SW1 --> R2[Internal Router (R2)<br>172.23.1.18/28]
    SW1 --> FW[Firewall<br>172.23.1.19/28]
```

## 3. Initial Assessment Steps
1. Verify OSPF neighbor status:
   ```bash
   /routing ospf neighbor print
   # Output: 
   #  0 instance=default address=172.23.1.18 state=ExStart 
   ```
2. Check interface status:
   ```bash
   /interface print where name~"ether1"
   # Output:
   # 7 R ether1 172.23.1.17/28  up
   ```
3. Review OSPF logs:
   ```bash
   /log print where message~"OSPF"
   # Output:
   # 12:05:33 ospf,WARNING: MTU mismatch with 172.23.1.18
   ```

## 4. Detailed Debugging Process
**Step 1**: Verify OSPF configuration
```bash
/routing ospf instance print
# Ensure all routers are in Area 0

/routing ospf interface print
# Confirm correct network interfaces are included
```

**Step 2**: Check MTU settings
```bash
/interface ethernet print 
# R2 Output BEFORE:
#   name=ether2 mtu=1400 

# Test path MTU:
/ping 172.23.1.18 size=1472 do-not-fragment=yes
# Output: 
# Packet needs to be fragmented but DF set
```

**Step 3**: Analyze OSPF packet capture
```bash
/tool sniffer quick interface=ether1 protocol=ospf
# Shows OSPF hello packets with MTU=1400 from R2
```

## 5. Key Findings & Root Cause
**Root Cause**: MTU mismatch between R1 (1500) and R2 (1400) causing OSPF adjacency failure.  
**Why**:
- OSPF requires matching MTU sizes for adjacency formation
- R2 was misconfigured with reduced MTU for a legacy VPN tunnel (never removed)

## 6. Solution Implementation
1. Correct MTU on R2:
   ```bash
   /interface ethernet set ether2 mtu=1500
   ```
2. Reset OSPF process:
   ```bash
   /routing ospf instance disable default
   /routing ospf instance enable default
   ```

**Config Comparison**:
```diff
# R2 BEFORE:
/interface ethernet set ether2 mtu=1400

# AFTER:
/interface ethernet set ether2 mtu=1500
```

## 7. Verification Process
1. Confirm OSPF adjacency:
   ```bash
   /routing ospf neighbor print
   # Output:
   # 0 instance=default address=172.23.1.18 state=Full
   ```
2. Validate routing table:
   ```bash
   /ip route print where protocol=ospf
   # Output:
   # DST: 10.0.0.0/24 gateway=172.23.1.17
   ```

## 8. Prevention Measures
1. Implement configuration standardization:
   ```bash
   /interface ethernet set [find] mtu=1500
   ```
2. Enable OSPF monitoring:
   ```bash
   /tool graphing interface add interfaces=ether1
   ```
3. Create pre-change validation checklist including MTU checks

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Check OSPF peer status |
| `/interface print detail` | Verify MTU/interface settings |
| `/log print where message~"OSPF"` | Filter OSPF-specific logs |

## 10. Common Pitfalls to Avoid
- **MTU Mismatches**: Always verify with `ping ... do-not-fragment`
- **Area ID Conflicts**: Ensure all peers use the same OSPF area
- **Passive Interfaces**: Never mark OSPF-facing interfaces as passive
- **Timer Incompatibility**: Keep hello/dead timers consistent
```
