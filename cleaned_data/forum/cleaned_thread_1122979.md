# Thread Information
Title: Thread-1122979
Section: RouterOS
Thread ID: 1122979

# Discussion

## Initial Question
HelloI have tried to find an answer to this in the documentation and on youtube without any luckSo I have an Rb5009 that has a handfull of vlans on it that is working just fine.But now I have an wAPax that I want to have different SSID`s on different vlans.The plan is to have the RB5009 to handle all the dhcp and firewall for everything.As far as I understand, the vlans I want to use for wireless need to be setup on the rb5009 as it will handle the dhcp and the port that goes to the wap should then be an trunk port, but does the vlans need to be defined under bridge-->vlan on the wap too and if yes, all vlans or only the ones that comes though the trunk to the wap? ---

## Response 1
Will you be using capsman? ---

## Response 2
Will you be using capsman?Since I only have one AP and don’t think I will get another one for a long time, no ---

## Response 3
So the guide for setting up vlans is this:viewtopic.php?t=143620The difference for AP is that only the trusted vlan has the bridge tagged as well in /interface bridge vlan settings.The router all vlans have the bridge tagged.Once you have both done,,,,,,,post for review/export file=anynameyouwish (minus router serial number, any public WANIP information, keys etc. )PS. I normally first take an unused port and take it off the bridge give it an address 192.168.55.1/30, and the plug into the port with my laptop changing ipv4 settings to 192.168.55.2Much safer place to do vlan configs on bridges...... dont forget to add etherX to the LAN interface list or TRUSTED interface list. ---

## Response 4
I looked into the AP config from that post and as I thought the vlans that will be used on the wifi +the trunk need to defined on the wAPax, but not the vlans that should not be accessible over wifiWill see if I can manage to set this up ---

## Response 5
With ax devices, the wifi driver can indeed handle tagging/untagging on its own. So you'll have to specify an/interface/wifi/datapathrow for each SSID; eachdatapathrow will have an individualvlan-idvalue and a commonbridgevalue. The/interface/wifi/configurationrows will specify thessidvalues and refer to thedatapathones.The wifi driver will make all the wifi interfaces member ports of the bridge in trunk mode and do the tagging/untagging internally; such an approach allows/interface/wifi/access-listrules or RADIUS authentication responses to override the VLAN ID specified on thedatapathrow, so some clients connected to a given SSID may be connected into other VLANs this way. This also removes the need to activatevlan-filteringon the bridge on the AP if you do not need it for other purposes. ---

## Response 6
I got it to workGot a bit confused on where to set the vlan-IDs, but made sense after a whileI thought I could set different vlan-IDs in the wifi configuration but if I do that, my wifi devices wont connect at all. As far as I understand, that makes the SSID tagged on that vlan.But if I after making an slave-SSID defines that "interface" as an port in the bridge setting, I can set the PVID there and then it works ---

## Response 7
I can see no/interface/wifi/datapathsection in your export so no wonder it did not work the way I've described. But the way you've done it is not wrong, it just does not make use of the advanced features of the wifi-qcom driver used on ax devices as compared to the wifi-qcom-ac one used on ac devices. ---

## Response 8
I found the Datapath in winbox now, but this is totally new to me so I have no clue how to setup that correct.But I guess it would look something like in this screenshot and then as you say, under wifi-->configuration the correct Datapath profile is selected.And if I do it this way, there is no need to define the PVID on the Bridge-->Inteface ? ---

## Response 9
If you do it that way, there is even no need to add the/interface/bridge/portrow as it is added dynamically instead. You can think of the datapath row as of a template for that. It means you have to remove the statically added/interface/bridge/portrow before re-provisioning the radios with the datapath added to the configuration. ---