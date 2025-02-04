---
generated_at: 2025-02-03T15:32:53.387658
topic: OSPF
category: Routing
version: 7.x
scale: SOHO
level: Advanced
subnet: 10.3.225.0/27
scenario: High CPU Usage
environment: Branch Office
affected_users: 897
duration: 5 hours
---

# Analysis Process
Okay, let me try to work through this problem. The user wants a detailed MikroTik RouterOS troubleshooting scenario for OSPF in a SOHO environment where high CPU usage is affecting 897 users for 5 hours. I need to cover all the sections mentioned, so let's break it down step by step.

First, the initial problem report and symptoms. High CPU usage on a router can be caused by a lot of things. Since it's related to OSPF, maybe there's an issue with OSPF processes consuming CPU. Symptoms might include users experiencing slowness, router's CPU pegged at 90-100%, OSPF neighbors flapping, or high traffic from OSPF.

Next, the environment description and network topology. The subnet is 10.3.225.0/27, which is a small subnet with 30 usable addresses. The network is a branch office, SOHO scale. The topology should include a branch router connected to a main office via a WAN link, maybe some switches and APs. Let me visualize that in Mermaid. I'll need to represent the branch router (RouterOS v7.x) connected to the main router, with a LAN switch and APs. The subnet is 10.3.225.0/27 on the LAN side.

Initial assessment steps would involve checking CPU usage, OSPF neighbors, interface statuses, and logs. Commands like `/system resource print` to check CPU, `/routing ospf neighbor print` to see neighbors, maybe `/log print` to look for OSPF errors.

For detailed debugging, I should use commands to check OSPF status, traffic, and possible route churn. Commands like `/routing ospf instance print`, `/routing ospf interface print`, maybe looking at the LSDB with `/routing ospf lsa print`. Also, checking if there's a routing loop or excessive LSAs. Maybe a packet capture for OSPF packets to see if there's a lot of Hello or LSA traffic.

Key findings and root cause analysis. Suppose the problem is that the OSPF is configured with a network type that's causing excessive LSA generation, like using broadcast on a point-to-point link. Or maybe a misconfiguration leading to duplicate router IDs or areas. Alternatively, a high number of LSAs due to a large network being advertised, but since it's SOHO, maybe a loop or a misconfigured network statement causing OSPF to advertise too many routes.

Solution implementation would involve correcting the OSPF network type, adjusting timers, filtering routes, or fixing any misconfigurations. For example, changing the OSPF network type from broadcast to point-to-point on a WAN link to reduce LSA flooding.

Verification steps would involve rechecking CPU usage, confirming OSPF neighbors are stable, and ensuring LSAs are at expected levels. Prevention measures could include proper OSPF network type configuration, route summarization, and monitoring.

Common pitfalls might include not checking OSPF network types, ignoring route summarization, or not monitoring OSPF LSAs. Also, not verifying MTU mismatches which can cause adjacency issues.

I need to make sure the CLI commands are accurate for RouterOS 7.x. For example, OSPF configuration in 7.x might be under `/routing ospf` instead of older versions. Also, commands like `/routing ospf interface set` to adjust interface parameters.

Including log examples would help. Maybe logs showing OSPF neighbor state changes or LSAs being received frequently. Before and after configurations, like changing the OSPF interface type from broadcast to point-to-point.

Also, the subnet 10.3.225.0/27 is specific, so ensuring that the OSPF configuration correctly advertises this subnet without including unintended networks.

Wait, the problem is high CPU usage. OSPF can cause high CPU if there's a lot of SPF calculations. Maybe the SPF is running too frequently because of network instability. So in the logs, there might be messages about SPF runs. Using `/routing ospf history print` could show SPF computation history.

Another possibility is that the router is receiving a default route via OSPF and there's a routing loop causing traffic to bounce, but since it's a SOHO, maybe not. Alternatively, a misconfigured area leading to excessive LSA generation.

In the scenario, the branch office router is connected to the main office. If the WAN link is unstable, OSPF neighbors might flap, causing SPF recalculations. But the user count is 897, which seems high for a SOHO. Maybe it's a typo, but I'll proceed as given.

So putting it all together, the root cause could be an OSPF network type mismatch on the WAN interface, causing frequent LSA updates and SPF calculations, leading to high CPU. The fix would be setting the correct network type, like point-to-point.

Another angle: if the subnet 10.3.225.0/27 is being advertised into OSPF, but there's a loop or another router advertising the same subnet, causing route flaps. But in a SOHO branch, maybe only one router is advertising that subnet.

Alternatively, the OSPF process is redistributing connected routes, and a lot of routes are being injected into OSPF, causing high CPU. But in a SOHO, the routes should be minimal. Unless there's a misconfiguration in redistribution.

I think the most plausible scenario for a SOHO is a network type mismatch on the WAN link. For example, the WAN is a point-to-point link but configured as broadcast, leading to DR/BDR elections and more LSA traffic. Changing it to point-to-point would reduce overhead.

