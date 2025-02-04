---
generated_at: 2025-02-03T16:15:44.480127
topic: BGP
category: Routing
version: 7.x
scale: Enterprise
level: Advanced
subnet: 172.29.146.128/25
scenario: QoS Misconfiguration
environment: Branch Office
affected_users: 594
duration: 11 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP with the given parameters. Let's start by understanding the user's requirements. The topic is BGP on RouterOS 7.x in an enterprise branch office. The subnet is 172.29.146.128/25, and the issue is a QoS misconfiguration affecting 594 users over 11 hours. The answer needs to follow the specified format with sections like Initial Problem Report, Network Topology in Mermaid, etc.

First, the Initial Problem Report and Symptoms. The symptoms mentioned are high latency, packet loss, and VoIP issues. I should describe how users reported these problems, especially during peak hours. Then, the Environment Description: it's a branch office connected to HQ and another branch via BGP. The subnet is part of a larger network. Need to create a Mermaid diagram showing the connections. Maybe include the ISP links and QoS policies.

Initial Assessment Steps: Check BGP status, verify routes, look for QoS configurations. Use commands like `/routing bgp summary print`, `/ip route print`, and check queue trees or simple queues in QoS. Then look at interface statistics for packet drops.

Detailed Debugging Process: Start by verifying BGP neighbors. Use `/routing bgp session print` to see if sessions are established. Then check if the routes are being advertised correctly with `/routing bgp advertisements print`. Next, inspect QoS configurations. Since the problem is QoS misconfiguration, maybe the queue rules are misapplied. Look at `/queue tree print` and `/queue simple print`. Check if the correct traffic is being prioritized or if there's a misclassification.

Key Findings and Root Cause Analysis: Suppose the QoS policy was applied to the wrong interface, causing BGP traffic to be throttled. Maybe the queue was set on the WAN interface but should have been on LAN, leading to congestion. Or incorrect DSCP markings affecting BGP.

Solution Implementation Steps: Adjust the QoS queue to correct the target interface or traffic classification. Remove the misconfiguration and reapply proper settings. For example, changing the queue tree's interface from ether1 to ether2. Then reset the BGP sessions to re-establish routes.

Verification Process: Check latency and packet loss after the fix. Monitor BGP sessions and routes. Use tools like ping, traceroute, and check QoS stats again.

Prevention Measures: Implement pre-change validation, monitoring with tools like The Dude, regular audits, and documentation.

Related Commands Reference: List all the commands used in the steps, like BGP and QoS commands.

Common Pitfalls: Forgetting to apply QoS correctly to the right interface, not monitoring traffic patterns, misclassifying traffic, etc.

I need to make sure CLI commands are in code blocks, include comments, log outputs, and before/after configurations where relevant. Let me structure each section accordingly, making sure the Mermaid diagram is correctly formatted. Also, ensure that the root cause ties back to QoS affecting BGP, like traffic being deprioritized leading to route flapping or congestion.

# Troubleshooting Guide
```markdown
# BGP Troubleshooting Scenario: QoS Misconfiguration (RouterOS 7.x)

---

## 1. Initial Problem Report and Symptoms
**Reported Issues**:
- Intermittent connectivity to cloud applications (594 users affected)
- VoIP call drops during peak hours (11:00 AM - 10:00 PM)
- Latency spikes (150ms+ during congestion vs. normal 25ms)

**Observed Symptoms**:
```log
[admin@Branch-Router] > ping 172.29.146.129 interval=1
  SEQ HOST                                     SIZE TTL TIME  STATUS             
    0 172.29.146.129                            56  64 153ms 
    1 172.29.146.129                            56  64 timeout
    2 172.29.146.129                            56  64 89ms  
    3 172.29.146.129                            56  64 162ms
```

---

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  Branch-Router -->|BGP/MPLS| HQ-Router
  Branch-Router -->|BGP/Stub| DR-Router
  Branch-Router --> ether1-WAN[ISP (100Mbps)]
  Branch-Router --> ether2-LAN[172.29.146.128/25]
  subgraph Branch Office
    ether2-LAN --> Switch --> User-VLAN
  end
```

