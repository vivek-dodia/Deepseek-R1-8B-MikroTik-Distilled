# Thread Information
Title: Thread-1117413
Section: RouterOS
Thread ID: 1117413

# Discussion

## Initial Question
I don't know if this will help MT and/or the experts here with the "disconnected" problem, but I have what, to me, is interesting info.I have a wAP running 7.16.1, qcom-ac, with interface "wifi2ghz" and a slave interface "2point4"Three devices at approximately 150 meters connect to 2point4 (all Sonoff THR-316) and stay connected rock solid, with signal strength between -76 and -84.Another device (Emporia Vue) at about 100 meters (but behind the wAP) tries to connect to wifi2ghz and continuously gets "connected" then "disconnected", even with signal strength around -70.
```
16:21:16wireless,info84:0D:8E:38:C0:64@wifi2ghzdisconnected,connection lost,signal strength-7016:21:17wireless,info84:0D:8E:38:C0:64@wifi2ghzconnected,signal strength-60Nothing else in the logs, even with topics wireless and debug enabled.From what I can tell, wifi2ghz and 2point4 are set up identically.Sounds like the problem is specific to the client, or client-AP pairing.Here is the registration table for the 3 rock-solid connected devices:
```

```
[admin@355wap-carport]/interface/wifi/registration-table>printbriefFlags:A-AUTHORIZEDColumns:INTERFACE,SSID,MAC-ADDRESS,UPTIME,SIGNAL#   INTERFACE  SSID     MAC-ADDRESS        UPTIME     SIGNAL;;;Hoophouse30A2point42point43C:E9:0E:89:EB:A411h1m54s-83;;;Hoophouse11A2point42point43C:E9:0E:8A:13:4410h31m12s-76;;;Hoophouse22A2point42point4C0:49:EF:F7:B9:F810h17m38s-81Here is the wAP config:
```

