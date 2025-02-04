# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211177

# Discussion

## Initial Question
Author: Tue Sep 24, 2024 6:12 pm
``` SCRIPT_VERSION=1.2.1 REQ_ID=01J8C5ZV2AY6V6HWEB6F4HQJW5 REQ_IP=172.21.104.34 REQ_FAMILY=1 REQ_CREATED=2024-09-22 06:16:32 ``` Hello scripting gurus. Please advise how to assign data from text file to the variables.I have a next file with content:
```
how to set variable value for $reqid to be a 01J8C5ZV2AY6V6HWEB6F4HQJW5, for $reqip = 172.21.104.34.Original script is posted herehttps://git.dn42.dev/dn42/pingfinder/sr ... tik.scriptbut very very outdated and doesn't work with latest ROS 6 & 7.Or maybe someone have a lot of vacant time to redo this script for the latest versions of ROS.Thank you in advance!


---
```

## Response 1
Author: [SOLVED]Tue Sep 24, 2024 8:04 pm
``` { :local kvtxt "SCRIPT_VERSION=1.2.1\r\nREQ_ID=01J8C5ZV2AY6V6HWEB6F4HQJW5\r\nREQ_IP=172.21.104.34\r\nREQ_FAMILY=1\r\nREQ_CREATED=2024-09-22 06:16:32" # now use :deserialize to get an RouterOS array from file txt :local kvarray [:deserialize delimiter=("=") from=dsv options=dsv.plain [:tocrlf $kvtxt]] # yes, it's an array :put [:typeof $kvarray] :put $kvarray # to better see what got parsed, :serialize's "pretty json" provides a nice output of the array: :put [:serialize to=json options=json.pretty $kvarray] # and can use scripting to find the values using ->0 for the key, and ->1 to get to useful form: :local myconfig [:toarray ""] :foreach v in=$kvarray do={ :set ($myconfig->($v->0)) ($v->1) } :put $myconfig :put ($myconfig->"SCRIPT_VERSION") } ``` ``` { # change file name with above format :local kvfilename "kvfile" # process the file into an array using :deserialize :local kvtxt [/file get $kvfilename contents] :local kvarray [:deserialize delimiter=("=") from=dsv options=dsv.plain [:tocrlf $kvtxt]] :local myconfig [:toarray ""] # this "pivots" the array-of-tuples returned from deserialize...into a normal key-value array :foreach v in=$kvarray do={ :set ($myconfig->($v->0)) ($v->1) } # to use then it's just :put ($myconfig->"SCRIPT_VERSION") :put ($myconfig->"REQ_ID") :put ($myconfig->"REQ_IP") :put ($myconfig->"REQ_FAMILY") :put ($myconfig->"REQ_CREATED") } ``` In 7.15+, you should be able to use the new [:deserialize from=dsv]. So for quick example...
```
arraySCRIPT_VERSION;1.2.1;REQ_ID;01J8C5ZV2AY6V6HWEB6F4HQJW5;REQ_IP;172.21.104.34;REQ_FAMILY;1;REQ_CREATED;2024-09-22 06:16:32[["SCRIPT_VERSION","1.2.1"],["REQ_ID","01J8C5ZV2AY6V6HWEB6F4HQJW5"],["REQ_IP","172.21.104.34"],["REQ_FAMILY",1],["REQ_CREATED","2024-09-22 06:16:32"]]REQ_CREATED=2024-09-22 06:16:32;REQ_FAMILY=1;REQ_ID=01J8C5ZV2AY6V6HWEB6F4HQJW5;REQ_IP=172.21.104.34;SCRIPT_VERSION=1.2.11.2.1Without showing what happening, the above could be simplified change the "kvfilename" as needed:example code1.2.101J8C5ZV2AY6V6HWEB6F4HQJW5172.21.104.3412024-09-22 06:16:32The array stuff is confusing at first but :deserialize does "half of the parsing", the array are easier "flip" than parsing using :pick and :find.  Now tt be better if  ' from=dsv options=...' had option to deal with tuples like your key=value\n... case - to avoid the :foreach above.https://help.mikrotik.com/docs/display/ROS/Scriptinghas the docs on :serialize and :deserialize stuff.There is a video from Mikrotik on working with arrays:https://www.youtube.com/watch?v=eWCJw0uZ-lE


---
```

## Response 2
Author: Wed Sep 25, 2024 3:50 pm
``` :global myconfig [:deserialize from=json [/file get $myjson contents]] ``` FWIW, if you can control the format of the file with variables... you may want to consider using JSON in the file...as that be one operation with the new deserialize:
```
But your original data have to be JSON:{"SCRIPT_VERSION": "1.2.1","REQ_ID": "01J8C5ZV2AY6V6HWEB6F4HQJW5","REQ_IP": "172.21.104.34","REQ_FAMILY": 1,"REQ_CREATED": "2024-09-22 06:16:32"}Maybe not possible, but for storing/reading variables from disk, JSON is likely a better format since it deals with types/escaping/unicode/etc.
```