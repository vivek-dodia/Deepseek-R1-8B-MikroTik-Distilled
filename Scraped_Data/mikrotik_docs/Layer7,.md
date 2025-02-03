---
title: Layer7
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/130220161/Layer7,
crawled_date: 2025-02-02T21:10:36.947432
section: mikrotik_docs
type: documentation
---

* 1Summary1.1Properties
* 2Examples2.1Simple L7 usage example2.2L7 in the input chain2.3Youtube Matcher
* 1.1Properties
* 2.1Simple L7 usage example
* 2.2L7 in the input chain
* 2.3Youtube Matcher
# Summary
Layer7-protocol is a method of searching for patterns in ICMP/TCP/UDP streams.
L7 matcher collects the first10 packetsof a connection or the first2KBof a connection and searches for the pattern in the collected data. If the pattern is not found in the collected data, the matcher stops inspecting further. Allocated memory is freed and the protocol is consideredunknown. You should take into account that a lot of connections will significantly increase memory and CPU usage. To avoid this, add regular firewall matchers to reduce the amount of data passed to layer-7 filters repeatedly.
An additional requirement is that the layer7 matcher must see both directions of traffic (incoming and outgoing). To satisfy this requirement l7 rules should be set intheforwardchain. If the rule is set intheinput/preroutingchain then the same rulemustbe also set intheoutput/postroutingchain, otherwise, the collected data may not be complete resulting in an incorrectly matched pattern.
Example L7 patterns compatible with RouterOS can be found onthel7-filter project page.
## Properties
```
/ip firewall layer7-protocol
```
Property | Description
----------------------
name(string; Default:) | Descriptive name of l7 pattern used by configuration in firewall rules. See example>>.
regexp(string; Default:) | POSIX compliant regular expression is used to match a pattern.
# Examples
### Simple L7 usage example
First, add Regexp strings to the protocols menu, to define the strings you will be looking for. In this example, we will use a pattern to match RDP packets.
```
/ip firewall layer7-protocol
add name=rdp regexp="rdpdr.*cliprdr.*rdpsnd"
```
Then, use the defined protocols in the firewall.
```
/ip firewall filter
# add few known protocols to reduce mem usage
add action=accept chain=forward comment="" disabled=no port=80 protocol=tcp
add action=accept chain=forward comment="" disabled=no port=443 protocol=tcp
# add l7 matcher
add action=accept chain=forward comment="" disabled=no layer7-protocol=\
    rdp protocol=tcp
```
As you can see before the l7 rule we added several regular rules that will match known traffic thus reducing memory usage.
### L7 in the input chain
In this example, we will try to match the telnet protocol connecting to our router.
```
/ip firewall layer7-protocol add comment="" name=telnet regexp="^\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe]"
```
Note that we need both directions which is why we need also the l7 rule in the output chain that sees outgoing packets.
```
/ip firewall filter
add action=accept chain=input comment="" disabled=no layer7-protocol=telnet \
    protocol=tcp
add action=passthrough chain=output comment="" disabled=no layer7-protocol=telnet \
    protocol=tcp
```
### Youtube Matcher
```
/ip firewall layer7-protocol
add name=youtube regexp="(GET \\/videoplayback\\\?|GET \\/crossdomain\\.xml)"
```