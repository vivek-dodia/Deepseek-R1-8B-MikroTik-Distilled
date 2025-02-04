# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207510

# Discussion

## Initial Question
Author: Fri May 10, 2024 3:37 pm
``` 
```
13:18:33 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 13:18:33 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 13:18:37 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 13:18:37 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 13:18:40 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 13:18:40 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 13:18:52 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 - here i switched wifi off on the device - 
 13:59:47 wireless,info 70:31:7F:DE:D9:E2@Wifi-AP1 disconnected, connection lost, signal strength -66
 13:59:47 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP1 disassociated, connection lost, signal strength -66
 13:59:55 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP1 associated, signal strength -62
 13:59:55 wireless,info 70:31:7F:DE:D9:E2@Wifi-AP1 connected, signal strength -62
```

```
```

```
[h1ghrise@Baranowice] /interface/wifi/configuration> pr
Flags: X - disabled 
 0   name="CONFIG_WIFI" ssid="Wifi" country=Austria 
     security.authentication-types=wpa2-psk,wpa3-psk .passphrase="[REDACTED]" .ft=yes .ft-over-ds=yes .connect-priority=0/1 
     datapath=DP_AC 
     datapath.bridge=BR-MAIN 
     channel.band=5ghz-ac .width=20/40/80mhz .skip-dfs-channels=all 

 1   name="CONFIG_IOT" ssid="IoT" country=Austria 
     security.authentication-types=wpa-psk,wpa2-psk .passphrase="[REDACTED]" .wps=disable .ft=yes .ft-over-ds=yes 
     datapath=DP_AC 
     datapath.bridge=BR-MAIN 
     channel.frequency=2412,2437,2462 .band=2ghz-g .width=20mhz .skip-dfs-channels=all
```

Hi Mikrotik Community,I have switched to new CAPsMAN a couple of weeks ago. My IoT Devices are (mostly) happy, and overall reception is way better than before.Im running an RB5009 and 2 CAp ACs (running qcom-ac driver), all on 7.14.3, with 2 SSIDs. one purely on 2.4Ghz for IOT, and another one purely for 5Ghz.My Iphone 14 Pro, the iPhone 13 from my Wife, my Macbook Pro all expiriencing "weird" Roaming behavior:(70:31:xx:xx is my iPhone), behavior is identical for other devices.I have to turn of wifi, to have the device use the next AP.Config:


---
```

## Response 1
Author: Fri May 10, 2024 3:40 pm
I reduced txpower of my APs in capsman2 and now they are roaming much better! ---

## Response 2
Author: Fri May 10, 2024 3:46 pm
I was doing this in capsman v1 as well, but heard that this is not necessary anymore. Can't find the thread, but bottom line was, not to mess with radio power distribution/settings.Can you kindly share how and where you reduced txpower? Its highly dynamic as it depends on location of aps, walls, etc. ---

## Response 3
Author: Fri May 10, 2024 4:02 pm
13:59:47 wireless, info 70:31:7F:DE:D9:E2@Wifi-AP1 disconnected, connection lost, signal strength -6613:59:47 wireless, debug 70:31:7F:DE:D9:E2@Wifi-AP1 disassociated, connection lost, signal strength -6613:59:55 wireless, debug 70:31:7F:DE:D9:E2@Wifi-AP1 associated, signal strength -6213:59:55 wireless, info 70:31:7F:DE:D9:E2@Wifi-AP1 connected, signal strength -62The issue might be that device sees signal strength from both APs quite strong and almost the same (-66dB vs. -62dB is not much of a difference). Even with mobility enhancements (802.11 r/k/v) it's still up to station to decide when to roam, the enhancements just give station additional information which helps it to decide and makes the reconnection process faster.If it bothers you that device is not connected to the strongest AP and it's the are where your device stays a lot of time, then you have to make larger difference in signal strengths of both APs. E.g. reduce power of AP which already provides the slightly lower signal strength (probably by some 10 dB). Or move one of APs so that signal strength at this particular spot drops considerably. ---

## Response 4
Author: Fri May 10, 2024 4:29 pm
I ran into problems when using combined WPA2-PSK and WPA3-PSK, only on Apple devices.In addition, I set DTIM to 3 (which is advised by Apple) and set group encryption explicitly to CCMP.And, at last, I lowered 2.4GHz Tx power as well. ---

## Response 5
Author: Fri May 10, 2024 4:44 pm
How to lower txpower efficiently? when using txpower in wireless configuration, it is mentioned it is unset per default. Value is an int between 0 and 40. So 30 would be a reduction by 10 dbm? ---

## Response 6
Author: Fri May 10, 2024 4:52 pm
It is the actual Tx Power used by the radio (antenna gain is not part of the setting).Mine is set to 5 dBm, which is sufficient for my environment. Think the neighbors appreciate it as well! ---

## Response 7
Author: Fri May 10, 2024 5:01 pm
``` 
```
16:39:17 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 16:39:17 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
 16:39:18 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 reauthenticating
