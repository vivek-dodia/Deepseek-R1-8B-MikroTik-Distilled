# Thread Information
Title: Thread-1117966
Section: RouterOS
Thread ID: 1117966

# Discussion

## Initial Question
I'm currently on the latest 7.17beta2 trying out the whitelisting for adlists.The way I've set them up is through static as FWD and under "forward to" I define a DNS server such as 1.1.1.1, this simply works.However, I can't seem to point toward the local server I'm running in my router, is there a wildcard for this or maybe I'm not seeing the problem?For reference:Which shows up as:Instead of hard-coding a "Forward To" address, can I point it to my local dns server instead?, does it require any additional setup for this to work?, or as its currently setup would this turn into an endless loop situation? ---

## Response 1
This doesnt seem to work. googleadservices.com is used in just about every shopping link so I need to whitelist it and I'd prefer to not be updating the adlist file frequently.Did you get anywhere with this? ---

## Response 2
Edited ---

## Response 3
I'm currently on the latest 7.17beta2 trying out the whitelisting for adlists.The way I've set them up is through static as FWD and under "forward to" I define a DNS server such as 1.1.1.1, this simply works.However, I can't seem to point toward the local server I'm running in my router, is there a wildcard for this or maybe I'm not seeing the problem?For reference:Which shows up as:Instead of hard-coding a "Forward To" address, can I point it to my local dns server instead?, does it require any additional setup for this to work?, or as its currently setup would this turn into an endless loop situation?We probably need better logic on how this works BUTIf you set up local DNS on the router and apply an adlist, this tells the router DNS to respond to everything not on those lists.Whitelist (exceptions) are resolved via a DNS you specify.If you specify the router itself, you are grabbing a whitelisted domain and asking the router to forward it to itself where it has an adlist that may be dropping that domain.Tl;DR - It looks like the intended use case for this is to point whitelisted domains to external DNS and not cache them. ---