---
generated_at: 2025-02-03T15:40:50.762338
topic: OSPF
category: Routing
version: 7.x
scale: Enterprise
level: Basic
subnet: 192.168.140.0/25
scenario: High CPU Usage
environment: Branch Office
affected_users: 688
duration: 10 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF on version 7.x in an enterprise branch office with high CPU usage affecting 688 users over 10 hours. Let's break down each section step by step.

First, the initial problem report. The user mentioned high CPU usage, so symptoms would include slow network, high CPU on the router, maybe OSPF neighbors flapping. I should note the duration, affected subnet, and that OSPF is involved.

Next, the environment. It's a branch office with a /25 subnet. The network topology should be in Mermaid. Let's think: branch router connected to two ISPs, then to core routers. Maybe two core routers in OSPF area 0, connected to the branch. The branch has VLANs for different departments.

Initial assessment steps. Check CPU usage, OSPF neighbors, routing table, interface errors, logs. Use commands like `/system resource print`, `/routing ospf neighbor print`, etc.

Debugging process. Start with checking OSPF neighbors. If neighbors are unstable, maybe hello timers mismatch. Look at the routing table—maybe too many routes causing CPU load. Check for route redistribution issues. Logs might show frequent LSAs or SPF calculations. Maybe enable OSPF debugging with `/routing ospf log` commands.

Key findings. Suppose the root cause is a routing loop from incorrect redistribution, causing excessive LSAs and SPF recalculations. Or maybe a misconfigured area leading to full SPF runs often. Another possibility is a large number of OSPF routes overwhelming the CPU.

Solution implementation. Correct the redistribution filters, adjust OSPF timers, maybe summarize routes. Modify configuration to prevent route leaks.

Verification. Check CPU usage again, ensure OSPF neighbors are stable, routing table looks correct, logs show fewer SPF events.

Prevention measures. Regular config audits, route summarization, adjust OSPF timers appropriately, monitor CPU and OSPF status.

Related commands. Include the commands used in assessment and debugging, like checking neighbors, routes, logs, etc.

Common pitfalls. Forgetting to filter redistributed routes, mismatched timers, not summarizing routes, ignoring CPU monitoring.

Wait, the user specified subnet 192.168.140.0/25. Should that be part of the OSPF configuration? Maybe that subnet is being advertised incorrectly, leading to many routes. Or maybe it's part of a larger network being redistributed into OSPF.

Also, high CPU could be due to OSPF processing too many LSAs. If there's a redistribution from another protocol without proper filtering, that might inject a lot of routes, causing OSPF to work overtime. For example, redistributing connected routes without a filter could add unnecessary subnets.

In the initial configuration, maybe the branch router was redistributing connected routes into OSPF, including all interfaces. If the branch has multiple subnets, including the 192.168.140.0/25, but maybe another subnet with a lot of /32 routes or something, that would create many LSAs. Correcting the redistribution to only include necessary networks would reduce the LSAs.

So the before configuration might have a redistribute connected with no filter, and the after would have a filter to only allow 192.168.140.0/25 and other necessary subnets.

Also, maybe the OSPF network type is set to broadcast where it should be point-to-point, causing more frequent hello packets. Or the hello and dead timers are mismatched between neighbors, causing flapping.

In the logs, you might see SPF runs every few seconds, which would spike CPU. Using `/routing ospf log print where topics=lsa,spf` would show those events.

Another angle: if the area is a stub area but not configured as such, leading to external routes being processed unnecessarily. Or a missing area configuration causing full LSAs.

Need to make sure all sections are covered with realistic details. Maybe include example log entries showing frequent SPF runs, and before/after config snippets showing redistribution filters added.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF High CPU Usage

## 1. Initial Problem Report and Symptoms
**Report**: Branch office users report severe network slowdowns affecting 688 users.  
**Symptoms**:
- Router CPU consistently at 95-100% for 10+ hours
- Intermittent OSPF neighbor adjacency drops
- Delayed routing convergence (15-30 sec)
- Increased latency (150ms+ for local resources)
- Affected subnet: `192.168.140.0/25`

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    BRANCH_RTR[Branch Router (RB4011)] --> ISP1
    BRANCH_RTR --> ISP2
    BRANCH_RTR --> CORE1[Core Router 1 (CCR1072)]
    BRANCH_RTR --> CORE2[Core Router 2 (CCR1072)]
    CORE1 <--> CORE2
    BRANCH_RTR --> SW1[Access Switch (CRS354)]
    SW1 --> VLAN140[VLAN140: 192.168.140.0/25]
    SW1 --> VLAN200[VLAN200: 10.200.0.0/24]
    
    classDef router fill:#e1f5fe,stroke:#039be5;
    classDef switch fill:#f0f4c3,stroke:#afb42b;
    class BRANCH_RTR,CORE1,CORE2 router
    class SW1 switch
