# Thread Information
Title: Thread-1115590
Section: RouterOS
Thread ID: 1115590

# Discussion

## Initial Question
Hi, I am fairly new to the MikroTik world and RouterOS. I am trying to configure a bridge with tag stacking. Below is my network diagram.I have tagged packets coming from another router to MikroTik, and I am not aware of what tag they use (for this case, let's say the tag is 44). I am trying to perform tag stacking by adding an outer tag of 23 and passing it through my trunk link to a customer switch. On the customer switch, both VLANs 23 and 44 are configured, but the client is connected to an access port with VLAN 44 as the inner tag.Am I missing something, or do I need any additional configuration/interface bridgeadd name=bridge1 vlan-filtering=yes ether-type=0x8100/interface bridge portadd bridge=bridge1 interface=ether3add bridge=bridge1 interface=ether5 tag-stacking=yes pvid=23/interface bridge vlanadd bridge=bridge1 tagged=ether3 untagged=ether5 vlan-ids=23 ---

## Response 1
Isn't that the purpose of Q-in-Q ?https://help.mikrotik.com/docs/spaces/R ... LAN-Q-in-Q ---

## Response 2
What if we don't know what tag put on CUST Router ? ---

## Response 3
done that today.#add bridge with NO stp protocol and add forward-reserved-addresses=yes (fully L2 transparent)/interface bridgeadd forward-reserved-addresses=yes name=bridge1 protocol-mode=none vlan-filtering=no#add uplink port to bridge/interface bridge portadd bridge=bridge1 ingress-filtering=no interface="qsfp28-1-1--[uplink]"#add customer with tag stackingadd bridge=bridge1 edge=no ingress-filtering=no interface="sfp28-2--[customer-vlan2000]" point-to-point=no pvid=2000 tag-stacking=yes#vlan12 = mgmt/interface bridge vlanadd bridge=bridge1 tagged="bridge1, qsfp28-1-1--[uplink]" vlan-ids=12#vlan2000 for q-in-qadd bridge=bridge1 tagged="qsfp28-1-1--[uplink],bridge1" untagged="sfp28-2--[customer-vlan2000]" vlan-ids=2000ive also mapped the bridge to the vlan, cause ive configured an ip address for connecting to the customer cisco switches.vlan 1 nativevlan30 trunkevery packet/vlan gets encapuslated within vlan2000. works perfect - also spanning tree and cdp on the ciscos (due to forward-reserved-addresses).btw, u should play a little bit with ingress-filtering - actually ive disabled it, but i will keep an eye on it for safety reason. ---