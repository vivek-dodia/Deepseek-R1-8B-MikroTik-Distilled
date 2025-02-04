---
generated_at: 2025-02-03T16:08:33.017181
topic: BGP
category: Routing
version: 7.x
scale: SOHO
level: Advanced
subnet: 172.18.241.160/27
scenario: VLAN Trunking Issues
environment: Multi-tenant Building
affected_users: 524
duration: 21 hours
---

# Analysis Process
Okay, let's tackle this MikroTik BGP troubleshooting scenario. The user wants a detailed example for a SOHO network in a multi-tenant building with VLAN trunking issues. First, I need to make sure I cover all the required sections: problem report, environment, assessment steps, debugging with CLI commands, root cause, solution, verification, prevention, commands reference, and pitfalls.

Starting with the initial problem report. The symptoms mentioned are intermittent connectivity and BGP flapping. Since it's a multi-tenant setup with VLAN trunking, maybe the VLAN tags aren't being properly handled on the MikroTik router. Affected users are 524, which is a lot for a SOHO, so maybe the subnet /27 is too small? Wait, /27 gives 30 usable addresses. But 524 users... Oh, perhaps the subnet is for management, and the actual user VLANs are larger. But the scenario says the subnet is 172.18.241.160/27, which is part of the problem. Maybe the VLAN trunk isn't allowing all necessary VLANs, causing some tenants to lose connectivity.

Environment description: The network topology needs to be in Mermaid. Let's outline the ISP, MikroTik router, switch, and tenants. The router connects to the ISP via BGP and to a switch with a trunk port. Tenants are on different VLANs via the switch. The BGP session is between the MikroTik and the ISP.

Initial assessment steps: Check BGP status with /routing/bgp/peer print. Look for established sessions. Check OSPF if it's used, but the topic is BGP. Then inspect the trunk port configuration on the router. Verify VLAN settings on the interface. Check logs for BGP flaps or VLAN errors. Also, maybe check IP addresses and subnet assignments.

Debugging process: Use commands like /interface bridge vlan print to see VLAN configurations. Check if the trunk port has all necessary VLANs. Then look at BGP configuration with /routing bgp template print. Maybe the BGP peer is using an incorrect local address if the VLAN interface is down. Check routes with /ip route print. Logs might show BGP transitions due to interface flapping if the VLAN isn't stable.

Key findings: Suppose the trunk port was missing some VLANs, so when a tenant's VLAN isn't tagged on the trunk, their traffic isn't routed. Also, BGP uses an interface that's dependent on a VLAN that's not properly trunked. So when that VLAN goes down, BGP session drops, causing route withdrawals and connectivity issues.

Solution: Add missing VLANs to the trunk port on the MikroTik. Adjust BGP configuration to use a stable IP address, maybe a loopback or a VLAN that's always up. Update OSPF if necessary, but the main focus is BGP and VLANs.

Verification: Check BGP session stability, test tenant connectivity, monitor logs. Prevention measures involve using loopback for BGP, proper VLAN trunking, and monitoring.

Common pitfalls might include relying on interface IPs for BGP that can go down, not verifying all VLANs on trunk ports, or not checking MTU issues causing BGP flaps.

I need to structure each section with appropriate CLI commands, maybe show before and after configurations. For example, before the trunk port only had VLAN10, after adding VLAN20 and 30. Also, BGP was using an IP from VLAN10, which could go down if the trunk had issues. Changing it to a loopback.

Need to include example log entries showing BGP state changes, and commands like /log print where BGP notifications appear. Also, use /interface bridge vlan add to correct the missing VLANs.

Make sure the CLI commands are in code blocks, explain complex ones with comments. Maybe in the detailed debugging, step through checking VLANs, then BGP, then tie them together. The root cause is the missing VLANs on the trunk leading to interface flapping, which affects BGP because the BGP peer is using that interface's IP.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario: VLAN Trunking in SOHO

