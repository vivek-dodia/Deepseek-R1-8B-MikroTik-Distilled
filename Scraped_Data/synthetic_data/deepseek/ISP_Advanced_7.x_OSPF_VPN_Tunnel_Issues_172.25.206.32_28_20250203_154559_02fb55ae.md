---
generated_at: 2025-02-03T15:46:51.924669
topic: OSPF
category: Routing
version: 7.x
scale: ISP
level: Advanced
subnet: 192.168.22.0/25
scenario: VPN Tunnel Issues
environment: Edge Location
affected_users: 513
duration: 11 hours
---

# Analysis Process
Okay, let's tackle this MikroTik OSPF troubleshooting scenario. The user wants a detailed example for an ISP edge location with VPN tunnel issues affecting over 500 users for 11 hours. I need to cover all the sections they listed, so I'll start by breaking down each part step by step.

First, the initial problem report. They mentioned VPN tunnel issues impacting 513 users. Symptoms probably include OSPF neighbors down, routes missing, and VPN tunnel flapping. Maybe users can't reach certain services, like their core data center. The duration is 11 hours, so maybe the problem started after a maintenance window.

Next, the environment description. The subnet is 192.168.22.0/25, which is a /25, so maybe used for internal addressing. Since it's an ISP edge location, there's likely an edge router connected to a core router via a VPN. The Mermaid diagram needs to show the Edge Router (ER01) connected to Core Router (CR01) via a VPN tunnel. The users are behind ER01. Also, maybe a backup link like BGP, but that's not the focus here. OSPF is used for dynamic routing over the VPN.

Initial assessment steps: Check OSPF neighbors, routes, interface status, VPN tunnel status. Use commands like `/routing ospf neighbor print`, `/routing ospf route print`, `/interface print`, and check the VPN interface (e.g., EoIP or GRE). Also look at logs for OSPF or VPN errors.

For detailed debugging, start with checking OSPF neighbors. If neighbors are down, check if the VPN tunnel is up. Maybe the tunnel is established but OSPF isn't forming adjacency. Check OSPF configuration: area settings, network ranges, authentication. If there's authentication, maybe a mismatch. Look at OSPF logs with `log print where topics=ospf`. Check MTU issues, since VPN tunnels can have MTU mismatches. Use `ping` with do-not-fragment to test. Also, check for firewall filters blocking OSPF traffic (protocol 89). Commands like `/ip firewall filter print` where protocol=89.

Key findings might be MTU mismatch because the VPN tunnel's MTU is lower than the physical interface, causing OSPF packets to be dropped. Or maybe OSPF is configured on the wrong interface. If the MTU is 1476 on the tunnel but the OSPF is using 1500, then packets get fragmented but maybe the ISP is blocking fragmented packets. That would cause OSPF hello packets to be dropped, leading to adjacency failures.

Solution: Adjust OSPF MTU to match the tunnel's MTU. Or adjust the tunnel's MTU if possible. Alternatively, enable TCP MSS clamping on the VPN interface. Update the OSPF network configuration to the correct subnet. Also, ensure firewall rules allow OSPF.

Verification: After changing MTU settings, check OSPF neighbors come up. Verify routes are exchanged. Test user connectivity. Use the same commands as initial assessment.

Prevention measures: Regular checks on VPN and OSPF status. Monitoring MTU settings. Implementing OSPF authentication. Documenting network changes.

Common pitfalls: Forgetting to adjust MTU on VPN tunnels, misconfiguring OSPF networks, or firewall rules blocking protocol 89.

Need to include CLI commands with comments, like checking OSPF neighbors, routes, interface details. Maybe before and after configurations showing the MTU change in OSPF. Log examples where OSPF packets are too big.

I should make sure the Mermaid diagram correctly represents the network topology with ER01 connected via VPN to CR01, and users in the 192.168.22.0/25 subnet. Include the backup BGP link as well.

Also, think about the root cause analysis. If the VPN uses an MTU of 1476, and OSPF is trying to send 1500-byte packets, those would need to fragment. If the ISP blocks fragments, the OSPF packets get dropped, leading to neighbor timeouts. Adjusting OSPF's interface MTU to match the tunnel's MTU would fix that.

Including example log entries where OSPF detects packet size issues. Maybe a line like "OSPF: Packet too large, MTU 1500, interface MTU 1476" or similar.

For the commands reference, list all the commands used in the debugging steps, like ospf neighbor print, interface print, ping with size and do-not-fragment, firewall filter checks, etc.

Okay, putting it all together now, making sure each section is covered with the necessary details and examples. Use code blocks for CLI commands, mermaid for the diagram, and include before/after configs where relevant.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF VPN Tunnel Issues

## 1. Initial Problem Report and Symptoms
**Report**:  
Users at the edge location (192.168.22.0/25) reported intermittent loss of connectivity to core services (e.g., billing, CRM) for 11 hours. VPN tunnel flapping observed.

**Symptoms**:
- OSPF adjacency between Edge Router (ER01) and Core Router (CR01) unstable.
- VPN tunnel interface (`eoip-tunnel1`) transitions between `running` and `disabled`.
- Missing OSPF routes in `/routing/ospf/route`.
- 513 users unable to access core subnets (10.10.0.0/16).

