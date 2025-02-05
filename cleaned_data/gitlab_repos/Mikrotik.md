# Repository Information
Name: Mikrotik

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/audy018/Mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
# Mikrotik
a Collection of handy Mikrotik Scripts
Many of these scripts rely on Telegram to send notifications to your telegram bot with variables set in the setGlobals script. More details below on how to activate your bot.
[![Donate Bitcoin](https://user-images.githubusercontent.com/18201320/42027759-bdec89d8-7aca-11e8-91b4-f36648eb0ae7.png)](https://jacauc.github.io/donate-bitcoin/)
# How to Create a Telegram bot
Detailed instructions for setting up the Telegram Bot: https://www.forsomedefinition.com/automation/creating-telegram-bot-notifications/
Simplified instructions:
0. Use telegram
1. Chat with @botfather
2. Type /newbot
3. Give your bot a name... e.g. myMikrotik
4. Give your bot a username... e.g. MyMikrotikBot
5. You will get a message like this:
![2018-01-06_15-53-12](https://user-images.githubusercontent.com/18201320/34640372-fd5d8314-f2f9-11e7-9b86-c9a30ee889b2.png)
6. RECORD THE TOKEN SHOWN IN THE MESSAGE
7. Start a chat with your bot and type /start
8. Exit aforementioned chat and create a Telegram Group conversation. Call it something like "Mikrotik Notifications"
9. Invite your bot to the group.
10. Access the following page (insert your bot's TOKEN and remove the <<< and >>> characters): 
```
https://api.telegram.org/bot<<<TOKEN>>>/getUpdates
```
11. Look for the group's ID as shown in green below. The group ID will normally be preceded by a minus sign. RECORD THE GROUPID:
![2018-01-06_16-06-23](https://user-images.githubusercontent.com/18201320/34640491-4faaa5f0-f2fc-11e7-853e-72cc5b1df323.png)
12. Do a test - You should now get a hello world message in the telegram group from your bot. If this didn't work, check steps 1-11 again. 
  ```
  https://api.telegram.org/bot<<<TOKEN>>>/sendMessage?chat_id=<<<-GROUPID>>>&text=Hello+World
  ```
13. Keep your GROUPID and TOKEN and replace the values accordingly in setGlobals Script.
[![Donate Bitcoin](https://user-images.githubusercontent.com/18201320/42027759-bdec89d8-7aca-11e8-91b4-f36648eb0ae7.png)](https://jacauc.github.io/donate-bitcoin/)