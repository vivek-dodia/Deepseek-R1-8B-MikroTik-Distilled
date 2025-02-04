---
generated_at: 2025-02-03T15:57:08.940200
topic: BGP
category: Routing
version: 6.x
scale: SMB
level: Advanced
subnet: 172.17.195.0/25
scenario: VLAN Trunking Issues
environment: Branch Office
affected_users: 433
duration: 7 hours
---

# Analysis Process
Okay, let's tackle this MikroTik BGP troubleshooting scenario. The user wants a detailed example with specific sections. First, I need to make sure I cover all the required parts: problem report, environment, assessment steps, debugging, etc. Let's start with the initial problem. The issue is VLAN trunking affecting BGP in a branch office. Users are experiencing network outages, so symptoms might include BGP peers down, VLANs not trunking properly, and maybe routing tables missing routes.

Next, the environment is a small to medium business with a subnet of 172.17.195.0/25. The network topology should be in Mermaid. Let me visualize that. There's a branch router connected to an ISP router via BGP. The branch router connects to a core switch with VLAN trunking (maybe VLANs 10 and 20). Then the core switch connects to access switches and users. I'll need to represent that in Mermaid syntax.

Initial assessment steps would involve checking BGP status, interface VLAN configurations, trunk ports, and logs. Using commands like /routing bgp peer print, /interface vlan print, /interface ethernet print. Also, checking logs for any BGP or VLAN related errors.

For the detailed debugging process, I'll need to walk through CLI commands. Maybe start with checking BGP peers. If the peer is in established state? If not, check if the IP is reachable. Then look at the VLAN interfaces. Maybe the trunk port isn't allowing all VLANs, or the VLAN IDs are mismatched. Also, check firewall filters that might be blocking BGP traffic (TCP 179). Logs might show connection timeouts or authentication failures.

Root cause could be a misconfigured trunk port on the MikroTik, not allowing VLAN 20, causing the BGP session to drop because the ISP peer is on that VLAN. Then the solution would be correcting the trunk configuration to include VLAN 20. Before and after configs would show the trunk port settings.

Verification would involve checking BGP peers again, pinging the ISP router, and testing user connectivity. Prevention measures include implementing configuration templates, regular audits, monitoring with tools like The Dude, and change management.

In the related commands, include the BGP, VLAN, and logging commands used. Common pitfalls might be forgetting to add VLANs to trunk ports, misconfiguring BGP timers, or firewall rules blocking BGP.

Wait, the scenario says VLAN trunking issues affecting BGP. So maybe the BGP session is running over a VLAN interface that's not properly trunked. If the trunk port on MikroTik is only allowing VLAN 10 but the BGP peer is on VLAN 20, then the traffic isn't passing through. That would cause the BGP peer to go down. So the initial config might have the trunk port with 'vlan-mode=yes' but not specifying the allowed VLANs properly. Changing it to 'vlan-mode=secure' and adding 'vlan-header=add-if-missing' along with the allowed VLANs would fix it.

Also, need to check if the VLAN interface on the MikroTik has the correct IP address. If the VLAN 20 interface is missing or has a wrong IP, BGP can't establish. Let me make sure the example configurations reflect that.

Including log outputs: maybe when BGP tries to connect, there are timeout messages. Or VLAN interface errors. Logs from /log print might show "BGP connection failed" or "interface VLAN20 not found".

I should structure each section step by step, making sure commands are in code blocks and comments explain what's happening. Also, before and after configurations for the trunk port would help. Let me put this all together now, ensuring all parts of the query are addressed.

# Troubleshooting Guide
```markdown
# BGP Troubleshooting Scenario: VLAN Trunking Issues

## 1. Initial Problem Report and Symptoms
**Report:**  
Branch office users (433 employees) report complete network outage lasting 7 hours.  
**Symptoms:**
- BGP peer sessions not establishing
- VLAN-tagged traffic not passing between core switch and router
- 172.17.195.0/25 subnet unreachable
- Inter-VLAN routing failures

## 2. Environment Description
**Network Topology:**
```mermaid
graph TD
    BR[Branch Router (MikroTik RB1100)] -->|VLAN Trunk (10,20)| CS[Core Switch (Cisco 3850)]
    CS -->|VLAN 10| AS1[Access Switch 1]
    CS -->|VLAN 20| AS2[Access Switch 2]
    BR <-.BGP Session.-> ISP[ISP Router (AS65000)]
