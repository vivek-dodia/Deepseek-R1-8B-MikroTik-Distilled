---
generated_at: 2025-02-03T15:19:47.844569
topic: OSPF
category: Routing
version: 6.x
scale: SMB
level: Basic
subnet: 10.81.124.0/27
scenario: QoS Misconfiguration
environment: Retail Network
affected_users: 491
duration: 12 hours
---

# Analysis Process
Okay, let me try to work through this MikroTik OSPF troubleshooting scenario. The user wants a detailed scenario based on the given parameters. Let's start by breaking down each section they mentioned and think about how to approach them.

First, the topic is OSPF with RouterOS 6.x in a Small-Medium Business (SMB) retail network. The subnet is 10.81.124.0/27, which is a /27 subnet, so that's 32 addresses. The problem is QoS misconfiguration affecting 491 users over 12 hours. 

Starting with the initial problem report. Symptoms might include slow network performance, OSPF routes not being advertised properly, maybe some areas of the network being unreachable. Since it's QoS related, perhaps traffic prioritization is wrong, causing critical services like POS systems to lag.

For the environment description and network topology in Mermaid, I need to outline a typical retail setup. Maybe a head office router connected to multiple store routers, with POS systems, CCTV, and guest Wi-Fi. The subnet 10.81.124.0/27 is used in one of the stores. The core router connects to the ISP and has QoS policies. OSPF is running between all routers.

Initial assessment steps would involve checking OSPF neighbors, routing tables, and QoS configurations. Using commands like `/routing ospf neighbor print` to see if neighbors are established. Checking routes with `/ip route print` and looking for missing OSPF routes. Also, verifying QoS settings with `/queue tree print` or `/queue simple print`.

For detailed debugging, maybe check OSPF adjacencies, look at the OSPF database, see if routes are being advertised. Then examine QoS configurations. Since the issue is QoS misconfiguration affecting OSPF, maybe the QoS is throttling OSPF traffic (multicast) or prioritizing the wrong traffic. For example, if OSPF is using multicast (224.0.0.5) and QoS is deprioritizing that, it could cause OSPF neighbor flapping or delayed route updates.

Key findings would be that the QoS rules were applied to all traffic, including OSPF, causing OSPF hellos to be delayed or dropped. Root cause: OSPF relies on timely hello packets; if QoS is prioritizing other traffic, OSPF adjacencies drop, leading to route flapping and network instability.

Solution would involve adjusting QoS policies to exempt OSPF traffic. Creating a queue rule that prioritizes OSPF multicast or marks OSPF traffic for higher priority. For example, using a firewall mangle rule to mark OSPF packets and then applying a queue that gives them priority.

Verification would involve checking OSPF neighbors are stable, routes are present, and QoS stats show OSPF traffic is prioritized. Prevention measures might include documenting QoS policies, testing changes in lab, monitoring OSPF status, and using traffic marking for control protocols.

Common pitfalls could be not considering control plane traffic in QoS, misapplying queue rules to all interfaces, or not testing after changes.

Now, putting this all together in the required format. Need to structure each section with the necessary details. For CLI commands, include examples like checking OSPF neighbors, looking at queues, mangle rules. Maybe show before and after configurations for the QoS settings.

Also, need to include Mermaid diagram for the network topology. Let me sketch that out. Core router connected to ISP, then connected to three store routers (Store1, Store2, Store3). Each store has POS, CCTV, Guest WiFi. The subnet in question is part of Store1. OSPF areas might be backbone area 0.0.0.0.

Log examples could show OSPF neighbor state changes, or queue drops on OSPF traffic. Before configuration, the queue tree applies to all traffic, after configuration, there's a separate queue for OSPF with higher priority.

Alright, I think that covers the main points. Now, structure each section step by step, include CLI commands with comments, example logs, before/after configurations, etc.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF with QoS Misconfiguration

## 1. Initial Problem Report and Symptoms
**Report:**  
Retail network users report severe latency in POS systems, CCTV streaming failures, and guest Wi-Fi outages.  
**Symptoms:**  
- Intermittent connectivity between stores (10.81.124.0/27 subnet) and HQ.  
- OSPF routes missing in routing tables.  
- High CPU usage on core router interfaces.  
- QoS statistics show 80% packet drops on low-priority queues.  

---

