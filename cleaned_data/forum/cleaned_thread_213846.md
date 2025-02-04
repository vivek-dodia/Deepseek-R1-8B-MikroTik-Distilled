# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213846

# Discussion

## Initial Question
Author: Sat Jan 11, 2025 1:32 am
Hi, I'm trying to run the command below via a script. It runs perfectly fine in the terminal as expected, but when I write it in a script and run it, nothing happens.log: executing script ssh-script from winbox failed, please check it manuallyScript :/system ssh address=y.y.y.y user=admin command="/user-manager user set [find name=x-x.x.x] disabled=no"(ssh keys used for authentication)After some investigation, I concluded that the problem is that Router A (SSH client) cannot connect to Router B (SSH server) via the script.how to solve this? ---

## Response 1
Author: [SOLVED]Sat Jan 11, 2025 7:21 pm
non interactive is/system ssh-exec