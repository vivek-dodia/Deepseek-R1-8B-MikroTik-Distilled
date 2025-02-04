# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 204351

# Discussion

## Initial Question
Author: Sat Feb 10, 2024 1:28 pm
Goodmorning, after generate a backup with my MacOS terminal, via SSH[admin@MikroTik] > /system backup save name=test password=<YOUR_PASSWORD>Configuration backup savedI would like to retrieve it, from the Router.A gentlemen on this forum, told me to use it Netinsall, and it work fine; BUT I do have MacBook, and to get Netinstall working I do need to use a Windows PC and the router connected via ETH Cable.Is there any command, via terminal (SSH) that allow me to download files from the Router ?For example, /file print, list me all the available files, is there a command like /file download name=test or /file get name=test ? (GET do something, but I believe not exactly what I'm looking for)Model RBwAPGR-5HacD2HnDRevision r3Firmware Typ ipq4000LCurrent Firmware 6.49.12Thank again for your support and endurance ---

## Response 1
Author: Sat Feb 10, 2024 2:03 pm
``` scp username@router_ip:filename . ``` from macos terminal: