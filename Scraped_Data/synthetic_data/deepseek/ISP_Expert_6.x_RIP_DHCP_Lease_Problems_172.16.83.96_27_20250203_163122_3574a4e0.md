---
generated_at: 2025-02-03T16:35:03.766050
topic: RIP
category: Routing
version: 6.x
scale: ISP
level: Expert
subnet: 172.26.54.0/24
scenario: DHCP Lease Problems
environment: Industrial Network
affected_users: 518
duration: 18 hours
---

# Analysis Process
Okay, let's tackle this MikroTik RIP troubleshooting scenario. The user wants a detailed ISP-scale problem with DHCP leases in an industrial network. First, I need to make sure I cover all the required sections. Let's start by breaking down each part.

1. **Initial Problem Report and Symptoms**: The affected users are 518, which is a large number, so likely a significant portion of the subnet. The duration is 18 hours, so it's a prolonged issue. Symptoms would include no internet access, inability to get IPs, maybe some intermittent connectivity. Need to mention that static IPs work, which points to DHCP issues.

2. **Environment Description**: The subnet is 172.26.54.0/24. Since it's an ISP and industrial network, maybe there are multiple routers running RIP. The topology should have a Mermaid diagram showing core, distribution, access layers. The DHCP server is on the access router. Maybe RIP is used between routers to advertise routes, including the DHCP subnet.

3. **Initial Assessment Steps**: Check DHCP server status, lease count, IP availability. Verify RIP configuration to ensure the DHCP subnet is being advertised. Check routing tables on neighboring routers to see if the route is present. Use commands like `/ip dhcp-server print`, `/ip dhcp-server lease print`, `/routing rip interface print`, `/routing rip neighbor print`, `/ip route print`.

4. **Detailed Debugging**: Look into DHCP server logs for errors. Maybe there are no leases being handed out because the server is down or out of addresses. Check if the RIP routes are correctly propagated. If the route to 172.26.54.0/24 isn't in the routing table of other routers, clients can't reach the DHCP server. Maybe there's a misconfiguration in RIP, like a missing network or a passive interface. Use commands like `/log print` to check DHCP logs, `/routing rip route print` to see advertised routes. Verify firewall rules that might block DHCP traffic.

5. **Root Cause Analysis**: Suppose the DHCP subnet isn't advertised via RIP, so other routers don't know the path. Maybe the RIP configuration on the access router doesn't include the DHCP network, so the core routers aren't receiving the route. Alternatively, a passive interface setting on the RIP interface might prevent sending updates. Another angle: DHCP server's IP isn't in the same subnet as the clients, but since it's ISP, maybe it's a relay issue. Wait, the scenario says DHCP lease problems, so maybe the DHCP server is reachable but not assigning leases correctly. However, if static IPs work, then the network route is okay. Wait, that's conflicting. If static IPs work, the routing is fine, so the problem is within the DHCP server itself. But the user specified RIP as the topic, so the issue must be related to RIP causing DHCP problems. Hmm, maybe the DHCP server is on a different subnet, and clients are on 172.26.54.0/24, but the route to the DHCP server isn't present because RIP isn't advertising it. Wait, but if static IPs work, the clients have correct routes. Maybe the DHCP server is in a different subnet, and the routers aren't getting the route via RIP, so DHCP requests aren't reaching the server. But in that case, static IPs would also have issues unless they have a default route. Alternatively, maybe the DHCP relay isn't configured, and the server is in another subnet. But the scenario states the subnet is 172.26.54.0/24, and the DHCP lease problem is within that subnet. Wait, maybe the DHCP server is on the same subnet, so RIP isn't directly involved. But since it's an ISP network, perhaps the DHCP server is centralized, and the RIP routes are necessary for the DHCP traffic to reach it. Alternatively, the issue is that the RIP configuration is causing routing loops or incorrect routes, leading to DHCP discovery packets not reaching the server. But I need to tie RIP into the DHCP problem. Maybe the DHCP server's network isn't advertised via RIP, so when clients get a lease, their default gateway isn't reachable because the route isn't present. Wait, but static IPs work. So if a client has a static IP and gateway, they can communicate. But DHCP clients might be getting a wrong gateway or no gateway. Wait, that's possible. If the DHCP server is misconfigured, giving wrong options. But the topic is RIP. Alternatively, the DHCP server is handing out correct options, but the routers aren't advertising the route to the DHCP server's network via RIP, so other routers don't know how to reach it. But if the DHCP server is on the same subnet as the clients, then RIP isn't needed for local communication. Hmm, maybe the issue is that the DHCP server is on a different subnet, and the RIP routes aren't being propagated, so the DHCP relay agent isn't functioning. For example, if the DHCP server is in another subnet, the relay agent (which would be the router) needs to forward DHCP requests to the server. If the route to the server's subnet isn't known due to RIP misconfiguration, the relay can't reach the server. In that case, static IPs would work if they have the correct gateway, but DHCP clients can't get leases because the relay can't communicate with the DHCP server. That makes sense. So the root cause would be that the DHCP server's subnet isn't advertised in RIP, so the relay agent (router) doesn't have a route to it, causing DHCP requests to be dropped. Therefore, the solution is to include the DHCP server's subnet in RIP configuration. Let's structure it that way.