```

```
```

```
Macbook (moving to AP2)
 16:46:48 wireless,debug F8:4D:89:92:04:06@Wifi-AP2 associated, signal strength -77
 16:46:48 wireless,info F8:4D:89:92:04:06@Wifi-AP1 roamed to F8:4D:89:92:04:06@Wifi-AP2, signal strength -77
 16:46:48 wireless,debug F8:4D:89:92:04:06@Wifi-AP1 disassociated, connected to other interface, signal strength -83
Macbook (moving to AP1)
 16:47:42 wireless,debug F8:4D:89:92:04:06@Wifi-AP1 associated, signal strength -65
 16:47:42 wireless,info F8:4D:89:92:04:06@Wifi-AP2 roamed to F8:4D:89:92:04:06@Wifi-AP1, signal strength -65
 16:47:42 wireless,debug F8:4D:89:92:04:06@Wifi-AP2 disassociated, connected to other interface, signal strength -82
```

In Capsman V1, I did it exactly like that. Put the txpower with a fixed value (10 in my case).Now there are different approaches.txpower = radio transmit power - gainSo, if I raise the gain, I reduce the TX power ?As both values are unset, raising the gain would efficiently lower the txpower by this amount?Edit: I set the antenna gain to 10, and walked around the flat to see if it made any difference. As soon as i left the range from AP1, where the phone was connected to, and approached the second AP, i noticed that the signal level indicator in the phone was "flapping" (hard to describe, signal quality jumped between 1 bar and 4 bars). In the Router logs:I moved back, log went silent.Edit2: Removed gain and changed the txpower value directly to 7. Now Roaming seems to work fine:


---
```

## Response 8
Author: Sat May 11, 2024 3:12 pm
``` 
```
13:56:10 wireless,info 04:99:BB:57:C5:3F@Wifi-AP1 disconnected, connection lost, signal strength -87
 13:56:15 wireless,info 04:99:BB:57:C5:3F@Wifi-AP2 connected, signal strength -62
```

Ok maybe i was a bit too enthusiastic.I setup the 5Ghz main Wifi on all (Apple) Devices, which connect to it, again. forgot the network, setup password again and it seem to work, but now i saw this:Devices start to experience issues again, despite the clear distinction in signal levels and setup FT/roaming opportunity.Is there anything else I may check?


---
```

## Response 9
Author: Sat May 11, 2024 3:20 pm
``` 
```
/export file=anynameyoulike
```

I would expect some debug logging? Did you disable that?Can you share the complete config?Remove serial and any other private info.


---
```

## Response 10
Author: Sat May 11, 2024 9:47 pm
``` 
```
# 2024-05-11 20:33:04 by RouterOS 7.14.3
# software id = [REDACTED]
#
# model = RB5009UPr+S+
# serial number = [REDACTED]
/container mounts
add dst=/opt/adguardhome/conf name=adguard_conf src=\
    /usb1-part1/docker/conf/adguard
add dst=/config name=homeassistant src=\
    /usb1-part1/container/mounts/homeassistant/config
add dst=/mosquitto/config name=mqtt src=/usb1-part1/docker/mqtt/config
/disk
add parent=usb1 partition-number=1 partition-offset=512 partition-size=\
    "500 107 861 504" type=partition
/interface bridge
add admin-mac=[REDACTED] auto-mac=no name=BR-MAIN port-cost-mode=short \
    protocol-mode=none vlan-filtering=yes
/interface ethernet
set [ find default-name=ether1 ] name="ether1 - WAN" poe-out=off
set [ find default-name=ether2 ] disabled=yes name="ether2 - Lab" poe-out=off
set [ find default-name=ether3 ] disabled=yes poe-out=off
set [ find default-name=ether4 ] disabled=yes poe-out=off
set [ find default-name=ether5 ] disabled=yes poe-out=off
set [ find default-name=ether6 ] name="ether6 - Zigbee"
set [ find default-name=ether7 ] name="ether7 - AP1"
set [ find default-name=ether8 ] name="ether8 - AP2"
set [ find default-name=sfp-sfpplus1 ] disabled=yes
/interface wireguard
add listen-port=31337 mtu=1420 name=VPN
/interface veth
add address=10.10.50.2/24 gateway=10.10.50.1 gateway6="" name=\
    "veth1 - AdGuard"
add address=10.10.20.2/24 gateway=10.10.20.1 gateway6="" name=\
    "veth2 - Homeassistant"
add address=10.10.20.6/24 gateway=10.10.20.1 gateway6="" name="veth3 - MQTT"
/interface vlan
add interface=BR-MAIN name="VLAN10 - Wifi" vlan-id=10
add interface=BR-MAIN name="VLAN20 - IoT" vlan-id=20
add interface=BR-MAIN name="VLAN50 - LAN" vlan-id=50
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wifi datapath
add bridge=BR-MAIN disabled=no name=DP_AC
/interface wifi configuration
add channel.band=5ghz-ac .skip-dfs-channels=all .width=20/40/80mhz country=\
    Austria datapath=DP_AC datapath.bridge=BR-MAIN disabled=no name=\
    CONFIG_WIFI security.authentication-types=wpa2-psk,wpa3-psk .ft=yes \
    .ft-over-ds=yes ssid=Wifi tx-power=5
