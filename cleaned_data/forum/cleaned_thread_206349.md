# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206349

# Discussion

## Initial Question
Author: Mon Apr 01, 2024 1:18 pm
``` :globalipaddress[/queue simpleget1target];:globaltest[:find $ipaddress"/"]; ``` Hello, I'm facing an issue.
```
The ipaddress variable returns: 192.168.0.2/32, however, test doesn't return anything. Why is that?Thank you for your assistance.


---
```

## Response 1
Author: Mon Apr 01, 2024 1:28 pm
``` :globalipaddress[/queue simpleget1target];:globaltest[:globalipaddress;:find $ipaddress"/"]; ``` 
```
Inside the function, ipaddress is not known so you have refer to it by :global ipaddress.


---
```

## Response 2
Author: [SOLVED]Mon Apr 01, 2024 2:51 pm
``` :globalipaddresses[/queue simpleget[find name=queue1]target]:globalipaddress[:pick $ipaddresses0]:globalcidrmark[:find $ipaddress"/"]:put"$[:pick $ipaddress 0 $cidrmark]" ``` ``` {:localipaddress([/queue simpleget[find name=queue1]target]->0);:put"$[:pick $ipaddress 0 [:find $ipaddress /]]"} ``` Couple other things too:- The first line use "get 1", however that's not an *id so it depends on print being called to establish the index of 1. Using "get ([find]->0)" or "get [find name=queue1]" instead avoid needing.- There can be multiple "target" from "/queue simple get", and :find does not work with arrays & so need use get the 1st element listed as "target" firstFor example, 
```
Although these could be a locals and combined:
```

```
---
```

## Response 3
Author: Mon Apr 01, 2024 9:53 pm
``` :globalipaddress[/queue simpleget1target];:globaltest[:globalipaddress;:find $ipaddress"/"]; ``` ``` :globalipaddresses[/queue simpleget[find name=queue1]target]:globalipaddress[:pick $ipaddresses0]:globalcidrmark[:find $ipaddress"/"]:put"$[:pick $ipaddress 0 $cidrmark]" ``` ``` {:localipaddress([/queue simpleget[find name=queue1]target]->0);:put"$[:pick $ipaddress 0 [:find $ipaddress /]]"} ``` Hi, Thank you for your answers
```
Inside the function, ipaddress is not known so you have refer to it by :global ipaddress.With this solution, I have a result : "$ipaddress"Couple other things too:- The first line use "get 1", however that's not an *id so it depends on print being called to establish the index of 1.  Using "get ([find]->0)" or "get [find name=queue1]" instead avoid needing.- There can be multiple "target" from "/queue simple get", and :find does not work with arrays & so need use get the 1st element listed as "target" firstFor example,
```

```
Although these could be a locals and combined:
```

```
- The first line use "get 1", however that's not an *id so it depends on print being called to establish the index of 1.  Using "get ([find]->0)" or "get [find name=queue1]" instead avoid needing.It was for the example, I understood that the get 1 corresponded to the number present in this menu on Winbox- There can be multiple "target" from "/queue simple get", and :find does not work with arrays & so need use get the 1st element listed as "target" firstIndeed, you have found my problem, I had not seen this return as an array but a character string !thanks a lot for your helpGood evening to youXavier
```