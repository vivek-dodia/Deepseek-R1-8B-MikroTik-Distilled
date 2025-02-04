---
generated_at: 2025-02-03T15:25:43.520293
topic: OSPF
category: Routing
version: 6.x
scale: Enterprise
level: Expert
subnet: 172.26.33.80/28
scenario: VPN Tunnel Issues
environment: Edge Location
affected_users: 76
duration: 7 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF with the given parameters. Let me start by breaking down each section and think through what needs to be included.

First, the user provided the topic as OSPF on RouterOS version 6.x in an enterprise network. The subnet is 172.26.33.80/28, which is a small subnet with 16 addresses. The environment is an edge location, and the scenario is VPN tunnel issues affecting 76 users for 7 hours. 

1. **Initial Problem Report and Symptoms**: I need to list the symptoms that users and monitoring tools would report. Users might experience intermittent connectivity, high latency, or inability to access certain resources. Monitoring tools might show OSPF adjacencies flapping, VPN tunnel instability, routing table inconsistencies. Since it's a VPN issue affecting OSPF, maybe OSPF routes aren't being advertised over the VPN tunnel, causing parts of the network to be unreachable.

2. **Environment Description and Network Topology**: The edge location has a MikroTik router (maybe model CCR1016) connected to a head office via IPsec VPN. There are two ISPs for redundancy. The subnet 172.26.33.80/28 is at the edge. I'll need to represent this in Mermaid format. Let me sketch that out. The edge router connects to ISP1 and ISP2, has a VPN tunnel to Head Office Router, and the LAN subnet. OSPF is running on all routers, with the edge router in area 0.

3. **Initial Assessment Steps**: Check OSPF neighbors, verify VPN tunnel status, review routing tables, check for interface errors, and look at logs. For CLI commands, use `/routing ospf neighbor print`, `/interface ipsec policy print`, `/ip route print`, etc.

4. **Detailed Debugging Process**: Start with OSPF neighbor checks. If neighbors are down, check if the VPN tunnel is up. Use commands like `/interface ipsec active-peers print` to see if the tunnel is active. Then check OSPF configuration on the tunnel interface. Maybe OSPF isn't enabled on the VPN interface, or the network type is misconfigured. For example, if the VPN is a point-to-point link but OSPF is set to broadcast, that could cause issues. Also, check MTU settings since IPsec adds overhead. Maybe the MTU is too high, causing fragmentation and dropped packets, leading to OSPF hello packet loss.

5. **Key Findings and Root Cause**: Suppose during debugging, they found that OSPF wasn't enabled on the VPN interface. Or maybe the OSPF network type was incorrect. Or MTU mismatch. For example, the VPN interface MTU is 1400, but the OSPF is using default 1500, leading to packet fragmentation and drops. Another possibility is that IPsec policies were misconfigured, causing the tunnel to drop periodically, which in turn causes OSPF adjacencies to reset.

6. **Solution Implementation**: Adjust OSPF network type on the VPN interface to point-to-point, set MTU to match the tunnel's MTU, ensure OSPF is enabled on the correct interfaces. Update IPsec policies if necessary.

7. **Verification**: Check OSPF neighbors again, monitor VPN tunnel stability, test connectivity, check routing tables for restored routes.

8. **Prevention Measures**: Consistent OSPF configuration templates, MTU checks, monitoring for IPSec and OSPF, regular audits.

9. **Related Commands Reference**: List all commands used in the process, like OSPF neighbor print, IPsec active peers, interface settings, etc.

10. **Common Pitfalls**: Forgetting to set OSPF network type on VPN interfaces, MTU mismatches, not including VPN interfaces in OSPF areas, misconfigured IPsec policies.

Wait, the user mentioned VPN Tunnel Issues. So the root cause is likely related to the VPN tunnel's stability affecting OSPF adjacencies. Maybe the OSPF hello packets are being dropped because the tunnel is down, or the OSPF is not configured to run over the tunnel interface. Another angle: perhaps the OSPF is configured on physical interfaces instead of the tunnel interface, so when the primary ISP fails, the VPN over the backup ISP isn't properly advertising routes.

