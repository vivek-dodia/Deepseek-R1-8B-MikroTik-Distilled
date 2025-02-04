# Thread Information
Title: Thread-1115210
Section: RouterOS
Thread ID: 1115210

# Discussion

## Initial Question
Having successfully upgraded a map lite to 7.16.2, including routerboard firmware, I tried in Winbox 4
```
/system reset configurationwith default config (no configdeselected) whereon it bricked.Reset (hold until alternating flashing lights) did not resolve it so, not having any Windows, I tried Netinstall on Linuxhttps://help.mikrotik.com/docs/spaces/R ... nsforLinux. My alternative would be under Wine on Mac.Holding reset from prior to power on until wireless and eth lights were steady, about 15 seconds, I ran as instructed
```

```
sudo ifconfig<interface>192.168.88.2/24working as shown by a furtherifconfig. However, the instruction:
```

```
sudo./netinstall-r-a192.168.88.3routeros-7.16.2-mipsbe.npkstopped thus:
```

```
Version:7.16.2(2024-11-2613:15:20)Willreset todefaultconfigUsinginterfaceenp88s0Usinginterfaceenp88s0WaitingforLink-UP on enp88s0WaitingforRouterBOARD...skipping the responses
```

```
OKUsingClientIP:192.168.88.3UsingServerIP:192.168.88.10[i]Fromthe docs.I hadset.2[/i]StartingPXE serverAfter the Reset light sequences mentioned above, it returns to a PWR light only. I am considering trying 6.49.17 instead of 7.16.2, or using the -e parameter for no config but cannot exclude that the IP setup is incorrect, for which I might need more Linux knowledge.Does anyone who has used Netinstall on Linux (or wishes to suggest it in Wine) have a diagnosis or suggestions please?

---
```

## Response 1
Command used looks correct to me (as in: it's the same I have in my notes).But ... you should not forget to ALSO send wireless package. Wireless drivers are not in the base ROS package anymore as of 7.13.So the wireless package (or wifi-qcom or wifi-qcom-ac depending on device) needs to be send as well when using netinstall or you will not have any wireless drivers. You can find those packages in extra. ---

## Response 2
Given the command was basically correct (as since proven), the problem lay in my Linux setup. Abandoning the NUC with a single ethernet port, I first installed Linux on a 4-port Jetway box but found continuing problems. I cannot say certainly whether that was error on my part or some of the reputed flakiness of the i-225 ports but I continued by setting up an N100 / i226 4-port box instead. Along the way I have learned to configure Kea DHCP on Linux so not all effort was lost.The real difficulty, which I have read or inferred in other discussions here, is that Mikrotik's documentation provides some description, not a process, and this is not all resolved by prior forum discussions, some of which are quite old.So, this is what worked for me, meaning it worked but is not comprehensively tested such that variations on it could be excluded. My setup was MacOS Safari as the window to a PiKVM connection to the Ubuntu Linux box. Others may be simpler.Configure the first spare port (after your DHCP client port) in Linux manually with address xxx.xxx.xxx.2, netmask 255.255.255.0 (choose your own private xxx, usually 192.168.88Download and extract netinstall.cli as instructed in Mikrotik docs, for the ROS version, 7.16 in my case.Download appropriate packages for the router. I went to the Hardware section for my specific device, a mAP Lite, as the easiest way to ensure you are fetching the right packages; in this case routeros-7.16.2-mipsbe.npk and wireless-7.16.2-mipsbe.npkWith the router connected up but unpowered, start netinstall-cli as advised in Mikrotik docs. I used the first option described there and also happened to use sudo after it first failed to find the port but am unsure that was relevant, so
```
sudo netinstall-cli-r-a192.168.88.1routeros-7.16.2-mipsbe.npk wireless-7.16.2-mipsbe.npkIt should recognise the ethernet port and stop at Waiting for RouterBOARD.With the Reset button pressed and held, power up the router. If your Linux ethernet port is not set to connect automatically then quickly connect now, during the reset period (other hand to mouse the GUI is easiest)netinstall should show connection and start formatting the router. If it remains stalled at Waiting, start again, perhaps with variations on timings.After it finished, netinstall did not quit. Eventually I quit it with Ctrl-C. The router was unaffected and is now operating with defaults, ready for me to try reconfiguration again.Despite the box-switching, I eventually found the Linux method quicker and easier than what would apparently have been required had I switched to a Windows emulation, there being no actual Windows machines in this house. Along the way I also used WinBox 4 for Linux, used first to check that netinstall had succeeded.Editing to add an important descriptive point.Much is written about the ramifications of holding the reset button before or after power up, or what is expressed by the activity of lights. Mikrotik is unhelpful by talking about "the light" on a hex when a map lite (for example) has four of them despite only one ethernet port. The above process skips the problem. You release the button when netinstall announces connection to the router, not caring about time or lights.

---
```

## Response 3
After it finished, netinstall did not quit. Eventually I quit it with Ctrl-C. The router was unaffected and is now operating with defaults, ready for me to try reconfiguration again.*) netinstall-cli - added "-o" option to install devices only once per netinstall run;Have seen in the Changlog from the latest version of netinstall-cli that you have to provide -o to end netinstall-cli when only one device being flashed.Maybe you have been using that.And if you using more of the netinstall-cli options like -v you should see more text of what netinstall-cli been doing. ---

## Response 4
I missed the -o option although I considered it might just be waiting for another. Thanks Patrik. ---