# Document Information
Title: SMB
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/117145608/SMB,

# Content
# Summary
Sub-menu:/ip smbPackages required:system
```
/ip smb
```
```
system
```
SMB server provides file sharing access to configured folders of the router.
# Server settings
Property | Description
----------------------
comment(string; Default:MikrotikSMB) | Set comment for the server
domain(string; Default:MSHOME) | Name of Windows Workgroup
enabled(yes | no | autoDefault:auto) | The default value is 'auto.' This means that the SMB server will automatically be enabled when the first non-disabled SMB share is configured under '/ip smb share'
interface(string; Default:all) | List of interfaces on which SMB service will be running. all - SMB will be available on all interfaces.
# Share settings
Sub-menu:/ip smb shares
```
/ip smb shares
```
Allows configuring share names and directories that will be accessible by SMB.
If the directory provided in the configuration does not exist it will be created automatically.
Property | Description
----------------------
comment(string; Default:default share) | Set a comment for the share
disabled(yes | no; Default:no) | If disabled, the share will not be accessible.
valid-users(list ofstrings; | Default:) | Specifies which users are allowed to access the Samba share. If it is left empty, all users will be able to access the share, once user or users are defined here, only they will be able to access the share
invalid-users(list ofstrings; | Default: ) | Used to specify users who are explicitly denied access to the Samba share.
require-encryption(yes|no; Default:no) | Enforces the use of encryption for all connections to a particular Samba share
name(string; Default: ) | Name of the SMB share
directory(string; Default: ) | Directory on router assigned to SMB share. If left empty value of thenameargument will be used from the root folder.
valid-users(list ofstrings; | Default:)
invalid-users(list ofstrings; | Default: )
require-encryption(yes|no; Default:no)
# User setup
Sub-menu:/ip smb user
```
/ip smb user
```
Set up users that can access SMB shares of the router.
Property | Description
----------------------
comment(string; Default: ) | Set a description for the user
disabled(yes | no; Default:no) | Defines whether the user is enabled or disabled
name(string; Default: ) | Login name of the SMB service user
password(string; Default: ) | Password for SMB user to connect to SMB service
read-only(yes | no; Default:yes) | Sets if the user has only read-only rights when accessing shares or full access rights.
# Example
To make RouterOS folder available through SMB service follow these steps:
```
/ip/smb/users/add read-only=no name=mtuser password=mtpasswd
```
```
/ip/smb/shares/add directory=backup name=backup
```
```
# this step is optional, as the default is "enabled=auto"
/ip/smb/set enabled=yes
```
Now check for results:
```
/ip/smb/print
enabled: yes
domain: MSHOME
comment: MikrotikSMB
interfaces: all
```
```
/ip smb/users/print
Flags: X - DISABLED; * - DEFAULT; r - READ-ONLY
Columns: NAME, PASSWORD
# NAME    PASSWORD
0 X*r guest
1     mtuser  mtpasswd
```
```
/ip/smb/shares/print
Flags: X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION
# NAME    DIRECTORY  REQUIRE-ENCRYPTION
;;; default share
0 X* pub     /pub       no
1    backup  backup     no
```
Now, additional configuration changes can be done, like disabling the default user and share, etc.