# Thread Information
Title: Thread-213356
Section: RouterOS
Thread ID: 213356

# Discussion

## Initial Question
Hi, This is my setup:2024-12-18_10h45_38.pngAll switches are connected with 1gbit to the core switch.The problem is, from my PC, connected to "Buero-Dennis" the ping to the bridge looks like this:2024-12-18_10h46_41.pngI just checked the VLAN configuration if there is a loop, i would say, this looks good.The log of the core switch is pretty much empty. Any idea or hints how to start investigating?Thank you!Snooops ---

## Response 1
1. Ping from PC to Buero-Dennis2. Ping from Buero-Dennis (tools) to Core3. Check or remove (set none) STP/RSTP/MSTP4. Check ethernet counters5. Check Bridge status for Root bridge election, check Link down counters6. Anything connected that can trigger a "Root bridge election" ?7. Broadcast storms or other excessive traffic bursts?... ---

## Response 2
Check Bridge STP priority as well if STP/RSTP/MSTP is used.Core switch should have lowest priority.See here for more info:https://help.mikrotik.com/docs/spaces/R ... ionprocess ---

## Response 3
Ping from PC to Buero-Dennis -> Stable 1msPing from PC to Firewall (which is connected on Core) -> Stable 1msPing from Firewall to Core -> occasionally timeoutsPing from Buero-Dennis to Core -> occasionally TimeoutsAll switches have problems to ping the core switch.STP was set to RSTP (on all switches), tried now set to NONE (on all switches), no improvement.Bridge Interface on all switches shows no Drops or Errors.checking now the other suggestions, but first i need todo some research on those features, as they are unknown to me.Thank you very much for your help! ---

## Response 4
Is it normal that the first interface has the same mac as the bridge?if i ping the mac of the bridge of the core switch i receive double the amount of packages than i have sent, isn't that weird? ---

## Response 5
Is it normal that the first interface has the same mac as the bridge?This is default behaviour if you don't set bridge MAC manually (bridge assumes MAC address of first member port).To the topic: so basically your core switch doesn't respond to every ping sent at, regardless of where it was sent from. So it might be something about core switch IP configuration (or it might actually be overloaded ... run CPU profiler and see if that might be the case). ---

## Response 6
The D4:01:C3...... is seemingly the Chateau LTE12? ---

## Response 7
To the topic: so basically your core switch doesn't respond to every ping sent at, regardless of where it was sent from. So it might be something about core switch IP configuration (or it might actually be overloaded ... run CPU profiler and see if that might be the case).CPU total is about 16-24 - looks good to me if it's a percentage metric.IP configuration could be a thing. Pinging the mac-address seems stable without any packet loss. I also changed the ip address, but the timeouts still persist.IP configuration of the bridge:2024-12-18_15h17_05.pngBtw: the coreswitch is also acting as a CAPsMAN, i disabled it, but the timeouts still persist.No firewall rules present ---

## Response 8
The D4:01:C3...... is seemingly the Chateau LTE12?ah sorry - this was a screenshot from a wrong switch. i cross-checked the behaviour of the ping and the mac-address configuration with a different device, this was a hAP ac^3 ---

## Response 9
And anything on the ethernet interfaces? ..RX or TX Pause, Error, Underrun, Collision, .... etc4. Check ethernet counters ---

## Response 10
To the topic: so basically your core switch doesn't respond to every ping sent at, regardless of where it was sent from. So it might be something about core switch IP configuration (or it might actually be overloaded ... run CPU profiler and see if that might be the case).CPU total is about 16-24 - looks good to me if it's a percentage metric.CRS328 has 1 or 2 cores (depending on ROS version running)... so 24% total CPU load can mean one CPU core loaded to almost 50% and that would be a problem. That's why I suggested to run CPU profiler (it shows load per CPU core and per process). And if CRS is configured properly and used as a switch, it should work with CPU load almost zero. ---

## Response 11
Thank you guys for your support! I really appreciate itbut the issue still persistAnd anything on the ethernet interfaces? ..RX or TX Pause, Error, Underrun, Collision, .... etcAll interfaces show no RX/TX drops or errors in the Interface List.CRS328 has 1 or 2 cores (depending on ROS version running)... so 24% total CPU load can mean one CPU core loaded to almost 50% and that would be a problem. That's why I suggested to run CPU profiler (it shows load per CPU core and per process). And if CRS is configured properly and used as a switch, it should work with CPU load almost zero.Ah yes, i remember. I checked the configuration - all Interfaces are using Hardware offloading. Profiler screenshot:2024-12-20_12h24_54.pngThank you!Snooops ---

## Response 12
How does profile output look like while pings are timing out? ---

## Response 13
The same, i was pinging during the creation of this screenshot ---

## Response 14
Finally i found the error.I had some VLANs configured in the Interfaces / VLAN tab, as soon as i deleted all VLAN configurations in that tab the ping was giving me stable responses. I have all VLANs configured in the Bridge, so that should do the magic. i don't know why i had the VLANs there, maybe there were created during some CAPsMAN try&error.Everything is working for now. ---

## Response 15
When using VLAN's, you should create an /interface/vlan for management purposes. And...the bridge should not have an IP address when using VLAN filtering. My best guess is that it does, but that would require the config for confirmation.Don't know if you are familiar with this great topic:viewtopic.php?t=143620 ---

## Response 16
For which management purposes? Management by who? By the switch chip? ---