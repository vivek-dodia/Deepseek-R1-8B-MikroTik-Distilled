# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208490

# Discussion

## Initial Question
Author: [SOLVED]Sat Jun 15, 2024 6:53 pm
``` /ip firewall layer7-protocoladdname=65a2a1ac1ecbf655d59bregexp=trialaddname=d022f473ac8ff533262f regexp=annuallyaddname=1a3c1a46a2b20b39b448regexp=unlimitedaddname=4a7135fe7bef7d4b046cregexp=trial ``` ``` {:globalLicense"4a7135fe7bef7d4b046c":if($License!="insert-license")do={/system ssh-execuser=GreenServeraddress=10.166.35.1command="/ip firewall layer7-protocol; :foreach item in=[find where name=$License] do={ }":localvLicense[get$item name];:localvvalue[get$item regexp];}} ``` Hi everyone, I find myself having to create the following scenario: I have many Mikrotik clients on x86 architecture.The clients are all clones, installed with a disk file in qcow2 important the serial disk to share the same license.Services run on these clients. the user has exclusive access via webfig with limited skin and permissions.On the client I installed ssh keys and ditto on the server. Then the machines talk to each other in ssh using ssh RSA keys.In the server, in IP firewall layer 7 I have this configuration:
```
The customer has access to a .json file which he accesses via SMB, where he can enter the license code which I will have already inserted in layer 7 on the server side.In the client via derialize I set the :global variable, so when the user enters the license a similar scenario occurs:
```

```
the problem is that if I set the :local vname and vvalue commands they are inside the ssh-exec command so they are set on the server.How do I reset them on the client, do I have to redo an ssh exec to the client?Or do I write the IP address and license entered by the client in the comments of the server and return the information to the client via a script that reads from the logs?Basically the result I would like to obtain is this:1. The user enters the license into the client;2. The client searches the server to see if the license exists and reads from the regexp whether it is monthly, annual or unlimited.3. The server must respond to the client by returning the license duration.4. If the license check is successful, the client must comment the license with "activated" in the server


---
```

## Response 1
Author: Sat Jun 15, 2024 7:21 pm
``` {:globalLicense"4a7135fe7bef7d4b046c":localIPclient[/ip addressget[findwhereinterface=l2tp-out1]address]:setIPclient[:pick $IPclient0[:find $IPclient"/"]]:put $IPclient:if($License!="insert-license")do={/system ssh-execuser=GreenServeraddress=10.166.35.1command="/ip firewall layer7-protocol; :foreach item in=[find where name=$License] do={ /system ssh-exec user=GreenHS address=$IPclient command=:global vvalue [get $item regexp]; }"}} ``` Something like that, but I'm putting one ssh-exec inside another. I don't think it works