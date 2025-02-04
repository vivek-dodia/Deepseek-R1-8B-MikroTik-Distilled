---
generated_at: 2025-02-03T16:24:22.941154
topic: RIP
category: Routing
version: 6.x
scale: SMB
level: Basic
subnet: 10.132.25.0/28
scenario: High CPU Usage
environment: Branch Office
affected_users: 125
duration: 8 hours
---

# Analysis Process
Okay, let's tackle this MikroTik RIP troubleshooting scenario. The user wants a detailed scenario for high CPU usage in a branch office with 125 users, subnet 10.132.25.0/28, running RouterOS 6.x. 

First, I need to outline the initial problem report. Symptoms include high CPU, network slowness, and RIP routes missing. Users affected for 8 hours. Then, the environment: branch office, SMB network. The network topology should be in Mermaid. Let me sketch that out. Probably two routers, maybe a main and a branch. The subnet is a /28, so 16 addresses. 

Initial assessment steps: check CPU usage with `/system resource print`, check processes with `/system process print`. Look at RIP status with `/routing rip neighbor print` and routes. Logs might show RIP flapping. 

Debugging process: Need to use CLI commands. Check RIP neighbors, see if they're active. Maybe authentication issues? Look at the routing table with `/ip route print`. Logs via `/log print where topics=rip`. Maybe enable debugging with `/routing rip set distribute=yes` and check traffic with a packet sniffer. 

Key findings: RIP updates too frequent, misconfigured timers causing high updates. Maybe the timers are set to very low values like 5 seconds instead of 30. Root cause is the timers leading to excessive CPU usage from RIP processing.

Solution: Adjust RIP timers to default. Update configuration. Verify with `:put [/routing rip interface get [find where interface=ether1] update]` to check the interval. 

Verification: Monitor CPU after changes. Check RIP neighbors and routes. Confirm network performance improved.

Prevention: Regular monitoring, correct timer settings, authentication, network segmentation.

Related commands: Include all the CLI commands used. Common pitfalls: incorrect timers, no authentication, not filtering routes.

I need to make sure the Mermaid diagram is correct. Maybe two routers connected via ether1 and ether2, with the subnet on the LAN side. Also, ensure that the before and after configurations show the timer changes. Log examples should reflect RIP updates happening too often.

Wait, in RouterOS 6.x, the RIP configuration commands might be different. For example, `/routing rip interface set` to adjust timers. Also, checking the neighbors and routes. Need to make sure the CLI commands are accurate for version 6.x, as some commands changed in later versions.

Also, the subnet is 10.132.25.0/28, which is a small subnet. Maybe the branch office is connected to a main office via RIP. High CPU from RIP processing could be due to frequent updates. If the timers are set too low, like update every 5 seconds, that would cause more CPU load. So in the configuration, before the fix, the update interval is 5s, after changing to 30s.

Including log outputs: when RIP updates are sent every 5 seconds, the logs would show that. After fixing, logs show every 30s. 

Make sure to mention that in RouterOS 6.x, the default RIP timers are update=30s, timeout=180s, so if they were set lower, that's the issue. Also, authentication might not be the issue here, but it's a possible pitfall. 

Check if there are any routing loops causing excessive updates, but in this case, it's the timers. Also, making sure that the network isn't too large for RIP, but since it's SMB, it's probably okay. 

In the prevention measures, maybe suggest using OSPF instead if the network grows, but for SMB, RIP is acceptable. 

Double-check all commands for version 6.x. For example, `/routing rip setup` might not be a command. Instead, it's configured under `/routing rip`. 

Okay, putting it all together now. Structure each section as per the user's request, using markdown. CLI commands in code blocks, comments where necessary. Log examples with timestamps. Mermaid diagram for topology. Before/after configs showing the timer change. Common pitfalls like ignoring timer settings or not using authentication.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP High CPU Usage