## 1. Initial Problem Report and Symptoms
**Report**: Tenants in a multi-tenant building report intermittent internet access.  
**Symptoms**:
- BGP session flaps every 5-10 minutes
- VLAN-tagged traffic drops between floors
- 30% packet loss on VoIP (VLAN 20)
- `/27` subnet (172.18.241.160/27) exhausted, causing DHCP failures
- Affected users: 524 (over 20 VLANs)

---

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  ISP[ISP BGP Peer: 203.0.113.1] -->|BGP/MPLS| RTR[MikroTik RB4011 (ROS v7.12)]
  RTR -->|Eth1: VLAN Trunk| SW[HP Switch]
  SW -->|VLAN 10| T1[Tenant Floor 1]
  SW -->|VLAN 20| T2[Tenant Floor 2]
  SW -->|VLAN 30| T3[Tenant Floor 3]
```

---

## 3. Initial Assessment Steps
1. **Check BGP Peer Status**:
   ```bash
   /routing/bgp/peer print
   # Output:
   # 0  name="ISP" instance=default remote-address=203.0.113.1 state=established
   ```
   
2. **Verify VLAN Trunk Configuration**:
   ```bash
   /interface bridge vlan print
   # BEFORE:
   #   bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=10
   ```

3. **Check Subnet Utilization**:
   ```bash
   /ip pool print
   # Total/27 subnet: 30 addresses, 524 users → Exhaustion confirmed
   ```

---

## 4. Detailed Debugging Process
**Step 1: Capture BGP Flaps**:
```bash
/log print where message ~ "BGP"
# Sample log:
# 08:15:23 bgp,error ISP sent notification: Hold timer expired
# 08:15:25 bgp,info ISP state changed from established to active
```

**Step 2: Test VLAN Connectivity**:
```bash
/tool vlan-test interface=ether1 vlan-id=20 count=10
# 4/10 packets lost → VLAN trunk misconfiguration
```

**Step 3: Debug BGP Timers**:
```bash
/routing/bgp/peer monitor ISP \
  where uptime < 5m && remote.address=203.0.113.1
# Output: Uptime fluctuates between 2m-8m
```

---

## 5. Key Findings & Root Cause
**Root Cause**:
- Missing VLANs (20,30) on trunk port `ether1` caused BGP source IP (172.18.241.161, VLAN 10) to flap
- `/27` subnet unable to support 524 users → DHCP starvation

---

## 6. Solution Implementation
**Step 1: Expand Subnet** (ISP coordination):
```bash
/ip address set [find address=172.18.241.161] network=172.18.241.128/25
```

**Step 2: Fix VLAN Trunk**:
```bash
/interface bridge vlan add bridge=bridge1 tagged=ether1 vlan-ids=20,30
```

**Step 3: Stabilize BGP Source**:
```bash
/routing/bgp/peer set ISP local-address=172.18.241.162
```

---

## 7. Verification Process
1. **Confirm BGP Stability**:
   ```bash
   :delay 10m;/routing/bgp/peer print where state=established
   # Output: ISP uptime > 1hr
   ```

2. **Test VLAN Traffic**:
   ```bash
   /ping 172.18.241.165 src-address=172.18.241.165 count=100 → 0% loss
   ```

---

## 8. Prevention Measures
- Use `/routing/bgp/connection` for BGP multipath
- Implement `/interface bonding` for trunk redundancy
- Enable `/tool romon` for switch-RouterOS sync

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/interface bridge vlan print` | Show VLAN assignments |
| `/routing/bgp/peer monitor 0` | Real-time BGP peer stats |
| `/tool vlan-test` | VLAN connectivity check |

---

## 10. Common Pitfalls to Avoid
- ❌ Using `/27` for multi-tenant DHCP → Always use `/24` or larger
- ❌ Hardcoding BGP `local-address` to VLAN interfaces → Use loopback
- ❌ Forgetting `tagged` ports in `/interface bridge vlan`
```
