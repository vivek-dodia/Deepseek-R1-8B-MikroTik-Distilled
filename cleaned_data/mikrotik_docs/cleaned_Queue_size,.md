# Document Information
Title: Queue size
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/137986083/Queue+size,

# Content
# Example
This example was created to highlight the queue size impact on traffic that was queued by a specific queue.
In Mikrotik RouterOS, queue size can be specified in the "/queue type" menu. Each queue type has a different option for specifying queue size (pfifo-limit, bfifo-limit, pcq-limit, pcq-total-limit, red-limit), but all principles are the same - queue size is the main option that decides should the package be dropped or scheduled for a later time.
```
/queue type
```
In a real-time environment, this process is happening continuously without any stops, steps, or other interruptions, but to show it as an example, we will divide it into steps, where it is possible to know exactly how many packets will be received/transited in every step.
We will not go into specific details of TCP and dropped packet retransmission - consider these packets as simple UDP streams.
As you can see in the picture above there are25 stepsand there are a total of1610 incoming packetsover this time frame.
# 100% Shaper
A queue is 100% shaper when every packet that is over the allowed limits will be dropped immediately. This way all packages that are not dropped will be sent out without any delay.
Let's applymax-limit=100packets per steplimitation to our example:
With this type of limitation, only 1250 out of 1610 packets were able to pass the queue (22,4% packet drop), but all packets arrive without delay.
# 100% Scheduler
A queue is 100% Scheduler when there are no packet drops at all, all packets are queued and will be sent out at the first possible moment.
In each step, the queue must send out queued packets from previous steps first and only then send out packets from this step, this way it is possible to keep the right sequence of packets.
We will again use the same limit (100 packets per step).
There was no packet loss, but 630(39,1%) packets had 1 step delay, and the other 170(10,6%) packets had 2 step delay. (delay = latency)
# Default-small queue type
It is also possible to choose the middle way when the queue uses both of these queuing aspects (shaping and scheduling). By default, most of the queues in RouterOS have a queue size of 10.
There were 320(19,9%) packets droppedand 80(5,0%) packets had 1 step delay.
# Default queue type
Another popular queue size in RouterOS is 50.
There were 190(11,8%) packets droppedand 400(24,8%) packets had 1 step delay.