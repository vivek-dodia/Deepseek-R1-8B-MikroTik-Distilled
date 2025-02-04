---
generated_at: 2025-02-03T15:42:44.012265
topic: OSPF
category: Routing
version: 7.x
scale: Enterprise
level: Expert
subnet: 10.136.134.160/27
scenario: OSPF Adjacency Problems
environment: Campus Network
affected_users: 949
duration: 19 hours
---

# Analysis Process
Okay, let's tackle this MikroTik OSPF adjacency problem. First, I need to create a detailed troubleshooting scenario based on the user's query. Let me start by breaking down each section they want included.

1. **Initial Problem Report and Symptoms**: The user mentioned OSPF adjacency issues in a campus network affecting 949 users for 19 hours. Symptoms would include OSPF neighbors not forming, traffic not routing, maybe interface errors. I should think about common OSPF problems like mismatched areas, timers, network types, or authentication.

2. **Environment Description and Network Topology**: The subnet is 10.136.134.160/27. Campus network implies multiple routers, maybe a mix of L3 switches and MikroTik devices. Need to draw a simple Mermaid diagram with core, distribution, access layers, and the affected router.

3. **Initial Assessment Steps**: Start with checking OSPF status, neighbor tables, interface configurations, logs. Use commands like `/routing ospf neighbor print`, `/routing ospf interface print`, and look for errors in the logs.

4. **Detailed Debugging Process**: Here, I need to go step by step. Check OSPF configurations, verify areas, hello/dead timers, network types. Maybe authentication is misconfigured. Use commands to check each aspect, maybe enable OSPF debugging to see if hellos are being sent/received.

5. **Key Findings and Root Cause Analysis**: Suppose the root cause is mismatched MTU settings on the interfaces. MikroTik might have MTU 1500 while another vendor uses 1492, causing adjacency issues. Or maybe area mismatches, or passive interfaces.

6. **Solution Implementation Steps**: Adjust MTU settings, correct area configurations, ensure timers match. Update the OSPF configuration and restart the OSPF process if necessary.

7. **Verification Process**: Check OSPF neighbors again, ensure routes are propagated, test connectivity, monitor logs for any errors post-fix.

8. **Prevention Measures**: Implement configuration templates, consistent MTU across devices, regular audits, monitoring with tools like The Dude.

9. **Related Commands Reference**: List all commands used in the process, like checking neighbors, interfaces, logs, enabling debug, etc.

10. **Common Pitfalls to Avoid**: Mention MTU mismatches, area mismatches, passive interfaces, authentication errors, network type mismatches.

Wait, the user specified RouterOS 7.x. Need to ensure commands are compatible. For example, in ROS7, OSPF configuration might be under `/routing ospf` instead of older versions. Also, logging commands might differ.

Including before and after configurations is important. For example, before: OSPF interface with MTU 1500, after changing to 1492. Or before area 0, after correcting to area 0.1.2.3.

Log examples: When debugging, OSPF hello packets not being received due to MTU mismatch. Maybe show log entries indicating dropped packets.

CLI commands should be in code blocks, with comments explaining each. For example:

```bash
/routing ospf neighbor print
# Check OSPF neighbor status
```

For complex commands, like enabling debug logging:

```bash
/system logging add topics=ospf,!debug
# Enable OSPF logging excluding debug level
```

I need to structure each section clearly, using markdown headings. Ensure that the Mermaid diagram correctly represents the campus network with core, distribution, access layers, and the affected subnet.

Possible root causes: MTU mismatch, area ID mismatch (like using area 0 on one side and area 0.0.0.0 on another), network type (broadcast vs point-to-point), authentication parameters, or even passive interfaces not advertising routes.

In the debugging process, step through each possibility. Check neighbor states (down, init, 2-way, exstart, etc.), which can indicate where the problem is. For example, if stuck in exstart, it's often MTU issues.

Also, consider that in RouterOS, OSPF interfaces might have different configurations, like passive interfaces or incorrect network type. For example, if an interface is set to passive, it won't form adjacencies.

Another thing: the subnet is /27, which is a small subnet. Maybe the OSPF interfaces are on a VLAN with that subnet, and there's a misconfiguration in the VLAN settings or IP assignment.

Including log outputs like:

```
[admin@MikroTik] > /log print
00:00:00 ospf,error Could not form adjacency with 10.136.134.161: MTU mismatch
```

But need to mimic realistic log entries.

Prevention measures: Use standardized configs, document network changes, regular health checks, maybe implement BFD for faster detection.

Common pitfalls: Forgetting that OSPF requires matching parameters on both ends, not checking interface MTU, ignoring passive interface settings, not monitoring OSPF adjacencies.

Now, putting it all together in the specified format, making sure each section is covered with appropriate details and examples.

