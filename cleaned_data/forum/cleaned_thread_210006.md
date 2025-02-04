# Thread Information
Title: Thread-210006
Section: RouterOS
Thread ID: 210006

# Discussion

## Initial Question
New CAP ax running 7.15.3 ARM64First power on, I connect to its temp WiFi SSID (password on sticker) and login to it with Winbox ("admin" password on sticker).I set a new admin password, then go to System > Reset Configuration > "Reset in CAPS Mode"It reboots and joins my CAPsMAN v2 controller and works just fine for WiFi, HOWEVER, I can no longer login to the CAP ax itself via Winbox. I've tried admin with my new password, admin with the sticker password, admin with a blank password and no matter what Winbox says "wrong username or password" when connecting.So the question is, does resetting into CAPS mode change the admin password to something else? All I can find in the Mikrotik doc about CAPS mode is this fromhttps://help.mikrotik.com/docs/display/ ... ations-CAP:CAPThis type of configuration is used when a device needs to be used as a wireless client device controlled by CAPsMAN.When CAP default configuration is loaded, ether1 is considered a management port with DHCP client configured. All other Ethernet interfaces are bridged and wlan1 is set to be managed by CAPsMAN.To load CAP configuration refer to Reset Button manual. ---

## Response 1
I set a new admin password, then go to System > Reset Configuration > "Reset in CAPS Mode"And did you also tick 'Keep users' ?If not ... reset to default it is.Quite logical.Be careful with sticker passwd.O, 0Upper I, lower LEven when MAC address shows striked zero, O can be zero, not O...Been there, done that, seen all possible problems.Phone camera x3 helps.Recently they changed the procedure to use a different font so those differences become more clear and they avoid ambiguous characters but what's in stock, can still have all these problems. ---

## Response 2
It's happening to me, also. Default password works for a complete factory reset, but when put into a caps mode reset, default password no longer works.With an 'O' or a '0', with old default password of 'admin', or no password doesn't work either.This has been a really frustrating install. Only one access point out of 21 is doing this.Another issue I've run into is that on the iPhone app, it resets an access point different from the one I'm connected to. The Android app doesn't have that problem. Also, the iPhone app doesn't give an option to connect to mac or IP. Consequently, I can't even isolate the problem. ---

## Response 3
I just had this on a newly purchased cAP AX that shipped with 7.11.3. Checked it before resetting, and it was working with the default password from the sticker.Used the reset button to reset into CAPS mode and the password didn't work. In my case a blank password worked. ---

## Response 4
Interesting ... 7.11.3 may contain a bug then for that part.But in the mean time we're already at 7.16.1. ---

## Response 5
It does seem to be a bug only in older versions. I just checked and this doesn't happen after the 7.16.1 upgrade.That may be why @dlynes had it happen only on one AP. ---

## Response 6
Hi all, I think I've encountered the same issue described here on the Audience AP running firmware 7.16.2 - after resting to CAPS mode I can no longer log in.What seems to be happening is that invoking the CAPS join mode (either via System \ Reset Configuration \ CAPS Mode without "Keep users" option enabled, or via the reset button) resets the password for admin user to something other than the default (by default, Audience devices have empty password).The device connects to CAPsMAN and gets the config, but it's impossible to log in to the admin interface (either web or WinBox).Additionally, trying to reset the device to defaults via the reset button doesn't seem to reset the admin credentials - network config is reset, but admin login is still impossible.The only way out it to flash the firmware via NetBoot.If the password is configured before enabling CAPS mode, and the "Keep users" option is selected, then the authentication works. ---