# Thread Information
Title: Thread-206828
Section: RouterOS
Thread ID: 206828

# Discussion

## Initial Question
Hi there, Has skins being deprecated in recent RouterOS? I am on 7.14.2 and uploading a skin via scp doesn't work, I can upload the json file to the root of the Mikrotik but no longer under /skins/ folder:
```
scp engineers.json admin@my-fw:/skins/engineers.json
scp:dest open"/skins/engineers.json":Unknownstatus
scp:failed to upload file engineers.json to/skins/engineers.jsonHowever once I create the skin in webfig and it shows automatically in files, then I can upload since the folder exists
```

```
scp engineers.json admin@my-fw:/skins/engineers.json
engineers.jsonSo the first issue is seems to be creating folders, I tried hacking it with smb share then deleting it, despite not being ideal, that didn't work either.The weirdest thing is that under the skin dropdown for the group, it doesn't show any skin, either the one I uploaded or the one the Mikrotik created itself!Am I going crazy or the feature is bugged out?ThanksP

---
```

## Response 1
Just create a new skin and compare/see where it gets stored. This should answer your question where to put the Json file correctly. ---

## Response 2
what hardware do you use? I used a routerboard with 7.14.2 just yesterday and the skin folder was present. In any case I would do as advised. log in from webfig and draw a skin and see where it is saved ---

## Response 3
In version 7.15 skins created are stored in flash/skins. I created a 'skins' directory outside the 'flash' directory and manually stored .json skin files there, problem solved. ---

## Response 4
Upgraded to 4.15.3 and now it recognizes the skins. However there is a catch.You can't upload them directly via SCP since it will fail, nor you can do the previous trick of setting an smb share with the skins folder name so it will create the folder then remove it.The only way I got it to work is to create another skin in webfig (this wasn't working previously either) then delete it and you can upload to the folder now.Automation down the bin, but hey ho!You are wrong about the flash directory, only some devices have that of which none of mines.CheersP ---

## Response 5
From what I’ve seen, creating a skin through WebFig first, then using that folder for your uploads, seems to be the workaround. I've also run into similar problems where SCP alone didn’t cut it.But if you’re into skins for other things like games, you might findskin.landhelpful. It’s where I go to buy and sell game skins, and it’s been working pretty smoothly for me. ---

## Response 6
From what I’ve seen, creating a skin through WebFig first, then using that folder for your uploads, seems to be the workaround. I've also run into similar problems where SCP alone didn’t cut it.That's the best advice: let webfig create it first.Especially if you have an older router, I'm not 100% upgrades actually upgrade the skin files so if router is older the format might not be right. Save default (or new ones) in webfig is what I'd recommend & it knows where to put it(which is generally /flash/skins if there is a flash directory, otherwise it's just "/skins") ---

## Response 7
I had the same issue (sending skins to the router with scp), but it just seems the way to do it has changed....1/ scp is not the easiest way, better doing a fetch (any protocol) as it will create any missing subfolders in /file2/ it seems you then need to reboot so the new skin is available for /user group add3/ /user group add...done ---