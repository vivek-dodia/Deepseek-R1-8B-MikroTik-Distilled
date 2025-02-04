---
generated_at: 2025-02-03T15:59:57.655009
topic: BGP
category: Routing
version: 6.x
scale: Enterprise
level: Basic
subnet: 172.20.129.0/25
scenario: DHCP Lease Problems
environment: Campus Network
affected_users: 352
duration: 19 hours
---

# Analysis Process
Okay, so I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP with DHCP lease problems in an enterprise campus network. Let me start breaking down each section step by step.

First, the initial problem report. The users are complaining about intermittent connectivity. Since it's a DHCP issue affecting 352 users, the symptoms might include clients not getting IPs, leases expiring, or maybe IP conflicts. The duration is 19 hours, which is quite long, so maybe the problem started after a maintenance or a configuration change. The BGP aspect suggests that routing might be involved, perhaps causing DHCP requests to not reach the server or responses not getting back.

Next, the environment description. The subnet is 172.20.129.0/25, which gives 126 usable addresses. But there are 352 users, so maybe there's a mismatch here. Wait, that subnet only allows up to 126 hosts. If there are 352 users, maybe there's a DHCP scope issue or multiple VLANs not being properly handled. The network topology is a campus network with multiple buildings connected via BGP. I should draw a Mermaid diagram showing core routers, distribution switches, access layer, DHCP server, and BGP peers. The DHCP server is on a different subnet, so maybe the relay isn't working properly.

Initial assessment steps: Check DHCP server status, leases, and logs. Verify BGP neighbors to ensure routes are advertised correctly. Look at interface configurations, especially the DHCP relay settings. Check if the DHCP requests are reaching the server. Use packet sniffer on the MikroTik router to capture DHCP traffic. Also, check the IP addresses assigned to clients to see if they're within the correct subnet.

For the debugging process, CLI commands would include checking BGP status with `/routing bgp neighbor print`, looking at routes with `/ip route print`. For DHCP, check the leases on the server and the relay configuration with `/ip dhcp-relay print`. Maybe the BGP routes are not properly advertising the subnet where the DHCP server resides, causing the relay agent to send requests to an unreachable server. Also, verify the DHCP lease time settings. If the lease time is too short and the server can't renew because of routing issues, clients would lose connectivity.

Key findings might be that the BGP session between the core router and distribution layer is down, so the route to the DHCP server's subnet isn't being advertised. Or maybe the DHCP relay is pointing to the wrong server IP. Another possibility is that the subnet mask on the DHCP server is incorrect, not matching the /25, leading to IP conflicts or leases not being assigned properly.

Solution implementation: Fix the BGP neighbor configuration to re-establish the session. Correct the DHCP relay settings to point to the right server. Adjust the DHCP scope to match the subnet. Update the lease times if necessary. Then, restart the BGP session and DHCP service.

Verification would involve checking BGP neighbors are up, routes are present, and testing DHCP requests. Use `dhcp-client` on a test device to get an IP. Check the lease on the server. Monitor for any drops in BGP or DHCP traffic.

Prevention measures: Implement BGP monitoring with tools like Netwatch, set up alerts for BGP session drops. Regularly audit DHCP configurations and lease utilization. Use redundant DHCP servers and BGP peers for failover.

Common pitfalls might be forgetting to update the DHCP scope when subnet changes occur, misconfiguring BGP filters that block necessary routes, or not checking both BGP and DHCP relay configurations together when issues arise.

I need to include CLI commands with comments, maybe show a before and after configuration for the DHCP relay or BGP settings. Log examples could be BGP neighbor state changes or DHCP relay logs showing timeouts.

Wait, the subnet given is /25, which is 128 addresses, but 126 usable. But there are 352 users. That doesn't add up. Maybe the subnet is part of a larger network with multiple VLANs, each with their own /25, but that's 352 users. Alternatively, maybe the DHCP server is supposed to hand out addresses from a larger pool, but the subnet is misconfigured. Or maybe the DHCP server is using a different scope, but the BGP routes aren't allowing the DHCP responses to route back correctly.

Another angle: If the BGP routes are flapping, the DHCP relay might intermittently fail to reach the server, leading to leases not being renewed. Clients with expired leases would lose connectivity. Since the problem is intermittent, it could be related to route instability.

So, putting it all together, the root cause could be a BGP route instability causing the DHCP relay to fail, leading to clients not renewing leases. The initial configuration might have a BGP neighbor with incorrect timers or authentication, causing the session to drop. When the BGP route to the DHCP server's network is unavailable, the relay can't forward requests, so new leases aren't granted, and renewals fail. After 19 hours, if the lease time is 24 hours, most clients would have tried to renew by then and failed, leading to widespread issues.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario: DHCP Lease Problems

## 1. Initial Problem Report and Symptoms
**Report**: 352 users report intermittent connectivity across campus network  
**Symptoms**:
- Random IP address loss (lease expiration)
- DHCP "no response" errors in client logs
- 60% of clients fall back to 169.254.x.x addresses
- BGP route fluctuations observed in core routers
- Issue persists for 19 hours since last maintenance window

