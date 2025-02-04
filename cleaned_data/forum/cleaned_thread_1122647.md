# Thread Information
Title: Thread-1122647
Section: RouterOS
Thread ID: 1122647

# Discussion

## Initial Question
Hi, after updating routerros to version 7.12 it does not see the leox sfp insert in 2.5G mode.the earlier version did not have this problem. does anyone have such a problem? any idea? the router is rb5009 ---

## Response 1
Please check release notes before upgrading.Notice - SFP/QSFP functionality has been refactored for consistent behavior and better scalability. Now, compliance with SFP/SFP+/QSFP MSA standard is mandatory. This may cause issues with SFP/QSFP modules that are not fully compliant. All current MikroTik modules abide this standard.Regards ---

## Response 2
That is so sad, they should create an option something like "ignore compatibility" where you accept any risks and instabilities and just let people experiment on their own risk. I really hope that they make such an option, otherwise it is crazy, because some modules can't be replaced or have no compatible analogues. ---

## Response 3
hmm, this could be a problem. Are you running the LeolabsLXT-010S-H? ---

## Response 4
Yes. I've GPON STICK LXT-010S-H ---

## Response 5
i have Leolabs LXT-010S-H and its work but if i removed Leolabs LXT-010S-H from mikrotik rb5009 and insert it again i have to reboot mikrotik 4 or 5 times. ---

## Response 6
7.13 too. I have the same LEOX SFP+ model and MikroTik is unable to get "Module Present" enabled on this.Old ubiquiti works out of the box ---

## Response 7
Hi, Any new info about this topic? Still Leox SFP not working? ---

## Response 8
I'm also interested whether the issue is still present or it was something transient at OP's side?I'm expecting my LXT-010S-H to be delivered these days so this might be a problem for me if it turns out to be caused by Mikrotik ROS changes.Do you guys have the latest firmware (V3.3.4L4) for that SFP module? ---

## Response 9
Hi!Could anyone share current status with LXT-010S-H SFP GPON? ---

## Response 10
Hi!Could anyone share current status with LXT-010S-H SFP GPON?I had no issues to connect and use LXT-010S-H in my test RB2011 running 7.12.1I only noticed a change when I upgraded it to 7.13.3 in terms that it was displaying no-link but other sfp data was there.I had to disable auto-negotiation and manually set speed to 1gbase X and then it connected without issues. ---

## Response 11
Please check release notes before upgrading.Notice - SFP/QSFP functionality has been refactored for consistent behavior and better scalability. Now, compliance with SFP/SFP+/QSFP MSA standard is mandatory. This may cause issues with SFP/QSFP modules that are not fully compliant. All current MikroTik modules abide this standard.RegardsAre you kidding? So Mikrotik adopted the same smug tactics as Microsoft - you have to buy new CPU and Motherboard if you want to use Windows 11. With Mikrotik you have to change your cables if you want the latest RouterOS. At least Microsoft allows to bypass the need to use new CPU. I bet there is no way how to disable the forced compliance even when it is not needed. You could have just set the compliance as default and let the users turn it off. Jeeez ---