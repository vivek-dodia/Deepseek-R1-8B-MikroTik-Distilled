# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 73287

# Discussion

## Initial Question
Author: Mon Jun 03, 2013 7:08 pm
``` { /tool fetch url="http://myip.dnsomatic.com/" mode=http dst-path=mypublicip.txt local ip [file get mypublicip.txt contents ] put $ip } ``` this script check your publick ip and return in a local variable.ros code ---

## Response 1
Author: Mon Jul 29, 2013 3:20 pm
``` # Set needed variables :global extinterface "ether1-gateway" :global ExtIpListName "external-ip" :global extip "" :global oldextip "" # Grab the current IP address on that interface. :local extip2 [/ip address get [/ip address find interface=$extinterface ] address]; :set extip [:pick $extip2 0 [:find $extip2 "/"]]; :log info "Current external IP = $extip" :if ([:len [/ip firewall address-list find list=$ExtIpListName]] > 0) do={ :set oldextip [/ip firewall address-list get [/ip firewall address-list find list=$ExtIpListName] address]; :if ($oldextip != $extip) do={ /ip firewall address-list set [/ip firewall address-list find list=$ExtIpListName address=$oldextip] address=$extip :log info "External IP relpace from $oldextip to $extip" } else={ :log info "External IP not changed" }; } else={ /ip firewall address-list add list=$ExtIpListName address=$extip :log info "New external IP added: $extip" }; ``` ``` add name=Refresh_External_IP policy=ftp, read, write, test, winbox, api source="# S\ et needed variables\r\ \n:global extinterface \"ether1-gateway\"\r\ \n:global ExtIpListName \"external-ip\"\r\ \n:global extip \"\"\r\ \n:global oldextip \"\"\r\ \n\r\ \n# Grab the current IP address on that interface.\r\ \n:local extip2 [/ip address get [/ip address find interface=\$extinterfac\ e ] address];\r\ \n:set extip [:pick \$extip2 0 [:find \$extip2 \"/\"]];\r\ \n:log info \"Current external IP = \$extip\"\r\ \n\r\ \n:if ([:len [/ip firewall address-list find list=\$ExtIpListName]] > 0) d\ o={\r\ \n :set oldextip [/ip firewall address-list get [/ip firewall address-li\ st find list=\$ExtIpListName] address];\r\ \n :if (\$oldextip != \$extip) do={\r\ \n /ip firewall address-list set [/ip firewall address-list find list\ =\$ExtIpListName address=\$oldextip] address=\$extip\r\ \n :log info \"External IP relpace from \$oldextip to \$extip\"\r\ \n } else={\r\ \n :log info \"External IP not changed\"\r\ \n };\r\ \n} else={\r\ \n /ip firewall address-list add list=\$ExtIpListName address=\$extip\r\ \n :log info \"New external IP added: \$extip\"\r\ \n};\r\ \n" ``` Hi!Here is a script to query and set the external interface IP address.Copy to Winbox System/Scripts menuName:Refresh_External_IPSource:ros codeCopy to terminal:plain codeUse as is free! ---