6. **Solution Implementation**: Add the DHCP server's network to RIP networks on the relevant routers. For example, if the DHCP server is on 10.10.10.0/24, ensure that network is included in the RIP configuration. Alternatively, if the DHCP server is in the 172.26.54.0/24 subnet, but the RIP configuration on the access router isn't advertising it. So in the access router's RIP setup, add 172.26.54.0/24 to the networks list.

7. **Verification**: After adding the network to RIP, check the routing tables on other routers to see if the route appears. Check DHCP leases being assigned. Use `ping` from a client to the DHCP server.

8. **Prevention**: Ensure all relevant subnets are included in RIP networks. Use passive interfaces where necessary. Monitor routing tables.

9. **Commands**: Include `routing rip interface add`, `routing rip network add`, `ip dhcp-server network add`, etc.

10. **Common Pitfalls**: Forgetting to advertise all necessary networks in RIP, passive interfaces blocking updates, split horizon issues.

Wait, but the subnet given is 172.26.54.0/24. Let me adjust the scenario. Suppose the DHCP server is on this subnet, but the RIP configuration on the router connected to this subnet isn't advertising it. Therefore, other routers don't have a route to 172.26.54.0/24, so when clients from other subnets try to reach it (if the DHCP server is serving multiple subnets via relay), the routes are missing. But in this case, the problem is that clients on 172.26.54.0/24 can't get DHCP leases. If the DHCP server is local, then RIP might not be directly involved. Alternatively, the router's interface for 172.26.54.0/24 is not included in RIP, so other routers don't know the route, and if the DHCP server is on a different subnet, the relay can't reach it. Hmm, maybe the DHCP server is on a different subnet, say 10.0.0.0/24, and the router connecting to 172.26.54.0/24 is supposed to relay DHCP requests to 10.0.0.2. But the route to 10.0.0.0/24 isn't being advertised via RIP, so the relay can't reach the server. Therefore, adding 10.0.0.0/24 to RIP networks on the server's router would propagate the route, allowing the relay to work. That ties RIP to the DHCP problem. So the initial problem is that the DHCP server's subnet isn't advertised via RIP, causing the relay agent (router) to not have a route, hence DHCP requests are not reaching the server.

But in the given scenario, the subnet is 172.26.54.0/24. Maybe the DHCP server is on this subnet, so clients should be able to reach it directly. But if the router's interface is not running RIP, then other routers might not know about this subnet. Wait, but if the clients are on the same subnet as the DHCP server, they don't need a router to communicate. So unless the DHCP server is on a different subnet, RIP wouldn't affect the lease process. This is confusing. Let me rethink.

Alternative approach: Maybe the issue is that the RIP configuration is causing the router to not act as a DHCP relay properly. For example, if the router's interfaces are not correctly participating in RIP, leading to incorrect routing tables, which affects the relay agent's ability to forward DHCP requests. Alternatively, the DHCP server is on a different network, and the route to that network isn't present because RIP isn't advertising it. Therefore, the router can't relay the DHCP requests to the server. In this case, adding the DHCP server's network to RIP would solve the problem.

