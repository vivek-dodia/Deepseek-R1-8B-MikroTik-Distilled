---
generated_at: 2025-02-03T16:54:21.849739
topic: Static Routes
category: Routing
version: 6.x
scale: SOHO
level: Expert
subnet: 10.80.101.128/25
scenario: QoS Misconfiguration
environment: Service Provider Core
affected_users: 671
duration: 5 hours
---

# Analysis Process
Okay, let me try to work through this MikroTik RouterOS troubleshooting scenario. The user wants a detailed scenario focused on static routes in a SOHO network with a specific subnet, version 6.x, and QoS misconfiguration affecting 671 users over 5 hours. 

First, I need to outline the initial problem report. The symptoms mentioned are high latency and packet loss. Since the affected users are 671, that's a significant number for a SOHO setup, which usually is small office/home office. Wait, maybe the environment is a Service Provider Core, which might handle more users. The subnet is 10.80.101.128/25, so that's a /25 subnet, which gives 128 addresses. But 671 users might be on multiple subnets? Or maybe it's a typo. Hmm, maybe the scenario is that the SOHO router is part of a larger Service Provider Core. Need to clarify the network topology.

For the environment description, they want a Mermaid diagram. Let me think about the network structure. The SOHO router is connected to the Service Provider Core. The SOHO's LAN is 10.80.101.128/25, and there's a default route to the ISP. But there's a QoS misconfiguration. Maybe the static routes are correct, but QoS policies are affecting traffic.

Initial assessment steps: Check interface status, routes, QoS settings. Use commands like /interface print, /ip route print, /queue tree print.

Debugging process: Check if static routes are correct. Verify the default route exists. Then check QoS. Maybe a queue tree or simple queue is misconfigured, marking traffic incorrectly or applying limits to the wrong interface. In RouterOS 6.x, queue trees are used for hierarchical QoS. If a static route is pointing traffic through an interface that's being shaped by QoS incorrectly, that could cause latency and packet loss.

Key findings: Maybe a queue intended for another subnet was applied to the SOHO's LAN interface, causing bandwidth throttling. Or a misapplied parent queue that's limiting the entire WAN interface.

Solution: Correct the queue tree to apply QoS policies to the correct interfaces or subnets. Update the static routes if necessary, but the problem is QoS, so adjusting queue configurations.

Verification: Check latency with ping, monitor traffic with Torch, check queue stats.

Prevention: Use comments in queues, regular audits, testing changes in off-hours.

Common pitfalls: Assuming static routes are the issue without checking QoS, not verifying queue parameters, incorrect parent interfaces.

Now, putting this into the structure specified. Need to include CLI commands with code blocks. For example, checking routes with /ip route print, looking for the default route. Then checking queue trees with /queue tree print. Maybe a queue was applied to the WAN interface (ether1) as a parent, but with a rate limit too low, causing congestion.

Log examples: Maybe logs showing queue drops, or interface statistics showing high utilization.

Before configuration: a queue tree with parent=global-in or parent=ether1 with a limited rate. After changing the parent or increasing the rate.

Including all the sections, ensuring each part is covered. Need to make sure the scenario flows logically from problem report to resolution.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting: Static Routes & QoS Misconfiguration

## 1. Initial Problem Report and Symptoms
**Report:**  
Service Provider NOC receives multiple complaints from SOHO users (671 affected) about high latency (>500ms) and 30% packet loss to core services. Issues persist for 5 hours post a recent QoS policy update.

**Symptoms:**
- Intermittent connectivity to `10.80.101.128/25` subnet
- VoIP call drops and video conferencing failures
- Asymmetric routing observed in traceroutes

---

## 2. Environment Description & Topology
```mermaid
graph TD
  SP_Core[Service Provider Core Router] -->|MPLS| SOHO_RTR[SOHO Router]
  SOHO_RTR -->|ether1 (WAN: 192.168.100.1/30)| SP_Core
  SOHO_RTR -->|ether2 (LAN: 10.80.101.129/25)| SOHO_SWITCH[SOHO Switch]
  SOHO_SWITCH --> USER1[User PC 10.80.101.130]
  SOHO_SWITCH --> USER2[User PC 10.80.101.131]
```

---

## 3. Initial Assessment Steps
1. **Verify Interface Status:**
   ```bash
   /interface print
   ```
   **Output:**  
   ```
   NAME    TYPE       MTU  RX-BYTE     TX-BYTE
   ether1  ethernet   1500 12.4GiB     8.2GiB
   ether2  ethernet   1500 3.1GiB      15.7GiB
   ```

2. **Check Static Routes:**
   ```bash
   /ip route print
   ```
   **Output:**  
   ```
   # DST-ADDRESS       GATEWAY         DISTANCE
   0 0.0.0.0/0        192.168.100.2   1
   1 10.80.101.128/25 ether2          1
   ```

3. **Review QoS Policies:**
   ```bash
   /queue tree print
   ```

---

## 4. Detailed Debugging Process
**Step 1:** Check QoS Queue Tree Configuration
```bash
/queue tree print where name="QoS-LAN"
```
**Output (Before):**
```
0 name="QoS-LAN" parent=ether1 packet-mark=all-limit rate=10M burst=100k
```

**Step 2:** Verify Traffic Flow
```bash
/tool torch interface=ether1
```
**Observation:** WAN interface (`ether1`) shows 95% utilization despite 1Gbps link.

**Step 3:** Analyze Packet Marks
```bash
/ip firewall mangle print
```
**Output:** No packet marks applied to prioritize traffic.

---

## 5. Key Findings & Root Cause
**Root Cause:**  
A misconfigured QoS queue tree (`QoS-LAN`) was bound to the WAN interface (`ether1`) with a 10M rate limit, throttling **all traffic** to/from the SOHO subnet. Static routes were correct, but QoS overrode bandwidth availability.

---

## 6. Solution Implementation
1. **Adjust QoS Rate Limit:**
   ```bash
   /queue tree set [find name="QoS-LAN"] rate=1G
   ```
2. **Add Priority Rules for VoIP:**
   ```bash
   /ip firewall mangle add chain=forward protocol=udp dst-port=5060,10000-20000 action=mark-packet new-packet-mark=voip passthrough=no
   /queue tree add name="QoS-VoIP" parent=ether1 packet-mark=voip priority=1
   ```

---

## 7. Verification Process
1. **Latency Test:**
   ```bash
   /ping 10.80.101.130 count=10
   ```
   **Output:**  
   ```
   seq=3 time=15ms
   seq=4 time=12ms
   ```

2. **QoS Stats Check:**
   ```bash
   /queue tree monitor QoS-LAN
   ```
   **Output:**  
   ```
   rate: 950Mbps (previously 10Mbps)
   ```

---

## 8. Prevention Measures
- Use descriptive names for QoS policies (e.g., `QoS-LAN-Throttle`).
- Test QoS changes in a maintenance window.
- Implement monitoring for interface utilization (`/tool graphing`).

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/ip route print` | List static routes |
| `/queue tree print` | Show QoS policies |
| `/tool torch` | Real-time traffic analysis |

---

## 10. Common Pitfalls to Avoid
- Binding QoS to the wrong interface (e.g., WAN instead of LAN).
- Using `parent=global` instead of a specific interface.
- Forgetting to remove debug rules after testing.
```
