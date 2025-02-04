---
generated_at: 2025-02-03T15:50:31.689420
topic: BGP
category: Routing
version: 6.x
scale: SOHO
level: Basic
subnet: 172.19.187.96/28
scenario: Performance Degradation
environment: Cloud Infrastructure
affected_users: 907
duration: 15 hours
---

# Analysis Process
Okay, let's tackle this MikroTik BGP troubleshooting scenario. The user wants a detailed scenario for a SOHO network with performance degradation over 15 hours affecting 907 users in a cloud setup. The subnet is 172.19.187.96/28, and the RouterOS version is 6.x.

First, I need to start with the initial problem report. The main symptom is performance degradation. Users are complaining about slow access and timeouts. Maybe there's packet loss or high latency. The BGP routes might be flapping, causing instability. Since it's a SOHO network, the setup is probably simple but maybe connected to a cloud provider. The duration is 15 hours, which suggests it's not a transient issue but something persistent.

Next, the environment description. Since it's a cloud infrastructure, maybe there's a MikroTik router acting as a BGP peer with a cloud provider's router. The network topology would involve the SOHO router connected to the cloud. I should draw this in Mermaid. Let me think: SOHO Router (172.19.187.97/28) <-> Cloud Provider Router (e.g., 10.0.0.2). The subnet /28 gives 16 IPs, so the SOHO router's IP is probably the first usable one.

Initial assessment steps: Check BGP sessions, look for established state. Use `/routing bgp session print` to see if the session is established. Then check routes with `/ip route print` to ensure BGP routes are present. Check CPU and memory usage with `/system resource print`. Maybe look at traffic with `/interface monitor-traffic` to see if there's congestion.

Debugging process: Start by checking BGP session status. If it's established, maybe routes are being withdrawn. Check BGP updates with logging. Use `/log print` and look for BGP messages. Maybe enable debug logging with `/routing bgp log set yes` and see if there are flapping routes. Check if the MTU is mismatched between the MikroTik and the cloud router. Use `/interface print` to check MTU settings. Also, look at BGP timers; maybe the hold time is too short. Check the configuration with `/routing bgp peer print`.

Key findings: Suppose the MTU is mismatched. The MikroTik has 1500, but the cloud router uses 1450, causing fragmentation and retransmissions. Or maybe BGP hold timers are misconfigured, leading to session resets. Another possibility is route flapping due to a misconfigured network statement, advertising incorrect prefixes.

Solution: Adjust MTU on the MikroTik interface to match the cloud, or configure TCP MSS clamping. Alternatively, fix BGP timers to have a longer hold time. Update the BGP configuration to advertise the correct subnet.

Verification: After changing MTU, check if packet fragmentation decreases. Use `/tool sniffer quick` to capture packets. Monitor BGP session stability with `/routing bgp session print`. Test user performance metrics.

Prevention: Ensure MTU matches across all devices. Regularly monitor BGP sessions and logs. Use BGP password authentication. Validate advertised networks.

Common pitfalls: Forgetting to adjust MTU, ignoring BGP timers, not filtering advertised routes. Also, using default BGP settings without tuning for the environment.

Now, putting this all together in the required format. Make sure to include CLI commands, logs, before/after configs. Use code blocks for commands and log snippets. Mention the specific subnet and version 6.x constraints. Maybe in version 6.x, some commands differ from later versions, so use appropriate syntax.

Check if the initial problem report includes things like latency spikes, which would tie into MTU issues. The log examples should show BGP state changes. For example, a log entry like "BGP session closed" or "hold timer expired".

In the configuration, before might have the wrong MTU or incorrect BGP peer settings. After would correct those. For example, changing the MTU from 1500 to 1450 on the interface, or setting the hold time from 30 seconds to 90.

Also, in RouterOS 6.x, some commands might be under `/routing bgp` instead of `/routing/bgp` as in v7. So need to use the correct paths.

