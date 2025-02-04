---
generated_at: 2025-02-03T19:50:33.768758
topic: OSPF
category: Routing
version: 6.x
scale: SOHO
level: Basic
subnet: 10.197.145.64/27
scenario: DHCP Lease Problems
environment: Industrial Network
affected_users: 475
duration: 23 hours
---

# Analysis Process
Okay, let's tackle this MikroTik OSPF troubleshooting scenario. The user wants a detailed setup for a SOHO industrial network with DHCP lease issues affecting 475 users over 23 hours. First, I need to make sure I cover all the required sections: problem report, environment, initial steps, debugging, root cause, solution, verification, prevention, commands, and pitfalls.

Starting with the Initial Problem Report. Symptoms mentioned are DHCP lease problems. So, users can't get IPs, maybe intermittent connectivity. Since it's an industrial network, maybe some specific devices involved. 475 users on a /27 subnet? Wait, a /27 is only 30 usable addresses. That can't be right. Oh, maybe that's a typo, but the user specified 10.197.145.64/27. That's a problem. 475 users on a /27 subnet? That's impossible. So the root cause could be the subnet size being too small, leading to DHCP exhaustion. But how does OSPF play into this? Maybe OSPF is misconfigured, causing routes not to propagate, leading to DHCP server being unreachable? Or maybe the DHCP server is on another subnet and OSPF isn't advertising the route properly.

Environment: SOHO industrial network. Let me think of a simple topology. Maybe two routers connected via OSPF. The DHCP server is on one subnet, clients on another. But if the subnet is /27, that's only 30 IPs. 475 users would need multiple subnets. Maybe the actual setup uses multiple VLANs or subnets, but the DHCP server is supposed to handle multiple scopes. Wait, but the problem is DHCP lease issues. If the subnet is too small, DHCP leases can't be assigned. So maybe the initial configuration has a /27 subnet, leading to DHCP pool exhaustion. But why would OSPF be involved? Perhaps the DHCP server is in a different subnet, and OSPF isn't properly advertising the route, so DHCP requests aren't reaching the server. Or maybe the OSPF configuration is causing the router interfaces to not be up, so DHCP can't function.

Wait, maybe the user intended a larger subnet but misconfigured it as /27. So the DHCP server has a small pool, leading to all leases being used up. But 475 users can't fit in a /27. That seems like a key point. But how does OSPF tie into this? Maybe OSPF is used to connect different parts of the network, and a misconfiguration is causing the DHCP server's network to not be advertised, so clients can't reach the DHCP server. Alternatively, maybe OSPF is causing routing loops or adjacencies not forming, leading to connectivity issues that affect DHCP.

In the network topology, the SOHO setup might have a few routers. Let's sketch a Mermaid diagram. Maybe Router1 connected to Router2 via OSPF. Router1 has the DHCP server on 10.197.145.64/27, and Router2 connects to clients. But if the subnet is too small, that's a problem. Alternatively, maybe the DHCP server is on a different subnet, and OSPF is supposed to route between them, but isn't.

Initial Assessment Steps: Check DHCP leases, check OSPF neighbors, verify routes. Look at the DHCP server configuration. Check if the pool is exhausted. Maybe the logs show DHCP discover packets but no offers. Also, check if the OSPF routes include the DHCP server's network.

Debugging Process: Use commands like `/ip dhcp-server lease print`, `/routing ospf neighbor print`, `/ip route print`, maybe check the OSPF LSAs. If the DHCP server's subnet is not being advertised, OSPF might be the culprit. Alternatively, if the DHCP pool is full, that's a different issue.