```
# 2024-11-17 16:28:50 by RouterOS 7.16.1# software id = D04C-WYEI## model = RBwAPG-5HacD2HnD# serial number = HDA0/interfacebridgeaddadmin-mac=18:FD:74:50:0F:CBauto-mac=nocomment=defconf name=bridge port-cost-mode=short/interfaceethernetset[finddefault-name=ether1]mac-address=18:FD:74:50:0F:CA/interfaceethernetset[finddefault-name=ether2]mac-address=18:FD:74:50:0F:CB/interfacewifiset[finddefault-name=wifi2]channel.band=5ghz-ac.frequency=5490-5570.skip-dfs-channels=disabled.width=20/40/80mhzcomment=wifi-5ghzconfiguration.country="United States".mode=ap.ssid=Chickens-5ghzdisabled=noname=wifi-5ghzsecurity.authentication-types=wpa2-psk.passphrase=<password>1!/interfacewifiset[finddefault-name=wifi1]channel.band=2ghz-n.frequency=2412.skip-dfs-channels=disabled.width=20mhzcomment=wifi2ghz configuration.country="United States".mode=ap.ssid=Chickensdisabled=noname=wifi2ghz security.authentication-types=wpa2-psk.passphrase=<password>1!/interfacewifiaddcomment=2point4configuration.mode=ap.ssid=2point4disabled=nomac-address=1A:FD:74:D7:58:38master-interface=wifi2ghz name=2point4security.authentication-types=wpa2-psk.passphrase=<password>1!/interfacelistaddcomment=defconf name=WAN/interfacelistaddcomment=defconf name=LAN/interfacelte apnset[finddefault=yes]ip-type=ipv4use-network-apn=no/ip pooladdname=192.168.0.220-192.168.0.251ranges=192.168.0.220-192.168.0.251/ip dhcp-serveraddaddress-pool=192.168.0.220-192.168.0.251interface=bridge lease-time=1hname=defconf/ip smb usersset[finddefault=yes]disabled=yes/routing bgptemplatesetdefaultdisabled=nooutput.network=bgp-networks/routing ospf instanceadddisabled=noname=default-v2/routing ospf areaadddisabled=yes instance=default-v2 name=backbone-v2/system logging actionset3remote=192.168.0.13/system logging actionaddname=logserver remote=192.168.0.112remote-port=51400target=remote/interfacebridge filteraddaction=drop chain=forward disabled=yes ip-protocol=udp log=yes mac-protocol=ip src-address=0.0.0.0/0src-port=67/interfacebridge portaddbridge=bridge comment=defconf ingress-filtering=nointerface=ether2internal-path-cost=10path-cost=10/interfacebridge portaddbridge=bridge comment=defconf disabled=yes ingress-filtering=nointerface=*3internal-path-cost=10learn=yes path-cost=10/interfacebridge portaddbridge=bridge comment=defconf disabled=yes ingress-filtering=nointerface=*4internal-path-cost=10path-cost=10/interfacebridge portaddbridge=bridge ingress-filtering=nointerface=ether1internal-path-cost=10path-cost=10/interfacebridge portaddbridge=bridge disabled=yes ingress-filtering=nointerface=*6internal-path-cost=10learn=yes path-cost=10/interfacebridge portaddbridge=bridgeinterface=wifi-5ghz/interfacebridge portaddbridge=bridgeinterface=wifi2ghz/interfacebridge portaddbridge=bridgeinterface=2point4/ip firewall connection trackingsetudp-timeout=10s/ip neighbor discovery-settingssetdiscover-interface-list=all/ip settingssetmax-neighbor-entries=8192/ipv6 settingssetdisable-ipv6=yes max-neighbor-entries=8192/interfacelist memberaddcomment=defconfinterface=bridge list=LAN/interfacelist memberaddcomment=defconf disabled=yesinterface=ether1 list=WAN/interfacelist memberaddinterface=ether1 list=LAN/interfaceovpn-server serversetauth=sha1,md5/interfacewifi access-listaddaction=accept comment="Hoophouse 3"disabled=nomac-address=3C:E9:0E:89:EB:A4/interfacewifi access-listaddaction=accept comment="Hoophouse 2"disabled=nomac-address=C0:49:EF:F7:B9:F8/interfacewifi access-listaddaction=accept comment="Diego's phone"disabled=nomac-address=2E:34:7B:25:BF:18/interfacewifi access-listaddaction=accept comment="Hoophouse 1"disabled=nomac-address=3C:E9:0E:8A:13:44/interfacewifi access-listaddaction=accept comment="Vue White"disabled=nomac-address=84:0D:8E:38:C0:64/ip addressaddaddress=192.168.0.80/24interface=bridge network=192.168.0.0/ip cloudsetddns-enabled=yes/ip dhcp-server leaseaddaddress=192.168.0.251client-id=1:c0:49:ef:f7:b9:f8 comment="THR316 Hoophouse 1"mac-address=C0:49:EF:F7:B9:F8 server=defconf/ip dhcp-server leaseaddaddress=192.168.0.249comment="TH10 Hoophouse 1"mac-address=E8:DB:84:9D:BD:BE server=defconf/ip dhcp-server leaseaddaddress=192.168.0.246comment="Shelly Uni Hoophouse 1"mac-address=E8:68:E7:F4:6E:29server=defconf/ip dhcp-server leaseaddaddress=192.168.0.243comment="Hoophouse Shelly Uni Tasmota 1"mac-address=C4:5B:BE:E2:0E:C0 server=defconf/ip dhcp-server leaseaddaddress=192.168.0.250comment="Emporia Vue"mac-address=10:52:1C:41:FA:A0 server=defconf/ip dhcp-server leaseaddaddress=192.168.0.245comment=tasmota-DED0DB-4315mac-address=C4:5B:BE:DE:D0:DB server=defconf/ip dhcp-server leaseaddaddress=192.168.0.244comment=Flume-GW-B70E mac-address=48:55:19:65:B7:0Eserver=defconf/ip dhcp-server leaseaddaddress=192.168.0.233block-access=yes comment="Emporia Vue (probably White)"disabled=yes mac-address=84:0D:8E:38:C0:64/ip dhcp-server leaseaddaddress=192.168.0.234client-id=1:3c:e9:e:89:eb:a4 comment=Hoophouse-3mac-address=3C:E9:0E:89:EB:A4 server=defconf/ip dhcp-server leaseaddaddress=192.168.0.235client-id=1:3c:e9:e:8a:13:44mac-address=3C:E9:0E:8A:13:44server=defconf/ip dhcp-server leaseaddaddress=192.168.0.224comment="Vue White"mac-address=84:0D:8E:38:C0:64server=defconf/ip dhcp-server leaseaddcomment="Ecobee Well"mac-address=44:61:32:3D:A4:4A/ip dhcp-server networkaddaddress=192.168.0.0/32dns-server=192.168.0.11gateway=192.168.0.1netmask=24/ip dnssetallow-remote-requests=yes servers=1.1.1.1,8.8.8.8,9.9.9.9,8.8.4.4/ip hotspot profileset[finddefault=yes]html-directory=hotspot/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip kid-controladdfri=0s-1dmon=0s-1dname=Monitorsat=0s-1dsun=0s-1dthu=0s-1dtue=0s-1dwed=0s-1d/ip routeadddisabled=nodst-address=0.0.0.0/0gateway=192.168.0.1routing-table=main suppress-hw-offload=no/ip servicesetwww-ssl disabled=no/ip smb sharesset[finddefault=yes]directory=/flash/pub/system clocksettime-zone-name=America/New_York/system identitysetname=355wap-carport/system loggingaddtopics=watchdog/system loggingaddaction=logserver prefix="serial=HDA08AX72ZK MikroTik"topics=hotspot/system loggingaddaction=logserver prefix="serial=HDA08AX72ZK MikroTik"topics=!debug,!packet,!snmp/system loggingaddaction=remote prefix="192.168.0.80 "topics=info/system loggingadddisabled=yes topics=debug/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=0.id.pool.ntp.org/system ntp client serversaddaddress=1.id.pool.ntp.org/system scheduleraddinterval=2dname=export-download on-event=export-download policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=2023-08-28start-time=01:32:53/system scheduleraddinterval=2wname=dynamic-data-rextended on-event=dynamic-data-rextended policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=2023-09-30start-time=02:58:29/system scheduleradddisabled=yes interval=5mname=Data_to_Splunkon-event=Data_to_Splunk_using_Syslogpolicy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=2024-09-06start-time=20:24:13/system scheduleraddname=SystemInfoJRSon-event=":delay 60\
    \n/system script run SystemInfoJRS"policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-time=startup/system scriptadddont-require-permissions=noname=export-download owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/system\r\
    \n:local cdate [clock get date] \r\
    \n:local yyyy  [:pick \$cdate 0  4]\r\
    \n:local MM    [:pick \$cdate 5  7]\r\
    \n:local dd    [:pick \$cdate 8 10]\r\
    \n:local identitydate \"\$[identity get name]_\$yyyy-\$MM-\$dd\"\r\
    \n/export show-sensitive file=\"\$identitydate\"\r\
    \n\r\
    \n/tool fetch upload=yes mode=ftp ascii=no src-path=\"/\$[\$identitydate].rsc\" dst-path=\"/mikrotik-backups/\$[\$identitydate].rsc\" address=192.168.2.22 port=21 user=mikrotik password=mikrotik\r\
    \n\r\
    \n/file remove \"\$[\$identitydate].rsc\"\r\
    \n\r\
    \n:log info (\"Uploaded rsc backup to 192.168.2.22 as \".\$identitydate)\r\
    \n\r\
    \n"/system scriptadddont-require-permissions=noname=backup owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/system\r\
    \n:local cdate [clock get date] \r\
    \n:local yyyy  [:pick \$cdate 0  4]\r\
    \n:local MM    [:pick \$cdate 5  7]\r\
    \n:local dd    [:pick \$cdate 8 10]\r\
    \n:local identitydate \"\$[identity get name]_\$yyyy-\$MM-\$dd\"\r\
    \n\r\
    \n\r\
    \n/system backup save name=\$identitydate\r\
    \n\r\
    \n/tool fetch upload=yes mode=ftp ascii=no src-path=\"/\$[\$identitydate].backup\" dst-path=\"/mikrotik-backups/\$[\$identitydate].backup\" address=192.168.2.22 port=21 user=mikrotik password=mikrotik\r\
    \n\r\
    \n/file remove \"\$[\$identitydate].backup\"\r\
    \n\r\
    \n"/system scriptadddont-require-permissions=noname="Get IP Addresses"owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/interface bridge host\r\
    \n:foreach item in=[find] do={\r\
    \n    :local iface  [get \$item interface]\r\
    \n    :local macadd [get \$item mac-address]\r\
    \n    :local idmac  [/ip arp find where mac-address=\$macadd]\r\
    \n    :if ([:len \$idmac] = 1) do={\r\
    \n        :local ifip [/ip arp get \$idmac address]\r\
    \n        :local HOST [/ip arp get \$idmac hostname]\r\
    \n        :put   \"interface=\$iface mac=\$macadd ip=\$ifip\"\r\
    \n        :log info \"interface=\$iface mac=\$macadd ip=\$ifip\"\r\
    \n\r\
    \n    }\r\
    \n}\r\
    \n"/system scriptadddont-require-permissions=noname=hello owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="        :log info \"hello\""/system scriptadddont-require-permissions=noname=dynamic-data-rextended owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/system\r\
    \n:local identitydate \"\$[identity get name]_\$[clock get date]\"\r\
    \n:local stringexec   \"/system iden print; :put \\\"\\\\r\\\\n\\\"; /ip cloud pri; :put \\\"\\\\r\\\\n\\\";  /ip dhcp-server lease pri det; :put \\\"\\\\r\\\\n\\\"; /int bridge host pri det\"\r\
    \n\r\
    \n:if ([:len [/system package find where name=\"wifiwave2\"]] > 1) do={\r\
    \n    :set stringexec \"\$stringexec; :put \\\"\\\\r\\\\n\\\" /int wifiwave2 reg pri det\"\r\
    \n} \r\
    \n\r\
    \n:if ([:len [/system package find where name=\"wifiwave2\"]] > 1) do={\r\
    \n    :set stringexec \"\$stringexec; :put \\\"\\\\r\\\\n\\\" /int wireless reg pri det\"\r\
    \n}\r\
    \n\r\
    \n\r\
    \n/file remove [find where name=tmpresults.txt]\r\
    \n:delay 1s\r\
    \n:execute \$stringexec file=tmpresults.txt\r\
    \n:delay 2s\r\
    \n\r\
    \n/tool fetch upload=yes mode=ftp ascii=no address=192.168.2.22 port=21 user=mikrotik password=mikrotik \\\r\
    \n    src-path=tmpresults.txt dst-path=\"/mikrotik-backups/\$identitydate-dynamicdata.txt\"\r\
    \n\r\
    \n/file remove [find where name=tmpresults.txt]"/system scriptadddont-require-permissions=noname=Data_to_Splunk_using_Syslogowner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Collect information from Mikrotik RouterOS\r\
    \n# Jotne 2024\r\
    \n# Script name=Data_to_Splunk_using_Syslog\r\
    \n:log info message=\"script=version ver=5.6\"\r\
    \n# ----------------------------------\r\
    \n\r\
    \n# Auto update syslog server. 5.3-5.4.\r\
    \n# Change <your syslog dns name> to the dns of your syslog server.\r\
    \n# The update is disabled by default.  Remove the # from the two next line to use it.\r\
    \n\r\
    \n#:local mySyslog [resolve <your syslog dns name>]\r\
    \n#/system/logging/action/set [find where name=\"logserver\"] remote=\$mySyslog\r\
    \n\r\
    \n\r\
    \n# What data to collect.  Set to false to skip the section \r\
    \n# ----------------------------------\r\
    \n:local SystemResource true\r\
    \n:local SystemInformation true\r\
    \n:local SystemHealth true\r\
    \n:local TrafficData true\r\
    \n:local AccountData true\r\
    \n:local uPnP true\r\
    \n:local Wireless true\r\
    \n:local AddressLists true\r\
    \n:local DHCP true\r\
    \n:local Neighbor true\r\
    \n:local InterfaceData true\r\
    \n:local CmdHistory true\r\
    \n:local CAPsMANN false\r\
    \n\r\
    \n:local Routing true\r\
    \n:local OSPF false\r\
    \n:local BGP false\r\
    \n\r\
    \n:local PPP true\r\
    \n:local IPSEC true\r\
    \n\r\
    \n# Get RouterOS main version (used to run different script on different version)\r\
    \n:local train [:tonum [:pick [/system resource get version] 0 1]] \r\
    \n\r\
    \n# Collect system resource\r\
    \n# ----------------------------------\r\
    \n:if (\$SystemResource) do={\r\
    \n\t/system resource\r\
    \n\t:local cpuload [get cpu-load]\r\
    \n\t:local freemem ([get free-memory]/1048576)\r\
    \n\t:local totmem ([get total-memory]/1048576)\r\
    \n\t:local freehddspace ([get free-hdd-space]/1048576)\r\
    \n\t:local totalhddspace ([get total-hdd-space]/1048576)\r\
    \n\t:local up [get uptime]\r\
    \n\t:local sector [get write-sect-total]\r\
    \n\t:log info message=\"script=resource free_memory=\$freemem MB total_memory=\$totmem MB free_hdd_space=\$freehddspace MB total_hdd_space=\$totalhddspace MB cpu_load=\$cpuload uptime=\$up write-sect-total=\$sector\"\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Make some part only run every hours\r\
    \n# ----------------------------------\r\
    \n:global Hour\r\
    \n:local run false\r\
    \n:local hour [:pick [/system clock get time] 0 2]\r\
    \n:if (\$Hour != \$hour) do={\r\
    \n\t:global Hour \$hour\r\
    \n\t:set run true\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Get NTP status\r\
    \n# ----------------------------------\r\
    \n:local ntpstatus \"\"\r\
    \n:if ([:len [/system package find where !disabled and name=ntp]] > 0 or [:tonum [:pick [/system resource get version] 0 1]] > 6) do={\r\
    \n    :set ntpstatus [/system ntp client get status]\r\
    \n} else={\r\
    \n    :if ([:typeof [/system ntp client get last-update-from]] = \"nil\") do={\r\
    \n        :set ntpstatus \"using-local-clock\"\r\
    \n    } else={\r\
    \n        :set ntpstatus \"synchronized\"\r\
    \n    }\r\
    \n}\r\
    \n:log info message=\"script=ntp status=\$ntpstatus\" \r\
    \n\r\
    \n\r\
    \n# Get interface traffic data for all interface\r\
    \n# ----------------------------------\r\
    \n:if (\$TrafficData) do={\r\
    \n\t:foreach id in=[/interface find] do={\r\
    \n\t\t:local output \"\$[/interface print stats as-value where .id=\$id]\"\r\
    \n\t\t:set ( \"\$output\"->\"script\" ) \"if_traffic\"\r\
    \n\t\t:log info message=\"\$output\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Get traffic data v2 (Kid Control)\r\
    \n# ----------------------------------\r\
    \n:if (\$AccountData) do={\r\
    \n\t:foreach logline in=[/ip kid-control device find] do={\r\
    \n\t\t:local output \"\$[/ip kid-control device get \$logline]\"\r\
    \n\t\t:set ( \"\$output\"->\"script\" ) \"kids\"\r\
    \n\t\t:log info message=\"\$output\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Finding dynmaic lines used in uPnP\r\
    \n# ----------------------------------\r\
    \n:if (\$uPnP) do={\r\
    \n\t:foreach logline in=[/ip firewall nat find where dynamic=yes and comment~\"^upnp \"] do={\r\
    \n\t\t:local output \"\$[/ip firewall nat print as-value from=\$logline]\"\r\
    \n\t\t:set ( \"\$output\"->\"script\" ) \"upnp\"\r\
    \n\t\t:log info message=\"\$output\" \r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Collect system information 5.5 added ID for non routerBoard 5.6 Remvoed serial\r\
    \n# ----------------------------------\r\
    \n:local model na\r\
    \n:local ffirmware na\r\
    \n:local cfirmware na\r\
    \n:local ufirmware na\r\
    \n:if (\$SystemInformation and \$run) do={\r\
    \n\t:local version ([/system resource get version])\r\
    \n\t:local board ([/system resource get board-name])\r\
    \n\t:local identity ([/system identity get name])\r\
    \n\t:do {\r\
    \n\t\t:if (\$board!=\"CHR\" OR \$board!=\"x86\") do={\r\
    \n\t\t\t/system routerboard\r\
    \n\t\t\t:set model ([get model])\r\
    \n\t\t\t:set ffirmware ([get factory-firmware])\r\
    \n\t\t\t:set cfirmware ([get current-firmware])\r\
    \n\t\t\t:set ufirmware ([get upgrade-firmware])\r\
    \n\t\t}\r\
    \n\t} on-error={}\r\
    \n\t:log info message=\"script=sysinfo version=\\\"\$version\\\" board-name=\\\"\$board\\\" model=\\\"\$model\\\" identity=\\\"\$identity\\\" factory-firmware=\\\"\$ffirmware\\\" current-firmware=\\\"\$cfirmware\\\" upgrade-firmware=\\\"\$ufirmware\\\"\"\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Collect system health\r\
    \n# ----------------------------------\r\
    \n:if (\$train > 6 and \$SystemHealth) do={\r\
    \n\t# New version (RouterOS >6)\r\
    \n\t:foreach id in=[/system health find] do={\r\
    \n\t\t:local health \"\$[/system health get \$id]\"\r\
    \n\t\t:set ( \"\$health\"->\"script\" ) \"health\"\r\
    \n\t\t:log info message=\"\$health\"\r\
    \n\t}\r\
    \n} else={\r\
    \n\t# Old version (RouterOS 6 or older)\r\
    \n\t:if (!([/system health get]~\"(state=disabled|^\\\$)\")) do={\r\
    \n\t\t:local health \"\$[/system health get]\"\r\
    \n\t\t:set ( \"\$health\"->\"script\" ) \"health\"\r\
    \n\t\t:log info message=\"\$health\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n\r\
    \n# Sends wireless client data to log server \r\
    \n# ----------------------------------\r\
    \n:if (\$Wireless && [:len [/int find where type=wlan]]>0) do={\r\
    \n\t/interface wireless registration-table\r\
    \n\t:foreach i in=[find] do={\r\
    \n\t\t:log info message=\".id=\$i;ap=\$([get \$i ap]);interface=\$([get \$i interface]);mac-address=\$([get \$i mac-address]);signal-strength=\$([get \$i signal-strength]);tx-rate=\$([get \$i tx-rate]);uptime=\$([get \$i uptime]);script=wifi\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Count IP in address-lists\r\
    \n#----------------------------------\r\
    \n:if (\$AddressLists) do={\r\
    \n\t:local array [ :toarray \"\" ]\r\
    \n\t:local addrcntdyn [:toarray \"\"] \r\
    \n\t:local addrcntstat [:toarray \"\"] \r\
    \n\t:local test\r\
    \n\t:foreach id in=[/ip firewall address-list find] do={\r\
    \n\t\t:local rec [/ip firewall address-list get \$id]\r\
    \n\t\t:local listname (\$rec->\"list\")\r\
    \n\t\t:local listdynamic (\$rec->\"dynamic\")\r\
    \n\t\t:if (!(\$array ~ \$listname)) do={ :set array (\$array , \$listname) }\r\
    \n\t\t:if (\$listdynamic = true) do={\r\
    \n\t\t\t:set (\$addrcntdyn->\$listname) (\$addrcntdyn->\$listname+1)\r\
    \n\t\t} else={\r\
    \n\t\t\t:set (\$addrcntstat->\$listname) (\$addrcntstat->\$listname+1)}\r\
    \n\t}\r\
    \n\t:foreach k in=\$array do={\r\
    \n\t\t:log info message=(\"script=address_lists list=\$k dynamic=\".((\$addrcntdyn->\$k)+0).\" static=\".((\$addrcntstat->\$k)+0))}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Get MNDP (CDP) Neighbors\r\
    \n# ----------------------------------\r\
    \n:if (\$Neighbor and \$run) do={\r\
    \n\t:foreach neighborID in=[/ip neighbor find] do={\r\
    \n\t\t:local nb [/ip neighbor get \$neighborID]\r\
    \n\t\t:local id [:pick (\"\$nb\"->\".id\") 1 99]\r\
    \n\t\t:foreach key,value in=\$nb do={\r\
    \n\t\t\t:local newline [:find \$value \"\\n\"]\r\
    \n\t\t\t:if ([\$newline]>0) do={\r\
    \n\t\t\t\t:set value [:pick \$value 0 \$newline]\r\
    \n\t\t\t}\r\
    \n\t\t\t:log info message=\"script=neighbor nid=\$id \$key=\\\"\$value\\\"\"\r\
    \n\t\t}\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Collect DHCP Pool information\r\
    \n# ----------------------------------\r\
    \n:if (\$DHCP and \$run) do={\r\
    \n\t/ip pool {\r\
    \n\t\t:local poolname\r\
    \n\t\t:local pooladdresses\r\
    \n\t\t:local poolused\r\
    \n\t\t:local minaddress\r\
    \n\t\t:local maxaddress\r\
    \n\t\t:local findindex\r\
    \n\r\
    \n# Iterate through IP Pools\r\
    \n\t\t:foreach pool in=[find] do={\r\
    \n\t\t\t:set poolname [get \$pool name]\r\
    \n\t\t\t:set pooladdresses 0\r\
    \n\t\t\t:set poolused 0\r\
    \n\r\
    \n# Iterate through current pool's IP ranges\r\
    \n\t\t\t:foreach range in=[:toarray [get \$pool range]] do={\r\
    \n\r\
    \n# Get min and max addresses\r\
    \n\t\t\t\t:set findindex [:find [:tostr \$range] \"-\"]\r\
    \n\t\t\t\t:if ([:len \$findindex] > 0) do={\r\
    \n\t\t\t\t\t:set minaddress [:pick [:tostr \$range] 0 \$findindex]\r\
    \n\t\t\t\t\t:set maxaddress [:pick [:tostr \$range] (\$findindex + 1) [:len [:tostr \$range]]]\r\
    \n\t\t\t\t} else={\r\
    \n\t\t\t\t\t:set minaddress [:tostr \$range]\r\
    \n\t\t\t\t\t:set maxaddress [:tostr \$range]\r\
    \n\t\t\t\t}\r\
    \n\r\
    \n# Calculate number of ip in one range\r\
    \n\t\t\t\t:set pooladdresses (\$maxaddress - \$minaddress)\r\
    \n\r\
    \n# /foreach range\r\
    \n\t\t\t}\r\
    \n\r\
    \n# Test if pools is used in DHCP or VPN and show leases used\r\
    \n\t\t\t:local dname [/ip dhcp-server find where address-pool=\$poolname]\r\
    \n\t\t\t:if ([:len \$dname] = 0) do={\r\
    \n# No DHCP server found, assume VPN\r\
    \n\t\t\t\t:set poolused [:len [used find pool=[:tostr \$poolname]]]\r\
    \n\t\t\t} else={\r\
    \n# DHCP server found, count leases\r\
    \n\t\t\t\t:local dname [/ip dhcp-server get [find where address-pool=\$poolname] name]\r\
    \n\t\t\t\t:set poolused [:len [/ip dhcp-server lease find where server=\$dname]]}\r\
    \n\r\
    \n# Send data\r\
    \n\t\t\t:log info message=(\"script=pool pool=\$poolname used=\$poolused total=\$pooladdresses\")\r\
    \n\r\
    \n# /foreach pool\r\
    \n\t\t}\r\
    \n# /ip pool\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Get detailed command history RouterOS >= v7\r\
    \n# ----------------------------------\r\
    \n:if (\$train > 6 and \$CmdHistory) do={\r\
    \n\t:global cmd\r\
    \n\t:local f 0\r\
    \n\t:foreach i in=[/system history find] do={\r\
    \n\t\t:if (\$i = \$cmd) do={ :set f 1 }\r\
    \n\t\t:if (\$f != 1) do={\r\
    \n\t\t\t:log info message=\"StartCMD\"\r\
    \n\t\t\t:log info message=[/system history get \$i]\r\
    \n\t\t\t:log info message=\"EndCMD\"\r\
    \n\t\t}\r\
    \n\t}\r\
    \n\t:global cmd  [:pick [/system history find] 0]\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Test if CAPsMANN is installed and run script 5.5\r\
    \n# ----------------------------------\r\
    \n:if ( ([:len [/interface find where type=\"cap\"]] > 0) and \$CAPsMANN) do={ \r\
    \n\t/system script run CAPsMANN\r\
    \n}\r\
    \n\r\
    \n\r\
    \n\r\
    \n# Collect routing information\r\
    \n# ----------------------------------\r\
    \n:if (\$Routing) do={\r\
    \n\t/ip route\r\
    \n\t:foreach id in=[find] do={\r\
    \n\t\t:local route \"\$[get \$id]\"\r\
    \n\t\t:set ( \"\$route\"->\"script\" ) \"route\"\r\
    \n\t\t:log info message=\"\$route\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n:if (\$OSPF) do={\r\
    \n\t/routing ospf neighbor\r\
    \n\t:foreach id in=[find] do={\r\
    \n\t\t:local ospf \"\$[get \$id]\"\r\
    \n\t\t:set ( \"\$ospf\"->\"script\" ) \"ospf\"\r\
    \n\t\t:log info message=\"\$ospf\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n:if (\$BGP) do={\r\
    \n\t/routing bgp session\r\
    \n\t:foreach id in=[find] do={\r\
    \n\t\t:local bgp \"\$[get \$id]\"\r\
    \n\t\t:set ( \"\$bgp\"->\"script\" ) \"bgp\"\r\
    \n\t\t:log info message=\"\$bgp\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n\r\
    \n# Collect PPP/IPSEC\r\
    \n# ----------------------------------\r\
    \n:if (\$PPP) do={\r\
    \n\t/ppp active\r\
    \n\t:foreach id in=[find] do={\r\
    \n\t\t:local ppp \"\$[get \$id]\"\r\
    \n\t\t:set ( \"\$ppp\"->\"script\" ) \"ppp\"\r\
    \n\t\t:log info message=\"\$ppp\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n:if (\$IPSEC) do={\r\
    \n\t/ip ipsec active-peers\r\
    \n\t:foreach id in=[find] do={\r\
    \n\t\t:local ipsec \"\$[get \$id]\"\r\
    \n\t\t:set ( \"\$ipsec\"->\"script\" ) \"ipsec\"\r\
    \n\t\t:log info message=\"\$ipsec\"\r\
    \n\t}\r\
    \n}\r\
    \n\r\
    \n# End Script\r\
    \n\r\
    \n"/system scriptadddont-require-permissions=yes name=Netwatchowner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="####################################\r\
    \n# Netwatch script\r\
    \n#\r\
    \n# Used as both up and down script\r\
    \n# Created Jotne 2021 v1.5\r\
    \n#\r\
    \n####################################\r\
    \n:local Host \$host\r\
    \n/tool netwatch\r\
    \n:local Status [get [find where host=\"\$Host\"] status]\r\
    \n:local Comment [get [find where host=\"\$Host\"] comment]\r\
    \n:local Interval [get [find where host=\"\$Host\"] interval]\r\
    \n:local Since [get [find where host=\"\$Host\"] since]\r\
    \n:log info \"script=netwatch watch_host=\$Host comment=\\\"\$Comment\\\" status=\$Status interval=\$Interval since=\\\"\$Since\\\"\""/system scriptadddont-require-permissions=noname=SystemInfoJRSowner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="\
    \n# Collect system resource\
    \n\t/system resource\
    \n\t:local cpuload [get cpu-load]\
    \n\t:local freemem ([get free-memory]/1048576)\
    \n\t:local totmem ([get total-memory]/1048576)\
    \n\t:local freehddspace ([get free-hdd-space]/1048576)\
    \n\t:local totalhddspace ([get total-hdd-space]/1048576)\
    \n\t:local up [get uptime]\
    \n\t:local sector [get write-sect-total]\
    \n\t:log info message=\"free_memory=\$freemem MB total_memory=\$totmem MB free_hdd_space=\$freehddspace MB total_hdd_space=\$totalhddspace MB cpu_load=\$cpuload uptime=\$up write-sect-total=\$sector\"\
    \n\
    \n\
    \n\
    \n# Collect system information 5.5 added ID for non routerBoard 5.6 Remvoed serial\
    \n:local model na\
    \n:local ffirmware na\
    \n:local cfirmware na\
    \n:local ufirmware na\
    \n\
    \n\t:local version ([/system resource get version])\
    \n\t:local board ([/system resource get board-name])\
    \n\t:local identity ([/system identity get name])\
    \n\t:do {\
    \n\t\t:if (\$board!=\"CHR\" OR \$board!=\"x86\") do={\
    \n\t\t\t/system routerboard\
    \n\t\t\t:set model ([get model])\
    \n\t\t\t:set ffirmware ([get factory-firmware])\
    \n\t\t\t:set cfirmware ([get current-firmware])\
    \n\t\t\t:set ufirmware ([get upgrade-firmware])\
    \n\t\t}\
    \n\t} on-error={}\
    \n\t:log info message=\"version=\\\"\$version\\\" board-name=\\\"\$board\\\" model=\\\"\$model\\\" identity=\\\"\$identity\\\"\"\
    \n\
    \n\
    \n# Collect IP addresses\
    \n:foreach neighborID in=[/ip address find] do={\
    \n\t\t:local nb [/ip address get \$neighborID]\
    \n\t\t:local id [:pick (\"\$nb\"->\".id\") 1 99]\
    \n\t\t:foreach key,value in=\$nb do={\
    \n\t\t\t:local newline [:find \$value \"\\n\"]\
    \n\t\t\t:if ([\$newline]>0) do={\
    \n\t\t\t\t:set value [:pick \$value 0 \$newline]\
    \n\t\t\t}\
    \n\t\t\t:if (\$key~\"add\") do={\
    \n#\t\t\t:log info message=\"script=IP-ADDRESSES nid=\$id value=\$key=\\\"\$value\\\"\"\
    \n\
    \n\t\t\t:log info message=\"System IP Address \$value\"\
    \n\t\t    }\
    \n\t    }\
    \n}\
    \n\
    \n\
    \n# Collect system health\
    \n#\t:foreach id in=[/system health find] do={\
    \n#\t\t:local health \"\$[/system health get \$id]\"\
    \n#\t\t:set ( \"\$health\"->\"script\" ) \"health\"\
    \n#\t\t:log info message=\"\$health\"\
    \n#\t}\
    \n\
    \n\
    \n\
    \n\
    \n# Get MNDP (CDP) Neighbors\
    \n#\t:foreach neighborID in=[/ip neighbor find] do={\
    \n#\t\t:local nb [/ip neighbor get \$neighborID]\
    \n#\t\t:local id [:pick (\"\$nb\"->\".id\") 1 99]\
    \n#\t\t:foreach key,value in=\$nb do={\
    \n#\t\t\t:local newline [:find \$value \"\\n\"]\
    \n#\t\t\t:if ([\$newline]>0) do={\
    \n#\t\t\t\t:set value [:pick \$value 0 \$newline]\
    \n#\t\t\t}\
    \n#\t\t\t:log info message=\"script=neighbor nid=\$id \$key=\\\"\$value\\\"\"\
    \n#\t\t}\
    \n#\t}\
    \n\
    \n\
    \n\
    \n\
    \n\
    \n"/system watchdogsetauto-send-supout=yes ping-start-after-boot=10mping-timeout=7msend-email-from=joseph@domain.com send-email-to=joseph@domain.com watch-address=1.1.1.1/tool netwatchadddisabled=nodown-script=Netwatchhost=1.1.1.1http-codes=""interval=5mname=Netwatch-1.1.1.1test-script=""type=simple up-script=Netwatch/tool romonsetenabled=yes/tool sniffersetfilter-interface=all filter-mac-address=3C:E9:0E:89:EB:A4/FF:FF:FF:FF:FF:FFEDIT:  I tried using G instead of N and the same behaviour occurs.

---
```

