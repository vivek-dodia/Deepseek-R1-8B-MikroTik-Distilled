# Document Information
Title: HTB (Hierarchical Token Bucket)
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/137986076/HTB+Hierarchical+Token+Bucket,

# Content
# Introduction
HTB (Hierarchical Token Bucket) is a classful queuing method that is useful for handling different kinds of traffic.  This article will concentrate on the "Token Bucket" part ofHierarchical Token Bucket(HTB) - an algorithm inside the single queue and configuration examples.
# Token Bucket algorithm (Red part of the diagram)
The Token Bucket algorithm is based on an analogy to a bucket where tokens, represented in bytes, are added at a specific rate. The bucket itself has a specified capacity.
If the bucket fills to capacity, newly arriving tokens are dropped
Bucket capacity = bucket-size * max-limit
Before allowing any packet to pass through the queue, the queue bucket is inspected to see if it already contains sufficient tokens at that moment.
If yes, the appropriate number of tokens are removed ("cashed in") and the packet is permitted to pass through the queue.
If not, the packets stay at the start of the packet waiting queue until the appropriate amount of tokens is available.
In the case of a multi-level queue structure, tokens used in a child queue are also 'charged' to their parent queues. In other words - child queues 'borrow' tokens from their parent queues.
# Packet queue (Blue part of the diagram)
The size of this packet queue, the sequence, how packets are added to this queue, and when packets are discarded is determined by:
# Token rate selection (Black part of the diagram)
The maximal token rate at any given time is equal to the highest activity of these values:
burst-limitis active only when 'burst' is in the allowed state - more info here:Queue Burst
In a case wherelimit-atis the highest value, extra tokens need to be issued to compensate for all missing tokens that were not borrowed from its parent queue.
# The Diagram
# Bucket Size in action
Let's have a simple setup where all traffic from and to one IP address is marked with a packet-mark:
```
/ip firewall mangle
add chain=forward action=mark-connection connection-mark=no-mark src-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-connection connection-mark=no-mark dst-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-packet connection-mark=pc1_conn new-packet-mark=pc1_traffic
```
# Default Queue Bucket
```
/queue tree
add name=download parent=Local packet-mark=PC1-traffic max-limit=10M
add name=upload parent=Public packet-mark=PC1-traffic max-limit=10M
```
In this case bucket-size=0.1, so bucket-capacity= 0.1 x 10M = 1M
If the bucket is full (that is, the client was not using the full capacity of the queue for some time), the next 1Mb of traffic can pass through the queue at an unrestricted speed.
# Large Queue Bucket
```
/queue tree
add name=download parent=Local packet-mark=PC1-traffic max-limit=10M bucket-size=10
add name=upload parent=Public packet-mark=PC1-traffic max-limit=10M bucket-size=10
```
Let's try to apply the same logic to a situation when bucket size is at its maximal value:
In this case bucket-size=10, so bucket-capacity= 10 x 10M = 100M
If the bucket is full (that is, the client was not using the full capacity of the queue for some time), the next 100Mb of traffic can pass through the queue at an unrestricted speed.
So you can have:
You can therefore see that the bucket permits a type of 'burstiness' of the traffic that passes through the queue. The behavior is similar to the normal burst feature but lacks the upper limit of the burst. This setback can be avoided if we utilize bucket size in the queue structure:
# Large Child Queue Bucket, Small Parent Queue Bucket
```
/queue tree
add name=download_parent parent=Local max-limit=20M
add name=download parent=download_parent packet-mark=PC1-traffic max-limit=10M bucket-size=10
add name=upload_parent parent=Public max-limit=20M
add name=upload parent=upload_parent packet-mark=PC1-traffic max-limit=10M bucket-size=10
```
In this case:
The parent will run out of tokens much faster than the child queue and as its child queue always borrows tokens from the parent queue the whole system is restricted to token-rate of the parent queue - in this case to max-limit=20M. This rate will be sustained until the child queue runs out of tokens and will be restricted to its token rate of 10Mbps.
In this way, we can have a burst at 20Mbps for up to 10 seconds.
# Configuration
We have to follow three basic steps to create HTB:
HTB allows to create of a hierarchical queue structure and determines relations between queues, like "parent-child" or "child-child".
As soon as the queue has at least one child it becomes aninnerqueue, all queues without children -areleafqueues.Leafqueues make actual traffic consumption,Innerqueues are responsible only for traffic distribution. Allleafqueues are treated on an equal basis.
In RouterOS, it is necessary to specifytheparentoption to assign a queue as a child to another queue.
# Dual Limitation
Each queue in HTB has two rate limits:
In other words, at firstlimit-at(CIR) of all queues will be satisfied, only then child queues will try to borrow the necessary data rate from their parents in order to reach theirmax-limit(MIR).
That is why, to ensure optimal (as designed) usage of the dual limitation feature, we suggest sticking to these rules:
CIR(parent)* ≥ CIR(child1) +...+ CIR(childN)*in case if parent is main parent CIR(parent)=MIR(parent)
MIR (parent) ≥ MIR(child1) & MIR (parent) ≥ MIR(child2) & ... & MIR (parent) ≥ MIR(childN)
Queue colors in Winbox:
# Priority
We already know thatlimit-at(CIR) to all queues will be given out no matter what.
Priority is responsible for the distribution of remaining parent queues traffic to child queues so that they are able to reachmax-limit
The queue with higher priority will reach itsmax-limitbefore the queue with lower priority. 8 is the lowest priority, and 1 is the highest.
Make a note that priority only works:
# Examples
In this section, we will analyze HTB in action. To do that we will take one HTB structure and will try to cover all the possible situations and features, by changing the amount of incoming traffic that HTB has to recycle. and changing some options.
# Structure
Our HTB structure will consist of 5 queues:
Queue03,Queue04,andQueue05are clients who require 10Mbps all the time Outgoing interface is able to handle 10Mbps of traffic.
# Example 1: Usual case
# Result of Example 1
# Example 2: Usual case with max-limit
# Result of Example 2
# Example 3: Inner queue limit-at
# Result of Example 3
# Example 4: Leaf queue limit-at
# Result of Example 4
* Clarification:Only by satisfying alllimit-ats HTB was forced to allocate 20Mbps - 6Mbps toQueue03, 2Mbps toQueue04, and 12Mbps toQueue05, but our output interface is able to handle 10Mbps. As the output interface queue is usually FIFO throughput allocation will keep the ratio 6:2:12 or 3:1:6