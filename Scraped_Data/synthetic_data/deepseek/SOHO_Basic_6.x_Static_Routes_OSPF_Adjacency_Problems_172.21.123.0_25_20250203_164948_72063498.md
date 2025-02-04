---
generated_at: 2025-02-03T16:51:45.474947
topic: Static Routes
category: Routing
version: 6.x
scale: SOHO
level: Basic
subnet: 192.168.136.128/25
scenario: OSPF Adjacency Problems
environment: Service Provider Core
affected_users: 578
duration: 18 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF Adjacency Problems in a SOHO environment with specific parameters. Let's break down each section step by step.

First, the initial problem report and symptoms. The user mentioned that 578 users are affected over 18 hours. So the symptoms should reflect a complete loss of connectivity, maybe BGP prefixes not being received because OSPF is down. The core router can't form OSPF adjacency with the edge router. Also, static routes might not be redistributed properly.

Next, the environment description and network topology. The subnet is 192.168.136.128/25, which is a /25 subnet. Since it's a SOHO network, the topology might be simple: a core router connected to an edge router, with the edge connected to the service provider. The core router has a static default route pointing to the edge. Maybe OSPF is used between core and edge for dynamic routing. I'll need to represent this in Mermaid format. Let me sketch that out.

For the initial assessment steps, the admin would check OSPF neighbors, interfaces, routes, and logs. Commands like `/routing ospf neighbor print` and `/ip route print` would be relevant here. Also, checking OSPF configuration and interface status.

Detailed debugging process: Start by verifying OSPF configuration on both routers. Check area IDs, network statements, authentication. Then look at interface settings—MTU mismatches are a common issue. Use commands to check interface MTU and compare. Then check OSPF authentication. If there's a password mismatch, that would prevent adjacency. Use `log print` to find authentication failures. Also, static route redistribution into OSPF—maybe the core isn't advertising the static default route because of a missing redistribute rule.

Key findings and root cause analysis: Probably MTU mismatch and missing redistribution configuration. Maybe authentication wasn't set on both ends. The static route wasn't being advertised because OSPF wasn't configured to redistribute static routes.

Solution implementation: Adjust MTU on the interfaces to match, add authentication, and fix the OSPF redistribution configuration. Show before and after config snippets.

Verification process: Check OSPF neighbors again, ensure routes are present, test connectivity. Commands like `/routing ospf neighbor print` and `/ip route print`.

Prevention measures: Standardize configurations, implement monitoring for OSPF adjacencies, documentation. Maybe use scripts to check settings automatically.

Related commands reference: List all the commands used in each section, like OSPF neighbor print, route print, etc.

Common pitfalls: MTU mismatches, authentication mismatches, forgetting to redistribute routes, area ID mismatches.

I need to make sure each section is covered with the right details. Also, include CLI commands in code blocks, add comments where necessary, and maybe some example log outputs. For example, when authentication fails, the logs might show a message about OSPF packet drop due to bad password.

Wait, the static route subnet is 192.168.136.128/25. So the network between core and edge is part of that subnet? Let me make sure the IP addresses in the topology are correctly assigned. The core router's interface might be 192.168.136.129, edge is 192.168.136.130, and the edge has a static default route to the ISP gateway. The core has a static route to edge for the default, and OSPF should redistribute that into the service provider's network? Or maybe the OSPF is between core and edge, and the static route is on the edge towards the ISP.

Hmm. The environment is a service provider core, which might mean the edge router is connected to the broader service provider network. But since it's SOHO, maybe the setup is smaller. The static routes could be on the core router, pointing to the edge, and OSPF is used between core and edge to share routes. But if OSPF adjacency is down, the core can't get routes from the edge, so the static route isn't being redistributed properly.

Also, in the problem scenario, the core can't form adjacency with the edge. So users connected to the core can't reach the internet through the edge. The static route on the core would be a default route via the edge's IP. But if OSPF is supposed to redistribute that static route into OSPF, maybe the edge isn't advertising it because redistribution isn't set up. Wait, but the main issue is OSPF adjacency. Without adjacency, no routes are exchanged. So the initial problem is adjacency down, leading to no route redistribution.

So the static route on the core is a default route via the edge. But if OSPF is not working, maybe that static route is still present, but other routes via OSPF are missing. Wait, maybe the service provider core uses OSPF to distribute routes, and the edge is supposed to advertise the static default route into OSPF. But if adjacency is down, that doesn't happen. So the core isn't receiving the default route via OSPF, but has a static default route. But maybe the static route is not configured correctly, leading to the outage. Or perhaps the static route is correct, but without OSPF adjacency, other routes are missing.

Wait, the scenario says "Static Routes" as the topic, but the problem is OSPF adjacency. Maybe the static routes are being redistributed into OSPF, but because adjacency is down, those routes aren't being advertised. So the core router has a static route that should be advertised via OSPF to the edge, but since adjacency is down, the edge doesn't receive it. Alternatively, the edge has a static route that's supposed to be advertised via OSPF to the core.

Hmm. The user's main issue is OSPF adjacency problems in a SOHO environment, but the topic is static routes. So perhaps the problem is that static routes are not being redistributed into OSPF, which could be part of the adjacency issue. Or maybe the static routes are configured but OSPF isn't forming adjacency, so the routes aren't being exchanged. So the root cause could be both adjacency issues (like MTU, auth) and static route redistribution configuration.

