# Thread Information
Title: Thread-29167
Section: RouterOS
Thread ID: 29167

# Discussion

## Initial Question
I have RouterOS 3.17 and would like to be able to issue a "/ip hotspot user print" command via ssh, authenticated with a key. This works fine:
```
$ ssh admin@microtik "/ip hotspot user print"
Flags: X - disabled, D - dynamic
 #   SERVER           NAME         ADDRESS         PROFILE         UPTIME
 0                    tester                       211WLANhot      58m9s
1                    usrWLAN-A...                 211WLANhot      0sThe issue appears when I have a user name that is longer. The output of the user name is then truncated, rendering the output useless for me.When I issue the same command from a sufficently wide terminal in an interactive session:
```

```
$ ssh admin@microtik
[microtik banner snipped]
[admin@microtik] > /ip hotspot user print
Flags: X - disabled, D - dynamic
 #   SERVER                               NAME                             ADDRESS         PROFILE                             UPTIME
 0                                        tester                                           211WLANhot                          58m9s
 1                                        usrWLAN-A-HPuA                                   211WLANhot                          0sthe user name is not truncated.How can I get untruncated output from a non-interactive session?Any hints will be appreciated.GreetingsMarc

---
```

## Response 1
you can use the different parameters for the print command, like "print detailed, print terse, print brief" etc ---

## Response 2
you can use the different parameters for the print command, like "print detailed, print terse, print brief" etcPrint brief does what I want. Actually, print detailed is print detail.GreetingsMarc ---

## Response 3
HiI am having exactly the same problem, except that none of the print options seem to be of any use. I am trying to print out the wireless registration table, but the data that is most important to me, the uptime, gets cut off. Is there anyway to prevent that?regards, Jason ---

## Response 4
tryprint detailorprint stats ---

## Response 5
aha!"print stats" works. Its a bunch more text, but it does the trick.Just as a note, the "print detail" does not work, the output is still truncated.thanks! ---

## Response 6
There are a lot of options for the print command, just type print and "?":
```
[admin@router] /interface wireless> print          
Print values of item properties in different formats.

advanced -- Show subset of properties in detailed form
append -- 
as-value -- 
basic -- Show subset of properties in detailed form
count-only -- 
detail -- Displays detailed information
file -- Print the content of the submenu into specific file
follow -- 
follow-only -- 
from -- Interface name or number obtained from print command
interval -- Displays information and refreshes it in selected time interval
oid -- print object IDs for SNMP protocol
terse -- Show details in compact and machine frendly fromat
value-list -- Show properties one per line
where -- 
without-paging -- Displays information in one piece

---
```

## Response 7
I know this is 15 years old, but it was the first result for setting ssh terminal width and it doesn't actually answer the question. Let me explain what the problem is and give a bunch of example data so you can see what the problem is.On a BSD host in my network I ransudo hostname this-is-a-really-long-hostname-because-i-am-testing-something. So for a few minutes, that VM thinks it has an absurdly long hostname. Then on that VM, I runsudo service netif restart. That causes the host to re-request its DHCP lease, sending this silly hostname to the DHCP server on my router.Now, like the OP I am sending commands to my Mikrotik (model: RB4011iGS+, revision: r2, current-firmware: 7.10.1, routeros 7.14.3) authenticated using an SSH key.If I login interactively with an SSH session from a terminal window that is wide on my screen, I can run:/ip/dhcp-server/lease/print where address="172.30.2.28"and I see this:
```
Flags: D - DYNAMIC
Columns: ADDRESS, MAC-ADDRESS, HOST-NAME, SERVER
#   ADDRESS      MAC-ADDRESS        HOST-NAME                                                      SERVER
0 D 172.30.2.28  6E:15:09:09:26:56  this-is-a-really-long-hostname-because-i-am-testing-something  marmiteTHIS IS THE OUTPUT I WANT. This is good. All i want to do is get this exact output non-interactively.If I run/ip/dhcp-server/lease/print file=test.txt where address="172.30.2.28"and then I look at the contents of test.txt, I see:
```

```
# 2024-12-07 10:26:42 by RouterOS 7.14.3
# software id = XXXX-XXXX
#
Flags: D - DYNAMIC
Columns: ADDRESS, MAC-ADDRESS
  #   ADDRESS      MAC-ADDRESS      
112 D 172.30.2.28  6E:15:09:09:26:56The entire HOST-NAME column has been omitted. I assume this is because it is too wide for whatever line length the print command uses. If it's for some other reason, then what do I need to do to change it?If I runssh gw '/ip/dhcp/lease/print where address="172.30.2.28"'to just get the ip leases output in a non-interactive way (the kind of thing one might put in a script), I get the same output:
```

