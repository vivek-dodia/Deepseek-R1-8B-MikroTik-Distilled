# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213750

# Discussion

## Initial Question
Author: Wed Jan 08, 2025 8:26 am
``` /export hide-sensitive file=MyConfig ``` ``` /export file=MyConfig ``` There is no reason why you can't configure your router to act as a switch using RouterOS (I did a couple of years ago to try it out) but you willl need to make all of the configuration changes manually. The main thing is to move eth0 to the bridge and remove the firewall rules, turn off dhcp server, etc so that itonlyacts as a switch.--Backups are your friend. Always make a backup!/system backup save encryption=aes-sha256 name=MyBackupPlease, export and attach your current config to your post if you want help with a config issue:RouterOS v6 codeRouterOS v7 code