Alright, structuring each section step by step with these points in mind. Make sure the Mermaid diagram is correct. Include all required sections, and cross-check the user's requirements.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario (RouterOS 6.x)

## 1. Initial Problem Report and Symptoms
**Report**: Cloud-hosted SOHO network (907 users) experiences intermittent connectivity and slow application response for 15 hours.  
**Symptoms**:
- Latency spikes to 800ms+ (normally <50ms)
- 30-40% packet loss during peak hours
- BGP route flapping observed in provider portal
- Users report SSH session timeouts and VoIP quality issues

```log
[admin@MikroTik] > log print where message ~ "BGP"
15:22:41 bgp,info Session 10.0.0.2 closed (hold time expired)
15:23:12 bgp,info Session 10.0.0.2 established
```

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    A[SOHO Router (172.19.187.97/28)] -->|BGP/MPLS Cloud Link| B[Cloud Provider Router (10.0.0.2)]
    B --> C[Cloud Application Servers]
    A --> D[Local Users /907]
```

## 3. Initial Assessment Steps
1. Verify BGP session status:
   ```bash
   /routing bgp session print
   ```
   ```output
   0 name="To-Cloud" remote-address=10.0.0.2 remote-as=64515 state=established 
   ```
2. Check route propagation:
   ```bash
   /ip route print where bgp 
   ```
3. Monitor interface metrics:
   ```bash
   /interface ethernet monitor ether1
   ```

## 4. Detailed Debugging Process
**Step 1: Verify BGP Configuration**
```bash
/routing bgp peer print
```
```output
0 remote-address=10.0.0.2 remote-as=64515 tcp-md5-key="" hold-time=30s keepalive-time=10s
```

**Step 2: Check MTU Mismatch**
```bash
/interface print
```
```output
0 R ether1 mtu=1500 
```
Cloud provider requires 1450 MTU for VPN tunnels.

**Step 3: Analyze Traffic Patterns**
```bash
/tool sniffer quick protocol=tcp port=179
```
```output
11:34:22 TCP Retransmission: 172.19.187.97:179 -> 10.0.0.2:51234 [SYN]
```

## 5. Key Findings & Root Cause
**Root Cause**: MTU mismatch causing TCP segmentation and BGP session resets:
- Local MTU: 1500 bytes
- Cloud MTU: 1450 bytes (including VPN overhead)
- Result: Fragmentation → Retransmissions → Hold Timer Expiry

**Secondary Issues**:
- Aggressive BGP timers (hold=30s)
- No TCP MD5 authentication

## 6. Solution Implementation
**Before**:
```bash
/interface ethernet set ether1 mtu=1500
/routing bgp peer set To-Cloud hold-time=30s keepalive-time=10s
```

**After**:
```bash
/interface ethernet set ether1 mtu=1450
/routing bgp peer set To-Cloud hold-time=90s keepalive-time=30s tcp-md5-key="secret123"
```

## 7. Verification Process
1. Confirm stable BGP session:
   ```bash
   /routing bgp session print count
   ```
   ```output
   uptime: 2h34m12s
   ```
2. Test path MTU:
   ```bash
   /ping 10.0.0.2 size=1472 do-not-fragment
   ```
3. Monitor traffic:
   ```bash
   /tool bandwidth-server
   ```

## 8. Prevention Measures
- Implement BGP monitoring with `/tool fetch` to external dashboard
- Enable BGP logging:  
  ```bash
  /routing bgp log set yes
  ```
- Regular MTU audits across all interfaces
- BGP peer template standardization

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp advertisement print` | Check advertised routes |
| `/interface detect-internet` | Verify cloud connectivity |
| `/tool torchr` | Real-time traffic analysis |

## 10. Common Pitfalls to Avoid
- **Never** use default BGP timers in cloud environments
- Avoid mixing IPv4/IPv6 BGP sessions without proper filtering
- Never skip TCP-MD5 authentication for public peers
- Don't assume cloud providers accept full BGP tables
```
