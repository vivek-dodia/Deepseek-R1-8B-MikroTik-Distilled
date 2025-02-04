# Thread Information
Title: Thread-214156
Section: RouterOS
Thread ID: 214156

# Discussion

## Initial Question
Hi everybody!I'm trying to do this:I have a connection with pppoe. And I have two way for authenticate this pppoe: ether1 on fiber, ether 2 on radio link (in case of fiber goes down).How can I make the PPOE output interface automatically change when the fiber goes down?Or: could I configure 2 pppoe with the same credentials on both interfaces, and make that pppoe on fiber is disabled when the fiber goes down, and activate the second pppoe on the backup interface?Can you help me? I hope I have been as clear as possible ---

## Response 1
It seems to me like the second approach is easier as it is more similar to usual failover.Though usually failover is done enabling and disabling routes, not enabling and disabling interfaces.Post your current configuration, following these instructions:viewtopic.php?t=203686#p1051720 ---