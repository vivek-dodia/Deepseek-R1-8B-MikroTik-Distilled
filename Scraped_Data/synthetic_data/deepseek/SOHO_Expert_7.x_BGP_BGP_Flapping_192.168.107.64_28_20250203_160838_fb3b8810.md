---
generated_at: 2025-02-03T16:09:23.963897
topic: BGP
category: Routing
version: 7.x
scale: SOHO
level: Expert
subnet: 10.34.134.32/27
scenario: BGP Flapping
environment: Cloud Infrastructure
affected_users: 774
duration: 4 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP flapping in a SOHO environment using RouterOS 7.x. Let's break down each section step by step.

First, the Initial Problem Report and Symptoms. The users are experiencing intermittent outages, and BGP is flapping. I should mention the duration (4 hours), affected users (774), and symptoms like packet loss, route instability, and possible high CPU or memory usage.

Next, Environment Description and Network Topology. The subnet is 10.34.134.32/27, cloud infrastructure. Maybe a simple setup with a MikroTik router connected to two cloud providers (AWS and GCP) via eBGP. Mermaid diagram with the router, two BGP peers, and the local network.

Initial Assessment Steps: Check BGP sessions, routing table, logs, CPU/memory. Use commands like /routing bgp session print, /ip route print, /log print, and resource monitoring commands.

Detailed Debugging Process: Start with checking BGP session status. If sessions are flapping, look into logs for reasons (like hold timeouts). Then check for route advertisements, maybe the prefix is being withdrawn. Use commands like /routing bgp advertisements print and /routing bgp updates print. Look into filters and AS paths. Check for configuration errors like incorrect AS numbers or timers. Maybe MTU issues? Use ping with do-not-fragment to test.

Key Findings: Perhaps the hold timer was misconfigured, or there's an MTU problem causing fragmented packets. Maybe a route filter is too restrictive, causing routes to flap.

Solution Implementation: Adjust BGP timers, fix MTU settings, correct route filters. Update configurations and maybe adjust TCP MSS.

Verification: Check BGP sessions are stable, monitor logs, test connectivity. Commands like /routing bgp session print where established=yes continuously.

Prevention Measures: Regular config audits, monitoring with tools like The Dude, proper MTU settings, and using BFD.

Related Commands Reference: List all commands used in each section with brief explanations.

Common Pitfalls: Forgetting to set redistribute rules correctly, mismatched hold times, ignoring MTU issues, and not using logging.

I need to make sure all sections are covered, CLI commands are in code blocks, and examples of log outputs are included. Also, before and after configs where relevant. Maybe show the BGP peer configuration before and after adjusting timers and MTU.

Wait, in a SOHO environment, the network isn't too complex. The cloud setup might have specific requirements. Maybe the MikroTik is in a cloud instance with virtual interfaces. The flapping could be due to incorrect BGP configurations not suitable for the cloud environment, like not accounting for latency or using incorrect authentication.

Also, considering the subnet /27, which is a small network. Maybe the MikroTik is advertising this subnet via BGP to the cloud providers. If the advertisement is unstable, routes would flap. Check if the subnet is correctly configured and advertised.

Another angle: maybe the cloud provider has some security groups or firewall rules blocking BGP ports, causing sessions to drop. But the user mentioned it's a BGP flapping issue, so more likely configuration on the MikroTik side.

In the logs, looking for messages like BGP session state change. For example, a log entry showing "session closed" due to hold timer expiry. Then, checking the configured hold time versus what the peer expects. If hold-time is set too low and the cloud provider expects a higher value, that could cause flapping.

Also, in cloud environments, sometimes the underlying network has an MTU lower than 1500, like 1460 for some providers. If the MikroTik is sending packets with DF set and the MTU is too high, the packets get dropped, leading to TCP retransmits (BGP uses TCP). This could cause session resets. So adjusting the MTU or enabling MSS clamping might help.

Putting it all together: The root cause is a combination of hold timer mismatch and MTU issues. The solution is adjusting BGP timers and setting the correct MTU/MSS.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS BGP Flapping Troubleshooting Scenario

