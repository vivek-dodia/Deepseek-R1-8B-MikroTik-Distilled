---
generated_at: 2025-02-03T16:01:42.697449
topic: BGP
category: Routing
version: 6.x
scale: Enterprise
level: Advanced
subnet: 172.25.72.224/27
scenario: VLAN Trunking Issues
environment: Remote Site
affected_users: 640
duration: 19 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP with VLAN trunking issues in an enterprise environment. Let me start by breaking down each section and what it requires.

First, the initial problem report and symptoms. The users are experiencing intermittent connectivity, so I should mention that. Maybe VLANs aren't trunking properly, leading to BGP session drops. The remote site has 640 users on subnet 172.25.72.224/27. The issue has been ongoing for 19 hours. Symptoms might include BGP neighbors flapping, high latency, packet loss, VLAN traffic not passing through the trunk, maybe even some log entries showing BGP state changes.

Next, the environment description and network topology. Since it's a remote site, the setup probably has a MikroTik router connected to a core switch, which then connects to access switches. The VLANs (maybe voice, data, IoT) are trunked over a link. Need to represent this in Mermaid. The router's interface connected to the core switch should have VLANs configured. BGP peers with the core router and another site.

Initial assessment steps: Check BGP status, interface VLAN configurations, logs for errors. Use commands like `/routing bgp neighbor print`, `/interface vlan print`, maybe `log print` around the time the issue started. Also check traffic on VLAN interfaces and physical ports.

Detailed debugging process. Start with verifying BGP sessions. If neighbors are established, maybe look at routes exchanged. Check if the VLAN trunk is allowing all necessary VLANs. Maybe the MTU is mismatched, causing fragmentation and BGP issues. Use commands like `/interface ethernet monitor` on the trunk port to check MTU. Look at BGP logs with `/routing bgp log print where message~"state changed"`. Check for VLAN filtering or missing VLAN entries on the trunk port. Maybe the trunk port isn't set to `frame-types=admit-only-vlan-tagged`, causing some native VLAN issues. Also, check for CRC errors on the physical interface which could indicate a bad cable or port.

Key findings and root cause analysis. Suppose the trunk port was misconfigured with the wrong frame-type, allowing untagged traffic which conflicts with the native VLAN. Or maybe a missing VLAN ID on the trunk, causing BGP (which runs over a specific VLAN) to drop when that VLAN isn't properly trunked. Another possibility is MTU mismatch leading to TCP MSS issues, making BGP sessions unstable.

Solution implementation steps: Correct the trunk port configuration to admit only VLAN-tagged frames, add missing VLANs, adjust MTU settings. For example, setting `frame-types=admit-only-vlan-tagged` on the trunk interface. Update VLAN configurations and BGP settings if necessary.

Verification process: Check BGP sessions are stable, test VLAN connectivity, monitor logs and traffic. Use `ping` over VLAN interfaces, check BGP routes with `/routing bgp advertisements print`.

Prevention measures: Implement configuration templates, regular audits, enable logging for BGP and interfaces, test MTU consistency across the network.

Related commands: List all the commands used in the steps, like checking BGP neighbors, VLAN interfaces, logs, etc.

Common pitfalls: Forgetting to set frame-types on trunk ports, MTU mismatches, not enabling BGP logging, missing VLANs on switches.

I need to make sure the CLI commands are accurate for RouterOS 6.x. For example, in version 6.x, the BGP configuration is under `/routing bgp` and not the newer `/routing/bgp` in v7. Also, VLAN configuration on interfaces uses `vlan-id` and `interface` parameters. MTU settings on both physical and VLAN interfaces are crucial because if the physical interface's MTU is 1500, the VLAN interface would need to account for the tag, but in practice, MikroTik handles this automatically if the physical interface's MTU is set correctly.

Wait, but if the physical link has an MTU of 1500, adding a VLAN tag (4 bytes) would make the frame 1504, which could cause issues if the network devices don't support jumbo frames. So maybe the physical interface's MTU should be 1504, or the TCP MSS adjusted. However, RouterOS might handle this with `ip tcp-mss` settings. Alternatively, if the trunk link's MTU is set to 1500 on both ends but VLAN interfaces are using 1500, the encapsulated frames would be too big, leading to fragmentation. BGP uses TCP, so if the MSS isn't adjusted, the sessions could have problems.

In the scenario, maybe the core switch expects VLAN-tagged frames but the MikroTik was sending untagged (native VLAN) which was conflicting. So setting `frame-types=admit-only-vlan-tagged` on the MikroTik's trunk port would prevent untagged traffic, ensuring that all VLANs are properly tagged. If a necessary VLAN wasn't allowed on the trunk, the BGP session (which might be running over a specific VLAN) would drop when that VLAN isn't present.

Also, checking if the BGP neighbor is configured with the correct IP address that's reachable via the correct VLAN interface. If the BGP session is supposed to be over VLAN 200, but the neighbor's IP is on that VLAN, but the trunk wasn't allowing VLAN 200, then the session can't establish.

In the logs, you might see BGP state changes from Established to Active or Idle. Using the command `/routing bgp log print where message~"state changed"` would show those events.

Another thing to check is the update-source for BGP. If the BGP session is sourced from a VLAN interface that's down or not properly configured, the neighbor relationship would fail.

Putting this all together, the root cause could be a combination of VLAN trunking misconfiguration (missing VLANs or incorrect frame-types) leading to BGP session instability. The solution would involve correcting the trunk port settings, ensuring all necessary VLANs are allowed, and verifying MTU settings to prevent fragmentation.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS BGP Troubleshooting Scenario: VLAN Trunking Issues

## 1. Initial Problem Report and Symptoms
**Reported Issues**:  
- Intermittent WAN connectivity at remote site (172.25.72.224/27)  
- BGP sessions flapping between remote site and core routers  
- VLAN traffic (Voice/Data) failing to traverse trunk link  

