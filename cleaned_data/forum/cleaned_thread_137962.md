# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 137962

# Discussion

## Initial Question
Author: Mon Aug 13, 2018 12:09 am
``` :foreach user in=[/ip firewall address-list find find address=10.2.2.2] do={ /ip firewall address-list disable $user } ``` ``` ip firewall address-list disable [/ip firewall address-list find address=10.2.2.2] ``` UsingPEAR2_Net_RouterOS-1.0.0b6The following works fine the in the Mikrotik Terminal. But I cant get it to work via the API. How would I do the following:
```
Or
```

```
---
```

## Response 1
Author: [SOLVED]Mon Aug 13, 2018 9:08 pm
``` $util = new RouterOS\Util($client); $util->setMenu('/ip firewall address-list')->disable(RouterOS\Query::where('address', '10.2.2.2')); ``` ``` $ids = array(); $util->setMenu('/ip firewall address-list'); foreach ($util->getAll(array('.proplist' => '.id'), RouterOS\Query::where('address', '10.2.2.2')) as $item) { $ids[] = $item('.id'); } $util->disable(implode(',', $ids)); ``` Easiest would be:
```
Although there is a bug with Util and queries with multiple matches that's already fixed in the upcoming version... Until that version is released, if you have more than one match, you could use:
```