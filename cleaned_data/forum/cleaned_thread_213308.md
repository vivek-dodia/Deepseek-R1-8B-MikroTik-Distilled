# Thread Information
Title: Thread-213308
Section: RouterOS
Thread ID: 213308

# Discussion

## Initial Question
I am experiencing an issue with my RouterBOARD 951ui-2HnD. I am unable to upload files or create a backup, encountering the error "no enough permission." I have tried using web, Winbox, and FTP methods, and even reset the router, but the error persists.I tried to generate the file supout.rif but encountered an error, which is attached. Any attempt to create or upload files results in errors. I have reset the router and tried with default settings, but the same error persists. ---

## Response 1
If you are usingadminuser device is probably hacked. Netinstall device and restore config from export (not backup!). ---

## Response 2
... restore config from export (not backup!).Or, better yet, start from default config and apply minimum changes required. It's possible that flakey config allowed exploit to succeed. ---

## Response 3
Could be, but also can be just simple admin password easy to guess and breach was done from LAN. ---

## Response 4
I've tried all of this and reinstalling through netinstall is also not possible because the router's hard drive is not recognized. Even after a hard reset, the router cannot upload a file or even create a backup file. It seems that nothing can be upload or download from server on the router. I even tried to update to the trial version and it also failed. ---

## Response 5
Trial version? Or you mean beta/rc version? ---