## Response 1
According to your posted and commented config "84:0D:8E:38:C0:64" is "Vue White" and not "Emporia Vue". ---

## Response 2
Onlyin case that the Emporia Vue is theonlydevice to connect to thewifi2ghzinterface, the following command might help:/interface bridge port set [find where bridge=bridge interface=wifi2ghz] edge=yesThe background is the following: if no station (client) is associated to an AP, the "ethernet side" of the AP goes down, so if it is configured as a port of a bridge, the bridge behaves as if you disconnected a cable from the port. Since by default, RSTP is allowed on bridges to prevent L2 loops from forming up in case of cabling mistakes, the port does not forward traffic for some seconds after you "connect the cable", waiting for eventual RSTP BPDUs to arrive. During that time, the associated wireless station cannot obtain a DHCP lease as its DHCPDISCOVER packets get nowhere. If the Emporia Vue implementation is "impatient", it may give up and start from scratch before the RSTP switches the bridge port to "forwarding" state, so the cycle keeps going on like this. ---

## Response 3
According to your posted and commented config "84:0D:8E:38:C0:64" is "Vue White" and not "Emporia Vue".Sorry for the confusion:"Emporia Vue" is the name of the company (Emporia) and product (Vue). I stated it this way so the reader would know what the device/client is."Vue White" is my internal name so I can identify which Emporia Vue this is (I have many). ---

