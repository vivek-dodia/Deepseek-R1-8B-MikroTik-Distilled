---
generated_at: 2025-02-03T16:07:50.801491
topic: BGP
category: Routing
version: 7.x
scale: SOHO
level: Basic
subnet: 192.168.238.128/25
scenario: High CPU Usage
environment: Campus Network
affected_users: 251
duration: 8 hours
---

# Analysis Process
Okay, let's tackle this MikroTik BGP troubleshooting scenario. The user wants a detailed scenario for SOHO with high CPU usage. Hmm, first, I need to outline each section as per the requirements. Let's start with the initial problem report. The symptoms include high CPU, BGP flapping, and users losing access. Affected users are 251, which is a lot for a SOHO. The duration is 8 hours, so it's a prolonged issue.

Next, the environment is a campus network with a /25 subnet. The network topology needs to be in Mermaid. Let me sketch that out. The SOHO router connects to an ISP and a campus core router. The clients are on 192.168.238.128/25. Maybe a default route to ISP and BGP to the campus core. Possible iBGP or eBGP here? Probably eBGP since it's connecting to the campus core.

Initial assessment steps. Check CPU usage with /system resource print. Look at BGP sessions with /routing bgp session print. Check routes and logs. Maybe the BGP sessions are flapping, causing route churn and high CPU. Also, check for any firewall rules that might be causing traffic to hit the CPU, like complex NAT or filter rules.

Debugging process. Use commands like /tool profile to start profiling CPU. Check BGP updates with /routing bgp updates print. Logs might show session state changes. Maybe there's a route reflector issue or too many prefixes being advertised. If the SOHO router is receiving a full BGP table, that's a problem. Also, check if there's a routing loop causing excessive updates.

Key findings could be that the SOHO router is receiving too many BGP routes, overwhelming the CPU. Or maybe a misconfiguration in BGP timers leading to constant session resets. Root cause would be accepting full BGP tables without proper filtering, leading to high CPU from processing updates.

Solution: Implement route filtering to only accept necessary prefixes. Adjust BGP timers if needed. Maybe use prefix lists or route-maps. Also, optimize firewall rules to offload traffic.

Verification would involve checking CPU usage post-fix, ensuring BGP sessions are stable, and routes are properly filtered. Prevention measures include proper BGP configuration best practices, route filtering, and regular monitoring.

Common pitfalls might be not filtering routes, using default BGP settings unsuitable for SOHO, or not monitoring CPU usage trends.

I need to include CLI commands for each step. For example, checking BGP sessions, enabling profiling, looking at routes. Also, show before and after configurations, like adding a prefix list to filter routes.

Wait, in a SOHO environment, it's unlikely they need full BGP tables. So the core router might be sending too many routes. The fix would be to configure inbound route filtering on the MikroTik to only allow the specific subnet or local routes.

Also, MikroTik's BGP in RouterOS 7.x might have different commands. Let me confirm the exact syntax for BGP configuration and filtering. Maybe using /routing filter add chain=... to drop unwanted prefixes.

Including log examples where BGP sessions go up/down frequently. And before/after CPU graphs from the resource tool.

Yes, this structure makes sense. Now, putting it all together with the required sections, commands, and explanations.

# Troubleshooting Guide
```markdown
# BGP Troubleshooting Scenario: High CPU Usage in MikroTik RouterOS 7.x

## 1. Initial Problem Report and Symptoms
**Report**: Campus network users report intermittent internet access and slow internal resource access.  
**Symptoms**:
- Router CPU consistently at 90-100% utilization
- BGP session flapping observed between SOHO router and campus core
- 251 users experiencing packet loss (>30% on traceroute)
- High routing table churn observed
- Issue persists for 8 hours since morning network maintenance

---

## 2. Environment Description & Network Topology

```mermaid
graph TD
    A[SOHO Router<br>(MikroTik RB4011)<br>192.168.238.129/25] -->|BGP AS 65001| B[Campus Core Router<br>(AS 65000)]
    A -->|Default Route| C[ISP Gateway<br>203.0.113.1]
    D[Client VLAN<br>192.168.238.128/25] --> A
    B -->|iBGP| E[Other Campus Routers]