add channel.band=2ghz-g .frequency=2412,2437,2462 .skip-dfs-channels=all \
    .width=20mhz country=Austria datapath=DP_AC datapath.bridge=BR-MAIN \
    disabled=no name=CONFIG_IOT security.authentication-types=\
    wpa-psk,wpa2-psk .ft=yes .ft-over-ds=yes .wps=disable ssid=IoT tx-power=5
/ip pool
add name=POOL_LAN ranges=10.10.50.2-10.10.50.254
add name=POOL_IOT ranges=10.10.20.2-10.10.20.254
add name=POOL_WIFI ranges=10.10.10.2-10.10.10.254
/ip dhcp-server
add address-pool=POOL_IOT interface="VLAN20 - IoT" lease-time=4w2d name=\
    DHCP-IOT
add address-pool=POOL_WIFI interface="VLAN10 - Wifi" lease-time=1w3d name=\
    DHCP-WIFI
add address-pool=POOL_LAN interface="VLAN50 - LAN" lease-time=14w2d name=\
    DHCP-LAN

/container
add hostname=SRV-AdGuard interface="veth1 - AdGuard" root-dir=\
    usb1-part1/docker/adguard start-on-boot=yes workdir=/opt/adguardhome/work
add interface="veth3 - MQTT" mounts=mqtt root-dir=usb1-part1/docker/mqtt/ \
    start-on-boot=yes
add comment=HomeAssistant envlist=ha_env interface="veth2 - Homeassistant" \
    mounts=homeassistant root-dir=usb1-part1/docker/ha start-on-boot=yes \
    workdir=/config
/container config
set registry-url=https://registry-1.docker.io tmpdir=usb1-part1/docker
/container envs
add key=TZ name=ha_env value=Europe/Vienna

/interface bridge port
add bridge=BR-MAIN comment="AP1" frame-types=\
    admit-only-vlan-tagged interface="ether7 - AP1" internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN comment="AP2" frame-types=\
    admit-only-vlan-tagged interface="ether8 - AP2" internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN frame-types=admit-only-untagged-and-priority-tagged \
    interface="veth1 - AdGuard" internal-path-cost=10 path-cost=10 pvid=50
add bridge=BR-MAIN interface="ether6 - Zigbee" internal-path-cost=10 \
    path-cost=10 pvid=20
add bridge=BR-MAIN frame-types=admit-only-untagged-and-priority-tagged \
    interface="veth3 - MQTT" internal-path-cost=10 path-cost=10 pvid=20
add bridge=BR-MAIN frame-types=admit-only-untagged-and-priority-tagged \
    interface="veth2 - Homeassistant" pvid=20
add bridge=BR-MAIN frame-types=admit-only-vlan-tagged interface=\
    "ether2 - Lab"
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/ipv6 settings
set accept-redirects=no accept-router-advertisements=no disable-ipv6=yes \
    forward=no
/interface bridge vlan
add bridge=BR-MAIN comment=Wifi tagged="BR-MAIN,ether7 - AP1,ether8 - AP2" \
    vlan-ids=10
add bridge=BR-MAIN comment=IoT tagged="BR-MAIN,ether7 - AP1,ether8 - AP2" \
    untagged="veth2 - Homeassistant" vlan-ids=20
add bridge=BR-MAIN comment=LAN tagged=\
    "BR-MAIN,ether7 - AP1,ether8 - AP2,ether2 - Lab" vlan-ids=50
/interface list member
add interface="ether1 - WAN" list=WAN
add interface=VPN list=LAN
add interface="VLAN10 - Wifi" list=LAN
add interface="VLAN20 - IoT" list=LAN
add interface="VLAN50 - LAN" list=LAN
/interface wifi capsman
set ca-certificate=[REDACTED] certificate=[REDACTED] \
    enabled=yes interfaces="VLAN50 - LAN" package-path="" \
    require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=\
    CONFIG_WIFI name-format=Wifi-%I supported-bands=5ghz-ac
add action=create-dynamic-enabled disabled=no master-configuration=CONFIG_IOT \
    name-format=IoT-%I supported-bands=2ghz-g
/interface wireguard peers
add allowed-address=10.10.99.2/32 comment="iPhone Ben" interface=VPN \
    public-key="[REDACTED]"
add allowed-address=10.10.99.3/32 comment="Macbook Ben" interface=VPN \
    public-key="[REDACTED]"
/ip address
add address=10.10.99.1/24 comment=Wireguard interface=VPN network=10.10.99.0
add address=10.10.50.1/24 interface="VLAN50 - LAN" network=10.10.50.0
add address=10.10.10.1/24 interface="VLAN10 - Wifi" network=10.10.10.0
add address=10.10.20.1/24 interface="VLAN20 - IoT" network=10.10.20.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add comment=defconf interface="ether1 - WAN"

/ip dhcp-server network
add address=10.10.10.0/24 gateway=10.10.10.1
add address=10.10.20.0/24 gateway=10.10.20.1
add address=10.10.50.0/24 dns-server=10.10.50.1 gateway=10.10.50.1
add address=10.13.37.0/24 gateway=10.13.37.1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan
/ip firewall address-list
add address=10.10.10.0/24 list=Management
add address=10.10.20.0/24 list=Management
add address=10.10.99.0/24 list=Management
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=accept chain=input comment="Allow Router Management" dst-port=\
    8291,22,445,139 log-prefix=ACCESS: protocol=tcp src-address-list=\
    Management
