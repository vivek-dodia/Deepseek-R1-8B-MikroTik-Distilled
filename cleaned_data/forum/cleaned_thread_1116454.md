# Thread Information
Title: Thread-1116454
Section: RouterOS
Thread ID: 1116454

# Discussion

## Initial Question
Hello!I can log the nat from my client how to connect the internet?My master router ist mikrotik!Thank you for your advance?I have Nice day!I can search the forum and have no post! ---

## Response 1
To log data from NAT table, or to log specific data from NAT table.Use action=log before NAT rule (log-prefix to assign prefix for the log info).E.g.'ip firewall nat add chain=srcnat action=log src-address=x.x.x.x/xxip firewall nat add chain=srcnat action=masquerade src-address=x.x.x.x/xx' ---

## Response 2
Sergejs!The example workt!I can download the logfile the log downloader? ---

## Response 3
I don't understand you correctly.But here isSyslogdaemon for Windows, that will help you to handle your logs. ---

## Response 4
I don't understand you correctly.But here isSyslogdaemon for Windows, that will help you to handle your logs.I put down!I tested in the nigth!Thank you! ---

## Response 5
I don't understand you correctly.But here isSyslogdaemon for Windows, that will help you to handle your logs.I put down!I tested in the nigth!Thank you! ---

## Response 6
Revitalizing this old question: is this still the way to do it? Using a RB5009 with 7.16.2, I'm not getting consistent results. It does log /some/ new outgoing connections, but only some, and some not... What is the current and preferred method of logging new outgoing NATted connections? ---