```

## 3. Initial Assessment Steps
1. Check CPU utilization:
```bash
/system resource print
# Output: CPU: 98% (user: 12%, system: 86%)
```

2. Verify OSPF neighbors:
```bash
/routing ospf neighbor print
# Output: 
# 0 instance=default address=10.10.10.1 state="Full" router-id=1.1.1.1 
# 1 instance=default address=10.10.10.2 state="Exchange" router-id=2.2.2.2
```

3. Check routing table size:
```bash
/ip route print count-only
# Output: 28952 routes
```

4. Monitor interface errors:
```bash
/interface ethernet monitor [find] 
# Output: RX errors: 0, TX errors: 0
```

## 4. Detailed Debugging Process
**Step 1**: Identify OSPF-related CPU usage:
```bash
/tool profile
# Output shows `routing-ospf` process consuming 84% CPU
```

**Step 2**: Check SPF calculation frequency:
```bash
/routing ospf log print where topics~"spf"
# Output:
# 12:34:56 spf,debug Area backbone: Start SPF (trigger: router-LSA)
# 12:34:59 spf,debug Area backbone: SPF duration 2.4s
```

**Step 3**: Analyze LSAs:
```bash
/routing ospf lsa print detail
# Shows 15,000+ Type-5 LSAs from external redistribution
```

**Step 4**: Check route redistribution:
```bash
/routing ospf instance print
# Redistributes: connected,static,bgp
```

**Step 5**: Verify OSPF timers:
```bash
/routing ospf interface-template print
# hello-interval=10s dead-interval=40s (mismatched with core routers' 5s/20s)
```

## 5. Key Findings and Root Cause
**Root Cause**: 
- Unfiltered BGP route redistribution into OSPF caused 28,000+ external routes
- Hello timer mismatch (10s/40s vs 5s/20s) caused neighbor flapping
- SPF recalculations every 3-5 seconds due to constant LSA updates

**Impact**:
- OSPF process overwhelmed by excessive LSA processing
- CPU couldn't handle frequent SPF calculations
- Routing instability exacerbated congestion

## 6. Solution Implementation
**Before** (Problematic Config):
```bash
/routing ospf instance
set redistribute=connected,static,bgp
```

**After** (Corrected Config):
```bash
/routing ospf instance
set redistribute=connected,static,bgp redistribute-filter=ospf-redist

/routing filter rule add chain=ospf-redist prefix=192.168.140.0/25 action=accept
/routing filter rule add chain=ospf-redist action=reject

/routing ospf interface-template
set dead-interval=20s hello-interval=5s
```

## 7. Verification Process
1. Confirm CPU normalization:
```bash
/system resource print
# CPU: 24% (system: 3%, user: 21%)
```

2. Validate OSPF stability:
```bash
/routing ospf neighbor print
# Both neighbors in "Full" state
```

3. Check route count:
```bash
/ip route print count-only
# 214 routes (from 28,952)
```

## 8. Prevention Measures
1. Implement route filtering for all redistributions
2. Enable OSPF throttling:
```bash
/routing ospf instance
set spf-delay=2s spf-holdtime=10s
```
3. Standardize OSPF timers across network
4. Create CPU monitoring alert:
```bash
/system health
set name=cpu-monitor interval=1m on-event="/log warning message=\"CPU over 80%\"" \
    sensor=cpu-temperature threshold=80
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf lsa print` | List all LSAs |
| `/tool profile` | Real-time process monitoring |
| `/routing filter rule print` | Show redistribution filters |
| `/log print where topics~"ospf"` | OSPF-specific logs |

## 10. Common Pitfalls to Avoid
1. **Unfiltered Redistribution**: Always use route filters when redistributing
2. **Timer Mismatches**: Standardize hello/dead intervals across all OSPF devices
3. **Ignoring SPF Throttling**: Use `spf-delay` and `spf-holdtime` to limit recalculations
4. **Overlooking Route Summarization**: Always summarize at area borders
5. **Missing Monitoring**: Implement proactive CPU and OSPF state monitoring
```
