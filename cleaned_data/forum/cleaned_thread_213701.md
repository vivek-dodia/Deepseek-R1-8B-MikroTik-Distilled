# Thread Information
Title: Thread-213701
Section: RouterOS
Thread ID: 213701

# Discussion

## Initial Question
Anybody has a knowledge if currently Mikrotik supports multicore PPPoE processing?With CCR2004 experience and PPPoE client can't really get anything above ~3.5Gbit/s download due to (probably) PPPoE limitation (router acts as PPPoE client to ISP).Will 2116 can be better here? ---

## Response 1
PPPOE-client is a single thread on MikroTik, and it is handled by CPU, no hardware offloading. ---

## Response 2
So this is my RB5009 example on PPPoE 2Gbit/s speedtest.If it's a single thread exaplain to me CPU loads : ---

## Response 3
So this is my RB5009 example on PPPoE 2Gbit/s speedtest.If it's a single thread exaplain to me CPU loads :PPPoE encapsulation/decapsulation is only 1 part in the chain.If you are receiving 2Gbits/sec, that traffic, after PPPoE framing is removed is going through FW-rules etc so it might incur additional load on other processes.But it's true your profiling seems to exhibit some spread across the cores.I've never seen any official change-log or feature list on RouterOS releases that 100% confirms that PPPoE handling would be fully multi-thread/multi-core. ---

## Response 4
So I just tested it with the following setup but then had to leave in a hurry, so I will send the diagram of the rest setup and the profiler results when I'm home.Setup:1. HAP AX32. Server with accel-ppp on Fedora 41 also for iperf and BTest3. Windows Client4. Android ClientScreenshot 2025-01-06 140606.pngThe Fedora 41 Server was running accel-ppp as an PPPoE Server with 4 Threads and 2 Iperf Servers.The HAP AX3 was connected with its ether1 Port to the server 2.5G Port. They negotiated 2.5GRunning Iperf on both clients, a single core of the CPU gets completely hammered with like 99% and just 980Mbps throughput.Using BTest with the Server being the "Server" Machine and the Client being the AX3 i just got 680MbpsScreenshot 2025-01-06 111727.pngScreenshot 2025-01-06 111443.pngI do have to state I'm running vlans for the clients.Which the AX3 has to run on the CPU.PPPoE/iPerf Server had just 2% CPU Usage.As a server i was using:Ryzen 7 7700X2.5G EthernetEDIT: added more details and picture of setup ---