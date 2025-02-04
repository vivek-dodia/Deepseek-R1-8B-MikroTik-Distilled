---
generated_at: 2025-02-03T16:23:30.624374
topic: RIP
category: Routing
version: 6.x
scale: SOHO
level: Expert
subnet: 10.72.165.16/28
scenario: Firewall Rule Conflicts
environment: Remote Site
affected_users: 257
duration: 6 hours
---

# Analysis Process
Okay, let's tackle this MikroTik RIP troubleshooting scenario. The user wants a detailed scenario with specific sections, including CLI commands, network topology, and more. Let me start by breaking down each part of the query to ensure I cover everything.

First, the topic is RIP on RouterOS 6.x in a SOHO network. The subnet given is 10.72.165.16/28, which is a small subnet with 14 usable IPs. The environment is a remote site with firewall rule conflicts affecting 257 users over 6 hours. Wait, 257 users on a /28 subnet? That doesn't add up. A /28 has 16 addresses, subtract network and broadcast, so 14 hosts. Maybe it's a typo, but I'll note that in the initial problem report as a possible inconsistency.

For the network topology in Mermaid, I need to visualize a SOHO setup. Typically, a remote site might have a MikroTik router connected to the main office via a WAN link, and a LAN with the given subnet. Maybe a couple of switches and APs. Let me sketch that out.

Initial assessment steps would include checking RIP status, routes, neighbor adjacencies, and firewall rules. Since the issue is firewall conflicts, I should focus on how firewall rules might be blocking RIP traffic. RIP uses UDP port 520, so checking for rules that drop UDP 520 or multicast addresses (224.0.0.9) would be important.

In the debugging process, CLI commands like `/routing rip neighbor print`, `/routing route print`, and checking firewall filters with `/ip firewall filter print` would be relevant. Maybe looking at logs where RIP updates are being dropped.

Root cause might be a firewall rule that's blocking RIP updates, perhaps a generic block rule that was added without considering RIP's requirements. For example, a rule that drops all UDP traffic except DNS, which would inadvertently block RIP.

Solution steps would involve adjusting the firewall rules to allow RIP traffic, placing the accept rules above the drop rules. Verification would include checking routes after the fix and confirming connectivity.

Prevention measures could include documenting firewall rules, testing changes in a lab, using specific rather than generic rules, and monitoring RIP status regularly.

Common pitfalls might be not considering multicast addresses in firewall rules, or misordering firewall rules which causes legitimate traffic to be blocked.

Wait, the user mentioned 257 users, but the subnet is /28. That's a discrepancy. Maybe the subnet is part of a larger network, or maybe it's a typo. I should mention that in the initial problem report as a symptom, like "users report inability to access resources, despite subnet size suggesting fewer users" or maybe the 257 is across multiple sites. But since it's a SOHO, maybe the 257 is a mistake. I'll include it as a reported symptom but note the inconsistency.

Also, for the Mermaid diagram, make sure to include the remote site router connected to the main office, with LAN devices on the 10.72.165.16/28 subnet. Maybe a switch and some PCs.

Including before and after firewall configurations would help. Before, there might be a drop rule for UDP that's blocking RIP, and after inserting an accept rule above it.

Log examples could show packets dropped on port 520. CLI commands to check logs, maybe `/log print` and filter for RIP or firewall entries.

Okay, putting it all together step by step, making sure each section is covered with the required details. Need to ensure CLI commands are accurate for RouterOS 6.x, as some syntax might differ in newer versions. For example, in 6.x, RIP configuration is under `/routing rip` whereas in later versions it's under `/routing rip instance`.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP Firewall Conflict (v6.x)

## 1. Initial Problem Report and Symptoms
**Report**: Remote SOHO site (10.72.165.16/28) reports complete network outage affecting 257 users.  
**Symptoms**:
- No RIP routes visible in routing table
- Intermittent connectivity to main office
- Users cannot access centralized resources
- Subnet size (14 usable IPs) vs user count mismatch (possible VLAN misreporting)
- Issue persists for 6 hours after recent firewall "optimization"

## 2. Environment Description & Network Topology
```mermaid
graph TD
    A[Main Office Router] <--> |RIP over IPSec| B[MikroTik RB951Ui-2HnD]
    B --> C[SOHO Switch]
    C --> D[AP1 (10.72.165.17)]
    C --> E[AP2 (10.72.165.18)]
    C --> F[VoIP Phone (10.72.165.19)]
    style B stroke:#f66,stroke-width:4px
```