```

---

## 3. Initial Assessment Steps
1. **Verify CPU Load**:
   ```bash
   /system resource print
   ```
   **Output**:
   ```txt
             cpu: 98%
       free-memory: 54.3MiB
   ```

2. **Check BGP Session Status**:
   ```bash
   /routing bgp session print
   ```
   **Output**:
   ```txt
   0 AS=65000 remote-address=10.10.10.1 established=8m12s uptime=00:07:54 
     prefixes-received=120000 state=established
   ```

3. **Identify Top CPU Consumers**:
   ```bash
   /tool profile
   ```

---

## 4. Detailed Debugging Process
**Step 1: Capture BGP Update Traffic**
```bash
/routing bgp updates print
```
**Output**:
```txt
[status=established] 10.10.10.1: Received UPDATE with 15,000 prefixes
```

**Step 2: Analyze Route Count**
```bash
/ip route print count-only where bgp
```
**Output**: `128743 routes`

**Step 3: Check BGP Filters**
```bash
/routing filter print
```
**Output**: *No active BGP route filters*

**Step 4: Capture Traffic Sample**
```bash
/tool sniffer quick port=179 protocol=tcp
```

---

## 5. Key Findings & Root Cause
**Findings**:
1. Receiving full Internet routing table (120k+ routes) from campus core
2. No route filtering configured
3. CPU spikes correlate with BGP UPDATE messages
4. Default BGP settings with aggressive keepalive (30s)

**Root Cause**:  
SOHO router incorrectly configured to receive full BGP tables from campus core, exceeding hardware capacity (RB4011 max recommended BGP routes: 50k).

---

## 6. Solution Implementation
**Before** (Problematic Config):
```bash
/routing bgp instance
set default as=65001 router-id=192.168.238.129
/routing bgp peer
add name=core remote-address=10.10.10.1 remote-as=65000
```

**After** (Corrected Config):
```bash
# Add route filter chain
/routing filter add chain=bgp-in rule="if (dst in 192.168.238.128/25) { accept } else { reject }"

# Configure BGP peer with filters
/routing bgp peer
set core input.filter-chain=bgp-in output.filter-chain=bgp-in
```

---

## 7. Verification Process
1. **Check CPU Post-Fix**:
   ```bash
   /system resource print
   ```
   **Output**:
   ```txt
             cpu: 24%
   ```

2. **Validate Route Count**:
   ```bash
   /ip route print count-only where bgp
   ```
   **Output**: `2 routes`

3. **BGP Session Stability**:
   ```bash
   /routing bgp session print
   ```
   **Output**:
   ```txt
   established=2h34m uptime=02:33:12
   ```

---

## 8. Prevention Measures
1. Implement BGP route filtering for all peers
2. Set reasonable BGP timers:
   ```bash
   /routing bgp peer set core hold-time=3m keepalive-time=1m
   ```
3. Enable BGP monitoring:
   ```bash
   /tool graphing interface add
   /tool bandwidth-server
   ```
4. Implement CPU usage alerts

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing bgp summary` | Show BGP session summary |
| `/routing filter` | Configure route filtering |
| `/tool profile` | CPU profiling tool |
| `/ip route export` | Export routing table |

---

## 10. Common Pitfalls to Avoid
1. **Full BGP Tables on SOHO Hardware**  
   *Never accept full tables on devices with <1GB RAM*

2. **Missing Route Refresh**  
   ```bash
   /routing bgp peer set core capability-refresh=yes
   ```

3. **Aggressive Timers**  
   Avoid sub-minute keepalives in campus environments

4. **Ignoring Soft Reconfig**  
   ```bash
   /routing bgp peer set core soft-reconfiguration=yes
   ```
```