## Response 2
Author: Sat Feb 27, 2016 11:08 am
``` .../myrosip.php?who=<<SOURCE_LABEL>>" mode=http dst-path=mypublicip.txt ``` ``` 2016-02-27 10:30:03 Error xx.xx.128.85 403 GET /myrosip.php?who=Fantastic ROS HTTP/1.0 Mikrotik/6.x Fetch 462 Apache access 2016-02-27 10:30:03 Error xx.xx.128.85 ModSecurity: [file "/etc/httpd/crs/activated_rules/modsecurity_crs_20_protocol_violations.conf"] [line "52"] [id "960911"] [rev "2"] [msg "Invalid HTTP Request Line"] [data "GET /myrosip.php?who=Fantastic ROS HTTP/1.0"] [severity "WARNING"] [ver "OWASP_CRS/2.2.8"] [maturity "9"] [accuracy "9"] [tag "OWASP_CRS/PROTOCOL_VIOLATION/INVALID_REQ"] [tag "CAPEC-272"] Warning. Match of "rx ^(?i:(?:[a-z]{3, 10}\\\\s+(?:\\\\w{3, 7}?://[\\\\w\\\\-\\\\./]*(?::\\\\d+)?)?/[^?#]*(?:\\\\?[^#\\\\s]*)?(?:#[\\\\S]*)?|connect (?:\\\\d{1, 3}\\\\.){3}\\\\d{1, 3}\\\\.?(?::\\\\d+)?|options \\\\*)\\\\s+[\\\\w\\\\./]+|get /[^?#]*(?:\\\\?[^#\\\\s]*)?(?:#[\\\\S]*)?)$" against "REQUEST_LINE" required. [hostname "mysite.com"] [uri "/myrosip.php"] [unique_id "VtFei5BMStIADvtxPsMAAAAV"] Apache error 2016-02-27 10:30:03 Error xx.xx.128.85 ModSecurity: [file "/etc/httpd/crs/activated_rules/modsecurity_crs_30_http_policy.conf"] [line "78"] [id "960034"] [rev "2"] [msg "HTTP protocol version is not allowed by policy"] [data "ROS HTTP/1.0"] [severity "CRITICAL"] [ver "OWASP_CRS/2.2.8"] [maturity "9"] [accuracy "9"] [tag "OWASP_CRS/POLICY/PROTOCOL_NOT_ALLOWED"] [tag "WASCTC/WASC-21"] [tag "OWASP_TOP_10/A6"] [tag "PCI/6.5.10"] Warning. Match of "within %{tx.allowed_http_versions}" against "REQUEST_PROTOCOL" required. [hostname "mysite.com"] [uri "/myrosip.php"] [unique_id "VtFei5BMStIADvtxPsMAAAAV"] Apache error 2016-02-27 10:30:03 Error xx.xx.128.85 ModSecurity: [file "/etc/httpd/crs/activated_rules/modsecurity_crs_49_inbound_blocking.conf"] [line "26"] [id "981176"] [msg "Inbound Anomaly Score Exceeded (Total Score: 5, SQLi=0, XSS=0): Last Matched Message: HTTP protocol version is not allowed by policy"] [data "Last Matched Data: GET /myrosip.php?who=Fantastic ROS HTTP/1.0"] Access denied with code 403 (phase 2). Pattern match "(.*)" at TX:960911-OWASP_CRS/PROTOCOL_VIOLATION/INVALID_REQ-REQUEST_LINE. [hostname "mysite.com"] [uri "/myrosip.php"] [unique_id "VtFei5BMStIADvtxPsMAAAAV"] Apache error 2016-02-27 10:30:03 Error xx.xx.128.85 ModSecurity: [file "/etc/httpd/crs/activated_rules/modsecurity_crs_60_correlation.conf"] [line "37"] [id "981204"] [msg "Inbound Anomaly Score Exceeded (Total Inbound Score: 5, SQLi=0, XSS=0): HTTP protocol version is not allowed by policy"] Warning. Operator GE matched 5 at TX:inbound_anomaly_score. [hostname "mysite.com"] [uri "/myrosip.php"] [unique_id "VtFei5BMStIADvtxPsMAAAAV"] ``` Hello to all.A small comment on zap71's post/script, in "<<SOURCE_LABEL>>"
```
avoid using any spaces, like "Fantastic ROS". It makes the server sad
```

```
---
```

