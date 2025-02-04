# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210971

# Discussion

## Initial Question
Author: Tue Sep 17, 2024 10:17 am
``` :local now [/system clock get date]; /tool fetch url=("sftp://user:secret@host/path/Backup_" . $now . ".rsc") src-path=("Backup_" . $now . ".rsc") upload=yes; ``` ``` executing script from scheduler failed, please check it manually ``` Hello everyone!I’m running the following MikroTik script from the scheduler:
```
The script has the following permissions: ftp, read, write, and sensitive.When I execute the script manually from the terminal, it runs without any issues.However, when the scheduler triggers it, I receive the following error message:
```

```
Could anyone help me understand why this is happening and how to fix it?I’d really appreciate your assistance!Thank you in advance!
```