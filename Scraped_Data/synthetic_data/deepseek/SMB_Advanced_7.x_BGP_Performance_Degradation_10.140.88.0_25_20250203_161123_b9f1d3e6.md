---
generated_at: 2025-02-03T16:13:12.049307
topic: BGP
category: Routing
version: 7.x
scale: SMB
level: Advanced
subnet: 192.168.58.128/27
scenario: Performance Degradation
environment: Remote Site
affected_users: 915
duration: 15 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP on version 7.x in an SMB network with the subnet 192.168.58.128/27. The environment is a remote site experiencing performance degradation affecting 915 users over 15 hours. Let me break down each section step by step.

First, the Initial Problem Report and Symptoms. Users are complaining about slow access to cloud apps and VoIP issues. The remote site has a BGP connection to the main office. I should mention latency spikes, packet loss, and maybe route flapping. Logs might show BGP state changes.

Next, the Environment Description and Network Topology. The SMB has a remote site with a MikroTik router (RouterOS 7.x) connected via BGP to the main office. The subnet is 192.168.58.128/27. The network has about 1000 users. I need to draw this in Mermaid. Let me structure it with the remote site router connected to an ISP and the main office via BGP. Include the LAN subnet and user count.

Initial Assessment Steps: Start by checking BGP neighbor status with /routing bgp neighbor print. Look for established state. Then check routes with /routing route print where bgp. Maybe check CPU and memory usage via /system resource print. Also, look at interface statistics for errors or high traffic.

Detailed Debugging Process: Use commands like /routing bgp neighbor print, /routing route print, /log print where message~"BGP". Maybe enable debug logging temporarily with /routing bgp log set yes and check logs again. Look for route flapping or session resets. Use tools like ping and traceroute to check connectivity. Maybe test traffic with traffic-generator for packet loss.

Key Findings and Root Cause Analysis: Suppose the logs show BGP session flapping due to high CPU from a route storm. Maybe the router is receiving too many BGP routes, causing CPU spikes and packet loss. The SMB router might not handle full Internet routes, leading to resource exhaustion.

Solution Implementation Steps: Implement route filtering to accept only necessary prefixes. Adjust BGP timers to be more forgiving. Set up prefix limits. Update the BGP configuration with these changes. Before and after configs would show adding filters and prefix limits.

Verification Process: Check CPU and memory again, confirm BGP sessions are stable, verify routes are filtered, and test user traffic for improvement.

Prevention Measures: Regular monitoring, implement route filtering from the start, use prefix limits, schedule updates during off-hours, and educate staff.

Related Commands Reference: List the commands used in each step, like checking neighbors, routes, logs, etc.

Common Pitfalls to Avoid: Not filtering routes, ignoring prefix limits, not monitoring resources, using default timers, and missing log checks.

I need to make sure CLI commands are in code blocks, include comments, and maybe some example log outputs. Also, before and after configuration snippets to show the changes. Let me structure each section with markdown headers and bullet points where needed. Check for any missing parts and ensure it flows logically from problem to solution.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS BGP Troubleshooting Scenario

## 1. Initial Problem Report and Symptoms
**Report**: Remote site users report intermittent slow access to cloud applications and VoIP quality degradation.  
**Symptoms**:
- Latency spikes from 50ms to 800ms during business hours
- 15-20% packet loss to central office (192.168.10.0/24)
- BGP route flapping observed in logs
- 915 users impacted across 192.168.58.128/27 subnet

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  A[Remote Site Router (RB4011, ROSv7)] -->|BGP/ISP| B[ISP Core Router]
  A -->|iBGP| C[Main Office Router]
  A --> D[LAN Switch]
  D --> E[192.168.58.128/27]
  E --> F[915 Users]
```

## 3. Initial Assessment Steps
1. Verify BGP neighbor status:
   ```bash
   /routing bgp neighbor print
   # Output:
   # 0 name="ISP" remote-address=203.0.113.1 remote-as=65530 state="established"
   # 1 name="MainOffice" remote-address=192.168.10.1 remote-as=65500 state="active" 
   ```
   **Finding**: Main Office BGP session stuck in "active" state

2. Check routing table health:
   ```bash
   /routing route print where bgp
   # Output shows 600k+ BGP routes
   ```

3. Monitor system resources:
   ```bash
   /system resource print
   # Output: cpu-load=98% memory-usage=89%
   ```

## 4. Detailed Debugging Process
**Step 1**: Enable BGP debugging
```bash
/routing bgp log set yes
/log print where message~"BGP"
# Sample log:
# 08:15:23 bgp,error Session to 192.168.10.1 failed: Hold timer expired
# 08:15:25 bgp,info Session to 203.0.113.1 reset: Route limit exceeded
```

**Step 2**: Analyze BGP configuration
```bash
/routing bgp instance print
# Output shows default "keepalive-time=1m" and "hold-time=3m"
```

**Step 3**: Check route filtering
```bash
/routing filter print
# No route filters configured
```

**Step 4**: Verify prefix limits
```bash
/routing bgp peer print where name="ISP"
# Output shows no prefix limits configured
```

## 5. Key Findings & Root Cause
**Root Cause**:  
Unfiltered BGP feed from ISP caused:
1. Route table explosion (600k+ routes)
2. CPU/memory exhaustion triggering BGP session resets
3. Default BGP timers too aggressive for satellite link

**Evidence**:
- 98% CPU from route processing
- No prefix limits on ISP peer
- Missing route filters for internal networks

## 6. Solution Implementation
**Before Configuration** (Problematic):
```bash
/routing bgp peer
add name=ISP remote-address=203.0.113.1 remote-as=65530
```

**After Configuration** (Fixed):
```bash
/routing bgp peer
set [find name=ISP] \
    prefix-limit=5000 \
    hold-time=1h \
    in-filter=allow-internal-only \
    out-filter=deny-all

/routing filter add chain=allow-internal-only \
    rule="if (dst in 192.168.0.0/16) { accept } else { reject }"
```

## 7. Verification Process
1. Confirm BGP stability:
   ```bash
   /routing bgp neighbor print
   # Output shows "established" state for both peers
   ```
2. Check route count:
   ```bash
   /routing route print count
   # Output: 127 routes (down from 600k+)
   ```
3. Validate performance:
   ```bash
   /ping 192.168.10.1 count=100
   # 0% packet loss, avg rtt=54ms
   ```

## 8. Prevention Measures
1. Implement strict prefix limits for all BGP peers
2. Create route filters for internal networks
3. Adjust BGP timers for high-latency links
4. Set up SNMP monitoring for CPU/route counts
5. Enable BGP logging permanently

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp neighbor print` | Check BGP peer status |
| `/routing route print where bgp` | List BGP-learned routes |
| `/tool traffic-generator quick` | Test packet loss |
| `/system resource monitor` | Real-time CPU monitoring |

## 10. Common Pitfalls to Avoid
1. **Never** accept full BGP tables on SMB routers
2. Avoid default BGP timers for high-latency links
3. Always set prefix limits on external peers
4. Don't ignore memory usage when running BGP
5. Never use `add-default-route=yes` without filters
```
