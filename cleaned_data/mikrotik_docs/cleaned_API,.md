# Document Information
Title: API
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API,

# Content
# Summary
Application Programmable Interface (API) allows users to create custom software solutions to communicate with RouterOS to gather information, adjust the configuration, and manage the router. API closely follows syntax from the command-line interface (CLI). It can be used to create translated or custom configuration tools to aid ease of use in running and managing routers with RouterOS.
API service must be enabled before trying to establish the API connection. By default, API uses TCP:8728and TCP:8729(secure).
API-SSL service is capable of working in two modes - with and without a certificate. In the case no certificate is used in/ip servicesettings then an anonymous Diffie-Hellman cipher has to be used to establish a connection. If a certificate is in use, a TLS session can be established.
# Protocol
Communication with the router is done by sending sentences and receiving one or more sentences in return. A sentence is a sequence of words terminated by zero-length words. Word is part of a sentence encoded in a certain way - encoded length and data. Communication happens by sending sentences to the router and receiving replies to sent sentences. Each sentence sent to the router using API should contain a command as a first word followed by words in no particular order, the end of the sentence is marked by a zero-length word. When the router receives a full sentence (command word, no or more attribute words, and zero-length word) it is evaluated and executed, then a reply is formed and returned.
# API words
Words are part of a sentence. Each word has to be encoded in a certain way - the length of the word followed by the word content. The length of the word should be given as a count of bytes that are going to be sent.
The length of the word is encoded as follows:
Value of length | # of bytes | Encoding
---------------------------------------
0 <= len <= 0x7F | 1 | len, lowest byte
0x80 <= len <= 0x3FFF | 2 | len | 0x8000, two lower bytes
0x4000 <= len <= 0x1FFFFF | 3 | len | 0xC00000, three lower bytes
0x200000 <= len <= 0xFFFFFFF | 4 | len | 0xE0000000
len >= 0x10000000 | 5 | 0xF0 and len as four bytes
In general,wordscan be described like this <<encoded word length><word content>>.Word contentcan be separated into 5 parts:command word,attribute word,API attribute word.query word,andreply word
# Command word
The first word in the sentence has to be a command followed by attribute words and a zero-length word or terminating word. The name of the command word should begin with '/'. Names of commands closely follow CLI, with spaces replaced with '/'. Some commands are specific to API;
Command word structure in the strict order:
API-specific commands:
```
login
cancel
```
Command word content examples:
```
/login
```
```
/user/active/listen
```
```
/interface/vlan/remove
```
```
/system/reboot
```
# Attribute word
Eachcommand wordhas its list ofattribute wordsdepending on content.
Attribute wordstructure consists of 5 parts in this order:
Examples without encoded length prefix:
```
=address=10.0.0.1
```
```
=name=iu=c3Eeg
```
```
=disable-running-check=yes
```
# API attribute word
API attribute word structure is in the strict order:
Currently, the only such API attribute is thetag.
# Query word
Sentences can have additional query parameters that restrict their scope. A detailed explanation is in thequery section.
Example of a sentence using query word attributes:
```
/interface/print
?type=ether
?type=vlan
?# |!
```
# Reply word
It is only sent by the router in response to the full sentence received from the client.
# API sentences
API sentence is the main object of communication using API.
# Initial login
Note:that each command and response ends with an empty word.
Login method post-v6.43:
/login
=name=admin
=password=
!done
# Tags
# Command description
# Queries
Theprintcommand accepts query words that limit the set of returned sentences.
Query | Description
-------------------
?name | pushes 'true' if an item has a value of propertyname, 'false' if it does not.
?-name | pushes 'true' if an item does not have a value of propertyname, 'false' otherwise.
?name=x?=name=x | pushes 'true' if the propertynamehas a value equal tox, 'false' otherwise.
?<name=x | pushes 'true' if the propertynamehas a value less thanx, 'false' otherwise.
?>name=x | pushes 'true' if the propertynamehas a value greater thanx, 'false' otherwise.
?# operations | applies operations to the values in the stack.operation string is evaluated from left to right.the sequence of decimal digits followed by any other character or end of the word is interpreted as a stack index. top value has an index 0.an index that is followed by a character pushes a copy of the value at that index.an index that is followed by the end of the word replaces all values with the value at that index.!character replaces the top value with the opposite.&pops two values and pushes the result of logical 'and' operation.|pops two values and pushes the result of logical 'or' operation..after an index does nothing..after another character pushes a copy of the top value.
Examples:
```
/interface/print
?type=ether
?type=vlan
?# |
```
```
/ip/route/print
?>comment=
```
# OID
Theprintcommand can return OID values for properties that are available in SNMP.
In the console, OID values can be seen by running the 'print oid' command. In API, these properties have a name that ends with ".oid", and can be retrieved by adding their name to the value of '.proplist'. An example:
/system/resource/print
=.proplist=uptime,cpu-load,uptime.oid,cpu-load.oid
!re
=uptime=01:22:53
=cpu-load=0
=uptime.oid=.1.3.6.1.2.1.1.3.0
=cpu-load.oid=.1.3.6.1.2.1.25.3.3.1.2.1
!done
# !trap
When for some reason API sentence fails trap is sent in return accompanied by amessageattribute and on some occasionscategoryargument.
# message
When an API sentence fails, some generic message or message from the used internal process is returned to give more details about the failure
```
<<< /ip/address/add
<<< =address=192.168.88.1
<<< =interface=asdf <<<
>>> !trap
>>> =category=1
>>> =message=input does not match any value of interface
```
# category
if it is a general error, it is categorized and the error category is returned. possible values for this attribute are
# Command examples
# /system/package/getall
/system/package/getall
!re
=.id=*5802
=disabled=no
=name=routeros-x86
=version=3.0beta2
=build-time=oct/18/2006 16:24:41
=scheduled=
!re
=.id=*5805
=disabled=no
=name=system
=version=3.0beta2
=build-time=oct/18/2006 17:20:46
=scheduled=
... more !re sentences ...
!re
=.id=*5902
=disabled=no
=name=advanced-tools
=version=3.0beta2
=build-time=oct/18/2006 17:20:49
=scheduled=
!done
# /user/active/listen
/user/active/listen
!re
=.id=*68
=radius=no
=when=oct/24/2006 08:40:42
=name=admin
=address=0.0.0.0
=via=console
!re
=.id=*68
=.dead=yes
... more !re sentences ...
# /cancel, simultaneous commands
/login
!done
=ret=856780b7411eefd3abadee2058c149a3
/login
=name=admin
=response=005062f7a5ef124d34675bf3e81f56c556
!done
--first start listening for interface changes (tag is 2)
/interface/listen
.tag=2
--disable interface (tag is 3)
/interface/set
=disabled=yes
=.id=ether1
.tag=3
--this is done for disable command (tag 3)
!done
.tag=3
--enable interface (tag is 4)
/interface/set
=disabled=no
=.id=ether1
.tag=4
--this update is generated by a change made by the first set command (tag 3)
!re
=.id=*1
=disabled=yes
=dynamic=no
=running=no
=name=ether1
=mtu=1500
=type=ether
.tag=2
--this is done for enable command (tag 4)
!done
.tag=4
--get interface list (tag is 5)
/interface/getall
.tag=5
--this update is generated by a change made by the second set command (tag 4)
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=2
--these are replies to getall command (tag 5)
!re
=.id=*1
=disabled=no
=dynamic=no
=running=yes
=name=ether1
=mtu=1500
=type=ether
.tag=5
!re
=.id=*2
=disabled=no
=dynamic=no
=running=yes
=name=ether2
=mtu=1500
=type=ether
.tag=5
--here interface getall ends (tag 5)
!done
.tag=5
--stop listening - request to cancel command with tag 2, cancel itself uses tag 7
/cancel
=tag=2
.tag=7
--listen command is interrupted (tag 2)
!trap
=category=2
=message=interrupted
.tag=2
--cancel command is finished (tag 7)
!done
.tag=7
--listen command is finished (tag 2)
!done
.tag=2
# Example client
A simpleAPI client in Python3
Example output:
```
debian@localhost:~/api-test$ ./api.py 10.0.0.1 admin ''
<<< /login
<<<
>>> !done
>>> =ret=93b438ec9b80057c06dd9fe67d56aa9a
>>>
<<< /login
<<< =name=admin
<<< =response=00e134102a9d330dd7b1849fedfea3cb57
<<<
>>> !done
>>>
/user/getall
<<< /user/getall
<<<
>>> !re
>>> =.id=*1
>>> =disabled=no
>>> =name=admin
>>> =group=full
>>> =address=0.0.0.0/0
>>> =netmask=0.0.0.0
>>>
>>> !done
>>>
```
# See also
# API examples
API implementations in different languages, provided by different sources. They are not ordered in any particular order.
* in C++17by Ayman Al-Qadhi