# Troubleshooting Guide
```markdown
# OSPF Adjacency Troubleshooting Scenario: Campus Network

## 1. Initial Problem Report and Symptoms
**Report**: Network team received alerts about intermittent connectivity between academic buildings.  
**Symptoms**:
- 949 users unable to access central resources
- OSPF neighbors flapping between "Full" and "Down" states
- Missing routes in OSPF LSDB
- Increased latency (300ms+) between core and distribution layers

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
  Core[Core Router (CR1)
  IP: 10.136.134.161/27
  Area 0.0.0.0] -->|Area 0.0.0.0| DistA[Distribution A (DA1)]
  Core -->|Area 0.0.0.0| DistB[Distribution B (DB1)]
  DistA -->|Area 0.0.0.1| Access1[Access Switch 1]
  DistA -->|Area 0.0.0.1| Access2[Access Switch 2]
  DistB -->|Area 0.0.0.1| Access3[Access Switch 3]
  classDef router fill:#f9f,stroke:#333;
  classDef switch fill:#ccf,stroke:#333;
  class Core,DistA,DistB router
  class Access1,Access2,Access3 switch
```

## 3. Initial Assessment Steps
1. Check OSPF neighbor status:
```bash
/routing ospf neighbor print
# Output:
# 0 instance=default address=10.136.134.162 state="Full" router-id=10.255.255.2 
# 1 instance=default address=10.136.134.163 state="Init" router-id=10.255.255.3
```

2. Verify interface status:
```bash
/interface ethernet print 
# Flags: X - disabled, R - running
#  0  R name="ether1-core" mtu=1500
```

3. Check OSPF logs:
```bash
/log print where message~"OSPF"
# Output:
# 13:45:23 ospf,error,neighbor 10.136.134.163: Dead timer expired
```

## 4. Detailed Debugging Process
**Step 1: Verify OSPF Configuration**
```bash
/routing ospf instance print
# instance=default router-id=10.255.255.1 disabled=no

/routing ospf area print
# area=0.0.0.0 instance=default
# area=0.0.0.1 instance=default

/routing ospf interface-template print
# 0 interface=ether1-core area=0.0.0.0 type=ptp
```

**Step 2: Check MTU Mismatch**
```bash
/interface print where name="ether1-core"
# mtu=1500 actual-mtu=1500

# On neighboring Cisco device:
# interface GigabitEthernet0/1
#  ip mtu 1492
```

**Step 3: Analyze Packet Capture**
```bash
/tool sniffer quick interface=ether1-core protocol=ospf
# OSPF Header Analysis:
# - MTU in DD packets: 1492 (neighbor) vs 1500 (local)
```

**Step 4: Verify Authentication**
```bash
/routing ospf interface-template print
# 0 authentication=md5 authentication-key-id=1
# On Cisco neighbor: authentication=sha1
```

## 5. Key Findings & Root Cause
**Root Cause**: MTU mismatch (1500 vs 1492) combined with MD5/SHA1 authentication mismatch causing OSPF adjacency failures.  
**Supporting Evidence**:
- Dead timer expiration logs
- Packet capture showing mismatched MTU in Database Description packets
- Authentication type mismatch in configuration

## 6. Solution Implementation
1. Standardize MTU on backbone links:
```bash
/interface ethernet set ether1-core mtu=1492
```

2. Align authentication configuration:
```bash
/routing ospf interface-template set 0 authentication=sha1
```

3. Update OSPF timers:
```bash
/routing ospf interface-template set 0 dead-interval=40 hello-interval=10
```

## 7. Verification Process
1. Confirm neighbor adjacency:
```bash
/routing ospf neighbor print
# 0 address=10.136.134.163 state="Full"
```

2. Validate route propagation:
```bash
/ip route print where protocol=ospf
# 0 dst-addr=10.136.135.0/24 gateway=10.136.134.163
```

3. Check interface statistics:
```bash
/interface monitor-traffic ether1-core
# rx-packets: 1234/s, tx-packets: 1230/s
```

## 8. Prevention Measures
1. Implement configuration standardization:
```bash
/system script add name="OSPF Baseline" source={...}
```

2. Enable proactive monitoring:
```bash
/tool graphing interface add interface=ether1-core
```

3. Establish change control process for network modifications

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Show adjacency status |
| `/routing ospf lsa print` | View LSDB contents |
| `/interface monitor-traffic [interface]` | Real-time traffic analysis |
| `/tool sniffer quick protocol=ospf` | OSPF packet capture |

## 10. Common Pitfalls to Avoid
1. **MTU Inconsistencies**:
   - Always verify `ip mtu` vs `mtu` settings
   - Check for jumbo frames on backbone links

2. **Authentication Mismatches**:
   ```bash
   # Bad practice
   /routing ospf interface-template set 0 authentication=md1
   # Good practice
   /routing ospf interface-template set 0 authentication=sha256
   ```

3. **Area Type Confusion**:
   - Use dotted notation (0.0.0.0) instead of decimal (0)

4. **Passive Interface Misconfiguration**:
   ```bash
   # Incorrect
   /routing ospf interface-template set 0 passive=yes
   # Correct
   /routing ospf interface-template set 0 passive=no
   ```
```
