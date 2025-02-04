---
generated_at: 2025-02-03T15:20:56.020439
topic: OSPF
category: Routing
version: 6.x
scale: SMB
level: Advanced
subnet: 172.22.42.0/24
scenario: Connectivity Loss
environment: Branch Office
affected_users: 710
duration: 4 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for OSPF in a Small/Medium Business (SMB) branch office environment. The RouterOS version is 6.x, and the subnet involved is 172.22.42.0/24. The problem is connectivity loss affecting 710 users for 4 hours. Let me break down each section as per the user's requirements.

Starting with the Initial Problem Report and Symptoms. The users can't reach the main office resources. So, symptoms would include OSPF neighbors down, routes missing from the routing table. Maybe some logs showing OSPF errors. Need to mention the time frame and the impact.

Next, the Environment Description and Network Topology. The branch has a MikroTik router (probably RouterOS v6.49.7) connected to the main office via a WAN link. The local subnet is 172.22.42.0/24. The Mermaid diagram should show the branch router connected to the main office router, and the local LAN. Maybe the OSPF area is backbone (area 0.0.0.0), interfaces involved. I need to make sure the Mermaid syntax is correct.

Initial Assessment Steps: First, check OSPF neighbor status with /routing ospf neighbor print. Then look at the routing table with /ip route print where ospf=yes. Check interface statuses with /interface print. Review logs for OSPF errors with /log print where message~"OSPF". Also, verify basic connectivity, like pinging the main office gateway.

Detailed Debugging Process: Start with checking OSPF neighbors. If neighbors are down, check if the interfaces are configured correctly. Verify OSPF configuration: networks, area, authentication. Maybe there's a mismatch in area IDs or authentication settings. Use commands like /routing ospf interface print to see interface settings. Look for passive interfaces that shouldn't be passive. Check if the WAN interface is included in OSPF. Maybe the MTU is mismatched between routers. Use /interface ethernet print to check MTU. Also, look at OSPF logs in more detail. Maybe debug with /routing ospf log print where level=debug. 

Key Findings and Root Cause: Suppose the issue is that the WAN interface wasn't included in the OSPF configuration, so the neighbor couldn't form. Or maybe there was an authentication mismatch. For example, the branch router had authentication set to simple password, but the main office used MD5. That would prevent adjacency. Or maybe the network statement was missing for the WAN interface.

Solution Implementation: Add the missing OSPF network for the WAN interface or correct the authentication settings. For example, updating the OSPF interface configuration to include the WAN interface with the correct authentication. Then, maybe reset OSPF processes with /routing ospf instance reset.

Verification: After fixing, check neighbors again, ensure routes are present. Ping tests to main office resources. Confirm users can access applications.

Prevention Measures: Regular configuration audits, enable OSPF logging, use consistent authentication, document network changes, implement monitoring tools like The Dude.

Related Commands: List the commands used in troubleshooting, like neighbor print, route print, interface print, etc.

Common Pitfalls: Forgetting to include interfaces in OSPF, mismatched authentication, MTU mismatches, passive interfaces incorrectly set, area ID mismatches.

Need to make sure CLI commands are in code blocks, with comments if necessary. Include example log outputs, like authentication failure logs. Show before and after configurations where relevant, such as OSPF interface settings before and after adding the WAN interface.

Wait, in RouterOS 6.x, OSPF is configured under /routing ospf. The interfaces are added under /routing ospf interface. So if the WAN interface was missing there, OSPF wouldn't form. Let me structure the example around that.

Another possibility: maybe the subnet mask on the WAN interface is different, causing OSPF not to recognize the neighbor. But the user specified the subnet as 172.22.42.0/24, which is the local LAN. The WAN link might be a different subnet, say 10.10.10.0/30. If the OSPF network configuration on the branch router doesn't include the WAN subnet (10.10.10.0/30), then OSPF won't advertise over that link. So in the OSPF network configuration, they might have only 172.22.42.0/24, missing the WAN network. Hence, neighbors can't form.

So in the initial configuration, the OSPF networks might be set to 172.22.42.0/24 (LAN) but not the WAN subnet. The fix would be adding the WAN subnet to OSPF interfaces.

Let me structure the scenario with that root cause. So the key finding is missing OSPF interface for the WAN, leading to no adjacency. Then, the solution is adding that interface.

In the before configuration, /routing ospf interface print might show only the LAN interface. After, it includes the WAN interface (e.g., ether1) with area backbone.

Also, check authentication. If the main office uses authentication but the branch doesn't, that's a problem. So maybe in the initial setup, there's no authentication, but the main office requires it. So adding authentication settings would be part of the fix.

But the user mentioned SMB and branch office. Maybe the common issue is just missing network in OSPF configuration. Let's go with that for simplicity.

So, initial problem: OSPF neighbors down because the WAN interface isn't included in OSPF. Therefore, the branch router isn't forming adjacency with the main office router. Hence, routes aren't exchanged, leading to connectivity loss.

In the detailed debugging, when they check /routing ospf neighbor print, there are no neighbors. Then checking /routing ospf interface print shows only LAN interface. Then, adding the WAN interface to OSPF.

Another thing: maybe the OSPF is configured on the LAN interface, which is passive. But passive interfaces don't send OSPF hello packets. Wait, in RouterOS, if you set an interface as passive, it won't send OSPF hellos. So if the WAN interface is set to passive by mistake, that would prevent neighbor relationships. But in this case, the WAN interface wasn't added at all.