## Response 3
Author: Fri Jul 29, 2016 2:34 am
``` { /tool fetch url="http://myip.dnsomatic.com/" mode=http dst-path=mypublicip.txt local ip [file get mypublicip.txt contents ] put $ip } ``` this script check your publick ip and return in a local variable.ros codeThanks very much... I used this on the script for DDNS update...1. Criar script (código abaixo) com o nome no-ip_ddns_update2. criar a scheduler(ou colar a linha abaixo no terminal)./system scheduler add comment="Update No-IP DDNS" disabled=no interval=5m \name=no-ip_ddns_update on-event=no-ip_ddns_update policy=read, write, testCódigo Script:# Atualização automática de DNS Dinâmico NO-IP#--------------- Defina os valores nessa sessão para configurar ------------------# Informações de acesso NO-IP:local noipuser "EMAIL OU NOME DE LOGIN DO NOIP":local noippass "SENHA DE LOGIN"# Defina o nome do servidor da web a ter o IP atualizado.# O nome do servidor não aceita espaços. Substitua o valor entre as aspas pelo nome(URL) do seu servidor.# Para especificar vários servidores, separe-os com vírgulas.:local noiphost "HOST, EX.: host.ddns.net"#------------------------------------------------------------------------------------# Não precisa alterar mais nada:global previousIP/tool fetch url="http://myip.dnsomatic.com/" mode=http dst-path=mypublicip.txt:local currentIP [file get mypublicip.txt contents]# Strip the net mask off the IP address:for i from=( [:len $currentIP] - 1) to=0 do={:if ( [:pick $currentIP $i] = "/") do={:set currentIP [:pick $currentIP 0 $i]}}:if ($currentIP != $previousIP) do={:log info "No-IP: O ip atual $currentIP não é igual ao IP anterior, atualização necessária":set previousIP $currentIP# The update URL. Note the "\3F" is hex for question mark (?). Required since ? is a special character in commands.:local url "http://dynupdate.no-ip.com/nic/update\3Fmyip=$currentIP":local noiphostarray:set noiphostarray [:toarray $noiphost]:foreach host in=$noiphostarray do={:log info "No-IP: Sending update for $host"/tool fetch url=($url . "&hostname=$host") user=$noipuser password=$noippass mode=http dst-path=("no-ip_ddns_update-" . $host . ".txt"):log info "No-IP: Servidor $host atualizado com o IP $currentIP"}} else={:log info "No-IP: IP anterior $previousIP é igual o IP atual, atualização não necessária."} ---

## Response 4
Author: Sun Jul 31, 2016 9:15 pm
``` :global currentIP [:resolve myip.opendns.com server=208.67.222.222]; ``` is there any way you can make it print the variable or does it have to save to a file.Yes, you can do this:
```
Will always return your public IP. Not needed to download/fetch a file.


---
```

## Response 5
Author: Mon Dec 05, 2016 7:39 pm
ExampleTo enable and activate this service:[admin@MikroTik] /ip cloud set ddns-enabled=yes[admin@MikroTik] /ip cloud printddns-enabled: yesupdate-time: yespublic-address: 159.148.172.205dns-name: 529c0491d41c.sn.mynetname.netstatus: updatedTo enable time update from cloud service:[admin@MikroTik] > ip cloud set update-time=yesTo enable automatic time zone detection:[admin@MikroTik] > system clock set time-zone-autodetect=yesPropertiesSub-menu: /ip cloudTapatalk kullanarak iPhone aracılığıyla gönderildi ---

## Response 6
Author: Fri Jun 15, 2018 11:20 am
Credz goes tohttps://wiki.mikrotik.com/wiki/Dynamic_ ... for_dynDNSThe cloud dns from Mikrotik times out every so often and made me get a paid dyndns account.The following script and scheduling works perfect in 6.x and works behind NAT / private ip. It will update dyn with your external IP.Make a script called: dynDNSPlace the following script in the box[Codebox]:global ddnsuser "username":global ddnspass "password":global ddnshost whatever.your.hostname.is:global ipddns [:resolve $ddnshost];:global ipfresh [:resolve myip.opendns.com server=208.67.222.222];:if ([ :typeof $ipfresh ] = nil ) do={:log info ("DynDNS: No ip address on $theinterface .")} else={:for i from=( [:len $ipfresh] - 1) to=0 do={:if ( [:pick $ipfresh $i] = "/") do={:set ipfresh [:pick $ipfresh 0 $i];}}:if ($ipddns != $ipfresh) do={:log info ("DynDNS: IP-DynDNS = $ipddns"):log info ("DynDNS: IP-Fresh = $ipfresh"):log info "DynDNS: Update IP needed, Sending UPDATE...!":global str "/nic/update\?hostname=$ddnshost&myip=$ipfresh&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG"/tool fetch address=members.dyndns.org src-path=$str mode=http user=$ddnsuser \password=$ddnspass dst-path=("/DynDNS.".$ddnshost):delay 1:global str [/file find name="DynDNS.$ddnshost"];/file remove $str:global ipddns $ipfresh:log info "DynDNS: IP updated to $ipfresh!"} else={:log info "DynDNS: dont need changes";}}[/Codebox]Schedule it (enter the following in a terminal window)[Codebox]/system scheduleradd interval=1m name=dynDNS on-event=dynDNS policy=ftp, reboot, read, write, policy, test, winbox, password, sniff, sensitive, api start-time=startup[/Codebox] ---

