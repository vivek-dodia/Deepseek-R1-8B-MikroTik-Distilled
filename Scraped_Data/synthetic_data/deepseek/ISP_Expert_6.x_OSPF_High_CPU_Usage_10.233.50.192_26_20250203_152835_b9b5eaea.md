---
generated_at: 2025-02-03T15:29:19.214938
topic: OSPF
category: Routing
version: 6.x
scale: ISP
level: Expert
subnet: 10.157.43.128/28
scenario: High CPU Usage
environment: Industrial Network
affected_users: 92
duration: 9 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF on version 6.x in an ISP industrial network with a specific subnet. The problem is high CPU usage affecting 92 users for 9 hours. Let me break down each section step by step.

First, the initial problem report. Users are complaining about slow internet and intermittent connectivity. The NMS shows high CPU on the core router, maybe around 90-100%. OSPF neighbors flapping? That's a common issue. I should mention those symptoms.

Next, the environment. It's an ISP industrial network, so maybe a core router connected to distribution routers, then access layers. The subnet is 10.157.43.128/28. I need to draw this in Mermaid. Let me think: Core Router (CR1) connected to Dist1 and Dist2, each connected to Access routers. The affected subnet is under Dist1. Include OSPF areas, probably backbone area 0.0.0.0 for core, and other areas for distribution.

Initial assessment steps. Check CPU usage with /system resource print. Look at OSPF neighbors with /routing ospf neighbor print. Logs via /log print where topics=ospf. Also interface errors and traffic. Maybe a loop causing high CPU?

Debugging process. Start with OSPF status. Commands like /routing ospf instance print, /routing ospf interface print. Check for LSAs flooding. Logs might show neighbor state changes. Then look at CPU processes with /tool profile. Maybe OSPF is consuming too much CPU. Check routing table with /ip route print. Are there duplicate routes or flapping routes?

Key findings. Maybe OSPF is redistributing connected routes, causing excessive LSAs. Or a misconfigured network type, like broadcast instead of point-to-point leading to more LSAs. Or a layer 2 loop causing excessive traffic and OSPF recalculations.

Solution. Adjust OSPF network types, filter redistributed routes, adjust timers. Maybe enable OSPF overload to stabilize. Update RouterOS if it's a known bug.

Verification. Check CPU after changes, confirm OSPF neighbors stable, no route flaps. Monitor traffic.

Prevention. Proper network design, route filtering, regular monitoring, use passive interfaces where possible.

Common pitfalls: Redistributing without filters, incorrect network types, not monitoring OSPF areas for size.

Let me make sure the CLI commands are correct for version 6.x. For example, OSPF commands in 6.x might differ slightly from later versions. Also, the log examples should reflect OSPF neighbor transitions. Before and after configs: maybe before redistributing connected routes, after adding a filter.

I need to structure each section with markdown, use code blocks for commands, include comments, log outputs, and configurations. Also, check that the subnet 10.157.43.128/28 is correctly placed in the topology.

Wait, the subnet is part of the industrial network. Maybe it's a customer VLAN or a specific segment connected via Dist1. Include that in the network topology description.

In the detailed debugging, maybe the logs show frequent adjacency changes. Then, when checking the OSPF interfaces, one interface is set to broadcast on a point-to-point link, causing unnecessary DR/BDR elections and LSA flooding. Adjusting the network type to point-to-point would reduce overhead.

Root cause: OSPF network type misconfiguration leading to excessive LSA generation and high CPU.

Solution steps: Change network type on the problematic interface, add route filters for redistribution, adjust timers if needed.

Verification: After changes, CPU drops, OSPF neighbors stay up, routing table stabilizes.

I think that covers the main points. Now structure it all into the required sections with proper formatting.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF High CPU Usage

## 1. Initial Problem Report and Symptoms
- **Report**: 92 industrial users report intermittent connectivity and slow internet access for 9 hours.
- **Symptoms**:
  - Core router CPU consistently at 90-100%.
  - OSPF neighbor adjacencies flapping between "Full" and "Down" states.
  - Frequent routing table changes in `/ip route print`.
  - Logs show `OSPF: LS ACK not received` and neighbor state transitions.

