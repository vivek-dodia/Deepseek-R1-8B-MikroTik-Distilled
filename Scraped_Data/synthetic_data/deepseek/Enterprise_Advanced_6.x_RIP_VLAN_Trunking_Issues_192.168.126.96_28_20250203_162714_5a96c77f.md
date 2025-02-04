---
generated_at: 2025-02-03T16:28:22.797362
topic: RIP
category: Routing
version: 6.x
scale: Enterprise
level: Advanced
subnet: 10.63.169.0/25
scenario: VLAN Trunking Issues
environment: Edge Location
affected_users: 516
duration: 15 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for RIP with VLAN trunking issues in an enterprise environment. Let me break down the user's requirements step by step.

First, the topic is RIP on RouterOS 6.x. The network scale is enterprise, so it's a larger setup. The subnet is 10.63.169.0/25, which is a /25, so that's 128 addresses. The environment is an edge location, which suggests this is a critical point connecting to external networks. The scenario is VLAN trunking issues affecting 516 users for 15 hours. 

The user wants sections from 1 to 10, each with specific details. Let me outline each section:

1. **Initial Problem Report and Symptoms**: Need to describe what users experienced—maybe connectivity issues between VLANs, RIP routes not propagating, high latency, packet loss. Mention that VLANs 10,20,30 are involved.

2. **Environment Description and Network Topology**: Use Mermaid. The edge router connects to core via VLAN trunk, and to access switches. Subnets are on different VLANs. Maybe a diagram showing EdgeRouter -> Core (VLAN trunk) -> Access switches with VLANs 10,20,30.

3. **Initial Assessment Steps**: Check interface status, VLAN configurations, RIP settings. Use commands like `/interface print`, `/interface vlan print`, `/routing rip interface print`.

4. **Detailed Debugging**: Check RIP neighbors, routing tables, packet captures. Commands like `/routing rip neighbor print`, `/ip route print`, use torch to capture traffic on VLAN interfaces. Look for missing routes or authentication issues.

5. **Key Findings and Root Cause**: Maybe VLAN tags not properly configured on RIP interfaces, causing routes not to be advertised. Or authentication mismatch between routers.

6. **Solution Implementation**: Correct VLAN settings on RIP interfaces, add authentication. Show before and after configs.

7. **Verification**: Check routes are present, test connectivity, monitor traffic.

8. **Prevention**: Regular audits, enable authentication, document VLAN-RIP mappings.

9. **Commands Reference**: List all commands used, like interface, routing, logging commands.

10. **Common Pitfalls**: Forgetting VLAN tags on RIP interfaces, auth mismatches, version mismatches.

Now, let's make sure each section has the necessary details. For example, in the initial problem report, users in different VLANs can't communicate. In the environment, the edge router uses VLAN trunking to connect to core. Maybe the RIP is configured on VLAN interfaces but without proper tags or authentication.

In the debugging process, when checking the RIP neighbors, if the VLAN interfaces aren't correctly tagged, the neighboring routers might not receive the RIP updates. Or perhaps the RIP version is different between devices. Also, checking if the VLAN trunk allows all necessary VLANs.

In the root cause analysis, maybe the RIP was configured on physical interfaces instead of VLAN interfaces, so the routes aren't being advertised over the trunk. Or the VLAN ID was misconfigured on one side, leading to mismatched tags.

The solution would involve reconfiguring RIP to use the VLAN interfaces, ensuring tags match, and setting up authentication if needed. Before configuration, RIP is on ether1; after, it's on VLAN interfaces like ether1.10 with correct tags.

Verification would involve checking the routing table for the expected routes, using ping between VLANs, and confirming RIP neighbors are established.

Prevention measures include ensuring RIP is on the correct interfaces, using authentication, and documenting network changes.

I need to include CLI commands with code blocks, like `/interface vlan add ...`, and show log outputs where relevant. For example, if there's a log entry about RIP authentication failure, that should be highlighted.

Also, common pitfalls: not enabling RIP on VLAN interfaces, forgetting to allow VLANs on the trunk port, or RIP version inconsistencies.

I should structure each section with headings, use bullet points where appropriate, and ensure that commands are properly formatted. Make sure the Mermaid diagram is correctly represented, showing the EdgeRouter connected to Core via a trunk with VLANs 10,20,30, and access switches connected to Core.

Double-check that all parts of the user's query are addressed, including the subnet, duration, number of users, and RouterOS version 6.x. Since it's 6.x, some commands might differ from later versions, so ensure accuracy there.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP VLAN Trunking Issues