## Response 7
Author: Tue Sep 17, 2019 9:34 am
``` { /tool fetch url="http://myip.dnsomatic.com/" mode=http dst-path=mypublicip.txt local ip [file get mypublicip.txt contents ] put $ip } ``` this script check your publick ip and return in a local variable.ros codePlese write code her when my router rebooted without proper-shutdown then this file send to me in my email ---

## Response 8
Author: Tue Sep 17, 2019 7:29 pm
``` :put [/ip cloud get public-address] ``` Why use all these complicate code, when you can just go to IP Cloud and turn it on. Then router does everything for you.To get the IP address in code:
```
---
```

## Response 9
Author: Wed Dec 04, 2019 12:54 am
``` :local filename "currentIP.txt" :local ip [file get currentIP.txt contents]; delay 1 :local cip ([:resolve myip.opendns.com server=208.67.222.222]); delay 1 :local sub ("New WAN address: $cip"); :local bod ("old WAN IP = $ip \nnew WAN IP = $cip"); delay 3 :if ($ip != $cip) do={/tool e-mail send to="your.email@email.com" subject="$sub" body="$bod"; delay 4 /file set $filename contents=$cip } } ``` This one works:before you run the script create a file in Windows calledcurrentIP.txt, write inside some IP address like1.1.1.1, save file and upload it to your router.Run script below:
```
Set a scheduler to run the script every 10 minutes (since startup) and it'll send you an email each time your WAN IP address has been changed.If no change, no emails will be sent.


---
```

## Response 10
Author: Tue Feb 18, 2020 1:35 am
``` # Install this script and name it "GetIPAddress" # Enable the scheduler to run once a day and also on boot /system scheduler add name=RunGetIPAddress1 interval=1d on-event="{:delay 10; /system script run GetIPAddress}" /system scheduler add name=RunGetIPAddress2 start-time=startup on-event="{:delay 120; /system script run GetIPAddress}" # SCRIPT { # declare variables :local filename "GetIPAddress.txt"; :local sNewIP ([:resolve myip.opendns.com server=208.67.222.222]); :local sOldIP (""); :local sURL ("https://server/GetIPAddress.php"); :local sDate [/system clock get date]; :local sTime [/system clock get time]; :local sIdentity [/system identity get name]; # message to post when ip address changes :local sFrom ("PutSomethingHere"); :local sSubject ("IP Address"); :local sBody ("Identity: $sIdentity | IP Address: $sNewIP | Date: $sDate| Time: $sTime"); # begin execution # create file if not found :if ([:len [/file find name=$filename]] <= 0) do={:put ("create file"); /file print file=$filename; delay 3; /file set $filename contents="file";} # read in file :set $sOldIP [/file get $filename contents]; # See if ip address has changed :if ($sOldIP != $sNewIP) do={ # post json string to server :log info "GetIPAddress: posting data to server"; /tool fetch keep-result=no mode=https http-method=post url="$sURL" http-data="{\"From\":\"$sFrom\",\"Subject\":\"$sSubject\",\"Body\":\"$sBody\"}"; # update ip address in file :log info "GetIPAddress: updating IP Address in file"; /file set $filename contents=$sNewIP; } else={ :log info "GetIPAddress: ip address has not changed"; } } ``` ``` <?php // Notifications from MikroTik units out in the field. Customize the $To field below. // time setup date_default_timezone_set('UTC'); // read in the type of request $request = http_build_query($_POST); $size = strlen($request); // verify client has not sent raw POST if($size == 0) { // if client does not send "Content-Type" header then $_POST data is stored in php://input ($HTTP_RAW_POST_DATA). $request = file_get_contents("php://input"); $size = strlen($request); $_POST = $request; } // act on the type of request if($size != 0) { // POST call ProcessPost(); } else { echo "error"; } // Client post a JSON string that look like: // "{'From': 'from', 'Subject': 'subject', 'Body': 'body'}"; function ProcessPost() { # Set to the email address you want posted data to go to. $To = 'test@mailinator.com'; // read in the POST JSON string into object $contents = utf8_encode($_POST); $json = json_decode($contents); // Build the email properties $subject = $json->{'Subject'}; $headers = 'Content-Type: text/plain; charset=utf-8' . "\n" . 'Content-Transfer-Encoding: 8bit' . "\n" . 'From: ' . $json->{'From'} . "\n" . 'Reply-To: ' . $To . "\n" . 'X-Mailer: PHP/' . phpversion(); $message = $json->{'Body'}; // send the email mail($To, $subject, $message, $headers); } ?> ``` I had a need to do this recently. Here is a full working example that posts JSON to a PHP server and then emails the data.Apply this to your router
```
Create aGetIPAddress.phpfile, copy/paste this code, and then place on your server:
```

