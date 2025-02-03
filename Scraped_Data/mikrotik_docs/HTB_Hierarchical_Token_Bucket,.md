---
title: HTB (Hierarchical Token Bucket)
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/137986076/HTB+Hierarchical+Token+Bucket,
crawled_date: 2025-02-02T21:10:42.900683
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Token Bucket algorithm (Red part of the diagram)2.1Packet queue (Blue part of the diagram)2.2Token rate selection (Black part of the diagram)2.3The Diagram2.4Bucket Size in action2.4.1Default Queue Bucket2.4.2Large Queue Bucket2.4.3Large Child Queue Bucket, Small Parent Queue Bucket
* 3Configuration3.1Dual Limitation3.1.1Priority3.2Examples3.2.1Structure3.2.2Example 1: Usual case3.2.3Result of Example 13.2.4Example 2: Usual case with max-limit3.2.5Result of Example 23.2.6Example 3: Inner queue limit-at3.2.7Result of Example 33.2.8Example 4: Leaf queue limit-at3.2.9Result of Example 4
* 2.1Packet queue (Blue part of the diagram)
* 2.2Token rate selection (Black part of the diagram)
* 2.3The Diagram
* 2.4Bucket Size in action2.4.1Default Queue Bucket2.4.2Large Queue Bucket2.4.3Large Child Queue Bucket, Small Parent Queue Bucket
* 2.4.1Default Queue Bucket
* 2.4.2Large Queue Bucket
* 2.4.3Large Child Queue Bucket, Small Parent Queue Bucket
* 3.1Dual Limitation3.1.1Priority
* 3.2Examples3.2.1Structure3.2.2Example 1: Usual case3.2.3Result of Example 13.2.4Example 2: Usual case with max-limit3.2.5Result of Example 23.2.6Example 3: Inner queue limit-at3.2.7Result of Example 33.2.8Example 4: Leaf queue limit-at3.2.9Result of Example 4
* 3.1.1Priority
* 3.2.1Structure
* 3.2.2Example 1: Usual case
* 3.2.3Result of Example 1
* 3.2.4Example 2: Usual case with max-limit
* 3.2.5Result of Example 2
* 3.2.6Example 3: Inner queue limit-at
* 3.2.7Result of Example 3
* 3.2.8Example 4: Leaf queue limit-at
* 3.2.9Result of Example 4
# Introduction
HTB (Hierarchical Token Bucket) is a classful queuing method that is useful for handling different kinds of traffic.  This article will concentrate on the "Token Bucket" part ofHierarchical Token Bucket(HTB) - an algorithm inside the single queue and configuration examples.
# Token Bucket algorithm (Red part of the diagram)
The Token Bucket algorithm is based on an analogy to a bucket where tokens, represented in bytes, are added at a specific rate. The bucket itself has a specified capacity.
If the bucket fills to capacity, newly arriving tokens are dropped
Bucket capacity = bucket-size * max-limit
* bucket size(0..10, Default:0.1) - queue option was added in RouterOS v6.35, before that it was hard-coded to a value of "0.1".
Before allowing any packet to pass through the queue, the queue bucket is inspected to see if it already contains sufficient tokens at that moment.
If yes, the appropriate number of tokens are removed ("cashed in") and the packet is permitted to pass through the queue.
If not, the packets stay at the start of the packet waiting queue until the appropriate amount of tokens is available.
In the case of a multi-level queue structure, tokens used in a child queue are also 'charged' to their parent queues. In other words - child queues 'borrow' tokens from their parent queues.
## Packet queue (Blue part of the diagram)
The size of this packet queue, the sequence, how packets are added to this queue, and when packets are discarded is determined by:
* queue-type-Queue
* queue-size-Queue Size
## Token rate selection (Black part of the diagram)
The maximal token rate at any given time is equal to the highest activity of these values:
* limit-at(NUMBER/NUMBER): guaranteed upload/download data rate to a target
* max-limit(NUMBER/NUMBER): maximal upload/download data rate that is allowed for a target
* burst-limit(NUMBER/NUMBER): maximal upload/download data rate that is allowed for a target while the 'burst' is active
burst-limitis active only when 'burst' is in the allowed state - more info here:Queue Burst
In a case wherelimit-atis the highest value, extra tokens need to be issued to compensate for all missing tokens that were not borrowed from its parent queue.
## The Diagram
## Bucket Size in action
Let's have a simple setup where all traffic from and to one IP address is marked with a packet-mark:
```
/ip firewall mangle
add chain=forward action=mark-connection connection-mark=no-mark src-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-connection connection-mark=no-mark dst-address=192.168.88.101 new-connection-mark=pc1_conn
add chain=forward action=mark-packet connection-mark=pc1_conn new-packet-mark=pc1_traffic
```
### Default Queue Bucket
```
/queue tree
add name=download parent=Local packet-mark=PC1-traffic max-limit=10M
add name=upload parent=Public packet-mark=PC1-traffic max-limit=10M
```
In this case bucket-size=0.1, so bucket-capacity= 0.1 x 10M = 1M
If the bucket is full (that is, the client was not using the full capacity of the queue for some time), the next 1Mb of traffic can pass through the queue at an unrestricted speed.
### Large Queue Bucket
```
/queue tree
add name=download parent=Local packet-mark=PC1-traffic max-limit=10M bucket-size=10
add name=upload parent=Public packet-mark=PC1-traffic max-limit=10M bucket-size=10
```
Let's try to apply the same logic to a situation when bucket size is at its maximal value:
In this case bucket-size=10, so bucket-capacity= 10 x 10M = 100M
If the bucket is full (that is, the client was not using the full capacity of the queue for some time), the next 100Mb of traffic can pass through the queue at an unrestricted speed.
So you can have:
* 20Mbps transfer speed for 10s
* 60Mbps transfer burst for 2s
* 1Gbps transfer burst for approximately 100ms
You can therefore see that the bucket permits a type of 'burstiness' of the traffic that passes through the queue. The behavior is similar to the normal burst feature but lacks the upper limit of the burst. This setback can be avoided if we utilize bucket size in the queue structure:
### Large Child Queue Bucket, Small Parent Queue Bucket
```
/queue tree
add name=download_parent parent=Local max-limit=20M
add name=download parent=download_parent packet-mark=PC1-traffic max-limit=10M bucket-size=10
add name=upload_parent parent=Public max-limit=20M
add name=upload parent=upload_parent packet-mark=PC1-traffic max-limit=10M bucket-size=10
```
In this case:
* parent queue bucket-size=0.1, bucket-capacity= 0.1 x 20M = 2M
* child queue bucket-size=10, bucket-capacity= 10 x 10M = 100M
The parent will run out of tokens much faster than the child queue and as its child queue always borrows tokens from the parent queue the whole system is restricted to token-rate of the parent queue - in this case to max-limit=20M. This rate will be sustained until the child queue runs out of tokens and will be restricted to its token rate of 10Mbps.
In this way, we can have a burst at 20Mbps for up to 10 seconds.
# Configuration
We have to follow three basic steps to create HTB:
* Match and mark traffic– classify traffic for further use. Consists of one or more matching parameters to select packets for the specific class;
* Create rules (policy) to mark traffic– put specific traffic classes into specific queues and define the actions that are taken for each class;
* Attach a policy for specific interface(-s)– append policy for all interfaces (global-in, global-out, or global-total), for a specific interface, or for a specific parent queue;
HTB allows to create of a hierarchical queue structure and determines relations between queues, like "parent-child" or "child-child".
As soon as the queue has at least one child it becomes aninnerqueue, all queues without children -areleafqueues.Leafqueues make actual traffic consumption,Innerqueues are responsible only for traffic distribution. Allleafqueues are treated on an equal basis.
In RouterOS, it is necessary to specifytheparentoption to assign a queue as a child to another queue.
## Dual Limitation
Each queue in HTB has two rate limits:
* CIR(Committed Information Rate) – (limit-atin RouterOS) worst case scenario, the flow will get this amount of traffic no matter what (assuming we can actually send so much data);
* MIR(Maximal Information Rate) – (max-limitin RouterOS) best case scenario, a rate that flow can get up to if their queue's parent has spare bandwidth;
In other words, at firstlimit-at(CIR) of all queues will be satisfied, only then child queues will try to borrow the necessary data rate from their parents in order to reach theirmax-limit(MIR).
That is why, to ensure optimal (as designed) usage of the dual limitation feature, we suggest sticking to these rules:
* The Sum of committed rates of all children must be less or equal to the amount of traffic that is available to parents;
CIR(parent)* ≥ CIR(child1) +...+ CIR(childN)*in case if parent is main parent CIR(parent)=MIR(parent)
* The maximal rate of any child must be less or equal to the maximal rate of the parent
MIR (parent) ≥ MIR(child1) & MIR (parent) ≥ MIR(child2) & ... & MIR (parent) ≥ MIR(childN)
Queue colors in Winbox:
* 0% - 50% available traffic used - green
* 51% - 75% available traffic used - yellow
* 76% - 100% available traffic used - red
### Priority
We already know thatlimit-at(CIR) to all queues will be given out no matter what.
Priority is responsible for the distribution of remaining parent queues traffic to child queues so that they are able to reachmax-limit
The queue with higher priority will reach itsmax-limitbefore the queue with lower priority. 8 is the lowest priority, and 1 is the highest.
Make a note that priority only works:
* forleafqueues - priority intheinnerqueue has no meaning.
* ifmax-limitis specified (not 0)
## Examples
In this section, we will analyze HTB in action. To do that we will take one HTB structure and will try to cover all the possible situations and features, by changing the amount of incoming traffic that HTB has to recycle. and changing some options.
### Structure
Our HTB structure will consist of 5 queues:
* Queue01inner queue with two children -Queue02andQueue03
* Queue02inner queue with two children -Queue04andQueue05
* Queue03leaf queue
* Queue04leaf queue
* Queue05leaf queue
Queue03,Queue04,andQueue05are clients who require 10Mbps all the time Outgoing interface is able to handle 10Mbps of traffic.
### Example 1: Usual case
* Queue01limit-at=0Mbps max-limit=10Mbps
* Queue02limit-at=4Mbps max-limit=10Mbps
* Queue03limit-at=6Mbps max-limit=10Mbps priority=1
* Queue04limit-at=2Mbps max-limit=10Mbps priority=3
* Queue05limit-at=2Mbps max-limit=10Mbps priority=5
### Result of Example 1
* Queue03will receive 6Mbps
* Queue04will receive 2Mbps
* Queue05will receive 2Mbps
* Clarification:HTB was built in a way, that, by satisfying alllimit-ats, the main queue no longer has throughput to distribute.
### Example 2: Usual case with max-limit
* Queue01limit-at=0Mbps max-limit=10Mbps
* Queue02limit-at=4Mbps max-limit=10Mbps
* Queue03limit-at=2Mbps max-limit=10Mbps priority=3
* Queue04limit-at=2Mbps max-limit=10Mbps priority=1
* Queue05limit-at=2Mbps max-limit=10Mbps priority=5
### Result of Example 2
* Queue03will receive 2Mbps
* Queue04will receive 6Mbps
* Queue05will receive 2Mbps
* Clarification:After satisfying alllimit-ats HTB will give throughput to the queue with the highest priority.
### Example 3: Inner queue limit-at
* Queue01limit-at=0Mbps max-limit=10Mbps
* Queue02limit-at=8Mbps max-limit=10Mbps
* Queue03limit-at=2Mbps max-limit=10Mbps priority=1
* Queue04limit-at=2Mbps max-limit=10Mbps priority=3
* Queue05limit-at=2Mbps max-limit=10Mbps priority=5
### Result of Example 3
* Queue03will receive 2Mbps
* Queue04will receive 6Mbps
* Queue05will receive 2Mbps
* Clarification:After satisfying alllimit-ats HTB will give throughput to the queue with the highest priority. But in this case,innerqueueQueue02hadlimit-atspecified, by doing so, it reserved 8Mbps of throughput for queuesQueue04andQueue05. Of these twoQueue04has the highest priority, which is why it gets additional throughput.
### Example 4: Leaf queue limit-at
* Queue01limit-at=0Mbps max-limit=10Mbps
* Queue02limit-at=4Mbps max-limit=10Mbps
* Queue03limit-at=6Mbps max-limit=10Mbps priority=1
* Queue04limit-at=2Mbps max-limit=10Mbps priority=3
* Queue05limit-at=12Mbps max-limit=15Mbps priority=5
### Result of Example 4
* Queue03will receive ~3Mbps
* Queue04will receive ~1Mbps
* Queue05will receive ~6Mbps
* Clarification:Only by satisfying alllimit-ats HTB was forced to allocate 20Mbps - 6Mbps toQueue03, 2Mbps toQueue04, and 12Mbps toQueue05, but our output interface is able to handle 10Mbps. As the output interface queue is usually FIFO throughput allocation will keep the ratio 6:2:12 or 3:1:6