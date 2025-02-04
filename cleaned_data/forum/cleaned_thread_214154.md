# Thread Information
Title: Thread-214154
Section: RouterOS
Thread ID: 214154

# Discussion

## Initial Question
Let's hypothetically assume the following:I change the MTU value of an Interface.
```
> interface/ethernet/set numbers=ether1 mtu=1499 ;How can I reset the DEFAULT (mtu=1500) value?

---
```

## Response 1
You can reset it to default by running same set command with different value.Finding out the default value for certain settings can be tricky though. One of them is e.g. L2MTU which can vary wildly depending on hardware type (and even device model, there are cases where different device models use same hardware but come with different defaults). ---

## Response 2
Finding out the default value for certain settings can be tricky though. One of them is e.g. L2MTU which can vary wildly depending on hardware type (and even device model, there are cases where different device models use same hardware but come with different defaults).Well, that's the problem!How come there is no command for this? ---

## Response 3
```
/interface/ethernet/set [find] mtu=1500

---
```

## Response 4
```
/interface/ethernet/set [find] mtu=1500But how do you know that 1500 ???

---
```

## Response 5
```
/interface/ethernet/reset [find] mtu=Runs with no complaints and chooses 1500 as default with RouterOS 7.16.2.

---
```

## Response 6
Yup, "reset" is the command to, well, reset something to default. Most RouterOS config items support the "reset" subcommand.FWIW, at the Terminal prompt, you can do a:
```
/interface/ethernet print
/interface/ethernet reset 0 mtu=In @ConradPino's example the [find] will find all ethernet, and reset the mtu to default on ALL ports.  Possible to add a filter in [find] to limit it to specific port(s).  Using [find] is needed if this is something you want to script for non-CLI use (since in /system/script, using the numbers= may change).  So for example, you can find by the "default name", since if you're reset'ing something in script, it's name may have changed... so using "default-name=" in the find let you get the right interface (even if user renamed the interface)
```

```
/interface/ethernet/reset [find default-name=ether1] mtu=If you don't provide "mtu=" - reset will make all attributes the default value.

---
```

## Response 7
Yup, "reset" is the command to, well, reset something to default. Most RouterOS config items support the "reset" subcommand.FWIW, at the Terminal prompt, you can do a:
```
/interface/ethernet reset 0 mtu=You win my friend!Many-many thanks!Indeed, the "reset" command already exists under ROS v7!!!(It doesn't exist under ROS v6.)I have so many observations that the additional option (e.g. mtu=) doesn't work for me, because it still resets everything on the given interface.

---
```

## Response 8
Stop suggest using "0" and use interface name.Ignoring the i*** of change randomly the MTU, the correct syntax isset ether1 mtu=1500and [find] must not be used alone, because change everything, not only that interface./interface ethernet reset NOT exist on v6 (exist only reset-counters and reset-mac-address)on v7 exist reset, reset-counters, and reset-mac-addressThe reset RESET ALL EXCEPT COMMENT... for reset and set AT SAME TIME can be added some parameters like
```
/interface/ethernet reset ether1 mtu=1500 l2mtu=1584This RESET ALL EXCEPT COMMENT, but after the reset set mtu and l2mtu to provided values.So the correct sytax to reset all ether1 parameters to default values, except comments, is:
```

```
/interface/ethernet reset [find where default-name=ether1]There is not a command to reset to default value a single property.In this case is easy to know that the default is 1500 and must be keeped like that,because if you not know the default value, mean that you do not really understand what is the MTU and how it works.

---
```

## Response 9
Stop suggest using "0" and use interface name.If you're working at the Terminal, using the numbers is fine – you need to do a recent print of course, which was shown....It's only in "background" scripts where using "0" or other numbers from a print is BAD idea & you need some [find ...] thing in that case. But not a terminal... the numbers are less typing if working interactively. ---

## Response 10
So the correct sytax to reset all ether1 parameters to default values, except comments, is:
```
/interface/ethernet reset [find where default-name=ether1]The "where" is redundant AFAIK, so not sure why you show that.  I am missing something?

---
```

## Response 11
I like corerct syntax and avoid shorting for unreadabilty.I dislike full syntax but not where:
```
/interface ethernet reset numbers=[/interface ethernet find where default-name=ether1]

---
```

## Response 12
@anaveven if you specificaties, the command will reset the whole interfaceIf you don't provide "mtu=" - reset will make all attributes the default value.[/quote] ---

## Response 13
@Amm0If you don't provide "mtu=" - reset will make all attributes the default value.even if you specificaties, the command will reset the whole interface ---

## Response 14
@anavWhere is???even if you specificaties, the command will reset the whole interfaceAlready wroted, with explanation....viewtopic.php?t=214154#p1121429(obviously MTU and L2MTU are 666 and 777 just for test..........)terminal code[rex@edge-MATRIX] /interface/ethernet> export # 2025-01-25 10:41:03 by RouterOS 7.16.2 # software id = 6AR6-6UI6 # # model = CCR2116-12G-4S+ # serial number = HCQ66BYW6ZX /interface ethernet [...] <CUT> set [ find default-name=ether5 ] comment="(non collegato)" l2mtu=777 mtu=666 [...] <CUT> [rex@edge-MATRIX] /interface/ethernet> reset ether5 mtu=1508 l2mtu=1580 [rex@edge-MATRIX] /interface/ethernet> export # 2025-01-25 10:41:46 by RouterOS 7.16.2 # software id = 6AR6-6UI6 # # model = CCR2116-12G-4S+ # serial number = HCQ66BYW6ZX /interface ethernet [...] <CUT> set [ find default-name=ether5 ] comment="(non collegato)" l2mtu=1580 mtu=1508 [...] <CUT> [rex@edge-MATRIX] /interface/ethernet> reset ether5 [rex@edge-MATRIX] /interface/ethernet> export # 2025-01-25 10:41:58 by RouterOS 7.16.2 # software id = 6AR6-6UI6 # # model = CCR2116-12G-4S+ # serial number = HCQ66BYW6ZX /interface ethernet [...] <CUT> set [ find default-name=ether5 ] comment="(non collegato)" [...] <CUT> ---

## Response 15
@nichky - I only commented since initial suggestion of plain/unqualified [find] was a BAD idea. But I didn't test the mtu= part myself.@anavWhere is???Easy to confuse, we're all one country over here now. ---