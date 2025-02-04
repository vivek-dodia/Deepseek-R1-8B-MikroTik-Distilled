---
generated_at: 2025-02-03T16:39:38.540088
topic: RIP
category: Routing
version: 7.x
scale: SOHO
level: Expert
subnet: 192.168.135.64/26
scenario: OSPF Adjacency Problems
environment: Branch Office
affected_users: 232
duration: 2 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF Adjacency Problems in a SOHO environment using RouterOS 7.x. Let me start by breaking down each section as specified.

First, the Initial Problem Report and Symptoms. Users can't reach resources at the main office. The branch office uses OSPF, and the adjacency isn't forming. Symptoms would include OSPF neighbors stuck in ExStart/Exchange, routing tables missing routes, and possibly interface errors. Maybe 232 users affected over 2 hours.

Next, Environment Description. It's a branch office with a subnet 192.168.135.64/26. The network topology is simple: BranchRouter connected to MainRouter via a WAN link. I'll need to represent this in Mermaid. Let me think, two routers connected through ether1 and ether2 interfaces. Include IP addresses, OSPF areas, and interfaces.

Initial Assessment Steps. Start with checking OSPF status, interface configurations, logs, neighbor status, and routing tables. The user would run commands like `/routing ospf instance print`, `/routing ospf neighbor print`, and check interfaces with `/interface print`.

Detailed Debugging Process. Need to verify OSPF configuration details: network statements, areas, hello intervals, MTU settings. Check for mismatched areas or authentication. Maybe use `ping` to test connectivity, look for ACLs or firewall rules blocking OSPF (multicast 224.0.0.5). Check MTU mismatches with `/interface ethernet print` and compare. Look into OSPF logs with `/log print where topics=ospf`.

Key Findings and Root Cause. Suppose the MTU on one interface is lower than the other, causing adjacency issues. Or maybe a firewall rule is blocking OSPF traffic. Another possibility is mismatched OSPF areas or network types.

Solution Implementation. Adjust MTU settings, correct OSPF area configurations, update firewall rules. For example, set MTU on both interfaces to 1500. Add firewall rules to accept OSPF traffic.

Verification Process. Check OSPF neighbors again, ensure routes are in the table, test connectivity. Commands like `/routing ospf neighbor print` should show Full state.

Prevention Measures. Standardize configurations, implement monitoring, document network changes, regular audits.

Related Commands. List commands used in the process, like OSPF instance, neighbor, interface, log, ping, firewall.

Common Pitfalls. Forgetting MTU, ignoring firewall rules, mismatched timers, area mismatches.

I need to make sure CLI commands are in code blocks, include example outputs where necessary, and show before/after configurations if relevant. Also, add comments explaining complex commands. Let me structure each section with appropriate markdown headings, bullet points, and code examples.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF Adjacency Problems

## 1. Initial Problem Report and Symptoms
**Report**: Branch office users report inability to access main office resources.  
**Symptoms**:
- OSPF adjacency between BranchRouter and MainRouter fails to form.
- Routing tables missing critical routes (e.g., `10.0.0.0/24`).
- OSPF neighbors stuck in `ExStart/Exchange` state.
- Interface errors on WAN link (high CRC/alignment errors).

---

## 2. Environment Description and Network Topology
**Network Scale**: SOHO (232 users)  
**Subnet**: `192.168.135.64/26` (Branch LAN)  
**RouterOS Version**: 7.12 (stable)  

```mermaid
graph TD
  A[BranchRouter] <--> |OSPF Area 0<br>192.168.135.65/30 (ether1)| B[MainRouter]
  A --> |192.168.135.64/26 (ether2)| C[Branch LAN]
  B --> |10.0.0.0/24 (ether2)| D[Main Office]
```

---

## 3. Initial Assessment Steps
1. **Check OSPF Status**:
   ```bash
   /routing ospf instance print
   # Output: Verify instances are enabled and areas match.
   ```
2. **Verify Interface Configuration**:
   ```bash
   /interface print where name~"ether1|ether2"
   # Output: Check IP addresses and MTU.
   ```
3. **Review OSPF Logs**:
   ```bash
   /log print where topics~"ospf"
   # Example log: "OSPF-1-ADJCHG: neighbor 192.168.135.66: ExStart negotiation failed"
   ```
4. **Check Neighbor Status**:
   ```bash
   /routing ospf neighbor print
   # Output: Neighbor stuck in "ExStart" state.
   ```

---

## 4. Detailed Debugging Process
### Step 1: Verify OSPF Configuration
```bash
/routing ospf interface print
# Check for mismatched area IDs or network types.
```

### Step 2: Test Layer 3 Connectivity
```bash
/ping 192.168.135.66
# Success: ICMP replies confirm L3 connectivity.
```

### Step 3: Check for Firewall Drops
```bash
/ip firewall filter print stats
# Look for drops on OSPF multicast (224.0.0.5/6).
```

### Step 4: Validate MTU Mismatches
```bash
/interface ethernet print where name=ether1
# Output: MTU=1500 (BranchRouter) vs. MTU=1492 (MainRouter)
```

### Step 5: Analyze OSPF Debug Logs
```bash
/system logging add topics=ospf
/log print follow
# Example log: "MTU mismatch 1500 vs 1492"
```

---

## 5. Key Findings and Root Cause Analysis
**Root Cause**: MTU mismatch between `ether1` (BranchRouter, MTU=1500) and `ether1` (MainRouter, MTU=1492).  
**Impact**: OSPF adjacency fails during database exchange due to oversized packets.  

---

## 6. Solution Implementation Steps
1. **Adjust MTU on MainRouter**:
   ```bash
   /interface ethernet set ether1 mtu=1500
   ```
2. **Reset OSPF Process**:
   ```bash
   /routing ospf instance disable [find]
   /routing ospf instance enable [find]
   ```

**Before/After Configuration**:
```diff
# MainRouter (Before)
/interface ethernet set ether1 mtu=1492

# MainRouter (After)
/interface ethernet set ether1 mtu=1500
```

---

## 7. Verification Process
1. **Confirm Adjacency**:
   ```bash
   /routing ospf neighbor print
   # Output: State=Full, Address=192.168.135.66
   ```
2. **Check Routes**:
   ```bash
   /ip route print where ospf
   # Output: 10.0.0.0/24 via OSPF
   ```

---

## 8. Prevention Measures
- Standardize MTU across all WAN links.
- Enable OSPF monitoring with tools like LibreNMS.
- Document network baseline configurations.

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf instance print` | List OSPF instances |
| `/routing ospf neighbor print` | Show OSPF neighbor states |
| `/interface ethernet print` | Check MTU/interface settings |
| `/log print topics=ospf` | Filter OSPF logs |

---

## 10. Common Pitfalls to Avoid
- **MTU Mismatches**: Always validate MTU on both ends.
- **Firewall Rules**: Ensure OSPF multicast (224.0.0.5/6) is allowed.
- **Area ID Mismatches**: Confirm OSPF areas match on adjacent routers.
- **Passive Interfaces**: Avoid marking WAN interfaces as passive.
```
