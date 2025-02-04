# Thread Information
Title: Thread-213932
Section: RouterOS
Thread ID: 213932

# Discussion

## Initial Question
Using this official example from the wiki:https://wiki.mikrotik.com/Manual:Interf ... ess_Ports)Why is it that you have to specify `untagged=ether6` after you've already assigned the pvid (`pvid=200`) while adding `ether6` as a bridge port? What happens if I don't add `ether6` to VLAN 200's `untagged` list? And what happens if I add it to VLAN 300's `untagged` list? ---

## Response 1
Why is it that you have to specify `untagged=ether6` after you've already assigned the pvid (`pvid=200`) while adding `ether6` as a bridge port?You do not have to.What happens if I don't add `ether6` to VLAN 200's `untagged` list?It is added dynamically based on the PVID setting. There may have been early versions of RouterOS when VLAN-aware bridges were introduced where this was not the case and you had to add the manual untagged membership.And what happens if I add it to VLAN 300's `untagged` list?Packets from VLAN 300 egressing through ether6 would be untagged, so it wouldn't make sense in regular network setups as any packets ingressing through ether6 would be tagged for VLAN 200 due to the portpvid=200setting.The old Wiki pages have not been updated for some time, the new documentation is more representative of current functionalityhttps://help.mikrotik.com/docs/spaces/R ... NFiltering ---

## Response 2
Why is it that you have to specify `untagged=ether6` after you've already assigned the pvid (`pvid=200`) while adding `ether6` as a bridge port?You do not have to.What happens if I don't add `ether6` to VLAN 200's `untagged` list?It is added dynamically based on the PVID setting. There may have been early versions of RouterOS when VLAN-aware bridges were introduced where this was not the case and you had to add the manual untagged membership.And what happens if I add it to VLAN 300's `untagged` list?Packets from VLAN 300 egressing through ether6 would be untagged, so it wouldn't make sense in regular network setups as any packets ingressing through ether6 would be tagged for VLAN 200 due to the portpvid=200setting.The old Wiki pages have not been updated for some time, the new documentation is more representative of current functionalityhttps://help.mikrotik.com/docs/spaces/R ... NFilteringThanks a lot for the swift answer. Yeah this all makes sense. I'm quite new to the whole Mikrotik ecosystem as you can probably tell, so I'm sort of expecting to run into a bunch of gotchas. Thanks again! ---

## Response 3
viewtopic.php?t=143620 ---