**Observable Symptoms**:  
- BGP neighbor state changes: `Established` ↔ `Active`  
- High packet loss (`ping 172.25.72.225 loss=45%`)  
- VLAN interfaces show `running=no` intermittently  
- Logs: `BGP connection closed` and `VLAN interface disabled`

---

## 2. Environment Description & Network Topology
**Network Scale**: Enterprise (640 users)  
**RouterOS Version**: 6.49.7  
**Key Devices**:  
- Remote Site Router (MikroTik CCR1016)  
- Core Switch (Cisco Catalyst 9500)  
- Access Switches (Stacked Cisco 3850s)  

```mermaid
graph TD
  A[Remote MikroTik Router] -- VLAN Trunk (ether1) --> B[Core Switch]
  B -- VLAN 200 (Data) --> C[Access Switch 1]
  B -- VLAN 201 (Voice) --> D[Access Switch 2]
  B -- BGP Peering --> E[Core Router (AS65000)]
  A -. BGP Peering .-> F[DR Site Router (AS65001)]
```

---

## 3. Initial Assessment Steps
1. **Verify BGP Status**:
   ```bash
   /routing bgp neighbor print
   # Output:
   # 0 name="Core" remote-address=172.25.72.225 remote-as=65000 state="Established"
   # 1 name="DR" remote-address=10.10.10.2 remote-as=65001 state="Active"
   ```

2. **Check VLAN Interfaces**:
   ```bash
   /interface vlan print
   # Flags: X - disabled, R - running
   # 0 R name="VLAN200" vlan-id=200 interface=ether1
   # 1   name="VLAN201" vlan-id=201 interface=ether1
   ```

3. **Review Logs**:
   ```bash
   /log print where time~19h && message~"BGP|VLAN"
   # Output:
   # 08:32:21 bgp,error BGP session closed with 172.25.72.225
   # 09:15:47 interface VLAN200 disabled due to no carrier
   ```

---

## 4. Detailed Debugging Process
**Step 1: Validate Trunk Port Configuration**  
Check trunk port `ether1` settings:
```bash
/interface ethernet print detail where name=ether1
# Before:
# mtu=1500 auto-negotiation=yes frame-types=admit-all
```

**Step 2: Test VLAN Connectivity**  
Ping core router via VLAN200:
```bash
/ping 172.25.72.225 src-address=172.25.72.226
# SEQ LOSS%  STATUS
# 1   100%  timeout
```

**Step 3: Capture Traffic on Trunk**  
Use packet sniffer:
```bash
/tool sniffer quick interface=ether1 filter-port=179
# Output shows TCP retransmissions on port 179 (BGP)
```

**Step 4: Check MTU Mismatch**  
Verify MTU consistency:
```bash
/interface vlan print detail where name=VLAN200
# mtu=1500 (inherits from ether1)
# Core switch trunk MTU: 1522 (Jumbo frames enabled)
```

---

## 5. Key Findings & Root Cause Analysis
**Root Cause**:  
- **MTU Mismatch**: Trunk port `ether1` MTU (1500) < Core Switch MTU (1522), causing BGP packet fragmentation.  
- **VLAN Filtering**: `frame-types=admit-all` allowed untagged traffic, corrupting VLAN201 carrier.  

**Impact**:  
- BGP updates fragmented → TCP retransmissions → Session resets  
- Untagged traffic flooded VLAN201 interface → Intermittent carrier loss  

---

## 6. Solution Implementation Steps
1. **Adjust Trunk Port MTU**:
   ```bash
   /interface ethernet set ether1 mtu=1522
   ```

2. **Enforce VLAN Tagging**:
   ```bash
   /interface ethernet set ether1 frame-types=admit-only-vlan-tagged
   ```

3. **Update VLAN Interface MTU**:
   ```bash
   /interface vlan set VLAN200 mtu=1500
   /interface vlan set VLAN201 mtu=1500
   ```

---

## 7. Verification Process
1. **Confirm BGP Stability**:
   ```bash
   /routing bgp neighbor print
   # 0 name="Core" state="Established" uptime=2h
   ```

2. **Test VLAN Traffic**:
   ```bash
   /ping 172.25.72.225 src-address=172.25.72.226 count=10
   # 10 packets transmitted, 0% loss
   ```

3. **Validate MTU**:
   ```bash
   /interface ethernet monitor ether1
   # mtu:1522 frame-types:admit-only-vlan-tagged
   ```

---

## 8. Prevention Measures
- **Standardize MTU**: Enforce 1522 MTU on all trunk ports  
- **BGP Keepalives**: Reduce hold timer to 30s for faster detection  
- **Monitoring**: Enable SNMP traps for BGP state changes  
- **Config Audits**: Weekly checks of VLAN/BGP configurations  

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp neighbor print` | Check BGP peer status |
| `/interface vlan monitor [find]` | VLAN interface diagnostics |
| `/tool sniffer quick` | Packet capture |
| `/log print where message~"BGP"` | Filter BGP logs |

---

## 10. Common Pitfalls to Avoid
- **MTU Ignorance**: Always match MTU across L2 devices  
- **VLAN Tagging**: Never use `admit-all` on trunks in mixed VLAN environments  
- **BGP Timers**: Avoid asymmetric hold timers between peers  
- **Logging Neglect**: Enable `bgp-log=yes` in `/routing bgp template`  
```bash
/routing bgp template set default bgp-log=yes
```

**After Configuration Snippet**:
```bash
/interface ethernet
set ether1 mtu=1522 frame-types=admit-only-vlan-tagged
/interface vlan
set VLAN200 mtu=1500
set VLAN201 mtu=1500
```