In the detailed debugging process, after fixing adjacency issues, they find that the static route isn't being advertised because redistribution isn't set. So the solution would involve both fixing adjacency (MTU, auth) and configuring OSPF to redistribute static routes.

Also, in the initial problem report, the static route might be present but not being redistributed because OSPF is down. So users lose connectivity because the core isn't getting necessary routes via OSPF.

I need to structure the debugging steps to first resolve the adjacency problem, then check route redistribution. For example, after fixing MTU and authentication, the adjacency comes up, but the static route still isn't in the routing table because redistribution isn't enabled. Then they adjust the OSPF configuration to redistribute static routes.

So key findings would include both MTU mismatch and missing OSPF redistribution configuration. Root cause analysis would explain how these two issues together caused the problem.

In the example configurations, before and after, the OSPF setup on the core might lack the redistribute-static option, and after it's added. Also, interface MTU settings and authentication settings are adjusted.

Log examples might show OSPF state transitions, authentication errors, etc.

I need to make sure all these elements are included in each section. Let me start drafting each part with these points in mind.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF Adjacency Problems

## 1. Initial Problem Report and Symptoms
- **Report**: 578 users report complete WAN/internet outage for 18 hours.
- **Symptoms**:
  - Core router fails to establish OSPF adjacency with edge router.
  - Static default route (`0.0.0.0/0`) missing from routing table.
  - BGP prefixes from service provider not received.
  - Ping tests fail between core (192.168.136.129) and edge (192.168.136.130).

## 2. Environment Description
- **Network Scale**: SOHO (Small Office/Home Office)
- **Subnet**: 192.168.136.128/25 (Usable IPs: 192.168.136.129 - 192.168.136.254)
- **Topology**:
```mermaid
graph TD
  Core[Core Router (MikroTik RB1100)] -->|OSPF Area 0<br>192.168.136.129/25| Edge[Edge Router (MikroTik RB760)]
  Edge -->|Static Route 0.0.0.0/0<br>ISP Gateway 203.0.113.1| ISP[Service Provider]
```

## 3. Initial Assessment Steps
1. Check OSPF neighbor status:
   ```bash
   /routing ospf neighbor print
   # Output: 
   #   state="Full" (Expected)
   #   Actual: state="Down"
   ```
2. Verify static route presence:
   ```bash
   /ip route print where dst-address=0.0.0.0/0
   # Output: 0 routes found
   ```
3. Check interface status:
   ```bash
   /interface print 
   # Confirmed ether1 (Core-Edge link) is "running"
   ```

## 4. Detailed Debugging Process
### Step 1: Verify OSPF Configuration
```bash
/routing ospf instance print
# Instance: area-id=0.0.0.0, router-id=192.168.136.129

/routing ospf network print
# Network: 192.168.136.128/25 area=backbone
```

### Step 2: Check Interface MTU Mismatch
```bash
/interface ethernet print 
# Core: ether1 mtu=1500
# Edge: ether1 mtu=1492 (PPPoE default)
```

### Step 3: Investigate OSPF Authentication
```bash
/routing ospf interface-template print
# Core: auth=sha1, auth-key=!secret123
# Edge: auth=none (Mismatch)
```

### Step 4: Verify Route Redistribution
```bash
/routing ospf redistribution print
# Missing static route redistribution rule
```

## 5. Key Findings & Root Cause
- **MTU Mismatch**: Core (1500) vs Edge (1492) caused packet fragmentation.
- **Authentication Mismatch**: SHA1 enabled on core but not edge.
- **Missing Redistribution**: Static route not advertised via OSPF.
- **Root Cause**: Combination of MTU mismatch and authentication failure blocked OSPF adjacency formation.

## 6. Solution Implementation
### Before (Edge Router Config):
```bash
/interface ethernet set ether1 mtu=1492
/routing ospf interface-template add interface=ether1 area=backbone
```

### After (Corrected Config):
```bash
/interface ethernet set ether1 mtu=1500
/routing ospf interface-template set 0 auth=sha1 auth-key=!secret123
/routing ospf redistribution add redistribute=static
```

## 7. Verification Process
1. Confirm OSPF adjacency:
   ```bash
   /routing ospf neighbor print
   # state=Full, address=192.168.136.130
   ```
2. Validate route propagation:
   ```bash
   /ip route print
   # 0.0.0.0/0 via 192.168.136.130 (OSPF)
   ```
3. End-to-end test:
   ```bash
   ping 8.8.8.8 count=5
   # 5 packets transmitted, 5 received
   ```

## 8. Prevention Measures
- Standardize MTU (1500) across all OSPF interfaces
- Implement configuration templates for OSPF authentication
- Enable OSPF logging:
  ```bash
  /system logging add topics=ospf
  ```
- Schedule weekly adjacency checks via script:
  ```bash
  :global ospfStatus [/routing ospf neighbor get [find] state]
  :if ($ospfStatus != "Full") do={ :log warning "OSPF Adjacency Down!" }
  ```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Check adjacency status |
| `/interface monitor ether1` | Verify interface metrics |
| `/log print where message~"OSPF"` | Filter OSPF-related logs |
| `/ip route export` | Show complete routing table |

## 10. Common Pitfalls to Avoid
- **MTU Mismatches**: Always verify on both ends of OSPF links
- **Silent Authentication Failures**: Use explicit `auth=none` if not using authentication
- **Area ID Mismatches**: Ensure all interfaces are in the same OSPF area
- **Redistribution Loops**: Use route filters when redistributing static/BGP routes
```
