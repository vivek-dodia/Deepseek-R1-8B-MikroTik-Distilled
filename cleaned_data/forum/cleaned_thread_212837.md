# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212837

# Discussion

## Initial Question
Author: Tue Nov 26, 2024 12:31 am
Is it possible to configure the hAPax2 with local wifi interfaces running in AX standard and activate CAPsMAN to manage two other cAPacs?If possible, could someone tell me the necessary steps?I have one hAPax2 (CAPsMAN) and two cAPac.Thanks in advance!!! ---

## Response 1
Author: [SOLVED]Tue Nov 26, 2024 8:35 am
The only way to do this, is to uninstall the qqireless package and install the wifi-qcom-ac package on the cAP ac.More info can be found here:https://help.mikrotik.com/docs/spaces/R ... edexamplesAnd here:https://help.mikrotik.com/docs/spaces/R ... 2/PackagesBasically (on the cAP ac):Uninstall wireless packageRebootInstall wifi-qcom-acAter installation, both devices are now available to be managed by the latest CAPsMAN version.There is a YouTube video about that:https://www.youtube.com/watch?v=bHotZT41w3E&t=89sBut also you can use the documentation for that:https://help.mikrotik.com/docs/spaces/R ... ionexample: ---

## Response 2
Author: Wed Nov 27, 2024 2:16 am
Thank you very much Erlinden!Your guidance was extremely important.Both cAPacs are now working perfectly.Regards.