But in the scenario, the duration is 7 hours, which suggests a persistent issue. Maybe OSPF was not configured on the tunnel interface, so when the primary link went down, the backup VPN tunnel wasn't advertising routes properly. Or OSPF was running over the physical WAN interface which became unstable, but the VPN tunnel is over a different interface, and OSPF wasn't set up on the tunnel interface.

Alternatively, maybe the IPsec policies were not correctly set to allow OSPF traffic (protocol 89), but that's less likely since OSPF runs over IP protocol 89, and IPsec might be encrypting all traffic, including OSPF. Wait, but OSPF multicast packets might not be getting through the VPN tunnel if the tunnel isn't set up to carry them. For example, if the VPN is a site-to-site tunnel but OSPF is trying to establish adjacency over the tunnel using multicast, which isn't supported, so OSPF needs to be configured with unicast neighbors.

Wait, OSPF typically uses multicast (224.0.0.5 and 224.0.0.6) for neighbor discovery. If the VPN tunnel is a point-to-point link, maybe the OSPF network type should be set to point-to-point, and static neighbors might need to be configured if multicast isn't working over the tunnel. Alternatively, if the VPN is a GRE tunnel, multicast would be possible, but with IPsec in transport mode, maybe not. But in this case, it's an IPsec tunnel. So if OSPF is running over an IPsec tunnel, the OSPF packets need to be encrypted. If the IPsec policies are not correctly set up to encrypt OSPF traffic (protocol 89), then the OSPF packets would be sent in clear text and might be dropped by the remote end, or the tunnel isn't encrypting them, leading to adjacency failures.

So possible root causes:

- OSPF not enabled on the VPN tunnel interface.

- OSPF network type mismatch (e.g., broadcast vs point-to-point).

- MTU issues causing OSPF packets to be fragmented and dropped.

- IPsec policies not correctly matching OSPF traffic (protocol 89), leading to packets not being encrypted and thus dropped by the remote router.

- Firewall rules blocking OSPF traffic over the VPN interface.

In the debugging process, the engineer would check OSPF neighbors, see that the adjacency over the VPN is down. Then check the VPN tunnel status. If the tunnel is up, check if OSPF is configured on the tunnel interface. Then check OSPF network type, MTU, and IPsec policies.

For example, if the IPsec policy is set to encrypt traffic between the edge router and head office, but the OSPF traffic is using the correct source and destination IPs. If the IPsec policy is using the wrong subnet or not covering the OSPF router IDs, then the OSPF packets might not be encrypted, and the head office router might drop them.

Alternatively, maybe the OSPF is configured to use the physical WAN interface's IP as the router ID, but the VPN tunnel is using a different IP, leading to mismatched neighbor addresses.

Another angle: OSPF authentication. If OSPF is using MD5 authentication and the keys don't match between the edge and head office, adjacency won't form. But the user didn't mention authentication, so maybe that's not the case here.

Putting it all together, let's create a scenario where the root cause is OSPF network type mismatch on the VPN tunnel interface. The VPN is a point-to-point link, but OSPF is configured as broadcast, leading to hello packets not being processed correctly. The engineer changes the network type to point-to-point, resolves the adjacency issue.

Alternatively, MTU issues. The IPsec tunnel has an MTU lower than 1500, but the OSPF packets are sent with DF bit set, causing fragmentation issues. Adjusting the MTU on the OSPF interface or enabling TCP MSS clamping could help.

But since the problem is VPN tunnel issues affecting OSPF, maybe the VPN tunnel itself is unstable. The logs show the tunnel going up and down, causing OSPF adjacencies to reset. The root cause could be rekeying issues in IPsec, leading to tunnel drops. For example, if the lifetime settings are mismatched between the two ends, the tunnel might rekey frequently, causing temporary outages.

In RouterOS, IPsec configuration might have lifetime settings. If the edge router is using a different lifetime (e.g., 1 hour) than the head office (e.g., 8 hours), the tunnel would rekey more often, causing disruptions. But the problem lasted 7 hours, which might align with a lifetime mismatch (e.g., 1-hour lifetime, so 7 rekeys, each causing a brief outage). However, OSPF might recover after the tunnel comes back, but if the tunnel is flapping, OSPF adjacencies would flap too.