Key Findings: The /27 subnet is too small, causing DHCP exhaustion. But how does OSPF play into this? Maybe the subnet mask was misconfigured in OSPF, leading to incorrect network advertisements. For example, if the OSPF network is advertised as /27 instead of a larger mask, but the actual subnet is larger. Wait, but the user specified the subnet as /27. So maybe the real issue is the subnet is too small, but OSPF isn't related. However, the scenario says the topic is OSPF, so the problem must be related to OSPF. Maybe the DHCP server is on a different network, and OSPF isn't advertising the route to that network, so clients can't reach the DHCP server. For example, if the DHCP server is on 10.197.145.64/27, but the clients are on another subnet, and the OSPF isn't propagating that route, so DHCP requests don't reach the server.

So the root cause could be that the OSPF configuration on the router connected to the DHCP server isn't advertising the network, so other routers don't know how to reach it. Therefore, clients on other subnets can't get DHCP leases because their requests don't reach the server.

Solution: Correct the OSPF configuration to include the DHCP server's network. Or adjust the subnet to a larger mask if that's the issue. But the user specified the subnet as /27. Maybe the actual issue is that the network was supposed to be a /23 or /22 but was misconfigured as /27, leading to DHCP pool exhaustion. Then the fix would be changing the subnet mask and adjusting OSPF accordingly.

But since the scenario's topic is OSPF, the problem should relate to OSPF misconfiguration. Let's think: perhaps the OSPF area is configured as a stub area, which doesn't allow external routes. If the DHCP server's network is connected via a different routing protocol or static route that's redistributed into OSPF, but the area is stub, those routes won't be propagated. Alternatively, OSPF isn't enabled on the interface connected to the DHCP server, so the network isn't advertised.

Another angle: MTU mismatches causing OSPF adjacency issues. If routers can't form OSPF neighbors, the network isn't advertised, leading to routing problems. But how does that affect DHCP? If the DHCP server is on a network that's not reachable due to missing OSPF routes, then clients can't get IPs.

Verification would involve checking OSPF neighbors, routes, and testing DHCP requests.

Prevention measures: Proper OSPF configuration, monitoring, subnet sizing.

Common pitfalls: Not checking OSPF adjacency states, incorrect network statements, MTU issues, area misconfigurations.

So putting this together:

Initial Problem Report: Users can't get IP addresses. Symptoms include DHCP discover but no offer. High number of users (475) on a /27 subnet, which is too small. Maybe the DHCP server's network isn't reachable due to OSPF not advertising it.

Environment: Two routers connected via OSPF. Router1 has DHCP server on 10.197.145.64/27. Router2 connects to clients. But the subnet is too small. However, OSPF isn't advertising the DHCP server's network to other routers.

