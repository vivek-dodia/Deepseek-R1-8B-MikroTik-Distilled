# Thread Information
Title: Thread-214218
Section: RouterOS
Thread ID: 214218

# Discussion

## Initial Question
Hello for all..!I have CCR2004 in my company and I want to create a dedicated QoS (Quality of Service) path for the SIP phones in my company to ensure smooth and uninterrupted communication between IP phones. This setup will prioritize their bandwidth, preventing other network activities from consuming the allocated bandwidth for voice calls.If anyone has experience with this, could you guide me to how can I achieve this? ---

## Response 1
Check out this example:https://mikrocloud.com/blog/qos/tos-and-dscp.For a more versatile way to prioritize important traffic without specifying traffic types, CAKEmight be a better option. Check out this blog: "CAKE Configuration" and this thread:viewtopic.php?t=213724.You might want to check out the preconfigured "cake-diffserv" options that are used to automatically prioritize and classify network traffic. In your case, "cake-diffserv=diffserv4" ordiffserv8would probably work better. ---