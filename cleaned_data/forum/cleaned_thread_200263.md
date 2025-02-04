# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 200263

# Discussion

## Initial Question
Author: Wed Oct 04, 2023 9:03 pm
``` global ddnsip [ /ip address get [/ip address find interface="ether1" ] address ] ``` Hi, can any tell me if this scipt is working on ROS 7.x
```
Error: invalid internal item numberIt was working perfectly on 6.x ..If I put in a corresponding number of the interface it works.. Something must've changed..What is the new way in 7.x .. I could not find it in wiki or forum..https://help.mikrotik.com/docs/display/ ... g+examplesThe Check IP is not working on any of my ROS 7x


---
```

## Response 1
Author: Wed Oct 04, 2023 9:10 pm
Works fine here: :put [ /ip address get [/ip address find interface="ether2" ] address ]Using: MikroTik RouterOS 7.12beta1 ---

## Response 2
Author: [SOLVED]Thu Oct 05, 2023 1:41 am
``` :global ddnsip [ /ip/address/get ([ /ip/address/find where interface="ether1" ]->0) address ]; ``` Just a guess... Possibly you have several ip addresses on that interface now?Try that for the first address:
```
... or add more properties to your filter.


---
```

## Response 3
Author: Thu Oct 05, 2023 5:56 pm
``` :global ddnsip [ /ip/address/get ([ /ip/address/find where interface="ether1" ]->0) address ]; ``` Just a guess... Possibly you have several ip addresses on that interface now?Try that for the first address:
```
... or add more properties to your filter.Yes.. exactly I have more addresses! If I remove them it works the old fashioned way. Disable additional addresses does not help!But your solution works with multiple addresses!.. Odd thing to change it like this..Thank you very much for help! Much appriciated!


---
```

## Response 4
Author: Thu Oct 05, 2023 11:35 pm
``` :global ddnsip [ /ip/address/get ([ /ip/address/find where interface="ether1" disabled=no ]->0) address ]; ``` If you want to handle active addresses only add "disabled=no" to your filter:
```
It is all about your code!
```