---
generated_at: 2025-02-03T16:11:18.960259
topic: BGP
category: Routing
version: 7.x
scale: SMB
level: Basic
subnet: 172.21.85.0/24
scenario: Firewall Rule Conflicts
environment: Industrial Network
affected_users: 414
duration: 24 hours
---

# Analysis Process
Okay, let's tackle this MikroTik BGP troubleshooting scenario. The user wants a detailed example with specific elements, so I need to cover all the sections they listed. Let me start by understanding the requirements.

First, the topic is BGP in RouterOS 7.x for an SMB-scale industrial network with the subnet 172.21.85.0/24. The issue is firewall rule conflicts affecting 414 users over 24 hours. I need to create a realistic scenario that fits these parameters.

Starting with the Initial Problem Report. Symptoms would likely include BGP peers down, routing instability, maybe traffic not passing through. Since it's a firewall conflict, perhaps the BGP port 179 is being blocked by a firewall rule. Also, considering the environment is industrial, maybe there are strict firewall policies that were updated, causing the conflict.

For the network topology in Mermaid, the SMB network might have two routers connected to an industrial switch, with the subnet and some devices. Need to make sure the Mermaid code is correct and represents the setup.

Initial assessment steps: Check BGP status with commands like /routing bgp peer print. Look at the firewall rules, especially filter and NAT. Check logs for denied packets. Verify if BGP sessions are established.

Debugging process: Use commands to check BGP peers, look at the firewall rules, maybe tcpdump to capture traffic on port 179. Check if the firewall is dropping BGP packets. Compare before and after configurations. Maybe a recent firewall rule added by an admin is blocking the BGP traffic.

Root cause analysis: A firewall rule intended to restrict access to industrial devices is blocking BGP TCP/179. The rule was placed above the BGP allow rule, causing it to take precedence.

Solution: Adjust the firewall rule order to allow BGP before the restrictive rules. Add a specific rule for BGP if missing.

Verification: Check BGP peer status again, test connectivity, monitor traffic.

Prevention measures: Document firewall rules, test changes in a lab, use a change management process.

Common pitfalls: Wrong rule order, not testing after changes, forgetting NAT interactions.

I need to structure each section properly, include CLI commands with code blocks, example log outputs, and before/after configs. Make sure the commands are for RouterOS 7.x. Also, the network topology in Mermaid should be accurate. Let me check the syntax for Mermaid to ensure it's correct.

In the firewall rules, perhaps the input chain has a drop rule for unexpected traffic that's blocking BGP. The order of rules matters, so if the allow for BGP is after the drop, it won't work. That's a common issue.

Example log entries might show packets dropped on port 179. CLI commands like /log print where topics=firewall would show those entries.

For the before and after configurations, show the relevant firewall rules. Before, the BGP allow is below a drop; after, moving it above.

In the related commands, include BGP peer checks, firewall rule checks, log checks, and tcpdump.

Need to make sure all parts of the user's query are addressed. They mentioned 414 users, 24-hour duration, industrial environment. Emphasize the impact on production due to the industrial setting, maybe critical machinery losing connectivity.

Okay, putting it all together step by step, making sure each section flows logically. Use markdown formatting with headers, code blocks for CLI, mermaid diagram, and bullet points where needed. Check for typos and accuracy.

# Troubleshooting Guide
```markdown
# BGP Troubleshooting Scenario: Firewall Rule Conflicts

## 1. Initial Problem Report and Symptoms
**Report:** Industrial control systems (414 users) lost connectivity to central monitoring systems for 24 hours.  
**Symptoms:**
- Intermittent BGP neighbor flapping (172.21.85.1 ⇄ 172.21.85.2)
- Industrial PLCs unreachable via OSPF-learned routes
- High CPU on edge routers during traffic spikes
- `/ip route` table missing BGP routes
```bash
[admin@RouterOS] > /routing bgp peer print 
 0 name="Peer_A" instance=default remote-address=172.21.85.2 state=established 
 1 name="Peer_B" instance=default remote-address=172.21.85.3 state=idle
