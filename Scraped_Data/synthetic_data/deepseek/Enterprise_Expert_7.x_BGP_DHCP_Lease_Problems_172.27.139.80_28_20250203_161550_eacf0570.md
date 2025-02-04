---
generated_at: 2025-02-03T16:17:01.210366
topic: BGP
category: Routing
version: 7.x
scale: Enterprise
level: Expert
subnet: 10.135.213.0/27
scenario: DHCP Lease Problems
environment: Multi-tenant Building
affected_users: 206
duration: 19 hours
---

# Analysis Process
Okay, so I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP in a multi-tenant building with DHCP lease problems affecting 206 users over 19 hours. Let me break this down step by step.

First, the initial problem report. Users can't get IP addresses via DHCP. Symptoms include lease exhaustion, maybe some BGP routes missing? Since it's an enterprise network with BGP, there might be multiple tenants each with their own subnets. The subnet given is 10.135.213.0/27, which is a small subnet—only 30 usable addresses. Wait, 206 users but a /27? That's only 30 IPs. That doesn't add up. Maybe the DHCP server is supposed to handle multiple subnets via BGP or something else. Oh, maybe the DHCP server is misconfigured, and BGP is involved in routing these subnets to different tenants. If BGP isn't advertising the routes correctly, maybe DHCP relays aren't working, so clients can't reach the DHCP server. Or maybe the DHCP server's subnet isn't being routed properly due to BGP issues.

Environment: Multi-tenant building. Network topology would have a core router running BGP, connected to multiple edge switches or routers for each tenant. The core router peers with other BGP routers, maybe in a data center or other buildings. The subnet 10.135.213.0/27 is part of one of the tenant networks. But wait, if it's a /27, how can there be 206 users? That's the puzzle. Maybe the DHCP server is supposed to assign addresses from multiple subnets, but due to a BGP misconfiguration, only this /27 is being used, leading to exhaustion. Or maybe the DHCP server is using a larger pool, but BGP isn't advertising the correct routes, so all clients are getting stuck on this small subnet.

Initial assessment steps: Check DHCP lease count, check BGP neighbors, verify routes in the routing table. Use commands like `/ip dhcp-server lease print`, `/routing bgp peer print`, `/ip route print`. Also check logs for DHCP events and BGP state changes.

Debugging process: Look into DHCP server configuration—maybe the address pool is set to 10.135.213.0/27, which is too small. But why is that the case? Maybe a misconfiguration where the pool was supposed to be a larger subnet. Also check BGP advertisements—if the DHCP server is in a different subnet, and BGP isn't advertising the route to that subnet, then DHCP requests might not reach the server. Or if the server is handing out addresses from a subnet that isn't properly advertised via BGP, clients can't communicate beyond their local network.

Key findings: Perhaps the DHCP server's pool was incorrectly set to /27 instead of a larger subnet. Additionally, BGP wasn't advertising the correct subnet because of a wrong network statement in the BGP configuration. So even if the DHCP server tried to assign addresses from a larger pool, the routes weren't being advertised, leading to connectivity issues after obtaining an IP. Wait, but the main issue is DHCP lease problems. Maybe the DHCP server ran out of addresses because the pool was too small. But 206 users—so maybe the DHCP server is supposed to use multiple subnets, but BGP wasn't advertising them, so all DHCP requests were being served from the single /27 subnet, exhausting it.

Root cause: The DHCP server's address pool was misconfigured with a /27 instead of a larger subnet, and BGP wasn't configured to advertise the correct network, causing both lease exhaustion and routing issues.

Solution: Correct the DHCP pool to a larger subnet (like /24) and ensure BGP is advertising that subnet. Also, check any DHCP relay configurations if the server is centralized.

Verification: After changing the pool, check leases again, confirm BGP routes are present in the routing table and advertised to peers. Test DHCP requests from a client.

Prevention: Regular audits of DHCP and BGP configurations, monitoring lease usage, and using subnetting best practices.

Common pitfalls: Not checking BGP advertisements, assuming DHCP is only a local issue without considering routing, misconfiguring subnet masks.

Now, how to structure all this into the required sections with CLI commands, logs, etc. Need to include example commands like checking BGP peers, looking at DHCP leases, examining routes. Maybe show before and after configurations for the DHCP server and BGP network statements.

For example, the initial DHCP config might have `add name=dhcp-pool ranges=10.135.213.2-10.135.213.30` which is only 29 addresses. After correction, it's `ranges=10.135.213.2-10.135.213.254` with a subnet mask of /24. And in BGP configuration, the network statement was missing or set to /27, now corrected to /24.

Logs might show DHCP lease exhaustion messages, and BGP logs showing that the correct network is being advertised after the fix.

