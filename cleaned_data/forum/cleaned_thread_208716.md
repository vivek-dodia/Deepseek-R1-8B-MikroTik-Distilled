# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208716

# Discussion

## Initial Question
Author: Mon Jun 24, 2024 5:40 pm
``` :do { /system backup save name=&backupName; /export file=&backupName; /tool fetch upload=yes url=sftp://&serverIp/home/&user/&backupName.backup user=&user password=&password src-path=&backupName.backup port=&port; /tool fetch upload=yes url=sftp://&serverIp/home/&user/&backupName.rsc user=&user password=&password src-path=&backupName.rsc port=&port; } on-error={ :log info "Error while generating backup"; /system script remove [/system script find name=&scriptName]; /file remove "&backupName.backup"; /file remove "&backupName.rsc"; :error "Error sending the backups to the SFTP server, check if the server is up and if the credentials are correct."; } /system script remove [/system script find name=&scriptName]; /file remove "&backupName.backup"; /file remove "&backupName.rsc"; ``` My company manages lots of different mikrotik devices and every day at 5 AM in the morning a remote server runs a script that sends API requests to each device that creates a script that will generate a .backup file and a .rsc file and send it to our ubuntu SFTP server. Most devices work fine with this implementation but lots of the CCR models we have are having connection timeout problems after running the fetch for about 9 to 10 seconds. Maybe the timeout is to low, but I don’t see any flag to increase it.We tried to debug it to see if it is a problem with our code but it does not seem like it, we logged via winbox in the devices that had problems and tried making the request manually to see if it would work but it doesn’t.PS: The file is received by the server but it is not complete because the timeout of 10s cut itThe backup script that we use:
```
PS: character & indicates the beginning of a variable name that will be replaced before sending to the mikrotik device
```