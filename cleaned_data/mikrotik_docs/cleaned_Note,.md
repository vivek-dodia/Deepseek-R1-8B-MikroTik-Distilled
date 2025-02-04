# Document Information
Title: Note
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/40992863/Note,

# Content
# Summary
```
/system note
```
The system note feature allows you to assign arbitrary text notes or messages that will be displayed on each login right after the banner. For example, you may distribute warnings between system administrators this way, or describe what does that particular router actually do. To configure system note, you may upload a plain text file namedsys-note.txton the router's FTP server, or, additionally, edit the settings in this menu
# Properties
Property | Description
----------------------
note(string; Default: ) | Note that will be displayed.
show-at-login(yes | no; Default:yes) | Whether to show system note on each login
show-at-cli-login(yes|no, Default:no) | Whether to show system note before telnet login prompt.
# Example
It is possible to add multi-line notes using an embedded text editor (/system note edit note), for example, add ASCII art to your home router:
```
system/note/set note=
```
```
.&@&   @&@@   @# @@&,      @@@      .@@@@@@@@@@@@@@@@@@@@@@@@@@,@           @@@           &@@@@          @@@          @@@@@@           @@@           @(&@@         @@@         @@@@@@@@     @@@     &@@@&&@@@@@@@@@@@@@@@&@@@@@
```