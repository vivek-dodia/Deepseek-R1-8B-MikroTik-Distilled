---
generated_at: 2025-02-03T16:19:47.809632
topic: BGP
category: Routing
version: 7.x
scale: ISP
level: Expert
subnet: 192.168.216.192/27
scenario: VLAN Trunking Issues
environment: Cloud Infrastructure
affected_users: 940
duration: 18 hours
---

# Analysis Process
Okay, I need to create a detailed MikroTik RouterOS troubleshooting scenario for BGP with VLAN trunking issues in a cloud-based ISP environment. Let's break down each section as per the user's requirements.

First, the initial problem report. The users are experiencing internet outages, and the BGP sessions are flapping. Since the subnet is 192.168.216.192/27, that's a /27 which gives 32 addresses. The environment is cloud infrastructure, so maybe the VLANs are between the MikroTik routers and cloud switches or other virtual routers. The duration is 18 hours, affecting 940 users. Symptoms would include BGP neighbor drops, maybe high CPU or interface errors.

Next, the environment description and network topology. The user wants it in Mermaid. Let me think: there's a core router connected to two edge routers (for redundancy?), each connected to cloud switches. The cloud switches have VLAN trunking to VMs. Maybe the BGP peers are between edge routers and the core, and perhaps with external peers. I'll need to represent that in Mermaid diagram code.

Initial assessment steps: Check BGP status with /routing/bgp/session print, look for established sessions. Verify VLAN interfaces with /interface vlan print. Check interface errors and CPU usage. Maybe look at logs for BGP or VLAN related messages.

Detailed debugging process: Start by checking BGP sessions. If they're flapping, maybe the underlying VLAN is dropping packets. Check the VLAN configuration on both MikroTik and the cloud switches. Verify MTU settings, since mismatched MTU can cause fragmentation issues. Use commands like /interface print stats to see errors. Maybe check the ARP table to ensure neighbors are reachable. Use ping with do-not-fragment to test MTU. Capture traffic on the VLAN interface to see if BGP packets are being transmitted but not received, indicating a trunking issue.

Key findings: Suppose the root cause is a misconfigured VLAN trunk on the cloud switch not allowing all necessary VLANs, causing intermittent connectivity. Or maybe the MikroTik's VLAN interface has an incorrect ID. Another possibility is an MTU mismatch causing BGP packets to be dropped. For example, if the cloud switch has an MTU of 1500 but the MikroTik is set to 1492, that could fragment packets leading to drops.

Solution implementation: Correct the VLAN trunk configuration on the cloud switch to allow the necessary VLAN. Adjust MTU settings on MikroTik interfaces if needed. Ensure BGP timers are consistent on both ends. Maybe adjust BGP keepalive and hold times to be more tolerant of delays, but that's a band-aid. The real fix is fixing the VLAN trunk.

Verification: Check BGP sessions are stable, monitor interface statistics for errors. Use continuous pings to test connectivity. Check logs for any recurring issues.

Prevention measures: Implement monitoring for BGP sessions and VLAN interfaces. Use automated alerts for session state changes. Regularly audit network device configurations, especially after changes. Document VLAN configurations and ensure consistency across devices.

Related commands: Include commands like /routing/bgp/session print, /interface vlan print, /ping, /tool sniffer, etc. Common pitfalls might be forgetting to check both ends of the VLAN trunk, ignoring MTU settings, or not monitoring session states.

I need to make sure each section is covered with appropriate CLI examples, maybe show a before and after configuration for the VLAN interface or BGP settings. Also include log snippets, like BGP state changes or interface errors.

Wait, the subnet given is 192.168.216.192/27. That's a private IP range. Maybe this is used for the internal BGP peering? Or perhaps the VLAN interfaces are using addresses from this subnet. Need to mention that in the environment description.

Also, since it's a cloud environment, the VLAN trunking might involve virtual switches or cloud provider's networking layer. So the issue could be on the cloud side, like missing VLAN configurations in the cloud's virtual network settings.

Putting it all together, making sure each section flows logically and includes all required elements. The CLI commands should be in code blocks with comments explaining them. Log outputs should be realistic, like showing BGP sessions going up/down or interface errors increasing.

# Troubleshooting Guide
```markdown
# MikroTik BGP Troubleshooting Scenario: VLAN Trunking Issues

## 1. Initial Problem Report and Symptoms
**Report:**  
940 users reported intermittent internet access over 18 hours. Multiple BGP sessions between core routers and edge routers in cloud environment were unstable.

**Symptoms:**
- BGP sessions flapping between `Established`/`Active` states
- VLAN interface `ether12-cloud-trunk` showing CRC errors
- 30% packet loss across 192.168.216.192/27 subnet
- Cloud VM connectivity dropping during BGP flaps

## 2. Environment Description
**Network Topology**
```mermaid
graph TD
    CR[Core Router<br>(MikroTik CCR1072)] -->|BGP/MPLS| ER1[Edge Router 1<br>(MikroTik CCR1009)]
    CR -->|BGP/MPLS| ER2[Edge Router 2<br>(MikroTik CCR1009)]
    ER1 -->|VLAN 3001 Trunk| CS1[Cloud Switch 1]
    ER2 -->|VLAN 3001 Trunk| CS2[Cloud Switch 2]
    CS1 -->|VLAN 3001| VM1[Customer VM Pool]
    CS2 -->|VLAN 3001| VM2[Customer VM Pool]
