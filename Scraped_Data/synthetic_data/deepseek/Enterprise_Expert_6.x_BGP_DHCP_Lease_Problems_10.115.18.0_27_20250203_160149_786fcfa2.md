---
generated_at: 2025-02-03T16:02:46.730369
topic: BGP
category: Routing
version: 6.x
scale: Enterprise
level: Expert
subnet: 10.207.244.32/28
scenario: DHCP Lease Problems
environment: Campus Network
affected_users: 934
duration: 11 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP with the given parameters. Let me start by breaking down each section and what's required.

First, the initial problem report and symptoms. The users are experiencing DHCP lease issues, and it's affecting a large number of people. The duration is 11 hours, so it's a prolonged issue. Symptoms might include inability to obtain IP addresses, intermittent connectivity, maybe some BGP routes flapping. I should mention the BGP aspect here since the topic is BGP, even though the main problem is DHCP. Maybe BGP is related to how DHCP is functioning in the network.

Next, the environment description and network topology. The network is a campus network with the subnet 10.207.244.32/28. That's a /28, so only 14 usable addresses. But the number of affected users is 934, which is way more than 14. Hmm, maybe that subnet is for the DHCP server or some infrastructure devices. The network topology in Mermaid. Let me think: the campus network probably has multiple layers. Maybe core routers, distribution switches, access switches, and then the DHCP server. Since BGP is involved, maybe there are multiple BGP peers. The core routers might be running BGP with other routers in the network. The DHCP server could be in a different subnet, and maybe BGP is used for routing between different parts of the campus. Wait, but in a campus network, BGP is not typically used internally; maybe it's for connecting to other campuses or the internet. Maybe the DHCP server is in a different VLAN or subnet, and BGP is used to route between these subnets. If BGP has an issue, maybe the routes to the DHCP server are not being advertised properly, so clients can't reach the DHCP server.

Initial assessment steps. Check BGP neighbors, verify routes, check DHCP server status, look at logs. The user would log into the MikroTik routers and check BGP status with commands like /routing bgp neighbor print. Also check the routing table for the DHCP server's subnet. Maybe the route is missing because BGP isn't advertising it. Also check DHCP leases on the server, but since it's RouterOS, maybe the DHCP server is running on a MikroTik device. So checking the DHCP server's configuration and leases.

Detailed debugging process with CLI commands. Start by checking BGP peers. Use /routing bgp neighbor print to see if neighbors are established. If not, check why. Then look at the routing table with /ip route print. Maybe the route to the DHCP server's network is missing. Then check if the DHCP server is running: /ip dhcp-server print. Maybe the server is down or not configured. Check logs with /log print. Maybe there are BGP flaps or DHCP errors. Also check firewall rules to ensure DHCP traffic is allowed. Maybe BGP wasn't advertising the DHCP subnet due to a misconfiguration in the network statements or route filters.

Key findings and root cause analysis. Suppose the BGP configuration was missing the network advertisement for the DHCP server's subnet. So, other routers don't know how to reach it, so clients can't get DHCP leases. Or maybe a BGP peer was down, causing the route to be withdrawn. The DHCP server's subnet is 10.207.244.32/28, and if that's not being advertised via BGP, then parts of the network can't reach it. Alternatively, maybe a route map or filter is blocking the advertisement. The root cause would be a missing BGP network statement for the DHCP subnet, leading to missing routes and DHCP issues.

Solution implementation steps. Add the network statement in BGP configuration. For example, in RouterOS: /routing bgp network add network=10.207.244.32/28. Then reset BGP sessions if necessary. Verify the routes propagate.

Verification process. Check BGP neighbors again, check routes on other routers, test DHCP requests. Maybe release and renew a DHCP lease on a client to see if it works now.

Prevention measures. Ensure all necessary networks are included in BGP advertisements. Use automated checks or monitoring for BGP routes. Regularly audit BGP configurations.

Related commands reference. List commands like /routing bgp neighbor print, /ip route print, etc.

Common pitfalls. Forgetting to advertise necessary subnets in BGP, not monitoring BGP session status, misconfigured route filters.

Wait, but how does BGP relate to DHCP in this scenario? If the DHCP server is in a different subnet, and the routers rely on BGP to learn the route to that subnet, then if BGP isn't advertising it, the clients can't reach the DHCP server. So the problem is that the route to the DHCP server's subnet isn't present in the routing tables of the access routers, so DHCP requests can't be routed there. Therefore, troubleshooting BGP would involve checking if that specific subnet is being advertised properly.

So the initial problem report is that users can't get DHCP leases. The network uses BGP for routing, and the DHCP server's subnet is not being advertised via BGP, so the routers don't know how to reach it. Hence, clients send DHCP requests, but they don't reach the server.

That makes sense. So the key steps are checking BGP advertisements for the DHCP server's subnet, ensuring it's included in the BGP network statements, and that the routes are present in the routing table.

Another possibility: maybe the DHCP relay agent is misconfigured. If the campus network uses DHCP relays (since the DHCP server is central), the relay agent needs to forward DHCP requests to the server. If the relay agent's IP is incorrect, or if the route to the server is missing (due to BGP), then the relay can't reach the server. So BGP's role is in ensuring the route exists for the relay to work.

So the scenario is: BGP isn't advertising the DHCP server's subnet, so the relay agent can't forward requests to the server. Therefore, clients can't get IPs.