```

## 3. Initial Assessment Steps
1. Check BGP peer status:
```bash
/routing bgp peer print
# Output:
# 0 name="ISP" instance=default remote-address=172.17.195.126 remote-as=65000 state=active 
```
2. Verify VLAN interfaces:
```bash
/interface vlan print
# Output:
# Flags: X - disabled, R - running 
#  0 R name=vlan10 vlan-id=10 interface=ether1
#  1 X name=vlan20 vlan-id=20 interface=ether1
```
3. Check trunk port configuration:
```bash
/interface ethernet print
# Output:
#  0 name=ether1 mtu=1500 l2mtu=1598 arp=enabled vlan-mode=yes
```

## 4. Detailed Debugging Process
**Step 1: Verify BGP Session Parameters**
```bash
/routing bgp instance print
# Output shows correct AS (65100) but missing router-id

/routing bgp peer print detail where remote-address=172.17.195.126
# authentication=none (should be md5)
```

**Step 2: Inspect VLAN Configuration**
```bash
/interface vlan print detail where name=vlan20
# Shows disabled status and missing IP address
```

**Step 3: Check Trunk Port Settings**
```bash
/interface ethernet monitor ether1
# vlan-mode=yes (should be secure)
# missing vlan-header=add-if-missing
```

**Step 4: Analyze Packet Capture**
```bash
/tool sniffer quick protocol=bgp interface=ether1
# Shows BGP OPEN messages but no replies from ISP
```

**Step 5: Verify Firewall Rules**
```bash
/ip firewall filter print
# Missing rule allowing BGP (TCP/179)
```

## 5. Key Findings & Root Cause
**Root Cause:**  
Misconfigured VLAN trunk port caused BGP peer (172.17.195.126) on VLAN 20 to become unreachable due to:
1. VLAN 20 interface disabled
2. Improper trunk port configuration (`vlan-mode=yes` instead of `secure`)
3. Missing BGP firewall allowance

## 6. Solution Implementation
**Before (Faulty Configuration):**
```bash
/interface ethernet set ether1 vlan-mode=yes
/interface vlan set vlan20 disabled=yes
```

**After (Corrected Configuration):**
```bash
# Configure trunk port properly
/interface ethernet set ether1 vlan-mode=secure vlan-header=add-if-missing

# Enable VLAN 20 interface
/interface vlan set vlan20 disabled=no
/ip address add address=172.17.195.65/25 interface=vlan20

# Add BGP firewall rule
/ip firewall filter add chain=input protocol=tcp dst-port=179 action=accept
```

## 7. Verification Process
1. Confirm BGP session establishment:
```bash
/routing bgp peer print 
# 0 name="ISP" ... state=established
```
2. Test VLAN trunking:
```bash
ping 172.17.195.126 interface=vlan20
# 64 bytes from 172.17.195.126: time=15ms
```
3. Validate routing table:
```bash
/ip route print 
# B 172.17.195.0/25 via 172.17.195.126
```

## 8. Prevention Measures
1. Implement configuration templates for VLAN interfaces
2. Enable BGP logging:
```bash
/routing bgp instance set default debug=yes
```
3. Regular topology audits using:
```bash
/system script add name=topology_check source="/interface vlan print;/routing bgp peer print"
```

## 9. Related Commands Reference
| Purpose | Command |
|---------|---------|
| BGP Status | `/routing bgp peer print` |
| VLAN Check | `/interface vlan print` |
| Trunk Config | `/interface ethernet print detail` |
| BGP Debug | `/routing bgp event log print where topic~"peer|update"` |

## 10. Common Pitfalls to Avoid
1. **VLAN Mode Misconfiguration:**  
   `vlan-mode=yes` (legacy mode) vs `vlan-mode=secure`

2. **Missing Interface Binding:**  
   Always specify parent interface in VLAN config

3. **BGP Authentication Mismatch:**  
   Ensure matching MD5 passwords:
```bash
/routing bgp peer set ISP password=securekey123
```

4. **Firewall Blocking:**  
   Always test with firewall temporarily disabled:
```bash
/ip firewall set enabled=no
```

**Log Example:**  
```
router/system,error bgp,error,peer,state Router failed to establish BGP session: TCP connection failed
```
```
