---
generated_at: 2025-02-03T15:22:27.942509
topic: OSPF
category: Routing
version: 6.x
scale: SMB
level: Expert
subnet: 192.168.15.192/26
scenario: Performance Degradation
environment: Retail Network
affected_users: 949
duration: 3 hours
---

# Analysis Process
Okay, so I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF on version 6.x in a retail SMB network. The subnet is 192.168.15.192/26, and the issue is performance degradation affecting 949 users over 3 hours. Let me break down each section step by step.

First, the initial problem report. The symptoms would be slow network access, maybe some services timing out. Users might complain about POS systems being slow, inventory management lagging. Maybe some intermittent connectivity. Since it's OSPF related, perhaps routing loops or neighbor adjacencies dropping.

Environment description: Retail network, SMB scale. Probably a few routers with OSPF configured. The subnet given is /26, so maybe that's a VLAN for POS terminals or something. The topology might have a couple of MikroTik routers connected via OSPF, maybe a core and a few distribution switches. Let me sketch a Mermaid diagram. Core router connected to two distribution routers, each connected to access switches. All running OSPF.

Initial assessment steps: Check OSPF neighbors, look for adjacencies. Verify routes in the routing table. Check CPU and memory usage on routers. Look at interface statistics for errors or high utilization. Maybe logs for OSPF errors.

Debugging process: Use CLI commands like `/routing ospf neighbor print` to see neighbors. `/routing ospf route print` for OSPF routes. Maybe `log print` to find OSPF-related logs. Check interface status with `/interface print` and look for flapping. If there's a duplicate Router ID, that could cause issues. Or maybe a misconfigured network statement causing incorrect routes.

Key findings: Suppose the core router's OSPF process has a high CPU because of too many LSAs. Or maybe a misconfigured area causing excessive flooding. Or a subnet mismatch in OSPF network configuration. Root cause could be a network statement including a /26 subnet but OSPF is configured for a different area, leading to route flapping.

Solution: Adjust the OSPF network statements to correctly advertise the subnet. Maybe change the area type to stub if it's a small network to reduce LSA traffic. Update Router IDs to prevent conflicts. Adjust timers if necessary.

Verification: After changes, check neighbors again, ensure routes are properly installed. Monitor CPU usage. Do a ping test across subnets. Check logs for any recurring errors.

Prevention: Regular configuration audits, enable OSPF authentication, use appropriate area types, monitor performance metrics.

Common pitfalls: Forgetting to configure network statements correctly, mismatched areas, not using passive interfaces where needed, ignoring MTU mismatches.

Wait, also in version 6.x, some OSPF commands might be different. For example, in RouterOS 6.x, OSPF is configured under `/routing ospf` whereas in later versions it's under `/routing/ospf`. Need to make sure commands are correct for 6.x.

Another thought: Maybe the subnet 192.168.15.192/26 is part of an OSPF area but the network statement was misconfigured as a /24, causing incorrect route advertisements. That would lead to suboptimal routing or loops. For example, if the OSPF network is advertised as 192.168.15.0/24 instead of /26, then other routers might send traffic to the wrong place.

Also, check for interface MTU mismatches. OSPF requires that MTU sizes match on both ends for adjacency to form. If there's a mismatch, neighbors might flap, causing instability.

In the logs, maybe see entries like "OSPF adjacency changed to DOWN" or "MTU mismatch". But in this scenario, the problem is performance degradation, not total outage, so maybe the adjacency is up but routes are not optimal.

Another possibility: Duplicate Router IDs causing confusion in the OSPF domain. If two routers have the same ID, LSAs could conflict, leading to incorrect SPF calculations.

So putting it all together, the root cause is likely a misconfigured network statement causing excessive LSAs or incorrect routing information. The solution is correcting the network statement, ensuring proper area configuration, and verifying Router IDs.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS OSPF Troubleshooting Scenario

