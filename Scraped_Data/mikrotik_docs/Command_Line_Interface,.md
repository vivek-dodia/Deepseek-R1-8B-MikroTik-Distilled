---
title: Command Line Interface
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328134/Command+Line+Interface,
crawled_date: 2025-02-02T21:09:16.589355
section: mikrotik_docs
type: documentation
---

* 1Login Options
* 2Banner and Messages
* 3Command Prompt
* 4Hierarchy
* 5Item Names and Numbers5.1Item Names5.2Item Numbers
* 6General Commands
* 7Input Modes
* 8Quick Typing
* 9Console Search
* 10Internal Chat System
* 11List of Keys
* 5.1Item Names
* 5.2Item Numbers
The console is used for accessing the MikroTik Router's configuration and management features using text terminals, either remotely using a serial port, telnet, SSH, console screen withinWinBox, or directly using monitor and keyboard. The console is also used for writing scripts. This manual describes the general console operation principles. Please consult the Scripting Manual on some advanced console commands and on how to write scripts.
# Login Options
Console login options enable or disable various console features like color, terminal detection, and many other.
Additional login parameters can be appended to the login name after the '+' sign.
```
login_name ::= user_name [ '+' parameters ]
    parameters ::= parameter [ parameters ]
    parameter ::= [ number ] 'a'..'z'
    number ::= '0'..'9' [ number ]
```
If the parameter is not present, then the default value is used. If the number is not present then the implicit value of the parameter is used.
Example: admin+ct80w - will disable console colors, disable auto detection and then set terminal width to 80.
Param | Default | Implicit | Description
----------------------------------------
"w" | auto | auto | Set terminal width
"h" | auto | auto | Set terminal height
"c" | on | off | disable/enable console colors
"t" | off | off | Disable auto-detection of terminal capabilities
"e" | on | off | Enables "dumb" terminal mode
# Banner and Messages
The login process will display the MikroTik banner and short help after validating the user name and password.
```
MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK
  MikroTik RouterOS 6.22 (c) 1999-2014       https://www.mikrotik.com/
[?]             Gives the list of available commands
command [?]     Gives help on the command and list of arguments
[Tab]           Completes the command/word. If the input is ambiguous,
                a second [Tab] gives possible options
/               Move up to base level
..              Move up one level
/command        Use command at the base level
```
After the banner can be printed other important information, like/system noteset by another admin, the last few critical log messages, demo version upgrade reminder, and default configuration description.
For example, the demo license prompt and last critical messages are printed
```
UPGRADE NOW FOR FULL SUPPORT
----------------------------
FULL SUPPORT benefits:
- receive technical support
- one year feature support
- one year online upgrades
    (avoid re-installation and re-configuring your router)
To upgrade, register your license "software ID"
on our account server www.mikrotik.com
Current installation "software ID": ABCD-456
Please press "Enter" to continue!
dec/10/2007 10:40:06 system,error,critical login failure for user root from 10.0.0.1 via telnet
dec/10/2007 10:40:07 system,error,critical login failure for user root from 10.0.0.1 via telnet
dec/10/2007 10:40:09 system,error,critical login failure for user test from 10.0.0.1 via telnet
```
# Command Prompt
At the end of the successful login sequence, the login process prints a banner that shows the command prompt, and hands over control to the user.
Default command prompt consists of user name, system identity, and current command path />
For example, change the current path from the root to the interface then go back to the root
```
[admin@MikroTik] > interface [enter]
  [admin@MikroTik] /interface> / [enter]
  [admin@MikroTik] >
```
Useup arrowto recall previous commands (if this is a multiline command, then you can pressF8in order to expand it) from command history (commands that added sensitive data, like passwords, will not be available in the history),TABkey to automatically complete words in the command you are typing,ENTERkey to execute the command,Control-Cto interrupt currently running command and return to prompt and?to display built-in help, inRouterOS v7,F1has to be used instead.
The easiest way to log out of the console is to pressControl-Dat the command prompt while the command line is empty (You can cancel the current command and get an empty line withControl-C, soControl-Cfollowed byControl-Dwill log you out in most cases).
It is possible to write commands that consist of multiple lines. When the entered line is not a complete command and more input is expected, the console shows a continuation prompt that lists all open parentheses, braces, brackets, and quotes, and also trailing backslash if the previous line ended withbackslash-white-space.
```
[admin@MikroTik] > {
    {... :put (\
    {(\... 1+2)}
    3
```
When you are editing such multiple line entries, the prompt shows the number of current lines and total line count instead of the usual username and system name.
```
line 2 of 3> :put (\
```
Sometimes commands ask for additional input from the user. For example, the command '/password' asks for old and new passwords. In such cases, the prompt shows the name of the requested value, followed by colon and space.
```
/password
```
```
[admin@MikroTik] > /password
    old password: ******
    new password: **********
    retype new password: **********
```
# Hierarchy
The console allows the configuration of the router's settings using text commands. Since there is a lot of available commands, they are split into groups organized in a way of hierarchical menu levels. The name of a menu level reflects the configuration information accessible in the relevant section.
For example, you can issue the/ip routeprintcommand:
```
/ip routeprint
```
```
[admin@MikroTik] > /ip route print 
Flags: D - dynamic; X - disabled, I - inactive, A - active; 
C - connect, S - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn 
 #     DST-ADDRESS        GATEWAY            DISTANCE
 0  XS 4.4.4.4            10.155.101.1      
   D o 0.0.0.0/0          10.155.101.1            110
 1  AS 0.0.0.0/0          10.155.101.1              1
   D b 1.0.4.0/24         10.155.101.1             20
   D b 1.0.4.0/24         10.155.101.1             20
   DAb 1.0.4.0/24         10.155.101.1             20
[admin@MikroTik] >
```
Instead of typing `/ip route` path before each command, the path can be typed only once to move into this particular branch of the menu hierarchy. Thus, the example above could also be executed like this:
```
[admin@MikroTik] > /ip route
[admin@MikroTik] /ip/route> print 
Flags: D - dynamic; X - disabled, I - inactive, A - active; 
C - connect, S - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn 
 #     DST-ADDRESS        GATEWAY            DISTANCE
 0  XS 4.4.4.4            10.155.101.1      
   D o 0.0.0.0/0          10.155.101.1            110
 1  AS 0.0.0.0/0          10.155.101.1              1
   D b 1.0.4.0/24         10.155.101.1             20
   D b 1.0.4.0/24         10.155.101.1             20
   DAb 1.0.4.0/24         10.155.101.1             20
[admin@MikroTik] >
```
Each word in the path can be separated byspace(as in the example above) or by "/"
```
[admin@MikroTik] > /ip/route/
[admin@MikroTik] /ip/route> print 
Flags: D - dynamic; X - disabled, I - inactive, A - active; 
C - connect, S - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn 
 #     DST-ADDRESS        GATEWAY            DISTANCE
 0  XS 4.4.4.4            10.155.101.1      
   D o 0.0.0.0/0          10.155.101.1            110
 1  AS 0.0.0.0/0          10.155.101.1              1
   D b 1.0.4.0/24         10.155.101.1             20
   D b 1.0.4.0/24         10.155.101.1             20
   DAb 1.0.4.0/24         10.155.101.1             20
[admin@MikroTik] >
```
Notice that the prompt changes in order to reflect where you are located in the menu hierarchy at the moment. To move to the top level again, type " / "
```
[admin@MikroTik] > ip route
[admin@MikroTik] /ip/route> /
[admin@MikroTik] >
```
To move up one command level, type " .. "
```
[admin@MikroTik] /ip/route> ..
[admin@MikroTik] /ip>
```
You can also use/and..to execute commands from other menu levels without changing the current level:
```
[admin@MikroTik] /ip/route> /ping 10.0.0.1
10.0.0.1 ping timeout
2 packets transmitted, 0 packets received, 100% packet loss
[admin@MikroTik] /ip/firewall/nat> .. service-port print
Flags: X - disabled, I - invalid
#   NAME                                                                PORTS
0   ftp                                                                 21
1   tftp                                                                69
2   irc                                                                 6667
3   h323
4   sip
5   pptp
[admin@MikroTik] /ip/firewall/nat>
```
# Item Names and Numbers
Many of the command levels operate with arrays of items: interfaces, routes, users, etc. Such arrays are displayed in similarly-looking lists. All items in the list have an item number followed by flags and parameter values.
To change the properties of an item, you have to use the set command and specify the name or number of the item.
## Item Names
Some lists have items with specific names assigned to each of them. Examples are interface or user levels. There you can use item names instead of item numbers.
You do not have to use the print command before accessing items by their names, which, as opposed to numbers, are not assigned by the console internally, but are properties of the items. Thus, they would not change on their own. However, there are all kinds of obscure situations possible when several users are changing the router's configuration at the same time. Generally, item names are more "stable" than the numbers, and also more informative, so you should prefer them to numbers when writing console scripts.
## Item Numbers
Item numbers are assigned by the print command and are not constant - it is possible that two successive print commands will order items differently. But the results of the last print commands are memorized and, thus, once assigned, item numbers can be used even after add, remove and move operations (since version 3, move operation does not renumber items). Item numbers are assigned on a per session basis, they will remain the same until you quit the console or until the next print command is executed. Also, numbers are assigned separately for every item list, so /ip address printwill not change the numbering of the interface list.
```
ip address print
```
You can specify multiple items as targets to some commands. Almost everywhere, where you can write the number of items, you can also write a list of numbers.
```
[admin@MikroTik] > interface print
Flags: X - disabled, D - dynamic, R - running
  #    NAME                 TYPE             MTU
  0  R ether1               ether            1500
  1  R ether2               ether            1500
  2  R ether3               ether            1500
  3  R ether4               ether            1500
[admin@MikroTik] > interface set 0,1,2 mtu=1460
[admin@MikroTik] > interface print
Flags: X - disabled, D - dynamic, R - running
  #    NAME                 TYPE             MTU
  0  R ether1               ether            1460
  1  R ether2               ether            1460
  2  R ether3               ether            1460
  3  R ether4               ether            1500
[admin@MikroTik] >
```
# General Commands
There are some commands that are common to nearly all menu levels, namely:print, set, remove, add, find, get, export, enable, disable, comment, move.These commands have similar behavior throughout different menu levels.
Property | Description
----------------------
add | This command usually has all the same arguments as a set, except the item number argument. It adds a new item with the values you have specified, usually at the end of the item list, in places where the order of items is relevant. There are some required properties that you have to supply, such as the interface for a new address, while other properties are set to defaults unless you explicitly specify them.Common Parameterscopy-from- Copies an existing item. It takes default values of a new item's properties from another item. If you do not want to make an exact copy, you can specify new values for some properties. When copying items that have names, you will usually have to give a new name to a copyplace-before- places a new item before an existing item with a specified position. Thus, you do not need to use the move command after adding an item to the listdisabled- controls disabled/enabled state of the newly added item(-s)comment- holds the description of a newly created itemReturn Valuesadd command returns the internal number of items it has added
edit | This command is associated with the set command. It can be used to edit values of properties that contain a large amount of text, such as scripts, but it works with all editable properties. Depending on the capabilities of the terminal, either a full-screen editor or a single line editor is launched to edit the value of the specified property.
find | The find command has the same arguments as a set, plus the flag arguments like disabled or active that take values yes or no depending on the value of the respective flag. To see all flags and their names, look at the top of the print command's output. The find command returns internal numbers of all items that have the same values of arguments as specified.
move | Changes the order of items in the list. Parameters:the first argument specifies the item(-s) being moved.the second argument specifies the item before which to place all items being moved (they are placed at the end of the list if the second argument is omitted).
print | Shows all information that's accessible from a particular command level. Thus,/system clock printshows the system date and time,/ip route printshows all routes etc. If there\'s a list of items in the current level and they are not read-only, i.e. you can change/remove them (example of read-only item list is/system history, which shows a history of executed actions), then print command also assigns numbers that are used by all commands that operate with items in this list.Common Parameters:append -brief- forces the print command to use tabular output formcount-only- shows the number of itemsdetail- forces the print command to use property=value output formfile- prints the contents of the specific sub-menu into a file on the router.follow -follow-only -follow-strict -from- show only specified items, in the same order in which they are given.interval- updates the output from the print command for every interval of seconds.oid- prints the OID value for properties that are accessible from SNMP.proplist- comma-separated and ordered list of property names that should be included for the returned items.show-ids -where- show only items that match specified criteria. The syntax of where the property is similar to the find command.without-paging- prints the output without stopping after each screenful.
remove | Removes specified item(-s) from a list.
set | Allows you to change values of general parameters or item parameters. The set command has arguments with names corresponding to values you can change. Use ? or double Tab to see a list of all arguments. If there is a list of items in this command level, then the set has one action argument that accepts the number of items (or list of numbers) you wish to set up. This command does not return anything.
Common Parameters
* copy-from- Copies an existing item. It takes default values of a new item's properties from another item. If you do not want to make an exact copy, you can specify new values for some properties. When copying items that have names, you will usually have to give a new name to a copy
* place-before- places a new item before an existing item with a specified position. Thus, you do not need to use the move command after adding an item to the list
* disabled- controls disabled/enabled state of the newly added item(-s)
* comment- holds the description of a newly created item
Return Values
* add command returns the internal number of items it has added
* the first argument specifies the item(-s) being moved.
* the second argument specifies the item before which to place all items being moved (they are placed at the end of the list if the second argument is omitted).
```
/system clock print
```
```
/ip route print
```
```
/system history
```
Common Parameters:
* append -
* brief- forces the print command to use tabular output form
* count-only- shows the number of items
* detail- forces the print command to use property=value output form
* file- prints the contents of the specific sub-menu into a file on the router.
* follow -
* follow-only -
* follow-strict -
* from- show only specified items, in the same order in which they are given.
* interval- updates the output from the print command for every interval of seconds.
* oid- prints the OID value for properties that are accessible from SNMP.
* proplist- comma-separated and ordered list of property names that should be included for the returned items.
* show-ids -
* where- show only items that match specified criteria. The syntax of where the property is similar to the find command.
* without-paging- prints the output without stopping after each screenful.
# Input Modes
It is possible to switch between several input modes:
* Normal mode- indicated by normal command prompt.
* Safe mode- safe mode is indicated by the word SAFE after the command prompt. In this mode, the configuration is saved to disk only after the safe mode is turned off. Safe mode can be turned on/off withCtrl+X or F4.Read more >>
* Hot-lock mode- indicated by additional yellow >. Hot-lock mode autocompletes commands and can be turned on/off withF7
# Quick Typing
There are two features in the console that help entering commands much quicker and easier - the [Tab] key completions, and abbreviations of command names. Completions work similarly to the bash shell in UNIX. If you press the [Tab] key after a part of a word, the console tries to find the command within the current context that begins with this word. If there is only one match, it is automatically appended, followed by a space:
/inte[Tab]_becomes/interface _
If there is more than one match, but they all have a common beginning, which is longer than that what you have typed, then the word is completed to this common part, and no space is appended:
/interface set e[Tab]_becomes/interface set ether_
If you've typed just the common part, pressing the tab key once has no effect. However, pressing it for the second time shows all possible completions in compact form:
```
[admin@MikroTik] > interface set e[Tab]_
[admin@MikroTik] > interface set ether[Tab]_
[admin@MikroTik] > interface set ether[Tab]_
ether1 ether5
[admin@MikroTik] > interface set ether_
```
The[Tab]key can be used almost in any context where the console might have a clue about possible values - command names, argument names, arguments that have only several possible values (like names of items in some lists or name of the protocol in firewall and NAT rules). You cannot complete numbers, IP addresses, and similar values.
Another way to press fewer keys while typing is to abbreviate command and argument names. You can type only the beginning of the command name, and, if it is not ambiguous, the console will accept it as a full name. So typing:
```
[admin@MikroTik] > pi 10.1 c 3 si 100
```
equals to:
```
[admin@MikroTik] > ping 10.0.0.1 count 3 size 100
```
It is possible to complete not only the beginning, but also any distinctive sub-string of a name: if there is no exact match, the console starts looking for words that have string being completed as first letters of a multiple word name, or that simply contain letters of this string in the same order. If a single such word is found, it is completed at the cursor position. For example:
```
[admin@MikroTik] > interface x[TAB]_
[admin@MikroTik] > interface export _
[admin@MikroTik] > interface mt[TAB]_
[admin@MikroTik] > interface monitor-traffic _
```
# Console Search
Console search allows performing keyword search through the list of RouterOS menus and the history. The search prompt is accessible with the[Ctrl+r]shortcut.
# Internal Chat System
RouterOS console has a built-in internal chat system. This allows remotely located admins to talk to each other directly in RouterOS CLI. To start the conversation prefix the intended message with the # symbol, anyone who is logged in at the time of sending the message will see it.
```
[admin@MikroTik] > # ready to break internet?
[admin@MikroTik] > 
fake_admin: i was born ready
[admin@MikroTik] >
```
```
[fake_admin@MikroTik] > 
admin: ready to break internet?
[fake_admin@MikroTik] > # i was born ready
[fake_admin@MikroTik] >
```
# List of Keys
Key | Description
-----------------
Control-C | keyboard interrupt
Control-D | log out (if an input line is empty)
Control-K | clear from the cursor to the end of the line
Control-U | clear from the cursor to the beginning of the line
Control-X or F4 | toggle safe mode
F7 | toggle hot-lock mode
Control-R or F3 | toggle console search
F6 | toggle cellar
F1 | show context-sensitive help.
Tab | perform line completion. When pressed a second time, show possible completions.
# | Send a message to an internal chat system
Delete | remove character at the cursor
Control-H or Backspace | removes character before cursor and moves the cursor back one position.
Control-\ | split line at cursor. Insert newline at the cursor position. Display second of the two resulting lines.
Control-B or Left | move cursor backward one character
Control-F or Right | move cursor forward one character
Control-P or Up | go to the previous line. If this is the first line of input then recall previous input from history.
Control-N or Down | go to the next line. If this is the last line of input then recall the next input from the history
Control-A or Home | move the cursor to the beginning of the line. If the cursor is already at the beginning of the line, then go to the beginning of the first line of the current input
Control-E or End | move the cursor to the end of the line. If the cursor is already at the end of the line, then move it to the end of the last line of the current input
Control-L or F5 | reset terminal and repaint screen