## 2. Environment Description
**Network Topology**:
```mermaid
graph TD
    A[Core Router (BGP AS 65530)] <--> B[Dist Switch 1]
    A <--> C[Dist Switch 2]
    B <--> D[Access Switch A]
    C <--> E[Access Switch B]
    D <--> F[AP Group 1]
    E <--> G[AP Group 2]
    H[DHCPServer(172.20.128.10)] <--> A
    I[Internet Gateway] <-.eBGP.-> A
```

## 3. Initial Assessment Steps
1. Verify BGP neighbor status:
   ```bash
   /routing bgp neighbor print where !established
   ```
2. Check DHCP server availability:
   ```bash
   /ping 172.20.128.10 count=10
   ```
3. Review DHCP leases:
   ```bash
   /ip dhcp-server lease print where server=dhcp1
   ```
4. Check routing table for DHCP server network:
   ```bash
   /ip route print where dst-address=172.20.128.0/23
   ```

## 4. Detailed Debugging Process
**Step 1: Verify BGP Advertisements**
```bash
/routing bgp advertisements print detail
```
```log
Flags: F - filtered 
  AS_Path: 65530 
  Dst: 172.20.128.0/23
  NextHop: 172.20.128.10
  Filtered: yes   # Route being filtered unexpectedly
```

**Step 2: Check BGP Filters**
```bash
/routing filter rule print
```
```log
3.. chain=output prefix=172.20.128.0/23 action=discard # Mistaken /23 filter
```

**Step 3: Test DHCP Relay Functionality**
```bash
/tool sniffer quick port=67,68
```
```log
18:22:01 RX DHCPDISCOVER SrcMAC:00:1B:FC:AA:BB:CC 
18:22:01 TX DHCPOFFER via 172.20.128.10:67
  Relay Agent: 172.20.129.1 # Correct relay IP
```

**Step 4: Analyze DHCP Server Capacity**
```bash
/ip dhcp-server lease print count-only where server=dhcp1
```
```log
count: 127/128 # Max lease pool reached
```

## 5. Key Findings & Root Cause
**Root Cause**: Combined BGP+DHCP failure:
1. BGP output filter blocking DHCP server network (172.20.128.0/23)
2. DHCP server pool exhausted (127/128 leases used)
3. /25 subnet mismatch with DHCP server's /23 configuration

**Failure Chain**:
```
BGP Filter → Route Withdrawal → DHCP Relay Timeout → Lease Exhaustion → IP Conflicts
```

## 6. Solution Implementation
**Step 1: Adjust BGP Filter**
```bash
/routing filter rule set [find where chain=output] action=accept
```

**Step 2: Expand DHCP Scope**
```diff
- /ip pool set dhcp-pool ranges=172.20.129.1-172.20.129.126
+ /ip pool set dhcp-pool ranges=172.20.129.1-172.20.129.254
```

**Step 3: Update Subnet Mask**
```bash
/ip dhcp-server network set numbers=0 network=172.20.129.0/24
```

## 7. Verification Process
1. Confirm BGP route propagation:
   ```bash
   /ip route print where dst-address=172.20.128.0/23
   ```
   ```log
   A S  dst-address=172.20.128.0/23 gateway=172.20.128.10
   ```

2. Test DHCP acquisition:
   ```bash
   /ip dhcp-client release [/ip dhcp-client find]
   /ip dhcp-client renew [/ip dhcp-client find]
   ```

3. Monitor lease distribution:
   ```bash
   /ip dhcp-server lease print where active 
   ```

## 8. Prevention Measures
1. Implement BGP monitoring:
   ```bash
   /tool netwatch add host=172.20.128.10 timeout=5s up-script="/log info \"DHCP Server UP\"" down-script="/log warning \"DHCP Server DOWN\""
   ```

2. Configure DHCP alerting:
   ```bash
   /system script add name=dhcp-alert source=":if ([/ip dhcp-server lease get [find] value-name=active-address] > 200) do={ /tool e-mail send to=\"noc@company.com\" subject=\"DHCP Pool 80% Full\" }"
   ```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp neighbor print` | Check BGP peer status |
| `/ip dhcp-server lease print` | Show assigned leases |
| `/tool sniffer quick port=67` | Capture DHCP traffic |
| `/ip route print detail` | Verify route availability |

## 10. Common Pitfalls to Avoid
1. **Subnet Mask Mismatches**: Ensure DHCP server/relay subnet declarations match actual network
2. **BGP Route Filtering**: Audit filters after network changes
3. **Lease Time Configuration**: Avoid short leases (<4h) in large networks
4. **Route Flap Damping**: Configure BGP timers properly (default 30s/180s)
5. **DHCP Relay Isolation**: Ensure relay agents can reach server via ICMP+UDP
```
