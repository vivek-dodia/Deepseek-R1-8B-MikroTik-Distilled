---
generated_at: 2025-02-03T16:40:28.481661
topic: RIP
category: Routing
version: 7.x
scale: SMB
level: Basic
subnet: 172.28.145.32/28
scenario: OSPF Adjacency Problems
environment: Remote Site
affected_users: 682
duration: 21 hours
---

# Analysis Process
Alright, let's tackle this MikroTik RIP troubleshooting scenario. First, I need to make sure I understand all the requirements. The user wants a detailed scenario focused on OSPF adjacency problems in a Remote Site SMB network using RouterOS 7.x. The subnet given is 172.28.145.32/28, with 682 users affected over 21 hours. 

Starting with the initial problem report: symptoms might include users unable to access resources, routing tables missing OSPF routes, and OSPF neighbors not forming adjacencies. I should note the time of the report and who reported it, maybe the network admin.

Next, the environment description. The network topology needs to be in Mermaid format. The SMB network probably has a main office and a remote site. The remote site has a MikroTik router (RouterOS 7.x) connected via a WAN link. The subnet is for the LAN side. Let me sketch that out with Mermaid nodes and connections.

Initial assessment steps: check OSPF status, verify interfaces, look for configuration mismatches. Using CLI commands like `/routing ospf instance print` and `/routing ospf neighbor print` to see neighbors. Also check interface configurations, MTU settings, and network statements.

For the debugging process, I need to go step by step. Check if OSPF is enabled, verify network areas, authentication settings. Look at logs with `/log print where topics=ospf`. Maybe there are authentication errors or hello timer mismatches. Use commands like `/routing ospf interface print` to check interface parameters. Compare configurations between routers. If the MTU is mismatched, that could be an issue. Also, check for passive interfaces mistakenly configured.

Key findings might be a mismatch in OSPF authentication or hello/dead timers. Root cause could be that one router was configured with MD5 authentication while the other used none. Or maybe the subnet mask on the interface doesn't match, causing neighbors to not recognize each other.

Solution steps would involve correcting the authentication settings on both routers, ensuring timers match, and adjusting MTU if necessary. Update the OSPF configuration and possibly the interface settings. Then, restart OSPF processes or reboot routers if needed.

Verification would involve checking OSPF neighbors again, ensuring routes are exchanged, and testing connectivity. Prevention measures include standardizing configurations, implementing monitoring, and regular audits.

Including CLI commands with code blocks, making sure to comment on complex ones. Also, show before and after configurations where relevant. Common pitfalls might be forgetting authentication, mismatched timers, or passive interfaces.

Wait, the user mentioned the topic is RIP but the scenario is OSPF Adjacency Problems. That's a conflict. Oh, maybe a typo? The topic should be OSPF. I'll proceed with OSPF as the scenario states OSPF Adjacency Problems. But need to confirm. If it's a mistake, but the scenario is correct, proceed with OSPF.

Another point: the subnet is /28, which is a small subnet. The remote site's LAN is 172.28.145.32/28, providing 14 usable addresses. But 682 users are affected. That seems inconsistent. Maybe the subnet is for the link between routers? Or perhaps the remote site has multiple subnets, but the problem subnet is the one connected via OSPF. Maybe the remote site router connects to a larger network, but the OSPF issue is on the WAN link with that /28 subnet. Need to clarify in the topology.

In the network topology, the remote site router's WAN interface might be on 172.28.145.34/28, connected to the main office router's interface 172.28.145.33/28. The LAN side of the remote router could have a larger subnet for the 682 users. But the problem is with the OSPF adjacency over the WAN link using the /28 subnet.

So in the Mermaid diagram, the Main Office Router and Remote Site Router connected via a WAN link with the given subnet. The Remote Site has a LAN with 682 users.

When checking OSPF configuration, ensure that the WAN interfaces are included in the OSPF network statements. Maybe the Remote Site router's OSPF is not advertising the correct networks, or the adjacency isn't forming due to interface issues.

In the debugging process, checking OSPF hello packets are being sent/received. Use packet sniffer if necessary. Also, verify that both routers are in the same area. Authentication type (none vs MD5) and key mismatches are common issues.

If the problem was ongoing for 21 hours, maybe a recent configuration change introduced the error, like adding authentication without updating both ends.