## 1. Initial Problem Report and Symptoms
**Report**: 516 users at edge location report intermittent connectivity between VLANs 10/20/30. Outage duration: 15 hours.  
**Symptoms**:
- RIP routes flapping in routing table
- VLAN-tagged traffic not traversing trunk link
- 80% packet loss between 10.63.169.0/25 and other subnets
- RIP neighbors showing "passive" status unexpectedly

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    A[Edge Router (RB1100)] -->|VLAN Trunk (ether1)<br>802.1Q VLANs 10,20,30| B[Core Switch (CRS326)]
    B --> C[Access Switch 1 (VLAN10)]
    B --> D[Access Switch 2 (VLAN20)]
    B --> E[Access Switch 3 (VLAN30)]
```

## 3. Initial Assessment Steps
1. Verify physical interface status:
```bash
/interface print 
# Look for "ether1" status - showed "status=up"
```
2. Check VLAN interface configurations:
```bash
/interface vlan print 
# Output showed VLANs 10/20/30 created but no IP addresses assigned
```
3. Validate RIP interface participation:
```bash
/routing rip interface print 
# Output showed RIP enabled on physical ether1 instead of VLAN interfaces
```

## 4. Detailed Debugging Process
**Step 1: Verify RIP neighbor relationships**
```bash
/routing rip neighbor print
# Output showed 0 neighbors - unexpected for enterprise network
```

**Step 2: Capture RIP traffic on trunk**
```bash
/tool torch interface=ether1 port=520 
# Showed outgoing RIP v1 packets but core expects RIP v2
```

**Step 3: Check VLAN filtering**
```bash
/interface ethernet switch vlan print 
# CRS326 showed VLANs 10/20/30 allowed on trunk port
```

**Step 4: Analyze routing table**
```bash
/ip route print where protocol=rip 
# Only showed 2/15 expected routes
```

**Critical Log Evidence**:
```log
[15h ago] rip,error no enabled interfaces!
[14h ago] interface,error ether1: received packet with unknown VLAN ID 30
```

## 5. Key Findings & Root Cause
**Root Cause**:  
Dual misconfiguration:
1. RIP configured on physical interface (ether1) instead of VLAN interfaces
2. RIP version mismatch (v1 on edge vs v2 on core)

**Impact**:  
VLAN-tagged RIP updates were being dropped by core switch due to:
- Untagged RIP packets from physical interface
- Protocol version incompatibility

## 6. Solution Implementation
**Before (Faulty Config)**:
```bash
/routing rip interface add interface=ether1
```

**After (Correct Config)**:
```bash
/interface vlan
add interface=ether1 name=vlan10 vlan-id=10
add interface=ether1 name=vlan20 vlan-id=20
add interface=ether1 name=vlan30 vlan-id=30

/routing rip interface
remove [find interface=ether1]
add interface=vlan10 version=2
add interface=vlan20 version=2
add interface=vlan30 version=2
```

## 7. Verification Process
1. Confirm RIP neighbors:
```bash
/routing rip neighbor print 
# Now shows 3 neighbors with "up" state
```

2. Validate route propagation:
```bash
/ip route print where protocol=rip
# Shows 15 routes with "A" (active) flag
```

3. End-to-end test:
```bash
ping 10.63.169.65 source=10.63.169.1 interval=100ms count=100
# 0% packet loss observed
```

## 8. Prevention Measures
1. Implement configuration audit script:
```bash
:global checkRipVlan do={
    /routing rip interface print detail where interface~"vlan"
}
```
2. Enable RIP authentication:
```bash
/routing rip interface set [find] authentication=md5 authentication-key=securekey123
```

3. Standardize RIP version enterprise-wide:
```bash
/routing rip set redistribute-static=no redistribute-connected=no version=2
```

## 9. Related Commands Reference
| Purpose | Command |
|---------|---------|
| VLAN Check | `/interface vlan print` |
| RIP Status | `/routing rip interface print detail` |
| Neighbor Debug | `/routing rip neighbor print detail` |
| Packet Capture | `/tool torch interface=vlan10 port=520` |

## 10. Common Pitfalls to Avoid
1. **Mixing Physical and VLAN Interfaces**  
   Never run RIP on physical trunk interfaces - always use VLAN sub-interfaces

2. **Version Mismatch**  
   Ensure consistent RIP version configuration across all devices:
   ```bash
   /routing rip set version=2
   ```

3. **Missing VLAN Filtering**  
   Always validate switchport configuration:
   ```bash
   /interface ethernet switch vlan print
   ```

4. **Authentication Oversight**  
   Use MD5 authentication to prevent rogue route injection:
   ```bash
   /routing rip interface set [find] authentication=md5
   ```
```