But in the scenario, the issue is persistent for 7 hours, so maybe the tunnel isn't establishing properly. Maybe the pre-shared key is incorrect, or the peer's IP changed, or NAT traversal issues. But the initial problem report says VPN tunnel issues, so perhaps the tunnel is down, and OSPF isn't able to form adjacencies over it.

Wait, OSPF requires layer 3 connectivity. If the VPN tunnel is down, OSPF can't establish adjacency. So if the VPN tunnel is down, that's the root cause. But why is the VPN tunnel down? Maybe misconfiguration in IPsec, like incorrect peer address, wrong PSK, or firewall blocking UDP 500 or 4500.

But the user wants the scenario to focus on OSPF, so maybe the VPN tunnel is up, but OSPF isn't working over it. So the VPN is up (IPsec established), but OSPF adjacency isn't forming. That points to OSPF configuration issues on the tunnel interface.

In that case, during the debugging, the engineer checks `/routing ospf neighbor print` and sees no neighbors on the VPN interface. Then checks `/interface print` to see if the tunnel interface is listed, and whether OSPF is enabled on it. Then checks the OSPF network type with `/routing ospf interface print`, sees it's set to broadcast instead of point-to-point. Changing that fixes the adjacency.

Alternatively, the OSPF area is not configured correctly on the tunnel interface. Or the OSPF is not enabled on the tunnel interface at all.

Another possibility: The OSPF router IDs are conflicting. If both routers have the same router ID, adjacency won't form. But that's a basic mistake, more likely in a lab than an enterprise, but possible.

Alternatively, the subnet 172.26.33.80/28 is part of the OSPF area, but if the VPN tunnel is using a different subnet that's not included in OSPF, the routes aren't advertised.

But given that the problem is VPN tunnel issues affecting OSPF, the key is that OSPF isn't properly configured over the VPN tunnel, leading to routing failures.

In the detailed debugging, the engineer would use commands like `/routing ospf neighbor print` to check neighbors, `/interface ipsec policy print` to check if the policies are correct, `/log print` to look for OSPF or IPsec errors.

In the example log outputs, maybe there are entries indicating OSPF hello packets not received, or IPsec negotiation failures.

For the solution, the engineer might adjust the OSPF network type on the tunnel interface, ensure OSPF is enabled on it, correct MTU settings, and verify IPsec policies.

Prevention measures would include ensuring OSPF is properly configured on all VPN interfaces, using consistent network types, monitoring OSPF adjacencies and VPN tunnel status, and regular configuration audits.

Common pitfalls could be neglecting to configure OSPF on tunnel interfaces, mismatched network types, MTU issues, or assuming VPN tunnels don't affect OSPF without proper testing.

So putting this all together into the structure the user provided. Now, let's structure each section with the necessary details, commands, and explanations.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF VPN Tunnel Issues

## 1. Initial Problem Report and Symptoms
- **Users Report**: Intermittent access to HQ resources, VoIP call drops, and slow file transfers.
- **Monitoring Alerts**: 
  - OSPF adjacency flapping between Edge Router and HQ Router
  - VPN tunnel interface (`ipsec-tunnel1`) unstable (UP/DOWN events)
  - Missing OSPF routes for `172.26.33.80/28` in HQ routing table
- **Logs**: Frequent `OSPF: Neighbor X.X.X.X state changed` and `IPsec phase2 rekey failed` entries.

---

## 2. Environment Description and Network Topology

```mermaid
graph TD
  ER[Edge Router (CCR1016)] --> ISP1[ISP1 (Primary)]
  ER --> ISP2[ISP2 (Backup)]
  ER --> LAN[LAN: 172.26.33.80/28]
  ER <-.-> |IPsec Tunnel (10.255.255.1/30)| HQ[Headquarters Router (CRS125)]
  HQ --> Core[Core Network: 10.0.0.0/16]
```

- **OSPF Areas**: All routers in Area 0 (Backbone)
- **VPN Tunnel**: Site-to-site IPsec (IKEv1) between ER (172.26.33.81) and HQ (203.0.113.10)

---

## 3. Initial Assessment Steps
1. **Verify OSPF Neighbors**:
   ```bash
   /routing ospf neighbor print
   # OUTPUT: No neighbors on interface "ipsec-tunnel1"
   ```
