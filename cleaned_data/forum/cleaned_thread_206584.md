# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206584

# Discussion

## Initial Question
Author: Tue Apr 09, 2024 2:36 pm
``` :local packageVersion (/file get (find ".npk") package-version) :put $packageVersion ``` Hi guys!I'm trying to create obtain the package version of one npk file and store it into a variable, but in every way i tried, my variable stills empty.
```
Can somebody help me with a solution please?


---
```

## Response 1
Author: Tue Apr 09, 2024 6:32 pm
``` :local packageVersion [/file get [find type="package"] package-version] ``` the file is called .npk?why you use () ???No the file is named as a mikrotik firmware, something like "routeros-arm-6.49.10.npk". I noticed this after posting, i changed to:
```
I didn't even think about the use (), i'm kind new to scripting, thanks for the hint!It's working with the script above. Thanks man!


---
```

## Response 2
Author: Wed Apr 10, 2024 5:56 pm
``` $(cat /etc/passwd) ``` I didn't even think about the use (), i'm kind new to scripting, thanks for the hint!If you know Linux/UNIX, the [] are similar to `` backtick to run a command and replace result in-place.Yes and the new way of doing this in UNIX/Linux, not using back tics chars. is like this.Use dollar sign and regular parentheses.
```
---
```

## Response 3
Author: Wed Apr 10, 2024 7:18 pm
``` $(cat /etc/passwd) ``` It's likely better thinking of the RouterOS CLI in terms of a REPL for a programming language, than ANY UNIX shell.It's thinking CLI is more like Linux/UNIX is where the trouble startsFWIW, I'm not sure $() is newer than ``. The $() is more for variable assignment IMO, while backtick works anywhere.Yes and the new way of doing this in UNIX/Linux, not using back tics chars. is like this.Use dollar sign and regular parentheses.