## 1. Initial Problem Report and Symptoms
- **Report**: Retail staff reports POS system latency and inventory sync failures
- **Symptoms**:
  - Intermittent packet loss between warehouse and front-office networks
  - 40% increased latency during peak hours (11 AM-2 PM)
  - OSPF routes flapping in routing table
  - CPU spikes (75-90%) on core router during incidents

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    Core[Core Router (RB1100)] -->|Area 0| Dist1[Distribution 1 (RB2011)]
    Core -->|Area 0| Dist2[Distribution 2 (RB2011)]
    Dist1 -->|Area 1| Access1[Access Switch (192.168.15.193/26)]
    Dist2 -->|Area 1| Access2[Access Switch (192.168.15.225/26)]
```

## 3. Initial Assessment Steps
1. Verify OSPF neighbor status:
   ```bash
   /routing ospf neighbor print
   ```
2. Check routing table stability:
   ```bash
   /ip route print where protocol=ospf
   ```
3. Monitor CPU usage:
   ```bash
   /system resource print
   ```
4. Review OSPF logs:
   ```bash
   /log print where message~"OSPF"
   ```

## 4. Detailed Debugging Process
**Step 1: Verify OSPF Adjacencies**
```bash
[admin@Core] > /routing ospf neighbor print
 0 instance=default area=backbone router-id=192.168.15.195 address=192.168.15.194 state="Full" 
 1 instance=default area=backbone router-id=192.168.15.225 address=192.168.15.226 state="Exchange"
```

**Step 2: Check OSPF Route Instability**
```bash
[admin@Core] > /ip route print stats
Flags: D - dynamic; X - disabled 
Columns: DST-ADDRESS, GATEWAY, DISTANCE
DA dst-address        gateway         distance
D  192.168.15.192/26  ether1          110 # Flapping every 90s
```

**Step 3: Analyze OSPF LSAs**
```bash
[admin@Core] > /routing ospf lsa print detail
type=router id=192.168.15.225 seq=0x8000000f age=35s # Rapid sequence increments
```

## 5. Key Findings & Root Cause
- **Finding 1**: Distribution 2 stuck in "Exchange" state
- **Finding 2**: Duplicate Router-ID (192.168.15.225) on Distribution 2 and Access Switch
- **Finding 3**: MTU mismatch between Core (1500) and Distribution 2 (1492)
- **Root Cause**: 
  - MTU mismatch causing OSPF adjacency flapping
  - Duplicate Router-ID generating conflicting LSAs
  - Route flapping causing CPU spikes and packet loss

## 6. Solution Implementation
**Step 1: Correct MTU on Distribution 2**
```bash
/interface ethernet set ether1 mtu=1500
```

**Step 2: Fix Router-ID Conflict**
```bash
# On Distribution 2:
/routing ospf set router-id=192.168.15.226
```

**Step 3: Stabilize OSPF Timers**
```bash
/routing ospf interface-template add interface=ether1 dead-interval=40s hello-interval=10s
```

## 7. Verification Process
1. Confirm stable adjacencies:
```bash
[admin@Core] > /routing ospf neighbor print
 0 state="Full" address=192.168.15.194
 1 state="Full" address=192.168.15.226
```

2. Check route stability:
```bash
/ip route monitor 192.168.15.192/26 # No flapping observed
```

3. Monitor CPU usage:
```bash
[admin@Core] > /system resource print
cpu-load: 25%
```

## 8. Prevention Measures
1. Implement OSPF authentication:
```bash
/routing ospf area set backbone authentication=md5 authentication-key=Ret@!l2023
```
2. Regular configuration audits
3. Enable OSPF monitoring:
```bash
/tool graphing interface add interface=ether1
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf instance print` | Show OSPF instances |
| `/routing ospf lsa print` | List OSPF LSAs |
| `/ip route flush protocol=ospf` | Clear OSPF routes |

## 10. Common Pitfalls to Avoid
1. **MTU Mismatch**: Ensure consistent MTU across OSPF interfaces
2. **Duplicate Router-IDs**: Use unique IDs per OSPF instance
3. **Passive Interfaces**: Configure passive interfaces on stub networks:
```bash
/routing ospf interface-template add passive=yes network=192.168.15.192/26
```
4. **Area Misconfiguration**: Avoid mixing area types (NSSA/Stub) without proper planning
```markdown
**Before Fix** (Problematic Config):
/routing ospf network add area=backbone network=192.168.15.0/24

**After Fix** (Correct Config):
/routing ospf network add area=backbone network=192.168.15.192/26
```