2. **Check VPN Tunnel Status**:
   ```bash
   /interface ipsec active-peers print
   # OUTPUT: 
   # 0 local-address=172.26.33.81 remote-address=203.0.113.10 state=established
   ```
3. **Review Routing Table**:
   ```bash
   /ip route print where ospf=yes
   # OUTPUT: Missing HQ routes (e.g., 10.0.0.0/16)
   ```

---

## 4. Detailed Debugging Process

### Step 1: Validate OSPF Interface Configuration
```bash
/routing ospf interface print
# BEFORE:
#   INTERFACE        NETWORK-TYPE AREA
#   ether1           broadcast    0.0.0.0
#   ipsec-tunnel1    broadcast    0.0.0.0  # Incorrect for P2P tunnel!
```

### Step 2: Check MTU Mismatches
```bash
/interface print 
# ipsec-tunnel1 MTU=1400 (IPsec overhead), physical interface MTU=1500
```

### Step 3: Inspect IPsec Policies
```bash
/interface ipsec policy print
# BEFORE: 
#   src-address=172.26.33.80/28 dst-address=10.0.0.0/16
#   proposal=default priority=10
# Missing OSPF (proto 89) policy!
```

### Step 4: Analyze Packet Capture
```bash
/tool sniffer quick protocol=ospf interface=ipsec-tunnel1
# OUTPUT: No OSPF packets detected (encryption mismatch)
```

---

## 5. Key Findings and Root Cause Analysis
- **Root Cause**: 
  1. OSPF network type misconfigured as `broadcast` on a point-to-point IPsec tunnel.
  2. IPsec policy missing OSPF protocol (89) encryption, causing packet drops.
  3. MTU fragmentation (1500 vs 1400) disrupting OSPF hello packets.
- **Impact**: OSPF adjacency failed to form, preventing route exchange via VPN.

---

## 6. Solution Implementation Steps
1. **Correct OSPF Network Type**:
   ```bash
   /routing ospf interface set [find interface=ipsec-tunnel1] network-type=point-to-point
   ```
2. **Adjust MTU Settings**:
   ```bash
   /interface set ipsec-tunnel1 mtu=1400
   /ip firewall mangle add chain=forward out-interface=ipsec-tunnel1 protocol=tcp tcp-flags=syn action=change-mss new-mss=1360
   ```
3. **Fix IPsec Policy**:
   ```bash
   /interface ipsec policy add src-address=172.26.33.80/28 dst-address=10.0.0.0/16 protocol=89 proposal=default
   ```

---

## 7. Verification Process
1. Confirm OSPF Adjacency:
   ```bash
   /routing ospf neighbor print
   # OUTPUT: HQ Router ID (10.255.255.2) in FULL state
   ```
2. Validate Routing Table:
   ```bash
   /ip route print where dst-address=10.0.0.0/16
   # OUTPUT: route added via OSPF
   ```
3. Test End-to-End Connectivity:
   ```bash
   /ping 10.0.1.1 count=10 interval=100ms
   # OUTPUT: 10/10 successful
   ```

---

## 8. Prevention Measures
- **Template Enforcement**: Use standardized OSPF/VPN configs across edge devices.
- **Monitoring**: Alert on OSPF neighbor state changes and IPsec tunnel stability.
- **MTU Audits**: Validate tunnel MTU matches physical interface settings.
- **Policy Reviews**: Quarterly audits of IPsec policies for protocol coverage.

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | List OSPF adjacencies |
| `/interface ipsec active-peers print` | Check VPN tunnel status |
| `/tool sniffer quick protocol=ospf` | Capture OSPF traffic |
| `/log print where topics=ospf,ipsec` | Filter relevant logs |

---

## 10. Common Pitfalls to Avoid
- **Pitfall**: Assuming default `broadcast` network type works for VPN tunnels.  
  **Fix**: Always use `point-to-point` for IPsec/GRE tunnels.
- **Pitfall**: Forgetting to encrypt OSPF (proto 89) in IPsec policies.  
  **Fix**: Explicitly allow protocol 89 in phase2 policies.
- **Pitfall**: Ignoring MTU mismatches between physical and tunnel interfaces.  
  **Fix**: Set `mtu=1400` and clamp TCP MSS on VPN interfaces.
```
