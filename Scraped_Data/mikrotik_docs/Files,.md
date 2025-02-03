---
title: Files
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/2555971/Files,
crawled_date: 2025-02-02T21:12:41.583339
section: mikrotik_docs
type: documentation
---

# 2Overview3Create new file or directory3.1Properties4Properties5Get file contents5.1Properties
* 2Overview
* 3Create new file or directory3.1Properties
* 4Properties
* 5Get file contents5.1Properties
* 3.1Properties
* 5.1Properties
# Overview
File menu shows all user space files on the router. It is possible to create a new file, directory, edit file content, delete file or directory.  If RouterOS ".npk" package is uploaded, the file menu will also show package-specific information, for example, architecture, build date and time, etc.
```
[admin@MikroTik] > file print detail 
 0 name=wireless-7.16.1-arm.npk type=package size=1924.1KiB last-modified=2024-11-25 13:14:28 package-name="wireless" package-version="7.16.1" package-build-time=2024-10-10 14:03:32 
   package-architecture="arm" 
 1 name=routeros-7.16.1-arm.npk type=package size=11.1MiB last-modified=2024-11-25 13:14:34 package-name="system" package-version="7.16.1" package-build-time=2024-10-10 14:03:32 
   package-architecture="arm" 
 2 name=flash type=disk last-modified=2024-11-25 13:12:10 
 3 name=flash/skins type=directory last-modified=2024-11-25 13:10:52 
 4 name=flash/skins/newskin.json type=.json file size=0 last-modified=2024-11-25 13:10:52 
 5 name=flash/filename type=file size=0 last-modified=2024-11-25 13:11:58 
 6 name=flash/directory_name type=directory last-modified=2024-11-25 13:12:10
```
# Create new file or directory
To create a new file or directory:
```
[admin@MikroTik] > file add name=/flash/filename type=file           
[admin@MikroTik] > file add name=/flash/directory_name type=directory
```
## Properties
Property | Description
----------------------
contents(string; Default: ) | File contents that must be added. Works only fortype=file
name(string; Default: ) | File/directory name
type(file | directory;Default:file) | Specifies type
# Properties
Property | Description
----------------------
contents(string; Default: ) | The actual content of the file
creation-time(time) | A time when the file was created
last-modified(time) | The time when the file was created or last modified. Introduced instead ofcreation-timein RouterOS 7.16.
name(string) | Name of the file
package-architecture(string) | Architecture that package is built for. Applies only to RouterOS ".npk" files
package-built-time(string) | A time when the package was built. Applies only to RouterOS ".npk" files
package-name(string) | Name of the installable package that. Applies only to RouterOS ".npk" files
package-version(string) | A version of the installable package that. Applies only to RouterOS ".npk" files
size(integer) | File size in bytes
type(string) | Type of the file. For folders, the file type is thedirectory
creation-time(time)
A time when the file was created
last-modified(time)
The time when the file was created or last modified. Introduced instead ofcreation-timein RouterOS 7.16.
# Get file contents
Using thegetcommand, it is possible to retrieve file contents only from files up to 60KB in size. For accessing contents of larger files, use commandread. The result is returned as an array.
For example:
```
[admin@MikroTik] > :put [/file/get text.txt contents]
123456
[admin@MikroTik] > /file/read file=text.txt offset=2 chunk-size=3    
  data: 345
```
## Properties
Property | Description
----------------------
chunk-size(integer [1..32768]; Default: ) | Chunk size that will be read from file
file(string; Default: ) | File name from which to read
offset(integer;Default:) | Specifies offset where to start read file