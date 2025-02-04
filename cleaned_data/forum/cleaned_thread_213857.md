# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213857

# Discussion

## Initial Question
Author: [SOLVED]Sat Jan 11, 2025 4:38 pm
``` /ip firewall nataddaction=dst-nat chain=dstnat dst-address=192.168.35.2dst-port=80protocol=tcp to-ports=5216addaction=dst-nat chain=dstnat dst-address=192.168.35.2dst-port=443protocol=tcp to-ports=5216 ``` Well, if we assume that the final desired result is:a. type the destination IP address in the browser without specifying portb. *somehow* connect the browser on a specific port of the specific destination IP addressa dstnat port remapping seems like a possible solution, it should be something *like*:
```
depending if the used port for the browser connection is normally 80 or 443, right?A browser bookmark with the port number included seems to me a lot simpler, though.


---
```

## Response 1
Author: Sat Jan 11, 2025 8:09 pm
``` /ip firewall nataddaction=dst-nat chain=dstnat dst-address=192.168.35.2dst-port=80protocol=tcp to-ports=5216addaction=dst-nat chain=dstnat dst-address=192.168.35.2dst-port=443protocol=tcp to-ports=5216 ``` ``` addaction=dst-nat chain=dstnat dst-address=192.168.35.2dst-port=80protocol=tcp to-ports=5216 ``` Add adstnat firewall rule.This is what the Docker/Podman --publish flag does for you automatically, which you must do by hand on RouterOS.Details.This also makes sense. Thanks for this information. I first time have situation like this, and today learned something usefull.Well, if we assume that the final desired result is:a. type the destination IP address in the browser without specifying portb. *somehow* connect the browser on a specific port of the specific destination IP addressa dstnat port remapping seems like a possible solution, it should be something *like*:
```
depending if the used port for the browser connection is normally 80 or 443, right?A browser bookmark with the port number included seems to me a lot simpler, though.Many thanks. The code:
```

```
makes the trick. Now just enter the IP, and it load the container dashboard without any ports to insert. I have many containers (some on my Mikrotik) and others on Mini PC with Proxmox, so remember all that ports its nightmare for me. This makes the work easy.
```