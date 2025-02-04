# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212776

# Discussion

## Initial Question
Author: Sun Nov 24, 2024 1:50 am
Hello.I have hAP ax3. Was firmware 7.15.1.Updated to 7.16.1. Stopped working WiFi, in logs appeared the entry "defconf gen: unable to find wireless interface(s)".Rolled back to 7.15.1 - problem remained.Reset to factory settings - did not help.Please tell me what I’m doing wrong?screen.jpg ---

## Response 1
Author: [SOLVED]Sun Nov 24, 2024 3:32 am
Well... Mikrotik has two (actually three) wireless drivers:wireless - works with 802.11n and ac capable deviceswifi-qcom-ac - works only with ac devices and enables some additional features compared to wirelesswifi-qcom - works with ax devicesAs Mikrotik publishes the above:https://help.mikrotik.com/docs/spaces/R ... 2BpackagesYou currently have BOTH wireless and wifi-qcom installed, and only wireless is enabled. As written above: this DOES NOT support your device.What you need to do: uninstall wireless and enable qcom-ac. You will need to reboot for it to take effect.Your wifi interfaces will appear. If you want default configuration, you will probably have to do a "reset to defaults" thingy (either with reset button or from menu...)Hope this helps! ---

## Response 2
Author: Sun Nov 24, 2024 11:16 am
Yes, after a few hours of experiments, I realized what had happened and corrected the situation. The model page to download offers wrong files, this is what caused my difficulties. Before the manual upgrade, I should have seen which packages are installed in this model. Thank you!page.jpg ---

## Response 3
Author: Sun Nov 24, 2024 12:17 pm
Glad it worked out.Could you point this out tosupport@mikrotik.comso they can fix this. ---

## Response 4
Author: Sun Nov 24, 2024 3:00 pm
That's the page forAC3.You can tell seeing arm version instead of arm64.Different thing.Page for AX3 is correct.And the only correct driver for AX3 is wifi-qcom.NOT wifi-qcom-ac. ---

## Response 5
Author: Sun Nov 24, 2024 3:27 pm
Yep. Ax3 does have the correct packages.I'm still at a loss as to what could have happened, because obviously arm packages wouldn't have installed at all... ---

## Response 6
Author: Mon Nov 25, 2024 12:53 am
Damn it! That’s right. I made the problem myself. It was a night, I was tired. ARM packages were not installed, so I went and found ARM64, the wrong package "wireless" on inertia. Then looked at the logs that he wants "Wi-Fi-qcom", gave him. Well and then you know. ---

## Response 7
Author: Mon Nov 25, 2024 7:41 am
Been there.Glad it's resolved.