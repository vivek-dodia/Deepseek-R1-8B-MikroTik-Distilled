---
generated_at: 2025-02-03T15:57:55.282075
topic: BGP
category: Routing
version: 6.x
scale: SMB
level: Expert
subnet: 172.17.124.160/28
scenario: BGP Flapping
environment: Campus Network
affected_users: 459
duration: 2 hours
---

# Analysis Process
Okay, let's tackle this BGP flapping scenario for a MikroTik RouterOS 6.x in an SMB campus network. The user wants a detailed troubleshooting guide, so I need to make sure each section is thorough but concise.

First, the initial problem report. Symptoms would include users losing connectivity, maybe complaints about internet access. Since it's BGP flapping, the BGP sessions between routers are going up and down. Logs might show route withdrawals and instability. I should mention intermittent outages and high CPU as possible symptoms.

Next, the environment. It's a campus network with a /28 subnet, 172.17.124.160/28. There are two routers connected to an ISP and two core switches. Need to draw a Mermaid diagram. Let me structure that: ISP links to R1 and R2, which connect to CoreSW1 and CoreSW2, then to users. The subnets involved are the /28 and maybe loopback addresses for BGP.

Initial assessment steps. Start with checking BGP status using /routing bgp neighbor print. Then look at logs for BGP messages. Check CPU and memory usage. Verify interface status and physical connections. Maybe look at routing tables.

Debugging process: Enable BGP logging, check neighbor configurations, look at updates and routes. Use commands like /log print where message~"BGP". Also, check for route flaps with /routing bgp advertisements print. Maybe look into timers and hold-downs. If there's a route causing flapping, maybe a faulty prefix is being advertised.

Root cause analysis: Maybe a misconfiguration in BGP timers leading to session drops. Or a flapping interface causing the BGP peer to reset. Could also be a routing loop or incorrect network statements advertising unstable routes. Let's say in this case, it's a duplex mismatch on the interface connected to the ISP, causing link flaps and thus BGP sessions to reset.

Solution: Fix the duplex settings on the interface. Adjust BGP timers if necessary. Maybe add a static route as a backup. Update configurations and monitor.

Verification: Check BGP session stability, logs, and user connectivity. Use commands like /ping and /routing bgp neighbor print to confirm.

Prevention: Regular checks on physical links, correct BGP timers, use BFD, implement route filtering. Maybe schedule maintenance during off-hours.

Common pitfalls: Forgetting to check physical layers, ignoring logs, misconfiguring BGP peers. Also, not testing after changes.

I need to include CLI commands with comments, example log outputs, and before/after configs. For instance, before the fix, the interface might have auto-negotiation on, leading to duplex mismatch. After, set it to full duplex manually.

Make sure each section flows logically. Use code blocks for commands and logs. Highlight the key findings and how the root cause was identified. Maybe show the log snippet where BGP state changes occur frequently, indicating flapping.

Also, mention related commands like /interface print, /system resource cpu print, etc. In pitfalls, warn against skipping physical checks or misapplying route filters.

I think that covers all the required sections. Need to structure it in markdown, use headers, and ensure each part answers the user's query comprehensively.

# Troubleshooting Guide
```markdown
# BGP Flapping Troubleshooting Scenario (RouterOS 6.x)

## 1. Initial Problem Report and Symptoms
**Report**: 459 users report intermittent internet outages across campus.  
**Symptoms**:
- BGP sessions resetting every 3-5 minutes
- High CPU usage on edge routers
- Routing table instability (`172.17.124.160/28` flapping)
- Logs show `BGP state changed` messages
- Users experience 30-60 second connectivity drops

---

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  ISP1[ISP A (AS65000)] --> R1
  ISP2[ISP B (AS65001)] --> R2
  R1 --> CoreSW1
  R2 --> CoreSW2
  CoreSW1 --> Users[/Users (459 devices)/]
  CoreSW2 --> Users
  subgraph MikroTik Routers
    R1(RouterOS 6.49.7)
    R2(RouterOS 6.49.7)
  end
```
**Key Details**:
- Dual-homed BGP with ISP A/B
- eBGP using AS 65530 (local)
- /28 subnet: `172.17.124.160/28`
- BGP timers: 30/90 seconds

---

## 3. Initial Assessment Steps
1. Check BGP neighbor status:
   ```bash
   /routing bgp neighbor print
   ```
   Output:
   ```
   0  instance=default remote-address=203.0.113.1 remote-as=65000 state=established 
   1  instance=default remote-address=198.51.100.1 remote-as=65001 state=active
   ```

2. Review system resources:
   ```bash
   /system resource print
   /system history print
   ```

3. Check interface statistics:
   ```bash
   /interface ethernet print stats
   ```

4. Verify route advertisements:
   ```bash
   /routing bgp advertisements print
   ```

---

## 4. Detailed Debugging Process
**Step 1: Enable BGP Debugging**
```bash
/log print where message~"BGP"
```
Output:
```
13:22:01 bgp,info BGP session closed with 203.0.113.1
13:22:04 bgp,info BGP connection established with 203.0.113.1
```

**Step 2: Check Route Flapping**
```bash
/routing route print where dst-address=172.17.124.160/28
```
Output shows frequent changes between ISP paths.

**Step 3: Verify BGP Timers**
```bash
/routing bgp instance print
```
Mismatched timers found (ISP A uses 60/180 vs local 30/90).

**Step 4: Interface Analysis**
```bash
/interface monitor-traffic ether1
```
Shows CRC errors increasing during flapping events.

---

## 5. Key Findings & Root Cause
**Root Cause**: Duplex mismatch on R1's ether1 (connected to ISP A):
- RouterOS auto-negotiation disabled
- ISP interface set to 100Mbps/full duplex
- Local interface at 100Mbps/half duplex

**Secondary Issues**:
- BGP timer mismatch causing premature session drops
- No route dampening configured

---

## 6. Solution Implementation
**Before** (Faulty Config):
```bash
/interface ethernet set ether1 auto-negotiation=no speed=100Mbps duplex=half
```

**After** (Corrected Config):
```bash
/interface ethernet set ether1 auto-negotiation=yes
# Wait for auto-negotiation
/interface ethernet monitor ether1 
# Verify negotiated settings
```

**BGP Timer Adjustment**:
```bash
/routing bgp neighbor set 0 hold-time=180 keepalive-time=60
```

---

## 7. Verification Process
1. Confirm stable BGP sessions:
   ```bash
   /routing bgp neighbor print interval=30s count=5
   ```

2. Monitor interface errors:
   ```bash
   /interface ethernet monitor ether1
   ```

3. Validate user connectivity:
   ```bash
   /ping 172.17.124.161 count=100 interval=1s
   ```

---

## 8. Prevention Measures
1. Implement BFD for faster failure detection
2. Enable route dampening:
   ```bash
   /routing bgp instance set default dampening=yes
   ```
3. Standardize BGP timer templates
4. Schedule quarterly interface audits

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp neighbor print` | Show BGP peer status |
| `/tool sniffer start interface=ether1` | Packet capture |
| `/interface ethernet monitor ether1` | Real-time interface stats |
| `/system routerboard print` | Check hardware status |

---

## 10. Common Pitfalls to Avoid
1. **Mismatched MTUs** causing TCP segmentation
2. **Ignoring physical layer** (CRC errors, duplex issues)
3. **Aggressive BGP timers** on high-latency links
4. **Missing route filters** allowing route leaks
5. **Overlooking syslog** messages during troubleshooting
```