Initial Assessment: Check DHCP leases (all used up). Check OSPF neighbors (maybe down). Check routes (missing DHCP server's network).

Debugging: Commands like `/routing ospf neighbor print` shows no adjacency. `/ip dhcp-server lease print` shows all leases used. Maybe OSPF network configuration missing the DHCP interface.

Root Cause: OSPF not advertising the DHCP server's subnet because the network isn't included in OSPF configuration. Or the subnet is too small, but since the topic is OSPF, it's more about the routing.

Solution: Add the DHCP server's network to OSPF. Or fix the subnet mask if it's incorrect.

Wait, but the subnet being /27 is part of the problem. 475 users can't be on a /27. So maybe the actual subnet is supposed to be larger, but was misconfigured. So the fix is changing the subnet mask to /23, expanding the DHCP pool, and ensuring OSPF advertises the correct network.

So combining both issues: a too-small subnet and OSPF misconfiguration. But the main topic is OSPF, so perhaps the OSPF issue is preventing the DHCP server from being reachable, but the subnet size is a red herring. Or maybe the subnet size is the actual problem, and OSPF is a distractor. But the user specified the topic as OSPF, so the problem must be related.

Alternatively, the network is supposed to have multiple subnets connected via OSPF, but the OSPF configuration is incorrect, so clients are all trying to get leases from a single /27 subnet, which is exhausted. But that's a stretch.

Hmm. Maybe the DHCP server is on a different VLAN, and the router isn't relaying DHCP requests because OSPF isn't properly routing between the VLANs. For example, if the DHCP server is on a different subnet and the router needs to have IP helpers configured, but OSPF isn't advertising the route, so the relay isn't working.

But in a SOHO environment, maybe they're using a single router with multiple interfaces. Wait, but SOHO is small office/home office, which typically doesn't have 475 users. Maybe the scenario is a mis-scale, but the user provided it, so proceed.

Alternatively, the industrial network has multiple segments connected via OSPF, and the DHCP server is centralized. If OSPF isn't functioning, the DHCP requests can't be relayed to the server.

In that case, the OSPF neighbors are down, so the routes aren't present. The debugging steps would show OSPF neighbors in down state. The root cause could be mismatched OSPF area IDs, authentication, or network statements.

So, putting this all together, the answer should have:

1. Problem report: Users can't get IPs. DHCP server unreachable due to OSPF routes missing.

2. Network topology with OSPF routers not forming adjacency.

3. Initial checks: OSPF neighbors down, DHCP leases not assigned.

4. Debugging with OSPF commands showing no neighbors, maybe authentication issues.

5. Root cause: OSPF authentication mismatch or network misconfiguration.

6. Solution: Correct OSPF settings, form adjacency, routes appear.

7. Verification: Check neighbors, routes, test DHCP.

8. Prevention: Monitor OSPF, use correct configurations.

But also considering the subnet size. If the subnet is /27 and 475 users, that's impossible. So maybe the actual subnet was supposed to be /23 but was misconfigured as /27. That's a DHCP problem, but the OSPF is a separate issue. However, the user wants the topic to be OSPF, so perhaps the main issue is OSPF-related, and the subnet size is a typo. Or the subnet is correct, but there are multiple subnets connected via OSPF, and the DHCP server is on another subnet not being advertised.

Alternatively, maybe the DHCP server is on a network that's not included in OSPF, so other routers don't know how to reach it. For example, the DHCP server is on 10.197.145.64/27, which is connected to Router1. Router1 is supposed to advertise this network via OSPF to Router2, which connects to the clients. If Router1 isn't advertising the network, Router2 doesn't have a route, so clients can't send DHCP requests to the server.

In that case, the solution is to include the DHCP server's network in OSPF on Router1.

So the detailed steps would involve checking OSPF configuration on Router1 to ensure the network 10.197.145.64/27 is included in the OSPF networks.

But in OSPF, the network statement needs to match the interface's IP and mask. If the interface is configured with /27, then the OSPF network statement should cover that.

Alternatively, maybe the OSPF is configured to advertise a different network, so the DHCP server's network isn't being advertised.

So the key finding is that the OSPF configuration on Router1 doesn't include the DHCP server's subnet, leading to no route advertisement. Therefore, Router2 doesn't know how to reach the DHCP server's network, so DHCP requests fail.

The fix would be adding the correct network statement in OSPF.

So, in the configuration before, the OSPF network might be 10.197.145.0/24, but the actual interface is 10.197.145.64/27. So the network statement is incorrect.

Alternatively, the OSPF isn't enabled on the interface connected to the DHCP server.

Therefore, the detailed steps would involve checking the OSPF networks and interfaces.

Putting this all together into the answer sections.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF & DHCP Lease Issues

## 1. Initial Problem Report and Symptoms
**Report**: 475 users in an industrial SOHO network lost IP connectivity for 23 hours.  
**Symptoms**:  
- Users unable to obtain/renew DHCP leases.  
- DHCP server logs show "no free leases" errors.  
- OSPF neighbors flapping intermittently.  
- Routing table missing critical subnets.  

---

## 2. Environment Description & Network Topology
**Network Type**: Industrial SOHO with 475 devices across VLANs.  
**Subnet**: `10.197.145.64/27` (DHCP pool: `10.197.145.66-10.197.145.94`).  
**OSPF Setup**: Two MikroTik routers (RouterA and RouterB) in Area 0.  

```mermaid
graph TD
  RouterA[RouterA (OSPF Area 0)] -->|OSPF Adjacency| RouterB[RouterB (OSPF Area 0)]
  RouterA --> SwitchA --> VLAN10(Industrial Devices)
  RouterB --> SwitchB --> VLAN20(DHCP Server: 10.197.145.64/27)
```

---

## 3. Initial Assessment Steps
1. **Verify DHCP Pool Exhaustion**:  
   ```bash
   /ip dhcp-server lease print
   # Output: 28 active leases (max for /27 subnet)
   ```
2. **Check OSPF Neighbor Status**:  
   ```bash
   /routing ospf neighbor print
   # Output: RouterB state=Full, RouterA state=Down
   ```
3. **Validate Routing Table**:  
   ```bash
   /ip route print where ospf=yes
   # Output: Missing 10.197.145.64/27 route
   ```

---

## 4. Detailed Debugging Process
### Step 1: Confirm OSPF Adjacency Issues
```bash
/log print where message~"OSPF"
# Log Example: "OSPF: adjacency changed from Full to Down"
```

### Step 2: Check OSPF Interface Configuration
```bash
/routing ospf interface print
# Output: RouterA interface MTU=1500, RouterB MTU=1492 (mismatch)
```

### Step 3: Validate DHCP Subnet Scope
```bash
/ip pool print
# Output: DHCP pool size=28 (insufficient for 475 users)
```

---

## 5. Key Findings & Root Cause Analysis
**Root Cause**:  
- **OSPF MTU Mismatch**: RouterA (MTU=1500) and RouterB (MTU=1492) caused adjacency failures.  
- **DHCP Subnet Oversubscription**: `/27` subnet supports only 28 leases for 475 users.  

**Impact**:  
- OSPF routes for `10.197.145.64/27` were not propagated.  
- DHCP server ran out of leases, leaving 447 users without IPs.  

---

## 6. Solution Implementation Steps
1. **Adjust OSPF MTU on RouterB**:  
   ```bash
   /interface ethernet set [find name=ether1] mtu=1500
   ```
2. **Expand DHCP Subnet to `/23`**:  
   ```bash
   /ip pool set dhcp_pool ranges=10.197.145.66-10.197.146.254
   /ip address set [find address=10.197.145.64/27] address=10.197.145.64/23
   ```
3. **Redistribute OSPF Routes**:  
   ```bash
   /routing ospf network add network=10.197.145.0/23 area=backbone
   ```

---

## 7. Verification Process
1. **Confirm OSPF Adjacency**:  
   ```bash
   /routing ospf neighbor print
   # Output: State=Full, MTU=1500
   ```
2. **Check DHCP Leases**:  
   ```bash
   /ip dhcp-server lease print count-only
   # Output: 475 leases
   ```
3. **Validate Routing Table**:  
   ```bash
   /ip route print where dst-address=10.197.145.0/23
   # Output: OSPF route present
   ```

---

## 8. Prevention Measures
- **OSPF**:  
  - Enable `mtu-ignore` if MTU mismatches are unavoidable.  
  - Use OSPF authentication.  
- **DHCP**:  
  - Allocate subnets with 30% overhead.  
  - Monitor leases with `/tool profile`.  

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Check OSPF adjacency status |
| `/ip dhcp-server lease print` | List active DHCP leases |
| `/log print where message~"OSPF"` | Filter OSPF logs |

---

## 10. Common Pitfalls to Avoid
- **MTU Mismatches**: Always validate MTU on OSPF interfaces.  
- **Subnet Sizing**: Avoid undersized DHCP pools in industrial networks.  
- **OSPF Network Statements**: Ensure all critical subnets are advertised.  
```bash
# Bad Example (Typo in subnet):
/routing ospf network add network=10.197.145.64/27 area=backbone
# Good Example:
/routing ospf network add network=10.197.145.0/23 area=backbone
```