add action=accept chain=input comment="Allow Wireguard" dst-port=31337 \
    protocol=udp
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www address=10.10.10.0/24,10.10.20.0/24,10.10.50.0/24,10.10.99.0/24
set ssh address=10.10.10.0/24,10.10.20.0/24,10.10.99.0/24
set api address=10.10.20.2/32
set winbox address=10.10.10.0/24,10.10.50.0/24,10.10.99.0/24
set api-ssl address=10.10.20.2/32 disabled=yes
/ip ssh
set strong-crypto=yes

/system clock
set time-zone-name=Europe/Vienna

/system logging
set 0 topics=info,!wireguard
add topics=debug,wireless
/system note
set show-at-login=no
/system script
add dont-require-permissions=yes name="Update HomeAssistant" owner=h1ghrise \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source=":local contComment \"HomeAssistant\"\r\
    \n:local logPrefix \"Container update: \"\r\
    \n\r\
    \n\r\
    \n:local abortWithMessage do={\r\
    \n  :log error \"\$(\$logPrefix)Error - \$1\"\r\
    \n  :error \$1\r\
    \n}\r\
    \n\r\
    \n/container\r\
    \n\r\
    \n:local contId [find where comment=\$contComment]\r\
    \n:if (\$contId = \"\") do={ \$abortWithMessage (\"container \$contComment\
    \_not found, aborting\") logPrefix=\$logPrefix }\r\
    \n\r\
    \n:local contStatus ([get \$contId]->\"status\")\r\
    \n:if (\$contStatus = \"extracting\") do={ \$abortWithMessage (\"container\
    \_\$contComment is extracting, aborting\") logPrefix=\$logPrefix }\r\
    \n\r\
    \n:log info \"\$(\$logPrefix)Container \$contComment update started\"\r\
    \n:local contStarted false\r\
    \n\r\
    \n:if (\$contStatus != \"stopped\") do={\r\
    \n  :if (\$contStatus = \"running\") do={\r\
    \n    :log warn \"\$(\$logPrefix)Container \$contComment is running, stopp\
    ing container\"\r\
    \n    :set contStarted true\r\
    \n    stop \$contId\r\
    \n  }\r\
    \n\r\
    \n  :local stopTimeoutSec 120\r\
    \n  :local sec 0\r\
    \n\r\
    \n  :while (([get \$contId]->\"status\") != \"stopped\" && \$sec <= \$stop\
    TimeoutSec) do={\r\
    \n    :delay 1\r\
    \n    :set sec (\$sec + 1)\r\
    \n  }\r\
    \n\r\
    \n  :if (\$sec > \$stopTimeoutSec) do={ \$abortWithMessage (\"container \$\
    contComment stop timed out, aborting\") logPrefix=\$logPrefix }\r\
    \n  :log info \"\$(\$logPrefix)Container \$contComment stopped\"\r\
    \n}\r\
    \n\r\
    \n:local cont [get \$contId]\r\
    \nremove \$contId\r\
    \n:delay 5\r\
    \n\r\
    \n\r\
    \n# after ROS upgrade check below if something has changed\r\
    \n# ------------------------------------------------------\r\
    \n# validAddArgs - array of container add command argument names which are\
    \_named exact as config property names\r\
    \n:local validAddArgs ( \"cmd\", \"comment\", \"dns\", \"domain-name\", \"\
    entrypoint\", \"envlist\", \"hostname\", \"interface\", \"logging\", \"mou\
    nts\", \"root-dir\", \"start-on-boot\", \"workdir\" )\r\
    \n# replaceArgs - key-value array for mapping container add command argume\
    nt name from different config property name, where key is config property \
    name and value is argument name\r\
    \n:local replaceArgs { \"tag\"=\"remote-image\" }\r\
    \n# addCmd - ROS CLI container add command\r\
    \n:local addCmd \"/container add\"\r\
    \n# -----------------------------------------------------\r\
    \n\r\
    \n\r\
    \n:local escapeStr do={\r\
    \n  :local strLen [:len \$1]\r\
    \n  :local escStr \"\"\r\
    \n\r\
    \n  :for i from=0 to=(\$strLen - 1) do={\r\
    \n    :local chr [:pick \$1 \$i (\$i + 1)]\r\
    \n\r\
    \n    :if (\$chr = \"\\\$\") do={ :set escStr \"\$escStr\\\\\\\$\" } else=\
    {\r\
    \n      :if (\$chr = \"\\\\\") do={ :set escStr \"\$escStr\\\\\\\\\" } els\
    e={\r\
    \n        :if (\$chr = \"\\\"\") do={ :set escStr \"\$escStr\\\\\\\"\" } e\
    lse={\r\
    \n          :set escStr \"\$escStr\$chr\"\r\
    \n        }\r\
    \n      }\r\
    \n    }\r\
    \n  }\r\
    \n\r\
    \n  :return \"\\\"\$escStr\\\"\"\r\
    \n}\r\
    \n\r\
    \n:local arrayToStr do={\r\
    \n  :local arrLen [:len \$1]\r\
    \n  :local strArr \"(\"\r\
    \n\r\
    \n  :for i from=0 to=(\$arrLen - 1) do={\r\
    \n    :local item [:pick \$1 \$i]\r\
    \n\r\
    \n    :if ([:len \$strArr] > 1) do={ :set \$strArr \"\$strArr,\" }\r\
    \n    :if ([:typeof \$item] = \"str\") do={\r\
    \n      :set \$strArr \"\$strArr\$([\$escapeStr \$item])\"\r\
    \n    } else={\r\
    \n      :set \$strArr \"\$strArr\$item\"\r\
    \n    }\r\
    \n  }\r\
    \n\r\
    \n  :return \"\$strArr)\"\r\
    \n}\r\
    \n\r\
    \n:local escapeValue do={\r\
    \n  :if ([:typeof \$1] = \"str\") do={ :return [\$escapeStr \$1] }\r\
    \n  :if ([:typeof \$1] = \"array\") do={ :return [\$arrayToStr \$1 escapeS\
    tr=\$escapeStr] }\r\
    \n  :if ([:typeof \$1] = \"bool\") do={:if (\$1) do={ :return \"yes\" } el\
    se={ :return \"no\" }}\r\
    \n  :return \$1\r\
    \n}\r\
    \n\r\
    \n:foreach k,v in=\$cont do={\r\
    \n  :if ([:len \$v] != 0) do={\r\
    \n    :if ([:find \$validAddArgs \$k] >= 0) do={\r\
    \n      :set addCmd \"\$addCmd \$k=\$([\$escapeValue \$v escapeStr=\$escap\
    eStr arrayToStr=\$arrayToStr])\"\r\
    \n    } else={\r\
    \n      :local rk (\$replaceArgs->\"\$k\")\r\
    \n      :if ([:typeof \$rk] != \"nothing\") do={ :set addCmd \"\$addCmd \$\
    rk=\$([\$escapeValue \$v escapeStr=\$escapeStr arrayToStr=\$arrayToStr])\"\
    \_}\r\
    \n    }\r\
    \n  }\r\
    \n}\r\
    \n\r\
    \n:execute \"\$addCmd\" as-string\r\
    \n:set contId [find where comment=\$contComment]\r\
    \n:if (\$contId = \"\") do={ \$abortWithMessage (\"unable to add container\
    \_\$contComment, check add command: \$addCmd\") logPrefix=\$logPrefix }\r\
    \n\r\
    \n# rise if not enough (30min) on slow network or device\r\
    \n:local extrTimeoutSec 1800\r\
    \n:local sec 0\r\
    \n\r\
    \n:while (([get \$contId]->\"status\") = \"extracting\" && \$sec <= \$extr\
    TimeoutSec) do={\r\
    \n  :delay 1\r\
    \n  :set sec (\$sec + 1)\r\
    \n}\r\
    \n\r\
    \n:if (\$sec > \$extrTimeoutSec) do={ \$abortWithMessage (\"container \$co\
    ntComment extract wait timed out, something is failed or slower than expec\
    ted\") logPrefix=\$logPrefix }\r\
    \n:if (\$contStarted) do={ start \$contId }\r\
    \n:log info \"\$(\$logPrefix)Container \$contComment update finished\""