## Response 4
Onlyin case that the Emporia Vue is theonlydevice to connect to thewifi2ghzinterface, the following command might help:/interface bridge port set [find where bridge=bridge interface=wifi2ghz] edge=yesThe background is the following: if no station (client) is associated to an AP, the "ethernet side" of the AP goes down, so if it is configured as a port of a bridge, the bridge behaves as if you disconnected a cable from the port. Since by default, RSTP is allowed on bridges to prevent L2 loops from forming up in case of cabling mistakes, the port does not forward traffic for some seconds after you "connect the cable", waiting for eventual RSTP BPDUs to arrive. During that time, the associated wireless station cannot obtain a DHCP lease as its DHCPDISCOVER packets get nowhere. If the Emporia Vue implementation is "impatient", it may give up and start from scratch before the RSTP switches the bridge port to "forwarding" state, so the cycle keeps going on like this.There is no upper limit to the level of power and flexibility of ROS. Similarly, there is no limit to the scope of your understanding of it.I enabled "edge=yes" on wifi2ghz:
```
[admin@355wap-carport]/interface/bridge/port>printdetailwhereedge=yesFlags:X-disabled,I-inactive;D-dynamic;H-hw-offload6Iinterface=wifi2ghz bridge=bridge priority=0x80edge=yes point-to-point=autolearn=autohorizon=noneauto-isolate=norestricted-role=norestricted-tcn=nopvid=1frame-types=admit-all ingress-filtering=yes 
       unknown-unicast-flood=yes unknown-multicast-flood=yes broadcast-flood=yes 
       tag-stacking=nobpdu-guard=notrusted=nomvrp-registrar-state=normal 
       mvrp-applicant-state=normal-participant multicast-router=temporary-query 
       fast-leave=no[admin@355wap-carportThere is another level of complexity to the environment:  This wAP is in the same campus as a nine Ubiquity Unify APs, with some overlap of covered areas.  And, the APs don't play terribly nicely with each other with respect to roaming.  So, the client in question has been connected to a different AP (for now).I disabled the AP that the device was connected to, and it (as expected) attempted to connect to the wAP.  Unfortunately, it exhibits the same failing behaviour:Screenshot 2024-11-18 121145.pngInterestingly, I had another device connect to wifi2ghz and it connects and stays connected just fine:Screenshot 2024-11-18 122343.pngFurther evidence of an "incompatibility" between the Emporia Vue and the wAP?  Or, something else specific about my environment or config?Thank you as always for the help and education.

---
```

