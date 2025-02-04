# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 203836

# Discussion

## Initial Question
Author: [SOLVED]Sat Jan 27, 2024 5:32 am
I need help with this code. Basically I want 2 schedules to be executed, one to do the validations while the user is active and the second so that when a user is disabled, with the first schedule the second schedule is then activated performing the analysis of "if the user is disabled , make said comment. Greetings. I accept suggestions.[/system scheduler add interval=3m comment="$comentario2" name=$user on-event="/ip hotspot user disable [find name=$user] \r\\n/ip hotspot active remove [find user=$user] \r\\n/ip hotspot cookie remove [find user=$user] \r\\n/ip hotspot user reset-counter [find name=$user] \r\\n/system scheduler remove [find name=$user] \r\\n/\r\"start-date=$adate start-time=$atime/sy schadd interval=10s name="MONITOR:$user" on-event=":if ([ /ip hotspot user find name=$user disabled=yes]) do={[ /ip hotspot user set $user comment="$comentario3 $temp4" ]} \r\\n/\r\" start-d=$adate start-t=($atime + 00:00:10)]