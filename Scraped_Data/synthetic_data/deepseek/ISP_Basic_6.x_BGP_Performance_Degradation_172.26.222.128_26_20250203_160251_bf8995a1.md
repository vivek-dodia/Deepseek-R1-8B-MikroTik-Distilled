---
generated_at: 2025-02-03T16:03:35.200220
topic: BGP
category: Routing
version: 6.x
scale: ISP
level: Basic
subnet: 192.168.133.160/27
scenario: Performance Degradation
environment: Data Center
affected_users: 613
duration: 15 hours
---

# Analysis Process
Okay, let me try to work through this MikroTik BGP troubleshooting scenario. The user wants a detailed case for an ISP data center with performance issues affecting over 600 users for 15 hours. I need to cover all the sections listed, so I'll start by breaking down each part.

First, the initial problem report. Symptoms are high latency and packet loss. Since it's BGP-related in a data center, maybe there's a routing issue causing traffic to take a suboptimal path. The duration is 15 hours, which suggests it's a persistent problem, not a transient one.

For the environment, it's an ISP data center using RouterOS 6.x. The subnet is 192.168.133.160/27. I'll need to create a Mermaid diagram showing the core routers connected to edge routers and peers. Maybe two core routers in a cluster, connected to multiple edge routers and external BGP peers.

Initial assessment steps: Check BGP session status, routing table, CPU/memory usage, and traffic flow. Use commands like `/routing bgp session print`, `/ip route print`, and monitor resources.

Debugging process: Look into BGP session details, route advertisements, maybe there's a flap or a misconfiguration in route filters. Check if the correct routes are being advertised and received. Use `export` commands to see BGP routes. Logs might show session resets. Could there be an issue with the BGP timers or MTU? Maybe a route reflector problem if they're using that.

Key findings: Perhaps a misconfigured route filter causing incorrect routes to be advertised, leading to suboptimal paths. Or a session flapping due to keepalive timeouts. Maybe a prefix limit being hit, causing routes to be withdrawn.

Solution: Adjust the route filters to correct the advertised routes. Fix BGP timers if necessary. Implement route dampening if flapping is an issue. Update prefix limits.

Verification: Check latency and packet loss again. Ensure BGP sessions are stable and routes are correct. Use `ping` and `traceroute` to test paths.

Prevention: Regular audits of BGP configs, monitoring with tools like Grafana, implement route validation (RPKI), use BFD for faster detection.

Commands: Include examples like `/routing bgp session print`, `/routing bgp advertisement print`, log checks with `/log print`.

Pitfalls: Forgetting to soft reset sessions after config changes, misapplying route filters, not monitoring all BGP sessions.

I need to make sure each section is covered. Maybe the root cause is a route filter that's too restrictive, causing the ISP to prefer a longer path through a congested link. When the filter was adjusted, the correct routes were advertised, traffic shifted, and performance improved.

Also, check if the subnet 192.168.133.160/27 is correctly advertised in BGP. Maybe it's being summarized or not advertised at all, leading to blackholes.

In the logs, maybe there are entries about BGP session resets or routes being withdrawn. The CPU might spike during route processing if there's a lot of churn.

Before and after configurations: Show the route filter rules before (maybe blocking certain prefixes) and after (allowing correct ones). Or adjust the BGP timers from default to more suitable values.

I think that's a rough outline. Now, structure each section with these thoughts, include CLI commands, logs, and Mermaid diagram.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario: ISP Data Center Performance Degradation

## 1. Initial Problem Report and Symptoms
**Report**: Multiple customers reported intermittent connectivity and slow internet speeds.  
**Symptoms**:
- Increased latency (150ms+ from normal 30ms)
- Packet loss (8-12% on core links)
- BGP route flapping observed in monitoring
- 613 business customers impacted across /27 subnet
- Issue persisted through router reboot 15 hours ago

## 2. Environment Description & Topology

