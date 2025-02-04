# Thread Information
Title: Thread-1118394
Section: RouterOS
Thread ID: 1118394

# Discussion

## Initial Question
When I try to log in to the router with WInBox over an SSH tunnel, I get the error "The router does not support a secure connection." If I enable Legacy Mode like it suggests, WinBox just hangs on "Logging in...".I'm using Winbox 3.41 (happened on 3.40 too) and the router is a RB5009 running 7.16.2. I am just doing a standard SSH port forward with Putty, forwarding 8291 to my router. It used to work fine. I'm not sure what changed. ---

## Response 1
Ah, never mind. I needed to add a firewall rule allowing src-address-type=local for ssh-tunneled connections to the router to work. ---