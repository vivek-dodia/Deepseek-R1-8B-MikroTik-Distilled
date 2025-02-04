---
generated_at: 2025-02-03T19:48:13.537491
topic: Static Routes
category: Routing
version: 6.x
scale: SMB
level: Basic
subnet: 172.17.111.0/24
scenario: DHCP Lease Problems
environment: Remote Site
affected_users: 527
duration: 4 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario based on the user's specifications. Let me break down each section they want and think through how to approach them.

First, the topic is Static Routes, and the problem is DHCP Lease issues. The network is a remote SMB site with a subnet 172.17.111.0/24. The RouterOS version is 6.x, which is a bit older. Affected users are 527, and the duration is 4 hours. 

Starting with the Initial Problem Report: Users can't get IPs via DHCP. Symptoms might include no IP assignments, some getting APIPA addresses, maybe some intermittent leases. Need to make sure the symptoms align with static route issues affecting DHCP.

Environment Description: They want a Mermaid diagram. The remote site has a router connected to a main office via a site-to-site VPN. The local subnet is 172.17.111.0/24, and the DHCP server is at the main office (maybe 10.10.10.1). The MikroTik router at the remote site (172.17.111.1) connects to a switch and then to users. The static route is pointing to the main office's DHCP server. Wait, but if the DHCP server is remote, the static route is crucial. If that's missing or wrong, DHCP requests won't reach the server.

Initial Assessment Steps: Check DHCP server status, leases, maybe ping the DHCP server from the router. Verify static routes. Look for configuration errors. Check interface statuses. Maybe check firewall rules blocking DHCP traffic.

Debugging Process: Use CLI commands like /ip route print to check static routes. Maybe the route to the main office's subnet (where DHCP server is) is missing or has the wrong gateway. Check DHCP client or server settings on the router. If the remote site's router is supposed to relay DHCP, maybe the helper address is missing. Since it's RouterOS 6.x, the DHCP relay setup might be different. Also, look at the firewall: are UDP ports 67 and 68 allowed? Logs from the DHCP server or firewall logs showing dropped packets.

Key Findings: Suppose the static route to the main office's DHCP server subnet was missing. So the DHCP requests from clients are broadcast, but the relay agent (if configured) needs to forward them to the DHCP server. Without a route, those packets can't reach the server. Root cause is the missing static route causing DHCPDISCOVER messages not to reach the server.

Solution Implementation: Add the static route via the site-to-site VPN interface. If using DHCP relay, ensure the relay is pointing to the correct server IP. Maybe adjust firewall rules. Show before and after configs for the static route.

Verification: After adding the route, check DHCP leases. Maybe release and renew on a client, check logs. Use packet sniffer on the router to see if DHCP traffic is going through.

Prevention Measures: Document static routes, implement monitoring for route changes, regular config backups, maybe move DHCP server locally if feasible to reduce dependency on routes.

Related Commands: /ip route print, /ip route add, /log print, /tool sniffer, /ip dhcp-server lease print.

Common Pitfalls: Forgetting to set routes after changes, not checking firewall rules, assuming DHCP relay is set up correctly without verification.

Wait, the user mentioned that the problem is DHCP Lease Problems, but the topic is Static Routes. So the issue is likely that the static route necessary for DHCP communication is missing or misconfigured. For example, if the DHCP server is in a different subnet (like the main office), the remote site's router needs a static route to reach that subnet. If that route is missing, DHCP requests from clients (which are relayed by the router) can't reach the server, hence no leases.

In the network topology, the remote site's router connects to the main office via VPN. The DHCP server is in the main office's network. So the static route on the remote router should direct traffic to the main office's subnet (where the DHCP server is) through the VPN tunnel. If that route isn't present, the DHCP relay (if configured) can't forward the requests, leading to the problem.

So in the scenario, the static route to the main office's subnet (10.10.10.0/24) via the VPN gateway is missing. Therefore, when the remote router receives DHCP requests from clients, it can't route them to the DHCP server. Clients don't get IPs, leading to APIPA addresses.

In the initial assessment, when they check /ip route print, that route isn't there. Then they add it, and things start working.

Need to make sure the static route's gateway is correct (pointing to the VPN interface or the correct IP). Also, check if the VPN itself is up, but maybe that's a separate issue. Since the problem is static routes, the VPN is assumed to be operational.

Another angle: Maybe the static route exists but is incorrect, like wrong gateway or distance. Or there's a conflicting route with a lower distance.

But given the scenario, the most straightforward root cause is a missing static route to the DHCP server's network.