/tool bandwidth-server
set enabled=no
/tool graphing interface
add interface="ether1 - WAN"
add interface="VLAN10 - Wifi"
add interface="VLAN20 - IoT"
add interface="VLAN50 - LAN"
/tool graphing resource
add allow-address=10.10.10.130/32 store-on-disk=no
/tool mac-server
set allowed-interface-list=none
/tool mac-server mac-winbox
set allowed-interface-list=none
/tool mac-server ping
set enabled=no
/tool romon
set enabled=yes
```

Hi,yes - I had wireless debug disabled after roaming was working fine.My config looks like this:


---
```

## Response 11
Author: Mon May 13, 2024 11:02 am
Apple recommends using the same SSID across all bands on your wifi network. Not doing so can cause compatibility issues(according to Apple).Have you tried using the same SSID for both bands ? ---

## Response 12
Author: Mon May 13, 2024 3:38 pm
Only the 5Ghz WIFI SSID is used for the Apple Devices. IoT on 2.4 Ghz is not known to themFrequency is handled by CapsMan and not restricted. So, I should restrict the used frequency on both APs, and set it manually to the same one? ---

## Response 13
Author: Thu Oct 31, 2024 9:51 pm
``` 
```
20:08:41 wireless,info 70:31:7F:DE:D9:E2@Wifi-AP1 disconnected, connection lost, signal strength -88
20:08:41 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP1 disassociated, connection lost, signal strength -88
```

```
```

```
20:08:43 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 associated, signal strength -55
20:08:43 wireless,info 70:31:7F:DE:D9:E2@Wifi-AP2 connected, signal strength -55
```

```
```

```
20:09:38 wireless,info 70:31:7F:DE:D9:E2@Wifi-AP2 disconnected, connection lost, signal strength -81
20:09:38 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP2 disassociated, connection lost, signal strength -81
```

```
```

```
20:12:08 wireless,debug 70:31:7F:DE:D9:E2@Wifi-AP1 associated, signal strength -68
20:12:08 wireless,info 70:31:7F:DE:D9:E2@Wifi-AP1 connected, signal strength -68
```

```
```

```
/interface bridge
add admin-mac=D4:01:C3:B8:8B:7D auto-mac=no name=BR-MAIN protocol-mode=none
/interface ethernet
set [ find default-name=ether1 ] name="ether1 - WAN" poe-out=off
set [ find default-name=ether2 ] name="ether2 - AP1"
set [ find default-name=ether3 ] name="ether3 - AP2"
set [ find default-name=sfp-sfpplus1 ] disabled=yes
/interface vlan
add interface=BR-MAIN name=VLAN10_WIFI vlan-id=10
add interface=BR-MAIN name=VLAN20_IOT vlan-id=20
add interface=BR-MAIN name=VLAN50_MGMT vlan-id=50
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wifi datapath
add bridge=BR-MAIN disabled=no name=DP_WIFI vlan-id=10
add bridge=BR-MAIN disabled=no name=DP_IOT vlan-id=20
/interface wifi security
add authentication-types=wpa2-psk disabled=no ft=yes ft-over-ds=yes name=\
    SEC_WIFI
