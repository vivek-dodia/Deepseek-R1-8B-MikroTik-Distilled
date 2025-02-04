---
generated_at: 2025-02-03T16:18:39.189048
topic: BGP
category: Routing
version: 7.x
scale: ISP
level: Advanced
subnet: 192.168.11.0/24
scenario: BGP Flapping
environment: Retail Network
affected_users: 309
duration: 9 hours
---

# Analysis Process
Alright, let's tackle this BGP flapping scenario for MikroTik RouterOS 7.x in an ISP retail network. The user wants a detailed troubleshooting guide, so I need to cover all the specified sections thoroughly. 

First, the Initial Problem Report. Symptoms include intermittent outages and high latency. Maybe start with users reporting connectivity issues, and checking BGP session status. Then look at the environment: it's an ISP with a retail network using 192.168.11.0/24. The network topology probably has edge routers connected to upstream providers and peers. I should sketch a Mermaid diagram showing the core, edge routers, customer routers, and the BGP connections. 

Next, Initial Assessment Steps. Check BGP sessions with /routing bgp session print. Look for established vs. active. Then check logs for BGP events. Maybe use /log print where message~"BGP". Also, check CPU and memory usage to rule out resource issues. 

For Detailed Debugging, start by enabling BGP debugging: /routing bgp log set debug=yes. Then monitor logs in real-time. Check BGP routes and look for flapping prefixes. Use /routing bgp advertisements print and /routing route where bgp. Also, check for route filters or AS path issues. Maybe there's a misconfiguration in the import/export rules. 

Key Findings might be a route oscillation caused by a duplicate router ID or a misconfigured filter. For example, a customer router advertising the same subnet as another, causing routes to flip. Root cause could be a duplicate subnet being advertised due to a misconfiguration. 

Solution Implementation would involve correcting the route filters to prevent the conflicting subnet from being advertised. Update the prefix lists and maybe adjust the BGP timers. Then reset the BGP sessions. 

Verification would involve checking sessions are stable, monitoring logs, and testing connectivity. Prevention Measures include implementing stricter route filters, using route validation, and monitoring tools. 

Common pitfalls might be not checking all BGP neighbors or missing route filters. Also, not testing config changes in a lab first. 

I need to make sure to include CLI commands with code blocks, example log outputs, and before/after config snippets. Also, reference related commands and pitfalls. Let me structure each section step by step, ensuring all user requirements are met. Watch out for technical accuracy, especially with RouterOS 7.x commands. Double-check BGP commands and log examples to match real scenarios. Avoid assumptions not backed by the given data, like specific hardware models. Focus on the subnet provided and the ISP context. Alright, let's put this all together in markdown with proper formatting.

# Troubleshooting Guide
```markdown
# BGP Flapping Troubleshooting Scenario (MikroTik RouterOS 7.x)

## 1. Initial Problem Report and Symptoms
**Report**: Retail customers (309 users) experience intermittent outages in 192.168.11.0/24 network.  
**Symptoms**:
- BGP session flapping every 2-7 minutes
- Increased latency (avg. 287ms → 920ms)
- Routing table instability (`/ip route print` shows frequent changes)
- 30% packet loss to upstream transit provider
- Syslog alerts: `BGP session state changed` events

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  A[Core Router (AS65530)] --> B[Edge Router 1 (AS64500)]
  A --> C[Edge Router 2 (AS64501)]
  B --> D[Upstream Provider A (AS12345)]
  B --> E[Peer Network (AS67890)]
  C --> F[Upstream Provider B (AS54321)]
  D --> G[Retail Customers: 192.168.11.0/24]
```

## 3. Initial Assessment Steps
1. Check BGP session status:
```bash
/routing bgp session print
# Output:
# 0 AS12345  established 192.168.11.1    64500  192.168.11.2
# 1 AS54321  active      203.0.113.5     64500  203.0.113.6
```

2. Review BGP-related logs:
```bash
/log print where message~"BGP"
# Output:
# 09:32:11 bgp,error Session to 192.168.11.1 closed: hold timer expired
# 09:39:47 bgp,info Session to 192.168.11.1 established
```

3. Verify resource utilization:
```bash
/system resource print
# Output:
#           cpu: 89% 
#           memory: 78%
```

## 4. Detailed Debugging Process
**Step 1: Enable BGP Debugging**
```bash
/routing bgp log set debug=yes
```

**Step 2: Monitor BGP Updates**
```bash
/log follow
# Sample Output:
# 10:15:22 bgp,debug,packet Sending UPDATE with WITHDRAW: 192.168.11.0/24
# 10:15:24 bgp,debug,packet Received UPDATE from 192.168.11.1: 192.168.11.0/24
```

**Step 3: Check Route Advertisements**
```bash
/routing bgp advertisements print detail
# Output shows conflicting advertisements for 192.168.11.0/24 from two different neighbors

/routing route where bgp
# Shows route oscillation between two next-hop addresses
```

**Step 4: Verify BGP Filters**
```bash
/routing filter print
# Before:
# 0 chain=from_peer accept where prefix=192.168.11.0/24
# 1 chain=to_peer accept where prefix-list=allowed_routes
```

## 5. Key Findings & Root Cause
**Findings**:
- Duplicate 192.168.11.0/24 advertisements from two edge routers
- Missing `bgp-med` configuration causing route oscillation
- Incorrect route filter allowing customer subnet to be re-advertised to peers

**Root Cause**: 
Misconfigured route redistribution on Edge Router 1 caused 192.168.11.0/24 to be advertised both via BGP and OSPF, creating a routing loop between BGP peers.

## 6. Solution Implementation
**Before**:
```bash
/routing filter rule add chain=to_peer action=accept prefix=192.168.11.0/24
```

**After**:
```bash
/routing filter rule set [find where prefix=192.168.11.0/24] action=reject
/routing bgp network add network=192.168.11.0/24
/routing bgp set default med=100
```

**Session Reset**:
```bash
/routing bgp session disable [find where remote.address=192.168.11.1]
/routing bgp session enable [find where remote.address=192.168.11.1]
```

## 7. Verification Process
1. Confirm stable BGP sessions:
```bash
/routing bgp session print where state="established"
```

2. Monitor route stability:
```bash
/routing route monitor [find where dst-address=192.168.11.0/24]
```

3. End-to-end test:
```bash
/ping 192.168.11.1 count=100 interval=1s
# Loss reduced to 0.2%
```

## 8. Prevention Measures
1. Implement strict route filters:
```bash
/routing filter add chain=bgp_out rule="if (dst == 192.168.11.0/24) { reject }"
```

2. Enable BGP route refresh:
```bash
/routing bgp template set default route-refresh=yes
```

3. Configure BGP dampening:
```bash
/routing bgp set default dampening=yes dampening-max-reach=1h
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp neighbor print` | List BGP peers |
| `/routing route export` | Show full routing table |
| `/tool sniffer quick` | Capture BGP packets (TCP 179) |

## 10. Common Pitfalls to Avoid
- **Missing `as-override`** in customer-facing BGP sessions
- **Route reflector** misconfiguration in large-scale deployments
- **Incorrect MED values** causing suboptimal path selection
- **Unfiltered customer routes** leaking to upstream providers
- **Ignoring BGP timers** mismatch warnings in logs
```
