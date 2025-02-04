---
generated_at: 2025-02-03T16:14:54.463185
topic: BGP
category: Routing
version: 7.x
scale: Enterprise
level: Basic
subnet: 172.28.251.128/25
scenario: QoS Misconfiguration
environment: Campus Network
affected_users: 460
duration: 17 hours
---

# Analysis Process
Okay, let's tackle this MikroTik BGP troubleshooting scenario. The user wants a detailed example with specific elements. First, I need to understand the scenario: an enterprise campus network using RouterOS 7.x, subnet 172.28.251.128/25, QoS misconfiguration affecting 460 users for 17 hours. 

Starting with the problem report and symptoms. Users are complaining about VoIP and video conferencing issues. BGP routes are unstable. That makes sense because QoS affects traffic prioritization, which would impact real-time applications. Maybe BGP routes are flapping because QoS is dropping BGP packets, which are usually low volume but need to be prioritized.

Next, the environment description. The network is a campus with core, distribution, and access layers. The core connects to two ISPs via BGP. The subnet in question is part of the user VLAN. I'll need to create a Mermaid diagram showing core, distribution switches, access switches, user VLAN, and ISP connections. Including IPs for clarity.

Initial assessment steps. Check BGP sessions with '/routing/bgp/session/print'. Look for established sessions. Then check logs for BGP errors. Verify QoS configuration with '/queue/tree/print' and see if BGP ports (179) are being prioritized or mistakenly limited. Also check traffic flow with Torch on the core router's interfaces. Maybe BGP traffic is being dropped by a queue.

Detailed debugging. Start by checking BGP neighbor status. If sessions are flapping, look into TCP resets. Use '/tool sniffer' to capture BGP packets. Check if QoS marks are applied correctly. Maybe BGP isn't marked as critical traffic. For example, if the QoS is prioritizing VoIP (like EF) but not BGP, then under congestion, BGP could be deprioritized. Check queue stats for drops on BGP traffic. Use '/queue tree print stats' to see packet drops on the parent queue.

Key findings: QoS policy is rate-limiting all traffic except VoIP, including BGP. BGP uses TCP/179, which wasn't exempted, leading to packet drops during congestion. This caused BGP sessions to reset, affecting routing and user traffic.

Solution: Modify the queue tree to exclude BGP traffic from rate-limiting. Create a firewall mangle rule to mark BGP connections and apply a higher priority queue. Update the QoS configuration to prioritize BGP along with VoIP.

Verification: Check BGP sessions are stable, monitor queue stats for drops, test user applications. Prevention measures: Document QoS policies, implement monitoring for BGP, test changes in lab, use DSCP markings.

CLI commands: Show BGP sessions, sniffer, queue tree stats, mangle rules. Common pitfalls: Forgetting BGP in QoS, not monitoring after changes, misapplying queue order.

I need to structure each section with markdown, include code blocks for commands, maybe example logs, and before/after configs. Make sure the Mermaid diagram is correct. Also, check that the solution addresses the root cause by exempting BGP traffic from QoS limits.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario: QoS Misconfiguration

## 1. Initial Problem Report and Symptoms
**Report:** Campus users report intermittent connectivity to cloud services and ERP system. VoIP quality degraded with jitter.  
**Symptoms:**
- 30-40% packet loss during peak hours (10:00-16:00)
- BGP route flapping observed in routing tables
- Interface queues hitting 100% utilization on core links
- AS_PATH changes every 8-12 minutes for critical prefixes
- High TCP retransmissions (15-20%) on BGP sessions

## 2. Environment Description
**Network Topology:**
```mermaid
graph TD
    CORE[Core Router (RB1100AHx4)] -->|BGP/10G| DIST1[Distribution Switch 1]
    CORE -->|BGP/10G| DIST2[Distribution Switch 2]
    DIST1 --> ACCESS1[Access Switch Stack 1-5]
    DIST2 --> ACCESS2[Access Switch Stack 6-10]
    CORE -->|eBGP| ISP1(ISP1 AS65000)
    CORE -->|eBGP| ISP2(ISP2 AS65001)
    ACCESS1 --> USERS[User VLAN 172.28.251.128/25]
```