## 1. Initial Problem Report and Symptoms
**Report**: Intermittent outages affecting 774 users over 4 hours  
**Symptoms**:
- 30-40% packet loss to cloud resources
- Frequent BGP session resets observed
- Inconsistent routing table entries
- CPU spikes to 85% during flap events
- Alerts: `BGP neighbor x.x.x.x (Admin Reset)`

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    A[MikroTik CHR v7.11] -->|eBGP/AS65530| B[AWS TGW/AS16509]
    A -->|eBGP/AS65530| C[GCP VLAN/AS396982]
    A --> D[Local Network 10.34.134.32/27]
```

## 3. Initial Assessment Steps
1. Verify BGP session status:
```bash
/routing bgp session print 
# Output:
# 0 name="aws" remote-as=16509 state=established
# 1 name="gcp" remote-as=396982 state=idle
```

2. Check routing table stability:
```bash
/ip route print count-interval=5
# Output shows frequent route count changes between 28-32
```

3. Review system resources:
```bash
/system resource print
# CPU: 85% load-average: 4.5
# Memory: 512MB/768MB (67% used)
```

## 4. Detailed Debugging Process
**Step 1: Capture BGP session states**
```bash
/routing bgp session print detail where disabled=no
```
```
  remote.address=172.31.0.1 state=established last-started=jan/01/2023 14:00:02 
  last-error=hold-timer-expired uptime=00:04:12
```

**Step 2: Analyze BGP update logs**
```bash
/log print where message~"BGP"
```
```
00:04:23 bgp,error AWS session closed: hold timer expired
00:04:35 bgp,info GCP session reset: TCP connection failed
```

**Step 3: Verify BGP timers**
```bash
/routing bgp connection print
```
```
0 name=aws hold-time=30s keepalive-time=10s
1 name=gcp hold-time=90s keepalive-time=30s
```

**Step 4: Check MTU settings**
```bash
/interface cloud print 
```
```
0 name=ether1 mtu=1500 actual-mtu=1460 (AWS Jumbo Frames)
```

## 5. Key Findings & Root Cause
**Findings**:
1. AWS BGP hold-time (30s) mismatched with AWS required 90s
2. MTU mismatch (1500 configured vs 1460 actual in cloud)
3. Missing TCP MSS clamping

**Root Cause**: Combination of:
- Aggressive BGP timers causing premature session drops
- MTU fragmentation triggering TCP retransmissions
- No BFD for fast failure detection

## 6. Solution Implementation
**Before**:
```bash
/routing bgp connection
set [find name=aws] hold-time=30s keepalive-time=10s
```

**After**:
```bash
/interface ethernet set ether1 mtu=1460
/routing bgp connection
set [find name=aws] hold-time=90s keepalive-time=30s
set [find name=gcp] tcp-mss=1360
/routing bgp peer
set [find name=aws] bfd=yes
```

## 7. Verification Process
1. Monitor session stability:
```bash
:global bgpCheck do={/routing bgp session print where established=yes} 
:put ([len $bgpCheck]." stable sessions")
# Output: "2 stable sessions"
```

2. Test MTU:
```bash
/ping 172.31.0.1 size=1472 do-not-fragment=yes
# Success rate: 100%
```

## 8. Prevention Measures
1. Implement BFD for all BGP peers
2. Set cloud-appropriate MTU (1460) with MSS clamping
3. Use consistent timer policy:
```bash
/routing bgp template
add name=cloud-template hold-time=90s keepalive-time=30s tcp-mss=1360
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgx history print` | Show BGP route change history |
| `/tool sniffer quick` | Capture BGP packets (port 179) |
| `/interface detect-internet` | Verify cloud connectivity |

## 10. Common Pitfalls to Avoid
❌ **Mismatched AS Numbers**:
```bash
# Wrong:
/routing bgp peer set remote-as=16509
# Right for AWS:
/routing bgp peer set remote-as=16509
```

❌ **Ignoring TCP MSS**:
```bash
# Always set for cloud:
/routing bgp connection set tcp-mss=1360
```

❌ **Overlooking BGP Filters**:
```bash
# Avoid over-filtering:
/routing filter add chain=outbound rule="if (dst in 10.34.134.32/27) accept"
```
```
