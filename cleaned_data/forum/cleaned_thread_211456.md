# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211456

# Discussion

## Initial Question
Author: Thu Oct 03, 2024 3:20 pm
``` :if ([:len [/interface find name=$interfaceName]] > 0) do={ :if ([/interface find name=$interfaceName] = "") do={ :if [/interface find name=$interfaceName] do={ ``` Hi, Because I can never remember how this works, I find myself using the following expressions interchangibly in order to determine whether one or more matching items exist:
```
I would like to use the last option, but I don't know whether it always works as expected, nor whether these are exactly equivalent.Edit: Although I apparently can't invert the last option easily, because I "cannot logically negate nothing". Second option is just awkward. First option is a little long, but feels the most robust, as one would expect [find] to always return an array of results.


---
```

## Response 1
Author: [SOLVED]Thu Oct 03, 2024 5:25 pm
``` :if ([:len [/interface find where name="the name"]] > 0) do={} else={} # or if used with print :if ([:len [/interface print as-value where name="the name"]] > 0) do={} else={} ``` ``` :put ({} = "") true :put ([:toarray ""] = "") true ``` ``` :put ([:toarray ""] = true) false :put ({} = true) false :put ([:toarray "1, 2, 3, 4"] = true) false :put ({1, 2, 3, 4} = true) false ``` The correct method is only the first.
```
Stop.Too often in scripts you get strange results when using an array and comparing it to simple strings:
```

```
Test for 3rd method:
```