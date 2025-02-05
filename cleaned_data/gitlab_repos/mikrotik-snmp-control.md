# Repository Information
Name: mikrotik-snmp-control

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/viktorov.k/mikrotik-snmp-control.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
Task: remotely disable and enable the required vpn l2tp interface on the Mikrotik gateway
At Mikrotik in the central office, a vpn was created and configured to communicate with the remote office. Via l2tp connections. 
It must be able to remotely disconnect the connection tunnel from the remote office.
This is done by sending a snmp request to the gateway.
The following settings are required on the central office gateway: l2tp-server interfaces are created and configured,
a script is created that includes or disables the l2tp-interface, known the OID of the script for MIB.
Created and configured snmp community with write access rights. 
In this example used community "public".
IP Mikrotik in Central Office: 192.168.99.5
interface name: l2tp-akd
script name that OFF interface: vpn_off_akd 
script name that On interface: vpn_on_akd
Mikrotik comand start from **/** symbol
Other comand via a console from host.
*it script disable interface*
/system script add name="vpn_off_akd" owner=root policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \     source="interface l2tp-server disable l2tp-akd"
*it script enable interface*
/system script add name="vpn_on_akd" owner=root policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \     source="interface l2tp-server enable l2tp-akd"
* view OID script from remote host or server*
snmpwalk -v2c -cpublic 192.168.99.5 1.3.6.1.4.1.14988.1.1.8
in the answer we see something like:
iso.3.6.1.4.1.14988.1.1.8.1.1.2.179 = STRING: "vpn_off_akd" 
iso.3.6.1.4.1.14988.1.1.8.1.1.2.204 = STRING: "vpn_on_akd"
So, OID for OFF=179 and OID for ON=204
Request snmp to execute the required script in general: snmpset -c public -v 1 192.168.99.5 1.3.6.1.4.1.14988.1.1.8.1.1.3.X s 1
Where X=179 for OFF, and X=204 for ON.