```

## 2. Environment Description
**Network Topology:**
```mermaid
graph TD
    A[Core Router (BGP AS 65501)] -->|172.21.85.0/24| B[Industrial Switch]
    B --> C[PLC Controller]
    B --> D[HMI Station]
    B --> E[Safety System]
    A -->|BGP| F[Edge Router (BGP AS 65502)]
```

## 3. Initial Assessment Steps
1. Verify BGP peer status:
   ```bash
   /routing bgp peer print where disabled=no
   ```
2. Check firewall filters:
   ```bash
   /ip firewall filter print where chain=input
   ```
3. Review connection tracking:
   ```bash
   /ip firewall connection print where protocol=tcp dst-port=179
   ```
4. Check route advertisement:
   ```bash
   /routing bgp advertisements print
   ```

## 4. Detailed Debugging Process
**Step 1: Identify BGP session issues**
```bash
[admin@RouterOS] > /routing bgp session print detail 
  remote-address: 172.21.85.2 state: established last-state: active 
    updates:        sent: 15 received: 0
    withdrawn:      sent: 0 received: 7
```

**Step 2: Firewall packet sniffing**
```bash
/interface list=all tcpdump port 179
```
**Output:**
```
17:45:23.123 IP 172.21.85.1.179 > 172.21.85.2.54123: Flags [S], seq 12345, length 0
17:45:23.125 IP 172.21.85.2 > 172.21.85.1: ICMP type 3 (unreachable port)
```

**Step 3: Analyze firewall rules**
```bash
/ip firewall filter print where dst-port=179
```
**Before Fix:**
```bash
Flags: X - disabled, I - invalid
 0  chain=input action=drop protocol=tcp dst-port=179 log=yes 
 1  chain=input action=accept protocol=tcp dst-port=179 src-address=172.21.85.0/24
```

## 5. Key Findings & Root Cause
**Root Cause:** Firewall rule #0 dropping BGP (TCP/179) traffic before rule #1 could process it  
**Impact Analysis:**
- 100% packet loss between AS 65501 ↔ 65502
- Route withdrawals caused OSPF convergence issues
- Industrial devices used BGP-learned default routes

## 6. Solution Implementation
**Step 1: Reorder firewall rules**
```bash
/ip firewall filter move 1 destination=0
```

**After Fix:**
```bash
 0  chain=input action=accept protocol=tcp dst-port=179 src-address=172.21.85.0/24
 1  chain=input action=drop protocol=tcp dst-port=179 log=yes
```

**Step 2: Soft-reset BGP sessions**
```bash
/routing bgp session reset [find where remote-address=172.21.85.2]
```

## 7. Verification Process
1. Confirm BGP session state:
   ```bash
   /routing bgp peer print where remote-address=172.21.85.2
    0 name="Peer_A" state=established established=23h55m
   ```
2. Validate route propagation:
   ```bash
   /ip route print where bgp 
   #  DST-ADDRESS        GATEWAY         DISTANCE
     0 192.168.100.0/24   172.21.85.2     200
   ```
3. Monitor traffic flow:
   ```bash
   /tool sniffer quick port=179
   ```

## 8. Prevention Measures
1. Implement firewall rule documentation standard
2. Create BGP-specific filter chain:
   ```bash
   /ip firewall filter add chain=bgp_in action=accept protocol=tcp dst-port=179
   ```
3. Enable BGP logging:
   ```bash
   /routing bgp instance set default log=yes
   ```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp peer monitor [name]` | Real-time BGP peer monitoring |
| `/ip firewall connection print protocol=tcp` | Show active TCP sessions |
| `/tool sniffer quick src-address=172.21.85.1` | Packet capture diagnostics |

## 10. Common Pitfalls to Avoid
1. **Rule Ordering:** Always place specific allow rules before general deny rules
2. **NAT Conflicts:** Ensure BGP traffic isn't subject to masquerade rules
3. **VRF Awareness:** Verify BGP instances are bound to correct routing tables
4. **Version Mismatch:** Confirm all peers use compatible BGP versions (RFC 4271)
5. **Timer Conflicts:** Keep BGP keepalive/hold timers consistent (default 60/180s)
```
