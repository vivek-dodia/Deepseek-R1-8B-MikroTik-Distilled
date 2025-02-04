# Thread Information
Title: Thread-213288
Section: RouterOS
Thread ID: 213288

# Discussion

## Initial Question
Using cli.I'm able to create the files for archiving. How do I get the files off the router without Webfig or Winbox? ---

## Response 1
Ssh / ftp / smb / ... you can even mail them to yourself.Plenty of options. ---

## Response 2
more specifically. I'm in a ssh session to the router.What mechanism (from the router) can you suggest to put the files on the ssh host connection...or ftp to ourexternal ftp server?I don't see an ftp command from the cli session, I tried running an scp connection to the router, no luck.any other ideas?New to the device, trying to get another device setup based on the working router configuration. Read about how you need to edit theconfigs when importing into a new device. ---

## Response 3
From the router, you have /tool/fetch mode=sftp (or =ftp):https://help.mikrotik.com/docs/spaces/R ... 8514/FetchOtherwise from Linux/etc, scp will work like ssh. But AFAIK there is no scp from router to another device. ---

## Response 4
scp worked.I was using:scp admin@192.168.80.1:/file/cluster.txt.rsc /home/bret/cluster.txt.rsc (errored out, assumed the /file was location)This worked:scp admin@192.168.80.1:/cluster.txt.rsc /home/bret/cluster.txt.rscAppreciate the suggestion. Stayed with it. Now I'll try importing.Cold here in Northern Cal. ---