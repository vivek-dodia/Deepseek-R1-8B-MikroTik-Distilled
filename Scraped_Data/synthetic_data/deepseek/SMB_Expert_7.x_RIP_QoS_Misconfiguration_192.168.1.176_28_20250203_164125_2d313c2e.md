---
generated_at: 2025-02-03T16:42:17.448709
topic: RIP
category: Routing
version: 7.x
scale: SMB
level: Expert
subnet: 10.31.63.0/25
scenario: QoS Misconfiguration
environment: Multi-tenant Building
affected_users: 417
duration: 2 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario based on the user's specifications. Let me start by understanding the requirements.

The topic is RIP (Routing Information Protocol) in RouterOS 7.x for a Small to Medium Business (SMB) network. The subnet is 10.31.63.0/25 in a multi-tenant building. The scenario is a QoS misconfiguration affecting 417 users over 2 hours. The answer needs to include 10 sections with specific elements like CLI commands, logs, mermaid diagrams, etc.

First, let's outline each section as per the user's instructions.

1. **Initial Problem Report and Symptoms**: Users report slow internet and VoIP issues. Symptoms include high latency, packet loss, and RIP routes not updating properly. Need to describe the symptoms clearly.

2. **Environment Description and Network Topology**: The network has multiple tenants with VLANs. The main router connects to switches and an ISP. I need to create a mermaid diagram showing the router, switches, VLANs, and ISP link.

3. **Initial Assessment Steps**: Checking interface statuses, RIP neighbors, routing tables, QoS settings, and logs. Include CLI commands like `/interface print`, `/routing rip neighbor print`, etc.

4. **Detailed Debugging Process**: Use commands to check RIP routes, QoS configurations, traffic flow, and logs. Maybe compare configurations before and after. Show CLI outputs, possibly with comments explaining what's wrong.

5. **Key Findings and Root Cause Analysis**: Discover that QoS is prioritizing all traffic as high priority, causing congestion and RIP updates to be delayed. Explain how this affects RIP convergence and traffic.

6. **Solution Implementation Steps**: Adjust QoS policies to prioritize VoIP and de-prioritize bulk traffic. Update queue types and rules. Show before and after config snippets.

7. **Verification Process**: Check routing table stability, VoIP performance, and QoS stats. Use commands like `/ping`, `/routing route print`, and `/queue simple print`.

8. **Prevention Measures**: Recommendations like regular QoS audits, monitoring tools, separate VLANs for management traffic, etc.

9. **Related Commands Reference**: List all CLI commands used in the scenario with brief descriptions.

10. **Common Pitfalls to Avoid**: Highlight mistakes like misclassifying traffic, not monitoring RIP, etc.

Now, I need to flesh out each section with accurate details. For the network topology in mermaid, I'll represent the main router connected to two switches (tenant and VoIP), each with their VLANs, and the ISP link. The subnet 10.31.63.0/25 is for the tenants.

In the QoS misconfiguration, maybe all traffic is marked as priority 1, causing no differentiation. This would lead to congestion, affecting VoIP and RIP updates which use multicast. RIP relies on timely updates; if QoS delays them, routes might not converge properly.

CLI commands should reflect checking RIP neighbors, routes, and QoS queues. For example, in the initial assessment, using `/routing rip neighbor print` to see if neighbors are present. When debugging, looking at `/routing rip statistics` to see update errors.

In the solution, adjusting the queue types from `pfifo` to `pcq` for fair bandwidth distribution and setting correct priorities. Maybe adding a queue for VoIP with high priority and another for bulk traffic with lower priority.

Verification would involve pinging VoIP servers to check latency, ensuring RIP routes are stable, and queue stats show proper traffic handling.

Common pitfalls might include not testing QoS changes in a lab first, or not considering RIP's multicast traffic in QoS policies.

I need to make sure the CLI examples are accurate for RouterOS 7.x. For instance, in QoS, using `/queue simple` configurations. Also, log examples should reflect possible entries when RIP updates are missed due to congestion.

Let me structure each section step by step, ensuring all elements are covered. Check that the mermaid diagram is correctly formatted and the commands are properly enclosed in code blocks with comments where necessary.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP with QoS Misconfiguration