## 3. Initial Assessment Steps
1. Verify RIP service status:
```bash
/routing rip interface print
# Output: Shows empty neighbor list
```

2. Check basic connectivity:
```bash
/ping 10.72.165.1 from=10.72.165.20
# Output: 10 packets transmitted, 0 received
```

3. Review firewall filter rules:
```bash
/ip firewall filter print where comment~"RIP"
# Output: No entries found
```

## 4. Detailed Debugging Process
**Step 1: Verify RIP Configuration**
```bash
/routing rip instance print
# Output:
# 0 name="default" afi=both originate-default=never redistribute-static=no
```

**Step 2: Check Routing Table**
```bash
/ip route print where protocol=rip
# Output: No RIP routes present
```

**Step 3: Capture RIP Traffic**
```bash
/tool sniffer quick protocol=udp port=520
# Output shows no incoming RIP updates
```

**Step 4: Analyze Firewall Drops**
```bash
/ip firewall filter add chain=forward action=log log-prefix="RIP-DEBUG" \
  protocol=udp dst-port=520
/log print follow
# Sample log:
# RIP-DEBUG forward: in:ether1 out:bridge proto UDP ... SRC:10.72.165.1:520 DST:224.0.0.9:520 ACTION:drop
```

## 5. Key Findings & Root Cause
**Findings**:
- Firewall rule #5 blocking UDP/520 and multicast (224.0.0.9)
- RIP authentication mismatch not configured (ruled out)
- No routes being propagated between sites

**Root Cause**:
```bash
/ip firewall filter print
# Before:
# 5 chain=forward action=drop protocol=udp dst-port=520-599 \
#   comment="Block suspicious UDP"
```
New firewall rule (#5) implemented 6 hours ago inadvertently blocks:
- RIP multicast updates (224.0.0.9)
- UDP/520 traffic
- Positioned above allow rules

## 6. Solution Implementation
**Step 1: Create RIP Allow Rules**
```bash
/ip firewall filter add chain=forward protocol=udp dst-port=520 \
  action=accept place-before=5 comment="Allow RIP Updates"
/ip firewall filter add chain=forward protocol=udp dst-address=224.0.0.9 \
  action=accept place-before=5 comment="Allow RIP Multicast"
```

**Step 2: Verify Rule Order**
```bash
/ip firewall filter print
# After:
# 4 chain=forward action=accept ... comment="Allow RIP Multicast"
# 5 chain=forward action=accept ... comment="Allow RIP Updates"
# 6 chain=forward action=drop ... comment="Block suspicious UDP"
```

## 7. Verification Process
**Check 1: RIP Neighbors**
```bash
/routing rip neighbor print
# Output:
# 0 instance=default address=10.72.165.1 uptime=5m
```

**Check 2: Route Propagation**
```bash
/ip route print where protocol=rip
# Output:
# 0 dst-address=192.168.1.0/24 gateway=10.72.165.1 distance=1
```

**Check 3: End-to-End Test**
```bash
/ping 192.168.1.1 from=10.72.165.20
# Output: 10 packets transmitted, 10 received
```

## 8. Prevention Measures
1. Implement change control process for firewall modifications
2. Create network documentation with service port matrix
3. Add monitoring for RIP neighbors:
```bash
/tool netwatch add host=10.72.165.1 timeout=60s up-script="/log info \"RIP Neighbor UP\"" \
  down-script="/log warning \"RIP Neighbor DOWN\""
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing rip interface print` | Show RIP interfaces |
| `/ip firewall filter move numbers=from=4 to=0` | Reorder firewall rules |
| `/tool sniffer quick protocol=udp port=520` | Capture RIP traffic |

## 10. Common Pitfalls to Avoid
- **Rule Ordering**: Always position allow rules above generic drop rules
- **Multicast Filtering**: Remember RIP uses 224.0.0.9 for updates
- **Version Mismatch**: Ensure all routers use RIP v2 (v1 lacks authentication)
- **Subnet Size**: Confirm actual user count matches subnet capacity
- **Silent Drops**: Use firewall logging before implementing new drop rules
```