## 3. Initial Assessment Steps
1. Verify BGP peer status:
   ```bash
   /routing/bgp/session/print where remote.address=172.28.251.129
   # Output:
   # 0 remote-address=172.28.251.129 remote-as=65530 state=established
   ```
   
2. Check interface queue utilization:
   ```bash
   /interface queue tree print stats
   # Output:
   # name="QoS-Parent" rate=945Mbps packet-rate=145kbps queue=100% 
   ```

3. Verify route stability:
   ```bash
   /routing/bgp/advertisements/print detail
   # Shows frequent withdrawals for 192.168.100.0/24
   ```

## 4. Detailed Debugging Process
**Step 1: Identify QoS Policy Impact**
```bash
/queue tree print
# Before:
# 0 name="QoS-Parent" parent=global-in priority=1 max-limit=1G 
# 1 name="VoIP" parent=QoS-Parent priority=8 limit=200M
# 2 name="Default" parent=QoS-Parent priority=1 limit=800M
```

**Step 2: Check BGP Traffic Marking**
```bash
/ip firewall mangle print
# Missing BGP-specific marking rules for TCP/179
```

**Step 3: Capture BGP Traffic**
```bash
/tool sniffer quick protocol=tcp port=179
# Output shows TCP retransmissions every 5-7 minutes
```

**Step 4: Analyze Queue Drops**
```bash
/queue tree monitor QoS-Parent
# Packets dropped: 142,500 in 15 minutes (95% TCP/179)
```

## 5. Key Findings & Root Cause
**Root Cause:**  
QoS policy was throttling all non-VoIP traffic to 800Mbps without BGP exception. During peak (950Mbps+ traffic), BGP packets were being dropped due to queue saturation.

**Key Evidence:**
- BGP received 0.15% of total queue capacity
- 142,500 BGP packets dropped during 17-hour outage
- TCP retransmit rate correlated with queue saturation events

## 6. Solution Implementation
**Step 1: Create BGP Priority Queue**
```bash
/queue tree add name="BGP-Priority" parent=QoS-Parent priority=7 \
    limit=50M max-limit=100M burst-limit=150M burst-threshold=80M \
    burst-time=30s
```

**Step 2: Add Firewall Marking**
```bash
/ip firewall mangle add chain=forward protocol=tcp dst-port=179 \
    action=mark-connection new-connection-mark=bgp_conn
/ip firewall mangle add chain=forward connection-mark=bgp_conn \
    action=mark-packet new-packet-mark=bgp_traffic
```

**Step 3: Update Queue Rules**
```bash
/queue tree set [find name="Default"] limit=750M
/queue tree set [find name="BGP-Priority"] packet-mark=bgp_traffic
```

## 7. Verification Process
1. Monitor queue utilization post-fix:
   ```bash
   /queue tree monitor QoS-Parent,BGP-Priority
   # Output shows BGP traffic using dedicated queue
   ```

2. Verify BGP stability:
   ```bash
   /routing/bgp/session/print stats
   # Established time >60 minutes, 0 withdrawals
   ```

3. User validation:
   ```bash
   /tool bandwidth-server monitor 172.28.251.200
   # Jitter reduced from 45ms to 8ms
   ```

## 8. Prevention Measures
1. Implement BGP monitoring:
   ```bash
   /tool graphing queue add name=bgp_q interfaces=all
   ```

2. Add QoS safeguard:
   ```bash
   :global qosCheck do={
     :if ([/queue tree get QoS-Parent queue] > 85) do={
       /log info "QoS queue saturation detected!"
     }
   }
   ```

3. Regular policy audits:
   ```bash
   /system script add name=QoS-Audit source="/queue tree print; /ip firewall mangle print"
   ```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing/bgp/session/print stats` | BGP session statistics |
| `/queue tree monitor [name]` | Real-time queue monitoring |
| `/tool sniffer quick protocol=tcp port=179` | BGP packet capture |

## 10. Common Pitfalls
1. **Queue Ordering:**  
   *Incorrect:* Priority 1 queues processed before priority 8  
   *Correct:* Lower priority numbers = higher precedence

2. **Burst Configuration:**  
   Avoid excessive burst limits (>150% of max-limit) that starve other queues

3. **Firewall Chain Order:**  
   Ensure BGP marking rules come before general QoS rules in mangle chain

4. **AS_PATH Filtering:**  
   Never combine QoS changes with BGP policy modifications during outages
```