---

## 3. Initial Assessment Steps
1. Verify BGP peer status:
   ```bash
   /routing bgp summary print
   ```
2. Check route advertisements:
   ```bash
   /ip route print where bgp
   ```
3. Review QoS configuration:
   ```bash
   /queue tree print detail
   ```
4. Check interface statistics:
   ```bash
   /interface ethernet monitor ether1,ether2
   ```

---

## 4. Detailed Debugging Process
**Step 1: BGP Session Validation**
```bash
[admin@Branch-Router] > /routing bgp session print
 0 name="HQ" remote.address=10.255.0.1 established=yes 
 1 name="DR" remote.address=10.255.0.2 established=no  # Session flapping
```

**Step 2: Traffic Flow Analysis**
```bash
[admin@Branch-Router] > /tool sniffer quick protocol=tcp port=179
 # No BGP keepalives detected on WAN interface
```

**Step 3: QoS Inspection**
```bash
[admin@Branch-Router] > /queue tree print
Flags: X - disabled, I - invalid 
 0   name="QoS-WAN" parent=ether1 packet-mark=all limit-at=10M/10M max-limit=100M/100M 
     # Misconfigured: All traffic throttled to 10M baseline
```

---

## 5. Key Findings & Root Cause
**Findings**:
- BGP marked as `background` class in QoS (default DSCP 8)
- WAN queue limiting ALL traffic to 10M baseline
- BGP keepalives deprioritized during congestion

**Root Cause**:
```log
QoS Policy Hierarchy:
1. VoIP (EF) - 30M guaranteed
2. Web (AF41) - 50M guaranteed
3. Background (DF) - 10M residual  # BGP trapped here
```

---

## 6. Solution Implementation
**Before (Faulty QoS)**:
```bash
/queue tree add name=QoS-WAN parent=ether1 packet-mark=all \
  limit-at=10M/10M max-limit=100M/100M
```

**After (Corrected QoS)**:
```bash
# Create BGP packet mark
/ip firewall mangle add chain=forward protocol=tcp dst-port=179 \
  action=mark-packet new-packet-mark=bgp-traffic

# Prioritize BGP
/queue tree add name=QoS-BGP parent=ether1 packet-mark=bgp-traffic \
  priority=1 limit-at=2M/2M max-limit=10M/10M
```

---

## 7. Verification Process
1. Confirm BGP stability:
   ```bash
   /routing bgp session print interval=30
   ```
2. Validate QoS counters:
   ```bash
   /queue tree monitor QoS-BGP
     rate: 1.8Mbps/1.9Mbps 
     packet-rate: 120/130
   ```
3. User validation:
   ```log
   [admin@Branch-Router] > ping 172.29.146.129 interval=1
     SEQ HOST                                     SIZE TTL TIME  STATUS             
       0 172.29.146.129                            56  64 24ms  
       1 172.29.146.129                            56  64 22ms
   ```

---

## 8. Prevention Measures
1. **Traffic Classification Policy**:
   ```bash
   /ip firewall mangle add chain=forward dscp=48 action=mark-packet \
     new-packet-mark=voice-traffic comment="EF: VoIP"
   ```
2. **BGP Monitoring**:
   ```bash
   /tool graphing interface add store-every=5min interfaces=ether1
   ```
3. **QoS Pre-Validation**:
   ```bash
   /tool traffic-generator quick duration=10s rate=100M
   ```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp export` | View BGP route advertisements |
| `/queue simple print detail` | Check QoS bandwidth allocation |
| `/ip firewall mangle print stats` | Verify traffic classification |

---

## 10. Common Pitfalls to Avoid
1. **Misordering QoS Rules**: Always prioritize control protocols (BGP/OSPF) over user traffic
2. **Ignoring DSCP Markings**: Use `ip firewall mangle` to classify before queuing
3. **Overlooking Asymmetric Limits**: Ensure `max-limit` matches physical interface capacity
4. **Neglecting Baseline Guarantees**: Allocate minimum `limit-at` for critical services
```
