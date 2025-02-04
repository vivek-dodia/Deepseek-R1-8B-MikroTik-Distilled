---
generated_at: 2025-02-03T16:49:43.097312
topic: RIP
category: Routing
version: 7.x
scale: ISP
level: Expert
subnet: 10.21.248.224/27
scenario: DHCP Lease Problems
environment: Edge Location
affected_users: 162
duration: 18 hours
---

# Analysis Process
Okay, let's tackle this MikroTik RIP troubleshooting scenario. The user wants a detailed ISP-level problem where DHCP leases are an issue. First, I need to recall how RIP works in RouterOS 7.x. Since the subnet is /27, that's a small block, maybe an edge location. The problem is DHCP leases affecting 162 users for 18 hours. 

Starting with the initial problem report. Users can't get IPs, so symptoms would include no internet, maybe DHCP discovery failures. Then the environment: ISP edge location using RIP. Need a Mermaid diagram showing the edge router connected to core and clients via a switch. The edge router handles DHCP and RIP.

Initial assessment steps: Check DHCP server status, leases, IP pool. Then look at RIP configuration to ensure routes are advertised. Maybe RIP isn't pushing the DHCP subnet to the core, so clients get IPs but no route out. 

Debugging process: Use CLI commands like /ip dhcp-server lease print, /routing rip interface print. Check if the RIP interface is correctly set. Maybe the network isn't included in RIP. Logs might show RIP updates not being sent.

Key findings: The DHCP subnet 10.21.248.224/27 isn't advertised via RIP, so the core doesn't know the route. Thus, even if clients get IPs, traffic can't route back. 

Solution: Add the network to RIP configuration. Verify with /routing rip network add network=10.21.248.224/27. Then check RIP routes and DHCP leases again.

Verification: Test DHCP request, check lease, ping external IP, traceroute. Prevention measures: Include all relevant networks in RIP, monitor routing tables, audit configs.

Common pitfalls: Forgetting to advertise DHCP subnets in dynamic routing protocols, not checking route propagation after DHCP changes.

I need to make sure the CLI commands are accurate for version 7.x. For example, in RIP, the networks are specified under /routing rip network. Also, log examples should show RIP updates missing the subnet. Before and after configs would show the network added to RIP.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: RIP/DHCP Lease Issues

## 1. Initial Problem Report and Symptoms
**Report:** 162 users at edge location report no internet access for 18 hours. DHCP server assigns IPs but no connectivity.  
**Symptoms:**
- Clients receive 169.254.x.x APIPA addresses
- Some clients get 10.21.248.224/27 addresses but no internet
- RIP routes not visible in core routers
- High DHCP discover/request counts in logs

## 2. Environment Description
**Network Topology:**
```mermaid
graph TD
    A[Core Router] --> B[Edge Router (RIP Speaker)]
    B --> C[Layer2 Switch]
    C --> D[Client Pool 1]
    C --> E[Client Pool 2]
    C --> F[Client Pool 3]
```
- **Edge Router:** RB4011 (ROS v7.11)
- **DHCP Pool:** 10.21.248.225-254/27
- **RIP Configuration:** v2, broadcast, authentication=md5
- **Interfaces:** ether1 (uplink), ether2-ether8 (client ports)

## 3. Initial Assessment Steps
1. Verify DHCP server status:
```bash
/ip dhcp-server print
# Status: running
```
2. Check lease allocation:
```bash
/ip dhcp-server lease print where status != bound
# 200 leases in "waiting" state
```
3. Confirm IP pool utilization:
```bash
/ip pool used print
# 10.21.248.225-254: 30 addresses used
```

## 4. Detailed Debugging Process
**Step 1: Check RIP route propagation**
```bash
/routing rip route print
# OUTPUT:
# Flags: A - ACTIVE
# Columns: DST-ADDRESS        NEXTHOP         GATEWAY
#          0.0.0.0/0          10.21.248.225   ether1
# Missing 10.21.248.224/27 network
```

**Step 2: Analyze interface participation in RIP**
```bash
/routing rip interface print
# OUTPUT:
#   INTERFACE      VERSION AUTHENTICATION
# 0 ether1         v2      md5
# 1 bridge-local   v2      none
```

**Step 3: Verify RIP network advertisements**
```bash
/routing rip network print
# OUTPUT:
# NETWORK          AUTHENTICATION
# 192.168.0.0/24   none
# Missing 10.21.248.224/27 network
```

**Step 4: Check DHCP server routing mark**
```bash
/ip dhcp-server network print
# OUTPUT:
# ADDRESS           GATEWAY         DNS
# 10.21.248.224/27 10.21.248.225   1.1.1.1
# No routing-mark specified
```

## 5. Key Findings & Root Cause
**Root Cause:**  
DHCP subnet `10.21.248.224/27` not advertised via RIP due to:
1. Missing RIP network declaration for DHCP subnet
2. Default route not being redistributed properly
3. DHCP server using main routing table while RIP used separate table

**Impact:**  
- Core routers unaware of client subnet
- Return traffic dropped at network edge
- DHCP ACKs contained invalid gateway info

## 6. Solution Implementation
**Before Configuration:**
```bash
/routing rip network print
# No 10.21.248.224/27 network
```

**Implementation Steps:**
1. Add DHCP subnet to RIP:
```bash
/routing rip network add network=10.21.248.224/27
```
2. Modify DHCP server routing mark:
```bash
/ip dhcp-server network set 0 routing-mark=RIP_Table
```
3. Force RIP redistribution:
```bash
/routing rip interface reset [find where interface=ether1]
```

**After Configuration:**
```bash
/routing rip route print
# Now shows 10.21.248.224/27 as ACTIVE
```

## 7. Verification Process
1. Client lease test:
```bash
/ip dhcp-server lease print where active=yes
# Shows 162 bound leases
```
2. Route propagation check:
```bash
/tool traceroute 10.21.248.230
# 1 10.21.248.225 5ms
# 2 10.100.0.1 (core) 10ms
```
3. Packet capture validation:
```bash
/tool sniff packet interface=ether1 protocol=udp port=520
# Shows RIP updates containing 10.21.248.224/27
```

## 8. Prevention Measures
1. Implement configuration audit script:
```bash
:global ripSubnets [/routing rip network get [find] value-name=network]
:if ([:len [:find $ripSubnets "10.21.248.224/27"]] = 0) do={ ... }
```
2. Enable RIP monitoring:
```bash
/system scheduler add interval=5m name="RIP Check" on-event="/log info \"RIP Networks: \$[/routing rip network print]\""
```
3. Implement DHCP-RIP binding:
```bash
/ip pool set [find name=client_pool] rip-include=yes
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing rip monitor` | Live RIP update monitoring |
| `/ip dhcp-server lease make-static` | Convert stuck leases |
| `/tool profile` | CPU/memory utilization check |

## 10. Common Pitfalls to Avoid
1. **DHCP/Routing Table Mismatch**  
   Always match `routing-mark` between DHCP and routing protocols

2. **RIP Version Conflicts**  
   Ensure consistent v2 configuration across all network devices

3. **Subnet Mask Propagation**  
   Always advertise exact /27 mask in RIP networks list

4. **Authentication Mismatches**  
   Verify MD5 keys match on all RIP-speaking routers:
```bash
/routing rip interface print detail where authentication=md5
```
```
