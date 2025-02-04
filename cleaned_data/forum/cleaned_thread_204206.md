# Thread Information
Title: Thread-204206
Section: RouterOS
Thread ID: 204206

# Discussion

## Initial Question
Hello, since 7.13, my fetch script returns this error when fetching a webpage: "failure: ERROR parsing http: there was no content-length or transfer-encoding"This fetch script calls a page from an ethernet relay board in the lan.The device (ref:https://www.kmtronic.com/lan-ethernet-i ... board.html):The routerOS code:
```
:put [/tool fetch url="http://192.168.1.199/FF0100" as-value output=user]The routerOS error returned:
```

```
failure: ERROR parsing http: there was no content-length or transfer-encodingThis behavior seems to have low visibility on the forums: looking around, I was only able to find one post from un9edsda here:viewtopic.php?p=1048176#p1048176It may be that the ethernet relay PCB doesn't revert a specific field, and I have no control over this, but until routerOS 7.13, this was not an issue: fetch seemed to be more flexible at accommodating this and returning the fetched content.I confirm that freshly released 7.13.4 still display this error message.What can be done to provide fetch the same level of flexibility it had until 7.12.1?Thank you

---
```

## Response 1
Issue should be fixed in latest 7.14 beta versions ---

## Response 2
fantastic news, many thanks Normis! ---

## Response 3
Hi Normis, I'm re-opening this:I just updated to 7.14, but the error persists, although the error message is slightly different
```
failure: there was no content-length or transfer-encodingIs there something I can provide you with in order to replicate?Thanks

---
```

## Response 4
i'm with ROS 14.3 stable branch and this error persists.I have a full range of scripts that push data to a prometheus pushgateway to audit quality of links and all of them just stop working on update.
```
"failure: there was no content-length or transfer-encoding"Is there any solution to this?Many thanks.

---
```

## Response 5
Also... i just realize that a sync script for an HA cluster just broke completly because of this.This is so bad... ---

## Response 6
Hi @brunolabozzetta! Since this is a user forum, it's probably better if you contact MikroTik directly via email at "support@mikrotik.com" or open a support ticket using the link "https://help.mikrotik.com/servicedesk/servicedesk." //BR, Larsa. ---

## Response 7
This error is already identified and was supposed to be fixed in 7.14But it’s still ongoing.Ideally MikroTik can provide an ETA on resolution ---

## Response 8
```
MikroTik RouterOS 7.16.1

/tool fetch mode=http url=http://192.168.0.1/ output=user-with-headers
status: failed

failure: there was no content-length or transfer-encodingSo the issue is still being there

---
```

## Response 9
Same here, v7.16.2 armis there any workaround? I've tried every possible setting without luck.Strangely, when I run the same /tool/fetch from a terminal, it works fine. It only doesn't work from the script ---

## Response 10
Hi, I have thoroughly investigated this error, and it is due to an incorrect response from the server.The header contains the Content-Type field but does NOT contain the Content-Length field, and this generates the error.If the server responds with the Content-Type field, it MUST also enter the Content-Length field.The combination are:Content-Type and Content-LengthORTransfer-Encoding and Content-LengthIt's a problem of the server side that is not compliant with HTTP 1.1.Header with error (don't works with fetch)header error.pngHeader correct with Content-Type (works with fetch)header ok.pngHeader correct with Transfer-Encoding (works with fetch)header ok transfer encoding.pngMarco ---

## Response 11
Same result as:viewtopic.php?p=1059616#p1059616 ---

