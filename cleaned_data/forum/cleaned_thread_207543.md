# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207543

# Discussion

## Initial Question
Author: Sat May 11, 2024 2:57 pm
``` 13:26:47script, infoContainerupdate:ContainerHomeAssistantupdate started13:26:47script, warningContainerupdate:ContainerHomeAssistantisrunning, stopping container13:26:58system, info, account user h1ghrise loggedoutfrom10.10.20.2via api ``` ``` 13:49:38script, infoContainerupdate:ContainerHomeAssistantupdate started13:49:38script, warningContainerupdate:ContainerHomeAssistantisrunning, stopping container13:49:44system, info, account user h1ghrise loggedoutfrom10.10.20.2via api13:49:49script, infoContainerupdate:ContainerHomeAssistantstopped13:49:49container, info, debug removing files, container f934a903-152d-4bdc-a04f-944b8e15a442... ``` ``` :if($contStatus!="stopped")do={:if($contStatus="running")do={:log warn"$($logPrefix)Container $contComment is running, stopping container":setcontStartedtruestop $contId}:localstopTimeoutSec120:localsec0:while(([get$contId]->"status")!="stopped"&&$sec<=$stopTimeoutSec)do={:delay1:setsec($sec+1)}:if($sec>$stopTimeoutSec)do={$abortWithMessage("container $contComment stop timed out, aborting")logPrefix=$logPrefix}:log info"$($logPrefix)Container $contComment stopped"} ``` Hi Mikrotik Community.im using the Community Script to update Containers from this post (viewtopic.php?p=1053882&hilit=container ... t#p1053882) to update my Home Assistant instance.This works really well, when executed on the Mikrotik (RB5009) itself.In Home Assistant, I built an automation, which utilizes the Mikrotik API to trigger the script.Unfortunately when trigged via API, the Script behaves differently:Triggered via API:
```
Do scripts get executes differently, when triggered via API? I cannot reproduce this behavior.No further entries. The Container is stopped, and nothing happens.Triggered on the Mikrotik directly:
```

```
the corresponding code in the script:
```

```
---
```

## Response 1
Author: Sat May 11, 2024 5:03 pm
``` :globalGcontainerUpdatedo={# After ROS upgrade check below if something has changed# ------------------------------------------------------# validAddArgs - array of container add command argument names which are named exact as config property names:localvalidAddArgs("cmd","comment","dns","domain-name","entrypoint","envlist","hostname","interface","logging","mounts","root-dir","start-on-boot","workdir")# replaceArgs - key-value array for mapping container add command argument name from different config property name,# where key is config property name and value is argument name:localreplaceArgs{"tag"="remote-image"}# addCmd - ROS CLI container add command:localaddCmd"/container add"# ------------------------------------------------------# stopTimeoutSec - container stop wait timeout in seconds:localstopTimeoutSec120# extrTimeoutSec - container download/extract wait timeout in seconds, rise if not enough (1800 = 30min) on slow network or device:localextrTimeoutSec1800# logPrefix - script log record prefix:locallogPrefix"Container update: ":localabortWithMessagedo={:log error"$($logPrefix)Error - $1":error $1}:locallogWithMessagedo={:if($level="W")do={:log warn"$logPrefix$1"}else={:log info"$logPrefix$1"}:put"[$level] $1"}:localcontComment $1/container:localcontId[findwherecomment=$contComment]:if($contId="")do={$abortWithMessage("container $contComment not found, aborting")logPrefix=$logPrefix}:localcontStatus([get$contId]->"status"):if($contStatus="extracting")do={$abortWithMessage("container $contComment is extracting, aborting")logPrefix=$logPrefix}$logWithMessage("Container $contComment update started")logPrefix=$logPrefix level="I":localcontStartedfalse:if($contStatus!="stopped")do={:if($contStatus="running")do={$logWithMessage("Container $contComment is running, stopping container")logPrefix=$logPrefix level="W":setcontStartedtruestop $contIdas-value}:localsec0:while(([get$contId]->"status")!="stopped"&&$sec<=$stopTimeoutSec)do={:delay1:setsec($sec+1)}:if($sec>$stopTimeoutSec)do={$abortWithMessage("container $contComment stop timed out, aborting")logPrefix=$logPrefix}$logWithMessage("Container $contComment stopped")logPrefix=$logPrefix level="W"}$logWithMessage("Removing old and adding new container $contComment")logPrefix=$logPrefix level="I":localcont[get$contId]remove$contId:delay5:localescapeStrdo={:localstrLen[:len $1]:localescStr"":forifrom=0to=($strLen-1)do={:localchr[:pick $1 $i($i+1)]:if($chr="\$")do={:setescStr"$escStr\\\$"}else={:if($chr="\\")do={:setescStr"$escStr\\\\"}else={:if($chr="\"")do={:setescStr"$escStr\\\""}else={:setescStr"$escStr$chr"}}}}:return"\"$escStr\""}:localarrayToStrdo={:localarrLen[:len $1]:localstrArr"(":forifrom=0to=($arrLen-1)do={:localitem[:pick $1 $i]:if([:len $strArr]>1)do={:set$strArr"$strArr,"}:if([:typeof$item]="str")do={:set$strArr"$strArr$([$escapeStr $item])"}else={:set$strArr"$strArr$item"}}:return"$strArr)"}:localescapeValuedo={:if([:typeof$1]="str")do={:return[$escapeStr $1]}:if([:typeof$1]="array")do={:return[$arrayToStr $1 escapeStr=$escapeStr]}:if([:typeof$1]="bool")do={:if($1)do={:return"yes"}else={:return"no"}}:return$1}:foreachk, vin=$contdo={:if([:len $v]!=0)do={:if([:find $validAddArgs $k]>=0)do={:setaddCmd"$addCmd $k=$([$escapeValue $v convertBool=$convertBool escapeStr=$escapeStr arrayToStr=$arrayToStr])"}else={:localrk($replaceArgs->"$k"):if([:typeof$rk]!="nothing")do={:setaddCmd"$addCmd $rk=$([$escapeValue $v escapeStr=$escapeStr arrayToStr=$arrayToStr])"}}}}:execute"$addCmd"as-string:setcontId[findwherecomment=$contComment]:if($contId="")do={$abortWithMessage("unable to add container $contComment, check add command: $addCmd")logPrefix=$logPrefix}:localsec0:while(([get$contId]->"status")="extracting"&&$sec<=$extrTimeoutSec)do={:delay1:setsec($sec+1)}:if($sec>$extrTimeoutSec)do={$abortWithMessage("container $contComment extract wait timed out, something is failed or slower than expected")logPrefix=$logPrefix}:if($contStarted)do={$logWithMessage("Starting container $contComment")logPrefix=$logPrefix level="I"start $contIdas-value}$logWithMessage("Container $contComment update finished")logPrefix=$logPrefix level="I"} ``` Glad that you find it useful, I did additionally some small changes to print out messages in terminal, not just in log and moved config vars on top for convenience, but core of script logic remains as in linked topic from OP, here is my latest ver:
```
Regarding issue, could be some permissions, can you manually create and run container over API and just with script is failing?If is not permissions issue, could be issue with payload serialization and escaping, try to log$addCmdvar before:executecommand (:log info $addCmd) and see if is different for same container configuration when executed from terminal and over API.For further troubleshooting help specify if is this related tolegacy APIorREST API.


---
```

## Response 2
Author: Sat May 11, 2024 6:51 pm
Assuming you're using REST or "native API" to run /system/script with update code, might be easy to try setting "Don't Check Permissions" on that script to see if it works then. And/or make sure the script owner is same as the user you're using to login with REST/API. ---

## Response 3
Author: Sat May 11, 2024 9:15 pm
``` :localcontComment"CommentToIdentifyContainer" ``` ``` :localcontComment $1 ``` Thanks both of you for your hints and feedback.First, thanks for the updated version. In the OP, the $contComment was supplied in the script itself:
```
Now its supplied with an argument?
```

```
Call me stupid, but where do i supply that?For the issue related part: I checked the permissions, and the script has not set the "don't require permissions" flag set. I set it and tried again withe the original script. Did not change anything.Also the user triggering the API call is the same who created the script.In general, Im using the regular API via an HACS Plugin:https://github.com/tomaae/homeassistant-mikrotik_router(using master branch, as default version in HACS does not work with 7.12+)


---
```

## Response 4
Author: Sat May 11, 2024 9:42 pm
``` :localcontComment"CommentToIdentifyContainer" ``` ``` :localcontComment $1 ``` ``` >/system/script/run<container_update_script_name>>$GcontainerUpdate"<some container1 comment>">$GcontainerUpdate"<some container2 comment>"... ``` 
```
Now its supplied with an argument?
```

```
Call me stupid, but where do i supply that?That's also script change but forgot to mention, whole script code is added into global var as function which accepts container comment as argument ($1). It is more convenient when you need to update multiple containers, now there is no need to edit script to change container comment or have multiple same scripts for each container update, eg.:
```

```
Running this script can be also added to startup scheduler so that you will always have$GcontainerUpdateon disposal when needed since it is not needed to re-run script to add global var. again unless script code has changed (or this global var. deleted).But if you want to behave as prev. script, just delete first line ":global GcontainerUpdate do={", last line closing bracket "}" and replace$1with container comment forcontCommentvar. value as you have now.For the issue related part: I checked the permissions, and the script has not set the "don't require permissions" flag set. I set it and tried again withe the original script. Did not change anything.Try to log execute string from$addCmdvariable as mentioned in prev. post and post both when is success from terminal and when is not from API. If are the same could be some issue with:executecommand executed over API then...P.S.As I see in this codehttps://github.com/tomaae/homeassistant ... pi.py#L312it just runs already created script on ROS, then it shouldn't be issue with script content, like escaping (I initially assumed that script is sent from remote over API), I guess this is related to some user restrictions or bug in ROS.


---
```

## Response 5
Author: Sat May 11, 2024 10:02 pm
``` :while(([get$contId]->"status")!="stopped"&&$sec<=$stopTimeoutSec)do={:delay1$logWithMessage("Container $contComment is still running, retrying...")logPrefix=$logPrefix level="W":setsec($sec+1)} ``` ``` 20:56:50script, infoContainerupdate:ContainerHomeAssistantupdate started20:56:50script, warningContainerupdate:ContainerHomeAssistantisrunning, stopping container20:56:51script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:52script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:53script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:54script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:55script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:56script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:57script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:58script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:56:59script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying...20:57:00script, warningContainerupdate:ContainerHomeAssistantisstill running, retrying... ``` ``` $logWithMessage("Removing old and adding new container $contComment")logPrefix=$logPrefix level="I" ``` Hi, thanks for your clarification. For now, I removed the function wrapper - I only want to update Home Assistant.Also, I have added some verbose logging, to pinpoint the issue:
```
It seems, that the part below the container stop check, never gets executed:
```

```
Log stops when container is stopped, but does not reach (?) the part, where it should log the removing of the old container:
```

```
---
```

## Response 6
Author: [SOLVED]Sat May 11, 2024 10:15 pm
``` :execute"/system/script/run <container-update-script-name>" ``` There is no either log "Container update: Container Container HomeAssistant stopped", (line:$logWithMessage ("Container $contComment stopped") logPrefix=$logPrefix level="W") which means can be timeouted by check in line above:if ($sec > $stopTimeoutSec) do={ $abortWithMessage ("container $contComment stop timed out, aborting") logPrefix=$logPrefix }but there is no error log "Container update: container Container Containerstop timed out, aborting" so I doubt that is the case, more likely script is terminated while was in wait loop for some reason.How long stopping this container takes?Maybe API connection is closed while script is running and ROS terminates script executed over API when closed, if that's the case try if this hack works - create additional script for executing over API which pefrforms script run async with:executecommand: