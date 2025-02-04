# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212955

# Discussion

## Initial Question
Author: [SOLVED]Sat Nov 30, 2024 11:31 pm
Here is my script. The first line shows syntax error::local currentIP [/tool fetch url=\"http://icanhazip.com\" as-value output=user]->\"data\";:local timestamp [/system clock get time];:local date [/system clock get date];:local logEntry (\"Public IP: \$currentIP at \$date \$timestamp\");The first syntax error is give by this part of the script: "url=\"http://". It helps if I remove replace it with "url="http://". However, I get error and it seems to be related to the very last part of the first line. Go figure...? ---

## Response 1
Author: Sun Dec 01, 2024 10:39 am
``` :localcurrentIP([/tool fetch url="http://icanhazip.com" as-value output=user]->"data"); ``` ``` :localcurrentIP[/ip/cloud/getpublic-address] ``` Hi, The parenthesis around the -> operator is missing. It should be:
```
BTW. I removed the escaping of the quotes to be able to run the command from CLI.If you use the build in editor from the CLI, the above error comes out pretty clear in the syntax highlighting.Also the same result can be achieved like this:
```