## Response 12
Hello, since 7.13, my fetch script returns this error when fetching a webpage: "failure: ERROR parsing http: there was no content-length or transfer-encoding"This fetch script calls a page from an ethernet relay board in the lan.The device (ref:https://www.kmtronic.com/lan-ethernet-i ... board.html):The routerOS code:
```
:put [/tool fetch url="http://192.168.1.199/FF0100" as-value output=user]The routerOS error returned:
```

```
failure: ERROR parsing http: there was no content-length or transfer-encodingThis behavior seems to have low visibility on the forums: looking around, I was only able to find one post from un9edsda here:viewtopic.php?p=1048176#p1048176It may be that the ethernet relay PCB doesn't revert a specific field, and I have no control over this, but until routerOS 7.13, this was not an issue: fetch seemed to be more flexible at accommodating this and returning the fetched content.I confirm that freshly released 7.13.4 still display this error message.What can be done to provide fetch the same level of flexibility it had until 7.12.1?Thank youHi, I found a workaround executing an asyncronous fetch request inside the script by execute function:here the example of my script
```

```
[[execute "tool fetch url=\"http://server-ip:port/leds.cgi?led=0\" "]]
[[execute "tool fetch url=\"http://server-ip:port/leds.cgi?led=1\" "]]I wrote to MikroTik support to describe in details this questions.I hope that this solution fix your problem.Marco

---
```

## Response 13
I confirm this works fine, no idea what it does different in the background, but it is a perfect workaround.Thank you very much!BTW: I have also contacted Mikrotik support, they were very helpful and fixed it in the next release.I understand it it most likely a broken server, but it seems there are too many of them to ignore itlike self signed certsHi, I found a workaround executing an asyncronous fetch request inside the script by execute function:here the example of my script
```
[[execute "tool fetch url=\"http://server-ip:port/leds.cgi?led=0\" "]]
[[execute "tool fetch url=\"http://server-ip:port/leds.cgi?led=1\" "]]I wrote to MikroTik support to describe in details this questions.I hope that this solution fix your problem.Marco

---
```

## Response 14
here the example of my script
```
[[execute "tool fetch url=\"http://server-ip:port/leds.cgi?led=0\" "]]
[[execute "tool fetch url=\"http://server-ip:port/leds.cgi?led=1\" "]]I wrote to MikroTik support to describe in details this questions.I hope that this solution fix your problem.MarcoThank you Marco,But unfortunately, this still doesn't work for me:- the http server does register the fetch and flip the switch accordingly- but on Mikrotik side, I still can't parse the response, instead the same error message is thrownThe same behavior occured before this asynchronous scripting unfortunately.Both codes return the same error message - running RouterOS version 7.16.2:
```

```
:put [[execute "tool fetch url=\"http://192.168.1.199/FF0100\" as-value output=user-with-headers"]]
```

```
:put [/tool fetch url="http://192.168.1.199/FF0100" as-value output=user-with-headers]The error message:
```

```
failure: there was no content-length or transfer-encodingBTW: I have also contacted Mikrotik support, they were very helpful and fixed it in the next release.I understand it it most likely a broken server, but it seems there are too many of them to ignore itlike self signed certsHi timemaster,do you mean that we can expect a fix in the future ... or is the fix already published in a previous release?

---
```

## Response 15
do you mean that we can expect a fix in the future ... or is the fix already published in a previous release?It was a nightly build of the 7.18 version. I don't know what the next stable release is, but I expect the one that follows the current nightly build. ---

## Response 16
do you mean that we can expect a fix in the future ... or is the fix already published in a previous release?It was a nightly build of the 7.18 version. I don't know what the next stable release is, but I expect the one that follows the current nightly build.Thanks for the clarification.Would you happen to have a link to the changelog to expectat in 7.18?I can't find much as currently 7.17 is in release candidate, and nothing on 7.18 is mentionned here:https://mikrotik.com/download/changelogs ---

## Response 17
Would you happen to have a link to the changelog to expectat in 7.18?Nightly builds are alpha/developers' versions and nothing is guaranteed to enter to beta of same version. So there's never any changelog for nightly builds. We've seen stuff removed from beta versions (rarely, but it did happen) so I'd guess that would happen even more often with alpha versions.Nightly builds are sometimes (not often) offered to users which reported particular problem and devs managed to replicate and fix the problem ... and offering nightly build with fix is some kind of courtesy to those users. Since same nightly builds contain other development code, they may break something else, which means that even user who receives such build, should use it with extreme care. Consider all the problem reports with beta/rc versions ... and assume that alpha/nightly versions are almost certainly worse. ---

## Response 18
Would you happen to have a link to the changelog to expectat in 7.18?Nightly builds are alpha/developers' versions and nothing is guaranteed to enter to beta of same version. So there's never any changelog for nightly builds. We've seen stuff removed from beta versions (rarely, but it did happen) so I'd guess that would happen even more often with alpha versions.Got it, makes sense, Where do you got your source then that 7.18 would feature a fix for this issue? ---

## Response 19
Where do you got your source then that 7.18 would feature a fix for this issue?See my second paragraph (add while you were posting your latest post). ---

## Response 20
Where do you got your source then that 7.18 would feature a fix for this issue?See my second paragraph (add while you were posting your latest post).Thanks.Still not very clear on your source to callout 7.18 as likely to fix this bug.Have you been handed over a 7.18 nightly build amongst whose feature the aim was to fix this issue you also faced? ---

## Response 21
Have you been handed over a 7.18 nightly build amongst whose feature the aim was to fix this issue you also faced?No, @timemaster seems to have received it this time. And I know it happened before (although rarely). So you have nothing to worry, there are no 'exceptional' forum members which receive something you don't. MT said that betas are something that is in development but users (feeling like living on the edge) can download and use ... at their own discretion.We, long-time users, have feeling that "beta" in MT world is more like "alpha" for the rest ... and "RC" in MT world is like "beta" for other vendors ... and my own experience with other vendors is that they may release some beta as last software version for certain device (because that device is then EoL) ... and that beta fixes some bugs present in all previous software versions. So MT's continued support is something to be glad for. ---

## Response 22
Have you been handed over a 7.18 nightly build amongst whose feature the aim was to fix this issue you also faced?No, @timemaster seems to have received it this time. And I know it happened before (although rarely). So you have nothing to worry, there are no 'exceptional' forum members which receive something you don't. MT said that betas are something that is in development but users (feeling like living on the edge) can download and use ... at their own discretion.We, long-time users, have feeling that "beta" in MT world is more like "alpha" for the rest ... and "RC" in MT world is like "beta" for other vendors ... and my own experience with other vendors is that they may release some beta as last software version for certain device (because that device is then EoL) ... and that beta fixes some bugs present in all previous software versions. So MT's continued support is something to be glad for.Ok got it, thanks ---