## 2. Environment Description and Network Topology
```mermaid
graph TD
  Core[Core Router (10.81.124.1/27)] --> ISP
  Core --> Store1[Store 1 Router (10.81.124.2/27)]
  Core --> Store2[Store 2 Router (10.81.124.3/27)]
  Core --> Store3[Store 3 Router (10.81.124.4/27)]
  Store1 --> POS[POS Terminals]
  Store1 --> CCTV[CCTV Cameras]
  Store1 --> Guest[Guest Wi-Fi]
  style Store1 fill:#f9f,stroke:#333
```
- **OSPF Areas**: All routers in OSPF Area 0.0.0.0.  
- **QoS Policy**: Prioritize POS (DSCP EF) and CCTV (DSCP AF41), deprioritize Guest Wi-Fi.  

---

## 3. Initial Assessment Steps
1. Check OSPF neighbor status:  
   ```bash
   /routing ospf neighbor print
   # Output:
   #   instance=default address=10.81.124.2 state="Full" router-id=192.168.1.2
   #   instance=default address=10.81.124.3 state="Init" router-id=192.168.1.3
   ```
   **Observation**: Store2 stuck in `Init` state.  

2. Verify OSPF routes:  
   ```bash
   /ip route print where protocol=ospf
   # Output: Only 2/10 expected OSPF routes present.
   ```

3. Check QoS configuration:  
   ```bash
   /queue tree print
   # Output:
   #  0 name="QoS-Priority" parent=global-in packet-mark=POS priority=1
   #  1 name="QoS-Default" parent=global-in packet-mark="" priority=8
   ```

---

## 4. Detailed Debugging Process with CLI Commands
**Step 1**: Capture OSPF traffic on Core Router:  
```bash
/tool sniffer quick protocol=ospf
# Logs:
# 12:05:23 OSPF: Hello packet from 10.81.124.3 dropped (queue congestion).
```

**Step 2**: Identify QoS misconfiguration affecting OSPF multicast (224.0.0.5):  
```bash
/queue tree print where name~"QoS-Default"
# Output:
#   queue=wireless priority=8 max-limit=10M
#   (Applies to all traffic, including OSPF)
```

**Step 3**: Verify firewall marks for OSPF:  
```bash
/ip firewall mangle print where comment~"OSPF"
# Output: No rules found.
```

---

## 5. Key Findings and Root Cause Analysis
**Root Cause**:  
- QoS policy `QoS-Default` applied to all traffic (including OSPF multicast), causing packet drops.  
- OSPF neighbor adjacency failed due to missed Hello packets.  

**Impact**:  
- OSPF routes were not propagated, leading to network segmentation.  
- POS/CCTV traffic deprioritized due to missing QoS marks.  

---

## 6. Solution Implementation Steps
**Step 1**: Create firewall rule to mark OSPF traffic:  
```bash
/ip firewall mangle add
chain=preroute protocol=ospf action=mark-packet new-packet-mark=OSPF passthrough=no
comment="Mark OSPF for QoS exemption"
```

**Step 2**: Adjust QoS queue to prioritize OSPF:  
```bash
/queue tree add name="QoS-OSPF" parent=global-in packet-mark=OSPF priority=1 max-limit=1M
/queue tree set [find name="QoS-Default"] priority=10
```

**Before/After QoS Configuration**:  
| Before | After |
|--------|-------|
| `priority=8` for all traffic | `priority=1` for OSPF, `priority=10` for default |

---

## 7. Verification Process
1. Confirm OSPF neighbors stabilize:  
   ```bash
   /routing ospf neighbor print
   # Output:
   #   address=10.81.124.3 state="Full"
   ```

2. Check QoS stats for OSPF traffic:  
   ```bash
   /queue tree monitor QoS-OSPF
   # Output: 0 packets dropped, 1200 packets queued.
   ```

---

## 8. Prevention Measures
- Document QoS policies for control protocols (OSPF, BGP).  
- Test QoS changes in lab before deployment.  
- Add monitoring for OSPF adjacency states (`/tool graphing interface add ospf-neighbors`).  

---

## 9. Related Commands Reference
```bash
/routing ospf instance print        # Check OSPF instances
/ip firewall mangle print           # List marking rules
/queue tree monitor [name]          # Real-time QoS stats
```

---

## 10. Common Pitfalls to Avoid
- ❌ Applying QoS policies without exempting control-plane traffic.  
- ❌ Using `global-in` queues without traffic marking.  
- ❌ Assuming OSPF uses TCP (it uses IP protocol 89).  
```