Alternatively, maybe the DHCP server is handing out incorrect gateway information because the RIP routes are missing. But static IPs work because they have the correct gateway set manually. DHCP clients get a gateway that's not reachable because the route isn't advertised. Wait, but the gateway is typically the router's interface IP on the same subnet. So if the gateway is 172.26.54.1, and the client is on 172.26.54.0/24, then the gateway is directly reachable. So even if RIP isn't working, the client can reach the gateway. Therefore, static IPs would work because their gateway is correct, but DHCP clients might have wrong gateway settings. But if the DHCP server is configured to give the correct gateway, then that's not the issue. Hmm.

Alternatively, the problem is that the DHCP server's IP pool is exhausted. But the initial assessment would check that. However, the scenario states that the problem is related to RIP. So I need to link RIP configuration to the DHCP lease problem.

Another angle: The DHCP server is on a different VLAN or subnet, and the router needs to have a route to that subnet. If RIP isn't advertising that route, the router can't reach the DHCP server, so DHCP requests fail. But static IPs on the client's subnet would still work if their gateway is correct. Wait, but if the client's subnet is 172.26.54.0/24 and the DHCP server is on another subnet, say 10.10.10.0/24, then the router needs a route to 10.10.10.0/24. If that route is learned via RIP, and it's missing, then the router can't relay the DHCP request. So in this case, the DHCP relay agent (the router) is configured to forward DHCP requests to 10.10.10.2, but the router doesn't have a route to 10.10.10.0/24 because RIP isn't advertising it. Therefore, the relay fails. Static IP clients on 172.26.54.0/24 can still communicate within their subnet and through their gateway if the gateway has other routes. But without the route to the DHCP server's subnet, the relay can't send the request. Therefore, the root cause is the missing RIP route for the DHCP server's subnet.

So, to structure this:

- Initial problem: Users can't get DHCP leases. Static IPs work, so layer 3 connectivity exists for those with static IPs. But DHCP clients can't get IPs.

- Environment: The DHCP server is on 10.10.10.0/24, and the clients are on 172.26.54.0/24. The router acts as a DHCP relay, forwarding requests to 10.10.10.2. However, the route to 10.10.10.0/24 is missing because RIP isn't advertising it. So the router can't reach the DHCP server.

- Initial assessment: Check DHCP lease table (maybe empty). Check if relay is configured. Check routes on the router for 10.10.10.0/24. Not present because RIP isn't advertising it.

- Debugging: Look into routing tables, RIP configurations. Find that the 10.10.10.0/24 network isn't included in the RIP networks on the DHCP server's router. Therefore, other routers don't learn the route.

- Solution: Add 10.10.10.0/24 to RIP networks on the DHCP server's router. Then, the route propagates, allowing the relay to reach the server.

But the given subnet is 172.26.54.0/24. Maybe the DHCP server is in this subnet, so the issue is different. Alternatively, the DHCP server is in 172.26.54.0/24, but other routers don't know the route to this subnet because it's not advertised via RIP. Therefore, if clients are on other subnets and using DHCP relay, the relay can't reach the server. But in the problem statement, the affected users are on 172.26.54.0/24. So maybe the DHCP server is on the same subnet, so RIP isn't involved in the local communication. Then why are there DHCP lease issues? Unless the DHCP server is offline, but the problem is linked to RIP.

Wait, maybe the DHCP server is on a different interface of the router, and the router's RIP configuration isn't including the DHCP server's network, causing other routers to not know how to reach it. But if the clients are on the same subnet as the DHCP server, they don't need the route. Hmm. This is tricky. Let me try to outline the scenario again.

Given that the topic is RIP and the problem is DHCP leases, I need to find a scenario where RIP misconfiguration affects DHCP. One possible scenario is:

- The network uses RIP to advertise routes between multiple routers.

- The DHCP server is located on a central subnet, say 10.0.0.0/24, and clients are on 172.26.54.0/24.

- The router on 172.26.54.0/24 is configured as a DHCP relay agent, forwarding requests to 10.0.0.2.