---

## 2. Environment Description & Network Topology
```mermaid
graph TD
  ER01[Edge Router (ER01)
      192.168.22.1/25
      OSPF Area 0.0.0.0
      VPN Tunnel: eoip-tunnel1] -->|VPN (Public IPs: 203.0.113.1 ↔ 198.51.100.1)| CR01[Core Router (CR01)
                                                                                      10.10.0.1/16
                                                                                      OSPF Area 0.0.0.0]
  ER01 -->|LAN| Users[Users: 192.168.22.0/25]
  CR01 -->|BGP| ISP_Backbone[ISP Backbone]
```

---

## 3. Initial Assessment Steps
1. **Check OSPF neighbor status**:
   ```bash
   /routing ospf neighbor print
   # Output: CR01 shows "Full" state intermittently; frequent "Down" events.
   ```
2. **Verify VPN tunnel status**:
   ```bash
   /interface eoip print
   # Output: `eoip-tunnel1` status: `running` ↔ `disabled` (flapping)
   ```
3. **Review OSPF routes**:
   ```bash
   /routing ospf route print
   # Output: Core routes (10.10.0.0/16) missing during outages.
   ```
4. **Check firewall filters**:
   ```bash
   /ip firewall filter print where protocol=89
   # Output: No rules blocking OSPF (protocol 89).
   ```

---

## 4. Detailed Debugging Process
**Step 1: Capture OSPF and VPN logs**:
```bash
/log print where topics=ospf,vpn
# Log Example:
# 2023-10-01 08:15:23 ospf,error CR01: OSPF packet too large (1500 bytes) on eoip-tunnel1 (MTU 1476)
# 2023-10-01 08:15:25 vpn,error eoip-tunnel1: MTU mismatch detected
```

**Step 2: Test VPN tunnel MTU**:
```bash
/ping 10.10.0.1 size=1476 do-not-fragment=yes
# Output: 100% packet loss (fragmentation required but DF set)
```

**Step 3: Verify OSPF MTU settings**:
```bash
/interface print where name=eoip-tunnel1
# Output: mtu=1476 (tunnel) vs. OSPF default mtu=1500
```

**Step 4: Check OSPF network configuration**:
```bash
/routing ospf network print
# Before Fix:
# network=192.168.22.0/25 area=backbone (Incorrect area ID)
```

---

## 5. Key Findings & Root Cause Analysis
**Root Cause**:  
- **MTU Mismatch**: VPN tunnel (`mtu=1476`) dropped OSPF packets (1500 bytes) due to DF bit set.
- **OSPF Area Misconfiguration**: ER01 OSPF network assigned to `backbone` instead of `0.0.0.0`.

**Impact**:  
Fragmented OSPF packets blocked by ISP, causing adjacency flapping and route loss.

---

## 6. Solution Implementation
**Step 1: Adjust OSPF MTU to match VPN tunnel**:
```bash
/interface set eoip-tunnel1 mtu=1476
/routing ospf interface-template set interface=eoip-tunnel1 mtu=1476
```

**Step 2: Correct OSPF area configuration**:
```bash
/routing ospf network set numbers=0 network=192.168.22.0/25 area=0.0.0.0
```

**Step 3: Enable TCP MSS clamping** (prevent future MTU issues):
```bash
/ip firewall mangle add chain=forward out-interface=eoip-tunnel1 protocol=tcp tcp-flags=syn action=change-mss new-mss=1436
```

---

## 7. Verification Process
1. Confirm OSPF adjacency stability:
   ```bash
   /routing ospf neighbor print
   # Output: CR01 state=Full, uptime=2h+
   ```
2. Validate core routes:
   ```bash
   /ip route print where dst-address=10.10.0.0/16
   # Output: OSPF route active, gateway=10.10.0.1
   ```
3. Test end-user connectivity:
   ```bash
   /ping 10.10.0.1 from=192.168.22.10
   # Output: 0% packet loss
   ```

---

## 8. Prevention Measures
- **MTU Consistency**: Enforce `mtu=1476` on all VPN-facing interfaces.
- **OSPF Monitoring**: Use `Toolbox` scripts to alert on OSPF state changes.
- **Pre-Change Validation**: Test MTU settings before deploying OSPF/VPN changes.

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Check OSPF adjacency status |
| `/interface monitor eoip-tunnel1` | Monitor VPN tunnel state |
| `/ip firewall filter print where protocol=89` | Verify OSPF traffic rules |
| `/tool sniffer quick protocol=89` | Capture OSPF packets |

---

## 10. Common Pitfalls to Avoid
- **Ignoring MTU**: Always match OSPF MTU to the lowest link in the path (e.g., VPN tunnels).
- **Area ID Mismatch**: Use `0.0.0.0` for backbone areas in RouterOS (not `backbone`).
- **Firewall Rules**: Avoid blocking protocol 89 or VPN encapsulation protocols (e.g., IP protocol 47 for GRE).
```
