---
generated_at: 2025-02-03T15:18:55.585250
topic: OSPF
category: Routing
version: 6.x
scale: SOHO
level: Expert
subnet: 192.168.127.128/28
scenario: QoS Misconfiguration
environment: Service Provider Core
affected_users: 639
duration: 6 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF with a QoS misconfiguration in a SOHO environment. Let's start by breaking down each section required.

1. **Initial Problem Report and Symptoms**: The user mentioned 639 affected users over 6 hours. Symptoms might include slow internet, packet loss, and OSPF instability. Maybe VoIP and video conferencing issues due to QoS.

2. **Environment Description**: It's a SOHO network in a Service Provider Core. The subnet is 192.168.127.128/28. Need a simple Mermaid topology. Let's say two edge routers connected to a core router, with customer networks attached.

3. **Initial Assessment Steps**: Check OSPF neighbors, interface status, routing tables. Use commands like `/routing ospf neighbor print`, `interface print`, `/ip route print`.

4. **Debugging Process**: Look into OSPF logs, check QoS configurations. Maybe someone applied a queue that's too aggressive, causing OSPF traffic to be deprioritized. Commands like `/system logging print`, `/queue tree print`.

5. **Key Findings**: QoS misconfiguration where OSPF traffic (protocol 89) isn't prioritized. Queue dropping OSPF packets, leading to neighbor flapping.

6. **Solution**: Adjust QoS rules to prioritize OSPF. Use firewall mangle to mark OSPF packets and apply a high-priority queue.

7. **Verification**: Check OSPF neighbors stable, routing table restored. Monitor queues with `/queue tree monitor`.

8. **Prevention**: Test QoS changes in lab, document configs, monitor OSPF and QoS regularly.

9. **Commands Reference**: List all commands used in each section.

10. **Common Pitfalls**: Forgetting to prioritize routing protocols in QoS, incorrect mangle rules, not monitoring after changes.

I need to make sure the CLI commands are accurate for RouterOS 6.x. For example, in version 6.x, OSPF is under `/routing ospf`, not the newer `/routing ospf-v3`. Also, queue trees might be used instead of simple queues in a service provider setup.

Wait, the subnet given is /28, which is 16 addresses. But SOHO with 639 users? That seems conflicting. Maybe the subnet is part of a larger network. Maybe the scenario has a typo, but I'll proceed as given, perhaps it's the core subnet.

In the QoS setup, maybe the queue tree was marking all traffic except web as low priority, but OSPF uses IP protocol 89, which wasn't included. So OSPF packets were getting dropped under congestion.

For the configuration before and after: Before, the mangle rule might not have OSPF marked. After, adding a rule to mark OSPF with high priority.

Also, in the logs, look for OSPF neighbor state changes. Maybe entries like "OSPF neighbor 192.168.127.130 changed state to Down" repeatedly.

Make sure to include CLI examples with comments, like marking OSPF packets in the firewall mangle.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF QoS Misconfiguration

## 1. Initial Problem Report and Symptoms
**Report**:  
"Multiple users report intermittent internet connectivity and VoIP call drops. Issues began after a recent QoS policy update."

**Symptoms**:  
- 639 users experiencing latency spikes (200ms+ during peak)  
- OSPF neighbor flapping observed on core routers  
- VoIP RTP streams marked as "low priority" in traffic logs  
- `/ip route` table shows missing OSPF routes periodically  

---

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  Core[Core Router (CR1)<br>192.168.127.129/28] --> Edge1[Edge Router (ER1)<br>192.168.127.130/28]
  Core --> Edge2[Edge Router (ER2)<br>192.168.127.131/28]
  Edge1 --> Customer1[Customer Network 1<br>10.10.1.0/24]
  Edge2 --> Customer2[Customer Network 2<br>10.10.2.0/24]
```

---

## 3. Initial Assessment Steps
1. **Verify OSPF neighbor status**:
```bash
/routing ospf neighbor print
# OUTPUT:
#  0 instance=default address=192.168.127.130 state="Full" router-id=1.1.1.1 
#  1 instance=default address=192.168.127.131 state="Exchange" router-id=2.2.2.2
```

2. **Check interface statistics**:
```bash
/interface ethernet monitor ether1
# OUTPUT:
#              status: link-ok
#       rate: 1Gbps-full
#  tx-drop: 1520
```

3. **Review QoS configuration**:
```bash
/queue tree print
# OUTPUT:
# 0 name="QoS-Policy" parent=global-in packet-mark=all_priority priority=1 
# 1 name="VoIP-High" parent=global-in packet-mark=voip priority=8
```

---

## 4. Detailed Debugging Process
**Step 1: Capture OSPF traffic**:
```bash
/tool sniffer quick protocol=89
# OUTPUT:
# 192.168.127.129 -> 224.0.0.5 OSPFv2 Hello 48  LOST 12/100 packets
```

**Step 2: Check firewall marks**:
```bash
/ip firewall mangle print
# BEFORE:
#  chain=forward action=mark-packet new-packet-mark=all_priority passthrough=no
#  (No OSPF-specific marking)
```

**Step 3: Verify QoS queue drops**:
```bash
/queue tree monitor QoS-Policy
# OUTPUT:
#   name: QoS-Policy
#   rate: 948Mbps
#   packet-drops: 1420
```

---

## 5. Key Findings & Root Cause
**Root Cause**:  
QoS policy (`all_priority` mark) applied to **global-in** queue without OSPF protocol exemption, causing:
- OSPF hello packets (IP protocol 89) deprioritized
- Queue drops during congestion (948Mbps/1Gbps utilization)
- OSPF neighbor relationships timing out

---

## 6. Solution Implementation
**Step 1: Create OSPF packet mark**:
```bash
/ip firewall mangle add
chain=prerouting protocol=ospf action=mark-packet 
new-packet-mark=ospf_high passthrough=no
```

**Step 2: Update QoS policy**:
```bash
/queue tree set QoS-Policy packet-mark=all_priority \
priority=1 burst-rate=100M burst-threshold=50M
/queue tree add name=OSPF-Priority parent=global-in \
packet-mark=ospf_high priority=7
```

---

## 7. Verification Process
**Check OSPF stability**:
```bash
/routing ospf neighbor print
# AFTER:
#  0 address=192.168.127.130 state="Full" 
#  1 address=192.168.127.131 state="Full"
```

**Monitor queue drops**:
```bash
/queue tree monitor OSPF-Priority
# OUTPUT:
#   packet-drops: 0
#   rate: 12Kbps
```

---

## 8. Prevention Measures
1. Test QoS policies in lab before deployment  
2. Add protocol-specific exceptions for routing traffic  
3. Implement monitoring alert for OSPF neighbor state changes:
```bash
/tool graphing interface add interface=ether1
```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf instance print` | Check OSPF instances |
| `/ip firewall mangle print where action=mark-packet` | View packet marks |
| `/queue tree export` | Export QoS configuration |

---

## 10. Common Pitfalls to Avoid
❌ **Mistake**: Applying blanket QoS policies without protocol exceptions  
✅ **Fix**: Always exempt routing protocol traffic (OSPF/BGP)  

❌ **Mistake**: Using `global-in` queue without burst control  
✅ **Fix**: Configure burst parameters for traffic spikes  

❌ **Mistake**: Assuming OSPF uses TCP/UDP ports  
✅ **Remember**: OSPF uses IP protocol 89 directly  
```