- However, the route to 10.0.0.0/24 is not being advertised via RIP from the central router to the access router.

- Therefore, the access router (172.26.54.0/24) doesn't have a route to 10.0.0.0/24, so DHCP relay fails.

- Static IP clients on 172.26.54.0/24 can still communicate if their default gateway is set correctly (assuming the gateway has other routes), but DHCP clients can't get leases because the relay can't reach the server.

- The solution is to ensure that the central router advertises 10.0.0.0/24 via RIP, and the access router learns it.

But how does this tie into the given subnet 172.26.54.0/24? Maybe the access router's subnet (172.26.54.0/24) isn't being advertised via RIP, so other parts of the network don't know how to reach it. Wait, but the DHCP server is on a different subnet. If the DHCP server's subnet is not advertised, the relay can't reach it. Alternatively, if the access router's subnet (172.26.54.0/24) isn't advertised, then the central routers don't know how to route traffic back to it. But if the DHCP server is on the central network, and the access router's subnet isn't advertised, then when the DHCP server sends the response back, the central router doesn't know how to route it to 172.26.54.0/24. Therefore, the DHCP response can't reach the client. This would cause DHCP issues. In this case, the access router needs to advertise 172.26.54.0/24 via RIP so that the central routers know the route. If it's not advertised, the central routers drop the DHCP responses. Static IP clients might have the same issue if their traffic needs to go through the central network, but maybe they're using a different default route or the problem is specific to DHCP traffic.

This seems plausible. So the root cause is that the access router isn't advertising 172.26.54.0/24 via RIP, so the rest of the network doesn't have a route back to that subnet. Therefore, DHCP responses from the server can't reach the clients. Static IP clients might be using a different default gateway that has a static route or another routing protocol, hence they work. But DHCP clients are getting their configuration via DHCP, which includes the default gateway. If the DHCP server is on a different subnet, and the route back is missing, then even if the client gets a lease, they can't communicate beyond their subnet. Wait, but the initial problem is DHCP lease problems, meaning clients can't even get a lease. So the DHCP discovery packets aren't reaching the server. If the server is on a different subnet and the relay isn't working because the route is missing, then the DHCP requests don't reach the server, hence no leases. Static IP clients have manually configured IPs and gateway, so they can communicate if the gateway has the necessary routes. But if the gateway (access router) isn't advertising its subnet via RIP, then traffic from the server to the client's subnet isn't routable, so even if the client has a static IP, they can't reach beyond their subnet. But the problem states that static IPs work, which suggests that the routing is okay for them. This is conflicting.

Alternatively, maybe the DHCP server is on the same subnet as the clients (172.26.54.0/24), so RIP isn't needed for DHCP communication. In that case, the issue is unrelated to RIP. But the topic is RIP, so the problem must involve RIP. Therefore, the DHCP server must be on a different subnet, and the issue is with the relay agent's ability to reach the server due to missing RIP routes.

Putting it all together:

- **Initial Problem**: 518 users on 172.26.54.0/24 can't get DHCP leases. Static IPs work, indicating layer 2 connectivity is okay.

- **Environment**: The network uses RIP. The DHCP server is on a different subnet (e.g., 10.10.10.0/24). The access router for 172.26.54.0/24 is configured as a DHCP relay to 10.10.10.2. However, the route to 10.10.10.0/24 isn't present in the access router's routing table because it's not advertised via RIP.

- **Initial Assessment**: Check DHCP server status, check relay configuration, check routes to DHCP server's subnet.

- **Debugging**: Find that the route to 10.10.10.0/24 is missing. Check RIP configuration on the DHCP server's router and find that 10.10.10.0/24 isn't included in the RIP networks.

- **Solution**: Add 10.10.10.0/24 to RIP networks on the DHCP server's router. This allows the route to be propagated, enabling the relay agent to reach the server.

This ties RIP to the DHCP issue through route propagation affecting the relay agent's functionality.

Now, let's structure all sections accordingly, ensuring that each part aligns with this scenario.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP & DHCP Lease Issues

