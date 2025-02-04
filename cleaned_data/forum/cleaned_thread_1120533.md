# Thread Information
Title: Thread-1120533
Section: RouterOS
Thread ID: 1120533

# Discussion

## Initial Question
Good day.Have this issue twice.On one branch was installed Mikrotik RB750 ver 6.3X. Connection between branch and headquarter provided by IPSec VPN IKEv2.Everything was fine till power failure. After it device rebooted without any errors, but section IP-->IPSec become totally empty, with no any records. And another setting like FW, DCHP, DNS, NTP, etc were OK, like they were before power failure. Only IPSec was missed.- I tried to restore settings from backup - no luck (the same situation with IPSec section)- I tried to restore settings form script - device freezed, only reboot helped me- I tried to to print out export command in Terminal - device freezed again, only reboot helped me- I tried to made reset factory default and after make restore - no luck again- I tried to make IPSec configuration from the begining, manually step-by-step. But Mikrotik just doesn't allow to press button Aplly or OK in configuration settings.OK, in that time we just decided that this was hardware issue (device was too old) and changed it to new RB4011 ver. 6.44.. For few month everything was OK but today we got another power failure and IPSec was missed one more time. Now we have totally the same symptoms. System log doesn't show any errorsSo now I have a lot of questions, but one of them - how to fix it? Should we buy new device each time after power failure? Why it impacts only on IPSec section?Regards ---

## Response 1
Same here: New (less than six months) RB4011iGS+ lost IPsec secret and L2TP server Enabled settings after a power cut.Obviusly VPN was not working; after re-enable L2TP server and setting up IPsec Secret again everything is (as far as I can tell yet) as it was.Anyone has any information about it? ---

## Response 2
Resurrecting this topic, because I have the same issue since yesterday, despite the power loss. The IPSec settings magically disappeared and even the supout.rif process times out at 64%. Can't reboot the device right now, because the SSTP server is heavily used. Maybe a reboot is possible at the weekend.Has anyone an idea about that? Or to solve this without reboot or reinstall the whole device?Deactivating the L2TP server, setting the password again have not helped. ---

## Response 3
Installing the newest software version (7.17) has helped, but I suspect, that a reinstallation of the old one would have helped too. Very strange behavior. We got it on a second device too. ---