Let me structure the answer accordingly. Initial problem report mentions high CPU, users experiencing issues. Environment has a branch router connected to main, with LAN on 10.3.225.0/27. Initial steps check CPU, OSPF neighbors. Debugging shows frequent SPF runs, OSPF network type as broadcast on a P2P link. Root cause is the network type. Fix is changing to P2P. Verify CPU drops, SPF runs decrease. Prevention includes correct network type setup and monitoring.

Commands would include checking OSPF neighbors, instances, interfaces. Logs showing neighbor transitions. Before config: interface uses network type broadcast. After: set to point-to-point. Verification with CPU usage and OSPF history.

Common pitfalls: not setting network type correctly, not monitoring SPF runs, ignoring interface MTU.

Okay, I think that's a solid approach. Now, structure all this into the required sections with markdown formatting, CLI commands in code blocks, mermaid diagram, etc.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS OSPF Troubleshooting Scenario

## 1. Initial Problem Report and Symptoms
**Report**: Branch office users report severe network slowdown (897 users affected).  
**Symptoms**:
- Router CPU consistently at 95-100% for 5 hours
- Intermittent packet loss to main office
- Delayed OSPF neighbor adjacencies
- Frequent route changes in routing table

---
## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    BRANCH_RTR[Branch Router (ROS v7.x)] -->|OSPF Area 0| MAIN_RTR[Main Office Router]
    BRANCH_RTR --> SWITCH[SOHO Switch]
    SWITCH --> AP1[Wi-Fi AP]
    SWITCH --> AP2[Wi-Fi AP]
    SWITCH --> USERS[897 Users]
    
    subgraph Branch LAN
    10.3.225.0/27
    end
```

---
## 3. Initial Assessment Steps
1. Check CPU utilization:
```bash
/system resource print
# Output: CPU: 98% (user: 12%, system: 86%)
```

2. Verify OSPF neighbor status:
```bash
/routing ospf neighbor print
# Output: 
# 0 instance=default address=192.168.1.1 state="Full" router-id=1.1.1.1 
#         state-changes=142
```

3. Review interface utilization:
```bash
/interface monitor-traffic ether1
# Output: rx: 850Mbps, tx: 840Mbps
```

---
## 4. Detailed Debugging Process
**Step 1**: Identify OSPF-related CPU usage
```bash
/tool profile
# Output shows "routing" process consuming 82% CPU
```

**Step 2**: Check OSPF SPF runs history
```bash
/routing ospf history print
# Output:
# 12:30:00  SPF: 142 runs (last duration: 450ms)
```

**Step 3**: Analyze OSPF LSAs
```bash
/routing ospf lsa print detail
# Output shows 1500 Type-1 LSAs from single neighbor
```

**Step 4**: Capture OSPF control traffic
```bash
/tool sniffer quick protocol=89
# Output: 1500 OSPF Hello packets/sec on WAN interface
```

**Step 5**: Verify interface configuration
```bash
/routing ospf interface print
# BEFORE:
# 0 interface=ether1 network-type=broadcast hello-interval=10
```

---
## 5. Key Findings & Root Cause
**Root Cause**: 
- OSPF network-type misconfigured as `broadcast` on point-to-point WAN link
- Resulted in excessive Hello packets (1500/sec) and SPF recalculations
- MTU mismatch (1500 vs 1492) caused retransmissions

**Impact**:
- OSPF consumed 86% CPU processing control plane traffic
- Route instability caused packet loss for user traffic

---
## 6. Solution Implementation
1. Correct OSPF network-type:
```bash
/routing ospf interface set [find interface=ether1] network-type=point-to-point
```

2. Adjust MTU settings:
```bash
/interface set ether1 mtu=1492
```

3. Optimize OSPF timers:
```bash
/routing ospf interface set [find interface=ether1] hello-interval=30 dead-interval=120
```

---
## 7. Verification Process
1. Confirm CPU reduction:
```bash
/system resource print
# AFTER: CPU: 22% (user: 18%, system: 4%)
```

2. Check OSPF stability:
```bash
/routing ospf history print
# AFTER: SPF: 1 run (last 60 minutes)
```

3. Validate traffic flow:
```bash
/ping 192.168.1.1 count=100
# Output: 100 packets transmitted, 0% lost
```

---
## 8. Prevention Measures
1. Implement OSPF network-type validation checklist
2. Add CPU monitoring threshold alerts:
```bash
/system health set [find] on-over-temperature="alert"
```
3. Enable OSPF logging:
```bash
/system logging add topics=ospf
```

---
## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf instance print` | Show OSPF instances |
| `/routing ospf lsa print` | List OSPF LSAs |
| `/tool sniffer quick protocol=89` | Capture OSPF packets |
| `/interface monitor-traffic` | Real-time traffic analysis |

---
## 10. Common Pitfalls to Avoid
1. **Mismatched network-types** between OSPF peers
2. **Ignoring MTU** settings on WAN interfaces
3. **Over-aggressive timers** causing protocol churn
4. **Missing route filters** leading to excessive LSAs
5. **Neglecting CPU profiling** during network changes
```