add authentication-types=wpa2-psk disabled=no ft=no ft-over-ds=no name=\
    SEC_IOT wps=disable
/interface wifi configuration
add channel.band=5ghz-ax .skip-dfs-channels=all .width=20/40mhz country=\
    Austria datapath=DP_WIFI disabled=no name=CFG_WIFI security=SEC_WIFI \
    ssid=Owcahome
add channel.band=2ghz-g .frequency=2412,2437,2462 .skip-dfs-channels=all \
    .width=20mhz country=Austria datapath=DP_IOT disabled=no name=CFG_IOT \
    security=SEC_IOT ssid=IoT
/ip pool
add name=POOL_WIFI ranges=10.10.10.2-10.10.10.254
add name=POOL_MGMT ranges=10.10.50.2-10.10.50.254
add name=POOL_IOT ranges=10.10.20.2-10.10.20.254
/ip dhcp-server
add address-pool=POOL_WIFI interface=VLAN10_WIFI lease-time=1d name=DHCP_WIFI
add address-pool=POOL_MGMT interface=VLAN50_MGMT lease-time=1h name=DHCP_MGMT
add address-pool=POOL_IOT interface=VLAN20_IOT name=DHCP_IOT
/interface bridge port
add bridge=BR-MAIN interface="ether2 - AP1"
add bridge=BR-MAIN interface="ether3 - AP2"
/interface bridge vlan
add bridge=BR-MAIN tagged="BR-MAIN,ether2 - AP1,ether3 - AP2" vlan-ids=50
add bridge=BR-MAIN tagged="BR-MAIN,ether2 - AP1,ether3 - AP2" vlan-ids=20
add bridge=BR-MAIN tagged="BR-MAIN,ether2 - AP1,ether3 - AP2" vlan-ids=10
/interface list member
add interface=VLAN10_WIFI list=LAN
add interface=VLAN20_IOT list=LAN
add interface=VLAN50_MGMT list=LAN
add interface="ether1 - WAN" list=WAN

/interface wifi capsman
set ca-certificate=auto certificate=auto enabled=yes interfaces=VLAN50_MGMT \
    package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled disabled=no master-configuration=CFG_WIFI \
    name-format=Wifi-%I slave-configurations="" supported-bands=5ghz-ax
add action=create-dynamic-enabled disabled=no master-configuration=CFG_IOT \
    name-format=IoT-%I slave-configurations="" supported-bands=2ghz-g
/ip address
add address=10.10.10.1/24 interface=VLAN10_WIFI network=10.10.10.0
add address=10.10.20.1/24 interface=VLAN20_IOT network=10.10.20.0
add address=10.10.50.1/24 interface=VLAN50_MGMT network=10.10.50.0

/ip dhcp-client
add comment=defconf interface="ether1 - WAN"
/ip dhcp-server network
add address=10.10.10.0/24 gateway=10.10.10.1
add address=10.10.20.0/24 gateway=10.10.20.1
add address=10.10.50.0/24 gateway=10.10.50.1
/ip dns
set allow-remote-requests=yes mdns-repeat-ifaces=VLAN10_WIFI,VLAN20_IOT
/ip firewall address-list
add address=10.10.10.0/24 list=Wifi
add address=10.10.20.20 list=SONOS
add address=10.10.20.21 list=SONOS
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
add action=accept chain=forward comment="Sonos to Controller" \
    dst-address-list=SONOS dst-port=1400 protocol=tcp src-address-list=Wifi
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5

/system clock
set time-zone-name=Europe/Vienna
/system logging
add topics=wireless,debug
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool romon
set enabled=yes
```

```
```

```
/interface bridge
add admin-mac=D4:01:C3:FA:36:68 auto-mac=no comment=defconf name=BR-MAIN \
    port-cost-mode=short protocol-mode=none
/interface ethernet
set [ find default-name=ether1 ] name="ether1 - Router"
set [ find default-name=ether2 ] poe-out=off
/interface vlan
add interface=BR-MAIN name=VLAN50_MGMT vlan-id=50
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wifi datapath
add bridge=BR-MAIN disabled=no name=DP_MAIN

