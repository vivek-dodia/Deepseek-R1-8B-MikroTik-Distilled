# Thread Information
Title: Thread-1117140
Section: RouterOS
Thread ID: 1117140

# Discussion

## Initial Question
I can't find the right section, so I'm writing here.I have an age-old question, it's all about whether it's possible with Mikrotik to redirect an insolvent client to a message (on the web server) that the client has not paid and the services are suspended. Because most examples are with webproxy, and as far as I know, everything only works with port 80, but not with 443.What can you suggest? ---

## Response 1
What routerOS/platform are we talking about ?So in essence everything starts with how you are identifying such "insolvent client" then ?You are running PPPoE servers ? Using AAA (RADIUS) I assume ?1) Go non-technical and simply block access. Customer will make a call to support "why it is not working?" and bingo.2) Perhaps something with DNS ? Through RADIUS you could assign these insolvent clients specific DNS settings ? On that DNS make some fancy config so it will bring the client to certain webpage whatevever he is trying to visit.... ---

## Response 2
Who can use pppoe in the 21st century?I'm talking about a mikrotik router, RouterOS.We describe clients with vlan, each client has a vlan and an ip address.The call is not suitable, there are redirections for this, as large operators do. ---

## Response 3
Who can use pppoe in the 21st century?A lot of people. PPPoE makes a lot of sense for accounting (for example, in your case it might make sense)I know, everything only works with port 80, but not with 443.Redirecting SSL Traffic is not easy since the customer will just get an "Invalid Certificate" message since the SNI won't match the certificate.The call is not suitable, there are redirections for this, as large operators do.Actually, here you usually get a letter and then they just block ur PPPoE Tunnel.If you just want to redirect, just use DNAT to ur target.EDIT:Something like this:https://help.mikrotik.com/docs/spaces/R ... HairpinNAT ---

## Response 4
Well, for example, there is a company like "Telia" where no one plays around when a customer doesn't pay. Traffic is blocked and the customer receives a message in the browser, regardless of whether it's port 80 or 443. ---

## Response 5
Technically you could run with a captive portal as most devices can discover that.But you'd have to modify the login page to the Portal so that it will just show you a message with "Invoice not paid"Not sure if ROS supports that.For example:https://support.mozilla.org/en-US/kb/captive-portal ---

## Response 6
Yes it can, see here:https://help.mikrotik.com/docs/spaces/R ... ive+portal ---