In that case, the root cause is the missing BGP advertisement for 10.207.244.32/28, leading to lack of routing to the DHCP server, thus DHCP lease issues.

I need to structure all this into the sections as per the user's request, including CLI commands and logs.

For example, when checking BGP neighbors:

/routing bgp neighbor print
Flags: X - disabled, E - established 
 0 E instance=default ... 10.207.244.34 remote-as=65000 ... 

If established, that's good. Then check advertised routes:

/routing bgp advertisment print
Maybe the 10.207.244.32/28 isn't listed here.

Then in the routing table:

/ip route print where dst-address=10.207.244.32/28
If it's missing, that's the issue.

So adding the network in BGP:

/routing bgp network add network=10.207.244.32/28

Then reset BGP sessions if needed with /routing bgp neighbor reset [id]

Then verify the route appears in the routing table.

In logs, maybe there were BGP updates, or route withdrawals.

I think that's the general flow. Now putting all this into the markdown structure with the required sections.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario: DHCP Lease Problems

## 1. Initial Problem Report and Symptoms
**Report:** 934 users in campus network unable to obtain/renew DHCP leases for 11+ hours.  
**Symptoms:**
- Clients stuck in `DHCP Discovering` state
- No `ACK` responses from DHCP server
- BGP route table missing `10.207.244.32/28` subnet
- Intermittent BGP session resets logged on core routers

## 2. Environment Description
**Network Topology:**
```mermaid
graph TD
  A[Core Router (BGP AS65000)] --> B[Distribution Switch]
  B --> C[Access Switch]
  C --> D[Client VLAN 100]
  A -. iBGP Peer .- E[Core Router 2 (AS65000)]
  A --> F[DHCP Server 10.207.244.33/28]
```

## 3. Initial Assessment Steps
1. Verify BGP neighbor status:
   ```bash
   /routing bgp neighbor print where remote.address=10.207.244.34
   ```
2. Check routing table for DHCP subnet:
   ```bash
   /ip route print where dst-address=10.207.244.32/28
   ```
3. Confirm DHCP server reachability:
   ```bash
   /ping 10.207.244.33 count=10
   ```

## 4. Detailed Debugging Process
**Step 1: Check BGP Sessions**
```bash
/routing bgp neighbor print
# Output:
# 0 E instance=default name=core2 remote-address=10.207.244.34 remote-as=65000 uptime=10h55m 
```

**Step 2: Verify Advertised Routes**
```bash
/routing bgp advertisement print
# NO entries for 10.207.244.32/28
```

**Step 3: Analyze BGP Network Configuration**
```bash
/routing bgp network print
# Before:
# 0 network=192.168.0.0/16
```

**Step 4: Check Route Filtering**
```bash
/routing filter rule print
# 0 action=accept chain=bgp_out prefix=192.168.0.0/16
# 1 action=discard chain=bgp_out
```

## 5. Key Findings & Root Cause
**Findings:**
- Missing BGP network advertisement for `10.207.244.32/28`
- Route filter blocking non-192.168.0.0/16 prefixes
- DHCP server subnet not propagated through iBGP

**Root Cause:**  
Critical DHCP server subnet excluded from BGP advertisements due to restrictive network statements and route filters, creating routing blackhole.

## 6. Solution Implementation
1. Add BGP network advertisement:
   ```bash
   /routing bgp network add network=10.207.244.32/28
   ```
2. Update route filters:
   ```bash
   /routing filter rule add chain=bgp_out action=accept prefix=10.207.244.32/28
   ```
3. Soft-reset BGP sessions:
   ```bash
   /routing bgp neighbor reset [find where remote.address=10.207.244.34]
   ```

## 7. Verification Process
1. Confirm route propagation:
   ```bash
   /ip route print where dst-address=10.207.244.32/28
   # Output:
   # 0 ADC 10.207.244.32/28        ether1        10.207.244.33
   ```
2. Test DHCP lease acquisition:
   ```bash
   /tool mac-telnet 00:AB:CD:EF:12:34
   > ip dhcp-client renew ether1
   ```
3. Monitor BGP updates:
   ```bash
   /log print where message~"BGP"
   # Output:
   # BGP session core2 state changed: established
   # BGP sent update with 10.207.244.32/28
   ```

## 8. Prevention Measures
1. Implement BGP prefix monitoring:
   ```bash
   /tool netwatch add host=10.207.244.33 timeout=5s up-script="/log info \"DHCP route active\"" down-script="/log warning \"DHCP route missing!\""
   ```
2. Create network documentation database
3. Establish change review process for BGP filters

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp instance print` | Show BGP instances |
| `/ip dhcp-server lease print` | List DHCP leases |
| `/routing filter rule export` | Export route filters |

## 10. Common Pitfalls to Avoid
1. **Over-filtering BGP routes:** Always test filter changes in stages
2. **Ignoring subnet masks:** Ensure `/28` is explicitly allowed, not covered by larger ranges
3. **Forgetting soft-resets:** Use `neighbor reset` after config changes
4. **Mixing iBGP/eBGP rules:** Campus networks often use iBGP with route reflectors

**Before/After Filter Configuration:**
```bash
# BEFORE:
/routing filter rule print
 0 action=accept chain=bgp_out prefix=192.168.0.0/16
 1 action=discard

# AFTER:
/routing filter rule print
 0 action=accept chain=bgp_out prefix=192.168.0.0/16
 1 action=accept chain=bgp_out prefix=10.207.244.32/28
 2 action=discard
```