/interface bridge port
add bridge=BR-MAIN comment=defconf interface=ether2 internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN comment=defconf interface=wifi1 internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN comment=defconf interface=wifi2 internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN interface="ether1 - Router"
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface bridge vlan
add bridge=BR-MAIN tagged="BR-MAIN,ether1 - Router" vlan-ids=50
/interface list member
add comment=defconf interface=BR-MAIN list=LAN
add interface=VLAN50_MGMT list=LAN
/interface wifi cap
set discovery-interfaces=VLAN50_MGMT enabled=yes slaves-datapath=DP_MAIN
/ip dhcp-client
add interface=VLAN50_MGMT
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" port=\
    33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/system clock
set time-zone-name=Europe/Vienna
/system identity
set name=AP1
/system note
set show-at-login=no
/system routerboard mode-button
set enabled=yes on-event=dark-mode
/system script
add comment=defconf dont-require-permissions=no name=dark-mode owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool romon
set enabled=yes
```

```
```

```
/interface bridge
add admin-mac=D4:01:C3:F8:B8:33 auto-mac=no comment=defconf name=BR-MAIN \
    port-cost-mode=short protocol-mode=none
/interface ethernet
set [ find default-name=ether1 ] name="ether1 - Router"
set [ find default-name=ether2 ] poe-out=off
/interface vlan
add interface=BR-MAIN name=VLAN50_MGMT vlan-id=50
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface wifi datapath
add bridge=BR-MAIN disabled=no name=DP_MAIN

/interface bridge port
add bridge=BR-MAIN comment=defconf interface=ether2 internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN comment=defconf interface=wifi1 internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN comment=defconf interface=wifi2 internal-path-cost=10 \
    path-cost=10
add bridge=BR-MAIN interface="ether1 - Router" internal-path-cost=10 \
    path-cost=10
/ip firewall connection tracking
set udp-timeout=10s
/ip neighbor discovery-settings
set discover-interface-list=LAN
/interface bridge vlan
add bridge=BR-MAIN tagged="ether1 - Router,BR-MAIN" vlan-ids=50
/interface list member
add comment=defconf interface=BR-MAIN list=LAN
add interface=VLAN50_MGMT list=LAN
/interface wifi cap
set discovery-interfaces=VLAN50_MGMT enabled=yes slaves-datapath=DP_MAIN
/ip dhcp-client
add comment=defconf interface=VLAN50_MGMT
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 comment=defconf name=router.lan type=A
/ip firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMP" protocol=icmp
add action=accept chain=input comment=\
    "defconf: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1
add action=drop chain=input comment="defconf: drop all not coming from LAN" \
    in-interface-list=!LAN
add action=accept chain=forward comment="defconf: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="defconf: accept out ipsec policy" \
    ipsec-policy=out,ipsec
add action=fasttrack-connection chain=forward comment="defconf: fasttrack" \
    connection-state=established,related hw-offload=yes
add action=accept chain=forward comment=\
    "defconf: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat \
    connection-state=new in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat comment="defconf: masquerade" \
    ipsec-policy=out,none out-interface-list=WAN
/ip ipsec profile
set [ find default=yes ] dpd-interval=2m dpd-maximum-failures=5
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" port=\
    33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/system clock
set time-zone-name=Europe/Vienna
/system identity
set name=AP2
/system note
set show-at-login=no
/system routerboard mode-button
set enabled=yes on-event=dark-mode
/system script
add comment=defconf dont-require-permissions=no name=dark-mode owner=*sys \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source="\r\
    \n   :if ([system leds settings get all-leds-off] = \"never\") do={\r\
    \n     /system leds settings set all-leds-off=immediate \r\
    \n   } else={\r\
    \n     /system leds settings set all-leds-off=never \r\
    \n   }\r\
    \n "
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
/tool romon
set enabled=yes
```

Hi,i want to ask again for help, since I am not able to figure out my mistake.I moved to a new apartment, and changed my cap ACs to cap AX APs. the RB5009 was also replaced with another one, so basically all brand new hardwareSetup is basically identical.- RB5009 as CapsMan- 3 VLANs (IOT, WIFI, MGMT)- 2 CAP AXAll devices run 7.16.1Apple devices initially connect to one of the APs, but do not roam. If they do, I get full reception on the device, but I cant do anything (no page loads, no app, etc.). It's like I'm not connected to the Internet. Disconnecting from Wifi, and manually connecting, fixes the issue.I notices as well, that connecting to the AP takes a LOT of time (up to 2-3 minutes).Log from earlier today:iPhone should roam to AP2, but does not.Reconnect to stronger AP2:Again disconnected and connection to wifi manually disabled (and reenabled) on iPhone.Notice the delay until connection to AP1 is made successfully. Nearly 3 Minutes passed until a successful connection to AP is madeMy configs:RB5009:AP1 config:AP2 (mostly identical):I can't figure it out.


---
```

## Response 14
Author: Thu Oct 31, 2024 10:16 pm
Why do your AP have a firewall?I prefer to follow the documentation on the CAP, in combination with bridge VLAN filtering for the ethernet ports.By leaving the 5GHz channel to auto, it is possible that the AP's are using the same frequencies. That could be a reason for having bad roaming experience. Check the frequencies or (better) set the (non overlapping) frequencies manually. ---