```

## 3. Initial Assessment Steps
1. Verify BGP session status:
```bash
/routing/bgp/session print
# Output:
# 0 name="CR_to_ER1" remote-address=192.168.216.193 established=55m
# 1 name="CR_to_ER2" remote-address=192.168.216.194 established=3m
```

2. Check VLAN interface status:
```bash
/interface vlan print 
# Flags: X - disabled, R - running 
# 0  R name="ether12-cloud-trunk" mtu=1500 vlan-id=3001 interface=ether12
```

3. Monitor interface errors:
```bash
/interface monitor-traffic ether12-cloud-trunk
#     rx-drop: 12345       tx-drop: 678
#     rx-error: 456        tx-error: 12
```

## 4. Detailed Debugging Process
**Step 1: Capture BGP Session Flaps**
```bash
/log print where message~"BGP"
# 2023-10-01 14:22:01 bgp,info CR_to_ER1: session closed
# 2023-10-01 14:22:05 bgp,info CR_to_ER1: session established
```

**Step 2: Verify VLAN Trunk Configuration**
```bash
/interface ethernet print 
# 12  name="ether12" mtu=9000 
# Cloud switch MTU was 1500 (misconfigured jumbo frames)
```

**Step 3: Test Path MTU**
```bash
/ping 192.168.216.193 size=1472 do-not-fragment=yes
# SEQ 3: timeout
/ping 192.168.216.193 size=1468 do-not-fragment=yes 
# 192.168.216.193 64 byte ping: ttl=64 time=0.3 ms
```

**Step 4: Packet Capture on Trunk Interface**
```bash
/tool sniffer quick interface=ether12-cloud-trunk filter-port=179
# Captured TCP retransmissions during BGP keepalive intervals
```

## 5. Key Findings & Root Cause
**Root Cause:**  
MTU mismatch between MikroTik (`mtu=9000` on ether12) and cloud switch (`mtu=1500`) caused fragmentation drops of BGP packets (179-byte TCP payload + headers).

**Supporting Evidence:**
- 45% CRC errors on ether12 interface
- Path MTU discovery failing at 1472 bytes
- BGP keepalive packets (60 bytes) worked, updates (1500+ bytes) failed

## 6. Solution Implementation
**Before (Faulty):**
```bash
/interface ethernet set ether12 mtu=9000
```

**After (Correct):**
```bash
/interface ethernet set ether12 mtu=1500
/interface vlan set [find name="ether12-cloud-trunk"] mtu=1500
```

**BGP Hard Reset:**
```bash
/routing/bgp/session disable [find name~"CR_to_ER"]
/routing/bgp/session enable [find name~"CR_to_ER"]
```

## 7. Verification Process
1. Monitor BGP stability:
```bash
:global bgpStatus do={ /routing/bgp/session print where established }
:put [$bgpStatus]
# Both sessions showed established >60m
```

2. Confirm MTU alignment:
```bash
/interface print 
# ether12: mtu=1500
```

3. Packet loss test:
```bash
/ping 192.168.216.193 count=100 interval=0.1
# 0% packet loss
```

## 8. Prevention Measures
1. Implement MTU consistency checks:
```bash
:foreach i in=[/interface find] do={
  /tool netwatch add host=[/interface get $i value-name=mtu] \
  interval=5m comment="MTU Monitor"
}
```

2. Add BGP session monitoring:
```bash
/system script add name=bgp-check source={
  /routing/bgp/session print where established \
  && :log info "BGP OK" \
  || :log warning "BGP Down"
}
/system scheduler add interval=1m name=bgp-monitor start-time=startup \
  on-event=bgp-check
```

## 9. Related Commands Reference
| Command | Purpose |
|---------|---------|
| `/routing/bgp/session print stats` | Show BGP message counters |
| `/interface vlan print detail` | Verify VLAN tagging |
| `/tool sniffer packet` | Capture specific BGP packets |
| `/ping size= do-not-fragment=yes` | Test path MTU |

## 10. Common Pitfalls to Avoid
1. **Mixing Jumbo Frames and Standard MTU:**  
   Always verify MTU end-to-end in cloud environments.

2. **Ignoring Interface Errors:**  
   CRC errors >0.1% of traffic indicate physical/media issues.

3. **BGP Timers Mismatch:**  
   Keepalive/hold-time must match on both peers:
```bash
/routing/bgp/session set [find] hold-time=3m keepalive-time=1m
```

4. **VLAN Tagging Conflicts:**  
   Ensure unique VLAN IDs across trunk ports:
```bash
/interface vlan set [find] vlan-id=3001
```
```