## 1. Initial Problem Report and Symptoms
**Report**: Branch office users report intermittent network outages and slow application performance.  
**Symptoms**:
- Sustained CPU usage >90% on edge router
- RIP routes intermittently missing from routing table
- Increased latency (150-300ms) across VLANs
- 125 users impacted for 8 hours
- Frequent route flaps in routing table

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    BR1[RBR1 (10.132.25.1/28)] -->|RIP via ether1| HQ_Router
    BR1 --> SW1[Switch]
    SW1 --> VLAN10(10.132.25.0/28 - User VLAN)
    SW1 --> VLAN20(10.132.30.0/24 - VoIP)
```

## 3. Initial Assessment Steps
1. Confirm CPU load:
```bash
/system resource print
```
```log
cpu-load: 94%
free-memory: 45.3MiB
```

2. Identify top processes:
```bash
/system process print where cpu-time>00:00:10
```
```log
  # NAME               CPU-TIME
  8 routing-RIP        00:12:45
```

3. Check RIP status:
```bash
/routing rip neighbor print
```
```log
 0 interface=ether1 address=10.132.25.2 uptime=8h2m status=established 
```

## 4. Detailed Debugging Process
**Step 1**: Verify RIP routes
```bash
/ip route print where protocol=rip
```
```log
Flags: X - disabled, A - active, D - dynamic 
 0 AD  10.132.30.0/24 rip-ether1 10.132.25.2       ether1 8h12m
```

**Step 2**: Check RIP interface settings
```bash
/routing rip interface print
```
```log
 0 interface=ether1 update-interval=5s authentication=none
```

**Step 3**: Monitor RIP traffic
```bash
/sniffer quick protocol=udp port=520
```
```log
TIME    SRC-ADDRESS    DST-ADDRESS
09:32:25 10.132.25.2   224.0.0.9:520 (RIPv2)
09:32:30 10.132.25.2   224.0.0.9:520
```

**Step 4**: Analyze system logs
```bash
/log print where topics=rip
```
```log
09:30:15 router,rip Route 10.132.30.0/24 updated via 10.132.25.2
09:30:20 router,rip Route 10.132.30.0/24 updated via 10.132.25.2
```

## 5. Key Findings & Root Cause
**Findings**:
- RIP update interval configured to 5s (default=30s)
- 1600+ RIP updates received in 8 hours
- No route filtering implemented
- CPU spikes correlate with routing table recalculations

**Root Cause**:  
Aggressive RIP timers (5s updates) caused excessive route recalculations, overwhelming the router's CPU in a /28 network with frequent ARP updates.

## 6. Solution Implementation
**Before**:
```bash
/routing rip interface print
 0 interface=ether1 update=5s timeout=15s
```

**After**:
```bash
/routing rip interface set 0 update-interval=30s timeout=180s
/routing rip set redistribute-static=no
/ip firewall filter add chain=output protocol=udp port=520 action=accept
```

## 7. Verification Process
1. Monitor CPU post-fix:
```bash
/system resource print
```
```log
cpu-load: 22%
```

2. Confirm stable routes:
```bash
/ip route print where protocol=rip
```
```log
 0 AD  10.132.30.0/24 rip-ether1 10.132.25.2       ether1 1h30m
```

## 8. Prevention Measures
1. Implement RIP authentication:
```bash
/routing rip interface set 0 authentication=md5 authentication-key=securekey
```

2. Add route filters:
```bash
/routing rip rule add interface=ether1 in-prefix=10.132.0.0/16
```

3. Set sane timers:
```bash
/routing rip interface set [find] update-interval=30s timeout=180s
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing rip neighbor print` | Show RIP peers |
| `/ip route print where protocol=rip` | List RIP-learned routes |
| `/system profile` | Monitor CPU per process |
| `/tool sniffer quick protocol=udp port=520` | Capture RIP traffic |

## 10. Common Pitfalls to Avoid
1. **Aggressive Timers**: Avoid <30s update intervals in small networks
2. **Missing Filters**: Always restrict RIP route redistribution
3. **No Authentication**: Open RIP interfaces expose routing to spoofing
4. **Mixed Versions**: Ensure all devices use RIPv2 (not v1)
5. **Silent Interfaces**: Configure `passive-interface` where needed
```bash
/routing rip interface set [find where interface=LAN_port] passive=yes
```