Including log examples where OSPF adjacency fails due to authentication. For example, "OSPF: hello packet from 172.28.145.33: authentication mismatch".

Then, the solution would be to configure matching authentication on both routers. Show before (no auth) and after (auth setup) configurations.

Common pitfalls: assuming OSPF is enabled by default, not checking all parameters, forgetting to commit changes after configuration.

I think that covers the main points. Need to structure each section as per the user's request, using markdown, CLI commands in code blocks, etc. Make sure to include all 10 sections.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: OSPF Adjacency Problems

## 1. Initial Problem Report and Symptoms
**Reported By**: Network Administrator  
**Time**: 21 hours ago  
**Symptoms**:
- Remote site users (682) cannot access central resources.
- OSPF routes missing from routing tables.
- OSPF neighbors stuck in `Init` or `ExStart` state.
- Intermittent packet loss between remote site and HQ.

---

## 2. Environment Description and Network Topology
**Network Type**: SMB (Small/Medium Business)  
**RouterOS Version**: 7.8  
**Subnet**: `172.28.145.32/28` (WAN link between HQ and Remote Site)  
**Remote Site**: Single MikroTik RB4011 router, connected via ISP to HQ.  

```mermaid
graph TD
  A[Main Office Router (OSPF Area 0)] -->|WAN: 172.28.145.33/28| B[Remote Site Router (OSPF Area 0)]
  B -->|LAN: 10.10.0.0/24| C[Remote Users (682)]
```

---

## 3. Initial Assessment Steps
1. **Verify OSPF Status**:
   ```bash
   /routing ospf neighbor print
   # Output: State=Init, Address=172.28.145.33
   ```
2. **Check Interface Status**:
   ```bash
   /interface print
   # Output: ether1 (WAN) - running, MTU=1500
   ```
3. **Confirm OSPF Configuration**:
   ```bash
   /routing ospf instance print
   /routing ospf network print
   ```

---

## 4. Detailed Debugging Process
### Step 1: Check OSPF Logs
```bash
/log print where topics=ospf
# Output: "OSPF: hello from 172.28.145.33: authentication mismatch"
```

### Step 2: Verify Authentication Settings
**Remote Site Router**:
```bash
/routing ospf interface template print
# Before:
#   authentication=md5, auth-key=wrongkey
```

**HQ Router**:
```bash
/routing ospf interface template print
# Before:
#   authentication=md5, auth-key=correctkey
```

### Step 3: Validate MTU and Network Statements
```bash
/interface ethernet print
# MTU=1500 on both ends

/routing ospf network print
# Output: network=172.28.145.32/28 area=backbone
```

---

## 5. Key Findings and Root Cause Analysis
**Root Cause**:  
- **Authentication Mismatch**: Remote site used `auth-key=wrongkey`, while HQ used `auth-key=correctkey`.  
- **Subnet Mask Typo**: Initial configuration had `/29` instead of `/28` in OSPF network statements (fixed prior to escalation).  

---

## 6. Solution Implementation Steps
1. **Update Authentication Key**:
   ```bash
   /routing ospf interface template set [find where interface=ether1] authentication=md5 auth-key=correctkey
   ```
2. **Synchronize OSPF Timers**:
   ```bash
   /routing ospf interface template set [find] hello-interval=10 dead-interval=40
   ```

---

## 7. Verification Process
1. **Confirm OSPF Adjacency**:
   ```bash
   /routing ospf neighbor print
   # After: State=Full, Address=172.28.145.33
   ```
2. **Validate Routes**:
   ```bash
   /ip route print where protocol=ospf
   # Output: 10.10.0.0/24 via OSPF
   ```

---

## 8. Prevention Measures
- Standardize OSPF templates across all routers.
- Use automation tools (e.g., Ansible) for configuration consistency.
- Enable OSPF logging for proactive monitoring:
  ```bash
  /system logging add topics=ospf
  ```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing ospf neighbor print` | Check OSPF neighbor states |
| `/log print where topics=ospf` | Filter OSPF-specific logs |
| `/routing ospf interface template set` | Modify OSPF interface settings |

---

## 10. Common Pitfalls to Avoid
- **Mismatched Authentication**: Ensure MD5 keys match on both ends.
- **Passive Interfaces**: Avoid marking WAN interfaces as `passive`.
- **MTU Mismatches**: Confirm MTU consistency (e.g., 1500 vs. 1492 for PPPoE).
```