```
Flags: D - DYNAMIC
Columns: ADDRESS, MAC-ADDRESS
 #   ADDRESS      MAC-ADDRESS      
17 D 172.30.2.28  6E:15:09:09:26:56If I use thebriefoption, as suggested in this thread, I still don't get the HOST-NAME column. If I use thedetailoption, I get the full hostname, but now the output is in this multi-line stanza format that I have to parse. What I really want is the IP address and the hostname and nothing else. And I don't care about line length. This is 2024 and I don't have some DEC VT100 that physically limits the number of letters on the screen. What would be awesome is JSON format, but I'll take text that doesn't omit entire columns.Thedocumentation on the command-line interfacesays that line width is controlled by parameters after the login name. That's really unusual, but whatever. It offers the following example: "admin+c80w - will disable console colors and set terminal width to 80". So I tryssh marmite+c80w@gwand indeed, I get an interactive SSH session and color is disabled as I expected. However, my actual terminal window is much wider than 80 characters and when I run the/ip/dhcp/lease/printcommand, I get the full host-name column. The output is far wider than 80 characters. So the 'c' flag for disabling color seems to work, but the 80w part doesn't seem to have the effect I expect. Likewise runningssh marmite+2000w@gw '/ip/dhcp/lease/print where address="172.30.2.28"' still gets me the output without the host-name column, even though I theoretically told it I was happy with 2000 character width. (I also tried some smaller values like 110w and 130w).So how do I get the/ip/dhcp/lease/printcommand to print really wide output when I use a non-interactive SSH connection to execute it?

---
```

## Response 8
[...]If I use thebriefoption, as suggested in this thread, I still don't get the HOST-NAME column. If I use thedetailoption, I get the full hostname, but now the output is in this multi-line stanza format that I have to parse. What I really want is the IP address and the hostname and nothing else. And I don't care about line length. This is 2024 and I don't have some DEC VT100 that physically limits the number of letters on the screen.What would be awesome is JSON format, but I'll take text that doesn't omit entire columns.Well, there is JSON support in current stable V7 via ":serialize", which avoid the complexities of "termcap things". And avoid needing the user+1000w scheme, which does seem like that should have worked based on docs...).So to get the leases as JSON file it look like this:
```
/file/remove [find name=leases.json]
/file/add name=leases.json contents=[:serialize to=json [/ip/dhcp/lease/print as-value] options=json.pretty]I show a /file/remove since /file/add will not override the file, and /file/set needs an existing file.   Also, I think options=json.pretty is only in v7.16 and not strictly needed just uses newlines in JSON to make it readable if output to screen.  And :serialize is pretty new, older V7 versions do not have :serialize command at all, which was added in ~7.15 (based on memory).There is also in 7.16 [:serialize to=dsv delimator= [...]], to get a CSV that might be useful too — but that has a bug (SUP-134773) in that CSV output does not work with "print".Thedocumentation on the command-line interfacesays that line width is controlled by parameters after the login name. [...] The output is far wider than 80 characters. So the 'c' flag for disabling color seems to work, but the 80w part doesn't seem to have the effect I expect. Likewise runningssh marmite+2000w@gw '/ip/dhcp/lease/print where address="172.30.2.28"' still gets me the output without the host-name column, even though I theoretically told it I was happy with 2000 character width. (I also tried some smaller values like 110w and 130w).So how do I get the/ip/dhcp/lease/printcommand to print really wide output when I use a non-interactive SSH connection to execute it?You can try add proplist= to control the columns too.  Not sure that work, but easy to try.

---
```

## Response 9
Super helpful. We still don't know how to control the ssh line width. But in my case this worked for me:
```
ssh marmite@gw "/ip/dhcp/lease/print proplist=\"address,host-name\""When I restrict the output to only those 2 columns, even my very silly hostname wasn't too long.The last thing I have to chuckle at is the header of the output telling me that there are 2 columns: address and host-name. I had to make a meme about it. But seriously. Thank you. I'm all set for what I needed. I hope someone else gets some value from this thread.
```

```
Columns: ADDRESS, HOST-NAME
  #   ADDRESS      HOST-NAME                                                    
112 D 172.30.2.28  this-is-a-really-long-hostname-because-i-am-testing-somethingScreenshot from 2024-12-09 20-24-10.png

---
```

## Response 10
I had to make a meme about it. But seriously. Thank you. I'm all set for what I needed. I hope someone else gets some value from this thread.LOL. A bug report tosupport@mikrotik.comon the user+1000w not working might have been more productive- as I'm pretty sure the user+100w stuff is broken, or at least it does not do anything in quick test AFAIK. ---