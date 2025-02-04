# Thread Information
Title: Thread-205059
Section: RouterOS
Thread ID: 205059

# Discussion

## Initial Question
Hello everyone, I am trying to mirror my traffic and feed the monitor port of a security onion.When i am doing a tcpdump at the security onion all i can see is broadcast packets and arp.There is something special for configuration?Searched and haven't found a solution, but many refers to this issue.viewtopic.php?t=115513Can anyone help?Thanks in advance ---

## Response 1
Show the configuration from /interface/bridge and /interface/ethernet ... it's likely that your switch has HW offload enabled (otherwise it wouldn't be able to switch traffic at wirespeed) and port mirroring doesn't actually work. ---

## Response 2
I confirm there's a problem with this device. It only mirrors broadcast traffic, but unicast (TCP, UDP etc) is missing in the stream.There's nothing special with the configuration, just followed this article:https://help.mikrotik.com/docs/spaces/R ... dMirroringShow the configuration from /interface/bridge and /interface/ethernet ... it's likely that your switch has HW offload enabled (otherwise it wouldn't be able to switch traffic at wirespeed) and port mirroring doesn't actually work.Of course I have HW offloading enabled! That's the whole point of switching (and mirroring) via switch chip. ---

## Response 3
Is your source and destination interface on the same switch chip internally? ---

## Response 4
Is your source and destination interface on the same switch chip internally?According to block diagram, there is only single switch chip:https://cdn.mikrotik.com/web-assets/pro ... 220955.png ---

## Response 5
I'm sorry, there is no issue with this switch.My problem was caused by misconfigured bridge in the Proxmox machine where I run the capture.I bet the original submitter of this post had similar problem. ---