# Thread Information
Title: Thread-213543
Section: RouterOS
Thread ID: 213543

# Discussion

## Initial Question
On:https://mikrotik.com/support- there is a new AI chat bot, it seems to work pretty well for some basic questions I throw at it.But does it feed with the actual /help docs or has some unreleased documentation?!When asking for IPSEC VTI support for example it is convinced Mikrotik supports it and even generates a configration for me with using "/interface vti" cli?Is VTI coming? Or is The Dude throwing false alarms?How do others experience this new "the dude" AI? ---

## Response 1
There's another nugget of information that could indicate that there's active work on VTI: a reddit user noticed that there's now asupport matrix indicating /31 subnet support for v7.18in theofficial routing documentation. While the two features definitely do not depend on one another, it's a typical use case to setup a VTI interface with a /31 subnet.Or the AI could be hallucinating, of course. ---