---
generated_at: 2025-02-03T16:47:51.258879
topic: RIP
category: Routing
version: 7.x
scale: ISP
level: Advanced
subnet: 10.137.6.0/25
scenario: VPN Tunnel Issues
environment: Edge Location
affected_users: 542
duration: 23 hours
---

# Analysis Process
Alright, I need to create a detailed MikroTik RouterOS troubleshooting scenario for RIP on version 7.x in an ISP environment with a specific subnet and VPN tunnel issues affecting 542 users for 23 hours. Let me break down each section step by step.

Starting with the Initial Problem Report and Symptoms. The users are complaining about internet downtime, so I should mention that. The edge location has a VPN tunnel, so symptoms should include high latency, packet loss, and RIP routes not propagating. Maybe the BGP over the VPN is down because RIP isn't sharing routes correctly.

For the Environment Description, the network topology needs to be in Mermaid. The ISP edge router connects to a core router via RIP, and there's a VPN tunnel to a remote site. The subnet 10.137.6.0/25 is involved. I'll draw that out with Mermaid syntax, making sure to include the VPN and RIP connections.

Initial Assessment Steps: Check interface statuses, RIP neighbors, routing tables, VPN tunnel status, and logs. Basic commands like /interface print, /routing rip neighbor print, /ip route print, and checking the VPN with /interface gre print. Also, log checks with /log print.

Detailed Debugging Process: Need to verify RIP configuration, check for authentication mismatches, debug RIP updates with packet sniffer, test VPN tunnel connectivity (ping, traceroute), check MTU issues, and maybe BGP dependencies. Commands like /routing rip instance print, /routing rip interface print, /tool sniffer, ping, and /ping with do-not-fragment. Also, looking at BGP sessions if they rely on RIP routes.

Key Findings and Root Cause: Suppose RIP authentication was misconfigured on one side, causing neighbors to drop updates. Also, MTU fragmentation over GRE VPN because of incorrect MTU settings. These two issues together caused routes not to propagate and VPN tunnel packets to drop.

Solution Implementation: Fix RIP authentication, adjust GRE MTU, and maybe add static routes as a backup. Commands to set authentication on RIP interfaces and adjust GRE MTU. Also, static route addition.

Verification: Check RIP neighbors again, verify routes in table, test VPN connectivity, and monitor traffic. Commands like /routing rip neighbor print, /ip route print, and continuous pings.

Prevention Measures: Regular config audits, monitoring tools for RIP and VPN, MTU checks on tunnels, and documentation. Maybe using Netwatch or SNMP.

Related Commands: List all the CLI commands used in each section for quick reference.

Common Pitfalls: Forgetting RIP authentication, ignoring MTU on VPNs, not monitoring route propagation, mixing routing protocols without proper redistribution.

I need to make sure the CLI commands are accurate for RouterOS 7.x. For example, RIP configuration in 7.x might have different paths. Also, check that GRE MTU settings are correctly applied. Maybe the authentication was using MD5 but one router was using plaintext. Log examples should show RIP neighbors not established and VPN packets being dropped.

Before and after configurations: Show the RIP interface settings before without authentication and after with MD5. Similarly, GRE interface MTU before 1476 and after 1400.

I should also include example log entries, like "RIP: authentication failed" or "GRE packet too big". The packet sniffer output would show RIP packets being sent but not received on the other side due to auth issues.

Need to structure each section clearly, use markdown formatting, code blocks for commands, and comments explaining complex steps. Avoid using markdown in the thinking process, but in the final answer, apply all the formatting as per the user's request.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP VPN Tunnel Issues

## 1. Initial Problem Report and Symptoms
**Report**: 542 users at ISP edge location (10.137.6.0/25) report internet downtime for 23 hours.  
**Symptoms**:
- Intermittent VPN tunnel drops between edge router and core network
- RIP routes not propagating to remote sites
- High latency/packet loss on GRE/IPsec tunnel
- BGP over VPN (used for backup) fails to establish

---

## 2. Environment Description & Network Topology
```mermaid
graph TD
  A[ISP Edge Router (10.137.6.1/25)] -->|RIP| B[Core Router (10.200.0.1)]
  A -->|GRE/IPsec VPN| C[Remote Site (192.168.100.1)]
  A --> D[Customer Pool: 10.137.6.2-126/25]
  style A stroke:#f66,stroke-width:2px
```

---