# Troubleshooting Guide
```markdown
# MikroTik RouterOS Troubleshooting Scenario: Static Routes & DHCP Lease Problems

## 1. Initial Problem Report and Symptoms
**Report:**  
Remote site users report inability to obtain IP addresses via DHCP. APIPA (169.254.x.x) addresses observed on workstations.

**Symptoms:**  
- 100% of 527 users offline  
- DHCP server unreachable from client subnet  
- No active leases in DHCP server logs  
- Intermittent `DHCPDISCOVER` timeouts in packet captures  

---

## 2. Environment Description & Network Topology
**Network Type:** SMB Remote Site with Hub-Spoke VPN to HQ  
**Subnet:** 172.17.111.0/24 (Remote Site)  
**RouterOS Version:** 6.49.7 (stable)  

```mermaid
graph TD
  A[Remote Site Router<br>(172.17.111.1/24)] -->|Site-to-Site VPN| B[Main Office Router<br>(10.10.10.1/24)]
  A --> C[Local Switch]
  C --> D[527 Users]
  style A fill:#e0f7fa,stroke:#333
  style B fill:#f0f4c3,stroke:#333
```

---

## 3. Initial Assessment Steps
1. Confirm VPN tunnel status:
   ```bash
   /interface pptp-client monitor [find where name="HQ-VPN"]
   ```
2. Check routing table for DHCP server path:
   ```bash
   /ip route print where dst-address=10.10.10.0/24
   ```
3. Verify DHCP relay configuration:
   ```bash
   /ip dhcp-relay print
   ```

---

## 4. Detailed Debugging Process
**Step 1: Route Validation**
```bash
[admin@Remote-Router] > /ip route print
Flags: X - disabled, A - active, D - dynamic 
 #    DST-ADDRESS        GATEWAY            DISTANCE
 0 DA 0.0.0.0/0          192.0.2.1          1       
 1 ADC 172.17.111.0/24   ether1             0       
 2 ADC 10.10.10.0/24     ppttp-out1         1       # Missing in actual config
```

**Step 2: DHCP Server Reachability Test**
```bash
[admin@Remote-Router] > /ping 10.10.10.1 src-address=172.17.111.1
HOST                                     SIZE  TTL TIME  STATUS             
10.10.10.1                                56    64 timeout
```

**Step 3: Firewall Rule Check**
```bash
/ip firewall filter print where protocol=udp and dst-port=67-68
# No rules blocking UDP 67/68 found
```

**Step 4: Packet Capture**
```bash
/tool sniffer quick protocol=udp port=67-68
# OUTPUT:
# 15:22:01 rx ether1 DHCPDISCOVER ff:ff:ff:ff:ff:ff 
# No packets transmitted via VPN interface
```

---

## 5. Key Findings & Root Cause
**Findings:**  
- Missing static route to `10.10.10.0/24` via VPN interface  
- DHCP relay attempts using default route (WAN) instead of VPN  
- Asymmetric routing causing DHCP server unreachability  

**Root Cause:**  
Recent firewall policy change accidentally removed critical static route to HQ network, breaking DHCP relay path.

---

## 6. Solution Implementation
**Before:**
```bash
/ip route print 
# No entry for 10.10.10.0/24
```

**After:**
```bash
/ip route add dst-address=10.10.10.0/24 gateway=pptp-out1 distance=1
```

---

## 7. Verification Process
1. Confirm route activation:
   ```bash
   [admin@Remote-Router] > /ip route print where dst-address=10.10.10.0/24
   Flags: A - ACTIVE 
    #   DST-ADDRESS       GATEWAY         DISTANCE
    2 A 10.10.10.0/24     pptp-out1       1
   ```
   
2. Test DHCP lease acquisition:
   ```bash
   [admin@Remote-Router] > /tool sniffer quick protocol=udp port=67
   # OUTPUT:
   # 15:30:12 tx pptp-out1 DHCPREQUEST 10.10.10.1:67
   # 15:30:12 rx pptp-out1 DHCPACK 10.10.10.1:68
   ```

---

## 8. Prevention Measures
1. Implement route monitoring:
   ```bash
   /tool netwatch add host=10.10.10.1 timeout=5s up-script="/log info HQ route UP" down-script="/log warning HQ route DOWN"
   ```
2. Enable configuration backups:
   ```bash
   /system backup save name=daily-config
   ```
3. Document critical routes with comments:
   ```bash
   /ip route set [find dst-address=10.10.10.0/24] comment="CRITICAL: DHCP Server Path"
   ```

---

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/ip route print` | Show routing table |
| `/tool sniffer quick` | Capture real-time traffic |
| `/ip dhcp-relay print` | Check DHCP relay config |
| `/ping src-address=` | Source-specific ping test |

---

## 10. Common Pitfalls to Avoid
1. **Default Route Dependency:** Never assume default route will handle specialized traffic  
2. **Silent Route Removal:** Always use `comment=` field for critical routes  
3. **VPN vs Physical Interfaces:** Verify interface types in routes (`pptp-out1` vs `ether1`)  
4. **Firewall Blindspots:** Test rules with `src-address=` when using VPNs  
5. **DHCP Timeout Mismanagement:** Keep `bootp-support=enabled` on interfaces  
```
