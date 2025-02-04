# Thread Information
Title: Thread-1121584
Section: RouterOS
Thread ID: 1121584

# Discussion

## Initial Question
Hello MikroTik Community, I am facing an issue with downgrading my MikroTik hAP ax3 ARM 64 router from RouterOS version 7.18beta2 to 7.16.2. I have tried multiple methods but have been unable to get the desired version to install successfully.Steps Taken:Verified the correct .npk file: I confirmed that I am using the correct routeros-7.16.2-arm64.npk file for my router’s architecture (ARM 64).Uploaded the .npk file: I uploaded the file to the "Files" directory by dragging and dropping the .npk file using Winbox.Rebooted the router: After uploading the .npk file, I rebooted the router.Checked the packages: I verified that the file was present in the "Files" directory using /file print. I also checked the installed packages with /system package print, but the 7.16.2 package does not appear, and the router continues to show 7.18beta2.Attempted to remove the 7.18beta2 packages: I used the following commands to remove all components of the newer version:/system package disable wifi-qcom routeros rose-storage/system package remove wifi-qcom routeros rose-storageHowever, the system continues to show 7.18beta2 packages as installed.Checked logs for errors: I checked the logs with /log print where message~"package", and the following warning appeared:omitting package system-7.16.2: newer package system-7.18beta2 is already installedRe-uploaded the .npk file: I re-uploaded the file and rebooted, but the issue persists.What further steps should I take to downgrade to RouterOS 7.16.2?would greatly appreciate any guidance or suggestions.Thank you for your help! ---

## Response 1
Is this a very new router?Check System > RouterBoard and see what the factory firmware version is. You can't downgrade to anything lower than that version. ---

## Response 2
Not that new![admin@MikroTik] /system> routerboard/printrouterboard: yesboard-name: hAP ax^3model: C53UiG+5HPaxD2HPaxDserial-number: ********firmware-type: ipq6000factory-firmware: 7.6current-firmware: 7.17upgrade-firmware: 7.18beta2 ---

## Response 3
For minimum ROS version you have to check this:
```
/system/resource/printSometimes it can be different than routerboot (I have a wAP ax withfactory-firmware: 7.15.2andfactory-software: 7.15.1).Anyway, proper way for downgrading is toget list of installed packages (disabled as well)upload all corresponding package files but for older version (e.g. routeros, wifi-qcom, rose, etc.)execute/system/package/downgraderebootBullet #3 is different from upgrading ROS via otherwise identical way.

---
```

## Response 4
It could be the new 'security' feature introduced in 7.17 -/system device-modehas been changed.By defaultinstall-any-versionis set tonowhich prevents installation of anything with a lesser version than listed inallowed-versions, seehttps://help.mikrotik.com/docs/spaces/R ... evice-mode ---

## Response 5
It could be the new 'security' feature introduced in 7.17 -/system device-modehas been changed.By defaultinstall-any-versionis set tonowhich prevents installation of anything with a lesser version than listed inallowed-versions...Right, but default setting forallowed-versionsis 7.13+ ... so downgrade to 7.16.2 should be possible. ---

## Response 6
"Rebooted the router: After uploading the .npk file, I rebooted the router." : To downgrade, you don't have to reboot, but click on the specific downgrade button on winbox (system/package)AND you have maybe, to configure the fu...ing device-mode to allow downgrade, if you see a message about that in logs.I'm trying upgrade to beta and downgrade with an hap ax3 on my lab.... ---

## Response 7
success for theses versions changes : 7.17 >> 7.16.2 >> 7.18b2 >> 7.16.2 >> 7.17In less than 15min, with only routeros+wifi-qcom packages and the last backup restored to avoid problems. ---

## Response 8
Thank you so much for testing this in your lab.I will try again when I get home.The new OS messed up my smb clients and I need fo downgrade for now.This time I’m going to copy all 3 packages and try again.I Will update this post… ---

## Response 9
No problem, i have a lab with rb5009, hex, hap ax3, hap ac3, cap ax and an old crs125 (capricious psu problem i think) if necessary. ---

## Response 10
Copying all three files together did the trick!Damn! I was rebooting and rebooting, lmao!Thank you so much for the help, as well as the other guys who commented. ---