---

## 2. Environment Description and Network Topology
**Network Type**: ISP Industrial Network with OSPF backbone (Area 0) and Area 1.  
**Subnet**: `10.157.43.128/28` (connected to Dist1 router).  

```mermaid
graph TD
  CR1[Core Router (CR1)] -->|OSPF Area 0| Dist1[Distribution Router (Dist1)]
  CR1 -->|OSPF Area 0| Dist2[Distribution Router (Dist2)]
  Dist1 -->|OSPF Area 1| Access1[Access Router (Industrial VLAN 10.157.43.128/28)]
  Dist1 -->|OSPF Area 1| Access2[Access Router]
```

---

## 3. Initial Assessment Steps
1. Check CPU usage:
   ```bash
   /system resource print
   ```
   **Output**:
   ```text
             cpu: 98%
   free-memory: 64MB
   ```
2. Verify OSPF neighbor status:
   ```bash
   /routing ospf neighbor print
   ```
   **Output**:
   ```text
   0 interface=ether1 address=10.0.0.2 state="Full" state-changes=142
   ```
3. Review OSPF logs:
   ```bash
   /log print where topics=ospf
   ```
   **Log Example**:
   ```text
   12:00:00 ospf,info CR1 OSPF neighbor 10.0.0.2 (ether1) changed state from Full to Down
   ```

---

## 4. Detailed Debugging Process with CLI Commands
### Step 1: OSPF Configuration Review
```bash
/routing ospf instance print
/routing ospf interface print
```
**Finding**: `ether1` on CR1 uses `network-type=broadcast` (misconfigured for a point-to-point link).

### Step 2: Analyze OSPF LSAs
```bash
/routing ospf lsa print detail
```
**Finding**: Excessive Type 1 (Router LSA) updates from Dist1.

### Step 3: CPU Process Breakdown
```bash
/tool profile
```
**Output**:
```text
  PID PROCESS               CPU% MEMORY
  12 ospf_worker           85%  32MB
```

### Step 4: Route Redistribution Check
```bash
/routing ospf redistribute print
```
**Finding**: Redistribution of `connected` routes without filtering.

---

## 5. Key Findings and Root Cause Analysis
- **Root Cause**: 
  1. `network-type=broadcast` on a point-to-point link caused DR/BDR election loops.
  2. Unfiltered redistribution of 142 connected routes into OSPF.
- **Impact**: Excessive LSA flooding and SPF recalculations, overwhelming CPU.

---

## 6. Solution Implementation Steps
1. Correct OSPF network type:
   ```bash
   /routing ospf interface set [find interface=ether1] network-type=point-to-point
   ```
2. Filter redistributed routes:
   ```bash
   /routing filter add chain=ospf_out protocol=connected action=discard
   ```
3. Stabilize timers (optional):
   ```bash
   /routing ospf interface set [find interface=ether1] hello-interval=10 dead-interval=40
   ```

**Before/After Configuration**:
```diff
/routing ospf interface print
# BEFORE:
  network-type: broadcast
# AFTER:
  network-type: point-to-point
```

---

## 7. Verification Process
1. Confirm CPU normalization:
   ```bash
   /system resource print  # CPU now at 15%
   ```
2. Check stable OSPF neighbors:
   ```bash
   /routing ospf neighbor print  # state="Full", state-changes=0
   ```
3. Validate route stability:
   ```bash
   /ip route print  # No frequent changes
   ```

---

## 8. Prevention Measures
- Use `network-type=point-to-point` on non-broadcast links.
- Always filter redistributed routes with `routing filters`.
- Enable OSPF logging for proactive monitoring:
  ```bash
  /log add topics=ospf
  ```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | List OSPF neighbors |
| `/tool profile` | Analyze CPU usage by process |
| `/routing filter add chain=ospf_out protocol=connected action=discard` | Block connected route redistribution |

---

## 10. Common Pitfalls to Avoid
- **Avoid**: Redistributing all connected routes without filters.
- **Avoid**: Using `broadcast` network type on point-to-point links.
- **Avoid**: Ignoring OSPF timer mismatches between neighbors.
```
