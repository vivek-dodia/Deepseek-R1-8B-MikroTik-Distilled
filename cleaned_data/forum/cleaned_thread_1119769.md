# Thread Information
Title: Thread-1119769
Section: RouterOS
Thread ID: 1119769

# Discussion

## Initial Question
Hello, I have this setup:Mikrotik router 1 (R1)- R1 reachable from web via r1.domain.com- L2TP server running- R2 connects to R1 via L2TP local address 192.168.1.50 and remote address 10.50.50.11- port forward: action=dst-nat chain=dstnat comment="R2 WEBSERVER REACH" dst-port=81 protocol=tcp to-addresses=10.50.50.30 to-ports=80- all firewall blocking rules turned off (during testing)Mikrotik router 2 (R2)- connects to R1 via L2TP- here is a web server on 10.50.50.30- all firewall blocking rules turned off (during testing)This setup working well if I connects anywhere to r1.domain.com:81My problem is, if I change the portforward to reach mikrotik webfig, I can't: action=dst-nat chain=dstnat comment="R2 WEBFIG" dst-port=81 protocol=tcp to-addresses=10.50.50.1 to-ports=80If I connected to R1 locally and type 10.50.50.1, the webfig is working well.(the R2 has dinamic IP so I can't create r2.domain.com, this is why I try to setup this type of setup to reach it)What is limiting the reach of webfig via l2tp or what I missed?Thank You ---

## Response 1
Exported configs of both router are needed:export file=anynameyouwish(minus sensitive info like serial numbers, passwords, public IPs, etc.) ---