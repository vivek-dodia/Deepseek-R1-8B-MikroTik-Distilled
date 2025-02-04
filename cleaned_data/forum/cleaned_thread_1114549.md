# Thread Information
Title: Thread-1114549
Section: RouterOS
Thread ID: 1114549

# Discussion

## Initial Question
Hello, I've recently bought two SXT 6 and have linked them wirelessly together (Bridge and Station-Bridge).i've nothing configured, only the bridge and added ports to them, and ofcourse the wireless interfaces.My problem is, that after every few hours, the ethernet will have high latency (delay) when i ping from anywhere.restarting the device solves the problem.then after few hours, same issue.both are making the same problem, but not at the same time.so i assume that something wrong with the ethernet is.replacing them with any other two devices (also Mikrotik) doesn't show this problem.version 6.49.13Any help please ? ---

## Response 1
/tool graphing interfaceadd/tool graphing queueadd/tool graphing resourceaddread logsafter error check resource utilization ---