## 3. Initial Assessment Steps
1. **Interface Status Check**:
```routeros
/interface print
# Check for "running" status on GRE/IPsec interfaces
```

2. **RIP Neighbor Verification**:
```routeros
/routing rip neighbor print
# Expecting 10.200.0.1 in 'established' state
```

3. **Routing Table Audit**:
```routeros
/ip route print where protocol=rip
# Missing 172.16.0.0/24 and 192.168.100.0/24 routes
```

4. **VPN Tunnel Status**:
```routeros
/interface gre print
/ip ipsec active-peers print
```

5. **Log Analysis**:
```routeros
/log print where message~"RIP|IPsec"
# Sample log output:
# 00:12:35 router,debug RIP: authentication failed from 10.200.0.1
# 00:12:40 ipsec,error no proposal found for 192.168.100.1
```

---

## 4. Detailed Debugging Process
### RIP Configuration Audit
```routeros
/routing rip instance print
/routing rip interface print
# Found mismatch in authentication settings:
# Instance uses MD5, but interface configured with plaintext
```

### VPN Tunnel Debugging
```routeros
/ping 192.168.100.1 src-address=10.137.6.1
# 50% packet loss

/tool traceroute 192.168.100.1 src-address=10.137.6.1
# Hops freeze at 203.0.113.5 (ISP transit)

/interface gre set [find name="vpn-tunnel"] mtu=1400
# Reduced from 1476 to bypass MTU blackhole
```

### Packet Capture Analysis
```routeros
/tool sniffer quick protocol=udp port=520
# RIP updates sent but not acknowledged
```

### BGP Dependency Check
```routeros
/routing bgp session print
# BGP sessions down due to missing RIP routes
```

---

## 5. Key Findings & Root Cause
**Root Causes**:
1. **RIP Authentication Mismatch**: Core router used MD5 auth while edge router had plaintext
2. **MTU Fragmentation**: GRE tunnel MTU (1476) exceeded ISP transit path MTU (1400)
3. **BGP-RIP Dependency**: BGP relied on RIP-learned routes that never propagated

**Impact**:  
Dual failure caused complete routing breakdown - VPN tunnel instability + RIP route starvation.

---

## 6. Solution Implementation
1. **Fix RIP Authentication**:
```routeros
/routing rip interface set [find where interface=ether1] authentication=md5 authentication-key=ISP_Key123
```

2. **Adjust VPN MTU**:
```routeros
/interface gre set [find name="vpn-tunnel"] mtu=1400
/ip ipsec policy set [find] mtu=1400
```

3. **Add Static Backup Route**:
```routeros
/ip route add dst-address=0.0.0.0/0 gateway=203.0.113.5 distance=5
```

---

## 7. Verification Process
1. Confirm RIP Neighbors:
```routeros
/routing rip neighbor print
# STATE: established
```

2. Validate Route Propagation:
```routeros
/ip route print where protocol=rip
# 172.16.0.0/24 rip 10.200.0.1
```

3. Test VPN Connectivity:
```routeros
/ping 192.168.100.1 count=100 interval=10ms
# 0% loss observed
```

---

## 8. Prevention Measures
1. Implement Configuration Audit Tool:
```routeros
/system script add name=config-check source="/routing rip interface print; /ip ipsec policy print"
```

2. Enable Monitoring:
```routeros
/tool netwatch add host=10.200.0.1 timeout=5s up-script="/log info RIP_UP" down-script="/log warn RIP_DOWN"
```

3. MTU Discovery Automation:
```routeros
:local newMTU [/tool ping 192.168.100.1 count=5 size=1500 do-not-fragment=yes]
/interface gre set [find] mtu=($newMTU - 28)
```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing rip export` | Show RIP redistribution rules |
| `/ip ipsec profile print` | Verify Phase 1 parameters |
| `/tool sniffer quick protocol=udp port=520` | Capture RIP updates |
| `/ping 10.200.0.1 do-not-fragment=yes size=1476` | Test path MTU |

---

## 10. Common Pitfalls to Avoid
1. **Mixed Authentication Types**: Never combine plaintext and MD5 on same RIP instance
2. **MTU Assumptions**: Always validate with `do-not-fragment` pings
3. **Silent RIP Failures**: Enable `debug` logging during troubleshooting:
```routeros
/routing rip set [find] debug=yes
```
4. **Protocol Redistribution**: Avoid mutual RIP-BGP redistribution without filters
```markdown
```
