# Thread Information
Title: Thread-1113441
Section: RouterOS
Thread ID: 1113441

# Discussion

## Initial Question
Hello, I recently just checked the logs on one of our devices and it looks like the logs are showing public IP entries as the gateway IP.I've tried to find out more about this but I'm unsure what's happening. Is there a way to change it so that it shows their Public IP instead of the gateway?Attached is the screenshot for referenceScreenshot 2024-12-06 090645.png ---

## Response 1
From the logging I get the feeling that SSH is publically available. Why?Is this MikroTik behind NAT? As the IP address it is showing is a private IP? Cam you supply a network diagram including IP addressing in it? ---

## Response 2
This kind of looks like what you would get, if your gateway was also a Mikrotik, and it had hairpin nat enabled for a SSH port forward/dst-nat connection to the internal router. (With attempted logins from inside) ---

## Response 3
Or maybe someone or something is somehow logged into or has a vpn into your gateway router, working on the next step. ---

## Response 4
This kind of looks like what you would get, if your gateway was also a Mikrotik, and it had hairpin nat enabled for a SSH port forward/dst-nat connection to the internal router. (With attempted logins from inside)Or even from the outside if that src-nat rule doesn't care. But indeed, some endpoint security softwares periodically attack the router to notify the user about weak user names and passwords there, behaving indistinguishably from real malware as far as the router can tell. ---