---
title: Routing Debugging Tools
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/59965489/Routing+Debugging+Tools,
crawled_date: 2025-02-02T21:12:21.559309
section: mikrotik_docs
type: documentation
---

Routing stats.
# /routing/stats/origin
# /routing/stats/process
This menu allows to monitor debugging information of all the routing processes.
```
[admin@rack1_b35_CCR1036] /routing/stats/process> print interval=1
Columns: TASKS, PRIVATE-MEM-BLOCKS, SHARED-MEM-BLOCKS, PSS, RSS, VMS, RETIRED, ID, PID, RPID, PROCESS-TIME, KERNEL-TIME, CUR-BUSY, MAX-BUSY, CUR-CALC, MAX-CALC
 # TASKS                         PRIVATE-  SHARED-ME  PSS        RSS     VMS      RETIRED  ID       PID  RPID  PROCESS  KERNEL-TIME  CUR-BUSY  MAX-BUSY  CUR-CALC  MAX-CALC
 0 routing tables                768.0KiB  1792.0KiB  2399.0KiB  6.4MiB  22.1MiB       34  main     317     0  2s260ms  1s940ms      10ms      170ms     20ms      1s210ms 
   rib                                                                                                                                                                     
 1 fib                           0         0          2263.0KiB  6.2MiB  22.3MiB           fib      351     1  250ms    1s720ms                1s210ms             1s210ms 
 2 ospf                          256.0KiB  256.0KiB   2559.0KiB  6.6MiB  22.3MiB           ospf     384     1  4s710ms  5s210ms                20ms                20ms    
 3 pimsm                         256.0KiB  0          2252.0KiB  5.8MiB  22.3MiB           pim      386     1  200ms    450ms                  10ms                10ms    
 4 fantasy                       0         0          2031.0KiB  5.1MiB  22.3MiB           fantasy  388     1  270ms    390ms                  10ms                10ms    
 5 configuration and reporting   0         512.0KiB   2351.0KiB  6.4MiB  22.3MiB           static   389     1  310ms    430ms                  10ms                10ms    
 6 ldp                           256.0KiB  256.0KiB   2455.0KiB  6.4MiB  22.3MiB           mpls     387     1  340ms    350ms                  40ms                40ms    
   Copy                                                                                                                                                                    
 7 rip                           256.0KiB  0          2230.0KiB  5.7MiB  22.3MiB           rip      377     1  230ms    380ms                  10ms                10ms    
 8 routing policy configuration  512.0KiB  512.0KiB   2355.0KiB  5.6MiB  22.3MiB           policy   358     1  240ms    390ms                  10ms                10ms    
 9 BGP service                   512.0KiB  0          2592.0KiB  6.3MiB  22.3MiB           bgp      364     1  360ms    600ms                  10ms                10ms    
10 BFD service                   256.0KiB  0          2206.0KiB  5.7MiB  22.3MiB           12       371     1  230ms    370ms                  10ms                10ms    
11 BGP Input 111.11.0.1          512.0KiB  512.0KiB   2560.0KiB  6.4MiB  22.3MiB        1  22       679     1  140ms    350ms                  10ms                10ms    
   BGP Output 111.11.0.1                                                                                                                                                   
12 Global memory                           256.0KiB                                        global     0     0
```
# /routing/stats/step