## 1. Initial Problem Report and Symptoms
**Report**: 417 users in a multi-tenant building report severe internet slowdowns and VoIP call drops.  
**Symptoms**:
- Latency spikes (200-1500ms) during business hours
- RIP routes intermittently missing from routing table
- VoIP (VLAN 100) RTP packet loss >25%
- Users in 10.31.63.0/25 subnet most affected

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  R[Main Router (RB4011)] -->|ether1| ISP
  R -->|ether2| SW1[Tenant Switch (CSS326)]
  R -->|ether3| SW2[VoIP Switch (CRS112)]
  SW1 -->|VLAN 200| T1[Tenant 1]
  SW1 -->|VLAN 201| T2[Tenant 2]
  SW2 -->|VLAN 100| V1[VoIP Phone Group 1]
  SW2 -->|VLAN 100| V2[VoIP Phone Group 2]
```

## 3. Initial Assessment Steps
1. Check interface status:
   ```bash
   /interface print where name~"ether[1-3]"
   # Output: All interfaces show "status=up"
   ```

2. Verify RIP neighbors:
   ```bash
   /routing rip neighbor print
   # Output: 0 peers found
   ```

3. Check routing table:
   ```bash
   /ip route print where static=no
   # Output: Only shows 2/4 expected RIP routes
   ```

4. Initial QoS check:
   ```bash
   /queue simple print 
   # Output: All traffic marked priority=1
   ```

## 4. Detailed Debugging Process
**Step 1: Verify RIP Configuration**
```bash
/routing rip instance print
# Output:
# 0 name="main" afi=ipv4 redistribute-static=no 
#   redistribute-connected=no redistribute-ospf=no

/routing rip interface print
# Output: No interfaces enabled for RIP
```

**Step 2: Analyze QoS Rules**
```bash
/queue type print
# Output: queue-type=pfifo for all interfaces

/queue simple print detail where target=10.31.63.0/25
# Output: max-limit=100M/100M priority=1 for all queues
```

**Step 3: Check Traffic Flow**
```bash
/tool sniffer quick port=520 protocol=udp
# Output: RIP updates observed with 300-500ms delays
```

**Step 4: Review Logs**
```bash
/log print where message~"RIP"
# Output:
# 12:05:23 router,debug,routing,error RIP: route update timeout
# 12:07:11 router,debug,routing,error RIP: neighbor 10.31.63.1 lost
```

## 5. Key Findings & Root Cause
**Findings**:
1. RIP not configured on any interfaces
2. QoS policy marked all traffic as priority=1
3. No bandwidth reservation for control protocols

**Root Cause**:  
Flat QoS prioritization caused congestion in 10.31.63.0/25 subnet, delaying RIP updates beyond timeout thresholds (120s). Missing routes led to suboptimal paths and packet loss.

## 6. Solution Implementation
**Before** (Problematic QoS):
```bash
/queue simple add name="TenantData" target=10.31.63.0/25 max-limit=100M/100M priority=1
```

**After** (Corrected Config):
```bash
# Configure RIP properly
/routing rip instance set [find] redistribute-connected=yes
/routing rip interface add interface=ether2

# Update QoS
/queue type add name="VoIP_High" kind=pcq pcq-rate=2M pcq-classifier=dst-address
/queue simple add name="VoIP" target=192.168.100.0/24 queue=VoIP_High priority=1
/queue simple add name="TenantData" target=10.31.63.0/25 max-limit=80M/80M priority=4
/queue simple add name="RIP_Control" dst-address=224.0.0.9 protocol=udp dst-port=520 priority=2
```

## 7. Verification Process
1. Confirm RIP convergence:
   ```bash
   /routing route print where protocol=rip
   # Output: 4 stable RIP routes
   ```

2. Test VoIP quality:
   ```bash
   /ping 192.168.100.1 count=100 interval=0.1
   # Output: 0% loss, avg-rtt=28ms
   ```

3. Verify QoS hierarchy:
   ```bash
   /queue simple print stats
   # Output: VoIP queue shows 25% utilization, TenantData at 78%
   ```

## 8. Prevention Measures
1. Implement QoS hierarchy template
2. Enable RIP timers monitoring:
   ```bash
   /tool snmp set enabled=yes
   /tool graphing interface add interface=ether2
   ```
3. Create firewall rule to protect RIP:
   ```bash
   /ip firewall filter add chain=input protocol=udp dst-port=520 action=accept
   ```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing rip neighbor print` | List RIP peers |
| `/queue type export` | Show QoS algorithms |
| `/tool sniffer quick` | Capture real-time traffic |

## 10. Common Pitfalls to Avoid
1. **Never** set all queues to same priority level
2. Avoid mixing control plane and data plane traffic classes
3. Ensure RIP interfaces match VLAN boundaries
4. Always leave 20% headroom for protocol overhead
5. Test QoS changes during maintenance windows
```