## 1. Initial Problem Report and Symptoms
**Report**: 518 users in 172.26.54.0/24 subnet (industrial network) report no internet access.  
**Symptoms**:  
- DHCP clients fail to obtain IP addresses.  
- Static IP clients function normally.  
- DHCP lease table shows 0 active leases.  
- Users experience issues for 18+ hours.  

---

## 2. Environment Description & Network Topology

```mermaid
graph TD
  Core[Core Router (R1)<br>10.10.10.1/24] -->|RIP| Distribution[Distribution Router (R2)]
  Distribution -->|RIP| Access[Access Router (R3)<br>172.26.54.1/24]
  Access --> Switch[Industrial Switch]
  Switch --> Client1[Client (DHCP)]
  Switch --> Client2[Client (Static IP)]
  Core -.-> DHCPServer[DHCPServer (10.10.10.2/24)]
```

---

## 3. Initial Assessment Steps
1. **Verify DHCP Server Status**:  
   ```bash
   /ip dhcp-server print
   # Status: running
   ```
2. **Check IP Pool Exhaustion**:  
   ```bash
   /ip dhcp-server lease print
   # 0 active leases
   ```
3. **Validate RIP Configuration**:  
   ```bash
   /routing rip interface print
   # Ensure interfaces participate in RIP
   ```
4. **Check Routing Table on R3**:  
   ```bash
   /ip route print where dst-address=10.10.10.0/24
   # No route found
   ```

---

## 4. Detailed Debugging Process
**Step 1**: Check DHCP Server Logs  
```bash
/log print where message~"DHCP"
# 2023-10-01 08:00:00 dhcp,error no relay route to 10.10.10.2
```

**Step 2**: Validate RIP Routes on R3  
```bash
/routing rip route print
# Missing 10.10.10.0/24 (DHCPServer subnet)
```

**Step 3**: Investigate RIP Configuration on R1 (Core)  
```bash
/routing rip network print
# 0  network=10.10.10.0/24 (correct)
```

**Step 4**: Check RIP Neighbors on R3  
```bash
/routing rip neighbor print
# No neighbors advertising 10.10.10.0/24
```

---

## 5. Key Findings & Root Cause Analysis
**Root Cause**:  
- **R1 (Core)** was not advertising the DHCP server subnet (`10.10.10.0/24`) via RIP.  
- **R3 (Access)** had no route to `10.10.10.0/24`, causing DHCP relay failures.  

**Impact**:  
- DHCP requests from `172.26.54.0/24` could not reach the centralized DHCP server.  

---

## 6. Solution Implementation Steps
1. **Add DHCP Server Subnet to RIP on R1**:  
   ```bash
   /routing rip network add network=10.10.10.0/24
   ```
2. **Force RIP Update Propagation**:  
   ```bash
   /routing rip interface reset [find where interface=ether1]
   ```
3. **Verify Route on R3**:  
   ```bash
   /ip route print where dst-address=10.10.10.0/24
   # 10.10.10.0/24 via 10.10.20.1 (R2), RIP
   ```

---

## 7. Verification Process
1. **Confirm DHCP Leases**:  
   ```bash
   /ip dhcp-server lease print
   # 518 active leases
   ```
2. **Test Connectivity**:  
   ```bash
   [Client] ping 8.8.8.8
   # Success (via DHCP-assigned gateway)
   ```

---

## 8. Prevention Measures
- Audit all RIP-advertised subnets periodically.  
- Enable passive RIP interfaces for non-router subnets.  
- Monitor routing tables with scripts:  
  ```bash
  :local routes [/ip route find where protocol=rip]; :put ($routes)
  ```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing rip network print` | List RIP-advertised networks |
| `/ip dhcp-server lease print` | Show DHCP leases |
| `/routing rip interface reset` | Force RIP updates |

---

## 10. Common Pitfalls to Avoid
- **Missing Subnets in RIP**: Ensure all critical subnets are explicitly added.  
- **Passive Interfaces**: Avoid marking router-facing interfaces as passive.  
- **Split Horizon**: Disable if using non-broadcast media (e.g., point-to-point links).  
```bash
/routing rip interface set [find] split-horizon=no
```
```