```
---
```

## Response 11
Author: Wed May 13, 2020 6:13 pm
``` { /tool fetch url="http://myip.dnsomatic.com/" mode=http dst-path=mypublicip.txt local ip [file get mypublicip.txt contents ] put $ip } ``` this script check your publick ip and return in a local variable.ros codeTHANK YOU !!!!Still Works! ---

## Response 12
Author: Mon May 02, 2022 1:53 pm
``` /tool fetch output=user url=https://ipinfo.co.za; ``` ``` status: finished downloaded: 0KiBC-z pause] data: Your IP address is: 81.180.71.14 ``` This is probably the easiest way:
```
Example output:
```

```
---
```

## Response 13
Author: [SOLVED]Mon May 02, 2022 2:29 pm
``` :put [:resolve myip.opendns.com server=208.67.222.222] ``` The result of your "code" isfailure: invalid URLThis is the simplest way, as long as the RouterBOARD can connect to the Internet.
```
---
```

## Response 14
Author: Mon May 02, 2022 6:02 pm
``` :put [/ip cloud get public-address] ``` As I write above.
```
---
```

## Response 15
Author: Thu Mar 16, 2023 4:05 am
``` :put [/ip cloud get public-address] ``` Why use all these complicate code, when you can just go to IP Cloud and turn it on. Then router does everything for you.To get the IP address in code:
```
Works like a charm! Thank you..


---
```

## Response 16
Author: Fri Aug 30, 2024 5:28 pm
``` :put [/ip cloud get public-address] ``` Why use all these complicate code, when you can just go to IP Cloud and turn it on. Then router does everything for you.To get the IP address in code:
```
Jotne, I want to put the dynamic wanip in a dstnat rule.  Note the comment for identification/location purposes./ip firewall natchain=dstnat dst-address-type=local in-interface=WAN2 protocol=udp dst-port=wg-port action=dst-nat to-addresses=dynamic-ip   comment="wireguard-workaround'The only similar script I have is the one to identify new Gateway and insert into routes...:if ($bound=1) do={:local gw $"gateway-address"/ip route set [ find comment="wireguard-workaround" gateway!=$gw ] gateway=$gw}How do I translate that to wanip versus gateweayIP?OR...........using your method which says to me put ( router findable address)   but where is this being put  it seems incomplete??:put [/ip cloud get public-address]


---
```

## Response 17
Author: Sat Aug 31, 2024 5:59 pm
``` { :local test [/ip cloud get public-address] :put $test } ``` Not sure what you mean by where is this being put. I can just add it to a variable and it works fine for me.
```
---
```

## Response 18
Author: Thu Sep 19, 2024 3:53 am
Jotne, I want to put the dynamic wanip in a dstnat rule. Note the comment for identification/location purposes./ip firewall natchain=dstnat dst-address-type=local in-interface=WAN2 protocol=udp dst-port=wg-port action=dst-nat to-addresses=dynamic-ip comment="wireguard-workaround'The only similar script I have is the one to identify new Gateway and insert into routes...:if ($bound=1) do={:local gw $"gateway-address"/ip route set [ find comment="wireguard-workaround" gateway!=$gw ] gateway=$gw}How do I translate that to wanip versus gateweayIP?Greetings anav. Try the code below for the dhcp script. Been using this for other rules as well./ip firewall nat set [find comment="wireguard-workaround"] to-addresses=$"lease-address"