Alternatively, the network is configured as 172.22.42.0/24, but the WAN interface's IP is 10.10.10.1/30, which isn't included in any OSPF network statement. So the OSPF process doesn't run on that interface.

So the solution is adding the WAN network to OSPF interfaces. For example:

Before:
/routing ospf network add network=172.22.42.0/24 area=backbone

After:
/routing ospf network add network=172.22.42.0/24 area=backbone
/routing ospf network add network=10.10.10.0/30 area=backbone

Or, using interface configuration instead of network statements. In RouterOS, OSPF can be configured with networks or interfaces. If using interface configuration, adding the WAN interface to OSPF interfaces.

So, in the initial setup, maybe the OSPF was only set up on the LAN interface (ether2), and the WAN interface (ether1) wasn't included. Hence, no OSPF adjacency over ether1.

Therefore, in the OSPF interface configuration, ether1 was missing. The fix is adding it.

Yes, that makes sense. So the detailed steps would involve checking OSPF interfaces, noticing that the WAN isn't listed, and adding it.

Now, putting all this together into the sections as specified. Making sure each part is covered with appropriate commands, logs, and configurations.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF Connectivity Loss

## 1. Initial Problem Report and Symptoms
**Report**: Branch office users report inability to access main office resources (ERP, file servers).  
**Symptoms**:
- OSPF adjacency lost between branch and main office routers
- Missing OSPF routes in routing table (`172.22.42.0/24` isolated)
- Logs show OSPF authentication failures
- 710 users affected for 4 hours

---

## 2. Environment Description and Network Topology
**Network Scale**: SMB (5 routers, 50+ devices)  
**Subnet**: `172.22.42.0/24` (Branch LAN)  
**RouterOS Version**: 6.49.7  

```mermaid
graph TD
  A[Branch Router (RB750Gr3)] -- OSPF/eth1-WAN --> B[Main Office Router (CCR1009)]
  A --> C[Switch]
  C --> D[172.22.42.0/24 Users]
  classDef router fill:#e6f3ff,stroke:#004c99;
  class A,B router;
```

---

## 3. Initial Assessment Steps
1. **Check OSPF neighbors**:
```bash
/routing ospf neighbor print
# Output: No neighbors in FULL state
```

2. **Verify OSPF routes**:
```bash
/ip route print where ospf=yes
# Output: No OSPF routes present
```

3. **Interface status check**:
```bash
/interface print 
# eth1 (WAN): running, MTU=1500
```

4. **OSPF logs**:
```bash
/log print where message~"OSPF"
# Sample log: "OSPF: packet dropped: authentication mismatch"
```

---

## 4. Detailed Debugging Process
**Step 1**: Verify OSPF configuration:
```bash
/routing ospf instance print
# Authentication: md5 (Main Office) vs simple (Branch)
```

**Step 2**: Check interface participation:
```bash
/routing ospf interface print
# eth1 missing from OSPF interfaces
```

**Step 3**: Validate MTU consistency:
```bash
/interface ethernet print 
# Both ends: MTU=1500 (No fragmentation issues)
```

**Step 4**: Debug authentication:
```bash
/routing ospf log set level=debug
/log print where message~"OSPF"
# Sample debug: "OSPF: Hello from 10.10.10.2: MD5 auth failed"
```

---

## 5. Key Findings and Root Cause Analysis
**Root Cause**: Authentication mismatch between branch (simple password) and main office (MD5).  
**Secondary Issue**: WAN interface (`eth1`) not included in OSPF configuration.  

---

## 6. Solution Implementation Steps
**Before Configuration**:
```bash
/routing ospf instance set [find] authentication=simple authentication-key=pass123
/routing ospf interface add interface=eth2
```

**After Configuration**:
```bash
/routing ospf instance set [find] authentication=md5 authentication-key=securekey789
/routing ospf interface add interface=eth1
```

**Apply Changes**:
```bash
/routing ospf instance reset
```

---

## 7. Verification Process
1. Confirm neighbor adjacency:
```bash
/routing ospf neighbor print
# STATE: FULL
```

2. Validate routes:
```bash
/ip route print where ospf=yes
# 0.0.0.0/0 via 10.10.10.2 (main office)
```

3. End-to-end test:
```bash
/ping 172.30.0.1 (Main Office Gateway)
# 10/10 packets received
```

---

## 8. Prevention Measures
- Implement configuration templates for OSPF authentication
- Enable OSPF logging with `/system logging add topics=ospf`
- Conduct quarterly network audits using `/export verbose`
- Deploy The Dude for real-time OSPF monitoring

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | List OSPF adjacencies |
| `/ip route print where ospf` | Show OSPF-learned routes |
| `/routing ospf log set level=debug` | Enable debug logging |
| `/routing ospf instance reset` | Soft-restart OSPF |

---

## 10. Common Pitfalls to Avoid
1. **Authentication Mismatches**: Ensure identical auth methods (simple/md5) across peers
2. **Passive Interfaces**: Avoid marking WAN interfaces as passive
3. **Network Statements**: Always include WAN interfaces in OSPF
4. **MTU Discrepancies**: Verify MTU matches on both ends of OSPF links
5. **Area Mismatches**: Confirm all interfaces are in the same OSPF area (backbone)
```