```mermaid
graph TD
    A[Core Router 1 (CR1)] <--> B[Core Router 2 (CR2)]
    A --> C[Edge Router 1 (ER1)]
    B --> D[Edge Router 2 (ER2)]
    C -->|eBGP| E[ISP Peer A]
    C -->|eBGP| F[ISP Peer B]
    D -->|eBGP| G[ISP Peer C]
    CR1 & CR2 --> H[Data Center Switching]
    H --> I[Customer Subnet 192.168.133.160/27]
```

## 3. Initial Assessment Steps
1. Verify BGP session status:
```routeros
/routing bgp session print
```
2. Check route table for customer subnet:
```routeros
/ip route print where dst-address=192.168.133.160/27
```
3. Monitor CPU/Memory usage:
```routeros
/system resource print
```
4. Check interface statistics:
```routeros
/interface ethernet monitor [find name~"uplink"]
```

## 4. Detailed Debugging Process
**Step 1: Verify BGP Sessions**
```routeros
/routing bgp session print detail where remote.address~"Peer"
```
Output:
```
  remote.address: 203.0.113.1
  remote.as: 64500
  state: established
  updates.sent: 15230
  updates.received: 23450
  withdrawn.sent: 420 ← High withdrawal count
```

**Step 2: Check Route Advertisements**
```routeros
/routing bgp advertisements print detail
```
Output:
```
prefix: 192.168.133.160/27
origin: igp
as-path: 64515 64500 ← Unexpected AS path prepending
```

**Step 3: Analyze Routing Table**
```routeros
/ip route print where bgp
```
Output:
```
# DST-ADDRESS        GATEWAY         DISTANCE
0 192.168.133.160/27 203.0.113.1     200
1 192.168.133.160/27 198.51.100.5    200 ← Duplicate routes
```

**Step 4: Check Logs**
```routeros
/log print where message~"BGP"
```
Output:
```
15:22:41 bgp,error Peer 203.0.113.1: Route limit exceeded (max 1000)
15:22:43 bgp,info Session 203.0.113.1 state changed: active → open
```

## 5. Key Findings & Root Cause
**Root Cause**: 
- Misconfigured route filter causing route oscillations
- Prefix limit exceeded on critical peer (203.0.113.1)
- ECMP routing conflict for customer subnet

**Technical Analysis**:
1. Route map incorrectly prepended AS path 64500
2. Default 1000 route limit hit due to full-table peer
3. Duplicate BGP routes created routing loops in ECMP

## 6. Solution Implementation
**Step 1: Adjust Route Filter**
```routeros
/routing filter rule [find chain=peer_A_out] set set-as-path="" 
```

**Step 2: Increase Prefix Limit**
```routeros
/routing bgp peer set [find address=203.0.113.1] prefix-limit=5000
```

**Step 3: Fix ECMP Configuration**
```routeros
/ip route set [find dst-address=192.168.133.160/27] ecmp=no
```

## 7. Verification Process
1. Monitor latency reduction:
```routeros
/ping 192.168.133.161 count=100
```
2. Check route stability:
```routeros
/routing bgp advertisements print interval=30s count=5
```
3. Verify BGP session health:
```routeros
/routing bgp session print detail where remote.address~"203.0.113.1"
```

## 8. Prevention Measures
1. Implement BGP route flap damping
2. Set up automated prefix limit alerts
3. Regular BGP policy audits
4. Enable RPKI validation
```routeros
/routing bgp peer set [find] rpki=strict
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp instance print` | Show BGP instances |
| `/routing bgp peer print stats` | Peer statistics |
| `/routing filter print` | View route policies |
| `/tool sniffer quick` | Packet capture |

## 10. Common Pitfalls to Avoid
1. Not using soft session reset after config changes:
```routeros
/routing bgp session reset [find]
```
2. Forgetting to maintain consistent route policies across peers
3. Overlooking MTU mismatches in BGP sessions
4. Not monitoring BGP memory usage in large tables
5. Ignoring route refresh capability negotiation
```markdown
**Before Fix**:
```routeros
/routing filter add chain=peer_A_out set-as-path=64500
```

**After Fix**:
```routeros
/routing filter add chain=peer_A_out
```
```