# Troubleshooting Guide
```markdown
# BGP Troubleshooting Scenario: DHCP Lease Problems in Multi-Tenant Building

## 1. Initial Problem Report and Symptoms
**Report**: 206 users across multiple tenants report inability to obtain IP addresses.  
**Symptoms**:
- `DHCPDISCOVER` requests unanswered
- 100% utilization of 10.135.213.0/27 pool
- Intermittent BGP route fluctuations in routing table
- Affected tenants isolated from core services

---

## 2. Environment Description & Network Topology

```mermaid
graph TD
  Core[Core Router (BGP AS 65530)] -->|iBGP| DC[Data Center Router]
  Core -->|eBGP| ISP[ISP Edge Router]
  Core -->|VRF Tenants| SW1[Tenant Switch 1]
  Core -->|VRF Tenants| SW2[Tenant Switch 2]
  SW1 -->|VLAN 100| CL1[Client Group 1]
  SW2 -->|VLAN 200| CL2[Client Group 2]
  DHCP[(DHCP Server)] --> Core
```

**Key Components**:
- RouterOS v7.12
- 8 BGP peers (4 iBGP, 4 eBGP)
- VRF-lite segmentation for tenants
- Centralized DHCP server with relay agents

---

## 3. Initial Assessment Steps

1. **Verify DHCP Server Status**:
```bash
/ip dhcp-server print
# Status: running
# Address Pool: 10.135.213.0/27 (30 addresses)
```

2. **Check Lease Utilization**:
```bash
/ip dhcp-server lease print count-only 
# 30 active leases (100% utilized)
```

3. **BGP Peer Status**:
```bash
/routing bgp peer print 
# 2/8 peers in 'established' state
```

4. **Route Validation**:
```bash
/ip route print where dst-address=10.135.213.0/27
# No BGP routes found, only connected
```

---

## 4. Detailed Debugging Process

**Step 1: Capture DHCP Debug Logs**
```bash
/log print where message~"DHCP"
# Sample output:
# 00:12:45 dhcp,error no free leases for subnet 10.135.213.0/27
```

**Step 2: Verify BGP Network Advertisements**
```bash
/routing bgp network print
# Missing 10.135.213.0/24 network (expected advertisement)
```

**Step 3: Check Route Filters**
```bash
/routing filter print
# Overly aggressive filter blocking /24 advertisements:
# rule: if (dst==10.135.213.0/27) accept else reject
```

**Step 4: Validate VRF Assignments**
```bash
/ip vrf print 
# DHCP relay interface assigned to incorrect VRF (main instead of tenant-vrf)
```

---

## 5. Key Findings & Root Cause

**Findings**:
1. DHCP pool configured as /27 instead of required /24
2. BGP route filter blocking larger subnet advertisements
3. DHCP relay operating in wrong VRF
4. BGP peer instability due to MTU mismatch

**Root Cause**:  
Incorrect subnet mask (/27) combined with restrictive BGP route filters prevented proper DHCP pool scaling and network advertisement, exacerbated by VRF misconfiguration isolating DHCP traffic.

---

## 6. Solution Implementation

**Step 1: Correct DHCP Pool**
```bash
/ip pool set [find name="tenant-pool"] ranges=10.135.213.2-10.135.213.254
```

**Step 2: Update BGP Network Advertisement**
```bash
/routing bgp network add network=10.135.213.0/24
```

**Step 3: Fix Route Filters**
```bash
/routing filter set [find where comment~"tenant-subnet"] \
chain=bgp-out rule="dst==10.135.213.0/24 accept"
```

**Step 4: Correct VRF Assignment**
```bash
/ip dhcp-relay set [find interface=ether5] vrf=tenant-vrf
```

---

## 7. Verification Process

1. Confirm DHCP Lease Distribution:
```bash
/ip dhcp-server lease print count-only 
# 206 active leases (now using /24 space)
```

2. Validate BGP Advertisements:
```bash
/routing bgp advertisements print 
# Showing 10.135.213.0/24 to all peers
```

3. Test End-to-End Connectivity:
```bash
/ping 10.135.213.150 src-address=10.135.213.1
# 5 packets transmitted, 5 received
```

---

## 8. Prevention Measures

1. Implement DHCP threshold alerts:
```bash
/tool bandwidth-server set dhcp alert=90%
```

2. Enable BGP Route Monitoring:
```bash
/routing bgp log-updown=yes log-status-changes=yes
```

3. Regular Configuration Audits:
```bash
/system script add name=config-audit source="/export compact show-sensitive"
```

---

## 9. Related Commands Reference

| Command | Purpose |
|---------|---------|
| `/ip dhcp-server lease print` | List active DHCP leases |
| `/routing bgp peer monitor [peer]` | Real-time BGP peer monitoring |
| `/ip route monitor [regexp.*BGP.*]` | Track BGP route changes |

---

## 10. Common Pitfalls to Avoid

1. **Subnet Mask Mismatch**: Ensure DHCP pool matches BGP-advertised networks
2. **VRF Leakage**: Confirm DHCP relay interfaces are in correct VRFs
3. **Silent Filter Drops**: Test route filters with `/routing filter test`
4. **MTU Inconsistencies**: Verify `ipv6-bgp-mtu` matches physical interfaces
```

**After Configuration Snippet**:
```bash
# DHCP Server
/ip pool set [find] name=tenant-pool ranges=10.135.213.2-10.135.213.254

# BGP Network
/routing bgp network add network=10.135.213.0/24

# VRF Assignment
/ip dhcp-relay set [find] vrf=tenant-vrf
```
