# Thread Information
Title: Thread-1123437
Section: RouterOS
Thread ID: 1123437

# Discussion

## Initial Question
I have RB5009UPr+S+. For testing purposes, I've switched CPU Frequency in RouterBOARD settings from Auto to 1400MHz. I want to revert it, but I cannot do that - getting "not allowed by device mode: ()":Untitled.pngI'm running 7.17.1 and the device is in Advanced Mode:
```
mode:advanced     
     allowed-versions:7.13+,6.49.8+flagged:noflagging-enabled:yes          
            scheduler:yes          
                socks:yes          
                fetch:yes          
                 pptp:yes          
                 l2tp:yes          
       bandwidth-test:yes          
          traffic-gen:nosniffer:yes          
                ipsec:yes          
                romon:yes          
                proxy:yes          
              hotspot:yes          
                  smb:yes          
                email:yes          
             zerotier:yes          
            container:yes          
  install-any-version:nopartitions:norouterboard:noattempt-count:0Any advice?

---
```

## Response 1
OK, so appearently, it required running:
```
/system/device-mode/update routerboard=yesHowever, I don't think that's expected behavior, is it? It's OK if this requires updating the mode, but then it shouldn't allowed me to change the frequency from "Auto" in the first place.

---
```

## Response 2
As of 7.17 it is as Mikrotik is trying to lock down features that can be abused by hackers and other nefarious actors. This change has been quite the lightning rod for complaint and anger but it doesn't look like they're going to change things. You'll have to run commands for specific features you want to turn on/off and then reboot the device by pulling the power or pressing reset button. Now image having to do that same thing with 100s or 1000s of fielded devices.... ---

## Response 3
... but then it shouldn't allowed me to change the frequency from "Auto" in the first place.At which ROS version did you set CPU frequency to 1400MHz? Versions lower than 7.17 allowed that without a hiccup ... ---

## Response 4
... but then it shouldn't allowed me to change the frequency from "Auto" in the first place.At which ROS version did you set CPU frequency to 1400MHz? Versions lower than 7.17 allowed that without a hiccup ...7.17.1. That's why it's strange. If I had set this using older version and couldn't revert after upgrade, it would make sense. Now, I changed it, but couldn't revert it back after a couple of minutes. The router wasn't even rebooted during that time. ---

## Response 5
Was routerboard version already updated at that time or not ?Anyhow, sounds like a bug.Depending on who looks at it ... ---

## Response 6
@tdabasinskas this is a bug IMHO. I have experienced this bug as well. I did came up with some test cases and reported them all to Mikrotik support this week. SUP-177436Depending on your action sequence there is a high chance that rebooting (/system/reboot) reverts cpu-frequency back to "auto" magically. Give it a try. ---

## Response 7
@tdabasinskas this is a bug IMHO. I have experienced this bug as well. I did came up with some test cases and reported them all to Mikrotik support this week. SUP-177436Depending on your action sequence there is a high chance that rebooting (/system/reboot) reverts cpu-frequency back to "auto" magically. Give it a try.Tried this in another router - a simple reboot didn't help. ---

## Response 8
I prefer not to go into detail regarding my observations and the test cases I used to reproduce this issue, as I believe it could be security-sensitive. Additionally, it is unclear whether this bug is limited to CPU frequency adjustments or if it represents a broader flaw affecting other device-mode restricted settings. I have not investigated further, as repeatedly cycling device modes via the mode/reset button is not practical for extended testing.@tdabasinskasPlease report to MikroTik support if not already.https://mikrotik.com/support ---

## Response 9
I prefer not to go into detail regarding my observations and the test cases I used to reproduce this issue, as I believe it could be security-sensitive. Additionally, it is unclear whether this bug is limited to CPU frequency adjustments or if it represents a broader flaw affecting other device-mode restricted settings. I have not investigated further, as repeatedly cycling device modes via the mode/reset button is not practical for extended testing.@tdabasinskasPlease report to MikroTik support if not already.https://mikrotik.com/supportYeah, created SUP-178269 for this. ---