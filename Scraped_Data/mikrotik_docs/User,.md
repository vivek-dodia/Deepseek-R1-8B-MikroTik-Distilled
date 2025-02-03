---
title: User
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/8978504/User,
crawled_date: 2025-02-02T21:09:46.133013
section: mikrotik_docs
type: documentation
---

# 2Summary3User Settings4User Groups4.1Properties4.2Default groups5Router Users5.1Properties5.2Actions5.3Notes6Monitoring Active Users6.1Properties6.2Request logout7Remote AAA7.1Properties8SSH Keys8.1Public keys8.2Private keys
* 2Summary
* 3User Settings
* 4User Groups4.1Properties4.2Default groups
* 5Router Users5.1Properties5.2Actions5.3Notes
* 6Monitoring Active Users6.1Properties6.2Request logout
* 7Remote AAA7.1Properties
* 8SSH Keys8.1Public keys8.2Private keys
* 4.1Properties
* 4.2Default groups
* 5.1Properties
* 5.2Actions
* 5.3Notes
* 6.1Properties
* 6.2Request logout
* 7.1Properties
* 8.1Public keys
* 8.2Private keys
# Summary
MikroTik RouterOS router user facility manages the users connecting the router from any of theManagement tools. The users are authenticated using either a local database or a designated RADIUS server. Each user is assigned to a user group, which denotes the rights of this user. A group policy is a combination of individual policy items.
In case the user authentication is performed using RADIUS, theRADIUSclient should be previously configured.
# User Settings
The settings submenu allows to control the password complexity requirements of the router users.
Property | Description
----------------------
minimum-password-length(integer; 0..4294967295; Default: ) | Specifies the minimum character length of the user password
minimum-categories(integer; 0..4; Default: ) | Specifies the complexity requirements of the password, with categories beinguppercase, lowercase, digit, symbol.
Specifies the complexity requirements of the password, with categories beinguppercase, lowercase, digit, symbol.
# User Groups
The router user groups provide a convenient way to assign different permissions and access rights to different user classes.
## Properties
Property | Description
----------------------
name(string; Default: ) | The name of the user group
policy(local | telnet | ssh | ftp | reboot | read | write | policy | test | winbox | password | web | sniff | sensitive | api | rest-api | romon; Default:none) | List of allowed policies:Login policies:local - policy that grants rights to log in locally via consoletelnet - policy that grants rights to log in remotely via telnetssh - policy that grants rights to log in remotely via secure shell protocolweb - policy that grants rights to log in remotely via WebFig.winbox - policy that grants rights to log in remotely via WinBox and bandwidth test authenticationpassword - policy that grants rights to change the passwordapi - grants rights to access router via API.rest-api - grants rights to access the router via REST API.ftp - policy that grants full rights to log in remotely via FTP.  Allows to read/write/erase files and to transfer files from/to the router. Should be used together with read/write policies.romon - policy that grants rights to connect to the RoMon server.Config Policies:reboot - policy that allows rebooting the routerread - policy that grants read access to the router's configuration. All console commands that do not alter the router's configuration are allowed. Doesn't affect FTPwrite - policy that grants write access to the router's configuration, except for user management. This policy does not allow to read the configuration, so make sure to enable read policy as wellpolicy - policy that grants user management rights. Should be used together with the write policy. Allows also to see global variables created by other users (requires also 'test' policy). Allows to designskins(requires also "sensitive" policy).test - policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper, fetch, email and other test commandssensitive - grants rights to change "hide sensitive" option, if this policy is disabled sensitive information is not displayed.sniff - policy that grants rights to use packet sniffer tool, traffic generator.
skin(name; Default:default) | Used skin for WebFig
Login policies:
* local - policy that grants rights to log in locally via console
* telnet - policy that grants rights to log in remotely via telnet
* ssh - policy that grants rights to log in remotely via secure shell protocol
* web - policy that grants rights to log in remotely via WebFig.
* winbox - policy that grants rights to log in remotely via WinBox and bandwidth test authentication
* password - policy that grants rights to change the password
* api - grants rights to access router via API.
* rest-api - grants rights to access the router via REST API.
* ftp - policy that grants full rights to log in remotely via FTP.  Allows to read/write/erase files and to transfer files from/to the router. Should be used together with read/write policies.
* romon - policy that grants rights to connect to the RoMon server.
Config Policies:
* reboot - policy that allows rebooting the router
* read - policy that grants read access to the router's configuration. All console commands that do not alter the router's configuration are allowed. Doesn't affect FTP
* write - policy that grants write access to the router's configuration, except for user management. This policy does not allow to read the configuration, so make sure to enable read policy as well
* policy - policy that grants user management rights. Should be used together with the write policy. Allows also to see global variables created by other users (requires also 'test' policy). Allows to designskins(requires also "sensitive" policy).
* test - policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper, fetch, email and other test commands
* sensitive - grants rights to change "hide sensitive" option, if this policy is disabled sensitive information is not displayed.
* sniff - policy that grants rights to use packet sniffer tool, traffic generator.
## Default groups
There are three default system groups which cannot be deleted:
```
[admin@MikroTik] > /user group print 
0 name="read" policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default 
1 name="write" policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!policy skin=default 
2 name="full" policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,web,sniff,sensitive,api,romon,rest-api skin=default
```
Please note, that even the "read" group includessensitive,reboot,and other important policies, meaning that this group should not be given to untrusted users. For truly limited groups, make a custom group, defining specific policies. All groups have access to file operations. Exclamation sign '!' just before the policy item name means NOT.
# Router Users
The router user database stores information such as username, password, allowed access addresses, and group about router management personnel.
## Properties
Property | Description
----------------------
address(IP/mask | IPv6 prefix; Default: ) | Host or network address from which the user is allowed to log in
group(string; Default: ) | Name of the group the user belongs to
inactivity-policy(lockscreen|logout|none; Default:none) | Specifies inactivity action - logout (user will be logged out) or lockscreen (session will be locked, require password input to continue). Works only for CLI sessions.
inactivity-timeout(time; Default:10min) | Specifies time after which user will be logged out or session will be locked. Minimal timeout - 1 minute, maximal timeout - 24 hours. Works only for CLI sessions.
name(string; Default: ) | User name. Must start and end with an alphanumeric character but can include "_", ".", "#", "-", and "@" symbols. However the "*" symbol is prohibited in the user name.
password(string; Default: ) | User password. If not specified, it is left blank (hit [Enter] when logging in). It conforms to standard Unix characteristics of passwords and may contain letters, digits, "*" and "_" symbols.
last-logged-in(time and date; Default:"") | Read-only field. Last time and date when a user logged in.
## Actions
Actions for existing router user.
Action | Description
--------------------
password | Option to change user password.
expire-password | Expires user password, on next login, router will prompt to change password.
## Notes
There is one predefined user with full access rights:
```
[admin@MikroTik] user> print
Flags: X - disabled
# NAME GROUP ADDRESS LAST-LOGGED-IN
0 ;;; system default user
admin full 0.0.0.0/0 dec/08/2010 16:19:24
```
There always should be at least one user with full access rights. If the user with full access rights is the only one, it cannot be removed.
# Monitoring Active Users
```
/user active print
```
The command shows the currently active users along with respective statistics information.
## Properties
All properties are read-only.
Property | Description
----------------------
address(IP/IPv6 address/MAC address) | Host IP/IPv6/MAC address from which the user is accessing the router.
group(string) | A group that the user belongs to.
name(string) | Username.
radius(true | false) | Whether a user is authenticated by the RADIUS server.
via(telnet | ssh | winbox | api | rest-api | web | ftp) | User's access method
by-romon(MAC address) | RoMON agent MAC address
when(time) | Time and date when the user logged in.
## Request logout
It is possible to close an active CLI session using the request logout function.
```
/user/active/request-logout ACTIVE_USER_SESSION_NUMBER
```
# Remote AAA
Router user remote AAA enables router user authentication and accounting via a RADIUS server. The RADIUS user database is consulted only if the required username is not found in the local user database.
## Properties
Property | Description
----------------------
accounting(yes | no; Default:yes) | If the RADIUS server should be sent accounting of login, logout. Bandwidth usage statistics are not part of/useraccounting
exclude-groups(list of group names; Default: ) | Exclude-groups consist of the groups that should not be allowed to be used for users authenticated by radius. If the radius server provides a group specified in this list, the default-group will be used instead.This is to protect against privilege escalation when one user (without policy permission) can change the radius server list, set up its own radius server andlog in as admin.
default-group(string; Default:read) | User group used by default for users authenticated via a RADIUS server.
interim-update(time; Default:0s) | Interim-Update time interval
use-radius(yes |no; Default:no) | Enable user authentication via RADIUS
```
/user
```
This is to protect against privilege escalation when one user (without policy permission) can change the radius server list, set up its own radius server and
# SSH Keys
This menu allows importing of private and public keys used for SSH authentication.
## Public keys
This menu is used to import and list imported public keys. Public keys are used to approve another device's identity when logging into a router using an SSH key.
On public key import, is it possible to specify key-owner.
Property | Description
----------------------
user(string; Default: ) | username to which the SSH key is assigned.
key-owner(string) | SSH key owner
public-key-file(string) | file name in the router's root directory containing the public key.
key-type(read-only) | key type
bits(read-only) | key length
## Private keys
This menu is used to import and list imported private keys. Private keys are used to approve the router's identity during login into another device using an SSH key.
On private key import, is it possible to specify key-owner.
Property | Description
----------------------
user(string; Default: ) | username to which the SSH key is assigned.
key-owner(string) | SSH key owner
private-key-file(string) | file name in the router's root directory containing the private key.
passphrase(string) | key file passphrase
key-type(read-only) | key type
bits(read-only) | key length