## Response 5
There is no upper limit to the level of power and flexibility of ROS. Similarly, there is no limit to the scope of your understanding of it.Yes indeed @Sindy is really very good at this.I do have a similar problem, with a "cheap GL.inet SFT1200 "/"OPAL" , which runs OpenWRT 18.x , and many people see the same problem.SFT1200 is a device with a switch and multiple interfaces.. so setting the wAP bridge port for wifi to "edge" might not be very wise.Well the connection is with SFT1200 on 'router/WISP' so the MT actually only sees one device.2.4GHz is unusable as it continously disconnects. 5GHz has calm periods and disconnect intensive periods.LOG on SFT sometimes says ... "received beacon claiming channel 0... we lost connection."Slowing down basic rates to 6Mbps , and avoiding VHT basic rate etc, improved stability a bit, but it is not solved.Other clients do not disconnect that often. (Maybe they don't disconnect on a bogus beacon, or they digest the beacon correctly)Keeping WLAN interface running when no connection, to be tested.Just as reference (SFT log)
```
SunNov310:19:582024daemon.info lua:(...pkg-mips_siflower/gl-sdk4-repeater/usr/sbin/repeater:548)<3>CTRL-EVENT-DISCONNECTED bssid=***edited***reason=1locally_generated=1SunNov310:19:582024kern.warn kernel:[317172.048909]lmac[1]vif working channel(36)isdifferentfromchannel(0)ofreceived beacon frame,notify that we are lost!SunNov310:19:582024kern.warn kernel:[317172.060313]lmac[1]{CTXT-0}unlinkfrom{VIF-1}:status=4nb_vif=2The 2.4GHz disconnects are for every AP brand, not only MT.

---
```

## Response 6
I do have a similar problem, with a "cheap GL.inet SFT1200 "/"OPAL" , which runs OpenWRT 18.x , and many people see the same problem.SFT1200 is a device with a switch and multiple interfaces.. so setting the wAP bridge port for wifi to "edge" might not be very wise.Well the connection is with SFT1200 on 'router/WISP' so the MT actually only sees one device.2.4GHz is unusable as it continously disconnects. 5GHz has calm periods and disconnect intensive periods.LOG on SFT sometimes says ... "received beacon claiming channel 0... we lost connection."Slowing down basic rates to 6Mbps , and avoiding VHT basic rate etc, improved stability a bit, but it is not solved.Other clients do not disconnect that often. (Maybe they don't disconnect on a bogus beacon, or they digest the beacon correctly)Keeping WLAN interface running when no connection, to be tested.The 2.4GHz disconnects are for every AP brand, not only MT.Is the SFT1200 connecting to the wAP wirelessly, and then repeatedly disconnecting and connecting?Or, does the SFT1200 exhibit the same disconnect problems with its clients as the wAP does?Any theories as to why 2.4ghz differently problematic than 5ghz? I imagine a knee-jerk response might be that 2.4 is typically far more congested (with RF signals). I don't think that would explain it in my case because the wAP's 2.4ghz scan (I think) does not show 'a lot' of signals..Screenshot 2024-11-19 054130.png ---

## Response 7
Is the SFT1200 connecting to the wAP wirelessly, and then repeatedly disconnecting and connecting?The SFT has the wAP (or any other MT AP) as uplink connection. The mode is called "repeater" in OpenWRT but the function is set as "router" or "WISP" not a bridged repeater.Sending the downlink wifi on the other band on the SFT does not affect the disconnects.No client problems for connections to the SFT.Crowded, well yes, the MT scan shows 30 AP/SSID in 2.4GHz and the same number in 5 GHz band. ---

## Response 8
Is it a SFT only problem? Maybe.But "emporia vue" has a lot of disconnect reports with Home Assistant and ESPhome also.For the SFT1200, problems are reported with Mikrotik as uplink/https://forum.gl-inet.com/t/gl-sft1200- ... k/25997/21The 2.4GHz is very very unstable. My tuning/setting here is setting the WLAN band on the MT to "2 GHz-only-G" , probably totally disabling A-MSDU aggregation. It is even better than 5 GHz uplink with this setting. (What cannot be repeated there at 5 GHz ac) ---

## Response 9
I have a hap ac2(AP mode) with wifi-qcom-ac connected wirelessly(2.4gHz) to another hap ac2(station bridge mode) every several days it goes through a period of connection disconnection cycle (up to 15 minutes) for no apparent reason signal is between -70 and -74, reason code 1 is given on station bridge side. STP set to None all the way thorough nothing in between.Topology as followingRB5009 (NAT Router) Ethernet -----> hap ac2(AP Mode 2.4gHz) ------->hap ac2(Station Bridge Mode)stn bridge.png ---

## Response 10
I have a hap ac2(AP mode) with wifi-qcom-ac connected wirelessly(2.4gHz) to another hap ac2(station bridge mode) every several days it goes through a period of connection disconnection cycle (up to 15 minutes) for no apparent reason signal is between -70 and -74, reason code 1 is given on station bridge side. STP set to None all the way thorough nothing in between.You could start a new topic, as your problem is probably not related. Interference might be your problem, especially because you use the complete bandwidth of wifi at 2.4GHz. ---

## Response 11
... especially because you use the complete bandwidth of wifi at 2.4GHz.Half (give or take) actually. 2.4GHz band (for anything newer than 802.11B) is 70MHz wide (in NA and related parts of universe) or 80MHz wide (elsewhere) ... and 2462/n/eC channel is 40MHz wide. ---

## Response 12
You could start a new topic, as your problem is probably not related.I think this is very similar to original posters issue, even reason code is 1, Only difference I can see is my network stack is entirely mikrotik, I don't think the issue is interference, also tried 20mHz same issue happens... ---

## Response 13
Half (give or take) actually. 2.4GHz band (for anything newer than 802.11B) is 70MHz wide (in NA and related parts of universe) or 80MHz wide (elsewhere) ... and 2462/n/eC channel is 40MHz wide.Yeah yeah, I know. There is more bandwidth. Let me try it in a different way:Frequency 2462, Control channel eC and channelwidth 40MHz makes use of frequencies from (roughly) 2432 to 2482 which doesn't overlap with channels 1/2/3/4/5 (2402 to 2447). The chance you run into interference is high.I think this is very similar to original posters issue, even reason code is 1, Only difference I can see is my network stack is entirely mikrotik, I don't think the issue is interference, also tried 20mHz same issue happens...AFAIK reason code 1 is undefined. Could be anything. Are you using auto channels? Did you have the exact same issues while using 20MHz?Can you share the config of bot hAP's? ---

## Response 14
Are you using auto channels? Did you have the exact same issues while using 20MHz?Can you share the config of bot hAP's?Yes auto channels, exact same issues while using 20MHz...here is the WiFi config:AP# model = RBD52G-5HacD2HnD/interface wifiset [ find default-name=wifi1 ] arp-timeout=auto channel.band=2ghz-n .width=\20/40mhz configuration.hide-ssid=yes .mode=ap .ssid=*** \disabled=no l2mtu=1560 mac-address=74:4D:28:5E:32:70 mtu=1500 name=wifi1 \radio-mac=74:4D:28:5E:32:70 security.authentication-types=wpa2-psk \.encryption=ccmp .management-protection=disabled .wps=disableStation Bridge# model = RBD52G-5HacD2HnD/interface wifiset [ find default-name=wifi1 ] arp-timeout=auto configuration.hide-ssid=no \.mode=station-bridge .ssid=*** disabled=no l2mtu=1560 \mac-address=74:4D:28:5E:46:86 name=wifi1 radio-mac=74:4D:28:5E:46:86 \security.authentication-types=wpa2-psk .encryption=ccmp ---