## Response 15
Author: Thu Oct 31, 2024 10:38 pm
Why did you cut out wifi interfaces from the config? ---

## Response 16
Author: Sat Nov 02, 2024 3:28 pm
``` 
```
/interface bridge vlan
add bridge=BR-MAIN comment=Management tagged=\
    "BR-MAIN,ether2 - AP1,ether3 - AP2" vlan-ids=50
add bridge=BR-MAIN comment=IoT tagged="BR-MAIN,ether2 - AP1,ether3 - AP2" \
    untagged="ether4 - Printer" vlan-ids=20
add bridge=BR-MAIN comment=WiFi tagged="BR-MAIN,ether2 - AP1,ether3 - AP2" \
    vlan-ids=10
```

```
```

```
/interface wifi channel
add disabled=no frequency=2412 name="CH 1 (2412)" width=20mhz
add disabled=no frequency=2437 name="CH 6 (2437)" width=20mhz
add disabled=no frequency=2462 name="CH 11(2462)" width=20mhz
add disabled=no frequency=5180 name="CH 36 (5180)" width=20/40/80mhz
add disabled=no frequency=5260 name="CH 52 (5260)" width=20/40/80mhz
add disabled=no frequency=5500 name="CH 100 (5500)" width=20/40/80mhz
add disabled=no frequency=5680 name="CH 136 (5680)" width=20/40/80mhz
add disabled=no frequency=5745 name="CH 149 (5745) SRD" width=20/40/80mhz
/interface wifi datapath
add bridge=BR-MAIN disabled=no name=DP_WIFI vlan-id=10
add bridge=BR-MAIN disabled=no name=DP_IOT vlan-id=20
/interface wifi security
add authentication-types=wpa2-psk disabled=no ft=yes ft-over-ds=yes name=\
    SEC_WIFI wps=disable
add authentication-types=wpa2-psk disabled=no ft=no ft-over-ds=no name=\
    SEC_IOT wps=disable
/interface wifi configuration
add channel="CH 149 (5745) SRD" channel.skip-dfs-channels=all country=Austria \
    datapath=DP_WIFI disabled=no name=WIFI-AP2-CH149 security=SEC_WIFI ssid=\
    Owcahome
add channel="CH 36 (5180)" channel.skip-dfs-channels=all country=Austria \
    datapath=DP_WIFI disabled=no name=WIFI-AP1-CH36 security=SEC_WIFI ssid=\
    Owcahome
add channel="CH 1 (2412)" channel.skip-dfs-channels=all country=Austria \
    datapath=DP_IOT disabled=no name=IOT-AP1-CH1 security=SEC_IOT ssid=IoT
add channel="CH 6 (2437)" channel.skip-dfs-channels=all country=Austria \
    datapath=DP_IOT disabled=no name=IOT-AP2-CH6 security=SEC_IOT ssid=IoT
/interface wifi capsman
set ca-certificate=auto certificate=auto enabled=yes interfaces=VLAN50_MGMT \
    package-path="" require-peer-certificate=no upgrade-policy=none
/interface wifi provisioning
add action=create-dynamic-enabled comment="5GHZ WIFI - AP1 CH36" disabled=no \
    master-configuration=WIFI-AP1-CH36 name-format=Wifi-%I radio-mac=\
    [REDACTED]  slave-configurations="" supported-bands=5ghz-ax
add action=create-dynamic-enabled comment="2.4 GHZ IOT - AP1 CH1" disabled=no \
    master-configuration=IOT-AP1-CH1 name-format=IoT-%I radio-mac=\
    [REDACTED] slave-configurations="" supported-bands=2ghz-g
add action=create-dynamic-enabled comment="5GHZ WIFI - AP2 CH100" disabled=no \
    master-configuration=WIFI-AP2-CH149 name-format=Wifi-%I radio-mac=\
    [REDACTED]  supported-bands=5ghz-ax
add action=create-dynamic-enabled comment="2.4GHZ - AP2 CH6" disabled=no \
    master-configuration=IOT-AP2-CH6 name-format=IoT-%I radio-mac=\
    [REDACTED] supported-bands=2ghz-g
```

Hi,thanks for your hints. I was reading a bit more and adapted my configuration.- enabledvlan-filteringon bridge on Capsman (RB5009). I somehow overlooked this setting. I noticed that the caps are listed asuntaggedfor pvid 1 - is this normal? (VLAN filtering isnotenabled on CAP`s bridge) For the other VLANs (10,20,50) bridge lists them astagged.- split up the wifi configuration, and added individual frequencies for all radios (as suggested by erlinden in a different post). I want to avoid DFS channels, so I chose CH149 (short range). Are there any downsides?Unfortunately no change visible. Devices are not roaming at all. With the previous setup (cap AC) and the vlan setup handled on the cap, it was working well.


---
```

## Response 17
Author: Sat Nov 02, 2024 3:38 pm
Exported also the interfaces from all devices (attached) ---

## Response 18
Author: [SOLVED]Wed Nov 06, 2024 8:09 pm
``` 
```
protocol-mode=none
```

I found the misconfiguration.Bridge on the caps hadset.After enabling RTSP, all issues went away.
```