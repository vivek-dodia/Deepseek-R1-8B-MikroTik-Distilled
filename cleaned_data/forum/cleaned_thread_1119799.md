# Thread Information
Title: Thread-1119799
Section: RouterOS
Thread ID: 1119799

# Discussion

## Initial Question
Are there any solution to add the simplest web server to the mikrotik?I needed it to redirect port-forwarding rule to such page if main web-server is down.I've decided to make new post with this specific question, see more details here:viewtopic.php?t=213949 ---

## Response 1
I believe that it Is possible to (ab-) use the hotspot/captive portal features.Particularly if - as in your case - you can redirect to a specific url and if the Mikrotik device isn't the gateway (or Is It?).I was thinking of something similar a few day ago, but in my intended case the issue Is connected with https, with the fact that the device Is NOT connected to the internet (but this can be worked around) and with the difficulties in having various devices/OS auto-detect the presence of the captive portal.JFYI:viewtopic.php?t=213862I am doing a few experiments that seem promising ,(minus the autodetection) but in my case the Mikrotik device involved Is an old spare-spare one dedicated to this use so It has to be seen if setting up a hotspot (even if "trasparent") may affect the normal operation of your router. ---